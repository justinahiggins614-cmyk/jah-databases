(function(){'use strict';
/* JAH The Resume Quality Assessment Signature Database generator — jahdb-resume-quality-assessment-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RQA-";
var FIELDS=["resume-writing","ats-optimization","resume-review-systems"];
var TOPICS={"resume-writing":["Signature The 6-Second Scan Test (Signature Edition) \u2014 resume-writing","Signature The One-Page Rule (and Exceptions) (Signature Edition) \u2014 resume-writing","Signature Quantifying Everything (Signature Edition) \u2014 resume-writing","Signature Tailoring Per Application (Signature Edition) \u2014 resume-writing","Signature LinkedIn-Resume Consistency (Signature Edition) \u2014 resume-writing","Signature Reference Sheet Preparation (Signature Edition) \u2014 resume-writing","Signature New Graduate Resume (Signature Edition) \u2014 resume-writing","Signature The Referral Advantage (Signature Edition) \u2014 resume-writing","Signature Resume A/B Testing (Signature Edition) \u2014 resume-writing","Signature The 'So What' Test (Signature Edition) \u2014 resume-writing","Signature The Final Proofread Protocol (Signature Edition) \u2014 resume-writing","Signature Resume Truthfulness Standards (Signature Edition) \u2014 resume-writing"],"ats-optimization":["Signature Achievement Bullets (XYZ Formula) (Signature Edition) \u2014 ats-optimization","Signature Professional Summary That Works (Signature Edition) \u2014 ats-optimization","Signature Action Verb Bank (Signature Edition) \u2014 ats-optimization","Signature Resume Review Checklist (50 Points) (Signature Edition) \u2014 ats-optimization","Signature Cover Letter Pairing (Signature Edition) \u2014 ats-optimization","Signature Resume for Career Changers (Signature Edition) \u2014 ats-optimization","Signature Resume Red Flags to Remove (Signature Edition) \u2014 ats-optimization","Signature Resume File Naming (Signature Edition) \u2014 ats-optimization","Signature AI Resume Screening Prep (Signature Edition) \u2014 ats-optimization","Signature Testimonials on Resumes (Signature Edition) \u2014 ats-optimization","Signature Resume Score Self-Audit (Signature Edition) \u2014 ats-optimization"],"resume-review-systems":["Signature ATS Keyword Optimization (Signature Edition) \u2014 resume-review-systems","Signature Skills Section Architecture (Signature Edition) \u2014 resume-review-systems","Signature Employment Gap Handling (Signature Edition) \u2014 resume-review-systems","Signature Peer Resume Review Protocol (Signature Edition) \u2014 resume-review-systems","Signature Portfolio and Work Samples (Signature Edition) \u2014 resume-review-systems","Signature Executive Resume Differences (Signature Edition) \u2014 resume-review-systems","Signature Keyword Density Without Stuffing (Signature Edition) \u2014 resume-review-systems","Signature Updating Quarterly (Signature Edition) \u2014 resume-review-systems","Signature Salary History: Don't Disclose (Signature Edition) \u2014 resume-review-systems","Signature Resume for Freelancers (Signature Edition) \u2014 resume-review-systems","Signature Beating the 'Overqualified' Label (Signature Edition) \u2014 resume-review-systems"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Resume Quality Assessment Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['employment and workplace record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Resume Quality Assessment Signature Database.',
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
var gen={version:'jahdb-resume-quality-assessment-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('resume-quality-assessment-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
