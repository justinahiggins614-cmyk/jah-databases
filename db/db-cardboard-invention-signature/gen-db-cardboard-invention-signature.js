(function(){'use strict';
/* JAH The Cardboard Invention Database — real working generator, jahdb-db-cardboard-invention-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CIS-";
var SLUG="db-cardboard-invention";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Cardboard Stool (Honeycomb)", "tier": "Foundations", "notes": "test 150lb before sitting", "mats": [["large boxes", "3", 0.0], ["glue gun + sticks", "1", 10.0], ["box cutter", "1", 7.0]], "tools": ["cutter"], "steps": ["cut strips 4in wide", "roll honeycomb coils", "glue coils into block", "top with double cardboard"], "time": "3h", "level": "beginner", "safety": "cutter safety"},
  {"kind": "diy", "t": "Desk Organizer Trays", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cereal boxes", "4", 0.0], ["washi tape", "1", 4.0], ["glue", "1", 3.0]], "tools": ["cutter"], "steps": ["cut boxes to tray height", "wrap with tape", "label each", "nest in drawer"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Play Oven", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["large box", "1", 0.0], ["paint", "1", 8.0], ["foil", "1", 3.0], ["knobs", "1", 4.0]], "tools": ["cutter"], "steps": ["cut door flap", "foil windows", "paint exterior", "knob dials"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Storage Bins with Handles", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["boxes", "4", 0.0], ["tape", "1", 4.0], ["labels", "1", 3.0]], "tools": ["cutter"], "steps": ["reinforce corners with tape", "cut handle slots", "label fronts", "stack"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Laptop Stand", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["glue", "1", 3.0]], "tools": ["cutter"], "steps": ["cut side profiles", "slot-fit cross brace", "test angle", "reinforce"], "time": "1h", "level": "beginner", "safety": "keep vents clear — overheating risk"},
  {"kind": "diy", "t": "Marble Maze", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["shallow box", "1", 0.0], ["straws", "1", 3.0], ["marble", "1", 1.0], ["glue", "1", 3.0]], "tools": ["cutter"], "steps": ["glue straw walls", "design path", "start and finish holes", "tilt to play"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Costume Armor", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["boxes", "3", 0.0], ["paint", "1", 8.0], ["elastic", "1", 4.0]], "tools": ["cutter"], "steps": ["cut chest and back plates", "shoulder pieces", "paint metallic", "elastic straps"], "time": "6h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Seed Starting Trays", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["toilet rolls", "20", 0.0], ["tray", "1", 3.0], ["soil", "1", 5.0]], "tools": ["scissors"], "steps": ["cut rolls in half", "fold bottoms", "fill with soil", "sow seeds"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Wall-Mount Mail Sorter", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["boxes", "3", 0.0], ["glue", "1", 3.0], ["labels", "1", 2.0]], "tools": ["cutter"], "steps": ["cut uniform slots", "stack and glue", "label each", "mount or stand"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Picture Frames", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["box panels", "4", 0.0], ["paint", "1", 5.0], ["tape", "1", 3.0]], "tools": ["cutter"], "steps": ["cut frame shape", "layer for thickness", "paint", "tape photo behind"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cat Scratcher Lounge", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["boxes", "5", 0.0], ["glue", "1", 4.0], ["catnip", "1", 3.0]], "tools": ["cutter"], "steps": ["cut 3in strips", "roll tight coils", "glue into pad", "sprinkle catnip"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Slot-Together Shelf Unit", "tier": "Compounded", "notes": "test with books gradually", "mats": [["double-wall boxes", "6", 0.0], ["glue", "1", 5.0], ["ruler", "1", 0.0]], "tools": ["cutter"], "steps": ["cut shelf boards", "slot-fit uprights (half-lap)", "no-glue assembly", "test load"], "time": "5h", "level": "intermediate", "safety": "half-lap slots must be snug"},
  {"kind": "diy", "t": "Cardboard Chair (Structural)", "tier": "Compounded", "notes": "test slowly to 200lb", "mats": [["triple-wall or layered", "8", 0.0], ["wood glue", "1", 8.0], ["clamps", "1", 15.0]], "tools": ["cutter"], "steps": ["laminate 3 layers for legs", "corrugated direction vertical", "glue and clamp 24h", "assemble"], "time": "10h", "level": "intermediate", "safety": "corrugation vertical = strength"},
  {"kind": "diy", "t": "Play Kitchen Full Set", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["appliance boxes", "3", 0.0], ["paint", "1", 10.0], ["faucet toy", "1", 6.0], ["knobs", "1", 5.0]], "tools": ["cutter"], "steps": ["fridge, stove, sink boxes", "paint each", "details glued", "arrange"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Loom", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["notches cut", "1", 0.0], ["yarn", "1", 6.0]], "tools": ["cutter"], "steps": ["cut notches top/bottom", "warp threads", "weave weft", "finish edges"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Pinhole Camera", "tier": "Compounded", "notes": "total darkness seal test", "mats": [["small box", "1", 0.0], ["foil", "1", 2.0], ["photo paper", "1", 12.0], ["tape", "1", 3.0]], "tools": ["pin"], "steps": ["light-seal box", "pinhole in foil", "load paper in dark", "expose and develop"], "time": "5h", "level": "intermediate", "safety": "darkroom needed for loading"},
  {"kind": "diy", "t": "Cardboard Guitar (Playable-ish)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["strings", "1", 8.0], ["dowel", "1", 3.0], ["tuning pegs", "1", 6.0]], "tools": ["cutter"], "steps": ["soundbox from box", "neck dowel", "bridge and nut", "tune carefully"], "time": "8h", "level": "intermediate", "safety": "string tension low — cardboard neck bends"},
  {"kind": "diy", "t": "Storage Ottoman", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box large", "1", 0.0], ["foam", "1", 15.0], ["fabric 2yd", "1", 16.0], ["staples", "1", 5.0]], "tools": ["staple gun"], "steps": ["reinforce box", "foam top", "wrap fabric", "staple under"], "time": "6h", "level": "intermediate", "safety": "staple gun safety"},
  {"kind": "diy", "t": "Cardboard Dollhouse", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["boxes", "4", 0.0], ["paint", "1", 8.0], ["wallpaper samples", "1", 5.0]], "tools": ["cutter"], "steps": ["2-story layout", "cut windows/doors", "wallpaper rooms", "furnish"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Desk with Cable Management", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["boxes", "4", 0.0], ["grommets", "1", 6.0], ["paint", "1", 8.0]], "tools": ["cutter"], "steps": ["desktop double-layer", "leg boxes slotted", "cable holes", "paint"], "time": "8h", "level": "intermediate", "safety": "double-layer top for monitors"},
  {"kind": "diy", "t": "Cardboard Arcade Cabinet", "tier": "Compounded", "notes": "ventilation slots", "mats": [["large boxes", "4", 0.0], ["buttons kit", "1", 25.0], ["paint", "1", 10.0]], "tools": ["cutter"], "steps": ["cabinet profile cut", "monitor shelf", "control panel angled", "paint and art"], "time": "16h", "level": "intermediate", "safety": "monitor secured"},
  {"kind": "diy", "t": "Geodesic Play Dome", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardboard triangles", "60", 0.0], ["tape reinforced", "1", 10.0]], "tools": ["cutter"], "steps": ["cut equilateral triangles", "tape into pent/hex clusters", "assemble dome", "door opening"], "time": "14h", "level": "advanced", "safety": "large structure — adult supervision for kids inside"},
  {"kind": "diy", "t": "Cardboard Boat (Floats!)", "tier": "Advanced", "notes": "seal is everything", "mats": [["waxed boxes or seal", "1", 15.0], ["tape", "1", 8.0], ["paint seal", "1", 12.0]], "tools": ["cutter"], "steps": ["hull shape folded", "seal every seam", "test in shallow water", "reinforce"], "time": "12h", "level": "advanced", "safety": "test near shore with life jackets"},
  {"kind": "diy", "t": "Full-Size Cardboard Bed", "tier": "Advanced", "notes": "test gradually", "mats": [["triple-wall sheets", "10", 30.0], ["glue", "1", 10.0], ["bolts", "1", 8.0]], "tools": ["cutter"], "steps": ["slat grid design", "legs corrugated vertical", "bolt joints", "test 300lb"], "time": "16h", "level": "advanced", "safety": "engineer the slats — this holds a human"},
  {"kind": "diy", "t": "Cardboard Kayak", "tier": "Advanced", "notes": "calm water only", "mats": [["large sheets", "1", 25.0], ["waterproof tape", "1", 15.0], ["sealant", "1", 18.0]], "tools": ["cutter"], "steps": ["stitch-and-glue hull", "tape seams", "3 seal coats", "float test"], "time": "20h", "level": "advanced", "safety": "wear life jacket on first float"},
  {"kind": "diy", "t": "Vending Machine Prop", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["boxes", "5", 0.0], ["acrylic", "1", 12.0], ["paint", "1", 10.0], ["LED", "1", 8.0]], "tools": ["cutter"], "steps": ["cabinet with window", "coil mechanism mock", "shelves stocked", "lights"], "time": "18h", "level": "advanced", "safety": "low-voltage LED only"},
  {"kind": "diy", "t": "Cardboard Castle (Walk-In)", "tier": "Advanced", "notes": "keep away from heaters", "mats": [["wardrobe boxes", "8", 0.0], ["tape", "1", 12.0], ["paint", "1", 15.0]], "tools": ["cutter"], "steps": ["wall panels", "battlements cut", "tower corners", "paint stone"], "time": "20h", "level": "advanced", "safety": "adult-supervised"},
  {"kind": "diy", "t": "Pinball Machine", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["boxes", "4", 0.0], ["marble", "1", 2.0], ["rubber bands", "1", 4.0], ["paint", "1", 8.0]], "tools": ["cutter"], "steps": ["playfield sloped", "flipper levers", "bumpers and ramps", "score by hand"], "time": "16h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Furniture Set", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["sheets", "12", 35.0], ["glue", "1", 12.0], ["edgebanding", "1", 10.0]], "tools": ["cutter"], "steps": ["table + 2 chairs", "uniform slot system", "glue critical joints", "finish edges"], "time": "24h", "level": "advanced", "safety": "test each piece to rated load"},
  {"kind": "diy", "t": "Rube Goldberg from Boxes", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["boxes", "6", 0.0], ["ramps", "1", 5.0], ["balls", "1", 6.0], ["tape", "1", 5.0]], "tools": ["cutter"], "steps": ["plan chain", "ramps and funnels", "triggers", "test each link"], "time": "14h", "level": "advanced", "safety": "test links independently before chaining"},
  {"kind": "diy", "t": "Cardboard Greenhouse", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["boxes", "8", 0.0], ["clear plastic", "1", 20.0], ["tape", "1", 10.0]], "tools": ["cutter"], "steps": ["frame from boxes", "plastic glazing", "door flap", "vent top"], "time": "12h", "level": "advanced", "safety": "anchor against wind"},
  {"kind": "diy", "t": "Giant Cardboard Robot", "tier": "Advanced", "notes": "joints reinforced", "mats": [["appliance boxes", "4", 0.0], ["foil", "1", 6.0], ["paint", "1", 12.0], ["LED", "1", 10.0]], "tools": ["cutter"], "steps": ["torso box", "limb boxes jointed", "foil details", "LED eyes"], "time": "16h", "level": "advanced", "safety": "low-voltage LED"},
  {"kind": "diy", "t": "Cardboard Sailboat Model", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["sheets", "1", 15.0], ["dowel mast", "1", 4.0], ["fabric sail", "1", 8.0], ["glue", "1", 6.0]], "tools": ["cutter"], "steps": ["hull built up", "deck fitted", "mast stepped", "rig sail"], "time": "18h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Modular Cardboard Wall", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["boxes", "12", 0.0], ["brackets", "1", 15.0], ["paint", "1", 20.0]], "tools": ["cutter"], "steps": ["uniform modules", "interlocking tabs", "paint scheme", "assemble wall"], "time": "22h", "level": "advanced", "safety": "anchor to wall studs"}
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

