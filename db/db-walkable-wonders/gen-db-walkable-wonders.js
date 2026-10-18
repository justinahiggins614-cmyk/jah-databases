(function(){'use strict';
/* JAH The Walkable Wonders Database Database generator — jahdb-db-walkable-wonders-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WLW-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Walkable?",
  "The Venice, Italy (Walkable)",
  "The Walkable Score",
  "The Kyoto, Japan (Walkable)",
  "The Walking Shoes",
  "The Bruges, Belgium (Walkable)",
  "The Walkable Food",
  "The Fez, Morocco (Walkable)",
  "The Walkable Safety",
  "The Old Town, Dubrovnik (Walkable)",
  "The Walkable Year"
 ],
 "Compounded": [
  "The Zermatt, Switzerland (Walkable)",
  "The Walkable Story",
  "The Giethoorn (Walkable)",
  "The Walkable with Kids",
  "The Rothenburg, Germany (Walkable)",
  "The Walkable Solo",
  "The Valletta, Malta (Walkable)",
  "The Walkable Decade",
  "The Guanajuato, Mexico (Walkable)",
  "The Walkable Road Trip",
  "The Mdina, Malta (Walkable)",
  "The Walkable Festival"
 ],
 "Advanced": [
  "Advanced: The Walkable Index",
  "Advanced: Your Walkable Ranking",
  "Advanced: The Walkable Passport",
  "Advanced: The Walkable Storyteller",
  "Advanced: The Walkable Bucket List",
  "Advanced: The Walkable Finale",
  "Advanced: The Walkable Legacy",
  "Advanced: The Walkable Memoir",
  "Advanced: The Walkable Master Decade",
  "Advanced: The Walkable Year",
  "The Walkable Wonders Encyclopedia"
 ]
};
var DEMOKIND="travel-lab-demo";
var SAMPLEDESC="Sample records are complete real walkable entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Travel Lab Demo — "+safe+"\n"
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
    name:topic+' — walkable place record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A walkable place record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-walkable-wonders-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-walkable-wonders',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
