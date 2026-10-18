(function(){'use strict';
/* JAH The Creative Lighting Database — real working generator, jahdb-db-creative-lighting-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRLIS-";
var SLUG="db-creative-lighting";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry.", "UL 588 for seasonal lighting; low-voltage LED preferred near flammable craft materials."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Mason Jar Fairy Lights", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["jars", "3", 9.0], ["fairy lights", "1", 10.0]], "tools": ["none"], "steps": ["clean jars", "lights inside", "lids", "place"], "time": "1h", "level": "beginner", "safety": "LED only — jars trap heat"},
  {"kind": "diy", "t": "Paper Lantern String", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["lanterns", "10", 15.0], ["LED string", "1", 12.0]], "tools": ["none"], "steps": ["expand lanterns", "clip to string", "hang", "timer"], "time": "2h", "level": "beginner", "safety": "LED only"},
  {"kind": "diy", "t": "Wine Bottle Lamp", "tier": "Foundations", "notes": "LED bulb (low heat)", "mats": [["bottle", "1", 0.0], ["lamp kit", "1", 15.0], ["shade", "1", 20.0]], "tools": ["drill"], "steps": ["drill bottle (diamond bit)", "kit through", "shade", "bulb LED"], "time": "3h", "level": "beginner", "safety": "drill glass slowly with water"},
  {"kind": "diy", "t": "Candle Cluster Styling", "tier": "Foundations", "notes": "clear of flammables", "mats": [["candles", "5", 20.0], ["tray", "1", 12.0]], "tools": ["none"], "steps": ["tray base", "vary heights", "greenery", "light"], "time": "1h", "level": "beginner", "safety": "never leave burning unattended"},
  {"kind": "diy", "t": "Glow-in-Dark Stars", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["stars", "1", 8.0]], "tools": ["none"], "steps": ["plan constellation", "stick", "charge", "enjoy"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "LED Strip Under Shelf", "tier": "Foundations", "notes": "don't overload", "mats": [["strip", "1", 15.0], ["power", "1", 0.0]], "tools": ["none"], "steps": ["clean surface", "stick strip", "power", "control"], "time": "1h", "level": "beginner", "safety": "low-voltage"},
  {"kind": "diy", "t": "Lampshade Refresh", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["shade", "1", 15.0], ["fabric", "1", 10.0], ["glue", "1", 6.0]], "tools": ["none"], "steps": ["strip old", "wrap new", "trim", "fit"], "time": "3h", "level": "beginner", "safety": "LED bulb only — fabric near heat is a risk"},
  {"kind": "diy", "t": "Twinkle Curtain", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["curtain lights", "1", 18.0], ["hooks", "1", 6.0]], "tools": ["none"], "steps": ["hang rod", "drape curtain", "timer", "enjoy"], "time": "2h", "level": "beginner", "safety": "indoor-rated only indoors"},
  {"kind": "diy", "t": "Neon-Style Rope Sign", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["LED rope", "1", 20.0], ["backing", "1", 10.0]], "tools": ["none"], "steps": ["design word", "fix rope", "mount", "plug"], "time": "3h", "level": "beginner", "safety": "low-voltage"},
  {"kind": "diy", "t": "Book Page Lamp", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["book", "1", 8.0], ["lamp kit", "1", 15.0]], "tools": ["drill"], "steps": ["hollow book", "kit through", "shade", "LED"], "time": "4h", "level": "beginner", "safety": "LED bulb only"},
  {"kind": "diy", "t": "Cloud Lamp (Cotton)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["lantern", "1", 10.0], ["cotton", "1", 8.0], ["LED", "1", 10.0], ["glue", "1", 5.0]], "tools": ["glue gun"], "steps": ["lantern base", "cotton cover", "LED inside", "hang"], "time": "4h", "level": "beginner", "safety": "LED only — cotton + heat = fire risk"},
  {"kind": "diy", "t": "Edison Pendant Trio", "tier": "Compounded", "notes": "wire nuts; ground; hire electrician if unsure", "mats": [["cord kits", "3", 45.0], ["bulbs", "1", 24.0], ["canopy", "1", 15.0]], "tools": ["screwdriver"], "steps": ["breaker off", "mount canopy", "wire kits", "hang varied"], "time": "6h", "level": "intermediate", "safety": "ELECTRICAL: breaker off"},
  {"kind": "diy", "t": "Backlit Wall Art", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["canvas", "1", 20.0], ["LED strip", "1", 15.0], ["frame", "1", 18.0]], "tools": ["none"], "steps": ["art on canvas", "strip behind", "frame float", "glow"], "time": "5h", "level": "intermediate", "safety": "low-voltage"},
  {"kind": "diy", "t": "Smart Bulb Scenes", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["smart bulbs", "4", 60.0], ["hub", "1", 0.0]], "tools": ["none"], "steps": ["install bulbs", "app setup", "scenes", "schedule"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Terrarium Lamp", "tier": "Compounded", "notes": "plants need light cycle", "mats": [["jar large", "1", 14.0], ["plants", "1", 12.0], ["LED puck", "1", 8.0]], "tools": ["trowel"], "steps": ["layer terrarium", "puck light top", "seal", "glow"], "time": "3h", "level": "intermediate", "safety": "LED only"},
  {"kind": "diy", "t": "Projection Night Sky", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["projector", "1", 40.0]], "tools": ["none"], "steps": ["position", "focus", "timer", "sleep"], "time": "1h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Cove Lighting Shelf", "tier": "Compounded", "notes": "channel prevents LED dots", "mats": [["LED strip", "1", 20.0], ["channel", "1", 15.0], ["power", "1", 12.0]], "tools": ["none"], "steps": ["channel mount", "strip in", "diffuser", "power"], "time": "4h", "level": "intermediate", "safety": "low-voltage"},
  {"kind": "diy", "t": "Stained Glass Panel Light", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["panel", "1", 30.0], ["light box", "1", 25.0]], "tools": ["none"], "steps": ["build box", "panel front", "LED inside", "hang"], "time": "6h", "level": "intermediate", "safety": "LED low heat"},
  {"kind": "diy", "t": "Motion-Sensor Path Lights", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["solar lights", "6", 36.0]], "tools": ["none"], "steps": ["sun survey", "stake", "test night", "adjust"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Color-Changing Headboard Glow", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["strip", "1", 18.0], ["headboard", "1", 0.0]], "tools": ["none"], "steps": ["strip behind", "control", "scenes", "sleep"], "time": "2h", "level": "intermediate", "safety": "low-voltage"},
  {"kind": "diy", "t": "Pendant from Colander", "tier": "Compounded", "notes": "ground metal", "mats": [["colander", "1", 12.0], ["cord kit", "1", 15.0], ["bulb", "1", 8.0]], "tools": ["drill"], "steps": ["drill center", "kit through", "hang", "bulb"], "time": "3h", "level": "intermediate", "safety": "breaker off"},
  {"kind": "diy", "t": "Light-Up Bar Shelf", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shelf", "1", 25.0], ["strip", "1", 15.0], ["glassware", "1", 0.0]], "tools": ["none"], "steps": ["shelf mount", "strip under", "glasses glow", "dimmer"], "time": "4h", "level": "intermediate", "safety": "low-voltage"},
  {"kind": "diy", "t": "Under-Cabinet Kitchen Lights", "tier": "Compounded", "notes": "driver ventilated", "mats": [["LED strip", "1", 22.0], ["channel", "1", 14.0], ["driver", "1", 16.0]], "tools": ["none"], "steps": ["measure", "channel mount", "strip", "driver"], "time": "3h", "level": "intermediate", "safety": "low-voltage"},
  {"kind": "diy", "t": "Chandelier Rewire", "tier": "Advanced", "notes": "if in doubt hire electrician; ground everything", "mats": [["chandelier", "1", 80.0], ["wire", "1", 15.0], ["sockets", "1", 20.0]], "tools": ["screwdriver"], "steps": ["breaker off", "strip old wire", "rewire sockets", "test"], "time": "10h", "level": "advanced", "safety": "ELECTRICAL: breaker off"},
  {"kind": "diy", "t": "Home Theater Bias Lighting", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["strip", "1", 25.0], ["controller", "1", 30.0]], "tools": ["none"], "steps": ["measure TV", "strip behind", "controller", "calibrate"], "time": "4h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Landscape Lighting Plan", "tier": "Advanced", "notes": "call 811 before digging", "mats": [["fixtures", "8", 160.0], ["transformer", "1", 60.0], ["cable", "1", 40.0]], "tools": ["shovel"], "steps": ["plan zones", "trench cable", "fixtures", "transformer"], "time": "16h", "level": "advanced", "safety": "low-voltage transformer"},
  {"kind": "diy", "t": "Neon Sign (Real Glass)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [], "tools": ["none"], "steps": ["design", "bend (pro)", "mount", "power"], "time": "20h", "level": "advanced", "safety": "real neon = high voltage — professional fabrication recommended"},
  {"kind": "diy", "t": "Smart Home Lighting Scenes", "tier": "Advanced", "notes": "neutral wire check; electrician if unsure", "mats": [["switches", "4", 120.0], ["bulbs", "1", 80.0]], "tools": ["screwdriver"], "steps": ["breaker off", "swap switches", "pair", "scenes"], "time": "10h", "level": "advanced", "safety": "breaker off"},
  {"kind": "diy", "t": "Fiber Optic Star Ceiling", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fiber kit", "1", 150.0], ["panels", "1", 60.0]], "tools": ["drill"], "steps": ["plan layout", "drill points", "fibers through", "light source"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "DMX Stage Wash", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fixtures", "4", 400.0], ["controller", "1", 150.0]], "tools": ["none"], "steps": ["hang fixtures", "DMX chain", "program scenes", "test"], "time": "16h", "level": "advanced", "safety": "secure overhead mounts — safety cables"},
  {"kind": "diy", "t": "Light Art Installation", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 200.0], ["controller", "1", 80.0]], "tools": ["varies"], "steps": ["concept", "build", "program", "install"], "time": "40h", "level": "advanced", "safety": "electrical safety per local code"},
  {"kind": "diy", "t": "Circadian Lighting Design", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tunable bulbs", "6", 150.0]], "tools": ["none"], "steps": ["audit rooms", "tunable bulbs", "schedule", "tune"], "time": "8h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Museum-Style Picture Lights", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["lights", "3", 120.0]], "tools": ["drill"], "steps": ["measure art", "mount centered", "wire or battery", "aim"], "time": "6h", "level": "advanced", "safety": "LED low heat near art"},
  {"kind": "diy", "t": "Outdoor Kitchen Lighting", "tier": "Advanced", "notes": "GFCI protection outdoors", "mats": [["fixtures", "1", 150.0], ["transformer", "1", 70.0]], "tools": ["shovel"], "steps": ["zones", "trench", "fixtures", "test night"], "time": "16h", "level": "advanced", "safety": "call 811"}
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

