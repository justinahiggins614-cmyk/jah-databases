(function(){'use strict';
/* JAH The School Blueprint Database generator — jahdb-blueprint-schools-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BSCH-";
var FIELDS=["Classroom Buildings","Specialty Facilities","Support"];
var TOPICS={
 "Classroom Buildings": [
  "One-Room Schoolhouse - Compact Architectural Blueprint - Classroom Buildings",
  "Elementary School - Compact Architectural Blueprint - Classroom Buildings",
  "Middle School - Compact Architectural Blueprint - Classroom Buildings",
  "High School - Compact Architectural Blueprint - Classroom Buildings",
  "One-Room Schoolhouse - Standard Architectural Blueprint - Classroom Buildings",
  "Elementary School - Standard Architectural Blueprint - Classroom Buildings",
  "Middle School - Standard Architectural Blueprint - Classroom Buildings",
  "High School - Standard Architectural Blueprint - Classroom Buildings",
  "One-Room Schoolhouse - Grand Architectural Blueprint - Classroom Buildings",
  "Elementary School - Grand Architectural Blueprint - Classroom Buildings",
  "Middle School - Grand Architectural Blueprint - Classroom Buildings",
  "High School - Grand Architectural Blueprint - Classroom Buildings"
 ],
 "Specialty Facilities": [
  "Science Wing - Compact Architectural Blueprint - Specialty Facilities",
  "Gymnasium - Compact Architectural Blueprint - Specialty Facilities",
  "Library Media Center - Compact Architectural Blueprint - Specialty Facilities",
  "Vocational Workshop - Compact Architectural Blueprint - Specialty Facilities",
  "Art School Studio - Compact Architectural Blueprint - Specialty Facilities",
  "Auditorium Building - Compact Architectural Blueprint - Specialty Facilities",
  "Science Wing - Standard Architectural Blueprint - Specialty Facilities",
  "Gymnasium - Standard Architectural Blueprint - Specialty Facilities",
  "Library Media Center - Standard Architectural Blueprint - Specialty Facilities",
  "Vocational Workshop - Standard Architectural Blueprint - Specialty Facilities",
  "Art School Studio - Standard Architectural Blueprint - Specialty Facilities",
  "Auditorium Building - Standard Architectural Blueprint - Specialty Facilities",
  "Science Wing - Grand Architectural Blueprint - Specialty Facilities",
  "Gymnasium - Grand Architectural Blueprint - Specialty Facilities",
  "Library Media Center - Grand Architectural Blueprint - Specialty Facilities",
  "Vocational Workshop - Grand Architectural Blueprint - Specialty Facilities",
  "Art School Studio - Grand Architectural Blueprint - Specialty Facilities"
 ],
 "Support": [
  "Cafeteria Hall - Compact Architectural Blueprint - Support",
  "Administration Building - Compact Architectural Blueprint - Support",
  "Cafeteria Hall - Standard Architectural Blueprint - Support",
  "Administration Building - Standard Architectural Blueprint - Support",
  "Cafeteria Hall - Grand Architectural Blueprint - Support"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Schools Blueprint Study — "+safe+"\n"
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
    name:topic+' — school blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A school blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-schools-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-schools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
