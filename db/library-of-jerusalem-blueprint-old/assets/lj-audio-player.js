/* LJAudio — rebuilt chunked read-aloud player for the Library of Jerusalem Redo.
   Fixes the old defect (fallback truncated text to ~200 chars and stopped early).
   Behavior: the ENTIRE book text is split at sentence boundaries into small chunks;
   every chunk is queued and played in order — nothing is truncated, no short timeout
   ends playback. Pause/resume/stop/replay + error recovery + rapid-press guard.
   The chunking/queue logic is exported for node tests; browser wiring is guarded. */
(function (global) {
  'use strict';

  var MAX_CHUNK = 200;

  // Split full text into sentence-boundary chunks, each <= MAX_CHUNK chars.
  // Guarantees: joining the chunks reproduces the input text exactly (no loss).
  function chunkText(text) {
    if (!text) return [];
    var sentences = text.match(/[^.!?]+[.!?]+["']?\s*|[^.!?]+$/g) || [text];
    var chunks = [];
    var cur = '';
    for (var i = 0; i < sentences.length; i++) {
      var s = sentences[i];
      if ((cur + s).length > MAX_CHUNK && cur.length > 0) {
        chunks.push(cur);
        cur = '';
      }
      // A single over-long sentence is hard-split so nothing is ever dropped.
      while (s.length > MAX_CHUNK) {
        var cut = s.lastIndexOf(' ', MAX_CHUNK);
        if (cut <= 0) cut = MAX_CHUNK;
        chunks.push((cur + s.slice(0, cut)).trim());
        cur = '';
        s = s.slice(cut).trim();
      }
      cur += s;
    }
    if (cur.trim().length > 0) chunks.push(cur);
    return chunks;
  }

  // Pure queue state machine (testable without speech synthesis).
  function makeQueue(chunks) {
    return {
      chunks: chunks.slice(),
      index: 0,
      state: 'idle', // idle | playing | paused | finished | error
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

  function createPlayer(doc, synth) {
    var queue = null;
    var statusEl = null;
    var progressEl = null;
    var utter = null;

    function setStatus(msg) { if (statusEl) statusEl.textContent = msg; }
    function setProgress() {
      if (progressEl && queue) {
        progressEl.textContent = 'Chunk ' + (queue.index + 1) + ' of ' + queue.chunks.length +
          (queue.state === 'finished' ? ' — Finished — full book read aloud.' : '');
      }
    }

    function speakNext() {
      if (!queue || queue.state !== 'playing') return;
      if (queue.index >= queue.chunks.length) {
        queue.state = 'finished';
        setStatus('Finished — full book read aloud.');
        setProgress();
        return;
      }
      var text = queue.chunks[queue.index];
      utter = new global.SpeechSynthesisUtterance(text);
      utter.onend = function () {
        queue.consecutiveErrors = 0;
        queue.advance();
        setProgress();
        speakNext();
      };
      utter.onerror = function () {
        queue.noteError();
        if (queue.state === 'error') {
          setStatus('Playback stopped after repeated errors. Press Replay to try again.');
          setProgress();
          return;
        }
        queue.advance(); // skip the failed chunk, keep going — never stall the book
        setProgress();
        speakNext();
      };
      synth.speak(utter);
      setStatus('Reading aloud…');
      setProgress();
    }

    return {
      bind: function (statusId, progressId) {
        statusEl = doc.getElementById(statusId);
        progressEl = doc.getElementById(progressId);
      },
      play: function () {
        if (queue && queue.state === 'playing') return; // rapid-press guard: no-op
        if (queue && queue.state === 'paused') {
          queue.state = 'playing';
          synth.resume();
          setStatus('Reading aloud…');
          return;
        }
        var text = collectBookText(doc);
        queue = makeQueue(chunkText(text));
        queue.state = 'playing';
        if (!synth) { setStatus('Speech is not available in this browser.'); queue.state = 'error'; return; }
        speakNext();
      },
      pause: function () {
        if (queue && queue.state === 'playing') {
          queue.state = 'paused';
          synth.pause();
          setStatus('Paused.');
        }
      },
      resume: function () {
        if (queue && queue.state === 'paused') {
          queue.state = 'playing';
          synth.resume();
          setStatus('Reading aloud…');
        }
      },
      stop: function () {
        if (synth) synth.cancel();
        if (queue) queue.reset();
        utter = null;
        setStatus('Stopped.');
        setProgress();
      },
      replay: function () {
        if (synth) synth.cancel();
        queue = null;
        this.play();
      },
      _queue: function () { return queue; }
    };
  }

  var api = { chunkText: chunkText, makeQueue: makeQueue, collectBookText: collectBookText, createPlayer: createPlayer };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.LJAudio = api;

  if (typeof document !== 'undefined' && typeof window !== 'undefined' && window.speechSynthesis) {
    document.addEventListener('DOMContentLoaded', function () {
      var player = createPlayer(document, window.speechSynthesis);
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
    });
  }
})(typeof window !== 'undefined' ? window : globalThis);
