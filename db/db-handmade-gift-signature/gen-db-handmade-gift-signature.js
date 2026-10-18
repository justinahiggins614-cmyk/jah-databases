(function(){'use strict';
/* JAH The Handmade Gift Database — real working generator, jahdb-db-handmade-gift-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HGS-";
var SLUG="db-handmade-gift";
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=["Work to the project's measured drawings; measure twice, cut once.", "Finishes used as directed with ventilation; keep rags that carry drying oils flat to dry."];
var CITATIONS=["Jackson, Albert, Day, David, and Jennings, Simon. 'The Complete Manual of Woodworking.' Knopf, 1996.", "'The New Complete Guide to Sewing.' Reader's Digest, 2009."];
var BANK=[
  {"kind": "diy", "t": "Handwritten Letter Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["stationery", "1", 10.0], ["envelopes", "1", 4.0], ["wax seal", "1", 8.0]], "tools": ["pen"], "steps": ["choose paper", "write letters", "seal envelopes", "bundle"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Photo Magnet Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["photos printed", "6", 6.0], ["magnets", "1", 5.0], ["mod podge", "1", 8.0]], "tools": ["brush"], "steps": ["cut photos", "mod podge to magnets", "dry", "gift box"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Sugar Scrub Jars", "tier": "Foundations", "notes": "external use only", "mats": [["sugar 2cups", "1", 2.0], ["coconut oil", "1", 6.0], ["jars", "3", 6.0], ["essential oil", "1", 8.0]], "tools": ["none"], "steps": ["mix sugar and oil", "scent lightly", "jar and label", "ribbon"], "time": "1h", "level": "beginner", "safety": "label ingredients (allergy safety)"},
  {"kind": "diy", "t": "Bookmark Collection", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cardstock", "1", 4.0], ["tassels", "1", 5.0], ["laminator", "1", 0.0]], "tools": ["scissors"], "steps": ["cut bookmarks", "decorate", "tassel on", "laminate"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Friendship Bracelets", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["embroidery floss", "1", 6.0]], "tools": ["none"], "steps": ["choose pattern", "knot rows", "finish ends", "pair up"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Pressed Flower Frame", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["flowers", "1", 0.0], ["heavy books", "1", 0.0], ["frame", "1", 10.0]], "tools": ["none"], "steps": ["press 2 weeks", "arrange", "frame", "gift"], "time": "1h + pressing", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Hot Cocoa Mix Jars", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["cocoa", "1", 5.0], ["jars", "3", 6.0], ["sugar", "1", 2.0], ["marshmallows", "1", 3.0]], "tools": ["none"], "steps": ["layer mix", "seal jars", "tag with instructions", "ribbon"], "time": "1h", "level": "beginner", "safety": "label ingredients for allergies"},
  {"kind": "diy", "t": "Seed Packet Set", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["seeds", "6", 12.0], ["envelopes", "1", 4.0], ["stamps", "1", 3.0]], "tools": ["pen"], "steps": ["decorate envelopes", "fill seeds", "planting notes", "bundle"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Custom Mug (Paint Pen)", "tier": "Foundations", "notes": "hand-wash recommended", "mats": [["mug", "1", 8.0], ["porcelain pens", "1", 12.0]], "tools": ["none"], "steps": ["clean mug", "draw design", "bake 350F 30min", "cool"], "time": "2h", "level": "beginner", "safety": "food-safe pens only"},
  {"kind": "diy", "t": "Lavender Sachets", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["lavender", "1", 8.0], ["fabric", "1", 6.0], ["ribbon", "1", 3.0]], "tools": ["sewing"], "steps": ["cut squares", "fill lavender", "sew shut", "ribbon"], "time": "2h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Photo Coasters", "tier": "Foundations", "notes": "A rewarding hands-on build.", "mats": [["tiles", "4", 6.0], ["photos", "1", 4.0], ["mod podge", "1", 0.0], ["felt", "1", 3.0]], "tools": ["brush"], "steps": ["mod podge photo", "seal 3 coats", "felt bottom", "set of 4"], "time": "3h", "level": "beginner", "safety": "none"},
  {"kind": "diy", "t": "Knitted Scarf", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["yarn 2 skeins", "1", 16.0], ["needles", "1", 8.0]], "tools": ["knitting"], "steps": ["cast on", "knit rows", "bind off", "fringe"], "time": "12h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Hand-Poured Candle Gift", "tier": "Compounded", "notes": "thermometer; keep from kids/pets", "mats": [["soy wax", "1", 12.0], ["jars", "3", 9.0], ["fragrance", "1", 8.0], ["wicks", "1", 4.0]], "tools": ["double boiler"], "steps": ["melt wax 170F", "wick jars", "pour at 130F", "cure 48h"], "time": "4h", "level": "intermediate", "safety": "never leave melting wax"},
  {"kind": "diy", "t": "Memory Quilt Square", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["fabric scraps", "1", 0.0], ["batting", "1", 8.0], ["backing", "1", 10.0]], "tools": ["sewing"], "steps": ["collect meaningful fabrics", "piece squares", "quilt", "bind"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Wooden Keepsake Box", "tier": "Compounded", "notes": "never touch tip", "mats": [["pine box", "1", 12.0], ["woodburner", "1", 20.0], ["stain", "1", 7.0]], "tools": ["burner"], "steps": ["sand box", "burn design", "stain", "felt inside"], "time": "6h", "level": "intermediate", "safety": "woodburner burns — ventilation"},
  {"kind": "diy", "t": "Bath Bomb Set", "tier": "Compounded", "notes": "external use only", "mats": [["baking soda", "1", 4.0], ["citric acid", "1", 8.0], ["molds", "1", 6.0], ["oils", "1", 8.0]], "tools": ["none"], "steps": ["mix dry", "spritz witch hazel", "pack molds", "dry 24h"], "time": "2h", "level": "intermediate", "safety": "label ingredients"},
  {"kind": "diy", "t": "Embroidered Hoop Art", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["hoop", "1", 6.0], ["fabric", "1", 5.0], ["floss", "1", 8.0]], "tools": ["needle"], "steps": ["transfer design", "stitch", "finish back", "hang"], "time": "8h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Leather Keychain", "tier": "Compounded", "notes": "sharp cutters", "mats": [["leather scraps", "1", 10.0], ["rivets", "1", 5.0], ["tools", "1", 12.0]], "tools": ["mallet"], "steps": ["cut strips", "stamp initials", "rivet ring", "condition"], "time": "3h", "level": "intermediate", "safety": "mallet safety"},
  {"kind": "diy", "t": "Recipe Book (Handmade)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 8.0], ["binder", "1", 6.0], ["photos", "1", 5.0], ["pens", "1", 6.0]], "tools": ["none"], "steps": ["collect recipes", "handwrite pages", "photos", "bind"], "time": "10h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Terrarium Gift", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["jar", "1", 10.0], ["plants", "3", 15.0], ["soil", "1", 5.0], ["pebbles", "1", 3.0]], "tools": ["trowel"], "steps": ["layer drainage", "soil and plants", "decor", "care card"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Soap Gift Set", "tier": "Compounded", "notes": "label ingredients", "mats": [["melt-pour base", "1", 14.0], ["molds", "1", 8.0], ["fragrance", "1", 8.0], ["color", "1", 5.0]], "tools": ["microwave"], "steps": ["melt base", "scent and color", "pour molds", "wrap"], "time": "3h", "level": "intermediate", "safety": "hot soap — handle with care"},
  {"kind": "diy", "t": "Custom Tote (Stenciled)", "tier": "Compounded", "notes": "A rewarding hands-on build.", "mats": [["tote", "1", 8.0], ["stencil", "1", 6.0], ["fabric paint", "1", 9.0]], "tools": ["brush"], "steps": ["position stencil", "dab paint", "dry", "cure"], "time": "2h", "level": "intermediate", "safety": "none"},
  {"kind": "diy", "t": "Quilted Wall Hanging", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 25.0], ["batting", "1", 10.0], ["binding", "1", 6.0]], "tools": ["sewing"], "steps": ["design layout", "piece top", "quilt layers", "bind and sleeve"], "time": "20h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Silver Ring (Basic)", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["silver wire", "1", 25.0], ["tools", "1", 30.0], ["polish", "1", 8.0]], "tools": ["pliers"], "steps": ["size wire", "solder join", "shape", "polish"], "time": "8h", "level": "advanced", "safety": "torch safety — ventilation, eye protection"},
  {"kind": "diy", "t": "Hand-Bound Journal", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["paper", "1", 12.0], ["bookboard", "1", 8.0], ["thread", "1", 5.0], ["glue", "1", 6.0]], "tools": ["awl"], "steps": ["fold signatures", "sew binding", "case bound", "press"], "time": "10h", "level": "advanced", "safety": "awl safety"},
  {"kind": "diy", "t": "Wooden Toy Camera Gift", "tier": "Advanced", "notes": "sand smooth", "mats": [["wood", "1", 15.0], ["lens", "1", 8.0], ["strap", "1", 6.0]], "tools": ["saw"], "steps": ["body build", "lens mount", "shutter click", "finish"], "time": "12h", "level": "advanced", "safety": "saw safety"},
  {"kind": "diy", "t": "Knitted Sweater", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["yarn 6 skeins", "1", 48.0], ["needles", "1", 10.0], ["pattern", "1", 8.0]], "tools": ["knitting"], "steps": ["gauge swatch", "knit pieces", "seam", "block"], "time": "60h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Stained Glass Suncatcher", "tier": "Advanced", "notes": "solder fumes ventilate; lead-free", "mats": [["glass", "1", 25.0], ["solder", "1", 12.0], ["foil", "1", 8.0], ["iron", "1", 25.0]], "tools": ["soldering"], "steps": ["cut glass", "foil edges", "solder", "patina"], "time": "12h", "level": "advanced", "safety": "glass cuts — gloves"},
  {"kind": "diy", "t": "Turned Wood Bowl", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["blank", "1", 18.0], ["lathe access", "1", 0.0], ["finish", "1", 10.0]], "tools": ["lathe"], "steps": ["mount blank", "turn shape", "sand", "finish"], "time": "8h", "level": "advanced", "safety": "lathe safety — face shield, no loose clothing"},
  {"kind": "diy", "t": "Porcelain Ornament Set", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["clay", "1", 20.0], ["tools", "1", 15.0], ["kiln access", "1", 0.0], ["glaze", "1", 12.0]], "tools": ["kiln"], "steps": ["throw or handbuild", "bisque fire", "glaze", "fire"], "time": "16h", "level": "advanced", "safety": "kiln safety — ventilation, supervision"},
  {"kind": "diy", "t": "Leather Tote", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["leather", "1", 60.0], ["thread", "1", 8.0], ["tools", "1", 25.0]], "tools": ["mallet"], "steps": ["cut panels", "skive edges", "stitch saddle", "finish"], "time": "20h", "level": "advanced", "safety": "sharp knives — cut away"},
  {"kind": "diy", "t": "Heirloom Quilt", "tier": "Advanced", "notes": "A rewarding hands-on build.", "mats": [["fabric", "1", 80.0], ["batting", "1", 25.0], ["thread", "1", 15.0]], "tools": ["sewing"], "steps": ["design", "piece precisely", "quilt", "bind"], "time": "80h", "level": "advanced", "safety": "none"},
  {"kind": "diy", "t": "Carved Walking Stick", "tier": "Advanced", "notes": "sharp tools", "mats": [["stick", "1", 0.0], ["carving set", "1", 30.0], ["finish", "1", 10.0]], "tools": ["carving"], "steps": ["strip bark", "carve grip", "detail shaft", "finish"], "time": "20h", "level": "advanced", "safety": "carve away from body"},
  {"kind": "diy", "t": "Custom Knife (Kit)", "tier": "Advanced", "notes": "epoxy ventilate", "mats": [["blade blank", "1", 40.0], ["handle wood", "1", 15.0], ["pins", "1", 5.0], ["epoxy", "1", 8.0]], "tools": ["files"], "steps": ["shape handle", "pin and epoxy", "sharpen", "sheath"], "time": "16h", "level": "advanced", "safety": "files and blades sharp"}
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

