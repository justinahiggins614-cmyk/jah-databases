(function(){'use strict';
/* JAH Lancia Stratos (1973-1978) Database generator — jahdb-car-classic-lancia-stratos-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-LSTRAT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Lancia Stratos (1973-1978)",
  "Design origins and launch — Lancia Stratos (1973-1978)",
  "Dimensions and general arrangement — Lancia Stratos (1973-1978)",
  "Powertrain basics — Lancia Stratos (1973-1978)",
  "Performance basics — Lancia Stratos (1973-1978)",
  "How it drives — Lancia Stratos (1973-1978)",
  "Production history, part one — Lancia Stratos (1973-1978)"
 ],
 "Compounded": [
  "Variants and model years — Lancia Stratos (1973-1978)",
  "Markets and sales — Lancia Stratos (1973-1978)",
  "Performance analysis — Lancia Stratos (1973-1978)",
  "Engineering details — Lancia Stratos (1973-1978)",
  "Production history, part two — Lancia Stratos (1973-1978)",
  "Ownership and maintenance — Lancia Stratos (1973-1978)",
  "Comparison with contemporaries — Lancia Stratos (1973-1978)"
 ],
 "Advanced": [
  "Engineering deep-dive — Lancia Stratos (1973-1978)",
  "Racing and motorsport heritage — Lancia Stratos (1973-1978)",
  "Production analysis — Lancia Stratos (1973-1978)",
  "Restoration guide — Lancia Stratos (1973-1978)",
  "Collector market and values — Lancia Stratos (1973-1978)",
  "Legacy and cultural impact — Lancia Stratos (1973-1978)"
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
  J.generators["car-classic-lancia-stratos"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
