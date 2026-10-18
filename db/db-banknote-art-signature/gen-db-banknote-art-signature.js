(function(){'use strict';
/* JAH The Banknote Art Database — real working generator, jahdb-db-banknote-art-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BAS-";
var SLUG="db-banknote-art";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value.", "PMG grading standards for paper money condition; never clean or press collectible notes."];
var CITATIONS=["Friedberg, Arthur L. and Ira S. 'Paper Money of the United States.' Coin & Currency Institute.", "'Standard Catalog of World Paper Money.' Krause Publications."];
var BANK=[
  {"kind": "gm", "t": "Anatomy of a Banknote", "tier": "Foundations", "concept": "design elements", "mechanism": "portrait, guilloche, serial", "parts": ["identify parts"], "build": "study a bill", "time": "2h", "level": "beginner", "safety": "none", "notes": "every line is anti-counterfeit"},
  {"kind": "gm", "t": "Portraits on Money", "tier": "Foundations", "concept": "faces tell stories", "mechanism": "who + why chosen", "parts": ["write up"], "build": "research 5", "time": "4h", "level": "beginner", "safety": "none", "notes": "nations choose heroes"},
  {"kind": "gm", "t": "Guilloche Patterns", "tier": "Foundations", "concept": "mesmerizing lines", "mechanism": "geometric lathe work", "parts": ["sketch"], "build": "study", "time": "3h", "level": "beginner", "safety": "none", "notes": "impossible to photocopy well"},
  {"kind": "gm", "t": "Watermarks", "tier": "Foundations", "concept": "hidden images", "mechanism": "hold to light", "parts": ["log"], "build": "test bills", "time": "2h", "level": "beginner", "safety": "none", "notes": "the classic security"},
  {"kind": "gm", "t": "Serial Numbers", "tier": "Foundations", "concept": "unique IDs", "mechanism": "print runs tracked", "parts": ["collect"], "build": "study", "time": "2h", "level": "beginner", "safety": "none", "notes": "fancy numbers premium"},
  {"kind": "gm", "t": "Paper vs Polymer", "tier": "Foundations", "concept": "substrate matters", "mechanism": "feel + durability", "parts": ["test"], "build": "compare", "time": "2h", "level": "beginner", "safety": "none", "notes": "polymer lasts 2.5x"},
  {"kind": "gm", "t": "Colors and Symbolism", "tier": "Foundations", "concept": "color means", "mechanism": "national palettes", "parts": ["chart"], "build": "study 10", "time": "4h", "level": "beginner", "safety": "none", "notes": "color psychology"},
  {"kind": "gm", "t": "Microprinting", "tier": "Foundations", "concept": "tiny text", "mechanism": "loupe reveals", "parts": ["log"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "needs magnification"},
  {"kind": "gm", "t": "Holograms and Foils", "tier": "Foundations", "concept": "shifting images", "mechanism": "tilt to verify", "parts": ["log"], "build": "test", "time": "2h", "level": "beginner", "safety": "none", "notes": "optically variable"},
  {"kind": "gm", "t": "UV Features", "tier": "Foundations", "concept": "hidden glow", "mechanism": "UV light reveals", "parts": ["log"], "build": "test", "time": "2h", "level": "beginner", "safety": "UV safety", "notes": "secret inks"},
  {"kind": "gm", "t": "Collecting Starter Set", "tier": "Foundations", "concept": "begin right", "mechanism": "10 notes + album", "parts": ["organize"], "build": "buy", "time": "6h", "level": "beginner", "safety": "fakes", "notes": "start circulated"},
  {"kind": "gm", "t": "Grading Banknotes", "tier": "Compounded", "concept": "grades = value", "mechanism": "70-point scale", "parts": ["grade 20"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "centering + corners"},
  {"kind": "gm", "t": "Error Notes", "tier": "Compounded", "concept": "mistakes valuable", "mechanism": "misprints + miscuts", "parts": ["hunt"], "build": "study", "time": "10h", "level": "intermediate", "safety": "fakes", "notes": "genuine errors premium"},
  {"kind": "gm", "t": "Star Notes", "tier": "Compounded", "concept": "replacement rarity", "mechanism": "star = reprint", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "low runs valuable"},
  {"kind": "gm", "t": "Hyperinflation Notes", "tier": "Compounded", "concept": "history lesson", "mechanism": "trillion-dollar bills", "parts": ["collect"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "cheap + fascinating"},
  {"kind": "gm", "t": "Notgeld (Emergency)", "tier": "Compounded", "concept": "crisis money", "mechanism": "WWI German notes", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "art in crisis"},
  {"kind": "gm", "t": "Colonial Currency", "tier": "Compounded", "concept": "early America", "mechanism": "continental dollars", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "fakes", "notes": "history in paper"},
  {"kind": "gm", "t": "Confederate Notes", "tier": "Compounded", "concept": "civil war finance", "mechanism": "CSA issues", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "repros", "notes": "reproductions flood market"},
  {"kind": "gm", "t": "Occupation Money", "tier": "Compounded", "concept": "war issues", "mechanism": "military + camp", "parts": ["collect"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "dark history"},
  {"kind": "gm", "t": "Polymer Pioneers", "tier": "Compounded", "concept": "plastic revolution", "mechanism": "first polymer notes", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "Australia 1988 first"},
  {"kind": "gm", "t": "Commemorative Issues", "tier": "Compounded", "concept": "celebration notes", "mechanism": "limited + pretty", "parts": ["collect"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "buy from central banks"},
  {"kind": "gm", "t": "Artists of Banknotes", "tier": "Compounded", "concept": "engravers matter", "mechanism": "master engravers", "parts": ["research"], "build": "study", "time": "10h", "level": "intermediate", "safety": "none", "notes": "unsung artists"},
  {"kind": "gm", "t": "Serial Number Ladders", "tier": "Compounded", "concept": "fancy numbers", "mechanism": "patterns premium", "parts": ["hunt"], "build": "study", "time": "8h", "level": "intermediate", "safety": "none", "notes": "solids + ladders"},
  {"kind": "gm", "t": "Counterfeit Detection", "tier": "Advanced", "concept": "spot fakes", "mechanism": "feel + look + tilt", "parts": ["test"], "build": "train", "time": "12h", "level": "advanced", "safety": "none", "notes": "the 3-step check"},
  {"kind": "gm", "t": "Rare Star Runs", "tier": "Advanced", "concept": "holy grails", "mechanism": "low print runs", "parts": ["hunt"], "build": "study", "time": "20h", "level": "advanced", "safety": "fakes", "notes": "population reports"},
  {"kind": "gm", "t": "Specimen Notes", "tier": "Advanced", "concept": "printer samples", "mechanism": "SPECIMEN overprint", "parts": ["collect"], "build": "study", "time": "16h", "level": "advanced", "safety": "none", "notes": "rare by design"},
  {"kind": "gm", "t": "Uncut Sheets", "tier": "Advanced", "concept": "as printed", "mechanism": "sheets of 4-32", "parts": ["collect"], "build": "study", "time": "12h", "level": "advanced", "safety": "storage", "notes": "frame carefully"},
  {"kind": "gm", "t": "National Bank Notes", "tier": "Advanced", "concept": "US history", "mechanism": "chartered banks", "parts": ["collect"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "thousands of varieties"},
  {"kind": "gm", "t": "Large Size US", "tier": "Advanced", "concept": "horse blankets", "mechanism": "pre-1929 big notes", "parts": ["collect"], "build": "study", "time": "16h", "level": "advanced", "safety": "none", "notes": "art-sized money"},
  {"kind": "gm", "t": "World Masterpieces", "tier": "Advanced", "concept": "most beautiful", "mechanism": "vote + study", "parts": ["collect"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "Switzerland often wins"},
  {"kind": "gm", "t": "Paper Money Investing", "tier": "Advanced", "concept": "returns?", "mechanism": "rarity + grade", "parts": ["track"], "build": "study", "time": "20h", "level": "advanced", "safety": "speculation", "notes": "top pop premiums"},
  {"kind": "gm", "t": "Exhibit Curation", "tier": "Advanced", "concept": "show money", "mechanism": "theme + story", "parts": ["display"], "build": "curate", "time": "30h", "level": "advanced", "safety": "security", "notes": "narrative matters"},
  {"kind": "gm", "t": "Banknote Conservation", "tier": "Advanced", "concept": "preserve paper", "mechanism": "archival + climate", "parts": ["store"], "build": "apply", "time": "12h", "level": "advanced", "safety": "none", "notes": "never laminate"},
  {"kind": "gm", "t": "Master Numismatist", "tier": "Advanced", "concept": "the summit", "mechanism": "expertise + ethics", "parts": ["mentor"], "build": "study", "time": "60h", "level": "advanced", "safety": "none", "notes": "publish research"}
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

