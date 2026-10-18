(function(){'use strict';
/* JAH The Repairability Design Database — real working generator, jahdb-db-repairability-design-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RDS-";
var SLUG="db-repairability-design";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Screwdrivers (Right)", "tier": "Foundations", "concept": "strip screws", "mechanism": "JIS + Phillips + Torx", "parts": ["drivers"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "repair: right bit, no strip"},
  {"kind": "gm", "t": "Spudgers + Picks", "tier": "Foundations", "concept": "open without break", "mechanism": "nylon tools", "parts": ["tools"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "repair: plastic before metal"},
  {"kind": "gm", "t": "Heat Gun (Basic)", "tier": "Foundations", "concept": "adhesive holds", "mechanism": "heat softens", "parts": ["gun"], "build": "learn", "time": "2h", "level": "beginner", "safety": "burn", "notes": "repair: 80C softens most"},
  {"kind": "gm", "t": "Multimeter Basics", "tier": "Foundations", "concept": "find faults", "mechanism": "continuity + volts", "parts": ["meter"], "build": "learn", "time": "3h", "level": "beginner", "safety": "electrical", "notes": "repair: beep = connected"},
  {"kind": "gm", "t": "Soldering (Through-Hole)", "tier": "Foundations", "concept": "joints fail", "mechanism": "iron + solder", "parts": ["iron"], "build": "learn", "time": "6h", "level": "beginner", "safety": "fume/burn", "notes": "repair: heat the joint"},
  {"kind": "gm", "t": "Glue Guide", "tier": "Foundations", "concept": "what sticks?", "mechanism": "chart + test", "parts": ["guide"], "build": "study", "time": "2h", "level": "beginner", "safety": "fumes", "notes": "repair: surface prep 90%"},
  {"kind": "gm", "t": "Clamps + Vise", "tier": "Foundations", "concept": "hold work", "mechanism": "assorted", "parts": ["clamps"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "repair: clamp, don't hold"},
  {"kind": "gm", "t": "Magnifier Lamp", "tier": "Foundations", "concept": "see small", "mechanism": "3x + light", "parts": ["lamp"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "repair: light + magnify"},
  {"kind": "gm", "t": "Parts Trays", "tier": "Foundations", "concept": "screws vanish", "mechanism": "magnetic mats", "parts": ["trays"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "repair: photo disassembly"},
  {"kind": "gm", "t": "iFixit Mindset", "tier": "Foundations", "concept": "fear of opening", "mechanism": "guides + confidence", "parts": ["mindset"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "repair: repairable by design"},
  {"kind": "gm", "t": "Battery Safety", "tier": "Foundations", "concept": "swollen danger", "mechanism": "recognize + handle", "parts": ["knowledge"], "build": "learn", "time": "2h", "level": "beginner", "safety": "puncture risk", "notes": "repair: swollen = pro only"},
  {"kind": "gm", "t": "Phone Screen Swap", "tier": "Compounded", "concept": "cracked screen", "mechanism": "kit + guide", "parts": ["kit"], "build": "repair", "time": "3h", "level": "intermediate", "safety": "battery safety", "notes": "repair: heat + patience"},
  {"kind": "gm", "t": "Laptop Battery", "tier": "Compounded", "concept": "dies fast", "mechanism": "OEM + guide", "parts": ["battery"], "build": "replace", "time": "2h", "level": "intermediate", "safety": "battery", "notes": "repair: calibrate 3 cycles"},
  {"kind": "gm", "t": "Headphone Cable", "tier": "Compounded", "concept": "one side out", "mechanism": "solder new cable", "parts": ["cable"], "build": "solder", "time": "3h", "level": "intermediate", "safety": "soldering", "notes": "repair: strain relief"},
  {"kind": "gm", "t": "Game Controller Drift", "tier": "Compounded", "concept": "stick drifts", "mechanism": "clean/replace stick", "parts": ["stick"], "build": "repair", "time": "2h", "level": "intermediate", "safety": "tiny screws", "notes": "repair: contact cleaner first"},
  {"kind": "gm", "t": "Vacuum Belt/Brush", "tier": "Compounded", "concept": "no suction", "mechanism": "belt + clean", "parts": ["parts"], "build": "repair", "time": "2h", "level": "intermediate", "safety": "unplug", "notes": "repair: check blockages"},
  {"kind": "gm", "t": "Lamp Rewire", "tier": "Compounded", "concept": "dead lamp", "mechanism": "cord + socket", "parts": ["parts"], "build": "rewire", "time": "3h", "level": "intermediate", "safety": "electrical", "notes": "repair: polarized plug"},
  {"kind": "gm", "t": "Chair Reglue", "tier": "Compounded", "concept": "wobbly", "mechanism": "glue + clamps", "parts": ["glue"], "build": "repair", "time": "4h", "level": "intermediate", "safety": "none", "notes": "repair: disassemble fully first"},
  {"kind": "gm", "t": "Zipper Replace", "tier": "Compounded", "concept": "zipper dies", "mechanism": "new zip + sew", "parts": ["zip"], "build": "sew", "time": "3h", "level": "intermediate", "safety": "none", "notes": "repair: measure teeth"},
  {"kind": "gm", "t": "Shoe Resole", "tier": "Compounded", "concept": "soles worn", "mechanism": "cobbler or DIY", "parts": ["sole"], "build": "repair", "time": "6h", "level": "intermediate", "safety": "cement fumes", "notes": "repair: cobbler often worth it"},
  {"kind": "gm", "t": "Appliance Cord", "tier": "Compounded", "concept": "frayed danger", "mechanism": "new cord + strain", "parts": ["cord"], "build": "replace", "time": "2h", "level": "intermediate", "safety": "electrical", "notes": "repair: unplug, obviously"},
  {"kind": "gm", "t": "Faucet Cartridge", "tier": "Compounded", "concept": "drips", "mechanism": "cartridge + tools", "parts": ["cartridge"], "build": "replace", "time": "2h", "level": "intermediate", "safety": "water off", "notes": "repair: bring old to store"},
  {"kind": "gm", "t": "Toaster Repair", "tier": "Compounded", "concept": "heat again", "mechanism": "element + clean", "parts": ["toaster"], "build": "repair", "time": "3h", "level": "intermediate", "safety": "electrical", "notes": "repair: unplug, obviously"},
  {"kind": "gm", "t": "Right-to-Repair Law", "tier": "Advanced", "concept": "rights?", "mechanism": "know your rights", "parts": ["knowledge"], "build": "study", "time": "4h", "level": "advanced", "safety": "none", "notes": "repair: advocate"},
  {"kind": "gm", "t": "Schematics Reading", "tier": "Advanced", "concept": "board repair", "mechanism": "read + probe", "parts": ["skill"], "build": "learn", "time": "20h", "level": "advanced", "safety": "electrical", "notes": "repair: signal path first"},
  {"kind": "gm", "t": "Microsoldering", "tier": "Advanced", "concept": "tiny joints", "mechanism": "microscope + iron", "parts": ["skill"], "build": "learn", "time": "40h", "level": "advanced", "safety": "fumes", "notes": "repair: practice boards"},
  {"kind": "gm", "t": "BGA Rework", "tier": "Advanced", "concept": "chip-level", "mechanism": "hot air + stencil", "parts": ["skill"], "build": "learn", "time": "60h", "level": "advanced", "safety": "fumes", "notes": "repair: pro equipment"},
  {"kind": "gm", "t": "Motor Rewind", "tier": "Advanced", "concept": "dead motor", "mechanism": "rewind coils", "parts": ["motor"], "build": "rewind", "time": "20h", "level": "advanced", "safety": "electrical", "notes": "repair: count turns"},
  {"kind": "gm", "t": "Furniture Restoration", "tier": "Advanced", "concept": "heirloom", "mechanism": "strip + repair + finish", "parts": ["piece"], "build": "restore", "time": "40h", "level": "advanced", "safety": "lead test", "notes": "repair: test lead first"},
  {"kind": "gm", "t": "Clock Repair", "tier": "Advanced", "concept": "ticking stops", "mechanism": "clean + oil", "parts": ["clock"], "build": "repair", "time": "20h", "level": "advanced", "safety": "mainspring", "notes": "repair: let down power first"},
  {"kind": "gm", "t": "Sewing Machine Service", "tier": "Advanced", "concept": "tension woes", "mechanism": "clean + time", "parts": ["machine"], "build": "service", "time": "10h", "level": "advanced", "safety": "none", "notes": "repair: manual first"},
  {"kind": "gm", "t": "Small Engine Rebuild", "tier": "Advanced", "concept": "won't start", "mechanism": "carb + spark", "parts": ["engine"], "build": "rebuild", "time": "16h", "level": "advanced", "safety": "fuel safety", "notes": "repair: fresh fuel first"},
  {"kind": "gm", "t": "Repair Business", "tier": "Advanced", "concept": "fix for pay", "mechanism": "shop + pricing", "parts": ["business"], "build": "open", "time": "100h", "level": "advanced", "safety": "business", "notes": "repair: 80% diagnostics"},
  {"kind": "gm", "t": "Design for Repair", "tier": "Advanced", "concept": "future proof", "mechanism": "modular + docs", "parts": ["design"], "build": "design", "time": "40h", "level": "advanced", "safety": "none", "notes": "repair: screws, not glue"}
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

