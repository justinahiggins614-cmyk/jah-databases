(function(){'use strict';
/* JAH The Enterprise Legacy Sql Database generator — jahdb-enterprise-legacy-sql-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LEGS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Oracle Database",
  "Microsoft SQL Server",
  "IBM Db2",
  "Teradata",
  "Informix",
  "SAP HANA",
  "SAP ASE",
  "Vertica",
  "Greenplum",
  "Firebird",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# __TOPIC__ — concept demo: ACID transaction (simulation)\n" +
   "db, wal = {\"balance\": 100}, []\n" +
   "def txn(ops, commit=True):\n" +
   "    before = dict(db)\n" +
   "    try:\n" +
   "        for op in ops: wal.append(op); op()\n" +
   "        if not commit: raise RuntimeError(\"rollback requested\")\n" +
   "        wal.clear(); return \"COMMITTED\"\n" +
   "    except RuntimeError:\n" +
   "        db.clear(); db.update(before); return \"ROLLED BACK\"\n" +
   "print(txn([lambda: db.update(balance=db[\"balance\"] - 30)], commit=True), db)\n" +
   "print(txn([lambda: db.update(balance=db[\"balance\"] - 90)], commit=False), db)\n" +
   "print(\"Concept demonstration of __TOPIC__'s transactional guarantees (simulation).\")\n" +
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
var gen={version:'jahdb-enterprise-legacy-sql-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('enterprise-legacy-sql',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
