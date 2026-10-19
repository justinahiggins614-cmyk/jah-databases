(function(){'use strict';
/* JAH Classic Novels Database generator — "jahdb-literature-classic-novels-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCN-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Pride and Prejudice — Jane Austen", "Jane Eyre — Charlotte Brontë", "Great Expectations — Charles Dickens", "Adventures of Huckleberry Finn — Mark Twain", "Treasure Island — Robert Louis Stevenson", "The Time Machine — H. G. Wells", "Frankenstein — Mary Shelley", "Dracula — Bram Stoker", "The Picture of Dorian Gray — Oscar Wilde", "Wuthering Heights — Emily Brontë", "Little Women — Louisa May Alcott", "The Call of the Wild — Jack London"], "Compounded": ["Moby-Dick — Herman Melville", "Crime and Punishment — Fyodor Dostoevsky", "Anna Karenina — Leo Tolstoy", "Les Misérables — Victor Hugo", "The Brothers Karamazov — Fyodor Dostoevsky", "Madame Bovary — Gustave Flaubert", "The Count of Monte Cristo — Alexandre Dumas", "Middlemarch — George Eliot", "Tess of the d'Urbervilles — Thomas Hardy", "The Red Badge of Courage — Stephen Crane", "Heart of Darkness — Joseph Conrad", "The Jungle — Upton Sinclair"], "Advanced": ["Ulysses — James Joyce", "War and Peace — Leo Tolstoy", "Don Quixote — Miguel de Cervantes", "In Search of Lost Time — Marcel Proust", "The Magic Mountain — Thomas Mann", "The Trial — Franz Kafka", "Absalom, Absalom! — William Faulkner", "The Sound and the Fury — William Faulkner", "One Hundred Years of Solitude — Gabriel García Márquez", "Infinite Jest — David Foster Wallace"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-classic-novels demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — literary record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A literary record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-literature-classic-novels-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-classic-novels",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
