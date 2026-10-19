(function(){'use strict';
/* JAH F-86 Sabre Database generator — jahdb-aircraft-mil-f-86-sabre-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-F86-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — F-86 Sabre",
  "Design origins and first flight — F-86 Sabre",
  "Dimensions and general arrangement — F-86 Sabre",
  "Powerplant basics — F-86 Sabre",
  "Performance basics — F-86 Sabre",
  "How it flies — F-86 Sabre",
  "Service history, part one — F-86 Sabre"
 ],
 "Compounded": [
  "Variants and sub-models — F-86 Sabre",
  "Operators around the world — F-86 Sabre",
  "Performance analysis — F-86 Sabre",
  "Systems and avionics — F-86 Sabre",
  "Service history, part two — F-86 Sabre",
  "Maintenance and operations — F-86 Sabre",
  "Comparison with contemporaries — F-86 Sabre"
 ],
 "Advanced": [
  "Engineering deep-dive — F-86 Sabre",
  "Weapons and mission systems — F-86 Sabre",
  "Production analysis — F-86 Sabre",
  "Upgrades and modernization programs — F-86 Sabre",
  "Legacy and preservation — F-86 Sabre",
  "Records and superlatives — F-86 Sabre"
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
  J.generators["aircraft-mil-f-86-sabre"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
