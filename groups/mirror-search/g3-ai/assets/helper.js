/* Mirror helper lookup: keyword answers from the subject's own archive
   sample. Shared by the page (window) and by Node tests (module.exports). */
(function (root) {
  'use strict';
  var STOP = ['what','does','do','did','is','are','was','were','the','a','an','how','why','when','where','which','who','whom','whose','can','could','would','should','i','you','me','my','it','its','this','that','these','those','of','for','from','to','in','on','at','by','with','about','and','or','but','not','no','yes','please','tell','give','show','there','here','then','than','as','be','been','being','have','has','had','will','shall','may','might','must','your','our','their','his','her','we','they','he','she','am','an'];
  function words(s) { return String(s == null ? '' : s).toLowerCase().match(/[a-z0-9]+/g) || []; }
  function contentWords(s) { return words(s).filter(function (w) { return STOP.indexOf(w) < 0; }); }
  function scoreEntry(q, name, keywords) {
    var qw = words(q), n = words(name), k = words(keywords), s = 0, i, w;
    for (i = 0; i < qw.length; i++) {
      w = qw[i];
      if (n.indexOf(w) < 0 && k.indexOf(w) < 0) return null;
      s += 3 * n.filter(function (x) { return x === w; }).length +
           1 * k.filter(function (x) { return x === w; }).length;
    }
    return s;
  }
  function lookup(records, q) {
    var qw = contentWords(q), best = null, bestScore = 0, i, r, hay, sc;
    if (!qw.length) return null;
    for (i = 0; i < records.length; i++) {
      r = records[i];
      hay = words((r.title || '') + ' ' + (r.keywords || '') + ' ' + (r.text || '') + ' ' + (r.subject || ''));
      sc = 0;
      qw.forEach(function (w) { if (hay.indexOf(w) >= 0) sc++; });
      if (sc > bestScore) { bestScore = sc; best = r; }
    }
    if (!best || bestScore === 0) return null;
    return { record: best, matched: bestScore, of: qw.length };
  }
  var api = { words: words, contentWords: contentWords, scoreEntry: scoreEntry, lookup: lookup };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.MirrorHelper = api;
})(typeof window !== 'undefined' ? window : this);
