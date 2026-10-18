(function(){'use strict';
/* JAH The Bead Pattern Database — real working generator, jahdb-db-bead-pattern-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BPS-";
var SLUG="db-bead-pattern";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Single-Strand Necklace", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 10.0], ["wire", "1", 4.0], ["clasp", "1", 3.0], ["crimps", "1", 2.0]], "tools": ["pliers"], "steps": ["string pattern", "crimp ends", "clasp", "test"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Stretch Bracelet", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 8.0], ["elastic", "1", 3.0], ["glue", "1", 2.0]], "tools": ["scissors"], "steps": ["string beads", "knot 3x", "glue knot", "trim"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Simple Earrings", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 6.0], ["headpins", "1", 3.0], ["ear wires", "1", 4.0]], "tools": ["pliers"], "steps": ["bead on pin", "loop top", "attach wire", "pair"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Bookmark with Beads", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 5.0], ["cord", "1", 3.0], ["tassel", "1", 2.0]], "tools": ["none"], "steps": ["cord through", "beads pattern", "tassel end", "knot"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Keychain Charm", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 6.0], ["keyring", "1", 2.0], ["wire", "1", 3.0]], "tools": ["pliers"], "steps": ["design dangle", "wire wrap", "ring on", "test"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Anklet", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 7.0], ["wire", "1", 4.0], ["clasp", "1", 3.0]], "tools": ["pliers"], "steps": ["measure ankle", "pattern", "clasp", "fit"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Beaded Pen", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 5.0], ["pen", "1", 3.0]], "tools": ["none"], "steps": ["disassemble top", "thread beads", "reassemble", "write"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Wine Charms Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 8.0], ["rings", "6", 4.0]], "tools": ["pliers"], "steps": ["theme per charm", "wire rings", "set of 6", "box"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Zipper Pulls", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 5.0], ["cord", "1", 2.0]], "tools": ["none"], "steps": ["cord loop", "beads", "knot", "attach"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Plant Hanger Beads", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 8.0], ["cord", "1", 5.0]], "tools": ["none"], "steps": ["cut cords", "bead accents", "knot hanger", "hang"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Beaded Suncatcher", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 10.0], ["ring", "1", 4.0], ["line", "1", 3.0]], "tools": ["none"], "steps": ["ring frame", "strands varied", "hang", "sun"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Loom Bracelet", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["loom", "1", 15.0], ["beads", "1", 10.0], ["thread", "1", 4.0]], "tools": ["loom"], "steps": ["warp loom", "weave rows", "pattern chart", "finish ends"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Peyote Stitch Cuff", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["delicas", "1", 14.0], ["thread", "1", 4.0], ["needle", "1", 3.0], ["clasp", "1", 5.0]], "tools": ["needle"], "steps": ["even-count start", "rows build", "pattern", "clasp"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Brick Stitch Earrings", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["delicas", "1", 10.0], ["thread", "1", 4.0], ["wires", "1", 4.0]], "tools": ["needle"], "steps": ["ladder base", "rows off", "shape", "wires"], "time": "5h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Herringbone Rope", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 12.0], ["thread", "1", 4.0]], "tools": ["needle"], "steps": ["two-bead start", "Ndebele rows", "rope forms", "clasp"], "time": "8h", "level": "intermediate", "safety": "tension even"},
  {"kind": "diy", "t": "Right-Angle Weave Bracelet", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 12.0], ["thread", "1", 4.0]], "tools": ["needle"], "steps": ["RAW units", "join strip", "pattern", "clasp"], "time": "7h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Beaded Bezel Pendant", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cabochon", "1", 10.0], ["delicas", "1", 10.0], ["backing", "1", 4.0]], "tools": ["needle"], "steps": ["bezel rows", "backing", "edge", "bail"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Spiral Rope Necklace", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["beads 2 colors", "1", 12.0], ["thread", "1", 4.0]], "tools": ["needle"], "steps": ["core beads", "spiral wrap", "length", "clasp"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Daisy Chain Bracelet", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 8.0], ["thread", "1", 3.0]], "tools": ["needle"], "steps": ["daisy units", "connect", "length", "clasp"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Wire-Wrapped Pendant", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["stone", "1", 12.0], ["wire", "1", 8.0]], "tools": ["pliers"], "steps": ["cage design", "wrap", "bail", "polish"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Beaded Lanyard", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 10.0], ["cord", "1", 5.0], ["clip", "1", 3.0]], "tools": ["none"], "steps": ["pattern plan", "knot beads", "clip", "test"], "time": "4h", "level": "intermediate", "safety": "breakaway clip for safety"},
  {"kind": "diy", "t": "Memory Wire Bracelet", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["memory wire", "1", 6.0], ["beads", "1", 10.0]], "tools": ["pliers"], "steps": ["cut coils", "bead on", "loop ends", "wear"], "time": "2h", "level": "intermediate", "safety": "wire ends sharp — loop well"},
  {"kind": "diy", "t": "Bead Embroidery Brooch", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cabochon", "1", 12.0], ["beads", "1", 14.0], ["backing", "1", 5.0], ["pin", "1", 3.0]], "tools": ["needle"], "steps": ["glue cab", "bead rows", "backing", "pin"], "time": "10h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Peyote Tapestry Panel", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["delicas", "1", 40.0], ["thread", "1", 6.0], ["frame", "1", 15.0]], "tools": ["loom/needle"], "steps": ["chart design", "weave panel", "frame", "hang"], "time": "30h", "level": "advanced", "safety": "chart first — no improvising"},
  {"kind": "diy", "t": "3D Beaded Ornament", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 15.0], ["thread", "1", 5.0]], "tools": ["needle"], "steps": ["geometric units", "assemble 3D", "tension", "hang"], "time": "12h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Beaded Bridal Set", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["pearls", "1", 35.0], ["crystals", "1", 25.0], ["findings", "1", 15.0]], "tools": ["needle/pliers"], "steps": ["design suite", "necklace", "earrings", "bracelet"], "time": "25h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Soutache Pendant", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cord", "1", 10.0], ["beads", "1", 12.0], ["cab", "1", 12.0], ["backing", "1", 5.0]], "tools": ["needle"], "steps": ["cord shapes", "bead accents", "cab center", "back"], "time": "12h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Beaded Box with Lid", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["delicas", "1", 25.0], ["thread", "1", 6.0]], "tools": ["needle"], "steps": ["base weave", "walls up", "lid", "fit"], "time": "20h", "level": "advanced", "safety": "even tension critical"},
  {"kind": "diy", "t": "Huichol-Style Bowl", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["bowl", "1", 10.0], ["beads", "1", 30.0], ["wax", "1", 8.0]], "tools": ["none"], "steps": ["wax base", "press beads", "pattern", "seal"], "time": "25h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Beaded Collar Necklace", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 30.0], ["thread", "1", 6.0], ["clasp", "1", 8.0]], "tools": ["needle"], "steps": ["netted base", "fringe layers", "clasp", "fit"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Russian Spiral Lariat", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 20.0], ["thread", "1", 5.0]], "tools": ["needle"], "steps": ["spiral stitch", "long rope", "ends finished", "style"], "time": "15h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Beaded Evening Bag", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["frame", "1", 20.0], ["beads", "1", 45.0], ["fabric", "1", 10.0]], "tools": ["needle"], "steps": ["fabric base", "bead cover", "frame on", "line"], "time": "40h", "level": "advanced", "safety": "plan weight — beaded bags are heavy"},
  {"kind": "diy", "t": "Millefiori Bead Making", "tier": "Advanced", "notes": "bake ventilate", "mats": [["polymer canes", "1", 20.0], ["blade", "1", 8.0], ["roller", "1", 10.0]], "tools": ["blade"], "steps": ["cane slices", "bead cores", "apply slices", "bake"], "time": "10h", "level": "advanced", "safety": "blade safety"},
  {"kind": "diy", "t": "Beaded Sculpture", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["beads", "1", 40.0], ["wire armature", "1", 10.0]], "tools": ["pliers"], "steps": ["armature", "bead skin", "details", "base"], "time": "35h", "level": "advanced", "safety": "none"}
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

