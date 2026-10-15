(function(){'use strict';
/* JAH The Relational Sql Signature Database generator — jahdb-relational-sql-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RSQLS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature PostgreSQL Engine",
  "Signature MySQL Engine",
  "Signature MariaDB Engine",
  "Signature Amazon Aurora Engine",
  "Signature Azure SQL Database Engine",
  "Signature PlanetScale Engine",
  "Signature Neon Engine",
  "Signature Citus Engine",
  "Signature AlloyDB Engine",
  "Signature Percona Server for MySQL Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: rows counted from Signature-One\n" +
   "SIG_ZERO = None  # the placed null: declared empty, never an accident\n" +
   "table = []       # the square grid; each row a measured line\n" +
   "def insert(name, score):\n" +
   "    row_id = len(table) + 1          # Signature-One: counting starts at 1\n" +
   "    table.append({\"row\": row_id, \"name\": name, \"score\": score if score is not None else SIG_ZERO})\n" +
   "    return row_id\n" +
   "insert(\"ada\", 92); insert(\"bob\", 71); insert(\"cara\", SIG_ZERO)\n" +
   "print(\"rows (Signature-One addressed):\")\n" +
   "for r in table: print(\" row\", r[\"row\"], r[\"name\"], r[\"score\"])\n" +
   "# plus tool: join two grids where row-lines cross\n" +
   "other = [{\"row\": 1, \"dept\": \"eng\"}, {\"row\": 3, \"dept\": \"ops\"}]\n" +
   "for r in table:\n" +
   "    d = next((o[\"dept\"] for o in other if o[\"row\"] == r[\"row\"]), SIG_ZERO)\n" +
   "    print(\" join row\", r[\"row\"], \"->\", d)\n" +
   "print(\"Nulls are placed Signature-Zero; rows are never addressed from nothing.\")\n" +
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
var gen={version:'jahdb-relational-sql-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('relational-sql-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
