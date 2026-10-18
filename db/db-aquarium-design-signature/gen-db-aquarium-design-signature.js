(function(){'use strict';
/* JAH The Aquarium Design Database — real working generator, jahdb-db-aquarium-design-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ADS-";
var SLUG="db-aquarium-design";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry.", "GFCI protection on all aquarium electrics; drip loops on every cord."];
var CITATIONS=["Amano, Takashi. 'Nature Aquarium World.' TFH Publications.", "Hiscock, Peter. 'Encyclopedia of Aquarium Plants.' Barron's, 2003."];
var BANK=[
  {"kind": "diy", "t": "First 10-Gallon Setup", "tier": "Foundations", "notes": "research nitrogen cycle", "mats": [["tank kit", "1", 80.0], ["substrate", "1", 15.0], ["decor", "1", 20.0], ["conditioner", "1", 8.0]], "tools": ["none"], "steps": ["rinse tank", "substrate", "fill, condition", "cycle 2-4 weeks"], "time": "4h + cycling", "level": "beginner", "safety": "cycle before fish — patience prevents deaths"},
  {"kind": "diy", "t": "Betta Tank (5 Gallon)", "tier": "Foundations", "notes": "lid — they jump", "mats": [["tank", "1", 50.0], ["heater", "1", 20.0], ["plants", "1", 20.0], ["food", "1", 8.0]], "tools": ["none"], "steps": ["5gal minimum", "heater 78F", "plants", "feed small"], "time": "3h", "level": "beginner", "safety": "no tankmates with bettas (mostly)"},
  {"kind": "diy", "t": "Goldfish Done Right", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tank 40gal", "1", 120.0], ["filter", "1", 50.0], ["food", "1", 10.0]], "tools": ["none"], "steps": ["40gal+ for fancy", "strong filter", "feed varied", "water changes"], "time": "4h", "level": "beginner", "safety": "goldfish get huge — no bowls, ever"},
  {"kind": "diy", "t": "Shrimp Nano Tank", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tank 5gal", "1", 60.0], ["plants", "1", 25.0], ["shrimp", "10", 30.0], ["food", "1", 8.0]], "tools": ["none"], "steps": ["plant heavily", "cycle", "add shrimp", "feed sparingly"], "time": "4h", "level": "beginner", "safety": "copper kills shrimp — check meds/ferts"},
  {"kind": "diy", "t": "Snail Cleanup Crew", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["snails", "5", 15.0]], "tools": ["none"], "steps": ["identify species", "acclimate", "algae duty", "supplement"], "time": "1h", "level": "beginner", "safety": "some snails breed fast — research first"},
  {"kind": "diy", "t": "Planted Tank Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 80.0], ["soil", "1", 25.0], ["plants", "1", 40.0], ["light", "1", 50.0]], "tools": ["none"], "steps": ["soil substrate", "plant densely", "light 8h", "fertilize"], "time": "6h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Water Testing 101", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["test kit", "1", 25.0]], "tools": ["none"], "steps": ["test ammonia/nitrite/nitrate", "log", "water change", "repeat"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Aquascape: Iwagumi", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 90.0], ["rocks", "1", 30.0], ["carpet plants", "1", 35.0], ["soil", "1", 25.0]], "tools": ["tweezers"], "steps": ["odd-number rocks", "carpet plant", "flood dry-start", "fill"], "time": "8h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Community Tank Stocking", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tank 20gal", "1", 100.0], ["fish", "1", 60.0], ["plants", "1", 30.0]], "tools": ["none"], "steps": ["research compatibility", "school sizes", "add slowly", "feed"], "time": "6h", "level": "beginner", "safety": "quarantine new fish 2 weeks"},
  {"kind": "diy", "t": "Sponge Filter Setup", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["sponge", "1", 12.0], ["air pump", "1", 18.0], ["tubing", "1", 5.0]], "tools": ["none"], "steps": ["assemble", "seed with media", "gentle flow", "maintain"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Algae Control Basics", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["timer", "1", 12.0], ["test kit", "1", 0.0]], "tools": ["none"], "steps": ["light 6-8h", "balance nutrients", "cleanup crew", "manual remove"], "time": "2h", "level": "beginner", "safety": "no algaecide shortcuts — fix the cause"},
  {"kind": "diy", "t": "CO2 Injection Setup", "tier": "Compounded", "notes": "check valve mandatory", "mats": [["tank", "1", 100.0], ["CO2 kit", "1", 130.0], ["diffuser", "1", 15.0], ["drop checker", "1", 10.0]], "tools": ["none"], "steps": ["secure bottle", "diffuser low", "1 bubble/sec start", "monitor livestock"], "time": "8h", "level": "intermediate", "safety": "CO2 can gas fish — start low, watch behavior"},
  {"kind": "diy", "t": "Sump Filtration", "tier": "Compounded", "notes": "test for leaks 48h", "mats": [["tank", "1", 150.0], ["sump", "1", 80.0], ["pump", "1", 60.0], ["plumbing", "1", 30.0]], "tools": ["drill"], "steps": ["drill or overflow", "plumb sump", "return pump", "tune"], "time": "12h", "level": "intermediate", "safety": "drill glass with diamond bit + water"},
  {"kind": "diy", "t": "Aquascape: Dutch Style", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 120.0], ["plants", "20", 80.0], ["soil", "1", 30.0]], "tools": ["tweezers"], "steps": ["tiered rows", "contrast colors", "trim often", "photo"], "time": "16h", "level": "intermediate", "safety": "trimming is the skill — weekly"},
  {"kind": "diy", "t": "Breeding Guppies", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 80.0], ["mops", "1", 10.0], ["food", "1", 12.0]], "tools": ["none"], "steps": ["ratio 1:3", "plants cover", "separate fry", "feed"], "time": "8h", "level": "intermediate", "safety": "population explodes — have a plan"},
  {"kind": "diy", "t": "Saltwater Nano (10gal)", "tier": "Compounded", "notes": "test constantly", "mats": [["tank", "1", 120.0], ["salt", "1", 25.0], ["live rock", "1", 60.0], ["test", "1", 35.0]], "tools": ["none"], "steps": ["mix salt 1.025", "cure rock", "cycle long", "stock slow"], "time": "12h", "level": "intermediate", "safety": "saltwater = patience"},
  {"kind": "diy", "t": "Discus Tank", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank 55gal", "1", 200.0], ["discus", "6", 180.0], ["heater", "1", 30.0], ["food", "1", 20.0]], "tools": ["none"], "steps": ["warm 84F", "pristine water", "beefheart mix", "changes"], "time": "12h", "level": "intermediate", "safety": "discus need dedication — daily water changes"},
  {"kind": "diy", "t": "Biotope: Amazon", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 130.0], ["wood", "1", 40.0], ["plants", "1", 50.0], ["fish", "1", 70.0]], "tools": ["none"], "steps": ["research habitat", "tannin water", "species correct", "maintain"], "time": "12h", "level": "intermediate", "safety": "authenticity rewards research"},
  {"kind": "diy", "t": "High-Tech Planted", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 150.0], ["light", "1", 120.0], ["CO2", "1", 130.0], ["ferts", "1", 30.0]], "tools": ["none"], "steps": ["strong light", "CO2 tuned", "EI dosing", "trim"], "time": "20h", "level": "intermediate", "safety": "balance light/CO2/nutrients or algae wins"},
  {"kind": "diy", "t": "Pond (Small Patio)", "tier": "Compounded", "notes": "winter plan", "mats": [["tub 50gal", "1", 60.0], ["pump", "1", 40.0], ["plants", "1", 40.0], ["fish", "1", 30.0]], "tools": ["shovel"], "steps": ["level spot", "tub in", "pump", "plant, stock"], "time": "10h", "level": "intermediate", "safety": "net against herons"},
  {"kind": "diy", "t": "Quarantine System", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank 10gal", "1", 60.0], ["filter", "1", 20.0], ["meds", "1", 25.0]], "tools": ["none"], "steps": ["bare setup", "cycle", "observe 2-4 weeks", "treat"], "time": "4h", "level": "intermediate", "safety": "quarantine saves display tanks"},
  {"kind": "diy", "t": "Auto Water Change", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["pump", "1", 40.0], ["tubing", "1", 20.0], ["timer", "1", 15.0]], "tools": ["none"], "steps": ["drain line", "fill line", "timer", "test"], "time": "6h", "level": "intermediate", "safety": "flood safety — test attended first"},
  {"kind": "diy", "t": "Automatic Feeder Setup", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["feeder", "1", 25.0], ["food", "1", 8.0]], "tools": ["none"], "steps": ["portion test", "mount", "schedule", "monitor"], "time": "1h", "level": "intermediate", "safety": "test portions 3 days before travel"},
  {"kind": "diy", "t": "Reef Tank (40gal)", "tier": "Advanced", "notes": "start with fish-only", "mats": [["tank", "1", 300.0], ["lights", "1", 400.0], ["skimmer", "1", 200.0], ["rock", "1", 150.0], ["corals", "1", 300.0]], "tools": ["none"], "steps": ["research 3 months", "equip", "cycle long", "add slowly"], "time": "60h", "level": "advanced", "safety": "reef = expensive and demanding"},
  {"kind": "diy", "t": "Large Cichlid Tank", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank 125gal", "1", 500.0], ["filter", "1", 200.0], ["rock", "1", 100.0], ["fish", "1", 200.0]], "tools": ["none"], "steps": ["floor support", "territories", "stock", "maintain"], "time": "30h", "level": "advanced", "safety": "125gal weighs 1400lb+ — floor load check"},
  {"kind": "diy", "t": "Aquaponics Loop", "tier": "Advanced", "notes": "food-safe materials", "mats": [["tank", "1", 150.0], ["grow bed", "1", 80.0], ["pump", "1", 50.0], ["media", "1", 40.0]], "tools": ["drill"], "steps": ["fish tank", "bed above", "pump loop", "plant"], "time": "24h", "level": "advanced", "safety": "balance fish/plants"},
  {"kind": "diy", "t": "Custom Stand Build", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["lumber", "1", 80.0], ["screws", "1", 15.0], ["level", "1", 0.0]], "tools": ["saw"], "steps": ["frame 2x4", "level top", "skin", "test load"], "time": "12h", "level": "advanced", "safety": "stand must hold 10lb/gallon — overbuild"},
  {"kind": "diy", "t": "Drilled Overflow System", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 200.0], ["drill kit", "1", 40.0], ["plumbing", "1", 60.0]], "tools": ["drill"], "steps": ["plan holes", "drill wet", "bulkheads", "test"], "time": "12h", "level": "advanced", "safety": "tempered glass can't be drilled — verify first"},
  {"kind": "diy", "t": "Fish Room (Multi-Tank)", "tier": "Advanced", "notes": "electrical GFCI; water source nearby", "mats": [["racks", "1", 200.0], ["tanks", "6", 400.0], ["filters", "1", 150.0]], "tools": ["none"], "steps": ["rack level", "plumb air", "tanks cycled", "stock"], "time": "40h", "level": "advanced", "safety": "floor load"},
  {"kind": "diy", "t": "Competition Aquascape", "tier": "Advanced", "notes": "photograph well", "mats": [["tank", "1", 200.0], ["hardscape", "1", 100.0], ["plants", "1", 150.0], ["photo", "1", 0.0]], "tools": ["none"], "steps": ["concept", "hardscape", "plant", "grow-in, photo"], "time": "60h", "level": "advanced", "safety": "months of grow-in"},
  {"kind": "diy", "t": "Breeding Rare Species", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tanks", "1", 300.0], ["stock", "1", 200.0]], "tools": ["none"], "steps": ["research papers", "condition", "trigger spawning", "raise fry"], "time": "50h", "level": "advanced", "safety": "document everything"},
  {"kind": "diy", "t": "Public-Style Display Tank", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank 200gal", "1", 800.0], ["equip", "1", 600.0], ["stock", "1", 500.0]], "tools": ["none"], "steps": ["plan", "equip", "stock", "maintain"], "time": "80h", "level": "advanced", "safety": "professional-level commitment"},
  {"kind": "diy", "t": "Pond Ecosystem (Large)", "tier": "Advanced", "notes": "heron protection", "mats": [["liner", "1", 200.0], ["pump", "1", 150.0], ["plants", "1", 150.0], ["fish", "1", 100.0]], "tools": ["shovel"], "steps": ["dig", "liner", "rock edge", "plant, stock"], "time": "40h", "level": "advanced", "safety": "call 811 before digging"},
  {"kind": "diy", "t": "Saltwater Breeding", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["systems", "1", 500.0], ["stock", "1", 300.0]], "tools": ["none"], "steps": ["research", "condition", "larval foods", "raise"], "time": "80h", "level": "advanced", "safety": "larval rearing is expert-level"}
];
var TIPS=["Cut everything before you glue anything.", "Dry-fit twice, fasten once.", "Sharp tools are safe tools \u2014 hone before you start.", "Finish scraps first to test color.", "Label your parts as you cut them.", "Take a photo before disassembly for reference."];
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

