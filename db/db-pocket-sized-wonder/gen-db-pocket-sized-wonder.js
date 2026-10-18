(function(){'use strict';
/* JAH The Pocket-Sized Wonder Database — real working generator, jahdb-db-pocket-sized-wonder-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-POSIWO-";
var SLUG="db-pocket-sized-wonder";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Classic Pocket Knife", "tier": "Foundations", "concept": "daily cutting needs", "mechanism": "folding blade + slip joint", "parts": ["blade", "handle"], "build": "study", "time": "2h", "level": "beginner", "safety": "blade sharp", "notes": "wonder: a century of daily carry"},
  {"kind": "gm", "t": "Mini Flashlight (AAA)", "tier": "Foundations", "concept": "dark corners everywhere", "mechanism": "AAA LED in 3-inch body", "parts": ["LED", "battery"], "build": "build", "time": "4h", "level": "beginner", "safety": "none", "notes": "wonder: 300 lumens from a finger"},
  {"kind": "gm", "t": "Pocket Multi-Tool", "tier": "Foundations", "concept": "small fixes away from kit", "mechanism": "pliers + drivers fold flat", "parts": ["steel"], "build": "study", "time": "2h", "level": "beginner", "safety": "tools sharp", "notes": "wonder: 10 tools, 4 inches"},
  {"kind": "gm", "t": "Tiny Tape Measure", "tier": "Foundations", "concept": "measure anywhere", "mechanism": "16ft in a 2-inch case", "parts": ["tape", "spring"], "build": "study", "time": "1h", "level": "beginner", "safety": "tape edge sharp", "notes": "wonder: spring recoil engineering"},
  {"kind": "gm", "t": "Pocket Notebook", "tier": "Foundations", "concept": "ideas evaporate", "mechanism": "48 pages, fits back pocket", "parts": ["paper"], "build": "bind", "time": "2h", "level": "beginner", "safety": "none", "notes": "wonder: the original cloud"},
  {"kind": "gm", "t": "Mini Lighter", "tier": "Foundations", "concept": "fire on demand", "mechanism": "butane + flint in matchbox size", "parts": ["lighter"], "build": "study", "time": "1h", "level": "beginner", "safety": "fire safety", "notes": "wonder: 3,000 lights per fill"},
  {"kind": "gm", "t": "Pocket Compass", "tier": "Foundations", "concept": "lost without signal", "mechanism": "magnetic needle + liquid damping", "parts": ["needle"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "wonder: works with zero power"},
  {"kind": "gm", "t": "Folding Scissors", "tier": "Foundations", "concept": "cut on the go", "mechanism": "scissors fold into handle", "parts": ["steel"], "build": "study", "time": "1h", "level": "beginner", "safety": "blades sharp", "notes": "wonder: full function, half size"},
  {"kind": "gm", "t": "Mini Screwdriver Set", "tier": "Foundations", "concept": "loose screws everywhere", "mechanism": "bits + ratchet in pen size", "parts": ["bits"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "wonder: 12 bits, one pen"},
  {"kind": "gm", "t": "Pocket Radio", "tier": "Foundations", "concept": "news without phone", "mechanism": "AM/FM + crank in palm size", "parts": ["radio"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "wonder: crank 1 min, listen 20"},
  {"kind": "gm", "t": "Tiny Umbrella", "tier": "Foundations", "concept": "rain surprises", "mechanism": "5-fold canopy in 7 inches", "parts": ["fabric"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "wonder: full canopy, pocket size"},
  {"kind": "gm", "t": "Pocket Microscope", "tier": "Compounded", "concept": "curiosity needs magnification", "mechanism": "60x lens + LED in pen", "parts": ["optics"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "wonder: pond water becomes alien world"},
  {"kind": "gm", "t": "Mini Tripod", "tier": "Compounded", "concept": "shaky phone video", "mechanism": "flexible legs grip anywhere", "parts": ["legs"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "wonder: wraps, stands, holds"},
  {"kind": "gm", "t": "Pocket Soldering Iron", "tier": "Compounded", "concept": "field repairs", "mechanism": "butane heat in pen size", "parts": ["iron"], "build": "build", "time": "8h", "level": "intermediate", "safety": "burn + fume safety", "notes": "wonder: 30 seconds to 450C"},
  {"kind": "gm", "t": "Tiny Drone", "tier": "Compounded", "concept": "aerial views anywhere", "mechanism": "palm-size quadcopter", "parts": ["drone"], "build": "fly", "time": "4h", "level": "intermediate", "safety": "prop safety", "notes": "wonder: stabilized flight in 80g"},
  {"kind": "gm", "t": "Pocket Projector", "tier": "Compounded", "concept": "share anywhere", "mechanism": "DLP + LED, phone-sized", "parts": ["projector"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "wonder: 100-inch screen from pocket"},
  {"kind": "gm", "t": "Mini Power Bank", "tier": "Compounded", "concept": "dead phone dread", "mechanism": "10,000mAh in card size", "parts": ["battery"], "build": "build", "time": "6h", "level": "intermediate", "safety": "battery safety", "notes": "wonder: 2 charges, wallet thin"},
  {"kind": "gm", "t": "Pocket Oscilloscope", "tier": "Compounded", "concept": "debug electronics anywhere", "mechanism": "1MHz scope in multimeter size", "parts": ["scope"], "build": "build", "time": "16h", "level": "intermediate", "safety": "electrical safety", "notes": "wonder: see signals in the field"},
  {"kind": "gm", "t": "Tiny Binoculars", "tier": "Compounded", "concept": "distance details", "mechanism": "8x21 roof prism compact", "parts": ["optics"], "build": "study", "time": "2h", "level": "intermediate", "safety": "none", "notes": "wonder: theater to trail"},
  {"kind": "gm", "t": "Pocket Weather Station", "tier": "Compounded", "concept": "microclimate matters", "mechanism": "temp/humidity/pressure sensing", "parts": ["sensor"], "build": "build", "time": "10h", "level": "intermediate", "safety": "low-voltage", "notes": "wonder: forecast your block"},
  {"kind": "gm", "t": "Mini Thermal Camera", "tier": "Compounded", "concept": "see heat leaks", "mechanism": "IR sensor + phone display", "parts": ["camera"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "wonder: find drafts instantly"},
  {"kind": "gm", "t": "Pocket Lock Picks (Legal)", "tier": "Compounded", "concept": "locked out (own lock)", "mechanism": "training picks + clear lock", "parts": ["picks"], "build": "practice", "time": "6h", "level": "intermediate", "safety": "legal: own locks only", "notes": "wonder: understand security by touching it"},
  {"kind": "gm", "t": "Pocket Satellite Messenger", "tier": "Advanced", "concept": "no signal, need help", "mechanism": "Iridium texts from palm device", "parts": ["messenger"], "build": "study", "time": "4h", "level": "advanced", "safety": "none", "notes": "wonder: SOS from anywhere on Earth"},
  {"kind": "gm", "t": "Pocket Spectrum Analyzer", "tier": "Advanced", "concept": "RF mysteries", "mechanism": "1GHz sweep in handheld", "parts": ["analyzer"], "build": "build", "time": "30h", "level": "advanced", "safety": "RF safety", "notes": "wonder: see the invisible spectrum"},
  {"kind": "gm", "t": "Mini 3D Scanner", "tier": "Advanced", "concept": "capture objects anywhere", "mechanism": "structured light + phone", "parts": ["scanner"], "build": "build", "time": "24h", "level": "advanced", "safety": "none", "notes": "wonder: pocket to printable"},
  {"kind": "gm", "t": "Pocket Geiger Counter", "tier": "Advanced", "concept": "radiation curiosity", "mechanism": "tube + click in mint-tin size", "parts": ["tube"], "build": "build", "time": "16h", "level": "advanced", "safety": "high voltage — pro", "notes": "wonder: hear the background"},
  {"kind": "gm", "t": "Tiny Lathe", "tier": "Advanced", "concept": "turn small parts anywhere", "mechanism": "watchmaker lathe, briefcase size", "parts": ["lathe"], "build": "build", "time": "40h", "level": "advanced", "safety": "machine safety", "notes": "wonder: 0.01mm from a suitcase"},
  {"kind": "gm", "t": "Pocket Server", "tier": "Advanced", "concept": "cloud in pocket", "mechanism": "Pi + SSD + battery server", "parts": ["computer"], "build": "build", "time": "10h", "level": "advanced", "safety": "none", "notes": "wonder: your data, your pocket"},
  {"kind": "gm", "t": "Mini Sequencer", "tier": "Advanced", "concept": "beats anywhere", "mechanism": "16-step + synth pocket", "parts": ["sequencer"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "wonder: album from a jacket pocket"},
  {"kind": "gm", "t": "Pocket Telescope", "tier": "Advanced", "concept": "stars anywhere", "mechanism": "70mm collapsible refractor", "parts": ["optics"], "build": "build", "time": "16h", "level": "advanced", "safety": "never sun", "notes": "wonder: Saturn's rings, carry-on"},
  {"kind": "gm", "t": "Tiny Foundry", "tier": "Advanced", "concept": "cast anywhere?", "mechanism": "propane micro-furnace (outdoor)", "parts": ["furnace"], "build": "build", "time": "30h", "level": "advanced", "safety": "molten metal — pro supervision", "notes": "wonder: bronze from a bucket"},
  {"kind": "gm", "t": "Pocket Lab (Chemistry)", "tier": "Advanced", "concept": "test anywhere", "mechanism": "reagents + strips kit", "parts": ["kit"], "build": "study", "time": "8h", "level": "advanced", "safety": "chemical safety", "notes": "wonder: water testing in the field"},
  {"kind": "gm", "t": "Mini Wind Turbine", "tier": "Advanced", "concept": "power anywhere", "mechanism": "400W foldable turbine", "parts": ["turbine"], "build": "build", "time": "24h", "level": "advanced", "safety": "blade safety", "notes": "wonder: campsite power from air"},
  {"kind": "gm", "t": "Pocket Anemometer", "tier": "Advanced", "concept": "wind where?", "mechanism": "tiny fan + readout", "parts": ["meter"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "wonder: drone pilots love"}
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

