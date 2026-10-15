(function(){'use strict';
/* JAH The Document Nosql Database generator — jahdb-document-nosql-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DOCN-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "MongoDB",
  "CouchDB",
  "PouchDB (sync)",
  "Couchbase Server",
  "RethinkDB",
  "RavenDB",
  "ArangoDB (document store)",
  "Amazon DocumentDB",
  "EJDB2",
  "Ditto",
  "FerretDB",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# __TOPIC__ — concept demo: JSON documents + dot-path query (simulation)\n" +
   "docs = [\n" +
   "    {\"_id\": 1, \"name\": \"ada\", \"addr\": {\"city\": \"austin\", \"zip\": \"78701\"}, \"tags\": [\"admin\", \"dev\"]},\n" +
   "    {\"_id\": 2, \"name\": \"bob\", \"addr\": {\"city\": \"boston\", \"zip\": \"02101\"}, \"tags\": [\"dev\"]},\n" +
   "]\n" +
   "def get(doc, path):\n" +
   "    cur = doc\n" +
   "    for part in path.split(\".\"):\n" +
   "        cur = cur.get(part) if isinstance(cur, dict) else None\n" +
   "    return cur\n" +
   "for d in docs:\n" +
   "    if get(d, \"addr.city\") == \"austin\": print(\"match:\", d[\"name\"], d[\"addr\"])\n" +
   "print(\"Concept demonstration of __TOPIC__'s document model (simulation).\")\n" +
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
var gen={version:'jahdb-document-nosql-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('document-nosql',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
