(function(){'use strict';
/* JAH Signature Science Fiction Database generator — "jahdb-literature-science-fiction-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSFS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Frankenstein — Mary Shelley (Signature Edition)", "The Time Machine — H. G. Wells (Signature Edition)", "The War of the Worlds — H. G. Wells (Signature Edition)", "Brave New World — Aldous Huxley (Signature Edition)", "1984 — George Orwell (Signature Edition)", "Fahrenheit 451 — Ray Bradbury (Signature Edition)", "Foundation — Isaac Asimov (Signature Edition)", "Dune — Frank Herbert (Signature Edition)", "Stranger in a Strange Land — Robert Heinlein (Signature Edition)", "The Hitchhiker's Guide — Douglas Adams (Signature Edition)", "Ender's Game — Orson Scott Card (Signature Edition)", "Jurassic Park — Michael Crichton (Signature Edition)"], "Compounded": ["Neuromancer — William Gibson (Signature Edition)", "Snow Crash — Neal Stephenson (Signature Edition)", "The Left Hand of Darkness — Ursula K. Le Guin (Signature Edition)", "Rendezvous with Rama — Arthur C. Clarke (Signature Edition)", "Childhood's End — Arthur C. Clarke (Signature Edition)", "The Martian Chronicles — Ray Bradbury (Signature Edition)", "I, Robot — Isaac Asimov (Signature Edition)", "Do Androids Dream of Electric Sheep? — Philip K. Dick (Signature Edition)", "The Dispossessed — Ursula K. Le Guin (Signature Edition)", "Hyperion — Dan Simmons (Signature Edition)", "The Forever War — Joe Haldeman (Signature Edition)", "Ringworld — Larry Niven (Signature Edition)"], "Advanced": ["Solaris — Stanisław Lem (Signature Edition)", "Roadside Picnic — Strugatsky Brothers (Signature Edition)", "The Stars My Destination — Alfred Bester (Signature Edition)", "A Fire Upon the Deep — Vernor Vinge (Signature Edition)", "Blindsight — Peter Watts (Signature Edition)", "Anathem — Neal Stephenson (Signature Edition)", "Consider Phlebas — Iain M. Banks (Signature Edition)", "Dhalgren — Samuel R. Delany (Signature Edition)", "Stand on Zanzibar — John Brunner (Signature Edition)", "The Female Man — Joanna Russ (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-science-fiction-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-literature-science-fiction-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-science-fiction-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
