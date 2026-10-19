(function(){'use strict';
/* JAH The DNA Data Storage Future Technology Database — Signature Edition generator — jahdb-futuretech-84-dna-data-storage-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT84-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["DNA Data Storage — the Double Helix (Signature Edition)", "DNA Data Storage — Plenty of Room (Signature Edition)", "DNA Data Storage — Recombinant DNA (Signature Edition)", "DNA Data Storage — Microvenus (Signature Edition)", "DNA Data Storage — DNA Microdots (Signature Edition)", "DNA Data Storage — the Human Genome (Signature Edition)", "DNA Data Storage — DNA to Order (Signature Edition)", "DNA Data Storage — a Book in DNA (Signature Edition)", "DNA Data Storage — Sonnets in DNA (Signature Edition)", "DNA Data Storage — Microsoft Bets on DNA (Signature Edition)", "DNA Data Storage — 200MB in DNA (Signature Edition)"], "Compounded": ["DNA Data Storage — DNA Fountain (Signature Edition)", "DNA Data Storage — Random Access (Signature Edition)", "DNA Data Storage — Automated DNA Storage (Signature Edition)", "DNA Data Storage — Catalog (Signature Edition)", "DNA Data Storage — DNA Advances (Signature Edition)", "DNA Data Storage — Twist Scales (Signature Edition)", "DNA Data Storage — Density Records (Signature Edition)", "DNA Data Storage — Commercial Pilots (Signature Edition)", "DNA Data Storage — the Molecular Wave (Signature Edition)", "DNA Data Storage — DNA Storage Costs Fall (Signature Edition)", "DNA Data Storage — The DNA Archive (Signature Edition)", "DNA Data Storage — Exabyte DNA (Signature Edition)"], "Advanced": ["DNA Data Storage — The Molecular Library (Signature Edition)", "DNA Data Storage — DNA in Data Centers (Signature Edition)", "DNA Data Storage — The Eternal Archive (Signature Edition)", "DNA Data Storage — Write Speed Solved (Signature Edition)", "DNA Data Storage — The Living Hard Drive (Signature Edition)", "DNA Data Storage — The Genomic Cloud (Signature Edition)", "DNA Data Storage — The DNA Internet (Signature Edition)", "DNA Data Storage — The Molecular Civilization (Signature Edition)", "DNA Data Storage — Immortal Data (Signature Edition)", "DNA Data Storage — The DNA Data Center (Signature Edition)", "DNA Data Storage — Everyday DNA Storage - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# DNA Data Storage study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-84-dna-data-storage-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-84-dna-data-storage-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
