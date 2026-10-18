(function(){'use strict';
/* JAH The Candle Design Studio — real working generator, jahdb-gen-candle-design-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CNDL-";
var SLUG="gen-candle-design-studio";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry.", "ASTM F2417 (candle fire safety): proper wick sizing, warning labels, never leave burning unattended."];
var CITATIONS=["ASTM F2417, 'Standard Specification for Fire Safety for Candles.' ASTM International."];
var BANK=[
  {"kind": "diy", "t": "First Container Candle", "tier": "Foundations", "notes": "thermometer mandatory; keep from kids/pets", "mats": [["soy wax 2lb", "1", 14.0], ["jars", "3", 9.0], ["wicks", "1", 5.0], ["fragrance", "1", 10.0], ["thermometer", "1", 8.0]], "tools": ["double boiler"], "steps": ["melt 170F", "wick jars", "cool to 130F", "pour, cure 48h"], "time": "3h", "level": "beginner", "safety": "never leave melting wax"},
  {"kind": "diy", "t": "Teacup Candle", "tier": "Foundations", "notes": "cup must be heat-safe", "mats": [["teacup", "1", 8.0], ["wax", "1", 8.0], ["wick", "1", 2.0], ["scent", "1", 5.0]], "tools": ["double boiler"], "steps": ["clean cup", "wick", "pour", "trim"], "time": "2h", "level": "beginner", "safety": "wax safety"},
  {"kind": "diy", "t": "Beeswax Tapers (Dipped)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beeswax", "1", 18.0], ["wicking", "1", 5.0], ["pot", "1", 10.0]], "tools": ["double boiler"], "steps": ["melt wax", "dip wick repeatedly", "cool between", "trim"], "time": "4h", "level": "beginner", "safety": "hot wax burns — long sleeves, no water near wax"},
  {"kind": "diy", "t": "Votive Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 10.0], ["molds", "1", 8.0], ["wicks", "1", 4.0], ["scent", "1", 6.0]], "tools": ["double boiler"], "steps": ["melt", "wick molds", "pour", "cure"], "time": "3h", "level": "beginner", "safety": "wax safety"},
  {"kind": "diy", "t": "Wax Melts (Wickless)", "tier": "Foundations", "notes": "warmer safety card", "mats": [["wax", "1", 10.0], ["molds", "1", 8.0], ["fragrance", "1", 8.0]], "tools": ["double boiler"], "steps": ["melt", "scent", "pour shapes", "cure"], "time": "2h", "level": "beginner", "safety": "wax safety"},
  {"kind": "diy", "t": "Citronella Patio", "tier": "Foundations", "notes": "keep from pets", "mats": [["wax", "1", 12.0], ["jars", "1", 9.0], ["citronella oil", "1", 10.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["melt", "scent strong", "pour", "outdoor"], "time": "3h", "level": "beginner", "safety": "outdoor use"},
  {"kind": "diy", "t": "Layered Color Candle", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 12.0], ["dyes", "1", 8.0], ["jars", "1", 6.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["melt batches", "pour layers cool", "cure", "trim"], "time": "4h", "level": "beginner", "safety": "wax safety"},
  {"kind": "diy", "t": "Coffee Bean Candle", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 10.0], ["jar", "1", 5.0], ["beans", "1", 6.0], ["wick", "1", 2.0]], "tools": ["double boiler"], "steps": ["beans base", "wick", "pour", "top beans"], "time": "2h", "level": "beginner", "safety": "wax safety"},
  {"kind": "diy", "t": "Mason Jar Citrus", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 10.0], ["jar", "1", 4.0], ["oil", "1", 8.0], ["dried citrus", "1", 5.0]], "tools": ["double boiler"], "steps": ["melt", "scent", "pour", "decorate top"], "time": "3h", "level": "beginner", "safety": "dried botanicals away from wick"},
  {"kind": "diy", "t": "Emergency Candles", "tier": "Foundations", "notes": "burn attended", "mats": [["wax", "1", 12.0], ["tins", "1", 8.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["melt", "wick tins", "pour long burn", "store"], "time": "3h", "level": "beginner", "safety": "store cool"},
  {"kind": "diy", "t": "Shaped Floating Candles", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 10.0], ["molds", "1", 10.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["melt", "pour molds", "wick", "float test"], "time": "3h", "level": "beginner", "safety": "float test before gifting"},
  {"kind": "diy", "t": "Tealight Batch (24)", "tier": "Foundations", "notes": "trim wicks 1/4in", "mats": [["wax", "1", 10.0], ["cups", "24", 8.0], ["wicks", "1", 5.0], ["scent", "1", 6.0]], "tools": ["double boiler"], "steps": ["melt", "wick cups", "pour", "trim"], "time": "3h", "level": "beginner", "safety": "wax safety"},
  {"kind": "diy", "t": "Scent Blending Lab", "tier": "Compounded", "notes": "more is not better", "mats": [["oils", "6", 40.0], ["strips", "1", 5.0], ["wax", "1", 10.0]], "tools": ["none"], "steps": ["test ratios", "blot strips", "pick blend", "candle test"], "time": "6h", "level": "intermediate", "safety": "fragrance load: 6-10% soy"},
  {"kind": "diy", "t": "Wood Wick Candle", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 12.0], ["wood wicks", "1", 10.0], ["jars", "1", 9.0], ["scent", "1", 10.0]], "tools": ["double boiler"], "steps": ["melt", "wood wick tabs", "pour", "trim 1/8in"], "time": "4h", "level": "intermediate", "safety": "wood wicks need proper sizing — test burn"},
  {"kind": "diy", "t": "Marbled Candle", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 12.0], ["dyes", "1", 8.0], ["jars", "1", 6.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["pour base", "drizzle colors", "swirl", "cure"], "time": "4h", "level": "intermediate", "safety": "wax safety"},
  {"kind": "diy", "t": "Botanical Topped", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 12.0], ["jars", "1", 9.0], ["dried flowers", "1", 10.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["pour base", "arrange top (edges)", "cure", "trim"], "time": "4h", "level": "intermediate", "safety": "botanicals at edges, never near wick — fire risk"},
  {"kind": "diy", "t": "Pillar Candle", "tier": "Compounded", "notes": "relief holes", "mats": [["wax", "1", 14.0], ["mold", "1", 15.0], ["wick", "1", 3.0], ["scent", "1", 8.0]], "tools": ["double boiler"], "steps": ["mold release", "wick centered", "pour in stages", "unmold"], "time": "5h", "level": "intermediate", "safety": "pour in stages to avoid sinkholes"},
  {"kind": "diy", "t": "Trio Gift Set", "tier": "Compounded", "notes": "cure all 48h+", "mats": [["wax", "1", 16.0], ["jars", "3", 12.0], ["scents", "3", 24.0], ["wicks", "1", 6.0]], "tools": ["double boiler"], "steps": ["batch per scent", "pour set", "labels", "cure"], "time": "6h", "level": "intermediate", "safety": "label scents"},
  {"kind": "diy", "t": "Candle + Matches Set", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["candle", "1", 0.0], ["matchbox", "1", 3.0], ["labels", "1", 5.0]], "tools": ["none"], "steps": ["make candle", "decorate matches", "box set", "gift"], "time": "4h", "level": "intermediate", "safety": "matches safety note included"},
  {"kind": "diy", "t": "Geode Candle", "tier": "Compounded", "notes": "wick clear zone", "mats": [["wax", "1", 14.0], ["crystals", "1", 15.0], ["jar", "1", 6.0], ["dye", "1", 6.0]], "tools": ["double boiler"], "steps": ["pour base", "crystal cluster", "wax around", "finish"], "time": "5h", "level": "intermediate", "safety": "crystals heat-safe only"},
  {"kind": "diy", "t": "Dessert-Style Candle", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 14.0], ["whipped wax", "1", 0.0], ["jars", "1", 9.0], ["scent", "1", 10.0]], "tools": ["mixer"], "steps": ["base pour", "whip topping", "pipe on", "cherry"], "time": "5h", "level": "intermediate", "safety": "label clearly NOT FOOD"},
  {"kind": "diy", "t": "Outdoor Torch Candles", "tier": "Compounded", "notes": "stable surface", "mats": [["wax", "1", 14.0], ["tins", "1", 10.0], ["citronella", "1", 10.0], ["wicks", "1", 5.0]], "tools": ["double boiler"], "steps": ["melt", "strong scent", "pour tins", "outdoor"], "time": "4h", "level": "intermediate", "safety": "outdoor only"},
  {"kind": "diy", "t": "Massage Candle", "tier": "Compounded", "notes": "test patch; pour cool", "mats": [["soy wax", "1", 14.0], ["oils", "1", 15.0], ["tins", "1", 8.0]], "tools": ["double boiler"], "steps": ["low-temp wax", "s skin-safe oils", "pour", "cure"], "time": "4h", "level": "intermediate", "safety": "skin-safe fragrances only"},
  {"kind": "diy", "t": "Wax Melt Clamshells", "tier": "Compounded", "notes": "cure before closing", "mats": [["wax", "1", 12.0], ["clamshells", "12", 10.0], ["fragrance", "1", 10.0]], "tools": ["double boiler"], "steps": ["melt", "scent", "pour clams", "label"], "time": "3h", "level": "intermediate", "safety": "wax safety"},
  {"kind": "diy", "t": "Signature Scent Line (3)", "tier": "Advanced", "notes": "keep batch records", "mats": [["wax 10lb", "1", 50.0], ["oils", "1", 80.0], ["jars", "12", 36.0], ["labels", "1", 20.0]], "tools": ["double boiler"], "steps": ["develop 3 blends", "test burns", "labels", "batch"], "time": "20h", "level": "advanced", "safety": "test burn every scent"},
  {"kind": "diy", "t": "Carved Pillar Design", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["pillar wax", "1", 20.0], ["carving tools", "1", 25.0]], "tools": ["carving"], "steps": ["cast pillar", "carve design", "detail", "finish"], "time": "12h", "level": "advanced", "safety": "carve away from body"},
  {"kind": "diy", "t": "Chandelier Candles", "tier": "Advanced", "notes": "drip protection", "mats": [["wax", "1", 20.0], ["molds", "1", 20.0], ["wicks", "1", 8.0]], "tools": ["double boiler"], "steps": ["mold set", "pour", "assemble", "hang"], "time": "12h", "level": "advanced", "safety": "secure hanging"},
  {"kind": "diy", "t": "Wedding Favor Batch (50)", "tier": "Advanced", "notes": "cure time planned", "mats": [["wax 20lb", "1", 90.0], ["tins", "50", 75.0], ["wicks", "1", 20.0], ["scent", "1", 40.0], ["labels", "1", 30.0]], "tools": ["double boiler"], "steps": ["batch plan", "pour line", "wick all", "label"], "time": "30h", "level": "advanced", "safety": "batch consistency"},
  {"kind": "diy", "t": "Beeswax Sculpted", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["beeswax", "1", 30.0], ["molds", "1", 20.0]], "tools": ["double boiler"], "steps": ["sculpt", "mold", "cast", "finish"], "time": "16h", "level": "advanced", "safety": "hot wax safety"},
  {"kind": "diy", "t": "Candle Business Basics", "tier": "Advanced", "notes": "CLP-compliant labels", "mats": [["supplies", "1", 300.0], ["labels", "1", 50.0]], "tools": ["none"], "steps": ["costing", "testing", "safety labels", "sell"], "time": "20h", "level": "advanced", "safety": "insurance"},
  {"kind": "diy", "t": "Refillable Vessel Line", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["vessels", "1", 100.0], ["wax", "1", 60.0], ["wicks", "1", 25.0]], "tools": ["double boiler"], "steps": ["vessel design", "wick guide", "refill kits", "instructions"], "time": "20h", "level": "advanced", "safety": "wick guide per vessel — safety"},
  {"kind": "diy", "t": "Cold-Throw Optimization", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 30.0], ["oils", "1", 50.0]], "tools": ["none"], "steps": ["test temps", "document", "cure tests", "pick"], "time": "16h", "level": "advanced", "safety": "systematic testing beats guessing"},
  {"kind": "diy", "t": "Luxury Coconut-Soy Blend", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 40.0], ["vessels", "1", 60.0], ["oils", "1", 40.0]], "tools": ["double boiler"], "steps": ["blend wax", "vessel", "wick test", "luxury finish"], "time": "16h", "level": "advanced", "safety": "wick testing is the craft"},
  {"kind": "diy", "t": "Candle Making Workshop Kit", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["kits", "10", 200.0]], "tools": ["none"], "steps": ["kit design", "instructions", "safety", "teach"], "time": "16h", "level": "advanced", "safety": "safety briefing mandatory"}
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

