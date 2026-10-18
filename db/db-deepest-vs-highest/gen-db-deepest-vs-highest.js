(function(){'use strict';
/* JAH The Deepest vs. Highest Database generator — jahdb-db-deepest-vs-highest-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DVH-";
var FIELDS=["Vertical Foundations","Sky High","Ocean Deep"];
var TOPICS={
 "Vertical Foundations": [
  "Everest vs Mariana Trench: Earth's Extremes - Vertical Foundations",
  "Burj Khalifa vs Mponeng Mine: Built Extremes - Vertical Foundations",
  "Airplane vs Submarine: Altitude vs Depth - Vertical Foundations",
  "Cloud vs Cave: Natural Highs and Lows - Vertical Foundations",
  "Satellite vs Trench: Explored Extremes - Vertical Foundations",
  "Hot Air Balloon vs Bathyscaphe: Gentle Extremes - Vertical Foundations",
  "Eagle vs Deep-Sea Fish: Life Extremes - Vertical Foundations",
  "Skyscraper vs Subway: City Vertical - Vertical Foundations",
  "Mountain vs Valley: Natural Pair - Vertical Foundations",
  "Kite vs Anchor: Tether Extremes - Vertical Foundations",
  "Tree Top vs Root Tip: Plant Vertical - Vertical Foundations",
  "Bird Migration vs Whale Dive: Animal Vertical - Vertical Foundations"
 ],
 "Sky High": [
  "Space Elevator (Concept) vs Deepest Drill: Future Vertical - Sky High",
  "Stratosphere vs Troposphere: Sky Layers - Sky High",
  "High-Altitude Lake vs Sea Level: Water Heights - Sky High",
  "Alpine Peak vs Hill: Climbing Scale - Sky High",
  "Cloud City (Concept) vs Underwater City: Future Habitats - Sky High",
  "Tallest Tree vs Tallest Building: Living vs Built - Sky High",
  "Aurora vs City Lights: Sky Glow - Sky High",
  "Paraglider vs BASE Jumper: Air Sports - Sky High",
  "Weather Balloon vs Dive Bell: Simple Vessels - Sky High",
  "Summit vs Base Camp: Mountain Life - Sky High"
 ],
 "Ocean Deep": [
  "Mariana Snailfish vs Surface Fish: Depth Life - Ocean Deep",
  "Hydrothermal Vent vs Coral Reef: Deep vs Shallow - Ocean Deep",
  "Trench vs Abyssal Plain: Seafloor - Ocean Deep",
  "Deep Scattering Layer vs Surface School: Fish Mass - Ocean Deep",
  "Whale Fall vs Forest Floor: Deep vs Land Recycling - Ocean Deep",
  "Submarine Canyon vs Grand Canyon: Carved Deep - Ocean Deep",
  "Black Smoker vs White Smoker: Vent Types - Ocean Deep",
  "Deep Current vs Surface Current: Ocean Rivers - Ocean Deep",
  "Hadal Zone vs Sunlight Zone: Ocean Layers - Ocean Deep",
  "Seamount vs Island: Underwater Mountains - Ocean Deep",
  "Brine Pool vs Freshwater Spring: Strange Waters - Ocean Deep",
  "Ancient Shipwreck vs Modern Wreck: Deep Time - Ocean Deep"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Deepest Vs Highest Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — elevation comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A elevation comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"deepest-vs-highest-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-deepest-vs-highest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-deepest-vs-highest',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
