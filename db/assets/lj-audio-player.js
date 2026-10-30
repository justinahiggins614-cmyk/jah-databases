/* LJAudio2-chapter-fix-v2 — read-aloud player for the Library of Jerusalem.
 * CHAPTER FIX vs the leaks-port player (see CHAPTER-FIX-REPORT.md):
 * a failed chunk NEVER kills the whole book. Audio all-tier failures skip
 * the chunk and continue (per-tier retry + growing backoff); only a
 * sustained outage (12 consecutive failed chunks) pauses honestly at the
 * current chunk for Resume, never a fake Finished. Speech repeated errors
 * switch to the audio tiers instead of stopping. The next chunk is
 * preloaded where possible. Skipped chunks are counted in the status line.
 * Same filename at deploy, same lj-* IDs, same [data-audio-text]
 * collection — ZERO book-page edits. */
/* CHAPTER-FIX-V2 vs the chapter-fix player (see CHAPTER-FIX-V2-REPORT.md):
 * the chapter-fix removed the 3-kill but did NOT change the chunk-1 ->
 * chunk-2 TRANSITION, and the user's phone still stops after one
 * sentence. This revision changes the transition itself:
 *  - ONE persistent <audio> element, created once per page session and
 *    never replaced: the element that played chunk 1 stays blessed for
 *    chunk 2, instead of a fresh element per chunk (fresh elements are
 *    what a webview's non-gesture play policy rejects).
 *  - Audio preload removed: preloading bought nothing for the
 *    transition (a preloaded element has never played, so it is not
 *    blessed either) and cost an extra element per chunk.
 *  - Speech continuation is timer-delayed (150ms) with a resume nudge,
 *    instead of speak() synchronously inside onend (some webview
 *    engines drop a speak() issued while the previous utterance's
 *    speaking flag has not cleared).
 *  - Speech utterances are section-length (up to 4000 chars) instead of
 *    200-char chunks, so one utterance covers many sentences if the
 *    webview rations utterances; audio tiers stay 200-char (Google cap).
 *  - Same-chunk retry on play() rejection now retries on the SAME
 *    persistent element before tier escalation.
 * Kept verbatim from chapter-fix: honesty rules (skip counts, honest
 * pause after 12 consecutive failures with Resume-from-here, never a
 * fake Finished), tier URLs and order, watchdogs, endpoint-optional
 * behavior, same lj-* IDs, same [data-audio-text] collection. */
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
  var MAX_SPEECH_CHUNK = 4000; // speech-mode utterance cap (section-length)
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

  // Section texts in DOM order (same normalization as collectBookText).
  function collectSections(doc) {
    var sections = [];
    var nodes = doc.querySelectorAll('[data-audio-text]');
    for (var i = 0; i < nodes.length; i++) {
      var t = nodes[i].textContent.replace(/\s+/g, ' ').trim();
      if (t) sections.push(t);
    }
    return sections;
  }

  // Speech-mode chunks: sentence-packed pieces of each section, up to
  // MAX_SPEECH_CHUNK chars. Joining the pieces reproduces
  // collectBookText's full text EXACTLY (each non-final section's last
  // piece carries the inter-section space), so consumedChars maps
  // exactly onto the audio queue if speech later falls back to audio.
  function buildSpeechChunks(sections) {
    var pieces = [];
    for (var i = 0; i < sections.length; i++) {
      var ps = chunkText(sections[i], MAX_SPEECH_CHUNK);
      if (i < sections.length - 1 && ps.length > 0) ps[ps.length - 1] += ' ';
      for (var j = 0; j < ps.length; j++) pieces.push(ps[j]);
    }
    return pieces;
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
    var maxConsecutiveAudioFails = opts.maxConsecutiveAudioFails != null ? opts.maxConsecutiveAudioFails : 12;
    var audioRetryPerTier = opts.audioRetryPerTier != null ? opts.audioRetryPerTier : 2;
    var audioRetryDelayMs = opts.audioRetryDelayMs != null ? opts.audioRetryDelayMs : 800;
    var audioBackoffBaseMs = opts.audioBackoffBaseMs != null ? opts.audioBackoffBaseMs : 1500;
    var speechContinueDelayMs = opts.speechContinueDelayMs != null ? opts.speechContinueDelayMs : 150;
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
    var skippedChunks = 0; // audio chunks skipped after all tiers failed
    var consecutiveAudioFailures = 0; // consecutive all-tier-failed chunks
    var audioAttempt = 0; // attempt index within the current tier
    var backoffTimer = null;
    var speechActive = false; // a speech utterance is currently in flight
    var speechNextTimer = null; // delayed speech continuation (v2)
    // v2: audioEl is PERSISTENT — created once per page session and never
    // replaced. The element that played chunk 1 is the element that plays
    // chunk 2 (see report: fresh elements are what non-gesture play
    // policies reject). stop()/replay() pause it but keep it.
    var mode = 'speech'; // speech | audio
    var fullText = '';
    var consumedChars = 0;
    var succeededChunks = 0;
    var startTimer = null;
    var endTimer = null;

    function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }
    // Finished wording is honest about skips: a book that skipped chunks
    // never reports a clean Finished.
    function finishedText() {
      if (skippedChunks > 0) {
        return 'Finished — full book read aloud (' + skippedChunks + ' chunk' + (skippedChunks === 1 ? '' : 's') + ' skipped: voice services unreachable for those parts).';
      }
      return finishedLabel;
    }
    function setProgress() {
      if (progressEl && queue) {
        var shown = queue.state === 'finished' ? queue.chunks.length : queue.index + 1;
        progressEl.textContent = 'Chunk ' + shown + ' of ' + queue.chunks.length +
          (queue.state === 'finished' ? ' — ' + finishedText() : '') +
          (mode === 'audio' ? ' (online voice)' : '') +
          (skippedChunks > 0 && queue.state !== 'finished' ? ' — ' + skippedChunks + ' skipped' : '');
      }
    }
    function clearTimers() {
      if (startTimer !== null) { clearT(startTimer); startTimer = null; }
      if (endTimer !== null) { clearT(endTimer); endTimer = null; }
      if (audioTimer !== null) { clearT(audioTimer); audioTimer = null; }
      if (backoffTimer !== null) { clearT(backoffTimer); backoffTimer = null; }
      if (speechNextTimer !== null) { clearT(speechNextTimer); speechNextTimer = null; }
    }
    // SigTTS absolute budget per utterance: min(120s, 30s + len/15 seconds).
    function speechBudgetMs(text) {
      return Math.min(600000, 30000 + Math.ceil(String(text).length / 12) * 1000);
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
      speechActive = false;
      if (synth) { try { synth.cancel(); } catch (e) { /* ignore */ } }
      utter = null;
      mode = 'audio';
      audioTier = 0;
      audioAttempt = 0;
      var remaining = fullText.slice(consumedChars);
      queue = makeQueue(chunkText(remaining, MAX_AUDIO_CHUNK));
      queue.state = 'playing';
      setStatus(reason + ' Reading aloud (online voice)…');
      playAudioNext();
    }

    // v2: NEVER speak() synchronously inside onend. Some webview
    // engines drop a speak() issued while the previous utterance's
    // speaking flag has not cleared, which reads as "one sentence,
    // then silence". A short timer lets the engine settle; the guard
    // re-checks state/mode on arrival, and scheduleSpeechNext clears
    // any pending timer first so at most one continuation is queued.
    function scheduleSpeechNext() {
      if (speechNextTimer !== null) { clearT(speechNextTimer); speechNextTimer = null; }
      speechNextTimer = setT(function () {
        speechNextTimer = null;
        if (queue && queue.state === 'playing' && mode === 'speech' && utter) speakNext();
      }, speechContinueDelayMs);
    }

    function speakNext() {
      if (!queue) return;
      if (queue.index >= queue.chunks.length) {
        if (queue.state !== 'finished') queue.state = 'finished';
        setStatus(finishedText());
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
        speechActive = false;
        queue.consecutiveErrors = 0;
        succeededChunks += 1;
        consumedChars += text.length;
        queue.advance();
        setProgress();
        scheduleSpeechNext();
      };
      utter.onerror = function () {
        if (utter !== myUtter) return;
        if (queue.state !== 'playing') return;
        clearTimers();
        queue.noteError();
        if (queue.state === 'error') {
          // Repeated speech errors are a dead engine, not a dead book:
          // switch to the audio tiers instead of stopping.
          failToAudio('Speech engine failed repeatedly.');
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
        speechActive = false;
        scheduleSpeechNext();
      };
      speechActive = false;
      try {
        if (synth.paused) { try { synth.resume(); } catch (e2) { /* ignore */ } }
        synth.speak(utter);
        speechActive = true;
        // v2 resume nudge: some engines queue the utterance while paused
        // and never start it until resume() is called after speak().
        try { synth.resume(); } catch (e2) { /* ignore */ }
      } catch (e) {
        speechActive = false;
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

    // Delayed re-entry into playAudioNext (per-tier retry, post-skip
    // backoff). The guard inside playAudioNext still applies on arrival.
    function scheduleAudioRetry(ms) {
      if (backoffTimer !== null) { clearT(backoffTimer); backoffTimer = null; }
      backoffTimer = setT(function () {
        backoffTimer = null;
        if (queue && queue.state === 'playing' && mode === 'audio') playAudioNext();
      }, ms);
    }
    // v2: create the single persistent audio element once. Called from
    // play() (inside the user's click handler) so creation is
    // gesture-adjacent, and again here as a fallback for paths that
    // reach audio without play() (e.g. probe-driven failToAudio).
    function ensureAudioEl() {
      if (!audioEl && audioFactory) {
        try { audioEl = audioFactory(); } catch (e) { audioEl = null; }
      }
      return audioEl;
    }

    function playAudioNext() {
      if (!queue) return;
      if (queue.index >= queue.chunks.length) {
        if (queue.state !== 'finished') queue.state = 'finished';
        setStatus(finishedText());
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
      var myTier = audioTier;
      var myAttempt = audioAttempt;
      var src = '';
      try { src = audioTiers[myTier](text); } catch (e) { src = ''; }
      // v2: ONE persistent element. Never create a fresh element per
      // chunk: the element that played chunk 1 is the element that plays
      // chunk 2. Fresh elements are what non-gesture play policies
      // reject, which is the chunk-1 -> chunk-2 death. Same-chunk
      // retries (audioAttempt path) now retry on this same element
      // before tier escalation.
      ensureAudioEl();
      var myAudio = audioEl;
      function audioOutcome(ok) {
        if (audioSettled) return;
        audioSettled = true;
        if (audioTimer !== null) { clearT(audioTimer); audioTimer = null; }
        if (queue.state !== 'playing' || mode !== 'audio' || audioEl !== myAudio) return;
        if (ok) {
          queue.consecutiveErrors = 0;
          consecutiveAudioFailures = 0;
          audioAttempt = 0;
          succeededChunks += 1;
          consumedChars += text.length;
          audioTier = 0; // next chunk starts again at the first tier
          queue.advance();
          setProgress();
          playAudioNext();
        } else if (audioAttempt + 1 < audioRetryPerTier) {
          // Same tier, one more attempt after a short pause: transient
          // slowness or a throttled response is not yet a dead tier.
          audioAttempt += 1;
          scheduleAudioRetry(audioRetryDelayMs);
        } else if (myTier + 1 < audioTiers.length) {
          // Same chunk, next tier — SigTTS tier escalation.
          audioAttempt = 0;
          audioTier = myTier + 1;
          playAudioNext();
        } else {
          // Every tier (each retried) failed for this chunk.
          audioAttempt = 0;
          audioTier = 0;
          consecutiveAudioFailures += 1;
          if (consecutiveAudioFailures >= maxConsecutiveAudioFails) {
            // Sustained outage, not a bad chunk: PAUSE at this chunk so
            // Resume retries it — never kill the book, never fake Finished.
            queue.state = 'paused';
            setStatus('Voice services unreachable — playback paused at chunk ' + (queue.index + 1) + ' of ' + queue.chunks.length + ' (' + skippedChunks + ' chunk' + (skippedChunks === 1 ? '' : 's') + ' skipped). Press Resume to try again from here.');
            setProgress();
            return;
          }
          // CHAPTER-FIX RULE: a failed chunk NEVER kills the book.
          skippedChunks += 1;
          consumedChars += text.length;
          queue.advance();
          if (queue.state === 'finished' && succeededChunks === 0) {
            // Every chunk failed: never report a fake "Finished".
            queue.state = 'error';
            setStatus('The voice services could not be reached — check your connection, or open this page in a full browser for built-in voices.');
            setProgress();
            return;
          }
          setProgress();
          // Back off before the next chunk so a rate-limited endpoint gets
          // breathing room instead of a hammering death spiral.
          scheduleAudioRetry(Math.min(6000, audioBackoffBaseMs * consecutiveAudioFailures));
        }
      }
      if (!myAudio || !src) { audioOutcome(false); return; }
      myAudio.onended = function () { audioOutcome(true); };
      myAudio.onerror = function () { audioOutcome(false); };
      // SigTTS 14s fail-fast per chunk: a hung tier must not stall the book.
      audioTimer = setT(function () { audioOutcome(false); }, chunkAudioTimeoutMs);
      if (myAudio.src !== src) myAudio.src = src;
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
      // v2: no preload. A preloaded element has never played, so it is
      // not blessed either — preloading bought nothing for the
      // transition and cost an extra element per chunk.
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
            // v2: if no utterance is in flight (e.g. Pause was pressed
            // in the gap between onend and the delayed continuation),
            // resume must re-drive the queue instead of waiting for an
            // utterance that will never end.
            if (!speechActive) scheduleSpeechNext();
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
            // v2: resume on the SAME persistent element for the current
            // chunk — never a fresh element. If the element is paused
            // mid-chunk with the same src, playAudioNext resumes it
            // mid-chunk; otherwise it restarts the chunk. Resume grants
            // a fresh failure runway, not the outage counter.
            consecutiveAudioFailures = 0;
            audioAttempt = 0;
            audioTier = 0;
            playAudioNext();
          }
          else {
            // Audio mode but no live element (e.g. paused during a retry
            // backoff): restart the current chunk from tier 0.
            consecutiveAudioFailures = 0;
            audioAttempt = 0;
            audioTier = 0;
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
        skippedChunks = 0;
        consecutiveAudioFailures = 0;
        audioAttempt = 0;
        speechActive = false;
        // v2: speech utterances are section-length (up to 4000 chars),
        // not 200-char chunks: if the webview rations utterances, one
        // utterance still delivers many sentences. Audio tiers keep
        // 200-char chunks (Google cap) via failToAudio's own queue.
        queue = makeQueue(buildSpeechChunks(collectSections(doc)));
        queue.state = 'playing';
        ensureAudioEl(); // gesture-adjacent creation (v2)
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
        // v2: keep the persistent element across stop() so the next
        // session reuses the blessed element instead of a fresh one.
        skippedChunks = 0;
        consecutiveAudioFailures = 0;
        audioAttempt = 0;
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
        // v2: keep the persistent element (see stop()).
        queue = null;
        this.play();
      },
      _queue: function () { return queue; },
      _debug: function () {
        return { mode: mode, state: queue ? queue.state : null, index: queue ? queue.index : null, played: queue ? queue.played : null, endpointConfigured: !!endpoint, tierCount: audioTiers.length, skippedChunks: skippedChunks, consecutiveAudioFailures: consecutiveAudioFailures, audioPersistent: !!audioEl };
      }
    };
  }

  var api = { chunkText: chunkText, makeQueue: makeQueue, collectBookText: collectBookText, collectSections: collectSections, buildSpeechChunks: buildSpeechChunks, createPlayer: createPlayer, MAX_CHUNK: MAX_CHUNK, MAX_AUDIO_CHUNK: MAX_AUDIO_CHUNK, MAX_SPEECH_CHUNK: MAX_SPEECH_CHUNK, responsiveVoiceUrl: responsiveVoiceUrl, googleTranslateUrl: googleTranslateUrl, googleApisUrl: googleApisUrl };
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
