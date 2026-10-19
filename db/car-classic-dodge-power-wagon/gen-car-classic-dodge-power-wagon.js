(function(){'use strict';
/* JAH Dodge Power Wagon (1945-1980) Database generator — jahdb-car-classic-dodge-power-wagon-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-DPW-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Dodge Power Wagon (1945-1980)",
  "Design origins and launch — Dodge Power Wagon (1945-1980)",
  "Dimensions and general arrangement — Dodge Power Wagon (1945-1980)",
  "Powertrain basics — Dodge Power Wagon (1945-1980)",
  "Performance basics — Dodge Power Wagon (1945-1980)",
  "How it drives — Dodge Power Wagon (1945-1980)",
  "Production history, part one — Dodge Power Wagon (1945-1980)"
 ],
 "Compounded": [
  "Variants and model years — Dodge Power Wagon (1945-1980)",
  "Markets and sales — Dodge Power Wagon (1945-1980)",
  "Performance analysis — Dodge Power Wagon (1945-1980)",
  "Engineering details — Dodge Power Wagon (1945-1980)",
  "Production history, part two — Dodge Power Wagon (1945-1980)",
  "Ownership and maintenance — Dodge Power Wagon (1945-1980)",
  "Comparison with contemporaries — Dodge Power Wagon (1945-1980)"
 ],
 "Advanced": [
  "Engineering deep-dive — Dodge Power Wagon (1945-1980)",
  "Racing and motorsport heritage — Dodge Power Wagon (1945-1980)",
  "Production analysis — Dodge Power Wagon (1945-1980)",
  "Restoration guide — Dodge Power Wagon (1945-1980)",
  "Collector market and values — Dodge Power Wagon (1945-1980)",
  "Legacy and cultural impact — Dodge Power Wagon (1945-1980)"
 ]
};
var DEMOKIND="car sample calculation";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# road performance sample — "+safe+"\n"
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
    name:topic+' — car record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A car record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. ',
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
  J.generators["car-classic-dodge-power-wagon"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
