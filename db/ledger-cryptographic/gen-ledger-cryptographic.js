(function(){'use strict';
/* JAH The Ledger Cryptographic Database generator — jahdb-ledger-cryptographic-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LEDG-";
var FIELDS=["engine records"];
var TOPICS={
 "engine records": [
  "immudb",
  "Amazon QLDB",
  "BigchainDB",
  "Hyperledger Fabric",
  "R3 Corda",
  "Fluree",
  "ProvenDB",
  "Postchain",
  "Amazon Managed Blockchain",
  "Dolt",
  "Trinsic",
  "Hyperledger Indy",
  "Verifiable Data Registry (VDR)",
  "SpacetimeDB",
  "Apache BookKeeper",
  "Ceramic Network",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# __TOPIC__ — concept demo: hash-chained log (simulation)\n" +
   "import hashlib\n" +
   "log = []\n" +
   "def append(data):\n" +
   "    prev = log[-1][\"hash\"] if log else \"GENESIS\"\n" +
   "    h = hashlib.sha256((prev + data).encode()).hexdigest()\n" +
   "    log.append({\"data\": data, \"hash\": h})\n" +
   "def verify():\n" +
   "    for i, e in enumerate(log):\n" +
   "        prev = log[i - 1][\"hash\"] if i else \"GENESIS\"\n" +
   "        if hashlib.sha256((prev + e[\"data\"]).encode()).hexdigest() != e[\"hash\"]:\n" +
   "            return False\n" +
   "    return True\n" +
   "append(\"tx1: ada pays bob 5\"); append(\"tx2: bob pays cara 2\")\n" +
   "print(\"verify:\", verify())\n" +
   "log[0][\"data\"] = \"tampered\"\n" +
   "print(\"after tamper, verify:\", verify())\n" +
   "print(\"Concept demonstration of __TOPIC__'s tamper-evidence (simulation).\")\n" +
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
var gen={version:'jahdb-ledger-cryptographic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ledger-cryptographic',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
