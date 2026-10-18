(function(){'use strict';
/* JAH The Emblem and Crest Database generator — jahdb-emblem-and-crest-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMCR-";
var FIELDS=["Symbol Foundations", "Emblem Design", "Heraldic Mastery"];
var TOPICS={
 "Symbol Foundations": [
  "The Language of Symbols",
  "Shield Shapes",
  "Tinctures: The Heraldic Palette",
  "Charges: The Cast of Symbols",
  "The Motto Scroll",
  "Monogram Design",
  "Badge vs Logo",
  "The Seal",
  "Color in Emblems",
  "Sketching the First Arms"
 ],
 "Emblem Design": [
  "The Design Brief",
  "Researching Precedents",
  "Thumbnail Storming",
  "Refining the Mark",
  "The Blazon Test",
  "Digital Construction",
  "The Presentation",
  "Family Crests Today",
  "Team and Club Badges",
  "The Maker's Mark",
  "Ribbon and Banner Design",
  "The Crest Animal",
  "Helmet and Mantling",
  "Supporters: Beasts That Hold",
  "The Compartment"
 ],
 "Heraldic Mastery": [
  "Marshalling: Combined Arms",
  "The Full Achievement",
  "Heraldry for Organizations",
  "The Living Tradition",
  "Your Arms, Your Legacy",
  "Canting Arms: Punning Heraldry",
  "The Heraldic Sea",
  "Modern Civic Heraldry",
  "The Personal Standard"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# emblem — "+safe+"\n"
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
    name:topic+' — emblem and crest design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A emblem and crest design record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"emblem-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emblem-and-crest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emblem-and-crest',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
