(function(){'use strict';
/* JAH The Outcome Verification Database generator — jahdb-outcome-verification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OV-";
var FIELDS=["result-checking-methods","measurement-techniques","verification-systems"];
var TOPICS={"result-checking-methods":["Before-and-After Measurement \u2014 result-checking-methods","Testimonial Verification \u2014 result-checking-methods","Goal Completion Criteria \u2014 result-checking-methods","Metric Gaming Detection \u2014 result-checking-methods","Budget Variance Review \u2014 result-checking-methods","Project Post-Mortem \u2014 result-checking-methods","Diet and Nutrition Verification \u2014 result-checking-methods","The Honest Weekly Review \u2014 result-checking-methods","Home Project Completion Check \u2014 result-checking-methods","The Proof-of-Work Portfolio \u2014 result-checking-methods","Verification Before Trust \u2014 result-checking-methods","Verifying Contractor Quotes \u2014 result-checking-methods"],"measurement-techniques":["The 30-Day Check-In \u2014 measurement-techniques","Habit Outcome Auditing \u2014 measurement-techniques","The Red-Team Retrospective \u2014 measurement-techniques","The 'Would I Recommend It' Test \u2014 measurement-techniques","Health Marker Tracking \u2014 measurement-techniques","Contractor Work Verification \u2014 measurement-techniques","Sleep Improvement Measurement \u2014 measurement-techniques","Relationship Check-In Scores \u2014 measurement-techniques","The 6-Month Life Audit \u2014 measurement-techniques","Warranty and Guarantee Claims \u2014 measurement-techniques","Outcome Celebration Protocol \u2014 measurement-techniques"],"verification-systems":["Receipt and Proof Filing \u2014 verification-systems","Purchase Satisfaction Scoring \u2014 verification-systems","Third-Party Verification \u2014 verification-systems","Time Audit vs Plan \u2014 verification-systems","Learning Outcome Testing \u2014 verification-systems","The Expectation Gap Log \u2014 verification-systems","Business Metric Verification \u2014 verification-systems","Car Repair Verification \u2014 verification-systems","Verifying Advice Quality \u2014 verification-systems","The Annual 'Did It Work' Review \u2014 verification-systems","The Verification Calendar \u2014 verification-systems"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Outcome Verification Database — generated study\n"
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
   + "    print('kind: everyday problem-solving record')\n"
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
    standards:['everyday problem-solving record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Outcome Verification Database.',
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
var gen={version:'jahdb-outcome-verification-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('outcome-verification',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
