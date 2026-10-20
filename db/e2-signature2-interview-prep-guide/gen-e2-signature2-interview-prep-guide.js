(function(){'use strict';
/* JAH The JAH Interview Prep Guide Database generator - e2-signature2-interview-prep-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2IPG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["What Interview Prep Guide Is and Why It Matters", "Getting Started: Your First Five Moves in Interview Prep Guide", "The Core Method for Interview Prep Guide, Step by Step", "The Numbers That Matter in Interview Prep Guide", "Your First 30 Days of Interview Prep Guide", "Essential Tools and Supplies for Interview Prep Guide", "Common Interview Prep Guide Mistakes and How to Avoid Them", "Interview Prep Guide Beginner FAQ", "The Interview Prep Guide Intermediate Playbook", "Interview Prep Guide Money Math: A Worked Example", "Interview Prep Guide Checklists You Can Reuse", "Interview Prep Guide: Safety, Legal, and Fine Print", "When Interview Prep Guide Goes Wrong: Troubleshooting", "Doing Interview Prep Guide With Others: Family and Team Edition", "The Annual Rhythm of Interview Prep Guide", "Advanced Interview Prep Guide Techniques", "Teaching Interview Prep Guide to Someone Else", "Measuring Success in Interview Prep Guide", "Complete Walkthrough: Interview Prep Guide in the Real World", "Interview Prep Guide Master Checklist and Next Steps"];
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
var gen={version:'e2-signature2-interview-prep-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-signature2-interview-prep-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
