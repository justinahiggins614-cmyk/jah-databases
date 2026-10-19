(function(){'use strict';
/* JAH The AI Bias Measurement Database generator — jahdb-ai-bias-measurement-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ABM-";
var FIELDS=["bias-detection-methods","fairness-metrics","bias-monitoring"];
var TOPICS={"bias-detection-methods":["What Counts as AI Bias \u2014 bias-detection-methods","Equalized Odds \u2014 bias-detection-methods","Individual Fairness \u2014 bias-detection-methods","Representation Analysis \u2014 bias-detection-methods","LLM Bias Benchmarks \u2014 bias-detection-methods","Recommender Bias \u2014 bias-detection-methods","Healthcare AI Bias \u2014 bias-detection-methods","A/B Testing for Fairness \u2014 bias-detection-methods","Mitigation: Post-processing \u2014 bias-detection-methods","The Bias Measurement Playbook \u2014 bias-detection-methods","Temporal Bias Drift \u2014 bias-detection-methods","Red-Teaming for Bias \u2014 bias-detection-methods"],"fairness-metrics":["Disparate Impact \u2014 fairness-metrics","Equal Opportunity \u2014 fairness-metrics","Counterfactual Fairness \u2014 fairness-metrics","Label Bias Detection \u2014 fairness-metrics","Vision Model Bias \u2014 fairness-metrics","Hiring AI Audits \u2014 fairness-metrics","Intersectional Analysis \u2014 fairness-metrics","Mitigation: Pre-processing \u2014 fairness-metrics","Documenting Bias Findings \u2014 fairness-metrics","Fairness Toolkits \u2014 fairness-metrics","Proxy Discrimination \u2014 fairness-metrics"],"bias-monitoring":["Demographic Parity \u2014 bias-monitoring","Calibration Across Groups \u2014 bias-monitoring","Bias in Training Data \u2014 bias-monitoring","NLP Bias Tests (WEAT/SEAT) \u2014 bias-monitoring","Speech Model Bias \u2014 bias-monitoring","Lending Fairness Tests \u2014 bias-monitoring","Bias Dashboards \u2014 bias-monitoring","Mitigation: In-processing \u2014 bias-monitoring","Stakeholder Review \u2014 bias-monitoring","Bias in Human Labels \u2014 bias-monitoring","Explainability for Bias \u2014 bias-monitoring"]};
var KINDS="AI-systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The AI Bias Measurement Database — generated study\n"
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
   + "    print('kind: AI-systems record')\n"
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
    standards:['AI-systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The AI Bias Measurement Database.',
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
var gen={version:'jahdb-ai-bias-measurement-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-bias-measurement',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
