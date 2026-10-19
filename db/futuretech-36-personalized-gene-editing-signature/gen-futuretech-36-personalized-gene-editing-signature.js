(function(){'use strict';
/* JAH The Personalized Gene Editing Future Technology Database — Signature Edition generator — jahdb-"futuretech-36-personalized-gene-editing-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT36-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Mendel's peas (Signature Edition)",
    "DNA's double helix (Signature Edition)",
    "Recombinant DNA (Signature Edition)",
    "Genetic screening: PKU (Signature Edition)",
    "The Human Genome Project (Signature Edition)",
    "BRCA testing (Signature Edition)",
    "Pharmacogenomics (Signature Edition)",
    "Gene therapy's first success (Signature Edition)",
    "CRISPR-Cas9 (Signature Edition)",
    "CRISPR in human cells (Signature Edition)",
    "Sickle cell: Casgevy approved (Signature Edition)",
    "Luxturna: eyes edited (Signature Edition)"
  ],
  "Compounded": [
    "In vivo CRISPR: Intellia (Signature Edition)",
    "Base editing (Signature Edition)",
    "Prime editing (Signature Edition)",
    "Personalized CRISPR for one patient (Signature Edition)",
    "CAR-T: edited immune cells (Signature Edition)",
    "He Jiankui: the line crossed (Signature Edition)",
    "Polygenic risk scores (Signature Edition)",
    "Somatic vs germline: the bright line (Signature Edition)",
    "Zinc fingers: the first editors (Signature Edition)",
    "TALENs (Signature Edition)",
    "The $1,000 genome (Signature Edition)"
  ],
  "Advanced": [
    "Direct-to-consumer DNA testing (Signature Edition)",
    "CRISPR diagnostics: SHERLOCK (Signature Edition)",
    "Epigenome editing (Signature Edition)",
    "Newborn genome sequencing (Signature Edition)",
    "In utero gene therapy (projection) (Signature Edition)",
    "The $1,000 edit (Signature Edition)",
    "Editing for common disease (Signature Edition)",
    "De-extinction edits (Signature Edition)",
    "Enhancement edits: the debate (Signature Edition)",
    "The working personalized gene edit (Signature Edition)",
    "A world without genetic disease (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature gene editing Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature gene editing record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature gene editing record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-36-personalized-gene-editing-signature",name:"The Personalized Gene Editing Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-36-personalized-gene-editing-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-36-personalized-gene-editing-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
