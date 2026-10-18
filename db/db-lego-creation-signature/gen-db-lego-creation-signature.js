(function(){'use strict';
/* JAH The LEGO Creation Database — real working generator, jahdb-db-lego-creation-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCS-";
var SLUG="db-lego-creation";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "First MOC: Small House", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["baseplate 16x", "16", 8.0]], "tools": ["none"], "steps": ["plan 8x10 footprint", "walls 4 high", "roof slope bricks", "door and windows"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Color Theory for Builders", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bricks sorted", "1", 0.0]], "tools": ["none"], "steps": ["pick 3-color palette", "60-30-10 rule", "test combos", "rebuild section"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Sturdy Walls: Brick Bonding", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bricks", "1", 0.0]], "tools": ["none"], "steps": ["stagger joints", "interlock corners", "plate layers between", "test strength"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Simple Vehicle: Cart", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wheels", "4", 5.0], ["bricks", "1", 0.0]], "tools": ["none"], "steps": ["chassis plate", "axle bricks", "wheels spin free", "load test"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Micro-Scale Tree", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["green slopes", "1", 4.0], ["brown trunk", "1", 2.0]], "tools": ["none"], "steps": ["trunk stacked", "canopy slopes layered", "vary greens", "base plate"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Minifigure Habitat Vignette", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["figure", "1", 4.0], ["baseplate 8x", "8", 5.0], ["parts", "1", 6.0]], "tools": ["none"], "steps": ["theme the scene", "figure in action", "details tell story", "photograph"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Mosaic Basics 16x16", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["plates 1x1", "200", 18.0], ["baseplate", "1", 8.0]], "tools": ["none"], "steps": ["pixelate image", "sort colors", "build rows", "frame"], "time": "6h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "SNOT Techniques Intro", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["brackets", "1", 8.0], ["headlight bricks", "1", 6.0]], "tools": ["none"], "steps": ["studs-not-on-top", "bracket sideways", "tile smooth", "practice cube"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Simple Bridge Span", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bricks", "1", 0.0]], "tools": ["none"], "steps": ["two towers", "arch or beam", "test with weight", "record span"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Furniture for Minifigs", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["parts", "1", 8.0]], "tools": ["none"], "steps": ["chair: seat+back", "table: top+legs", "bed: base+headboard", "scale check"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Greebling: Surface Detail", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["small parts", "1", 10.0]], "tools": ["none"], "steps": ["base shape first", "add vents/pipes", "asymmetry", "step back check"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Working Drawbridge", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["hinge bricks", "1", 8.0], ["chain", "1", 4.0], ["tower parts", "1", 10.0]], "tools": ["none"], "steps": ["towers both sides", "hinge deck", "chain windlass", "raises/lowers"], "time": "5h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Gear-Driven Windmill", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["technic gears", "1", 15.0], ["axles", "1", 6.0], ["sails", "1", 8.0]], "tools": ["none"], "steps": ["tower sturdy", "gear train 3:1", "blades catch wind", "test spin"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Modular Building Standard", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["baseplate 32x", "32", 12.0], ["parts", "1", 30.0]], "tools": ["none"], "steps": ["32-stud module", "technic pin joins", "interior detail", "roof lifts off"], "time": "14h", "level": "intermediate", "safety": "plan the pin alignment first"},
  {"kind": "diy", "t": "Technic Suspension Car", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["technic set", "1", 40.0], ["shocks", "1", 10.0]], "tools": ["none"], "steps": ["chassis rails", "spring suspension", "steering linkage", "test drive"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Castle with Interior", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["gray parts", "1", 35.0], ["figures", "1", 12.0]], "tools": ["none"], "steps": ["outer walls", "gatehouse working", "great hall inside", "tower tops"], "time": "16h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Spaceship with Greebles", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["parts", "1", 30.0], ["trans pieces", "1", 10.0]], "tools": ["none"], "steps": ["hull shape", "greeble panels", "cockpit interior", "stand"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Working Crane", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 45.0], ["string", "1", 4.0], ["hook", "1", 3.0]], "tools": ["none"], "steps": ["base stable", "boom extends", "winch winds", "load test"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Mosaic Portrait 32x32", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["plates", "800", 60.0], ["baseplate", "1", 12.0]], "tools": ["none"], "steps": ["pixelate photo", "color match", "build in sections", "join"], "time": "20h", "level": "intermediate", "safety": "sort colors first — saves hours"},
  {"kind": "diy", "t": "Pneumatic Lift", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["pneumatic parts", "1", 35.0]], "tools": ["none"], "steps": ["pump and cylinder", "tubing routed", "valve control", "lifts load"], "time": "8h", "level": "intermediate", "safety": "check tubing seals"},
  {"kind": "diy", "t": "Ball-Contraption Module", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 40.0], ["balls", "1", 5.0]], "tools": ["none"], "steps": ["input/output heights", "reliable lift", "test 100 cycles", "connect standard"], "time": "14h", "level": "intermediate", "safety": "reliability over speed"},
  {"kind": "diy", "t": "Great Ball Contraption Loop", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 120.0], ["motors", "2", 40.0], ["balls", "1", 10.0]], "tools": ["none"], "steps": ["3+ modules", "motor drive", "continuous loop", "jam-proofing"], "time": "30h", "level": "advanced", "safety": "motors: check battery safety"},
  {"kind": "diy", "t": "UCS-Scale Starship", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [], "tools": ["none"], "steps": ["frame first", "hull plating", "interior if visible", "display stand"], "time": "60h", "level": "advanced", "safety": "big builds need internal technic frame"},
  {"kind": "diy", "t": "Working Clock", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["technic gears", "1", 60.0], ["pendulum", "1", 10.0], ["weights", "1", 8.0]], "tools": ["none"], "steps": ["escapement design", "gear ratios 60:1", "pendulum period", "test accuracy"], "time": "40h", "level": "advanced", "safety": "escapement geometry is fiddly — prototype"},
  {"kind": "diy", "t": "Automated Factory Line", "tier": "Advanced", "notes": "no mains power", "mats": [["technic", "1", 150.0], ["motors", "3", 60.0], ["sensors", "1", 0.0]], "tools": ["none"], "steps": ["conveyor stages", "each station task", "synchronize", "run demo"], "time": "50h", "level": "advanced", "safety": "wire motors safely"},
  {"kind": "diy", "t": "Bridge: 6-Foot Span", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["bricks", "1", 80.0]], "tools": ["none"], "steps": ["truss design", "test sections", "assemble span", "load test"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "LEGO Computer Case Mod", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["case", "1", 60.0], ["bricks", "1", 40.0]], "tools": ["screwdriver"], "steps": ["measure case", "brick shell panels", "ventilation gaps", "assemble"], "time": "16h", "level": "advanced", "safety": "ventilation gaps mandatory — heat kills PCs"},
  {"kind": "diy", "t": "Stop-Motion Armature Rig", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 50.0], ["camera", "1", 0.0]], "tools": ["none"], "steps": ["jointed armature", "tie-downs", "frame-by-frame", "test walk"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Marble Run Machine", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 70.0], ["marbles", "1", 8.0]], "tools": ["none"], "steps": ["lift mechanism", "track switches", "continuous loop", "tune"], "time": "30h", "level": "advanced", "safety": "tune one section at a time"},
  {"kind": "diy", "t": "Working V8 Engine Model", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 90.0]], "tools": ["none"], "steps": ["crankshaft", "pistons 8", "timing", "hand-crank runs"], "time": "35h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Modular City Block", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["parts", "1", 200.0], ["baseplates", "4", 48.0]], "tools": ["none"], "steps": ["road plates", "4 modules pinned", "interiors", "lighting"], "time": "60h", "level": "advanced", "safety": "standardize the pin positions"},
  {"kind": "diy", "t": "LEGO Kinetic Sculpture", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["technic", "1", 100.0], ["motor", "1", 20.0]], "tools": ["none"], "steps": ["cam program", "followers", "balanced motion", "base"], "time": "30h", "level": "advanced", "safety": "balance rotating masses"},
  {"kind": "diy", "t": "Brick-Built Guitar (Playable)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["bricks", "1", 60.0], ["strings", "1", 8.0], ["tuners", "1", 10.0]], "tools": ["none"], "steps": ["body hollow", "neck reinforced", "bridge placement", "tune and play"], "time": "25h", "level": "advanced", "safety": "string tension — reinforce neck heavily"},
  {"kind": "diy", "t": "Amusement Park Ride", "tier": "Advanced", "notes": "pinch points guarded", "mats": [["technic", "1", 130.0], ["motor", "1", 20.0]], "tools": ["none"], "steps": ["ride mechanism", "safety bar", "motor drive", "test"], "time": "40h", "level": "advanced", "safety": "low speed"}
];
var TIPS=["Cut everything before you glue anything.", "Dry-fit twice, fasten once.", "Sharp tools are safe tools \u2014 hone before you start.", "Finish scraps first to test color.", "Label your parts as you cut them.", "Take a photo before disassembly for reference."];
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

