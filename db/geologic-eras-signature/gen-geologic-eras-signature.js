(function(){'use strict';
/* JAH Signature Geologic Eras Database generator — jahdb-geologic-eras-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ERAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Hadean Eon", "Signature Study: Eoarchean Era", "Signature Study: Paleoarchean Era", "Signature Study: Mesoarchean Era", "Signature Study: Neoarchean Era", "Signature Study: Paleoproterozoic Era", "Signature Study: Mesoproterozoic Era", "Signature Study: Neoproterozoic Era", "Signature Study: Cambrian Period", "Signature Study: Ordovician Period", "Signature Study: Silurian Period", "Signature Study: Devonian Period"], "Compounded": ["Signature Study: Mississippian Subperiod", "Signature Study: Pennsylvanian Subperiod", "Signature Study: Permian Period", "Signature Study: Triassic Period", "Signature Study: Jurassic Period", "Signature Study: Cretaceous Period", "Signature Study: Paleogene Period", "Signature Study: Neogene Period", "Signature Study: Quaternary Period", "Signature Study: Formation of the Moon", "Signature Study: Late Heavy Bombardment"], "Advanced": ["Signature Study: Origin of Life", "Signature Study: Great Oxidation Event", "Signature Study: Huronian Glaciation", "Signature Study: First Eukaryotes", "Signature Study: Cambrian Explosion", "Signature Study: Ordovician-Silurian Extinction", "Signature Study: Late Devonian Extinction", "Signature Study: Permian-Triassic Extinction", "Signature Study: Triassic-Jurassic Extinction", "Signature Study: Cretaceous-Paleogene Extinction", "Signature Study: Rise of Homo sapiens"]};
var DEMOKIND="deep time math";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature geologic demo: Ma-span arithmetic with real ICS boundary dates. Educational illustration.\n# Topic: \""+safe+"\" | Field: "+field+"\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('Sample record — structural sample, not an archive entry.')\n"
   + "print(record['topic'] + ' [' + record['field'] + ']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A Signature deep-time study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:"signature-generated",
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
var gen={version:"jahdb-geologic-eras-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('geologic-eras-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
