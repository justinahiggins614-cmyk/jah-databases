(function(){'use strict';
/* JAH The Shoe Design Lab — real working generator, jahdb-db-shoe-design-lab-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SDL-";
var SLUG="db-shoe-design-lab";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Sneaker Cleaning & Care", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cleaner kit", "1", 15.0], ["brushes", "1", 8.0], ["protector", "1", 10.0]], "tools": ["brush"], "steps": ["dry brush", "foam clean", "rinse", "protect"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Lace Styles Guide", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["laces 3 pairs", "1", 12.0]], "tools": ["none"], "steps": ["learn 5 styles", "match shoe", "thread", "tie"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Painted Canvas Sneakers", "tier": "Foundations", "notes": "test paint flex", "mats": [["canvas shoes", "1", 30.0], ["fabric paint", "1", 12.0], ["brushes", "1", 8.0]], "tools": ["brush"], "steps": ["clean shoes", "sketch design", "paint layers", "seal"], "time": "6h", "level": "beginner", "safety": "ventilate"},
  {"kind": "diy", "t": "Shoe Deodorizing", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["baking soda", "1", 3.0], ["tea bags", "1", 2.0]], "tools": ["none"], "steps": ["sprinkle soda", "overnight", "shake out", "tea bags store"], "time": "30m", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Insole Upgrade", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["insoles", "1", 20.0]], "tools": ["scissors"], "steps": ["remove stock", "trace size", "trim", "insert"], "time": "30m", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Waterproofing Boots", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wax", "1", 12.0], ["cloth", "1", 3.0], ["brush", "1", 5.0]], "tools": ["cloth"], "steps": ["clean boots", "warm wax", "rub in", "buff"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Decorative Shoe Clips", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["clips", "1", 6.0], ["gems", "1", 8.0], ["glue", "1", 4.0]], "tools": ["none"], "steps": ["design clip", "glue gems", "dry", "clip on"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Slip-On Conversion", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["lace-ups", "1", 0.0], ["elastic", "1", 6.0]], "tools": ["sewing"], "steps": ["remove laces", "elastic triangles", "sew", "test"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Shoe Painting Prep", "tier": "Foundations", "notes": "gloves", "mats": [["acetone", "1", 6.0], ["tape", "1", 4.0], ["sandpaper", "1", 4.0]], "tools": ["none"], "steps": ["tape soles", "deglaze leather", "sand lightly", "clean"], "time": "2h", "level": "beginner", "safety": "acetone ventilate"},
  {"kind": "diy", "t": "Custom Shoelace Charms", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["charms", "1", 8.0], ["wire", "1", 4.0]], "tools": ["pliers"], "steps": ["design", "wire loops", "attach", "wear"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Suede Care Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["suede kit", "1", 14.0]], "tools": ["brush"], "steps": ["dry brush", "eraser spots", "spray protect", "store"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Shoe Donation Refresh", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["used shoes", "1", 0.0], ["cleaner", "1", 10.0], ["laces", "1", 6.0]], "tools": ["brush"], "steps": ["clean", "new laces", "deodorize", "donate"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Full Sneaker Custom Paint", "tier": "Compounded", "notes": "respirator for airbrush", "mats": [["shoes", "1", 60.0], ["angelus paint", "1", 30.0], ["finisher", "1", 10.0], ["tape", "1", 5.0]], "tools": ["airbrush/brush"], "steps": ["prep deglaze", "tape", "base coats", "details, seal"], "time": "12h", "level": "intermediate", "safety": "ventilate"},
  {"kind": "diy", "t": "Sole Swap (Donor)", "tier": "Compounded", "notes": "clamp firmly", "mats": [["donor soles", "1", 25.0], ["shoes", "1", 40.0], ["glue", "1", 10.0], ["clamps", "1", 12.0]], "tools": ["clamps"], "steps": ["remove old sole", "prep surfaces", "glue, clamp 24h", "trim"], "time": "8h", "level": "intermediate", "safety": "strong glue ventilate"},
  {"kind": "diy", "t": "Leather Dye Job", "tier": "Compounded", "notes": "ventilate", "mats": [["dye", "1", 12.0], ["deglazer", "1", 8.0], ["finish", "1", 10.0], ["wool", "1", 4.0]], "tools": ["gloves"], "steps": ["deglaze", "dye coats", "dry", "finish"], "time": "6h", "level": "intermediate", "safety": "dye stains — gloves, cover area"},
  {"kind": "diy", "t": "Adding Ankle Strap", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoes", "1", 40.0], ["strap leather", "1", 10.0], ["buckle", "1", 6.0], ["rivets", "1", 5.0]], "tools": ["hole punch"], "steps": ["cut strap", "punch holes", "rivet", "test"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Platform Addition", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoes", "1", 50.0], ["platform soles", "1", 30.0], ["glue", "1", 10.0]], "tools": ["clamps"], "steps": ["prep sole", "glue platform", "clamp 24h", "edge finish"], "time": "8h", "level": "intermediate", "safety": "test stability before wearing out"},
  {"kind": "diy", "t": "Embroidered Sneakers", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoes", "1", 50.0], ["thread", "1", 8.0], ["needle", "1", 3.0]], "tools": ["needle"], "steps": ["sketch", "stitch design", "knot inside", "seal"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Boot Resole (Cobbler-Style)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["boots", "1", 80.0], ["soles", "1", 35.0], ["cement", "1", 12.0]], "tools": ["clamps"], "steps": ["remove worn sole", "prep", "contact cement both", "press 24h"], "time": "10h", "level": "intermediate", "safety": "contact cement — respirator, ventilation"},
  {"kind": "diy", "t": "Studded/Spiked Design", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoes", "1", 50.0], ["studs", "50", 15.0], ["tools", "1", 8.0]], "tools": ["pliers"], "steps": ["layout", "punch/screw", "even rows", "test"], "time": "5h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Two-Tone Color Block", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoes", "1", 60.0], ["paint", "1", 25.0], ["tape", "1", 5.0]], "tools": ["brush"], "steps": ["tape lines", "paint blocks", "detail", "seal"], "time": "10h", "level": "intermediate", "safety": "ventilate"},
  {"kind": "diy", "t": "Heel Cap Replacement", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["heels", "1", 40.0], ["heel tips", "1", 8.0], ["glue", "1", 8.0]], "tools": ["hammer"], "steps": ["remove caps", "glue new", "tap set", "test"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Perforated Brogue Pattern", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["shoes", "1", 70.0], ["punch set", "1", 18.0]], "tools": ["punch"], "steps": ["mark pattern", "punch holes", "edge paint", "finish"], "time": "8h", "level": "intermediate", "safety": "punch on hard surface"},
  {"kind": "diy", "t": "Shoe Last Basics", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["last pair", "1", 60.0]], "tools": ["none"], "steps": ["measure foot", "select last", "understand shapes", "plan"], "time": "4h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Hand-Sewn Moccasins", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["leather", "1", 45.0], ["thread", "1", 8.0], ["needle", "1", 6.0], ["pattern", "1", 12.0]], "tools": ["needle"], "steps": ["cut pattern", "punch holes", "saddle stitch", "sole"], "time": "20h", "level": "advanced", "safety": "sharp awl — punch away"},
  {"kind": "diy", "t": "Goodyear Welt Resole", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["boots", "1", 150.0], ["welt", "1", 20.0], ["soles", "1", 40.0], ["tools", "1", 60.0]], "tools": ["hammer"], "steps": ["remove sole", "stitch welt", "new sole", "finish"], "time": "16h", "level": "advanced", "safety": "specialized skill — practice on beaters"},
  {"kind": "diy", "t": "Bespoke Sneaker Pattern", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 80.0], ["lasts", "1", 60.0], ["tools", "1", 40.0]], "tools": ["none"], "steps": ["draft pattern", "cut", "stitch upper", "last and sole"], "time": "40h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Leather Boot from Scratch", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["leather", "1", 90.0], ["lasts", "1", 60.0], ["soles", "1", 40.0], ["tools", "1", 50.0]], "tools": ["hammer"], "steps": ["click patterns", "close upper", "last", "welt and sole"], "time": "60h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Patent Leather Finish", "tier": "Advanced", "notes": "dust-free area", "mats": [["shoes", "1", 80.0], ["patent coating", "1", 20.0]], "tools": ["spray"], "steps": ["prep glass-smooth", "coats thin", "level", "cure"], "time": "12h", "level": "advanced", "safety": "spray respirator"},
  {"kind": "diy", "t": "Hand-Welted Dress Shoe", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 150.0], ["tools", "1", 80.0]], "tools": ["awl"], "steps": ["pattern", "upper closed", "hand welt", "sole"], "time": "80h", "level": "advanced", "safety": "months of practice — start simple"},
  {"kind": "diy", "t": "Orthotic-Friendly Build", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 70.0]], "tools": ["none"], "steps": ["assess needs", "rocker sole", "wide last", "test walk"], "time": "30h", "level": "advanced", "safety": "consult professional for medical needs"},
  {"kind": "diy", "t": "3D-Printed Midsole", "tier": "Advanced", "notes": "TPU needs direct-drive; test fit before gluing", "mats": [["TPU", "1", 35.0], ["printer", "1", 0.0], ["design", "1", 0.0]], "tools": ["printer"], "steps": ["foot scan", "design lattice", "print 10-14h (estimate)", "assemble"], "time": "24h", "level": "advanced", "safety": "print times are estimates — midsoles print 10-14h at 0.2mm"},
  {"kind": "diy", "t": "Vintage Shoe Restoration", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["vintage", "1", 60.0], ["leather care", "1", 25.0], ["dye", "1", 15.0]], "tools": ["none"], "steps": ["assess", "clean deep", "recolor", "condition"], "time": "16h", "level": "advanced", "safety": "test products hidden spot first"},
  {"kind": "diy", "t": "Runway Concept Shoe", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["materials", "1", 120.0]], "tools": ["varies"], "steps": ["sketch concept", "prototype", "refine", "present"], "time": "50h", "level": "advanced", "safety": "none"}
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

