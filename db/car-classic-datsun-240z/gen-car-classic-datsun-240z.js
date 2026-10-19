(function(){'use strict';
/* JAH Datsun 240Z (1969-1973) Database generator — jahdb-car-classic-datsun-240z-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-D240Z-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Datsun 240Z (1969-1973)",
  "Design origins and launch — Datsun 240Z (1969-1973)",
  "Dimensions and general arrangement — Datsun 240Z (1969-1973)",
  "Powertrain basics — Datsun 240Z (1969-1973)",
  "Performance basics — Datsun 240Z (1969-1973)",
  "How it drives — Datsun 240Z (1969-1973)",
  "Production history, part one — Datsun 240Z (1969-1973)"
 ],
 "Compounded": [
  "Variants and model years — Datsun 240Z (1969-1973)",
  "Markets and sales — Datsun 240Z (1969-1973)",
  "Performance analysis — Datsun 240Z (1969-1973)",
  "Engineering details — Datsun 240Z (1969-1973)",
  "Production history, part two — Datsun 240Z (1969-1973)",
  "Ownership and maintenance — Datsun 240Z (1969-1973)",
  "Comparison with contemporaries — Datsun 240Z (1969-1973)"
 ],
 "Advanced": [
  "Engineering deep-dive — Datsun 240Z (1969-1973)",
  "Racing and motorsport heritage — Datsun 240Z (1969-1973)",
  "Production analysis — Datsun 240Z (1969-1973)",
  "Restoration guide — Datsun 240Z (1969-1973)",
  "Collector market and values — Datsun 240Z (1969-1973)",
  "Legacy and cultural impact — Datsun 240Z (1969-1973)"
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
  J.generators["car-classic-datsun-240z"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
