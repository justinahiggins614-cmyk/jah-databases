(function(){'use strict';
/* JAH The Upcycling Genius Database — real working generator, jahdb-db-upcycling-genius-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UG-";
var SLUG="db-upcycling-genius";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Pallet-Wood Planter Box", "tier": "Foundations", "notes": "check pallets for HT stamp (heat-treated, safe) not MB (methyl bromide)", "mats": [["reclaimed pallet slats", "12", 0.0], ["deck screws 1.25in", "40", 4.0], ["landscape fabric", "1yd", 3.0], ["potting soil 20qt", "1", 8.0]], "tools": ["pry bar", "circular saw", "drill", "sander", "tape measure"], "steps": ["break down pallet and denail", "cut slats to 24in", "predrill and screw box frame", "sand 120-grit", "staple fabric liner", "fill with soil and plant"], "time": "4h", "level": "beginner", "safety": "eye protection,gloves,dust mask"},
  {"kind": "diy", "t": "T-Shirt Tote Bag (No Sew)", "tier": "Foundations", "notes": "tie knots tight so seams hold", "mats": [["old t-shirts", "2", 0.0], ["fabric scissors", "1", 0.0], ["washable marker", "1", 2.0]], "tools": ["scissors", "ruler"], "steps": ["lay shirt flat and cut off sleeves", "cut neckline wider", "turn inside out,tie fringe strips in pairs", "turn right-side out"], "time": "1h", "level": "beginner", "safety": "sharp scissors safety"},
  {"kind": "diy", "t": "Jar Lanterns from Tin Cans", "tier": "Foundations", "notes": "never use real candles near paint fumes — tea lights only, LED preferred", "mats": [["clean tin cans", "4", 0.0], ["tea lights", "4", 3.0], ["spray paint", "1", 6.0], ["wire for handles", "4ft", 2.0]], "tools": ["hammer", "nail", "pliers"], "steps": ["fill can with water and freeze", "hammer nail-hole pattern", "thaw,dry,paint outside only", "twist wire handle", "drop in tea light"], "time": "2h", "level": "beginner", "safety": "work gloves for sharp edges"},
  {"kind": "diy", "t": "Wine-Bottle Herb Garden", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["empty wine bottles", "3", 0.0], ["herb starts", "3", 9.0], ["potting mix", "8qt", 5.0], ["pebbles", "2cups", 0.0]], "tools": ["bottle cutter or string method", "gloves", "sandpaper"], "steps": ["score and separate bottle", "sand cut edge smooth", "layer pebbles then soil", "plant herbs and water"], "time": "3h", "level": "beginner", "safety": "cut glass is sharp — sand thoroughly, keep away from children"},
  {"kind": "diy", "t": "Cardboard Drawer Organizers", "tier": "Foundations", "notes": "replace dull blades", "mats": [["shipping boxes", "2", 0.0], ["washi tape", "2", 4.0], ["glue stick", "1", 2.0], ["ruler", "1", 0.0]], "tools": ["box cutter", "ruler", "cutting mat"], "steps": ["measure drawer interior", "cut box panels to height", "score and fold dividers", "glue and tape edges", "fit and adjust"], "time": "2h", "level": "beginner", "safety": "cut away from body on a mat"},
  {"kind": "diy", "t": "Mason-Jar Soap Dispenser", "tier": "Foundations", "notes": "drill metal slowly", "mats": [["mason jar", "1", 3.0], ["soap pump top", "1", 4.0], ["drill bit 1in", "1", 0.0]], "tools": ["drill", "clamp"], "steps": ["clamp lid securely", "drill center hole", "thread pump through", "fill with soap"], "time": "30m", "level": "beginner", "safety": "clamp work, eye protection"},
  {"kind": "diy", "t": "Sweater-to-Pillow Covers", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["old sweaters", "2", 0.0], ["pillow inserts 16in", "2", 10.0], ["needle and thread", "1", 3.0]], "tools": ["scissors", "needle", "pins"], "steps": ["cut sweater panels 17in square", "pin right sides together", "stitch 1/2in seam,leave gap", "turn,insert pillow,slip-stitch closed"], "time": "2h", "level": "beginner", "safety": "none beyond needle care"},
  {"kind": "diy", "t": "Magazine-Page Gift Bowls", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["old magazines", "3", 0.0], ["mod podge", "1", 8.0], ["balloon", "1", 2.0], ["brush", "1", 3.0]], "tools": ["brush", "scissors"], "steps": ["cut strips from pages", "inflate balloon as mold", "layer strips with mod podge", "dry 24h, pop balloon"], "time": "3h", "level": "beginner", "safety": "none beyond craft glue"},
  {"kind": "diy", "t": "Tire Garden Ottoman", "tier": "Compounded", "notes": "hot glue burns; ventilate if painting tire", "mats": [["used tire", "1", 0.0], ["rope 100ft", "1", 12.0], ["plywood round 18in", "1", 6.0], ["wood screws", "12", 3.0], ["legs or casters", "4", 10.0]], "tools": ["drill", "jigsaw", "screwdriver", "glue gun"], "steps": ["scrub and dry tire", "cut plywood top and bottom", "screw bottom disk inside", "wrap rope with hot glue from center out", "screw on legs"], "time": "6h", "level": "intermediate", "safety": "gloves"},
  {"kind": "diy", "t": "Door-to-Desk Conversion", "tier": "Compounded", "notes": "ventilate for polyurethane", "mats": [["old solid door", "1", 15.0], ["hairpin legs 28in", "4", 40.0], ["sandpaper set", "1", 6.0], ["polyurethane", "1qt", 12.0]], "tools": ["sander", "drill", "screwdriver"], "steps": ["strip hardware and sand 80→220 grit", "fill holes with wood filler", "sand and wipe tack cloth", "apply 3 poly coats, sanding between", "screw on legs"], "time": "8h", "level": "intermediate", "safety": "dust mask while sanding"},
  {"kind": "diy", "t": "Suitcase Side Table", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["vintage suitcase", "1", 10.0], ["table legs 16in", "4", 24.0], ["plywood insert", "1", 5.0], ["brackets", "4", 4.0]], "tools": ["drill", "screwdriver", "saw"], "steps": ["reinforce suitcase interior with plywood", "screw legs to bottom through plywood", "add interior shelf if deep", "touch up exterior"], "time": "5h", "level": "intermediate", "safety": "check suitcase for musty smell — air out, wipe with vinegar"},
  {"kind": "diy", "t": "Ladder Bookshelf", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wooden ladder", "1", 20.0], ["pine boards", "3", 18.0], ["brackets", "6", 8.0], ["screws", "24", 4.0]], "tools": ["saw", "drill", "level"], "steps": ["sand ladder smooth", "cut boards to rung width", "bracket boards across rungs", "level and wall-anchor top"], "time": "5h", "level": "intermediate", "safety": "always anchor tall furniture to wall studs"},
  {"kind": "diy", "t": "Crate Coffee Table", "tier": "Compounded", "notes": "locking casters so table stays put", "mats": [["wooden crates", "4", 24.0], ["caster wheels", "4", 14.0], ["wood stain", "1pt", 8.0], ["screws", "20", 3.0]], "tools": ["drill", "sander", "brush"], "steps": ["sand crates", "stain and dry 24h", "arrange 2x2 open-sides out", "screw together,add casters"], "time": "6h", "level": "intermediate", "safety": "ventilate for stain"},
  {"kind": "diy", "t": "Bottle-Cap Mosaic Tray", "tier": "Compounded", "notes": "grout dust mask", "mats": [["bottle caps", "80", 0.0], ["wood tray", "1", 8.0], ["grout", "1lb", 5.0], ["glue", "1", 4.0]], "tools": ["pliers", "spreader", "sponge"], "steps": ["arrange caps in pattern", "glue caps down, dry overnight", "press grout into gaps", "wipe haze, seal"], "time": "6h", "level": "intermediate", "safety": "gloves"},
  {"kind": "diy", "t": "Denim Patchwork Quilt Top", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["old jeans", "8", 0.0], ["batting twin", "1", 12.0], ["backing fabric 3yd", "1", 15.0], ["thread", "2", 6.0]], "tools": ["sewing machine", "rotary cutter", "mat"], "steps": ["cut 6in squares from jeans", "piece squares into rows", "sew rows together", "layer top,batting,backing", "quilt and bind"], "time": "12h", "level": "intermediate", "safety": "rotary cutter safety — always roll away from body"},
  {"kind": "diy", "t": "CD-Mosaic Mirror Frame", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["old CDs", "10", 0.0], ["plain mirror", "1", 12.0], ["MDF frame", "1", 6.0], ["tile adhesive", "1", 7.0]], "tools": ["scissors", "nippers", "gloves"], "steps": ["cut CDs into shards (score and snap)", "adhere shards to frame", "grout gaps", "wipe and polish"], "time": "5h", "level": "intermediate", "safety": "CD shards are sharp — gloves and eye protection"},
  {"kind": "diy", "t": "Pallet Coffee Table", "tier": "Compounded", "notes": "HT-stamp pallets only", "mats": [["pallets", "2", 0.0], ["sandpaper", "1", 5.0], ["casters", "4", 14.0], ["wood oil", "1pt", 9.0]], "tools": ["pry bar", "sander", "drill"], "steps": ["break down one pallet for slats", "sand everything 120-grit", "build box frame from second pallet", "top with slats, oil finish", "add casters"], "time": "8h", "level": "intermediate", "safety": "denail carefully"},
  {"kind": "diy", "t": "Chandelier from Kitchen Grater", "tier": "Compounded", "notes": "if unsure hire an electrician", "mats": [["metal graters", "3", 9.0], ["pendant light kits", "3", 18.0], ["edison bulbs", "3", 9.0], ["ceiling canopy", "1", 6.0]], "tools": ["screwdriver", "wire strippers", "drill"], "steps": ["strip grater handles", "wire pendant kits through graters", "mount to canopy bar", "hang and wire to ceiling box"], "time": "4h", "level": "intermediate", "safety": "ELECTRICAL SAFETY: turn off breaker, use wire nuts, ground metal"},
  {"kind": "diy", "t": "Bookshelf from Drawers", "tier": "Compounded", "notes": "heavy books low", "mats": [["old dresser drawers", "4", 0.0], ["shelf brackets", "8", 10.0], ["paint", "1qt", 12.0], ["screws", "16", 3.0]], "tools": ["drill", "brush", "level"], "steps": ["clean and sand drawers", "paint inside and out", "mount brackets to studs", "set drawers as shadow-box shelves"], "time": "6h", "level": "intermediate", "safety": "mount to studs"},
  {"kind": "diy", "t": "Drum-Barrel Fire Pit Seating", "tier": "Compounded", "notes": "never burn treated wood", "mats": [["steel drum", "1", 15.0], ["heat paint", "1", 8.0], ["outdoor cushions", "2", 20.0], ["plywood rounds", "2", 8.0]], "tools": ["angle grinder or jigsaw", "drill"], "steps": ["cut drum to 18in height", "grind edge smooth", "paint with heat paint", "top with plywood and cushion"], "time": "5h", "level": "intermediate", "safety": "grinder sparks and noise — face shield, gloves, hearing protection"},
  {"kind": "diy", "t": "Cable-Spool Table", "tier": "Compounded", "notes": "spools are heavy — get help moving", "mats": [["wooden cable spool", "1", 20.0], ["sandpaper", "1", 5.0], ["polyurethane", "1qt", 12.0]], "tools": ["sander", "brush"], "steps": ["sand all surfaces 80→220", "wipe clean", "3 coats poly, sand between", "level on floor"], "time": "6h", "level": "intermediate", "safety": "dust mask"},
  {"kind": "diy", "t": "Window-Frame Greenhouse", "tier": "Advanced", "notes": "tempered or replace cracked glass", "mats": [["old windows", "8", 40.0], ["2x4 lumber", "10", 35.0], ["screws", "60", 8.0], ["hinges", "4", 10.0], ["gravel", "4bags", 16.0]], "tools": ["saw", "drill", "level", "post hole digger"], "steps": ["build 4x6ft base frame", "anchor corner posts", "mount windows as walls", "screw roof windows with slope", "add door window on hinges", "gravel floor"], "time": "20h", "level": "advanced", "safety": "structural safety — anchor against wind"},
  {"kind": "diy", "t": "Bathtub Sofa", "tier": "Advanced", "notes": "face shield, help lifting; seal cut edge against rust", "mats": [["cast-iron tub", "1", 50.0], ["plywood", "1", 25.0], ["foam 4in", "1", 40.0], ["upholstery fabric 4yd", "1", 48.0], ["legs", "4", 20.0]], "tools": ["angle grinder", "saw", "staple gun", "drill"], "steps": ["cut tub side panel with grinder", "smooth and cap cut edge", "build plywood seat deck", "foam and upholster seat", "mount legs, level"], "time": "24h", "level": "advanced", "safety": "grinder + cast iron = heavy sparks and weight"},
  {"kind": "diy", "t": "Piano-Shell Bar Cabinet", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["upright piano shell", "1", 60.0], ["LED strip", "1", 15.0], ["shelves", "3", 20.0], ["mirror tiles", "6", 18.0], ["lock", "1", 8.0]], "tools": ["screwdrivers", "saw", "drill"], "steps": ["remove action and strings (tension!)", "clean and paint interior", "install shelves and mirror back", "wire LED strip", "fit lock"], "time": "18h", "level": "advanced", "safety": "piano strings under high tension — wear eye protection, loosen gradually or have a technician release them"},
  {"kind": "diy", "t": "Shipping-Container Shed (Mini)", "tier": "Advanced", "notes": "check local permits for structures", "mats": [["mini container 6ft", "1", 400.0], ["vents", "2", 30.0], ["paint", "2gal", 60.0], ["shelving", "3", 45.0]], "tools": ["grinder", "welder or bolts", "roller"], "steps": ["level gravel pad", "cut vent openings", "prime and paint exterior", "install shelving and lighting", "seal roof seams"], "time": "40h", "level": "advanced", "safety": "cutting steel — face shield, gloves"},
  {"kind": "diy", "t": "Staircase Bookshelf Wall", "tier": "Advanced", "notes": "test-load before styling", "mats": [["reclaimed stair treads", "6", 30.0], ["2x6 lumber", "6", 30.0], ["brackets", "12", 24.0], ["screws", "80", 10.0]], "tools": ["saw", "drill", "stud finder", "level"], "steps": ["map stud layout", "cut treads to uniform depth", "mount ledger boards to studs", "set treads as floating shelves", "stagger for staircase effect"], "time": "16h", "level": "advanced", "safety": "every shelf must hit studs"},
  {"kind": "diy", "t": "Barn-Door Room Divider", "tier": "Advanced", "notes": "two-person hang", "mats": [["barn doors", "2", 80.0], ["overhead track 8ft", "1", 45.0], ["rollers", "4", 20.0], ["floor guide", "1", 8.0]], "tools": ["drill", "level", "wrench"], "steps": ["mount track to header (must hit studs)", "hang rollers and doors", "install floor guide", "adjust and test glide"], "time": "10h", "level": "advanced", "safety": "track must anchor to solid header — doors are heavy"},
  {"kind": "diy", "t": "Kayak Bookshelf", "tier": "Advanced", "notes": "cap sharp cut edges", "mats": [["old kayak", "1", 40.0], ["wall brackets", "4", 24.0], ["screws", "16", 5.0], ["LED puck lights", "3", 12.0]], "tools": ["saw", "drill", "stud finder"], "steps": ["cut kayak lengthwise (top half)", "sand cut edges smooth", "mount brackets to studs", "set hull as shelf, add lights"], "time": "12h", "level": "advanced", "safety": "secure heavy hull to studs"},
  {"kind": "diy", "t": "Engine-Block Coffee Table", "tier": "Advanced", "notes": "solvent gloves and ventilation", "mats": [["engine block", "1", 80.0], ["glass top 36in", "1", 90.0], ["degreaser", "2", 14.0], ["clear coat", "1", 12.0], ["felt pads", "4", 3.0]], "tools": ["engine hoist or 3 helpers", "brushes"], "steps": ["degrease thoroughly (multiple passes)", "dry and clear-coat", "set on felt pads", "lay glass top"], "time": "10h", "level": "advanced", "safety": "engine blocks weigh 200+ lb — mechanical lift, never solo"},
  {"kind": "diy", "t": "Silo Grain-Bin Gazebo", "tier": "Advanced", "notes": "check permits and wind load", "mats": [["grain bin 12ft", "1", 600.0], ["posts", "6", 90.0], ["concrete", "8bags", 48.0], ["roof sealant", "2gal", 70.0]], "tools": ["come-along", "drill", "ladder"], "steps": ["pour post footings", "raise bin rings with come-along", "bolt rings per pattern", "seal roof, add vents"], "time": "48h", "level": "advanced", "safety": "working at height — harnesses, scaffolding"},
  {"kind": "diy", "t": "Train-Trestle Desk", "tier": "Advanced", "notes": "pre-drill hardwood", "mats": [["trestle table base", "1", 120.0], ["butcher block top", "1", 150.0], ["wire grommets", "3", 12.0], ["cable tray", "1", 18.0]], "tools": ["drill", "sander", "wrench"], "steps": ["refinish base", "cut cable holes in top", "mount grommets and tray", "assemble and level"], "time": "14h", "level": "advanced", "safety": "heavy top — two-person flip"},
  {"kind": "diy", "t": "Church-Pew Bench", "tier": "Advanced", "notes": "pews are long — support both ends when moving", "mats": [["church pew", "1", 100.0], ["sandpaper", "1", 6.0], ["stain", "1qt", 14.0], ["poly", "1qt", 12.0]], "tools": ["sander", "brush"], "steps": ["sand 80→220", "stain evenly, dry 24h", "3 poly coats", "felt pads on feet"], "time": "12h", "level": "advanced", "safety": "dust mask"},
  {"kind": "diy", "t": "Water-Tower Planter", "tier": "Advanced", "notes": "heavy when wet — place before filling", "mats": [["wooden barrel", "1", 45.0], ["legs 4x4", "4", 24.0], ["liner", "1", 10.0], ["soil 3cuft", "2", 18.0]], "tools": ["saw", "drill"], "steps": ["build leg frame", "set barrel, drill drainage", "line and fill", "plant"], "time": "8h", "level": "advanced", "safety": "drainage prevents rot"},
  {"kind": "diy", "t": "Windmill Garden Feature (Working)", "tier": "Advanced", "notes": "keep blades clear of paths; balance to prevent wobble", "mats": [["cedar boards", "8", 48.0], ["bearings", "2", 16.0], ["pole 10ft", "1", 35.0], ["hardware", "1", 12.0]], "tools": ["saw", "drill"], "steps": ["cut 4 blades with airfoil taper", "mount hub on bearings", "raise pole in concrete", "attach head, balance blades"], "time": "16h", "level": "advanced", "safety": "concrete-set pole"}
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

