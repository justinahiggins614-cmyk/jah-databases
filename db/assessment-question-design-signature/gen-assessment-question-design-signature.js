(function(){'use strict';
/* JAH The Assessment Question Design Signature Database generator — jahdb-assessment-question-design-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AQD-";
var FIELDS=["question-types","test-construction","grading-and-analysis"];
var TOPICS={"question-types":["Signature Bloom's Taxonomy Alignment (Signature Edition) \u2014 question-types","Signature Short Answer Questions (Signature Edition) \u2014 question-types","Signature Matching Questions (Signature Edition) \u2014 question-types","Signature Test Blueprints (Signature Edition) \u2014 question-types","Signature Avoiding Trick Questions (Signature Edition) \u2014 question-types","Signature Exit Tickets (Signature Edition) \u2014 question-types","Signature Partial Credit Policies (Signature Edition) \u2014 question-types","Signature Oral Exams (Signature Edition) \u2014 question-types","Signature Peer Assessment Systems (Signature Edition) \u2014 question-types","Signature Analyzing Class Results (Signature Edition) \u2014 question-types","Signature The Test Review Session (Signature Edition) \u2014 question-types","Signature Two-Stage Exams (Signature Edition) \u2014 question-types"],"test-construction":["Signature Multiple Choice That Works (Signature Edition) \u2014 test-construction","Signature Essay Prompts That Elicit Thinking (Signature Edition) \u2014 test-construction","Signature Fill-in-the-Blank Rules (Signature Edition) \u2014 test-construction","Signature Item Difficulty Targeting (Signature Edition) \u2014 test-construction","Signature Accommodations in Design (Signature Edition) \u2014 test-construction","Signature Quiz Frequency Effects (Signature Edition) \u2014 test-construction","Signature Curving: When and How (Signature Edition) \u2014 test-construction","Signature Portfolio Assessment (Signature Edition) \u2014 test-construction","Signature Standardized Test Prep Ethics (Signature Edition) \u2014 test-construction","Signature Question Banking (Signature Edition) \u2014 test-construction","Signature Building Assessments Backward (Signature Edition) \u2014 test-construction"],"grading-and-analysis":["Signature True/False Done Right (Signature Edition) \u2014 grading-and-analysis","Signature Rubric Construction (Signature Edition) \u2014 grading-and-analysis","Signature Performance Assessments (Signature Edition) \u2014 grading-and-analysis","Signature Distractor Analysis (Signature Edition) \u2014 grading-and-analysis","Signature Formative vs Summative (Signature Edition) \u2014 grading-and-analysis","Signature Grading for Learning (Signature Edition) \u2014 grading-and-analysis","Signature Cheating-Resistant Design (Signature Edition) \u2014 grading-and-analysis","Signature Self-Assessment Training (Signature Edition) \u2014 grading-and-analysis","Signature Test Anxiety Reduction (Signature Edition) \u2014 grading-and-analysis","Signature Accessibility in Testing (Signature Edition) \u2014 grading-and-analysis","Signature The Assessment Audit (Signature Edition) \u2014 grading-and-analysis"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Assessment Question Design Signature Database — generated study\n"
   + "# Topic: "+safe+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\", 'seed': "+seed+"}\n"
   + "CHECKS = ['topic_set','field_set','seed_set']\n"
   + "def validate(r):\n"
   + "    missing = [c for c in CHECKS if not r.get(c.replace('_set','')) and c!='seed_set']\n"
   + "    assert r['title'] and r['field'], 'record incomplete'\n"
   + "    return True\n"
   + "def main():\n"
   + "    assert validate(record)\n"
   + "    print('study: '+record['title'])\n"
   + "    print('field: '+record['field'])\n"
   + "    print('kind: education and learning record')\n"
   + "    print('Sample record — structural sample, not an archive entry.')\n"
   + "if __name__ == '__main__':\n"
   + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['education and learning record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Assessment Question Design Signature Database.',
    last_verified:'2026-10-18',
    ladder_rank:1, ladder_tier:'Foundations',
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Structural sample demo.'},
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
var gen={version:'jahdb-assessment-question-design-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('assessment-question-design-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
