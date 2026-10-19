(function(){'use strict';
/* JAH The Fundamentals of Startup Basics Database generator — jahdb-fundamentals-startup-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FU-STAR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Startup Basics Studies", "The Core Vocabulary of Startup Basics", "The History of Startup Basics", "Problem first", "Validate", "Tools and Methods of Startup Basics", "How Startup Basics Is Practiced"], "Compounded": ["MVP", "Co-founders", "Validate method", "Build method", "Runway", "Traction", "Case Studies in Startup Basics"], "Advanced": ["Talk to customers before building.", "Funding", "Pivot", "Fund method", "Current Research Frontiers in Startup Basics", "The Future of Startup Basics"]};
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
    name:topic+' — startup basics fundamentals record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A startup basics fundamentals record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-fundamentals-startup-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fundamentals-startup-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
