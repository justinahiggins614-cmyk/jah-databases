(function(){'use strict';
/* JAH The Giant Domino Chain Database — real working generator, jahdb-db-giant-domino-chain-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GDC-";
var SLUG="db-giant-domino-chain";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Test structures gradually to rated load; keep a clear fall/drop zone during testing.", "Pinch points guarded on moving mechanisms; secure tall builds against tipping.", "Event builds: clear fall zones, team lifting for heavy sets, weather plan for outdoors."];
var CITATIONS=["Petroski, Henry. 'To Engineer Is Human.' St. Martin's Press, 1985.", "'Marks\\' Standard Handbook for Mechanical Engineers.' McGraw-Hill, 12th ed.", "Walker, Jearl. 'The Flying Circus of Physics.' 2nd ed. Wiley, 2006."];
var BANK=[
  {"kind": "gm", "t": "Domino Physics 101", "tier": "Foundations", "concept": "why fall?", "mechanism": "toppling torque", "parts": ["study"], "build": "read", "time": "2h", "level": "beginner", "safety": "none", "notes": "domino: taller falls faster"},
  {"kind": "gm", "t": "Spacing Rules", "tier": "Foundations", "concept": "gap matters", "mechanism": "1.5x thickness", "parts": ["dominoes"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "domino: the golden gap"},
  {"kind": "gm", "t": "First 100 Chain", "tier": "Foundations", "concept": "chain joy", "mechanism": "100 straight", "parts": ["dominoes"], "build": "set", "time": "3h", "level": "beginner", "safety": "none", "notes": "domino: straight first"},
  {"kind": "gm", "t": "The Turn", "tier": "Foundations", "concept": "corners", "mechanism": "angled placement", "parts": ["dominoes"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "domino: 30-degree turns"},
  {"kind": "gm", "t": "Stairs Up/Down", "tier": "Foundations", "concept": "levels", "mechanism": "step blocks", "parts": ["dominoes"], "build": "test", "time": "3h", "level": "beginner", "safety": "fall zone", "notes": "domino: small steps"},
  {"kind": "gm", "t": "Bridge Over Gap", "tier": "Foundations", "concept": "span", "mechanism": "plank bridge", "parts": ["dominoes"], "build": "test", "time": "3h", "level": "beginner", "safety": "none", "notes": "domino: level bridge"},
  {"kind": "gm", "t": "Circle Chain", "tier": "Foundations", "concept": "loop", "mechanism": "ring layout", "parts": ["dominoes"], "build": "set", "time": "3h", "level": "beginner", "safety": "none", "notes": "domino: ends meet"},
  {"kind": "gm", "t": "Pyramid Stack", "tier": "Foundations", "concept": "up", "mechanism": "stacked rows", "parts": ["dominoes"], "build": "build", "time": "4h", "level": "beginner", "safety": "fall zone", "notes": "domino: wide base"},
  {"kind": "gm", "t": "Color Patterns", "tier": "Foundations", "concept": "pretty fall", "mechanism": "color sequences", "parts": ["dominoes"], "build": "plan", "time": "4h", "level": "beginner", "safety": "none", "notes": "domino: plan on paper"},
  {"kind": "gm", "t": "Outdoor Setup", "tier": "Foundations", "concept": "wind foe", "mechanism": "heavy + sheltered", "parts": ["dominoes"], "build": "set", "time": "4h", "level": "beginner", "safety": "weather", "notes": "domino: morning calm"},
  {"kind": "gm", "t": "Cleanup Fast", "tier": "Foundations", "concept": "reset quick", "mechanism": "sweep + sort", "parts": ["dominoes"], "build": "clean", "time": "1h", "level": "beginner", "safety": "none", "notes": "domino: bins by color"},
  {"kind": "gm", "t": "Domino Day History", "tier": "Foundations", "concept": "record culture", "mechanism": "film + story", "parts": ["study"], "build": "watch", "time": "4h", "level": "beginner", "safety": "none", "notes": "domino: from 1976 TV"},
  {"kind": "gm", "t": "3D Structures", "tier": "Compounded", "concept": "build up", "mechanism": "towers + walls", "parts": ["dominoes"], "build": "build", "time": "10h", "level": "intermediate", "safety": "fall zone", "notes": "domino: 3D = wow"},
  {"kind": "gm", "t": "Chain Reactions+", "tier": "Compounded", "concept": "more than fall", "mechanism": "balls + ramps", "parts": ["kit"], "build": "build", "time": "10h", "level": "intermediate", "safety": "choke", "notes": "domino: dominoes trigger all"},
  {"kind": "gm", "t": "1000-Domino Run", "tier": "Compounded", "concept": "big chain", "mechanism": "1000 planned", "parts": ["dominoes"], "build": "set", "time": "16h", "level": "intermediate", "safety": "none", "notes": "domino: sections + builders"},
  {"kind": "gm", "t": "Timelapse Film", "tier": "Compounded", "concept": "share the fall", "mechanism": "camera + edit", "parts": ["film"], "build": "film", "time": "8h", "level": "intermediate", "safety": "none", "notes": "domino: top-down angle"},
  {"kind": "gm", "t": "Music Sync Fall", "tier": "Compounded", "concept": "fall to beat", "mechanism": "timed drops", "parts": ["dominoes"], "build": "plan", "time": "12h", "level": "intermediate", "safety": "none", "notes": "domino: bpm = spacing"},
  {"kind": "gm", "t": "Portrait Fall", "tier": "Compounded", "concept": "image appears", "mechanism": "pixel plan", "parts": ["dominoes"], "build": "plan", "time": "20h", "level": "intermediate", "safety": "none", "notes": "domino: 100x100 grid"},
  {"kind": "gm", "t": "Builder Math", "tier": "Compounded", "concept": "how many?", "mechanism": "area + density", "parts": ["dominoes"], "build": "calc", "time": "4h", "level": "intermediate", "safety": "none", "notes": "domino: 50 per square meter"},
  {"kind": "gm", "t": "Field Kit Pack", "tier": "Compounded", "concept": "build anywhere", "mechanism": "kit + transport", "parts": ["kit"], "build": "pack", "time": "6h", "level": "intermediate", "safety": "none", "notes": "domino: padded cases"},
  {"kind": "gm", "t": "Stadium Chain", "tier": "Compounded", "concept": "huge floor", "mechanism": "team build", "parts": ["dominoes"], "build": "set", "time": "30h", "level": "intermediate", "safety": "none", "notes": "domino: zone captains"},
  {"kind": "gm", "t": "Record Attempt (Local)", "tier": "Compounded", "concept": "record chase", "mechanism": "count + witness", "parts": ["dominoes"], "build": "set", "time": "40h", "level": "intermediate", "safety": "none", "notes": "domino: document everything"},
  {"kind": "gm", "t": "Topple Art Film", "tier": "Compounded", "concept": "art film", "mechanism": "story + fall", "parts": ["film"], "build": "make", "time": "20h", "level": "intermediate", "safety": "none", "notes": "domino: story first"},
  {"kind": "gm", "t": "Night Glow Chain", "tier": "Compounded", "concept": "glow fall", "mechanism": "UV + white", "parts": ["dominoes"], "build": "set", "time": "12h", "level": "intermediate", "safety": "none", "notes": "domino: blacklight magic"},
  {"kind": "gm", "t": "Underwater (Tank)", "tier": "Compounded", "concept": "slow motion", "mechanism": "tank + weights", "parts": ["tank"], "build": "test", "time": "8h", "level": "intermediate", "safety": "water", "notes": "domino: dreamy slow"},
  {"kind": "gm", "t": "Slow-Mo Science", "tier": "Advanced", "concept": "see physics", "mechanism": "high-speed cam", "parts": ["film"], "build": "film", "time": "12h", "level": "advanced", "safety": "none", "notes": "domino: 1000fps reveals"},
  {"kind": "gm", "t": "Domino Robot Setter", "tier": "Advanced", "concept": "auto set", "mechanism": "robot places", "parts": ["robot"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "domino: the meta build"},
  {"kind": "gm", "t": "Eternal Chain (Loop)", "tier": "Advanced", "concept": "never ends", "mechanism": "lifter returns", "parts": ["machine"], "build": "build", "time": "60h", "level": "advanced", "safety": "pinch", "notes": "domino: the loop dream"},
  {"kind": "gm", "t": "World Record (4.9M)", "tier": "Advanced", "concept": "biggest ever", "mechanism": "team + months", "parts": ["dominoes"], "build": "study", "time": "40h", "level": "advanced", "safety": "none", "notes": "domino: 2019 record film"},
  {"kind": "gm", "t": "Domino Computer", "tier": "Advanced", "concept": "logic falls", "mechanism": "AND/OR gates", "parts": ["dominoes"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "domino: computation topples"},
  {"kind": "gm", "t": "Chain Machine Hybrid", "tier": "Advanced", "concept": "Rube + domino", "mechanism": "combined", "parts": ["machine"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "domino: best of both"},
  {"kind": "gm", "t": "Teaching Physics", "tier": "Advanced", "concept": "learn falling", "mechanism": "class sets", "parts": ["class"], "build": "plan", "time": "16h", "level": "advanced", "safety": "none", "notes": "domino: energy + momentum"},
  {"kind": "gm", "t": "Festival Installation", "tier": "Advanced", "concept": "public wow", "mechanism": "durable + reset", "parts": ["install"], "build": "build", "time": "80h", "level": "advanced", "safety": "pro", "notes": "domino: reset in hours"},
  {"kind": "gm", "t": "Master Builder", "tier": "Advanced", "concept": "the craft", "mechanism": "portfolio", "parts": ["portfolio"], "build": "make", "time": "40h", "level": "advanced", "safety": "none", "notes": "domino: film all"}
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

