(function(){'use strict';
/* JAH Public Trails Database generator — jahdb-public-trails-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-TRAIL-';
var FIELDS=["north-america", "europe", "asia", "south-america", "africa", "oceania"];
var TOPICS={
 "africa":["Kilimanjaro — Machame Route","Rwenzori Trek","Mount Kenya Trek (Sirimon–Chogoria)","Drakensberg Grand Traverse"],
 "asia":["Lycian Way","Jordan Trail","Annapurna Circuit","Everest Base Camp Trek","Kumano Kodo","Snowman Trek (Bhutan)","Baltoro / K2 Concordia Trek","Markha Valley Trek","Nakasendo Trail","Shikoku 88-Temple Pilgrimage","Israel National Trail","Tiger Leaping Gorge / Tiger's Nest (Bhutan)","Great Himalaya Trail"],
 "europe":["Camino Francés (Camino de Santiago)","Tour du Mont Blanc","GR20 (Corsica)","West Highland Way","Pennine Way","South West Coast Path","Laugavegur (Iceland)","Kungsleden (Sweden)","Alta Via 1 (Dolomites)","GR11 (Spanish Pyrenees)","GR10 (French Pyrenees)","Fisherman's Trail (Portugal)","Walker's Haute Route","Tour of the Matterhorn","Alta Via 2 (Dolomites)"],
 "north-america":["Appalachian Trail","Pacific Crest Trail","Continental Divide Trail","John Muir Trail","Wonderland Trail","Long Trail (Vermont)","Colorado Trail","Arizona Trail","Bruce Trail (Canada)","West Coast Trail (Canada)","Chilkoot Trail","Florida Trail","Ice Age Trail","North Country Trail","Pacific Northwest Trail","Hayduke Trail"],
 "oceania":["Kokoda Track","Overland Track (Tasmania)","Larapinta Trail","Te Araroa","Milford Track","Routeburn Track","Abel Tasman Coast Track","Tongariro Northern Circuit","Kepler Track","Bibbulmun Track"],
 "south-america":["Inca Trail","Torres del Paine W Trek"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Study Lab — "+safe+"\n"
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
    name:topic+' — trail study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A trail study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'trail-planner',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-trails-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-trails',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
