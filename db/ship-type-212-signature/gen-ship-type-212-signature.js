(function(){'use strict';
/* JAH Type 212 Submarine Database generator — jahdb-ship-type-212-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSC-T212S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Type 212 Submarine",
  "Design origins and authorization — Type 212 Submarine",
  "Dimensions and general arrangement — Type 212 Submarine",
  "Propulsion basics — Type 212 Submarine",
  "Performance basics — Type 212 Submarine",
  "How a warship works — Type 212 Submarine",
  "Service history, part one — Type 212 Submarine"
 ],
 "Compounded": [
  "Ships of the class — Type 212 Submarine",
  "Operators and deployments — Type 212 Submarine",
  "Performance analysis — Type 212 Submarine",
  "Weapons and sensors — Type 212 Submarine",
  "Service history, part two — Type 212 Submarine",
  "Crew and daily life — Type 212 Submarine",
  "Comparison with contemporaries — Type 212 Submarine"
 ],
 "Advanced": [
  "Engineering deep-dive — Type 212 Submarine",
  "Combat systems in detail — Type 212 Submarine",
  "Construction analysis — Type 212 Submarine",
  "Modernization and refits — Type 212 Submarine",
  "Legacy and preservation — Type 212 Submarine",
  "Records and superlatives — Type 212 Submarine"
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
  J.generators["ship-type-212-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
