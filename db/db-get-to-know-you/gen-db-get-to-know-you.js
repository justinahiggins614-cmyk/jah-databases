(function(){'use strict';
/* JAH The Get to Know You Database Database generator — jahdb-db-get-to-know-you-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GTKY-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Question: Where are you from originally...",
  "Question: What do you do for fun around here...",
  "Question: How did you end up in this class...",
  "Question: What kind of music are you into...",
  "Question: What food have you enjoyed most here...",
  "Question: What shows are you watching lately...",
  "Question: What pets have been part of your life...",
  "Question: What did you do last weekend...",
  "Question: How long have you lived here...",
  "Question: What is your favorite thing about this neighborhood...",
  "Question: Where did you go to school..."
 ],
 "Compounded": [
  "Question: What is something you're passionate about...",
  "Question: How do you like to spend your free time...",
  "Question: What is the best advice you've gotten...",
  "Question: What are you working toward right now...",
  "Question: What is a skill you'd love to learn...",
  "Question: How would your friends describe you...",
  "Question: What is your favorite memory from last year...",
  "Question: What does your ideal weekend look like...",
  "Question: What are you most grateful for these days...",
  "Question: How do you recharge when you're drained...",
  "Question: What is something you've changed your mind about...",
  "Question: What tradition matters most to you..."
 ],
 "Advanced": [
  "Question: What do you want your life to stand for...",
  "Question: When did you last feel truly proud...",
  "Question: What fear have you outgrown...",
  "Question: How have you changed in five years...",
  "Question: What are you still hoping for...",
  "Question: Who shaped you most...",
  "Question: What lesson took longest to learn...",
  "Question: What would you tell your younger self...",
  "Question: What does a good life mean to you...",
  "Question: What are you working through right now...",
  "Question: When do you feel most alive..."
 ]
};
var DEMOKIND="bridge-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Get to Know You Study — "+safe+"\n"
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
    name:topic+' — get-to-know-you record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A get-to-know-you record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-get-to-know-you-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-get-to-know-you',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
