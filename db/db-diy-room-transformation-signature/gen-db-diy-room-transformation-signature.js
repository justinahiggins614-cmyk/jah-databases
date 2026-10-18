(function(){'use strict';
/* JAH The DIY Room Transformation Database — real working generator, jahdb-db-diy-room-transformation-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DRTS-";
var SLUG="db-diy-room-transformation";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "One-Weekend Bedroom Refresh", "tier": "Foundations", "notes": "ladder safety for high walls", "mats": [["paint 1gal", "1", 35.0], ["bedding set", "1", 45.0], ["curtains", "2", 30.0], ["LED bulbs", "4", 12.0], ["wall hooks", "6", 10.0]], "tools": ["roller kit", "screwdriver", "drill"], "steps": ["declutter first (bag,box,donate)", "paint one accent wall", "s swap bedding and curtains", "install hooks for vertical storage", "reposition lamp for reading light"], "time": "8h", "level": "beginner", "safety": "ventilate while painting"},
  {"kind": "diy", "t": "Rental-Friendly Accent Wall", "tier": "Foundations", "notes": "landlord approval in writing", "mats": [["peel-and-stick wallpaper", "2rolls", 50.0], ["smoothing tool", "1", 8.0], ["utility knife", "1", 5.0]], "tools": ["ladder", "tape measure"], "steps": ["clean wall with damp cloth", "mark plumb line", "apply panels top-down smoothing bubbles", "trim at baseboard"], "time": "4h", "level": "beginner", "safety": "test adhesive on hidden spot"},
  {"kind": "diy", "t": "Entryway Drop Zone", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["coat hooks", "4", 16.0], ["bench or crate", "1", 25.0], ["tray for keys", "1", 8.0], ["basket", "1", 12.0]], "tools": ["drill", "level"], "steps": ["mount hooks at 60in height", "place bench below", "tray on bench for keys", "basket for mail"], "time": "3h", "level": "beginner", "safety": "anchor hooks to studs for coats"},
  {"kind": "diy", "t": "Closet-to-Office Nook", "tier": "Foundations", "notes": "keep cords off floor", "mats": [["shelf board", "1", 15.0], ["brackets", "2", 8.0], ["desk lamp", "1", 20.0], ["power strip", "1", 12.0]], "tools": ["drill", "screwdriver"], "steps": ["clear closet", "mount shelf at 30in as desk", "add lamp and power", "organize vertical storage above"], "time": "5h", "level": "beginner", "safety": "do not overload single shelf"},
  {"kind": "diy", "t": "Gallery Wall Layout", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["frames assorted", "8", 40.0], ["paper templates", "8", 0.0], ["painter tape", "1", 6.0], ["nails", "20", 3.0]], "tools": ["hammer", "level"], "steps": ["trace frames on paper,tape to wall", "arrange until balanced", "nail through template centers", "hang and level each"], "time": "4h", "level": "beginner", "safety": "hang heavy frames on studs or anchors"},
  {"kind": "diy", "t": "Bathroom Vanity Styling", "tier": "Foundations", "notes": "bucket under trap when disconnecting", "mats": [["new faucet set", "1", 45.0], ["mirror", "1", 30.0], ["towels", "4", 24.0], ["tray", "1", 10.0]], "tools": ["wrench", "screwdriver", "plumber tape"], "steps": ["shut water valves", "swap faucet (tape threads)", "hang mirror at eye level", "style towels and tray"], "time": "4h", "level": "beginner", "safety": "water shutoff first"},
  {"kind": "diy", "t": "Mudroom Boot Tray Station", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["boot tray", "1", 15.0], ["hooks", "4", 16.0], ["small rug", "1", 20.0]], "tools": ["drill"], "steps": ["tray by the door", "hooks above for leashes", "rug underfoot"], "time": "2h", "level": "beginner", "safety": "anchor hooks to studs"},
  {"kind": "diy", "t": "Reading Corner Build", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["armchair", "1", 80.0], ["floor lamp", "1", 35.0], ["side table", "1", 25.0], ["throw blanket", "1", 20.0]], "tools": ["none"], "steps": ["pick brightest corner", "chair angled to window", "lamp behind shoulder", "table within reach"], "time": "2h", "level": "beginner", "safety": "none — arrange, don't build"},
  {"kind": "diy", "t": "Hallway Runner Refresh", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["runner rug", "1", 60.0], ["rug tape", "1", 8.0], ["art", "3", 30.0]], "tools": ["none"], "steps": ["measure hall", "tape rug flat", "art at eye level 57in center"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Kitchen Open-Shelf Swap", "tier": "Compounded", "notes": "patch wall after removal", "mats": [["pine boards 2", "8ft", 24.0], ["brackets", "6", 18.0], ["screws", "1", 4.0], ["baskets", "3", 21.0]], "tools": ["drill", "stud finder", "level"], "steps": ["remove one upper cabinet door or cabinet", "mount brackets to studs", "set boards level", "style with daily dishes"], "time": "6h", "level": "intermediate", "safety": "cabinets are heavy — two people"},
  {"kind": "diy", "t": "Small-Bathroom Big Impact", "tier": "Compounded", "notes": "if wiring confuses you, call an electrician", "mats": [["peel stick tile 20sqft", "1", 60.0], ["new mirror", "1", 40.0], ["vanity light", "1", 55.0], ["caulk", "1", 6.0]], "tools": ["utility knife", "screwdriver", "caulk gun"], "steps": ["clean and degrease tile", "apply peel-stick over old tile", "swap mirror and light fixture", "re-caulk tub edge"], "time": "8h", "level": "intermediate", "safety": "ELECTRICAL: breaker off for light swap"},
  {"kind": "diy", "t": "Home Office That Works", "tier": "Compounded", "notes": "monitor arm must clamp to solid desk", "mats": [["desk 48in", "1", 90.0], ["ergonomic chair", "1", 120.0], ["monitor arm", "1", 40.0], ["rug 5x7", "1", 60.0]], "tools": ["drill", "wrench"], "steps": ["position desk facing door if possible", "mount monitor at eye level", "chair set so feet flat", "rug anchors the zone"], "time": "6h", "level": "intermediate", "safety": "lift with legs"},
  {"kind": "diy", "t": "Dining Room Warm-Up", "tier": "Compounded", "notes": "check dimmer-bulb compatibility", "mats": [["pendant light", "1", 70.0], ["table runner", "1", 18.0], ["chairs paint", "1qt", 14.0], ["centerpiece tray", "1", 15.0]], "tools": ["screwdriver", "brush"], "steps": ["swap light fixture (breaker off)", "paint chairs, dry 24h", "runner and tray centerpiece", "dimmer switch if compatible"], "time": "7h", "level": "intermediate", "safety": "breaker off for fixture"},
  {"kind": "diy", "t": "Kids Room That Grows", "tier": "Compounded", "notes": "guardrails mandatory; anchor to wall", "mats": [["loft bed", "1", 200.0], ["desk", "1", 60.0], ["bins", "6", 36.0], ["wall paint 1gal", "1", 35.0]], "tools": ["wrench", "drill", "roller"], "steps": ["assemble loft per manual", "desk tucks underneath", "bins labeled by category", "paint one wall together"], "time": "10h", "level": "intermediate", "safety": "follow bed manual exactly"},
  {"kind": "diy", "t": "Laundry Room Rescue", "tier": "Compounded", "notes": "lint trap cleaned", "mats": [["shelf boards", "2", 20.0], ["drying rack wall-mount", "1", 30.0], ["baskets", "3", 24.0], ["folding table", "1", 40.0]], "tools": ["drill", "level"], "steps": ["mount shelves above machines", "wall-mount drying rack", "baskets for sorting", "table for folding"], "time": "6h", "level": "intermediate", "safety": "keep clearance above dryer"},
  {"kind": "diy", "t": "Balcony to Outdoor Room", "tier": "Compounded", "notes": "secure items against wind", "mats": [["outdoor rug", "1", 45.0], ["string lights", "2", 25.0], ["planters", "4", 40.0], ["folding chairs", "2", 60.0]], "tools": ["none"], "steps": ["rug defines floor", "lights on railing hooks", "planters as green walls", "chairs angled for conversation"], "time": "5h", "level": "intermediate", "safety": "check balcony weight limits"},
  {"kind": "diy", "t": "Pantry Overhaul", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shelf risers", "3", 30.0], ["clear bins", "8", 40.0], ["labels", "1", 8.0], ["door rack", "1", 25.0]], "tools": ["none"], "steps": ["empty and wipe shelves", "group by category", "risers double stacking", "bins labeled, door rack for spices"], "time": "5h", "level": "intermediate", "safety": "check expiry dates while emptying"},
  {"kind": "diy", "t": "Garage Zone Makeover", "tier": "Compounded", "notes": "keep chemicals locked", "mats": [["pegboard 4x8", "2", 50.0], ["hooks set", "1", 20.0], ["bins", "6", 48.0], ["workbench", "1", 120.0]], "tools": ["drill", "level"], "steps": ["mount pegboard to studs", "zone: tools, sports, garden", "bins labeled high", "bench as project surface"], "time": "8h", "level": "intermediate", "safety": "heavy items low"},
  {"kind": "diy", "t": "Attic Reading Loft", "tier": "Compounded", "notes": "ventilation for comfort", "mats": [["rug", "1", 50.0], ["floor cushions", "4", 60.0], ["battery lights", "3", 24.0], ["low shelf", "1", 35.0]], "tools": ["none"], "steps": ["deep clean first", "rug and cushions define lounge", "battery lights (no wiring)", "low shelf for books"], "time": "4h", "level": "intermediate", "safety": "check floor load rating"},
  {"kind": "diy", "t": "Mudroom from Hallway", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["bench with cubbies", "1", 110.0], ["hooks", "6", 24.0], ["boot tray", "1", 15.0], ["mirror", "1", 30.0]], "tools": ["drill", "level"], "steps": ["bench against longest wall", "hooks above at 60in", "tray under bench", "mirror opposite for light"], "time": "6h", "level": "intermediate", "safety": "anchor bench to wall"},
  {"kind": "diy", "t": "Studio Apartment Zones", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["bookshelf divider", "1", 90.0], ["rug", "2", 80.0], ["curtain + rod", "1", 45.0], ["plants", "3", 36.0]], "tools": ["drill"], "steps": ["shelf divides sleep/living", "rugs define each zone", "curtain hides storage", "plants soften edges"], "time": "7h", "level": "intermediate", "safety": "keep pathways 30in+ clear"},
  {"kind": "diy", "t": "Spare Room to Guest Suite", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["bed frame", "1", 150.0], ["bedding", "1", 70.0], ["blackout curtains", "1", 40.0], ["luggage rack", "1", 35.0]], "tools": ["wrench", "drill"], "steps": ["frame centered on wall", "hotel-style bedding layers", "blackouts for sleep", "luggage rack + outlet station"], "time": "8h", "level": "intermediate", "safety": "none beyond assembly"},
  {"kind": "diy", "t": "Basement Family Lounge", "tier": "Advanced", "notes": "radon test recommended", "mats": [["carpet tiles 200sqft", "1", 220.0], ["sectional", "1", 600.0], ["media console", "1", 150.0], ["acoustic panels", "6", 90.0]], "tools": ["utility knife", "drill"], "steps": ["test for moisture first (tape test 48h)", "carpet tiles over dry floor", "sectional facing focal wall", "panels at reflection points"], "time": "20h", "level": "advanced", "safety": "moisture test mandatory — never finish a damp basement"},
  {"kind": "diy", "t": "Open-Plan Kitchen-Diner", "tier": "Advanced", "notes": "tile saw water and eye protection", "mats": [["island cart", "1", 250.0], ["pendants", "2", 140.0], ["stools", "3", 180.0], ["backsplash tile 30sqft", "1", 90.0]], "tools": ["tile saw", "drill", "screwdriver"], "steps": ["island defines kitchen edge", "pendants 30in above island", "stools tucked under", "tile backsplash weekend two"], "time": "24h", "level": "advanced", "safety": "breaker off for pendants"},
  {"kind": "diy", "t": "Primary Suite Retreat", "tier": "Advanced", "notes": "two-person headboard hang", "mats": [["paint 2gal", "1", 70.0], ["upholstered headboard", "1", 180.0], ["nightstands", "2", 120.0], ["dimmers", "2", 30.0]], "tools": ["roller", "drill", "screwdriver"], "steps": ["paint in calming tone", "headboard as focal point", "matching nightstands", "dimmers on bedside lamps (breaker off)"], "time": "16h", "level": "advanced", "safety": "breaker off for dimmers"},
  {"kind": "diy", "t": "Home Gym Corner", "tier": "Advanced", "notes": "keep egress clear", "mats": [["rubber flooring 100sqft", "1", 150.0], ["rack", "1", 300.0], ["bench", "1", 120.0], ["mirror 3x", "5", 80.0]], "tools": ["wrench", "drill"], "steps": ["flooring first (interlocking)", "rack bolted per manual", "bench and weights zoned", "mirror for form check"], "time": "12h", "level": "advanced", "safety": "rack must anchor to floor/wall per manual"},
  {"kind": "diy", "t": "Craft Room Command Center", "tier": "Advanced", "notes": "ventilation for paints/glues", "mats": [["worktables", "2", 160.0], ["pegboard wall", "1", 60.0], ["task lighting", "2", 70.0], ["storage drawers", "1", 110.0]], "tools": ["drill", "level"], "steps": ["tables in L-shape", "pegboard for tools", "task lights over work zones", "drawers sorted by craft"], "time": "14h", "level": "advanced", "safety": "task lighting wired safely"},
  {"kind": "diy", "t": "Teen Hangout Basement", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["sectional", "1", 500.0], ["LED strips", "3", 45.0], ["mini fridge", "1", 150.0]], "tools": ["drill"], "steps": ["zone: lounge + gaming", "LED behind furniture (low voltage)", "fridge on dedicated outlet", "sound dampening panels"], "time": "16h", "level": "advanced", "safety": "do not overload circuits — fridge + gaming on separate breakers ideally"},
  {"kind": "diy", "t": "Nursery That Converts", "tier": "Advanced", "notes": "no blankets/bumpers (safe sleep); anchor dresser", "mats": [["convertible crib", "1", 280.0], ["dresser/changer", "1", 200.0], ["glider", "1", 180.0], ["blackout", "1", 40.0]], "tools": ["wrench", "drill"], "steps": ["crib per manual, no drop-sides", "dresser doubles as changer", "glider near window", "blackouts + white noise"], "time": "12h", "level": "advanced", "safety": "crib slats <2-3/8in apart"},
  {"kind": "diy", "t": "Outdoor Kitchen Patio", "tier": "Advanced", "notes": "never under roof overhang; fire extinguisher nearby", "mats": [["grill", "1", 400.0], ["prep table", "1", 120.0], ["storage cabinet", "1", 150.0], ["string lights", "1", 30.0]], "tools": ["wrench", "drill"], "steps": ["grill 10ft from house", "prep zone beside grill", "weatherproof storage", "lights overhead"], "time": "14h", "level": "advanced", "safety": "gas grill clearances per manual"},
  {"kind": "diy", "t": "Whole-Home Paint Refresh", "tier": "Advanced", "notes": "ventilate; keep paint from heat sources", "mats": [["paint 8gal", "1", 280.0], ["roller kits", "3", 36.0], ["painter tape", "6", 30.0], ["drop cloths", "4", 40.0]], "tools": ["roller", "brush", "ladder"], "steps": ["one room at a time", "cut in then roll", "two coats minimum", "touch-ups last"], "time": "40h", "level": "advanced", "safety": "ladder safety"},
  {"kind": "diy", "t": "Attic to Bonus Room", "tier": "Advanced", "notes": "egress window for bedroom code; hire electrician for new circuits", "mats": [["insulation", "1", 200.0], ["drywall 20 sheets", "1", 240.0], ["flooring 300sqft", "1", 450.0], ["lighting", "1", 120.0]], "tools": ["drywall saw", "drill", "sander"], "steps": ["insulate between rafters", "drywall and tape seams", "flooring over subfloor", "add lighting (electrician)"], "time": "60h", "level": "advanced", "safety": "permits likely required"},
  {"kind": "diy", "t": "Garage to Studio Conversion", "tier": "Advanced", "notes": "check HOA rules", "mats": [["insulation", "1", 250.0], ["drywall", "1", 300.0], ["mini-split", "1", 1200.0], ["flooring", "1", 400.0]], "tools": ["varies"], "steps": ["insulate walls/ceiling", "drywall and finish", "mini-split for climate", "flooring last"], "time": "80h", "level": "advanced", "safety": "permits + HVAC pro required"},
  {"kind": "diy", "t": "Backyard Deck Refresh", "tier": "Advanced", "notes": "stain in shade, 50-90F", "mats": [["deck cleaner", "2gal", 30.0], ["stain 5gal", "1", 180.0], ["brushes", "1", 25.0], ["replacement boards", "10", 60.0]], "tools": ["pressure washer", "brush"], "steps": ["wash and dry 48h", "replace damaged boards", "sand rough spots", "two coats stain"], "time": "24h", "level": "advanced", "safety": "pressure washer safety (never point at people)"}
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

