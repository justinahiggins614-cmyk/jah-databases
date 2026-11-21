
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

/* Database-concept generator: drafts a new database concept from real
   manifest databases. Deterministic: same seed = same concept. */
function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  var kinds=['Archive','Catalog','Guide','Index','Atlas','Register','Primer','Field Guide'];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var src=pick(r, data.records);
    var kind=pick(r, kinds);
    var id='JAH-DBGEN-'+num6(r);
    var base=src.title.replace(/ Database$/,'');
    if(!/^The /i.test(base)) base='The '+base;
    var name=base+' '+kind+' Database';
    out.push({id:id, kind:kind, pattern:src.slug,
      text:'Generated database concept '+id+' (simulated): "'+name+'" \u2014 in the manner of "'+src.title+'" ('+src.slug+', '+src.count+' records, kind: '+src.kind+'). A concept only: a subject, a kind, and a plain description. Not a database, not a record, and it never claims the archive holds it.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
