(function(){'use strict';
/* JAH The Model-Making Universe — real working generator, jahdb-db-model-making-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDM-";
var SLUG="db-model-making";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "First Plastic Kit: Snap-Fit Car", "tier": "Foundations", "notes": "decal water not drinkable", "mats": [["snap kit", "1", 18.0], ["sprue cutters", "1", 10.0], ["sandpaper", "1", 4.0]], "tools": ["cutters"], "steps": ["cut parts from sprue", "sand nubs", "snap together", "decals in water"], "time": "4h", "level": "beginner", "safety": "cut away from fingers"},
  {"kind": "diy", "t": "Painting Basics: Brush Control", "tier": "Foundations", "notes": "wash brushes promptly", "mats": [["practice model", "1", 12.0], ["acrylic set", "1", 15.0], ["brushes", "5", 10.0], ["palette", "1", 4.0]], "tools": ["brushes"], "steps": ["thin paints (milk consistency)", "basecoat smooth", "layer highlights", "wash recesses"], "time": "6h", "level": "beginner", "safety": "ventilate"},
  {"kind": "diy", "t": "Wood Ship Hull Planking (Intro)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["balsa hull kit", "1", 25.0], ["wood glue", "1", 5.0], ["pins", "1", 3.0], ["sandpaper", "1", 4.0]], "tools": ["knife", "pins"], "steps": ["pin first plank", "glue subsequent planks", "sand fair", "seal"], "time": "10h", "level": "beginner", "safety": "knife safety"},
  {"kind": "diy", "t": "Paper Model: Simple Building", "tier": "Foundations", "notes": "mat protection", "mats": [["printed kit", "1", 8.0], ["glue stick", "1", 3.0], ["craft knife", "1", 7.0], ["cutting mat", "1", 9.0]], "tools": ["knife"], "steps": ["score fold lines", "cut precisely", "fold and glue tabs", "weight while drying"], "time": "3h", "level": "beginner", "safety": "fresh blades"},
  {"kind": "diy", "t": "Clay Figure: Basic Humanoid", "tier": "Foundations", "notes": "ventilate oven", "mats": [["polymer clay 4 colors", "1", 16.0], ["clay tools", "1", 10.0], ["baking tray", "1", 0.0]], "tools": ["tools"], "steps": ["armature of foil", "build masses", "cure 275F 15min per 1/4in", "cool slowly"], "time": "5h", "level": "beginner", "safety": "dedicated clay baking tray — not food tray"},
  {"kind": "diy", "t": "Foam Terrain Tile", "tier": "Foundations", "notes": "flock dust mask", "mats": [["foam board", "2", 8.0], ["paint", "1", 8.0], ["flock", "1", 6.0], ["glue", "1", 4.0]], "tools": ["knife"], "steps": ["cut tile 12in", "carve texture", "paint base", "flock while wet"], "time": "4h", "level": "beginner", "safety": "knife safety"},
  {"kind": "diy", "t": "Simple Diorama Base", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wood plaque", "1", 8.0], ["ground paste", "1", 10.0], ["static grass", "1", 7.0]], "tools": ["spatula"], "steps": ["spread ground paste", "press texture", "static grass", "seal"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Decal Application Mastery", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["decals sheet", "1", 8.0], ["setting solution", "1", 7.0], ["tweezers", "1", 5.0]], "tools": ["tweezers"], "steps": ["gloss coat first", "slide decal", "setting solution", "seal flat"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Weathering with Washes", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["model", "1", 15.0], ["wash set", "1", 12.0], ["matte varnish", "1", 8.0]], "tools": ["brush"], "steps": ["gloss base first", "wash into recesses", "wipe high points", "matte seal"], "time": "3h", "level": "beginner", "safety": "ventilate varnish"},
  {"kind": "diy", "t": "Kitbashing: Two Kits One Model", "tier": "Foundations", "notes": "putty fumes ventilate", "mats": [["kits", "2", 40.0], ["saw", "1", 9.0], ["putty", "1", 8.0]], "tools": ["saw"], "steps": ["plan the merge", "cut donor parts", "putty seams", "sand and prime"], "time": "8h", "level": "beginner", "safety": "saw safety"},
  {"kind": "diy", "t": "Resin Casting: Simple Parts", "tier": "Compounded", "notes": "gloves mandatory", "mats": [["silicone mold kit", "1", 25.0], ["resin", "1", 20.0], ["cups/sticks", "1", 5.0], ["gloves", "1", 4.0]], "tools": ["none"], "steps": ["build mold box", "mix silicone 1:1", "pour over master", "demold, cast resin"], "time": "6h", "level": "intermediate", "safety": "resin fumes — respirator and ventilation"},
  {"kind": "diy", "t": "Photo-Etch Basics", "tier": "Compounded", "notes": "debonder handy", "mats": [["PE set", "1", 18.0], ["CA glue", "1", 6.0], ["PE bender", "1", 22.0], ["tweezers", "1", 8.0]], "tools": ["bender"], "steps": ["fold on bender", "CA tiny dots", "attach to model", "prime"], "time": "5h", "level": "intermediate", "safety": "CA glue — ventilation, avoid skin bonding"},
  {"kind": "diy", "t": "Airbrush Fundamentals", "tier": "Compounded", "notes": "respirator for enamels/lacquers", "mats": [["airbrush kit", "1", 90.0], ["compressor", "1", 120.0], ["paint", "1", 20.0], ["cleaner", "1", 8.0]], "tools": ["airbrush"], "steps": ["thin paint properly", "practice dots and lines", "basecoat model", "clean immediately"], "time": "10h", "level": "intermediate", "safety": "spray booth or outdoor"},
  {"kind": "diy", "t": "Scratch-Built Structure", "tier": "Compounded", "notes": "solvent glue ventilate", "mats": [["styrene sheets", "1", 18.0], ["glue", "1", 6.0], ["plans", "1", 0.0], ["knife", "1", 7.0]], "tools": ["knife"], "steps": ["draft plans", "cut walls", "brace corners", "detail and paint"], "time": "14h", "level": "intermediate", "safety": "knife safety"},
  {"kind": "diy", "t": "Figure Painting: Faces", "tier": "Compounded", "notes": "thin paints", "mats": [["figure", "1", 20.0], ["fine brushes", "1", 14.0], ["paints", "1", 18.0]], "tools": ["brush"], "steps": ["base skin tone", "shadow and highlight", "eyes last (tiny dots)", "seal"], "time": "8h", "level": "intermediate", "safety": "magnifier helps"},
  {"kind": "diy", "t": "Ship Rigging: Intro", "tier": "Compounded", "notes": "work top-down", "mats": [["ship kit", "1", 45.0], ["rigging thread", "1", 6.0], ["tweezers", "1", 8.0], ["beeswax", "1", 3.0]], "tools": ["tweezers"], "steps": ["plan rigging order", "wax thread", "standing rigging first", "running rigging last"], "time": "16h", "level": "intermediate", "safety": "patience"},
  {"kind": "diy", "t": "Armor Weathering: Chipping", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank kit", "1", 35.0], ["chipping fluid", "1", 10.0], ["paints", "1", 15.0]], "tools": ["brush"], "steps": ["base rust color", "chipping fluid", "top coat", "activate chips with water"], "time": "8h", "level": "intermediate", "safety": "ventilate"},
  {"kind": "diy", "t": "Vacuum-Formed Canopy", "tier": "Compounded", "notes": "ventilate", "mats": [["vacuum former or DIY", "1", 30.0], ["plastic sheet", "1", 8.0], ["master", "1", 0.0]], "tools": ["former"], "steps": ["heat plastic", "form over master", "trim canopy", "polish"], "time": "4h", "level": "intermediate", "safety": "heat safety — gloves"},
  {"kind": "diy", "t": "LED Lighting a Model", "tier": "Compounded", "notes": "lead-free solder; low voltage only", "mats": [["LEDs", "10", 8.0], ["resistors", "1", 4.0], ["battery box", "1", 5.0], ["wire", "1", 5.0], ["solder kit", "1", 20.0]], "tools": ["soldering iron"], "steps": ["plan circuit", "resistor per LED", "solder joints", "hide battery"], "time": "8h", "level": "intermediate", "safety": "soldering iron burns"},
  {"kind": "diy", "t": "Water Effects: Pond", "tier": "Compounded", "notes": "gloves", "mats": [["resin water", "1", 16.0], ["pond base", "1", 8.0], ["paint", "1", 6.0]], "tools": ["none"], "steps": ["paint depth gradient", "pour thin layers", "tint layers", "cure fully"], "time": "6h", "level": "intermediate", "safety": "resin fumes ventilate"},
  {"kind": "diy", "t": "3D-Printed Detail Parts", "tier": "Compounded", "notes": "ventilate printer area", "mats": [["printer access", "1", 0.0], ["PLA", "1", 22.0], ["calipers", "1", 12.0]], "tools": ["printer"], "steps": ["measure kit part", "model in CAD", "slicing: 0.12mm layers", "print and test fit"], "time": "8h", "level": "intermediate", "safety": "print times are estimates — a 2in part at 0.12mm ≈ 1-2h"},
  {"kind": "diy", "t": "Diorama Storytelling", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 12.0], ["figures", "5", 25.0], ["groundwork", "1", 15.0]], "tools": ["varies"], "steps": ["sketch the story", "composition triangle", "groundwork", "figures interact"], "time": "16h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Metal Barrel Replacement", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["brass barrels", "1", 14.0], ["drill bits", "1", 10.0], ["pin vise", "1", 12.0]], "tools": ["pin vise"], "steps": ["drill out plastic", "fit brass", "align carefully", "glue"], "time": "4h", "level": "advanced", "safety": "tiny drill bits break — light pressure"},
  {"kind": "diy", "t": "Full Rigged Ship", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["ship kit", "1", 80.0], ["rigging", "1", 10.0], ["blocks", "50", 20.0], ["sails cloth", "1", 12.0]], "tools": ["tweezers"], "steps": ["hull and decks", "masts stepped", "standing rigging", "running rigging, sails"], "time": "60h", "level": "advanced", "safety": "months-long project — pace yourself"},
  {"kind": "diy", "t": "Competition Figure", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["figure kit", "1", 40.0], ["paints", "1", 30.0], ["base", "1", 15.0]], "tools": ["airbrush", "brush"], "steps": ["prep flawless", "airbrush blends", "hand detail", "base scene"], "time": "40h", "level": "advanced", "safety": "photograph progress for critique"},
  {"kind": "diy", "t": "Scratch-Built Locomotive", "tier": "Advanced", "notes": "test electrics low-voltage", "mats": [["plans", "1", 15.0], ["brass stock", "1", 40.0], ["solder", "1", 10.0], ["motor", "1", 25.0]], "tools": ["soldering"], "steps": ["frame and drivers", "boiler and cab", "motor install", "test and detail"], "time": "80h", "level": "advanced", "safety": "soldering ventilation"},
  {"kind": "diy", "t": "Museum-Quality Armor", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kit", "1", 60.0], ["PE", "1", 25.0], ["resin wheels", "1", 18.0], ["paints", "1", 25.0]], "tools": ["airbrush"], "steps": ["PE interior", "perfect seams", "modulation painting", "pigment weathering"], "time": "50h", "level": "advanced", "safety": "reference photos essential"},
  {"kind": "diy", "t": "Working RC Conversion", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kit", "1", 35.0], ["RC gear", "1", 80.0], ["servo", "1", 15.0], ["battery", "1", 20.0]], "tools": ["soldering"], "steps": ["plan drivetrain", "install motor/servo", "wire receiver", "test range"], "time": "30h", "level": "advanced", "safety": "LiPo safety — charge supervised, storage bag"},
  {"kind": "diy", "t": "Large-Scale Aircraft", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["1", "32 kit", 120.0], ["PE", "1", 30.0], ["paints", "1", 30.0]], "tools": ["airbrush"], "steps": ["cockpit detail", "seams eliminated", "rivet detail", "natural metal finish"], "time": "60h", "level": "advanced", "safety": "NMF shows every flaw — prep is everything"},
  {"kind": "diy", "t": "Master Diorama", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["base large", "1", 25.0], ["kits", "3", 90.0], ["figures", "12", 60.0], ["materials", "1", 40.0]], "tools": ["full bench"], "steps": ["concept sketch", "build in layers", "unify lighting", "photograph"], "time": "80h", "level": "advanced", "safety": "largest commitment — plan in phases"},
  {"kind": "diy", "t": "Brass Etch Locomotive", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["etch kit", "1", 150.0], ["solder", "1", 12.0], ["motor", "1", 30.0]], "tools": ["soldering"], "steps": ["fold etch carefully", "solder frames", "add motor", "paint and line"], "time": "70h", "level": "advanced", "safety": "etched brass is sharp — handle with care"},
  {"kind": "diy", "t": "Figure Sculpt from Scratch", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["armature wire", "1", 8.0], ["epoxy putty", "1", 18.0], ["sculpt tools", "1", 20.0]], "tools": ["tools"], "steps": ["wire armature", "bulk with putty", "refine anatomy", "mold or paint"], "time": "40h", "level": "advanced", "safety": "anatomy reference required"},
  {"kind": "diy", "t": "Waterline Ship Diorama", "tier": "Advanced", "notes": "ventilate", "mats": [["ship kit", "1", 50.0], ["sea base", "1", 20.0], ["resin", "1", 20.0], ["figures", "1", 25.0]], "tools": ["none"], "steps": ["waterline hull", "sea sculpted", "wake effects", "figures on deck"], "time": "45h", "level": "advanced", "safety": "resin layers thin"},
  {"kind": "diy", "t": "Cutaway Technical Model", "tier": "Advanced", "notes": "preserve alignment", "mats": [["kit", "1", 40.0], ["saw", "1", 12.0], ["interior detail", "1", 30.0]], "tools": ["saw"], "steps": ["plan cut lines", "saw carefully", "detail interior", "display cutaway"], "time": "35h", "level": "advanced", "safety": "saw safety"}
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

