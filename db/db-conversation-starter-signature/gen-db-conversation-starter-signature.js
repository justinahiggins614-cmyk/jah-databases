(function(){'use strict';
/* JAH The Conversation Starter Database Signature Database generator — jahdb-db-conversation-starter-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CVSTAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Starter: Hi! I don't think we've met - I'm Alex...",
  "Starter: That looks interesting - what is it...",
  "Starter: Have you been here before...",
  "Starter: I love your jacket - where did you find it...",
  "Starter: What brings you here today...",
  "Starter: Are you working on anything fun lately...",
  "Starter: This coffee is great - do you come here often...",
  "Starter: I'm new here - any tips for a beginner...",
  "Starter: What did you think of the speaker...",
  "Starter: Your dog is adorable - what's their name...",
  "Starter: Is this seat taken..."
 ],
 "Compounded": [
  "Starter: What's the most interesting thing you've learned latel...",
  "Starter: I'm trying to get into hiking - any trail recommendati...",
  "Starter: What do you do when you're not working...",
  "Starter: I overheard you mention travel - where's your favorite...",
  "Starter: What's keeping you busy these days...",
  "Starter: I'm collecting book recommendations - read anything go...",
  "Starter: What part of this do you enjoy most...",
  "Starter: How did you get into this...",
  "Starter: What's something you're looking forward to...",
  "Starter: I noticed you're reading - how is it...",
  "Starter: What's your take on the new exhibit...",
  "Starter: Do you have any fun weekend plans..."
 ],
 "Advanced": [
  "Starter: What's something you changed your mind about recently...",
  "Starter: What are you most proud of that doesn't fit on a resum...",
  "Starter: If you could master anything overnight, what would it...",
  "Starter: What's the best conversation you've had lately...",
  "Starter: What does a perfect day look like for you...",
  "Starter: What's something small that made your week...",
  "Starter: How do you like to spend your Sundays...",
  "Starter: What's a skill you wish school had taught...",
  "Starter: What are you curious about these days...",
  "Starter: What's the kindest thing someone did for you lately...",
  "Starter: If you had an extra hour daily, how would you spend it..."
 ]
};
var DEMOKIND="opener-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Conversation Starter Study — "+safe+"\n"
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
    name:topic+' — conversation starter record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A conversation starter record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-conversation-starter-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-conversation-starter-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
