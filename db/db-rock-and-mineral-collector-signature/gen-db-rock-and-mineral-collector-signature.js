(function(){'use strict';
/* JAH The Rock and Mineral Collector Database — real working generator, jahdb-db-rock-and-mineral-collector-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RAMCS-";
var SLUG="db-rock-and-mineral-collector";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value.", "Collect within land-use laws; permits required on public lands for vertebrate fossils and artifacts."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Rock vs Mineral", "tier": "Foundations", "concept": "definitions", "mechanism": "natural + crystal structure", "parts": ["test"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "minerals have formulas"},
  {"kind": "gm", "t": "The Big Three Rocks", "tier": "Foundations", "concept": "igneous/sed/meta", "mechanism": "how each forms", "parts": ["identify"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "the rock cycle"},
  {"kind": "gm", "t": "Mohs Hardness", "tier": "Foundations", "concept": "scratch test", "mechanism": "1-10 scale", "parts": ["practice"], "build": "test kit", "time": "3h", "level": "beginner", "safety": "none", "notes": "fingernail 2.5, steel 5.5"},
  {"kind": "gm", "t": "Streak Test", "tier": "Foundations", "concept": "true color", "mechanism": "unglazed porcelain", "parts": ["log"], "build": "test 10", "time": "2h", "level": "beginner", "safety": "dust", "notes": "streak beats surface"},
  {"kind": "gm", "t": "Luster Types", "tier": "Foundations", "concept": "light play", "mechanism": "metallic to dull", "parts": ["identify"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "describe what you see"},
  {"kind": "gm", "t": "Crystal Shapes", "tier": "Foundations", "concept": "geometry", "mechanism": "systems + habits", "parts": ["identify"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "quartz = 6 sides"},
  {"kind": "gm", "t": "Quartz Family", "tier": "Foundations", "concept": "common beauty", "mechanism": "varieties", "parts": ["collect"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "amethyst to agate"},
  {"kind": "gm", "t": "Field Guide Use", "tier": "Foundations", "concept": "identify anywhere", "mechanism": "guide + tests", "parts": ["identify"], "build": "practice", "time": "6h", "level": "beginner", "safety": "none", "notes": "location narrows ID"},
  {"kind": "gm", "t": "Safe Collecting", "tier": "Foundations", "concept": "ethics first", "mechanism": "permission + LNT", "parts": ["collect"], "build": "learn", "time": "4h", "level": "beginner", "safety": "land rules", "notes": "take only photos where banned"},
  {"kind": "gm", "t": "Cleaning Finds", "tier": "Foundations", "concept": "reveal beauty", "mechanism": "water + brush", "parts": ["dry"], "build": "wash", "time": "2h", "level": "beginner", "safety": "chemicals", "notes": "start gentle"},
  {"kind": "gm", "t": "Display Basics", "tier": "Foundations", "concept": "show them", "mechanism": "shelves + labels", "parts": ["label"], "build": "display", "time": "4h", "level": "beginner", "safety": "sun fade", "notes": "label locality"},
  {"kind": "gm", "t": "Fluorescent Minerals", "tier": "Compounded", "concept": "glow rocks", "mechanism": "UV + species", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "UV safety", "notes": "shortwave magic"},
  {"kind": "gm", "t": "Agate Hunting", "tier": "Compounded", "concept": "banded beauty", "mechanism": "lake shores", "parts": ["tumble"], "build": "hunt", "time": "12h", "level": "intermediate", "safety": "none", "notes": "laker agates prized"},
  {"kind": "gm", "t": "Fossil vs Mineral", "tier": "Compounded", "concept": "don't confuse", "mechanism": "tests differ", "parts": ["practice"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "context clues"},
  {"kind": "gm", "t": "Tumbling Polish", "tier": "Compounded", "concept": "shine rough", "mechanism": "tumbler + grit", "parts": ["polish"], "build": "tumble", "time": "10h", "level": "intermediate", "safety": "none", "notes": "4 stages, weeks"},
  {"kind": "gm", "t": "Gold Panning", "tier": "Compounded", "concept": "color in pan", "mechanism": "technique + spots", "parts": ["practice"], "build": "pan", "time": "12h", "level": "intermediate", "safety": "claims", "notes": "pan public areas"},
  {"kind": "gm", "t": "Crystal Digging", "tier": "Compounded", "concept": "dig your own", "mechanism": "fee mines", "parts": ["find"], "build": "dig", "time": "16h", "level": "intermediate", "safety": "dig safety", "notes": "herkimer diamonds!"},
  {"kind": "gm", "t": "Micromounts", "tier": "Compounded", "concept": "tiny wonders", "mechanism": "scope + boxes", "parts": ["view"], "build": "mount", "time": "8h", "level": "intermediate", "safety": "none", "notes": "small = spectacular"},
  {"kind": "gm", "t": "UV Display Case", "tier": "Compounded", "concept": "glow show", "mechanism": "case + lights", "parts": ["build"], "build": "case,lights", "time": "10h", "level": "intermediate", "safety": "UV safety", "notes": "dark room wow"},
  {"kind": "gm", "t": "Mineral Shows", "tier": "Compounded", "concept": "see best", "mechanism": "attend + learn", "parts": ["buy"], "build": "attend", "time": "12h", "level": "intermediate", "safety": "budget", "notes": "Tucson in February"},
  {"kind": "gm", "t": "Trading Specimens", "tier": "Compounded", "concept": "swap doubles", "mechanism": "ethics + pack", "parts": ["ship"], "build": "trade", "time": "6h", "level": "intermediate", "safety": "none", "notes": "pad well"},
  {"kind": "gm", "t": "Labeling Science", "tier": "Compounded", "concept": "data matters", "mechanism": "locality + ID", "parts": ["catalog"], "build": "label all", "time": "8h", "level": "intermediate", "safety": "none", "notes": "locality = value"},
  {"kind": "gm", "t": "Zeolites", "tier": "Compounded", "concept": "delicate crystals", "mechanism": "basalt quarries", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "fragile beauties"},
  {"kind": "gm", "t": "Copper Minerals", "tier": "Compounded", "concept": "blue + green", "mechanism": "oxidation zones", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "mine safety", "notes": "malachite + azurite"},
  {"kind": "gm", "t": "Rare Species", "tier": "Advanced", "concept": "holy grails", "mechanism": "type localities", "parts": ["hunt"], "build": "study", "time": "30h", "level": "advanced", "safety": "none", "notes": "small + rare"},
  {"kind": "gm", "t": "Museum Quality", "tier": "Advanced", "concept": "best of best", "mechanism": "aesthetics + rarity", "parts": ["collect"], "build": "study", "time": "40h", "level": "advanced", "safety": "none", "notes": "damage-free"},
  {"kind": "gm", "t": "Field Research", "tier": "Advanced", "concept": "find new", "mechanism": "geology + maps", "parts": ["explore"], "build": "research", "time": "60h", "level": "advanced", "safety": "claims", "notes": "document finds"},
  {"kind": "gm", "t": "Cutting Stones", "tier": "Advanced", "concept": "shape beauty", "mechanism": "trim saw + polish", "parts": ["practice"], "build": "cut", "time": "40h", "level": "advanced", "safety": "blade safety", "notes": "slabs to cabs"},
  {"kind": "gm", "t": "Faceting (Intro)", "tier": "Advanced", "concept": "sparkle math", "mechanism": "angles + polish", "parts": ["learn"], "build": "facet", "time": "80h", "level": "advanced", "safety": "none", "notes": "years to master"},
  {"kind": "gm", "t": "Collection Catalog", "tier": "Advanced", "concept": "know all", "mechanism": "database + photos", "parts": ["build"], "build": "catalog", "time": "40h", "level": "advanced", "safety": "none", "notes": "insurance"},
  {"kind": "gm", "t": "Teaching Geology", "tier": "Advanced", "concept": "share rocks", "mechanism": "kits + walks", "parts": ["lead"], "build": "teach", "time": "20h", "level": "advanced", "safety": "none", "notes": "kids love rocks"},
  {"kind": "gm", "t": "Master Mineral Collector", "tier": "Advanced", "concept": "the life", "mechanism": "focus + field", "parts": ["mentor"], "build": "reflect", "time": "80h", "level": "advanced", "safety": "none", "notes": "specialize"},
  {"kind": "gm", "t": "Pegmatite Hunting", "tier": "Advanced", "concept": "giant crystals", "mechanism": "pegmatite dikes", "parts": ["hunt"], "build": "study", "time": "30h", "level": "advanced", "safety": "dig safety", "notes": "tourmaline dreams"},
  {"kind": "gm", "t": "Systematic Collection", "tier": "Advanced", "concept": "science order", "mechanism": "Dana classification", "parts": ["catalog"], "build": "organize", "time": "30h", "level": "advanced", "safety": "none", "notes": "one of each family"}
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

