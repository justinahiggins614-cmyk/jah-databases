(function(){'use strict';
/* JAH The Stop-Motion Creator Database — real working generator, jahdb-gen-stop-motion-creator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMCS-";
var SLUG="gen-stop-motion-creator";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "First Flip: 24 Frames", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["phone", "1", 0.0], ["app", "1", 5.0], ["clay", "1", 8.0]], "tools": ["none"], "steps": ["storyboard 3 shots", "shoot 24 frames", "play 12fps", "share"], "time": "3h", "level": "beginner", "safety": "12fps = 24 frames for 2 seconds — plan small"},
  {"kind": "diy", "t": "Paper Cut-Out Short", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 5.0], ["app", "1", 0.0], ["light", "1", 10.0]], "tools": ["none"], "steps": ["cut characters", "move 5mm/frame", "shoot", "edit"], "time": "4h", "level": "beginner", "safety": "lock camera — tripod or stack of books"},
  {"kind": "diy", "t": "Clay Ball Bounce", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["clay", "1", 8.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["ball squash/stretch", "12 frames", "play", "tweak"], "time": "2h", "level": "beginner", "safety": "onion skin on — see last frame"},
  {"kind": "diy", "t": "Object Animation: Toys Walk", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["toys", "1", 0.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["tiny moves", "shoot", "play", "laugh"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Pixilation: Human Puppet", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["friends", "1", 0.0], ["app", "1", 0.0], ["tripod", "1", 15.0]], "tools": ["tripod"], "steps": ["pose increments", "shoot", "play", "edit"], "time": "4h", "level": "beginner", "safety": "plan moves — humans tire"},
  {"kind": "diy", "t": "Whiteboard Animation", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["board", "1", 15.0], ["markers", "1", 8.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["draw increment", "shoot", "erase cycle", "edit"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Food Animation", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["snacks", "1", 8.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["move bites", "shoot", "play", "eat cast"], "time": "2h", "level": "beginner", "safety": "food safety — shoot fast, refrigerate"},
  {"kind": "diy", "t": "LEGO Walk Cycle", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["lego", "1", 0.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["8-frame walk", "shoot", "loop", "share"], "time": "3h", "level": "beginner", "safety": "tape minifig feet — wobble ruins takes"},
  {"kind": "diy", "t": "Sand Animation", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["sand", "1", 5.0], ["lightbox", "1", 20.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["draw in sand", "shoot", "morph", "edit"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Chalk Walk", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["chalk", "1", 5.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["draw frames", "shoot each", "play", "wash"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Sticky Note Flip", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["notes", "1", 5.0], ["pen", "1", 3.0]], "tools": ["none"], "steps": ["draw sequence", "flip", "film flip", "share"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Time-Lapse Build", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["project", "1", 0.0], ["app", "1", 0.0], ["tripod", "1", 15.0]], "tools": ["tripod"], "steps": ["frame shot", "interval", "shoot", "compile"], "time": "3h", "level": "beginner", "safety": "lock exposure and focus"},
  {"kind": "diy", "t": "Armature Puppet Build", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wire", "1", 8.0], ["foam", "1", 10.0], ["clay", "1", 12.0], ["paint", "1", 8.0]], "tools": ["pliers"], "steps": ["wire skeleton", "foam muscle", "clay skin", "paint"], "time": "10h", "level": "intermediate", "safety": "tie-downs in feet — essential"},
  {"kind": "diy", "t": "Set Building: Bedroom", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foamcore", "1", 15.0], ["paint", "1", 10.0], ["props", "1", 12.0]], "tools": ["knife"], "steps": ["scale plan", "walls", "props", "light"], "time": "10h", "level": "intermediate", "safety": "scale consistency — measure everything"},
  {"kind": "diy", "t": "Lip Sync Basics", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["puppet", "1", 0.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["record dialogue", "break phonemes", "mouth shapes", "shoot"], "time": "8h", "level": "intermediate", "safety": "8 mouth shapes cover most speech"},
  {"kind": "diy", "t": "Walk Cycle Refined", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["puppet", "1", 0.0]], "tools": ["none"], "steps": ["contact/down/passing/up", "ease", "shoot", "review"], "time": "6h", "level": "intermediate", "safety": "reference video yourself walking"},
  {"kind": "diy", "t": "Lighting for Mood", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["lamps", "3", 30.0], ["diffusion", "1", 10.0]], "tools": ["none"], "steps": ["key/fill/back", "diffuse", "test", "shoot"], "time": "4h", "level": "intermediate", "safety": "LED cool — hot lights melt clay"},
  {"kind": "diy", "t": "Camera Moves (Pan)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["slider", "1", 25.0], ["app", "1", 0.0]], "tools": ["slider"], "steps": ["plan move", "mark increments", "shoot", "edit"], "time": "6h", "level": "intermediate", "safety": "move camera, not set — fewer accidents"},
  {"kind": "diy", "t": "Replacement Faces", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["clay", "1", 10.0], ["molds", "1", 8.0]], "tools": ["none"], "steps": ["sculpt 6 mouths", "bake", "swap per frame", "shoot"], "time": "10h", "level": "intermediate", "safety": "bake all at once — color match"},
  {"kind": "diy", "t": "Flying Rig", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wire", "1", 8.0], ["stand", "1", 12.0]], "tools": ["none"], "steps": ["rig puppet", "shoot", "paint out wire", "edit"], "time": "8h", "level": "intermediate", "safety": "paint-out in editing — plan background"},
  {"kind": "diy", "t": "Title Cards That Move", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 5.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["design cards", "animate in", "time", "edit"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Green Screen Mini", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["green paper", "1", 8.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["green backdrop", "shoot", "key out", "composite"], "time": "5h", "level": "intermediate", "safety": "even lighting on green — no shadows"},
  {"kind": "diy", "t": "Voice-Over Recording", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["mic", "1", 25.0], ["script", "1", 0.0], ["software", "1", 0.0]], "tools": ["none"], "steps": ["write script", "record clean", "edit", "sync"], "time": "4h", "level": "intermediate", "safety": "closet recording — clothes damp echo"},
  {"kind": "diy", "t": "Water Effects (Gel)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["gel", "1", 12.0], ["app", "1", 0.0]], "tools": ["none"], "steps": ["gel water", "animate ripples", "shoot", "edit"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Crowd Scene", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["puppets", "5", 30.0], ["set", "1", 15.0]], "tools": ["none"], "steps": ["choreograph", "shoot layers", "composite", "edit"], "time": "12h", "level": "intermediate", "safety": "shoot in passes — sanity saver"},
  {"kind": "diy", "t": "Sound Design", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["mic", "1", 30.0], ["software", "1", 0.0]], "tools": ["none"], "steps": ["record foley", "score", "mix", "sync"], "time": "8h", "level": "intermediate", "safety": "royalty-free music only"},
  {"kind": "diy", "t": "Feature Storyboard", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 10.0]], "tools": ["none"], "steps": ["90-page story", "boards", "animatic", "revise"], "time": "40h", "level": "advanced", "safety": "story is everything — rewrite freely"},
  {"kind": "diy", "t": "Multi-Puppet Dialogue", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["puppets", "3", 60.0], ["set", "1", 30.0]], "tools": ["none"], "steps": ["script", "block", "shoot coverage", "edit"], "time": "30h", "level": "advanced", "safety": "shoot master first, then coverage"},
  {"kind": "diy", "t": "Complex Set: Street", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 80.0]], "tools": ["saw"], "steps": ["build street", "dress shops", "light", "shoot"], "time": "40h", "level": "advanced", "safety": "modular set — redress for angles"},
  {"kind": "diy", "t": "Creature Animation", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["puppet", "1", 80.0]], "tools": ["none"], "steps": ["study animal", "gallop cycle", "shoot", "refine"], "time": "30h", "level": "advanced", "safety": "reference footage essential"},
  {"kind": "diy", "t": "Underwater Sequence", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 40.0], ["puppet", "1", 40.0]], "tools": ["none"], "steps": ["tank setup", "slow moves", "bubbles", "edit"], "time": "20h", "level": "advanced", "safety": "waterproof puppet — seal well"},
  {"kind": "diy", "t": "Night Shoot Lighting", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["lights", "1", 60.0]], "tools": ["none"], "steps": ["motivate sources", "practicals", "test", "shoot"], "time": "16h", "level": "advanced", "safety": "lock exposure — auto ruins takes"},
  {"kind": "diy", "t": "Festival-Ready Short", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 100.0], ["festival fees", "1", 50.0]], "tools": ["none"], "steps": ["story", "produce", "sound mix", "submit"], "time": "100h", "level": "advanced", "safety": "sound mix = half the film"},
  {"kind": "diy", "t": "Teaching Stop-Motion Class", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kits", "1", 120.0]], "tools": ["none"], "steps": ["curriculum", "stations", "shoot", "screen"], "time": "16h", "level": "advanced", "safety": "stations keep kids moving"}
];
var TIPS=["Cut everything before you glue anything.", "Dry-fit twice, fasten once.", "Sharp tools are safe tools \u2014 hone before you start.", "Finish scraps first to test color.", "Label your parts as you cut them.", "Take a photo before disassembly for reference."];
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

