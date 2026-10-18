(function(){'use strict';
/* JAH The Rube Goldberg Machine Database — real working generator, jahdb-gen-rube-goldberg-machine-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RGMS-";
var SLUG="gen-rube-goldberg-machine";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Test structures gradually to rated load; keep a clear fall/drop zone during testing.", "Pinch points guarded on moving mechanisms; secure tall builds against tipping."];
var CITATIONS=["Petroski, Henry. 'To Engineer Is Human.' St. Martin's Press, 1985.", "'Marks\\' Standard Handbook for Mechanical Engineers.' McGraw-Hill, 12th ed.", "Walker, Jearl. 'The Flying Circus of Physics.' 2nd ed. Wiley, 2006."];
var BANK=[
  {"kind": "gm", "t": "Domino + Ball", "tier": "Foundations", "concept": "start simple", "mechanism": "domino tips ball", "parts": ["set"], "build": "build", "time": "2h", "level": "beginner", "safety": "none", "notes": "chain: one link, reliable"},
  {"kind": "gm", "t": "Ramp to Bell", "tier": "Foundations", "concept": "roll + ring", "mechanism": "ramp + bell", "parts": ["ramp"], "build": "build", "time": "2h", "level": "beginner", "safety": "choke", "notes": "chain: gravity does work"},
  {"kind": "gm", "t": "Pulley Lift Flag", "tier": "Foundations", "concept": "up + wave", "mechanism": "pulley raises flag", "parts": ["pulley"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "chain: pulleys redirect"},
  {"kind": "gm", "t": "Balloon Pop Dart", "tier": "Foundations", "concept": "pop + start", "mechanism": "dart pops balloon", "parts": ["set"], "build": "build", "time": "2h", "level": "beginner", "safety": "balloon pop", "notes": "chain: stored air energy"},
  {"kind": "gm", "t": "Water Pour Wheel", "tier": "Foundations", "concept": "pour + spin", "mechanism": "water turns wheel", "parts": ["wheel"], "build": "build", "time": "3h", "level": "beginner", "safety": "water", "notes": "chain: flow = motion"},
  {"kind": "gm", "t": "Book Fall Switch", "tier": "Foundations", "concept": "fall + trigger", "mechanism": "book hits switch", "parts": ["book"], "build": "build", "time": "2h", "level": "beginner", "safety": "none", "notes": "chain: weight triggers"},
  {"kind": "gm", "t": "Marble + Mousetrap", "tier": "Foundations", "concept": "snap + launch", "mechanism": "trap hits ball", "parts": ["trap"], "build": "build", "time": "3h", "level": "beginner", "safety": "snap", "notes": "chain: spring energy"},
  {"kind": "gm", "t": "Fan + Sail Car", "tier": "Foundations", "concept": "blow + roll", "mechanism": "fan pushes car", "parts": ["fan"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "chain: air power"},
  {"kind": "gm", "t": "Ice Melt Drip", "tier": "Foundations", "concept": "wait + drip", "mechanism": "ice melts, tips cup", "parts": ["ice"], "build": "build", "time": "4h", "level": "beginner", "safety": "water", "notes": "chain: patience link"},
  {"kind": "gm", "t": "Pendulum Hit", "tier": "Foundations", "concept": "swing + strike", "mechanism": "pendulum hits domino", "parts": ["pendulum"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "chain: period timing"},
  {"kind": "gm", "t": "Lever Catapult", "tier": "Foundations", "concept": "press + fling", "mechanism": "lever launches ball", "parts": ["lever"], "build": "build", "time": "3h", "level": "beginner", "safety": "eye", "notes": "chain: fulcrum placement"},
  {"kind": "gm", "t": "Pulley + Weight Door", "tier": "Compounded", "concept": "drop + open", "mechanism": "weight pulls string", "parts": ["pulley"], "build": "build", "time": "6h", "level": "intermediate", "safety": "drop zone", "notes": "chain: counterweight"},
  {"kind": "gm", "t": "Siphon Trigger", "tier": "Compounded", "concept": "siphon + pour", "mechanism": "siphon fills cup", "parts": ["siphon"], "build": "build", "time": "6h", "level": "intermediate", "safety": "water", "notes": "chain: atmospheric magic"},
  {"kind": "gm", "t": "Chemical Clock Color", "tier": "Compounded", "concept": "wait + change", "mechanism": "iodine clock", "parts": ["kit"], "build": "build", "time": "6h", "level": "intermediate", "safety": "chemical", "notes": "chain: timed chemistry"},
  {"kind": "gm", "t": "Rat Trap Car", "tier": "Compounded", "concept": "snap + race", "mechanism": "trap powers axle", "parts": ["trap"], "build": "build", "time": "8h", "level": "intermediate", "safety": "snap", "notes": "chain: distance tuned"},
  {"kind": "gm", "t": "Electric + Relay", "tier": "Compounded", "concept": "circuit + action", "mechanism": "relay switches motor", "parts": ["circuit"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "chain: electrons link"},
  {"kind": "gm", "t": "Compressed Air Cannon", "tier": "Compounded", "concept": "blast + push", "mechanism": "air + ball", "parts": ["canon"], "build": "build", "time": "8h", "level": "intermediate", "safety": "pressure", "notes": "chain: low pressure only"},
  {"kind": "gm", "t": "Gear Train Timer", "tier": "Compounded", "concept": "slow + release", "mechanism": "gears delay", "parts": ["gears"], "build": "build", "time": "12h", "level": "intermediate", "safety": "pinch", "notes": "chain: ratio = delay"},
  {"kind": "gm", "t": "Water Clock Drip", "tier": "Compounded", "concept": "drip + measure", "mechanism": "calibrated drip", "parts": ["drip"], "build": "build", "time": "8h", "level": "intermediate", "safety": "water", "notes": "chain: flow timing"},
  {"kind": "gm", "t": "Magnetic Release", "tier": "Compounded", "concept": "hold + drop", "mechanism": "electromagnet releases", "parts": ["magnet"], "build": "build", "time": "8h", "level": "intermediate", "safety": "low-voltage", "notes": "chain: clean release"},
  {"kind": "gm", "t": "Spring-Loaded Drawer", "tier": "Compounded", "concept": "pop + push", "mechanism": "spring launches", "parts": ["drawer"], "build": "build", "time": "6h", "level": "intermediate", "safety": "spring", "notes": "chain: latch trigger"},
  {"kind": "gm", "t": "Conveyor Belt Link", "tier": "Compounded", "concept": "carry + drop", "mechanism": "belt moves object", "parts": ["belt"], "build": "build", "time": "12h", "level": "intermediate", "safety": "pinch", "notes": "chain: constant feed"},
  {"kind": "gm", "t": "Multi-Room Chain", "tier": "Advanced", "concept": "house-scale", "mechanism": "links across rooms", "parts": ["house"], "build": "build", "time": "40h", "level": "advanced", "safety": "household", "notes": "chain: test per room"},
  {"kind": "gm", "t": "Toothpaste Squeeze Task", "tier": "Advanced", "concept": "morning link", "mechanism": "chain squeezes tube", "parts": ["machine"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "chain: gentle pressure"},
  {"kind": "gm", "t": "Pet Feeder Chain", "tier": "Advanced", "concept": "feed pet", "mechanism": "chain dispenses", "parts": ["machine"], "build": "build", "time": "30h", "level": "advanced", "safety": "pet safe", "notes": "chain: reliable daily"},
  {"kind": "gm", "t": "Wake-Up Chain", "tier": "Advanced", "concept": "morning routine", "mechanism": "chain starts coffee", "parts": ["machine"], "build": "build", "time": "40h", "level": "advanced", "safety": "hot safety", "notes": "chain: coffee by chain"},
  {"kind": "gm", "t": "100-Step Machine", "tier": "Advanced", "concept": "epic", "mechanism": "100 reliable links", "parts": ["machine"], "build": "build", "time": "100h", "level": "advanced", "safety": "none", "notes": "chain: reliability > cleverness"},
  {"kind": "gm", "t": "Task: Pour Cereal", "tier": "Advanced", "concept": "breakfast machine", "mechanism": "chain pours bowl", "parts": ["machine"], "build": "build", "time": "40h", "level": "advanced", "safety": "food safety", "notes": "chain: the classic task"},
  {"kind": "gm", "t": "Task: Water Plant", "tier": "Advanced", "concept": "plant care", "mechanism": "chain waters", "parts": ["machine"], "build": "build", "time": "30h", "level": "advanced", "safety": "water", "notes": "chain: gentle pour"},
  {"kind": "gm", "t": "Task: Turn Page", "tier": "Advanced", "concept": "read link", "mechanism": "chain turns page", "parts": ["machine"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "chain: delicate touch"},
  {"kind": "gm", "t": "Competition Machine", "tier": "Advanced", "concept": "contest ready", "mechanism": "rules + reliability", "parts": ["machine"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "chain: document energy transfers"},
  {"kind": "gm", "t": "Museum Chain", "tier": "Advanced", "concept": "public + durable", "mechanism": "robust links", "parts": ["install"], "build": "build", "time": "100h", "level": "advanced", "safety": "pro", "notes": "chain: 10,000 cycles"},
  {"kind": "gm", "t": "Teaching Energy", "tier": "Advanced", "concept": "physics live", "mechanism": "curriculum + machine", "parts": ["class"], "build": "plan", "time": "30h", "level": "advanced", "safety": "none", "notes": "chain: label each transfer"},
  {"kind": "gm", "t": "Master Chain Builder", "tier": "Advanced", "concept": "the craft", "mechanism": "portfolio + film", "parts": ["portfolio"], "build": "make", "time": "60h", "level": "advanced", "safety": "none", "notes": "chain: film every link"}
];
var TIPS=["Build one stage and test it before connecting the next.", "Time the real machine and tune to the math.", "Guard every pinch point before demonstrating.", "Level the base before trusting the tower.", "Keep a build log with measurements.", "Test to failure on purpose \u2014 once."];
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

