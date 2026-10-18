(function(){'use strict';
/* JAH The Kid-Friendly Learning Gadget Database — real working generator, jahdb-db-kid-friendly-learning-gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KFLGS-";
var SLUG="db-kid-friendly-learning-gadget";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing.", "ASTM F963 (toy safety): age-grade every product, non-toxic materials, no sharp points for young children."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Learning Abacus", "tier": "Foundations", "concept": "math tangible", "mechanism": "100 beads slide", "parts": ["abacus"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "learn: count by 10s"},
  {"kind": "gm", "t": "Letter Magnets", "tier": "Foundations", "concept": "letters play", "mechanism": "magnetic letters", "parts": ["magnets"], "build": "study", "time": "1h", "level": "beginner", "safety": "choke", "notes": "learn: CVC words"},
  {"kind": "gm", "t": "Shape Sorter", "tier": "Foundations", "concept": "shapes fit", "mechanism": "box + shapes", "parts": ["sorter"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "learn: trial and error"},
  {"kind": "gm", "t": "Counting Bears", "tier": "Foundations", "concept": "count fun", "mechanism": "96 bears + cups", "parts": ["bears"], "build": "study", "time": "1h", "level": "beginner", "safety": "choke", "notes": "learn: sort by color"},
  {"kind": "gm", "t": "Puzzle (24pc)", "tier": "Foundations", "concept": "pictures build", "mechanism": "24 pieces", "parts": ["puzzle"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "learn: edges first"},
  {"kind": "gm", "t": "Flash Cards (DIY)", "tier": "Foundations", "concept": "facts stick", "mechanism": "cards + drawings", "parts": ["cards"], "build": "make", "time": "3h", "level": "beginner", "safety": "none", "notes": "learn: kid draws them"},
  {"kind": "gm", "t": "Sandpaper Letters", "tier": "Foundations", "concept": "trace to learn", "mechanism": "rough letters", "parts": ["letters"], "build": "make", "time": "3h", "level": "beginner", "safety": "none", "notes": "learn: Montessori classic"},
  {"kind": "gm", "t": "Number Line Rug", "tier": "Foundations", "concept": "numbers walk", "mechanism": "rug 1-20", "parts": ["rug"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "learn: hop the math"},
  {"kind": "gm", "t": "Color Mixing Kit", "tier": "Foundations", "concept": "colors blend", "mechanism": "paint + chart", "parts": ["kit"], "build": "study", "time": "2h", "level": "beginner", "safety": "smocks", "notes": "learn: predict then mix"},
  {"kind": "gm", "t": "Magnifying Bug Box", "tier": "Foundations", "concept": "nature close", "mechanism": "box + loupe", "parts": ["box"], "build": "study", "time": "2h", "level": "beginner", "safety": "release", "notes": "learn: observe then release"},
  {"kind": "gm", "t": "Story Stones", "tier": "Foundations", "concept": "tell tales", "mechanism": "painted stones", "parts": ["stones"], "build": "make", "time": "3h", "level": "beginner", "safety": "none", "notes": "learn: draw 3, tell story"},
  {"kind": "gm", "t": "Snap Circuits Jr", "tier": "Compounded", "concept": "electronics safe", "mechanism": "snap parts", "parts": ["kit"], "build": "build", "time": "8h", "level": "intermediate", "safety": "low-voltage", "notes": "learn: 100 projects"},
  {"kind": "gm", "t": "Coding Robot (Bee-Bot)", "tier": "Compounded", "concept": "code tangible", "mechanism": "button sequences", "parts": ["robot"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "learn: forward 3, turn"},
  {"kind": "gm", "t": "Globe (Kids)", "tier": "Compounded", "concept": "world big", "mechanism": "raised relief globe", "parts": ["globe"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "learn: spin and find"},
  {"kind": "gm", "t": "Telescope (Kids)", "tier": "Compounded", "concept": "moon close", "mechanism": "70mm starter", "parts": ["scope"], "build": "study", "time": "4h", "level": "intermediate", "safety": "never sun", "notes": "learn: moon first"},
  {"kind": "gm", "t": "Microscope (Kids)", "tier": "Compounded", "concept": "tiny world", "mechanism": "40-400x kit", "parts": ["scope"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "learn: onion skin"},
  {"kind": "gm", "t": "Rock Tumbler", "tier": "Compounded", "concept": "rocks shine", "mechanism": "tumbler + grit", "parts": ["tumbler"], "build": "run", "time": "8h", "level": "intermediate", "safety": "none", "notes": "learn: 4-week patience"},
  {"kind": "gm", "t": "Crystal Growing", "tier": "Compounded", "concept": "chemistry pretty", "mechanism": "kit grows crystals", "parts": ["kit"], "build": "grow", "time": "6h", "level": "intermediate", "safety": "none", "notes": "learn: supersaturation"},
  {"kind": "gm", "t": "Volcano Kit", "tier": "Compounded", "concept": "eruptions!", "mechanism": "baking soda + vinegar", "parts": ["kit"], "build": "study", "time": "2h", "level": "intermediate", "safety": "outdoor", "notes": "learn: acid + base"},
  {"kind": "gm", "t": "Solar System Model", "tier": "Compounded", "concept": "space scale", "mechanism": "hanging planets", "parts": ["model"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "learn: scale is mind-bending"},
  {"kind": "gm", "t": "Human Body Puzzle", "tier": "Compounded", "concept": "inside us", "mechanism": "floor puzzle organs", "parts": ["puzzle"], "build": "study", "time": "3h", "level": "intermediate", "safety": "none", "notes": "learn: systems connect"},
  {"kind": "gm", "t": "Coding Cards (Unplugged)", "tier": "Compounded", "concept": "code no screen", "mechanism": "arrow cards", "parts": ["deck"], "build": "study", "time": "3h", "level": "intermediate", "safety": "none", "notes": "learn: be the robot"},
  {"kind": "gm", "t": "Math Card Game", "tier": "Compounded", "concept": "facts fun", "mechanism": "deck + rules", "parts": ["game"], "build": "make", "time": "4h", "level": "intermediate", "safety": "none", "notes": "learn: 10 min daily"},
  {"kind": "gm", "t": "Geography Puzzle", "tier": "Compounded", "concept": "world pieces", "mechanism": "floor map", "parts": ["puzzle"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "learn: continents first"},
  {"kind": "gm", "t": "Weather Station (Kids)", "tier": "Advanced", "concept": "sky science", "mechanism": "gauge + vane + thermo", "parts": ["station"], "build": "build", "time": "10h", "level": "advanced", "safety": "none", "notes": "learn: record daily"},
  {"kind": "gm", "t": "Robotics Kit (Lego)", "tier": "Advanced", "concept": "build + code", "mechanism": "kit + app", "parts": ["kit"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "learn: sensors first"},
  {"kind": "gm", "t": "Chemistry Set (Safe)", "tier": "Advanced", "concept": "reactions!", "mechanism": "kid-safe kit", "parts": ["kit"], "build": "study", "time": "10h", "level": "advanced", "safety": "adult supervise", "notes": "learn: goggles always"},
  {"kind": "gm", "t": "Garden Science Kit", "tier": "Advanced", "concept": "grow + learn", "mechanism": "seeds + journal", "parts": ["kit"], "build": "grow", "time": "16h", "level": "advanced", "safety": "none", "notes": "learn: measure growth"},
  {"kind": "gm", "t": "Birdhouse + Cam", "tier": "Advanced", "concept": "birds close", "mechanism": "house + camera", "parts": ["house"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "learn: nesting season"},
  {"kind": "gm", "t": "Archaeology Dig Kit", "tier": "Advanced", "concept": "dig history", "mechanism": "block + tools", "parts": ["kit"], "build": "dig", "time": "8h", "level": "advanced", "safety": "dust mask", "notes": "learn: brush, don't bash"},
  {"kind": "gm", "t": "Electricity Lab (Kids)", "tier": "Advanced", "concept": "circuits safe", "mechanism": "battery + bulbs kit", "parts": ["kit"], "build": "build", "time": "10h", "level": "advanced", "safety": "low-voltage", "notes": "learn: complete the loop"},
  {"kind": "gm", "t": "Map Skills Kit", "tier": "Advanced", "concept": "navigate", "mechanism": "compass + maps", "parts": ["kit"], "build": "study", "time": "8h", "level": "advanced", "safety": "none", "notes": "learn: treasure hunts"},
  {"kind": "gm", "t": "First Aid (Kids)", "tier": "Advanced", "concept": "help hurt", "mechanism": "kid kit + training", "parts": ["kit"], "build": "learn", "time": "6h", "level": "advanced", "safety": "adult lead", "notes": "learn: call, don't touch blood"},
  {"kind": "gm", "t": "Master Learning Shelf", "tier": "Advanced", "concept": "everything", "mechanism": "rotating trays", "parts": ["shelf"], "build": "curate", "time": "12h", "level": "advanced", "safety": "none", "notes": "learn: rotate monthly"}
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

