(function(){'use strict';
/* JAH The Prop-Making Universe — real working generator, jahdb-db-prop-making-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRMA-";
var SLUG="db-prop-making";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Foam Sword (LARP-Safe)", "tier": "Foundations", "notes": "LARP check rules before use", "mats": [["EVA foam", "1", 15.0], ["dowel core", "1", 4.0], ["paint", "1", 10.0], ["sealant", "1", 8.0]], "tools": ["heat gun"], "steps": ["cut blade profile", "dowel core", "heat shape", "paint, seal"], "time": "8h", "level": "beginner", "safety": "heat gun burns"},
  {"kind": "diy", "t": "Cardboard Shield", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["paint", "1", 8.0], ["handle", "1", 4.0]], "tools": ["cutter"], "steps": ["cut circle", "dome shape", "paint emblem", "handle back"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Wand (Wooden)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["dowel", "1", 3.0], ["paint", "1", 6.0], ["crystal", "1", 4.0], ["glue", "1", 3.0]], "tools": ["sandpaper"], "steps": ["shape handle", "sand smooth", "paint", "crystal tip"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Potion Bottles", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bottles", "5", 8.0], ["labels", "1", 5.0], ["resin or water", "1", 6.0], ["corks", "1", 4.0]], "tools": ["none"], "steps": ["clean bottles", "fill colored", "label", "wax seal"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Foam Dagger", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 10.0], ["paint", "1", 8.0]], "tools": ["knife"], "steps": ["cut profile", "bevel edge", "paint", "seal"], "time": "4h", "level": "beginner", "safety": "knife safety"},
  {"kind": "diy", "t": "Treasure Map", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 3.0], ["tea", "1", 2.0]], "tools": ["none"], "steps": ["tea-stain", "burn edges (careful)", "draw map", "roll"], "time": "2h", "level": "beginner", "safety": "burn edges over sink — fire safety"},
  {"kind": "diy", "t": "Crown (Foam)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 8.0], ["paint", "1", 8.0], ["gems", "1", 6.0]], "tools": ["heat gun"], "steps": ["cut band", "shape", "paint gold", "gems"], "time": "4h", "level": "beginner", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Spell Book Cover", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["book", "1", 8.0], ["foam", "1", 6.0], ["paint", "1", 8.0]], "tools": ["glue"], "steps": ["foam details", "paint aged", "pages stain", "finish"], "time": "5h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Torch Prop (LED)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["dowel", "1", 3.0], ["foam", "1", 5.0], ["LED", "1", 6.0], ["paint", "1", 6.0]], "tools": ["none"], "steps": ["handle", "foam flame", "LED inside", "paint"], "time": "3h", "level": "beginner", "safety": "LED only — never real flame"},
  {"kind": "diy", "t": "Ancient Scroll", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 4.0], ["dowels", "2", 4.0], ["tea", "1", 2.0]], "tools": ["none"], "steps": ["stain paper", "dowel ends", "roll", "tie"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Foam Armor Bracer", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 10.0], ["straps", "1", 6.0], ["paint", "1", 8.0]], "tools": ["heat gun"], "steps": ["cut shape", "heat curve", "paint", "straps"], "time": "5h", "level": "beginner", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Sci-Fi Blaster", "tier": "Compounded", "notes": "convention rules — orange tip", "mats": [["foam", "1", 15.0], ["PVC", "1", 8.0], ["paint", "1", 12.0], ["LED", "1", 8.0]], "tools": ["heat gun"], "steps": ["body shape", "barrel PVC", "paint", "LED"], "time": "12h", "level": "intermediate", "safety": "low-voltage LED"},
  {"kind": "diy", "t": "Helmet (Foam Build)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 25.0], ["paint", "1", 12.0], ["visor", "1", 10.0], ["straps", "1", 8.0]], "tools": ["heat gun"], "steps": ["template scale", "dome form", "visor", "straps"], "time": "16h", "level": "intermediate", "safety": "ventilation when worn — don't seal"},
  {"kind": "diy", "t": "Staff with Crystal", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["dowel", "1", 5.0], ["foam", "1", 10.0], ["crystal", "1", 12.0], ["paint", "1", 10.0], ["LED", "1", 8.0]], "tools": ["heat gun"], "steps": ["staff", "topper sculpt", "paint", "LED glow"], "time": "12h", "level": "intermediate", "safety": "low-voltage LED"},
  {"kind": "diy", "t": "Backpack Prop", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["foam", "1", 12.0], ["paint", "1", 10.0], ["straps", "1", 8.0]], "tools": ["cutter"], "steps": ["box base", "foam details", "paint", "straps"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Mask (Base + Detail)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["mask base", "1", 12.0], ["foam", "1", 10.0], ["paint", "1", 10.0]], "tools": ["heat gun"], "steps": ["fit base", "foam details", "paint", "strap"], "time": "10h", "level": "intermediate", "safety": "breathing holes kept clear"},
  {"kind": "diy", "t": "Wings (Articulated)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 20.0], ["frame", "1", 15.0], ["fabric", "1", 18.0], ["paint", "1", 12.0]], "tools": ["heat gun"], "steps": ["frame build", "foam feathers", "fabric cover", "articulate"], "time": "20h", "level": "intermediate", "safety": "weight balanced"},
  {"kind": "diy", "t": "Chest Armor", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 30.0], ["straps", "1", 10.0], ["paint", "1", 12.0]], "tools": ["heat gun"], "steps": ["torso template", "shape", "paint", "straps"], "time": "18h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Ray Gun (Retro)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 12.0], ["fins", "1", 8.0], ["paint", "1", 10.0], ["dome", "1", 6.0]], "tools": ["heat gun"], "steps": ["body", "fins", "dome", "paint chrome"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Book of Spells (Light-Up)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["book", "1", 10.0], ["LED", "1", 8.0], ["foam", "1", 8.0], ["paint", "1", 8.0]], "tools": ["none"], "steps": ["hollow book", "LED pages", "foam cover", "paint"], "time": "8h", "level": "intermediate", "safety": "low-voltage LED"},
  {"kind": "diy", "t": "Shoulder Pauldrons", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 18.0], ["straps", "1", 8.0], ["paint", "1", 10.0]], "tools": ["heat gun"], "steps": ["layer plates", "shape", "paint", "strap"], "time": "12h", "level": "intermediate", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Full Foam Armor Set", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [], "tools": ["heat gun"], "steps": ["full templates", "all pieces", "paint uniform", "straps"], "time": "60h", "level": "advanced", "safety": "plan mobility — sit, walk, stairs test"},
  {"kind": "diy", "t": "Animatronic Eye", "tier": "Advanced", "notes": "solder ventilate", "mats": [["servo", "1", 15.0], ["arduino", "1", 25.0], ["eye", "1", 20.0], ["housing", "1", 15.0]], "tools": ["soldering"], "steps": ["eye build", "servo mount", "code blink", "install"], "time": "24h", "level": "advanced", "safety": "low-voltage electronics"},
  {"kind": "diy", "t": "Working Lightsaber (Neopixel)", "tier": "Advanced", "notes": "battery safety — Li-ion supervised", "mats": [["blade", "1", 40.0], ["neopixel", "1", 35.0], ["board", "1", 60.0], ["hilt", "1", 30.0]], "tools": ["soldering"], "steps": ["hilt build", "blade install", "board wire", "config"], "time": "30h", "level": "advanced", "safety": "soldering safety"},
  {"kind": "diy", "t": "Helmet with HUD", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["helmet", "1", 40.0], ["display", "1", 60.0], ["battery", "1", 20.0]], "tools": ["soldering"], "steps": ["helmet base", "display mount", "wire", "test"], "time": "30h", "level": "advanced", "safety": "don't block vision — safety first"},
  {"kind": "diy", "t": "Mechanical Wings", "tier": "Advanced", "notes": "battery safety", "mats": [["frame", "1", 40.0], ["servos", "2", 30.0], ["fabric", "1", 25.0], ["battery", "1", 20.0]], "tools": ["soldering"], "steps": ["frame", "servo linkage", "fabric", "test"], "time": "40h", "level": "advanced", "safety": "pinch points guarded"},
  {"kind": "diy", "t": "Talking Portrait", "tier": "Advanced", "notes": "secure mount", "mats": [["frame", "1", 20.0], ["screen", "1", 50.0], ["speaker", "1", 25.0]], "tools": ["none"], "steps": ["frame", "screen mount", "video loop", "speaker"], "time": "20h", "level": "advanced", "safety": "low-voltage"},
  {"kind": "diy", "t": "Fog Machine Integration", "tier": "Advanced", "notes": "keep from smoke alarms", "mats": [["fogger", "1", 60.0], ["tubing", "1", 15.0], ["prop", "1", 20.0]], "tools": ["none"], "steps": ["prop build", "fog routing", "trigger", "test"], "time": "16h", "level": "advanced", "safety": "fog fluid safety — ventilate"},
  {"kind": "diy", "t": "Full Creature Suit Head", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 40.0], ["fur", "1", 50.0], ["eyes", "1", 25.0], ["fan", "1", 15.0]], "tools": ["heat gun"], "steps": ["sculpt", "fur", "eyes", "fan vent"], "time": "40h", "level": "advanced", "safety": "ventilation fan mandatory inside head"},
  {"kind": "diy", "t": "Spinning Propeller Pack", "tier": "Advanced", "notes": "test secured", "mats": [["motor", "1", 25.0], ["props", "1", 20.0], ["frame", "1", 20.0], ["battery", "1", 25.0]], "tools": ["soldering"], "steps": ["frame", "motor mount", "props", "test"], "time": "24h", "level": "advanced", "safety": "props dangerous — guards"},
  {"kind": "diy", "t": "LED Matrix Chest Piece", "tier": "Advanced", "notes": "code tested", "mats": [["matrix", "1", 30.0], ["controller", "1", 25.0], ["foam", "1", 15.0], ["battery", "1", 20.0]], "tools": ["soldering"], "steps": ["foam base", "matrix mount", "code patterns", "wear"], "time": "24h", "level": "advanced", "safety": "battery safety"},
  {"kind": "diy", "t": "Weathered Hero Prop Replica", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 30.0], ["materials", "1", 40.0], ["paint", "1", 20.0]], "tools": ["varies"], "steps": ["research", "build", "weathering layers", "display"], "time": "40h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Puppet (Rod-Controlled)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 25.0], ["rods", "1", 10.0], ["fabric", "1", 20.0], ["paint", "1", 12.0]], "tools": ["sewing"], "steps": ["head sculpt", "body", "rods", "perform"], "time": "30h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Set Piece: Throne", "tier": "Advanced", "notes": "sturdy — people sit on it", "mats": [["wood", "1", 60.0], ["foam", "1", 30.0], ["paint", "1", 25.0], ["fabric", "1", 20.0]], "tools": ["saw"], "steps": ["frame", "foam carve", "paint", "upholster"], "time": "40h", "level": "advanced", "safety": "saw safety"}
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

