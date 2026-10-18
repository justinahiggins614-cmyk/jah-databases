(function(){'use strict';
/* JAH The Pet-Tech Invention Database — real working generator, jahdb-db-pet-tech-invention-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PTIS-";
var SLUG="db-pet-tech-invention";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing.", "Pet products: non-toxic materials, no small detachable parts, chew-proof cords on heated items."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Slow Feeder Bowl", "tier": "Foundations", "concept": "gobble + bloat", "mechanism": "maze slows eating", "parts": ["bowl"], "build": "study", "time": "1h", "level": "beginner", "safety": "food-safe", "notes": "pet: 10-min meals"},
  {"kind": "gm", "t": "Snuffle Mat", "tier": "Foundations", "concept": "bored noses", "mechanism": "fabric strips hide treats", "parts": ["mat"], "build": "make", "time": "3h", "level": "beginner", "safety": "supervise", "notes": "pet: forage instinct"},
  {"kind": "gm", "t": "Lick Mat", "tier": "Foundations", "concept": "anxious licking", "mechanism": "texture + spread", "parts": ["mat"], "build": "study", "time": "1h", "level": "beginner", "safety": "food-safe", "notes": "pet: peanut butter thin"},
  {"kind": "gm", "t": "Water Fountain", "tier": "Foundations", "concept": "stale water", "mechanism": "flowing + filter", "parts": ["fountain"], "build": "clean", "time": "2h", "level": "beginner", "safety": "electrical", "notes": "pet: clean weekly"},
  {"kind": "gm", "t": "ID Tag (Engraved)", "tier": "Foundations", "concept": "lost pets", "mechanism": "tag + microchip", "parts": ["tag"], "build": "order", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: chip + tag both"},
  {"kind": "gm", "t": "Treat Pouch", "tier": "Foundations", "concept": "training treats", "mechanism": "belt pouch", "parts": ["pouch"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: high-value rewards"},
  {"kind": "gm", "t": "Grooming Brush", "tier": "Foundations", "concept": "shedding", "mechanism": "deshed tool", "parts": ["brush"], "build": "study", "time": "1h", "level": "beginner", "safety": "gentle", "notes": "pet: short sessions"},
  {"kind": "gm", "t": "Nail Clippers", "tier": "Foundations", "concept": "clicking nails", "mechanism": "clipper + styptic", "parts": ["clipper"], "build": "learn", "time": "2h", "level": "beginner", "safety": "quick safety", "notes": "pet: tiny trims weekly"},
  {"kind": "gm", "t": "Poop Bag Holder", "tier": "Foundations", "concept": "walks need bags", "mechanism": "dispenser + bags", "parts": ["holder"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: always carry 2"},
  {"kind": "gm", "t": "Collar Light", "tier": "Foundations", "concept": "night walks", "mechanism": "LED clip", "parts": ["light"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: be seen"},
  {"kind": "gm", "t": "Calming Shirt", "tier": "Foundations", "concept": "anxiety", "mechanism": "gentle pressure wrap", "parts": ["shirt"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: introduce calmly"},
  {"kind": "gm", "t": "Automatic Feeder", "tier": "Compounded", "concept": "schedule feeding", "mechanism": "timed portions", "parts": ["feeder"], "build": "set", "time": "3h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: test 3 days"},
  {"kind": "gm", "t": "Pet Camera + Treat", "tier": "Compounded", "concept": "check + reward", "mechanism": "cam + toss", "parts": ["device"], "build": "install", "time": "4h", "level": "intermediate", "safety": "none", "notes": "pet: talk calmly"},
  {"kind": "gm", "t": "GPS Tracker (Collar)", "tier": "Compounded", "concept": "escape artists", "mechanism": "GPS collar", "parts": ["tracker"], "build": "fit", "time": "2h", "level": "intermediate", "safety": "fit 2 fingers", "notes": "pet: charge weekly"},
  {"kind": "gm", "t": "Smart Door (Pet)", "tier": "Compounded", "concept": "in/out freedom", "mechanism": "chip-reading flap", "parts": ["door"], "build": "install", "time": "6h", "level": "intermediate", "safety": "none", "notes": "pet: train with treats"},
  {"kind": "gm", "t": "Activity Monitor", "tier": "Compounded", "concept": "enough exercise?", "mechanism": "collar tracker", "parts": ["monitor"], "build": "fit", "time": "2h", "level": "intermediate", "safety": "none", "notes": "pet: breed baselines"},
  {"kind": "gm", "t": "Self-Cleaning Litter", "tier": "Compounded", "concept": "scooping chore", "mechanism": "auto rake box", "parts": ["box"], "build": "set", "time": "4h", "level": "intermediate", "safety": "none", "notes": "pet: transition slowly"},
  {"kind": "gm", "t": "Elevated Feeder", "tier": "Compounded", "concept": "neck strain", "mechanism": "raised bowls", "parts": ["feeder"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "pet: elbow height"},
  {"kind": "gm", "t": "Cooling Mat", "tier": "Compounded", "concept": "hot pets", "mechanism": "pressure-activated gel", "parts": ["mat"], "build": "study", "time": "1h", "level": "intermediate", "safety": "non-toxic", "notes": "pet: shade too"},
  {"kind": "gm", "t": "Heated Bed", "tier": "Compounded", "concept": "old joints", "mechanism": "low-watt heat", "parts": ["bed"], "build": "study", "time": "1h", "level": "intermediate", "safety": "chew-proof cord", "notes": "pet: thermostat control"},
  {"kind": "gm", "t": "Puzzle Feeders (Set)", "tier": "Compounded", "concept": "bored brains", "mechanism": "levels 1-3 puzzles", "parts": ["puzzles"], "build": "study", "time": "3h", "level": "intermediate", "safety": "supervise", "notes": "pet: start easy"},
  {"kind": "gm", "t": "Car Barrier", "tier": "Compounded", "concept": "safe travel", "mechanism": "barrier + harness", "parts": ["barrier"], "build": "install", "time": "2h", "level": "intermediate", "safety": "crash-tested", "notes": "pet: back seat only"},
  {"kind": "gm", "t": "Pet Stroller", "tier": "Advanced", "concept": "old/small pets", "mechanism": "stroller + mesh", "parts": ["stroller"], "build": "study", "time": "2h", "level": "advanced", "safety": "brakes", "notes": "pet: zip closed"},
  {"kind": "gm", "t": "Wheelchair (Pet)", "tier": "Advanced", "concept": "mobility loss", "mechanism": "rear support cart", "parts": ["cart"], "build": "fit", "time": "6h", "level": "advanced", "safety": "vet fit", "notes": "pet: vet guidance"},
  {"kind": "gm", "t": "Prosthetic (Pet)", "tier": "Advanced", "concept": "limb loss", "mechanism": "custom prosthetic", "parts": ["prosthetic"], "build": "pro", "time": "20h", "level": "advanced", "safety": "vet pro", "notes": "pet: rehab plan"},
  {"kind": "gm", "t": "Oxygen Cage (DIY?)", "tier": "Advanced", "concept": "breathing crisis", "mechanism": "vet only", "parts": ["vet"], "build": "vet", "time": "1h", "level": "advanced", "safety": "vet only", "notes": "pet: emergency vet now"},
  {"kind": "gm", "t": "Rehab Pool", "tier": "Advanced", "concept": "joint rehab", "mechanism": "warm water therapy", "parts": ["pool"], "build": "build", "time": "20h", "level": "advanced", "safety": "vet pro", "notes": "pet: supervised only"},
  {"kind": "gm", "t": "Enrichment Room", "tier": "Advanced", "concept": "indoor life", "mechanism": "climbing + hiding", "parts": ["room"], "build": "build", "time": "30h", "level": "advanced", "safety": "non-toxic", "notes": "pet: vertical space"},
  {"kind": "gm", "t": "Catio (Enclosure)", "tier": "Advanced", "concept": "safe outdoors", "mechanism": "mesh + shelves", "parts": ["catio"], "build": "build", "time": "30h", "level": "advanced", "safety": "secure", "notes": "pet: escape-proof"},
  {"kind": "gm", "t": "Aquarium (Species Tank)", "tier": "Advanced", "concept": "fish thrive", "mechanism": "biotope setup", "parts": ["tank"], "build": "build", "time": "20h", "level": "advanced", "safety": "cycle", "notes": "pet: research species"},
  {"kind": "gm", "t": "Aviary (Indoor)", "tier": "Advanced", "concept": "birds fly", "mechanism": "large flight cage", "parts": ["aviary"], "build": "build", "time": "40h", "level": "advanced", "safety": "safe metals", "notes": "pet: no Teflon fumes"},
  {"kind": "gm", "t": "Reptile Bioactive", "tier": "Advanced", "concept": "natural living", "mechanism": "bioactive vivarium", "parts": ["viv"], "build": "build", "time": "30h", "level": "advanced", "safety": "heat safety", "notes": "pet: thermostat all heat"},
  {"kind": "gm", "t": "Master Pet Tech Home", "tier": "Advanced", "concept": "everything", "mechanism": "integrated system", "parts": ["home"], "build": "build", "time": "60h", "level": "advanced", "safety": "pro", "notes": "pet: pet-first design"},
  {"kind": "gm", "t": "Cat Wheel", "tier": "Advanced", "concept": "indoor zoomies", "mechanism": "exercise wheel", "parts": ["wheel"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "pet: train with treats"}
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

