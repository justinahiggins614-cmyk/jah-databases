
/* Find records in the archive sample by title or description words. */
function findRecords(q, sample){
  var needle=String(q||'').trim().toLowerCase();
  if(!needle) return [];
  var words=needle.split(/\s+/);
  return sample.filter(function(r){
    var hay=((r.title||'')+' '+(r.description||'')).toLowerCase();
    return words.every(function(w){ return hay.indexOf(w)>=0; });
  }).slice(0,8);
}
if(typeof module!=='undefined'){module.exports={findRecords:findRecords};}
