(function(){'use strict';
/* JAH The Molecular Nanotechnology Future Technology Database — Signature Edition generator — jahdb-futuretech-99-molecular-nanotechnology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT99-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Molecular Nanotechnology — Faraday's Nanoparticles (Signature Edition)", "Molecular Nanotechnology — Plenty of Room - Feynman's Challenge (Signature Edition)", "Molecular Nanotechnology — the Word Nanotechnology (Signature Edition)", "Molecular Nanotechnology — Seeing Atoms (Signature Edition)", "Molecular Nanotechnology — Buckyballs (Signature Edition)", "Molecular Nanotechnology — Engines of Creation (Signature Edition)", "Molecular Nanotechnology — IBM in Atoms (Signature Edition)", "Molecular Nanotechnology — Nanotubes - the Carbon Thread (Signature Edition)", "Molecular Nanotechnology — Nanosystems (Signature Edition)", "Molecular Nanotechnology — Nanowires (Signature Edition)", "Molecular Nanotechnology — the NNI (Signature Edition)"], "Compounded": ["Molecular Nanotechnology — the Great Debate (Signature Edition)", "Molecular Nanotechnology — Graphene (Signature Edition)", "Molecular Nanotechnology — DNA Origami (Signature Edition)", "Molecular Nanotechnology — Nano Products (Signature Edition)", "Molecular Nanotechnology — the Molecular Nobel (Signature Edition)", "Molecular Nanotechnology — DNA Robots (Signature Edition)", "Molecular Nanotechnology — Nanoparticle Vaccines (Signature Edition)", "Molecular Nanotechnology — Nano Mainstream (Signature Edition)", "Molecular Nanotechnology — the Molecular Wave - Nanotech Matures (Signature Edition)", "Molecular Nanotechnology — The Assembler (Signature Edition)", "Molecular Nanotechnology — Molecular Manufacturing (Signature Edition)", "Molecular Nanotechnology — The Nanofactory (Signature Edition)"], "Advanced": ["Molecular Nanotechnology — The Matter Compiler (Signature Edition)", "Molecular Nanotechnology — Programmable Matter in Molecular Nanotechnology (Signature Edition)", "Molecular Nanotechnology — The Medical Nanobot (Signature Edition)", "Molecular Nanotechnology — The Molecular Economy (Signature Edition)", "Molecular Nanotechnology — The Post-Scarcity World (Signature Edition)", "Molecular Nanotechnology — The Nanotech Civilization (Signature Edition)", "Molecular Nanotechnology — The Diamond Age (Signature Edition)", "Molecular Nanotechnology — The Molecular Internet (Signature Edition)", "Molecular Nanotechnology — The Universal Assembler (Signature Edition)", "Molecular Nanotechnology — The Assembled World (Signature Edition)", "Molecular Nanotechnology — Everyday Nanotech - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Molecular Nanotechnology study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-99-molecular-nanotechnology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-99-molecular-nanotechnology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
