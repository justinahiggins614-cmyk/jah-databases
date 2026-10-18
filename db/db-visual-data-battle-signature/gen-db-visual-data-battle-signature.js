(function(){'use strict';
/* JAH The Visual Data Battle Signature Database generator — jahdb-db-visual-data-battle-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VDBS-";
var FIELDS=["Chart Battles","Map Battles","Display Battles"];
var TOPICS={
 "Chart Battles": [
  "Bar vs Line: Trends (Signature Edition) - Chart Battles",
  "Pie vs Bar: Parts (Signature Edition) - Chart Battles",
  "Scatter vs Bubble: Relations (Signature Edition) - Chart Battles",
  "Histogram vs Box Plot: Distributions (Signature Edition) - Chart Battles",
  "Heatmap vs Table: Matrices (Signature Edition) - Chart Battles",
  "Area vs Line: Volumes (Signature Edition) - Chart Battles",
  "Radar vs Bar: Profiles (Signature Edition) - Chart Battles",
  "Sankey vs Pie: Flows (Signature Edition) - Chart Battles",
  "Gantt vs Kanban: Projects (Signature Edition) - Chart Battles",
  "Word Cloud vs Bar: Text (Signature Edition) - Chart Battles",
  "Treemap vs Pie: Hierarchy (Signature Edition) - Chart Battles",
  "Line vs Step: Changes (Signature Edition) - Chart Battles"
 ],
 "Map Battles": [
  "Choropleth vs Cartogram: Maps (Signature Edition) - Map Battles",
  "Dot Map vs Heatmap: Density (Signature Edition) - Map Battles",
  "Flow Map vs Arrows: Movement (Signature Edition) - Map Battles",
  "Topographic vs Satellite: Terrain (Signature Edition) - Map Battles",
  "Subway Map vs Geographic: Transit (Signature Edition) - Map Battles",
  "Globe vs Flat Map: Earth (Signature Edition) - Map Battles",
  "Isoline vs 3D: Elevation (Signature Edition) - Map Battles",
  "Proportional Symbol vs Choropleth: Data Maps (Signature Edition) - Map Battles",
  "Night Lights vs Day: Humanity (Signature Edition) - Map Battles",
  "Timeline vs Table: History (Signature Edition) - Map Battles"
 ],
 "Display Battles": [
  "Dashboard vs Report: Business (Signature Edition) - Display Battles",
  "Infographic vs Article: Explain (Signature Edition) - Display Battles",
  "Slide vs Document: Present (Signature Edition) - Display Battles",
  "Video vs Text: Learn (Signature Edition) - Display Battles",
  "Photo vs Illustration: Show (Signature Edition) - Display Battles",
  "Animation vs Static: Explain (Signature Edition) - Display Battles",
  "Interactive vs Static: Explore (Signature Edition) - Display Battles",
  "Minimal vs Rich: Design (Signature Edition) - Display Battles",
  "Dark vs Light: Theme (Signature Edition) - Display Battles",
  "Serif vs Sans: Type (Signature Edition) - Display Battles",
  "Grid vs Freeform: Layout (Signature Edition) - Display Battles",
  "Icon vs Text: Labels (Signature Edition) - Display Battles"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Visual Data Study — "+safe+"\n"
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
    name:topic+' — visualization showdown record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A visualization showdown record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"visual-data-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-visual-data-battle-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-visual-data-battle-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
