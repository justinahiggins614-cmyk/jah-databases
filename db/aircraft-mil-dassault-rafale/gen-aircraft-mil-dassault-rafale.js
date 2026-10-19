(function(){'use strict';
/* JAH Dassault Rafale Database generator — jahdb-aircraft-mil-dassault-rafale-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-RAFALE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Dassault Rafale",
  "Design origins and first flight — Dassault Rafale",
  "Dimensions and general arrangement — Dassault Rafale",
  "Powerplant basics — Dassault Rafale",
  "Performance basics — Dassault Rafale",
  "How it flies — Dassault Rafale",
  "Service history, part one — Dassault Rafale"
 ],
 "Compounded": [
  "Variants and sub-models — Dassault Rafale",
  "Operators around the world — Dassault Rafale",
  "Performance analysis — Dassault Rafale",
  "Systems and avionics — Dassault Rafale",
  "Service history, part two — Dassault Rafale",
  "Maintenance and operations — Dassault Rafale",
  "Comparison with contemporaries — Dassault Rafale"
 ],
 "Advanced": [
  "Engineering deep-dive — Dassault Rafale",
  "Weapons and mission systems — Dassault Rafale",
  "Production analysis — Dassault Rafale",
  "Upgrades and modernization programs — Dassault Rafale",
  "Legacy and preservation — Dassault Rafale",
  "Records and superlatives — Dassault Rafale"
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
  J.generators["aircraft-mil-dassault-rafale"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
