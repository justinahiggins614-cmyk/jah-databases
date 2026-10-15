(function(){'use strict';
/* JAH The Wide Column Stores Database generator — jahdb-wide-column-stores-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WCOL-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Apache Cassandra",
  "Apache HBase",
  "ScyllaDB",
  "Google Cloud Bigtable",
  "Azure Table Storage",
  "Amazon Keyspaces",
  "Apache Accumulo",
  "DataStax Astra DB",
  "Apache Phoenix",
  "Hypertable",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# __TOPIC__ — concept demo: column families, sparse rows (simulation)\n" +
   "rows = {}\n" +
   "def put(row, cf, col, val):\n" +
   "    rows.setdefault(row, {}).setdefault(cf, {})[col] = val\n" +
   "put(\"user:1\", \"info\", \"name\", \"ada\"); put(\"user:1\", \"info\", \"email\", \"a@x.io\")\n" +
   "put(\"user:1\", \"stats\", \"logins\", 42); put(\"user:2\", \"info\", \"name\", \"bob\")\n" +
   "for r, cfs in rows.items():\n" +
   "    print(r, {cf: sorted(cols) for cf, cols in cfs.items()})\n" +
   "print(\"user:2 has no stats column-family: sparsity is free.\")\n" +
   "print(\"Concept demonstration of __TOPIC__'s wide-column model (simulation).\")\n" +
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
var gen={version:'jahdb-wide-column-stores-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wide-column-stores',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
