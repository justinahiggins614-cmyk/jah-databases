(function(){'use strict';
/* JAH The Furniture Hack Database — real working generator, jahdb-db-furniture-hack-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FH-";
var SLUG="db-furniture-hack";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "IKEA Dresser to Nightstands", "tier": "Foundations", "notes": "sand sharp edges", "mats": [["used dresser", "1", 40.0], ["saw", "1", 0.0], ["legs 4in", "8", 24.0], ["knobs", "6", 12.0]], "tools": ["saw", "drill", "screwdriver"], "steps": ["cut dresser in half vertically", "sand cut edges", "attach legs", "swap knobs"], "time": "5h", "level": "beginner", "safety": "support both halves while cutting"},
  {"kind": "diy", "t": "Chair Reupholstery Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["old dining chair", "1", 10.0], ["fabric 1yd", "1", 14.0], ["staple gun", "1", 18.0], ["batting", "1", 8.0]], "tools": ["screwdriver", "staple gun", "scissors"], "steps": ["remove seat from frame", "strip old fabric", "layer batting, pull fabric tight", "staple underneath, trim", "reattach"], "time": "3h", "level": "beginner", "safety": "staple gun safety — point away from body"},
  {"kind": "diy", "t": "Tabletop Chalkboard", "tier": "Foundations", "notes": "cure 3 days before writing", "mats": [["table", "1", 0.0], ["chalkboard paint", "1pt", 12.0], ["sandpaper", "1", 4.0], ["chalk", "1", 2.0]], "tools": ["sander", "brush"], "steps": ["sand tabletop smooth", "2 coats chalkboard paint", "season with chalk dust", "write menu or notes"], "time": "3h", "level": "beginner", "safety": "ventilate"},
  {"kind": "diy", "t": "Bookshelf Color-Block", "tier": "Foundations", "notes": "drop cloths", "mats": [["bookshelf", "1", 30.0], ["paint 2 colors", "2qt", 28.0], ["tape", "1", 6.0]], "tools": ["brush", "roller"], "steps": ["clean and sand lightly", "tape geometric sections", "paint blocks, dry between", "seal with poly"], "time": "6h", "level": "beginner", "safety": "ventilate"},
  {"kind": "diy", "t": "Stool to Plant Stand", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wooden stool", "1", 12.0], ["paint", "1pt", 8.0], ["outdoor sealer", "1", 7.0]], "tools": ["brush", "sandpaper"], "steps": ["sand stool", "paint color of choice", "seal for outdoor use", "top with potted plant"], "time": "3h", "level": "beginner", "safety": "none beyond basic painting"},
  {"kind": "diy", "t": "Drawer to Wall Shelf", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["old drawer", "1", 0.0], ["brackets", "2", 8.0], ["paint", "1pt", 8.0]], "tools": ["drill", "brush"], "steps": ["paint drawer inside/out", "mount brackets to studs", "set drawer as shadow box", "style contents"], "time": "3h", "level": "beginner", "safety": "anchor to studs"},
  {"kind": "diy", "t": "Coffee Table Lift-Top Hack", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["coffee table", "1", 40.0], ["lift-top hinges", "2", 22.0], ["screws", "1", 4.0]], "tools": ["drill", "screwdriver"], "steps": ["mark hinge positions", "attach hinges to base", "attach top", "test smooth motion"], "time": "4h", "level": "beginner", "safety": "pre-drill to avoid splits"},
  {"kind": "diy", "t": "Wardrobe to Pantry", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["old wardrobe", "1", 60.0], ["shelf boards", "4", 32.0], ["paint", "1qt", 14.0], ["bins", "6", 30.0]], "tools": ["saw", "drill", "brush"], "steps": ["remove clothing rod", "paint interior", "cut and install shelves", "bins for categories"], "time": "8h", "level": "intermediate", "safety": "anchor tall wardrobe to wall"},
  {"kind": "diy", "t": "Crib to Desk Conversion", "tier": "Compounded", "notes": "sand thoroughly", "mats": [["old crib", "1", 0.0], ["shelf board", "1", 18.0], ["brackets", "2", 8.0], ["paint", "1qt", 14.0]], "tools": ["saw", "drill"], "steps": ["use one side rail as desk back", "mount shelf board at 30in", "paint to match", "add task lamp"], "time": "6h", "level": "intermediate", "safety": "only convert cribs retired from sleep use"},
  {"kind": "diy", "t": "Dresser to Bathroom Vanity", "tier": "Compounded", "notes": "check for leaks 24h; seal wood against moisture", "mats": [["dresser", "1", 50.0], ["vessel sink", "1", 80.0], ["faucet", "1", 60.0], ["plumbing kit", "1", 25.0]], "tools": ["jigsaw", "wrench", "drill"], "steps": ["cut top for sink and faucet", "seal cut edges", "set sink, connect drain", "connect supply lines"], "time": "10h", "level": "intermediate", "safety": "water shutoff first"},
  {"kind": "diy", "t": "Piano Bench Storage Seat", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["piano bench", "1", 30.0], ["hinges", "2", 8.0], ["foam", "1", 15.0], ["fabric", "1yd", 14.0]], "tools": ["drill", "staple gun"], "steps": ["hollow bench if solid", "hinge the top", "foam and upholster lid", "store inside"], "time": "6h", "level": "intermediate", "safety": "staple gun safety"},
  {"kind": "diy", "t": "Headboard from Doors", "tier": "Compounded", "notes": "hit studs", "mats": [["old doors", "2", 40.0], ["sandpaper", "1", 5.0], ["paint", "1qt", 14.0], ["mounting cleat", "1", 10.0]], "tools": ["sander", "drill", "brush"], "steps": ["sand doors smooth", "paint or stain", "join with cleat", "mount to wall studs"], "time": "8h", "level": "intermediate", "safety": "two-person lift"},
  {"kind": "diy", "t": "Desk to Vanity Station", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["small desk", "1", 35.0], ["mirror", "1", 25.0], ["organizer trays", "3", 18.0], ["LED strip", "1", 12.0]], "tools": ["screwdriver", "drill"], "steps": ["clear desk", "mount mirror above", "trays for supplies", "LED under shelf"], "time": "5h", "level": "intermediate", "safety": "none beyond mounting"},
  {"kind": "diy", "t": "Bookshelf Room Divider", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["bookshelves 2", "2", 80.0], ["brackets", "4", 16.0], ["backing panels", "2", 20.0]], "tools": ["drill", "level"], "steps": ["place back to back", "bracket together top/bottom", "add backing panels", "anchor to wall"], "time": "6h", "level": "intermediate", "safety": "anchor to wall — tip-over risk"},
  {"kind": "diy", "t": "Nightstand Charging Station", "tier": "Compounded", "notes": "keep away from water", "mats": [["nightstand", "1", 25.0], ["power strip", "1", 14.0], ["drill bit 2in", "1", 8.0], ["cable clips", "1", 5.0]], "tools": ["drill"], "steps": ["drill cord hole in back", "mount strip inside", "route chargers", "cable clips tidy"], "time": "3h", "level": "intermediate", "safety": "do not overload strip"},
  {"kind": "diy", "t": "Table Leaf Extensions", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["dining table", "1", 0.0], ["plywood", "1", 28.0], ["hinges", "4", 12.0], ["folding brackets", "2", 16.0]], "tools": ["saw", "drill"], "steps": ["cut leaves to match", "hinge or bracket mount", "finish to match top", "test stability"], "time": "8h", "level": "intermediate", "safety": "support leaves when open — test with weight"},
  {"kind": "diy", "t": "Filing Cabinet Tool Chest", "tier": "Compounded", "notes": "heavy tools low", "mats": [["filing cabinet", "1", 25.0], ["foam liner", "1", 10.0], ["casters", "4", 16.0], ["paint", "1qt", 12.0]], "tools": ["drill", "brush"], "steps": ["clean and paint", "foam-line drawers", "casters on base", "label drawers"], "time": "6h", "level": "intermediate", "safety": "locking casters"},
  {"kind": "diy", "t": "Side Table from Stacked Books", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["hardcover books", "8", 8.0], ["brackets", "2", 10.0], ["wood glue", "1", 5.0], ["glass top", "1", 20.0]], "tools": ["drill"], "steps": ["stack and align books", "glue spine stack", "bracket to wall", "glass top"], "time": "4h", "level": "intermediate", "safety": "wall anchor — tall stacks tip"},
  {"kind": "diy", "t": "Coat Rack from Reclaimed Wood", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["barn board", "1", 15.0], ["hooks", "5", 20.0], ["screws", "1", 4.0], ["poly", "1", 8.0]], "tools": ["drill", "saw"], "steps": ["cut board to 36in", "sand and seal", "mount hooks", "hang on studs"], "time": "4h", "level": "intermediate", "safety": "hit studs for coats"},
  {"kind": "diy", "t": "Rocking Chair Restoration", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["rocking chair", "1", 25.0], ["wood glue", "1", 8.0], ["clamps", "4", 20.0], ["stain", "1pt", 9.0]], "tools": ["clamps", "brush"], "steps": ["disassemble loose joints", "reglue and clamp 24h", "strip old finish", "sand and stain"], "time": "10h", "level": "intermediate", "safety": "check for lead paint on antiques — test kit first"},
  {"kind": "diy", "t": "Trunk Coffee Table", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["steamer trunk", "1", 45.0], ["legs 6in", "4", 20.0], ["tray insert", "1", 12.0]], "tools": ["drill", "screwdriver"], "steps": ["clean interior thoroughly", "attach legs to bottom", "tray organizes inside", "condition leather straps"], "time": "5h", "level": "intermediate", "safety": "air out musty trunks (vinegar wipe, sun)"},
  {"kind": "diy", "t": "Bench from Headboard+Footboard", "tier": "Advanced", "notes": "test 300lb load", "mats": [["headboard", "1", 30.0], ["footboard", "1", 30.0], ["seat boards", "3", 27.0], ["apron boards", "2", 14.0]], "tools": ["saw", "drill", "clamps"], "steps": ["cut footboard to bench height", "join with aprons", "add seat boards", "finish and seal"], "time": "12h", "level": "advanced", "safety": "structural screws, not just glue"},
  {"kind": "diy", "t": "Armoire to Home Office", "tier": "Advanced", "notes": "cable management for safety", "mats": [["armoire", "1", 80.0], ["shelf", "1", 20.0], ["power grommet", "1", 10.0], ["LED", "1", 15.0], ["paint", "1qt", 14.0]], "tools": ["saw", "drill", "brush"], "steps": ["remove doors or keep", "install desk shelf at 30in", "drill grommet for cords", "paint interior light color"], "time": "12h", "level": "advanced", "safety": "ventilate"},
  {"kind": "diy", "t": "Sofa to Sectional Rebuild", "tier": "Advanced", "notes": "heavy lifting", "mats": [["sofa", "1", 0.0], ["plywood", "2", 50.0], ["foam", "2", 60.0], ["fabric 8yd", "1", 96.0], ["staples", "1", 8.0]], "tools": ["staple gun", "saw", "sewing machine"], "steps": ["strip sofa to frame", "rebuild one arm as chaise", "new foam all over", "reupholster in sections"], "time": "30h", "level": "advanced", "safety": "upholstery is a skill — practice seams first"},
  {"kind": "diy", "t": "Dining Set Mix-and-Match", "tier": "Advanced", "notes": "consistent finish across pieces", "mats": [["table", "1", 60.0], ["chairs", "6", 90.0], ["paint 2qt", "1", 28.0], ["fabric 3yd", "1", 42.0]], "tools": ["sander", "sewing machine"], "steps": ["sand all pieces", "unify with paint color", "reupholster seats in one fabric", "wax finish"], "time": "20h", "level": "advanced", "safety": "dust mask"},
  {"kind": "diy", "t": "Murphy Bed from Scratch", "tier": "Advanced", "notes": "must anchor to studs; keep clear of swing zone", "mats": [["plywood 8 sheets", "1", 240.0], ["murphy hardware kit", "1", 280.0], ["screws", "1", 20.0], ["mattress", "1", 300.0]], "tools": ["saw", "drill", "level"], "steps": ["build cabinet carcass", "install pivot hardware per manual", "build bed frame", "mount to studs AND floor", "test balance"], "time": "30h", "level": "advanced", "safety": "hardware kit mandatory — no DIY pivots"},
  {"kind": "diy", "t": "Kitchen Island from Dresser", "tier": "Advanced", "notes": "top overhang <12in without support", "mats": [["dresser", "1", 60.0], ["butcher block top", "1", 120.0], ["casters", "4", 28.0], ["paint", "1", 14.0]], "tools": ["saw", "drill"], "steps": ["reinforce dresser frame", "cut top to fit block", "paint body", "mount locking casters"], "time": "12h", "level": "advanced", "safety": "locking casters"},
  {"kind": "diy", "t": "Loft Bed with Desk", "tier": "Advanced", "notes": "bolted joints; 300lb+ rating; anchor to wall", "mats": [["2x6 lumber", "10", 60.0], ["2x4 lumber", "8", 32.0], ["plywood", "1", 45.0], ["bolts", "1", 25.0], ["mattress", "1", 200.0]], "tools": ["saw", "drill", "wrench"], "steps": ["build 4 posts with cross-bracing", "bolt (don't just screw) frame", "deck plywood, guardrails", "desk below"], "time": "20h", "level": "advanced", "safety": "guardrails both sides"},
  {"kind": "diy", "t": "Window Seat with Storage", "tier": "Advanced", "notes": "wall anchor; check window condensation", "mats": [["cabinets 2", "2", 120.0], ["butcher top", "1", 80.0], ["cushion custom", "1", 90.0], ["trim", "1", 25.0]], "tools": ["saw", "drill", "level"], "steps": ["level base cabinets", "secure together and to wall", "top with butcher block", "trim and cushion"], "time": "16h", "level": "advanced", "safety": "level precisely"},
  {"kind": "diy", "t": "Barnwood Accent Wall", "tier": "Advanced", "notes": "check boards for nails/metal first", "mats": [["reclaimed boards 100sqft", "1", 150.0], ["nails", "1", 10.0], ["poly", "1", 20.0]], "tools": ["nail gun", "saw"], "steps": ["plan layout on floor", "nail to studs (mark first)", "stagger joints", "seal lightly"], "time": "14h", "level": "advanced", "safety": "nail gun safety — sequential trigger"},
  {"kind": "diy", "t": "Custom Closet System", "tier": "Advanced", "notes": "level every shelf", "mats": [["melamine boards", "6", 120.0], ["rods", "3", 30.0], ["brackets", "12", 36.0], ["drawers kit", "1", 80.0]], "tools": ["saw", "drill", "level"], "steps": ["measure twice", "cut verticals", "mount to studs", "rods and drawers per plan"], "time": "20h", "level": "advanced", "safety": "every vertical hits a stud"},
  {"kind": "diy", "t": "Pet-Friendly Sofa Rebuild", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["sofa frame", "1", 40.0], ["performance fabric 10yd", "1", 140.0], ["foam", "1", 70.0], ["staples", "1", 8.0]], "tools": ["staple gun", "saw"], "steps": ["strip to frame", "reinforce springs", "performance fabric (stain-resistant)", "tight upholstery"], "time": "24h", "level": "advanced", "safety": "performance fabric worth the cost with pets"},
  {"kind": "diy", "t": "TV Console from Low Dresser", "tier": "Advanced", "notes": "cable management", "mats": [["low dresser", "1", 45.0], ["cable grommets", "2", 10.0], ["paint", "1qt", 14.0], ["legs", "4", 20.0]], "tools": ["drill", "saw"], "steps": ["remove top drawers for components", "drill grommet holes", "paint body", "legs for height"], "time": "10h", "level": "advanced", "safety": "ventilate electronics area"},
  {"kind": "diy", "t": "Outdoor Sectional from Pallets", "tier": "Advanced", "notes": "seal end grain; cushions stored in rain", "mats": [["pallets", "6", 0.0], ["deck screws", "1", 12.0], ["outdoor cushions", "1", 150.0], ["wood sealer", "1gal", 35.0]], "tools": ["sander", "drill"], "steps": ["break down and sand pallets", "build 3 base boxes", "build backrests", "seal all sides", "cushions on top"], "time": "18h", "level": "advanced", "safety": "HT pallets only"}
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

