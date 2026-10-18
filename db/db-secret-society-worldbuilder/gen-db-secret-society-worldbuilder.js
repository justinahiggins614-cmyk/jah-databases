(function(){'use strict';
/* JAH The Secret Society Worldbuilder Database generator — jahdb-db-secret-society-worldbuilder-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSSW-";
var FIELDS=["Orders","Lodges","Circles"];
var TOPICS={
 "Orders": [
  "The Lantern Bearers \u2014 Orders",
  "The Lantern Bearers \u2014 Deep Dive \u2014 Orders",
  "The Unfinished Cartographers \u2014 Orders",
  "The Unfinished Cartographers \u2014 Deep Dive \u2014 Orders",
  "The Watchers of the Tide \u2014 Orders",
  "The Watchers of the Tide \u2014 Deep Dive \u2014 Orders",
  "The Stargazers' Debt \u2014 Orders",
  "The Stargazers' Debt \u2014 Deep Dive \u2014 Orders",
  "The Rememberers \u2014 Orders",
  "The Rememberers \u2014 Deep Dive \u2014 Orders",
  "The Clockwinders \u2014 Orders",
  "The Clockwinders \u2014 Deep Dive \u2014 Orders",
  "The Lighthouse Society \u2014 Orders",
  "The Lighthouse Society \u2014 Deep Dive \u2014 Orders"
 ],
 "Lodges": [
  "The Keepers of Lost Things \u2014 Lodges",
  "The Keepers of Lost Things \u2014 Deep Dive \u2014 Lodges",
  "The Menders \u2014 Lodges",
  "The Menders \u2014 Deep Dive \u2014 Lodges",
  "The Ferrymen \u2014 Lodges",
  "The Ferrymen \u2014 Deep Dive \u2014 Lodges",
  "The Seed Keepers \u2014 Lodges",
  "The Seed Keepers \u2014 Deep Dive \u2014 Lodges",
  "The Grand Lodge \u2014 Lodges",
  "The Grand Lodge \u2014 Deep Dive \u2014 Lodges"
 ],
 "Circles": [
  "The Silent Orchestra \u2014 Circles",
  "The Silent Orchestra \u2014 Deep Dive \u2014 Circles",
  "The Midnight Gardeners \u2014 Circles",
  "The Midnight Gardeners \u2014 Deep Dive \u2014 Circles",
  "The Letter Writers \u2014 Circles",
  "The Letter Writers \u2014 Deep Dive \u2014 Circles",
  "The Listeners \u2014 Circles",
  "The Listeners \u2014 Deep Dive \u2014 Circles",
  "The Storytellers' Truce \u2014 Circles",
  "The Storytellers' Truce \u2014 Deep Dive \u2014 Circles"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Secret Society Study — "+safe+"\n"
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
    name:topic+' — secret society world record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A secret society world record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-secret-society-worldbuilder-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-secret-society-worldbuilder',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
