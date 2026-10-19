(function(){'use strict';
/* JAH C-130 Hercules Database generator — jahdb-aircraft-mil-c-130-hercules-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-C130S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — C-130 Hercules",
  "Design origins and first flight — C-130 Hercules",
  "Dimensions and general arrangement — C-130 Hercules",
  "Powerplant basics — C-130 Hercules",
  "Performance basics — C-130 Hercules",
  "How it flies — C-130 Hercules",
  "Service history, part one — C-130 Hercules"
 ],
 "Compounded": [
  "Variants and sub-models — C-130 Hercules",
  "Operators around the world — C-130 Hercules",
  "Performance analysis — C-130 Hercules",
  "Systems and avionics — C-130 Hercules",
  "Service history, part two — C-130 Hercules",
  "Maintenance and operations — C-130 Hercules",
  "Comparison with contemporaries — C-130 Hercules"
 ],
 "Advanced": [
  "Engineering deep-dive — C-130 Hercules",
  "Weapons and mission systems — C-130 Hercules",
  "Production analysis — C-130 Hercules",
  "Upgrades and modernization programs — C-130 Hercules",
  "Legacy and preservation — C-130 Hercules",
  "Records and superlatives — C-130 Hercules"
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
  J.generators["aircraft-mil-c-130-hercules-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
