(function(){'use strict';
/* JAH The DNA Data Storage Future Technology Database generator — jahdb-futuretech-84-dna-data-storage-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT84-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1953: the Double Helix - Foundations",
  "1959: Plenty of Room - Foundations",
  "1970s: Recombinant DNA - Foundations",
  "1988: Microvenus - Foundations",
  "1999: DNA Microdots - Foundations",
  "2001: the Human Genome - Foundations",
  "2007: DNA to Order - Foundations",
  "2012: a Book in DNA - Foundations",
  "2013: Sonnets in DNA - Foundations",
  "2015: Microsoft Bets on DNA - Foundations",
  "2016: 200MB in DNA - Foundations"
 ],
 "Compounded": [
  "2017: DNA Fountain - Compounded",
  "2018: Random Access - Compounded",
  "2019: Automated DNA Storage - Compounded",
  "2020: Catalog - Compounded",
  "2021: DNA Advances - Compounded",
  "2022: Twist Scales - Compounded",
  "2023: Density Records - Compounded",
  "2024: Commercial Pilots - Compounded",
  "2025: the Molecular Wave - Compounded",
  "2025: DNA Storage Costs Fall - Compounded",
  "The DNA Archive - Compounded",
  "Exabyte DNA - Compounded"
 ],
 "Advanced": [
  "The Molecular Library - Advanced",
  "DNA in Data Centers - Advanced",
  "The Eternal Archive - Advanced",
  "Write Speed Solved - Advanced",
  "The Living Hard Drive - Advanced",
  "The Genomic Cloud - Advanced",
  "The DNA Internet - Advanced",
  "The Molecular Civilization - Advanced",
  "Immortal Data - Advanced",
  "The DNA Data Center - Advanced",
  "Everyday DNA Storage - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — DNA data storage record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A DNA data storage record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-84-dna-data-storage-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-84-dna-data-storage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-84-dna-data-storage',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
