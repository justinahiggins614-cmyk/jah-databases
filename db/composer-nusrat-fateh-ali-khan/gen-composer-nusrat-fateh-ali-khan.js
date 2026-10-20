(function(){'use strict';
/* Nusrat Fateh Ali Khan Composer Database generator — jahdb-composer-nusrat-fateh-ali-khan-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMP-039-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
"Foundations": ["Nusrat Fateh Ali Khan: Complete Overview", "History of Nusrat Fateh Ali Khan", "Nusrat Fateh Ali Khan: Key Facts at a Glance", "How Nusrat Fateh Ali Khan Works", "Nusrat Fateh Ali Khan: Essential Vocabulary", "Nusrat Fateh Ali Khan Flashcards"],
"Compounded": ["Nusrat Fateh Ali Khan In Depth", "Nusrat Fateh Ali Khan: Records, Firsts, and Trivia", "Nusrat Fateh Ali Khan: Timeline", "Learning From This Composer", "Nusrat Fateh Ali Khan: Common Misconceptions", "Nusrat Fateh Ali Khan By the Numbers"],
"Advanced": ["Nusrat Fateh Ali Khan Compared", "Quiz: Nusrat Fateh Ali Khan", "Nusrat Fateh Ali Khan: Study Checklist", "Nusrat Fateh Ali Khan: Connections", "Nusrat Fateh Ali Khan: Fast Facts", "Nusrat Fateh Ali Khan: Field Notes", "Nusrat Fateh Ali Khan: Review", "Nusrat Fateh Ali Khan: Standards and Sources"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# composer-nusrat-fateh-ali-khan-demo \u2014 "+safe+"\n"
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
var gen={version:'jahdb-composer-nusrat-fateh-ali-khan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('composer-nusrat-fateh-ali-khan',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
