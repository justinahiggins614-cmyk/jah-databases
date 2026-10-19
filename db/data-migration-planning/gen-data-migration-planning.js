(function(){'use strict';
/* JAH The Data Migration Planning Database generator — jahdb-data-migration-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DMP-";
var FIELDS=["migration-assessment","mapping-and-testing","cutover-execution"];
var TOPICS={"migration-assessment":["Migration Strategy Choice \u2014 migration-assessment","Target System Prep \u2014 migration-assessment","Migration Tooling \u2014 migration-assessment","Downtime Planning \u2014 migration-assessment","Delta Migrations \u2014 migration-assessment","Legacy Decommission \u2014 migration-assessment","Email Migrations \u2014 migration-assessment","Application Data Migration \u2014 migration-assessment","Risk Management \u2014 migration-assessment","Small Business Migrations \u2014 migration-assessment","The Migration Checklist \u2014 migration-assessment","Migration Runbook \u2014 migration-assessment"],"mapping-and-testing":["Data Inventory \u2014 mapping-and-testing","Data Mapping \u2014 mapping-and-testing","Test Migrations \u2014 mapping-and-testing","Rollback Planning \u2014 mapping-and-testing","User Training (New System) \u2014 mapping-and-testing","Data Archiving Strategy \u2014 mapping-and-testing","Database Migrations \u2014 mapping-and-testing","Migration Project Management \u2014 mapping-and-testing","Performance Baselines \u2014 mapping-and-testing","Migration Budgeting \u2014 mapping-and-testing","Data Quality Gates \u2014 mapping-and-testing"],"cutover-execution":["Source System Analysis \u2014 cutover-execution","Data Cleansing \u2014 cutover-execution","Validation Rules \u2014 cutover-execution","Cutover Execution \u2014 cutover-execution","Post-Migration Validation \u2014 cutover-execution","Cloud Migrations \u2014 cutover-execution","File Share Migrations \u2014 cutover-execution","Stakeholder Communication \u2014 cutover-execution","Security During Migration \u2014 cutover-execution","Lessons Learned \u2014 cutover-execution","Parallel Run Strategy \u2014 cutover-execution"]};
var KINDS="software and IT-support record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Migration Planning Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['software and IT-support record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Data Migration Planning Database.',
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
var gen={version:'jahdb-data-migration-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-migration-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
