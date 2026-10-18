(function(){'use strict';
/* JAH The Home Energy Display Database — real working generator, jahdb-db-home-energy-display-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HED-";
var SLUG="db-home-energy-display";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing.", "Electrical panel work by licensed electricians; clamp meters rated for the service."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Kill-A-Watt Audit", "tier": "Foundations", "concept": "what uses power?", "mechanism": "plug meter measures", "parts": ["meter"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "energy: measure everything 24h"},
  {"kind": "gm", "t": "LED Swap Math", "tier": "Foundations", "concept": "bulbs eat watts", "mechanism": "LED uses 85% less", "parts": ["bulbs"], "build": "swap", "time": "2h", "level": "beginner", "safety": "none", "notes": "energy: payback in months"},
  {"kind": "gm", "t": "Phantom Load Hunt", "tier": "Foundations", "concept": "off isn't off", "mechanism": "meter finds vampires", "parts": ["meter"], "build": "hunt", "time": "3h", "level": "beginner", "safety": "none", "notes": "energy: power strips kill vampires"},
  {"kind": "gm", "t": "Thermostat Setback", "tier": "Foundations", "concept": "heat empty house", "mechanism": "7-degree setback saves", "parts": ["thermostat"], "build": "set", "time": "1h", "level": "beginner", "safety": "none", "notes": "energy: 10% per year"},
  {"kind": "gm", "t": "Water Heater Temp", "tier": "Foundations", "concept": "scalding waste", "mechanism": "120F is enough", "parts": ["heater"], "build": "set", "time": "1h", "level": "beginner", "safety": "scald safety", "notes": "energy: 120F saves + safe"},
  {"kind": "gm", "t": "Fridge Coil Clean", "tier": "Foundations", "concept": "fridge works hard", "mechanism": "vacuum coils", "parts": ["fridge"], "build": "clean", "time": "1h", "level": "beginner", "safety": "unplug first", "notes": "energy: 15% easier"},
  {"kind": "gm", "t": "Window Film", "tier": "Foundations", "concept": "heat escapes", "mechanism": "low-e film kit", "parts": ["film"], "build": "install", "time": "4h", "level": "beginner", "safety": "none", "notes": "energy: renter-friendly"},
  {"kind": "gm", "t": "Door Draft Snakes", "tier": "Foundations", "concept": "drafts chill", "mechanism": "sew draft stoppers", "parts": ["stoppers"], "build": "sew", "time": "2h", "level": "beginner", "safety": "none", "notes": "energy: feel the difference"},
  {"kind": "gm", "t": "Shower Timer", "tier": "Foundations", "concept": "long showers", "mechanism": "5-min timer", "parts": ["timer"], "build": "use", "time": "1h", "level": "beginner", "safety": "none", "notes": "energy: hot water = energy"},
  {"kind": "gm", "t": "Laundry Cold Wash", "tier": "Foundations", "concept": "heat costs", "mechanism": "cold + full loads", "parts": ["habit"], "build": "change", "time": "1h", "level": "beginner", "safety": "none", "notes": "energy: 90% of wash energy is heat"},
  {"kind": "gm", "t": "Dishwasher Full Only", "tier": "Foundations", "concept": "half loads waste", "mechanism": "full + eco mode", "parts": ["habit"], "build": "change", "time": "1h", "level": "beginner", "safety": "none", "notes": "energy: air-dry option"},
  {"kind": "gm", "t": "Smart Thermostat", "tier": "Compounded", "concept": "schedule smart", "mechanism": "learning thermostat", "parts": ["thermostat"], "build": "install", "time": "4h", "level": "intermediate", "safety": "HVAC wiring", "notes": "energy: 8-12% savings"},
  {"kind": "gm", "t": "Home Energy Monitor", "tier": "Compounded", "concept": "see usage live", "mechanism": "clamp meter + app", "parts": ["monitor"], "build": "install", "time": "6h", "level": "intermediate", "safety": "electrical pro", "notes": "energy: what gets measured drops"},
  {"kind": "gm", "t": "Insulation Top-Up", "tier": "Compounded", "concept": "heat rises out", "mechanism": "blow-in attic R-49", "parts": ["insulation"], "build": "install", "time": "12h", "level": "intermediate", "safety": "dust mask", "notes": "energy: best bang buck"},
  {"kind": "gm", "t": "Air Sealing", "tier": "Compounded", "concept": "leaks everywhere", "mechanism": "caulk + foam gaps", "parts": ["sealant"], "build": "seal", "time": "10h", "level": "intermediate", "safety": "none", "notes": "energy: 15% heating"},
  {"kind": "gm", "t": "Heat Pump Water Heater", "tier": "Compounded", "concept": "water heat efficient", "mechanism": "heat pump 3x", "parts": ["heater"], "build": "install", "time": "12h", "level": "intermediate", "safety": "plumbing pro", "notes": "energy: 60% less"},
  {"kind": "gm", "t": "Induction Cooktop", "tier": "Compounded", "concept": "gas wastes heat", "mechanism": "induction 90% efficient", "parts": ["cooktop"], "build": "install", "time": "8h", "level": "intermediate", "safety": "electrical pro", "notes": "energy: boils faster"},
  {"kind": "gm", "t": "Smart Power Strips", "tier": "Compounded", "concept": "vampires persist", "mechanism": "auto-off strips", "parts": ["strips"], "build": "install", "time": "2h", "level": "intermediate", "safety": "none", "notes": "energy: entertainment center"},
  {"kind": "gm", "t": "Attic Tent", "tier": "Compounded", "concept": "pull-down leaks", "mechanism": "insulated tent cover", "parts": ["tent"], "build": "install", "time": "3h", "level": "intermediate", "safety": "none", "notes": "energy: seal the hole"},
  {"kind": "gm", "t": "Duct Sealing", "tier": "Compounded", "concept": "ducts leak 30%", "mechanism": "mastic seal joints", "parts": ["mastic"], "build": "seal", "time": "10h", "level": "intermediate", "safety": "dust", "notes": "energy: mastic > tape"},
  {"kind": "gm", "t": "Window Inserts", "tier": "Compounded", "concept": "old windows", "mechanism": "interior storm inserts", "parts": ["inserts"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "energy: half the cost of new"},
  {"kind": "gm", "t": "Behavior Dashboard", "tier": "Compounded", "concept": "habits matter", "mechanism": "display + goals", "parts": ["dashboard"], "build": "build", "time": "8h", "level": "intermediate", "safety": "low-voltage", "notes": "energy: gamify savings"},
  {"kind": "gm", "t": "Solar Monitor", "tier": "Compounded", "concept": "make + use", "mechanism": "solar + app", "parts": ["monitor"], "build": "install", "time": "8h", "level": "intermediate", "safety": "electrical pro", "notes": "energy: self-consume first"},
  {"kind": "gm", "t": "EV Charging Timer", "tier": "Compounded", "concept": "cheap miles", "mechanism": "off-peak schedule", "parts": ["timer"], "build": "set", "time": "2h", "level": "intermediate", "safety": "electrical", "notes": "energy: midnight electrons"},
  {"kind": "gm", "t": "Solar (Rooftop)", "tier": "Advanced", "concept": "make power", "mechanism": "5kW + net metering", "parts": ["solar"], "build": "install", "time": "40h", "level": "advanced", "safety": "solar pro", "notes": "energy: 25-year math"},
  {"kind": "gm", "t": "Heat Pump (Whole Home)", "tier": "Advanced", "concept": "heat efficiently", "mechanism": "cold-climate heat pump", "parts": ["pump"], "build": "install", "time": "30h", "level": "advanced", "safety": "HVAC pro", "notes": "energy: 300% efficient"},
  {"kind": "gm", "t": "Battery Backup", "tier": "Advanced", "concept": "outages hurt", "mechanism": "10kWh + critical panel", "parts": ["battery"], "build": "install", "time": "20h", "level": "advanced", "safety": "electrical pro", "notes": "energy: fridge + heat survive"},
  {"kind": "gm", "t": "Deep Energy Retrofit", "tier": "Advanced", "concept": "leaky house", "mechanism": "insulate + seal + HVAC", "parts": ["retrofit"], "build": "build", "time": "200h", "level": "advanced", "safety": "pro", "notes": "energy: 50%+ reduction"},
  {"kind": "gm", "t": "Net-Zero Home", "tier": "Advanced", "concept": "zero bills", "mechanism": "solar + efficient + tight", "parts": ["home"], "build": "build", "time": "500h", "level": "advanced", "safety": "pro", "notes": "energy: the summit"},
  {"kind": "gm", "t": "Community Solar", "tier": "Advanced", "concept": "no roof?", "mechanism": "subscribe local solar", "parts": ["subscription"], "build": "join", "time": "4h", "level": "advanced", "safety": "none", "notes": "energy: renters can too"},
  {"kind": "gm", "t": "Time-of-Use Shifting", "tier": "Advanced", "concept": "rates vary", "mechanism": "shift loads off-peak", "parts": ["habit"], "build": "plan", "time": "6h", "level": "advanced", "safety": "none", "notes": "energy: laundry at night"},
  {"kind": "gm", "t": "Home Battery DIY (Safe)", "tier": "Advanced", "concept": "store solar", "mechanism": "pro-installed only", "parts": ["battery"], "build": "pro", "time": "20h", "level": "advanced", "safety": "electrical pro", "notes": "energy: never DIY mains battery"},
  {"kind": "gm", "t": "Energy Audit Pro", "tier": "Advanced", "concept": "know everything", "mechanism": "blower door + IR", "parts": ["audit"], "build": "hire", "time": "8h", "level": "advanced", "safety": "none", "notes": "energy: start here actually"},
  {"kind": "gm", "t": "Passive House Retrofit", "tier": "Advanced", "concept": "ultimate efficiency", "mechanism": "superinsulate + HRV", "parts": ["retrofit"], "build": "build", "time": "400h", "level": "advanced", "safety": "pro", "notes": "energy: 90% less heat"}
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

