(function(){'use strict';
/* JAH The JAH Side Hustle Guide Database generator - e2-signature2-side-hustle-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2SHG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["What Side Hustle Guide Is and Why It Matters", "Getting Started: Your First Five Moves in Side Hustle Guide", "The Core Method for Side Hustle Guide, Step by Step", "The Numbers That Matter in Side Hustle Guide", "Your First 30 Days of Side Hustle Guide", "Essential Tools and Supplies for Side Hustle Guide", "Common Side Hustle Guide Mistakes and How to Avoid Them", "Side Hustle Guide Beginner FAQ", "The Side Hustle Guide Intermediate Playbook", "Side Hustle Guide Money Math: A Worked Example", "Side Hustle Guide Checklists You Can Reuse", "Side Hustle Guide: Safety, Legal, and Fine Print", "When Side Hustle Guide Goes Wrong: Troubleshooting", "Doing Side Hustle Guide With Others: Family and Team Edition", "The Annual Rhythm of Side Hustle Guide", "Advanced Side Hustle Guide Techniques", "Teaching Side Hustle Guide to Someone Else", "Measuring Success in Side Hustle Guide", "Complete Walkthrough: Side Hustle Guide in the Real World", "Side Hustle Guide Master Checklist and Next Steps"];
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
var gen={version:'e2-signature2-side-hustle-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-signature2-side-hustle-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
