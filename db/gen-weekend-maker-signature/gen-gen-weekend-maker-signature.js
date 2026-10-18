(function(){'use strict';
/* JAH The Weekend Maker Database — real working generator, jahdb-gen-weekend-maker-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WMS-";
var SLUG="gen-weekend-maker";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Floating Shelves (Set of 3)", "tier": "Foundations", "notes": "level everything", "mats": [["pine boards", "3", 24.0], ["brackets", "1", 18.0], ["screws", "1", 5.0], ["stain", "1", 9.0]], "tools": ["drill", "level"], "steps": ["cut to length", "sand 120", "stain", "mount to studs"], "time": "6h", "level": "beginner", "safety": "anchor to studs"},
  {"kind": "diy", "t": "Raised Garden Bed", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cedar 2x6x8", "4", 48.0], ["screws", "1", 8.0], ["soil 8cuft", "1", 32.0]], "tools": ["drill", "saw"], "steps": ["cut boards", "screw corners", "level ground", "fill soil"], "time": "5h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Fire Pit (Block)", "tier": "Foundations", "notes": "10ft from structures", "mats": [["blocks", "30", 90.0], ["gravel", "1", 15.0], ["adhesive", "1", 12.0]], "tools": ["shovel"], "steps": ["level circle", "gravel base", "stack 3 courses", "adhesive"], "time": "6h", "level": "beginner", "safety": "check burn bans"},
  {"kind": "diy", "t": "Mudroom Bench", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["2x4x8", "4", 20.0], ["plywood", "1", 25.0], ["screws", "1", 8.0], ["hooks", "1", 12.0]], "tools": ["saw", "drill"], "steps": ["frame", "top", "cubbies", "hooks"], "time": "8h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Garden Trellis", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cedar slats", "1", 25.0], ["screws", "1", 6.0]], "tools": ["saw", "drill"], "steps": ["cut slats", "lattice pattern", "posts", "install"], "time": "5h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Workshop Pegboard Wall", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["pegboard", "1", 25.0], ["hooks", "1", 15.0], ["furring", "1", 10.0]], "tools": ["drill"], "steps": ["furring strips", "mount board", "hooks", "organize"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Outdoor Planter Boxes", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cedar", "1", 35.0], ["screws", "1", 7.0], ["soil", "1", 15.0]], "tools": ["saw", "drill"], "steps": ["cut", "assemble", "drainage", "plant"], "time": "6h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Closet System Refresh", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["shelving", "1", 60.0], ["rods", "1", 20.0], ["brackets", "1", 15.0]], "tools": ["drill"], "steps": ["demo old", "mount standards", "shelves", "rods"], "time": "8h", "level": "beginner", "safety": "anchor to studs"},
  {"kind": "diy", "t": "Backyard Cornhole Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["plywood", "1", 30.0], ["2x4", "1", 12.0], ["bags", "1", 20.0], ["paint", "1", 10.0]], "tools": ["saw"], "steps": ["cut tops", "frames", "legs", "paint"], "time": "8h", "level": "beginner", "safety": "saw safety"},
  {"kind": "diy", "t": "Entryway Coat Rack", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["board", "1", 15.0], ["hooks", "5", 20.0], ["screws", "1", 4.0]], "tools": ["drill"], "steps": ["cut", "sand", "hooks", "mount studs"], "time": "4h", "level": "beginner", "safety": "hit studs"},
  {"kind": "diy", "t": "Window Boxes", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cedar", "1", 28.0], ["screws", "1", 6.0], ["brackets", "1", 14.0], ["soil", "1", 10.0]], "tools": ["saw", "drill"], "steps": ["build boxes", "brackets", "mount", "plant"], "time": "6h", "level": "beginner", "safety": "secure brackets — soil is heavy wet"},
  {"kind": "diy", "t": "Deck Storage Bench", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cedar", "1", 80.0], ["hinges", "1", 15.0], ["screws", "1", 10.0], ["sealer", "1", 18.0]], "tools": ["saw", "drill"], "steps": ["frame", "hinged lid", "slats", "seal"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Pergola (Small)", "tier": "Compounded", "notes": "posts plumb", "mats": [["posts 4x4x10", "4", 80.0], ["beams", "1", 60.0], ["screws", "1", 20.0], ["concrete", "1", 30.0]], "tools": ["post hole digger"], "steps": ["dig 3ft", "set posts", "beams", "rafters"], "time": "16h", "level": "intermediate", "safety": "call 811 before digging"},
  {"kind": "diy", "t": "Chicken Coop", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["lumber", "1", 120.0], ["hardware cloth", "1", 40.0], ["hinges", "1", 15.0], ["roofing", "1", 35.0]], "tools": ["saw", "drill"], "steps": ["frame", "wire walls", "roof", "door"], "time": "20h", "level": "intermediate", "safety": "hardware cloth not chicken wire — predators"},
  {"kind": "diy", "t": "Outdoor Kitchen Cart", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cedar", "1", 90.0], ["casters", "1", 30.0], ["screws", "1", 12.0], ["stain", "1", 15.0]], "tools": ["saw", "drill"], "steps": ["frame", "top", "storage", "casters"], "time": "14h", "level": "intermediate", "safety": "locking casters"},
  {"kind": "diy", "t": "Shed Shelving", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["2x4", "1", 40.0], ["plywood", "1", 35.0], ["screws", "1", 10.0]], "tools": ["saw", "drill"], "steps": ["uprights", "shelves", "level", "anchor"], "time": "10h", "level": "intermediate", "safety": "anchor to wall"},
  {"kind": "diy", "t": "Treehouse Platform", "tier": "Compounded", "notes": "railing 36in+; adult build", "mats": [["lumber", "1", 200.0], ["brackets", "1", 40.0], ["screws", "1", 25.0]], "tools": ["saw", "drill"], "steps": ["plan tree-safe", "platform", "railing", "ladder"], "time": "24h", "level": "intermediate", "safety": "TAB bolts for tree health"},
  {"kind": "diy", "t": "Greenhouse (Small Kit+)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["kit", "1", 250.0], ["base lumber", "1", 40.0], ["gravel", "1", 20.0]], "tools": ["drill"], "steps": ["level base", "assemble kit", "anchor", "vent"], "time": "16h", "level": "intermediate", "safety": "anchor against wind"},
  {"kind": "diy", "t": "Pizza Oven (Brick)", "tier": "Compounded", "notes": "cure slowly", "mats": [["firebrick", "100", 200.0], ["mortar", "1", 40.0], ["base blocks", "1", 60.0]], "tools": ["trowel"], "steps": ["base", "dome form", "brick dome", "cure fires"], "time": "24h", "level": "intermediate", "safety": "refractory mortar only"},
  {"kind": "diy", "t": "Rain Barrel System", "tier": "Compounded", "notes": "winter drain", "mats": [["barrels", "2", 60.0], ["diverter", "1", 35.0], ["spigots", "1", 15.0], ["stand", "1", 25.0]], "tools": ["drill"], "steps": ["stand", "diverter", "spigots", "overflow"], "time": "8h", "level": "intermediate", "safety": "mosquito screen"},
  {"kind": "diy", "t": "Compost Bin (3-Bay)", "tier": "Compounded", "notes": "turn schedule", "mats": [["pallets", "9", 0.0], ["screws", "1", 12.0]], "tools": ["drill"], "steps": ["bays", "slats front", "roof", "fill"], "time": "10h", "level": "intermediate", "safety": "HT pallets"},
  {"kind": "diy", "t": "Outdoor Shower", "tier": "Compounded", "notes": "hot water anti-scald", "mats": [["lumber", "1", 100.0], ["plumbing", "1", 80.0], ["fixture", "1", 60.0]], "tools": ["saw"], "steps": ["platform", "walls", "plumb", "drain"], "time": "20h", "level": "intermediate", "safety": "drain to approved"},
  {"kind": "diy", "t": "Full Deck Build (12x12)", "tier": "Advanced", "notes": "call 811; ledger flashing critical", "mats": [["lumber", "1", 900.0], ["concrete", "1", 120.0], ["screws", "1", 60.0], ["permit", "1", 150.0]], "tools": ["post hole digger"], "steps": ["permit", "footings", "frame", "decking, rails"], "time": "60h", "level": "advanced", "safety": "PERMIT + inspections"},
  {"kind": "diy", "t": "Workshop Shed (8x10)", "tier": "Advanced", "notes": "square every wall", "mats": [["lumber", "1", 800.0], ["roofing", "1", 200.0], ["siding", "1", 250.0], ["door", "1", 120.0]], "tools": ["saw"], "steps": ["foundation", "walls", "roof", "door"], "time": "80h", "level": "advanced", "safety": "permit likely"},
  {"kind": "diy", "t": "Treehouse (Full)", "tier": "Advanced", "notes": "safety rails", "mats": [["lumber", "1", 600.0], ["hardware", "1", 150.0], ["roofing", "1", 100.0]], "tools": ["saw"], "steps": ["design", "platform", "walls", "roof"], "time": "100h", "level": "advanced", "safety": "engineer review for big builds"},
  {"kind": "diy", "t": "Outdoor Kitchen (Built-In)", "tier": "Advanced", "notes": "permits", "mats": [["blocks", "1", 400.0], ["grill", "1", 500.0], ["counters", "1", 300.0]], "tools": ["trowel"], "steps": ["plan", "structure", "utilities", "finish"], "time": "80h", "level": "advanced", "safety": "gas pro for lines"},
  {"kind": "diy", "t": "Stone Patio", "tier": "Advanced", "notes": "slope away from house", "mats": [["pavers", "1", 600.0], ["base", "1", 200.0], ["edging", "1", 80.0]], "tools": ["tamper"], "steps": ["excavate", "base compact", "lay", "polymeric sand"], "time": "40h", "level": "advanced", "safety": "call 811"},
  {"kind": "diy", "t": "Retaining Wall", "tier": "Advanced", "notes": "drainage is everything", "mats": [["blocks", "1", 500.0], ["gravel", "1", 150.0], ["drain", "1", 40.0]], "tools": ["tamper"], "steps": ["trench", "base", "courses", "drain"], "time": "40h", "level": "advanced", "safety": "over 3ft = engineer"},
  {"kind": "diy", "t": "Barn-Style Shed", "tier": "Advanced", "notes": "help for roof day", "mats": [["lumber", "1", 1000.0], ["roofing", "1", 300.0], ["siding", "1", 300.0]], "tools": ["saw"], "steps": ["plans", "frame", "roof", "finish"], "time": "100h", "level": "advanced", "safety": "permit"},
  {"kind": "diy", "t": "Root Cellar", "tier": "Advanced", "notes": "ventilation", "mats": [["blocks", "1", 400.0], ["lumber", "1", 150.0], ["vents", "1", 40.0]], "tools": ["shovel"], "steps": ["dig", "walls", "roof", "vents"], "time": "60h", "level": "advanced", "safety": "structural — get guidance"},
  {"kind": "diy", "t": "Sauna (Barrel Kit+)", "tier": "Advanced", "notes": "ventilation", "mats": [["kit", "1", 2500.0], ["base", "1", 200.0], ["electrical", "1", 300.0]], "tools": ["drill"], "steps": ["base", "assemble", "wire (pro)", "bench"], "time": "40h", "level": "advanced", "safety": "electrician for heater"},
  {"kind": "diy", "t": "Dock/Pier Section", "tier": "Advanced", "notes": "life jackets on build days", "mats": [["lumber", "1", 500.0], ["hardware", "1", 150.0]], "tools": ["saw"], "steps": ["piles", "frame", "decking", "cleats"], "time": "60h", "level": "advanced", "safety": "waterway permits"},
  {"kind": "diy", "t": "Greenhouse (Large)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kit", "1", 1500.0], ["base", "1", 300.0]], "tools": ["drill"], "steps": ["permit?", "base", "assemble", "systems"], "time": "60h", "level": "advanced", "safety": "anchor + snow load rated"},
  {"kind": "diy", "t": "ADU Finish-Out", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [], "tools": ["varies"], "steps": ["permit", "frame", "systems", "finish"], "time": "200h", "level": "advanced", "safety": "permits + licensed trades for electrical/plumbing/HVAC"}
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

