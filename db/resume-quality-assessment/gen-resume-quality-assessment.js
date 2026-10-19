(function(){'use strict';
/* JAH The Resume Quality Assessment Database generator — jahdb-resume-quality-assessment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RQA-";
var FIELDS=["resume-writing","ats-optimization","resume-review-systems"];
var TOPICS={"resume-writing":["The 6-Second Scan Test \u2014 resume-writing","The One-Page Rule (and Exceptions) \u2014 resume-writing","Quantifying Everything \u2014 resume-writing","Tailoring Per Application \u2014 resume-writing","LinkedIn-Resume Consistency \u2014 resume-writing","Reference Sheet Preparation \u2014 resume-writing","New Graduate Resume \u2014 resume-writing","The Referral Advantage \u2014 resume-writing","Resume A/B Testing \u2014 resume-writing","The 'So What' Test \u2014 resume-writing","The Final Proofread Protocol \u2014 resume-writing","Resume Truthfulness Standards \u2014 resume-writing"],"ats-optimization":["Achievement Bullets (XYZ Formula) \u2014 ats-optimization","Professional Summary That Works \u2014 ats-optimization","Action Verb Bank \u2014 ats-optimization","Resume Review Checklist (50 Points) \u2014 ats-optimization","Cover Letter Pairing \u2014 ats-optimization","Resume for Career Changers \u2014 ats-optimization","Resume Red Flags to Remove \u2014 ats-optimization","Resume File Naming \u2014 ats-optimization","AI Resume Screening Prep \u2014 ats-optimization","Testimonials on Resumes \u2014 ats-optimization","Resume Score Self-Audit \u2014 ats-optimization"],"resume-review-systems":["ATS Keyword Optimization \u2014 resume-review-systems","Skills Section Architecture \u2014 resume-review-systems","Employment Gap Handling \u2014 resume-review-systems","Peer Resume Review Protocol \u2014 resume-review-systems","Portfolio and Work Samples \u2014 resume-review-systems","Executive Resume Differences \u2014 resume-review-systems","Keyword Density Without Stuffing \u2014 resume-review-systems","Updating Quarterly \u2014 resume-review-systems","Salary History: Don't Disclose \u2014 resume-review-systems","Resume for Freelancers \u2014 resume-review-systems","Beating the 'Overqualified' Label \u2014 resume-review-systems"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Resume Quality Assessment Database — generated study\n"
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
   + "    print('kind: employment and workplace record')\n"
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
    standards:['employment and workplace record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Resume Quality Assessment Database.',
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
var gen={version:'jahdb-resume-quality-assessment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('resume-quality-assessment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
