(function(){'use strict';
/* JAH The Renovation Cost Planning Database generator — jahdb-renovation-cost-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RCP-";
var FIELDS=["project-scoping","cost-estimation","contractor-management"];
var TOPICS={"project-scoping":["The 20% Contingency Rule \u2014 project-scoping","Kitchen Remodel Cost Breakdown \u2014 project-scoping","The Design-Build vs Bid Decision \u2014 project-scoping","ROI: What Renovations Return \u2014 project-scoping","Vetting Contractors \u2014 project-scoping","Timeline Planning Realism \u2014 project-scoping","Asbestos and Lead Testing Budget \u2014 project-scoping","Paint Budget Reality \u2014 project-scoping","Roof Replacement Budgeting \u2014 project-scoping","Addition Cost Planning \u2014 project-scoping","Warranty Documentation \u2014 project-scoping","Small Project Budget Formulas \u2014 project-scoping"],"cost-estimation":["Scope Writing That Prevents Disputes \u2014 cost-estimation","Bathroom Remodel Cost Breakdown \u2014 cost-estimation","Permit Costs and Timelines \u2014 cost-estimation","Change Order Control \u2014 cost-estimation","The Contract Checklist \u2014 cost-estimation","Material Selection Budget Tiers \u2014 cost-estimation","Energy Upgrades in the Budget \u2014 cost-estimation","Plumbing Rough-In Costs \u2014 cost-estimation","Window Replacement Math \u2014 cost-estimation","Outdoor and Landscape Budgets \u2014 cost-estimation","Renovation Regret Prevention \u2014 cost-estimation"],"contractor-management":["Getting Three Comparable Bids \u2014 contractor-management","Cost Per Square Foot Benchmarks \u2014 contractor-management","Financing: Cash vs HELOC vs Loan \u2014 contractor-management","Payment Schedules That Protect You \u2014 contractor-management","DIY vs Hire Decision Matrix \u2014 contractor-management","Living Through Renovation \u2014 contractor-management","Flooring Cost Comparison \u2014 contractor-management","Electrical Panel and Rewiring \u2014 contractor-management","HVAC Replacement Planning \u2014 contractor-management","The Final Walkthrough System \u2014 contractor-management","Post-Renovation Cost Audit \u2014 contractor-management"]};
var KINDS="home and household-systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Renovation Cost Planning Database — generated study\n"
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
   + "    print('kind: home and household-systems record')\n"
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
    standards:['home and household-systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Renovation Cost Planning Database.',
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
var gen={version:'jahdb-renovation-cost-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('renovation-cost-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
