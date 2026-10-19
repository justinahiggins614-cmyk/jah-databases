(function(){'use strict';
/* JAH Borei-class Submarine Database generator — jahdb-ship-borei-class-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSC-BOREIS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Borei-class Submarine",
  "Design origins and authorization — Borei-class Submarine",
  "Dimensions and general arrangement — Borei-class Submarine",
  "Propulsion basics — Borei-class Submarine",
  "Performance basics — Borei-class Submarine",
  "How a warship works — Borei-class Submarine",
  "Service history, part one — Borei-class Submarine"
 ],
 "Compounded": [
  "Ships of the class — Borei-class Submarine",
  "Operators and deployments — Borei-class Submarine",
  "Performance analysis — Borei-class Submarine",
  "Weapons and sensors — Borei-class Submarine",
  "Service history, part two — Borei-class Submarine",
  "Crew and daily life — Borei-class Submarine",
  "Comparison with contemporaries — Borei-class Submarine"
 ],
 "Advanced": [
  "Engineering deep-dive — Borei-class Submarine",
  "Combat systems in detail — Borei-class Submarine",
  "Construction analysis — Borei-class Submarine",
  "Modernization and refits — Borei-class Submarine",
  "Legacy and preservation — Borei-class Submarine",
  "Records and superlatives — Borei-class Submarine"
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
    description:'SAMPLE RECORD (generated — structural sample). A ship record of "'+topic+'" in '+field+'. Signature-original sample — explicitly labeled, never presented as public record. ',
    field:field,
    src:"signature-generated-completion",
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
  J.generators["ship-borei-class-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
