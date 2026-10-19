(function(){'use strict';
/* JAH P-3 Orion Database generator — jahdb-aircraft-mil-p-3-orion-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-P3-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — P-3 Orion",
  "Design origins and first flight — P-3 Orion",
  "Dimensions and general arrangement — P-3 Orion",
  "Powerplant basics — P-3 Orion",
  "Performance basics — P-3 Orion",
  "How it flies — P-3 Orion",
  "Service history, part one — P-3 Orion"
 ],
 "Compounded": [
  "Variants and sub-models — P-3 Orion",
  "Operators around the world — P-3 Orion",
  "Performance analysis — P-3 Orion",
  "Systems and avionics — P-3 Orion",
  "Service history, part two — P-3 Orion",
  "Maintenance and operations — P-3 Orion",
  "Comparison with contemporaries — P-3 Orion"
 ],
 "Advanced": [
  "Engineering deep-dive — P-3 Orion",
  "Weapons and mission systems — P-3 Orion",
  "Production analysis — P-3 Orion",
  "Upgrades and modernization programs — P-3 Orion",
  "Legacy and preservation — P-3 Orion",
  "Records and superlatives — P-3 Orion"
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
  J.generators["aircraft-mil-p-3-orion"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
