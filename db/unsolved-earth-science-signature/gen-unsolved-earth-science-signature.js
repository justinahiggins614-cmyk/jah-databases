(function(){'use strict';
/* JAH The Unsolved Earth Science Signature Database generator — jahdb-unsolved-earth-science-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Topics mirror the archive's 34
   seeded records; generated records are labeled samples, never archive entries. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USESS-";
var FIELDS=["Seismology", "Volcanology", "Climate", "Paleoclimate", "Oceans", "Geomagnetism", "Geodynamics", "Geochemistry", "Planetary Formation", "Deep Earth"];
var TOPICS=[
 ["Can Earthquakes Be Predicted? (Signature Edition)", "Seismology", "Signature original interpretation."],
 ["Can Volcanic Eruptions Be Forecast Reliably? (Signature Edition)", "Volcanology", "Signature original interpretation."],
 ["How High and How Fast Will Sea Level Rise? (Signature Edition)", "Climate", "Signature original interpretation."],
 ["Where Are Earth's Climate Tipping Points? (Signature Edition)", "Climate", "Signature original interpretation."],
 ["Why Did Earth's Climate Flip Abruptly in the Past? (Signature Edition)", "Paleoclimate", "Signature original interpretation."],
 ["What Makes El Nino Irregular, and Can It Be Forecast Years Ahead? (Signature Edition)", "Oceans", "Signature original interpretation."],
 ["How Much Carbon Will Thawing Permafrost Release? (Signature Edition)", "Climate", "Signature original interpretation."],
 ["Is the Atlantic Overturning Circulation Heading for Collapse? (Signature Edition)", "Oceans", "Signature original interpretation."],
 ["Why Does Earths Magnetic Field Reverse, and When Is Next? (Signature Edition)", "Geomagnetism", "Signature original interpretation."],
 ["What Causes Deep-Focus Earthquakes? (Signature Edition)", "Seismology", "Signature original interpretation."],
 ["What Drives Slow Earthquakes and Tremor? (Signature Edition)", "Seismology", "Signature original interpretation."],
 ["How and When Did Plate Tectonics Begin? (Signature Edition)", "Geodynamics", "Signature original interpretation."],
 ["How Did the Continents Grow? (Signature Edition)", "Geodynamics", "Signature original interpretation."],
 ["How Much Life Is in the Deep Biosphere? (Signature Edition)", "Geochemistry", "Signature original interpretation."],
 ["How Much Water Is Hidden Inside the Mantle? (Signature Edition)", "Geochemistry", "Signature original interpretation."],
 ["Where Did Earths Oceans Come From? (Signature Edition)", "Planetary Formation", "Signature original interpretation."],
 ["How Does Carbon Move Through the Deep Earth? (Signature Edition)", "Geochemistry", "Signature original interpretation."],
 ["What Are the Giant Blobs at the Base of the Mantle? (Signature Edition)", "Deep Earth", "Signature original interpretation."],
 ["What Drives Mantle Plumes? (Signature Edition)", "Geodynamics", "Signature original interpretation."],
 ["What Is the Core-Mantle Boundary Really Like? (Signature Edition)", "Deep Earth", "Signature original interpretation."],
 ["What Powers Earths Magnetic Field? (Signature Edition)", "Geomagnetism", "Signature original interpretation."],
 ["How Old Is the Solid Inner Core? (Signature Edition)", "Deep Earth", "Signature original interpretation."],
 ["Why Is the Inner Core Seismically Anisotropic? (Signature Edition)", "Deep Earth", "Signature original interpretation."],
 ["Does the Inner Core Spin Faster Than the Rest of Earth? (Signature Edition)", "Deep Earth", "Signature original interpretation."],
 ["How Exactly Did the Moon Form? (Signature Edition)", "Planetary Formation", "Signature original interpretation."],
 ["How Did Earth Escape Snowball Glaciations? (Signature Edition)", "Paleoclimate", "Signature original interpretation."],
 ["Why Was the Young Earth Warm Under a Faint Young Sun? (Signature Edition)", "Paleoclimate", "Signature original interpretation."],
 ["What Caused the Great Oxidation Event? (Signature Edition)", "Geochemistry", "Signature original interpretation."],
 ["What Killed Almost Everything at the End of the Permian? (Signature Edition)", "Paleoclimate", "Signature original interpretation."],
 ["Where Does Earths Missing Heat Come From? (Signature Edition)", "Geodynamics", "Signature original interpretation."],
 ["Where Does Deep Nitrogen Go? (Signature Edition)", "Geochemistry", "Signature original interpretation."],
 ["How Strong Is the Oceans Biological Carbon Pump? (Signature Edition)", "Oceans", "Signature original interpretation."],
 ["How Long Does Deep Water Stay in the Deep Ocean? (Signature Edition)", "Oceans", "Signature original interpretation."],
 ["What Is Earths Complete Volatile Budget? (Signature Edition)", "Planetary Formation", "Signature original interpretation."]
];
function topicFor(seed){
  return TOPICS[((seed-1)%TOPICS.length+TOPICS.length)%TOPICS.length];
}
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}"+ "\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts){
  opts=opts||{};
  var rnd=prng(seed);
  var t=topicFor(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:t[1];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:t[0]+' — unsolved problem record (sample)',
    title:t[0],
    description:'SAMPLE RECORD (generated — structural sample). '+t[2]+' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'unsolved-demo',language:'python',program:demoProgram(t[0],field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-unsolved-earth-science-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("unsolved-earth-science-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
