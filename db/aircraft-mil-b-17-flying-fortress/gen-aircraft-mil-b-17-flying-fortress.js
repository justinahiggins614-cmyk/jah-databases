(function(){'use strict';
/* JAH B-17 Flying Fortress Database generator — jahdb-aircraft-mil-b-17-flying-fortress-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-B17-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — B-17 Flying Fortress",
  "Design origins and first flight — B-17 Flying Fortress",
  "Dimensions and general arrangement — B-17 Flying Fortress",
  "Powerplant basics — B-17 Flying Fortress",
  "Performance basics — B-17 Flying Fortress",
  "How it flies — B-17 Flying Fortress",
  "Service history, part one — B-17 Flying Fortress"
 ],
 "Compounded": [
  "Variants and sub-models — B-17 Flying Fortress",
  "Operators around the world — B-17 Flying Fortress",
  "Performance analysis — B-17 Flying Fortress",
  "Systems and avionics — B-17 Flying Fortress",
  "Service history, part two — B-17 Flying Fortress",
  "Maintenance and operations — B-17 Flying Fortress",
  "Comparison with contemporaries — B-17 Flying Fortress"
 ],
 "Advanced": [
  "Engineering deep-dive — B-17 Flying Fortress",
  "Weapons and mission systems — B-17 Flying Fortress",
  "Production analysis — B-17 Flying Fortress",
  "Upgrades and modernization programs — B-17 Flying Fortress",
  "Legacy and preservation — B-17 Flying Fortress",
  "Records and superlatives — B-17 Flying Fortress"
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
  J.generators["aircraft-mil-b-17-flying-fortress"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
