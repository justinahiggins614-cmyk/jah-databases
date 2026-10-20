(function(){'use strict';
/* Diego Velázquez Painter Database generator — jahdb-painter-diego-vel-zquez-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PAI-006-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
"Foundations": ["Diego Vel\u00e1zquez: Complete Overview", "History of Diego Vel\u00e1zquez", "Diego Vel\u00e1zquez: Key Facts at a Glance", "How Diego Vel\u00e1zquez Works", "Diego Vel\u00e1zquez: Essential Vocabulary", "Diego Vel\u00e1zquez Flashcards"],
"Compounded": ["Diego Vel\u00e1zquez In Depth", "Diego Vel\u00e1zquez: Records, Firsts, and Trivia", "Diego Vel\u00e1zquez: Timeline", "Learning From This Painter", "Diego Vel\u00e1zquez: Common Misconceptions", "Diego Vel\u00e1zquez By the Numbers"],
"Advanced": ["Diego Vel\u00e1zquez Compared", "Quiz: Diego Vel\u00e1zquez", "Diego Vel\u00e1zquez: Study Checklist", "Diego Vel\u00e1zquez: Connections", "Diego Vel\u00e1zquez: Fast Facts", "Diego Vel\u00e1zquez: Field Notes", "Diego Vel\u00e1zquez: Review", "Diego Vel\u00e1zquez: Standards and Sources"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# painter-diego-vel-zquez-demo \u2014 "+safe+"\n"
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
var gen={version:'jahdb-painter-diego-vel-zquez-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('painter-diego-vel-zquez',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
