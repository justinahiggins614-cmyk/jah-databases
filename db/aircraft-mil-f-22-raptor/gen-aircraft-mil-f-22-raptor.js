(function(){'use strict';
/* JAH F-22 Raptor Database generator — jahdb-aircraft-mil-f-22-raptor-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-F22-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — F-22 Raptor",
  "Design origins and first flight — F-22 Raptor",
  "Dimensions and general arrangement — F-22 Raptor",
  "Powerplant basics — F-22 Raptor",
  "Performance basics — F-22 Raptor",
  "How it flies — F-22 Raptor",
  "Service history, part one — F-22 Raptor"
 ],
 "Compounded": [
  "Variants and sub-models — F-22 Raptor",
  "Operators around the world — F-22 Raptor",
  "Performance analysis — F-22 Raptor",
  "Systems and avionics — F-22 Raptor",
  "Service history, part two — F-22 Raptor",
  "Maintenance and operations — F-22 Raptor",
  "Comparison with contemporaries — F-22 Raptor"
 ],
 "Advanced": [
  "Engineering deep-dive — F-22 Raptor",
  "Weapons and mission systems — F-22 Raptor",
  "Production analysis — F-22 Raptor",
  "Upgrades and modernization programs — F-22 Raptor",
  "Legacy and preservation — F-22 Raptor",
  "Records and superlatives — F-22 Raptor"
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
  J.generators["aircraft-mil-f-22-raptor"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
