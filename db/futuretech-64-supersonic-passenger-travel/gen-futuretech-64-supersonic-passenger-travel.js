(function(){'use strict';
/* JAH The Supersonic Passenger Travel Future Technology Database generator — jahdb-futuretech-64-supersonic-passenger-travel-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT64-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1947: Yeager Breaks the Sound Barrier - Foundations",
  "1962: the Concorde Treaty - Foundations",
  "1968: the Tu-144 Flies First - Foundations",
  "1969: Concorde's First Flight - Foundations",
  "1973: the Boom Ban - Foundations",
  "1976: Concorde Enters Service - Foundations",
  "1977: the Tu-144 Carries Passengers - Foundations",
  "1978: the Tu-144 Grounded - Foundations",
  "2000: Flight 4590 - Foundations",
  "2003: Concorde Retires - Foundations",
  "2014: Boom - the Comeback Startup - Foundations"
 ],
 "Compounded": [
  "2017: X-59 - the Quiet Supersonic - Compounded",
  "2020: XB-1 Rolled Out - Compounded",
  "2021: United Orders Supersonic - Compounded",
  "2021: Aerion Shuts Down - Compounded",
  "2022: American Orders Too - Compounded",
  "2022: the Symphony Engine - Compounded",
  "2024: XB-1's First Flight - Compounded",
  "2024: X-59 Revealed - Compounded",
  "2025: the Barrier Falls Again - Compounded",
  "2025: Measuring the Thump - Compounded",
  "2025: the Ban Under Review - Compounded",
  "2025: Building the Overture Factory - Compounded"
 ],
 "Advanced": [
  "2025: the Supersonic Peloton - Advanced",
  "Overture Enters Service - Advanced",
  "Overland Supersonic Legalized - Advanced",
  "Supersonic Business Jets - Advanced",
  "Second-Generation Fleets - Advanced",
  "Faster Turnarounds - Advanced",
  "Affordable Supersonic - Advanced",
  "Supersonic Cargo - Advanced",
  "Hypersonic Research - Advanced",
  "The Global Supersonic Network - Advanced",
  "Everyday Supersonic - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — supersonic passenger travel record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A supersonic passenger travel record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-64-supersonic-passenger-travel-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-64-supersonic-passenger-travel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-64-supersonic-passenger-travel',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
