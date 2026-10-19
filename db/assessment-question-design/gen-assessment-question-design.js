(function(){'use strict';
/* JAH The Assessment Question Design Database generator — jahdb-assessment-question-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AQD-";
var FIELDS=["question-types","test-construction","grading-and-analysis"];
var TOPICS={"question-types":["Bloom's Taxonomy Alignment \u2014 question-types","Short Answer Questions \u2014 question-types","Matching Questions \u2014 question-types","Test Blueprints \u2014 question-types","Avoiding Trick Questions \u2014 question-types","Exit Tickets \u2014 question-types","Partial Credit Policies \u2014 question-types","Oral Exams \u2014 question-types","Peer Assessment Systems \u2014 question-types","Analyzing Class Results \u2014 question-types","The Test Review Session \u2014 question-types","Two-Stage Exams \u2014 question-types"],"test-construction":["Multiple Choice That Works \u2014 test-construction","Essay Prompts That Elicit Thinking \u2014 test-construction","Fill-in-the-Blank Rules \u2014 test-construction","Item Difficulty Targeting \u2014 test-construction","Accommodations in Design \u2014 test-construction","Quiz Frequency Effects \u2014 test-construction","Curving: When and How \u2014 test-construction","Portfolio Assessment \u2014 test-construction","Standardized Test Prep Ethics \u2014 test-construction","Question Banking \u2014 test-construction","Building Assessments Backward \u2014 test-construction"],"grading-and-analysis":["True/False Done Right \u2014 grading-and-analysis","Rubric Construction \u2014 grading-and-analysis","Performance Assessments \u2014 grading-and-analysis","Distractor Analysis \u2014 grading-and-analysis","Formative vs Summative \u2014 grading-and-analysis","Grading for Learning \u2014 grading-and-analysis","Cheating-Resistant Design \u2014 grading-and-analysis","Self-Assessment Training \u2014 grading-and-analysis","Test Anxiety Reduction \u2014 grading-and-analysis","Accessibility in Testing \u2014 grading-and-analysis","The Assessment Audit \u2014 grading-and-analysis"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Assessment Question Design Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['education and learning record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Assessment Question Design Database.',
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
var gen={version:'jahdb-assessment-question-design-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('assessment-question-design',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
