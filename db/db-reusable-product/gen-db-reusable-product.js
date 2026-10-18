(function(){'use strict';
/* JAH The Reusable Product Universe — real working generator, jahdb-db-reusable-product-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-REPR-";
var SLUG="db-reusable-product";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Water Bottle (Steel)", "tier": "Foundations", "concept": "ditch plastic", "mechanism": "insulated steel", "parts": ["bottle"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "reuse: 1000+ uses"},
  {"kind": "gm", "t": "Coffee Cup (Reusable)", "tier": "Foundations", "concept": "daily waste", "mechanism": "insulated + lid", "parts": ["cup"], "build": "study", "time": "1h", "level": "beginner", "safety": "hot", "notes": "reuse: cafes discount"},
  {"kind": "gm", "t": "Shopping Bags", "tier": "Foundations", "concept": "bag mountain", "mechanism": "5 sturdy totes", "parts": ["bags"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "reuse: car + door habit"},
  {"kind": "gm", "t": "Produce Bags", "tier": "Foundations", "concept": "plastic produce", "mechanism": "mesh set", "parts": ["bags"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "reuse: tare at scale"},
  {"kind": "gm", "t": "Beeswax Wraps", "tier": "Foundations", "concept": "cling waste", "mechanism": "washable wraps", "parts": ["wraps"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "reuse: 1 year each"},
  {"kind": "gm", "t": "Cloth Napkins", "tier": "Foundations", "concept": "paper pile", "mechanism": "24 cloth", "parts": ["napkins"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "reuse: dark hides stains"},
  {"kind": "gm", "t": "Handkerchiefs", "tier": "Foundations", "concept": "tissue waste", "mechanism": "12 cotton", "parts": ["hanks"], "build": "use", "time": "1h", "level": "beginner", "safety": "hygiene", "notes": "reuse: hot wash"},
  {"kind": "gm", "t": "Razor (Safety)", "tier": "Foundations", "concept": "plastic razors", "mechanism": "metal safety + blades", "parts": ["razor"], "build": "learn", "time": "2h", "level": "beginner", "safety": "blade", "notes": "reuse: 10c per blade"},
  {"kind": "gm", "t": "Menstrual Cup", "tier": "Foundations", "concept": "monthly waste", "mechanism": "cup 10-year", "parts": ["cup"], "build": "learn", "time": "2h", "level": "beginner", "safety": "hygiene", "notes": "reuse: boil monthly"},
  {"kind": "gm", "t": "Cloth Diapers", "tier": "Foundations", "concept": "diaper mountain", "mechanism": "24 + covers", "parts": ["diapers"], "build": "learn", "time": "4h", "level": "beginner", "safety": "wash routine", "notes": "reuse: 2.5yr payback"},
  {"kind": "gm", "t": "Swedish Dishcloths", "tier": "Foundations", "concept": "paper towels", "mechanism": "10 compostable", "parts": ["cloths"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "reuse: 200 uses each"},
  {"kind": "gm", "t": "Silicone Lids", "tier": "Compounded", "concept": "wrap waste", "mechanism": "stretch lids set", "parts": ["lids"], "build": "use", "time": "1h", "level": "intermediate", "safety": "none", "notes": "reuse: bowl + can"},
  {"kind": "gm", "t": "Stasher Bags", "tier": "Compounded", "concept": "ziploc habit", "mechanism": "silicone bags", "parts": ["bags"], "build": "use", "time": "1h", "level": "intermediate", "safety": "none", "notes": "reuse: freezer + sous vide"},
  {"kind": "gm", "t": "Shampoo Bars", "tier": "Compounded", "concept": "bottle waste", "mechanism": "bar + tin", "parts": ["bars"], "build": "use", "time": "2h", "level": "intermediate", "safety": "transition", "notes": "reuse: 80 washes"},
  {"kind": "gm", "t": "Soap Nuts / Berries", "tier": "Compounded", "concept": "detergent jugs", "mechanism": "wash berries", "parts": ["nuts"], "build": "use", "time": "2h", "level": "intermediate", "safety": "none", "notes": "reuse: compost after"},
  {"kind": "gm", "t": "Bidet Attachment", "tier": "Compounded", "concept": "paper waste", "mechanism": "seat bidet", "parts": ["bidet"], "build": "install", "time": "2h", "level": "intermediate", "safety": "plumbing", "notes": "reuse: 75% less paper"},
  {"kind": "gm", "t": "Compostable Sponges", "tier": "Compounded", "concept": "plastic sponges", "mechanism": "loofah + cellulose", "parts": ["sponges"], "build": "use", "time": "1h", "level": "intermediate", "safety": "none", "notes": "reuse: sanitize weekly"},
  {"kind": "gm", "t": "Refill Station Map", "tier": "Compounded", "concept": "refills where?", "mechanism": "local map + jars", "parts": ["map"], "build": "make", "time": "4h", "level": "intermediate", "safety": "none", "notes": "reuse: tare jars"},
  {"kind": "gm", "t": "Milk (Glass Bottle)", "tier": "Compounded", "concept": "jug waste", "mechanism": "delivery + return", "parts": ["service"], "build": "join", "time": "2h", "level": "intermediate", "safety": "none", "notes": "reuse: old school returns"},
  {"kind": "gm", "t": "Bulk Shopping Kit", "tier": "Compounded", "concept": "package-free", "mechanism": "jars + bags + list", "parts": ["kit"], "build": "pack", "time": "3h", "level": "intermediate", "safety": "tare", "notes": "reuse: system beats willpower"},
  {"kind": "gm", "t": "Diaper Service", "tier": "Compounded", "concept": "wash hassle", "mechanism": "service + cloth", "parts": ["service"], "build": "join", "time": "2h", "level": "intermediate", "safety": "none", "notes": "reuse: best of both"},
  {"kind": "gm", "t": "Tool Library", "tier": "Compounded", "concept": "buy rarely", "mechanism": "borrow tools", "parts": ["library"], "build": "join", "time": "2h", "level": "intermediate", "safety": "none", "notes": "reuse: share economy"},
  {"kind": "gm", "t": "Safety Razor (Women's)", "tier": "Compounded", "concept": "smooth + waste-free", "mechanism": "long handle", "parts": ["razor"], "build": "learn", "time": "2h", "level": "intermediate", "safety": "blade", "notes": "reuse: no pressure"},
  {"kind": "gm", "t": "Period Underwear", "tier": "Compounded", "concept": "backup + planet", "mechanism": "absorbent", "parts": ["underwear"], "build": "use", "time": "2h", "level": "intermediate", "safety": "hygiene", "notes": "reuse: rinse cold"},
  {"kind": "gm", "t": "Zero-Waste Kitchen", "tier": "Advanced", "concept": "trash jar year", "mechanism": "systems + bulk", "parts": ["kitchen"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "reuse: 5 Rs order"},
  {"kind": "gm", "t": "Package-Free Home", "tier": "Advanced", "concept": "no trash", "mechanism": "refill + make", "parts": ["home"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "reuse: gradual, room by room"},
  {"kind": "gm", "t": "Community Fridge", "tier": "Advanced", "concept": "food waste", "mechanism": "share fridge", "parts": ["fridge"], "build": "start", "time": "20h", "level": "advanced", "safety": "food safety", "notes": "reuse: take what need"},
  {"kind": "gm", "t": "Repair Cafe", "tier": "Advanced", "concept": "throwaway culture", "mechanism": "monthly fix events", "parts": ["cafe"], "build": "start", "time": "30h", "level": "advanced", "safety": "none", "notes": "reuse: fix > replace"},
  {"kind": "gm", "t": "Library of Things", "tier": "Advanced", "concept": "own less", "mechanism": "borrow library", "parts": ["library"], "build": "start", "time": "40h", "level": "advanced", "safety": "none", "notes": "reuse: 1000 items shared"},
  {"kind": "gm", "t": "Refill Shop (Open)", "tier": "Advanced", "concept": "sell refills", "mechanism": "bulk + tare", "parts": ["shop"], "build": "open", "time": "200h", "level": "advanced", "safety": "business", "notes": "reuse: weigh, fill, pay"},
  {"kind": "gm", "t": "Compost Collective", "tier": "Advanced", "concept": "scraps to soil", "mechanism": "neighborhood pickup", "parts": ["service"], "build": "start", "time": "40h", "level": "advanced", "safety": "none", "notes": "reuse: 5-gal buckets"},
  {"kind": "gm", "t": "Clothing Swap", "tier": "Advanced", "concept": "fast fashion", "mechanism": "swap events", "parts": ["swap"], "build": "host", "time": "16h", "level": "advanced", "safety": "none", "notes": "reuse: quality over quantity"},
  {"kind": "gm", "t": "Food Rescue", "tier": "Advanced", "concept": "waste food", "mechanism": "rescue + share", "parts": ["program"], "build": "start", "time": "30h", "level": "advanced", "safety": "food safety", "notes": "reuse: apps help"},
  {"kind": "gm", "t": "Master Reuse Systems", "tier": "Advanced", "concept": "everything", "mechanism": "home + community", "parts": ["systems"], "build": "build", "time": "80h", "level": "advanced", "safety": "none", "notes": "reuse: culture shift"}
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

