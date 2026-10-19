(function(){'use strict';
/* JAH The Synthetic Biology Future Technology Database — Signature Edition generator — jahdb-"futuretech-40-synthetic-biology-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT40-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Fermentation: ancient biotech (Signature Edition)",
    "Pasteur's germ theory (Signature Edition)",
    "Antibiotics from microbes (Signature Edition)",
    "Recombinant DNA: engineering microbes (Signature Edition)",
    "Genentech: the biotech industry (Signature Edition)",
    "Insulin from bacteria (Signature Edition)",
    "PCR: copying DNA (Signature Edition)",
    "The toggle switch (Signature Edition)",
    "The repressilator (Signature Edition)",
    "Artemisinin from yeast (Signature Edition)",
    "BioBricks and iGEM (Signature Edition)",
    "Venter's synthetic genome (Signature Edition)"
  ],
  "Compounded": [
    "Minimal genome: JCVI-syn3.0 (Signature Edition)",
    "CRISPR as the editing tool (Signature Edition)",
    "Synthetic yeast: Sc2.0 (Signature Edition)",
    "Cell-free systems (Signature Edition)",
    "Engineered living materials (Signature Edition)",
    "Biosecurity frameworks (Signature Edition)",
    "Mirror life debates (Signature Edition)",
    "The Asilomar legacy (Signature Edition)",
    "Bioremediation microbes (Signature Edition)",
    "Golden Rice (Signature Edition)",
    "The BioBrick registry (Signature Edition)"
  ],
  "Advanced": [
    "The Carlson curves (Signature Edition)",
    "Synthetic spider silk (Signature Edition)",
    "Engineered probiotics (Signature Edition)",
    "DIY bio movement (Signature Edition)",
    "Cellular agriculture (Signature Edition)",
    "Xenobiology (Signature Edition)",
    "The biosecurity bargain (Signature Edition)",
    "Synthetic nitrogen fixation (Signature Edition)",
    "Living computers (Signature Edition)",
    "The working synthetic biology (Signature Edition)",
    "Biology as technology (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature synthetic biology Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature synthetic biology record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature synthetic biology record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-40-synthetic-biology-signature",name:"The Synthetic Biology Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-40-synthetic-biology-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-40-synthetic-biology-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
