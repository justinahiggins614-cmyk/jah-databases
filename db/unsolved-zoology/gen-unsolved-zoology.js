(function(){'use strict';
/* JAH The Unsolved Zoology Database generator — jahdb-unsolved-zoology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USZO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Giraffes Have Long Necks - Foundations",
  "Why Zebras Have Stripes - Foundations",
  "Why Animals Sleep - Foundations",
  "How Homing Pigeons Navigate - Foundations",
  "How Monarch Butterflies Migrate - Foundations",
  "How Salmon Find Their Birth River - Foundations",
  "Why Whales Strand Themselves - Foundations",
  "Why Lemming Populations Cycle - Foundations",
  "How Desert Ants Navigate - Foundations",
  "How Electric Fish Sense Electricity - Foundations",
  "Why There Are No Wheels in Nature - Foundations",
  "How Cephalopods Change Color and Texture - Foundations"
 ],
 "Compounded": [
  "What Marks an Animal as Conscious - Compounded",
  "Do Non-Human Animals Have Language - Compounded",
  "How Eusociality Evolved - Compounded",
  "Why Sex Persists Despite the Twofold Cost - Compounded",
  "How Insect Flight Evolved - Compounded",
  "How Bats Evolved Flight and Echolocation - Compounded",
  "Why Some Animals Regenerate and Mammals Cannot - Compounded",
  "How the Vertebrate Jaw Evolved - Compounded",
  "Why Animals Age - Compounded",
  "How Parasites Control Host Behavior - Compounded",
  "How Tool Use Evolved in Animals - Compounded",
  "How Animals Time Their Migration - Compounded"
 ],
 "Advanced": [
  "What Caused the Cambrian Explosion - Advanced",
  "How Multicellular Animals Originated - Advanced",
  "Why Bilateral Symmetry Dominates Animals - Advanced",
  "Which Animal Branched Off First - Advanced",
  "What Selects Survivors of Mass Extinctions - Advanced",
  "How Birds Evolved Flight - Advanced",
  "Why Some Species Live for Centuries - Advanced",
  "Can We Predict Animal Evolution - Advanced",
  "How Consciousness Evolved - Advanced",
  "What the Last Common Ancestor of Animals Looked Like - Advanced"
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
var gen={version:'jahdb-unsolved-zoology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-zoology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
