(function(){'use strict';
/* JAH The Autonomous System Verification Database generator — jahdb-autonomous-system-verification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ASV-";
var FIELDS=["verification-methods","safety-assurance","testing-at-scale"];
var TOPICS={"verification-methods":["Why Autonomy Needs Proof \u2014 verification-methods","The Verification Playbook \u2014 verification-methods","Runtime Verification \u2014 verification-methods","Edge Case Discovery \u2014 verification-methods","Digital Twins \u2014 verification-methods","ODD Monitoring \u2014 verification-methods","Diverse Redundancy \u2014 verification-methods","UL 4600 \u2014 verification-methods","Disengagement Analysis \u2014 verification-methods","OTA Update Safety \u2014 verification-methods","Ethics (Trolley Problems) \u2014 verification-methods","The Verified Autonomous System \u2014 verification-methods"],"safety-assurance":["Safety Cases \u2014 safety-assurance","Model Checking \u2014 safety-assurance","Simulation Testing \u2014 safety-assurance","Fuzz Testing (Autonomy) \u2014 safety-assurance","Hardware-in-the-Loop \u2014 safety-assurance","Minimal Risk Condition \u2014 safety-assurance","SOTIF (ISO 21448) \u2014 safety-assurance","Regulatory Approval \u2014 safety-assurance","Safety Metrics \u2014 safety-assurance","Cybersecurity (Autonomy) \u2014 safety-assurance","Public Trust \u2014 safety-assurance"],"testing-at-scale":["Formal Verification \u2014 testing-at-scale","Theorem Proving \u2014 testing-at-scale","Scenario Libraries \u2014 testing-at-scale","Metamorphic Testing \u2014 testing-at-scale","Operational Design Domain \u2014 testing-at-scale","Redundancy \u2014 testing-at-scale","ISO 26262 (Functional Safety) \u2014 testing-at-scale","Incident Investigation \u2014 testing-at-scale","Continuous Monitoring \u2014 testing-at-scale","Human Factors (Autonomy) \u2014 testing-at-scale","Insurance and Liability \u2014 testing-at-scale"]};
var KINDS="advanced planning and systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Autonomous System Verification Database — generated study\n"
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
   + "    print('kind: advanced planning and systems record')\n"
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
    standards:['advanced planning and systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Autonomous System Verification Database.',
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
var gen={version:'jahdb-autonomous-system-verification-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('autonomous-system-verification',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
