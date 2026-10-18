(function(){'use strict';
/* JAH The Personalized Gift Generator — real working generator, jahdb-gen-personalized-gift-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PGGS-";
var SLUG="gen-personalized-gift-generator";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Gift for the New Parent", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["gift box", "1", 8.0], ["onesie", "1", 12.0], ["notebook", "1", 6.0], ["pen", "1", 4.0]], "tools": ["none"], "steps": ["pick practical theme", "wrap onesie", "notebook for milestones", "card"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Coffee Lover", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beans", "1", 12.0], ["mug", "1", 10.0], ["french press", "1", 25.0]], "tools": ["none"], "steps": ["fresh beans", "mug chosen", "brew guide card", "bundle"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Reader", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["book", "1", 18.0], ["bookmark", "1", 5.0], ["tea", "1", 8.0]], "tools": ["none"], "steps": ["pick by their shelf", "bookmark handmade", "caddy tea", "wrap"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Gardener", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["seeds", "1", 10.0], ["gloves", "1", 12.0], ["trowel", "1", 14.0]], "tools": ["none"], "steps": ["zone-right seeds", "quality gloves", "trowel", "tote"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the New Homeowner", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tool set", "1", 30.0], ["plant", "1", 15.0], ["doormat", "1", 20.0]], "tools": ["none"], "steps": ["basic tools", "hardy plant", "mat", "card"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Fitness Friend", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bottle", "1", 18.0], ["towel", "1", 12.0], ["bands", "1", 15.0]], "tools": ["none"], "steps": ["insulated bottle", "quick-dry towel", "bands", "bag"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Artist", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["sketchbook", "1", 14.0], ["pencils", "1", 10.0], ["eraser", "1", 4.0]], "tools": ["none"], "steps": ["quality paper", "pencil set", "kneaded eraser", "wrap"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Cook", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["spice set", "1", 16.0], ["apron", "1", 20.0], ["towels", "1", 10.0]], "tools": ["none"], "steps": ["fresh spices", "apron", "towels", "recipe card"], "time": "2h", "level": "beginner", "safety": "check allergies for food gifts"},
  {"kind": "diy", "t": "Gift for the Traveler", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["packing cubes", "1", 20.0], ["journal", "1", 12.0], ["adapter", "1", 15.0]], "tools": ["none"], "steps": ["cubes set", "journal", "adapter", "pouch"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Music Lover", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["vinyl or CD", "1", 20.0], ["poster", "1", 12.0], ["picks", "1", 5.0]], "tools": ["none"], "steps": ["favorite album art", "poster", "picks", "wrap"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Gift for the Pet Owner", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["treats", "1", 10.0], ["toy", "1", 8.0], ["bandana", "1", 7.0]], "tools": ["none"], "steps": ["healthy treats", "durable toy", "bandana", "bag"], "time": "2h", "level": "beginner", "safety": "check pet allergies"},
  {"kind": "diy", "t": "Milestone Birthday (30/40/50)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["memory jar", "1", 10.0], ["photos", "1", 8.0], ["letters kit", "1", 6.0], ["box", "1", 12.0]], "tools": ["none"], "steps": ["collect 30 notes", "photos timeline", "letters from friends", "assemble"], "time": "8h", "level": "intermediate", "safety": "start collecting weeks early"},
  {"kind": "diy", "t": "Wedding Gift, Personal", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["frame", "1", 25.0], ["photo", "1", 10.0], ["vows print", "1", 15.0], ["box", "1", 10.0]], "tools": ["none"], "steps": ["favorite photo", "vows calligraphy print", "frame", "box"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Graduation Launch Kit", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["planner", "1", 18.0], ["gift card", "1", 25.0], ["pen set", "1", 12.0], ["tote", "1", 15.0]], "tools": ["none"], "steps": ["planner", "card", "pens", "tote"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "New Baby Keepsake", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["handprint kit", "1", 15.0], ["frame", "1", 18.0], ["journal", "1", 12.0]], "tools": ["none"], "steps": ["handprint art", "frame it", "journal for parents", "wrap"], "time": "4h", "level": "intermediate", "safety": "non-toxic kit only"},
  {"kind": "diy", "t": "Housewarming Custom Map", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["map print", "1", 20.0], ["frame", "1", 25.0], ["pins", "1", 5.0]], "tools": ["none"], "steps": ["map of meaningful place", "mark spots", "frame", "note"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Anniversary Timeline", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["prints", "10", 12.0], ["scrapbook", "1", 15.0], ["pens", "1", 8.0]], "tools": ["scissors"], "steps": ["timeline layout", "photos per year", "notes", "bind"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Retirement Adventure Fund", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 8.0], ["map", "1", 10.0], ["notes", "1", 5.0], ["box", "1", 8.0]], "tools": ["none"], "steps": ["adventure jar", "map marked", "notes from colleagues", "present"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Get-Well Comfort Box", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tea", "1", 10.0], ["socks", "1", 12.0], ["book", "1", 15.0], ["candle", "1", 12.0]], "tools": ["none"], "steps": ["soothing tea", "cozy socks", "light book", "candle"], "time": "3h", "level": "intermediate", "safety": "check scent sensitivities"},
  {"kind": "diy", "t": "Teacher Thank-You", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tote", "1", 12.0], ["supplies", "1", 15.0], ["card kit", "1", 6.0]], "tools": ["none"], "steps": ["tote", "classroom supplies", "handwritten card", "deliver"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Coach/mentor Tribute", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["frame", "1", 20.0], ["photo", "1", 8.0], ["letter", "1", 0.0], ["box", "1", 8.0]], "tools": ["none"], "steps": ["team photo", "letter", "frame", "box"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Long-Distance Love Box", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 10.0], ["letters", "12", 6.0], ["photos", "1", 8.0], ["small gifts", "1", 20.0]], "tools": ["none"], "steps": ["12 open-when letters", "photos", "small gifts", "ship"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Heirloom Recipe Collection", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["binder", "1", 15.0], ["dividers", "1", 8.0], ["photos", "1", 10.0], ["pens", "1", 8.0]], "tools": ["none"], "steps": ["collect family recipes", "test favorites", "handwrite", "photos"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Custom Star Map", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["star chart", "1", 25.0], ["frame", "1", 30.0]], "tools": ["none"], "steps": ["date and place", "generate chart", "frame museum style", "note"], "time": "4h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Handmade Quilt for Baby", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 40.0], ["batting", "1", 12.0], ["thread", "1", 8.0]], "tools": ["sewing"], "steps": ["choose theme", "piece top", "quilt", "bind"], "time": "30h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Wooden Memory Box", "tier": "Advanced", "notes": "ventilate", "mats": [["box kit", "1", 25.0], ["burner", "1", 0.0], ["stain", "1", 8.0]], "tools": ["burner"], "steps": ["assemble", "burn names/dates", "stain", "felt"], "time": "10h", "level": "advanced", "safety": "burner safety"},
  {"kind": "diy", "t": "Portrait Commission Gift", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["photo", "1", 0.0], ["frame", "1", 40.0]], "tools": ["none"], "steps": ["choose artist", "provide photos", "approve sketch", "frame"], "time": "6h", "level": "advanced", "safety": "commission early — artists book out"},
  {"kind": "diy", "t": "Experience Day Planned", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tickets", "1", 100.0], ["itinerary", "1", 0.0], ["card", "1", 5.0]], "tools": ["none"], "steps": ["plan full day", "book ahead", "itinerary card", "go"], "time": "8h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Family Cookbook Bound", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["printing", "1", 60.0], ["binder", "1", 15.0], ["photos", "1", 10.0]], "tools": ["none"], "steps": ["gather recipes", "edit and test", "print", "bind"], "time": "30h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Custom Jewelry Piece", "tier": "Advanced", "notes": "lead-free", "mats": [], "tools": ["none"], "steps": ["design consult", "approve wax", "final piece", "box"], "time": "4h", "level": "advanced", "safety": "reputable jeweler"},
  {"kind": "diy", "t": "Video Tribute Edited", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["software", "1", 0.0], ["clips", "1", 0.0]], "tools": ["computer"], "steps": ["collect clips", "edit story", "music licensed", "export"], "time": "20h", "level": "advanced", "safety": "licensed music only"},
  {"kind": "diy", "t": "Handwritten Book of Letters", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 15.0], ["binding", "1", 12.0], ["pens", "1", 10.0]], "tools": ["none"], "steps": ["20+ letters", "handwrite", "bind", "present"], "time": "25h", "level": "advanced", "safety": "start months early"},
  {"kind": "diy", "t": "Restored Family Photo Set", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["scans", "1", 0.0], ["printing", "1", 30.0], ["frames", "5", 50.0]], "tools": ["computer"], "steps": ["scan high-res", "restore", "print archival", "frame"], "time": "15h", "level": "advanced", "safety": "archival inks for longevity"},
  {"kind": "diy", "t": "Charity Donation in Name", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["card", "1", 5.0]], "tools": ["none"], "steps": ["choose meaningful cause", "donate", "card explains", "share"], "time": "2h", "level": "advanced", "safety": "verify charity legitimacy"}
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

