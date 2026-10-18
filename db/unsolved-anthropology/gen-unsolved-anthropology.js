(function(){'use strict';
/* JAH The Unsolved Anthropology Database generator — jahdb-unsolved-anthropology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USAN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Bipedalism Came First - Human Origins",
  "The Tripling of the Hominin Brain - Human Origins",
  "The Fate of the Neanderthals - Human Origins",
  "Who Were the Denisovans - Human Origins",
  "The Hobbit of Flores - Human Origins",
  "The Cooking Hypothesis - Human Origins",
  "Why Grandmothers Exist - Human Origins",
  "Why Humans Pair-Bond - Human Origins",
  "The Origins of Language - Language and Mind",
  "Why Every Culture Has Religion - Culture and Society",
  "The Incest Taboo - Culture and Society"
 ],
 "Compounded": [
  "Why Farm: The Agricultural Riddle - Deep Time",
  "The Peopling of the Americas - Deep Time",
  "The Upper Paleolithic Creative Explosion - Deep Time",
  "The Megafaunal Extinctions - Deep Time",
  "Why Writing Was Invented Four Times - Deep Time",
  "From Chiefdoms to States - Culture and Society",
  "Why Complex Societies Collapse - Culture and Society",
  "The Original Affluent Society Debate - Culture and Society",
  "Why Humans Cooperate With Strangers - Culture and Society",
  "The Evolution of Morality - Language and Mind",
  "Ritual: Why Costly Rituals Persist - Culture and Society",
  "The Self-Domestication Hypothesis - Human Origins"
 ],
 "Advanced": [
  "Are There True Cultural Universals - Culture and Society",
  "The Units of Cultural Evolution - Culture and Society",
  "The Demographic Transition Puzzle - Culture and Society",
  "The Origins of Inequality - Culture and Society",
  "The Sexual Division of Labor - Human Origins",
  "Why Symbolic Behavior Came So Late - Deep Time",
  "The Function of Prehistoric Art - Deep Time",
  "Dreaming and Sleep: The Evolutionary Why - Human Origins",
  "Race: Biology and the Remaining Puzzles - Human Origins",
  "The Gender Divergence in Prehistory - Culture and Society",
  "What Makes Humans Unique: The Synthesis - Language and Mind"
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
var gen={version:'jahdb-unsolved-anthropology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-anthropology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
