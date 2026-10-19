(function(){'use strict';
/* JAH The Medication Interaction Questions Database generator — jahdb-medication-interaction-questions-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MIQ-";
var FIELDS=["interaction-awareness","pharmacist-conversations","medication-safety"];
var TOPICS={"interaction-awareness":["The Brown Bag Review \u2014 interaction-awareness","Food-Drug Interactions \u2014 interaction-awareness","The 'Do Not Stop Abruptly' List \u2014 interaction-awareness","Pharmacist Consultations \u2014 interaction-awareness","Medication Timing Optimization \u2014 interaction-awareness","Pregnancy Medication Questions \u2014 interaction-awareness","Opioid Safety Conversations \u2014 interaction-awareness","Blood Pressure Med Adherence \u2014 interaction-awareness","Medication Cost Questions \u2014 interaction-awareness","Herbal-Drug Interaction Screen \u2014 interaction-awareness","The Annual Medication Audit \u2014 interaction-awareness","Medication Allergy Documentation \u2014 interaction-awareness"],"pharmacist-conversations":["Questions for New Prescriptions \u2014 pharmacist-conversations","Supplement Interactions \u2014 pharmacist-conversations","Missed Dose Rules \u2014 pharmacist-conversations","Generic vs Brand \u2014 pharmacist-conversations","Duplicate Therapy Detection \u2014 pharmacist-conversations","Pediatric Dosing Safety \u2014 pharmacist-conversations","Blood Thinner Vigilance \u2014 pharmacist-conversations","Mental Health Med Questions \u2014 pharmacist-conversations","Traveling with Medications \u2014 pharmacist-conversations","Medication Storage Rules \u2014 pharmacist-conversations","Questions for the Specialist \u2014 pharmacist-conversations"],"medication-safety":["Drug-Drug Interactions Basics \u2014 medication-safety","Side Effect Triage \u2014 medication-safety","Medication List Maintenance \u2014 medication-safety","Pill Organizers That Work \u2014 medication-safety","Beers Criteria (Older Adults) \u2014 medication-safety","Antibiotic Stewardship Questions \u2014 medication-safety","Diabetes Medication Questions \u2014 medication-safety","Deprescribing Conversations \u2014 medication-safety","Emergency Medication Info \u2014 medication-safety","Disposal: Take-Back Programs \u2014 medication-safety","When to Get a Second Opinion on Meds \u2014 medication-safety"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Medication Interaction Questions Database — generated study\n"
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
    provenance:'Generated structural sample for the The Medication Interaction Questions Database.',
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
var gen={version:'jahdb-medication-interaction-questions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('medication-interaction-questions',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
