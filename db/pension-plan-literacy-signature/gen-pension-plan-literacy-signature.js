(function(){'use strict';
/* JAH The Pension Plan Literacy Signature Database generator — jahdb-pension-plan-literacy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPL-";
var FIELDS=["pension-basics","401k-and-ira-mastery","social-security-strategy"];
var TOPICS={"pension-basics":["Signature Defined Benefit vs Defined Contribution (Signature Edition) \u2014 pension-basics","Signature Employer Match: Free Money Math (Signature Edition) \u2014 pension-basics","Signature Asset Allocation by Age (Signature Edition) \u2014 pension-basics","Signature Social Security Basics (Signature Edition) \u2014 pension-basics","Signature Required Minimum Distributions (Signature Edition) \u2014 pension-basics","Signature PBGC Pension Insurance (Signature Edition) \u2014 pension-basics","Signature Self-Employed Retirement (SEP/Solo 401k) (Signature Edition) \u2014 pension-basics","Signature Roth Conversion Ladders (Signature Edition) \u2014 pension-basics","Signature Working Longer: The Math (Signature Edition) \u2014 pension-basics","Signature Rollovers: 401(k) to IRA (Signature Edition) \u2014 pension-basics","Signature Long-Term Care Planning (Signature Edition) \u2014 pension-basics","Signature Retirement Scam Defense (Signature Edition) \u2014 pension-basics"],"401k-and-ira-mastery":["Signature How Pensions Calculate Benefits (Signature Edition) \u2014 401k-and-ira-mastery","Signature Traditional vs Roth 401(k) (Signature Edition) \u2014 401k-and-ira-mastery","Signature Expense Ratios: The Silent Killer (Signature Edition) \u2014 401k-and-ira-mastery","Signature When to Claim Social Security (Signature Edition) \u2014 401k-and-ira-mastery","Signature Pension Lump Sum vs Annuity (Signature Edition) \u2014 401k-and-ira-mastery","Signature Military and Government Pensions (Signature Edition) \u2014 401k-and-ira-mastery","Signature Catch-Up Contributions at 50+ (Signature Edition) \u2014 401k-and-ira-mastery","Signature Sequence of Returns Risk (Signature Edition) \u2014 401k-and-ira-mastery","Signature Pension Benefit Statements (Signature Edition) \u2014 401k-and-ira-mastery","Signature The Retirement Budget Build (Signature Edition) \u2014 401k-and-ira-mastery","Signature Estate + Retirement Integration (Signature Edition) \u2014 401k-and-ira-mastery"],"social-security-strategy":["Signature 401(k) Contribution Limits (Signature Edition) \u2014 social-security-strategy","Signature IRA Basics: Traditional and Roth (Signature Edition) \u2014 social-security-strategy","Signature Vesting Schedules (Signature Edition) \u2014 social-security-strategy","Signature The 4% Rule (and Its Limits) (Signature Edition) \u2014 social-security-strategy","Signature Cash Balance Plans (Signature Edition) \u2014 social-security-strategy","Signature TSP Mastery (Federal) (Signature Edition) \u2014 social-security-strategy","Signature Healthcare in Retirement (Signature Edition) \u2014 social-security-strategy","Signature Annuities: When They Fit (Signature Edition) \u2014 social-security-strategy","Signature Survivor Benefit Choices (Signature Edition) \u2014 social-security-strategy","Signature Tax Diversification (Signature Edition) \u2014 social-security-strategy","Signature The Annual Retirement Checkup (Signature Edition) \u2014 social-security-strategy"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Pension Plan Literacy Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['money and financial-decision record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Pension Plan Literacy Signature Database.',
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
var gen={version:'jahdb-pension-plan-literacy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pension-plan-literacy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
