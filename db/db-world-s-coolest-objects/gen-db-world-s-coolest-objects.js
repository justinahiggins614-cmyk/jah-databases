(function(){'use strict';
/* JAH The World's Coolest Objects Database — real working generator, jahdb-db-world-s-coolest-objects-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WSCO-";
var SLUG="db-world-s-coolest-objects";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Humble Paperclip", "tier": "Foundations", "concept": "one bent wire holds papers for a century", "mechanism": "spring steel looped in a double oval grips by torsion", "parts": ["wire", "pliers"], "build": "bend, test hold", "time": "1h", "level": "beginner", "safety": "none", "notes": "design lesson: do one thing perfectly"},
  {"kind": "gm", "t": "The Swiss Army Knife", "tier": "Foundations", "concept": "many tools, one pocket", "mechanism": "layered pivots share a single axis", "parts": ["blades", "springs", "scales"], "build": "study pivot", "time": "2h", "level": "beginner", "safety": "blades sharp", "notes": "lesson: density without clutter"},
  {"kind": "gm", "t": "The Post-it Note", "tier": "Foundations", "concept": "bookmarks that damage pages", "mechanism": "low-tack microsphere adhesive releases cleanly", "parts": ["paper", "adhesive"], "build": "test tack", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: a failed strong glue became a perfect weak one"},
  {"kind": "gm", "t": "Velcro", "tier": "Foundations", "concept": "fastening without tying", "mechanism": "hook-and-loop: tiny hooks catch loops", "parts": ["nylon tape"], "build": "press test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: nature (burrs) as R&D lab"},
  {"kind": "gm", "t": "The Thermos", "tier": "Foundations", "concept": "drinks go cold", "mechanism": "vacuum between double walls stops conduction", "parts": ["steel", "stopper"], "build": "feel test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: nothing (vacuum) as insulation"},
  {"kind": "gm", "t": "Bubble Wrap", "tier": "Foundations", "concept": "fragile shipping breaks", "mechanism": "air pockets distribute impact", "parts": ["plastic film"], "build": "pop test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: invented as wallpaper, saved as packaging"},
  {"kind": "gm", "t": "The Slinky", "tier": "Foundations", "concept": "a spring that walks", "mechanism": "gravity + spring tension trade energy down stairs", "parts": ["steel coil"], "build": "stair test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: accident (dropped spring) as product"},
  {"kind": "gm", "t": "Duct Tape", "tier": "Foundations", "concept": "field repairs need everything", "mechanism": "cloth-reinforced adhesive: strong, tearable, waterproof", "parts": ["tape"], "build": "tear test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: wartime need to peacetime ubiquity"},
  {"kind": "gm", "t": "The Zipper", "tier": "Foundations", "concept": "buttons are slow", "mechanism": "interlocking teeth guided by a slider", "parts": ["teeth", "tape", "slider"], "build": "zip test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: 20 years of refinement before adoption"},
  {"kind": "gm", "t": "Safety Pin", "tier": "Foundations", "concept": "holding cloth without sewing", "mechanism": "spring coil keeps point sheathed", "parts": ["wire"], "build": "pin test", "time": "1h", "level": "beginner", "safety": "pin sharp", "notes": "lesson: 3,000-year-old design still optimal"},
  {"kind": "gm", "t": "The Umbrella", "tier": "Foundations", "concept": "rain ruins outings", "mechanism": "collapsible canopy on a stick", "parts": ["fabric", "ribs"], "build": "open test", "time": "1h", "level": "beginner", "safety": "none", "notes": "lesson: 4,000 years old, barely changed"},
  {"kind": "gm", "t": "Mechanical Pencil", "tier": "Compounded", "concept": "sharpening wastes lead", "mechanism": "clutch advances fixed lead lengths", "parts": ["lead", "spring"], "build": "click test", "time": "2h", "level": "intermediate", "safety": "none", "notes": "lesson: precision from tiny mechanisms"},
  {"kind": "gm", "t": "The Retractable Pen", "tier": "Compounded", "concept": "caps get lost", "mechanism": "spring cam locks tip in/out", "parts": ["pen", "spring"], "build": "click test", "time": "2h", "level": "intermediate", "safety": "none", "notes": "lesson: one-handed operation wins"},
  {"kind": "gm", "t": "Noise-Cancelling Headphones", "tier": "Compounded", "concept": "engine drone exhausts travelers", "mechanism": "anti-phase sound cancels ambient waves", "parts": ["drivers", "mics", "DSP"], "build": "listen test", "time": "4h", "level": "intermediate", "safety": "none", "notes": "lesson: fight waves with waves"},
  {"kind": "gm", "t": "The French Press", "tier": "Compounded", "concept": "paper filters strip flavor", "mechanism": "mesh plunger separates grounds cleanly", "parts": ["glass", "mesh"], "build": "brew test", "time": "2h", "level": "intermediate", "safety": "glass hot", "notes": "lesson: subtraction (no filter) as feature"},
  {"kind": "gm", "t": "Instant Camera", "tier": "Compounded", "concept": "waiting for photos kills moments", "mechanism": "self-developing film chemistry", "parts": ["film", "lens"], "build": "shoot test", "time": "3h", "level": "intermediate", "safety": "none", "notes": "lesson: impatience as a market"},
  {"kind": "gm", "t": "The Leatherman", "tier": "Compounded", "concept": "toolbox won't fit pocket", "mechanism": "pliers-first multitool with inside tools", "parts": ["steel"], "build": "fold test", "time": "3h", "level": "intermediate", "safety": "tools sharp", "notes": "lesson: lead with the hardest tool (pliers)"},
  {"kind": "gm", "t": "Kindle / E-Reader", "tier": "Compounded", "concept": "books are heavy", "mechanism": "e-ink reflects light like paper", "parts": ["display", "battery"], "build": "read test", "time": "4h", "level": "intermediate", "safety": "none", "notes": "lesson: match the old medium's virtues"},
  {"kind": "gm", "t": "The Dyson Fan", "tier": "Compounded", "concept": "blades are ugly and unsafe", "mechanism": "air multiplier: induced airflow, no blades", "parts": ["motor", "loop"], "build": "feel test", "time": "4h", "level": "intermediate", "safety": "none", "notes": "lesson: remove the scary part entirely"},
  {"kind": "gm", "t": "Modular Phone Concept", "tier": "Compounded", "concept": "phones die as units", "mechanism": "modules swap: camera, battery, screen", "parts": ["modules"], "build": "swap test", "time": "6h", "level": "intermediate", "safety": "none", "notes": "lesson: longevity vs thinness tradeoff"},
  {"kind": "gm", "t": "The Rocket Stove", "tier": "Compounded", "concept": "open fires waste fuel", "mechanism": "insulated chimney + precise airflow burns clean", "parts": ["steel"], "build": "burn test", "time": "6h", "level": "intermediate", "safety": "fire safety", "notes": "lesson: efficiency from airflow geometry"},
  {"kind": "gm", "t": "Gravity Light", "tier": "Compounded", "concept": "kerosene is costly and smoky", "mechanism": "falling weight drives a generator", "parts": ["weight", "gears"], "build": "hang test", "time": "6h", "level": "intermediate", "safety": "weight drop zone", "notes": "lesson: gravity as a battery"},
  {"kind": "gm", "t": "The Hyperloop Concept", "tier": "Advanced", "concept": "traffic and short flights waste time", "mechanism": "low-pressure tube + maglev pods", "parts": ["tube", "magnets"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "lesson: old idea (vactrain) + new materials"},
  {"kind": "gm", "t": "SpaceX Reusable Booster", "tier": "Advanced", "concept": "rockets are disposable", "mechanism": "propulsive landing: grid fins + relight", "parts": ["engines", "fins"], "build": "watch landing", "time": "10h", "level": "advanced", "safety": "none", "notes": "lesson: the expensive part comes back"},
  {"kind": "gm", "t": "The Large Hadron Collider", "tier": "Advanced", "concept": "particles hide secrets", "mechanism": "27km ring accelerates protons to near light speed", "parts": ["magnets", "detectors"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "lesson: biggest machine ever built for curiosity"},
  {"kind": "gm", "t": "CRISPR (as object)", "tier": "Advanced", "concept": "genetic disease", "mechanism": "guide RNA directs Cas9 to edit DNA", "parts": ["protein", "RNA"], "build": "study", "time": "20h", "level": "advanced", "safety": "ethics", "notes": "lesson: a bacterial immune system becomes a tool"},
  {"kind": "gm", "t": "The James Webb Telescope", "tier": "Advanced", "concept": "atmosphere blurs space", "mechanism": "gold mirrors unfold a million miles out", "parts": ["mirrors", "sunshield"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "lesson: origami engineering at cosmic scale"},
  {"kind": "gm", "t": "Fusion Reactor (Tokamak)", "tier": "Advanced", "concept": "endless clean energy needed", "mechanism": "magnetic bottle holds 150M-degree plasma", "parts": ["magnets"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "lesson: building a star on Earth"},
  {"kind": "gm", "t": "The Panama Canal", "tier": "Advanced", "concept": "ships detour continents", "mechanism": "locks lift ships over mountains", "parts": ["locks", "water"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "lesson: water stairs for ocean giants"},
  {"kind": "gm", "t": "Burj Khalifa", "tier": "Advanced", "concept": "cities need vertical room", "mechanism": "buttressed core + setbacks resist wind", "parts": ["concrete", "steel"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "lesson: desert flower geometry at 828m"},
  {"kind": "gm", "t": "The Internet (as object)", "tier": "Advanced", "concept": "knowledge locked in places", "mechanism": "packet switching routes around damage", "parts": ["cables", "routers"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "lesson: designed to survive, ended up connecting"},
  {"kind": "gm", "t": "The Printing Press", "tier": "Advanced", "concept": "books cost fortunes", "mechanism": "movable type + press = mass pages", "parts": ["type", "press"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "lesson: the original information revolution"},
  {"kind": "gm", "t": "The Steam Engine", "tier": "Advanced", "concept": "mines flood", "mechanism": "pressure + vacuum pump water, then drive all", "parts": ["boiler", "piston"], "build": "study", "time": "10h", "level": "advanced", "safety": "pressure safety", "notes": "lesson: one machine starts industry"},
  {"kind": "gm", "t": "The Antikythera Mechanism", "tier": "Advanced", "concept": "ancient astronomy needed computing", "mechanism": "bronze gears predict eclipses", "parts": ["gears"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "lesson: 2,000-year-old analog computer"}
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

