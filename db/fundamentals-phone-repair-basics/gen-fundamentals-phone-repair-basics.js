(function(){'use strict';
/* JAH The Fundamentals of Phone Repair Basics Database generator — jahdb-fundamentals-phone-repair-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FU-PHON-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Phone Repair Basics Studies", "The Core Vocabulary of Phone Repair Basics", "The History of Phone Repair Basics", "Diagnose", "Tools", "Tools and Methods of Phone Repair Basics", "How Phone Repair Basics Is Practiced"], "Compounded": ["Guides", "Battery", "Diagnose method", "Repair method", "Adhesive", "ESD", "Case Studies in Phone Repair Basics"], "Advanced": ["Back up data first.", "Test", "Data", "Verify method", "Current Research Frontiers in Phone Repair Basics", "The Future of Phone Repair Basics"]};
var DEMOKIND="fundamentals study";
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
    name:topic+' — phone repair basics fundamentals record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A phone repair basics fundamentals record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-fundamentals-phone-repair-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fundamentals-phone-repair-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
