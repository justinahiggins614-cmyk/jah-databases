(function(){'use strict';
/* JAH The DIY Instrument Maker Database — real working generator, jahdb-gen-diy-instrument-maker-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DIM-";
var SLUG="gen-diy-instrument-maker";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Shaker (Rice in Can)", "tier": "Foundations", "concept": "rhythm", "mechanism": "rice + sealed can", "parts": ["shaker"], "build": "make", "time": "1h", "level": "beginner", "safety": "none", "notes": "instrument: seal tight"},
  {"kind": "gm", "t": "Drum (Bucket)", "tier": "Foundations", "concept": "beat", "mechanism": "bucket + sticks", "parts": ["drum"], "build": "study", "time": "1h", "level": "beginner", "safety": "hearing", "notes": "instrument: 5-gallon bass"},
  {"kind": "gm", "t": "Kazoo", "tier": "Foundations", "concept": "buzz melody", "mechanism": "membrane vibrates", "parts": ["kazoo"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "instrument: hum, don't blow"},
  {"kind": "gm", "t": "Spoons", "tier": "Foundations", "concept": "percussion", "mechanism": "two spoons click", "parts": ["spoons"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "instrument: loose grip"},
  {"kind": "gm", "t": "Washboard", "tier": "Foundations", "concept": "rhythm", "mechanism": "thimbles on ridges", "parts": ["board"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "instrument: metal > wood"},
  {"kind": "gm", "t": "Jug (Bass)", "tier": "Foundations", "concept": "bass notes", "mechanism": "buzz lips on jug", "parts": ["jug"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "instrument: bigger = lower"},
  {"kind": "gm", "t": "Rubber Band Guitar", "tier": "Foundations", "concept": "strings", "mechanism": "box + bands", "parts": ["guitar"], "build": "make", "time": "2h", "level": "beginner", "safety": "none", "notes": "instrument: tension tunes"},
  {"kind": "gm", "t": "Paper Flute", "tier": "Foundations", "concept": "melody", "mechanism": "straw + holes", "parts": ["flute"], "build": "make", "time": "1h", "level": "beginner", "safety": "none", "notes": "instrument: cover holes fully"},
  {"kind": "gm", "t": "Water Glasses", "tier": "Foundations", "concept": "ethereal tones", "mechanism": "tuned water levels", "parts": ["glasses"], "build": "tune", "time": "2h", "level": "beginner", "safety": "glass care", "notes": "instrument: more water = lower"},
  {"kind": "gm", "t": "Boomwhackers (DIY)", "tier": "Foundations", "concept": "pitched percussion", "mechanism": "tuned tubes", "parts": ["tubes"], "build": "cut", "time": "3h", "level": "beginner", "safety": "none", "notes": "instrument: length tunes pitch"},
  {"kind": "gm", "t": "Rain Stick", "tier": "Foundations", "concept": "rain sound", "mechanism": "nails + rice in tube", "parts": ["stick"], "build": "make", "time": "3h", "level": "beginner", "safety": "none", "notes": "instrument: spiral nails slow fall"},
  {"kind": "gm", "t": "Cigar Box Guitar (3-String)", "tier": "Compounded", "concept": "real strings", "mechanism": "box + neck + strings", "parts": ["guitar"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "instrument: open G tuning"},
  {"kind": "gm", "t": "Kalimba (Thumb Piano)", "tier": "Compounded", "concept": "melody", "mechanism": "tuned steel tines", "parts": ["kalimba"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "instrument: tine length tunes"},
  {"kind": "gm", "t": "Didgeridoo (PVC)", "tier": "Compounded", "concept": "drone", "mechanism": "circular breathing tube", "parts": ["didge"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "instrument: beeswax mouthpiece"},
  {"kind": "gm", "t": "Cajon (Box Drum)", "tier": "Compounded", "concept": "drum kit in box", "mechanism": "snare + bass in box", "parts": ["cajon"], "build": "build", "time": "12h", "level": "intermediate", "safety": "saw safety", "notes": "instrument: snare wires inside"},
  {"kind": "gm", "t": "Ukulele Kit", "tier": "Compounded", "concept": "real chords", "mechanism": "kit build + setup", "parts": ["uke"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "instrument: setup matters most"},
  {"kind": "gm", "t": "Native Flute (PVC)", "tier": "Compounded", "concept": "haunting melody", "mechanism": "tuned 5-hole flute", "parts": ["flute"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "instrument: slow air"},
  {"kind": "gm", "t": "Stomp Box", "tier": "Compounded", "concept": "beat with feet", "mechanism": "piezo in box", "parts": ["box"], "build": "build", "time": "6h", "level": "intermediate", "safety": "low-voltage", "notes": "instrument: through PA"},
  {"kind": "gm", "t": "Washtub Bass", "tier": "Compounded", "concept": "bass line", "mechanism": "tub + string + stick", "parts": ["bass"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "instrument: tension = pitch"},
  {"kind": "gm", "t": "Xylophone (Wood)", "tier": "Compounded", "concept": "melody", "mechanism": "tuned bars", "parts": ["xylo"], "build": "build", "time": "16h", "level": "intermediate", "safety": "saw safety", "notes": "instrument: bar length tunes"},
  {"kind": "gm", "t": "Ocarina (Clay)", "tier": "Compounded", "concept": "sweet tones", "mechanism": "4-hole clay", "parts": ["ocarina"], "build": "make", "time": "10h", "level": "intermediate", "safety": "kiln", "notes": "instrument: hole size tunes"},
  {"kind": "gm", "t": "Hurdy-Gurdy (Kit)", "tier": "Compounded", "concept": "medieval drone", "mechanism": "wheel + strings kit", "parts": ["gurdy"], "build": "build", "time": "30h", "level": "intermediate", "safety": "none", "notes": "instrument: rosin the wheel"},
  {"kind": "gm", "t": "Violin (Kit Build)", "tier": "Advanced", "concept": "classical", "mechanism": "kit + varnish", "parts": ["violin"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "instrument: setup is luthier work"},
  {"kind": "gm", "t": "Guitar (Full Build)", "tier": "Advanced", "concept": "your guitar", "mechanism": "tonewood + frets", "parts": ["guitar"], "build": "build", "time": "100h", "level": "advanced", "safety": "none", "notes": "instrument: fretwork is the skill"},
  {"kind": "gm", "t": "Banjo (Kit)", "tier": "Advanced", "concept": "twang", "mechanism": "rim + head + neck", "parts": ["banjo"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "instrument: head tension tunes"},
  {"kind": "gm", "t": "Mandolin (Kit)", "tier": "Advanced", "concept": "chop chords", "mechanism": "carved top kit", "parts": ["mando"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "instrument: double courses"},
  {"kind": "gm", "t": "Dulcimer", "tier": "Advanced", "concept": "sweet drone", "mechanism": "hourglass + frets", "parts": ["dulcimer"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "instrument: DAD tuning"},
  {"kind": "gm", "t": "Harp (Small)", "tier": "Advanced", "concept": "glissando", "mechanism": "22 strings", "parts": ["harp"], "build": "build", "time": "60h", "level": "advanced", "safety": "string tension", "notes": "instrument: levers for sharps"},
  {"kind": "gm", "t": "Accordion (Restore)", "tier": "Advanced", "concept": "squeezebox", "mechanism": "restore reeds", "parts": ["accordion"], "build": "restore", "time": "40h", "level": "advanced", "safety": "none", "notes": "instrument: reed tuning pro"},
  {"kind": "gm", "t": "Bagpipes (Practice)", "tier": "Advanced", "concept": "drone on", "mechanism": "practice chanter", "parts": ["pipes"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "instrument: chanter first, year one"},
  {"kind": "gm", "t": "Steel Drum (Intro)", "tier": "Advanced", "concept": "island tones", "mechanism": "tuned 55-gal", "parts": ["drum"], "build": "study", "time": "30h", "level": "advanced", "safety": "none", "notes": "instrument: tuning is art"},
  {"kind": "gm", "t": "Theremin (Kit)", "tier": "Advanced", "concept": "play air", "mechanism": "heterodyne kit", "parts": ["theremin"], "build": "build", "time": "20h", "level": "advanced", "safety": "low-voltage", "notes": "instrument: pitch hand, volume hand"},
  {"kind": "gm", "t": "Modular Synth Voice", "tier": "Advanced", "concept": "electronic", "mechanism": "VCO+VCF+VCA DIY", "parts": ["synth"], "build": "build", "time": "40h", "level": "advanced", "safety": "soldering", "notes": "instrument: start with one voice"},
  {"kind": "gm", "t": "Bowed Psaltery", "tier": "Advanced", "concept": "bowed melody", "mechanism": "triangle + strings", "parts": ["psaltery"], "build": "build", "time": "40h", "level": "advanced", "safety": "string", "notes": "instrument: bow the edge"}
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

