(function(){'use strict';
/* JAH The Pension Plan Literacy Database generator — jahdb-pension-plan-literacy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPL-";
var FIELDS=["pension-basics","401k-and-ira-mastery","social-security-strategy"];
var TOPICS={"pension-basics":["Defined Benefit vs Defined Contribution \u2014 pension-basics","Employer Match: Free Money Math \u2014 pension-basics","Asset Allocation by Age \u2014 pension-basics","Social Security Basics \u2014 pension-basics","Required Minimum Distributions \u2014 pension-basics","PBGC Pension Insurance \u2014 pension-basics","Self-Employed Retirement (SEP/Solo 401k) \u2014 pension-basics","Roth Conversion Ladders \u2014 pension-basics","Working Longer: The Math \u2014 pension-basics","Rollovers: 401(k) to IRA \u2014 pension-basics","Long-Term Care Planning \u2014 pension-basics","Retirement Scam Defense \u2014 pension-basics"],"401k-and-ira-mastery":["How Pensions Calculate Benefits \u2014 401k-and-ira-mastery","Traditional vs Roth 401(k) \u2014 401k-and-ira-mastery","Expense Ratios: The Silent Killer \u2014 401k-and-ira-mastery","When to Claim Social Security \u2014 401k-and-ira-mastery","Pension Lump Sum vs Annuity \u2014 401k-and-ira-mastery","Military and Government Pensions \u2014 401k-and-ira-mastery","Catch-Up Contributions at 50+ \u2014 401k-and-ira-mastery","Sequence of Returns Risk \u2014 401k-and-ira-mastery","Pension Benefit Statements \u2014 401k-and-ira-mastery","The Retirement Budget Build \u2014 401k-and-ira-mastery","Estate + Retirement Integration \u2014 401k-and-ira-mastery"],"social-security-strategy":["401(k) Contribution Limits \u2014 social-security-strategy","IRA Basics: Traditional and Roth \u2014 social-security-strategy","Vesting Schedules \u2014 social-security-strategy","The 4% Rule (and Its Limits) \u2014 social-security-strategy","Cash Balance Plans \u2014 social-security-strategy","TSP Mastery (Federal) \u2014 social-security-strategy","Healthcare in Retirement \u2014 social-security-strategy","Annuities: When They Fit \u2014 social-security-strategy","Survivor Benefit Choices \u2014 social-security-strategy","Tax Diversification \u2014 social-security-strategy","The Annual Retirement Checkup \u2014 social-security-strategy"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Pension Plan Literacy Database — generated study\n"
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
    provenance:'Generated structural sample for the The Pension Plan Literacy Database.',
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
var gen={version:'jahdb-pension-plan-literacy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pension-plan-literacy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
