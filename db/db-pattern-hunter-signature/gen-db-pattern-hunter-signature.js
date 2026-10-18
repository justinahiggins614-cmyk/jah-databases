(function(){'use strict';
/* JAH The Pattern Hunter Database Signature Database generator — jahdb-db-pattern-hunter-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PATHUNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Pattern: 2, 4, 6, 8, 10...",
  "Pattern: 5, 10, 15, 20, 25...",
  "Pattern: 1, 3, 5, 7, 9...",
  "Pattern: 10, 20, 30, 40, 50...",
  "Pattern: 3, 6, 9, 12, 15...",
  "Pattern: 100, 90, 80, 70, 60...",
  "Pattern: 1, 4, 9, 16, 25...",
  "Pattern: 2, 4, 8, 16, 32...",
  "Pattern: 1, 1, 2, 3, 5...",
  "Pattern: 1, 2, 4, 7, 11...",
  "Pattern: 3, 3, 3, 3, 3..."
 ],
 "Compounded": [
  "Pattern: 2, 3, 5, 7, 11...",
  "Pattern: 1, 3, 6, 10, 15...",
  "Pattern: 1, 8, 27, 64, 125...",
  "Pattern: 5, 11, 17, 23, 29...",
  "Pattern: 3, 9, 27, 81, 243...",
  "Pattern: 0, 1, 4, 9, 16...",
  "Pattern: 2, 6, 12, 20, 30...",
  "Pattern: 1, 2, 6, 24, 120...",
  "Pattern: 7, 14, 28, 56, 112...",
  "Pattern: 64, 32, 16, 8, 4...",
  "Pattern: 1, 4, 7, 10, 13...",
  "Pattern: 4, 7, 12, 19, 28..."
 ],
 "Advanced": [
  "Pattern: 1, 11, 21, 1211, 111221...",
  "Pattern: 2, 5, 11, 23, 47...",
  "Pattern: 1, 2, 5, 10, 17...",
  "Pattern: 0, 2, 6, 12, 20...",
  "Pattern: 1, 3, 4, 7, 11...",
  "Pattern: 3, 5, 9, 17, 33...",
  "Pattern: 8, 6, 4, 2, 0...",
  "Pattern: 1, 5, 13, 29, 61...",
  "Pattern: 6, 10, 18, 34, 66...",
  "Pattern: 2, 5, 10, 17, 26...",
  "Pattern: 11, 13, 17, 19, 23..."
 ]
};
var DEMOKIND="sequence-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Pattern Hunter Study — "+safe+"\n"
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
    name:topic+' — pattern puzzle record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A pattern puzzle record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-pattern-hunter-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-pattern-hunter-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
