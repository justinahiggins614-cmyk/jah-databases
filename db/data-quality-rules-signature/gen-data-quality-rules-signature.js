(function(){'use strict';
/* JAH The Data Quality Rules Signature Database generator — jahdb-data-quality-rules-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DQR-";
var FIELDS=["quality-profiling","validation-rules","quality-monitoring"];
var TOPICS={"quality-profiling":["Signature The Six Dimensions (Signature Edition) \u2014 quality-profiling","Signature Uniqueness Rules (Signature Edition) \u2014 quality-profiling","Signature Accuracy Sampling (Signature Edition) \u2014 quality-profiling","Signature Great Expectations Intro (Signature Edition) \u2014 quality-profiling","Signature Data Quality Dashboards (Signature Edition) \u2014 quality-profiling","Signature Quarantine Patterns (Signature Edition) \u2014 quality-profiling","Signature Master Data Management (Signature Edition) \u2014 quality-profiling","Signature Measuring Quality ROI (Signature Edition) \u2014 quality-profiling","Signature Duplicate Detection Methods (Signature Edition) \u2014 quality-profiling","Signature Enrichment Validation (Signature Edition) \u2014 quality-profiling","Signature Streaming Quality (Signature Edition) \u2014 quality-profiling","Signature Crowdsourced Quality (Signature Edition) \u2014 quality-profiling"],"validation-rules":["Signature Data Profiling (Signature Edition) \u2014 validation-rules","Signature Validity Rules (Signature Edition) \u2014 validation-rules","Signature Timeliness Rules (Signature Edition) \u2014 validation-rules","Signature dbt Tests (Signature Edition) \u2014 validation-rules","Signature SLA/SLO for Data (Signature Edition) \u2014 validation-rules","Signature Root Cause Analysis (Signature Edition) \u2014 validation-rules","Signature Reference Data Management (Signature Edition) \u2014 validation-rules","Signature The DQ Playbook (Signature Edition) \u2014 validation-rules","Signature Outlier Treatment (Signature Edition) \u2014 validation-rules","Signature Pipeline Data Tests (Signature Edition) \u2014 validation-rules","Signature DQ in ML Pipelines (Signature Edition) \u2014 validation-rules"],"quality-monitoring":["Signature Completeness Rules (Signature Edition) \u2014 quality-monitoring","Signature Consistency Rules (Signature Edition) \u2014 quality-monitoring","Signature Schema Validation (Signature Edition) \u2014 quality-monitoring","Signature Anomaly Detection (Signature Edition) \u2014 quality-monitoring","Signature Data Contracts (Signature Edition) \u2014 quality-monitoring","Signature Data Lineage (Signature Edition) \u2014 quality-monitoring","Signature Data Quality Roles (Signature Edition) \u2014 quality-monitoring","Signature Null Handling Rules (Signature Edition) \u2014 quality-monitoring","Signature Standardization Rules (Signature Edition) \u2014 quality-monitoring","Signature Backfill Quality (Signature Edition) \u2014 quality-monitoring","Signature Data Quality Scorecards (Signature Edition) \u2014 quality-monitoring"]};
var KINDS="data-engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Quality Rules Signature Database — generated study\n"
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
   + "    print('kind: data-engineering record')\n"
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
    standards:['data-engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Data Quality Rules Signature Database.',
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
var gen={version:'jahdb-data-quality-rules-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-quality-rules-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
