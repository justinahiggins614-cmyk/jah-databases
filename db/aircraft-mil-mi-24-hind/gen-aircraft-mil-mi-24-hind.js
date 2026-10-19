(function(){'use strict';
/* JAH Mil Mi-24 Hind Database generator — jahdb-aircraft-mil-mi-24-hind-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-MI24-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Mil Mi-24 Hind",
  "Design origins and first flight — Mil Mi-24 Hind",
  "Dimensions and general arrangement — Mil Mi-24 Hind",
  "Powerplant basics — Mil Mi-24 Hind",
  "Performance basics — Mil Mi-24 Hind",
  "How it flies — Mil Mi-24 Hind",
  "Service history, part one — Mil Mi-24 Hind"
 ],
 "Compounded": [
  "Variants and sub-models — Mil Mi-24 Hind",
  "Operators around the world — Mil Mi-24 Hind",
  "Performance analysis — Mil Mi-24 Hind",
  "Systems and avionics — Mil Mi-24 Hind",
  "Service history, part two — Mil Mi-24 Hind",
  "Maintenance and operations — Mil Mi-24 Hind",
  "Comparison with contemporaries — Mil Mi-24 Hind"
 ],
 "Advanced": [
  "Engineering deep-dive — Mil Mi-24 Hind",
  "Weapons and mission systems — Mil Mi-24 Hind",
  "Production analysis — Mil Mi-24 Hind",
  "Upgrades and modernization programs — Mil Mi-24 Hind",
  "Legacy and preservation — Mil Mi-24 Hind",
  "Records and superlatives — Mil Mi-24 Hind"
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
  J.generators["aircraft-mil-mi-24-hind"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
