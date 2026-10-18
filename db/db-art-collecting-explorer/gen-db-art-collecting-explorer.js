(function(){'use strict';
/* JAH The Art Collecting Explorer — real working generator, jahdb-db-art-collecting-explorer-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ACE-";
var SLUG="db-art-collecting-explorer";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Learning to Look", "tier": "Foundations", "concept": "seeing is skill", "mechanism": "slow looking", "parts": ["visit"], "build": "practice", "time": "6h", "level": "beginner", "safety": "none", "notes": "10 minutes per work"},
  {"kind": "gm", "t": "What Moves You", "tier": "Foundations", "concept": "taste personal", "mechanism": "notice reactions", "parts": ["reflect"], "build": "journal", "time": "4h", "level": "beginner", "safety": "none", "notes": "collect what you love"},
  {"kind": "gm", "t": "Prints vs Originals", "tier": "Foundations", "concept": "editions matter", "mechanism": "learn terms", "parts": ["compare"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "edition + signature"},
  {"kind": "gm", "t": "Local Artists First", "tier": "Foundations", "concept": "start near", "mechanism": "studios + fairs", "parts": ["buy 1"], "build": "visit", "time": "8h", "level": "beginner", "safety": "none", "notes": "relationships matter"},
  {"kind": "gm", "t": "Framing Basics", "tier": "Foundations", "concept": "frame = respect", "mechanism": "acid-free + UV", "parts": ["hang"], "build": "frame 1", "time": "4h", "level": "beginner", "safety": "none", "notes": "conservation framing"},
  {"kind": "gm", "t": "Hanging Art Well", "tier": "Foundations", "concept": "height matters", "mechanism": "57in center", "parts": ["level"], "build": "hang", "time": "2h", "level": "beginner", "safety": "none", "notes": "museum height"},
  {"kind": "gm", "t": "Art Under $100", "tier": "Foundations", "concept": "start small", "mechanism": "prints + smalls", "parts": ["buy"], "build": "hunt", "time": "6h", "level": "beginner", "safety": "none", "notes": "student shows gold"},
  {"kind": "gm", "t": "Caring for Art", "tier": "Foundations", "concept": "preserve", "mechanism": "light + humidity", "parts": ["adjust"], "build": "assess", "time": "4h", "level": "beginner", "safety": "none", "notes": "no direct sun"},
  {"kind": "gm", "t": "Documenting", "tier": "Foundations", "concept": "record it", "mechanism": "photos + receipts", "parts": ["file"], "build": "photo", "time": "2h", "level": "beginner", "safety": "none", "notes": "provenance starts now"},
  {"kind": "gm", "t": "Gallery Etiquette", "tier": "Foundations", "concept": "look + ask", "mechanism": "respect + curiosity", "parts": ["ask"], "build": "visit", "time": "4h", "level": "beginner", "safety": "none", "notes": "it's okay to ask prices"},
  {"kind": "gm", "t": "Art Books", "tier": "Foundations", "concept": "learn cheap", "mechanism": "library + monographs", "parts": ["study"], "build": "read", "time": "8h", "level": "beginner", "safety": "none", "notes": "knowledge compounds"},
  {"kind": "gm", "t": "Provenance", "tier": "Compounded", "concept": "history = value", "mechanism": "chain of ownership", "parts": ["verify"], "build": "research", "time": "12h", "level": "intermediate", "safety": "forgery", "notes": "paper trails"},
  {"kind": "gm", "t": "Condition Reports", "tier": "Compounded", "concept": "state matters", "mechanism": "examine + report", "parts": ["practice"], "build": "learn", "time": "8h", "level": "intermediate", "safety": "none", "notes": "raking light reveals"},
  {"kind": "gm", "t": "Auction Buying", "tier": "Compounded", "concept": "paddle up", "mechanism": "preview + limit", "parts": ["bid"], "build": "attend", "time": "12h", "level": "intermediate", "safety": "fever", "notes": "buyer's premium 25%"},
  {"kind": "gm", "t": "Working with Galleries", "tier": "Compounded", "concept": "relationships", "mechanism": "representation", "parts": ["inquire"], "build": "visit", "time": "10h", "level": "intermediate", "safety": "none", "notes": "ask about artists"},
  {"kind": "gm", "t": "Emerging Artists", "tier": "Compounded", "concept": "early = affordable", "mechanism": "research + visit", "parts": ["buy"], "build": "scout", "time": "20h", "level": "intermediate", "safety": "risk", "notes": "buy the best work"},
  {"kind": "gm", "t": "Photography Collecting", "tier": "Compounded", "concept": "lens art", "mechanism": "editions + prints", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "vintage vs contemporary"},
  {"kind": "gm", "t": "Sculpture (Small)", "tier": "Compounded", "concept": "3D collecting", "mechanism": "space + weight", "parts": ["buy"], "build": "study", "time": "12h", "level": "intermediate", "safety": "weight", "notes": "plan placement"},
  {"kind": "gm", "t": "Works on Paper", "tier": "Compounded", "concept": "fragile beauty", "mechanism": "care + framing", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "light", "notes": "UV museum glass"},
  {"kind": "gm", "t": "Art Fairs", "tier": "Compounded", "concept": "see everything", "mechanism": "plan + pace", "parts": ["buy"], "build": "attend", "time": "16h", "level": "intermediate", "safety": "fatigue", "notes": "preview day best"},
  {"kind": "gm", "t": "Commissions", "tier": "Compounded", "concept": "your vision", "mechanism": "artist + brief", "parts": ["enjoy"], "build": "commission", "time": "20h", "level": "intermediate", "safety": "contract", "notes": "50% deposit standard"},
  {"kind": "gm", "t": "Art as Gift", "tier": "Compounded", "concept": "give meaning", "mechanism": "know taste", "parts": ["give"], "build": "choose", "time": "6h", "level": "intermediate", "safety": "none", "notes": "receipt for exchange"},
  {"kind": "gm", "t": "Outsider Art", "tier": "Compounded", "concept": "raw vision", "mechanism": "self-taught", "parts": ["collect"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "authenticity rules"},
  {"kind": "gm", "t": "Blue-Chip (Study)", "tier": "Advanced", "concept": "top tier", "mechanism": "auction records", "parts": ["analyze"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "study, don't stretch"},
  {"kind": "gm", "t": "Authentication", "tier": "Advanced", "concept": "real or not?", "mechanism": "experts + science", "parts": ["verify"], "build": "learn", "time": "30h", "level": "advanced", "safety": "forgery", "notes": "catalogue raisonne"},
  {"kind": "gm", "t": "Estate Collections", "tier": "Advanced", "concept": "legacies", "mechanism": "appraise + plan", "parts": ["execute"], "build": "plan", "time": "30h", "level": "advanced", "safety": "tax pro", "notes": "donate or sell"},
  {"kind": "gm", "t": "Museum Relations", "tier": "Advanced", "concept": "give back", "mechanism": "loans + gifts", "parts": ["donate"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "curators remember"},
  {"kind": "gm", "t": "Art Funds (Study)", "tier": "Advanced", "concept": "pooled investing", "mechanism": "fees + risk", "parts": ["analyze"], "build": "study", "time": "20h", "level": "advanced", "safety": "risk", "notes": "love first"},
  {"kind": "gm", "t": "Conservation", "tier": "Advanced", "concept": "save art", "mechanism": "pro treatment", "parts": ["treat"], "build": "hire", "time": "20h", "level": "advanced", "safety": "none", "notes": "conservators = doctors"},
  {"kind": "gm", "t": "Curating Home", "tier": "Advanced", "concept": "live with art", "mechanism": "rotate + light", "parts": ["enjoy"], "build": "curate", "time": "20h", "level": "advanced", "safety": "none", "notes": "your museum"},
  {"kind": "gm", "t": "Legacy Collection", "tier": "Advanced", "concept": "after you", "mechanism": "plan + document", "parts": ["file"], "build": "plan", "time": "20h", "level": "advanced", "safety": "lawyer", "notes": "stories with pieces"},
  {"kind": "gm", "t": "Market Cycles", "tier": "Advanced", "concept": "timing", "mechanism": "trends + data", "parts": ["track"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "buy in downturns"},
  {"kind": "gm", "t": "Master Eye", "tier": "Advanced", "concept": "decades looking", "mechanism": "practice + travel", "parts": ["see"], "build": "travel", "time": "100h", "level": "advanced", "safety": "none", "notes": "see 10,000 works"},
  {"kind": "gm", "t": "Digital Art (NFTs?)", "tier": "Advanced", "concept": "pixels ownable", "mechanism": "research + caution", "parts": ["analyze"], "build": "study", "time": "16h", "level": "advanced", "safety": "speculation", "notes": "understand before buy"}
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

