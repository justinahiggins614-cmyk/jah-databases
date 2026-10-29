/* LJAudio2-leaks-port — read-aloud player for the Library of Jerusalem.
   DEPLOY NAME: db/assets/lj-audio-player.js (same filename, same lj-*
   button IDs, same [data-audio-text] collection as v1/v2), so NO book-page
   markup edits are needed. Replaces lj-audio-player-v2.js at deploy time.

   WHAT THIS PORT IS: v2's queue/watchdog architecture with the PROVEN
   JAH-N Wiki Leaks read-aloud fallback in place of v2's Worker-only
   endpoint. Wiki Leaks (jah-n-wiki-leaks/index.html, SigTTS guard
   injected 2026-10-11; shared helper ~/workspace/hidden_files/
   sigtts-helper.js) already solves the exact case Jerusalem fails on:
   speechSynthesis EXISTS but is dead in Android/Facebook WebView.
   Its tiers need NO provider key and NO backend of ours:

     Tier order (SigTTS TTS_URLS, verbatim):
       1. https://code.responsivevoice.org/getvoice.php (tl=en-US, sv=g2)
       2. https://translate.google.com/translate_tts (client=tw-ob)
       3. https://translate.googleapis.com/translate_tts (client=tw-ob)
     Plus, ONLY if configured: the Cloudflare Worker endpoint
     (window.LJ_TTS_ENDPOINT) is tried FIRST as an additional tier.
     Endpoint empty = public tiers only. The Worker is an optional
     upgrade, never a precondition — this player works fully with no
     endpoint, no key, no provider decision.

   PORTED FROM SIGTTS (see LEAKS-PORT-REPORT.md for file/line refs):
     - voiceAlive probe: 3s wait for voices; empty voices forever = dead
     - onstart watchdog 6s + per-chunk absolute budget
       min(120000, 30000 + ceil(len/15)*1000) ms
     - chunk-by-chunk online audio over <audio>, 14s fail-fast per chunk,
       tier escalation per chunk, onDone exactly once
     - honest failure wording (never a fake Finished, never a silent stall)

   KEPT FROM V2 (unchanged semantics):
     - chunkText sentence-boundary chunking (exact-join guarantee)
     - makeQueue state machine, pause/resume/stop/replay, rapid-press guard
     - isolated speech-utterance errors skip one chunk and keep going;
       3 consecutive errors stop honestly (dead-engine detection stays
       with the probe + watchdogs, not single errors — see report)
     - resume at the exact char offset where speech died (consumedChars)
     - empty-text honesty: "Nothing to read on this page."

   CHANGES VS V2 (deliberate, documented in the report):
     - Audio chunks capped at 200 chars (not 900): Google translate_tts
       rejects long queries, so tiered chunks stay <= 200 chars.
     - Probe verdict is now binding: voices never arriving within the
       wait means dead -> tiers immediately (v2 spoke anyway).
     - finishedLabel option built in (window.LJ_FINISHED_LABEL): suite
       pages finish with "Finished — full page read aloud." without a
       separate player patch. Default book wording unchanged.
     - Status path wording: "(online voice)" instead of "(audio service)".
     - No "not connected yet" dead end exists anymore: with no endpoint
       the player falls back to the public tiers, and only reports failure
       when every tier has actually failed.

   HONEST LIMITS: the public tiers are third-party services; they can
   change, rate-limit, or block. No key is involved anywhere. Playback
   still needs the user's on-phone confirmation after deploy — nothing
   here claims it works until he presses Play and hears it. */
(function (global) {
  'use strict';

  var MAX_CHUNK = 200;        // Web Speech chunk size (short = reliable)
  var MAX_AUDIO_CHUNK = 200;  // tiered-audio chunk size (Google TTS cap)
  var AUDIO_CHUNK_TIMEOUT_MS = 14000; // SigTTS fail-fast per audio chunk

  // Tiered public voice URLs — SigTTS TTS_URLS, verbatim.
  function responsiveVoiceUrl(t) {
    return 'https://code.responsivevoice.org/getvoice.php?t=' + encodeURIComponent(t) +
      '&tl=en-US&sv=g2&vn=&pitch=0.5&rate=0.95';
  }
  function googleTranslateUrl(t) {
    return 'https://translate.google.com/translate_tts?ie=UTF-8&q=' + encodeURIComponent(t) +
      '&tl=en&client=tw-ob';
  }
  function googleApisUrl(t) {
    return 'https://translate.googleapis.com/translate_tts?ie=UTF-8&q=' + encodeURIComponent(t) +
      '&tl=en&client=tw-ob';
  }

  // Split full text into sentence-boundary chunks, each <= max chars.
  // Guarantees: joining the chunks reproduces the input text exactly.
  function chunkText(text, max) {
    max = max || MAX_CHUNK;
    if (!text) return [];
    var sentences = text.match(/[^.!?]+[.!?]+["']?\s*|[^.!?]+$/g) || [text];
    var chunks = [];
    var cur = '';
    for (var i = 0; i < sentences.length; i++) {
      var s = sentences[i];
      if ((cur + s).length > max && cur.length > 0) {
        chunks.push(cur);
        cur = '';
      }
      while (s.length > max) {
        var cut = s.lastIndexOf(' ', max);
        if (cut <= 0) cut = max;
        chunks.push(cur + s.slice(0, cut));
        cur = '';
        s = s.slice(cut);
      }
      cur += s;
    }
    if (cur.length > 0) chunks.push(cur);
    return chunks;
  }

  // Pure queue state machine (testable without speech synthesis).
  function makeQueue(chunks) {
    return {
      chunks: chunks.slice(),
      index: 0,
      state: 'idle', // idle | playing | paused | finished | error | empty
      played: 0,
      consecutiveErrors: 0,
      advance: function () {
        if (this.index < this.chunks.length) { this.index += 1; this.played += 1; }
        if (this.index >= this.chunks.length) this.state = 'finished';
      },
      noteError: function () {
        this.consecutiveErrors += 1;
        if (this.consecutiveErrors >= 3) this.state = 'error';
      },
      reset: function () {
        this.index = 0; this.played = 0; this.consecutiveErrors = 0; this.state = 'idle';
      }
    };
  }

  function collectBookText(doc) {
    var parts = [];
    var nodes = doc.querySelectorAll('[data-audio-text]');
    for (var i = 0; i < nodes.length; i++) {
      var t = nodes[i].textContent.replace(/\s+/g, ' ').trim();
      if (t) parts.push(t);
    }
    return parts.join(' ');
  }

  function resolveEndpoint(opts) {
    if (opts && opts.endpoint) return opts.endpoint;
    if (typeof global !== 'undefined' && global.LJ_TTS_ENDPOINT) return global.LJ_TTS_ENDPOINT;
    return '';
  }

  function resolveFinishedLabel(opts) {
    if (opts && opts.finishedLabel) return opts.finishedLabel;
    if (typeof global !== 'undefined' && global.LJ_FINISHED_LABEL) return global.LJ_FINISHED_LABEL;
    return 'Finished — full book read aloud.';
  }

  function createPlayer(doc, synth, opts) {
    opts = opts || {};
    var endpoint = resolveEndpoint(opts);
    // Deploy-time placeholder: replaced with the real Worker URL at deploy.
    // If it survives unreplaced, it is simply "not configured" — the
    // public tiers below still work, so it is never a dead end.
    if (endpoint === '__LJ_TTS_ENDPOINT__') endpoint = '';
    var finishedLabel = resolveFinishedLabel(opts);
    var startWatchdogMs = opts.startWatchdogMs != null ? opts.startWatchdogMs : 6000;
    var voicesTimeoutMs = opts.voicesTimeoutMs != null ? opts.voicesTimeoutMs : 3000;
    var chunkAudioTimeoutMs = opts.chunkAudioTimeoutMs != null ? opts.chunkAudioTimeoutMs : AUDIO_CHUNK_TIMEOUT_MS;
    var setT = opts.setTimeoutFn || setTimeout;
    var clearT = opts.clearTimeoutFn || clearTimeout;
    var audioFactory = opts.audioFactory || null;

    // Tier list: Worker first ONLY if configured, then the SigTTS tiers.
    var audioTiers = [];
    if (endpoint) {
      audioTiers.push(function (t) { return endpoint + '?text=' + encodeURIComponent(t); });
    }
    audioTiers.push(responsiveVoiceUrl, googleTranslateUrl, googleApisUrl);

    var queue = null;
    var statusEl = null;
    var progressEl = null;
    var utter = null;
    var audioEl = null;
    var audioTimer = null;
    var audioTier = 0;       // current tier for the chunk being played
    var audioSettled = false; // per-attempt guard: one outcome only
    var mode = 'speech'; // speech | audio
    var fullText = '';
    var consumedChars = 0;
    var succeededChunks = 0;
    var startTimer = null;
    var endTimer = null;

    function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }
    function setProgress() {
      if (progressEl && queue) {
        var shown = queue.state === 'finished' ? queue.chunks.length : queue.index + 1;
        progressEl.textContent = 'Chunk ' + shown + ' of ' + queue.chunks.length +
          (queue.state === 'finished' ? ' — ' + finishedLabel : '') +
          (mode === 'audio' ? ' (online voice)' : '');
      }
    }
    function clearTimers() {
      if (startTimer !== null) { clearT(startTimer); startTimer = null; }
      if (endTimer !== null) { clearT(endTimer); endTimer = null; }
      if (audioTimer !== null) { clearT(audioTimer); audioTimer = null; }
    }
    // SigTTS absolute budget per utterance: min(120s, 30s + len/15 seconds).
    function speechBudgetMs(text) {
      return Math.min(120000, 30000 + Math.ceil(String(text).length / 15) * 1000);
    }

    function failToAudio(reason) {
      // Speech engine is dead or stalled. Never sit silent: switch modes.
      // If we are ALREADY on audio, there is nowhere left to fall back to.
      if (mode === 'audio') {
        if (queue) queue.state = 'error';
        setStatus('The voice services could not be reached — check your connection, or open this page in a full browser for built-in voices.');
        setProgress();
        return;
      }
      clearTimers();
      if (synth) { try { synth.cancel(); } catch (e) { /* ignore */ } }
      utter = null;
      mode = 'audio';
      audioTier = 0;
      var remaining = fullText.slice(consumedChars);
      queue = makeQueue(chunkText(remaining, MAX_AUDIO_CHUNK));
      queue.state = 'playing';
      setStatus(reason + ' Reading aloud (online voice)…');
      playAudioNext();
    }

    function speakNext() {
      if (!queue) return;
      if (queue.index >= queue.chunks.length) {
        if (queue.state !== 'finished') queue.state = 'finished';
        setStatus(finishedLabel);
        setProgress();
        return;
      }
      if (queue.state !== 'playing' || mode !== 'speech') return;
      var text = queue.chunks[queue.index];
      var myUtter;
      try {
        myUtter = new global.SpeechSynthesisUtterance(text);
      } catch (e) {
        failToAudio('Speech engine error.');
        return;
      }
      utter = myUtter;
      var started = false;
      utter.onstart = function () { if (utter !== myUtter) return; started = true; if (startTimer !== null) { clearT(startTimer); startTimer = null; } };
      utter.onend = function () {
        if (utter !== myUtter) return;
        if (queue.state !== 'playing') return;
        clearTimers();
        queue.consecutiveErrors = 0;
        succeededChunks += 1;
        consumedChars += text.length;
        queue.advance();
        setProgress();
        speakNext();
      };
      utter.onerror = function () {
        if (utter !== myUtter) return;
        if (queue.state !== 'playing') return;
        clearTimers();
        queue.noteError();
        if (queue.state === 'error') {
          setStatus('Playback stopped after repeated errors. Press Replay to try again.');
          setProgress();
          return;
        }
        consumedChars += text.length;
        queue.advance(); // skip the failed chunk, keep going — never stall the book
        if (queue.state === 'finished' && succeededChunks === 0) {
          // Every chunk failed: never report a fake "Finished".
          queue.state = 'error';
          setStatus('Playback failed — no audio could be played. Press Replay to try again.');
          setProgress();
          return;
        }
        setProgress();
        speakNext();
      };
      try {
        synth.speak(utter);
      } catch (e) {
        failToAudio('Speech engine error.');
        return;
      }
      // SigTTS watchdogs: 6s onstart + per-chunk absolute budget.
      // If the engine never starts or never ends this chunk, abandon
      // speech and fall back to the tiers instead of stalling forever.
      startTimer = setT(function () {
        if (queue && queue.state === 'playing' && mode === 'speech' && utter === myUtter && !started) {
          failToAudio('Speech engine did not start.');
        }
      }, startWatchdogMs);
      endTimer = setT(function () {
        if (queue && queue.state === 'playing' && mode === 'speech' && utter === myUtter) {
          failToAudio('Speech playback stalled.');
        }
      }, speechBudgetMs(text));
      setStatus('Reading aloud…');
      setProgress();
    }

    function playAudioNext() {
      if (!queue) return;
      if (queue.index >= queue.chunks.length) {
        if (queue.state !== 'finished') queue.state = 'finished';
        setStatus(finishedLabel);
        setProgress();
        return;
      }
      if (queue.state !== 'playing' || mode !== 'audio') return;
      var text = queue.chunks[queue.index];
      if (!audioFactory) {
        queue.state = 'error';
        setStatus('The voice services could not be reached — check your connection, or open this page in a full browser for built-in voices.');
        setProgress();
        return;
      }
      audioSettled = false;
      audioEl = audioFactory();
      var myAudio = audioEl;
      var myTier = audioTier;
      function audioOutcome(ok) {
        if (audioSettled) return;
        audioSettled = true;
        if (audioTimer !== null) { clearT(audioTimer); audioTimer = null; }
        if (queue.state !== 'playing' || mode !== 'audio' || audioEl !== myAudio) return;
        if (ok) {
          queue.consecutiveErrors = 0;
          succeededChunks += 1;
          audioTier = 0; // next chunk starts again at the first tier
          queue.advance();
          setProgress();
          playAudioNext();
        } else if (myTier + 1 < audioTiers.length) {
          // Same chunk, next tier — SigTTS tier escalation.
          audioTier = myTier + 1;
          playAudioNext();
        } else {
          // Every tier failed for this chunk: skip it, keep going.
          audioTier = 0;
          queue.noteError();
          if (queue.state === 'error') {
            setStatus('The voice services stopped after repeated errors. Press Replay to try again.');
            setProgress();
            return;
          }
          queue.advance();
          if (queue.state === 'finished' && succeededChunks === 0) {
            // Every chunk failed: never report a fake "Finished".
            queue.state = 'error';
            setStatus('The voice services could not be reached — check your connection, or open this page in a full browser for built-in voices.');
            setProgress();
            return;
          }
          setProgress();
          playAudioNext();
        }
      }
      myAudio.onended = function () { audioOutcome(true); };
      myAudio.onerror = function () { audioOutcome(false); };
      // SigTTS 14s fail-fast per chunk: a hung tier must not stall the book.
      audioTimer = setT(function () { audioOutcome(false); }, chunkAudioTimeoutMs);
      var src = '';
      try { src = audioTiers[myTier](text); } catch (e) { audioOutcome(false); return; }
      myAudio.src = src;
      try {
        var p = myAudio.play();
        if (p && typeof p.catch === 'function') {
          p.catch(function () { audioOutcome(false); });
        }
      } catch (e) {
        audioOutcome(false);
        return;
      }
      setStatus('Reading aloud (online voice)…');
      setProgress();
    }

    // SigTTS voiceAlive probe: voices present = live; voices never arriving
    // within the wait = dead. The verdict is BINDING: a dead verdict goes
    // straight to the tiers instead of speaking into a dead engine.
    function probeVoices(cb) {
      if (!synth || typeof synth.getVoices !== 'function') { cb(false); return; }
      try {
        if (synth.getVoices().length > 0) { cb(true); return; }
      } catch (e) { cb(false); return; }
      var done = false;
      var finish = function () {
        if (done) return;
        done = true;
        var alive = false;
        try { alive = synth.getVoices().length > 0; } catch (e) { alive = false; }
        cb(alive);
      };
      if (typeof synth.addEventListener === 'function') {
        try { synth.addEventListener('voiceschanged', finish); } catch (e) { /* ignore */ }
      }
      setT(finish, voicesTimeoutMs);
    }

    return {
      bind: function (statusId, progressId) {
        statusEl = doc.getElementById(statusId);
        progressEl = doc.getElementById(progressId);
      },
      play: function () {
        if (queue && queue.state === 'playing') return; // rapid-press guard
        if (queue && queue.state === 'paused') {
          queue.state = 'playing';
          if (mode === 'speech') {
            if (synth) synth.resume();
            // Resume watchdog: some engines accept resume() and then never
            // finish the utterance. If nothing advances within a full
            // chunk budget, fall back instead of stalling.
            var resumeIndex = queue.index;
            endTimer = setT(function () {
              if (queue && queue.state === 'playing' && mode === 'speech' && queue.index === resumeIndex) {
                failToAudio('Speech playback stalled.');
              }
            }, 45000);
          }
          else if (audioEl) {
            // Restart the current chunk attempt from its tier: the paused
            // element is orphaned (stays paused, silent) and playAudioNext
            // builds a fresh element + fresh 14s timer for the same chunk.
            var pausedEl = audioEl;
            try { pausedEl.pause(); } catch (e) { /* ignore */ }
            audioEl = null;
            playAudioNext();
          }
          setStatus(mode === 'audio' ? 'Reading aloud (online voice)…' : 'Reading aloud…');
          return;
        }
        fullText = collectBookText(doc);
        if (!fullText) {
          // Never fake-finish an empty page.
          queue = makeQueue([]);
          queue.state = 'empty';
          setStatus('Nothing to read on this page.');
          if (progressEl) progressEl.textContent = 'No readable text on this page.';
          return;
        }
        mode = 'speech';
        consumedChars = 0;
        succeededChunks = 0;
        audioTier = 0;
        queue = makeQueue(chunkText(fullText, MAX_CHUNK));
        queue.state = 'playing';
        if (!synth) { failToAudio('Speech is unavailable in this browser.'); return; }
        var self = this;
        probeVoices(function (alive) {
          if (!queue || queue.state !== 'playing') return;
          if (alive) speakNext();
          else failToAudio('No working voice found in this browser.');
        });
      },
      pause: function () {
        if (queue && queue.state === 'playing') {
          queue.state = 'paused';
          clearTimers();
          if (mode === 'speech') { if (synth) synth.pause(); }
          else if (audioEl) { try { audioEl.pause(); } catch (e) { /* ignore */ } }
          setStatus('Paused.');
        }
      },
      resume: function () { this.play(); },
      stop: function () {
        clearTimers();
        if (synth) { try { synth.cancel(); } catch (e) { /* ignore */ } }
        if (audioEl) { try { audioEl.pause(); } catch (e) { /* ignore */ } }
        audioEl = null;
        utter = null;
        mode = 'speech';
        if (queue) queue.reset();
        setStatus('Stopped.');
        setProgress();
      },
      replay: function () {
        clearTimers();
        if (synth) { try { synth.cancel(); } catch (e) { /* ignore */ } }
        if (audioEl) { try { audioEl.pause(); } catch (e) { /* ignore */ } }
        audioEl = null;
        queue = null;
        this.play();
      },
      _queue: function () { return queue; },
      _debug: function () {
        return { mode: mode, state: queue ? queue.state : null, index: queue ? queue.index : null, played: queue ? queue.played : null, endpointConfigured: !!endpoint, tierCount: audioTiers.length };
      }
    };
  }

  var api = { chunkText: chunkText, makeQueue: makeQueue, collectBookText: collectBookText, createPlayer: createPlayer, MAX_CHUNK: MAX_CHUNK, MAX_AUDIO_CHUNK: MAX_AUDIO_CHUNK, responsiveVoiceUrl: responsiveVoiceUrl, googleTranslateUrl: googleTranslateUrl, googleApisUrl: googleApisUrl };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.LJAudio2 = api;
  // Back-compat alias: pages already load this file as the read-aloud player.
  global.LJAudio = api;

  if (typeof document !== 'undefined' && typeof window !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function () {
      var player = createPlayer(document, window.speechSynthesis, {
        audioFactory: function () { return new Audio(); },
        endpoint: window.LJ_TTS_ENDPOINT || '__LJ_TTS_ENDPOINT__'
      });
      player.bind('lj-status', 'lj-progress');
      var bind = function (id, fn) {
        var el = document.getElementById(id);
        if (el) el.addEventListener('click', fn);
      };
      bind('lj-play', function () { player.play(); });
      bind('lj-pause', function () { player.pause(); });
      bind('lj-resume', function () { player.resume(); });
      bind('lj-stop', function () { player.stop(); });
      bind('lj-replay', function () { player.replay(); });
      // Buttons stay live even without speech support: pressing Play tries
      // the online voice tiers, which need no browser speech engine.
      if (!window.speechSynthesis) {
        var noSpeechEl = document.getElementById('lj-status');
        if (noSpeechEl) noSpeechEl.textContent = 'This browser has no built-in speech engine. Press Play to try the online voice.';
      }
    });
  }
})(typeof window !== 'undefined' ? window : globalThis);
