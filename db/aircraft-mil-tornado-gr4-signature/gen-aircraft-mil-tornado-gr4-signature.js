(function(){'use strict';
/* JAH Panavia Tornado Database generator — jahdb-aircraft-mil-tornado-gr4-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-TORNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Panavia Tornado",
  "Design origins and first flight — Panavia Tornado",
  "Dimensions and general arrangement — Panavia Tornado",
  "Powerplant basics — Panavia Tornado",
  "Performance basics — Panavia Tornado",
  "How it flies — Panavia Tornado",
  "Service history, part one — Panavia Tornado"
 ],
 "Compounded": [
  "Variants and sub-models — Panavia Tornado",
  "Operators around the world — Panavia Tornado",
  "Performance analysis — Panavia Tornado",
  "Systems and avionics — Panavia Tornado",
  "Service history, part two — Panavia Tornado",
  "Maintenance and operations — Panavia Tornado",
  "Comparison with contemporaries — Panavia Tornado"
 ],
 "Advanced": [
  "Engineering deep-dive — Panavia Tornado",
  "Weapons and mission systems — Panavia Tornado",
  "Production analysis — Panavia Tornado",
  "Upgrades and modernization programs — Panavia Tornado",
  "Legacy and preservation — Panavia Tornado",
  "Records and superlatives — Panavia Tornado"
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
  J.generators["aircraft-mil-tornado-gr4-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
