(function(){'use strict';
/* JAH Fiat 124 Spider (1966-1985) Database generator — jahdb-car-classic-fiat-124-spider-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-F124S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Fiat 124 Spider (1966-1985)",
  "Design origins and launch — Fiat 124 Spider (1966-1985)",
  "Dimensions and general arrangement — Fiat 124 Spider (1966-1985)",
  "Powertrain basics — Fiat 124 Spider (1966-1985)",
  "Performance basics — Fiat 124 Spider (1966-1985)",
  "How it drives — Fiat 124 Spider (1966-1985)",
  "Production history, part one — Fiat 124 Spider (1966-1985)"
 ],
 "Compounded": [
  "Variants and model years — Fiat 124 Spider (1966-1985)",
  "Markets and sales — Fiat 124 Spider (1966-1985)",
  "Performance analysis — Fiat 124 Spider (1966-1985)",
  "Engineering details — Fiat 124 Spider (1966-1985)",
  "Production history, part two — Fiat 124 Spider (1966-1985)",
  "Ownership and maintenance — Fiat 124 Spider (1966-1985)",
  "Comparison with contemporaries — Fiat 124 Spider (1966-1985)"
 ],
 "Advanced": [
  "Engineering deep-dive — Fiat 124 Spider (1966-1985)",
  "Racing and motorsport heritage — Fiat 124 Spider (1966-1985)",
  "Production analysis — Fiat 124 Spider (1966-1985)",
  "Restoration guide — Fiat 124 Spider (1966-1985)",
  "Collector market and values — Fiat 124 Spider (1966-1985)",
  "Legacy and cultural impact — Fiat 124 Spider (1966-1985)"
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
  J.generators["car-classic-fiat-124-spider"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
