(function(){'use strict';
/* JAH The Side Project Idea Database — real working generator, jahdb-db-side-project-idea-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPI-";
var SLUG="db-side-project-idea";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Pick Your Why", "tier": "Foundations", "concept": "motivation", "mechanism": "learn/earn/fun", "parts": ["choose"], "build": "reflect", "time": "2h", "level": "beginner", "safety": "none", "notes": "one why per project"},
  {"kind": "gm", "t": "The 5-Hour Week", "tier": "Foundations", "concept": "timebox", "mechanism": "5hr weekly", "parts": ["protect"], "build": "schedule", "time": "2h", "level": "beginner", "safety": "burnout", "notes": "calendar block"},
  {"kind": "gm", "t": "Ship Tiny", "tier": "Foundations", "concept": "finish", "mechanism": "2-week scope", "parts": ["ship"], "build": "scope", "time": "20h", "level": "beginner", "safety": "none", "notes": "done > perfect"},
  {"kind": "gm", "t": "Learning in Public", "tier": "Foundations", "concept": "grow audience", "mechanism": "share progress", "parts": ["repeat"], "build": "post", "time": "10h", "level": "beginner", "safety": "none", "notes": "teach what you learn"},
  {"kind": "gm", "t": "Weekend App", "tier": "Foundations", "concept": "build fast", "mechanism": "no-code + launch", "parts": ["launch"], "build": "build", "time": "20h", "level": "beginner", "safety": "none", "notes": "solve your problem"},
  {"kind": "gm", "t": "Newsletter (Niche)", "tier": "Foundations", "concept": "own audience", "mechanism": "weekly + niche", "parts": ["publish"], "build": "start", "time": "16h", "level": "beginner", "safety": "none", "notes": "100 issues"},
  {"kind": "gm", "t": "YouTube (Teach)", "tier": "Foundations", "concept": "video teaching", "mechanism": "phone + edit", "parts": ["publish"], "build": "start", "time": "20h", "level": "beginner", "safety": "none", "notes": "10 videos to judge"},
  {"kind": "gm", "t": "Etsy Shop", "tier": "Foundations", "concept": "sell crafts", "mechanism": "10 listings", "parts": ["sell"], "build": "open", "time": "20h", "level": "beginner", "safety": "fees", "notes": "photos sell"},
  {"kind": "gm", "t": "Print on Demand", "tier": "Foundations", "concept": "no inventory", "mechanism": "designs + POD", "parts": ["sell"], "build": "launch", "time": "16h", "level": "beginner", "safety": "none", "notes": "niche designs"},
  {"kind": "gm", "t": "Blog (Authority)", "tier": "Foundations", "concept": "write asset", "mechanism": "50 posts", "parts": ["write"], "build": "start", "time": "40h", "level": "beginner", "safety": "none", "notes": "SEO compounds"},
  {"kind": "gm", "t": "Open Source (Tiny)", "tier": "Foundations", "concept": "code public", "mechanism": "solve + share", "parts": ["publish"], "build": "build", "time": "20h", "level": "beginner", "safety": "none", "notes": "README matters"},
  {"kind": "gm", "t": "Micro-SaaS", "tier": "Compounded", "concept": "$500 MRR", "mechanism": "tiny + charge", "parts": ["launch"], "build": "build", "time": "80h", "level": "intermediate", "safety": "none", "notes": "stripe day one"},
  {"kind": "gm", "t": "Paid Community", "tier": "Compounded", "concept": "belonging", "mechanism": "niche + rituals", "parts": ["grow"], "build": "launch", "time": "60h", "level": "intermediate", "safety": "none", "notes": "100 true fans"},
  {"kind": "gm", "t": "Digital Product", "tier": "Compounded", "concept": "sell files", "mechanism": "template + gumroad", "parts": ["sell"], "build": "create", "time": "40h", "level": "intermediate", "safety": "none", "notes": "solve painful"},
  {"kind": "gm", "t": "Freelance Productized", "tier": "Compounded", "concept": "package skill", "mechanism": "fixed scope + price", "parts": ["deliver"], "build": "launch", "time": "40h", "level": "intermediate", "safety": "none", "notes": "no custom quotes"},
  {"kind": "gm", "t": "Podcast (Niche)", "tier": "Compounded", "concept": "voice asset", "mechanism": "20 episodes", "parts": ["publish"], "build": "launch", "time": "60h", "level": "intermediate", "safety": "none", "notes": "niche deep"},
  {"kind": "gm", "t": "Course (Mini)", "tier": "Compounded", "concept": "teach skill", "mechanism": "2hr + outcome", "parts": ["sell"], "build": "create", "time": "60h", "level": "intermediate", "safety": "none", "notes": "transformation"},
  {"kind": "gm", "t": "App (Indie)", "tier": "Compounded", "concept": "ship software", "mechanism": "native + simple", "parts": ["launch"], "build": "build", "time": "100h", "level": "intermediate", "safety": "none", "notes": "1.0 tiny"},
  {"kind": "gm", "t": "Game (Jam)", "tier": "Compounded", "concept": "play fun", "mechanism": "game jam", "parts": ["ship"], "build": "build", "time": "60h", "level": "intermediate", "safety": "none", "notes": "finish > feature"},
  {"kind": "gm", "t": "Book (Short)", "tier": "Compounded", "concept": "authority", "mechanism": "100 pages", "parts": ["publish"], "build": "write", "time": "100h", "level": "intermediate", "safety": "none", "notes": "outline first"},
  {"kind": "gm", "t": "Tool (Internal)", "tier": "Compounded", "concept": "scratch itch", "mechanism": "automate pain", "parts": ["use"], "build": "build", "time": "40h", "level": "intermediate", "safety": "none", "notes": "dogfood"},
  {"kind": "gm", "t": "Data Project", "tier": "Compounded", "concept": "insight public", "mechanism": "dataset + viz", "parts": ["publish"], "build": "build", "time": "60h", "level": "intermediate", "safety": "none", "notes": "story > chart"},
  {"kind": "gm", "t": "Notion Templates", "tier": "Compounded", "concept": "sell systems", "mechanism": "pack + sell", "parts": ["sell"], "build": "create", "time": "30h", "level": "intermediate", "safety": "none", "notes": "SEO + twitter"},
  {"kind": "gm", "t": "Icon Pack", "tier": "Compounded", "concept": "pixels pay", "mechanism": "design + sell", "parts": ["sell"], "build": "create", "time": "40h", "level": "intermediate", "safety": "none", "notes": "dribbble launch"},
  {"kind": "gm", "t": "Hardware (Tiny)", "tier": "Advanced", "concept": "atoms!", "mechanism": "kit + tindie", "parts": ["ship"], "build": "build", "time": "120h", "level": "advanced", "safety": "none", "notes": "batch 100"},
  {"kind": "gm", "t": "Biotech (Citizen)", "tier": "Advanced", "concept": "life hacks", "mechanism": "community lab", "parts": ["experiment"], "build": "join", "time": "100h", "level": "advanced", "safety": "safety", "notes": "community labs"},
  {"kind": "gm", "t": "Film (Short)", "tier": "Advanced", "concept": "story screen", "mechanism": "weekend shoot", "parts": ["submit"], "build": "make", "time": "100h", "level": "advanced", "safety": "none", "notes": "sound = half"},
  {"kind": "gm", "t": "Album (DIY)", "tier": "Advanced", "concept": "music out", "mechanism": "record + release", "parts": ["release"], "build": "record", "time": "120h", "level": "advanced", "safety": "none", "notes": "distrokid"},
  {"kind": "gm", "t": "Nonprofit (Tiny)", "tier": "Advanced", "concept": "cause", "mechanism": "mission + 3 people", "parts": ["serve"], "build": "found", "time": "100h", "level": "advanced", "safety": "legal", "notes": "start serving"},
  {"kind": "gm", "t": "Research (Indie)", "tier": "Advanced", "concept": "discover", "mechanism": "question + method", "parts": ["publish"], "build": "research", "time": "200h", "level": "advanced", "safety": "none", "notes": "preprint"},
  {"kind": "gm", "t": "Conference (Micro)", "tier": "Advanced", "concept": "gather tribe", "mechanism": "50 people", "parts": ["host"], "build": "organize", "time": "100h", "level": "advanced", "safety": "none", "notes": "hallway track"},
  {"kind": "gm", "t": "Master Shipper", "tier": "Advanced", "concept": "always shipping", "mechanism": "systems", "parts": ["teach"], "build": "reflect", "time": "100h", "level": "advanced", "safety": "none", "notes": "portfolio of done"},
  {"kind": "gm", "t": "Wedding Films", "tier": "Advanced", "concept": "love stories", "mechanism": "shoot + edit", "parts": ["deliver"], "build": "film", "time": "80h", "level": "advanced", "safety": "contracts", "notes": "book 6mo out"},
  {"kind": "gm", "t": "SaaS (Indie Hacker)", "tier": "Advanced", "concept": "tiny team, real MRR", "mechanism": "build + launch", "parts": ["grow"], "build": "build", "time": "200h", "level": "advanced", "safety": "none", "notes": "7-day streaks"}
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

