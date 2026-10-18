(function(){'use strict';
/* JAH The Unsolved Architecture Signature Database generator — jahdb-unsolved-architecture-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USACS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Form Follows Function: True (Signature Edition) - Design",
  "The Ornament Question (Signature Edition) - Design",
  "Why Buildings Fail (Signature Edition) - Practice",
  "The Authority Problem in Architecture (Signature Edition) - Practice",
  "What Makes a Building Beautiful (Signature Edition) - Theory",
  "Proportion: The Golden Ratio Myth (Signature Edition) - Theory",
  "Light as a Building Material (Signature Edition) - Design",
  "The Staircase Problem (Signature Edition) - Design",
  "Threshold Design: The Entrance (Signature Edition) - Design",
  "The Facade Problem (Signature Edition) - Design",
  "Materials Honesty: Must It Hold (Signature Edition) - Theory"
 ],
 "Compounded": [
  "Brutalism: Failure or Triumph (Signature Edition) - Styles",
  "The Social Promise of Modernism (Signature Edition) - Styles",
  "Postmodernism: What Was It (Signature Edition) - Styles",
  "Vernacular Architecture: The Lesson (Signature Edition) - Styles",
  "The Skyscraper Problem (Signature Edition) - Design",
  "Housing: Why So Ugly (Signature Edition) - Practice",
  "The Public Space Problem (Signature Edition) - Urban",
  "Monuments: Who Decides (Signature Edition) - Urban",
  "Preservation Versus Progress (Signature Edition) - Urban",
  "The Museum Problem (Signature Edition) - Practice",
  "Sacred Space Design (Signature Edition) - Design",
  "The Kitchen Problem (Signature Edition) - Design"
 ],
 "Advanced": [
  "Parametricism: The Promise (Signature Edition) - Styles",
  "Biomimicry in Architecture (Signature Edition) - Design",
  "The Carbon Problem in Building (Signature Edition) - Practice",
  "Architecture and Climate Adaptation (Signature Edition) - Practice",
  "The Smart Building Problem (Signature Edition) - Practice",
  "Designing for Neurodiversity (Signature Edition) - Design",
  "The Aging Building Stock (Signature Edition) - Urban",
  "Informal Settlements: The Design Response (Signature Edition) - Urban",
  "Architecture After Capitalism (Signature Edition) - Theory",
  "The Authorship Problem (Signature Edition) - Theory",
  "A Unified Theory of Architecture (Signature Edition) - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Architecture Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-architecture-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-architecture-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-architecture-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
