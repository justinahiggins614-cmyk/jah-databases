(function(){'use strict';
/* JAH The Secret Identity Puzzle Signature Database generator — jahdb-db-secret-identity-puzzle-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSIPS-";
var FIELDS=["Masked Figures","Double Lives","Hidden Heirs"];
var TOPICS={
 "Masked Figures": [
  "The Midnight Conductor (Signature Edition) \u2014 Masked Figures",
  "The Signature Method for The Midnight Conductor \u2014 Masked Figures",
  "The Captain's Widow (Signature Edition) \u2014 Masked Figures",
  "The Signature Method for The Captain's Widow \u2014 Masked Figures",
  "The Pianist's Hands (Signature Edition) \u2014 Masked Figures",
  "The Signature Method for The Pianist's Hands \u2014 Masked Figures",
  "The Twin's Alibi (Signature Edition) \u2014 Masked Figures",
  "The Signature Method for The Twin's Alibi \u2014 Masked Figures",
  "The Night Watchman (Signature Edition) \u2014 Masked Figures",
  "The Signature Method for The Night Watchman \u2014 Masked Figures",
  "The Unmasking (Signature Edition) \u2014 Masked Figures",
  "The Signature Method for The Unmasking \u2014 Masked Figures"
 ],
 "Double Lives": [
  "The Night Librarian (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Night Librarian \u2014 Double Lives",
  "The Baker's Apprentice (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Baker's Apprentice \u2014 Double Lives",
  "The Village Doctor (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Village Doctor \u2014 Double Lives",
  "The Retired Judge (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Retired Judge \u2014 Double Lives",
  "The Anonymous Author (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Anonymous Author \u2014 Double Lives",
  "The Ghostwriter (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Ghostwriter \u2014 Double Lives",
  "The Forger's Hand (Signature Edition) \u2014 Double Lives",
  "The Signature Method for The Forger's Hand \u2014 Double Lives"
 ],
 "Hidden Heirs": [
  "The Gardener's Daughter (Signature Edition) \u2014 Hidden Heirs",
  "The Signature Method for The Gardener's Daughter \u2014 Hidden Heirs",
  "The Missing Heir (Signature Edition) \u2014 Hidden Heirs",
  "The Signature Method for The Missing Heir \u2014 Hidden Heirs",
  "The Heiress in Hiding (Signature Edition) \u2014 Hidden Heirs",
  "The Signature Method for The Heiress in Hiding \u2014 Hidden Heirs",
  "The Stranger's Scar (Signature Edition) \u2014 Hidden Heirs",
  "The Signature Method for The Stranger's Scar \u2014 Hidden Heirs"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Secret Identity Study — "+safe+"\n"
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
    name:topic+' — secret identity puzzle record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A secret identity puzzle record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-secret-identity-puzzle-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-secret-identity-puzzle-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
