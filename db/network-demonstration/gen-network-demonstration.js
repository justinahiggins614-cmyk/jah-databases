(function(){'use strict';
/* JAH The Network Demonstration Database generator — jahdb-network-demonstration-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NETD-";
var FIELDS=["demo-runs","demonstration-studies"];
var STUDIES=[
 ["Make a database of lighthouse keepers",["oceanography","sailboats"]],
 ["Explain fermentation for a beginner",["cookbook","biology-public"]],
 ["Give me the key facts about volcanoes",["volcanoes","geology"]],
 ["Compare the main types of chess openings",["chess","board-games"]],
 ["Give me the history of bridges",["architecture","civil-engineering"]],
 ["Design a rainwater harvesting plan",["water-systems","gardening"]],
 ["Explain how solar panels are made",["solar-energy-systems-engineers","electrical-engineering"]],
 ["Make a database of knots",["sailboats","db-lighthouse-explorer"]],
 ["Give me the key facts about the Boeing 747",["aircraft-boeing-747","aviation"]],
 ["Explain sourdough starter science",["cookbook","biology-public"]],
 ["Compare FDM and resin 3D printing",["public-3d-print-archive","signature-3d-print"]],
 ["Design a home woodworking shop layout",["woodworking-public","blueprints"]],
 ["Give me the history of telescopes",["astronomy-public","optics"]],
 ["Explain tides for a beginner",["physics-public","oceanography"]],
 ["Make a database of train stations",["transportation","railway-systems"]]
];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var st=pick(STUDIES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:"Demonstration Study: "+st[0],
    title:"Demonstration Study: "+st[0],
    t:"Demonstration Study: "+st[0],
    g:field, field:field,
    run_id:"study-gen-"+seed,
    request:st[0],
    pipeline:["intake","database-access","specialized-ai-generation","verification","save-and-replay"],
    databases_consulted:st[1].map(function(s){return {slug:s,cited:[],why:"Manifest match for the request keywords."};}),
    artifact:{kind:"brief",title:"Brief — "+st[0]},
    verification:{checks:["database index fetched live","cited records found in index","brief cites its sources"],result:"pass"},
    replay:["Run the request through db/network-demonstration/ Demo tab","Or headless: python3 code/demo_replay.py --list"],
    src:"signature-generated-sample", sample:true,
    description:"SAMPLE RECORD (generated — structural sample). A demonstration study of "+st[0]+". Generated samples are clearly labeled and never presented as archive records.",
    provenance:"JAH Network Demonstration — generator sample",
    last_verified:"2026-10-19",
    disclaimer:"Generated sample record — not an archive record. Seeded archive records are the authoritative entries.",
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.request)e.push('request');
  if(!r.artifact||!r.artifact.title)e.push('artifact');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.request===record.request&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate request+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-network-demonstration-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-demonstration',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
