(function(){'use strict';
/* JAH The Mobile Creator Studio Database — real working generator, jahdb-gen-mobile-creator-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MCS-";
var SLUG="gen-mobile-creator-studio";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Electrical builds: keep mains-voltage work to qualified persons; low-voltage prototypes only for beginners.", "Prototype before final assembly; test every function before enclosing."];
var CITATIONS=["Norman, Donald A. 'The Design of Everyday Things.' Revised ed. MIT Press, 2013.", "Petroski, Henry. 'The Evolution of Useful Things.' Knopf, 1992."];
var BANK=[
  {"kind": "gm", "t": "Phone Filming Kit", "tier": "Foundations", "concept": "film anywhere", "mechanism": "phone + grip + mic", "parts": ["kit"], "build": "build", "time": "6h", "level": "beginner", "safety": "none", "notes": "studio: audio > video"},
  {"kind": "gm", "t": "Vlog Lighting", "tier": "Foundations", "concept": "look good", "mechanism": "ring + window", "parts": ["lights"], "build": "set", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: window is key light"},
  {"kind": "gm", "t": "Audio (Lavalier)", "tier": "Foundations", "concept": "hear clearly", "mechanism": "wired lav mic", "parts": ["mic"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "studio: 6in from mouth"},
  {"kind": "gm", "t": "Tripod + Mount", "tier": "Foundations", "concept": "steady shots", "mechanism": "pocket tripod", "parts": ["tripod"], "build": "study", "time": "1h", "level": "beginner", "safety": "none", "notes": "studio: lock exposure"},
  {"kind": "gm", "t": "Backdrop (Portable)", "tier": "Foundations", "concept": "clean background", "mechanism": "collapsible green", "parts": ["backdrop"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: even light, no shadows"},
  {"kind": "gm", "t": "Script + Teleprompter", "tier": "Foundations", "concept": "speak smooth", "mechanism": "phone prompter app", "parts": ["app"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: bullet points, not script"},
  {"kind": "gm", "t": "Thumbnail Kit", "tier": "Foundations", "concept": "clicks matter", "mechanism": "phone + templates", "parts": ["kit"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: face + 3 words"},
  {"kind": "gm", "t": "Editing (Phone)", "tier": "Foundations", "concept": "edit anywhere", "mechanism": "app + presets", "parts": ["app"], "build": "study", "time": "6h", "level": "beginner", "safety": "none", "notes": "studio: cut on beats"},
  {"kind": "gm", "t": "Music (Licensed)", "tier": "Foundations", "concept": "soundtrack", "mechanism": "licensed libraries", "parts": ["music"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: license everything"},
  {"kind": "gm", "t": "Posting Schedule", "tier": "Foundations", "concept": "consistency", "mechanism": "calendar + batch", "parts": ["plan"], "build": "plan", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: batch monthly"},
  {"kind": "gm", "t": "Analytics Basics", "tier": "Foundations", "concept": "what works?", "mechanism": "platform stats", "parts": ["stats"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "studio: retention > views"},
  {"kind": "gm", "t": "Mirrorless Kit (Travel)", "tier": "Compounded", "concept": "pro look portable", "mechanism": "body + 2 lenses", "parts": ["kit"], "build": "pack", "time": "8h", "level": "intermediate", "safety": "none", "notes": "studio: 35mm + 85mm"},
  {"kind": "gm", "t": "Audio (Field Recorder)", "tier": "Compounded", "concept": "pro sound", "mechanism": "recorder + shotgun", "parts": ["recorder"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "studio: 24-bit/48k"},
  {"kind": "gm", "t": "Lighting (3-Point Kit)", "tier": "Compounded", "concept": "shape light", "mechanism": "3 LEDs + stands", "parts": ["lights"], "build": "set", "time": "6h", "level": "intermediate", "safety": "none", "notes": "studio: key/fill/back"},
  {"kind": "gm", "t": "Gimbal (Phone)", "tier": "Compounded", "concept": "smooth moves", "mechanism": "3-axis gimbal", "parts": ["gimbal"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "studio: ninja walk"},
  {"kind": "gm", "t": "Drone (Sub-250g)", "tier": "Compounded", "concept": "aerials", "mechanism": "mini drone + ND", "parts": ["drone"], "build": "fly", "time": "8h", "level": "intermediate", "safety": "drone laws", "notes": "studio: golden hour"},
  {"kind": "gm", "t": "Livestream Kit", "tier": "Compounded", "concept": "go live anywhere", "mechanism": "encoder + bonded data", "parts": ["kit"], "build": "build", "time": "10h", "level": "intermediate", "safety": "none", "notes": "studio: wired when possible"},
  {"kind": "gm", "t": "Podcast (Mobile)", "tier": "Compounded", "concept": "podcast anywhere", "mechanism": "2 mics + recorder", "parts": ["kit"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "studio: room tone first"},
  {"kind": "gm", "t": "Photo Editing (Travel)", "tier": "Compounded", "concept": "edit anywhere", "mechanism": "laptop + calibrated", "parts": ["kit"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "studio: calibrate monthly"},
  {"kind": "gm", "t": "Backdrop + Lights (Pop)", "tier": "Compounded", "concept": "studio anywhere", "mechanism": "pop tent + LEDs", "parts": ["tent"], "build": "set", "time": "4h", "level": "intermediate", "safety": "none", "notes": "studio: 10-min setup"},
  {"kind": "gm", "t": "Teleprompter (Pro)", "tier": "Compounded", "concept": "read natural", "mechanism": "beam-splitter + tablet", "parts": ["prompter"], "build": "build", "time": "8h", "level": "intermediate", "safety": "none", "notes": "studio: eye-line at lens"},
  {"kind": "gm", "t": "Multi-Cam (2 Cam)", "tier": "Compounded", "concept": "cutaways", "mechanism": "2 cams + sync", "parts": ["kit"], "build": "build", "time": "12h", "level": "intermediate", "safety": "none", "notes": "studio: clap sync"},
  {"kind": "gm", "t": "360 Camera Kit", "tier": "Compounded", "concept": "all directions", "mechanism": "camera + stitch", "parts": ["kit"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "studio: hide the tripod"},
  {"kind": "gm", "t": "Cinema Camera (Compact)", "tier": "Advanced", "concept": "film look", "mechanism": "compact cinema + primes", "parts": ["kit"], "build": "pack", "time": "16h", "level": "advanced", "safety": "none", "notes": "studio: ND essential"},
  {"kind": "gm", "t": "Audio (Full Field)", "tier": "Advanced", "concept": "pro audio anywhere", "mechanism": "mixer + booms + lavs", "parts": ["kit"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "studio: boom > lav outdoors"},
  {"kind": "gm", "t": "Lighting (Aputure-Level)", "tier": "Advanced", "concept": "shape anything", "mechanism": "COB + modifiers", "parts": ["lights"], "build": "set", "time": "12h", "level": "advanced", "safety": "none", "notes": "studio: diffusion is magic"},
  {"kind": "gm", "t": "Live Switcher Kit", "tier": "Advanced", "concept": "switch live", "mechanism": "switcher + cams", "parts": ["kit"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "studio: ISO record all"},
  {"kind": "gm", "t": "Documentary Rig", "tier": "Advanced", "concept": "run and gun", "mechanism": "shoulder + audio + ND", "parts": ["rig"], "build": "build", "time": "16h", "level": "advanced", "safety": "none", "notes": "studio: balance the rig"},
  {"kind": "gm", "t": "Studio in a Van", "tier": "Advanced", "concept": "tour studio", "mechanism": "van + power + edit", "parts": ["van"], "build": "build", "time": "100h", "level": "advanced", "safety": "electrical pro", "notes": "studio: shore power"},
  {"kind": "gm", "t": "Broadcast Backpack", "tier": "Advanced", "concept": "live anywhere", "mechanism": "bonded cellular rig", "parts": ["rig"], "build": "build", "time": "30h", "level": "advanced", "safety": "none", "notes": "studio: 3 carriers"},
  {"kind": "gm", "t": "Color Suite (Mobile)", "tier": "Advanced", "concept": "grade anywhere", "mechanism": "laptop + panel + scope", "parts": ["kit"], "build": "build", "time": "20h", "level": "advanced", "safety": "none", "notes": "studio: scopes don't lie"},
  {"kind": "gm", "t": "Master Mobile Studio", "tier": "Advanced", "concept": "everything", "mechanism": "curated pro kit", "parts": ["kit"], "build": "pack", "time": "30h", "level": "advanced", "safety": "insurance", "notes": "studio: redundancy saves shoots"},
  {"kind": "gm", "t": "Teaching Creator Class", "tier": "Advanced", "concept": "teach creating", "mechanism": "curriculum + kits", "parts": ["class"], "build": "plan", "time": "20h", "level": "advanced", "safety": "none", "notes": "studio: story first, gear second"},
  {"kind": "gm", "t": "Field Monitor", "tier": "Advanced", "concept": "see clearly", "mechanism": "7in + hood", "parts": ["monitor"], "build": "build", "time": "12h", "level": "advanced", "safety": "none", "notes": "studio: 1000 nits daylight"}
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

