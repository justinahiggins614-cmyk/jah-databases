(function(){'use strict';
/* JAH The Embedded Mobile Local Signature Database generator — jahdb-embedded-mobile-local-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMBLS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature SQLite Engine",
  "Signature Realm Engine",
  "Signature ObjectBox Engine",
  "Signature Couchbase Lite Engine",
  "Signature WatermelonDB Engine",
  "Signature RxDB Engine",
  "Signature LokiJS Engine",
  "Signature NeDB Engine",
  "Signature lowdb Engine",
  "Signature SQL.js Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: one square file, sub-squares\n" +
   "PAGE = 4\n" +
   "pages = []  # the file: a square of page sub-squares\n" +
   "def write(rec):\n" +
   "    if not pages or len(pages[-1]) >= PAGE: pages.append([])\n" +
   "    pages[-1].append(rec)\n" +
   "    return (len(pages), len(pages[-1]))  # (page, slot): measured from Signature-One\n" +
   "for r in [\"r1\", \"r2\", \"r3\", \"r4\", \"r5\"]:\n" +
   "    print(r, \"-> page/slot\", write(r))\n" +
   "print(\"file squares:\", pages)\n" +
   "print(\"Offsets are lines measured from the file's Signature-One start.\")\n" +
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
var gen={version:'jahdb-embedded-mobile-local-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('embedded-mobile-local-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
