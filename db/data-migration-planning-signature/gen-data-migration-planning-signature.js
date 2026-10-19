(function(){'use strict';
/* JAH The Data Migration Planning Signature Database generator — jahdb-data-migration-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DMP-";
var FIELDS=["migration-assessment","mapping-and-testing","cutover-execution"];
var TOPICS={"migration-assessment":["Signature Migration Strategy Choice (Signature Edition) \u2014 migration-assessment","Signature Target System Prep (Signature Edition) \u2014 migration-assessment","Signature Migration Tooling (Signature Edition) \u2014 migration-assessment","Signature Downtime Planning (Signature Edition) \u2014 migration-assessment","Signature Delta Migrations (Signature Edition) \u2014 migration-assessment","Signature Legacy Decommission (Signature Edition) \u2014 migration-assessment","Signature Email Migrations (Signature Edition) \u2014 migration-assessment","Signature Application Data Migration (Signature Edition) \u2014 migration-assessment","Signature Risk Management (Signature Edition) \u2014 migration-assessment","Signature Small Business Migrations (Signature Edition) \u2014 migration-assessment","Signature The Migration Checklist (Signature Edition) \u2014 migration-assessment","Signature Migration Runbook (Signature Edition) \u2014 migration-assessment"],"mapping-and-testing":["Signature Data Inventory (Signature Edition) \u2014 mapping-and-testing","Signature Data Mapping (Signature Edition) \u2014 mapping-and-testing","Signature Test Migrations (Signature Edition) \u2014 mapping-and-testing","Signature Rollback Planning (Signature Edition) \u2014 mapping-and-testing","Signature User Training (New System) (Signature Edition) \u2014 mapping-and-testing","Signature Data Archiving Strategy (Signature Edition) \u2014 mapping-and-testing","Signature Database Migrations (Signature Edition) \u2014 mapping-and-testing","Signature Migration Project Management (Signature Edition) \u2014 mapping-and-testing","Signature Performance Baselines (Signature Edition) \u2014 mapping-and-testing","Signature Migration Budgeting (Signature Edition) \u2014 mapping-and-testing","Signature Data Quality Gates (Signature Edition) \u2014 mapping-and-testing"],"cutover-execution":["Signature Source System Analysis (Signature Edition) \u2014 cutover-execution","Signature Data Cleansing (Signature Edition) \u2014 cutover-execution","Signature Validation Rules (Signature Edition) \u2014 cutover-execution","Signature Cutover Execution (Signature Edition) \u2014 cutover-execution","Signature Post-Migration Validation (Signature Edition) \u2014 cutover-execution","Signature Cloud Migrations (Signature Edition) \u2014 cutover-execution","Signature File Share Migrations (Signature Edition) \u2014 cutover-execution","Signature Stakeholder Communication (Signature Edition) \u2014 cutover-execution","Signature Security During Migration (Signature Edition) \u2014 cutover-execution","Signature Lessons Learned (Signature Edition) \u2014 cutover-execution","Signature Parallel Run Strategy (Signature Edition) \u2014 cutover-execution"]};
var KINDS="software and IT-support record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Migration Planning Signature Database — generated study\n"
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
   + "    print('kind: software and IT-support record')\n"
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
    standards:['software and IT-support record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Data Migration Planning Signature Database.',
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
var gen={version:'jahdb-data-migration-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-migration-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
