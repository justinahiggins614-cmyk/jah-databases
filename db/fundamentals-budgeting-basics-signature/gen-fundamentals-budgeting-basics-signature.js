(function(){'use strict';
/* JAH The Fundamentals of Budgeting Basics Database generator — jahdb-fundamentals-budgeting-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FS-BUDG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Budgeting Basics Studies", "The Core Vocabulary of Budgeting Basics", "The History of Budgeting Basics", "Track first", "Zero-based", "Tools and Methods of Budgeting Basics", "How Budgeting Basics Is Practiced"], "Compounded": ["50/30/20", "Sinking funds", "Track method", "Plan method", "Envelope method", "Review monthly", "Case Studies in Budgeting Basics"], "Advanced": ["Track spending before budgeting; you cannot plan what you cannot see.", "Irregular income", "Buffer", "Maintain method", "Current Research Frontiers in Budgeting Basics", "The Future of Budgeting Basics"]};
var DEMOKIND="fundamentals study companion";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — "+field+" flashcard\n"
   + "card = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('TOPIC: ' + card['topic'])\n"
   + "print('FIELD: ' + card['field'])\n"
   + "print('Study prompt: explain this topic in your own words, then check the archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — budgeting basics fundamentals record (Signature edition)',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A budgeting basics fundamentals record (Signature edition) of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-completion',
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
var gen={version:'jahdb-fundamentals-budgeting-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fundamentals-budgeting-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
