(function(){'use strict';
/* Søren Kierkegaard Philosopher Database generator — jahdb-philosopher-s-ren-kierkegaard-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PHI-028-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
"Foundations": ["S\u00f8ren Kierkegaard: Complete Overview", "History of S\u00f8ren Kierkegaard", "S\u00f8ren Kierkegaard: Key Facts at a Glance", "How S\u00f8ren Kierkegaard Works", "S\u00f8ren Kierkegaard: Essential Vocabulary", "S\u00f8ren Kierkegaard Flashcards"],
"Compounded": ["S\u00f8ren Kierkegaard In Depth", "S\u00f8ren Kierkegaard: Records, Firsts, and Trivia", "S\u00f8ren Kierkegaard: Timeline", "Learning From This Philosopher", "S\u00f8ren Kierkegaard: Common Misconceptions", "S\u00f8ren Kierkegaard By the Numbers"],
"Advanced": ["S\u00f8ren Kierkegaard Compared", "Quiz: S\u00f8ren Kierkegaard", "S\u00f8ren Kierkegaard: Study Checklist", "S\u00f8ren Kierkegaard: Connections", "S\u00f8ren Kierkegaard: Fast Facts", "S\u00f8ren Kierkegaard: Field Notes", "S\u00f8ren Kierkegaard: Review", "S\u00f8ren Kierkegaard: Standards and Sources"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# philosopher-s-ren-kierkegaard-demo \u2014 "+safe+"\n"
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
var gen={version:'jahdb-philosopher-s-ren-kierkegaard-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('philosopher-s-ren-kierkegaard',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
