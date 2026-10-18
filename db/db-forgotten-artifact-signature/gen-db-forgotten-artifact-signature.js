(function(){'use strict';
/* JAH The Forgotten Artifact Signature Database generator — jahdb-db-forgotten-artifact-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MFADS-";
var FIELDS=["Tools","Vessels","Tokens"];
var TOPICS={
 "Tools": [
  "The Bronze Hand (Signature Edition) \u2014 Tools",
  "The Signature Method for The Bronze Hand \u2014 Tools",
  "The Iron Key (Signature Edition) \u2014 Tools",
  "The Signature Method for The Iron Key \u2014 Tools",
  "The Crystal Lens (Signature Edition) \u2014 Tools",
  "The Signature Method for The Crystal Lens \u2014 Tools",
  "The Silent Bell of Remembrance (Signature Edition) \u2014 Tools",
  "The Signature Method for The Silent Bell of Remembrance \u2014 Tools",
  "The Mariner's Compass (Signature Edition) \u2014 Tools",
  "The Signature Method for The Mariner's Compass \u2014 Tools",
  "The Abacus With Extra Beads (Signature Edition) \u2014 Tools",
  "The Signature Method for The Abacus With Extra Beads \u2014 Tools",
  "The Ship's Hourglass (Signature Edition) \u2014 Tools",
  "The Signature Method for The Ship's Hourglass \u2014 Tools",
  "The Pocket Sundial (Signature Edition) \u2014 Tools",
  "The Signature Method for The Pocket Sundial \u2014 Tools",
  "The Dark Lantern (Signature Edition) \u2014 Tools",
  "The Signature Method for The Dark Lantern \u2014 Tools",
  "The Silver Quill (Signature Edition) \u2014 Tools",
  "The Signature Method for The Silver Quill \u2014 Tools"
 ],
 "Vessels": [
  "The Glass Orb (Signature Edition) \u2014 Vessels",
  "The Signature Method for The Glass Orb \u2014 Vessels",
  "The Hand Mirror (Signature Edition) \u2014 Vessels",
  "The Signature Method for The Hand Mirror \u2014 Vessels",
  "The Curiosity Cabinet (Signature Edition) \u2014 Vessels",
  "The Signature Method for The Curiosity Cabinet \u2014 Vessels"
 ],
 "Tokens": [
  "The Stone Tablet (Signature Edition) \u2014 Tokens",
  "The Signature Method for The Stone Tablet \u2014 Tokens",
  "The Bone Dice (Signature Edition) \u2014 Tokens",
  "The Signature Method for The Bone Dice \u2014 Tokens",
  "The Plague Mask (Signature Edition) \u2014 Tokens",
  "The Signature Method for The Plague Mask \u2014 Tokens",
  "The Wax Seal (Signature Edition) \u2014 Tokens",
  "The Signature Method for The Wax Seal \u2014 Tokens"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Forgotten Artifact Study — "+safe+"\n"
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
    name:topic+' — forgotten artifact record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A forgotten artifact record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-forgotten-artifact-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-forgotten-artifact-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
