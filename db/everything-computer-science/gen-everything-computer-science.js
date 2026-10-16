(function(){'use strict';
/* JAH The Everything Computer Science Database generator — jahdb-everything-computer-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVCS-";
var FIELDS=["Foundations","Algorithms","Theory","Systems","Security","Signature Computer Science"];
var TOPICS={
 "Foundations": [
  "Data Structures: Arrays, Linked Lists, Trees, Graphs \u2014 Foundations",
  "Programming Languages: Paradigms and Types \u2014 Foundations"
 ],
 "Algorithms": [
  "Algorithms: Sorting and Searching \u2014 Algorithms"
 ],
 "Theory": [
  "Computational Complexity: Big-O Notation \u2014 Theory"
 ],
 "Systems": [
  "Operating Systems: Processes, Memory, Files \u2014 Systems",
  "Computer Networks: Packets and Protocols \u2014 Systems",
  "Databases: The Relational Model and SQL \u2014 Systems"
 ],
 "Security": [
  "Cryptography: Keys, Hashes, and Public-Key Systems \u2014 Security"
 ],
 "Signature Computer Science": [
  "Signature Deterministic Computation Engine (Signature Edition) \u2014 Signature Computer Science",
  "Signature Data Geometry (Signature Edition) \u2014 Signature Computer Science",
  "Signature Algorithm Workability Proofs (Signature Edition) \u2014 Signature Computer Science",
  "Signature Secure Channel Constructor (Signature Edition) \u2014 Signature Computer Science"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Computer Science — "+safe+"\n"
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
    name:topic+' — computer science record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A computer science record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-computer-science-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-computer-science',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
