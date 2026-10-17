(function(){'use strict';
/* JAH The General Knowledge Quiz Database generator — jahdb-quiz-general-knowledge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZGK-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "General Knowledge Quiz: Easy World Capitals - Foundations",
  "General Knowledge Quiz: Animal Kingdom Basics - Foundations",
  "General Knowledge Quiz: Colors, Shapes and First Numbers - Foundations",
  "General Knowledge Quiz: Days, Months and Seasons - Foundations",
  "General Knowledge Quiz: Easy Arithmetic - Foundations",
  "General Knowledge Quiz: Famous Landmarks - Foundations",
  "General Knowledge Quiz: Food and Fruit Facts - Foundations",
  "General Knowledge Quiz: The Human Body Basics - Foundations",
  "General Knowledge Quiz: Sports Basics - Foundations",
  "General Knowledge Quiz: Music Basics - Foundations",
  "General Knowledge Quiz: Continents and Oceans - Foundations",
  "General Knowledge Quiz: Space Basics - Foundations",
  "General Knowledge Quiz: World Capitals Challenge - Foundations",
  "General Knowledge Quiz: History Milestones - Foundations",
  "General Knowledge Quiz: Everyday Science - Foundations",
  "General Knowledge Quiz: Riddles and Wordplay Starter Set - Foundations"
 ],
 "Compounded": [
  "General Knowledge Quiz: Literature Basics - Compounded",
  "General Knowledge Quiz: Rivers, Mountains and Deserts - Compounded",
  "General Knowledge Quiz: Inventions and Inventors - Compounded",
  "General Knowledge Quiz: Flags and Nations - Compounded",
  "General Knowledge Quiz: The Living World - Compounded",
  "General Knowledge Quiz: Art and Artists - Compounded",
  "General Knowledge Quiz: Logic Puzzles - Compounded",
  "General Knowledge Quiz: Math Word Problems - Compounded",
  "General Knowledge Quiz: History Dates and Events - Compounded",
  "General Knowledge Quiz: Chemistry and Physics - Compounded"
 ],
 "Advanced": [
  "General Knowledge Quiz: Geography Mixed Challenge - Advanced",
  "General Knowledge Quiz: Wordplay Masters - Advanced",
  "General Knowledge Quiz: Literature Quotes and Authors - Advanced",
  "General Knowledge Quiz: Technology and Computers - Advanced",
  "General Knowledge Quiz: Advanced General Knowledge - Advanced",
  "General Knowledge Quiz: Lateral Thinking Masters - Advanced",
  "General Knowledge Quiz: Science The Deep Dive - Advanced",
  "General Knowledge Quiz: The Ultimate General Knowledge Final - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# General Knowledge Quiz — "+safe+"\n"
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
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"quiz-runner-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-quiz-general-knowledge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-general-knowledge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
