(function(){'use strict';
/* JAH The Portable Lab Database — real working generator, jahdb-db-portable-lab-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-POLAS-";
var SLUG="db-portable-lab";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Water Test Kit", "tier": "Foundations", "concept": "water safe?", "mechanism": "strips + meter kit", "parts": ["kit"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "lab: pH, chlorine, hardness"},
  {"kind": "gm", "t": "Soil Test Kit", "tier": "Foundations", "concept": "garden hungry?", "mechanism": "NPK + pH kit", "parts": ["kit"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "lab: test before fertilizing"},
  {"kind": "gm", "t": "Air Quality (Handheld)", "tier": "Foundations", "concept": "air okay?", "mechanism": "PM + VOC handheld", "parts": ["meter"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "lab: cook with vent"},
  {"kind": "gm", "t": "Magnifier (Field)", "tier": "Foundations", "concept": "see small", "mechanism": "10x loupe", "parts": ["loupe"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "lab: triplet lens best"},
  {"kind": "gm", "t": "pH Meter (Pocket)", "tier": "Foundations", "concept": "acidity?", "mechanism": "digital pH pen", "parts": ["meter"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "lab: calibrate monthly"},
  {"kind": "gm", "t": "Thermometer (IR)", "tier": "Foundations", "concept": "how hot?", "mechanism": "IR gun", "parts": ["gun"], "build": "study", "time": "1h", "level": "beginner", "safety": "laser safety", "notes": "lab: emissivity matters"},
  {"kind": "gm", "t": "Multimeter (Field)", "tier": "Foundations", "concept": "volts?", "mechanism": "pocket DMM", "parts": ["meter"], "build": "study", "time": "2h", "level": "beginner", "safety": "electrical", "notes": "lab: test leads first"},
  {"kind": "gm", "t": "Field Microscope", "tier": "Foundations", "concept": "tiny world", "mechanism": "60x + light", "parts": ["scope"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "lab: pond water wow"},
  {"kind": "gm", "t": "Sample Jars Kit", "tier": "Foundations", "concept": "collect", "mechanism": "jars + labels", "parts": ["jars"], "build": "pack", "time": "1h", "level": "beginner", "safety": "none", "notes": "lab: label everything"},
  {"kind": "gm", "t": "Notebook (Rite in Rain)", "tier": "Foundations", "concept": "record", "mechanism": "all-weather book", "parts": ["book"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "lab: pencil works wet"},
  {"kind": "gm", "t": "GPS (Handheld)", "tier": "Foundations", "concept": "where?", "mechanism": "handheld GPS", "parts": ["gps"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "lab: waypoint everything"},
  {"kind": "gm", "t": "Spectrometer (DIY)", "tier": "Compounded", "concept": "what color?", "mechanism": "grating + phone camera", "parts": ["spec"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "lab: calibrate with CFL"},
  {"kind": "gm", "t": "Turbidity Tube", "tier": "Compounded", "concept": "water clear?", "mechanism": "secchi tube", "parts": ["tube"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "lab: citizen science"},
  {"kind": "gm", "t": "Dissolved Oxygen Kit", "tier": "Compounded", "concept": "fish okay?", "mechanism": "titration kit", "parts": ["kit"], "build": "study", "time": "4h", "level": "intermediate", "safety": "chemical", "notes": "lab: dawn readings lowest"},
  {"kind": "gm", "t": "Weather Station (Portable)", "tier": "Compounded", "concept": "microclimate?", "mechanism": "temp/hum/pressure", "parts": ["station"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "lab: shade the sensor"},
  {"kind": "gm", "t": "Sound Meter", "tier": "Compounded", "concept": "how loud?", "mechanism": "dB meter", "parts": ["meter"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "lab: A-weighting"},
  {"kind": "gm", "t": "Light Meter", "tier": "Compounded", "concept": "enough light?", "mechanism": "lux meter", "parts": ["meter"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "lab: plants need DLI"},
  {"kind": "gm", "t": "Geiger (Pocket)", "tier": "Compounded", "concept": "radiation?", "mechanism": "tube + phone", "parts": ["tube"], "build": "build", "time": "16h", "level": "intermediate", "safety": "high voltage", "notes": "lab: background first"},
  {"kind": "gm", "t": "Chromatography (Paper)", "tier": "Compounded", "concept": "separate inks", "mechanism": "paper + solvent", "parts": ["kit"], "build": "study", "time": "4h", "level": "intermediate", "safety": "solvent ventilate", "notes": "lab: markers separate beautifully"},
  {"kind": "gm", "t": "Electroscope (DIY)", "tier": "Compounded", "concept": "static?", "mechanism": "foil leaves jar", "parts": ["scope"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "lab: charge by rubbing"},
  {"kind": "gm", "t": "Barometer (DIY)", "tier": "Compounded", "concept": "pressure?", "mechanism": "balloon + jar", "parts": ["meter"], "build": "build", "time": "3h", "level": "intermediate", "safety": "none", "notes": "lab: storms drop pressure"},
  {"kind": "gm", "t": "Rain Gauge", "tier": "Compounded", "concept": "how much?", "mechanism": "funnel + tube", "parts": ["gauge"], "build": "build", "time": "2h", "level": "intermediate", "safety": "none", "notes": "lab: level placement"},
  {"kind": "gm", "t": "Soil Respiration Kit", "tier": "Compounded", "concept": "soil alive?", "mechanism": "CO2 trap", "parts": ["kit"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "lab: biology breathing"},
  {"kind": "gm", "t": "Portable Centrifuge", "tier": "Advanced", "concept": "separate?", "mechanism": "hand-crank + tubes", "parts": ["fuge"], "build": "build", "time": "20h", "level": "advanced", "safety": "spin safety", "notes": "lab: balance tubes"},
  {"kind": "gm", "t": "PCR (Mini)", "tier": "Advanced", "concept": "amplify DNA", "mechanism": "mini thermal cycler", "parts": ["cycler"], "build": "build", "time": "60h", "level": "advanced", "safety": "lab pro", "notes": "lab: primers matter"},
  {"kind": "gm", "t": "Gel Electrophoresis", "tier": "Advanced", "concept": "separate DNA", "mechanism": "gel box + power", "parts": ["gel"], "build": "build", "time": "30h", "level": "advanced", "safety": "electrical", "notes": "lab: stain safety"},
  {"kind": "gm", "t": "Microscope (Compound)", "tier": "Advanced", "concept": "cells?", "mechanism": "portable compound", "parts": ["scope"], "build": "study", "time": "8h", "level": "advanced", "safety": "none", "notes": "lab: 400x reveals cells"},
  {"kind": "gm", "t": "Telescope (Field)", "tier": "Advanced", "concept": "stars?", "mechanism": "80mm portable", "parts": ["scope"], "build": "study", "time": "8h", "level": "advanced", "safety": "never sun", "notes": "lab: dark skies"},
  {"kind": "gm", "t": "Drone Survey Kit", "tier": "Advanced", "concept": "map land", "mechanism": "drone + software", "parts": ["drone"], "build": "fly", "time": "20h", "level": "advanced", "safety": "drone laws", "notes": "lab: overlap 70%"},
  {"kind": "gm", "t": "Seismic (DIY)", "tier": "Advanced", "concept": "quakes?", "mechanism": "pendulum sensor", "parts": ["sensor"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "lab: quiet basement"},
  {"kind": "gm", "t": "Weather Balloon", "tier": "Advanced", "concept": "upper air", "mechanism": "balloon + sonde", "parts": ["balloon"], "build": "launch", "time": "30h", "level": "advanced", "safety": "FAA rules", "notes": "lab: notify FAA"},
  {"kind": "gm", "t": "Cave Survey Kit", "tier": "Advanced", "concept": "map caves", "mechanism": "dist + compass + book", "parts": ["kit"], "build": "study", "time": "12h", "level": "advanced", "safety": "cave safety", "notes": "lab: 3 sources light"},
  {"kind": "gm", "t": "Full Field Station", "tier": "Advanced", "concept": "lab anywhere", "mechanism": "Pelican-case lab", "parts": ["case"], "build": "pack", "time": "40h", "level": "advanced", "safety": "training", "notes": "lab: protocol binder"},
  {"kind": "gm", "t": "Plankton Net", "tier": "Advanced", "concept": "tiny sea life", "mechanism": "fine mesh tow", "parts": ["net"], "build": "build", "time": "12h", "level": "advanced", "safety": "water safety", "notes": "lab: tow slowly"}
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

