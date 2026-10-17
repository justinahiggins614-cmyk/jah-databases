(function(){'use strict';
/* JAH The Unsolved Zoology Signature Database generator — jahdb-unsolved-zoology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USZOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Giraffes Have Long Necks (Signature Edition) - Foundations",
  "Why Zebras Have Stripes (Signature Edition) - Foundations",
  "Why Animals Sleep (Signature Edition) - Foundations",
  "How Homing Pigeons Navigate (Signature Edition) - Foundations",
  "How Monarch Butterflies Migrate (Signature Edition) - Foundations",
  "How Salmon Find Their Birth River (Signature Edition) - Foundations",
  "Why Whales Strand Themselves (Signature Edition) - Foundations",
  "Why Lemming Populations Cycle (Signature Edition) - Foundations",
  "How Desert Ants Navigate (Signature Edition) - Foundations",
  "How Electric Fish Sense Electricity (Signature Edition) - Foundations",
  "Why There Are No Wheels in Nature (Signature Edition) - Foundations",
  "How Cephalopods Change Color and Texture (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "What Marks an Animal as Conscious (Signature Edition) - Compounded",
  "Do Non-Human Animals Have Language (Signature Edition) - Compounded",
  "How Eusociality Evolved (Signature Edition) - Compounded",
  "Why Sex Persists Despite the Twofold Cost (Signature Edition) - Compounded",
  "How Insect Flight Evolved (Signature Edition) - Compounded",
  "How Bats Evolved Flight and Echolocation (Signature Edition) - Compounded",
  "Why Some Animals Regenerate and Mammals Cannot (Signature Edition) - Compounded",
  "How the Vertebrate Jaw Evolved (Signature Edition) - Compounded",
  "Why Animals Age (Signature Edition) - Compounded",
  "How Parasites Control Host Behavior (Signature Edition) - Compounded",
  "How Tool Use Evolved in Animals (Signature Edition) - Compounded",
  "How Animals Time Their Migration (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "What Caused the Cambrian Explosion (Signature Edition) - Advanced",
  "How Multicellular Animals Originated (Signature Edition) - Advanced",
  "Why Bilateral Symmetry Dominates Animals (Signature Edition) - Advanced",
  "Which Animal Branched Off First (Signature Edition) - Advanced",
  "What Selects Survivors of Mass Extinctions (Signature Edition) - Advanced",
  "How Birds Evolved Flight (Signature Edition) - Advanced",
  "Why Some Species Live for Centuries (Signature Edition) - Advanced",
  "Can We Predict Animal Evolution (Signature Edition) - Advanced",
  "How Consciousness Evolved (Signature Edition) - Advanced",
  "What the Last Common Ancestor of Animals Looked Like (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Zoology Study — "+safe+"\n"
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
    demo:{kind:"unsolved-zoology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-zoology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-zoology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
