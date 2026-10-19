(function(){'use strict';
/* JAH Nelson-class Battleship Database generator — jahdb-ship-nelson-class-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSC-NELS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Nelson-class Battleship",
  "Design origins and authorization — Nelson-class Battleship",
  "Dimensions and general arrangement — Nelson-class Battleship",
  "Propulsion basics — Nelson-class Battleship",
  "Performance basics — Nelson-class Battleship",
  "How a warship works — Nelson-class Battleship",
  "Service history, part one — Nelson-class Battleship"
 ],
 "Compounded": [
  "Ships of the class — Nelson-class Battleship",
  "Operators and deployments — Nelson-class Battleship",
  "Performance analysis — Nelson-class Battleship",
  "Weapons and sensors — Nelson-class Battleship",
  "Service history, part two — Nelson-class Battleship",
  "Crew and daily life — Nelson-class Battleship",
  "Comparison with contemporaries — Nelson-class Battleship"
 ],
 "Advanced": [
  "Engineering deep-dive — Nelson-class Battleship",
  "Combat systems in detail — Nelson-class Battleship",
  "Construction analysis — Nelson-class Battleship",
  "Modernization and refits — Nelson-class Battleship",
  "Legacy and preservation — Nelson-class Battleship",
  "Records and superlatives — Nelson-class Battleship"
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
  J.generators["ship-nelson-class"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
