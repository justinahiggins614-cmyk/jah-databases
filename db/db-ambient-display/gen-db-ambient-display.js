(function(){'use strict';
/* JAH The Ambient Display Database — real working generator, jahdb-db-ambient-display-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AMDI-";
var SLUG="db-ambient-display";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing.", "Low-voltage builds only; mains-powered displays installed by qualified persons."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Word Clock", "tier": "Foundations", "concept": "time as words", "mechanism": "LED matrix spells time", "parts": ["clock"], "build": "build", "time": "12h", "level": "beginner", "safety": "low-voltage", "notes": "display: glanceable time"},
  {"kind": "gm", "t": "Weather Cube", "tier": "Foundations", "concept": "weather glance", "mechanism": "cube glows forecast", "parts": ["cube"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "display: blue=rain, yellow=sun"},
  {"kind": "gm", "t": "Sunrise Lamp", "tier": "Foundations", "concept": "wake gentle", "mechanism": "dawn simulation", "parts": ["lamp"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "display: 30-min dawn"},
  {"kind": "gm", "t": "Tide Clock", "tier": "Foundations", "concept": "tide glance", "mechanism": "dial tracks tides", "parts": ["clock"], "build": "build", "time": "8h", "level": "beginner", "safety": "none", "notes": "display: set to local port"},
  {"kind": "gm", "t": "Moon Phase Light", "tier": "Foundations", "concept": "moon tonight", "mechanism": "globe shows phase", "parts": ["moon"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "display: sync monthly"},
  {"kind": "gm", "t": "Stock Ticker (Calm)", "tier": "Foundations", "concept": "market calm", "mechanism": "e-ink + sparklines", "parts": ["ticker"], "build": "build", "time": "12h", "level": "beginner", "safety": "low-voltage", "notes": "display: daily, not ticks"},
  {"kind": "gm", "t": "Calendar Glow", "tier": "Foundations", "concept": "day glance", "mechanism": "color = schedule load", "parts": ["glow"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "display: red = busy"},
  {"kind": "gm", "t": "Plant Happiness", "tier": "Foundations", "concept": "plant needs", "mechanism": "leaf color = moisture", "parts": ["plant"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "display: the plant talks"},
  {"kind": "gm", "t": "Commute Light", "tier": "Foundations", "concept": "leave now?", "mechanism": "green/yellow/red traffic", "parts": ["light"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "display: check before keys"},
  {"kind": "gm", "t": "Laundry Done Glow", "tier": "Foundations", "concept": "forget laundry", "mechanism": "vibration + glow", "parts": ["sensor"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "display: buzz the dryer"},
  {"kind": "gm", "t": "Mailbox Flag (Smart)", "tier": "Foundations", "concept": "mail?", "mechanism": "sensor + indoor glow", "parts": ["flag"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "display: flag up = mail"},
  {"kind": "gm", "t": "Energy Orb", "tier": "Compounded", "concept": "usage visible", "mechanism": "orb color = watts", "parts": ["orb"], "build": "build", "time": "12h", "level": "intermediate", "safety": "electrical pro", "notes": "display: red = expensive now"},
  {"kind": "gm", "t": "Air Quality Bloom", "tier": "Compounded", "concept": "air visible", "mechanism": "flower opens/closes", "parts": ["bloom"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "display: bloom = fresh"},
  {"kind": "gm", "t": "Network Status Light", "tier": "Compounded", "concept": "net down?", "mechanism": "glow = up/down", "parts": ["lamp"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "display: red = reboot router"},
  {"kind": "gm", "t": "Bus Arrival Glow", "tier": "Compounded", "concept": "bus when?", "mechanism": "countdown glow", "parts": ["display"], "build": "build", "time": "12h", "level": "intermediate", "safety": "low-voltage", "notes": "display: pulse = 5 min"},
  {"kind": "gm", "t": "Meeting Room Sign", "tier": "Compounded", "concept": "occupied?", "mechanism": "e-ink + glow", "parts": ["sign"], "build": "build", "time": "12h", "level": "intermediate", "safety": "low-voltage", "notes": "display: red = in use"},
  {"kind": "gm", "t": "Crypto Calm (E-Ink)", "tier": "Compounded", "concept": "prices calm", "mechanism": "sparkline e-ink", "parts": ["display"], "build": "build", "time": "12h", "level": "intermediate", "safety": "low-voltage", "notes": "display: weekly view"},
  {"kind": "gm", "t": "Sleep Score Sunrise", "tier": "Compounded", "concept": "sleep glance", "mechanism": "dawn color = score", "parts": ["lamp"], "build": "build", "time": "12h", "level": "intermediate", "safety": "low-voltage", "notes": "display: blue = great"},
  {"kind": "gm", "t": "Garden Moisture Map", "tier": "Compounded", "concept": "water where?", "mechanism": "grid glows dry spots", "parts": ["map"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "display: water the red"},
  {"kind": "gm", "t": "Fridge Expiry Glow", "tier": "Compounded", "concept": "food rots", "mechanism": "camera + shelf glow", "parts": ["shelf"], "build": "build", "time": "20h", "level": "intermediate", "safety": "low-voltage", "notes": "display: eat the glowing"},
  {"kind": "gm", "t": "Stove-On Reminder", "tier": "Compounded", "concept": "stove left?", "mechanism": "heat + timer glow", "parts": ["sensor"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "display: never leave glowing"},
  {"kind": "gm", "t": "Water Usage Fountain", "tier": "Compounded", "concept": "water visible", "mechanism": "flow = usage", "parts": ["fountain"], "build": "build", "time": "16h", "level": "intermediate", "safety": "plumbing", "notes": "display: drought mode trickle"},
  {"kind": "gm", "t": "Laundry Room Glow", "tier": "Compounded", "concept": "dryer done?", "mechanism": "vibration + light", "parts": ["sensor"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "display: fold reminder"},
  {"kind": "gm", "t": "Fridge Door Ajar", "tier": "Compounded", "concept": "door open?", "mechanism": "sensor + chime", "parts": ["sensor"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "display: gentle nag"},
  {"kind": "gm", "t": "Whole-Home Dashboard", "tier": "Advanced", "concept": "home at glance", "mechanism": "e-ink wall panel", "parts": ["panel"], "build": "build", "time": "30h", "level": "advanced", "safety": "low-voltage", "notes": "display: one glance morning"},
  {"kind": "gm", "t": "Ambient Office Wall", "tier": "Advanced", "concept": "team pulse", "mechanism": "wall of calm data", "parts": ["wall"], "build": "build", "time": "40h", "level": "advanced", "safety": "low-voltage", "notes": "display: no numbers, just feel"},
  {"kind": "gm", "t": "Museum Calm Display", "tier": "Advanced", "concept": "info without screens", "mechanism": "physical pixels", "parts": ["display"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "display: flip-dot poetry"},
  {"kind": "gm", "t": "Hospital Calm Board", "tier": "Advanced", "concept": "anxiety down", "mechanism": "soft status glow", "parts": ["board"], "build": "build", "time": "40h", "level": "advanced", "safety": "pro", "notes": "display: calm is clinical"},
  {"kind": "gm", "t": "City Data Sculpture", "tier": "Advanced", "concept": "city pulse", "mechanism": "public ambient art", "parts": ["art"], "build": "build", "time": "80h", "level": "advanced", "safety": "pro", "notes": "display: data as beauty"},
  {"kind": "gm", "t": "Elder Care Glow", "tier": "Advanced", "concept": "okay at glance", "mechanism": "presence + routine glow", "parts": ["glow"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "display: dignity first"},
  {"kind": "gm", "t": "Classroom Calm Board", "tier": "Advanced", "concept": "noise visible", "mechanism": "volume = color", "parts": ["board"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "display: self-regulation"},
  {"kind": "gm", "t": "Factory Andon (Calm)", "tier": "Advanced", "concept": "status calm", "mechanism": "andon reimagined", "parts": ["andon"], "build": "build", "time": "30h", "level": "advanced", "safety": "pro", "notes": "display: calm > alarm"},
  {"kind": "gm", "t": "Gallery Data Art", "tier": "Advanced", "concept": "data beautiful", "mechanism": "ambient installations", "parts": ["art"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "display: feel the numbers"},
  {"kind": "gm", "t": "Master Ambient Home", "tier": "Advanced", "concept": "everything calm", "mechanism": "whole-home system", "parts": ["home"], "build": "build", "time": "80h", "level": "advanced", "safety": "pro", "notes": "display: the home whispers"}
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

