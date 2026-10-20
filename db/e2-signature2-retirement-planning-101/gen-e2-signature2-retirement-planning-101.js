(function(){'use strict';
/* JAH The JAH Retirement Planning 101 Database generator - e2-signature2-retirement-planning-101-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2RP1-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["What Retirement Planning 101 Is and Why It Matters", "Getting Started: Your First Five Moves in Retirement Planning 101", "The Core Method for Retirement Planning 101, Step by Step", "The Numbers That Matter in Retirement Planning 101", "Your First 30 Days of Retirement Planning 101", "Essential Tools and Supplies for Retirement Planning 101", "Common Retirement Planning 101 Mistakes and How to Avoid Them", "Retirement Planning 101 Beginner FAQ", "The Retirement Planning 101 Intermediate Playbook", "Retirement Planning 101 Money Math: A Worked Example", "Retirement Planning 101 Checklists You Can Reuse", "Retirement Planning 101: Safety, Legal, and Fine Print", "When Retirement Planning 101 Goes Wrong: Troubleshooting", "Doing Retirement Planning 101 With Others: Family and Team Edition", "The Annual Rhythm of Retirement Planning 101", "Advanced Retirement Planning 101 Techniques", "Teaching Retirement Planning 101 to Someone Else", "Measuring Success in Retirement Planning 101", "Complete Walkthrough: Retirement Planning 101 in the Real World", "Retirement Planning 101 Master Checklist and Next Steps"];
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+"\n# Field: "+field+"\nrecord={'title': \""+safe+"\", 'field': \""+field+"\"}\nprint('Record: '+record['title']+' ['+record['field']+']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var topic=pick(TOPICS,rnd);
  return {id:PREFIX+String(seed).padStart(6,'0'),title:topic,field:field,src:'public-harvest',
    summary:'Generated record for '+topic+'.',demo:{language:'python',program:demoProgram(topic,field)},_seed:seed};
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
var gen={version:'e2-signature2-retirement-planning-101-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-signature2-retirement-planning-101',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
