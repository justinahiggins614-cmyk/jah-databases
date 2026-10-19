(function(){'use strict';
/* JAH The Wage and Overtime Reference Signature Database generator — jahdb-wage-and-overtime-reference-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WOR-";
var FIELDS=["wage-basics","overtime-rules","paycheck-rights"];
var TOPICS={"wage-basics":["Signature Federal Minimum Wage (Signature Edition) \u2014 wage-basics","Signature Tipped Wage Rules (Signature Edition) \u2014 wage-basics","Signature Final Paycheck Laws (Signature Edition) \u2014 wage-basics","Signature Prevailing Wage Jobs (Signature Edition) \u2014 wage-basics","Signature Discussing Pay Is Protected (Signature Edition) \u2014 wage-basics","Signature Travel Time Pay (Signature Edition) \u2014 wage-basics","Signature Wage Theft: Spotting It (Signature Edition) \u2014 wage-basics","Signature Salary Negotiation Basics (Signature Edition) \u2014 wage-basics","Signature Comp Time Rules (Signature Edition) \u2014 wage-basics","Signature Domestic Worker Rights (Signature Edition) \u2014 wage-basics","Signature Pay Frequency Laws (Signature Edition) \u2014 wage-basics","Signature Severance Pay Basics (Signature Edition) \u2014 wage-basics"],"overtime-rules":["Signature Overtime: Time-and-a-Half Rule (Signature Edition) \u2014 overtime-rules","Signature Calculating Your Regular Rate (Signature Edition) \u2014 overtime-rules","Signature Independent Contractor vs Employee (Signature Edition) \u2014 overtime-rules","Signature Youth Employment Rules (Signature Edition) \u2014 overtime-rules","Signature Overtime for Remote Workers (Signature Edition) \u2014 overtime-rules","Signature Training Time Pay (Signature Edition) \u2014 overtime-rules","Signature Filing a Wage Claim (Signature Edition) \u2014 overtime-rules","Signature Raise Request Playbook (Signature Edition) \u2014 overtime-rules","Signature Piece Rate and Overtime (Signature Edition) \u2014 overtime-rules","Signature Commission Pay and Overtime (Signature Edition) \u2014 overtime-rules","Signature The Paycheck Audit (Signature Edition) \u2014 overtime-rules"],"paycheck-rights":["Signature Exempt vs Non-Exempt (Signature Edition) \u2014 paycheck-rights","Signature Paycheck Deductions: Legal vs Not (Signature Edition) \u2014 paycheck-rights","Signature Gig Worker Pay Realities (Signature Edition) \u2014 paycheck-rights","Signature Equal Pay Rights (Signature Edition) \u2014 paycheck-rights","Signature On-Call Pay Rules (Signature Edition) \u2014 paycheck-rights","Signature Meal and Rest Breaks (Signature Edition) \u2014 paycheck-rights","Signature Pay Stub Requirements (Signature Edition) \u2014 paycheck-rights","Signature Overtime Exemption Salary Threshold (Signature Edition) \u2014 paycheck-rights","Signature Agricultural Wage Exceptions (Signature Edition) \u2014 paycheck-rights","Signature Prevailing Wage Fringe Benefits (Signature Edition) \u2014 paycheck-rights","Signature Knowing Your State Labor Department (Signature Edition) \u2014 paycheck-rights"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Wage and Overtime Reference Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Wage and Overtime Reference Signature Database.',
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
var gen={version:'jahdb-wage-and-overtime-reference-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wage-and-overtime-reference-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
