(function(){'use strict';
/* JAH The Innovative Mouse Database — real working generator, jahdb-db-innovative-mouse-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IM-";
var SLUG="db-innovative-mouse";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Vertical Mouse", "tier": "Foundations", "concept": "wrists pronate painfully", "mechanism": "handshake grip keeps neutral", "parts": ["mouse"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "innovation: rotate the hand, not the wrist"},
  {"kind": "gm", "t": "Trackball", "tier": "Foundations", "concept": "desks are small", "mechanism": "ball moves, hand stays", "parts": ["ball"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "innovation: fingers do the moving"},
  {"kind": "gm", "t": "The Tiny Travel Mouse", "tier": "Foundations", "concept": "bags are full", "mechanism": "60% size, full function", "parts": ["mouse"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "innovation: small but not cramped"},
  {"kind": "gm", "t": "Silent Click Mouse", "tier": "Foundations", "concept": "clicks annoy", "mechanism": "dampened switches hush", "parts": ["mouse"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "innovation: 90% quieter"},
  {"kind": "gm", "t": "The Left-Handed Mouse", "tier": "Foundations", "concept": "lefties adapt", "mechanism": "true mirror design", "parts": ["mouse"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "innovation: not just mirrored buttons"},
  {"kind": "gm", "t": "Pen Mouse", "tier": "Foundations", "concept": "drawing with brick", "mechanism": "pen grip + absolute positioning", "parts": ["pen"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "innovation: hold like you write"},
  {"kind": "gm", "t": "The Gyro Air Mouse", "tier": "Foundations", "concept": "couch computing", "mechanism": "IMU moves cursor in air", "parts": ["mouse"], "build": "build", "time": "10h", "level": "beginner", "safety": "low-voltage", "notes": "innovation: point at the screen"},
  {"kind": "gm", "t": "Foot Mouse", "tier": "Foundations", "concept": "hands busy", "mechanism": "feet click and move", "parts": ["pedals"], "build": "build", "time": "12h", "level": "beginner", "safety": "none", "notes": "innovation: accessibility win"},
  {"kind": "gm", "t": "The Ring Mouse", "tier": "Foundations", "concept": "desks optional", "mechanism": "ring + thumb track", "parts": ["ring"], "build": "build", "time": "12h", "level": "beginner", "safety": "low-voltage", "notes": "innovation: wearable pointing"},
  {"kind": "gm", "t": "Eye-Tracking Mouse", "tier": "Foundations", "concept": "hands-free need", "mechanism": "camera follows gaze", "parts": ["tracker"], "build": "build", "time": "16h", "level": "beginner", "safety": "none", "notes": "innovation: look to click (dwell)"},
  {"kind": "gm", "t": "Voice Mouse", "tier": "Foundations", "concept": "RSI limits", "mechanism": "voice moves cursor", "parts": ["software"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "innovation: grid + commands"},
  {"kind": "gm", "t": "The Modular Mouse", "tier": "Compounded", "concept": "hands differ", "mechanism": "shells swap by size", "parts": ["mouse"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "innovation: fit like shoes"},
  {"kind": "gm", "t": "Adjustable Angle Mouse", "tier": "Compounded", "concept": "one angle fits none", "mechanism": "tilt 20-60 degrees", "parts": ["mouse"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "innovation: dial your pronation"},
  {"kind": "gm", "t": "The Joystick Mouse", "tier": "Compounded", "concept": "precision tasks", "mechanism": "stick + buttons hybrid", "parts": ["stick"], "build": "build", "time": "16h", "level": "intermediate", "safety": "low-voltage", "notes": "innovation: CAD loves sticks"},
  {"kind": "gm", "t": "Haptic Mouse", "tier": "Compounded", "concept": "feedback flat", "mechanism": "vibration textures surfaces", "parts": ["mouse"], "build": "build", "time": "20h", "level": "intermediate", "safety": "low-voltage", "notes": "innovation: feel the UI"},
  {"kind": "gm", "t": "The Split Mouse", "tier": "Compounded", "concept": "both hands?", "mechanism": "two halves, one cursor", "parts": ["halves"], "build": "build", "time": "24h", "level": "intermediate", "safety": "low-voltage", "notes": "innovation: ambidextrous pointing"},
  {"kind": "gm", "t": "3D Mouse (Space)", "tier": "Compounded", "concept": "3D navigation hard", "mechanism": "6DOF puck for CAD", "parts": ["puck"], "build": "build", "time": "20h", "level": "intermediate", "safety": "low-voltage", "notes": "innovation: push, pull, twist"},
  {"kind": "gm", "t": "The Brain Mouse (Concept)", "tier": "Compounded", "concept": "no movement possible", "mechanism": "EEG selects + dwells", "parts": ["eeg"], "build": "study", "time": "30h", "level": "intermediate", "safety": "none", "notes": "innovation: slowest but most profound"},
  {"kind": "gm", "t": "Gesture Mouse", "tier": "Compounded", "concept": "touch is limited", "mechanism": "camera reads hand gestures", "parts": ["camera"], "build": "build", "time": "20h", "level": "intermediate", "safety": "none", "notes": "innovation: pinch to click"},
  {"kind": "gm", "t": "The Roller Mouse", "tier": "Compounded", "concept": "reach strains", "mechanism": "bar below keyboard rolls", "parts": ["bar"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "innovation: never reach for mouse"},
  {"kind": "gm", "t": "Tongue Mouse (Assistive)", "tier": "Compounded", "concept": "no limb control", "mechanism": "tongue magnet + sensors", "parts": ["sensor"], "build": "build", "time": "30h", "level": "intermediate", "safety": "medical pro", "notes": "innovation: assistive tech frontier"},
  {"kind": "gm", "t": "The Exoskeleton Mouse", "tier": "Compounded", "concept": "weak grip", "mechanism": "powered grip assist", "parts": ["exo"], "build": "build", "time": "40h", "level": "intermediate", "safety": "pro", "notes": "innovation: strength where needed"},
  {"kind": "gm", "t": "Neuralink-Style (Concept)", "tier": "Advanced", "concept": "thought to cursor", "mechanism": "implanted electrodes", "parts": ["implant"], "build": "study", "time": "80h", "level": "advanced", "safety": "medical", "notes": "innovation: the far horizon"},
  {"kind": "gm", "t": "Full-Hand VR Mouse", "tier": "Advanced", "concept": "VR needs hands", "mechanism": "tracked glove + haptics", "parts": ["glove"], "build": "build", "time": "60h", "level": "advanced", "safety": "low-voltage", "notes": "innovation: grab the data"},
  {"kind": "gm", "t": "The Shapeshifting Mouse", "tier": "Advanced", "concept": "tasks differ", "mechanism": "surface morphs by app", "parts": ["mouse"], "build": "build", "time": "60h", "level": "advanced", "safety": "low-voltage", "notes": "innovation: flat for web, tall for CAD"},
  {"kind": "gm", "t": "Swarm Mice (Concept)", "tier": "Advanced", "concept": "one cursor limits", "mechanism": "many tiny robots collaborate", "parts": ["robots"], "build": "study", "time": "80h", "level": "advanced", "safety": "none", "notes": "innovation: pointing as swarm"},
  {"kind": "gm", "t": "The Projected Mouse", "tier": "Advanced", "concept": "hardware optional", "mechanism": "laser projection + sensing", "parts": ["projector"], "build": "build", "time": "40h", "level": "advanced", "safety": "laser safety", "notes": "innovation: no mouse at all"},
  {"kind": "gm", "t": "DNA Data Mouse (Whimsy)", "tier": "Advanced", "concept": "storage everywhere", "mechanism": "DNA writes data (slowly)", "parts": ["dna"], "build": "study", "time": "80h", "level": "advanced", "safety": "lab pro", "notes": "innovation: the densest storage"},
  {"kind": "gm", "t": "Quantum Mouse (Joke+Real)", "tier": "Advanced", "concept": "uncertainty!", "mechanism": "superposition cursor (concept)", "parts": ["thought"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "innovation: it's both clicked and not"},
  {"kind": "gm", "t": "The Empathy Mouse", "tier": "Advanced", "concept": "frustration unseen", "mechanism": "grip + temp sense stress", "parts": ["mouse"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "innovation: UI adapts to you"},
  {"kind": "gm", "t": "Holographic Mouse", "tier": "Advanced", "concept": "screens flat", "mechanism": "volumetric cursor control", "parts": ["hologram"], "build": "build", "time": "80h", "level": "advanced", "safety": "none", "notes": "innovation: point in 3D space"},
  {"kind": "gm", "t": "The Final Mouse (Ergo)", "tier": "Advanced", "concept": "perfect fit", "mechanism": "sculpted to your hand scan", "parts": ["mouse"], "build": "build", "time": "40h", "level": "advanced", "safety": "3D print 6-10h estimate", "notes": "innovation: scan, print, point — print time estimate 6-10h at 0.15mm"},
  {"kind": "gm", "t": "Open-Source Mouse", "tier": "Advanced", "concept": "mice are closed", "mechanism": "fully hackable design", "parts": ["mouse"], "build": "build", "time": "40h", "level": "advanced", "safety": "low-voltage", "notes": "innovation: repair and remix"},
  {"kind": "gm", "t": "The Foot Pedal Mouse", "tier": "Advanced", "concept": "hands-free click", "mechanism": "pedals + head tracking", "parts": ["pedals"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "innovation: feet click, head moves"}
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

