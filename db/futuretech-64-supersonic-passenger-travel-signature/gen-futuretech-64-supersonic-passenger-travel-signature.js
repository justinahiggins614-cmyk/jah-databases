(function(){'use strict';
/* JAH The Supersonic Passenger Travel Future Technology Database — Signature Edition generator — jahdb-futuretech-64-supersonic-passenger-travel-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT64-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Supersonic Passenger Travel — Yeager Breaks the Sound Barrier (Signature Edition)", "Supersonic Passenger Travel — the Concorde Treaty (Signature Edition)", "Supersonic Passenger Travel — the Tu-144 Flies First (Signature Edition)", "Supersonic Passenger Travel — Concorde's First Flight (Signature Edition)", "Supersonic Passenger Travel — the Boom Ban (Signature Edition)", "Supersonic Passenger Travel — Concorde Enters Service (Signature Edition)", "Supersonic Passenger Travel — the Tu-144 Carries Passengers (Signature Edition)", "Supersonic Passenger Travel — the Tu-144 Grounded (Signature Edition)", "Supersonic Passenger Travel — Flight 4590 (Signature Edition)", "Supersonic Passenger Travel — Concorde Retires (Signature Edition)", "Supersonic Passenger Travel — Boom - the Comeback Startup (Signature Edition)"], "Compounded": ["Supersonic Passenger Travel — X-59 - the Quiet Supersonic (Signature Edition)", "Supersonic Passenger Travel — XB-1 Rolled Out (Signature Edition)", "Supersonic Passenger Travel — United Orders Supersonic (Signature Edition)", "Supersonic Passenger Travel — Aerion Shuts Down (Signature Edition)", "Supersonic Passenger Travel — American Orders Too (Signature Edition)", "Supersonic Passenger Travel — the Symphony Engine (Signature Edition)", "Supersonic Passenger Travel — XB-1's First Flight (Signature Edition)", "Supersonic Passenger Travel — X-59 Revealed (Signature Edition)", "Supersonic Passenger Travel — the Barrier Falls Again (Signature Edition)", "Supersonic Passenger Travel — Measuring the Thump (Signature Edition)", "Supersonic Passenger Travel — the Ban Under Review (Signature Edition)", "Supersonic Passenger Travel — Building the Overture Factory (Signature Edition)"], "Advanced": ["Supersonic Passenger Travel — the Supersonic Peloton (Signature Edition)", "Supersonic Passenger Travel — Overture Enters Service (Signature Edition)", "Supersonic Passenger Travel — Overland Supersonic Legalized (Signature Edition)", "Supersonic Passenger Travel — Supersonic Business Jets (Signature Edition)", "Supersonic Passenger Travel — Second-Generation Fleets (Signature Edition)", "Supersonic Passenger Travel — Faster Turnarounds (Signature Edition)", "Supersonic Passenger Travel — Affordable Supersonic (Signature Edition)", "Supersonic Passenger Travel — Supersonic Cargo (Signature Edition)", "Supersonic Passenger Travel — Hypersonic Research (Signature Edition)", "Supersonic Passenger Travel — The Global Supersonic Network (Signature Edition)", "Supersonic Passenger Travel — Everyday Supersonic - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Supersonic Passenger Travel study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-64-supersonic-passenger-travel-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-64-supersonic-passenger-travel-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
