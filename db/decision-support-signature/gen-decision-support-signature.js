(function(){'use strict';
/* JAH The Decision Support Signature Database generator — jahdb-decision-support-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DS-";
var FIELDS=["decision-frameworks","choice-analysis-methods","decision-aids"];
var TOPICS={"decision-frameworks":["Signature Weighted Decision Matrix (Signature Edition) \u2014 decision-frameworks","Signature Decision Tree Mapping (Signature Edition) \u2014 decision-frameworks","Signature Regret Minimization Framework (Signature Edition) \u2014 decision-frameworks","Signature Red Team Review (Signature Edition) \u2014 decision-frameworks","Signature Satisficing vs Maximizing (Signature Edition) \u2014 decision-frameworks","Signature Decision Journal (Signature Edition) \u2014 decision-frameworks","Signature Pareto Prioritization (80/20) (Signature Edition) \u2014 decision-frameworks","Signature Coin-Flip Clarity Test (Signature Edition) \u2014 decision-frameworks","Signature Scenario Planning (Personal) (Signature Edition) \u2014 decision-frameworks","Signature Expected Regret Comparison (Signature Edition) \u2014 decision-frameworks","Signature Choice Architecture (Nudges) (Signature Edition) \u2014 decision-frameworks","Signature Decision Review Cadence (Signature Edition) \u2014 decision-frameworks"],"choice-analysis-methods":["Signature Pros-and-Cons with Weights (Signature Edition) \u2014 choice-analysis-methods","Signature Cost-Benefit Analysis (Personal) (Signature Edition) \u2014 choice-analysis-methods","Signature The 10-10-10 Rule (Signature Edition) \u2014 choice-analysis-methods","Signature Second-Order Thinking (Signature Edition) \u2014 choice-analysis-methods","Signature The Delegation Test (Signature Edition) \u2014 choice-analysis-methods","Signature Base Rate Check (Signature Edition) \u2014 choice-analysis-methods","Signature Eisenhower Matrix (Signature Edition) \u2014 choice-analysis-methods","Signature Advisor Aggregation (Signature Edition) \u2014 choice-analysis-methods","Signature Worst-Case / Best-Case Bounds (Signature Edition) \u2014 choice-analysis-methods","Signature Value-of-Information Test (Signature Edition) \u2014 choice-analysis-methods","Signature Default Option Design (Signature Edition) \u2014 choice-analysis-methods"],"decision-aids":["Signature Expected Value Calculation (Signature Edition) \u2014 decision-aids","Signature Personal SWOT Analysis (Signature Edition) \u2014 decision-aids","Signature Pre-Mortem Exercise (Signature Edition) \u2014 decision-aids","Signature Opportunity Cost Accounting (Signature Edition) \u2014 decision-aids","Signature Reversible vs Irreversible Sort (Signature Edition) \u2014 decision-aids","Signature Fermi Estimation (Signature Edition) \u2014 decision-aids","Signature The Two-List Method (Signature Edition) \u2014 decision-aids","Signature Devil's Advocate Session (Signature Edition) \u2014 decision-aids","Signature Minimax Choice Rule (Signature Edition) \u2014 decision-aids","Signature Decision Fatigue Management (Signature Edition) \u2014 decision-aids","Signature Commitment Devices (Signature Edition) \u2014 decision-aids"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Decision Support Signature Database — generated study\n"
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
   + "    print('kind: everyday problem-solving record')\n"
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
    standards:['everyday problem-solving record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Decision Support Signature Database.',
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
var gen={version:'jahdb-decision-support-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decision-support-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
