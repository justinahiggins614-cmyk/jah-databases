(function(){'use strict';
/* JAH The Fossil Collector Database — real working generator, jahdb-db-fossil-collector-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FOCOS-";
var SLUG="db-fossil-collector";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value.", "BLM and state rules: invertebrate fossils casual collection allowed in places; vertebrates need permits; never collect in parks."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "What Is a Fossil", "tier": "Foundations", "concept": "deep time", "mechanism": "remains + traces", "parts": ["learn"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "millions of years"},
  {"kind": "gm", "t": "Fossil vs Rock", "tier": "Foundations", "concept": "tell apart", "mechanism": "patterns + context", "parts": ["practice"], "build": "study", "time": "3h", "level": "beginner", "safety": "none", "notes": "symmetry hints life"},
  {"kind": "gm", "t": "Trilobites", "tier": "Foundations", "concept": "sea bugs", "mechanism": "Cambrian stars", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "275M years of them"},
  {"kind": "gm", "t": "Ammonites", "tier": "Foundations", "concept": "spiral shells", "mechanism": "sutures + chambers", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "coiled beauty"},
  {"kind": "gm", "t": "Shark Teeth", "tier": "Foundations", "concept": "toothy finds", "mechanism": "species + age", "parts": ["find"], "build": "hunt", "time": "6h", "level": "beginner", "safety": "none", "notes": "rivers + beaches"},
  {"kind": "gm", "t": "Petrified Wood", "tier": "Foundations", "concept": "stone trees", "mechanism": "cells replaced", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Arizona rainbow"},
  {"kind": "gm", "t": "Leaf Fossils", "tier": "Foundations", "concept": "green ghosts", "mechanism": "shale splits", "parts": ["find"], "build": "split", "time": "6h", "level": "beginner", "safety": "eye", "notes": "split along layers"},
  {"kind": "gm", "t": "Crinoids", "tier": "Foundations", "concept": "sea lilies", "mechanism": "stems + cups", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Mississippian seas"},
  {"kind": "gm", "t": "Brachiopods", "tier": "Foundations", "concept": "lamp shells", "mechanism": "symmetry test", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "not clams!"},
  {"kind": "gm", "t": "Coral (Fossil)", "tier": "Foundations", "concept": "ancient reefs", "mechanism": "patterns", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Petoskey stones"},
  {"kind": "gm", "t": "Coprolite (Fun)", "tier": "Foundations", "concept": "dino poop!", "mechanism": "spiral shapes", "parts": ["laugh"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "kids love"},
  {"kind": "gm", "t": "Dinosaur Bone", "tier": "Compounded", "concept": "giant finds", "mechanism": "texture + weight", "parts": ["hunt"], "build": "study", "time": "12h", "level": "intermediate", "safety": "claims", "notes": "never collect parks"},
  {"kind": "gm", "t": "Mammal Teeth", "tier": "Compounded", "concept": "ice age", "mechanism": "enamel patterns", "parts": ["hunt"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "mastodon molars"},
  {"kind": "gm", "t": "Fish Fossils", "tier": "Compounded", "concept": "Green River", "mechanism": "split limestone", "parts": ["find"], "build": "split", "time": "16h", "level": "intermediate", "safety": "eye", "notes": "quarry trips"},
  {"kind": "gm", "t": "Insects in Amber", "tier": "Compounded", "concept": "golden tomb", "mechanism": "inclusions", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "fakes", "notes": "Baltic real"},
  {"kind": "gm", "t": "Plant Fossils", "tier": "Compounded", "concept": "coal forests", "mechanism": "ferns + bark", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "Mazon Creek"},
  {"kind": "gm", "t": "Trace Fossils", "tier": "Compounded", "concept": "footprints!", "mechanism": "tracks + burrows", "parts": ["find"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "behavior fossilized"},
  {"kind": "gm", "t": "Preparation Basics", "tier": "Compounded", "concept": "reveal fossil", "mechanism": "tools + patience", "parts": ["practice"], "build": "prep", "time": "20h", "level": "intermediate", "safety": "dust", "notes": "air scribe pro"},
  {"kind": "gm", "t": "Legal Collecting", "tier": "Compounded", "concept": "laws matter", "mechanism": "BLM + private", "parts": ["permit"], "build": "learn", "time": "8h", "level": "intermediate", "safety": "fines", "notes": "vertebrates need permits"},
  {"kind": "gm", "t": "Museum Prep Volunteer", "tier": "Compounded", "concept": "learn pro", "mechanism": "volunteer lab", "parts": ["prep"], "build": "volunteer", "time": "20h", "level": "intermediate", "safety": "none", "notes": "best education"},
  {"kind": "gm", "t": "Field Jacketing", "tier": "Compounded", "concept": "protect big", "mechanism": "plaster + burlap", "parts": ["practice"], "build": "jacket", "time": "12h", "level": "intermediate", "safety": "weight", "notes": "like a cast"},
  {"kind": "gm", "t": "Microfossils", "tier": "Compounded", "concept": "tiny time", "mechanism": "wash + scope", "parts": ["view"], "build": "process", "time": "10h", "level": "intermediate", "safety": "none", "notes": "forams date rocks"},
  {"kind": "gm", "t": "Echinoids", "tier": "Compounded", "concept": "sea urchins", "mechanism": "symmetry", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "5-part symmetry"},
  {"kind": "gm", "t": "Graptolites", "tier": "Compounded", "concept": "saw blades", "mechanism": "shale bedding", "parts": ["find"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "index fossils"},
  {"kind": "gm", "t": "Dinosaur Eggs", "tier": "Advanced", "concept": "baby dinos", "mechanism": "shell texture", "parts": ["collect"], "build": "study", "time": "20h", "level": "advanced", "safety": "fakes", "notes": "rare + faked"},
  {"kind": "gm", "t": "Feathered Fossils", "tier": "Advanced", "concept": "dino-birds", "mechanism": "Solnhofen + China", "parts": ["research"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "Liaoning wonders"},
  {"kind": "gm", "t": "Hominid (Study)", "tier": "Advanced", "concept": "us, long ago", "mechanism": "casts + sites", "parts": ["learn"], "build": "study", "time": "30h", "level": "advanced", "safety": "none", "notes": "casts, not originals"},
  {"kind": "gm", "t": "Mass Extinction Beds", "tier": "Advanced", "concept": "the big five", "mechanism": "boundary clays", "parts": ["research"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "iridium layer"},
  {"kind": "gm", "t": "Private Quarry", "tier": "Advanced", "concept": "your dig", "mechanism": "lease + work", "parts": ["dig"], "build": "arrange", "time": "60h", "level": "advanced", "safety": "liability", "notes": "insurance"},
  {"kind": "gm", "t": "Publishing Finds", "tier": "Advanced", "concept": "science!", "mechanism": "document + submit", "parts": ["publish"], "build": "write", "time": "40h", "level": "advanced", "safety": "none", "notes": "amateurs discover"},
  {"kind": "gm", "t": "Donating Fossils to Museums", "tier": "Advanced", "concept": "legacy", "mechanism": "science first", "parts": ["arrange"], "build": "donate", "time": "20h", "level": "advanced", "safety": "none", "notes": "significant finds"},
  {"kind": "gm", "t": "Master Paleontologist (Amateur)", "tier": "Advanced", "concept": "the life", "mechanism": "study + field", "parts": ["mentor"], "build": "learn", "time": "100h", "level": "advanced", "safety": "none", "notes": "join societies"},
  {"kind": "gm", "t": "Dinosaur Trackways", "tier": "Advanced", "concept": "walk with giants", "mechanism": "sites + casts", "parts": ["study"], "build": "visit", "time": "20h", "level": "advanced", "safety": "permits", "notes": "Paluxy river"},
  {"kind": "gm", "t": "Preparation Lab Setup", "tier": "Advanced", "concept": "pro prep", "mechanism": "tools + dust", "parts": ["prep"], "build": "build", "time": "30h", "level": "advanced", "safety": "dust", "notes": "air abrasive pro"}
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

