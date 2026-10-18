(function(){'use strict';
/* JAH The Computer Power Comparison Signature Database generator — jahdb-db-computer-power-comparison-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPCS-";
var FIELDS=["Everyday Computing","Gaming & Graphics","Supercomputing"];
var TOPICS={
 "Everyday Computing": [
  "Phone vs Laptop: Daily Power (Signature Edition) - Everyday Computing",
  "Tablet vs Laptop: Portable Work (Signature Edition) - Everyday Computing",
  "Desktop vs Laptop: Power (Signature Edition) - Everyday Computing",
  "Chromebook vs Laptop: Simple (Signature Edition) - Everyday Computing",
  "Mac vs PC: Platforms (Signature Edition) - Everyday Computing",
  "Raspberry Pi vs Desktop: Tiny (Signature Edition) - Everyday Computing",
  "Smartwatch vs Phone: Wrist (Signature Edition) - Everyday Computing",
  "E-Reader vs Tablet: Computing Power (Signature Edition) - Everyday Computing",
  "Calculator vs Phone: Math (Signature Edition) - Everyday Computing",
  "Server vs Desktop: Always-On (Signature Edition) - Everyday Computing",
  "Thin Client vs PC: Office (Signature Edition) - Everyday Computing",
  "Smart TV vs Monitor: Big Screen (Signature Edition) - Everyday Computing"
 ],
 "Gaming & Graphics": [
  "PS5 vs Xbox: Consoles (Signature Edition) - Gaming & Graphics",
  "Console vs PC: Gaming (Signature Edition) - Gaming & Graphics",
  "GPU: NVIDIA vs AMD (Signature Edition) - Gaming & Graphics",
  "CPU: Intel vs AMD (Signature Edition) - Gaming & Graphics",
  "Integrated vs Dedicated GPU (Signature Edition) - Gaming & Graphics",
  "SSD vs HDD: Storage (Signature Edition) - Gaming & Graphics",
  "RAM: More vs Faster (Signature Edition) - Gaming & Graphics",
  "Monitor: 4K vs 144Hz (Signature Edition) - Gaming & Graphics",
  "VR Headset vs Monitor: Immersion (Signature Edition) - Gaming & Graphics",
  "Cloud Gaming vs Local: Play (Signature Edition) - Gaming & Graphics"
 ],
 "Supercomputing": [
  "Supercomputer vs Quantum: Peak (Signature Edition) - Supercomputing",
  "CPU vs GPU: Compute (Signature Edition) - Supercomputing",
  "On-Prem vs Cloud: HPC (Signature Edition) - Supercomputing",
  "Then vs Now: 1990 vs 2025 (Signature Edition) - Supercomputing",
  "Analog vs Digital: Compute (Signature Edition) - Supercomputing",
  "Mainframe vs Cloud: Enterprise (Signature Edition) - Supercomputing",
  "Edge vs Cloud: Where Compute (Signature Edition) - Supercomputing",
  "Open vs Closed: Supercomputing (Signature Edition) - Supercomputing",
  "Wetware vs Hardware: Future (Signature Edition) - Supercomputing",
  "Abacus vs Phone: Full Circle (Signature Edition) - Supercomputing",
  "ENIAC vs Watch: Origin vs Now (Signature Edition) - Supercomputing",
  "Data Center vs Basement: Hosting (Signature Edition) - Supercomputing"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Computer Power Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — computing comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A computing comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"computer-power-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-computer-power-comparison-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-computer-power-comparison-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
