(function(){'use strict';
/* JAH Messerschmitt Me 262 Database generator — jahdb-aircraft-mil-me-262-schwalbe-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-ME262S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Messerschmitt Me 262",
  "Design origins and first flight — Messerschmitt Me 262",
  "Dimensions and general arrangement — Messerschmitt Me 262",
  "Powerplant basics — Messerschmitt Me 262",
  "Performance basics — Messerschmitt Me 262",
  "How it flies — Messerschmitt Me 262",
  "Service history, part one — Messerschmitt Me 262"
 ],
 "Compounded": [
  "Variants and sub-models — Messerschmitt Me 262",
  "Operators around the world — Messerschmitt Me 262",
  "Performance analysis — Messerschmitt Me 262",
  "Systems and avionics — Messerschmitt Me 262",
  "Service history, part two — Messerschmitt Me 262",
  "Maintenance and operations — Messerschmitt Me 262",
  "Comparison with contemporaries — Messerschmitt Me 262"
 ],
 "Advanced": [
  "Engineering deep-dive — Messerschmitt Me 262",
  "Weapons and mission systems — Messerschmitt Me 262",
  "Production analysis — Messerschmitt Me 262",
  "Upgrades and modernization programs — Messerschmitt Me 262",
  "Legacy and preservation — Messerschmitt Me 262",
  "Records and superlatives — Messerschmitt Me 262"
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
  J.generators["aircraft-mil-me-262-schwalbe-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
