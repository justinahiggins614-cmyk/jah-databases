(function(){'use strict';
/* JAH The Signature JAH Polar Oceans Oceanography Database generator — jahdb-e2-sci-polar-oceans-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-E2SCIPOLAROS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature Approach to Polar Oceans Oceanography", "Signature Polar Oceans Oceanography Principles", "The Signature Polar Oceans Oceanography Starter System", "Signature Vocabulary for Polar Oceans Oceanography, Reimagined", "Signature Tools for Polar Oceans Oceanography, Reimagined", "Signature Safety Redesign for Polar Oceans Oceanography", "The Signature Learning Path for Polar Oceans Oceanography"], "Compounded": ["Signature Method I: Core Polar Oceans Oceanography Practice", "Signature Method II: Polar Oceans Oceanography Operations", "Signature Method III: Polar Oceans Oceanography Resources", "Signature Polar Oceans Oceanography Experience Design", "Signature Polar Oceans Oceanography Quality System", "Signature Polar Oceans Oceanography Troubleshooting Engine", "Signature Polar Oceans Oceanography Stewardship and Cost Philosophy"], "Advanced": ["Signature Method IV: Polar Oceans Oceanography Mastery", "Signature Method V: Teaching Polar Oceans Oceanography", "Signature Polar Oceans Oceanography Community Model", "Signature Polar Oceans Oceanography Future Concepts", "The Signature Polar Oceans Oceanography Master Plan", "Signature Polar Oceans Oceanography Compound Systems"]};
var KEYS={"The Signature Approach to Polar Oceans Oceanography": ["Signature-original: designed from first principles, not copied.", "First principles over inherited habit.", "Labeled Signature — never presented as public record.", "Real-world testing before any teaching."], "Signature Polar Oceans Oceanography Principles": ["Originality: new designs, not remixes.", "Honest labeling: Signature means Signature-made.", "Real-world testing before teaching.", "Respect for the public craft underneath."], "The Signature Polar Oceans Oceanography Starter System": ["One small Signature project first.", "Signature methods only during the learning stage.", "Document everything that works.", "Mastery of one method before adding the next."], "Signature Vocabulary for Polar Oceans Oceanography, Reimagined": ["Every term defined by what it does.", "Definitions must be testable in practice.", "Inherited jargon translated, not worshipped.", "One shared vocabulary for the whole archive."], "Signature Tools for Polar Oceans Oceanography, Reimagined": ["Every tool justified by its function.", "Simplest form that does the job wins.", "Build or adapt before you buy.", "Tools documented with their limits stated."], "Signature Safety Redesign for Polar Oceans Oceanography": ["Safety designed in, not hoped for.", "Every hazard named with its check.", "Stop conditions defined before starting.", "Incident reporting is mandatory and blameless."], "The Signature Learning Path for Polar Oceans Oceanography": ["Foundations before compounding.", "Exit criteria at every stage.", "Demonstrated skill gates progress.", "The whole path visible from day one."], "Signature Method I: Core Polar Oceans Oceanography Practice": ["One core routine, done the Signature way.", "Inputs, steps, checks, outputs — all specified.", "Repeatable by anyone who reads the record.", "The foundation every later method assumes."], "Signature Method II: Polar Oceans Oceanography Operations": ["Setup, maintenance, scheduling, teardown.", "The unglamorous work made systematic.", "Reliability is a design choice.", "Checklists beat memory every time."], "Signature Method III: Polar Oceans Oceanography Resources": ["Materials, references, time, attention.", "Know what each unit of work costs.", "Use less while doing more.", "Waste is a design flaw to be engineered out."], "Signature Polar Oceans Oceanography Experience Design": ["Pacing, clarity, feedback, delight.", "Designed from the user's point of view.", "Every friction point named and reduced.", "Respect for the user's time is the metric."], "Signature Polar Oceans Oceanography Quality System": ["Standards written down and measurable.", "Inspection points at every handoff.", "Correction loops, not blame loops.", "What gets measured gets made well."], "Signature Polar Oceans Oceanography Troubleshooting Engine": ["Symptom to cause to fix, in order.", "Tests at every branch of the tree.", "Diagnose first, repair second.", "Document every resolution for the next time."], "Signature Polar Oceans Oceanography Stewardship and Cost Philosophy": ["Spend where results multiply.", "Cut where spending adds nothing.", "Honest books, always.", "Sustainability is a feature."], "Signature Method IV: Polar Oceans Oceanography Mastery": ["Competence refined into artistry.", "Deliberate practice with expert feedback.", "Iteration as a permanent habit.", "Mastery is a system, not a gift."], "Signature Method V: Teaching Polar Oceans Oceanography": ["Explain, demonstrate, correct, assess.", "Simple explanations prove understanding.", "Students learn by doing, not watching.", "Assessment measures real skill."], "Signature Polar Oceans Oceanography Community Model": ["Practitioners gathered around shared standards.", "Results shared openly, reviewed honestly.", "Newcomers mentored, experts challenged.", "Community as learning infrastructure."], "Signature Polar Oceans Oceanography Future Concepts": ["Prototypes of the possible future.", "Speculation labeled as speculation.", "Every concept built to be tested.", "The future is designed, not awaited."], "The Signature Polar Oceans Oceanography Master Plan": ["All methods in one coherent sequence.", "Milestones, resources, quality gates.", "Ambition made executable.", "The plan is a living document."], "Signature Polar Oceans Oceanography Compound Systems": ["Simple methods linked into new capabilities.", "Interactions managed, not hoped away.", "The whole tested, not just the parts.", "Composition as a deliberate art."]};
var DEMOKIND="signature oceanography simulator";
var RKIND="oceanography";
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
  if(!new RegExp('^'+"JAH\-E2SCIPOLAROS\-"+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-e2-sci-polar-oceans-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('e2-sci-polar-oceans-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
