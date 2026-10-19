(function(){'use strict';
/* JAH The Career Retraining Resources Map Database generator — jahdb-career-retraining-resources-map-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRRM-";
var FIELDS=["training-programs","funding-sources","career-change-systems"];
var TOPICS={"training-programs":["American Job Centers \u2014 training-programs","Apprenticeships (Registered) \u2014 training-programs","Free Online Training \u2014 training-programs","Skilled Trades Training \u2014 training-programs","Disability Employment (VR) \u2014 training-programs","Youth Programs (Job Corps) \u2014 training-programs","Resume Rebuilding \u2014 training-programs","Salary Negotiation (New Field) \u2014 training-programs","State-Specific Programs \u2014 training-programs","Keeping Skills Current \u2014 training-programs","Success Stories as Fuel \u2014 training-programs","Portfolio Building \u2014 training-programs"],"funding-sources":["WIOA Training Funds \u2014 funding-sources","Community College Workforce \u2014 funding-sources","Tech Retraining Paths \u2014 funding-sources","CDL and Driving Careers \u2014 funding-sources","Second Chance Employment \u2014 funding-sources","Single Parent Retraining \u2014 funding-sources","Interview After Retraining \u2014 funding-sources","Avoiding Training Scams \u2014 funding-sources","The 90-Day Retraining Plan \u2014 funding-sources","The Career Change Budget \u2014 funding-sources","The Retraining Checklist \u2014 funding-sources"],"career-change-systems":["Trade Adjustment Assistance \u2014 career-change-systems","Pell Grants for Retraining \u2014 career-change-systems","Healthcare Retraining \u2014 career-change-systems","Veterans Retraining (VR&E) \u2014 career-change-systems","Older Worker Retraining (SCSEP) \u2014 career-change-systems","English Learner Career Paths \u2014 career-change-systems","Networking for Career Changers \u2014 career-change-systems","Employer-Paid Training \u2014 career-change-systems","Measuring Training ROI \u2014 career-change-systems","Mental Game of Change \u2014 career-change-systems","Certifications That Pay \u2014 career-change-systems"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Career Retraining Resources Map Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Career Retraining Resources Map Database.',
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
var gen={version:'jahdb-career-retraining-resources-map-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('career-retraining-resources-map',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
