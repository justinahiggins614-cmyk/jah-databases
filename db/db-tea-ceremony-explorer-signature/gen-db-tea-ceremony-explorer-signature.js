(function(){'use strict';
/* JAH The Tea Ceremony Explorer Signature Database generator — jahdb-db-tea-ceremony-explorer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TCES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Tea: The Five Families",
  "Water and Temperature",
  "Western Brewing Basics",
  "Gongfu Brewing",
  "Green Teas of the World",
  "Matcha, Whisked",
  "Oolong: The Spectrum",
  "Black Teas, Bold and Classic",
  "Pu-erh and Dark Teas",
  "Herbal Tisanes",
  "The Japanese Tea Gathering"
 ],
 "Compounded": [
  "Chinese Tea Culture",
  "British Afternoon Tea",
  "Moroccan Mint Tea",
  "Russian Samovar Tradition",
  "Iced Tea Mastery",
  "Tea and Food Pairings",
  "Teaware: The Essential Kit",
  "Storing and Aging Tea",
  "Tea Tasting Flights",
  "Chai, Indian Style",
  "Bubble Tea, Honestly",
  "Iced Matcha"
 ],
 "Advanced": [
  "Advanced: Tea Ceremony Hosting",
  "Advanced: The Tea Journal",
  "Advanced: Sourcing Great Tea",
  "The Tea Ceremony Explorer Master Collection",
  "Advanced: Tea Blending",
  "Advanced: The Tea Ceremony Garden",
  "Advanced: Tea and Meditation",
  "Advanced: Rare Teas Worth Seeking",
  "Advanced: The Tea House Business",
  "Advanced: Tea Storage Cellar Design",
  "The Tea Ceremony Explorer Encyclopedia"
 ]
};
var DEMOKIND="food-lab-demo";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Food Lab Demo — "+safe+"\n"
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
    name:topic+' — tea record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tea record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-tea-ceremony-explorer-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-tea-ceremony-explorer-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
