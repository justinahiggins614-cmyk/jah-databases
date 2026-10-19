(function(){'use strict';
/* JAH The Medical Record Organization Database generator — jahdb-medical-record-organization-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MRO-";
var FIELDS=["record-systems","care-coordination","health-tracking"];
var TOPICS={"record-systems":["Personal Health Record Setup \u2014 record-systems","Imaging Disc Management \u2014 record-systems","Family History Tree \u2014 record-systems","Blood Pressure Log \u2014 record-systems","Care Team Contact Sheet \u2014 record-systems","Referral Tracking \u2014 record-systems","Hospital Stay Log \u2014 record-systems","Pediatric Records \u2014 record-systems","Dental Records \u2014 record-systems","Genetic Test Results \u2014 record-systems","Patient Portal Management \u2014 record-systems","Travel Health File \u2014 record-systems"],"care-coordination":["The One-Page Health Summary \u2014 care-coordination","Vaccination Records \u2014 care-coordination","Allergy and Reaction Log \u2014 care-coordination","Blood Sugar Log \u2014 care-coordination","Visit Prep Sheet \u2014 care-coordination","Second Opinion Records \u2014 care-coordination","Discharge Plan Management \u2014 care-coordination","Elder Parent Records \u2014 care-coordination","Vision Records \u2014 care-coordination","Advance Directive Storage \u2014 care-coordination","Correcting Record Errors \u2014 care-coordination"],"health-tracking":["Test Result Filing \u2014 health-tracking","Surgical History Log \u2014 health-tracking","Symptom Diary Method \u2014 health-tracking","Weight Trend Tracking \u2014 health-tracking","After-Visit Summary Filing \u2014 health-tracking","Emergency Room Packet \u2014 health-tracking","Chronic Condition Binder \u2014 health-tracking","Mental Health Records \u2014 health-tracking","Lab Trend Spreadsheets \u2014 health-tracking","Insurance and Billing File \u2014 health-tracking","The Annual Records Review \u2014 health-tracking"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Medical Record Organization Database — generated study\n"
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
   + "    print('kind: health-information record')\n"
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
    standards:['health-information record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Medical Record Organization Database.',
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
var gen={version:'jahdb-medical-record-organization-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('medical-record-organization',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
