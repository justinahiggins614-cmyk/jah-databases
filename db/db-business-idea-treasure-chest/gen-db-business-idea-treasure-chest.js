(function(){'use strict';
/* JAH The Business Idea Treasure Chest — real working generator, jahdb-db-business-idea-treasure-chest-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BITC-";
var SLUG="db-business-idea-treasure-chest";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Osterwalder, Alexander and Pigneur, Yves. 'Business Model Generation.' Wiley, 2010.", "Ries, Eric. 'The Lean Startup.' Crown Business, 2011."];
var BANK=[
  {"kind": "gm", "t": "Idea vs Opportunity", "tier": "Foundations", "concept": "ideas cheap", "mechanism": "opportunity = idea + market", "parts": ["assess"], "build": "learn", "time": "4h", "level": "beginner", "safety": "none", "notes": "fall in love with problem"},
  {"kind": "gm", "t": "Problem First", "tier": "Foundations", "concept": "pain pays", "mechanism": "find real pains", "parts": ["list"], "build": "interview 10", "time": "8h", "level": "beginner", "safety": "none", "notes": "mom test: don't pitch"},
  {"kind": "gm", "t": "The One-Page Plan", "tier": "Foundations", "concept": "clarity", "mechanism": "problem/solution/money", "parts": ["refine"], "build": "write", "time": "4h", "level": "beginner", "safety": "none", "notes": "if not one page, unclear"},
  {"kind": "gm", "t": "Customers Before Product", "tier": "Foundations", "concept": "validate", "mechanism": "10 conversations", "parts": ["decide"], "build": "interview", "time": "10h", "level": "beginner", "safety": "none", "notes": "no compliments, seek truth"},
  {"kind": "gm", "t": "Pricing Basics", "tier": "Foundations", "concept": "charge right", "mechanism": "cost + value", "parts": ["test"], "build": "calculate", "time": "6h", "level": "beginner", "safety": "none", "notes": "charge more than comfortable"},
  {"kind": "gm", "t": "MVP Thinking", "tier": "Foundations", "concept": "smallest test", "mechanism": "concierge first", "parts": ["test"], "build": "build", "time": "12h", "level": "beginner", "safety": "none", "notes": "do things that don't scale"},
  {"kind": "gm", "t": "Side Hustle Start", "tier": "Foundations", "concept": "nights + weekends", "mechanism": "5hr/week", "parts": ["launch"], "build": "plan", "time": "10h", "level": "beginner", "safety": "none", "notes": "validate before quit"},
  {"kind": "gm", "t": "Freelance First", "tier": "Foundations", "concept": "sell skill", "mechanism": "profile + first client", "parts": ["deliver"], "build": "launch", "time": "12h", "level": "beginner", "safety": "none", "notes": "first client teaches"},
  {"kind": "gm", "t": "Local Service Biz", "tier": "Foundations", "concept": "nearby needs", "mechanism": "lawn/clean/fix", "parts": ["serve"], "build": "launch", "time": "12h", "level": "beginner", "safety": "insurance", "notes": "reviews = gold"},
  {"kind": "gm", "t": "Online Store (Simple)", "tier": "Foundations", "concept": "sell things", "mechanism": "niche + supplier", "parts": ["sell"], "build": "launch", "time": "20h", "level": "beginner", "safety": "none", "notes": "one product first"},
  {"kind": "gm", "t": "Content Business", "tier": "Foundations", "concept": "audience asset", "mechanism": "teach + publish", "parts": ["publish"], "build": "start", "time": "20h", "level": "beginner", "safety": "none", "notes": "100 posts before judge"},
  {"kind": "gm", "t": "SaaS (Tiny)", "tier": "Compounded", "concept": "software margins", "mechanism": "solve + charge", "parts": ["build"], "build": "validate", "time": "60h", "level": "intermediate", "safety": "none", "notes": "$29/mo x 100 = freedom"},
  {"kind": "gm", "t": "Marketplace (Niche)", "tier": "Compounded", "concept": "connect sides", "mechanism": "supply first", "parts": ["grow"], "build": "launch", "time": "60h", "level": "intermediate", "safety": "chicken-egg", "notes": "constrain geography"},
  {"kind": "gm", "t": "Subscription Box", "tier": "Compounded", "concept": "recurring joy", "mechanism": "curation + logistics", "parts": ["ship"], "build": "launch", "time": "40h", "level": "intermediate", "safety": "churn", "notes": "churn kills"},
  {"kind": "gm", "t": "Franchise (Study)", "tier": "Compounded", "concept": "system business", "mechanism": "FDD + math", "parts": ["analyze"], "build": "study", "time": "20h", "level": "intermediate", "safety": "fees", "notes": "talk to franchisees"},
  {"kind": "gm", "t": "E-commerce Brand", "tier": "Compounded", "concept": "brand + product", "mechanism": "differentiate", "parts": ["scale"], "build": "launch", "time": "60h", "level": "intermediate", "safety": "ads", "notes": "CAC < LTV"},
  {"kind": "gm", "t": "Agency Model", "tier": "Compounded", "concept": "sell service", "mechanism": "niche + results", "parts": ["deliver"], "build": "launch", "time": "40h", "level": "intermediate", "safety": "none", "notes": "productize service"},
  {"kind": "gm", "t": "Course Business", "tier": "Compounded", "concept": "teach once", "mechanism": "outcome + proof", "parts": ["sell"], "build": "create", "time": "40h", "level": "intermediate", "safety": "none", "notes": "transformation sells"},
  {"kind": "gm", "t": "App (No-Code)", "tier": "Compounded", "concept": "validate fast", "mechanism": "no-code build", "parts": ["launch"], "build": "build", "time": "40h", "level": "intermediate", "safety": "none", "notes": "users before code"},
  {"kind": "gm", "t": "Food Business", "tier": "Compounded", "concept": "taste + permits", "mechanism": "cottage laws", "parts": ["launch"], "build": "research", "time": "40h", "level": "intermediate", "safety": "food safety", "notes": "farmers market first"},
  {"kind": "gm", "t": "Real Estate (Rental)", "tier": "Compounded", "concept": "cashflow", "mechanism": "analyze + buy", "parts": ["offer"], "build": "study", "time": "60h", "level": "intermediate", "safety": "debt", "notes": "1% rule start"},
  {"kind": "gm", "t": "Buying a Business", "tier": "Compounded", "concept": "skip startup", "mechanism": "search + diligence", "parts": ["buy"], "build": "search", "time": "100h", "level": "intermediate", "safety": "pro", "notes": "SBA loans"},
  {"kind": "gm", "t": "Vending Routes", "tier": "Compounded", "concept": "passive-ish", "mechanism": "locations + machines", "parts": ["launch"], "build": "research", "time": "40h", "level": "intermediate", "safety": "theft", "notes": "cash businesses"},
  {"kind": "gm", "t": "Laundromat (Study)", "tier": "Compounded", "concept": "cashflow classic", "mechanism": "math + location", "parts": ["analyze"], "build": "study", "time": "20h", "level": "intermediate", "safety": "none", "notes": "water bills!"},
  {"kind": "gm", "t": "Venture Scale", "tier": "Advanced", "concept": "big swings", "mechanism": "VC + growth", "parts": ["pitch"], "build": "study", "time": "100h", "level": "advanced", "safety": "dilution", "notes": "only for huge markets"},
  {"kind": "gm", "t": "Franchisor", "tier": "Advanced", "concept": "sell systems", "mechanism": "prove + document", "parts": ["sell"], "build": "build", "time": "200h", "level": "advanced", "safety": "legal", "notes": "FDD required"},
  {"kind": "gm", "t": "Roll-Up Strategy", "tier": "Advanced", "concept": "buy many", "mechanism": "acquire + integrate", "parts": ["execute"], "build": "plan", "time": "200h", "level": "advanced", "safety": "debt", "notes": "boring industries"},
  {"kind": "gm", "t": "IP Licensing", "tier": "Advanced", "concept": "rent ideas", "mechanism": "patent + license", "parts": ["license"], "build": "develop", "time": "100h", "level": "advanced", "safety": "legal", "notes": "provisional first"},
  {"kind": "gm", "t": "Social Enterprise", "tier": "Advanced", "concept": "profit + purpose", "mechanism": "model + mission", "parts": ["launch"], "build": "design", "time": "80h", "level": "advanced", "safety": "none", "notes": "measure impact"},
  {"kind": "gm", "t": "Holding Company", "tier": "Advanced", "concept": "portfolio", "mechanism": "acquire + hold", "parts": ["buy"], "build": "build", "time": "200h", "level": "advanced", "safety": "pro", "notes": "Berkshire model"},
  {"kind": "gm", "t": "Exit Planning", "tier": "Advanced", "concept": "sell well", "mechanism": "3yr prep", "parts": ["sell"], "build": "plan", "time": "100h", "level": "advanced", "safety": "pro", "notes": "buyers buy systems"},
  {"kind": "gm", "t": "Master Business Builder", "tier": "Advanced", "concept": "serial", "mechanism": "pattern + team", "parts": ["build"], "build": "reflect", "time": "200h", "level": "advanced", "safety": "none", "notes": "teach founders"},
  {"kind": "gm", "t": "Storage Units", "tier": "Advanced", "concept": "rent boxes", "mechanism": "develop + manage", "parts": ["analyze"], "build": "study", "time": "40h", "level": "advanced", "safety": "debt", "notes": "occupancy math"},
  {"kind": "gm", "t": "Car Wash (Express)", "tier": "Advanced", "concept": "subscriptions", "mechanism": "site + systems", "parts": ["analyze"], "build": "study", "time": "40h", "level": "advanced", "safety": "none", "notes": "membership model"}
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

