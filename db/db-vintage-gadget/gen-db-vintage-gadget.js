(function(){'use strict';
/* JAH The Vintage Gadget Database — real working generator, jahdb-db-vintage-gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VG-";
var SLUG="db-vintage-gadget";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Why Vintage Tech", "tier": "Foundations", "concept": "design endures", "mechanism": "build + aesthetics", "parts": ["journal"], "build": "reflect", "time": "2h", "level": "beginner", "safety": "none", "notes": "they don't make them like this"},
  {"kind": "gm", "t": "First Find: Typewriter", "tier": "Foundations", "concept": "clickety joy", "mechanism": "manual machine", "parts": ["clean"], "build": "find", "time": "6h", "level": "beginner", "safety": "none", "notes": "oil + ribbon"},
  {"kind": "gm", "t": "Rotary Phone", "tier": "Foundations", "concept": "ring ring", "mechanism": "restore + use", "parts": ["wire"], "build": "find", "time": "6h", "level": "beginner", "safety": "low-voltage", "notes": "pulse needs adapter"},
  {"kind": "gm", "t": "Film Camera (35mm)", "tier": "Foundations", "concept": "analog magic", "mechanism": "load + shoot", "parts": ["test"], "build": "find", "time": "8h", "level": "beginner", "safety": "none", "notes": "light seals first"},
  {"kind": "gm", "t": "Tube Radio", "tier": "Foundations", "concept": "warm sound", "mechanism": "recap + align", "parts": ["restore"], "build": "find", "time": "16h", "level": "beginner", "safety": "HIGH VOLTAGE", "notes": "pro for chassis"},
  {"kind": "gm", "t": "Polaroid (Vintage)", "tier": "Foundations", "concept": "instant nostalgia", "mechanism": "film + clean", "parts": ["shoot"], "build": "find", "time": "4h", "level": "beginner", "safety": "battery", "notes": "film expensive"},
  {"kind": "gm", "t": "Calculator (Vintage)", "tier": "Foundations", "concept": "LED glow", "mechanism": "restore", "parts": ["clean"], "build": "find", "time": "4h", "level": "beginner", "safety": "battery", "notes": "corrosion check"},
  {"kind": "gm", "t": "Game Console (Retro)", "tier": "Foundations", "concept": "pixels!", "mechanism": "clean + test", "parts": ["play"], "build": "find", "time": "6h", "level": "beginner", "safety": "capacitors", "notes": "recap eventually"},
  {"kind": "gm", "t": "The Walkman Era", "tier": "Foundations", "concept": "mixtape era", "mechanism": "belts + clean", "parts": ["fix"], "build": "find", "time": "6h", "level": "beginner", "safety": "none", "notes": "belts always"},
  {"kind": "gm", "t": "CRT TV (Small)", "tier": "Foundations", "concept": "scanlines", "mechanism": "test + use", "parts": ["tune"], "build": "find", "time": "6h", "level": "beginner", "safety": "HIGH VOLTAGE", "notes": "pro inside"},
  {"kind": "gm", "t": "Slide Projector", "tier": "Foundations", "concept": "big memories", "mechanism": "bulb + clean", "parts": ["show"], "build": "find", "time": "4h", "level": "beginner", "safety": "hot bulb", "notes": "cool before move"},
  {"kind": "gm", "t": "Tube Amp Restoration", "tier": "Compounded", "concept": "tone heaven", "mechanism": "recap + tubes", "parts": ["restore"], "build": "amp", "time": "30h", "level": "intermediate", "safety": "LETHAL VOLTAGE", "notes": "pro supervision"},
  {"kind": "gm", "t": "Shortwave Radio", "tier": "Compounded", "concept": "world bands", "mechanism": "align + antenna", "parts": ["restore"], "build": "radio", "time": "20h", "level": "intermediate", "safety": "voltage", "notes": "longwire antenna"},
  {"kind": "gm", "t": "Mechanical Calculator", "tier": "Compounded", "concept": "gears compute", "mechanism": "oil + adjust", "parts": ["restore"], "build": "calc", "time": "20h", "level": "intermediate", "safety": "none", "notes": "patience"},
  {"kind": "gm", "t": "Teletype Machine", "tier": "Compounded", "concept": "clackety news", "mechanism": "restore", "parts": ["restore"], "build": "tty", "time": "40h", "level": "intermediate", "safety": "voltage", "notes": "heavy!"},
  {"kind": "gm", "t": "Oscilloscope (Tube)", "tier": "Compounded", "concept": "green trace", "mechanism": "recap + calibrate", "parts": ["restore"], "build": "scope", "time": "30h", "level": "intermediate", "safety": "HIGH VOLTAGE", "notes": "pro"},
  {"kind": "gm", "t": "Jukebox (Wallbox)", "tier": "Compounded", "concept": "diner dreams", "mechanism": "mechanism", "parts": ["restore"], "build": "box", "time": "40h", "level": "intermediate", "safety": "voltage", "notes": "parts hunt"},
  {"kind": "gm", "t": "Pinball (EM)", "tier": "Compounded", "concept": "chimes + relays", "mechanism": "clean + adjust", "parts": ["restore"], "build": "pin", "time": "60h", "level": "intermediate", "safety": "voltage", "notes": "schematics essential"},
  {"kind": "gm", "t": "Mainframe Terminal", "tier": "Compounded", "concept": "green screen", "mechanism": "RS-232 + Pi", "parts": ["build"], "build": "term", "time": "20h", "level": "intermediate", "safety": "voltage", "notes": "Pi inside"},
  {"kind": "gm", "t": "Singer Sewing (Treadle)", "tier": "Compounded", "concept": "foot power", "mechanism": "oil + time", "parts": ["restore"], "build": "machine", "time": "16h", "level": "intermediate", "safety": "none", "notes": "timing matters"},
  {"kind": "gm", "t": "Phonograph (Wind-Up)", "tier": "Compounded", "concept": "acoustic music", "mechanism": "spring + horn", "parts": ["restore"], "build": "phono", "time": "20h", "level": "intermediate", "safety": "spring", "notes": "78s only"},
  {"kind": "gm", "t": "Enigma (Replica)", "tier": "Compounded", "concept": "crypto history", "mechanism": "kit build", "parts": ["build"], "build": "kit", "time": "30h", "level": "intermediate", "safety": "none", "notes": "fascinating"},
  {"kind": "gm", "t": "Telegraph Key", "tier": "Compounded", "concept": "dots + dashes", "mechanism": "restore + learn", "parts": ["restore"], "build": "key", "time": "10h", "level": "intermediate", "safety": "none", "notes": "learn CW"},
  {"kind": "gm", "t": "Adding Machine", "tier": "Compounded", "concept": "crank math", "mechanism": "oil + use", "parts": ["restore"], "build": "machine", "time": "12h", "level": "intermediate", "safety": "none", "notes": "satisfying ka-chunk"},
  {"kind": "gm", "t": "Apollo Guidance (Sim)", "tier": "Advanced", "concept": "moon computer", "mechanism": "emulate + panel", "parts": ["build"], "build": "agc", "time": "60h", "level": "advanced", "safety": "none", "notes": "DSKY replica"},
  {"kind": "gm", "t": "PDP-8 Restoration", "tier": "Advanced", "concept": "mini pioneer", "mechanism": "restore boards", "parts": ["restore"], "build": "pdp", "time": "100h", "level": "advanced", "safety": "voltage", "notes": "core memory!"},
  {"kind": "gm", "t": "Tube Computer (Build)", "tier": "Advanced", "concept": "compute with glass", "mechanism": "kit + tubes", "parts": ["build"], "build": "computer", "time": "200h", "level": "advanced", "safety": "HIGH VOLTAGE", "notes": "expert"},
  {"kind": "gm", "t": "Radar (Vintage)", "tier": "Advanced", "concept": "see far", "mechanism": "restore display", "parts": ["restore"], "build": "radar", "time": "100h", "level": "advanced", "safety": "RADIATION", "notes": "pro only"},
  {"kind": "gm", "t": "Television (Mechanical)", "tier": "Advanced", "concept": "spinning disc", "mechanism": "Nipkow build", "parts": ["build"], "build": "tv", "time": "80h", "level": "advanced", "safety": "none", "notes": "1920s tech"},
  {"kind": "gm", "t": "Computer Museum", "tier": "Advanced", "concept": "preserve all", "mechanism": "curation", "parts": ["curate"], "build": "museum", "time": "100h", "level": "advanced", "safety": "none", "notes": "working exhibits"},
  {"kind": "gm", "t": "Chip Collection", "tier": "Advanced", "concept": "silicon history", "mechanism": "CPUs + stories", "parts": ["collect"], "build": "chips", "time": "40h", "level": "advanced", "safety": "ESD", "notes": "gold tops pretty"},
  {"kind": "gm", "t": "Manual Library", "tier": "Advanced", "concept": "paper knowledge", "mechanism": "schematics + manuals", "parts": ["collect"], "build": "library", "time": "40h", "level": "advanced", "safety": "none", "notes": "scan + share"},
  {"kind": "gm", "t": "Master Restorer", "tier": "Advanced", "concept": "the craft", "mechanism": "decades practice", "parts": ["mentor"], "build": "path", "time": "200h", "level": "advanced", "safety": "respect voltage", "notes": "teach"},
  {"kind": "gm", "t": "Slide Rule", "tier": "Advanced", "concept": "logarithmic genius", "mechanism": "learn + use", "parts": ["study"], "build": "rule", "time": "16h", "level": "advanced", "safety": "none", "notes": "3 significant figures"}
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

