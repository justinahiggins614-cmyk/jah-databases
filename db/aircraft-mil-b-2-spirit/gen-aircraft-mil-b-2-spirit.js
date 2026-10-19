(function(){'use strict';
/* JAH B-2 Spirit Database generator — jahdb-aircraft-mil-b-2-spirit-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAC-B2-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — B-2 Spirit",
  "Design origins and first flight — B-2 Spirit",
  "Dimensions and general arrangement — B-2 Spirit",
  "Powerplant basics — B-2 Spirit",
  "Performance basics — B-2 Spirit",
  "How it flies — B-2 Spirit",
  "Service history, part one — B-2 Spirit"
 ],
 "Compounded": [
  "Variants and sub-models — B-2 Spirit",
  "Operators around the world — B-2 Spirit",
  "Performance analysis — B-2 Spirit",
  "Systems and avionics — B-2 Spirit",
  "Service history, part two — B-2 Spirit",
  "Maintenance and operations — B-2 Spirit",
  "Comparison with contemporaries — B-2 Spirit"
 ],
 "Advanced": [
  "Engineering deep-dive — B-2 Spirit",
  "Weapons and mission systems — B-2 Spirit",
  "Production analysis — B-2 Spirit",
  "Upgrades and modernization programs — B-2 Spirit",
  "Legacy and preservation — B-2 Spirit",
  "Records and superlatives — B-2 Spirit"
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
  J.generators["aircraft-mil-b-2-spirit"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
