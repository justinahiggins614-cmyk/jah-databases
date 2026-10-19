(function(){'use strict';
/* JAH Tu-95 Bear Database generator — jahdb-aircraft-mil-tu-95-bear-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-TU95-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Tu-95 Bear",
  "Design origins and first flight — Tu-95 Bear",
  "Dimensions and general arrangement — Tu-95 Bear",
  "Powerplant basics — Tu-95 Bear",
  "Performance basics — Tu-95 Bear",
  "How it flies — Tu-95 Bear",
  "Service history, part one — Tu-95 Bear"
 ],
 "Compounded": [
  "Variants and sub-models — Tu-95 Bear",
  "Operators around the world — Tu-95 Bear",
  "Performance analysis — Tu-95 Bear",
  "Systems and avionics — Tu-95 Bear",
  "Service history, part two — Tu-95 Bear",
  "Maintenance and operations — Tu-95 Bear",
  "Comparison with contemporaries — Tu-95 Bear"
 ],
 "Advanced": [
  "Engineering deep-dive — Tu-95 Bear",
  "Weapons and mission systems — Tu-95 Bear",
  "Production analysis — Tu-95 Bear",
  "Upgrades and modernization programs — Tu-95 Bear",
  "Legacy and preservation — Tu-95 Bear",
  "Records and superlatives — Tu-95 Bear"
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
  J.generators["aircraft-mil-tu-95-bear"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
