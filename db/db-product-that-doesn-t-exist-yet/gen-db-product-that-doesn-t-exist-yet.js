(function(){'use strict';
/* JAH The Product That Doesn't Exist Yet Database — real working generator, jahdb-db-product-that-doesn-t-exist-yet-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PTDTEY-";
var SLUG="db-product-that-doesn-t-exist-yet";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Laundry-Folding Robot (Home)", "tier": "Foundations", "concept": "folding eats Sundays", "mechanism": "vision + soft grippers fold standard loads", "parts": ["arms", "camera"], "build": "prototype", "time": "40h", "level": "beginner", "safety": "none", "notes": "concept: start with t-shirts only"},
  {"kind": "gm", "t": "Self-Cleaning Water Bottle", "tier": "Foundations", "concept": "bottles grow grime", "mechanism": "UV-C cap sterilizes in 60 seconds", "parts": ["LED", "cap"], "build": "build", "time": "8h", "level": "beginner", "safety": "UV safety — sealed only", "notes": "concept: cap does the work"},
  {"kind": "gm", "t": "The Universal Remote (True)", "tier": "Foundations", "concept": "5 remotes, 0 patience", "mechanism": "one remote learns any IR + IP device", "parts": ["remote"], "build": "program", "time": "6h", "level": "beginner", "safety": "none", "notes": "concept: setup must be 5 minutes"},
  {"kind": "gm", "t": "Mood-Reading Night Light", "tier": "Foundations", "concept": "kids fear dark", "mechanism": "warm dim + stories, no blue light", "parts": ["lamp"], "build": "build", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "concept: light as comfort"},
  {"kind": "gm", "t": "The Perfect Travel Pillow", "tier": "Foundations", "concept": "necks suffer flights", "mechanism": "inflatable + chin support hybrid", "parts": ["fabric", "valve"], "build": "sew", "time": "8h", "level": "beginner", "safety": "none", "notes": "concept: chin support is the missing piece"},
  {"kind": "gm", "t": "Smart Plant Pot", "tier": "Foundations", "concept": "plants die silently", "mechanism": "moisture + light sensing, water reminder", "parts": ["sensor", "pot"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "concept: the pot talks first"},
  {"kind": "gm", "t": "The Quiet Blender", "tier": "Foundations", "concept": "blenders wake houses", "mechanism": "sound-damped enclosure + slow start", "parts": ["enclosure"], "build": "build", "time": "10h", "level": "beginner", "safety": "none", "notes": "concept: enclosure, not quieter motor"},
  {"kind": "gm", "t": "Lost-Key Finder (No Phone)", "tier": "Foundations", "concept": "keys vanish", "mechanism": "dedicated finder fob with direction", "parts": ["fob"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "concept: no app required"},
  {"kind": "gm", "t": "The Honest Alarm", "tier": "Foundations", "concept": "snooze ruins mornings", "mechanism": "walks-away-to-silence design", "parts": ["clock"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "concept: commitment device"},
  {"kind": "gm", "t": "Self-Stirring Pot", "tier": "Foundations", "concept": "sauces stick", "mechanism": "heat-safe stirrer + timer", "parts": ["motor"], "build": "build", "time": "10h", "level": "beginner", "safety": "food-safe materials", "notes": "concept: stir the boring parts"},
  {"kind": "gm", "t": "The Package Porch Box", "tier": "Foundations", "concept": "porch pirates", "mechanism": "lockable drop box with delivery code", "parts": ["box", "lock"], "build": "build", "time": "12h", "level": "beginner", "safety": "none", "notes": "concept: the mailbox, bigger"},
  {"kind": "gm", "t": "AR Measuring Tape", "tier": "Compounded", "concept": "measuring alone is hard", "mechanism": "phone AR + laser spot check", "parts": ["phone", "laser"], "build": "build", "time": "16h", "level": "intermediate", "safety": "laser safety", "notes": "concept: measure rooms solo"},
  {"kind": "gm", "t": "The Compost Countertop Unit", "tier": "Compounded", "concept": "compost smells", "mechanism": "sealed + carbon filter + grind", "parts": ["unit"], "build": "build", "time": "20h", "level": "intermediate", "safety": "none", "notes": "concept: apartment compost without ick"},
  {"kind": "gm", "t": "Sleep-Tracking Pillow", "tier": "Compounded", "concept": "trackers annoy wrists", "mechanism": "pillow sensors read sleep unobtrusively", "parts": ["sensors"], "build": "build", "time": "20h", "level": "intermediate", "safety": "low-voltage", "notes": "concept: track without wearing"},
  {"kind": "gm", "t": "The Honest Fridge", "tier": "Compounded", "concept": "food rots unseen", "mechanism": "camera inventory + expiry alerts", "parts": ["camera"], "build": "build", "time": "20h", "level": "intermediate", "safety": "none", "notes": "concept: the fridge keeps the list"},
  {"kind": "gm", "t": "Modular E-Bike Battery", "tier": "Compounded", "concept": "e-bike range anxiety", "mechanism": "swappable standard packs at cafes", "parts": ["battery"], "build": "design", "time": "30h", "level": "intermediate", "safety": "battery safety", "notes": "concept: infrastructure, not bigger battery"},
  {"kind": "gm", "t": "The Silent Keyboard (True)", "tier": "Compounded", "concept": "keyboards clack", "mechanism": "membrane + dampened switches silent", "parts": ["switches"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "concept: silence without mush"},
  {"kind": "gm", "t": "Home Air-Quality Dashboard", "tier": "Compounded", "concept": "air is invisible", "mechanism": "CO2/PM/VOC sensing + advice", "parts": ["sensors"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "concept: see the air, change habits"},
  {"kind": "gm", "t": "The Perfect Backpack (AI-Fit)", "tier": "Compounded", "concept": "packs fit poorly", "mechanism": "scan + adjustable frame custom", "parts": ["frame"], "build": "build", "time": "24h", "level": "intermediate", "safety": "none", "notes": "concept: fit like shoes"},
  {"kind": "gm", "t": "Elder Check-In Lamp", "tier": "Compounded", "concept": "worry about aging parents", "mechanism": "lamp use patterns signal okay", "parts": ["lamp"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "concept: dignity-preserving monitoring"},
  {"kind": "gm", "t": "The Garden Robot (Weeder)", "tier": "Compounded", "concept": "weeding breaks backs", "mechanism": "vision weeder for home beds", "parts": ["robot"], "build": "build", "time": "40h", "level": "intermediate", "safety": "blade safety", "notes": "concept: start with one bed"},
  {"kind": "gm", "t": "Universal Charger (True)", "tier": "Compounded", "concept": "drawer of dead chargers", "mechanism": "GaN multi-tip + cable built in", "parts": ["charger"], "build": "build", "time": "12h", "level": "intermediate", "safety": "mains — pro", "notes": "concept: one charger to end chargers"},
  {"kind": "gm", "t": "The Honest Scale", "tier": "Advanced", "concept": "scales shame", "mechanism": "trend-only display, no daily number", "parts": ["scale"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "concept: measure trends, not days"},
  {"kind": "gm", "t": "Home Micro-Factory", "tier": "Advanced", "concept": "making needs factories", "mechanism": "desktop CNC + printer + assembly cell", "parts": ["machines"], "build": "build", "time": "100h", "level": "advanced", "safety": "machine safety", "notes": "concept: the garage fab lab"},
  {"kind": "gm", "t": "The Empathy Speaker", "tier": "Advanced", "concept": "calls feel cold", "mechanism": "voice + presence simulation for elders", "parts": ["speaker"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "concept: presence over features"},
  {"kind": "gm", "t": "Personal Air Taxi (Concept)", "tier": "Advanced", "concept": "traffic wastes life", "mechanism": "eVTOL for 50-mile hops", "parts": ["aircraft"], "build": "study", "time": "100h", "level": "advanced", "safety": "aviation regs", "notes": "concept: the hard part is certification"},
  {"kind": "gm", "t": "The Memory Prosthetic", "tier": "Advanced", "concept": "memories fade", "mechanism": "lifelog + recall assistant", "parts": ["device"], "build": "design", "time": "80h", "level": "advanced", "safety": "privacy", "notes": "concept: recall, not record"},
  {"kind": "gm", "t": "Ocean Cleanup Drone", "tier": "Advanced", "concept": "oceans fill with plastic", "mechanism": "autonomous skimmer fleets", "parts": ["drones"], "build": "build", "time": "100h", "level": "advanced", "safety": "marine safety", "notes": "concept: scale is the product"},
  {"kind": "gm", "t": "The Universal Translator (True)", "tier": "Advanced", "concept": "language divides", "mechanism": "real-time earbud translation", "parts": ["earbuds"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "concept: latency under 1s or bust"},
  {"kind": "gm", "t": "Home Fusion (Dream)", "tier": "Advanced", "concept": "energy bills forever", "mechanism": "tabletop fusion (don't)", "parts": ["physics"], "build": "study", "time": "100h", "level": "advanced", "safety": "none", "notes": "concept: honestly labeled impossible — for now"},
  {"kind": "gm", "t": "The Honest News Filter", "tier": "Advanced", "concept": "news overwhelms", "mechanism": "personal relevance + source diversity", "parts": ["software"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "concept: calm over engagement"},
  {"kind": "gm", "t": "Asteroid Mining Rig", "tier": "Advanced", "concept": "Earth resources finite", "mechanism": "autonomous prospect + return", "parts": ["spacecraft"], "build": "study", "time": "100h", "level": "advanced", "safety": "space law", "notes": "concept: economics first, rockets second"},
  {"kind": "gm", "t": "The Empathy Machine (VR)", "tier": "Advanced", "concept": "perspective is hard", "mechanism": "embodied VR perspective experiences", "parts": ["VR"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "concept: walk a mile, literally"},
  {"kind": "gm", "t": "The Honest Label Printer", "tier": "Advanced", "concept": "label everything", "mechanism": "phone + thermal", "parts": ["printer"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "concept: organization as product"}
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
  var suf="";
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

