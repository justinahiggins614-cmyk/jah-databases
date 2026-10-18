(function(){'use strict';
/* JAH The Costume Creator Database — real working generator, jahdb-gen-costume-creator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CCS-";
var SLUG="gen-costume-creator";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Pirate (Closet Build)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["striped shirt", "1", 15.0], ["sash", "1", 8.0], ["bandana", "1", 5.0], ["boots", "1", 0.0]], "tools": ["scissors"], "steps": ["shirt", "sash belt", "bandana", "boots"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Witch (Classic)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["black dress", "1", 20.0], ["hat", "1", 12.0], ["cape", "1", 15.0]], "tools": ["none"], "steps": ["dress", "hat", "cape", "broom"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Vampire Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cape", "1", 18.0], ["fangs", "1", 5.0], ["pale makeup", "1", 10.0]], "tools": ["none"], "steps": ["cape", "fangs", "makeup", "hair slick"], "time": "2h", "level": "beginner", "safety": "costume makeup patch-test skin"},
  {"kind": "diy", "t": "Superhero (DIY Suit)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["morph suit", "1", 25.0], ["belt", "1", 10.0], ["emblem", "1", 6.0]], "tools": ["none"], "steps": ["suit", "belt", "emblem iron-on", "boots"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Ghost (Elevated Sheet)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["sheet", "1", 12.0], ["glasses frames", "1", 5.0]], "tools": ["scissors"], "steps": ["eye holes", "tattered hem", "frames over", "spooky"], "time": "2h", "level": "beginner", "safety": "visibility — trim holes large"},
  {"kind": "diy", "t": "Cat (Simple)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["black outfit", "1", 0.0], ["ears", "1", 8.0], ["tail", "1", 10.0], ["makeup", "1", 8.0]], "tools": ["none"], "steps": ["outfit", "ears", "tail", "whiskers"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Scarecrow", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["flannel", "1", 15.0], ["overalls", "1", 20.0], ["straw", "1", 5.0], ["hat", "1", 10.0]], "tools": ["none"], "steps": ["flannel", "overalls", "straw cuffs", "hat"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Tourist (Funny)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["hawaiian shirt", "1", 15.0], ["camera toy", "1", 8.0], ["shorts", "1", 0.0], ["socks", "1", 5.0]], "tools": ["none"], "steps": ["shirt", "socks+sandals", "camera", "map"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Greek Toga", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["sheet", "1", 12.0], ["gold rope", "1", 5.0], ["laurel", "1", 8.0]], "tools": ["none"], "steps": ["drape toga", "rope belt", "laurel", "sandals"], "time": "2h", "level": "beginner", "safety": "secure draping — safety pins"},
  {"kind": "diy", "t": "Robot (Boxes)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["boxes", "1", 0.0], ["foil", "1", 8.0], ["paint", "1", 6.0], ["lights", "1", 5.0]], "tools": ["cutter"], "steps": ["box torso", "foil cover", "button panel", "antenna"], "time": "4h", "level": "beginner", "safety": "low-voltage lights only"},
  {"kind": "diy", "t": "Mummy Wrap", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["gauze rolls", "6", 12.0], ["torn sheets", "1", 0.0]], "tools": ["none"], "steps": ["base layer", "wrap limbs", "tea-stain", "finish"], "time": "3h", "level": "beginner", "safety": "don't wrap tight — circulation"},
  {"kind": "diy", "t": "Steampunk Adventurer", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["corset/vest", "1", 40.0], ["goggles", "1", 15.0], ["gears", "1", 10.0], ["boots", "1", 0.0]], "tools": ["glue"], "steps": ["base outfit", "gear accents", "goggles", "props"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Medieval Knight (Foam)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["EVA foam", "1", 30.0], ["paint", "1", 12.0], ["straps", "1", 10.0]], "tools": ["heat gun"], "steps": ["cut plates", "heat shape", "paint metallic", "strap"], "time": "16h", "level": "intermediate", "safety": "heat gun burns — gloves, ventilation"},
  {"kind": "diy", "t": "1920s Flapper", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["dress", "1", 45.0], ["headband", "1", 12.0], ["feather", "1", 8.0], ["gloves", "1", 10.0]], "tools": ["sewing"], "steps": ["dress", "headband", "feather", "long beads"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Space Explorer", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["jumpsuit", "1", 35.0], ["patches", "1", 12.0], ["helmet toy", "1", 20.0], ["boots", "1", 0.0]], "tools": ["sewing"], "steps": ["jumpsuit", "mission patches", "helmet", "boots"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Victorian Gentleman", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["coat", "1", 50.0], ["tophat", "1", 25.0], ["cane", "1", 15.0], ["pocket watch", "1", 12.0]], "tools": ["none"], "steps": ["coat", "hat", "cane", "watch"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Warrior Princess", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["dress base", "1", 30.0], ["armor foam", "1", 25.0], ["paint", "1", 10.0], ["wig", "1", 20.0]], "tools": ["heat gun"], "steps": ["dress", "foam armor", "paint", "wig style"], "time": "16h", "level": "intermediate", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Mad Scientist", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["lab coat", "1", 25.0], ["wig", "1", 15.0], ["goggles", "1", 10.0], ["props", "1", 12.0]], "tools": ["none"], "steps": ["coat", "wild wig", "goggles", "beakers"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Fairy (Layered)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["dress", "1", 30.0], ["wings", "1", 25.0], ["flower crown", "1", 15.0], ["glitter", "1", 8.0]], "tools": ["none"], "steps": ["dress", "wings", "flower crown", "glitter"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Zombie (Makeup-Heavy)", "tier": "Compounded", "notes": "fake blood stains", "mats": [["torn clothes", "1", 10.0], ["makeup kit", "1", 25.0], ["fake blood", "1", 8.0]], "tools": ["none"], "steps": ["distress clothes", "wound makeup", "blood", "act"], "time": "5h", "level": "intermediate", "safety": "patch-test makeup"},
  {"kind": "diy", "t": "Superheroine (Sewn)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 30.0], ["pattern", "1", 12.0], ["emblem", "1", 8.0], ["boots", "1", 0.0]], "tools": ["sewing"], "steps": ["bodysuit", "emblem", "cape", "mask"], "time": "14h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Plague Doctor", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["coat", "1", 40.0], ["mask base", "1", 25.0], ["hat", "1", 20.0], ["staff", "1", 12.0]], "tools": ["none"], "steps": ["coat", "beak mask", "hat", "staff"], "time": "8h", "level": "intermediate", "safety": "mask ventilation — don't seal airtight"},
  {"kind": "diy", "t": "Iron Man (Foam Build)", "tier": "Advanced", "notes": "LED low voltage", "mats": [["EVA foam", "1", 60.0], ["paint", "1", 20.0], ["LEDs", "1", 15.0], ["straps", "1", 12.0]], "tools": ["heat gun"], "steps": ["pepakura scale", "foam cut", "heat form", "paint, lights"], "time": "40h", "level": "advanced", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Stormtrooper Armor", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kit or foam", "1", 150.0], ["paint", "1", 25.0], ["straps", "1", 15.0]], "tools": ["heat gun"], "steps": ["size kit", "trim", "paint white", "strap"], "time": "40h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Elsa Ice Gown", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 60.0], ["pattern", "1", 15.0], ["crystals", "1", 30.0]], "tools": ["sewing"], "steps": ["gown", "cape sheer", "crystal scatter", "fit"], "time": "30h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Samurai Armor", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 50.0], ["lacing", "1", 15.0], ["paint", "1", 20.0], ["helmet", "1", 30.0]], "tools": ["heat gun"], "steps": ["plates", "lace rows", "helmet", "stand"], "time": "40h", "level": "advanced", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Dragon (Wearable)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 70.0], ["foam", "1", 40.0], ["wings frame", "1", 25.0], ["paint", "1", 20.0]], "tools": ["sewing"], "steps": ["body suit", "wings articulated", "head", "tail"], "time": "50h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Ball Gown (Historical)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fabric 10yd", "1", 120.0], ["pattern", "1", 20.0], ["hoop", "1", 40.0]], "tools": ["sewing"], "steps": ["mockup first", "gown", "hoop", "finish"], "time": "60h", "level": "advanced", "safety": "mockup saves fabric"},
  {"kind": "diy", "t": "Mecha Suit", "tier": "Advanced", "notes": "ventilation inside suit", "mats": [["foam", "1", 80.0], ["electronics", "1", 30.0], ["paint", "1", 25.0]], "tools": ["heat gun"], "steps": ["frame", "armor shells", "lights", "wear test"], "time": "60h", "level": "advanced", "safety": "weight distribution"},
  {"kind": "diy", "t": "Alien Creature", "tier": "Advanced", "notes": "never sleep in contacts", "mats": [["bodysuit", "1", 35.0], ["prosthetics", "1", 50.0], ["paint", "1", 25.0], ["contacts", "1", 0.0]], "tools": ["none"], "steps": ["suit", "prosthetic apply", "paint blend", "perform"], "time": "20h", "level": "advanced", "safety": "prosthetic adhesive patch test"},
  {"kind": "diy", "t": "Anime Armor Set", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam", "1", 60.0], ["paint", "1", 25.0], ["wig", "1", 30.0]], "tools": ["heat gun"], "steps": ["reference study", "foam build", "paint", "wig"], "time": "45h", "level": "advanced", "safety": "heat gun safety"},
  {"kind": "diy", "t": "Royal Guard", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["coat", "1", 60.0], ["bearskin faux", "1", 40.0], ["trousers", "1", 30.0]], "tools": ["sewing"], "steps": ["coat", "hat", "trousers", "polish"], "time": "30h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Cyborg (SFX)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["makeup", "1", 40.0], ["prosthetics", "1", 45.0], ["circuit props", "1", 20.0]], "tools": ["none"], "steps": ["skin prep", "prosthetics", "paint", "costume"], "time": "16h", "level": "advanced", "safety": "patch-test all adhesives"},
  {"kind": "diy", "t": "Full Fursuit Partial", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fur", "1", 120.0], ["foam head base", "1", 40.0], ["eyes", "1", 20.0]], "tools": ["sewing"], "steps": ["head foam", "fur cover", "eyes", "body"], "time": "60h", "level": "advanced", "safety": "ventilation in head — mesh eyes, fan"}
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

