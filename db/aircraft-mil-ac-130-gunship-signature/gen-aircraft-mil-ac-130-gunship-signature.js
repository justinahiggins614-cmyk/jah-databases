(function(){'use strict';
/* JAH AC-130 Gunship Database generator — jahdb-aircraft-mil-ac-130-gunship-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-AC130S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — AC-130 Gunship",
  "Design origins and first flight — AC-130 Gunship",
  "Dimensions and general arrangement — AC-130 Gunship",
  "Powerplant basics — AC-130 Gunship",
  "Performance basics — AC-130 Gunship",
  "How it flies — AC-130 Gunship",
  "Service history, part one — AC-130 Gunship"
 ],
 "Compounded": [
  "Variants and sub-models — AC-130 Gunship",
  "Operators around the world — AC-130 Gunship",
  "Performance analysis — AC-130 Gunship",
  "Systems and avionics — AC-130 Gunship",
  "Service history, part two — AC-130 Gunship",
  "Maintenance and operations — AC-130 Gunship",
  "Comparison with contemporaries — AC-130 Gunship"
 ],
 "Advanced": [
  "Engineering deep-dive — AC-130 Gunship",
  "Weapons and mission systems — AC-130 Gunship",
  "Production analysis — AC-130 Gunship",
  "Upgrades and modernization programs — AC-130 Gunship",
  "Legacy and preservation — AC-130 Gunship",
  "Records and superlatives — AC-130 Gunship"
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
  J.generators["aircraft-mil-ac-130-gunship-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
