(function(){'use strict';
/* JAH The Neurodiversity-Inclusive Workflows Signature Database generator — jahdb-neurodiversity-inclusive-workflows-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NIW-";
var FIELDS=["inclusive-process-design","accommodation-systems","strength-based-workflows"];
var TOPICS={"inclusive-process-design":["Signature Neurodiversity Basics (Signature Edition) \u2014 inclusive-process-design","Signature ADHD-Friendly Task Design (Signature Edition) \u2014 inclusive-process-design","Signature Sensory-Friendly Spaces (Signature Edition) \u2014 inclusive-process-design","Signature Written Instructions (Signature Edition) \u2014 inclusive-process-design","Signature Interview Accommodations (Signature Edition) \u2014 inclusive-process-design","Signature Disclosure Decisions (Signature Edition) \u2014 inclusive-process-design","Signature Async-First Workflows (Signature Edition) \u2014 inclusive-process-design","Signature Lighting Adjustments (Signature Edition) \u2014 inclusive-process-design","Signature Remote Work Benefits (Signature Edition) \u2014 inclusive-process-design","Signature Executive Function Support (Signature Edition) \u2014 inclusive-process-design","Signature Measuring Inclusion (Signature Edition) \u2014 inclusive-process-design","Signature Policy Templates (Signature Edition) \u2014 inclusive-process-design"],"accommodation-systems":["Signature Universal Design for Work (Signature Edition) \u2014 accommodation-systems","Signature Autism-Friendly Communication (Signature Edition) \u2014 accommodation-systems","Signature Flexible Scheduling (Signature Edition) \u2014 accommodation-systems","Signature Reducing Ambiguity (Signature Edition) \u2014 accommodation-systems","Signature Onboarding Redesign (Signature Edition) \u2014 accommodation-systems","Signature Manager Training (Signature Edition) \u2014 accommodation-systems","Signature Focus Time Protection (Signature Edition) \u2014 accommodation-systems","Signature Stimming Acceptance (Signature Edition) \u2014 accommodation-systems","Signature Assistive Tech (Signature Edition) \u2014 accommodation-systems","Signature Burnout Prevention (Signature Edition) \u2014 accommodation-systems","Signature The ND Workplace Audit (Signature Edition) \u2014 accommodation-systems"],"strength-based-workflows":["Signature The Inclusive Playbook (Signature Edition) \u2014 strength-based-workflows","Signature Dyslexia-Friendly Documents (Signature Edition) \u2014 strength-based-workflows","Signature Meeting Redesign (Signature Edition) \u2014 strength-based-workflows","Signature Strength-Based Roles (Signature Edition) \u2014 strength-based-workflows","Signature Performance Reviews (Signature Edition) \u2014 strength-based-workflows","Signature Quiet Hiring Practices (Signature Edition) \u2014 strength-based-workflows","Signature Noise Management (Signature Edition) \u2014 strength-based-workflows","Signature Social Expectations (Signature Edition) \u2014 strength-based-workflows","Signature Time Blindness Aids (Signature Edition) \u2014 strength-based-workflows","Signature Employee Resource Groups (Signature Edition) \u2014 strength-based-workflows","Signature Celebrating Neurodiversity (Signature Edition) \u2014 strength-based-workflows"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Neurodiversity-Inclusive Workflows Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Neurodiversity-Inclusive Workflows Signature Database.',
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
var gen={version:'jahdb-neurodiversity-inclusive-workflows-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('neurodiversity-inclusive-workflows-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
