(function(){'use strict';
/* JAH The Student Loan Navigation Database generator — jahdb-student-loan-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SLN-";
var FIELDS=["borrowing-decisions","repayment-plans","forgiveness-and-refinance"];
var TOPICS={"borrowing-decisions":["How Much to Borrow Rule \u2014 borrowing-decisions","Scholarship Stacking Strategy \u2014 borrowing-decisions","Standard 10-Year Plan Math \u2014 borrowing-decisions","Avoiding Default \u2014 borrowing-decisions","Community College Transfer Path \u2014 borrowing-decisions","Extra Payment Strategy \u2014 borrowing-decisions","Military Education Benefits \u2014 borrowing-decisions","Tax Benefits for Student Loans \u2014 borrowing-decisions","Living Costs: The Hidden Half \u2014 borrowing-decisions","Repayment After Graduation Checklist \u2014 borrowing-decisions","When to Pause Extra Payments \u2014 borrowing-decisions","Consolidation: Federal Direct \u2014 borrowing-decisions"],"repayment-plans":["Federal vs Private Loans \u2014 repayment-plans","Income-Driven Repayment (IDR) Plans \u2014 repayment-plans","Graduated Repayment \u2014 repayment-plans","Parent PLUS Loan Reality \u2014 repayment-plans","Employer Tuition Benefits \u2014 repayment-plans","Forbearance: Emergency Only \u2014 repayment-plans","Graduate School Debt Rules \u2014 repayment-plans","The 'Degree ROI' Calculation \u2014 repayment-plans","Appealing Financial Aid Offers \u2014 repayment-plans","Paying During School \u2014 repayment-plans","Tracking Forgiveness Progress \u2014 repayment-plans"],"forgiveness-and-refinance":["FAFSA Mastery \u2014 forgiveness-and-refinance","Public Service Loan Forgiveness (PSLF) \u2014 forgiveness-and-refinance","Refinancing Private Loans \u2014 forgiveness-and-refinance","Work-Study Optimization \u2014 forgiveness-and-refinance","Loan Servicer Management \u2014 forgiveness-and-refinance","Teacher and Nurse Forgiveness \u2014 forgiveness-and-refinance","Cosigner Release and Protection \u2014 forgiveness-and-refinance","Part-Time Work During School \u2014 forgiveness-and-refinance","Student Loan Scam Avoidance \u2014 forgiveness-and-refinance","The 5-Year Payoff Sprint \u2014 forgiveness-and-refinance","Life After the Last Payment \u2014 forgiveness-and-refinance"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Student Loan Navigation Database — generated study\n"
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
   + "    print('kind: money and financial-decision record')\n"
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
    standards:['money and financial-decision record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Student Loan Navigation Database.',
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
var gen={version:'jahdb-student-loan-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('student-loan-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
