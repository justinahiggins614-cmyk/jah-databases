(function(){'use strict';
/* JAH The Child Health Appointment Preparation Database generator — jahdb-child-health-appointment-preparation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHAP-";
var FIELDS=["visit-preparation","pediatric-visit-types","follow-through"];
var TOPICS={"visit-preparation":["Well-Child Visit Schedule \u2014 visit-preparation","Preparing Kids Emotionally \u2014 visit-preparation","Developmental Screening \u2014 visit-preparation","Allergy Appointment Prep \u2014 visit-preparation","Vision and Hearing Screens \u2014 visit-preparation","Fever: When to Worry \u2014 visit-preparation","Mental Health Screening Visits \u2014 visit-preparation","Second Opinions for Kids \u2014 visit-preparation","Hospital Stay with Kids \u2014 visit-preparation","Teen Confidentiality \u2014 visit-preparation","After-Visit Action List \u2014 visit-preparation","Dental Visit Preparation \u2014 visit-preparation"],"pediatric-visit-types":["The Pre-Visit Question List \u2014 pediatric-visit-types","Vaccination Visit Prep \u2014 pediatric-visit-types","ADHD Evaluation Prep \u2014 pediatric-visit-types","Dermatology for Kids \u2014 pediatric-visit-types","Specialist Referral Prep \u2014 pediatric-visit-types","Medication Dosing for Kids \u2014 pediatric-visit-types","Eating Concern Appointments \u2014 pediatric-visit-types","Coordinating Multiple Specialists \u2014 pediatric-visit-types","Surgery Day Prep \u2014 pediatric-visit-types","Transition to Adult Care \u2014 pediatric-visit-types","When to Switch Pediatricians \u2014 pediatric-visit-types"],"follow-through":["Symptom Timeline for Kids \u2014 follow-through","Newborn First Visits \u2014 follow-through","Asthma Visit Prep \u2014 follow-through","Orthodontic Consult Prep \u2014 follow-through","ER vs Urgent Care vs Pediatrician \u2014 follow-through","Chronic Condition School Plans \u2014 follow-through","Sleep Issue Visits \u2014 follow-through","Insurance Authorization Prep \u2014 follow-through","Follow-Up Compliance \u2014 follow-through","The Child Health Binder \u2014 follow-through","The Annual Child Health Review \u2014 follow-through"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Child Health Appointment Preparation Database — generated study\n"
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
    provenance:'Generated structural sample for the The Child Health Appointment Preparation Database.',
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
var gen={version:'jahdb-child-health-appointment-preparation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('child-health-appointment-preparation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
