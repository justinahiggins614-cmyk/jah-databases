(function(){'use strict';
/* JAH The Visual Data Battle Database generator — jahdb-db-visual-data-battle-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VDB-";
var FIELDS=["Chart Battles","Map Battles","Display Battles"];
var TOPICS={
 "Chart Battles": [
  "Bar vs Line: Trends - Chart Battles",
  "Pie vs Bar: Parts - Chart Battles",
  "Scatter vs Bubble: Relations - Chart Battles",
  "Histogram vs Box Plot: Distributions - Chart Battles",
  "Heatmap vs Table: Matrices - Chart Battles",
  "Area vs Line: Volumes - Chart Battles",
  "Radar vs Bar: Profiles - Chart Battles",
  "Sankey vs Pie: Flows - Chart Battles",
  "Gantt vs Kanban: Projects - Chart Battles",
  "Word Cloud vs Bar: Text - Chart Battles",
  "Treemap vs Pie: Hierarchy - Chart Battles",
  "Line vs Step: Changes - Chart Battles"
 ],
 "Map Battles": [
  "Choropleth vs Cartogram: Maps - Map Battles",
  "Dot Map vs Heatmap: Density - Map Battles",
  "Flow Map vs Arrows: Movement - Map Battles",
  "Topographic vs Satellite: Terrain - Map Battles",
  "Subway Map vs Geographic: Transit - Map Battles",
  "Globe vs Flat Map: Earth - Map Battles",
  "Isoline vs 3D: Elevation - Map Battles",
  "Proportional Symbol vs Choropleth: Data Maps - Map Battles",
  "Night Lights vs Day: Humanity - Map Battles",
  "Timeline vs Table: History - Map Battles"
 ],
 "Display Battles": [
  "Dashboard vs Report: Business - Display Battles",
  "Infographic vs Article: Explain - Display Battles",
  "Slide vs Document: Present - Display Battles",
  "Video vs Text: Learn - Display Battles",
  "Photo vs Illustration: Show - Display Battles",
  "Animation vs Static: Explain - Display Battles",
  "Interactive vs Static: Explore - Display Battles",
  "Minimal vs Rich: Design - Display Battles",
  "Dark vs Light: Theme - Display Battles",
  "Serif vs Sans: Type - Display Battles",
  "Grid vs Freeform: Layout - Display Battles",
  "Icon vs Text: Labels - Display Battles"
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
var gen={version:'jahdb-db-visual-data-battle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-visual-data-battle',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
