(function(){'use strict';
/* JAH Porsche 356 (1948-1965) Database generator — jahdb-car-classic-porsche-356-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-P356-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Porsche 356 (1948-1965)",
  "Design origins and launch — Porsche 356 (1948-1965)",
  "Dimensions and general arrangement — Porsche 356 (1948-1965)",
  "Powertrain basics — Porsche 356 (1948-1965)",
  "Performance basics — Porsche 356 (1948-1965)",
  "How it drives — Porsche 356 (1948-1965)",
  "Production history, part one — Porsche 356 (1948-1965)"
 ],
 "Compounded": [
  "Variants and model years — Porsche 356 (1948-1965)",
  "Markets and sales — Porsche 356 (1948-1965)",
  "Performance analysis — Porsche 356 (1948-1965)",
  "Engineering details — Porsche 356 (1948-1965)",
  "Production history, part two — Porsche 356 (1948-1965)",
  "Ownership and maintenance — Porsche 356 (1948-1965)",
  "Comparison with contemporaries — Porsche 356 (1948-1965)"
 ],
 "Advanced": [
  "Engineering deep-dive — Porsche 356 (1948-1965)",
  "Racing and motorsport heritage — Porsche 356 (1948-1965)",
  "Production analysis — Porsche 356 (1948-1965)",
  "Restoration guide — Porsche 356 (1948-1965)",
  "Collector market and values — Porsche 356 (1948-1965)",
  "Legacy and cultural impact — Porsche 356 (1948-1965)"
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
  J.generators["car-classic-porsche-356"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
