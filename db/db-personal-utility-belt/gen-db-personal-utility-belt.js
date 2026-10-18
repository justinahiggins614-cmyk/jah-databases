(function(){'use strict';
/* JAH The Personal Utility Belt Database — real working generator, jahdb-db-personal-utility-belt-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PEUTBE-";
var SLUG="db-personal-utility-belt";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Minimalist Wallet", "tier": "Foundations", "concept": "bulk kills pockets", "mechanism": "6 cards + cash band", "parts": ["wallet"], "build": "make", "time": "3h", "level": "beginner", "safety": "none", "notes": "carry: front pocket, always"},
  {"kind": "gm", "t": "Key Organizer", "tier": "Foundations", "concept": "keys stab thighs", "mechanism": "stacked silencer", "parts": ["organizer"], "build": "build", "time": "2h", "level": "beginner", "safety": "none", "notes": "carry: silent pocket"},
  {"kind": "gm", "t": "Pocket Knife (EDC)", "tier": "Foundations", "concept": "daily cutting", "mechanism": "3in folder, one-hand", "parts": ["knife"], "build": "study", "time": "1h", "level": "beginner", "safety": "blade laws", "notes": "carry: check local laws"},
  {"kind": "gm", "t": "Mini Flashlight", "tier": "Foundations", "concept": "darkness surprises", "mechanism": "500lm AAA light", "parts": ["light"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "carry: bezel up"},
  {"kind": "gm", "t": "Pen (EDC)", "tier": "Foundations", "concept": "pens die", "mechanism": "metal bolt-action pen", "parts": ["pen"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "carry: writes anywhere"},
  {"kind": "gm", "t": "Multitool (Pocket)", "tier": "Foundations", "concept": "fixes happen", "mechanism": "pliers-based mini", "parts": ["tool"], "build": "study", "time": "1h", "level": "beginner", "safety": "tools sharp", "notes": "carry: belt sheath"},
  {"kind": "gm", "t": "Phone + Case", "tier": "Foundations", "concept": "phone is tool", "mechanism": "cases with grip", "parts": ["phone"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "carry: the hub"},
  {"kind": "gm", "t": "Lighter", "tier": "Foundations", "concept": "fire useful", "mechanism": "butane insert", "parts": ["light"], "build": "study", "time": "1h", "level": "beginner", "safety": "fire safety", "notes": "carry: sealed"},
  {"kind": "gm", "t": "Paracord Bracelet", "tier": "Foundations", "concept": "cordage emergency", "mechanism": "9ft wearable", "parts": ["bracelet"], "build": "weave", "time": "2h", "level": "beginner", "safety": "none", "notes": "carry: wrist"},
  {"kind": "gm", "t": "Handkerchief", "tier": "Foundations", "concept": "tissues fail", "mechanism": "cloth hanky", "parts": ["cloth"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "carry: back pocket classic"},
  {"kind": "gm", "t": "Lip Balm + Lotion", "tier": "Foundations", "concept": "dry discomfort", "mechanism": "tiny tins", "parts": ["tins"], "build": "pack", "time": "1h", "level": "beginner", "safety": "none", "notes": "carry: jacket pocket"},
  {"kind": "gm", "t": "Tactical Pen", "tier": "Compounded", "concept": "pen + glass breaker", "mechanism": "machined pen", "parts": ["pen"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "carry: know the law"},
  {"kind": "gm", "t": "Pocket Pry Bar", "tier": "Compounded", "concept": "packages + nails", "mechanism": "titanium mini bar", "parts": ["bar"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "carry: keychain"},
  {"kind": "gm", "t": "EDC Pouch (Organizer)", "tier": "Compounded", "concept": "pocket chaos", "mechanism": "pouch with slots", "parts": ["pouch"], "build": "sew", "time": "4h", "level": "intermediate", "safety": "none", "notes": "carry: bag-in-bag"},
  {"kind": "gm", "t": "Notebook (Pocket)", "tier": "Compounded", "concept": "ideas flee", "mechanism": "48pg + pen loop", "parts": ["book"], "build": "bind", "time": "2h", "level": "intermediate", "safety": "none", "notes": "carry: back pocket"},
  {"kind": "gm", "t": "Multi-Bit Driver", "tier": "Compounded", "concept": "screws loosen", "mechanism": "pen-size + bits", "parts": ["driver"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "carry: shirt pocket"},
  {"kind": "gm", "t": "Pocket Saw", "tier": "Compounded", "concept": "wood needs cutting", "mechanism": "folding saw", "parts": ["folding saw"], "build": "saw", "time": "1h", "level": "intermediate", "safety": "blade sharp", "notes": "carry: sheath"},
  {"kind": "gm", "t": "Whistle (Safety)", "tier": "Compounded", "concept": "need attention", "mechanism": "120db pea-less", "parts": ["whistle"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "carry: neck or pack"},
  {"kind": "gm", "t": "Fire Kit (Pocket)", "tier": "Compounded", "concept": "fire emergency", "mechanism": "ferro rod + tinder", "parts": ["kit"], "build": "pack", "time": "2h", "level": "intermediate", "safety": "fire safety", "notes": "carry: waterproof tin"},
  {"kind": "gm", "t": "Belt First-Aid Kit", "tier": "Compounded", "concept": "bleeds happen", "mechanism": "bandaids + gauze mini", "parts": ["kit"], "build": "pack", "time": "1h", "level": "intermediate", "safety": "none", "notes": "carry: everywhere"},
  {"kind": "gm", "t": "Water Filter (Straw)", "tier": "Compounded", "concept": "water doubts", "mechanism": "filter straw", "parts": ["filter"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "carry: hiking essential"},
  {"kind": "gm", "t": "Belt Headlamp", "tier": "Compounded", "concept": "hands need free", "mechanism": "300lm headlamp", "parts": ["lamp"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "carry: pack lid"},
  {"kind": "gm", "t": "Utility Belt (Full)", "tier": "Advanced", "concept": "carry system", "mechanism": "belt + pouches modular", "parts": ["belt"], "build": "build", "time": "10h", "level": "advanced", "safety": "none", "notes": "carry: trade-tested layout"},
  {"kind": "gm", "t": "Chest Rig (EDC)", "tier": "Advanced", "concept": "belt full", "mechanism": "chest pouches", "parts": ["rig"], "build": "sew", "time": "12h", "level": "advanced", "safety": "none", "notes": "carry: photographers love"},
  {"kind": "gm", "t": "Go-Bag (72h)", "tier": "Advanced", "concept": "disaster ready", "mechanism": "72h essentials packed", "parts": ["bag"], "build": "pack", "time": "8h", "level": "advanced", "safety": "none", "notes": "carry: rotate food/water"},
  {"kind": "gm", "t": "Everyday Backpack", "tier": "Advanced", "concept": "daily carry", "mechanism": "laptop + tools + gym", "parts": ["pack"], "build": "plan", "time": "6h", "level": "advanced", "safety": "none", "notes": "carry: one bag rule"},
  {"kind": "gm", "t": "Tech Pouch", "tier": "Advanced", "concept": "cables chaos", "mechanism": "cables + adapters + bank", "parts": ["pouch"], "build": "pack", "time": "4h", "level": "advanced", "safety": "battery safety", "notes": "carry: grab and go"},
  {"kind": "gm", "t": "Medical (IFAK)", "tier": "Advanced", "concept": "trauma ready", "mechanism": "tourniquet + chest seal", "parts": ["kit"], "build": "pack", "time": "4h", "level": "advanced", "safety": "training first", "notes": "carry: training beats gear"},
  {"kind": "gm", "t": "Tool Roll", "tier": "Advanced", "concept": "tools organized", "mechanism": "canvas roll + tools", "parts": ["roll"], "build": "sew", "time": "8h", "level": "advanced", "safety": "tools sharp", "notes": "carry: workshop to field"},
  {"kind": "gm", "t": "Fishing Kit (Pocket)", "tier": "Advanced", "concept": "fish anywhere", "mechanism": "line + hooks + lures", "parts": ["kit"], "build": "pack", "time": "3h", "level": "advanced", "safety": "hooks sharp", "notes": "carry: altoids tin"},
  {"kind": "gm", "t": "Foraging Kit", "tier": "Advanced", "concept": "wild food", "mechanism": "bags + knife + guide", "parts": ["kit"], "build": "pack", "time": "4h", "level": "advanced", "safety": "expert ID only", "notes": "carry: never eat unsure"},
  {"kind": "gm", "t": "Repair Kit (Universal)", "tier": "Advanced", "concept": "things break", "mechanism": "tape + glue + bits", "parts": ["kit"], "build": "pack", "time": "4h", "level": "advanced", "safety": "none", "notes": "carry: fix most things"},
  {"kind": "gm", "t": "Survival Tin", "tier": "Advanced", "concept": "worst case", "mechanism": "fire + shelter + signal", "parts": ["tin"], "build": "pack", "time": "4h", "level": "advanced", "safety": "skills first", "notes": "carry: knowledge weighs nothing"},
  {"kind": "gm", "t": "Photographer's Belt", "tier": "Advanced", "concept": "gear at hand", "mechanism": "lens + body pouches", "parts": ["belt"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "carry: weight on hips"}
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

