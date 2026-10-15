(function(){'use strict';
/* JAH The Embedded Storage Engines Signature Database generator — jahdb-embedded-storage-engines-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STENS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature RocksDB Engine",
  "Signature LevelDB Engine",
  "Signature LMDB Engine",
  "Signature Pebble Engine",
  "Signature WiredTiger Engine",
  "Signature BadgerDB Engine",
  "Signature FASTER Engine",
  "Signature Sophia Engine",
  "Signature ForestDB Engine",
  "Signature Berkeley DB Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: live line, stacked squares\n" +
   "mem = []          # the live line (memtable): measured writes in order\n" +
   "squares = []      # stacked squares (SSTables): sealed sorted runs\n" +
   "def put(k, v):\n" +
   "    mem.append((k, v))\n" +
   "    if len(mem) >= 3:\n" +
   "        squares.append(sorted(mem)); mem.clear()  # square sealed\n" +
   "def get(k):\n" +
   "    for kk, vv in reversed(mem):\n" +
   "        if kk == k: return vv\n" +
   "    for sq in reversed(squares):\n" +
   "        for kk, vv in sq:\n" +
   "            if kk == k: return vv\n" +
   "    return None\n" +
   "for k, v in [(\"a\", 1), (\"b\", 2), (\"c\", 3)]:\n" +
   "    put(k, v)\n" +
   "print(\"live line:\", mem, \"| stacked squares:\", squares)\n" +
   "print(\"get a ->\", get(\"a\"), \"| get z ->\", get(\"z\"), \"(honest miss)\")\n" +
   "print(\"Compaction is the triangle merge of stacked squares.\")\n" +
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
var gen={version:'jahdb-embedded-storage-engines-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('embedded-storage-engines-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
