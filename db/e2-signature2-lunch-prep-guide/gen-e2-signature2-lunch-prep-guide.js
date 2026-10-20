(function(){'use strict';
/* JAH The JAH Lunch Prep Guide Database generator - e2-signature2-lunch-prep-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2LPG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["What Lunch Prep Guide Is and Why It Matters", "Getting Started: Your First Five Moves in Lunch Prep Guide", "The Core Method for Lunch Prep Guide, Step by Step", "The Numbers That Matter in Lunch Prep Guide", "Your First 30 Days of Lunch Prep Guide", "Essential Tools and Supplies for Lunch Prep Guide", "Common Lunch Prep Guide Mistakes and How to Avoid Them", "Lunch Prep Guide Beginner FAQ", "The Lunch Prep Guide Intermediate Playbook", "Lunch Prep Guide Money Math: A Worked Example", "Lunch Prep Guide Checklists You Can Reuse", "Lunch Prep Guide: Safety, Legal, and Fine Print", "When Lunch Prep Guide Goes Wrong: Troubleshooting", "Doing Lunch Prep Guide With Others: Family and Team Edition", "The Annual Rhythm of Lunch Prep Guide", "Advanced Lunch Prep Guide Techniques", "Teaching Lunch Prep Guide to Someone Else", "Measuring Success in Lunch Prep Guide", "Complete Walkthrough: Lunch Prep Guide in the Real World", "Lunch Prep Guide Master Checklist and Next Steps"];
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
var gen={version:'e2-signature2-lunch-prep-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-signature2-lunch-prep-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
