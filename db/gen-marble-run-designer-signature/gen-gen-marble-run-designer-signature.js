(function(){'use strict';
/* JAH The Marble Run Designer Database — real working generator, jahdb-gen-marble-run-designer-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MARUDES-";
var SLUG="gen-marble-run-designer";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Test structures gradually to rated load; keep a clear fall/drop zone during testing.", "Pinch points guarded on moving mechanisms; secure tall builds against tipping.", "ASTM F963: marbles are a choking hazard — age-grade builds and supervise young children."];
var CITATIONS=["Petroski, Henry. 'To Engineer Is Human.' St. Martin's Press, 1985.", "'Marks\\' Standard Handbook for Mechanical Engineers.' McGraw-Hill, 12th ed.", "Walker, Jearl. 'The Flying Circus of Physics.' 2nd ed. Wiley, 2006."];
var BANK=[
  {"kind": "gm", "t": "First Straight Drop", "tier": "Foundations", "concept": "marble falls", "mechanism": "straight track", "parts": ["track"], "build": "build", "time": "2h", "level": "beginner", "safety": "choke", "notes": "run: slope 10-15 degrees"},
  {"kind": "gm", "t": "The Gentle Curve", "tier": "Foundations", "concept": "turn marble", "mechanism": "curved track", "parts": ["track"], "build": "build", "time": "2h", "level": "beginner", "safety": "choke", "notes": "run: bank the curve"},
  {"kind": "gm", "t": "Funnel Finish", "tier": "Foundations", "concept": "catch marble", "mechanism": "funnel + cup", "parts": ["funnel"], "build": "build", "time": "2h", "level": "beginner", "safety": "choke", "notes": "run: center always wins"},
  {"kind": "gm", "t": "Stairs Descent", "tier": "Foundations", "concept": "step down", "mechanism": "xylophone stairs", "parts": ["stairs"], "build": "build", "time": "3h", "level": "beginner", "safety": "choke", "notes": "run: music + motion"},
  {"kind": "gm", "t": "Zigzag Run", "tier": "Foundations", "concept": "slow the fall", "mechanism": "zigzag baffles", "parts": ["track"], "build": "build", "time": "3h", "level": "beginner", "safety": "choke", "notes": "run: zigzag = time"},
  {"kind": "gm", "t": "Loop-the-Loop (Small)", "tier": "Foundations", "concept": "upside down", "mechanism": "loop needs speed", "parts": ["loop"], "build": "build", "time": "4h", "level": "beginner", "safety": "choke", "notes": "run: speed at top > sqrt(g*r)"},
  {"kind": "gm", "t": "Spiral Tower", "tier": "Foundations", "concept": "down in style", "mechanism": "helix track", "parts": ["spiral"], "build": "build", "time": "6h", "level": "beginner", "safety": "choke", "notes": "run: constant slope"},
  {"kind": "gm", "t": "Split & Merge", "tier": "Foundations", "concept": "two paths", "mechanism": "Y split rejoins", "parts": ["track"], "build": "build", "time": "4h", "level": "beginner", "safety": "choke", "notes": "run: race your marbles"},
  {"kind": "gm", "t": "Bell Chime Drop", "tier": "Foundations", "concept": "sound the run", "mechanism": "bell at drop", "parts": ["bell"], "build": "build", "time": "3h", "level": "beginner", "safety": "choke", "notes": "run: chime = checkpoint"},
  {"kind": "gm", "t": "Wall Mount Run", "tier": "Foundations", "concept": "vertical space", "mechanism": "pegs + tracks", "parts": ["wall"], "build": "mount", "time": "6h", "level": "beginner", "safety": "secure", "notes": "run: French cleat"},
  {"kind": "gm", "t": "Tabletop Starter", "tier": "Foundations", "concept": "small space", "mechanism": "box + tracks", "parts": ["box"], "build": "build", "time": "4h", "level": "beginner", "safety": "choke", "notes": "run: shoebox scale"},
  {"kind": "gm", "t": "Marble Run Math Sheet", "tier": "Foundations", "concept": "predict speed", "mechanism": "energy equations", "parts": ["study"], "build": "calc", "time": "3h", "level": "beginner", "safety": "choke", "notes": "run: v = sqrt(2gh)"},
  {"kind": "gm", "t": "Lift: Archimedes Screw", "tier": "Compounded", "concept": "up again", "mechanism": "screw lifts marbles", "parts": ["screw"], "build": "build", "time": "12h", "level": "intermediate", "safety": "pinch", "notes": "run: the eternal return"},
  {"kind": "gm", "t": "Lift: Chain Conveyor", "tier": "Compounded", "concept": "up again", "mechanism": "chain + cups", "parts": ["lift"], "build": "build", "time": "12h", "level": "intermediate", "safety": "pinch", "notes": "run: cups carry"},
  {"kind": "gm", "t": "Lift: Water Wheel", "tier": "Compounded", "concept": "up with water", "mechanism": "wheel + cups", "parts": ["wheel"], "build": "build", "time": "16h", "level": "intermediate", "safety": "water", "notes": "run: flow lifts"},
  {"kind": "gm", "t": "Switch Tracks", "tier": "Compounded", "concept": "choose path", "mechanism": "diverter gate", "parts": ["switch"], "build": "build", "time": "8h", "level": "intermediate", "safety": "choke", "notes": "run: weighted gate"},
  {"kind": "gm", "t": "Marble Counter", "tier": "Compounded", "concept": "count laps", "mechanism": "sensor + display", "parts": ["counter"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "run: break-beam"},
  {"kind": "gm", "t": "Timed Race (2-Lane)", "tier": "Compounded", "concept": "race fair", "mechanism": "dual tracks + timer", "parts": ["lanes"], "build": "build", "time": "10h", "level": "intermediate", "safety": "choke", "notes": "run: photo finish"},
  {"kind": "gm", "t": "Musical Run", "tier": "Compounded", "concept": "play music", "mechanism": "tuned chimes", "parts": ["chimes"], "build": "build", "time": "12h", "level": "intermediate", "safety": "choke", "notes": "run: pentatonic path"},
  {"kind": "gm", "t": "Elevator Lift", "tier": "Compounded", "concept": "up smooth", "mechanism": "cam + platform", "parts": ["lift"], "build": "build", "time": "16h", "level": "intermediate", "safety": "pinch", "notes": "run: dwell at top"},
  {"kind": "gm", "t": "Vortex Bowl", "tier": "Compounded", "concept": "swirl down", "mechanism": "funnel spiral", "parts": ["bowl"], "build": "build", "time": "8h", "level": "intermediate", "safety": "choke", "notes": "run: angular momentum"},
  {"kind": "gm", "t": "Plinko Board", "tier": "Compounded", "concept": "chance path", "mechanism": "peg board", "parts": ["board"], "build": "build", "time": "8h", "level": "intermediate", "safety": "choke", "notes": "run: bell curve appears"},
  {"kind": "gm", "t": "Great Ball Contraption", "tier": "Compounded", "concept": "endless loop", "mechanism": "modules + lift", "parts": ["gbc"], "build": "build", "time": "30h", "level": "intermediate", "safety": "pinch", "notes": "run: standard interfaces"},
  {"kind": "gm", "t": "Cycloid Fastest Path", "tier": "Compounded", "concept": "fastest descent", "mechanism": "brachistochrone curve", "parts": ["study"], "build": "calc", "time": "6h", "level": "intermediate", "safety": "choke", "notes": "run: math beats straight"},
  {"kind": "gm", "t": "Motorized Lift Tower", "tier": "Advanced", "concept": "auto loop", "mechanism": "motor + chain", "parts": ["tower"], "build": "build", "time": "24h", "level": "advanced", "safety": "pinch, motor", "notes": "run: continuous joy"},
  {"kind": "gm", "t": "Computer-Designed Run", "tier": "Advanced", "concept": "perfect physics", "mechanism": "sim + build", "parts": ["sim"], "build": "design", "time": "20h", "level": "advanced", "safety": "none", "notes": "run: simulate first"},
  {"kind": "gm", "t": "Giant Outdoor Run", "tier": "Advanced", "concept": "big marbles", "mechanism": "gutter + frame", "parts": ["run"], "build": "build", "time": "40h", "level": "advanced", "safety": "secure", "notes": "run: bocce balls!"},
  {"kind": "gm", "t": "Musical Marble Machine", "tier": "Advanced", "concept": "play songs", "mechanism": "programmable chimes", "parts": ["machine"], "build": "build", "time": "60h", "level": "advanced", "safety": "choke", "notes": "run: Wintergatan dreams"},
  {"kind": "gm", "t": "Marble Computer", "tier": "Advanced", "concept": "compute marbles", "mechanism": "logic gates", "parts": ["gates"], "build": "build", "time": "80h", "level": "advanced", "safety": "none", "notes": "run: AND/OR with balls"},
  {"kind": "gm", "t": "Sound + Run Combo", "tier": "Advanced", "concept": "hear the run", "mechanism": "tuned track notes", "parts": ["run"], "build": "build", "time": "20h", "level": "advanced", "safety": "choke", "notes": "run: compose while building"},
  {"kind": "gm", "t": "Competition Run", "tier": "Advanced", "concept": "race ready", "mechanism": "rules + tuning", "parts": ["run"], "build": "tune", "time": "30h", "level": "advanced", "safety": "choke", "notes": "run: consistency wins"},
  {"kind": "gm", "t": "Museum Installation", "tier": "Advanced", "concept": "public run", "mechanism": "durable + safe", "parts": ["install"], "build": "build", "time": "80h", "level": "advanced", "safety": "pro", "notes": "run: 10-year design"},
  {"kind": "gm", "t": "Master Designer Portfolio", "tier": "Advanced", "concept": "show work", "mechanism": "document + film", "parts": ["portfolio"], "build": "make", "time": "30h", "level": "advanced", "safety": "none", "notes": "run: film everything"},
  {"kind": "gm", "t": "Physics Lab Run", "tier": "Advanced", "concept": "measure", "mechanism": "timers + analysis", "parts": ["lab"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "run: verify the math"}
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

