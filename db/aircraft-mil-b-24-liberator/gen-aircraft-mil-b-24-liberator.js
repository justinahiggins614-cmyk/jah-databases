(function(){'use strict';
/* JAH B-24 Liberator Database generator — jahdb-aircraft-mil-b-24-liberator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-B24-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — B-24 Liberator",
  "Design origins and first flight — B-24 Liberator",
  "Dimensions and general arrangement — B-24 Liberator",
  "Powerplant basics — B-24 Liberator",
  "Performance basics — B-24 Liberator",
  "How it flies — B-24 Liberator",
  "Service history, part one — B-24 Liberator"
 ],
 "Compounded": [
  "Variants and sub-models — B-24 Liberator",
  "Operators around the world — B-24 Liberator",
  "Performance analysis — B-24 Liberator",
  "Systems and avionics — B-24 Liberator",
  "Service history, part two — B-24 Liberator",
  "Maintenance and operations — B-24 Liberator",
  "Comparison with contemporaries — B-24 Liberator"
 ],
 "Advanced": [
  "Engineering deep-dive — B-24 Liberator",
  "Weapons and mission systems — B-24 Liberator",
  "Production analysis — B-24 Liberator",
  "Upgrades and modernization programs — B-24 Liberator",
  "Legacy and preservation — B-24 Liberator",
  "Records and superlatives — B-24 Liberator"
 ]
};
var DEMOKIND="aircraft sample calculation";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# flight performance sample — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — aircraft record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A aircraft record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. ',
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  if(!r||!r.id||!r.title)return {ok:false,reason:'missing id/title'};
  if(r.id.indexOf(PREFIX)!==0)return {ok:false,reason:'bad prefix'};
  return {ok:true};
}
try{
  var J=window.JAHDB=window.JAHDB||{};J.generators=J.generators||{};
  J.generators["aircraft-mil-b-24-liberator"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
