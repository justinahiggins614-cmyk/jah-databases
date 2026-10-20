(function(){'use strict';
/* JAH The JAH New Puppy Guide Database generator - e2-signature2-new-puppy-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2NPG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["What New Puppy Guide Is and Why It Matters", "Getting Started: Your First Five Moves in New Puppy Guide", "The Core Method for New Puppy Guide, Step by Step", "The Numbers That Matter in New Puppy Guide", "Your First 30 Days of New Puppy Guide", "Essential Tools and Supplies for New Puppy Guide", "Common New Puppy Guide Mistakes and How to Avoid Them", "New Puppy Guide Beginner FAQ", "The New Puppy Guide Intermediate Playbook", "New Puppy Guide Money Math: A Worked Example", "New Puppy Guide Checklists You Can Reuse", "New Puppy Guide: Safety, Legal, and Fine Print", "When New Puppy Guide Goes Wrong: Troubleshooting", "Doing New Puppy Guide With Others: Family and Team Edition", "The Annual Rhythm of New Puppy Guide", "Advanced New Puppy Guide Techniques", "Teaching New Puppy Guide to Someone Else", "Measuring Success in New Puppy Guide", "Complete Walkthrough: New Puppy Guide in the Real World", "New Puppy Guide Master Checklist and Next Steps"];
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
var gen={version:'e2-signature2-new-puppy-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-signature2-new-puppy-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
