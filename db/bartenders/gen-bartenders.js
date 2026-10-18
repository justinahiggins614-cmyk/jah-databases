(function(){'use strict';
/* JAH The Bartenders Database generator — jahdb-bartenders-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BART-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Bartenders Do",
  "The Bar Setup",
  "Classic Cocktails",
  "Pouring and Measuring",
  "Bar Tools",
  "Beer and Wine Basics",
  "Customer Service",
  "ID Checking and Responsible Service",
  "Speed and Efficiency",
  "Bar Sanitation",
  "History of the Cocktail",
 ],
 "Compounded": [
  "Craft Cocktail Design",
  "Advanced Mixology Techniques",
  "Whiskey Knowledge",
  "Bar Management Basics",
  "Creating a Cocktail Menu",
  "Flair Bartending Intro",
  "Wine Service",
  "High-Volume Bartending",
  "Regulars and Hospitality",
  "Inventory and Costing",
  "Event Bartending",
  "Bar Business Basics",
 ],
 "Advanced": [
  "Bar Ownership",
  "Advanced Spirits Knowledge",
  "Competition Bartending",
  "Consulting",
  "Teaching Bartending",
  "The Bartender Career Ladder",
  "Future of Bars",
  "Distillery and Brewery Relations",
  "Brand Ambassadorship",
  "Bar Program Consulting for Restaurants",
  "Legacy and Mentorship in Bartending",
 ],
};
var DEMOKIND="bar calculation";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Bar calculator — "+safe+"\n"
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
    name:topic+' — bartender profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miners profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-bartenders-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bartenders',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
