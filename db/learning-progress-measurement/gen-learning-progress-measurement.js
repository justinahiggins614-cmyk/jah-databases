(function(){'use strict';
/* JAH The Learning Progress Measurement Database generator — jahdb-learning-progress-measurement-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LPM-";
var FIELDS=["progress-tracking","mastery-assessment","growth-analytics"];
var TOPICS={"progress-tracking":["Learning Baselines \u2014 progress-tracking","Spaced Repetition Tracking \u2014 progress-tracking","Math Fact Fluency \u2014 progress-tracking","Learning Curves \u2014 progress-tracking","Student Self-Tracking \u2014 progress-tracking","Pre/Post Effect Sizes \u2014 progress-tracking","Milestone Celebrations \u2014 progress-tracking","Measuring Engagement \u2014 progress-tracking","Sports Skill Assessment \u2014 progress-tracking","Reflection Journals as Data \u2014 progress-tracking","When Measures Disagree \u2014 progress-tracking","The One-Page Learning Report \u2014 progress-tracking"],"mastery-assessment":["Mastery Thresholds (80% Rule) \u2014 mastery-assessment","Portfolio Growth Evidence \u2014 mastery-assessment","Writing Progress Rubrics \u2014 mastery-assessment","Confidence-Weighted Testing \u2014 mastery-assessment","Growth Percentiles \u2014 mastery-assessment","Longitudinal Tracking \u2014 mastery-assessment","Parent Progress Reports \u2014 mastery-assessment","Language Proficiency Levels \u2014 mastery-assessment","Coding Progress Markers \u2014 mastery-assessment","Peer Benchmarking \u2014 mastery-assessment","Sharing Data with Students \u2014 mastery-assessment"],"growth-analytics":["The Testing Effect as Measurement \u2014 growth-analytics","Reading Level Tracking \u2014 growth-analytics","Skill Checklists \u2014 growth-analytics","Exit Ticket Trends \u2014 growth-analytics","Competency-Based Progression \u2014 growth-analytics","The Learning Dashboard \u2014 growth-analytics","Intervention Trigger Rules \u2014 growth-analytics","Music Practice Metrics \u2014 growth-analytics","The 'Can Do' Statement Bank \u2014 growth-analytics","The Annual Learning Review \u2014 growth-analytics","The Measurement Audit \u2014 growth-analytics"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Learning Progress Measurement Database — generated study\n"
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
    provenance:'Generated structural sample for the The Learning Progress Measurement Database.',
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
var gen={version:'jahdb-learning-progress-measurement-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('learning-progress-measurement',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
