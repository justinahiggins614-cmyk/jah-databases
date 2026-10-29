/* suite-read-helper.js — dynamic read-marking for JS-loaded Jerusalem suite
   pages (e2-city-jerusalem + e2-city-jerusalem-signature).

   WHY IT EXISTS: those two pages render archive records with JavaScript
   (loadCatSample) AFTER page load, so a static patch cannot mark record
   text ahead of time. LJAudio2 collects [data-audio-text] sections at Play
   time, so this helper tags rendered record cards as they appear and the
   player picks them up with ZERO player changes.

   WHAT IT TAGS (and only this): inside #groups and #results, each rendered
   .card gets data-audio-text on its <h3> (record title) and its <p class>
   description paragraph. It never tags the full-record <dl> (raw field
   dumps are not read aloud), generator output (#gOut), or the merge queue.
   Tagging is idempotent: a card already tagged (data-lj-tagged="1") is
   skipped, so re-runs and re-renders never double-mark.

   LOAD ORDER: this file is loaded before lj-audio-player.js on e2 pages.
   It works regardless of load order (observer + initial sweep), but the
   documented order keeps the dependency explicit. No key, no endpoint,
   no provider information is in this file. */
(function () {
  'use strict';

  function tagCard(card) {
    if (!card || card.getAttribute('data-lj-tagged') === '1') return 0;
    var n = 0;
    var h = card.querySelector('h3');
    if (h && !h.hasAttribute('data-audio-text')) {
      h.setAttribute('data-audio-text', '');
      n++;
    }
    var ps = card.querySelectorAll('p.dim');
    for (var i = 0; i < ps.length; i++) {
      if (!ps[i].hasAttribute('data-audio-text')) {
        ps[i].setAttribute('data-audio-text', '');
        n++;
      }
    }
    card.setAttribute('data-lj-tagged', '1');
    return n;
  }

  function sweep(root) {
    if (!root || typeof root.querySelectorAll !== 'function') return 0;
    var cards = root.querySelectorAll('.card');
    var n = 0;
    for (var i = 0; i < cards.length; i++) n += tagCard(cards[i]);
    return n;
  }

  function start() {
    var targets = [];
    ['groups', 'results'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) targets.push(el);
    });
    targets.forEach(function (el) { sweep(el); });
    if (typeof MutationObserver === 'function') {
      var obs = new MutationObserver(function (mutations) {
        mutations.forEach(function (m) {
          for (var i = 0; i < m.addedNodes.length; i++) {
            var node = m.addedNodes[i];
            if (node.nodeType !== 1) continue;
            if (node.classList && node.classList.contains('card')) tagCard(node);
            else sweep(node);
          }
        });
      });
      targets.forEach(function (el) {
        obs.observe(el, { childList: true, subtree: true });
      });
    }
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', start);
    } else {
      start();
    }
  }

  // Exported for node tests.
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { tagCard: tagCard, sweep: sweep };
  }
})();
