(function(){'use strict';
/* JAH The Meteorite Discovery Database — real working generator, jahdb-db-meteorite-discovery-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEDI-";
var SLUG="db-meteorite-discovery";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value.", "Meteoritical Society naming and classification standards; document find coordinates and chain of custody."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "What Is a Meteorite", "tier": "Foundations", "concept": "space rocks", "mechanism": "fall to Earth", "parts": ["learn"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "older than Earth rocks"},
  {"kind": "gm", "t": "Meteor Wrong (Meteowrong)", "tier": "Foundations", "concept": "not meteorites", "mechanism": "slag + hematite", "parts": ["test"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "99% are wrongs"},
  {"kind": "gm", "t": "Fusion Crust", "tier": "Foundations", "concept": "burnt skin", "mechanism": "thin black crust", "parts": ["identify"], "build": "study", "time": "3h", "level": "beginner", "safety": "none", "notes": "atmospheric branding"},
  {"kind": "gm", "t": "Magnet Test", "tier": "Foundations", "concept": "iron loves magnets", "mechanism": "stick test", "parts": ["practice"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "most stick"},
  {"kind": "gm", "t": "Regmaglypts", "tier": "Foundations", "concept": "thumbprints", "mechanism": "ablation dents", "parts": ["identify"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "melted dimples"},
  {"kind": "gm", "t": "Chondrules", "tier": "Foundations", "concept": "tiny spheres", "mechanism": "cut face", "parts": ["view"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "solar system droplets"},
  {"kind": "gm", "t": "Iron vs Stone", "tier": "Foundations", "concept": "two families", "mechanism": "nickel test", "parts": ["test"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "irons = metal"},
  {"kind": "gm", "t": "Famous Falls", "tier": "Foundations", "concept": "witnessed!", "mechanism": "stories", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Chelyabinsk 2013"},
  {"kind": "gm", "t": "Finds vs Falls", "tier": "Foundations", "concept": "seen vs found", "mechanism": "provenance", "parts": ["learn"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "falls premium"},
  {"kind": "gm", "t": "Desert Hunting", "tier": "Foundations", "concept": "dark on light", "mechanism": "deserts preserve", "parts": ["plan"], "build": "study", "time": "8h", "level": "beginner", "safety": "desert safety", "notes": "permission first"},
  {"kind": "gm", "t": "Legal Basics", "tier": "Foundations", "concept": "who owns?", "mechanism": "laws vary", "parts": ["research"], "build": "learn", "time": "4h", "level": "beginner", "safety": "none", "notes": "BLM: permit needed"},
  {"kind": "gm", "t": "Widmanstatten Pattern", "tier": "Compounded", "concept": "crystal proof", "mechanism": "etch + view", "parts": ["see"], "build": "etch", "time": "8h", "level": "intermediate", "safety": "acid safety", "notes": "cannot be faked"},
  {"kind": "gm", "t": "Nickel Test", "tier": "Compounded", "concept": "confirm iron", "mechanism": "dimethylglyoxime", "parts": ["practice"], "build": "test", "time": "4h", "level": "intermediate", "safety": "chemical", "notes": "pink = nickel"},
  {"kind": "gm", "t": "Classification", "tier": "Compounded", "concept": "types matter", "mechanism": "iron/stone/stony-iron", "parts": ["classify"], "build": "study", "time": "12h", "level": "intermediate", "safety": "lab", "notes": "thin sections"},
  {"kind": "gm", "t": "Strewn Fields", "tier": "Compounded", "concept": "ellipses", "mechanism": "map falls", "parts": ["research"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "wind sorts by mass"},
  {"kind": "gm", "t": "Metal Detector Hunt", "tier": "Compounded", "concept": "find buried", "mechanism": "sweep + dig", "parts": ["find"], "build": "hunt", "time": "16h", "level": "intermediate", "safety": "dig safety", "notes": "all-metal mode"},
  {"kind": "gm", "t": "Thin Sections", "tier": "Compounded", "concept": "see inside", "mechanism": "30-micron slice", "parts": ["view"], "build": "make", "time": "12h", "level": "intermediate", "safety": "none", "notes": "polarized wow"},
  {"kind": "gm", "t": "Provenance Papers", "tier": "Compounded", "concept": "prove it", "mechanism": "documentation", "parts": ["file"], "build": "gather", "time": "6h", "level": "intermediate", "safety": "none", "notes": "chain of custody"},
  {"kind": "gm", "t": "Cutting (Trim Saw)", "tier": "Compounded", "concept": "window in", "mechanism": "trim slice", "parts": ["cut"], "build": "saw", "time": "8h", "level": "intermediate", "safety": "blade", "notes": "coolant"},
  {"kind": "gm", "t": "Etching Iron", "tier": "Compounded", "concept": "reveal pattern", "mechanism": "acid etch", "parts": ["see"], "build": "etch", "time": "6h", "level": "intermediate", "safety": "acid", "notes": "neutralize"},
  {"kind": "gm", "t": "Display (Nitrogen?)", "tier": "Compounded", "concept": "stop rust", "mechanism": "dry + oil", "parts": ["display"], "build": "store", "time": "4h", "level": "intermediate", "safety": "none", "notes": "lawsone treatment"},
  {"kind": "gm", "t": "Buying Smart", "tier": "Compounded", "concept": "avoid fakes", "mechanism": "reputable dealers", "parts": ["buy"], "build": "study", "time": "10h", "level": "intermediate", "safety": "fakes", "notes": "IMCA dealers"},
  {"kind": "gm", "t": "Achondrites", "tier": "Compounded", "concept": "melted asteroids", "mechanism": "basaltic", "parts": ["research"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "Vesta visitors"},
  {"kind": "gm", "t": "Impact Glass", "tier": "Compounded", "concept": "earth melted", "mechanism": "tektites", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "moldavite green"},
  {"kind": "gm", "t": "Lunar Meteorites", "tier": "Advanced", "concept": "moon rocks!", "mechanism": "anorthosite", "parts": ["research"], "build": "study", "time": "20h", "level": "advanced", "safety": "price", "notes": "$$$ per gram"},
  {"kind": "gm", "t": "Martian Meteorites", "tier": "Advanced", "concept": "Mars rocks!", "mechanism": "shergottites", "parts": ["research"], "build": "study", "time": "20h", "level": "advanced", "safety": "price", "notes": "trapped gas proves"},
  {"kind": "gm", "t": "Pallasites", "tier": "Advanced", "concept": "gem + metal", "mechanism": "olivine in iron", "parts": ["collect"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "Esquel beauty"},
  {"kind": "gm", "t": "Carbonaceous Chondrites", "tier": "Advanced", "concept": "life's ingredients", "mechanism": "organics", "parts": ["research"], "build": "study", "time": "20h", "level": "advanced", "safety": "contamination", "notes": "handle clean"},
  {"kind": "gm", "t": "Hunting Expeditions", "tier": "Advanced", "concept": "serious hunt", "mechanism": "team + permits", "parts": ["hunt"], "build": "plan", "time": "60h", "level": "advanced", "safety": "remote safety", "notes": "Antarctica dream"},
  {"kind": "gm", "t": "Lab Analysis", "tier": "Advanced", "concept": "know all", "mechanism": "probe + isotopes", "parts": ["analyze"], "build": "submit", "time": "30h", "level": "advanced", "safety": "fees", "notes": "university labs"},
  {"kind": "gm", "t": "Publishing Meteorite Finds", "tier": "Advanced", "concept": "science", "mechanism": "document + submit", "parts": ["publish"], "build": "write", "time": "30h", "level": "advanced", "safety": "none", "notes": "Meteoritical Society"},
  {"kind": "gm", "t": "Collection Curation", "tier": "Advanced", "concept": "museum grade", "mechanism": "climate + catalog", "parts": ["maintain"], "build": "curate", "time": "30h", "level": "advanced", "safety": "none", "notes": "rust never sleeps"},
  {"kind": "gm", "t": "Master Meteorite Hunter", "tier": "Advanced", "concept": "the life", "mechanism": "decades hunting", "parts": ["mentor"], "build": "reflect", "time": "80h", "level": "advanced", "safety": "none", "notes": "patience + deserts"},
  {"kind": "gm", "t": "Shocking History", "tier": "Advanced", "concept": "craters story", "mechanism": "structures", "parts": ["visit"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "Meteor Crater AZ"}
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

