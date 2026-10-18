(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-famous-poets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FPOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Makes a Poet Great (Signature edition)",
  "Homer (Signature edition)",
  "Sappho (Signature edition)",
  "Virgil (Signature edition)",
  "Dante Alighieri (Signature edition)",
  "Geoffrey Chaucer (Signature edition)",
  "William Shakespeare (Poet) (Signature edition)",
  "John Milton (Signature edition)",
  "William Wordsworth (Signature edition)",
  "John Donne (Signature edition)",
  "William Blake (Signature edition)"
 ],
 "Compounded": [
  "John Keats (Signature edition)",
  "Percy Bysshe Shelley (Signature edition)",
  "Lord Byron (Signature edition)",
  "Emily Dickinson (Signature edition)",
  "Walt Whitman (Signature edition)",
  "Edgar Allan Poe (Poet) (Signature edition)",
  "Robert Frost (Signature edition)",
  "T.S. Eliot (Signature edition)",
  "W.B. Yeats (Signature edition)",
  "Pablo Neruda (Signature edition)",
  "Langston Hughes (Signature edition)",
  "Rainer Maria Rilke (Signature edition)"
 ],
 "Advanced": [
  "Sylvia Plath (Signature edition)",
  "Seamus Heaney (Signature edition)",
  "Maya Angelou (Signature edition)",
  "Mary Oliver (Signature edition)",
  "Rumi (Signature edition)",
  "Matsuo Basho (Signature edition)",
  "Li Bai (Li Po) (Signature edition)",
  "Anna Akhmatova (Signature edition)",
  "Derek Walcott (Signature edition)",
  "Louise Gluck (Signature edition)",
  "The Poet Laureate Tradition (Signature edition)"
 ]
};
var DEMOKIND="rhyme-scheme labeling";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Rhyme-scheme labeler — "+safe+"\n"
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
var gen={version:'jahdb-famous-poets-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('famous-poets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
