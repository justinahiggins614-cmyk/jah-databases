(function(){'use strict';
/* JAH The Abstract Machines Database generator — jahdb-abstract-machines-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ACM-";
var FIELDS=["model"];
var TOPICS={
 "model": [
  "Turing Machines \u2014 model",
  "Universal Turing Machines \u2014 model",
  "Finite Automata \u2014 model",
  "Deterministic Finite Automata \u2014 model",
  "Nondeterministic Finite Automata \u2014 model",
  "Pushdown Automata \u2014 model",
  "Linear Bounded Automata \u2014 model",
  "Register Machines \u2014 model",
  "Counter Machines \u2014 model",
  "Random Access Machines \u2014 model",
  "Lambda Calculus \u2014 model",
  "Simply Typed Lambda Calculus \u2014 model",
  "Combinatory Logic \u2014 model",
  "SKI Combinators \u2014 model",
  "Graph Reduction \u2014 model",
  "Term Rewriting Systems \u2014 model",
  "String Rewriting \u2014 model",
  "Markov Algorithms \u2014 model",
  "Post Systems \u2014 model",
  "Petri Nets \u2014 model",
  "Colored Petri Nets \u2014 model",
  "Timed Petri Nets \u2014 model",
  "Statecharts \u2014 model",
  "Finite State Transducers \u2014 model",
  "B\u00fcchi Automata \u2014 model",
  "Tree Automata \u2014 model",
  "Alternating Automata \u2014 model",
  "Quantum Turing Machines \u2014 model",
  "Probabilistic Turing Machines \u2014 model",
  "Oracle Machines \u2014 model",
  "Interactive Proof Systems \u2014 model",
  "Cellular Automata \u2014 model",
  "Elementary Cellular Automata \u2014 model",
  "Lindenmayer Systems \u2014 model",
  "Substitution Systems \u2014 model",
  "Tag Systems \u2014 model",
  "Wang Tiles \u2014 model",
  "Abstract State Machines \u2014 model",
  "Pi-Calculus \u2014 model",
  "Ambient Calculus \u2014 model",
  "Actor Model \u2014 model",
  "CSP \u2014 model",
  "CCS \u2014 model",
  "Kahn Process Networks \u2014 model",
  "Synchronous Dataflow \u2014 model",
  "Boolean Networks \u2014 model",
  "Neural Network Models \u2014 model",
  "Spiking Neuron Models \u2014 model",
  "Membrane Computing \u2014 model",
  "DNA Computing Models \u2014 model",
  "Chemical Reaction Networks \u2014 model",
  "Population Protocols \u2014 model",
  "Swarm Models \u2014 model",
  "Game Semantics \u2014 model",
  "Trace Semantics \u2014 model",
  "Denotational Models \u2014 model",
  "Operational Models \u2014 model",
  "Axiomatic Models \u2014 model"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Abstract Machines — "+safe+"\n"
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
    name:topic+' — computational model record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A computational model record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-abstract-machines-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('abstract-machines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
