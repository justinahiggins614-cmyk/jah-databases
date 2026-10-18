(function(){'use strict';
/* JAH The Smart Everyday Tool Database — real working generator, jahdb-db-smart-everyday-tool-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SETS-";
var SLUG="db-smart-everyday-tool";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Smart Tape Measure", "tier": "Foundations", "concept": "measure + math", "mechanism": "digital + app log", "parts": ["tape"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "tool: log beats memory"},
  {"kind": "gm", "t": "Connected Stud Finder", "tier": "Foundations", "concept": "find + mark", "mechanism": "deep scan + edge display", "parts": ["finder"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "tool: mark both edges"},
  {"kind": "gm", "t": "Smart Level", "tier": "Foundations", "concept": "level + record", "mechanism": "digital angle + photo", "parts": ["level"], "build": "build", "time": "6h", "level": "beginner", "safety": "none", "notes": "tool: photo the reading"},
  {"kind": "gm", "t": "Inventory Pen", "tier": "Foundations", "concept": "counting stock", "mechanism": "scan + tally pen", "parts": ["pen"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "tool: beep confirms"},
  {"kind": "gm", "t": "Smart Highlighter", "tier": "Foundations", "concept": "study + digitize", "mechanism": "scan highlights to notes", "parts": ["highlighter"], "build": "build", "time": "12h", "level": "beginner", "safety": "none", "notes": "tool: OCR the highlights"},
  {"kind": "gm", "t": "Posture Trainer", "tier": "Foundations", "concept": "slouch all day", "mechanism": "vibration reminder clip", "parts": ["clip"], "build": "build", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "tool: gentle buzz, not nag"},
  {"kind": "gm", "t": "Smart Water Bottle", "tier": "Foundations", "concept": "drink more", "mechanism": "glows when behind", "parts": ["bottle"], "build": "build", "time": "6h", "level": "beginner", "safety": "none", "notes": "tool: goal by weight, not time"},
  {"kind": "gm", "t": "Medication Reminder Cap", "tier": "Foundations", "concept": "missed doses", "mechanism": "cap counts + reminds", "parts": ["cap"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "tool: the cap knows"},
  {"kind": "gm", "t": "Smart Luggage Tag", "tier": "Foundations", "concept": "lost bags", "mechanism": "GPS + e-ink tag", "parts": ["tag"], "build": "build", "time": "10h", "level": "beginner", "safety": "none", "notes": "tool: airline-readable"},
  {"kind": "gm", "t": "Key Finder (Mesh)", "tier": "Foundations", "concept": "lost keys", "mechanism": "mesh network ping", "parts": ["fob"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "tool: community find"},
  {"kind": "gm", "t": "Smart Umbrella", "tier": "Foundations", "concept": "left behind", "mechanism": "phone alert when separated", "parts": ["umbrella"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "tool: rain forecast nudge"},
  {"kind": "gm", "t": "Connected Multimeter", "tier": "Compounded", "concept": "measure + log", "mechanism": "bluetooth readings to phone", "parts": ["meter"], "build": "build", "time": "12h", "level": "intermediate", "safety": "electrical safety", "notes": "tool: log the troubleshooting"},
  {"kind": "gm", "t": "Smart Torque Wrench", "tier": "Compounded", "concept": "tight enough?", "mechanism": "click + digital readout", "parts": ["wrench"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "tool: spec, not feel"},
  {"kind": "gm", "t": "Thermal Leak Detector", "tier": "Compounded", "concept": "drafts hide", "mechanism": "IR + phone overlay", "parts": ["camera"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "tool: scan on cold mornings"},
  {"kind": "gm", "t": "Smart Smoke + CO", "tier": "Compounded", "concept": "alarms ignored", "mechanism": "voice alerts + phone", "parts": ["detector"], "build": "install", "time": "4h", "level": "intermediate", "safety": "none", "notes": "tool: 10-year battery"},
  {"kind": "gm", "t": "Water Leak Sensor", "tier": "Compounded", "concept": "leaks destroy", "mechanism": "puck sensors + shutoff", "parts": ["sensor"], "build": "install", "time": "6h", "level": "intermediate", "safety": "none", "notes": "tool: under every sink"},
  {"kind": "gm", "t": "Smart Doorbell", "tier": "Compounded", "concept": "missed knocks", "mechanism": "camera + motion + talk", "parts": ["doorbell"], "build": "install", "time": "6h", "level": "intermediate", "safety": "low-voltage", "notes": "tool: answer from anywhere"},
  {"kind": "gm", "t": "Air Quality Monitor", "tier": "Compounded", "concept": "air invisible", "mechanism": "PM/VOC/CO2 + advice", "parts": ["monitor"], "build": "build", "time": "12h", "level": "intermediate", "safety": "low-voltage", "notes": "tool: act on the numbers"},
  {"kind": "gm", "t": "Smart Sprinkler", "tier": "Compounded", "concept": "water waste", "mechanism": "weather + soil sensing", "parts": ["controller"], "build": "install", "time": "8h", "level": "intermediate", "safety": "none", "notes": "tool: skip after rain"},
  {"kind": "gm", "t": "Energy Monitor (Home)", "tier": "Compounded", "concept": "bills mystery", "mechanism": "clamp meter + app", "parts": ["monitor"], "build": "install", "time": "8h", "level": "intermediate", "safety": "electrical — pro", "notes": "tool: find the hogs"},
  {"kind": "gm", "t": "Smart Lock", "tier": "Compounded", "concept": "keys hassle", "mechanism": "code + phone + auto-lock", "parts": ["lock"], "build": "install", "time": "4h", "level": "intermediate", "safety": "none", "notes": "tool: codes per person"},
  {"kind": "gm", "t": "Pet Feeder (Smart)", "tier": "Compounded", "concept": "feeding schedule", "mechanism": "camera + portion control", "parts": ["feeder"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "tool: camera confirms eating"},
  {"kind": "gm", "t": "Smart Garden Sensor", "tier": "Advanced", "concept": "plants guess", "mechanism": "soil + light + advice", "parts": ["sensor"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "tool: water when dry 2in"},
  {"kind": "gm", "t": "Home Hub (Local)", "tier": "Advanced", "concept": "cloud dependence", "mechanism": "local-first automation", "parts": ["hub"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "tool: works offline"},
  {"kind": "gm", "t": "Predictive Maintenance", "tier": "Advanced", "concept": "breakdowns surprise", "mechanism": "vibration + temp trends", "parts": ["sensor"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "tool: trends beat thresholds"},
  {"kind": "gm", "t": "Smart Mirror", "tier": "Advanced", "concept": "info while brushing", "mechanism": "display behind mirror", "parts": ["mirror"], "build": "build", "time": "16h", "level": "advanced", "safety": "low-voltage", "notes": "tool: glanceable only"},
  {"kind": "gm", "t": "Workshop Air Monitor", "tier": "Advanced", "concept": "dust harms", "mechanism": "PM sensing + collector trigger", "parts": ["monitor"], "build": "build", "time": "12h", "level": "advanced", "safety": "dust mask too", "notes": "tool: auto-start collector"},
  {"kind": "gm", "t": "Smart Beehive Monitor", "tier": "Advanced", "concept": "hive health hidden", "mechanism": "weight + temp + sound", "parts": ["monitor"], "build": "install", "time": "12h", "level": "advanced", "safety": "bee safety", "notes": "tool: weight tells most"},
  {"kind": "gm", "t": "Elder Safety System", "tier": "Advanced", "concept": "worry remotely", "mechanism": "motion patterns + alerts", "parts": ["system"], "build": "install", "time": "16h", "level": "advanced", "safety": "none", "notes": "tool: dignity first"},
  {"kind": "gm", "t": "Smart Compost Monitor", "tier": "Advanced", "concept": "compost guesswork", "mechanism": "temp + moisture probes", "parts": ["probes"], "build": "build", "time": "10h", "level": "advanced", "safety": "none", "notes": "tool: 140F = cooking"},
  {"kind": "gm", "t": "Pool Chemistry Automator", "tier": "Advanced", "concept": "pool testing chore", "mechanism": "sensors + dosing", "parts": ["system"], "build": "install", "time": "20h", "level": "advanced", "safety": "chemical safety", "notes": "tool: test manually weekly too"},
  {"kind": "gm", "t": "Whole-Home Water Monitor", "tier": "Advanced", "concept": "leaks + waste", "mechanism": "flow sensing + auto shutoff", "parts": ["monitor"], "build": "install", "time": "12h", "level": "advanced", "safety": "plumbing pro", "notes": "tool: shutoff saves homes"},
  {"kind": "gm", "t": "Smart Workshop Inventory", "tier": "Advanced", "concept": "parts chaos", "mechanism": "bins + scanner + app", "parts": ["system"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "tool: scan on use"},
  {"kind": "gm", "t": "Smart Pill Organizer", "tier": "Advanced", "concept": "never miss", "mechanism": "7-day + alerts", "parts": ["organizer"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "tool: caregiver alerts"}
];
var TIPS=["Prototype the mechanism in cardboard first.", "Test with the cheapest parts that can work.", "Measure current draw before choosing a battery.", "Leave 20% headroom in every rating.", "Document the wiring before closing the case.", "User-test the interaction early."];
function money(n){return "$"+n.toFixed(2);}
function planDiy(tp,rnd){
  var total=0,i;
  for(i=0;i<tp.mats.length;i++)total+=tp.mats[i][2];
  var tip=pick(TIPS,rnd);
  var L=[];
  L.push("COMPLETE PLAN: "+tp.t);
  L.push("");
  L.push("Overview: "+tp.notes+" Estimated hands-on time "+tp.time+" ("+tp.level+" level). Maker tip: "+tip);
  L.push("");
  L.push("Materials ("+tp.mats.length+" items, about "+money(total)+"):");
  for(i=0;i<tp.mats.length;i++)L.push("  - "+tp.mats[i][0]+" ("+tp.mats[i][1]+") ~"+money(tp.mats[i][2]));
  L.push("");
  L.push("Tools: "+(tp.tools.length?tp.tools.join(", "):"basic hand tools"));
  L.push("");
  L.push("Steps:");
  for(i=0;i<tp.steps.length;i++)L.push("  "+(i+1)+". "+tp.steps[i]);
  L.push("");
  L.push("Timeline: split "+tp.time+" into "+(tp.steps.length>6?"three":"two")+" sessions; never rush the final fitting and finish.");
  L.push("Safety: "+tp.safety);
  var hiw="This plan works because each stage prepares the next: measure and cut before joining, join before finishing. "+
    tp.notes+" Work the steps in order, and when a step resists, re-measure rather than forcing it. Safety is part of the method: "+tp.safety+".";
  var kp=["About "+money(total)+" in materials ("+tp.mats.length+" items).",
    "Roughly "+tp.time+" of hands-on work ("+tp.level+" level).",
    "Key technique: "+tp.notes.split(".")[0]+".",
    "Tools: "+(tp.tools.length?tp.tools.slice(0,6).join(", "):"basic hand tools")+".",
    "Safety: "+tp.safety+".",
    "Maker tip: "+tip];
  var req=["Materials: "+tp.mats.map(function(m){return m[0]+" ("+m[1]+")";}).join("; "),
    "Tools: "+(tp.tools.length?tp.tools.join(", "):"basic hand tools"),
    "Safety gear: "+tp.safety];
  return {description:L.join("\n"),how_it_works:hiw,key_points:kp,requirements:req};
}
function planGm(tp,rnd){
  var tip=pick(TIPS,rnd);
  var L=[];
  L.push("COMPLETE CONCEPT PLAN: "+tp.t);
  L.push("");
  L.push("Concept: "+tp.concept);
  L.push("");
  L.push("Mechanism: "+tp.mechanism);
  L.push("");
  L.push("Parts: "+tp.parts.join(", "));
  L.push("");
  L.push("Validation path: "+tp.build+" Expect about "+tp.time+" of work at "+tp.level+" level. Maker tip: "+tip);
  L.push("Safety: "+tp.safety);
  var hiw="The mechanism is the heart of it: "+tp.mechanism+" Prototype the core interaction first — "+
    "mock up the mechanics in cardboard, breadboard any electronics, and test before enclosing. "+tp.build+" Safety: "+tp.safety+".";
  var kp=["Core mechanism: "+tp.mechanism+".",
    "Key parts: "+tp.parts.slice(0,6).join(", ")+".",
    "About "+tp.time+" of work ("+tp.level+" level).",
    "Prototype the mechanism before the enclosure.",
    "Safety: "+tp.safety+".",
    "Maker tip: "+tip];
  var req=["Parts: "+tp.parts.join(", "),
    "Validation: "+tp.build,
    "Safety: "+tp.safety];
  return {description:L.join("\n"),how_it_works:hiw,key_points:kp,requirements:req};
}
function demoProgram(tp){
  var L=[];
  L.push("#!/usr/bin/env python3");
  L.push('"""'+String(tp.t).replace(/"/g,"'")+' — generated plan demo.');
  L.push("Property of Justin Addam Higgins (JAH).");
  L.push('"""');
  if(tp.kind==="diy"){
    L.push("MATS="+JSON.stringify(tp.mats.map(function(m){return [m[0],m[2]];})));
    L.push("def main():");
    L.push("    total=sum(c for _,c in MATS)");
    L.push('    print("Plan: '+String(tp.t).replace(/"/g,"'")+'")');
    L.push('    for n,c in MATS: print("  %-28s $%6.2f" % (n[:28],c))');
    L.push('    print("  %-28s $%6.2f" % ("TOTAL", total))');
    L.push('    print("OK: plan materials total $%.2f" % total)');
  }else{
    L.push("PARTS="+JSON.stringify(tp.parts));
    L.push("def main():");
    L.push('    print("Concept: '+String(tp.t).replace(/"/g,"'")+'")');
    L.push('    print("Parts (%d):" % len(PARTS))');
    L.push('    for p in PARTS: print("  - "+p)');
    L.push('    print("OK: %d parts listed" % len(PARTS))');
  }
  L.push('if __name__=="__main__": main()');
  return L.join("\n");
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var pool=BANK.filter(function(b){return !opts.field||b.tier===opts.field;});
  if(!pool.length)pool=BANK;
  var tp=(typeof opts.topicIndex==="number"&&BANK[opts.topicIndex])?BANK[opts.topicIndex]:pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,"0");
  var plan=tp.kind==="gm"?planGm(tp,rnd):planDiy(tp,rnd);
  var suf=" (Signature Edition)";
  return {
    id:id,t:tp.t+suf,g:tp.tier,name:tp.t+suf,title:tp.t+suf,
    description:"SAMPLE RECORD (generated — clearly labeled sample, not an archive record).\n\n"+plan.description,
    how_it_works:plan.how_it_works,
    key_points:plan.key_points,requirements:plan.requirements,
    standards:STANDARDS,citations:CITATIONS,
    src:"signature-generated-sample",sample:true,
    disclaimer:"Generated sample record — not an archive record. Seeded archive records are the authoritative entries.",
    ladder_tier:tp.tier,
    demo:{kind:"python",language:"python",program:demoProgram(tp),note:"Working demonstration program generated with this plan."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.src)e.push("src");
  if(!r.demo||!r.demo.program)e.push("demo");
  var d=String(r.description||"");
  if(d.indexOf("Materials")<0&&d.indexOf("Parts")<0)e.push("plan-materials");
  if(d.indexOf("Steps")<0&&d.indexOf("Validation")<0)e.push("plan-steps");
  if(d.indexOf("Safety")<0)e.push("plan-safety");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.g===record.g;});
  return dups.length?{ok:false,errors:["duplicate title+tier in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-"+SLUG+"-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();

