(function(){'use strict';
/* JAH The Everything CIA Database generator — jahdb-everything-cia-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVCIA-";
var FIELDS=["Origins","Cold War","Oversight","Declassified History"];
var TOPICS={
 "Origins": [
  "The Founding of the CIA \u2014 Origins",
  "The Office of Strategic Services \u2014 Origins"
 ],
 "Cold War": [
  "The U-2 Program \u2014 Cold War",
  "The Bay of Pigs \u2014 Cold War",
  "The CIA in the Cold War \u2014 Cold War",
  "Cold War Case Studies (Signature Edition) \u2014 Cold War"
 ],
 "Oversight": [
  "The Church Committee \u2014 Oversight",
  "Directors of Central Intelligence \u2014 Oversight",
  "Oversight Frameworks (Signature Edition) \u2014 Oversight"
 ],
 "Declassified History": [
  "Declassified Archives and CREST \u2014 Declassified History",
  "Intelligence History Method (Signature Edition) \u2014 Declassified History",
  "Declassification Studies (Signature Edition) \u2014 Declassified History"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Cia — "+safe+"\n"
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
    name:topic+' — cia history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cia history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-cia-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-cia',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
