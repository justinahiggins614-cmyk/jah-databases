(function(){'use strict';
/* JAH The Everyday Object Reinvention Database — real working generator, jahdb-db-everyday-object-reinvention-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EORS-";
var SLUG="db-everyday-object-reinvention";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Chair, Rethought", "tier": "Foundations", "concept": "chairs hurt backs", "mechanism": "saddle seat + tilt keeps spine neutral", "parts": ["seat", "base"], "build": "sit test", "time": "4h", "level": "beginner", "safety": "none", "notes": "prototype with cushions before building"},
  {"kind": "gm", "t": "The Humble Broom", "tier": "Foundations", "concept": "dust escapes bristles", "mechanism": "angled electrostatic head traps fine dust", "parts": ["head", "handle"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "reinvention: change the bristle, not the handle"},
  {"kind": "gm", "t": "The Door Handle", "tier": "Foundations", "concept": "hands full, handle useless", "mechanism": "foot pull + elbow lever options", "parts": ["lever"], "build": "install", "time": "3h", "level": "beginner", "safety": "none", "notes": "reinvention: design for occupied hands"},
  {"kind": "gm", "t": "The Light Switch", "tier": "Foundations", "concept": "fumbling in dark", "mechanism": "glow + large paddle, voice backup", "parts": ["switch"], "build": "install", "time": "2h", "level": "beginner", "safety": "electrical: breaker off", "notes": "reinvention: the switch finds you"},
  {"kind": "gm", "t": "The Coffee Mug", "tier": "Foundations", "concept": "coffee cools, hands burn", "mechanism": "double-wall ceramic + thumb rest", "parts": ["clay"], "build": "throw", "time": "6h", "level": "beginner", "safety": "kiln safety", "notes": "reinvention: thermal comfort as feature"},
  {"kind": "gm", "t": "The Backpack Strap", "tier": "Foundations", "concept": "straps dig shoulders", "mechanism": "wide curved + sternum load share", "parts": ["webbing"], "build": "sew", "time": "4h", "level": "beginner", "safety": "none", "notes": "reinvention: distribute, don't pad"},
  {"kind": "gm", "t": "The Kitchen Knife Handle", "tier": "Foundations", "concept": "grips slip wet", "mechanism": "oval + textured, finger guard", "parts": ["handle"], "build": "shape", "time": "4h", "level": "beginner", "safety": "blade sharp", "notes": "reinvention: the handle is half the knife"},
  {"kind": "gm", "t": "The Umbrella, Again", "tier": "Foundations", "concept": "umbrellas flip", "mechanism": "vented double canopy spills wind", "parts": ["fabric"], "build": "sew", "time": "8h", "level": "beginner", "safety": "none", "notes": "reinvention: let wind through, don't fight it"},
  {"kind": "gm", "t": "The Pillow", "tier": "Foundations", "concept": "necks ache", "mechanism": "contoured memory foam + cooling", "parts": ["foam"], "build": "cut", "time": "3h", "level": "beginner", "safety": "none", "notes": "reinvention: sleep position dictates shape"},
  {"kind": "gm", "t": "The Wallet", "tier": "Foundations", "concept": "wallets bulk pockets", "mechanism": "6-card + cash strap minimal", "parts": ["leather"], "build": "stitch", "time": "4h", "level": "beginner", "safety": "none", "notes": "reinvention: carry less, better"},
  {"kind": "gm", "t": "The Water Bottle", "tier": "Foundations", "concept": "bottles leak in bags", "mechanism": "locking cap + one-hand open", "parts": ["bottle"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "reinvention: the cap is the product"},
  {"kind": "gm", "t": "The Desk Lamp", "tier": "Compounded", "concept": "glare strains eyes", "mechanism": "asymmetric lens throws light forward only", "parts": ["LED", "lens"], "build": "build", "time": "8h", "level": "intermediate", "safety": "low-voltage", "notes": "reinvention: light the desk, not the eyes"},
  {"kind": "gm", "t": "The Toaster", "tier": "Compounded", "concept": "toast burns edges", "mechanism": "even radiant + auto-lower", "parts": ["elements"], "build": "wire", "time": "10h", "level": "intermediate", "safety": "mains electricity — pro only", "notes": "reinvention: evenness over speed"},
  {"kind": "gm", "t": "The Vacuum Cleaner", "tier": "Compounded", "concept": "bags lose suction", "mechanism": "cyclonic separation, no bag", "parts": ["motor", "cone"], "build": "test", "time": "12h", "level": "intermediate", "safety": "dust mask", "notes": "reinvention: remove the consumable"},
  {"kind": "gm", "t": "The Alarm Clock", "tier": "Compounded", "concept": "alarms jolt awake", "mechanism": "dawn simulation + gradual sound", "parts": ["LED", "speaker"], "build": "build", "time": "8h", "level": "intermediate", "safety": "low-voltage", "notes": "reinvention: wake like sunrise"},
  {"kind": "gm", "t": "The Suitcase", "tier": "Compounded", "concept": "bags tip and drag", "mechanism": "4 spinner wheels + low center", "parts": ["wheels"], "build": "fit", "time": "6h", "level": "intermediate", "safety": "none", "notes": "reinvention: wheels changed everything twice"},
  {"kind": "gm", "t": "The Shower Head", "tier": "Compounded", "concept": "showers waste water", "mechanism": "air-injected droplets feel full at 1.5gpm", "parts": ["head"], "build": "install", "time": "2h", "level": "intermediate", "safety": "none", "notes": "reinvention: feel vs flow"},
  {"kind": "gm", "t": "The Cutting Board", "tier": "Compounded", "concept": "boards dull knives", "mechanism": "end-grain wood self-heals", "parts": ["wood"], "build": "glue", "time": "8h", "level": "intermediate", "safety": "none", "notes": "reinvention: orientation matters"},
  {"kind": "gm", "t": "The Bike Lock", "tier": "Compounded", "concept": "locks get cut", "mechanism": "hardened U + alarm shackle", "parts": ["steel"], "build": "test", "time": "6h", "level": "intermediate", "safety": "none", "notes": "reinvention: deter, delay, detect"},
  {"kind": "gm", "t": "The Iron", "tier": "Compounded", "concept": "irons drip and scorch", "mechanism": "steam burst + auto-off", "parts": ["element"], "build": "pro", "time": "10h", "level": "intermediate", "safety": "mains — pro only", "notes": "reinvention: safety as feature"},
  {"kind": "gm", "t": "The Trash Can", "tier": "Compounded", "concept": "bags slip, smells escape", "mechanism": "motion lid + carbon filter", "parts": ["can"], "build": "fit", "time": "4h", "level": "intermediate", "safety": "none", "notes": "reinvention: the bin disappears"},
  {"kind": "gm", "t": "The Fan", "tier": "Compounded", "concept": "fans are noisy", "mechanism": "bladeless + quiet DC motor", "parts": ["motor"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "reinvention: silence is the upgrade"},
  {"kind": "gm", "t": "The Refrigerator Shelf", "tier": "Advanced", "concept": "fridge space wastes", "mechanism": "split sliding + door-in-door", "parts": ["glass"], "build": "fit", "time": "12h", "level": "advanced", "safety": "none", "notes": "reinvention: access beats volume"},
  {"kind": "gm", "t": "The Washing Machine", "tier": "Advanced", "concept": "washers waste water", "mechanism": "front-load + recirculating", "parts": ["drum"], "build": "pro", "time": "20h", "level": "advanced", "safety": "plumbing pro", "notes": "reinvention: tumble, don't agitate"},
  {"kind": "gm", "t": "The Stove", "tier": "Advanced", "concept": "burners heat uneven", "mechanism": "induction zones + bridge", "parts": ["coils"], "build": "pro", "time": "20h", "level": "advanced", "safety": "electrical pro", "notes": "reinvention: heat the pan, not the air"},
  {"kind": "gm", "t": "The Toilet", "tier": "Advanced", "concept": "toilets waste water", "mechanism": "dual-flush + pressure assist", "parts": ["valves"], "build": "pro", "time": "16h", "level": "advanced", "safety": "plumbing pro", "notes": "reinvention: 1.6 gallons can work"},
  {"kind": "gm", "t": "The Mattress", "tier": "Advanced", "concept": "mattresses sleep hot", "mechanism": "zoned coils + airflow layers", "parts": ["coils", "foam"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "reinvention: zones, not one firmness"},
  {"kind": "gm", "t": "The Window", "tier": "Advanced", "concept": "windows leak energy", "mechanism": "triple glaze + low-e + argon", "parts": ["glass"], "build": "pro", "time": "20h", "level": "advanced", "safety": "glass handling pro", "notes": "reinvention: the window as wall"},
  {"kind": "gm", "t": "The Doorbell", "tier": "Advanced", "concept": "missed visitors", "mechanism": "camera + motion + phone alert", "parts": ["camera"], "build": "install", "time": "8h", "level": "advanced", "safety": "low-voltage", "notes": "reinvention: the doorbell sees"},
  {"kind": "gm", "t": "The Thermostat", "tier": "Advanced", "concept": "heating wastes energy", "mechanism": "learning schedule + sensors", "parts": ["thermostat"], "build": "install", "time": "8h", "level": "advanced", "safety": "HVAC wiring — pro if unsure", "notes": "reinvention: the house learns"},
  {"kind": "gm", "t": "The Smoke Detector", "tier": "Advanced", "concept": "alarms false-trigger", "mechanism": "photoelectric + hush + 10yr battery", "parts": ["detector"], "build": "install", "time": "4h", "level": "advanced", "safety": "none", "notes": "reinvention: trust keeps it on the ceiling"},
  {"kind": "gm", "t": "The Fire Extinguisher", "tier": "Advanced", "concept": "extinguishers confuse", "mechanism": "one-pull + clear pictograms", "parts": ["extinguisher"], "build": "mount", "time": "2h", "level": "advanced", "safety": "none", "notes": "reinvention: usability saves lives"},
  {"kind": "gm", "t": "The Ladder", "tier": "Advanced", "concept": "ladders tip", "mechanism": "wide base + levelers + platform step", "parts": ["ladder"], "build": "use", "time": "4h", "level": "advanced", "safety": "ladder safety", "notes": "reinvention: stability is the feature"},
  {"kind": "gm", "t": "The Step Stool", "tier": "Advanced", "concept": "reach safely", "mechanism": "fold + grip + light", "parts": ["stool"], "build": "build", "time": "10h", "level": "advanced", "safety": "ladder safety", "notes": "reinvention: the forgotten essential"}
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

