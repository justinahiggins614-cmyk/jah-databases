(function(){'use strict';
/* JAH The Toy Collectors Database — real working generator, jahdb-db-toy-collectors-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TOCOS-";
var SLUG="db-toy-collectors";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value.", "Learn AFA/CAS grading conventions for action figures; keep packaging when present."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Why Toys Endure", "tier": "Foundations", "concept": "nostalgia economy", "mechanism": "memories = value", "parts": ["journal"], "build": "reflect", "time": "2h", "level": "beginner", "safety": "none", "notes": "buy what you loved"},
  {"kind": "gm", "t": "Condition Grading", "tier": "Foundations", "concept": "grade matters", "mechanism": "C-10 scale", "parts": ["grade 10"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "box = half value"},
  {"kind": "gm", "t": "In-Box vs Loose", "tier": "Foundations", "concept": "packaging premium", "mechanism": "MIB vs played", "parts": ["decide"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "collect your way"},
  {"kind": "gm", "t": "Thrift Hunting", "tier": "Foundations", "concept": "cheap thrills", "mechanism": "thrift + garage", "parts": ["log"], "build": "hunt", "time": "6h", "level": "beginner", "safety": "none", "notes": "go weekly"},
  {"kind": "gm", "t": "Cleaning Vintage", "tier": "Foundations", "concept": "grime hides value", "mechanism": "gentle methods", "parts": ["photo"], "build": "clean 5", "time": "4h", "level": "beginner", "safety": "harsh chemicals", "notes": "test hidden spot"},
  {"kind": "gm", "t": "Storage Solutions", "tier": "Foundations", "concept": "preserve play", "mechanism": "bins + silica", "parts": ["store"], "build": "organize", "time": "4h", "level": "beginner", "safety": "none", "notes": "acid-free tissue"},
  {"kind": "gm", "t": "Price Guides", "tier": "Foundations", "concept": "know values", "mechanism": "sold listings", "parts": ["log"], "build": "research 10", "time": "4h", "level": "beginner", "safety": "none", "notes": "sold, not asking"},
  {"kind": "gm", "t": "Collector Forums", "tier": "Foundations", "concept": "knowledge shared", "mechanism": "join + lurk", "parts": ["ask"], "build": "join", "time": "4h", "level": "beginner", "safety": "none", "notes": "search before asking"},
  {"kind": "gm", "t": "First Display", "tier": "Foundations", "concept": "show them", "mechanism": "cases + shelves", "parts": ["install"], "build": "display", "time": "6h", "level": "beginner", "safety": "UV", "notes": "dust covers"},
  {"kind": "gm", "t": "Documenting Your Toys", "tier": "Foundations", "concept": "prove it", "mechanism": "photos + receipts", "parts": ["file"], "build": "photo all", "time": "6h", "level": "beginner", "safety": "none", "notes": "insurance inventory"},
  {"kind": "gm", "t": "Trading Basics", "tier": "Foundations", "concept": "swap dupes", "mechanism": "trade + meet", "parts": ["succeed"], "build": "trade 1", "time": "4h", "level": "beginner", "safety": "scams", "notes": "meet public"},
  {"kind": "gm", "t": "Action Figures (Vintage)", "tier": "Compounded", "concept": "80s gold", "mechanism": "line + variants", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "repro", "notes": "weapons = value"},
  {"kind": "gm", "t": "Die-Cast Cars", "tier": "Compounded", "concept": "tiny chrome", "mechanism": "redlines + treasure", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "fakes", "notes": "blister premium"},
  {"kind": "gm", "t": "Dolls (Collectible)", "tier": "Compounded", "concept": "porcelain + fashion", "mechanism": "marks + outfits", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "complete outfits"},
  {"kind": "gm", "t": "Model Trains", "tier": "Compounded", "concept": "iron horses", "mechanism": "gauge + era", "parts": ["collect"], "build": "study", "time": "16h", "level": "intermediate", "safety": "none", "notes": "run them!"},
  {"kind": "gm", "t": "Board Games (Vintage)", "tier": "Compounded", "concept": "cardboard gold", "mechanism": "complete + unpunched", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "count pieces"},
  {"kind": "gm", "t": "Video Games (Retro)", "tier": "Compounded", "concept": "pixels valuable", "mechanism": "complete in box", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "repro", "notes": "battery saves die"},
  {"kind": "gm", "t": "LEGO (Retired Sets)", "tier": "Compounded", "concept": "brick investing", "mechanism": "retired + sealed", "parts": ["track"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "sealed = premium"},
  {"kind": "gm", "t": "Comic Toys Tie-In", "tier": "Compounded", "concept": "plastic + paper", "mechanism": "cross-collect", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "synergy value"},
  {"kind": "gm", "t": "Tin Toys", "tier": "Compounded", "concept": "litho charm", "mechanism": "wind-up + friction", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "rust", "notes": "working = premium"},
  {"kind": "gm", "t": "Plush (Vintage)", "tier": "Compounded", "concept": "soft nostalgia", "mechanism": "tags + tush", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "moths", "notes": "clean carefully"},
  {"kind": "gm", "t": "Toy Authentication", "tier": "Compounded", "concept": "fakes flood", "mechanism": "marks + materials", "parts": ["verify"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "expert eyes"},
  {"kind": "gm", "t": "Plastic Color Variants", "tier": "Compounded", "concept": "chase variants", "mechanism": "color + stamp", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "variants multiply"},
  {"kind": "gm", "t": "Prototypes & Samples", "tier": "Advanced", "concept": "holy grails", "mechanism": "test shots + proofs", "parts": ["hunt"], "build": "study", "time": "30h", "level": "advanced", "safety": "fakes", "notes": "provenance critical"},
  {"kind": "gm", "t": "Factory Errors", "tier": "Advanced", "concept": "mistakes rare", "mechanism": "misprints + miscards", "parts": ["hunt"], "build": "study", "time": "20h", "level": "advanced", "safety": "custom", "notes": "factory provenance"},
  {"kind": "gm", "t": "Store Displays", "tier": "Advanced", "concept": "retail history", "mechanism": "displays + signage", "parts": ["collect"], "build": "study", "time": "20h", "level": "advanced", "safety": "space", "notes": "huge but cool"},
  {"kind": "gm", "t": "Original Art (Packaging)", "tier": "Advanced", "concept": "art before toy", "mechanism": "paintings + proofs", "parts": ["collect"], "build": "study", "time": "30h", "level": "advanced", "safety": "none", "notes": "one of one"},
  {"kind": "gm", "t": "Complete Runs", "tier": "Advanced", "concept": "every one", "mechanism": "full set chase", "parts": ["collect"], "build": "plan", "time": "60h", "level": "advanced", "safety": "none", "notes": "variants count"},
  {"kind": "gm", "t": "Museum Loans", "tier": "Advanced", "concept": "share history", "mechanism": "loan + exhibit", "parts": ["display"], "build": "arrange", "time": "30h", "level": "advanced", "safety": "insurance", "notes": "legacy"},
  {"kind": "gm", "t": "Price Database", "tier": "Advanced", "concept": "data wins", "mechanism": "track + analyze", "parts": ["track"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "your edge"},
  {"kind": "gm", "t": "Restoration (Pro)", "tier": "Advanced", "concept": "save damaged", "mechanism": "pro techniques", "parts": ["practice"], "build": "learn", "time": "30h", "level": "advanced", "safety": "value risk", "notes": "document before"},
  {"kind": "gm", "t": "Estate Hunting", "tier": "Advanced", "concept": "collections surface", "mechanism": "network + speed", "parts": ["buy"], "build": "hunt", "time": "30h", "level": "advanced", "safety": "cash", "notes": "be ready"},
  {"kind": "gm", "t": "Master Toy Collector", "tier": "Advanced", "concept": "the life", "mechanism": "focus + patience", "parts": ["mentor"], "build": "reflect", "time": "60h", "level": "advanced", "safety": "none", "notes": "teach"},
  {"kind": "gm", "t": "Box Art Gallery", "tier": "Advanced", "concept": "art before plastic", "mechanism": "displays", "parts": ["collect"], "build": "study", "time": "16h", "level": "advanced", "safety": "space", "notes": "frame the art"}
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

