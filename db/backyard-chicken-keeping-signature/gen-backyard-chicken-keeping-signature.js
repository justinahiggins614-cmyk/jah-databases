(function(){'use strict';
/* JAH Backyard Chicken Keeping Database generator — jahdb-backyard-chicken-keeping-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BACKCKS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Legal Check (Signature Edition)", "Choosing Breeds (Signature Edition)", "Coop Design (Signature Edition)", "Predator Proofing (Signature Edition)", "Feeding (Signature Edition)", "Water Systems (Signature Edition)", "Egg Collection (Signature Edition)", "Health Basics (Signature Edition)", "Parasites (Signature Edition)", "Winter Care (Signature Edition)", "Summer Care (Signature Edition)"], "Compounded": ["Introducing New Birds (Signature Edition)", "Broody Hens (Signature Edition)", "Molting (Signature Edition)", "End of Laying (Signature Edition)", "Teaching Chicken Keeping (Signature Edition)", "The Annual Flock Review (Signature Edition)", "Chickens and Gardens (Signature Edition)", "Chicken Math (Signature Edition)", "Noise Management (Signature Edition)", "Vacation Care (Signature Edition)", "Record Keeping (Signature Edition)", "Biosecurity (Signature Edition)"], "Advanced": ["Selling Eggs (Signature Edition)", "Meat Birds (Signature Edition)", "Ducks (Signature Edition)", "Quail (Signature Edition)", "Chicken Tractors (Signature Edition)", "Deep Litter Method (Signature Edition)", "Fermented Feed (Signature Edition)", "Sprouted Fodder (Signature Edition)", "Predator Identification (Signature Edition)", "First Aid Kit (Signature Edition)", "Community Flocks (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — poultry guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — poultry guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A poultry guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"backyard-chicken-keeping-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-backyard-chicken-keeping-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("backyard-chicken-keeping-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
