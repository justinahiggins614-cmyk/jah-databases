(function(){'use strict';
/* JAH The Collectors' Universe — real working generator, jahdb-db-collectors-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COLL-";
var SLUG="db-collectors";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value.", "ANA grading standards where applicable; document provenance for valuable pieces."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Why We Collect", "tier": "Foundations", "concept": "psychology of collecting", "mechanism": "completion, nostalgia, mastery drive collecting", "parts": ["join a forum"], "build": "read collector stories", "time": "4h", "level": "beginner", "safety": "none", "notes": "start with what you love"},
  {"kind": "gm", "t": "Choosing Your Focus", "tier": "Foundations", "concept": "narrow beats broad", "mechanism": "one theme deep beats ten shallow", "parts": ["pick 1"], "build": "list 3 passions", "time": "3h", "level": "beginner", "safety": "none", "notes": "focus = expertise"},
  {"kind": "gm", "t": "The Collector's Budget", "tier": "Foundations", "concept": "money discipline", "mechanism": "monthly cap + want list", "parts": ["track spending"], "build": "set budget", "time": "2h", "level": "beginner", "safety": "overspending", "notes": "collect within means"},
  {"kind": "gm", "t": "Where to Find Things", "tier": "Foundations", "concept": "sourcing", "mechanism": "thrift, estate, shows, online", "parts": ["compare prices"], "build": "visit 3 sources", "time": "6h", "level": "beginner", "safety": "fakes", "notes": "learn prices before buying"},
  {"kind": "gm", "t": "Condition Basics", "tier": "Foundations", "concept": "condition = value", "mechanism": "mint > excellent > good", "parts": ["practice grade"], "build": "study grading", "time": "4h", "level": "beginner", "safety": "none", "notes": "buy the best you can afford"},
  {"kind": "gm", "t": "Storage 101", "tier": "Foundations", "concept": "preservation", "mechanism": "cool, dark, dry, archival", "parts": ["move collection"], "build": "set up storage", "time": "4h", "level": "beginner", "safety": "none", "notes": "archival materials only"},
  {"kind": "gm", "t": "Cataloging Your Collection", "tier": "Foundations", "concept": "know what you own", "mechanism": "spreadsheet + photos", "parts": ["log details"], "build": "photograph all", "time": "8h", "level": "beginner", "safety": "none", "notes": "insurance needs inventory"},
  {"kind": "gm", "t": "Collector Communities", "tier": "Foundations", "concept": "people share knowledge", "mechanism": "clubs, forums, shows", "parts": ["attend show"], "build": "join 1 club", "time": "6h", "level": "beginner", "safety": "none", "notes": "mentors accelerate"},
  {"kind": "gm", "t": "The Thrill of the Hunt", "tier": "Foundations", "concept": "finding beats buying", "mechanism": "flea markets reward patience", "parts": ["log finds"], "build": "hunt weekly", "time": "6h", "level": "beginner", "safety": "none", "notes": "patience pays"},
  {"kind": "gm", "t": "Displaying Proudly", "tier": "Foundations", "concept": "show it well", "mechanism": "cases + lighting", "parts": ["install"], "build": "plan display", "time": "6h", "level": "beginner", "safety": "UV damage", "notes": "UV-filter glass"},
  {"kind": "gm", "t": "Gifting Duplicates", "tier": "Foundations", "concept": "share the joy", "mechanism": "trade + gift extras", "parts": ["gift"], "build": "sort dupes", "time": "2h", "level": "beginner", "safety": "none", "notes": "generosity builds community"},
  {"kind": "gm", "t": "Grading Like a Pro", "tier": "Compounded", "concept": "grades set prices", "mechanism": "learn published standards", "parts": ["grade 20 items"], "build": "study guides", "time": "10h", "level": "intermediate", "safety": "none", "notes": "grade honestly"},
  {"kind": "gm", "t": "Authentication Basics", "tier": "Compounded", "concept": "fakes exist", "mechanism": "maker marks + materials", "parts": ["verify buys"], "build": "study marks", "time": "10h", "level": "intermediate", "safety": "fakes", "notes": "buy from reputable"},
  {"kind": "gm", "t": "Estate Sale Strategy", "tier": "Compounded", "concept": "best sourcing", "mechanism": "arrive early, know values", "parts": ["attend 3"], "build": "research", "time": "12h", "level": "intermediate", "safety": "none", "notes": "day-2 discounts"},
  {"kind": "gm", "t": "Auction Tactics", "tier": "Compounded", "concept": "auctions reward discipline", "mechanism": "set max, stick to it", "parts": ["bid 1"], "build": "watch 2", "time": "8h", "level": "intermediate", "safety": "fever", "notes": "fees add 20%+"},
  {"kind": "gm", "t": "Trading Up", "tier": "Compounded", "concept": "improve holdings", "mechanism": "sell 3 good, buy 1 great", "parts": ["reinvest"], "build": "list sales", "time": "12h", "level": "intermediate", "safety": "none", "notes": "quality over quantity"},
  {"kind": "gm", "t": "Insurance for Collectibles", "tier": "Compounded", "concept": "protect value", "mechanism": "schedule + appraise", "parts": ["get quote"], "build": "inventory", "time": "6h", "level": "intermediate", "safety": "none", "notes": "photos + receipts"},
  {"kind": "gm", "t": "Taxes and Collecting", "tier": "Compounded", "concept": "sales have tax", "mechanism": "records + rules", "parts": ["consult pro"], "build": "log all", "time": "6h", "level": "intermediate", "safety": "none", "notes": "keep receipts 7 years"},
  {"kind": "gm", "t": "Restoration Ethics", "tier": "Compounded", "concept": "restore or not?", "mechanism": "originality vs beauty", "parts": ["decide per item"], "build": "study", "time": "8h", "level": "intermediate", "safety": "over-restore", "notes": "document everything"},
  {"kind": "gm", "t": "Provenance Research", "tier": "Compounded", "concept": "history adds value", "mechanism": "trace ownership", "parts": ["write up"], "build": "research 1 item", "time": "12h", "level": "intermediate", "safety": "none", "notes": "paper trails thrill"},
  {"kind": "gm", "t": "Specializing Deep", "tier": "Compounded", "concept": "expertise pays", "mechanism": "one niche mastery", "parts": ["study 1yr"], "build": "pick niche", "time": "20h", "level": "intermediate", "safety": "none", "notes": "be the expert"},
  {"kind": "gm", "t": "Selling Smart", "tier": "Compounded", "concept": "exit well", "mechanism": "grade + photo + venue", "parts": ["ship safe"], "build": "list 5", "time": "12h", "level": "intermediate", "safety": "scams", "notes": "reputation matters"},
  {"kind": "gm", "t": "Photographing for Insurance", "tier": "Compounded", "concept": "proof of value", "mechanism": "photos + list", "parts": ["file"], "build": "shoot", "time": "6h", "level": "intermediate", "safety": "none", "notes": "angle + detail shots"},
  {"kind": "gm", "t": "Appraisal Process", "tier": "Advanced", "concept": "know value", "mechanism": "certified appraisal", "parts": ["review"], "build": "hire appraiser", "time": "6h", "level": "advanced", "safety": "fees", "notes": "for insurance/estate"},
  {"kind": "gm", "t": "Museum Donation", "tier": "Advanced", "concept": "legacy giving", "mechanism": "deed + valuation", "parts": ["donate"], "build": "research", "time": "20h", "level": "advanced", "safety": "tax pro", "notes": "curators choose"},
  {"kind": "gm", "t": "Collection as Investment", "tier": "Advanced", "concept": "returns?", "mechanism": "rarity + demand drive", "parts": ["track 5yr"], "build": "study market", "time": "20h", "level": "advanced", "safety": "speculation", "notes": "buy love first, profit maybe"},
  {"kind": "gm", "t": "Heirloom Planning", "tier": "Advanced", "concept": "pass it on", "mechanism": "wills + stories", "parts": ["plan"], "build": "document", "time": "12h", "level": "advanced", "safety": "none", "notes": "stories = value"},
  {"kind": "gm", "t": "Curating an Exhibit", "tier": "Advanced", "concept": "share publicly", "mechanism": "theme + labels + loan", "parts": ["install"], "build": "propose", "time": "40h", "level": "advanced", "safety": "none", "notes": "libraries love exhibits"},
  {"kind": "gm", "t": "Writing the Guide", "tier": "Advanced", "concept": "publish expertise", "mechanism": "research + write", "parts": ["publish"], "build": "write", "time": "80h", "level": "advanced", "safety": "none", "notes": "the ultimate collection"},
  {"kind": "gm", "t": "Master Collector", "tier": "Advanced", "concept": "the long game", "mechanism": "50 years of focus", "parts": ["mentor"], "build": "reflect", "time": "40h", "level": "advanced", "safety": "none", "notes": "teach the next"},
  {"kind": "gm", "t": "Fraud Detection", "tier": "Advanced", "concept": "protect yourself", "mechanism": "forensics + marks", "parts": ["verify"], "build": "study cases", "time": "20h", "level": "advanced", "safety": "none", "notes": "trust but verify"},
  {"kind": "gm", "t": "Estate Planning", "tier": "Advanced", "concept": "after you", "mechanism": "inventory + wishes", "parts": ["file"], "build": "plan", "time": "12h", "level": "advanced", "safety": "lawyer", "notes": "don't burden heirs"},
  {"kind": "gm", "t": "Market Analysis", "tier": "Advanced", "concept": "timing matters", "mechanism": "cycles + trends", "parts": ["analyze"], "build": "track", "time": "20h", "level": "advanced", "safety": "none", "notes": "buy low, hold"},
  {"kind": "gm", "t": "Conservation Science", "tier": "Advanced", "concept": "preserve forever", "mechanism": "climate + materials", "parts": ["apply"], "build": "science", "time": "20h", "level": "advanced", "safety": "none", "notes": "museums set standard"}
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

