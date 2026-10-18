(function(){'use strict';
/* JAH The Weirdest Vehicles Signature Database generator — jahdb-db-weirdest-vehicles-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WDVHS-";
var FIELDS=["Weird Vehicle Foundations", "The Weird Fleet", "Weird Vehicle Mastery"];
var TOPICS={"Weird Vehicle Foundations": ["Why Weird Matters", "Reading Weird Design", "The Three-Wheeler World", "Amphibious Oddities", "Microcar Madness", "The Jet Age Cars", "Steam and Alternative Power", "Weird Military Machines", "Concept Car Craziness", "Failed Production Cars", "The Weird Community"], "The Weird Fleet": ["The Peel P50", "The Amphicar", "The BMW Isetta", "The DeLorean DMC-12", "The Tucker 48", "The Edsel", "The Reliant Robin", "The Oscar Mayer Wienermobile", "The Gibbs Aquada", "The Rinspeed Oddities", "The Peel Trident", "The Modern Weird"], "Weird Vehicle Mastery": ["The Philosophy of Weird", "Collecting Oddities", "Restoring the Strange", "Weird Vehicle Events", "Documenting Weirdness", "Designing the Next Weird", "Teaching Weird Appreciation", "The Museum of Odd", "Weird as Inspiration", "The Joy of Weird", "The Weird Legacy"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# minibot — "+safe+"\n"
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
    name:topic+' — weird vehicle record',
    title:topic,
    description:"SAMPLE RECORD (generated — structural Signature sample). A Signature-original weird vehicle record sample of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated Signature sample record — not an archive record. Seeded Signature records are the authoritative entries.',
    demo:{kind:"topic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-db-weirdest-vehicles-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-weirdest-vehicles-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
