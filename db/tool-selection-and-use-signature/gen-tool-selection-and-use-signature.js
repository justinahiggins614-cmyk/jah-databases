(function(){'use strict';
/* JAH Tool Selection and Use Database generator — jahdb-tool-selection-and-use-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TOOLSAUS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Starter Toolbox (Signature Edition)", "Tape Measures and Measuring (Signature Edition)", "Hammers and Striking (Signature Edition)", "Screwdriver Selection (Signature Edition)", "Pliers and Gripping Tools (Signature Edition)", "Levels and Plumb (Signature Edition)", "Utility Knives (Signature Edition)", "Cordless Drills (Signature Edition)", "Drill Bits (Signature Edition)", "Saws: Handsaws (Signature Edition)", "Circular Saws (Signature Edition)"], "Compounded": ["Jigsaws (Signature Edition)", " Sanders (Signature Edition)", "Wrenches and Sockets (Signature Edition)", "Clamps (Signature Edition)", "Stud Finders (Signature Edition)", "Safety Glasses and Gear (Signature Edition)", "Ladders (Signature Edition)", "Multimeters (Signature Edition)", "Caulk Guns (Signature Edition)", "Painting Tools (Signature Edition)", "Tool Storage Systems (Signature Edition)", "Sharpening Basics (Signature Edition)"], "Advanced": ["Air Tools and Compressors (Signature Edition)", "Rotary Tools (Signature Edition)", "Oscillating Multi-Tools (Signature Edition)", "Shop Vacuums and Dust (Signature Edition)", "Workbenches (Signature Edition)", "Measuring Advanced: Squares (Signature Edition)", "Fastener Selection (Signature Edition)", "Adhesives and Glues (Signature Edition)", "Borrowing and Renting (Signature Edition)", "Tool Maintenance Calendar (Signature Edition)", "Teaching Tool Skills (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — tool guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — tool guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tool guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tool-selection-and-use-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-tool-selection-and-use-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("tool-selection-and-use-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
