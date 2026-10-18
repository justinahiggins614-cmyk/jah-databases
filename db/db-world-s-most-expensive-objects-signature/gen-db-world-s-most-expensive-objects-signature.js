(function(){'use strict';
/* JAH The World's Most Expensive Objects Database — real working generator, jahdb-db-world-s-most-expensive-objects-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WSMEOS-";
var SLUG="db-world-s-most-expensive-objects";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Verify facts against primary sources before acting on valuations or market claims.", "Keep receipts, photos, and provenance records for everything of value."];
var CITATIONS=["Yeoman, R.S. 'A Guide Book of United States Coins.' Whitman, annual.", "Bernstein, Peter L. 'Against the Gods: The Remarkable Story of Risk.' Wiley, 1996."];
var BANK=[
  {"kind": "gm", "t": "Why Price Fascinates", "tier": "Foundations", "concept": "value stories", "mechanism": "rarity + story + demand", "parts": ["reflect"], "build": "read", "time": "2h", "level": "beginner", "safety": "none", "notes": "price = story + scarcity"},
  {"kind": "gm", "t": "Most Expensive Painting", "tier": "Foundations", "concept": "Salvator Mundi $450M", "mechanism": "controversy + history", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "attribution debates"},
  {"kind": "gm", "t": "Most Expensive Car", "tier": "Foundations", "concept": "Ferrari 250 GTO $70M", "mechanism": "racing + rarity", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "36 made"},
  {"kind": "gm", "t": "Most Expensive House", "tier": "Foundations", "concept": "The One $126M", "mechanism": "scale + location", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "location cubed"},
  {"kind": "gm", "t": "Most Expensive Jewel", "tier": "Foundations", "concept": "Pink Star $71M", "mechanism": "59.6ct pink", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "color + clarity"},
  {"kind": "gm", "t": "Most Expensive Watch", "tier": "Foundations", "concept": "Patek $31M", "mechanism": "complication + history", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Graves Supercomplication"},
  {"kind": "gm", "t": "Most Expensive Coin", "tier": "Foundations", "concept": "1933 Double Eagle $18.9M", "mechanism": "story + legality", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "the legal one"},
  {"kind": "gm", "t": "Most Expensive Stamp", "tier": "Foundations", "concept": "British Guiana $9.5M", "mechanism": "one known", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "1c magenta"},
  {"kind": "gm", "t": "Most Expensive Book", "tier": "Foundations", "concept": "Codex Leicester $30.8M", "mechanism": "da Vinci notebook", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Gates owns it"},
  {"kind": "gm", "t": "Most Expensive Guitar", "tier": "Foundations", "concept": "Cobain Mustang $6M", "mechanism": "provenance", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "Smells Like Teen Spirit"},
  {"kind": "gm", "t": "Most Expensive Photo", "tier": "Foundations", "concept": "Rhein II $4.3M", "mechanism": "Gursky scale", "parts": ["read"], "build": "study", "time": "4h", "level": "beginner", "safety": "none", "notes": "minimalism premium"},
  {"kind": "gm", "t": "Yacht (Expensive)", "tier": "Compounded", "concept": "$4.8B History Supreme", "mechanism": "gold + platinum", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "claims debated"},
  {"kind": "gm", "t": "Private Jet (Top)", "tier": "Compounded", "concept": "$600M+ custom", "mechanism": "flying palace", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "operating costs too"},
  {"kind": "gm", "t": "Island (Private)", "tier": "Compounded", "concept": "$100M+ islands", "mechanism": "location + development", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "upkeep $$$"},
  {"kind": "gm", "t": "Diamond (Largest)", "tier": "Compounded", "concept": "Cullinan 3,106ct", "mechanism": "1905 find", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "Crown Jewels now"},
  {"kind": "gm", "t": "Wine (Bottle)", "tier": "Compounded", "concept": "$558K Screaming Eagle", "mechanism": "vintage + rarity", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "1945 Romanee-Conti"},
  {"kind": "gm", "t": "Whisky (Bottle)", "tier": "Compounded", "concept": "$1.9M Macallan 1926", "mechanism": "age + art label", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "60 bottles"},
  {"kind": "gm", "t": "Handbag (Diamond)", "tier": "Compounded", "concept": "$3.8M Hermes", "mechanism": "diamonds + exotic", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "Ginza Tanaka"},
  {"kind": "gm", "t": "The Million-Dollar Chess Set", "tier": "Compounded", "concept": "$600K jeweled", "mechanism": "gold + diamonds", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "Charles Hollander"},
  {"kind": "gm", "t": "Bed (Luxury)", "tier": "Compounded", "concept": "$6.3M Baldacchino", "mechanism": "canopy + history", "parts": ["read"], "build": "study", "time": "6h", "level": "intermediate", "safety": "none", "notes": "sleep like royalty"},
  {"kind": "gm", "t": "Toilet (Gold)", "tier": "Compounded", "concept": "$1.3M gold loo", "mechanism": "Hang Fung", "parts": ["laugh"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "24k functional"},
  {"kind": "gm", "t": "Parking Spot", "tier": "Compounded", "concept": "$1M Manhattan", "mechanism": "location", "parts": ["read"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "scarcity extreme"},
  {"kind": "gm", "t": "Most Expensive Sneakers", "tier": "Compounded", "concept": "$2.2M Nike", "mechanism": "Moon Shoe", "parts": ["read"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "1972 waffle"},
  {"kind": "gm", "t": "Most Expensive Comic", "tier": "Compounded", "concept": "$3.2M Action #1", "mechanism": "Superman debut", "parts": ["read"], "build": "study", "time": "4h", "level": "intermediate", "safety": "none", "notes": "9.0 grade"},
  {"kind": "gm", "t": "Antimatter (Gram)", "tier": "Advanced", "concept": "$62.5T theoretical", "mechanism": "production cost", "parts": ["read"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "not for sale, ever"},
  {"kind": "gm", "t": "Asteroid (Value)", "tier": "Advanced", "concept": "$10 quintillion?", "mechanism": "16 Psyche metal", "parts": ["read"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "economics says no"},
  {"kind": "gm", "t": "Manhattan Project", "tier": "Advanced", "concept": "$2B 1945", "mechanism": "history cost", "parts": ["read"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "$30B today"},
  {"kind": "gm", "t": "ISS ($150B)", "tier": "Advanced", "concept": "most expensive object", "mechanism": "station cost", "parts": ["read"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "never sold"},
  {"kind": "gm", "t": "Three Gorges Dam", "tier": "Advanced", "concept": "$37B dam", "mechanism": "scale", "parts": ["read"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "concrete + displacement"},
  {"kind": "gm", "t": "Veblen Goods Theory", "tier": "Advanced", "concept": "price = desire", "mechanism": "luxury economics", "parts": ["read"], "build": "study", "time": "10h", "level": "advanced", "safety": "none", "notes": "expensive because expensive"},
  {"kind": "gm", "t": "Bubble Lessons", "tier": "Advanced", "concept": "tulips to NFTs", "mechanism": "cycles", "parts": ["read"], "build": "study", "time": "12h", "level": "advanced", "safety": "speculation", "notes": "history rhymes"},
  {"kind": "gm", "t": "What Price Misses", "tier": "Advanced", "concept": "value vs price", "mechanism": "meaning", "parts": ["write"], "build": "reflect", "time": "6h", "level": "advanced", "safety": "none", "notes": "priceless things"},
  {"kind": "gm", "t": "Master Analyst", "tier": "Advanced", "concept": "the lens", "mechanism": "economics + story", "parts": ["write"], "build": "study", "time": "20h", "level": "advanced", "safety": "none", "notes": "teach value"},
  {"kind": "gm", "t": "Most Expensive Dress", "tier": "Advanced", "concept": "$12M Marilyn", "mechanism": "subway grate", "parts": ["read"], "build": "study", "time": "6h", "level": "advanced", "safety": "none", "notes": "auction legend"}
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

