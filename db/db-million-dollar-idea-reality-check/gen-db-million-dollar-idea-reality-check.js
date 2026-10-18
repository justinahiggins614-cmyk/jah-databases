(function(){'use strict';
/* JAH The Million-Dollar Idea Reality Check — real working generator, jahdb-db-million-dollar-idea-reality-check-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDIRC-";
var SLUG="db-million-dollar-idea-reality-check";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Ries, Eric. 'The Lean Startup.' Crown Business, 2011.", "Malkiel, Burton G. 'A Random Walk Down Wall Street.' Norton, 12th ed."];
var BANK=[
  {"kind": "gm", "t": "The Idea Scorecard", "tier": "Foundations", "concept": "rate honestly", "mechanism": "10 factors", "parts": ["decide"], "build": "score", "time": "4h", "level": "beginner", "safety": "none", "notes": "kill fast, cheap"},
  {"kind": "gm", "t": "Market Size Math", "tier": "Foundations", "concept": "big enough?", "mechanism": "TAM bottom-up", "parts": ["decide"], "build": "calculate", "time": "6h", "level": "beginner", "safety": "none", "notes": "100M+ for venture"},
  {"kind": "gm", "t": "Competition Reality", "tier": "Foundations", "concept": "who else?", "mechanism": "map + moat", "parts": ["decide"], "build": "research", "time": "8h", "level": "beginner", "safety": "none", "notes": "no competition = no market?"},
  {"kind": "gm", "t": "Founder Fit", "tier": "Foundations", "concept": "why you?", "mechanism": "skills + network", "parts": ["decide"], "build": "assess", "time": "4h", "level": "beginner", "safety": "none", "notes": "unfair advantages"},
  {"kind": "gm", "t": "Timing Check", "tier": "Foundations", "concept": "why now?", "mechanism": "tech + behavior", "parts": ["decide"], "build": "assess", "time": "4h", "level": "beginner", "safety": "none", "notes": "too early kills"},
  {"kind": "gm", "t": "Money Math", "tier": "Foundations", "concept": "does it pay?", "mechanism": "unit economics", "parts": ["decide"], "build": "model", "time": "8h", "level": "beginner", "safety": "none", "notes": "LTV 3x CAC"},
  {"kind": "gm", "t": "The Mom Test", "tier": "Foundations", "concept": "truth serum", "mechanism": "ask right", "parts": ["learn"], "build": "interview", "time": "8h", "level": "beginner", "safety": "none", "notes": "compliments lie"},
  {"kind": "gm", "t": "Pre-Sell Test", "tier": "Foundations", "concept": "wallet votes", "mechanism": "sell first", "parts": ["decide"], "build": "sell", "time": "12h", "level": "beginner", "safety": "refunds", "notes": "10 buyers = real"},
  {"kind": "gm", "t": "The 10x Rule", "tier": "Foundations", "concept": "better enough?", "mechanism": "10x or niche", "parts": ["decide"], "build": "assess", "time": "4h", "level": "beginner", "safety": "none", "notes": "3x won't switch"},
  {"kind": "gm", "t": "Regulation Risk", "tier": "Foundations", "concept": "legal?", "mechanism": "rules + licenses", "parts": ["decide"], "build": "research", "time": "6h", "level": "beginner", "safety": "legal", "notes": "lawyer early"},
  {"kind": "gm", "t": "Cofounder Check", "tier": "Foundations", "concept": "team matters", "mechanism": "solo vs team", "parts": ["decide"], "build": "assess", "time": "4h", "level": "beginner", "safety": "none", "notes": "vesting 4yr"},
  {"kind": "gm", "t": "The App Idea", "tier": "Compounded", "concept": "everyone's app", "mechanism": "build cost + CAC", "parts": ["decide"], "build": "reality-check", "time": "10h", "level": "intermediate", "safety": "none", "notes": "$50k+ to build right"},
  {"kind": "gm", "t": "The Restaurant Dream", "tier": "Compounded", "concept": "food love", "mechanism": "90% fail stats", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "food truck first"},
  {"kind": "gm", "t": "The Invention", "tier": "Compounded", "concept": "patent + product", "mechanism": "provisional + license", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "license > manufacture"},
  {"kind": "gm", "t": "The Social Network", "tier": "Compounded", "concept": "next big social app", "mechanism": "cold start hell", "parts": ["decide"], "build": "reality-check", "time": "10h", "level": "intermediate", "safety": "none", "notes": "constrain to ignite"},
  {"kind": "gm", "t": "The Marketplace", "tier": "Compounded", "concept": "two-sided", "mechanism": "chicken-egg", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "supply first"},
  {"kind": "gm", "t": "The Hardware Dream", "tier": "Compounded", "concept": "atoms hard", "mechanism": "cost + inventory", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "10x software cost"},
  {"kind": "gm", "t": "The Franchise Dream", "tier": "Compounded", "concept": "be your boss", "mechanism": "fees + FDD", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "talk to failures"},
  {"kind": "gm", "t": "The Book Dream", "tier": "Compounded", "concept": "bestseller?", "mechanism": "advance math", "parts": ["decide"], "build": "reality-check", "time": "8h", "level": "intermediate", "safety": "none", "notes": "platform sells"},
  {"kind": "gm", "t": "The Course Dream", "tier": "Compounded", "concept": "passive income?", "mechanism": "launch work", "parts": ["decide"], "build": "reality-check", "time": "10h", "level": "intermediate", "safety": "none", "notes": "audience first"},
  {"kind": "gm", "t": "The SaaS", "tier": "Compounded", "concept": "recurring dream", "mechanism": "CAC + churn", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "churn kills"},
  {"kind": "gm", "t": "The Influencer", "tier": "Compounded", "concept": "fame pays?", "mechanism": "1% make it", "parts": ["decide"], "build": "reality-check", "time": "8h", "level": "intermediate", "safety": "none", "notes": "niche + years"},
  {"kind": "gm", "t": "The Coffee Shop Dream", "tier": "Compounded", "concept": "caffeine dream", "mechanism": "location math", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "200 cups/day breakeven"},
  {"kind": "gm", "t": "The Food Truck", "tier": "Compounded", "concept": "wheels + food", "mechanism": "permits + commissary", "parts": ["decide"], "build": "reality-check", "time": "12h", "level": "intermediate", "safety": "none", "notes": "14hr days"},
  {"kind": "gm", "t": "The Biotech Moonshot", "tier": "Advanced", "concept": "cure all", "mechanism": "10yr + $1B", "parts": ["decide"], "build": "reality-check", "time": "20h", "level": "advanced", "safety": "none", "notes": "team + papers"},
  {"kind": "gm", "t": "The Space Startup", "tier": "Advanced", "concept": "orbit dreams", "mechanism": "$100M+", "parts": ["decide"], "build": "reality-check", "time": "20h", "level": "advanced", "safety": "none", "notes": "government customer"},
  {"kind": "gm", "t": "The Fusion Bet", "tier": "Advanced", "concept": "star power", "mechanism": "physics + billions", "parts": ["decide"], "build": "reality-check", "time": "20h", "level": "advanced", "safety": "none", "notes": "decades"},
  {"kind": "gm", "t": "The City Builder", "tier": "Advanced", "concept": "new cities", "mechanism": "billions + politics", "parts": ["decide"], "build": "reality-check", "time": "20h", "level": "advanced", "safety": "none", "notes": "charter cities"},
  {"kind": "gm", "t": "The Honest Pivot", "tier": "Advanced", "concept": "change direction", "mechanism": "data + courage", "parts": ["pivot"], "build": "assess", "time": "12h", "level": "advanced", "safety": "ego", "notes": "sunk cost fallacy"},
  {"kind": "gm", "t": "The Graceful Kill", "tier": "Advanced", "concept": "end well", "mechanism": "learn + return", "parts": ["close"], "build": "decide", "time": "12h", "level": "advanced", "safety": "none", "notes": "fail fast, learn"},
  {"kind": "gm", "t": "The Overnight (10yr)", "tier": "Advanced", "concept": "success stories", "mechanism": "timeline truth", "parts": ["persist"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "10 years overnight"},
  {"kind": "gm", "t": "Master Checker", "tier": "Advanced", "concept": "the discipline", "mechanism": "check everything", "parts": ["teach"], "build": "practice", "time": "40h", "level": "advanced", "safety": "none", "notes": "kind candor"},
  {"kind": "gm", "t": "The Bar", "tier": "Advanced", "concept": "nightlife dream", "mechanism": "liquor license", "parts": ["decide"], "build": "reality-check", "time": "16h", "level": "advanced", "safety": "legal", "notes": "licenses $$$"},
  {"kind": "gm", "t": "The Gym Dream", "tier": "Advanced", "concept": "fitness passion", "mechanism": "retention math", "parts": ["decide"], "build": "reality-check", "time": "16h", "level": "advanced", "safety": "none", "notes": "January lie"}
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

