(function(){'use strict';
/* JAH The Conversation Card Deck Database Signature Database generator — jahdb-db-conversation-card-deck-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CONCARDDES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Card: What is your favorite way to spend a free afternoon...",
  "Card: What food could you eat every week without getting bor...",
  "Card: What is a small thing that always makes you smile...",
  "Card: If you could learn any skill instantly, what would it...",
  "Card: What is your favorite season, and why...",
  "Card: What movie have you watched more than twice...",
  "Card: What is the best trip you have ever taken...",
  "Card: What hobby have you always wanted to try...",
  "Card: What is your go-to comfort food...",
  "Card: If you had a free Saturday with no obligations, what w...",
  "Card: What song never fails to lift your mood..."
 ],
 "Compounded": [
  "Card: What is something you believed as a kid that turned ou...",
  "Card: What is the most useful thing anyone ever taught you...",
  "Card: What would you do differently if you could relive one...",
  "Card: What is a tradition from your family you want to keep...",
  "Card: When do you feel most like yourself...",
  "Card: What is the kindest thing a stranger ever did for you...",
  "Card: What fear have you mostly outgrown...",
  "Card: What is something you're proud of that few people know...",
  "Card: If you could have dinner with anyone, living or not, w...",
  "Card: What is the best advice you've ever received...",
  "Card: What small habit improved your life most...",
  "Card: What place feels like home to you, and why..."
 ],
 "Advanced": [
  "Card: What do you want your life to have stood for...",
  "Card: When did you last change your mind about something imp...",
  "Card: What is the hardest thing you've ever forgiven...",
  "Card: What would you attempt if you knew you couldn't fail...",
  "Card: How have you changed most in the last five years...",
  "Card: What does a good life mean to you...",
  "Card: What are you still hoping for...",
  "Card: What lesson took you longest to learn...",
  "Card: Who shaped you most, and how...",
  "Card: What would you tell your younger self...",
  "Card: What are you most grateful for right now..."
 ]
};
var DEMOKIND="card-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Conversation Card Study — "+safe+"\n"
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
    name:topic+' — conversation card record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A conversation card record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-conversation-card-deck-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-conversation-card-deck-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
