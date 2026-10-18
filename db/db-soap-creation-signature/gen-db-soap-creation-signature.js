(function(){'use strict';
/* JAH The Soap Creation Database — real working generator, jahdb-db-soap-creation-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SOAPS-";
var SLUG="db-soap-creation";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry.", "FDA cosmetic rules: label ingredients honestly; lye soap must cure fully before sale or use."];
var CITATIONS=["Cavitch, Susan Miller. 'The Soapmaker\\'s Companion.' Storey Publishing, 1997."];
var BANK=[
  {"kind": "diy", "t": "Melt-and-Pour First Bars", "tier": "Foundations", "notes": "no lye in melt-and-pour", "mats": [["base 2lb", "1", 14.0], ["molds", "1", 10.0], ["fragrance", "1", 8.0], ["color", "1", 6.0]], "tools": ["microwave"], "steps": ["cut base", "melt gently", "scent/color", "pour"], "time": "2h", "level": "beginner", "safety": "hot soap burns — handle with care"},
  {"kind": "diy", "t": "Soap Safety Fundamentals", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["gloves", "1", 8.0], ["goggles", "1", 10.0], ["vinegar", "1", 3.0]], "tools": ["none"], "steps": ["PPE always", "lye to water", "ventilate", "pets/kids away"], "time": "1h", "level": "beginner", "safety": "LYE SAFETY: lye + water (never reverse), goggles+gloves, vinegar for splashes, ventilate"},
  {"kind": "diy", "t": "Simple Castile (Olive)", "tier": "Foundations", "notes": "cure full 4-6 weeks for mildness", "mats": [["olive oil", "1", 15.0], ["lye", "1", 8.0], ["water", "1", 0.0], ["mold", "1", 12.0]], "tools": ["stick blender"], "steps": ["lye water (cool)", "oils", "blend to trace", "pour, cure 4-6 weeks"], "time": "3h + cure", "level": "beginner", "safety": "full lye safety"},
  {"kind": "diy", "t": "Goat Milk Soap", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 14.0], ["goat milk", "1", 8.0], ["molds", "1", 10.0]], "tools": ["microwave"], "steps": ["melt base", "warm milk", "scent", "pour"], "time": "2h", "level": "beginner", "safety": "hot soap safety"},
  {"kind": "diy", "t": "Exfoliating Oatmeal Bar", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 14.0], ["oatmeal", "1", 4.0], ["molds", "1", 10.0], ["honey", "1", 5.0]], "tools": ["microwave"], "steps": ["melt", "oatmeal in", "pour", "wrap"], "time": "2h", "level": "beginner", "safety": "label ingredients (allergies)"},
  {"kind": "diy", "t": "Shampoo Bar (M&P)", "tier": "Foundations", "notes": "transition period", "mats": [["base", "1", 14.0], ["oils", "1", 8.0], ["molds", "1", 10.0]], "tools": ["microwave"], "steps": ["melt", "add oils", "pour", "test"], "time": "2h", "level": "beginner", "safety": "pH note — M&P is alkaline"},
  {"kind": "diy", "t": "Glycerin Clear Soap", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["clear base", "1", 16.0], ["molds", "1", 10.0], ["color", "1", 6.0]], "tools": ["microwave"], "steps": ["melt low", "suds minimal", "pour", "cool"], "time": "2h", "level": "beginner", "safety": "don't boil — bubbles cloud"},
  {"kind": "diy", "t": "Coffee Scrub Bar", "tier": "Foundations", "notes": "grounds exfoliate strongly", "mats": [["base", "1", 14.0], ["coffee", "1", 4.0], ["molds", "1", 10.0]], "tools": ["microwave"], "steps": ["melt", "grounds in", "pour", "wrap"], "time": "2h", "level": "beginner", "safety": "label"},
  {"kind": "diy", "t": "Kids Soap Shapes", "tier": "Foundations", "notes": "kid-safe scents", "mats": [["base", "1", 14.0], ["molds fun", "1", 12.0], ["colors", "1", 8.0]], "tools": ["microwave"], "steps": ["melt", "color swirls", "pour", "pop out"], "time": "2h", "level": "beginner", "safety": "adult handles hot soap"},
  {"kind": "diy", "t": "Shaving Soap Puck", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 14.0], ["clay", "1", 5.0], ["tins", "1", 8.0], ["scent", "1", 8.0]], "tools": ["microwave"], "steps": ["melt", "clay in", "pour tins", "cure"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Laundry Stain Stick", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 12.0], ["washing soda", "1", 5.0], ["mold", "1", 8.0]], "tools": ["microwave"], "steps": ["melt", "add soda", "pour stick", "label"], "time": "2h", "level": "beginner", "safety": "label NOT for skin"},
  {"kind": "diy", "t": "Loofah Soap Slices", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 14.0], ["loofah", "1", 6.0], ["molds", "1", 8.0]], "tools": ["microwave"], "steps": ["slice loofah", "melt", "pour over", "cool"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cold Process: Basic Recipe", "tier": "Compounded", "notes": "stick blender splashes — goggles", "mats": [["oils", "1", 25.0], ["lye", "1", 10.0], ["mold", "1", 15.0], ["stick blender", "1", 30.0]], "tools": ["blender"], "steps": ["lye water", "oils 100F", "blend trace", "pour, cure 4-6w"], "time": "4h + cure", "level": "intermediate", "safety": "FULL LYE PROTOCOL"},
  {"kind": "diy", "t": "Swirl Techniques", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["batch", "1", 20.0], ["colors", "1", 12.0]], "tools": ["none"], "steps": ["trace light", "divide colors", "swirl pour", "hanger swirl"], "time": "5h", "level": "intermediate", "safety": "work fast — trace waits for no one"},
  {"kind": "diy", "t": "Layered Soap", "tier": "Compounded", "notes": "layers bond warm", "mats": [["batch", "1", 20.0]], "tools": ["none"], "steps": ["pour layer", "spray alcohol", "cool firm", "repeat"], "time": "5h", "level": "intermediate", "safety": "alcohol spray prevents ash"},
  {"kind": "diy", "t": "Soap Stamping", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["bars", "1", 0.0], ["stamp", "1", 15.0]], "tools": ["mallet"], "steps": ["cure 2 weeks", "stamp firm", "mallet tap", "bevel"], "time": "1h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Hot Process Method", "tier": "Compounded", "notes": "lye safety", "mats": [["oils", "1", 25.0], ["lye", "1", 10.0], ["crockpot", "1", 30.0]], "tools": ["crockpot"], "steps": ["lye water", "oils in pot", "cook to gel", "mold"], "time": "5h", "level": "intermediate", "safety": "crockpot volcano — stir"},
  {"kind": "diy", "t": "Salt Bars", "tier": "Compounded", "notes": "cure 8+ weeks", "mats": [["oils", "1", 20.0], ["salt", "1", 6.0], ["mold", "1", 15.0]], "tools": ["none"], "steps": ["trace", "salt 80%", "pour fast", "cure long"], "time": "4h", "level": "intermediate", "safety": "salt accelerates — work fast"},
  {"kind": "diy", "t": "Beer Soap", "tier": "Compounded", "notes": "lye safety", "mats": [["beer", "1", 5.0], ["oils", "1", 22.0], ["mold", "1", 15.0]], "tools": ["none"], "steps": ["boil off alcohol", "cool", "lye in beer", "trace, pour"], "time": "4h", "level": "intermediate", "safety": "boil beer flat first"},
  {"kind": "diy", "t": "Clay Facial Bars", "tier": "Compounded", "notes": "patch test", "mats": [["oils", "1", 22.0], ["clay", "1", 8.0], ["mold", "1", 15.0]], "tools": ["none"], "steps": ["trace", "clay slurry", "scent", "pour"], "time": "4h", "level": "intermediate", "safety": "label for face"},
  {"kind": "diy", "t": "Shampoo Bars (CP)", "tier": "Compounded", "notes": "transition tips card", "mats": [["oils", "1", 25.0], ["lye", "1", 10.0], ["mold", "1", 15.0]], "tools": ["blender"], "steps": ["formulate", "trace", "pour", "cure 6w"], "time": "4h + cure", "level": "intermediate", "safety": "pH 9-10 normal for soap"},
  {"kind": "diy", "t": "Dish Soap Bars", "tier": "Compounded", "notes": "gloves to use", "mats": [["coconut oil", "1", 15.0], ["lye", "1", 8.0], ["mold", "1", 12.0]], "tools": ["blender"], "steps": ["100% coconut", "0% superfat", "trace", "pour"], "time": "3h", "level": "intermediate", "safety": "0 superfat = cleaning"},
  {"kind": "diy", "t": "Lye Calculator Mastery", "tier": "Compounded", "notes": "always run recipes through calculator", "mats": [["scale", "1", 20.0]], "tools": ["none"], "steps": ["weigh precisely", "superfat 5%", "water 33%", "record"], "time": "2h", "level": "intermediate", "safety": "scale accuracy = safety"},
  {"kind": "diy", "t": "Confetti Soap", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["scraps", "1", 0.0], ["base", "1", 10.0], ["molds", "1", 8.0]], "tools": ["microwave"], "steps": ["chop scraps", "melt base", "stir in", "pour"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Charcoal Detox Bar", "tier": "Compounded", "notes": "charcoal stains washcloths", "mats": [["base", "1", 14.0], ["charcoal", "1", 6.0], ["molds", "1", 10.0], ["tea tree", "1", 7.0]], "tools": ["microwave"], "steps": ["melt", "charcoal in", "pour", "wrap"], "time": "2h", "level": "intermediate", "safety": "label"},
  {"kind": "diy", "t": "Rose Clay Bars", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 14.0], ["rose clay", "1", 8.0], ["molds", "1", 10.0], ["scent", "1", 8.0]], "tools": ["microwave"], "steps": ["melt", "clay slurry", "pour", "wrap"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Milk Soaps (CP)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["milks", "1", 15.0], ["oils", "1", 25.0], ["lye", "1", 10.0]], "tools": ["blender"], "steps": ["freeze milk", "lye into slush", "keep cool", "pour"], "time": "5h", "level": "advanced", "safety": "milk scorches — ice bath method"},
  {"kind": "diy", "t": "Intricate Multi-Swirl", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["batch", "1", 30.0], ["colors", "1", 18.0]], "tools": ["none"], "steps": ["plan design", "thin trace", "multi-pour", "cut reveal"], "time": "6h", "level": "advanced", "safety": "design on paper first"},
  {"kind": "diy", "t": "Soap Business Batch (100)", "tier": "Advanced", "notes": "cosmetic regs; batch records", "mats": [["supplies", "1", 200.0], ["labels", "1", 40.0], ["scale", "1", 0.0]], "tools": ["blender"], "steps": ["scale recipe", "production line", "cure racks", "label"], "time": "20h", "level": "advanced", "safety": "insurance"},
  {"kind": "diy", "t": "Shave Soap Formula", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["oils", "1", 30.0], ["lye duo", "1", 12.0], ["tins", "1", 15.0]], "tools": ["blender"], "steps": ["dual-lye", "cook", "superfat", "tin"], "time": "6h", "level": "advanced", "safety": "dual-lye math — calculator essential"},
  {"kind": "diy", "t": "Transparent CP Soap", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["oils", "1", 30.0], ["solvents", "1", 20.0], ["mold", "1", 15.0]], "tools": ["none"], "steps": ["cook", "dissolve test", "solvents", "pour"], "time": "8h", "level": "advanced", "safety": "solvents flammable — no open flame"},
  {"kind": "diy", "t": "Salt Spa Bars Luxury", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["oils", "1", 30.0], ["salts", "1", 15.0], ["mold", "1", 20.0]], "tools": ["none"], "steps": ["formulate", "cure 3 months", "package", "label"], "time": "6h + cure", "level": "advanced", "safety": "long cure = luxury mildness"},
  {"kind": "diy", "t": "Custom Fragrance Blend", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["oils", "1", 40.0], ["batch", "1", 25.0]], "tools": ["none"], "steps": ["test blends", "anchor notes", "batch", "cure test"], "time": "10h", "level": "advanced", "safety": "fragrance discoloration — vanilla browns"},
  {"kind": "diy", "t": "Teaching Soap Workshop", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kits", "1", 150.0]], "tools": ["none"], "steps": ["demo M&P only", "safety talk", "make", "take home"], "time": "8h", "level": "advanced", "safety": "demo lye, let students do M&P — liability"}
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

