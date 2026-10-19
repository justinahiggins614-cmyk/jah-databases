(function(){'use strict';
/* JAH Foundation and Structural Warning Signs Database generator — jahdb-foundation-and-structural-warning-signs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FOUNASWS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Hairline Cracks in Foundation Walls (Signature Edition)", "Stair-Step Cracks in Masonry (Signature Edition)", "Horizontal Basement Wall Cracks (Signature Edition)", "Sloping and Uneven Floors (Signature Edition)", "Doors and Windows That Stick (Signature Edition)", "Gaps Between Walls and Ceilings (Signature Edition)", "Water Intrusion Signs (Signature Edition)", "Sagging or Bouncy Floors (Signature Edition)", "Roofline and Ridge Sagging (Signature Edition)", "Chimney Separation (Signature Edition)", "Crack Monitoring Techniques (Signature Edition)"], "Compounded": ["Soil and Grading Problems (Signature Edition)", "Expansive Soils (Signature Edition)", "Tree Root Intrusion (Signature Edition)", "Plumbing Leaks Under Slabs (Signature Edition)", "Termite and Wood-Destroying Insects (Signature Edition)", "Mold as a Structural Indicator (Signature Edition)", "Retaining Wall Distress (Signature Edition)", "Deck and Porch Attachment (Signature Edition)", "Post and Beam Concerns (Signature Edition)", "When to Call an Engineer (Signature Edition)", "Documenting for Insurance (Signature Edition)", "Pre-Purchase Structural Checks (Signature Edition)"], "Advanced": ["Seasonal Structural Rhythms (Signature Edition)", "Foundation Repair Methods (Signature Edition)", "Waterproofing Strategies (Signature Edition)", "Monitoring Schedules (Signature Edition)", "Historic Home Structures (Signature Edition)", "New Construction Settlement (Signature Edition)", "Earthquake and Storm Aftermath (Signature Edition)", "The Structural Logbook (Signature Edition)", "Working With Engineers (Signature Edition)", "Cost Planning for Repairs (Signature Edition)", "Teaching Household Members (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — warning-sign guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — warning-sign guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A warning-sign guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"foundation-and-structural-warning-signs-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-foundation-and-structural-warning-signs-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("foundation-and-structural-warning-signs-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
