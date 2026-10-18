(function(){'use strict';
/* JAH The Bargain Hunter Database — real working generator, jahdb-db-bargain-hunter-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BH-";
var SLUG="db-bargain-hunter";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Malkiel, Burton G. 'A Random Walk Down Wall Street.' Norton, 12th ed."];
var BANK=[
  {"kind": "gm", "t": "The Bargain Mindset", "tier": "Foundations", "concept": "pay less on purpose", "mechanism": "research + patience", "parts": ["practice"], "build": "adopt", "time": "2h", "level": "beginner", "safety": "none", "notes": "never pay first price"},
  {"kind": "gm", "t": "Price Tracking", "tier": "Foundations", "concept": "know the price", "mechanism": "camel + alerts", "parts": ["buy low"], "build": "track 5", "time": "4h", "level": "beginner", "safety": "none", "notes": "history beats memory"},
  {"kind": "gm", "t": "Coupons That Work", "tier": "Foundations", "concept": "stack savings", "mechanism": "store + maker", "parts": ["use"], "build": "collect", "time": "4h", "level": "beginner", "safety": "none", "notes": "stacking = art"},
  {"kind": "gm", "t": "Cashback Basics", "tier": "Foundations", "concept": "paid to buy", "mechanism": "cards + apps", "parts": ["earn"], "build": "set up", "time": "4h", "level": "beginner", "safety": "debt", "notes": "pay in full always"},
  {"kind": "gm", "t": "Thrift Store Gold", "tier": "Foundations", "concept": "secondhand first", "mechanism": "thrift + estate", "parts": ["find"], "build": "hunt weekly", "time": "8h", "level": "beginner", "safety": "none", "notes": "go often"},
  {"kind": "gm", "t": "Clearance Cycles", "tier": "Foundations", "concept": "timing", "mechanism": "end-of-season", "parts": ["shop"], "build": "learn", "time": "4h", "level": "beginner", "safety": "none", "notes": "January + July"},
  {"kind": "gm", "t": "Warehouse Clubs", "tier": "Foundations", "concept": "bulk math", "mechanism": "unit price", "parts": ["calculate"], "build": "join", "time": "4h", "level": "beginner", "safety": "membership", "notes": "unit price rules"},
  {"kind": "gm", "t": "Refurbished Tech", "tier": "Foundations", "concept": "like new, less", "mechanism": "certified refurb", "parts": ["test"], "build": "buy", "time": "4h", "level": "beginner", "safety": "warranty", "notes": "manufacturer refurb"},
  {"kind": "gm", "t": "Grocery Savings", "tier": "Foundations", "concept": "food budget", "mechanism": "list + sales + bulk", "parts": ["shop"], "build": "plan", "time": "4h", "level": "beginner", "safety": "none", "notes": "list = law"},
  {"kind": "gm", "t": "DIY vs Buy", "tier": "Foundations", "concept": "make or buy", "mechanism": "cost + time", "parts": ["decide"], "build": "calculate", "time": "2h", "level": "beginner", "safety": "none", "notes": "hourly rate math"},
  {"kind": "gm", "t": "Library Everything", "tier": "Foundations", "concept": "free first", "mechanism": "books + tools + more", "parts": ["borrow"], "build": "join", "time": "2h", "level": "beginner", "safety": "none", "notes": "libraries lend tools"},
  {"kind": "gm", "t": "Coupon Apps", "tier": "Foundations", "concept": "phone savings", "mechanism": "stack apps", "parts": ["save"], "build": "install", "time": "4h", "level": "beginner", "safety": "none", "notes": "one trip, many apps"},
  {"kind": "gm", "t": "Buy Nothing Groups", "tier": "Foundations", "concept": "free first", "mechanism": "local groups", "parts": ["take"], "build": "join", "time": "4h", "level": "beginner", "safety": "none", "notes": "give before take"},
  {"kind": "gm", "t": "Bargain Negotiation Basics", "tier": "Compounded", "concept": "ask nicely", "mechanism": "research + ask", "parts": ["save"], "build": "practice", "time": "8h", "level": "intermediate", "safety": "none", "notes": "the worst is no"},
  {"kind": "gm", "t": "Car Buying", "tier": "Compounded", "concept": "biggest haggle", "mechanism": "out-the-door price", "parts": ["buy"], "build": "research", "time": "20h", "level": "intermediate", "safety": "none", "notes": "end of month"},
  {"kind": "gm", "t": "Home Haggle", "tier": "Compounded", "concept": "house prices", "mechanism": "comps + terms", "parts": ["negotiate"], "build": "offer", "time": "30h", "level": "intermediate", "safety": "none", "notes": "terms beat price"},
  {"kind": "gm", "t": "Travel Deals", "tier": "Compounded", "concept": "fly cheap", "mechanism": "flex + alerts", "parts": ["book"], "build": "track", "time": "10h", "level": "intermediate", "safety": "none", "notes": "Tuesday myth, flexibility real"},
  {"kind": "gm", "t": "Insurance Shopping", "tier": "Compounded", "concept": "yearly raise?", "mechanism": "shop yearly", "parts": ["switch"], "build": "compare", "time": "6h", "level": "intermediate", "safety": "coverage", "notes": "apples to apples"},
  {"kind": "gm", "t": "Phone Plans", "tier": "Compounded", "concept": "overpaying?", "mechanism": "MVNO + usage", "parts": ["switch"], "build": "analyze", "time": "4h", "level": "intermediate", "safety": "none", "notes": "usage first"},
  {"kind": "gm", "t": "Energy Switching", "tier": "Compounded", "concept": "rates vary", "mechanism": "compare + switch", "parts": ["save"], "build": "shop", "time": "4h", "level": "intermediate", "safety": "none", "notes": "fixed vs variable"},
  {"kind": "gm", "t": "Medical Bills", "tier": "Compounded", "concept": "bills negotiable", "mechanism": "itemize + ask", "parts": ["negotiate"], "build": "review", "time": "8h", "level": "intermediate", "safety": "none", "notes": "cash price lower"},
  {"kind": "gm", "t": "College Costs", "tier": "Compounded", "concept": "sticker vs net", "mechanism": "aid + appeal", "parts": ["appeal"], "build": "apply", "time": "20h", "level": "intermediate", "safety": "debt", "notes": "appeal aid offers"},
  {"kind": "gm", "t": "Furniture (Floor Models)", "tier": "Compounded", "concept": "display discount", "mechanism": "ask + inspect", "parts": ["buy"], "build": "hunt", "time": "8h", "level": "intermediate", "safety": "none", "notes": "20-40% off"},
  {"kind": "gm", "t": "Matress Buying", "tier": "Compounded", "concept": "mystery pricing", "mechanism": "test + negotiate", "parts": ["buy"], "build": "shop", "time": "10h", "level": "intermediate", "safety": "none", "notes": "holiday weekends"},
  {"kind": "gm", "t": "Price Mistakes", "tier": "Compounded", "concept": "glitch deals", "mechanism": "alerts + speed", "parts": ["buy"], "build": "hunt", "time": "8h", "level": "intermediate", "safety": "honor", "notes": "act fast, polite"},
  {"kind": "gm", "t": "Open-Box Deals", "tier": "Compounded", "concept": "new-ish less", "mechanism": "inspect + warranty", "parts": ["buy"], "build": "hunt", "time": "6h", "level": "intermediate", "safety": "none", "notes": "ask about returns"},
  {"kind": "gm", "t": "Demo Units", "tier": "Compounded", "concept": "tried, true", "mechanism": "floor + demo", "parts": ["buy"], "build": "hunt", "time": "6h", "level": "intermediate", "safety": "none", "notes": "20-30% off"},
  {"kind": "gm", "t": "Investment Fees", "tier": "Advanced", "concept": "fees eat returns", "mechanism": "index + low fee", "parts": ["switch"], "build": "audit", "time": "8h", "level": "advanced", "safety": "none", "notes": "1% = 30% over life"},
  {"kind": "gm", "t": "Tax Optimization", "tier": "Advanced", "concept": "keep more", "mechanism": "deductions + timing", "parts": ["file"], "build": "plan", "time": "12h", "level": "advanced", "safety": "pro", "notes": "CPA for complex"},
  {"kind": "gm", "t": "Real Estate (Investor)", "tier": "Advanced", "concept": "deals math", "mechanism": "cap rate + cashflow", "parts": ["offer"], "build": "analyze", "time": "40h", "level": "advanced", "safety": "risk", "notes": "numbers first"},
  {"kind": "gm", "t": "Business Buying", "tier": "Advanced", "concept": "buy cashflow", "mechanism": "due diligence", "parts": ["buy"], "build": "analyze", "time": "80h", "level": "advanced", "safety": "pro", "notes": "buy boring businesses"},
  {"kind": "gm", "t": "Auction Houses", "tier": "Advanced", "concept": "bid smart", "mechanism": "premium + condition", "parts": ["bid"], "build": "attend", "time": "20h", "level": "advanced", "safety": "fever", "notes": "set max, walk"},
  {"kind": "gm", "t": "Estate Liquidation", "tier": "Advanced", "concept": "everything must go", "mechanism": "lot + negotiate", "parts": ["buy"], "build": "attend", "time": "16h", "level": "advanced", "safety": "none", "notes": "last day deals"},
  {"kind": "gm", "t": "Master Hunter", "tier": "Advanced", "concept": "the life", "mechanism": "systems + patience", "parts": ["teach"], "build": "build", "time": "40h", "level": "advanced", "safety": "none", "notes": "teach others"}
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

