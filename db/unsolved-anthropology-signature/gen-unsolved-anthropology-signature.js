(function(){'use strict';
/* JAH The Unsolved Anthropology Signature Database generator — jahdb-unsolved-anthropology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USANS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Bipedalism Came First (Signature Edition) - Human Origins",
  "The Tripling of the Hominin Brain (Signature Edition) - Human Origins",
  "The Fate of the Neanderthals (Signature Edition) - Human Origins",
  "Who Were the Denisovans (Signature Edition) - Human Origins",
  "The Hobbit of Flores (Signature Edition) - Human Origins",
  "The Cooking Hypothesis (Signature Edition) - Human Origins",
  "Why Grandmothers Exist (Signature Edition) - Human Origins",
  "Why Humans Pair-Bond (Signature Edition) - Human Origins",
  "The Origins of Language (Signature Edition) - Language and Mind",
  "Why Every Culture Has Religion (Signature Edition) - Culture and Society",
  "The Incest Taboo (Signature Edition) - Culture and Society"
 ],
 "Compounded": [
  "Why Farm: The Agricultural Riddle (Signature Edition) - Deep Time",
  "The Peopling of the Americas (Signature Edition) - Deep Time",
  "The Upper Paleolithic Creative Explosion (Signature Edition) - Deep Time",
  "The Megafaunal Extinctions (Signature Edition) - Deep Time",
  "Why Writing Was Invented Four Times (Signature Edition) - Deep Time",
  "From Chiefdoms to States (Signature Edition) - Culture and Society",
  "Why Complex Societies Collapse (Signature Edition) - Culture and Society",
  "The Original Affluent Society Debate (Signature Edition) - Culture and Society",
  "Why Humans Cooperate With Strangers (Signature Edition) - Culture and Society",
  "The Evolution of Morality (Signature Edition) - Language and Mind",
  "Ritual: Why Costly Rituals Persist (Signature Edition) - Culture and Society",
  "The Self-Domestication Hypothesis (Signature Edition) - Human Origins"
 ],
 "Advanced": [
  "Are There True Cultural Universals (Signature Edition) - Culture and Society",
  "The Units of Cultural Evolution (Signature Edition) - Culture and Society",
  "The Demographic Transition Puzzle (Signature Edition) - Culture and Society",
  "The Origins of Inequality (Signature Edition) - Culture and Society",
  "The Sexual Division of Labor (Signature Edition) - Human Origins",
  "Why Symbolic Behavior Came So Late (Signature Edition) - Deep Time",
  "The Function of Prehistoric Art (Signature Edition) - Deep Time",
  "Dreaming and Sleep: The Evolutionary Why (Signature Edition) - Human Origins",
  "Race: Biology and the Remaining Puzzles (Signature Edition) - Human Origins",
  "The Gender Divergence in Prehistory (Signature Edition) - Culture and Society",
  "What Makes Humans Unique: The Synthesis (Signature Edition) - Language and Mind"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Anthropology Study — "+safe+"\n"
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
    demo:{kind:"unsolved-anthropology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-anthropology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-anthropology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
