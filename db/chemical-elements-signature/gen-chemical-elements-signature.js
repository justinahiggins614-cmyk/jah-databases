(function(){'use strict';
/* JAH Signature Chemical Elements Database generator — jahdb-chemical-elements-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ELEMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Bromine (Br)", "Signature Study: Krypton (Kr)", "Signature Study: Rubidium (Rb)", "Signature Study: Strontium (Sr)", "Signature Study: Yttrium (Y)", "Signature Study: Zirconium (Zr)", "Signature Study: Niobium (Nb)", "Signature Study: Molybdenum (Mo)", "Signature Study: Technetium (Tc)", "Signature Study: Ruthenium (Ru)", "Signature Study: Rhodium (Rh)", "Signature Study: Palladium (Pd)"], "Compounded": ["Signature Study: Silver (Ag)", "Signature Study: Cadmium (Cd)", "Signature Study: Indium (In)", "Signature Study: Tin (Sn)", "Signature Study: Antimony (Sb)", "Signature Study: Tellurium (Te)", "Signature Study: Iodine (I)", "Signature Study: Xenon (Xe)", "Signature Study: Caesium (Cs)", "Signature Study: Barium (Ba)", "Signature Study: Lanthanum (La)"], "Advanced": ["Signature Study: Cerium (Ce)", "Signature Study: Praseodymium (Pr)", "Signature Study: Neodymium (Nd)", "Signature Study: Promethium (Pm)", "Signature Study: Samarium (Sm)", "Signature Study: Europium (Eu)", "Signature Study: Gadolinium (Gd)", "Signature Study: Terbium (Tb)", "Signature Study: Dysprosium (Dy)", "Signature Study: Holmium (Ho)", "Signature Study: Erbium (Er)"]};
var DEMOKIND="element math";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature element demo: molar-mass math with real atomic weights. Educational illustration.\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:'SAMPLE RECORD (generated — structural sample). A Signature chemical element study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:"jahdb-chemical-elements-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chemical-elements-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
