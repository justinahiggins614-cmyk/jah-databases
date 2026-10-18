(function(){'use strict';
/* JAH The Paper Engineering Database — real working generator, jahdb-db-paper-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PE-";
var SLUG="db-paper-engineering";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Accordion-Fold Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "5", 4.0], ["bone folder", "1", 5.0], ["glue stick", "1", 3.0]], "tools": ["ruler"], "steps": ["mark equal divisions", "score with bone folder", "fold mountain-valley", "glue ends"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Simple Pop-Up Card", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "2", 3.0], ["craft knife", "1", 7.0], ["cutting mat", "1", 9.0], ["glue", "1", 3.0]], "tools": ["knife"], "steps": ["fold base card", "cut two parallel slits", "push tab inward", "glue shape to tab"], "time": "2h", "level": "beginner", "safety": "knife safety — fresh blades, cut on mat"},
  {"kind": "diy", "t": "Paper Box (No Glue)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["square paper 12in", "4", 4.0]], "tools": ["none"], "steps": ["fold diagonals both ways", "fold corners to center", "fold edges to center", "lock side walls"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Kirigami Snowflake", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["copy paper", "10", 2.0], ["scissors", "1", 5.0]], "tools": ["scissors"], "steps": ["fold triangle in thirds", "cut shapes from edges", "unfold carefully", "press flat"], "time": "1h", "level": "beginner", "safety": "scissor safety"},
  {"kind": "diy", "t": "Paper Airplane Science", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["copy paper", "20", 3.0]], "tools": ["none"], "steps": ["fold center crease", "fold nose layers", "wing folds symmetric", "test and trim"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Origami Crane", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["origami paper 6in", "20", 5.0]], "tools": ["none"], "steps": ["preliminary fold", "petal folds", "neck and tail pulls", "wing folds down"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Paper Chain Decor", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["construction paper", "20", 5.0], ["glue stick", "1", 3.0]], "tools": ["scissors"], "steps": ["cut 1x8in strips", "loop and glue first", "thread next through", "hang strands"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Pop-Up Mouth Card", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "2", 3.0], ["knife", "1", 0.0], ["glue", "1", 3.0]], "tools": ["knife"], "steps": ["cut V-fold mouth", "attach teeth strip", "jaw moves when opened", "decorate"], "time": "2h", "level": "beginner", "safety": "knife safety"},
  {"kind": "diy", "t": "Paper Beads", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["magazine pages", "5", 0.0], ["skewers", "1", 2.0], ["mod podge", "1", 8.0]], "tools": ["skewer"], "steps": ["cut long triangles", "roll on skewer", "seal with mod podge", "dry on rack"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Spiral Paper Mobile", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "6", 4.0], ["thread", "1", 3.0], ["embroidery hoop", "1", 5.0]], "tools": ["scissors"], "steps": ["cut graduated circles", "spiral cut each", "thread through center", "hang from hoop"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Layered Shadow Box Card", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock 5 layers", "1", 5.0], ["foam tape", "1", 4.0], ["LED tea light", "1", 2.0]], "tools": ["knife"], "steps": ["cut nested frames", "stack with foam tape", "scene inside", "light behind"], "time": "3h", "level": "beginner", "safety": "LED only"},
  {"kind": "diy", "t": "Pull-Tab Slider Card", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "3", 4.0], ["brad", "1", 2.0], ["knife", "1", 0.0]], "tools": ["knife"], "steps": ["cut channel slot", "tab with brad pivot", "image slides when pulled", "assemble layers"], "time": "3h", "level": "intermediate", "safety": "knife safety"},
  {"kind": "diy", "t": "Pop-Up House", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "4", 5.0], ["printed windows", "1", 2.0], ["glue", "1", 3.0]], "tools": ["knife"], "steps": ["box base with slit tabs", "roof V-folds", "window layers pop", "door swings"], "time": "4h", "level": "intermediate", "safety": "plan tab positions first"},
  {"kind": "diy", "t": "Kirigami Architecture", "tier": "Compounded", "notes": "patience", "mats": [["heavy paper", "5", 6.0], ["knife", "1", 0.0], ["mat", "1", 0.0]], "tools": ["knife"], "steps": ["draw facade grid", "cut windows precisely", "fold stories up", "back with contrast paper"], "time": "5h", "level": "intermediate", "safety": "sharp knife essential"},
  {"kind": "diy", "t": "Spinning Volvelle Wheel", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "3", 4.0], ["brad", "1", 2.0], ["printed dials", "1", 2.0]], "tools": ["knife"], "steps": ["cut two circles", "window in top disk", "brad center pivot", "calibrate alignment"], "time": "3h", "level": "intermediate", "safety": "test rotation before gluing"},
  {"kind": "diy", "t": "Paper Automata: Pecking Bird", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 4.0], ["cam wheel", "1", 1.0], ["axle dowel", "1", 2.0], ["glue", "1", 3.0]], "tools": ["knife"], "steps": ["build cam and follower", "bird on follower", "crank turns cam", "bird pecks"], "time": "6h", "level": "intermediate", "safety": "cam timing is everything — test dry"},
  {"kind": "diy", "t": "Pop-Up Carousel", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "6", 6.0], ["dowel", "1", 2.0], ["glue", "1", 3.0], ["paint", "1", 5.0]], "tools": ["knife"], "steps": ["hexagon tiers", "V-fold animals", "center pole dowel", "roof canopy"], "time": "8h", "level": "intermediate", "safety": "symmetric folds or it leans"},
  {"kind": "diy", "t": "Tunnel Book Scene", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "5", 5.0], ["knife", "1", 0.0], ["accordion sides", "1", 2.0]], "tools": ["knife"], "steps": ["cut frame layers", "accordion sides both", "align depth", "cover boards"], "time": "5h", "level": "intermediate", "safety": "keep frames parallel"},
  {"kind": "diy", "t": "Paper Lantern (LED)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["rice paper", "1", 6.0], ["bamboo strips", "1", 4.0], ["LED string", "1", 8.0], ["glue", "1", 3.0]], "tools": ["none"], "steps": ["bamboo frame", "paper panels glued", "LED inside (never flame)", "hang"], "time": "4h", "level": "intermediate", "safety": "LED ONLY — paper + flame is a fire hazard"},
  {"kind": "diy", "t": "Quilled Mandala", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["quilling strips", "1", 8.0], ["slotted tool", "1", 5.0], ["glue", "1", 3.0], ["board", "1", 4.0]], "tools": ["tool"], "steps": ["roll tight coils", "shape teardrops/eyes", "arrange mandala", "glue and frame"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Pop-Up City Skyline", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "8", 7.0], ["printed windows", "1", 3.0], ["glue", "1", 3.0]], "tools": ["knife"], "steps": ["building V-folds varied heights", "window strips", "street base", "opens flat"], "time": "7h", "level": "intermediate", "safety": "score before folding thick card"},
  {"kind": "diy", "t": "Mechanical Paper Gears", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["chipboard", "1", 6.0], ["brads", "1", 3.0], ["printed gear templates", "1", 2.0]], "tools": ["knife"], "steps": ["cut gear teeth carefully", "brad pivots", "mesh teeth", "crank drives train"], "time": "6h", "level": "intermediate", "safety": "tooth count must mesh — use template"},
  {"kind": "diy", "t": "Waterfall Card", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "4", 5.0], ["brads", "2", 3.0], ["printed panels", "4", 3.0]], "tools": ["knife"], "steps": ["mechanism strip with panels", "pull tab cascades", "align panel order", "decorate"], "time": "5h", "level": "advanced", "safety": "prototype mechanism in scrap first"},
  {"kind": "diy", "t": "Multi-Scene Pop-Up Book", "tier": "Advanced", "notes": "test every open/close", "mats": [["cardstock", "20", 12.0], ["book board", "1", 6.0], ["glue", "1", 5.0], ["printed art", "1", 5.0]], "tools": ["knife"], "steps": ["plan 4 spreads", "engineer each mechanism", "bind with tape hinge", "cover boards"], "time": "20h", "level": "advanced", "safety": "one spread at a time"},
  {"kind": "diy", "t": "Paper Engine: Walking Toy", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 5.0], ["linkages", "1", 2.0], ["brads", "1", 3.0]], "tools": ["knife"], "steps": ["four-bar linkage design", "legs on cranks", "push stick drives", "walks on table"], "time": "10h", "level": "advanced", "safety": "linkage geometry — prototype in cardboard"},
  {"kind": "diy", "t": "Kaleidoscope Book", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["mirror card", "1", 10.0], ["cardstock", "1", 5.0], ["beads", "1", 4.0], ["tube", "1", 3.0]], "tools": ["knife"], "steps": ["triangle mirror insert", "object cell with beads", "rotate for patterns", "bind as book"], "time": "8h", "level": "advanced", "safety": "mirror edges sharp — tape them"},
  {"kind": "diy", "t": "Pop-Up Globe", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 8.0], ["printed gores", "1", 4.0], ["brad", "1", 2.0], ["stand", "1", 5.0]], "tools": ["knife"], "steps": ["cut gore strips", "brad at poles", "opens to sphere", "stand mount"], "time": "8h", "level": "advanced", "safety": "gore math matters — 12 gores standard"},
  {"kind": "diy", "t": "Paper Clock with Hands", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 5.0], ["clock movement", "1", 9.0], ["hands", "1", 4.0], ["frame", "1", 6.0]], "tools": ["knife"], "steps": ["design clock face", "movement through center", "hands fitted", "frame"], "time": "6h", "level": "advanced", "safety": "movement shaft length must match thickness"},
  {"kind": "diy", "t": "Architectural Paper Model", "tier": "Advanced", "notes": "metal ruler as guide", "mats": [["museum board", "1", 18.0], ["knife blades", "1", 8.0], ["glue", "1", 5.0], ["plans", "1", 0.0]], "tools": ["knife"], "steps": ["scale plans 1:100", "cut walls precisely", "assemble floors", "roof and site"], "time": "30h", "level": "advanced", "safety": "sharp blades"},
  {"kind": "diy", "t": "Paper Automata Theater", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 10.0], ["cams and gears", "1", 8.0], ["crank", "1", 3.0], ["paint", "1", 8.0]], "tools": ["knife"], "steps": ["stage box", "two cam programs", "figures animated", "single crank drives all"], "time": "24h", "level": "advanced", "safety": "cam profiles drawn first, tested in scrap"},
  {"kind": "diy", "t": "Giant Pop-Up Installation", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["foam core", "10", 40.0], ["utility knife", "1", 9.0], ["hot glue", "1", 8.0]], "tools": ["knife"], "steps": ["scale up a card mechanism", "foam core structure", "test open/close cycles", "anchor base"], "time": "20h", "level": "advanced", "safety": "large mechanisms need counterweights"},
  {"kind": "diy", "t": "Paper Bridge Challenge", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "20", 10.0], ["weights for test", "1", 0.0], ["glue", "1", 4.0]], "tools": ["none"], "steps": ["design truss", "build deck and trusses", "test load gradually", "redesign weak joints"], "time": "8h", "level": "advanced", "safety": "none — test to failure safely"},
  {"kind": "diy", "t": "Origami Tessellation Art", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["large paper", "10", 12.0], ["bone folder", "1", 0.0]], "tools": ["none"], "steps": ["pre-crease grid", "collapse pleats", "tessellation pattern", "frame behind glass"], "time": "12h", "level": "advanced", "safety": "pre-creasing accuracy is everything"},
  {"kind": "diy", "t": "Pop-Up Botanical Study", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 8.0], ["printed botanicals", "1", 6.0], ["vellum", "1", 5.0], ["binding", "1", 6.0]], "tools": ["knife"], "steps": ["layered petal mechanisms", "vellum overlays", "labels", "bound volume"], "time": "18h", "level": "advanced", "safety": "botanical accuracy rewards research"}
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

