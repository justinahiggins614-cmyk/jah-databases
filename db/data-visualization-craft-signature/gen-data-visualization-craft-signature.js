(function(){'use strict';
/* JAH Data Visualization Craft Database generator — jahdb-data-visualization-craft-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DATAVCS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Choosing Chart Types (Signature Edition)", "Bar Charts (Signature Edition)", "Line Charts (Signature Edition)", "Honest Axes (Signature Edition)", "Color Use (Signature Edition)", "Decluttering (Signature Edition)", "Dashboards (Signature Edition)", "Storytelling (Signature Edition)", "Common Misleads (Signature Edition)", "Tools Compared (Signature Edition)", "Accessibility (Signature Edition)"], "Compounded": ["Teaching Visualization (Signature Edition)", "The Portfolio Review (Signature Edition)", "Scatterplots (Signature Edition)", "Histograms (Signature Edition)", "Heatmaps (Signature Edition)", "Small Multiples (Signature Edition)", "Annotations (Signature Edition)", "Interactivity (Signature Edition)", "Pie Charts (Signature Edition)", "Tables (Signature Edition)", "Geographic Maps (Signature Edition)", "Time Series Design (Signature Edition)"], "Advanced": ["Uncertainty Visualization (Signature Edition)", "Comparisons (Signature Edition)", "Narrative Structure (Signature Edition)", "Executive Summaries (Signature Edition)", "Scientific Figures (Signature Edition)", "Infographics (Signature Edition)", "Real-Time Dashboards (Signature Edition)", "Mobile Visualization (Signature Edition)", "Print Design (Signature Edition)", "Ethics of Visualization (Signature Edition)", "Critique Practice (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — visualization guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — visualization guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A visualization guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"data-visualization-craft-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-data-visualization-craft-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("data-visualization-craft-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
