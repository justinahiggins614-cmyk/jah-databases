(function(){'use strict';
/* JAH The Mystery Definition Database Database generator — jahdb-db-mystery-definition-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MYSDEF-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Mystery word #1 (5 letters): _____",
  "Mystery word #2 (3 letters): ___",
  "Mystery word #3 (3 letters): ___",
  "Mystery word #4 (4 letters): ____",
  "Mystery word #5 (5 letters): _____",
  "Mystery word #6 (4 letters): ____",
  "Mystery word #7 (5 letters): _____",
  "Mystery word #8 (4 letters): ____",
  "Mystery word #9 (4 letters): ____",
  "Mystery word #10 (4 letters): ____",
  "Mystery word #11 (5 letters): _____"
 ],
 "Compounded": [
  "Mystery word #12 (9 letters): _________",
  "Mystery word #13 (7 letters): _______",
  "Mystery word #14 (7 letters): _______",
  "Mystery word #15 (10 letters): __________",
  "Mystery word #16 (12 letters): ____________",
  "Mystery word #17 (9 letters): _________",
  "Mystery word #18 (10 letters): __________",
  "Mystery word #19 (9 letters): _________",
  "Mystery word #20 (10 letters): __________",
  "Mystery word #21 (8 letters): ________",
  "Mystery word #22 (7 letters): _______",
  "Mystery word #23 (7 letters): _______"
 ],
 "Advanced": [
  "Mystery word #24 (11 letters): ___________",
  "Mystery word #25 (9 letters): _________",
  "Mystery word #26 (14 letters): ______________",
  "Mystery word #27 (14 letters): ______________",
  "Mystery word #28 (9 letters): _________",
  "Mystery word #29 (8 letters): ________",
  "Mystery word #30 (6 letters): ______",
  "Mystery word #31 (11 letters): ___________",
  "Mystery word #32 (9 letters): _________",
  "Mystery word #33 (6 letters): ______",
  "Mystery word #34 (9 letters): _________"
 ]
};
var DEMOKIND="definition-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mystery Definition Study — "+safe+"\n"
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
    name:topic+' — mystery definition record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mystery definition record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-mystery-definition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mystery-definition',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
