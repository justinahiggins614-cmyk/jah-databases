(function(){'use strict';
/* JAH The Product Opportunity Finder — real working generator, jahdb-db-product-opportunity-finder-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-POFS-";
var SLUG="db-product-opportunity-finder";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Jobs to Be Done", "tier": "Foundations", "concept": "hire products", "mechanism": "progress + struggle", "parts": ["interview"], "build": "learn", "time": "8h", "level": "beginner", "safety": "none", "notes": "people hire products"},
  {"kind": "gm", "t": "Complaint Mining", "tier": "Foundations", "concept": "gold in gripes", "mechanism": "reviews 1-3 star", "parts": ["list"], "build": "mine 100", "time": "8h", "level": "beginner", "safety": "none", "notes": "sort by frequency"},
  {"kind": "gm", "t": "Workaround Watching", "tier": "Foundations", "concept": "hacks = opportunities", "mechanism": "watch + note", "parts": ["list"], "build": "observe", "time": "8h", "level": "beginner", "safety": "none", "notes": "spreadsheets everywhere"},
  {"kind": "gm", "t": "Niche Forums", "tier": "Foundations", "concept": "passions pay", "mechanism": "reddit + groups", "parts": ["list"], "build": "lurk", "time": "8h", "level": "beginner", "safety": "none", "notes": "complaints = roadmap"},
  {"kind": "gm", "t": "Search Trend Gaps", "tier": "Foundations", "concept": "rising queries", "mechanism": "trends + keywords", "parts": ["list"], "build": "research", "time": "6h", "level": "beginner", "safety": "none", "notes": "breakout = early"},
  {"kind": "gm", "t": "Regulation Creates", "tier": "Foundations", "concept": "laws = markets", "mechanism": "new rules", "parts": ["list"], "build": "track", "time": "6h", "level": "beginner", "safety": "none", "notes": "compliance products"},
  {"kind": "gm", "t": "Demographic Shifts", "tier": "Foundations", "concept": "people change", "mechanism": "aging + urban", "parts": ["list"], "build": "study", "time": "6h", "level": "beginner", "safety": "none", "notes": "follow the cohorts"},
  {"kind": "gm", "t": "Tech Enables", "tier": "Foundations", "concept": "new tech, new products", "mechanism": "AI + sensors", "parts": ["list"], "build": "study", "time": "8h", "level": "beginner", "safety": "none", "notes": "cheaper + smaller"},
  {"kind": "gm", "t": "Unbundling", "tier": "Foundations", "concept": "break bundles", "mechanism": "one feature great", "parts": ["list"], "build": "study", "time": "6h", "level": "beginner", "safety": "none", "notes": "Craigslist unbundled"},
  {"kind": "gm", "t": "Rebundling", "tier": "Foundations", "concept": "recombine", "mechanism": "super apps", "parts": ["list"], "build": "study", "time": "6h", "level": "beginner", "safety": "none", "notes": "wechat model"},
  {"kind": "gm", "t": "Copy + Improve", "tier": "Foundations", "concept": "better mousetrap", "mechanism": "clone + fix", "parts": ["list"], "build": "study", "time": "8h", "level": "beginner", "safety": "legal", "notes": "execution > idea"},
  {"kind": "gm", "t": "Market Sizing", "tier": "Compounded", "concept": "big enough?", "mechanism": "TAM/SAM/SOM", "parts": ["decide"], "build": "calculate", "time": "10h", "level": "intermediate", "safety": "none", "notes": "bottom-up beats top-down"},
  {"kind": "gm", "t": "Competitor Teardown", "tier": "Compounded", "concept": "know rivals", "mechanism": "buy + dissect", "parts": ["report"], "build": "teardown", "time": "16h", "level": "intermediate", "safety": "none", "notes": "their reviews = roadmap"},
  {"kind": "gm", "t": "Willingness to Pay", "tier": "Compounded", "concept": "charge what?", "mechanism": "van westendorp", "parts": ["price"], "build": "survey", "time": "12h", "level": "intermediate", "safety": "none", "notes": "ask money questions"},
  {"kind": "gm", "t": "Landing Page Test", "tier": "Compounded", "concept": "demand before build", "mechanism": "page + ads", "parts": ["measure"], "build": "test", "time": "20h", "level": "intermediate", "safety": "ad spend", "notes": "5% conversion = signal"},
  {"kind": "gm", "t": "Concierge MVP", "tier": "Compounded", "concept": "manual first", "mechanism": "do by hand", "parts": ["learn"], "build": "serve 10", "time": "20h", "level": "intermediate", "safety": "none", "notes": "learn before automate"},
  {"kind": "gm", "t": "Wizard of Oz", "tier": "Compounded", "concept": "fake backend", "mechanism": "humans behind", "parts": ["learn"], "build": "test", "time": "20h", "level": "intermediate", "safety": "none", "notes": "users don't know"},
  {"kind": "gm", "t": "Pre-Sales", "tier": "Compounded", "concept": "money talks", "mechanism": "sell before build", "parts": ["validate"], "build": "sell", "time": "20h", "level": "intermediate", "safety": "refunds", "notes": "10 pre-sales = go"},
  {"kind": "gm", "t": "Cohort Analysis", "tier": "Compounded", "concept": "retention truth", "mechanism": "cohorts", "parts": ["decide"], "build": "analyze", "time": "12h", "level": "intermediate", "safety": "none", "notes": "retention = product-market"},
  {"kind": "gm", "t": "Unit Economics", "tier": "Compounded", "concept": "math works?", "mechanism": "CAC + LTV + margin", "parts": ["decide"], "build": "model", "time": "12h", "level": "intermediate", "safety": "none", "notes": "LTV 3x CAC"},
  {"kind": "gm", "t": "Moat Thinking", "tier": "Compounded", "concept": "defensible?", "mechanism": "network + brand + scale", "parts": ["decide"], "build": "assess", "time": "10h", "level": "intermediate", "safety": "none", "notes": "moats compound"},
  {"kind": "gm", "t": "Timing Analysis", "tier": "Compounded", "concept": "why now?", "mechanism": "tech + behavior + law", "parts": ["decide"], "build": "assess", "time": "8h", "level": "intermediate", "safety": "none", "notes": "too early = dead"},
  {"kind": "gm", "t": "API Opportunities", "tier": "Compounded", "concept": "build on platforms", "mechanism": "gaps + docs", "parts": ["list"], "build": "study", "time": "12h", "level": "intermediate", "safety": "platform risk", "notes": "app store gaps"},
  {"kind": "gm", "t": "Aging Tech Replacement", "tier": "Compounded", "concept": "old systems die", "mechanism": "migrate + modernize", "parts": ["list"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "boring = profitable"},
  {"kind": "gm", "t": "Niche SaaS Mining", "tier": "Compounded", "concept": "tiny markets", "mechanism": "100 users x $100", "parts": ["list"], "build": "study", "time": "12h", "level": "intermediate", "safety": "none", "notes": "vertical depth"},
  {"kind": "gm", "t": "Platform Risk", "tier": "Advanced", "concept": "rented land?", "mechanism": "API + algorithm", "parts": ["mitigate"], "build": "assess", "time": "12h", "level": "advanced", "safety": "none", "notes": "own the customer"},
  {"kind": "gm", "t": "Regulatory Moats", "tier": "Advanced", "concept": "license = moat", "mechanism": "certifications", "parts": ["plan"], "build": "study", "time": "20h", "level": "advanced", "safety": "legal", "notes": "hard = defensible"},
  {"kind": "gm", "t": "Network Effects", "tier": "Advanced", "concept": "value grows", "mechanism": "design loops", "parts": ["build"], "build": "design", "time": "40h", "level": "advanced", "safety": "cold start", "notes": "seed supply first"},
  {"kind": "gm", "t": "Marketplace Dynamics", "tier": "Advanced", "concept": "two sides", "mechanism": "liquidity", "parts": ["launch"], "build": "design", "time": "60h", "level": "advanced", "safety": "none", "notes": "constrain to ignite"},
  {"kind": "gm", "t": "Blue Ocean", "tier": "Advanced", "concept": "no competition", "mechanism": "value innovation", "parts": ["create"], "build": "study", "time": "30h", "level": "advanced", "safety": "none", "notes": "eliminate + create"},
  {"kind": "gm", "t": "Disruption Theory", "tier": "Advanced", "concept": "from below", "mechanism": "overshoot + foothold", "parts": ["apply"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "incumbents flee up"},
  {"kind": "gm", "t": "Master Scout", "tier": "Advanced", "concept": "the eye", "mechanism": "pattern + reps", "parts": ["teach"], "build": "practice", "time": "100h", "level": "advanced", "safety": "none", "notes": "100 opportunities seen"},
  {"kind": "gm", "t": "Service Arbitrage", "tier": "Advanced", "concept": "buy low sell high", "mechanism": "offshore + local", "parts": ["list"], "build": "study", "time": "20h", "level": "advanced", "safety": "quality", "notes": "manage quality"},
  {"kind": "gm", "t": "Roll-Up Data", "tier": "Advanced", "concept": "fragmented markets", "mechanism": "acquire + systemize", "parts": ["list"], "build": "study", "time": "30h", "level": "advanced", "safety": "debt", "notes": "boring industries"}
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

