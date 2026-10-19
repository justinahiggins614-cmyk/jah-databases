(function(){'use strict';
/* JAH Ferrari Testarossa (1984-1996) Database generator — jahdb-car-classic-ferrari-testarossa-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-FTESTA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Ferrari Testarossa (1984-1996)",
  "Design origins and launch — Ferrari Testarossa (1984-1996)",
  "Dimensions and general arrangement — Ferrari Testarossa (1984-1996)",
  "Powertrain basics — Ferrari Testarossa (1984-1996)",
  "Performance basics — Ferrari Testarossa (1984-1996)",
  "How it drives — Ferrari Testarossa (1984-1996)",
  "Production history, part one — Ferrari Testarossa (1984-1996)"
 ],
 "Compounded": [
  "Variants and model years — Ferrari Testarossa (1984-1996)",
  "Markets and sales — Ferrari Testarossa (1984-1996)",
  "Performance analysis — Ferrari Testarossa (1984-1996)",
  "Engineering details — Ferrari Testarossa (1984-1996)",
  "Production history, part two — Ferrari Testarossa (1984-1996)",
  "Ownership and maintenance — Ferrari Testarossa (1984-1996)",
  "Comparison with contemporaries — Ferrari Testarossa (1984-1996)"
 ],
 "Advanced": [
  "Engineering deep-dive — Ferrari Testarossa (1984-1996)",
  "Racing and motorsport heritage — Ferrari Testarossa (1984-1996)",
  "Production analysis — Ferrari Testarossa (1984-1996)",
  "Restoration guide — Ferrari Testarossa (1984-1996)",
  "Collector market and values — Ferrari Testarossa (1984-1996)",
  "Legacy and cultural impact — Ferrari Testarossa (1984-1996)"
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
  J.generators["car-classic-ferrari-testarossa"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
