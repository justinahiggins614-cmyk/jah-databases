(function(){'use strict';
/* Queijo São Jorge Cheese Database generator — jahdb-cheese-queijo-s-o-jorge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHE-017-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
"Foundations": ["Queijo S\u00e3o Jorge: Complete Overview", "History of Queijo S\u00e3o Jorge", "Queijo S\u00e3o Jorge: Key Facts at a Glance", "How Queijo S\u00e3o Jorge Works", "Queijo S\u00e3o Jorge: Essential Vocabulary", "Queijo S\u00e3o Jorge Flashcards"],
"Compounded": ["Queijo S\u00e3o Jorge In Depth", "Queijo S\u00e3o Jorge: Records, Firsts, and Trivia", "Queijo S\u00e3o Jorge: Timeline", "Enjoying This Cheese", "Queijo S\u00e3o Jorge: Common Misconceptions", "Queijo S\u00e3o Jorge By the Numbers"],
"Advanced": ["Queijo S\u00e3o Jorge Compared", "Quiz: Queijo S\u00e3o Jorge", "Queijo S\u00e3o Jorge: Study Checklist", "Queijo S\u00e3o Jorge: Connections", "Queijo S\u00e3o Jorge: Fast Facts", "Queijo S\u00e3o Jorge: Field Notes", "Queijo S\u00e3o Jorge: Review", "Queijo S\u00e3o Jorge: Standards and Sources"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# cheese-queijo-s-o-jorge-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 chess opening record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A chess opening record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chess-opening-repertoire-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-cheese-queijo-s-o-jorge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cheese-queijo-s-o-jorge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
