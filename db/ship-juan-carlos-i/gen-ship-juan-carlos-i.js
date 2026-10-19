(function(){'use strict';
/* JAH Juan Carlos I Amphibious Assault Ship Database generator — jahdb-ship-juan-carlos-i-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSC-JC1-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Juan Carlos I Amphibious Assault Ship",
  "Design origins and authorization — Juan Carlos I Amphibious Assault Ship",
  "Dimensions and general arrangement — Juan Carlos I Amphibious Assault Ship",
  "Propulsion basics — Juan Carlos I Amphibious Assault Ship",
  "Performance basics — Juan Carlos I Amphibious Assault Ship",
  "How a warship works — Juan Carlos I Amphibious Assault Ship",
  "Service history, part one — Juan Carlos I Amphibious Assault Ship"
 ],
 "Compounded": [
  "Ships of the class — Juan Carlos I Amphibious Assault Ship",
  "Operators and deployments — Juan Carlos I Amphibious Assault Ship",
  "Performance analysis — Juan Carlos I Amphibious Assault Ship",
  "Weapons and sensors — Juan Carlos I Amphibious Assault Ship",
  "Service history, part two — Juan Carlos I Amphibious Assault Ship",
  "Crew and daily life — Juan Carlos I Amphibious Assault Ship",
  "Comparison with contemporaries — Juan Carlos I Amphibious Assault Ship"
 ],
 "Advanced": [
  "Engineering deep-dive — Juan Carlos I Amphibious Assault Ship",
  "Combat systems in detail — Juan Carlos I Amphibious Assault Ship",
  "Construction analysis — Juan Carlos I Amphibious Assault Ship",
  "Modernization and refits — Juan Carlos I Amphibious Assault Ship",
  "Legacy and preservation — Juan Carlos I Amphibious Assault Ship",
  "Records and superlatives — Juan Carlos I Amphibious Assault Ship"
 ]
};
var DEMOKIND="ship sample calculation";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# sea performance sample — "+safe+"\n"
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
    name:topic+' — ship record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A ship record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. ',
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
  J.generators["ship-juan-carlos-i"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
