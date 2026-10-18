(function(){'use strict';
/* JAH The Toy Design Studio — real working generator, jahdb-gen-toy-design-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TDS-";
var SLUG="gen-toy-design-studio";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry.", "ASTM F963 (toy safety) and CPSIA: no small parts for under-3s, non-toxic finishes, choke-tube test all parts."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Sock Puppet Character", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["socks", "2", 4.0], ["felt", "1", 5.0], ["glue", "1", 4.0], ["googly eyes", "1", 3.0]], "tools": ["scissors"], "steps": ["design character", "felt features", "glue details", "name it"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Cardboard Box Guitar", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["rubber bands", "1", 3.0], ["dowel", "1", 2.0]], "tools": ["cutter"], "steps": ["cut sound hole", "band strings", "dowel neck", "tune by tension"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Felt Board Story Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["felt 5 colors", "1", 10.0], ["board", "1", 8.0], ["scissors", "1", 0.0]], "tools": ["scissors"], "steps": ["cut characters", "board backing", "story cards", "play"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Balloon Rocket Racer", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["balloons", "1", 4.0], ["straw", "1", 1.0], ["tape", "1", 2.0], ["string", "1", 2.0]], "tools": ["none"], "steps": ["thread straw on string", "tape balloon", "release!", "race"], "time": "1h", "level": "beginner", "safety": "none — supervise small parts"},
  {"kind": "diy", "t": "Paper Bag Puppets", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bags", "5", 4.0], ["markers", "1", 6.0], ["glue", "1", 3.0]], "tools": ["scissors"], "steps": ["draw face on flap", "cut accessories", "glue on", "perform"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "DIY Kaleidoscope", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tube", "1", 3.0], ["mirror card", "1", 6.0], ["beads", "1", 3.0], ["tape", "1", 2.0]], "tools": ["scissors"], "steps": ["triangle mirrors", "bead cell", "tape tube", "twist view"], "time": "2h", "level": "beginner", "safety": "tape mirror edges"},
  {"kind": "diy", "t": "Wind-Up Paper Butterfly", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 2.0], ["rubber band", "1", 1.0], ["wire", "1", 2.0]], "tools": ["pliers"], "steps": ["fold wings", "rubber band motor", "wire body", "wind and release"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Marble Run from Tubes", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["paper tubes", "10", 0.0], ["tape", "1", 3.0], ["marbles", "1", 4.0]], "tools": ["scissors"], "steps": ["cut tubes half", "tape track", "test slope", "finish line"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Beanbag Toss Game", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 6.0], ["beans", "1", 4.0], ["box", "1", 0.0], ["paint", "1", 5.0]], "tools": ["sewing"], "steps": ["sew beanbags", "paint target box", "cut holes", "score"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Shadow Puppet Theater", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["paper", "1", 4.0], ["dowels", "1", 3.0], ["lamp", "1", 0.0]], "tools": ["cutter"], "steps": ["cut screen", "puppet silhouettes", "dowel handles", "perform"], "time": "4h", "level": "beginner", "safety": "lamp heat — LED only"},
  {"kind": "diy", "t": "Spinning Top Lathe (Hand)", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["dowel", "1", 2.0], ["paint", "1", 4.0], ["string", "1", 2.0]], "tools": ["none"], "steps": ["shape top", "cord wrap", "pull to spin", "paint designs"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Wooden Pull Toy", "tier": "Compounded", "notes": "non-toxic finish; no small parts for under-3", "mats": [["pine", "1", 8.0], ["wheels", "4", 6.0], ["axles", "1", 3.0], ["paint", "1", 6.0], ["non-toxic", "1", 0.0]], "tools": ["saw"], "steps": ["cut body shape", "sand smooth", "axle wheels", "paint non-toxic"], "time": "6h", "level": "intermediate", "safety": "sand splinter-free"},
  {"kind": "diy", "t": "Cloth Doll", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 10.0], ["stuffing", "1", 8.0], ["yarn", "1", 4.0], ["buttons", "1", 3.0]], "tools": ["sewing"], "steps": ["pattern cut", "sew and stuff", "yarn hair", "face embroidered"], "time": "8h", "level": "intermediate", "safety": "embroidered faces for under-3 (no buttons)"},
  {"kind": "diy", "t": "Peg Doll Family", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["peg dolls", "5", 10.0], ["paint", "1", 8.0], ["sealer", "1", 5.0]], "tools": ["brush"], "steps": ["sand pegs", "paint characters", "seal non-toxic", "felt capes"], "time": "5h", "level": "intermediate", "safety": "non-toxic paint and sealer"},
  {"kind": "diy", "t": "Balance Board", "tier": "Compounded", "notes": "clear space", "mats": [["plywood", "1", 18.0], ["dowel", "1", 4.0], ["sandpaper", "1", 4.0], ["non-slip", "1", 6.0]], "tools": ["saw"], "steps": ["cut board shape", "sand edges", "dowel fulcrum", "grip tape top"], "time": "4h", "level": "intermediate", "safety": "adult spotter"},
  {"kind": "diy", "t": "Toy Cash Register", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["buttons", "1", 6.0], ["drawer", "1", 4.0], ["play money", "1", 5.0]], "tools": ["cutter"], "steps": ["register body", "button panel", "drawer slides", "stock play money"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Magnetic Fishing Game", "tier": "Compounded", "notes": "supervise", "mats": [["dowels", "4", 6.0], ["magnets", "1", 8.0], ["felt fish", "10", 10.0], ["string", "1", 3.0]], "tools": ["sewing"], "steps": ["felt fish sewn", "magnet in nose", "rod with magnet", "pond box"], "time": "5h", "level": "intermediate", "safety": "magnets — keep from under-3"},
  {"kind": "diy", "t": "Play Food Set (Felt)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["felt", "1", 12.0], ["stuffing", "1", 6.0]], "tools": ["sewing"], "steps": ["cut food shapes", "sew and stuff", "details embroidered", "basket"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Toy Camera (Working Shutter)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["box", "1", 0.0], ["lens toy", "1", 5.0], ["shutter flap", "1", 2.0], ["strap", "1", 4.0]], "tools": ["cutter"], "steps": ["camera body", "viewfinder hole", "click shutter", "strap"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Dollhouse Furniture Set", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["balsa", "1", 12.0], ["fabric scraps", "1", 5.0], ["glue", "1", 4.0]], "tools": ["knife"], "steps": ["cut to 1:12", "assemble pieces", "upholster tiny", "arrange"], "time": "10h", "level": "intermediate", "safety": "knife safety"},
  {"kind": "diy", "t": "Wind-Up Car", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["wood", "1", 8.0], ["wheels", "1", 6.0], ["rubber band", "1", 2.0], ["axle", "1", 3.0]], "tools": ["saw"], "steps": ["chassis", "band motor", "wheels", "wind and go"], "time": "5h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Abacus", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["frame wood", "1", 10.0], ["dowels", "1", 4.0], ["beads", "50", 8.0]], "tools": ["drill"], "steps": ["frame build", "dowel rods", "10 beads each", "finish"], "time": "6h", "level": "intermediate", "safety": "beads secure — no loose small parts"},
  {"kind": "diy", "t": "3D-Printed Articulated Dragon", "tier": "Advanced", "notes": "ventilate; small parts — age 6+; check layer adhesion", "mats": [["PLA", "1", 22.0], ["printer", "1", 0.0], ["files", "1", 0.0]], "tools": ["printer"], "steps": ["choose articulated model", "slice 0.15mm", "print 8-12h (estimate)", "assemble links"], "time": "14h", "level": "advanced", "safety": "print times are estimates — 8-12h at 0.15mm, 20% infill"},
  {"kind": "diy", "t": "Wooden Train Set Pieces", "tier": "Advanced", "notes": "non-toxic finish; choke-test parts", "mats": [["hardwood", "1", 20.0], ["wheels", "1", 10.0], ["magnets", "1", 8.0], ["paint", "1", 10.0]], "tools": ["saw"], "steps": ["cut engine and cars", "sand perfectly", "magnet couplers", "paint non-toxic"], "time": "16h", "level": "advanced", "safety": "magnets enclosed"},
  {"kind": "diy", "t": "Dollhouse (Full)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plywood", "1", 35.0], ["trim", "1", 12.0], ["paint", "1", 15.0], ["wallpaper", "1", 10.0]], "tools": ["saw"], "steps": ["cut house shell", "assemble square", "trim and paint", "wallpaper rooms"], "time": "30h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Rocking Horse", "tier": "Advanced", "notes": "weight-tested; non-toxic finish", "mats": [["plywood", "1", 30.0], ["dowels", "1", 8.0], ["handles", "1", 10.0], ["paint", "1", 12.0]], "tools": ["saw"], "steps": ["cut horse profile", "legs and rockers", "sand smooth", "paint"], "time": "24h", "level": "advanced", "safety": "rockers stop-limited"},
  {"kind": "diy", "t": "Play Kitchen", "tier": "Advanced", "notes": "non-toxic paint", "mats": [["plywood", "1", 45.0], ["hardware", "1", 20.0], ["paint", "1", 18.0], ["faucet toy", "1", 10.0]], "tools": ["saw"], "steps": ["cabinet boxes", "door hinges", "sink and stove top", "paint"], "time": "30h", "level": "advanced", "safety": "tip-over anchor"},
  {"kind": "diy", "t": "Marble Machine", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plywood", "1", 25.0], ["marbles", "1", 8.0], ["dowels", "1", 6.0]], "tools": ["saw"], "steps": ["track layout", "lifts and funnels", "test each", "finish"], "time": "24h", "level": "advanced", "safety": "marbles — age 3+ only, supervise"},
  {"kind": "diy", "t": "Toy Crane (Working)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["wood", "1", 20.0], ["string", "1", 4.0], ["wheels", "1", 8.0], ["hook", "1", 3.0]], "tools": ["saw"], "steps": ["tower and jib", "pulley system", "winch crank", "load test"], "time": "20h", "level": "advanced", "safety": "string pinch supervision"},
  {"kind": "diy", "t": "Balance Bike (Wooden)", "tier": "Advanced", "notes": "adult assembly check; weight limit", "mats": [["plywood", "1", 35.0], ["wheels 12in", "1", 40.0], ["hardware", "1", 15.0]], "tools": ["saw"], "steps": ["frame cut", "fork and bars", "wheel mount", "test ride"], "time": "24h", "level": "advanced", "safety": "helmet required"},
  {"kind": "diy", "t": "Puppet Theater", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["plywood", "1", 30.0], ["curtain", "1", 12.0], ["paint", "1", 10.0]], "tools": ["saw"], "steps": ["stage frame", "curtain rod", "paint facade", "lighting"], "time": "20h", "level": "advanced", "safety": "LED lighting only"},
  {"kind": "diy", "t": "Toy Workbench", "tier": "Advanced", "notes": "rounded edges", "mats": [["2x4", "1", 25.0], ["plywood", "1", 20.0], ["vise toy", "1", 15.0], ["tools wooden", "1", 12.0]], "tools": ["saw"], "steps": ["bench build", "vise mounted", "tool storage", "finish"], "time": "24h", "level": "advanced", "safety": "real-tool supervision"},
  {"kind": "diy", "t": "RC Car (Simple)", "tier": "Advanced", "notes": "age 8+", "mats": [["chassis kit", "1", 40.0], ["motor", "1", 15.0], ["battery", "1", 18.0], ["radio", "1", 35.0]], "tools": ["soldering"], "steps": ["assemble chassis", "wire motor", "bind radio", "test drive"], "time": "20h", "level": "advanced", "safety": "LiPo charge supervised"},
  {"kind": "diy", "t": "Kaleidoscope Table", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tube large", "1", 10.0], ["mirrors", "1", 18.0], ["objects", "1", 8.0], ["stand", "1", 12.0]], "tools": ["saw"], "steps": ["big tube", "mirror triangle", "object wheel", "stand"], "time": "16h", "level": "advanced", "safety": "tape mirror edges"}
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

