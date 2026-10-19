(function(){'use strict';
/* JAH The Workforce Demand Analysis Database generator — jahdb-workforce-demand-analysis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WDA-";
var FIELDS=["labor-market-analysis","skill-gap-methods","hiring-demand-planning"];
var TOPICS={"labor-market-analysis":["Reading BLS Data \u2014 labor-market-analysis","Workforce Planning Horizons \u2014 labor-market-analysis","Demand Forecasting Models \u2014 labor-market-analysis","Automation Impact Assessment \u2014 labor-market-analysis","Succession Demand Modeling \u2014 labor-market-analysis","Internal Mobility Analysis \u2014 labor-market-analysis","Hiring Manager Effectiveness \u2014 labor-market-analysis","Contingent Conversion Analysis \u2014 labor-market-analysis","AI in Hiring: Audit It \u2014 labor-market-analysis","Total Rewards Communication \u2014 labor-market-analysis","Benchmarking Participation \u2014 labor-market-analysis","The Demand Review Cadence \u2014 labor-market-analysis"],"skill-gap-methods":["Job Posting Analytics \u2014 skill-gap-methods","Turnover Analysis \u2014 skill-gap-methods","Labor Market Tightness \u2014 skill-gap-methods","Gig and Contingent Demand \u2014 skill-gap-methods","Location Strategy Analysis \u2014 skill-gap-methods","Headcount vs Productivity \u2014 skill-gap-methods","University Pipeline ROI \u2014 skill-gap-methods","Workforce Scenario Planning \u2014 skill-gap-methods","Return-to-Office Impact \u2014 skill-gap-methods","Labor Law Change Tracking \u2014 skill-gap-methods","Workforce Risk Register \u2014 skill-gap-methods"],"hiring-demand-planning":["Skill Gap Analysis \u2014 hiring-demand-planning","Time-to-Fill Benchmarks \u2014 hiring-demand-planning","Wage Benchmarking \u2014 hiring-demand-planning","Diversity Pipeline Analysis \u2014 hiring-demand-planning","Employer Brand Measurement \u2014 hiring-demand-planning","Attrition Risk Scoring \u2014 hiring-demand-planning","Skills-Based Hiring Analysis \u2014 hiring-demand-planning","The Annual Workforce Report \u2014 hiring-demand-planning","Four-Day Week Pilots \u2014 hiring-demand-planning","The Workforce Dashboard \u2014 hiring-demand-planning","Planning for Growth Spurts \u2014 hiring-demand-planning"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Workforce Demand Analysis Database — generated study\n"
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
    provenance:'Generated structural sample for the The Workforce Demand Analysis Database.',
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
var gen={version:'jahdb-workforce-demand-analysis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('workforce-demand-analysis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
