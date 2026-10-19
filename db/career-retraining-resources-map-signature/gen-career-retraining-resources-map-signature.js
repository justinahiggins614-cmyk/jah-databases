(function(){'use strict';
/* JAH The Career Retraining Resources Map Signature Database generator — jahdb-career-retraining-resources-map-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRRM-";
var FIELDS=["training-programs","funding-sources","career-change-systems"];
var TOPICS={"training-programs":["Signature American Job Centers (Signature Edition) \u2014 training-programs","Signature Apprenticeships (Registered) (Signature Edition) \u2014 training-programs","Signature Free Online Training (Signature Edition) \u2014 training-programs","Signature Skilled Trades Training (Signature Edition) \u2014 training-programs","Signature Disability Employment (VR) (Signature Edition) \u2014 training-programs","Signature Youth Programs (Job Corps) (Signature Edition) \u2014 training-programs","Signature Resume Rebuilding (Signature Edition) \u2014 training-programs","Signature Salary Negotiation (New Field) (Signature Edition) \u2014 training-programs","Signature State-Specific Programs (Signature Edition) \u2014 training-programs","Signature Keeping Skills Current (Signature Edition) \u2014 training-programs","Signature Success Stories as Fuel (Signature Edition) \u2014 training-programs","Signature Portfolio Building (Signature Edition) \u2014 training-programs"],"funding-sources":["Signature WIOA Training Funds (Signature Edition) \u2014 funding-sources","Signature Community College Workforce (Signature Edition) \u2014 funding-sources","Signature Tech Retraining Paths (Signature Edition) \u2014 funding-sources","Signature CDL and Driving Careers (Signature Edition) \u2014 funding-sources","Signature Second Chance Employment (Signature Edition) \u2014 funding-sources","Signature Single Parent Retraining (Signature Edition) \u2014 funding-sources","Signature Interview After Retraining (Signature Edition) \u2014 funding-sources","Signature Avoiding Training Scams (Signature Edition) \u2014 funding-sources","Signature The 90-Day Retraining Plan (Signature Edition) \u2014 funding-sources","Signature The Career Change Budget (Signature Edition) \u2014 funding-sources","Signature The Retraining Checklist (Signature Edition) \u2014 funding-sources"],"career-change-systems":["Signature Trade Adjustment Assistance (Signature Edition) \u2014 career-change-systems","Signature Pell Grants for Retraining (Signature Edition) \u2014 career-change-systems","Signature Healthcare Retraining (Signature Edition) \u2014 career-change-systems","Signature Veterans Retraining (VR&E) (Signature Edition) \u2014 career-change-systems","Signature Older Worker Retraining (SCSEP) (Signature Edition) \u2014 career-change-systems","Signature English Learner Career Paths (Signature Edition) \u2014 career-change-systems","Signature Networking for Career Changers (Signature Edition) \u2014 career-change-systems","Signature Employer-Paid Training (Signature Edition) \u2014 career-change-systems","Signature Measuring Training ROI (Signature Edition) \u2014 career-change-systems","Signature Mental Game of Change (Signature Edition) \u2014 career-change-systems","Signature Certifications That Pay (Signature Edition) \u2014 career-change-systems"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Career Retraining Resources Map Signature Database — generated study\n"
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
   + "    print('kind: government-assistance record')\n"
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
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Career Retraining Resources Map Signature Database.',
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
var gen={version:'jahdb-career-retraining-resources-map-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('career-retraining-resources-map-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
