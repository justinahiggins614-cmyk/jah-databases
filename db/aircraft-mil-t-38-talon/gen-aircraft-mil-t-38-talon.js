(function(){'use strict';
/* JAH T-38 Talon Database generator — jahdb-aircraft-mil-t-38-talon-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-T38-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — T-38 Talon",
  "Design origins and first flight — T-38 Talon",
  "Dimensions and general arrangement — T-38 Talon",
  "Powerplant basics — T-38 Talon",
  "Performance basics — T-38 Talon",
  "How it flies — T-38 Talon",
  "Service history, part one — T-38 Talon"
 ],
 "Compounded": [
  "Variants and sub-models — T-38 Talon",
  "Operators around the world — T-38 Talon",
  "Performance analysis — T-38 Talon",
  "Systems and avionics — T-38 Talon",
  "Service history, part two — T-38 Talon",
  "Maintenance and operations — T-38 Talon",
  "Comparison with contemporaries — T-38 Talon"
 ],
 "Advanced": [
  "Engineering deep-dive — T-38 Talon",
  "Weapons and mission systems — T-38 Talon",
  "Production analysis — T-38 Talon",
  "Upgrades and modernization programs — T-38 Talon",
  "Legacy and preservation — T-38 Talon",
  "Records and superlatives — T-38 Talon"
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
  J.generators["aircraft-mil-t-38-talon"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
