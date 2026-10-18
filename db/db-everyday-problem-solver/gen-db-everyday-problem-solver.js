(function(){'use strict';
/* JAH The Everyday Problem Solver Database — real working generator, jahdb-db-everyday-problem-solver-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EPS-";
var SLUG="db-everyday-problem-solver";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Keys Always Lost", "tier": "Foundations", "concept": "find fast", "mechanism": "hook + tile", "parts": ["use"], "build": "install", "time": "2h", "level": "beginner", "safety": "none", "notes": "same spot always"},
  {"kind": "gm", "t": "Cables Tangled", "tier": "Foundations", "concept": "neat tech", "mechanism": "labels + ties", "parts": ["maintain"], "build": "organize", "time": "2h", "level": "beginner", "safety": "none", "notes": "label both ends"},
  {"kind": "gm", "t": "Fridge Chaos", "tier": "Foundations", "concept": "find food", "mechanism": "bins + zones", "parts": ["maintain"], "build": "organize", "time": "3h", "level": "beginner", "safety": "none", "notes": "eat-me-first box"},
  {"kind": "gm", "t": "Morning Rush", "tier": "Foundations", "concept": "smooth AM", "mechanism": "prep night before", "parts": ["follow"], "build": "system", "time": "2h", "level": "beginner", "safety": "none", "notes": "decisions at night"},
  {"kind": "gm", "t": "Laundry Mountain", "tier": "Foundations", "concept": "never done", "mechanism": "daily load habit", "parts": ["do"], "build": "habit", "time": "2h", "level": "beginner", "safety": "none", "notes": "one load daily"},
  {"kind": "gm", "t": "Mail Pile", "tier": "Foundations", "concept": "paper flood", "mechanism": "sort station", "parts": ["process"], "build": "set up", "time": "2h", "level": "beginner", "safety": "none", "notes": "touch once"},
  {"kind": "gm", "t": "Junk Drawer", "tier": "Foundations", "concept": "chaos drawer", "mechanism": "tray + purge", "parts": ["maintain"], "build": "organize", "time": "2h", "level": "beginner", "safety": "none", "notes": "one junk drawer max"},
  {"kind": "gm", "t": "Spice Hunt", "tier": "Foundations", "concept": "find spice", "mechanism": "tier + labels", "parts": ["cook"], "build": "organize", "time": "2h", "level": "beginner", "safety": "none", "notes": "alphabetical wins"},
  {"kind": "gm", "t": "Tupperware Avalanche", "tier": "Foundations", "concept": "lid match", "mechanism": "lids file + purge", "parts": ["maintain"], "build": "organize", "time": "2h", "level": "beginner", "safety": "none", "notes": "match sets only"},
  {"kind": "gm", "t": "Cord Clutter", "tier": "Foundations", "concept": "behind TV", "mechanism": "box + labels", "parts": ["maintain"], "build": "tame", "time": "2h", "level": "beginner", "safety": "vent", "notes": "photo before unplug"},
  {"kind": "gm", "t": "Shoes Everywhere", "tier": "Foundations", "concept": "entry mess", "mechanism": "rack + rule", "parts": ["enforce"], "build": "install", "time": "2h", "level": "beginner", "safety": "none", "notes": "one pair out"},
  {"kind": "gm", "t": "Noisy Neighbors", "tier": "Compounded", "concept": "sleep matters", "mechanism": "seal + mask + talk", "parts": ["sleep"], "build": "fix", "time": "8h", "level": "intermediate", "safety": "none", "notes": "talk kindly first"},
  {"kind": "gm", "t": "Drafty Windows", "tier": "Compounded", "concept": "cold bills", "mechanism": "film + caulk", "parts": ["save"], "build": "seal", "time": "6h", "level": "intermediate", "safety": "none", "notes": "candle test drafts"},
  {"kind": "gm", "t": "Slow WiFi", "tier": "Compounded", "concept": "dead zones", "mechanism": "placement + mesh", "parts": ["speed"], "build": "fix", "time": "6h", "level": "intermediate", "safety": "none", "notes": "router high + central"},
  {"kind": "gm", "t": "Stained Grout", "tier": "Compounded", "concept": "dingy tile", "mechanism": "steam + seal", "parts": ["maintain"], "build": "restore", "time": "6h", "level": "intermediate", "safety": "chemical", "notes": "seal yearly"},
  {"kind": "gm", "t": "Squeaky Door", "tier": "Compounded", "concept": "annoying", "mechanism": "oil hinge pins", "parts": ["silence"], "build": "fix", "time": "1h", "level": "intermediate", "safety": "none", "notes": "remove pin, oil"},
  {"kind": "gm", "t": "Running Toilet", "tier": "Compounded", "concept": "water waste", "mechanism": "flapper + fill", "parts": ["save"], "build": "fix", "time": "2h", "level": "intermediate", "safety": "water off", "notes": "dye test leak"},
  {"kind": "gm", "t": "Clogged Drain", "tier": "Compounded", "concept": "slow water", "mechanism": "plunger + snake", "parts": ["flow"], "build": "clear", "time": "2h", "level": "intermediate", "safety": "chemical", "notes": "baking soda monthly"},
  {"kind": "gm", "t": "Flickering Light", "tier": "Compounded", "concept": "annoying", "mechanism": "bulb + ballast", "parts": ["steady"], "build": "fix", "time": "2h", "level": "intermediate", "safety": "breaker", "notes": "LED upgrade"},
  {"kind": "gm", "t": "Sticky Lock", "tier": "Compounded", "concept": "key struggles", "mechanism": "graphite + clean", "parts": ["smooth"], "build": "fix", "time": "1h", "level": "intermediate", "safety": "none", "notes": "never oil pins"},
  {"kind": "gm", "t": "Cold Floors", "tier": "Compounded", "concept": "chilly feet", "mechanism": "rugs + seal", "parts": ["cozy"], "build": "warm", "time": "4h", "level": "intermediate", "safety": "none", "notes": "pad under rug"},
  {"kind": "gm", "t": "Sun Glare", "tier": "Compounded", "concept": "blind screen", "mechanism": "film + shades", "parts": ["see"], "build": "fix", "time": "4h", "level": "intermediate", "safety": "none", "notes": "north light best"},
  {"kind": "gm", "t": "Smelly Shoes", "tier": "Compounded", "concept": "odor out", "mechanism": "baking soda + sun", "parts": ["fresh"], "build": "fix", "time": "2h", "level": "intermediate", "safety": "none", "notes": "tea bags overnight"},
  {"kind": "gm", "t": "Foggy Mirror", "tier": "Compounded", "concept": "see after shower", "mechanism": "shaving cream trick", "parts": ["clear"], "build": "fix", "time": "1h", "level": "intermediate", "safety": "none", "notes": "buff off"},
  {"kind": "gm", "t": "Static Cling", "tier": "Compounded", "concept": "cling off", "mechanism": "safety pin trick", "parts": ["smooth"], "build": "fix", "time": "1h", "level": "intermediate", "safety": "none", "notes": "pin in hem"},
  {"kind": "gm", "t": "Basement Damp", "tier": "Advanced", "concept": "musty", "mechanism": "seal + dehumidify", "parts": ["dry"], "build": "fix", "time": "20h", "level": "advanced", "safety": "mold pro", "notes": "exterior water first"},
  {"kind": "gm", "t": "Ice Dams", "tier": "Advanced", "concept": "roof leaks", "mechanism": "vent + seal attic", "parts": ["protect"], "build": "fix", "time": "20h", "level": "advanced", "safety": "roof pro", "notes": "insulation + air seal"},
  {"kind": "gm", "t": "Foundation Cracks", "tier": "Advanced", "concept": "worry?", "mechanism": "monitor + pro", "parts": ["fix"], "build": "assess", "time": "12h", "level": "advanced", "safety": "structural pro", "notes": "hairline vs structural"},
  {"kind": "gm", "t": "Lead Paint", "tier": "Advanced", "concept": "old homes", "mechanism": "test + pro", "parts": ["remediate"], "build": "test", "time": "16h", "level": "advanced", "safety": "lead pro", "notes": "EPA RRP rules"},
  {"kind": "gm", "t": "Radon", "tier": "Advanced", "concept": "silent gas", "mechanism": "test + mitigate", "parts": ["fix"], "build": "test", "time": "12h", "level": "advanced", "safety": "pro", "notes": "test every 2yr"},
  {"kind": "gm", "t": "Mold (Hidden)", "tier": "Advanced", "concept": "health", "mechanism": "find + pro", "parts": ["remediate"], "build": "assess", "time": "20h", "level": "advanced", "safety": "mold pro", "notes": "fix moisture first"},
  {"kind": "gm", "t": "Old Wiring", "tier": "Advanced", "concept": "fire risk", "mechanism": "inspect + upgrade", "parts": ["fix"], "build": "assess", "time": "30h", "level": "advanced", "safety": "electrician", "notes": "knob-and-tube pro"},
  {"kind": "gm", "t": "Galvanized Pipes", "tier": "Advanced", "concept": "low pressure", "mechanism": "replace sections", "parts": ["fix"], "build": "assess", "time": "30h", "level": "advanced", "safety": "plumber", "notes": "PEX repipe"},
  {"kind": "gm", "t": "Master Fixer", "tier": "Advanced", "concept": "the life", "mechanism": "skills + tools", "parts": ["teach"], "build": "learn", "time": "100h", "level": "advanced", "safety": "know limits", "notes": "pro for danger"}
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

