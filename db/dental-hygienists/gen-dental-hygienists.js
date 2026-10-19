(function(){'use strict';
/* JAH The Dental Hygienists Database generator — jahdb-dental-hygienists-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEHY-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Dental Hygienists Do", "A Day in the Life of a Hygienist", "Training and Education Path", "Licensing and Certification", "Core Tools of the Trade", "Safety and Infection Control", "Key Terms and Jargon"], "Compounded": ["Ultrasonic Scaling Technique", "Hand Scaling With Curettes", "Patient Education That Sticks", "Radiographic Technique", "Documentation and Clinical Notes", "Ethics and Professional Conduct", "Working With the Dental Team"], "Advanced": ["Troubleshooting Difficult Cases", "Regulations and Scope of Practice", "History and Pioneers", "Technology and the Future", "Teaching, Mentoring, and Leadership", "Career Ladder and Advancement"]};
var DEMOKIND="hygiene care planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# hygiene care planner — "+safe+"\n"
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
    name:topic+' — dental hygienist profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A dental hygienist profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-dental-hygienists-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dental-hygienists',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
