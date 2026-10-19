(function(){'use strict';
/* JAH The Child Health Appointment Preparation Signature Database generator — jahdb-child-health-appointment-preparation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHAP-";
var FIELDS=["visit-preparation","pediatric-visit-types","follow-through"];
var TOPICS={"visit-preparation":["Signature Well-Child Visit Schedule (Signature Edition) \u2014 visit-preparation","Signature Preparing Kids Emotionally (Signature Edition) \u2014 visit-preparation","Signature Developmental Screening (Signature Edition) \u2014 visit-preparation","Signature Allergy Appointment Prep (Signature Edition) \u2014 visit-preparation","Signature Vision and Hearing Screens (Signature Edition) \u2014 visit-preparation","Signature Fever: When to Worry (Signature Edition) \u2014 visit-preparation","Signature Mental Health Screening Visits (Signature Edition) \u2014 visit-preparation","Signature Second Opinions for Kids (Signature Edition) \u2014 visit-preparation","Signature Hospital Stay with Kids (Signature Edition) \u2014 visit-preparation","Signature Teen Confidentiality (Signature Edition) \u2014 visit-preparation","Signature After-Visit Action List (Signature Edition) \u2014 visit-preparation","Signature Dental Visit Preparation (Signature Edition) \u2014 visit-preparation"],"pediatric-visit-types":["Signature The Pre-Visit Question List (Signature Edition) \u2014 pediatric-visit-types","Signature Vaccination Visit Prep (Signature Edition) \u2014 pediatric-visit-types","Signature ADHD Evaluation Prep (Signature Edition) \u2014 pediatric-visit-types","Signature Dermatology for Kids (Signature Edition) \u2014 pediatric-visit-types","Signature Specialist Referral Prep (Signature Edition) \u2014 pediatric-visit-types","Signature Medication Dosing for Kids (Signature Edition) \u2014 pediatric-visit-types","Signature Eating Concern Appointments (Signature Edition) \u2014 pediatric-visit-types","Signature Coordinating Multiple Specialists (Signature Edition) \u2014 pediatric-visit-types","Signature Surgery Day Prep (Signature Edition) \u2014 pediatric-visit-types","Signature Transition to Adult Care (Signature Edition) \u2014 pediatric-visit-types","Signature When to Switch Pediatricians (Signature Edition) \u2014 pediatric-visit-types"],"follow-through":["Signature Symptom Timeline for Kids (Signature Edition) \u2014 follow-through","Signature Newborn First Visits (Signature Edition) \u2014 follow-through","Signature Asthma Visit Prep (Signature Edition) \u2014 follow-through","Signature Orthodontic Consult Prep (Signature Edition) \u2014 follow-through","Signature ER vs Urgent Care vs Pediatrician (Signature Edition) \u2014 follow-through","Signature Chronic Condition School Plans (Signature Edition) \u2014 follow-through","Signature Sleep Issue Visits (Signature Edition) \u2014 follow-through","Signature Insurance Authorization Prep (Signature Edition) \u2014 follow-through","Signature Follow-Up Compliance (Signature Edition) \u2014 follow-through","Signature The Child Health Binder (Signature Edition) \u2014 follow-through","Signature The Annual Child Health Review (Signature Edition) \u2014 follow-through"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Child Health Appointment Preparation Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['health-information record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Child Health Appointment Preparation Signature Database.',
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
var gen={version:'jahdb-child-health-appointment-preparation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('child-health-appointment-preparation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
