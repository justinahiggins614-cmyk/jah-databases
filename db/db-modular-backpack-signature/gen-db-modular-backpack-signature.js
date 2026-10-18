(function(){'use strict';
/* JAH The Modular Backpack Database — real working generator, jahdb-db-modular-backpack-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDBKS-";
var SLUG="db-modular-backpack";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Daypack (20L)", "tier": "Foundations", "concept": "daily needs", "mechanism": "20L + laptop sleeve", "parts": ["pack"], "build": "sew", "time": "12h", "level": "beginner", "safety": "none", "notes": "pack: the baseline"},
  {"kind": "gm", "t": "Packing Cubes", "tier": "Foundations", "concept": "chaos inside", "mechanism": "cubes categorize", "parts": ["cubes"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "pack: outfit cubes"},
  {"kind": "gm", "t": "Hip Belt Pocket", "tier": "Foundations", "concept": "phone access", "mechanism": "zip pocket on belt", "parts": ["pocket"], "build": "sew", "time": "3h", "level": "beginner", "safety": "none", "notes": "pack: phone + snacks"},
  {"kind": "gm", "t": "Lid/Brain Pocket", "tier": "Foundations", "concept": "quick access", "mechanism": "top lid pocket", "parts": ["lid"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "pack: rain shell lives here"},
  {"kind": "gm", "t": "Side Pockets", "tier": "Foundations", "concept": "bottles roll", "mechanism": "stretch mesh sides", "parts": ["pockets"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "pack: 1L bottles"},
  {"kind": "gm", "t": "Compression Straps", "tier": "Foundations", "concept": "loads shift", "mechanism": "straps stabilize", "parts": ["straps"], "build": "sew", "time": "3h", "level": "beginner", "safety": "none", "notes": "pack: cinch the load"},
  {"kind": "gm", "t": "Sternum Strap", "tier": "Foundations", "concept": "straps slip", "mechanism": "chest strap anchors", "parts": ["strap"], "build": "fit", "time": "1h", "level": "beginner", "safety": "none", "notes": "pack: at collarbone"},
  {"kind": "gm", "t": "Rain Cover", "tier": "Foundations", "concept": "rain soaks", "mechanism": "cover + dry bags", "parts": ["cover"], "build": "sew", "time": "3h", "level": "beginner", "safety": "none", "notes": "pack: line with trash compactor bag"},
  {"kind": "gm", "t": "Hydration Sleeve", "tier": "Foundations", "concept": "drink more", "mechanism": "bladder + hose port", "parts": ["sleeve"], "build": "sew", "time": "3h", "level": "beginner", "safety": "none", "notes": "pack: clean bladder monthly"},
  {"kind": "gm", "t": "Laptop Sleeve", "tier": "Foundations", "concept": "laptops bruise", "mechanism": "suspended padded sleeve", "parts": ["sleeve"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "pack: never on bottom"},
  {"kind": "gm", "t": "Camera Insert", "tier": "Foundations", "concept": "cameras bounce", "mechanism": "padded dividers", "parts": ["insert"], "build": "sew", "time": "6h", "level": "beginner", "safety": "none", "notes": "pack: dividers by kit"},
  {"kind": "gm", "t": "Frameless Ultralight", "tier": "Compounded", "concept": "weight matters", "mechanism": "frameless 40L, <1lb", "parts": ["pack"], "build": "sew", "time": "16h", "level": "intermediate", "safety": "none", "notes": "pack: base weight <10lb only"},
  {"kind": "gm", "t": "External Frame (Classic)", "tier": "Compounded", "concept": "heavy loads", "mechanism": "frame carries weight", "parts": ["frame"], "build": "build", "time": "20h", "level": "intermediate", "safety": "none", "notes": "pack: 50lb+ comfortably"},
  {"kind": "gm", "t": "Internal Frame", "tier": "Compounded", "concept": "trails need balance", "mechanism": "stays + hipbelt transfer", "parts": ["pack"], "build": "sew", "time": "24h", "level": "intermediate", "safety": "none", "notes": "pack: 80% on hips"},
  {"kind": "gm", "t": "Roll-Top Closure", "tier": "Compounded", "concept": "weather + volume", "mechanism": "roll seals dry", "parts": ["pack"], "build": "sew", "time": "14h", "level": "intermediate", "safety": "none", "notes": "pack: 3 rolls minimum"},
  {"kind": "gm", "t": "Front Panel Load", "tier": "Compounded", "concept": "access matters", "mechanism": "full zip panel", "parts": ["pack"], "build": "sew", "time": "16h", "level": "intermediate", "safety": "none", "notes": "pack: suitcase style"},
  {"kind": "gm", "t": "Detachable Daypack", "tier": "Compounded", "concept": "basecamp days", "mechanism": "lid becomes pack", "parts": ["lid"], "build": "sew", "time": "10h", "level": "intermediate", "safety": "none", "notes": "pack: summit sans base"},
  {"kind": "gm", "t": "Camera Backpack", "tier": "Compounded", "concept": "gear + hike", "mechanism": "back access + ICU", "parts": ["pack"], "build": "sew", "time": "20h", "level": "intermediate", "safety": "none", "notes": "pack: never set down in dirt"},
  {"kind": "gm", "t": "Climbing Pack", "tier": "Compounded", "concept": "rock needs slim", "mechanism": "stripped + gear loops", "parts": ["pack"], "build": "sew", "time": "16h", "level": "intermediate", "safety": "none", "notes": "pack: rope strap top"},
  {"kind": "gm", "t": "Ski Pack", "tier": "Compounded", "concept": "snow needs carry", "mechanism": "diagonal + A-frame", "parts": ["pack"], "build": "sew", "time": "16h", "level": "intermediate", "safety": "avalanche gear", "notes": "pack: avy tools in dedicated pocket"},
  {"kind": "gm", "t": "Travel Backpack", "tier": "Compounded", "concept": "one bag travel", "mechanism": "40L + lockable zips", "parts": ["pack"], "build": "sew", "time": "20h", "level": "intermediate", "safety": "none", "notes": "pack: carry-on legal"},
  {"kind": "gm", "t": "Kids Pack", "tier": "Compounded", "concept": "kids carry too", "mechanism": "fit torso + light", "parts": ["pack"], "build": "sew", "time": "10h", "level": "intermediate", "safety": "none", "notes": "pack: <10% body weight"},
  {"kind": "gm", "t": "Convertible (Backpack+Duffel)", "tier": "Compounded", "concept": "carry vs haul", "mechanism": "straps hide", "parts": ["pack"], "build": "sew", "time": "18h", "level": "intermediate", "safety": "none", "notes": "pack: back panel hides"},
  {"kind": "gm", "t": "Expedition Pack (100L)", "tier": "Advanced", "concept": "expeditions haul", "mechanism": "100L + expedition frame", "parts": ["pack"], "build": "sew", "time": "40h", "level": "advanced", "safety": "none", "notes": "pack: train with weight"},
  {"kind": "gm", "t": "Packraft Pack", "tier": "Advanced", "concept": "paddle + hike", "mechanism": "pack holds raft", "parts": ["pack"], "build": "sew", "time": "24h", "level": "advanced", "safety": "water safety", "notes": "pack: raft on top"},
  {"kind": "gm", "t": "Camera Expedition", "tier": "Advanced", "concept": "pro in wild", "mechanism": "custom dividers + frame", "parts": ["pack"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "pack: insurance for gear"},
  {"kind": "gm", "t": "Military-Style Ruck", "tier": "Advanced", "concept": "rucking fitness", "mechanism": "frame + weight plates", "parts": ["ruck"], "build": "build", "time": "20h", "level": "advanced", "safety": "start light", "notes": "pack: 10% rule"},
  {"kind": "gm", "t": "Bikepacking Bags", "tier": "Advanced", "concept": "bikes carry", "mechanism": "frame + seat + bar bags", "parts": ["bags"], "build": "sew", "time": "24h", "level": "advanced", "safety": "none", "notes": "pack: weight low + centered"},
  {"kind": "gm", "t": "Canyoneering Pack", "tier": "Advanced", "concept": "water + rock", "mechanism": "drain + drag proof", "parts": ["pack"], "build": "sew", "time": "20h", "level": "advanced", "safety": "canyoneering training", "notes": "pack: drains fast"},
  {"kind": "gm", "t": "Photography Roller", "tier": "Advanced", "concept": "airports + gear", "mechanism": "roller + backpack hybrid", "parts": ["roller"], "build": "build", "time": "24h", "level": "advanced", "safety": "none", "notes": "pack: carry-on dims"},
  {"kind": "gm", "t": "Adaptive Pack", "tier": "Advanced", "concept": "mobility needs", "mechanism": "custom access design", "parts": ["pack"], "build": "design", "time": "30h", "level": "advanced", "safety": "co-design", "notes": "pack: user leads design"},
  {"kind": "gm", "t": "Myog Master Pack", "tier": "Advanced", "concept": "dream pack", "mechanism": "full custom build", "parts": ["pack"], "build": "sew", "time": "50h", "level": "advanced", "safety": "none", "notes": "pack: pattern, prototype, perfect"},
  {"kind": "gm", "t": "Pack Repair Lab", "tier": "Advanced", "concept": "packs die", "mechanism": "repair + mod station", "parts": ["kit"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "pack: repair > replace"},
  {"kind": "gm", "t": "Rolling Backpack", "tier": "Advanced", "concept": "wheel or wear", "mechanism": "wheels + handle", "parts": ["pack"], "build": "build", "time": "24h", "level": "advanced", "safety": "none", "notes": "pack: travel hybrid"}
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

