(function(){'use strict';
/* JAH The Miniature World Builder — real working generator, jahdb-gen-miniature-world-builder-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MWBS-";
var SLUG="gen-miniature-world-builder";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Cozy Cottage Interior (1:12)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["balsa sheets", "6", 18.0], ["basswood strips", "1", 8.0], ["dollhouse wallpaper", "3", 12.0], ["mini furniture kit", "1", 25.0]], "tools": ["craft knife", "glue", "ruler"], "steps": ["cut walls to 1:12 scale", "wallpaper before assembly", "glue room box", "furnish and light"], "time": "10h", "level": "beginner", "safety": "craft knife safety — cut away from body, fresh blades"},
  {"kind": "diy", "t": "Fairy Garden in a Pot", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["large pot", "1", 15.0], ["soil", "4qt", 5.0], ["mini plants", "5", 20.0], ["fairy house", "1", 12.0], ["pebbles", "1", 4.0]], "tools": ["trowel"], "steps": ["fill pot with soil", "plant minis around edges", "place house as focal", "pebble paths"], "time": "3h", "level": "beginner", "safety": "none beyond gardening basics"},
  {"kind": "diy", "t": "Diorama: Desert Oasis", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["shoebox", "1", 0.0], ["sand", "2cups", 0.0], ["blue paper", "1", 1.0], ["plastic palm", "1", 5.0], ["paint", "1", 6.0]], "tools": ["scissors", "glue"], "steps": ["paint box interior sky", "sand dunes glued down", "paper pond with gloss", "palm and rocks placed"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Miniature Book Nook", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["books (real)", "2", 0.0], ["foam board", "2", 8.0], ["LED tea light", "2", 4.0], ["mini books", "20", 6.0]], "tools": ["craft knife", "glue"], "steps": ["measure shelf gap", "build alley walls", "layer depth scenes", "light from behind"], "time": "6h", "level": "beginner", "safety": "LED only — no real flames near books"},
  {"kind": "diy", "t": "Terrarium-Style Mini Forest", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["glass jar large", "1", 12.0], ["moss", "1bag", 8.0], ["twigs", "1", 0.0], ["mini figures", "3", 9.0]], "tools": ["tweezers"], "steps": ["layer pebbles, charcoal, soil", "place moss carpets", "twig trees", "figures for scale"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "1:24 Garage Diorama", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["foam board", "3", 12.0], ["toy car 1", "24:1", 15.0], ["paint set", "1", 10.0], ["printed posters", "1", 3.0]], "tools": ["knife", "glue"], "steps": ["build 3 walls and floor", "paint concrete texture", "posters as wall art", "park car, add tools"], "time": "8h", "level": "beginner", "safety": "knife safety"},
  {"kind": "diy", "t": "Miniature Greenhouse", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["acrylic sheets", "4", 16.0], ["balsa frame", "1", 8.0], ["mini pots", "10", 10.0], ["soil", "1", 4.0], ["seeds", "1", 3.0]], "tools": ["knife", "glue"], "steps": ["frame the house", "glaze with acrylic", "bench inside", "plant real micro-greens"], "time": "8h", "level": "intermediate", "safety": "real plants need light — place in sun"},
  {"kind": "diy", "t": "Medieval Castle Courtyard", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam blocks", "10", 20.0], ["gray paint", "1", 8.0], ["mini figures", "6", 18.0], ["torch LEDs", "4", 8.0]], "tools": ["knife", "paint"], "steps": ["stack block walls", "paint stone texture", "courtyard details", "LED torches"], "time": "14h", "level": "intermediate", "safety": "plan layout before gluing"},
  {"kind": "diy", "t": "Japanese Tea Garden (Mini)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shallow tray", "1", 14.0], ["sand", "3cups", 3.0], ["rocks", "1", 0.0], ["mini bridge", "1", 10.0], ["moss", "1", 6.0]], "tools": ["rake fork"], "steps": ["sand base raked", "rock placement (odd numbers)", "bridge over dry stream", "moss accents"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Victorian Dollhouse Room", "tier": "Compounded", "notes": "check scale consistency", "mats": [["room box kit", "1", 30.0], ["wallpaper", "1", 8.0], ["chandelier mini", "1", 12.0], ["furniture set", "1", 35.0]], "tools": ["knife", "glue", "tweezers"], "steps": ["assemble box square", "paper walls", "wire chandelier (battery)", "furnish period-correct"], "time": "16h", "level": "intermediate", "safety": "battery LEDs only"},
  {"kind": "diy", "t": "Sci-Fi Corridor Diorama", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam board", "4", 16.0], ["metallic paint", "1", 10.0], ["LED strip", "1", 12.0], ["greebles (kit parts)", "1", 8.0]], "tools": ["knife", "glue"], "steps": ["build corridor perspective", "paint metallic panels", "gutters of greebles", "LED cove lighting"], "time": "12h", "level": "intermediate", "safety": "low-voltage LED only"},
  {"kind": "diy", "t": "Miniature Bakery Shop", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["room box", "1", 25.0], ["polymer clay", "1", 15.0], ["mini shelves", "1", 12.0], ["paint", "1", 8.0]], "tools": ["clay tools", "knife"], "steps": ["sculpt breads and cakes", "bake clay per instructions", "shelf the goods", "signage painted"], "time": "14h", "level": "intermediate", "safety": "ventilate when baking clay"},
  {"kind": "diy", "t": "Treehouse Village", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["branches", "1", 0.0], ["balsa", "1", 10.0], ["twine", "1", 4.0], ["mini houses", "3", 24.0]], "tools": ["saw", "glue"], "steps": ["select sturdy branch", "platform decks", "houses on decks", "rope bridges between"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Underwater Scene Diorama", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoebox", "1", 0.0], ["blue cellophane", "1", 4.0], ["plastic fish", "8", 10.0], ["sand", "1", 2.0], ["shells", "1", 0.0]], "tools": ["scissors", "glue"], "steps": ["line box with cellophane", "sand seabed", "hang fish on thread", "shells and plants"], "time": "5h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Miniature Library", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam board", "2", 8.0], ["mini books", "50", 15.0], ["wood stain", "1", 7.0], ["LED", "1", 6.0]], "tools": ["knife", "glue"], "steps": ["build shelf walls", "stain wood tone", "fill with books", "lamp glow"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Farm at 1:32", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["plywood base", "1", 12.0], ["model barn kit", "1", 28.0], ["animals", "8", 16.0], ["fencing", "1", 8.0]], "tools": ["saw", "glue", "paint"], "steps": ["base with fields painted", "barn assembled", "fence pastures", "animals placed"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Steampunk Airship Dock", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["balsa", "2", 16.0], ["brass paint", "1", 9.0], ["balloon (paper)", "1", 6.0], ["rigging thread", "1", 4.0], ["LED", "1", 8.0]], "tools": ["knife", "glue"], "steps": ["build dock tower", "airship hull and balloon", "rigging lines", "light the dock"], "time": "20h", "level": "advanced", "safety": "plan rigging before assembly"},
  {"kind": "diy", "t": "Miniature City Block", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam board", "10", 40.0], ["printed building wraps", "1", 12.0], ["street paint", "1", 8.0], ["cars", "6", 24.0], ["lights", "1", 15.0]], "tools": ["knife", "glue"], "steps": ["grid the block", "wrap buildings", "paint streets", "wire streetlights (battery)"], "time": "24h", "level": "advanced", "safety": "keep wiring accessible"},
  {"kind": "diy", "t": "Fantasy Tavern Interior", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["room box", "1", 30.0], ["mini barrels", "4", 12.0], ["fireplace kit", "1", 18.0], ["figures", "5", 15.0]], "tools": ["knife", "glue", "paint"], "steps": ["stone fireplace build", "bar and tables", "barrels and mugs", "fireplace LED flicker"], "time": "22h", "level": "advanced", "safety": "LED flicker circuits are low voltage"},
  {"kind": "diy", "t": "Working Mini Waterwheel", "tier": "Advanced", "notes": "seal wood", "mats": [["basswood", "1", 10.0], ["dowel", "1", 3.0], ["basin", "1", 8.0], ["small pump", "1", 18.0]], "tools": ["saw", "drill", "glue"], "steps": ["cut wheel and paddles", "axle on dowel", "basin with pump", "water flow turns wheel"], "time": "16h", "level": "advanced", "safety": "pump is low-voltage"},
  {"kind": "diy", "t": "Miniature Observatory", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["dome kit or bowl", "1", 14.0], ["telescope mini", "1", 12.0], ["star paint", "1", 8.0], ["fiber LEDs", "1", 16.0]], "tools": ["knife", "glue"], "steps": ["dome with slit", "telescope on mount", "starfield ceiling", "fiber stars"], "time": "18h", "level": "advanced", "safety": "fiber LEDs need planning"},
  {"kind": "diy", "t": "Desert Canyon Railroad", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plywood 2x4", "1", 25.0], ["track N-scale", "1", 40.0], ["train set", "1", 60.0], ["plaster cloth", "1", 18.0]], "tools": ["saw"], "steps": ["benchwork frame", "track laid and tested", "plaster canyon", "paint and ballast"], "time": "30h", "level": "advanced", "safety": "test track before scenery"},
  {"kind": "diy", "t": "Miniature Theater with Lights", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam board", "6", 24.0], ["red fabric", "1", 10.0], ["LED spots", "4", 16.0], ["figures", "10", 20.0]], "tools": ["knife", "sew", "glue"], "steps": ["stage and proscenium", "curtains sewn", "spotlights aimed", "audience placed"], "time": "24h", "level": "advanced", "safety": "low-voltage lighting only"},
  {"kind": "diy", "t": "Clockwork Village Square", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["balsa", "3", 24.0], ["clock mechanism", "1", 18.0], ["figures", "8", 16.0], ["paint", "1", 10.0]], "tools": ["knife", "glue"], "steps": ["square layout", "clock tower working", "shops around", "figures in scene"], "time": "26h", "level": "advanced", "safety": "clock hands clearance planned"},
  {"kind": "diy", "t": "Miniature Shipyard", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plywood", "1", 20.0], ["hull kit", "1", 35.0], ["rigging", "1", 6.0], ["paint", "1", 12.0]], "tools": ["saw", "knife"], "steps": ["slipway build", "hull planked", "masts and rigging", "water base"], "time": "30h", "level": "advanced", "safety": "rigging order matters — masts before lines"},
  {"kind": "diy", "t": "Alpine Village Diorama", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam", "4", 20.0], ["chalet kits", "3", 45.0], ["snow flock", "1", 8.0], ["train", "1", 40.0]], "tools": ["knife", "glue"], "steps": ["mountain forms", "snow flocking", "chalets placed", "train loop"], "time": "28h", "level": "advanced", "safety": "flock in ventilated area"},
  {"kind": "diy", "t": "Miniature Aquarium (Faux)", "tier": "Advanced", "notes": "cure per instructions", "mats": [["glass box", "1", 20.0], ["resin water kit", "1", 18.0], ["fish models", "6", 15.0], ["sand", "1", 4.0], ["plants", "1", 8.0]], "tools": ["none"], "steps": ["sand and plants", "position fish on wires", "pour resin in layers", "cure fully"], "time": "12h", "level": "advanced", "safety": "resin fumes — ventilate, gloves"},
  {"kind": "diy", "t": "Haunted House Diorama", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam board", "5", 20.0], ["black paint", "1", 8.0], ["LED orange", "1", 10.0], ["sound module", "1", 15.0], ["figures", "1", 12.0]], "tools": ["knife", "glue"], "steps": ["crooked house build", "paint aged", "orange window glow", "sound module hidden"], "time": "22h", "level": "advanced", "safety": "battery power only"},
  {"kind": "diy", "t": "Miniature Space Station", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plastic kits", "2", 40.0], ["metallic paint", "1", 10.0], ["fiber LEDs", "1", 16.0], ["base", "1", 12.0]], "tools": ["knife", "glue"], "steps": ["modules joined", "paint hull panels", "fiber starfield", "display base"], "time": "26h", "level": "advanced", "safety": "plan LED routing early"},
  {"kind": "diy", "t": "Working Drawbridge Castle", "tier": "Advanced", "notes": "pinch points guarded", "mats": [["foam blocks", "12", 24.0], ["servo micro", "1", 12.0], ["battery box", "1", 6.0], ["paint", "1", 10.0]], "tools": ["knife", "glue"], "steps": ["castle walls", "bridge on hinge", "servo linkage", "remote raise/lower"], "time": "24h", "level": "advanced", "safety": "low-voltage servo"},
  {"kind": "diy", "t": "Miniature Hot Air Balloon Festival", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["paper balloons", "5", 20.0], ["baskets", "1", 10.0], ["sky backdrop", "1", 12.0], ["LED", "1", 8.0]], "tools": ["none"], "steps": ["balloon envelopes", "basket rigging", "sky backdrop", "dawn lighting"], "time": "18h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Diorama: Coral Reef", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["shoebox large", "1", 0.0], ["coral models", "1", 25.0], ["fish", "10", 15.0], ["sand", "1", 3.0], ["blue paint", "1", 6.0]], "tools": ["glue"], "steps": ["reef structure", "coral placement", "fish on threads", "lighting blue"], "time": "16h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Miniature Construction Site", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plywood", "1", 18.0], ["toy machines", "3", 36.0], ["sand pile", "1", 4.0], ["barriers", "1", 8.0], ["paint", "1", 8.0]], "tools": ["saw"], "steps": ["site base", "machines posed", "sand and barriers", "safety signage"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Grand Ballroom (1:12)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["room box large", "1", 40.0], ["chandelier", "1", 18.0], ["fabric 2yd", "1", 16.0], ["figures", "12", 30.0], ["mirror", "1", 10.0]], "tools": ["knife", "sew", "glue"], "steps": ["parquet floor print", "drapes sewn", "chandelier hung (battery)", "figures dancing"], "time": "30h", "level": "advanced", "safety": "scale consistency checked throughout"}
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

