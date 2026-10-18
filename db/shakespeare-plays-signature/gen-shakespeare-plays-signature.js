(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-shakespeare-plays-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SKPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Who Was Shakespeare (Signature edition)",
  "Hamlet (Signature edition)",
  "Romeo and Juliet (Signature edition)",
  "Macbeth (Signature edition)",
  "Othello (Signature edition)",
  "King Lear (Signature edition)",
  "A Midsummer Night's Dream (Signature edition)",
  "The Tempest (Signature edition)",
  "Much Ado About Nothing (Signature edition)",
  "Henry V (Signature edition)",
  "Julius Caesar (Signature edition)"
 ],
 "Compounded": [
  "The Globe Theatre (Signature edition)",
  "Iambic Pentameter (Signature edition)",
  "The Five-Act Structure (Signature edition)",
  "Shakespeare's Fools (Signature edition)",
  "The Histories Cycle (Signature edition)",
  "The Problem Plays (Signature edition)",
  "Cross-Dressing in Comedy (Signature edition)",
  "Shakespeare's Villains (Signature edition)",
  "The Authorship Question (Signature edition)",
  "The First Folio (Signature edition)",
  "Shakespeare's Sources (Signature edition)",
  "The Late Romances (Signature edition)"
 ],
 "Advanced": [
  "Shakespearean Criticism (Signature edition)",
  "Feminist Readings (Signature edition)",
  "Postcolonial Tempest (Signature edition)",
  "Shakespeare in Film (Signature edition)",
  "Modern Stagings (Signature edition)",
  "Verse Speaking (Signature edition)",
  "Textual Variants (Quarto/Folio) (Signature edition)",
  "Soliloquy Technique (Signature edition)",
  "Shakespeare's Language Legacy (Signature edition)",
  "The Sonnets (Context) (Signature edition)",
  "Shakespeare's Legacy (Signature edition)"
 ]
};
var DEMOKIND="verse scanning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Verse scanner — "+safe+"\n"
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
    name:topic+' — music genre record',
    title:topic,
    description:'SIGNATURE SAMPLE (generated — structural sample). A music genre record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-shakespeare-plays-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shakespeare-plays-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
