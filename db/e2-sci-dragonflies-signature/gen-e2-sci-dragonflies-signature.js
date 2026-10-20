(function(){'use strict';
/* JAH The Signature JAH Dragonflies Entomology Database generator — jahdb-e2-sci-dragonflies-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2SCIDRAGONS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature Approach to Dragonflies Entomology", "Signature Dragonflies Entomology Principles", "The Signature Dragonflies Entomology Starter System", "Signature Vocabulary for Dragonflies Entomology, Reimagined", "Signature Tools for Dragonflies Entomology, Reimagined", "Signature Safety Redesign for Dragonflies Entomology", "The Signature Learning Path for Dragonflies Entomology"], "Compounded": ["Signature Method I: Core Dragonflies Entomology Practice", "Signature Method II: Dragonflies Entomology Operations", "Signature Method III: Dragonflies Entomology Resources", "Signature Dragonflies Entomology Experience Design", "Signature Dragonflies Entomology Quality System", "Signature Dragonflies Entomology Troubleshooting Engine", "Signature Dragonflies Entomology Stewardship and Cost Philosophy"], "Advanced": ["Signature Method IV: Dragonflies Entomology Mastery", "Signature Method V: Teaching Dragonflies Entomology", "Signature Dragonflies Entomology Community Model", "Signature Dragonflies Entomology Future Concepts", "The Signature Dragonflies Entomology Master Plan", "Signature Dragonflies Entomology Compound Systems"]};
var KEYS={"The Signature Approach to Dragonflies Entomology": ["Signature-original: designed from first principles, not copied.", "First principles over inherited habit.", "Labeled Signature — never presented as public record.", "Real-world testing before any teaching."], "Signature Dragonflies Entomology Principles": ["Originality: new designs, not remixes.", "Honest labeling: Signature means Signature-made.", "Real-world testing before teaching.", "Respect for the public craft underneath."], "The Signature Dragonflies Entomology Starter System": ["One small Signature project first.", "Signature methods only during the learning stage.", "Document everything that works.", "Mastery of one method before adding the next."], "Signature Vocabulary for Dragonflies Entomology, Reimagined": ["Every term defined by what it does.", "Definitions must be testable in practice.", "Inherited jargon translated, not worshipped.", "One shared vocabulary for the whole archive."], "Signature Tools for Dragonflies Entomology, Reimagined": ["Every tool justified by its function.", "Simplest form that does the job wins.", "Build or adapt before you buy.", "Tools documented with their limits stated."], "Signature Safety Redesign for Dragonflies Entomology": ["Safety designed in, not hoped for.", "Every hazard named with its check.", "Stop conditions defined before starting.", "Incident reporting is mandatory and blameless."], "The Signature Learning Path for Dragonflies Entomology": ["Foundations before compounding.", "Exit criteria at every stage.", "Demonstrated skill gates progress.", "The whole path visible from day one."], "Signature Method I: Core Dragonflies Entomology Practice": ["One core routine, done the Signature way.", "Inputs, steps, checks, outputs — all specified.", "Repeatable by anyone who reads the record.", "The foundation every later method assumes."], "Signature Method II: Dragonflies Entomology Operations": ["Setup, maintenance, scheduling, teardown.", "The unglamorous work made systematic.", "Reliability is a design choice.", "Checklists beat memory every time."], "Signature Method III: Dragonflies Entomology Resources": ["Materials, references, time, attention.", "Know what each unit of work costs.", "Use less while doing more.", "Waste is a design flaw to be engineered out."], "Signature Dragonflies Entomology Experience Design": ["Pacing, clarity, feedback, delight.", "Designed from the user's point of view.", "Every friction point named and reduced.", "Respect for the user's time is the metric."], "Signature Dragonflies Entomology Quality System": ["Standards written down and measurable.", "Inspection points at every handoff.", "Correction loops, not blame loops.", "What gets measured gets made well."], "Signature Dragonflies Entomology Troubleshooting Engine": ["Symptom to cause to fix, in order.", "Tests at every branch of the tree.", "Diagnose first, repair second.", "Document every resolution for the next time."], "Signature Dragonflies Entomology Stewardship and Cost Philosophy": ["Spend where results multiply.", "Cut where spending adds nothing.", "Honest books, always.", "Sustainability is a feature."], "Signature Method IV: Dragonflies Entomology Mastery": ["Competence refined into artistry.", "Deliberate practice with expert feedback.", "Iteration as a permanent habit.", "Mastery is a system, not a gift."], "Signature Method V: Teaching Dragonflies Entomology": ["Explain, demonstrate, correct, assess.", "Simple explanations prove understanding.", "Students learn by doing, not watching.", "Assessment measures real skill."], "Signature Dragonflies Entomology Community Model": ["Practitioners gathered around shared standards.", "Results shared openly, reviewed honestly.", "Newcomers mentored, experts challenged.", "Community as learning infrastructure."], "Signature Dragonflies Entomology Future Concepts": ["Prototypes of the possible future.", "Speculation labeled as speculation.", "Every concept built to be tested.", "The future is designed, not awaited."], "The Signature Dragonflies Entomology Master Plan": ["All methods in one coherent sequence.", "Milestones, resources, quality gates.", "Ambition made executable.", "The plan is a living document."], "Signature Dragonflies Entomology Compound Systems": ["Simple methods linked into new capabilities.", "Interactions managed, not hoped away.", "The whole tested, not just the parts.", "Composition as a deliberate art."]};
var DEMOKIND="signature entomology simulator";
var RKIND="entomology";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var pysafe=safe.replace(/'/g,"\u2019");
  var ks=KEYS[topic]||["Study the topic.","Test it in practice.","Document what works.","Teach it to someone else."];
  var L=[];
  L.push("# "+DEMOKIND+" \u2014 "+safe);
  L.push("# Tier: "+String(field).replace(/\\/g,'\\\\').replace(/"/g,"'"));
  L.push("checklist = [");
  for(var i=0;i<ks.length;i++){ L.push('    "'+String(ks[i]).replace(/\\/g,'\\\\').replace(/"/g,'\\"')+'",'); }
  L.push("]");
  L.push("def run(items):");
  L.push("    print('CHECKLIST: "+pysafe+"')");
  L.push("    detail = 0");
  L.push("    for i, item in enumerate(items, 1):");
  L.push("        print(str(i) + '. ' + item)");
  L.push("        detail += len(item)");
  L.push("    print('items=' + str(len(items)) + ' detail_chars=' + str(detail))");
  L.push("    return len(items)");
  L.push("run(checklist)");
  return L.join("\n")+"\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 '+RKIND+' record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A '+RKIND+' record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+"JAH\-E2SCIDRAGONS\-"+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-e2-sci-dragonflies-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-sci-dragonflies-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
