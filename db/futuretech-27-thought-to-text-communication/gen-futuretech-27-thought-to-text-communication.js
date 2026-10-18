(function(){'use strict';
/* JAH The Thought-to-Text Communication Future Technology Database generator — jahdb-"futuretech-27-thought-to-text-communication"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT27-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Locked-in syndrome described",
    "The Diving Bell and the Butterfly",
    "Eye-tracking communication",
    "Farwell-Donchin P300 speller",
    "BrainGate typing",
    "ECoG speech decoding begins",
    "Handwriting BCI: 90 characters per minute",
    "UCSF speech neuroprosthesis",
    "78 wpm with an avatar",
    "fMRI semantic decoding",
    "ALS patients speak again",
    "Non-invasive speech decoding advances"
  ],
  "Compounded": [
    "Multilingual thought decoding",
    "Real-time conversation pace",
    "Thought-to-text for stroke",
    "The home-use BCI speller",
    "SSVEP spellers: fast and non-invasive",
    "Attempted vs imagined speech",
    "The cocktail-party brain",
    "Decoding inner speech itself",
    "Thought-to-text for extreme jobs",
    "The end of keyboards",
    "The 150-wpm barrier (projection)"
  ],
  "Advanced": [
    "Silent speech for everyone",
    "Emotion in decoded speech",
    "Thought privacy: the inner voice",
    "Courtrooms and decoded testimony",
    "The universal thought keyboard",
    "Dream transcription (projection)",
    "Inner monologue interfaces",
    "Thought-to-thought messaging",
    "The working thought-to-text",
    "A world where no one is silenced",
    "The ethics of the inner voice"
  ]
};
function demoProgram(topic,field,seed){
  return "# Thought-to-Text Communication Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 thought-to-text record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A thought-to-text record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-27-thought-to-text-communication",name:"The Thought-to-Text Communication Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-27-thought-to-text-communication"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-27-thought-to-text-communication",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
