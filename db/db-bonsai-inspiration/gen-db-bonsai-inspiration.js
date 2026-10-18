(function(){'use strict';
/* JAH The Bonsai Inspiration Database — real working generator, jahdb-db-bonsai-inspiration-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BI-";
var SLUG="db-bonsai-inspiration";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Chan, Peter. 'Bonsai Masterclass.' Sterling, 2007."];
var BANK=[
  {"kind": "diy", "t": "What Is Bonsai", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["book", "1", 20.0]], "tools": ["none"], "steps": ["history", "styles", "species", "begin"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "First Tree: Juniper", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["juniper", "1", 25.0], ["pot", "1", 15.0], ["soil", "1", 10.0], ["tools", "1", 20.0]], "tools": ["tools"], "steps": ["select tree", "slip pot", "water", "outdoor"], "time": "3h", "level": "beginner", "safety": "junipers live outdoors — indoors kills them"},
  {"kind": "diy", "t": "Watering Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["watering can", "1", 12.0]], "tools": ["none"], "steps": ["check daily", "water thoroughly", "drain", "observe"], "time": "1h", "level": "beginner", "safety": "number one killer: overwatering AND underwatering"},
  {"kind": "diy", "t": "Ficus (Indoor Starter)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["ficus", "1", 30.0], ["pot", "1", 15.0], ["soil", "1", 10.0]], "tools": ["none"], "steps": ["bright window", "water", "prune", "enjoy"], "time": "2h", "level": "beginner", "safety": "best true indoor bonsai"},
  {"kind": "diy", "t": "Pruning First Steps", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["concave cutter", "1", 25.0]], "tools": ["cutter"], "steps": ["pinch new growth", "cut to shape", "seal large", "aftercare"], "time": "2h", "level": "beginner", "safety": "clean tools between trees"},
  {"kind": "diy", "t": "Repotting Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["soil", "1", 12.0], ["pot", "1", 15.0], ["mesh", "1", 3.0], ["wire", "1", 5.0]], "tools": ["tools"], "steps": ["every 2-3 years", "root prune 1/3", "wire in", "water"], "time": "3h", "level": "beginner", "safety": "repot in spring before buds"},
  {"kind": "diy", "t": "Fertilizing Schedule", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["fertilizer", "1", 12.0]], "tools": ["none"], "steps": ["growing season feed", "organic cakes", "reduce fall", "none winter"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Choosing Your First Pot", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["pot", "1", 20.0]], "tools": ["none"], "steps": ["size: 2/3 height", "drainage holes", "color harmony", "feet"], "time": "1h", "level": "beginner", "safety": "drainage holes mandatory"},
  {"kind": "diy", "t": "Jade (Succulent Bonsai)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["jade", "1", 20.0], ["pot", "1", 12.0], ["gritty soil", "1", 8.0]], "tools": ["none"], "steps": ["bright light", "sparse water", "prune", "shape"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Moss and Top Dressing", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["moss", "1", 8.0], ["gravel", "1", 5.0]], "tools": ["tweezers"], "steps": ["soil level", "moss patches", "gravel", "mist"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Winter Care Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["mulch", "1", 8.0]], "tools": ["none"], "steps": ["hardy: mulch in", "tender: indoors", "water winter", "protect wind"], "time": "2h", "level": "beginner", "safety": "roots freeze before tops — protect pots"},
  {"kind": "diy", "t": "Bonsai Soil Mixing", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["akadama", "1", 18.0], ["pumice", "1", 12.0], ["lava", "1", 12.0], ["sieve", "1", 15.0]], "tools": ["sieve"], "steps": ["sieve fines", "mix 1:1:1", "store dry", "use"], "time": "2h", "level": "beginner", "safety": "dust mask when sieving dry components"},
  {"kind": "diy", "t": "Wiring Techniques", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wire set", "1", 18.0], ["cutters", "1", 12.0]], "tools": ["cutters"], "steps": ["wrap 45 degrees", "bend gently", "check monthly", "remove timely"], "time": "6h", "level": "intermediate", "safety": "wire scars — remove before biting in"},
  {"kind": "diy", "t": "Chinese Elm Styling", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["elm", "1", 40.0], ["tools", "1", 0.0]], "tools": ["tools"], "steps": ["broom style", "clip-and-grow", "ramify", "refine"], "time": "10h", "level": "intermediate", "safety": "great beginner-intermediate tree"},
  {"kind": "diy", "t": "Trunk Chop & Taper", "tier": "Compounded", "notes": "patience years", "mats": [["tree", "1", 35.0], ["saw", "1", 15.0], ["sealant", "1", 8.0]], "tools": ["saw"], "steps": ["chop at taper point", "seal", "grow leader", "repeat"], "time": "8h", "level": "intermediate", "safety": "sealant on large cuts"},
  {"kind": "diy", "t": "Root Over Rock", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tree", "1", 30.0], ["rock", "1", 12.0], ["soil", "1", 10.0], ["wrap", "1", 5.0]], "tools": ["none"], "steps": ["roots over rock", "tie", "bury 2 years", "expose"], "time": "6h + years", "level": "intermediate", "safety": "long project — commit"},
  {"kind": "diy", "t": "Forest Planting", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["trees", "7", 70.0], ["pot", "1", 35.0], ["soil", "1", 15.0]], "tools": ["tools"], "steps": ["odd numbers", "heights vary", "plant", "aftercare"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Deadwood (Jin/Shari)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tree", "1", 50.0], ["jin pliers", "1", 20.0], ["lime sulfur", "1", 12.0]], "tools": ["pliers"], "steps": ["strip bark", "carve", "lime sulfur", "preserve"], "time": "8h", "level": "intermediate", "safety": "lime sulfur — gloves, ventilation"},
  {"kind": "diy", "t": "Air Layering", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tree", "1", 0.0], ["sphagnum", "1", 8.0], ["plastic", "1", 4.0], ["knife", "1", 10.0]], "tools": ["knife"], "steps": ["ring bark", "moss wrap", "wait roots", "separate"], "time": "4h + months", "level": "intermediate", "safety": "knife safety"},
  {"kind": "diy", "t": "Pine Candle Pruning", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["pine", "1", 60.0], ["tools", "1", 0.0]], "tools": ["tools"], "steps": ["candle cut spring", "needle pull fall", "balance energy", "refine"], "time": "8h", "level": "intermediate", "safety": "timing is species-specific"},
  {"kind": "diy", "t": "Deciduous Ramification", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["maple", "1", 45.0], ["tools", "1", 0.0]], "tools": ["tools"], "steps": ["grow and cut", "wound seal", "branch pairs", "winter silhouette"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Grafting Branches", "tier": "Compounded", "notes": "clean cuts", "mats": [["tree", "1", 40.0], ["scions", "1", 0.0], ["tape", "1", 6.0], ["knife", "1", 12.0]], "tools": ["knife"], "steps": ["approach graft", "secure", "wait fuse", "separate"], "time": "6h", "level": "intermediate", "safety": "knife safety"},
  {"kind": "diy", "t": "Display (Tokonoma Style)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["stand", "1", 25.0], ["scroll", "1", 20.0]], "tools": ["none"], "steps": ["tree", "accent", "scroll", "view"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Elm Broom Restyle", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["elm", "1", 45.0], ["tools", "1", 0.0]], "tools": ["tools"], "steps": ["assess", "structural prune", "wire", "aftercare"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Literati Style", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["pine", "1", 80.0], ["pot", "1", 30.0]], "tools": ["tools"], "steps": ["tall thin trunk", "minimal branches", "pot small", "age"], "time": "20h", "level": "advanced", "safety": "hardest style — restraint"},
  {"kind": "diy", "t": "Cascade (Kengai)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["juniper", "1", 70.0], ["tall pot", "1", 40.0], ["wire", "1", 15.0]], "tools": ["tools"], "steps": ["trunk down", "wire cascade", "balance", "pot"], "time": "16h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": " collected Yamadori", "tier": "Advanced", "notes": "survival first, styling later", "mats": [["permit", "1", 0.0], ["tools", "1", 30.0], ["aftercare", "1", 20.0]], "tools": ["saw"], "steps": ["legal collect", "root care", "recover years", "style"], "time": "20h + years", "level": "advanced", "safety": "permits required"},
  {"kind": "diy", "t": "Shohin (Mini) Collection", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["trees", "5", 150.0], ["pots", "1", 75.0]], "tools": ["tools"], "steps": ["small scale", "daily water", "refine", "display"], "time": "30h", "level": "advanced", "safety": "shohin dry fast — water twice daily summer"},
  {"kind": "diy", "t": "Bonsai from Seed", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["seeds", "1", 10.0], ["pots", "1", 20.0], ["soil", "1", 15.0]], "tools": ["none"], "steps": ["stratify", "sow", "grow 5+ years", "style"], "time": "10h + years", "level": "advanced", "safety": "decade project — the long game"},
  {"kind": "diy", "t": "Grafting Roots (Nebari)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tree", "1", 60.0], ["seedlings", "1", 20.0], ["tools", "1", 15.0]], "tools": ["knife"], "steps": ["drill/approach", "seedling roots", "fuse", "develop"], "time": "12h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Exhibition Preparation", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tree", "1", 0.0], ["pot", "1", 50.0], ["stand", "1", 40.0]], "tools": ["tools"], "steps": ["select", "repot timing", "detail moss", "transport"], "time": "20h", "level": "advanced", "safety": "transport safely — the risky part"},
  {"kind": "diy", "t": "Ancient Olive Styling", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["olive", "1", 120.0], ["tools", "1", 20.0]], "tools": ["tools"], "steps": ["deadwood", "hollow carve", "style", "aftercare"], "time": "30h", "level": "advanced", "safety": "power carving — eye protection, dust mask"},
  {"kind": "diy", "t": "Bonsai Garden Design", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["space", "1", 0.0], ["benches", "1", 150.0], ["trees", "1", 300.0]], "tools": ["saw"], "steps": ["benches", "display", "water", "maintain"], "time": "40h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Teaching Bonsai Workshop", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 100.0]], "tools": ["none"], "steps": ["curriculum", "trees", "tools", "teach"], "time": "16h", "level": "advanced", "safety": "none"}
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

