(function(){'use strict';
/* JAH The Personal Safety Gadget Database — real working generator, jahdb-db-personal-safety-gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSGS-";
var SLUG="db-personal-safety-gadget";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing.", "Check local laws for defensive tools; training matters more than gear."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Reflective Gear", "tier": "Foundations", "concept": "seen at night", "mechanism": "reflective vest + bands", "parts": ["gear"], "build": "wear", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: 360-degree visibility"},
  {"kind": "gm", "t": "Bike Lights", "tier": "Foundations", "concept": "dark rides", "mechanism": "USB front + rear", "parts": ["lights"], "build": "install", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: flashing rear"},
  {"kind": "gm", "t": "Whistle", "tier": "Foundations", "concept": "need help", "mechanism": "120db whistle", "parts": ["whistle"], "build": "carry", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: 3 blasts = help"},
  {"kind": "gm", "t": "Door Wedge Alarm", "tier": "Foundations", "concept": "hotel worry", "mechanism": "wedge + 120db alarm", "parts": ["wedge"], "build": "pack", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: 30-second install"},
  {"kind": "gm", "t": "Personal Alarm (Pull-Pin)", "tier": "Foundations", "concept": "deter threat", "mechanism": "130db pull alarm", "parts": ["alarm"], "build": "carry", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: pull, drop, run"},
  {"kind": "gm", "t": "First Aid (Pocket)", "tier": "Foundations", "concept": "bleeds", "mechanism": "kit + training", "parts": ["kit"], "build": "pack", "time": "2h", "level": "beginner", "safety": "training", "notes": "safety: training beats kit"},
  {"kind": "gm", "t": "Headlamp", "tier": "Foundations", "concept": "dark paths", "mechanism": "300lm headlamp", "parts": ["lamp"], "build": "wear", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: see + be seen"},
  {"kind": "gm", "t": "Sunscreen + Hat", "tier": "Foundations", "concept": "sun harms", "mechanism": "SPF + brim", "parts": ["gear"], "build": "wear", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: reapply 2h"},
  {"kind": "gm", "t": "Water + Snacks", "tier": "Foundations", "concept": "bonk danger", "mechanism": "carry always", "parts": ["kit"], "build": "pack", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: eat before hungry"},
  {"kind": "gm", "t": "Charged Phone", "tier": "Foundations", "concept": "stranded", "mechanism": "bank + cable", "parts": ["bank"], "build": "pack", "time": "1h", "level": "beginner", "safety": "battery", "notes": "safety: 20% rule"},
  {"kind": "gm", "t": "ID + Emergency Card", "tier": "Foundations", "concept": "if hurt", "mechanism": "card in wallet", "parts": ["card"], "build": "make", "time": "1h", "level": "beginner", "safety": "none", "notes": "safety: ICE contacts"},
  {"kind": "gm", "t": "Pepper Spray (Legal)", "tier": "Compounded", "concept": "deter attacker", "mechanism": "spray + training", "parts": ["spray"], "build": "carry", "time": "2h", "level": "intermediate", "safety": "legal check", "notes": "safety: wind awareness; practice"},
  {"kind": "gm", "t": "Tactical Flashlight", "tier": "Compounded", "concept": "blind + see", "mechanism": "1000lm strobe", "parts": ["light"], "build": "carry", "time": "1h", "level": "intermediate", "safety": "none", "notes": "safety: strobe disorients"},
  {"kind": "gm", "t": "Door Bar", "tier": "Compounded", "concept": "hotel + home", "mechanism": "adjustable bar", "parts": ["bar"], "build": "use", "time": "1h", "level": "intermediate", "safety": "none", "notes": "safety: under knob"},
  {"kind": "gm", "t": "Window Locks", "tier": "Compounded", "concept": "windows entry", "mechanism": "pin locks", "parts": ["locks"], "build": "install", "time": "3h", "level": "intermediate", "safety": "none", "notes": "safety: 4in vent option"},
  {"kind": "gm", "t": "Safe (Quick Access)", "tier": "Compounded", "concept": "secure valuables", "mechanism": "biometric safe", "parts": ["safe"], "build": "install", "time": "4h", "level": "intermediate", "safety": "bolt down", "notes": "safety: bolt to studs"},
  {"kind": "gm", "t": "Dash Cam", "tier": "Compounded", "concept": "crash proof", "mechanism": "cam + parking mode", "parts": ["cam"], "build": "install", "time": "3h", "level": "intermediate", "safety": "none", "notes": "safety: hardwire kit"},
  {"kind": "gm", "t": "GPS Tracker (Car)", "tier": "Compounded", "concept": "find car", "mechanism": "hidden tracker", "parts": ["tracker"], "build": "install", "time": "2h", "level": "intermediate", "safety": "none", "notes": "safety: consent laws"},
  {"kind": "gm", "t": "Smoke + CO (10yr)", "tier": "Compounded", "concept": "silent killers", "mechanism": "sealed 10yr alarms", "parts": ["alarms"], "build": "install", "time": "2h", "level": "intermediate", "safety": "none", "notes": "safety: every level + bedroom"},
  {"kind": "gm", "t": "Fire Extinguisher", "tier": "Compounded", "concept": "small fires", "mechanism": "ABC + training", "parts": ["ext"], "build": "mount", "time": "2h", "level": "intermediate", "safety": "training", "notes": "safety: PASS training"},
  {"kind": "gm", "t": "Escape Ladder", "tier": "Compounded", "concept": "upstairs fire", "mechanism": "chain ladder", "parts": ["ladder"], "build": "store", "time": "1h", "level": "intermediate", "safety": "practice", "notes": "safety: practice deploy"},
  {"kind": "gm", "t": "Water Sensor + Shutoff", "tier": "Compounded", "concept": "floods ruin", "mechanism": "sensor + auto valve", "parts": ["sensor"], "build": "install", "time": "6h", "level": "intermediate", "safety": "plumbing", "notes": "safety: test monthly"},
  {"kind": "gm", "t": "Bike Radar", "tier": "Compounded", "concept": "cars behind", "mechanism": "radar + display", "parts": ["radar"], "build": "install", "time": "4h", "level": "intermediate", "safety": "none", "notes": "safety: see threats early"},
  {"kind": "gm", "t": "Home Security System", "tier": "Advanced", "concept": "break-ins", "mechanism": "pro monitored", "parts": ["system"], "build": "install", "time": "16h", "level": "advanced", "safety": "pro", "notes": "safety: layered defense"},
  {"kind": "gm", "t": "Safe Room (Concept)", "tier": "Advanced", "concept": "worst case", "mechanism": "reinforced room", "parts": ["room"], "build": "build", "time": "80h", "level": "advanced", "safety": "pro", "notes": "safety: comms inside"},
  {"kind": "gm", "t": "Storm Shelter", "tier": "Advanced", "concept": "tornadoes", "mechanism": "FEMA-rated shelter", "parts": ["shelter"], "build": "install", "time": "40h", "level": "advanced", "safety": "pro install", "notes": "safety: register location"},
  {"kind": "gm", "t": "Generator (Home)", "tier": "Advanced", "concept": "outages", "mechanism": "standby + transfer", "parts": ["gen"], "build": "install", "time": "20h", "level": "advanced", "safety": "electrical pro + CO", "notes": "safety: CO detectors; never indoor"},
  {"kind": "gm", "t": "Lightning Protection", "tier": "Advanced", "concept": "strikes", "mechanism": "rods + grounding", "parts": ["system"], "build": "install", "time": "16h", "level": "advanced", "safety": "pro", "notes": "safety: UL-listed"},
  {"kind": "gm", "t": "Wildfire Defense", "tier": "Advanced", "concept": "embers ignite", "mechanism": "defensible space + vents", "parts": ["defense"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "safety: 100ft clearance"},
  {"kind": "gm", "t": "Flood Barriers", "tier": "Advanced", "concept": "water rises", "mechanism": "door + vent barriers", "parts": ["barriers"], "build": "install", "time": "16h", "level": "advanced", "safety": "none", "notes": "safety: deploy early"},
  {"kind": "gm", "t": "Earthquake Retrofit", "tier": "Advanced", "concept": "shaking", "mechanism": "bolts + bracing", "parts": ["retrofit"], "build": "build", "time": "60h", "level": "advanced", "safety": "pro", "notes": "safety: strap water heater"},
  {"kind": "gm", "t": "Personal Locator Beacon", "tier": "Advanced", "concept": "lost outdoors", "mechanism": "satellite SOS", "parts": ["plb"], "build": "carry", "time": "2h", "level": "advanced", "safety": "register", "notes": "safety: register NOAA"},
  {"kind": "gm", "t": "Satellite Messenger", "tier": "Advanced", "concept": "no signal", "mechanism": "2-way satellite", "parts": ["device"], "build": "carry", "time": "2h", "level": "advanced", "safety": "subscription", "notes": "safety: test before trip"},
  {"kind": "gm", "t": "Master Safety Plan", "tier": "Advanced", "concept": "everything", "mechanism": "plan + kits + drills", "parts": ["plan"], "build": "write", "time": "12h", "level": "advanced", "safety": "none", "notes": "safety: drill twice yearly"}
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

