(function(){'use strict';
/* JAH The Document Nosql Signature Database generator — jahdb-document-nosql-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DOCNS-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "Signature MongoDB Engine",
  "Signature CouchDB Engine",
  "Signature PouchDB (sync) Engine",
  "Signature Couchbase Server Engine",
  "Signature RethinkDB Engine",
  "Signature RavenDB Engine",
  "Signature ArangoDB (document store) Engine",
  "Signature Amazon DocumentDB Engine",
  "Signature EJDB2 Engine",
  "Signature Ditto Engine",
  "Signature FerretDB Engine",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Signature __TOPIC__ Engine — geometric demo: documents as nested squares\n" +
   "SIG_ZERO = None\n" +
   "def square(doc, depth=0):\n" +
   "    pad = \"  \" * depth\n" +
   "    for k, v in doc.items():\n" +
   "        if isinstance(v, dict):\n" +
   "            print(pad + \"square[\" + k + \"]\")\n" +
   "            square(v, depth + 1)\n" +
   "        elif isinstance(v, list):\n" +
   "            print(pad + \"line[\" + k + \"] length\", len(v) if v else \"SIG_ZERO(empty)\")\n" +
   "        else:\n" +
   "            print(pad + \"field \" + k + \" =\", v if v is not None else \"SIG_ZERO\")\n" +
   "square({\"name\": \"ada\", \"addr\": {\"city\": \"austin\"}, \"tags\": []})\n" +
   "print(\"Fields are line segments from the document's Signature-One origin.\")\n" +
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
var gen={version:'jahdb-document-nosql-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('document-nosql-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
