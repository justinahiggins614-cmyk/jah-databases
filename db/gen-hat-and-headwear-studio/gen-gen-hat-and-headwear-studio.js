(function(){'use strict';
/* JAH The Hat and Headwear Studio — real working generator, jahdb-gen-hat-and-headwear-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HAHS-";
var SLUG="gen-hat-and-headwear-studio";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Beanie (Knit, Basic)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["yarn", "1", 10.0], ["needles", "1", 8.0]], "tools": ["knitting"], "steps": ["gauge swatch", "cast on", "knit tube", "decrease crown"], "time": "8h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Beanie (Crochet)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["yarn", "1", 10.0], ["hook", "1", 5.0]], "tools": ["crochet"], "steps": ["magic ring", "increase rounds", "straight sides", "close"], "time": "6h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Headband (Knit)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["yarn", "1", 6.0], ["needles", "1", 0.0]], "tools": ["knitting"], "steps": ["cast on", "garter rows", "bind off", "seam"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Sun Hat (Straw Kit)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["straw blank", "1", 18.0], ["ribbon", "1", 5.0], ["glue", "1", 4.0]], "tools": ["none"], "steps": ["shape crown", "ribbon band", "bow", "fit"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Fascinator Base", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 8.0], ["feathers", "1", 10.0], ["clip", "1", 3.0], ["glue", "1", 4.0]], "tools": ["glue gun"], "steps": ["cover base", "feather spray", "clip under", "try on"], "time": "3h", "level": "beginner", "safety": "glue gun burns — low temp for beginners"},
  {"kind": "diy", "t": "Paper Party Hats", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 5.0], ["elastic", "1", 3.0], ["decor", "1", 5.0]], "tools": ["scissors"], "steps": ["cone shape", "elastic", "decorate", "wear"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Sleep Cap", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 8.0], ["elastic", "1", 3.0]], "tools": ["sewing"], "steps": ["cut pattern", "sew seam", "casing elastic", "finish"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Bandana Styles", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bandanas", "3", 12.0]], "tools": ["none"], "steps": ["learn 5 folds", "fit", "tie", "style"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Winter Ear Warmer", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["fleece", "1", 8.0]], "tools": ["sewing"], "steps": ["cut band", "sew", "turn", "wear"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Baseball Cap Refresh", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cap", "1", 15.0], ["paint", "1", 10.0], ["patches", "1", 8.0]], "tools": ["brush"], "steps": ["clean", "paint or patch", "seal", "wear"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Bucket Hat (Sew)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["fabric 1yd", "1", 12.0]], "tools": ["sewing"], "steps": ["cut 5 pieces", "sew crown", "brim layers", "topstitch"], "time": "5h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Headwrap Styles", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["scarves", "3", 15.0]], "tools": ["none"], "steps": ["learn wraps", "fit", "style", "wear"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Fedora Reshape", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["felt blank", "1", 35.0], ["steam", "1", 0.0], ["ribbon", "1", 6.0]], "tools": ["steamer"], "steps": ["steam crown", "shape", "ribbon band", "dry"], "time": "4h", "level": "intermediate", "safety": "steam burns — gloves"},
  {"kind": "diy", "t": "Cloche (Felted)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wool roving", "1", 18.0], ["resist", "1", 5.0], ["soap", "1", 3.0]], "tools": ["felting"], "steps": ["lay roving", "wet felt", "shape on form", "dry"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Top Hat (Costume)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["buckram", "1", 10.0], ["fabric", "1", 12.0], ["pattern", "1", 8.0]], "tools": ["sewing"], "steps": ["cut buckram", "cover fabric", "brim", "assemble"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Beret (Knit)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["yarn", "1", 12.0], ["needles", "1", 0.0]], "tools": ["knitting"], "steps": ["cast on many", "decrease circle", "block", "stem"], "time": "10h", "level": "intermediate", "safety": "blocking needs patience"},
  {"kind": "diy", "t": "Newsboy Cap", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 14.0], ["pattern", "1", 10.0], ["interfacing", "1", 5.0]], "tools": ["sewing"], "steps": ["cut 8 panels", "sew crown", "brim", "button top"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Sun Hat (Sewn Wide Brim)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 14.0], ["brim wire", "1", 5.0], ["pattern", "1", 10.0]], "tools": ["sewing"], "steps": ["crown", "wide brim", "wire edge", "band"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Turban Wrap Style", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["jersey 2yd", "1", 16.0]], "tools": ["none"], "steps": ["cut length", "wrap technique", "tuck", "style"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Cowboy Hat Reshape", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["felt hat", "1", 60.0], ["steam", "1", 0.0]], "tools": ["steamer"], "steps": ["steam brim", "shape curl", "cool set", "band"], "time": "3h", "level": "intermediate", "safety": "steam burns"},
  {"kind": "diy", "t": "Pillbox Hat", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["buckram", "1", 8.0], ["fabric", "1", 10.0], ["veil", "1", 8.0]], "tools": ["sewing"], "steps": ["oval base", "cover", "veil", "comb"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Deerstalker", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tweed", "1", 18.0], ["pattern", "1", 12.0], ["lining", "1", 8.0]], "tools": ["sewing"], "steps": ["6 panels", "earflaps", "bows", "line"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Swim Cap Decorated", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cap", "1", 10.0], ["waterproof paint", "1", 12.0]], "tools": ["brush"], "steps": ["clean", "paint", "seal", "swim"], "time": "4h", "level": "intermediate", "safety": "paint fully cured before water"},
  {"kind": "diy", "t": "Bowler (Felt Kit)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["felt hood", "1", 40.0], ["block", "1", 25.0], ["ribbon", "1", 8.0]], "tools": ["steamer"], "steps": ["block hood", "shape brim", "ribbon", "sweatband"], "time": "12h", "level": "advanced", "safety": "hat blocks are an investment"},
  {"kind": "diy", "t": "Top Hat (Fur Felt)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fur felt", "1", 80.0], ["block", "1", 0.0], ["silk", "1", 15.0]], "tools": ["steamer"], "steps": ["block crown", "brim curl", "silk top", "finish"], "time": "20h", "level": "advanced", "safety": "fur felt needs careful steam"},
  {"kind": "diy", "t": "Derby with Veiling", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 15.0], ["veiling", "1", 12.0], ["feathers", "1", 15.0]], "tools": ["sewing"], "steps": ["cover base", "drape veiling", "feather trim", "comb"], "time": "10h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Historical Tricorn", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["felt", "1", 45.0], ["pattern", "1", 12.0], ["trim", "1", 10.0]], "tools": ["sewing"], "steps": ["cut crown", "fold brim 3", "trim edge", "cock"], "time": "14h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Witch Hat (Structured)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["buckram", "1", 10.0], ["fabric", "1", 15.0], ["wire", "1", 5.0]], "tools": ["sewing"], "steps": ["cone wired", "brim", "cover", "bend tip"], "time": "10h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Crown/tiara (Wirework)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["wire", "1", 12.0], ["beads", "1", 15.0], ["band", "1", 8.0]], "tools": ["pliers"], "steps": ["frame", "bead wraps", "symmetry", "finish"], "time": "12h", "level": "advanced", "safety": "wire ends tucked"},
  {"kind": "diy", "t": "Viking Cap (Faux Fur)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["faux fur", "1", 20.0], ["lining", "1", 10.0], ["pattern", "1", 10.0]], "tools": ["sewing"], "steps": ["cut fur", "sew", "line", "fit"], "time": "8h", "level": "advanced", "safety": "fur sheds — cut from back"},
  {"kind": "diy", "t": "Ascot Cap Pattern", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["wool", "1", 20.0], ["pattern", "1", 12.0], ["lining", "1", 10.0]], "tools": ["sewing"], "steps": ["panels", "sew", "lining", "press"], "time": "10h", "level": "advanced", "safety": "pressing matters"},
  {"kind": "diy", "t": "Headdress (Statement)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["base", "1", 15.0], ["mixed media", "1", 30.0]], "tools": ["varies"], "steps": ["concept", "structure", "surface", "balance"], "time": "16h", "level": "advanced", "safety": "weight balanced for wear"},
  {"kind": "diy", "t": "Panama-Style Weave", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["straw", "1", 40.0], ["block", "1", 0.0]], "tools": ["none"], "steps": ["weave crown", "brim", "block", "trim"], "time": "30h", "level": "advanced", "safety": "true panama weaving is master-level"},
  {"kind": "diy", "t": "Mad Hatter Top Hat", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["buckram", "1", 12.0], ["fabric", "1", 18.0], ["patchwork", "1", 10.0], ["cards", "1", 5.0]], "tools": ["sewing"], "steps": ["tall crown", "patchwork cover", "cards trim", "finish"], "time": "16h", "level": "advanced", "safety": "none"}
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

