(function(){'use strict';
/* JAH The Fallacy Detective Database Signature Database generator — jahdb-db-fallacy-detective-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FALDETS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Fallacy: You're too young to understand politics...",
  "Fallacy: Everyone is buying it, so it must be good...",
  "Fallacy: My opponent wants to defund everything, so vote for...",
  "Fallacy: It rained after I danced, so my dance caused the rai...",
  "Fallacy: You're either with us or against us...",
  "Fallacy: The expert said it, so it must be true...",
  "Fallacy: We've always done it this way...",
  "Fallacy: If we allow this, soon we'll allow everything...",
  "Fallacy: You can't prove ghosts don't exist, so they do...",
  "Fallacy: He's a criminal, so his argument about taxes is wron...",
  "Fallacy: This is new, so it must be better..."
 ],
 "Compounded": [
  "Fallacy: The study must be wrong because the researcher is bi...",
  "Fallacy: We tried nothing and it failed, so trying is pointle...",
  "Fallacy: A few fans were rude, so the whole fandom is toxic...",
  "Fallacy: You're a fine one to talk about honesty...",
  "Fallacy: The parts are light, so the whole must be light...",
  "Fallacy: The team is strong, so every player is strong...",
  "Fallacy: No one has complained, so the policy works...",
  "Fallacy: The law says so, so it must be right...",
  "Fallacy: Nature made it, so it's safe...",
  "Fallacy: He's rich, so his business advice is sound...",
  "Fallacy: The middle ground must be right...",
  "Fallacy: After this, therefore because of this..."
 ],
 "Advanced": [
  "Fallacy: The survivors all agree, so the plan works...",
  "Fallacy: This question assumes the answer - answer it...",
  "Fallacy: The correlation is strong, so the cause is found...",
  "Fallacy: If A then B; B happened, so A caused it...",
  "Fallacy: If A then B; not A, so not B...",
  "Fallacy: The exception disproves the rule...",
  "Fallacy: We can't test it, so it's equally likely true...",
  "Fallacy: The definition assumes what it defines...",
  "Fallacy: The word changed meaning mid-argument...",
  "Fallacy: The anecdote beats the statistics...",
  "Fallacy: Doing something beats doing nothing, so do this..."
 ]
};
var DEMOKIND="fallacy-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fallacy Study — "+safe+"\n"
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
    name:topic+' — fallacy case record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fallacy case record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-fallacy-detective-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-fallacy-detective-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
