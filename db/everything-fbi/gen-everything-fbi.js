(function(){'use strict';
/* JAH The Everything FBI Database generator — jahdb-everything-fbi-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVFBI-";
var FIELDS=["Origins","History","Investigations","Oversight"];
var TOPICS={
 "Origins": [
  "The Founding of the FBI \u2014 Origins",
  "Public Records Research (Signature Edition) \u2014 Origins"
 ],
 "History": [
  "The Hoover Era \u2014 History",
  "COINTELPRO \u2014 History",
  "The FBI and the Civil Rights Era \u2014 History"
 ],
 "Investigations": [
  "The FBI Laboratory \u2014 Investigations",
  "The Ten Most Wanted List \u2014 Investigations",
  "The Post-9/11 Reorganization \u2014 Investigations",
  "Investigative History (Signature Edition) \u2014 Investigations",
  "Forensic Science Development (Signature Edition) \u2014 Investigations"
 ],
 "Oversight": [
  "Directors of the FBI \u2014 Oversight",
  "Law Enforcement Oversight (Signature Edition) \u2014 Oversight"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Fbi — "+safe+"\n"
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
    name:topic+' — fbi history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fbi history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-fbi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-fbi',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
