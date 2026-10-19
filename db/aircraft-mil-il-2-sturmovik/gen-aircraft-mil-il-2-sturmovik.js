(function(){'use strict';
/* JAH Ilyushin Il-2 Sturmovik Database generator — jahdb-aircraft-mil-il-2-sturmovik-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-IL2-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Ilyushin Il-2 Sturmovik",
  "Design origins and first flight — Ilyushin Il-2 Sturmovik",
  "Dimensions and general arrangement — Ilyushin Il-2 Sturmovik",
  "Powerplant basics — Ilyushin Il-2 Sturmovik",
  "Performance basics — Ilyushin Il-2 Sturmovik",
  "How it flies — Ilyushin Il-2 Sturmovik",
  "Service history, part one — Ilyushin Il-2 Sturmovik"
 ],
 "Compounded": [
  "Variants and sub-models — Ilyushin Il-2 Sturmovik",
  "Operators around the world — Ilyushin Il-2 Sturmovik",
  "Performance analysis — Ilyushin Il-2 Sturmovik",
  "Systems and avionics — Ilyushin Il-2 Sturmovik",
  "Service history, part two — Ilyushin Il-2 Sturmovik",
  "Maintenance and operations — Ilyushin Il-2 Sturmovik",
  "Comparison with contemporaries — Ilyushin Il-2 Sturmovik"
 ],
 "Advanced": [
  "Engineering deep-dive — Ilyushin Il-2 Sturmovik",
  "Weapons and mission systems — Ilyushin Il-2 Sturmovik",
  "Production analysis — Ilyushin Il-2 Sturmovik",
  "Upgrades and modernization programs — Ilyushin Il-2 Sturmovik",
  "Legacy and preservation — Ilyushin Il-2 Sturmovik",
  "Records and superlatives — Ilyushin Il-2 Sturmovik"
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
  J.generators["aircraft-mil-il-2-sturmovik"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
