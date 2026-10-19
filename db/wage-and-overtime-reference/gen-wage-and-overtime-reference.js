(function(){'use strict';
/* JAH The Wage and Overtime Reference Database generator — jahdb-wage-and-overtime-reference-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WOR-";
var FIELDS=["wage-basics","overtime-rules","paycheck-rights"];
var TOPICS={"wage-basics":["Federal Minimum Wage \u2014 wage-basics","Tipped Wage Rules \u2014 wage-basics","Final Paycheck Laws \u2014 wage-basics","Prevailing Wage Jobs \u2014 wage-basics","Discussing Pay Is Protected \u2014 wage-basics","Travel Time Pay \u2014 wage-basics","Wage Theft: Spotting It \u2014 wage-basics","Salary Negotiation Basics \u2014 wage-basics","Comp Time Rules \u2014 wage-basics","Domestic Worker Rights \u2014 wage-basics","Pay Frequency Laws \u2014 wage-basics","Severance Pay Basics \u2014 wage-basics"],"overtime-rules":["Overtime: Time-and-a-Half Rule \u2014 overtime-rules","Calculating Your Regular Rate \u2014 overtime-rules","Independent Contractor vs Employee \u2014 overtime-rules","Youth Employment Rules \u2014 overtime-rules","Overtime for Remote Workers \u2014 overtime-rules","Training Time Pay \u2014 overtime-rules","Filing a Wage Claim \u2014 overtime-rules","Raise Request Playbook \u2014 overtime-rules","Piece Rate and Overtime \u2014 overtime-rules","Commission Pay and Overtime \u2014 overtime-rules","The Paycheck Audit \u2014 overtime-rules"],"paycheck-rights":["Exempt vs Non-Exempt \u2014 paycheck-rights","Paycheck Deductions: Legal vs Not \u2014 paycheck-rights","Gig Worker Pay Realities \u2014 paycheck-rights","Equal Pay Rights \u2014 paycheck-rights","On-Call Pay Rules \u2014 paycheck-rights","Meal and Rest Breaks \u2014 paycheck-rights","Pay Stub Requirements \u2014 paycheck-rights","Overtime Exemption Salary Threshold \u2014 paycheck-rights","Agricultural Wage Exceptions \u2014 paycheck-rights","Prevailing Wage Fringe Benefits \u2014 paycheck-rights","Knowing Your State Labor Department \u2014 paycheck-rights"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Wage and Overtime Reference Database — generated study\n"
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
    provenance:'Generated structural sample for the The Wage and Overtime Reference Database.',
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
var gen={version:'jahdb-wage-and-overtime-reference-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wage-and-overtime-reference',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
