(function(){'use strict';
/* JAH The Tower Challenge Database — real working generator, jahdb-db-tower-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TOCH-";
var SLUG="db-tower-challenge";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Test structures gradually to rated load; keep a clear fall/drop zone during testing.", "Pinch points guarded on moving mechanisms; secure tall builds against tipping."];
var CITATIONS=["Petroski, Henry. 'To Engineer Is Human.' St. Martin's Press, 1985.", "'Marks\\' Standard Handbook for Mechanical Engineers.' McGraw-Hill, 12th ed.", "Walker, Jearl. 'The Flying Circus of Physics.' 2nd ed. Wiley, 2006."];
var BANK=[
  {"kind": "gm", "t": "Block Tower Basics", "tier": "Foundations", "concept": "build tall", "mechanism": "wide base, alternate", "parts": ["blocks"], "build": "build", "time": "2h", "level": "beginner", "safety": "fall zone", "notes": "tower: 3x base rule"},
  {"kind": "gm", "t": "Jenga Strategy", "tier": "Foundations", "concept": "don't topple", "mechanism": "low + center pulls", "parts": ["jenga"], "build": "play", "time": "2h", "level": "beginner", "safety": "none", "notes": "tower: test wobble first"},
  {"kind": "gm", "t": "Card Tower", "tier": "Foundations", "concept": "fragile tall", "mechanism": "fold + lean", "parts": ["cards"], "build": "play", "time": "2h", "level": "beginner", "safety": "none", "notes": "tower: still air needed"},
  {"kind": "gm", "t": "Cup Stacking", "tier": "Foundations", "concept": "speed tall", "mechanism": "nest + stack", "parts": ["cups"], "build": "play", "time": "1h", "level": "beginner", "safety": "none", "notes": "tower: 3-3-3 pattern"},
  {"kind": "gm", "t": "Marshmallow Spaghetti", "tier": "Foundations", "concept": "team tall", "mechanism": "tape + sticks", "parts": ["kit"], "build": "build", "time": "2h", "level": "beginner", "safety": "none", "notes": "tower: triangle trumps"},
  {"kind": "gm", "t": "Coin Tower", "tier": "Foundations", "concept": "steady hands", "mechanism": "edge stacking", "parts": ["coins"], "build": "stack", "time": "1h", "level": "beginner", "safety": "none", "notes": "tower: breathe out"},
  {"kind": "gm", "t": "Book Tower", "tier": "Foundations", "concept": "heavy tall", "mechanism": "largest bottom", "parts": ["books"], "build": "stack", "time": "1h", "level": "beginner", "safety": "fall zone", "notes": "tower: spine alternate"},
  {"kind": "gm", "t": "Toothpick + Clay", "tier": "Foundations", "concept": "mini tall", "mechanism": "clay joints", "parts": ["kit"], "build": "build", "time": "2h", "level": "beginner", "safety": "none", "notes": "tower: joints matter"},
  {"kind": "gm", "t": "Popsicle Stick Tower", "tier": "Foundations", "concept": "sticks tall", "mechanism": "glue trusses", "parts": ["sticks"], "build": "build", "time": "4h", "level": "beginner", "safety": "glue", "notes": "tower: triangles everywhere"},
  {"kind": "gm", "t": "Newspaper Tower", "tier": "Foundations", "concept": "paper strong", "mechanism": "roll columns", "parts": ["paper"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "tower: rolls beat sheets"},
  {"kind": "gm", "t": "Straw Tower", "tier": "Foundations", "concept": "light tall", "mechanism": "tape joints", "parts": ["straws"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "tower: X-brace"},
  {"kind": "gm", "t": "Balsa Wood Tower", "tier": "Compounded", "concept": "strong light", "mechanism": "truss design", "parts": ["balsa"], "build": "build", "time": "10h", "level": "intermediate", "safety": "knife", "notes": "tower: test to failure"},
  {"kind": "gm", "t": "Bridge + Tower", "tier": "Compounded", "concept": "span + height", "mechanism": "combined structure", "parts": ["kit"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "tower: load paths"},
  {"kind": "gm", "t": "Earthquake Table Test", "tier": "Compounded", "concept": "shake survival", "mechanism": "cross-brace + base", "parts": ["table"], "build": "test", "time": "8h", "level": "intermediate", "safety": "none", "notes": "tower: flexible wins"},
  {"kind": "gm", "t": "Cantilever Challenge", "tier": "Compounded", "concept": "reach out", "mechanism": "balance + counterweight", "parts": ["blocks"], "build": "build", "time": "4h", "level": "intermediate", "safety": "fall zone", "notes": "tower: 1/3 rule"},
  {"kind": "gm", "t": "Arch Build", "tier": "Compounded", "concept": "span without beam", "mechanism": "voussoir compression", "parts": ["blocks"], "build": "build", "time": "6h", "level": "intermediate", "safety": "fall zone", "notes": "tower: keystone last"},
  {"kind": "gm", "t": "Dome (Geodesic)", "tier": "Compounded", "concept": "cover space", "mechanism": "triangles", "parts": ["kit"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "tower: fuller's gift"},
  {"kind": "gm", "t": "Suspension Model", "tier": "Compounded", "concept": "long span", "mechanism": "cables + towers", "parts": ["string"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "tower: cables in tension"},
  {"kind": "gm", "t": "Skyscraper Model", "tier": "Compounded", "concept": "wind matters", "mechanism": "tube + setbacks", "parts": ["kit"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "tower: tuned mass damper"},
  {"kind": "gm", "t": "Crane Model", "tier": "Compounded", "concept": "lift high", "mechanism": "counterweight + jib", "parts": ["kit"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "tower: never exceed chart"},
  {"kind": "gm", "t": "Pisa Lean Study", "tier": "Compounded", "concept": "lean but stand", "mechanism": "wide + deep base", "parts": ["books", "models"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "tower: center of mass inside"},
  {"kind": "gm", "t": "Tower Crane (Real)", "tier": "Compounded", "concept": "build skyscrapers", "mechanism": "climb + slew", "parts": ["crane"], "build": "study", "time": "8h", "level": "intermediate", "safety": "pro only", "notes": "tower: climbs itself"},
  {"kind": "gm", "t": "Leaning Tower Math", "tier": "Compounded", "concept": "how far lean?", "mechanism": "center of mass calc", "parts": ["study"], "build": "calc", "time": "4h", "level": "intermediate", "safety": "none", "notes": "tower: 4 degrees and standing"},
  {"kind": "gm", "t": "Eiffel Study", "tier": "Advanced", "concept": "iron lace tall", "mechanism": "lattice + arch", "parts": ["books", "models"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "tower: 300m of math"},
  {"kind": "gm", "t": "Burj Khalifa Study", "tier": "Advanced", "concept": "tallest", "mechanism": "buttressed core", "parts": ["books", "models"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "tower: 828m, wind-shaped"},
  {"kind": "gm", "t": "Taipei 101 Damper", "tier": "Advanced", "concept": "quake + wind", "mechanism": "730-ton ball", "parts": ["books", "models"], "build": "study", "time": "8h", "level": "advanced", "safety": "none", "notes": "tower: the ball saves it"},
  {"kind": "gm", "t": "Shanghai Tower Twist", "tier": "Advanced", "concept": "wind vortex", "mechanism": "120-degree twist", "parts": ["books", "models"], "build": "study", "time": "8h", "level": "advanced", "safety": "none", "notes": "tower: twist sheds wind"},
  {"kind": "gm", "t": "Space Elevator (Concept)", "tier": "Advanced", "concept": "orbit cheap", "mechanism": "ribbon + climber", "parts": ["books", "models"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "tower: materials not yet"},
  {"kind": "gm", "t": "Launch Tower", "tier": "Advanced", "concept": "rockets need", "mechanism": "service + umbilical", "parts": ["books", "models"], "build": "study", "time": "10h", "level": "advanced", "safety": "pro", "notes": "tower: lightning mast"},
  {"kind": "gm", "t": "Tower Restoration", "tier": "Advanced", "concept": "old tall", "mechanism": "inspect + repair", "parts": ["tower"], "build": "study", "time": "20h", "level": "advanced", "safety": "pro", "notes": "tower: masonry matters"},
  {"kind": "gm", "t": "Tensegrity Tower", "tier": "Advanced", "concept": "float compression", "mechanism": "tensegrity mast", "parts": ["kit"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "tower: Snelson's magic"},
  {"kind": "gm", "t": "Master Builder Challenge", "tier": "Advanced", "concept": "ultimate", "mechanism": "1000+ pieces", "parts": ["kit"], "build": "build", "time": "40h", "level": "advanced", "safety": "fall zone", "notes": "tower: plan in phases"},
  {"kind": "gm", "t": "Tallest Card Tower (Record)", "tier": "Advanced", "concept": "record 25ft", "mechanism": "fold + patience", "parts": ["cards"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "tower: Bryan Berg method"},
  {"kind": "gm", "t": "Spaghetti Bridge Record", "tier": "Advanced", "concept": "strong light", "mechanism": "glue + design", "parts": ["pasta"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "tower: 200x weight possible"}
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

