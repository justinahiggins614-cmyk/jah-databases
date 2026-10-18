(function(){'use strict';
/* JAH The Giant Gadget Database — real working generator, jahdb-db-giant-gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GGS-";
var SLUG="db-giant-gadget";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Giant Newton Cradle", "tier": "Foundations", "concept": "desktop toy, room scale", "mechanism": "5 bowling balls on cables", "parts": ["balls", "cables"], "build": "hang", "time": "12h", "level": "beginner", "safety": "heavy — secure mount", "notes": "wonder: momentum you can feel"},
  {"kind": "gm", "t": "Oversized Jenga", "tier": "Foundations", "concept": "party classic, giant", "mechanism": "2x4 blocks stacked 3x3", "parts": ["wood"], "build": "cut", "time": "6h", "level": "beginner", "safety": "saw safety", "notes": "wonder: the crash is the game"},
  {"kind": "gm", "t": "Giant Bubble Wands", "tier": "Foundations", "concept": "tiny bubbles disappoint", "mechanism": "1m wands + pro solution", "parts": ["wands"], "build": "mix", "time": "3h", "level": "beginner", "safety": "none", "notes": "wonder: car-sized bubbles"},
  {"kind": "gm", "t": "Big Abacus", "tier": "Foundations", "concept": "math you can climb", "mechanism": "2m frame, sliding balls", "parts": ["wood"], "build": "build", "time": "10h", "level": "beginner", "safety": "none", "notes": "wonder: arithmetic at playground scale"},
  {"kind": "gm", "t": "Giant Dominoes", "tier": "Foundations", "concept": "table dominoes tip", "mechanism": "foam bricks topple satisfyingly", "parts": ["foam"], "build": "cut", "time": "6h", "level": "beginner", "safety": "none", "notes": "wonder: chain reactions walk"},
  {"kind": "gm", "t": "Oversized Chess", "tier": "Foundations", "concept": "chess feels abstract", "mechanism": "3ft pieces on lawn board", "parts": ["pieces"], "build": "carve", "time": "20h", "level": "beginner", "safety": "none", "notes": "wonder: strategy you step through"},
  {"kind": "gm", "t": "Giant Lite-Brite", "tier": "Foundations", "concept": "tiny pegs frustrate", "mechanism": "1m pegboard + glowing pegs", "parts": ["board", "LEDs"], "build": "build", "time": "16h", "level": "beginner", "safety": "low-voltage", "notes": "wonder: pixel art walk-up"},
  {"kind": "gm", "t": "Big Marble Run", "tier": "Foundations", "concept": "desk toy limits", "mechanism": "gutter tracks down a wall", "parts": ["gutters"], "build": "mount", "time": "12h", "level": "beginner", "safety": "secure mount", "notes": "wonder: 10-second runs"},
  {"kind": "gm", "t": "Giant Etch-a-Sketch", "tier": "Foundations", "concept": "tiny knobs cramp", "mechanism": "1m screen, big knobs", "parts": ["screen"], "build": "build", "time": "20h", "level": "beginner", "safety": "none", "notes": "wonder: drawing at arm scale"},
  {"kind": "gm", "t": "Oversized Hourglass", "tier": "Foundations", "concept": "time feels abstract", "mechanism": "2m timers with sand", "parts": ["glass", "sand"], "build": "build", "time": "16h", "level": "beginner", "safety": "glass safety", "notes": "wonder: watch an hour fall"},
  {"kind": "gm", "t": "Giant Calculator", "tier": "Foundations", "concept": "math is invisible", "mechanism": "1m buttons, real logic", "parts": ["buttons"], "build": "wire", "time": "24h", "level": "beginner", "safety": "low-voltage", "notes": "wonder: punch numbers with fists"},
  {"kind": "gm", "t": "Human-Size Hamster Wheel", "tier": "Compounded", "concept": "energy to burn", "mechanism": "3m wheel, human power", "parts": ["wheel"], "build": "build", "time": "40h", "level": "intermediate", "safety": "fall safety", "notes": "wonder: walk to nowhere, joyfully"},
  {"kind": "gm", "t": "Giant Periscope", "tier": "Compounded", "concept": "see over fences", "mechanism": "2m mirrors at 45 degrees", "parts": ["mirrors"], "build": "build", "time": "10h", "level": "intermediate", "safety": "mirror edges", "notes": "wonder: submarine vision standing"},
  {"kind": "gm", "t": "Big Wind Chimes", "tier": "Compounded", "concept": "tiny chimes whisper", "mechanism": "2m aluminum tubes sing", "parts": ["tubes"], "build": "hang", "time": "12h", "level": "intermediate", "safety": "secure hang", "notes": "wonder: bass notes from breeze"},
  {"kind": "gm", "t": "Oversized Music Box", "tier": "Compounded", "concept": "music boxes whisper", "mechanism": "1m cylinder plays loud", "parts": ["drum"], "build": "build", "time": "30h", "level": "intermediate", "safety": "none", "notes": "wonder: mechanical music room-filling"},
  {"kind": "gm", "t": "Giant Kaleidoscope", "tier": "Compounded", "concept": "handheld limits", "mechanism": "walk-in mirror triangle", "parts": ["mirrors"], "build": "build", "time": "24h", "level": "intermediate", "safety": "mirror safety", "notes": "wonder: stand inside the pattern"},
  {"kind": "gm", "t": "Big Zoetrope", "tier": "Compounded", "concept": "animation needs screens", "mechanism": "2m spinning drum animates", "parts": ["drum"], "build": "build", "time": "20h", "level": "intermediate", "safety": "spin safety", "notes": "wonder: movies before film"},
  {"kind": "gm", "t": "Giant Slinky Stairs", "tier": "Compounded", "concept": "desk slinky small", "mechanism": "6ft spring walks stairs", "parts": ["spring"], "build": "build", "time": "16h", "level": "intermediate", "safety": "pinch safety", "notes": "wonder: physics at stair scale"},
  {"kind": "gm", "t": "Oversized Plinko", "tier": "Compounded", "concept": "TV game, real", "mechanism": "2m board, chip drops", "parts": ["board"], "build": "build", "time": "16h", "level": "intermediate", "safety": "none", "notes": "wonder: probability you can watch"},
  {"kind": "gm", "t": "Big Pinball", "tier": "Compounded", "concept": "arcade nostalgia", "mechanism": "2m playfield, real flippers", "parts": ["playfield"], "build": "build", "time": "40h", "level": "intermediate", "safety": "none", "notes": "wonder: body-english encouraged"},
  {"kind": "gm", "t": "Giant Spirograph", "tier": "Compounded", "concept": "tiny gears slip", "mechanism": "1m rings draw murals", "parts": ["rings"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "wonder: math as mural"},
  {"kind": "gm", "t": "Human Sundial", "tier": "Compounded", "concept": "time is abstract", "mechanism": "your shadow tells time", "parts": ["plaza"], "build": "paint", "time": "8h", "level": "intermediate", "safety": "none", "notes": "wonder: become the gnomon"},
  {"kind": "gm", "t": "World's Largest Rubber Band Ball", "tier": "Advanced", "concept": "office toy record", "mechanism": "millions of bands, crane needed", "parts": ["bands"], "build": "wrap", "time": "200h", "level": "advanced", "safety": "structural — pro", "notes": "wonder: 4 tons of bounce"},
  {"kind": "gm", "t": "Giant Trebuchet", "tier": "Advanced", "concept": "pumpkins need flying", "mechanism": "20m siege engine throws far", "parts": ["timber"], "build": "build", "time": "100h", "level": "advanced", "safety": "range safety — pro", "notes": "wonder: medieval aerospace"},
  {"kind": "gm", "t": "Big Tesla Coil", "tier": "Advanced", "concept": "electricity wants drama", "mechanism": "3m sparks sing music", "parts": ["coil"], "build": "build", "time": "80h", "level": "advanced", "safety": "HIGH VOLTAGE — expert only", "notes": "wonder: lightning conducts music"},
  {"kind": "gm", "t": "Giant Camera Obscura", "tier": "Advanced", "concept": "photography's ancestor", "mechanism": "room-size pinhole projects world", "parts": ["lens"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "wonder: stand inside a camera"},
  {"kind": "gm", "t": "Oversized Pipe Organ", "tier": "Advanced", "concept": "organs are buildings", "mechanism": "shipping-container pipes play", "parts": ["pipes"], "build": "build", "time": "100h", "level": "advanced", "safety": "none", "notes": "wonder: music you feel in ribs"},
  {"kind": "gm", "t": "Giant Pendulum Wave", "tier": "Advanced", "concept": "physics is beautiful", "mechanism": "16 pendulums dance patterns", "parts": ["pendulums"], "build": "hang", "time": "24h", "level": "advanced", "safety": "secure mount", "notes": "wonder: chaos resolving to order"},
  {"kind": "gm", "t": "Big Domino Computer", "tier": "Advanced", "concept": "computing without chips", "mechanism": "10,000 dominoes do logic", "parts": ["dominoes"], "build": "set", "time": "100h", "level": "advanced", "safety": "none", "notes": "wonder: AND gates that fall over"},
  {"kind": "gm", "t": "Human-Powered Roller Coaster", "tier": "Advanced", "concept": "coasters need hills", "mechanism": "bike-powered backyard coaster", "parts": ["track"], "build": "build", "time": "200h", "level": "advanced", "safety": "engineer review", "notes": "wonder: pedal to thrill"},
  {"kind": "gm", "t": "Giant Xylophone", "tier": "Advanced", "concept": "music you can walk", "mechanism": "2m bars tuned pentatonic", "parts": ["bars"], "build": "tune", "time": "30h", "level": "advanced", "safety": "none", "notes": "wonder: play with mallets, dance"},
  {"kind": "gm", "t": "Oversized Typewriter", "tier": "Advanced", "concept": "typing is invisible", "mechanism": "1m keys clack real letters", "parts": ["keys"], "build": "build", "time": "60h", "level": "advanced", "safety": "none", "notes": "wonder: write a novel loudly"},
  {"kind": "gm", "t": "Giant Mousetrap (Car)", "tier": "Advanced", "concept": "cartoon physics real", "mechanism": "car-size trap snaps safely", "parts": ["trap"], "build": "build", "time": "40h", "level": "advanced", "safety": "snap safety — pro", "notes": "wonder: the snap heard 'round the block"},
  {"kind": "gm", "t": "Giant Abacus (Outdoor)", "tier": "Advanced", "concept": "math playground", "mechanism": "2m frame + balls", "parts": ["abacus"], "build": "build", "time": "30h", "level": "advanced", "safety": "secure", "notes": "wonder: climbable arithmetic"}
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

