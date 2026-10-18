(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-fantasy-literature-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FANS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Fantasy Literature (Signature edition)",
  "The Lord of the Rings (Signature edition)",
  "The Hobbit (Signature edition)",
  "A Wizard of Earthsea (Signature edition)",
  "The Lion, the Witch and the Wardrobe (Signature edition)",
  "Harry Potter and the Philosopher's Stone (Signature edition)",
  "The Once and Future King (Signature edition)",
  "Conan the Barbarian (Signature edition)",
  "The Princess Bride (Signature edition)",
  "The Chronicles of Prydain (Signature edition)",
  "The Dark Is Rising (Signature edition)"
 ],
 "Compounded": [
  "High Fantasy vs Low Fantasy (Signature edition)",
  "The Hero's Journey in Fantasy (Signature edition)",
  "Magic Systems: Hard vs Soft (Signature edition)",
  "Tolkien's Worldbuilding Legacy (Signature edition)",
  "Discworld (Signature edition)",
  "A Song of Ice and Fire (Signature edition)",
  "The Name of the Wind (Signature edition)",
  "Urban Fantasy (Signature edition)",
  "Portal Fantasy (Signature edition)",
  "Dark Fantasy (Signature edition)",
  "Epic Fantasy Doorstoppers (Signature edition)",
  "Fairy-Tale Retellings (Signature edition)"
 ],
 "Advanced": [
  "Grimdark Fantasy (Signature edition)",
  "The New Weird (Signature edition)",
  "Fantasy Literary Criticism (Signature edition)",
  "Women Writers of Fantasy (Signature edition)",
  "Non-Western Fantasy Traditions (Signature edition)",
  "The Economics of Epic Series (Signature edition)",
  "Mythic Roots of Fantasy (Signature edition)",
  "Allegory in Fantasy: The Lewis-Tolkien Debate (Signature edition)",
  "Cozy Fantasy (Signature edition)",
  "Progression Fantasy (Signature edition)",
  "The Fantasy Canon Debates (Signature edition)"
 ]
};
var DEMOKIND="quest-stage mapping";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Quest-stage mapper — "+safe+"\n"
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
var gen={version:'jahdb-fantasy-literature-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fantasy-literature-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
