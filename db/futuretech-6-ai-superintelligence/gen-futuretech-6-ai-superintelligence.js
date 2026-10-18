(function(){'use strict';
/* JAH The AI Superintelligence Future Technology Database generator — jahdb-"futuretech-6-ai-superintelligence"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT6-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Turing proposes the imitation game",
    "The Dartmouth proposal names the field",
    "Logic Theorist: machines prove theorems",
    "The perceptron learns from examples",
    "Expert systems: DENDRAL and MYCIN",
    "Backpropagation makes deep learning possible",
    "Deep Blue defeats Kasparov",
    "Watson wins Jeopardy!",
    "AlexNet ignites the deep learning boom",
    "Deep reinforcement learning masters Atari",
    "AlphaGo defeats Lee Sedol",
    "The Transformer: Attention Is All You Need"
  ],
  "Compounded": [
    "GPT-3: scale brings emergent ability",
    "AlphaFold cracks protein folding",
    "ChatGPT brings AI to the public",
    "GPT-4: the multimodal frontier",
    "Scaling laws become engineering doctrine",
    "Evaluation science: benchmarks and red-teaming",
    "Reasoning models: test-time compute",
    "AI agents do multi-step work",
    "AI helps design the chips that train AI",
    "Automated research: AI as lab assistant",
    "Frontier labs name superintelligence the goal"
  ],
  "Advanced": [
    "Expert-level automation across professions",
    "Self-improving research loops",
    "The intelligence explosion scenario",
    "The alignment problem: steering superintelligence",
    "Superintelligence in science: compressed centuries",
    "Superintelligence in engineering and manufacturing",
    "Economic transformation hypotheses",
    "Governance frameworks for superintelligence",
    "Whole-civilization coordination",
    "Corrigibility: systems that accept oversight",
    "The working superintelligence: what done looks like"
  ]
};
function demoProgram(topic,field,seed){
  return "# AI Superintelligence Study \u2014 "+topic+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\n"
   + "print(summarize(record))\n"
   + "print('Generated variant \u2014 not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 AI superintelligence record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A AI superintelligence record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Generated variant \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Generated variant demo.'},
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-6-ai-superintelligence",name:"The AI Superintelligence Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-6-ai-superintelligence"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-6-ai-superintelligence",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
