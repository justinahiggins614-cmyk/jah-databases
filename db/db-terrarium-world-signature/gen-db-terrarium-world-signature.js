(function(){'use strict';
/* JAH The Terrarium World Database — real working generator, jahdb-db-terrarium-world-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TWS-";
var SLUG="db-terrarium-world";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry.", "Use horticultural charcoal and drainage layers; avoid treated woods inside closed systems."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "First Closed Terrarium", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 12.0], ["pebbles", "1", 4.0], ["charcoal", "1", 5.0], ["soil", "1", 6.0], ["moss", "1", 8.0], ["plants", "3", 15.0]], "tools": ["trowel"], "steps": ["pebbles", "charcoal", "soil", "plants, mist, seal"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Open Succulent Bowl", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bowl", "1", 14.0], ["cactus soil", "1", 7.0], ["succulents", "5", 20.0], ["pebbles", "1", 4.0]], "tools": ["trowel"], "steps": ["drainage layer", "soil", "arrange", "top dress"], "time": "2h", "level": "beginner", "safety": "gloves for cactus spines"},
  {"kind": "diy", "t": "Moss Terrarium", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 10.0], ["moss", "1", 10.0], ["pebbles", "1", 3.0], ["soil", "1", 4.0]], "tools": ["tweezers"], "steps": ["layers", "moss carpet", "mist", "lid"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Air Plant Display", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tillandsia", "5", 20.0], ["driftwood", "1", 12.0]], "tools": ["none"], "steps": ["soak plants", "arrange", "mist weekly", "bright indirect"], "time": "1h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Herb Windowsill Garden", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["pots", "4", 12.0], ["soil", "1", 6.0], ["herbs", "4", 16.0]], "tools": ["trowel"], "steps": ["pot", "soil", "plant", "water, sun"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Fern Terrarium", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 12.0], ["ferns", "3", 18.0], ["soil", "1", 6.0], ["pebbles", "1", 4.0]], "tools": ["trowel"], "steps": ["layers", "plant ferns", "mist", "indirect light"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Carnivorous Plant Pot", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["sundew", "1", 12.0], ["peat", "1", 6.0], ["pot", "1", 8.0], ["distilled water", "1", 3.0]], "tools": ["trowel"], "steps": ["peat/perlite", "plant", "tray water", "sun"], "time": "2h", "level": "beginner", "safety": "distilled water only — minerals kill"},
  {"kind": "diy", "t": "Succulent Wreath", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["wreath form", "1", 14.0], ["succulents", "20", 40.0], ["moss", "1", 8.0], ["pins", "1", 4.0]], "tools": ["none"], "steps": ["moss base", "pin succulents", "hang", "mist"], "time": "4h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Bottle Garden", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["bottle", "1", 8.0], ["plants", "1", 12.0], ["soil", "1", 5.0], ["tools long", "1", 10.0]], "tools": ["tweezers"], "steps": ["funnel soil", "long tools plant", "mist", "place"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Fairy Garden Terrarium", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 12.0], ["mini plants", "1", 12.0], ["house", "1", 10.0], ["pebbles", "1", 4.0]], "tools": ["trowel"], "steps": ["layers", "house", "plants", "paths"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Coffee Cup Succulent", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["mug", "1", 5.0], ["succulent", "1", 4.0], ["soil", "1", 3.0]], "tools": ["none"], "steps": ["drainage hole (drill)", "soil", "plant", "sip sun"], "time": "1h", "level": "beginner", "safety": "drill ceramic slowly with water"},
  {"kind": "diy", "t": "Orchid Terrarium", "tier": "Compounded", "notes": "air flow", "mats": [["jar", "1", 15.0], ["orchid", "1", 25.0], ["bark", "1", 8.0], ["moss", "1", 6.0]], "tools": ["trowel"], "steps": ["bark base", "orchid set", "moss", "humid"], "time": "3h", "level": "intermediate", "safety": "no soil — bark only"},
  {"kind": "diy", "t": "Desert Terrarium", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 30.0], ["sand", "1", 10.0], ["cacti", "5", 25.0], ["rocks", "1", 0.0]], "tools": ["trowel"], "steps": ["sand deep", "rocks", "cacti", "top sun"], "time": "4h", "level": "intermediate", "safety": "gloves and tongs for cacti"},
  {"kind": "diy", "t": "Tropical Wardian Case", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["case", "1", 60.0], ["plants", "8", 40.0], ["soil", "1", 10.0], ["mister", "1", 15.0]], "tools": ["trowel"], "steps": ["drainage", "soil", "plant layers", "mist system"], "time": "6h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Aquatic Terrarium (Planted Tank)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 40.0], ["substrate", "1", 20.0], ["plants", "1", 35.0], ["light", "1", 45.0], ["filter", "1", 30.0]], "tools": ["none"], "steps": ["substrate slope", "plant", "fill slowly", "light cycle"], "time": "8h", "level": "intermediate", "safety": "cycle tank before livestock"},
  {"kind": "diy", "t": "Bonsai Terrarium", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 18.0], ["bonsai", "1", 35.0], ["soil", "1", 8.0], ["tools", "1", 15.0]], "tools": ["tools"], "steps": ["root prune", "plant", "moss", "prune"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Carnivorous Bog Garden", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["container", "1", 20.0], ["peat", "1", 10.0], ["sarracenia", "3", 30.0], ["water", "1", 3.0]], "tools": ["trowel"], "steps": ["peat/sand", "plant", "tray water", "full sun"], "time": "4h", "level": "intermediate", "safety": "rainwater/distilled only"},
  {"kind": "diy", "t": "Moss Wall Art", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["frame", "1", 20.0], ["moss", "1", 25.0], ["glue", "1", 8.0]], "tools": ["glue gun"], "steps": ["preserved moss", "arrange", "glue", "hang"], "time": "5h", "level": "intermediate", "safety": "preserved moss needs no water"},
  {"kind": "diy", "t": "Epiphyte Branch Display", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["branch", "1", 0.0], ["orchids", "3", 36.0], ["moss", "1", 8.0], ["wire", "1", 5.0]], "tools": ["wire"], "steps": ["mount orchids", "moss wrap", "mist", "hang"], "time": "4h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Terrarium with Waterfall", "tier": "Compounded", "notes": "drip loop on cord", "mats": [["tank", "1", 50.0], ["pump", "1", 25.0], ["foam", "1", 15.0], ["plants", "1", 30.0]], "tools": ["none"], "steps": ["foam falls", "pump hidden", "plants", "test flow"], "time": "10h", "level": "intermediate", "safety": "low-voltage pump"},
  {"kind": "diy", "t": "Large Floor Terrarium", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["jar 10gal", "1", 60.0], ["plants", "12", 60.0], ["soil", "1", 15.0]], "tools": ["trowel"], "steps": ["big layers", "plant design", "hardscape", "maintain"], "time": "8h", "level": "intermediate", "safety": "heavy — place before filling"},
  {"kind": "diy", "t": "Seasonal Terrarium Refresh", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["plants", "1", 20.0], ["soil", "1", 8.0]], "tools": ["trowel"], "steps": ["assess", "replace tired", "refresh soil", "restyle"], "time": "3h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Hanging Kokedama", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["plant", "1", 12.0], ["moss", "1", 8.0], ["soil", "1", 5.0], ["twine", "1", 4.0]], "tools": ["none"], "steps": ["root ball", "moss wrap", "twine", "hang, mist"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Paludarium (Half Land/Half Water)", "tier": "Advanced", "notes": "secure land area", "mats": [["tank", "1", 80.0], ["filter", "1", 40.0], ["plants", "1", 50.0], ["hardscape", "1", 30.0]], "tools": ["none"], "steps": ["land/water divide", "filter", "plant both", "stock"], "time": "16h", "level": "advanced", "safety": "cycle water"},
  {"kind": "diy", "t": "Highland Terrarium (Cool)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 70.0], ["cooling", "1", 40.0], ["plants", "1", 60.0]], "tools": ["none"], "steps": ["cool setup", "highland plants", "monitor temp", "maintain"], "time": "16h", "level": "advanced", "safety": "temperature control critical"},
  {"kind": "diy", "t": "Orchidarium (Climate)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cabinet", "1", 150.0], ["orchids", "1", 100.0], ["mister", "1", 40.0], ["fans", "1", 25.0]], "tools": ["none"], "steps": ["seal cabinet", "misters", "fans", "monitor"], "time": "20h", "level": "advanced", "safety": "electrical safety with water — GFCI, drip loops"},
  {"kind": "diy", "t": "Carnivorous Highland Setup", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 80.0], ["cooling", "1", 50.0], ["plants", "1", 70.0]], "tools": ["none"], "steps": ["cool temps", "pure water", "highland species", "monitor"], "time": "20h", "level": "advanced", "safety": "strict water purity"},
  {"kind": "diy", "t": "Moss Terrarium Landscape", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 60.0], ["moss", "10", 50.0], ["rocks", "1", 20.0]], "tools": ["tweezers"], "steps": ["hardscape", "moss species", "detail", "maintain"], "time": "12h", "level": "advanced", "safety": "species ID matters for care"},
  {"kind": "diy", "t": "Bonsai Forest Planting", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["pot", "1", 40.0], ["trees", "7", 105.0], ["soil", "1", 15.0], ["wire", "1", 10.0]], "tools": ["tools"], "steps": ["arrange forest", "wire", "plant", "aftercare"], "time": "10h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Aquascape (Competition)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["tank", "1", 100.0], ["soil", "1", 30.0], ["plants", "1", 80.0], ["CO2", "1", 120.0], ["light", "1", 90.0]], "tools": ["none"], "steps": ["hardscape golden ratio", "plant", "CO2 tune", "maintain"], "time": "30h", "level": "advanced", "safety": "CO2 safety — check valves, no leaks"},
  {"kind": "diy", "t": "Vivarium with Dart Frogs", "tier": "Advanced", "notes": "source captive-bred", "mats": [["tank", "1", 120.0], ["plants", "1", 80.0], ["drainage", "1", 30.0], ["frogs", "1", 150.0]], "tools": ["none"], "steps": ["drainage", "plant 1 month", "fruit fly culture", "introduce"], "time": "30h", "level": "advanced", "safety": "research species needs deeply"},
  {"kind": "diy", "t": "Large Paludarium Build", "tier": "Advanced", "notes": "GFCI everything", "mats": [["tank 75gal", "1", 200.0], ["materials", "1", 150.0], ["livestock", "1", 100.0]], "tools": ["none"], "steps": ["plan", "build land", "plumb water", "plant, cycle"], "time": "40h", "level": "advanced", "safety": "weight — floor load"},
  {"kind": "diy", "t": "Greenhouse Cabinet", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["cabinet", "1", 120.0], ["lights", "1", 80.0], ["fans", "1", 30.0], ["humidifier", "1", 40.0]], "tools": ["drill"], "steps": ["seal", "lights", "airflow", "monitor"], "time": "16h", "level": "advanced", "safety": "electrical + water safety — GFCI"},
  {"kind": "diy", "t": "Terrarium Business Starter", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["supplies", "1", 300.0]], "tools": ["none"], "steps": ["costing", "designs", "sourcing", "sell"], "time": "20h", "level": "advanced", "safety": "business basics — price for profit"}
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

