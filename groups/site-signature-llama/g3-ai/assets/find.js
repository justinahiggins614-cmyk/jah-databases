/* findRecords(q, sample): keyword lookup over the archive sample. Pure. */
function findRecords(q, sample) {
  if (!q || typeof q !== 'string') return [];
  var needle = q.toLowerCase().trim();
  if (!needle) return [];
  var words = needle.split(/\s+/).filter(function (w) { return w.length > 2; });
  if (!words.length) words = [needle];
  return sample.filter(function (r) {
    var hay = ((r.title || '') + ' ' + (r.desc || '')).toLowerCase();
    return words.every(function (w) { return hay.indexOf(w) !== -1; });
  });
}
function localAnswer(q, sample) {
  var hits = findRecords(q, sample);
  if (!hits.length) return 'The archive sample on this page does not hold an answer to that question. Try one of the sample questions below.';
  var h = hits[0];
  return h.title + ' (' + h.id + '): ' + h.desc;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { findRecords: findRecords, localAnswer: localAnswer };
