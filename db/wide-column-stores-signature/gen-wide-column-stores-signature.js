(function(){'use strict';
/* JAH The Wide Column Stores Signature Database generator — jahdb-wide-column-stores-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WCOLS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature Apache Cassandra Engine",
  "Signature Apache HBase Engine",
  "Signature ScyllaDB Engine",
  "Signature Google Cloud Bigtable Engine",
  "Signature Azure Table Storage Engine",
  "Signature Amazon Keyspaces Engine",
  "Signature Apache Accumulo Engine",
  "Signature DataStax Astra DB Engine",
  "Signature Apache Phoenix Engine",
  "Signature Hypertable Engine",
  "Signature Apache Kudu Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: crossing lines, placed zeros\n" +
   "SIG_ZERO = None\n" +
   "grid = {}  # (row-line, column-line) -> value; missing = placed SIG_ZERO\n" +
   "def put(r, c, v): grid[(r, c)] = v\n" +
   "def get(r, c): return grid.get((r, c), SIG_ZERO)\n" +
   "put(\"r1\", \"info:name\", \"ada\"); put(\"r1\", \"stats:logins\", 42)\n" +
   "for r in [\"r1\", \"r2\"]:\n" +
   "    for c in [\"info:name\", \"stats:logins\"]:\n" +
   "        print(\"crossing\", r, \"x\", c, \"->\", get(r, c))\n" +
   "print(\"Sparse cells are placed Signature-Zero: declared, never garbage.\")\n" +
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
var gen={version:'jahdb-wide-column-stores-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wide-column-stores-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
