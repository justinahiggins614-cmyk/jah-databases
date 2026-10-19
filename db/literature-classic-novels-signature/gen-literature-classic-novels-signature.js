(function(){'use strict';
/* JAH Signature Classic Novels Database generator — "jahdb-literature-classic-novels-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Pride and Prejudice — Jane Austen (Signature Edition)", "Jane Eyre — Charlotte Brontë (Signature Edition)", "Great Expectations — Charles Dickens (Signature Edition)", "Adventures of Huckleberry Finn — Mark Twain (Signature Edition)", "Treasure Island — Robert Louis Stevenson (Signature Edition)", "The Time Machine — H. G. Wells (Signature Edition)", "Frankenstein — Mary Shelley (Signature Edition)", "Dracula — Bram Stoker (Signature Edition)", "The Picture of Dorian Gray — Oscar Wilde (Signature Edition)", "Wuthering Heights — Emily Brontë (Signature Edition)", "Little Women — Louisa May Alcott (Signature Edition)", "The Call of the Wild — Jack London (Signature Edition)"], "Compounded": ["Moby-Dick — Herman Melville (Signature Edition)", "Crime and Punishment — Fyodor Dostoevsky (Signature Edition)", "Anna Karenina — Leo Tolstoy (Signature Edition)", "Les Misérables — Victor Hugo (Signature Edition)", "The Brothers Karamazov — Fyodor Dostoevsky (Signature Edition)", "Madame Bovary — Gustave Flaubert (Signature Edition)", "The Count of Monte Cristo — Alexandre Dumas (Signature Edition)", "Middlemarch — George Eliot (Signature Edition)", "Tess of the d'Urbervilles — Thomas Hardy (Signature Edition)", "The Red Badge of Courage — Stephen Crane (Signature Edition)", "Heart of Darkness — Joseph Conrad (Signature Edition)", "The Jungle — Upton Sinclair (Signature Edition)"], "Advanced": ["Ulysses — James Joyce (Signature Edition)", "War and Peace — Leo Tolstoy (Signature Edition)", "Don Quixote — Miguel de Cervantes (Signature Edition)", "In Search of Lost Time — Marcel Proust (Signature Edition)", "The Magic Mountain — Thomas Mann (Signature Edition)", "The Trial — Franz Kafka (Signature Edition)", "Absalom, Absalom! — William Faulkner (Signature Edition)", "The Sound and the Fury — William Faulkner (Signature Edition)", "One Hundred Years of Solitude — Gabriel García Márquez (Signature Edition)", "Infinite Jest — David Foster Wallace (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-classic-novels-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original literary record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original literary record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-literature-classic-novels-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-classic-novels-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
