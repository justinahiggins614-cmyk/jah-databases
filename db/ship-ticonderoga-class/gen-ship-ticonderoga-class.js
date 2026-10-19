(function(){'use strict';
/* JAH Ticonderoga-class Cruiser Database generator — jahdb-ship-ticonderoga-class-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSC-TICO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Ticonderoga-class Cruiser",
  "Design origins and authorization — Ticonderoga-class Cruiser",
  "Dimensions and general arrangement — Ticonderoga-class Cruiser",
  "Propulsion basics — Ticonderoga-class Cruiser",
  "Performance basics — Ticonderoga-class Cruiser",
  "How a warship works — Ticonderoga-class Cruiser",
  "Service history, part one — Ticonderoga-class Cruiser"
 ],
 "Compounded": [
  "Ships of the class — Ticonderoga-class Cruiser",
  "Operators and deployments — Ticonderoga-class Cruiser",
  "Performance analysis — Ticonderoga-class Cruiser",
  "Weapons and sensors — Ticonderoga-class Cruiser",
  "Service history, part two — Ticonderoga-class Cruiser",
  "Crew and daily life — Ticonderoga-class Cruiser",
  "Comparison with contemporaries — Ticonderoga-class Cruiser"
 ],
 "Advanced": [
  "Engineering deep-dive — Ticonderoga-class Cruiser",
  "Combat systems in detail — Ticonderoga-class Cruiser",
  "Construction analysis — Ticonderoga-class Cruiser",
  "Modernization and refits — Ticonderoga-class Cruiser",
  "Legacy and preservation — Ticonderoga-class Cruiser",
  "Records and superlatives — Ticonderoga-class Cruiser"
 ]
};
var DEMOKIND="ship sample calculation";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# sea performance sample — "+safe+"\n"
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
    name:topic+' — ship record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A ship record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. ',
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
  J.generators["ship-ticonderoga-class"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
