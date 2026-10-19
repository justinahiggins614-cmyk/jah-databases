(function(){'use strict';
/* JAH A-6 Intruder Database generator — jahdb-aircraft-mil-a-6-intruder-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-A6S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — A-6 Intruder",
  "Design origins and first flight — A-6 Intruder",
  "Dimensions and general arrangement — A-6 Intruder",
  "Powerplant basics — A-6 Intruder",
  "Performance basics — A-6 Intruder",
  "How it flies — A-6 Intruder",
  "Service history, part one — A-6 Intruder"
 ],
 "Compounded": [
  "Variants and sub-models — A-6 Intruder",
  "Operators around the world — A-6 Intruder",
  "Performance analysis — A-6 Intruder",
  "Systems and avionics — A-6 Intruder",
  "Service history, part two — A-6 Intruder",
  "Maintenance and operations — A-6 Intruder",
  "Comparison with contemporaries — A-6 Intruder"
 ],
 "Advanced": [
  "Engineering deep-dive — A-6 Intruder",
  "Weapons and mission systems — A-6 Intruder",
  "Production analysis — A-6 Intruder",
  "Upgrades and modernization programs — A-6 Intruder",
  "Legacy and preservation — A-6 Intruder",
  "Records and superlatives — A-6 Intruder"
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
    description:'SAMPLE RECORD (generated — structural sample). A aircraft record of "'+topic+'" in '+field+'. Signature-original sample — explicitly labeled, never presented as public record. ',
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
  J.generators["aircraft-mil-a-6-intruder-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
