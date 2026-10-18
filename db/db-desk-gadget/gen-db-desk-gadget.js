(function(){'use strict';
/* JAH The Desk Gadget Database — real working generator, jahdb-db-desk-gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DG-";
var SLUG="db-desk-gadget";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "The Perfect Pen Cup", "tier": "Foundations", "concept": "pens scatter", "mechanism": "weighted cup + phone slot", "parts": ["cup"], "build": "make", "time": "2h", "level": "beginner", "safety": "none", "notes": "gadget: weight prevents tip"},
  {"kind": "gm", "t": "Desk Clock (Analog)", "tier": "Foundations", "concept": "time checks break flow", "mechanism": "silent sweep analog", "parts": ["clock"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "gadget: silent sweep, no tick"},
  {"kind": "gm", "t": "Cable Tidy Box", "tier": "Foundations", "concept": "cable spaghetti", "mechanism": "box hides power strip", "parts": ["box"], "build": "make", "time": "2h", "level": "beginner", "safety": "ventilation", "notes": "gadget: vent the box — heat"},
  {"kind": "gm", "t": "Monitor Riser", "tier": "Foundations", "concept": "necks crane", "mechanism": "riser + storage", "parts": ["wood"], "build": "build", "time": "4h", "level": "beginner", "safety": "none", "notes": "gadget: eye level = top third"},
  {"kind": "gm", "t": "Desk Plant (Unkillable)", "tier": "Foundations", "concept": "desks need life", "mechanism": "pothos + self-watering pot", "parts": ["plant"], "build": "pot", "time": "1h", "level": "beginner", "safety": "none", "notes": "gadget: pothos forgives"},
  {"kind": "gm", "t": "Sticky Note Dispenser", "tier": "Foundations", "concept": "notes curl", "mechanism": "weighted pop-up dispenser", "parts": ["dispenser"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "gadget: one-hand pull"},
  {"kind": "gm", "t": "Desk Headphone Stand", "tier": "Foundations", "concept": "headphones vanish", "mechanism": "stand + cable wrap", "parts": ["stand"], "build": "build", "time": "3h", "level": "beginner", "safety": "none", "notes": "gadget: hang, don't fold"},
  {"kind": "gm", "t": "Desk Fan (USB)", "tier": "Foundations", "concept": "stuffy afternoons", "mechanism": "quiet USB fan", "parts": ["fan"], "build": "build", "time": "4h", "level": "beginner", "safety": "low-voltage", "notes": "gadget: brushless = quiet"},
  {"kind": "gm", "t": "Mug Warmer", "tier": "Foundations", "concept": "coffee cools", "mechanism": "USB warmer plate", "parts": ["warmer"], "build": "build", "time": "4h", "level": "beginner", "safety": "low-voltage", "notes": "gadget: 55C is the sweet spot"},
  {"kind": "gm", "t": "Paperweight (Pretty)", "tier": "Foundations", "concept": "papers fly", "mechanism": "heavy + beautiful object", "parts": ["stone"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "gadget: 300g+ actually holds"},
  {"kind": "gm", "t": "Desk Organizer Tray", "tier": "Foundations", "concept": "drawers chaos", "mechanism": "tiered tray system", "parts": ["tray"], "build": "make", "time": "3h", "level": "beginner", "safety": "none", "notes": "gadget: vertical beats flat"},
  {"kind": "gm", "t": "Mechanical Keyboard", "tier": "Compounded", "concept": "typing all day", "mechanism": "hot-swap + tactile switches", "parts": ["keyboard"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "gadget: try switches first"},
  {"kind": "gm", "t": "Desk Mat (Extended)", "tier": "Compounded", "concept": "mouse skips", "mechanism": "900mm mat, stitched edge", "parts": ["mat"], "build": "study", "time": "1h", "level": "intermediate", "safety": "none", "notes": "gadget: 4mm thick, washable"},
  {"kind": "gm", "t": "Monitor Light Bar", "tier": "Compounded", "concept": "glare strains", "mechanism": "asymmetric bar, no screen glare", "parts": ["bar"], "build": "install", "time": "2h", "level": "intermediate", "safety": "low-voltage", "notes": "gadget: light the desk, not screen"},
  {"kind": "gm", "t": "Ergonomic Footrest", "tier": "Compounded", "concept": "feet dangle", "mechanism": "angled + rocking footrest", "parts": ["rest"], "build": "build", "time": "4h", "level": "intermediate", "safety": "none", "notes": "gadget: rock to circulate"},
  {"kind": "gm", "t": "Desk Shelf (Riser+)", "tier": "Compounded", "concept": "monitors low, desk full", "mechanism": "shelf + storage cubbies", "parts": ["shelf"], "build": "build", "time": "6h", "level": "intermediate", "safety": "none", "notes": "gadget: 2-tier doubles space"},
  {"kind": "gm", "t": "Whiteboard (Desk)", "tier": "Compounded", "concept": "ideas evaporate", "mechanism": "glass desktop board", "parts": ["board"], "build": "install", "time": "3h", "level": "intermediate", "safety": "none", "notes": "gadget: glass wipes forever"},
  {"kind": "gm", "t": "Cable Spine", "tier": "Compounded", "concept": "cables dangle", "mechanism": "spine channels to floor", "parts": ["spine"], "build": "install", "time": "2h", "level": "intermediate", "safety": "none", "notes": "gadget: sit-stand needs slack"},
  {"kind": "gm", "t": "Desk Drawer Unit", "tier": "Compounded", "concept": "supplies scatter", "mechanism": "3-drawer + lock unit", "parts": ["drawers"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "gadget: lock the bottom one"},
  {"kind": "gm", "t": "Plant Light (Desk)", "tier": "Compounded", "concept": "plants stretch", "mechanism": "full-spectrum clip light", "parts": ["light"], "build": "install", "time": "2h", "level": "intermediate", "safety": "low-voltage", "notes": "gadget: 12h timer"},
  {"kind": "gm", "t": "Noise Machine", "tier": "Compounded", "concept": "office hum", "mechanism": "brown noise + timer", "parts": ["speaker"], "build": "build", "time": "4h", "level": "intermediate", "safety": "low-voltage", "notes": "gadget: brown > white for focus"},
  {"kind": "gm", "t": "Desk Exercise Kit", "tier": "Compounded", "concept": "sitting kills", "mechanism": "bands + pedal exerciser", "parts": ["kit"], "build": "use", "time": "2h", "level": "intermediate", "safety": "none", "notes": "gadget: pedals under desk"},
  {"kind": "gm", "t": "Sit-Stand Converter", "tier": "Advanced", "concept": "sitting all day", "mechanism": "gas-spring riser platform", "parts": ["converter"], "build": "build", "time": "12h", "level": "advanced", "safety": "pinch safety", "notes": "gadget: 15kg rating minimum"},
  {"kind": "gm", "t": "Triple Monitor Arm", "tier": "Advanced", "concept": "screens crowd", "mechanism": "pole + 3 arms", "parts": ["arm"], "build": "install", "time": "6h", "level": "advanced", "safety": "clamp to solid desk", "notes": "gadget: align bezels"},
  {"kind": "gm", "t": "Desk PC Build", "tier": "Advanced", "concept": "tower hogs floor", "mechanism": "desk-integrated PC", "parts": ["PC"], "build": "build", "time": "20h", "level": "advanced", "safety": "electrical safety", "notes": "gadget: airflow planned"},
  {"kind": "gm", "t": "Acoustic Panels (Desk)", "tier": "Advanced", "concept": "echo fatigues", "mechanism": "petals absorb reflections", "parts": ["panels"], "build": "mount", "time": "8h", "level": "advanced", "safety": "none", "notes": "gadget: behind monitor first"},
  {"kind": "gm", "t": "Smart Desk Controller", "tier": "Advanced", "concept": "forget to stand", "mechanism": "reminders + height presets", "parts": ["controller"], "build": "build", "time": "12h", "level": "advanced", "safety": "low-voltage", "notes": "gadget: gentle nudges"},
  {"kind": "gm", "t": "Desk Garden (Hydro)", "tier": "Advanced", "concept": "green focus", "mechanism": "NFT herb wall", "parts": ["system"], "build": "build", "time": "16h", "level": "advanced", "safety": "water + electric safety", "notes": "gadget: basil in weeks"},
  {"kind": "gm", "t": "Cable-Free Desk", "tier": "Advanced", "concept": "cables everywhere", "mechanism": "wireless everything + dock", "parts": ["dock"], "build": "build", "time": "10h", "level": "advanced", "safety": "none", "notes": "gadget: one cable to rule them"},
  {"kind": "gm", "t": "Standing Desk (DIY)", "tier": "Advanced", "concept": "retail costs", "mechanism": "electric legs + top", "parts": ["desk"], "build": "build", "time": "16h", "level": "advanced", "safety": "pinch safety", "notes": "gadget: 3-stage legs stable"},
  {"kind": "gm", "t": "Desk Aquarium (Nano)", "tier": "Advanced", "concept": "calm focus", "mechanism": "5gal + betta + plants", "parts": ["tank"], "build": "build", "time": "10h", "level": "advanced", "safety": "water + electric GFCI", "notes": "gadget: cycle before fish"},
  {"kind": "gm", "t": "Focus Timer (Physical)", "tier": "Advanced", "concept": "phone distracts", "mechanism": "mechanical 25-min timer", "parts": ["timer"], "build": "build", "time": "6h", "level": "advanced", "safety": "none", "notes": "gadget: twist = commitment"},
  {"kind": "gm", "t": "Desk Command Center", "tier": "Advanced", "concept": "everything scattered", "mechanism": "pegboard + power + light", "parts": ["board"], "build": "build", "time": "12h", "level": "advanced", "safety": "low-voltage", "notes": "gadget: zones for tools"},
  {"kind": "gm", "t": "Desk Treadmill (Under)", "tier": "Advanced", "concept": "walk while working", "mechanism": "slim treadmill", "parts": ["treadmill"], "build": "study", "time": "4h", "level": "advanced", "safety": "none", "notes": "gadget: 2mph max typing"}
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

