(function(){'use strict';
/* JAH The Browser Emerging Signature Database generator — jahdb-browser-emerging-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BEMGS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature PouchDB (browser) Engine",
  "Signature Filebase Engine",
  "Signature Dexie.js Engine",
  "Signature ElectricSQL Engine",
  "Signature Turso Engine",
  "Signature chDB Engine",
  "Signature DuckDB-WASM Engine",
  "Signature TinyBase Engine",
  "Signature Automerge Engine",
  "Signature PGlite Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: pocket squares and sync lines\n" +
   "pocket = {\"a\": 1}          # the pocket square (device store)\n" +
   "cloud_square = {\"a\": 1, \"b\": 2}\n" +
   "plus_marks = []            # offline edits: plus marks on the pocket square\n" +
   "def mark(k, v): pocket[k] = v; plus_marks.append(k)\n" +
   "def merge():\n" +
   "    for k in plus_marks: cloud_square[k] = pocket[k]\n" +
   "    plus_marks.clear()\n" +
   "mark(\"c\", 3)\n" +
   "print(\"pocket:\", pocket, \"plus marks:\", plus_marks)\n" +
   "merge()\n" +
   "print(\"merged cloud square:\", cloud_square)\n" +
   "print(\"Sync draws lines between device squares; plus marks merge on reconnect.\")\n" +
   "\n";
  return tpl.split('__TOPIC__').join(safe);
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — electronics diagnostic record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A electronics diagnostic record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-browser-emerging-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('browser-emerging-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
