(function(){'use strict';
/* JAH The Everything MI6 Database generator — jahdb-everything-mi6-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVMI6-";
var FIELDS=["Origins","History","Declassified","Legacy"];
var TOPICS={
 "Origins": [
  "The Founding of MI6 \u2014 Origins",
  "Mansfield Cumming, the First C \u2014 Origins",
  "Secret Service Origins (Signature Edition) \u2014 Origins"
 ],
 "History": [
  "SIS in the First World War \u2014 History",
  "SIS in the Second World War \u2014 History",
  "SIS and the Cambridge Spies \u2014 History"
 ],
 "Declassified": [
  "The Authorized History \u2014 Declassified",
  "Intelligence Historiography (Signature Edition) \u2014 Declassified",
  "The Authorized History Model (Signature Edition) \u2014 Declassified"
 ],
 "Legacy": [
  "Vauxhall Cross \u2014 Legacy",
  "Chiefs of the Secret Intelligence Service \u2014 Legacy",
  "Public Accountability (Signature Edition) \u2014 Legacy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Mi6 — "+safe+"\n"
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
    name:topic+' — mi6 history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mi6 history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-mi6-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-mi6',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
