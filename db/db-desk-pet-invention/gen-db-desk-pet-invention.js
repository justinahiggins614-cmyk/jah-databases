(function(){'use strict';
/* JAH The Desk Pet Invention Database — real working generator, jahdb-db-desk-pet-invention-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DPI-";
var SLUG="db-desk-pet-invention";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Wobble Bot (Wind-Up)", "tier": "Foundations", "concept": "desk joy", "mechanism": "wind-up wobble", "parts": ["toy"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: the gateway desk pet"},
  {"kind": "gm", "t": "Solar Dancer", "tier": "Foundations", "concept": "sunshine moves", "mechanism": "solar + wobble", "parts": ["solar"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: needs bright desk"},
  {"kind": "gm", "t": "Newton Cradle (Mini)", "tier": "Foundations", "concept": "clickety calm", "mechanism": "mini cradle", "parts": ["cradle"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: pull and release"},
  {"kind": "gm", "t": "Sand Art Frame", "tier": "Foundations", "concept": "mesmerizing", "mechanism": "flip + settle", "parts": ["sand"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: new scene each flip"},
  {"kind": "gm", "t": "Liquid Motion Tumbler", "tier": "Foundations", "concept": "calm watching", "mechanism": "slow oil drip", "parts": ["tumbler"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: flip for calm"},
  {"kind": "gm", "t": "Ferrofluid Desk Toy", "tier": "Foundations", "concept": "alien blob", "mechanism": "magnet moves fluid", "parts": ["ferro"], "build": "study", "time": "2h", "level": "beginner", "safety": "stains", "notes": "pet: sealed only"},
  {"kind": "gm", "t": "Kinetic Rings", "tier": "Foundations", "concept": "spin calm", "mechanism": "magnetic levitation", "parts": ["rings"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: spin and breathe"},
  {"kind": "gm", "t": "Mini Zen Garden", "tier": "Foundations", "concept": "rake calm", "mechanism": "sand + rake + stones", "parts": ["garden"], "build": "make", "time": "2h", "level": "beginner", "safety": "none", "notes": "pet: rake daily"},
  {"kind": "gm", "t": "Decision Maker (Ball)", "tier": "Foundations", "concept": "decide fun", "mechanism": "shake ball answers", "parts": ["ball"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: ask wisely"},
  {"kind": "gm", "t": "Wacky Wobbler", "tier": "Foundations", "concept": "nodding joy", "mechanism": "bobblehead", "parts": ["wobbler"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: dashboard classic"},
  {"kind": "gm", "t": "Stress Ball", "tier": "Foundations", "concept": "squeeze stress", "mechanism": "foam ball", "parts": ["ball"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "pet: keep two"},
  {"kind": "gm", "t": "USB Aquarium", "tier": "Compounded", "concept": "tiny fish", "mechanism": "USB + plastic fish", "parts": ["tank"], "build": "build", "time": "6h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: no real fish — plastic only"},
  {"kind": "gm", "t": "Mini Robot Pet", "tier": "Compounded", "concept": "beeps back", "mechanism": "arduino + servo", "parts": ["robot"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: personality in code"},
  {"kind": "gm", "t": "Plant Pet (Smart)", "tier": "Compounded", "concept": "green friend", "mechanism": "sensor + face pot", "parts": ["plant"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: waters itself-ish"},
  {"kind": "gm", "t": "Kinetic Sculpture", "tier": "Compounded", "concept": "moving art", "mechanism": "motor + arms", "parts": ["art"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: perpetual motion-ish"},
  {"kind": "gm", "t": "Digital Pet (Tamagotchi+)", "tier": "Compounded", "concept": "care habit", "mechanism": "screen + buttons", "parts": ["pet"], "build": "build", "time": "20h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: feed on time"},
  {"kind": "gm", "t": "Wind-Up Walker", "tier": "Compounded", "concept": "walks desk", "mechanism": "clockwork legs", "parts": ["walker"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "pet: wind and watch"},
  {"kind": "gm", "t": "Magnetic Sculpture", "tier": "Compounded", "concept": "build shapes", "mechanism": "magnetic balls", "parts": ["balls"], "build": "study", "time": "2h", "level": "intermediate", "safety": "magnets swallow", "notes": "pet: 216 balls zen"},
  {"kind": "gm", "t": "Levitating Plant", "tier": "Compounded", "concept": "floats!", "mechanism": "maglev planter", "parts": ["lev"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "pet: spin slowly"},
  {"kind": "gm", "t": "Hourglass (1-Min)", "tier": "Compounded", "concept": "time visible", "mechanism": "sand timer", "parts": ["glass"], "build": "study", "time": "1h", "level": "intermediate", "safety": "glass", "notes": "pet: focus sprints"},
  {"kind": "gm", "t": "Perpetual Motion (Fake)", "tier": "Compounded", "concept": "wonder", "mechanism": "hidden battery mobile", "parts": ["mobile"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: label the trick"},
  {"kind": "gm", "t": "Mood Lamp Pet", "tier": "Compounded", "concept": "glows feelings", "mechanism": "color + touch", "parts": ["lamp"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "pet: tap to change"},
  {"kind": "gm", "t": "Kinetic Desk Toy (Gears)", "tier": "Compounded", "concept": "watch work", "mechanism": "gear + crank", "parts": ["toy"], "build": "build", "time": "12h", "level": "intermediate", "safety": "pinch", "notes": "pet: crank calm"},
  {"kind": "gm", "t": "Robot Arm (Tiny)", "tier": "Advanced", "concept": "grab things", "mechanism": "4DOF mini arm", "parts": ["arm"], "build": "build", "time": "30h", "level": "advanced", "safety": "low-voltage", "notes": "pet: pick up paperclips"},
  {"kind": "gm", "t": "AI Desk Companion", "tier": "Advanced", "concept": "talks back", "mechanism": "voice + display", "parts": ["ai"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "pet: personality scripted"},
  {"kind": "gm", "t": "Self-Watering Terrarium", "tier": "Advanced", "concept": "ecosystem", "mechanism": "sealed + cycle", "parts": ["terra"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "pet: months sealed"},
  {"kind": "gm", "t": "Ants (Gel Farm)", "tier": "Advanced", "concept": "live colony", "mechanism": "gel + ants", "parts": ["farm"], "build": "study", "time": "4h", "level": "advanced", "safety": "escape-proof", "notes": "pet: no queen = months"},
  {"kind": "gm", "t": "Sea Monkeys+", "tier": "Advanced", "concept": "instant pets", "mechanism": "brine shrimp kit", "parts": ["kit"], "build": "study", "time": "2h", "level": "advanced", "safety": "none", "notes": "pet: aerate daily"},
  {"kind": "gm", "t": "Moss Ball (Marimo)", "tier": "Advanced", "concept": "slow friend", "mechanism": "marimo + jar", "parts": ["moss"], "build": "study", "time": "1h", "level": "advanced", "safety": "none", "notes": "pet: roll weekly, lives years"},
  {"kind": "gm", "t": "Triops Kit", "tier": "Advanced", "concept": "prehistoric pets", "mechanism": "eggs + tank", "parts": ["triops"], "build": "study", "time": "4h", "level": "advanced", "safety": "none", "notes": "pet: hatch in days"},
  {"kind": "gm", "t": "Mini Ecosystem (Sealed)", "tier": "Advanced", "concept": "world in jar", "mechanism": "plants + water sealed", "parts": ["jar"], "build": "build", "time": "8h", "level": "advanced", "safety": "none", "notes": "pet: balance light"},
  {"kind": "gm", "t": "Programmable Pet", "tier": "Advanced", "concept": "your code pet", "mechanism": "micro:bit + motors", "parts": ["pet"], "build": "build", "time": "30h", "level": "advanced", "safety": "low-voltage", "notes": "pet: teach tricks"},
  {"kind": "gm", "t": "Desk Pet Museum", "tier": "Advanced", "concept": "collection", "mechanism": "curated shelf", "parts": ["museum"], "build": "curate", "time": "10h", "level": "advanced", "safety": "none", "notes": "pet: label each era"},
  {"kind": "gm", "t": "Desk Fountain (Tiny)", "tier": "Advanced", "concept": "water calm", "mechanism": "pump + stones", "parts": ["fountain"], "build": "build", "time": "10h", "level": "advanced", "safety": "water+electric", "notes": "pet: white noise"}
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

