(function(){'use strict';
/* JAH The Mind Uploading Future Technology Database — Signature Edition generator — jahdb-"futuretech-34-mind-uploading-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT34-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The soul in philosophy (Signature Edition)",
    "Descartes' dualism (Signature Edition)",
    "Frankenstein's assembled man (Signature Edition)",
    "The Turing test for minds (Signature Edition)",
    "Moravec's uploading vision (Signature Edition)",
    "Kurzweil's singularity (Signature Edition)",
    "The Ship of Theseus, neural edition (Signature Edition)",
    "Cryonics: the cold bet (Signature Edition)",
    "Brain preservation prizes (Signature Edition)",
    "Connectomics as the path (Signature Edition)",
    "Digital immortality startups (Signature Edition)",
    "Whole-brain emulation research (Signature Edition)"
  ],
  "Compounded": [
    "The identity upload debate (Signature Edition)",
    "Gilgamesh seeks immortality (Signature Edition)",
    "Elixir of life quests (Signature Edition)",
    "Alcor's first patients (Signature Edition)",
    "The simulation argument's impact (Signature Edition)",
    "The 2045 Initiative (Signature Edition)",
    "Carbon Copies project (Signature Edition)",
    "Digital twins of the dead (Signature Edition)",
    "The museum of minds (Signature Edition)",
    "Uploading and the law (Signature Edition)",
    "The upload divide (Signature Edition)"
  ],
  "Advanced": [
    "Gradual uploading (projection) (Signature Edition)",
    "Destructive uploading (projection) (Signature Edition)",
    "The upload's first words (Signature Edition)",
    "Upload rights and personhood (Signature Edition)",
    "Multiple copies: the branching self (Signature Edition)",
    "Upload economics (Signature Edition)",
    "The religion question (Signature Edition)",
    "Uploading animals (Signature Edition)",
    "The working mind upload (Signature Edition)",
    "Life after uploading (Signature Edition)",
    "The last death (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature mind uploading Study \u2014 "+topic+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+", 'src': 'signature'}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\n"
   + "print(summarize(record))\n"
   + "print('Signature-generated variant \u2014 not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 Signature mind uploading record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature mind uploading record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Signature-generated variant \u2014 not an archive record. Seeded archive records are the authoritative entries.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-34-mind-uploading-signature",name:"The Mind Uploading Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-34-mind-uploading-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-34-mind-uploading-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
