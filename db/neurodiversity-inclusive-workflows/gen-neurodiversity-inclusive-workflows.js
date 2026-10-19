(function(){'use strict';
/* JAH The Neurodiversity-Inclusive Workflows Database generator — jahdb-neurodiversity-inclusive-workflows-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NIW-";
var FIELDS=["inclusive-process-design","accommodation-systems","strength-based-workflows"];
var TOPICS={"inclusive-process-design":["Neurodiversity Basics \u2014 inclusive-process-design","ADHD-Friendly Task Design \u2014 inclusive-process-design","Sensory-Friendly Spaces \u2014 inclusive-process-design","Written Instructions \u2014 inclusive-process-design","Interview Accommodations \u2014 inclusive-process-design","Disclosure Decisions \u2014 inclusive-process-design","Async-First Workflows \u2014 inclusive-process-design","Lighting Adjustments \u2014 inclusive-process-design","Remote Work Benefits \u2014 inclusive-process-design","Executive Function Support \u2014 inclusive-process-design","Measuring Inclusion \u2014 inclusive-process-design","Policy Templates \u2014 inclusive-process-design"],"accommodation-systems":["Universal Design for Work \u2014 accommodation-systems","Autism-Friendly Communication \u2014 accommodation-systems","Flexible Scheduling \u2014 accommodation-systems","Reducing Ambiguity \u2014 accommodation-systems","Onboarding Redesign \u2014 accommodation-systems","Manager Training \u2014 accommodation-systems","Focus Time Protection \u2014 accommodation-systems","Stimming Acceptance \u2014 accommodation-systems","Assistive Tech \u2014 accommodation-systems","Burnout Prevention \u2014 accommodation-systems","The ND Workplace Audit \u2014 accommodation-systems"],"strength-based-workflows":["The Inclusive Playbook \u2014 strength-based-workflows","Dyslexia-Friendly Documents \u2014 strength-based-workflows","Meeting Redesign \u2014 strength-based-workflows","Strength-Based Roles \u2014 strength-based-workflows","Performance Reviews \u2014 strength-based-workflows","Quiet Hiring Practices \u2014 strength-based-workflows","Noise Management \u2014 strength-based-workflows","Social Expectations \u2014 strength-based-workflows","Time Blindness Aids \u2014 strength-based-workflows","Employee Resource Groups \u2014 strength-based-workflows","Celebrating Neurodiversity \u2014 strength-based-workflows"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Neurodiversity-Inclusive Workflows Database — generated study\n"
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
   + "    print('kind: accessibility record')\n"
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
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Neurodiversity-Inclusive Workflows Database.',
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
var gen={version:'jahdb-neurodiversity-inclusive-workflows-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('neurodiversity-inclusive-workflows',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
