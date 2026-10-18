(function(){'use strict';
/* JAH The Custom Controller Database — real working generator, jahdb-db-custom-controller-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CUCOS-";
var SLUG="db-custom-controller";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing.", "FCC Part 15 for intentional radiators; low-voltage USB builds stay in the safe zone."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Arcade Stick", "tier": "Foundations", "concept": "fighting needs precision", "mechanism": "stick + 8 buttons USB", "parts": ["parts"], "build": "build", "time": "10h", "level": "beginner", "safety": "soldering fumes", "notes": "controller: Sanwa parts worth it"},
  {"kind": "gm", "t": "Macro Pad (6-Key)", "tier": "Foundations", "concept": "shortcuts buried", "mechanism": "6 keys + knob USB", "parts": ["parts"], "build": "build", "time": "8h", "level": "beginner", "safety": "soldering", "notes": "controller: knob = volume/scroll"},
  {"kind": "gm", "t": "Foot Pedal (Single)", "tier": "Foundations", "concept": "hands full", "mechanism": "USB foot switch", "parts": ["pedal"], "build": "build", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "controller: push-to-talk"},
  {"kind": "gm", "t": "Big Button (Accessibility)", "tier": "Foundations", "concept": "small buttons hard", "mechanism": "100mm arcade button USB", "parts": ["parts"], "build": "build", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "controller: accessibility first"},
  {"kind": "gm", "t": "Presentation Clicker", "tier": "Foundations", "concept": "tethered presenting", "mechanism": "2-button wireless", "parts": ["parts"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "controller: laser-free (safer)"},
  {"kind": "gm", "t": "DJ Mini Controller", "tier": "Foundations", "concept": "mix on the go", "mechanism": "2 decks + crossfader MIDI", "parts": ["parts"], "build": "build", "time": "12h", "level": "beginner", "safety": "low-voltage", "notes": "controller: map to free software"},
  {"kind": "gm", "t": "Game Buzzer Set", "tier": "Foundations", "concept": "quiz nights", "mechanism": "4 buzzers + lights", "parts": ["parts"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "controller: fastest finger wins"},
  {"kind": "gm", "t": "Stream Deck (DIY)", "tier": "Foundations", "concept": "streaming shortcuts", "mechanism": "15 keys + icons", "parts": ["parts"], "build": "build", "time": "12h", "level": "beginner", "safety": "low-voltage", "notes": "controller: icons on tiny screens"},
  {"kind": "gm", "t": "Flight Sim Throttle", "tier": "Foundations", "concept": "flying needs feel", "mechanism": "sliding throttle quadrant", "parts": ["parts"], "build": "build", "time": "12h", "level": "beginner", "safety": "none", "notes": "controller: detents at idle"},
  {"kind": "gm", "t": "Drum Pad (Single)", "tier": "Foundations", "concept": "beats anywhere", "mechanism": "piezo pad + MIDI", "parts": ["parts"], "build": "build", "time": "8h", "level": "beginner", "safety": "low-voltage", "notes": "controller: velocity matters"},
  {"kind": "gm", "t": "Camera Shutter Remote", "tier": "Foundations", "concept": "shake ruins shots", "mechanism": "wired/wireless trigger", "parts": ["parts"], "build": "build", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "controller: half-press focus"},
  {"kind": "gm", "t": "Racing Wheel (DIY)", "tier": "Compounded", "concept": "racing needs wheel", "mechanism": "270-degree + pedals", "parts": ["parts"], "build": "build", "time": "30h", "level": "intermediate", "safety": "soldering", "notes": "controller: FFB is advanced — start spring"},
  {"kind": "gm", "t": "HOTAS Setup", "tier": "Compounded", "concept": "flight sim immersion", "mechanism": "stick + throttle separate", "parts": ["parts"], "build": "build", "time": "30h", "level": "intermediate", "safety": "none", "notes": "controller: mounts matter"},
  {"kind": "gm", "t": "MIDI Fighter", "tier": "Compounded", "concept": "finger drumming", "mechanism": "16 pads velocity", "parts": ["parts"], "build": "build", "time": "20h", "level": "intermediate", "safety": "soldering", "notes": "controller: aftertouch bonus"},
  {"kind": "gm", "t": "Accessibility Switch Hub", "tier": "Compounded", "concept": "one switch many needs", "mechanism": "hub + scanning software", "parts": ["parts"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "controller: co-design with user"},
  {"kind": "gm", "t": "Train Controller", "tier": "Compounded", "concept": "model trains", "mechanism": "throttle + direction + sound", "parts": ["parts"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "controller: momentum simulation"},
  {"kind": "gm", "t": "Pinball Plunger", "tier": "Compounded", "concept": "pinball feel", "mechanism": "spring plunger + sensor", "parts": ["parts"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "controller: analog skill shot"},
  {"kind": "gm", "t": "Guitar Hero Controller", "tier": "Compounded", "concept": "rhythm games", "mechanism": "5 frets + strum bar", "parts": ["parts"], "build": "build", "time": "20h", "level": "intermediate", "safety": "soldering", "notes": "controller: strum feel is everything"},
  {"kind": "gm", "t": "VR Treadmill (Slip)", "tier": "Compounded", "concept": "walk in VR", "mechanism": "low-friction dish + shoes", "parts": ["dish"], "build": "build", "time": "30h", "level": "intermediate", "safety": "fall safety", "notes": "controller: harness first"},
  {"kind": "gm", "t": "Motion Controller Glove", "tier": "Compounded", "concept": "hands in VR", "mechanism": "flex sensors + IMU", "parts": ["glove"], "build": "build", "time": "24h", "level": "intermediate", "safety": "low-voltage", "notes": "controller: calibrate per hand"},
  {"kind": "gm", "t": "Sim Racing Pedals", "tier": "Compounded", "concept": "braking feel", "mechanism": "load cell brake pedal", "parts": ["parts"], "build": "build", "time": "20h", "level": "intermediate", "safety": "none", "notes": "controller: load cell > potentiometer"},
  {"kind": "gm", "t": "Custom Keyboard (Full)", "tier": "Compounded", "concept": "typing is personal", "mechanism": "full hand-wire build", "parts": ["parts"], "build": "build", "time": "30h", "level": "intermediate", "safety": "soldering", "notes": "controller: layout first, solder second"},
  {"kind": "gm", "t": "Force-Feedback Wheel", "tier": "Advanced", "concept": "real racing feel", "mechanism": "direct drive motor", "parts": ["parts"], "build": "build", "time": "60h", "level": "advanced", "safety": "torque safety", "notes": "controller: 10Nm+ respects"},
  {"kind": "gm", "t": "Full Cockpit", "tier": "Advanced", "concept": "full immersion", "mechanism": "seat + panels + controls", "parts": ["cockpit"], "build": "build", "time": "100h", "level": "advanced", "safety": "none", "notes": "controller: start with seat"},
  {"kind": "gm", "t": "Motion Platform (2DOF)", "tier": "Advanced", "concept": "feel the road", "mechanism": "2 actuators tilt seat", "parts": ["platform"], "build": "build", "time": "80h", "level": "advanced", "safety": "pinch, power", "notes": "controller: e-stop mandatory"},
  {"kind": "gm", "t": "Haptic Gloves", "tier": "Advanced", "concept": "touch VR", "mechanism": "vibration + force per finger", "parts": ["gloves"], "build": "build", "time": "60h", "level": "advanced", "safety": "low-voltage", "notes": "controller: research-grade"},
  {"kind": "gm", "t": "Eye-Tracking Aim", "tier": "Advanced", "concept": "aim with eyes", "mechanism": "tracker + software", "parts": ["tracker"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "controller: dwell-click option"},
  {"kind": "gm", "t": "Brain-Control Switch", "tier": "Advanced", "concept": "hands-free control", "mechanism": "EEG + simple commands", "parts": ["eeg"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "controller: 2 commands reliably"},
  {"kind": "gm", "t": "Full Arcade Cabinet", "tier": "Advanced", "concept": "arcade at home", "mechanism": "cabinet + controls + screen", "parts": ["cabinet"], "build": "build", "time": "80h", "level": "advanced", "safety": "electrical safety", "notes": "controller: 6-button layout standard"},
  {"kind": "gm", "t": "Robot Arm Controller", "tier": "Advanced", "concept": "control arms", "mechanism": "6DOF pendant", "parts": ["pendant"], "build": "build", "time": "40h", "level": "advanced", "safety": "low-voltage", "notes": "controller: deadman switch"},
  {"kind": "gm", "t": "Exoskeleton Controller", "tier": "Advanced", "concept": "assist control", "mechanism": "intent + force sensing", "parts": ["exo"], "build": "build", "time": "100h", "level": "advanced", "safety": "pro", "notes": "controller: safety-rated"},
  {"kind": "gm", "t": "Musical Instrument (New)", "tier": "Advanced", "concept": "new sounds", "mechanism": "novel gestural controller", "parts": ["instrument"], "build": "build", "time": "80h", "level": "advanced", "safety": "low-voltage", "notes": "controller: playability first"},
  {"kind": "gm", "t": "Industrial Pendant", "tier": "Advanced", "concept": "machine control", "mechanism": "2-hand + e-stop pendant", "parts": ["pendant"], "build": "build", "time": "40h", "level": "advanced", "safety": "pro", "notes": "controller: standards apply"},
  {"kind": "gm", "t": "Orchestral Controller", "tier": "Advanced", "concept": "conduct music", "mechanism": "baton + sensors", "parts": ["baton"], "build": "build", "time": "40h", "level": "advanced", "safety": "low-voltage", "notes": "controller: gesture = dynamics"}
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

