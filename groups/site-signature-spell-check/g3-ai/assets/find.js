/* Keyword lookup over the shipped archive sample. Browser + Node. */
(function(g){
'use strict';
function findRecords(q, sample){
  q = String(q == null ? '' : q).toLowerCase().trim();
  if(!q) return [];
  var words = q.split(/\s+/);
  return (sample || []).filter(function(r){
    var hay = ((r.t || r.title || '') + ' ' + (r.description || '') + ' ' + (r.g || r.group || '')).toLowerCase();
    return words.every(function(w){ return hay.indexOf(w) !== -1; });
  });
}
var API = {findRecords: findRecords};
if(typeof module !== 'undefined'){ module.exports = API; }
if(typeof window !== 'undefined'){ window.SigFind = API; }
if(typeof globalThis !== 'undefined'){ globalThis.SigFind = API; }
})(typeof globalThis !== 'undefined' ? globalThis : this);
