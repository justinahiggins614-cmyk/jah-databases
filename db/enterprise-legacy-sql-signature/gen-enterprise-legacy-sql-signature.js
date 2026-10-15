(function(){'use strict';
/* JAH The Enterprise Legacy Sql Signature Database generator — jahdb-enterprise-legacy-sql-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LEGSS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature Oracle Database Engine",
  "Signature Microsoft SQL Server Engine",
  "Signature IBM Db2 Engine",
  "Signature Teradata Engine",
  "Signature Informix Engine",
  "Signature SAP HANA Engine",
  "Signature SAP ASE Engine",
  "Signature Vertica Engine",
  "Signature Greenplum Engine",
  "Signature Firebird Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: the blueprint square\n" +
   "SIG_ZERO = None\n" +
   "schema = {\"accounts\": {\"squares\": [\"id\", \"balance\"], \"lines\": [\"id unique\", \"balance >= SIG_ZERO\"]}}\n" +
   "def check(table, row):\n" +
   "    for rule in schema[table][\"lines\"]:\n" +
   "        if \"balance >=\" in rule and row.get(\"balance\", SIG_ZERO) is SIG_ZERO:\n" +
   "            return \"REJECTED: null balance violates the measured line\"\n" +
   "    return \"ACCEPTED\"\n" +
   "print(check(\"accounts\", {\"id\": 1, \"balance\": 100}))\n" +
   "print(check(\"accounts\", {\"id\": 2, \"balance\": SIG_ZERO}))\n" +
   "print(\"Constraints are lines that must not break; transactions are atomic plus-crossings.\")\n" +
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
var gen={version:'jahdb-enterprise-legacy-sql-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('enterprise-legacy-sql-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
