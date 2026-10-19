(function(){'use strict';
/* JAH Jaguar XK120 (1948-1954) Database generator — jahdb-car-classic-jaguar-xk120-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCC-JAGXKS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Introduction and overview — Jaguar XK120 (1948-1954)",
  "Design origins and launch — Jaguar XK120 (1948-1954)",
  "Dimensions and general arrangement — Jaguar XK120 (1948-1954)",
  "Powertrain basics — Jaguar XK120 (1948-1954)",
  "Performance basics — Jaguar XK120 (1948-1954)",
  "How it drives — Jaguar XK120 (1948-1954)",
  "Production history, part one — Jaguar XK120 (1948-1954)"
 ],
 "Compounded": [
  "Variants and model years — Jaguar XK120 (1948-1954)",
  "Markets and sales — Jaguar XK120 (1948-1954)",
  "Performance analysis — Jaguar XK120 (1948-1954)",
  "Engineering details — Jaguar XK120 (1948-1954)",
  "Production history, part two — Jaguar XK120 (1948-1954)",
  "Ownership and maintenance — Jaguar XK120 (1948-1954)",
  "Comparison with contemporaries — Jaguar XK120 (1948-1954)"
 ],
 "Advanced": [
  "Engineering deep-dive — Jaguar XK120 (1948-1954)",
  "Racing and motorsport heritage — Jaguar XK120 (1948-1954)",
  "Production analysis — Jaguar XK120 (1948-1954)",
  "Restoration guide — Jaguar XK120 (1948-1954)",
  "Collector market and values — Jaguar XK120 (1948-1954)",
  "Legacy and cultural impact — Jaguar XK120 (1948-1954)"
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
    description:'SAMPLE RECORD (generated — structural sample). A car record of "'+topic+'" in '+field+'. Signature-original sample — explicitly labeled, never presented as public record. ',
    field:field,
    src:"signature-generated-completion",
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
  J.generators["car-classic-jaguar-xk120-signature"]={generate:generate,validate:validate,fields:FIELDS,prefix:PREFIX};
}catch(e){}
})();
