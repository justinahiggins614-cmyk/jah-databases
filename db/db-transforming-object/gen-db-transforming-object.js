(function(){'use strict';
/* JAH The Transforming Object Database — real working generator, jahdb-db-transforming-object-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TO-";
var SLUG="db-transforming-object";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Folding Chair", "tier": "Foundations", "concept": "seating vs space", "mechanism": "X-legs collapse flat", "parts": ["wood"], "build": "build", "time": "6h", "level": "beginner", "safety": "pinch points", "notes": "transform: sit to slim in seconds"},
  {"kind": "gm", "t": "Murphy Bed", "tier": "Foundations", "concept": "bed vs room", "mechanism": "pivots vertical into cabinet", "parts": ["bed"], "build": "install", "time": "20h", "level": "beginner", "safety": "anchor — pro", "notes": "transform: bedroom to office"},
  {"kind": "gm", "t": "Convertible Sofa", "tier": "Foundations", "concept": "sit vs sleep", "mechanism": "back folds to bed", "parts": ["sofa"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "transform: the classic dual-use"},
  {"kind": "gm", "t": "Folding Bike", "tier": "Foundations", "concept": "bike vs trunk", "mechanism": "hinges halve the frame", "parts": ["bike"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "transform: ride to carry"},
  {"kind": "gm", "t": "Drop-Leaf Table", "tier": "Foundations", "concept": "daily vs dinner", "mechanism": "leaves rise on brackets", "parts": ["table"], "build": "build", "time": "10h", "level": "beginner", "safety": "support leaves", "notes": "transform: 4 to 10 seats"},
  {"kind": "gm", "t": "Transformer Toy", "tier": "Foundations", "concept": "robot vs vehicle", "mechanism": "joints reconfigure", "parts": ["toy"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "transform: play twice"},
  {"kind": "gm", "t": "Folding Ladder", "tier": "Foundations", "concept": "reach vs store", "mechanism": "sections telescope", "parts": ["ladder"], "build": "study", "time": "2h", "level": "beginner", "safety": "ladder safety", "notes": "transform: 12ft to 3ft"},
  {"kind": "gm", "t": "Convertible Backpack", "tier": "Foundations", "concept": "carry vs wheel", "mechanism": "straps hide, wheels pop", "parts": ["pack"], "build": "sew", "time": "10h", "level": "beginner", "safety": "none", "notes": "transform: back to ground"},
  {"kind": "gm", "t": "Nest Tables", "tier": "Foundations", "concept": "one table vs three", "mechanism": "tables nest graduated", "parts": ["tables"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "transform: spread when needed"},
  {"kind": "gm", "t": "Folding Knife", "tier": "Foundations", "concept": "blade vs pocket", "mechanism": "pivot hides edge", "parts": ["knife"], "build": "study", "time": "1h", "level": "beginner", "safety": "blade sharp", "notes": "transform: tool to safe"},
  {"kind": "gm", "t": "Umbrella (again)", "tier": "Foundations", "concept": "dry vs down", "mechanism": "canopy collapses", "parts": ["umbrella"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "transform: the original transform"},
  {"kind": "gm", "t": "Expandable Suitcase", "tier": "Compounded", "concept": "weekend vs month", "mechanism": "zipper adds 3 inches", "parts": ["case"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "transform: grow on demand"},
  {"kind": "gm", "t": "Convertible Crib", "tier": "Compounded", "concept": "baby vs kid", "mechanism": "rails become headboard", "parts": ["crib"], "build": "convert", "time": "6h", "level": "intermediate", "safety": "follow manual", "notes": "transform: birth to teen"},
  {"kind": "gm", "t": "Folding Kayak", "tier": "Compounded", "concept": "paddle vs closet", "mechanism": "skin over folding frame", "parts": ["kayak"], "build": "assemble", "time": "4h", "level": "intermediate", "safety": "none", "notes": "transform: boat in a bag"},
  {"kind": "gm", "t": "Transformer Furniture (Wall)", "tier": "Compounded", "concept": "desk vs bed", "mechanism": "single pivot swaps both", "parts": ["unit"], "build": "install", "time": "30h", "level": "intermediate", "safety": "anchor pro", "notes": "transform: work to sleep"},
  {"kind": "gm", "t": "Convertible Car Seat", "tier": "Compounded", "concept": "rear vs forward", "mechanism": "recline + harness shift", "parts": ["seat"], "build": "study", "time": "2h", "level": "intermediate", "safety": "follow manual exactly", "notes": "transform: grows with child"},
  {"kind": "gm", "t": "Folding Guitar", "tier": "Compounded", "concept": "play vs pack", "mechanism": "neck detaches, body folds", "parts": ["guitar"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "transform: stage to overhead bin"},
  {"kind": "gm", "t": "Expandable House (Concept)", "tier": "Compounded", "concept": "small vs family", "mechanism": "modules unfold on site", "parts": ["house"], "build": "study", "time": "40h", "level": "intermediate", "safety": "pro build", "notes": "transform: 400 to 1200 sqft"},
  {"kind": "gm", "t": "Convertible Drone", "tier": "Compounded", "concept": "fly vs drive", "mechanism": "arms fold to wheels", "parts": ["drone"], "build": "build", "time": "30h", "level": "intermediate", "safety": "prop safety", "notes": "transform: sky to street"},
  {"kind": "gm", "t": "Folding Solar Panel", "tier": "Compounded", "concept": "power vs pack", "mechanism": "panels accordion", "parts": ["panel"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "transform: 200W in a briefcase"},
  {"kind": "gm", "t": "Transformer Desk (Sit-Stand)", "tier": "Compounded", "concept": "sit vs stand", "mechanism": "legs telescope electric", "parts": ["desk"], "build": "build", "time": "10h", "level": "intermediate", "safety": "pinch safety", "notes": "transform: posture on demand"},
  {"kind": "gm", "t": "Convertible Jacket", "tier": "Compounded", "concept": "jacket vs vest", "mechanism": "sleeves zip off", "parts": ["jacket"], "build": "sew", "time": "6h", "level": "intermediate", "safety": "none", "notes": "transform: weather decides"},
  {"kind": "gm", "t": "Optimists Pram (Concept)", "tier": "Advanced", "concept": "stroller vs bike trailer", "mechanism": "frame reconfigures", "parts": ["pram"], "build": "design", "time": "40h", "level": "advanced", "safety": "child safety pro", "notes": "transform: walk to ride"},
  {"kind": "gm", "t": "Transformer Building (Facade)", "tier": "Advanced", "concept": "shade vs view", "mechanism": "panels track sun", "parts": ["facade"], "build": "study", "time": "60h", "level": "advanced", "safety": "pro", "notes": "transform: the building breathes"},
  {"kind": "gm", "t": "Folding Bridge (Concept)", "tier": "Advanced", "concept": "cross vs clear", "mechanism": "spans retract for ships", "parts": ["bridge"], "build": "study", "time": "80h", "level": "advanced", "safety": "pro", "notes": "transform: road to river"},
  {"kind": "gm", "t": "Convertible Stadium", "tier": "Advanced", "concept": "sport vs concert", "mechanism": "seats slide, roof closes", "parts": ["stadium"], "build": "study", "time": "40h", "level": "advanced", "safety": "pro", "notes": "transform: the venue shapeshifts"},
  {"kind": "gm", "t": "Transformer Robot (Real)", "tier": "Advanced", "concept": "walk vs roll", "mechanism": "legs become wheels", "parts": ["robot"], "build": "build", "time": "100h", "level": "advanced", "safety": "pinch, battery", "notes": "transform: research frontier"},
  {"kind": "gm", "t": "Folding Space Habitat", "tier": "Advanced", "concept": "launch vs live", "mechanism": "origami expands in orbit", "parts": ["habitat"], "build": "study", "time": "80h", "level": "advanced", "safety": "pro", "notes": "transform: rocket fairing to rooms"},
  {"kind": "gm", "t": "Convertible Airplane Seat", "tier": "Advanced", "concept": "sit vs sleep", "mechanism": "seat becomes lie-flat", "parts": ["seat"], "build": "study", "time": "20h", "level": "advanced", "safety": "pro", "notes": "transform: economy's dream"},
  {"kind": "gm", "t": "Transformer Wheel", "tier": "Advanced", "concept": "round vs track", "mechanism": "wheel unfolds to treads", "parts": ["wheel"], "build": "build", "time": "60h", "level": "advanced", "safety": "pro", "notes": "transform: road to rubble"},
  {"kind": "gm", "t": "Folding Wind Turbine", "tier": "Advanced", "concept": "power vs storm", "mechanism": "blades fold in hurricanes", "parts": ["turbine"], "build": "study", "time": "40h", "level": "advanced", "safety": "pro", "notes": "transform: survive to generate"},
  {"kind": "gm", "t": "Convertible Classroom", "tier": "Advanced", "concept": "lecture vs lab", "mechanism": "walls and desks move", "parts": ["room"], "build": "design", "time": "40h", "level": "advanced", "safety": "pro", "notes": "transform: pedagogy in motion"},
  {"kind": "gm", "t": "Transformer Prosthetic", "tier": "Advanced", "concept": "walk vs run", "mechanism": "blade swaps by activity", "parts": ["prosthetic"], "build": "study", "time": "30h", "level": "advanced", "safety": "medical pro", "notes": "transform: one limb, many sports"},
  {"kind": "gm", "t": "Transformer Table (Dining)", "tier": "Advanced", "concept": "daily vs feast", "mechanism": "expanding mechanism", "parts": ["table"], "build": "build", "time": "40h", "level": "advanced", "safety": "pinch", "notes": "transform: 4 to 12 seats"}
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

