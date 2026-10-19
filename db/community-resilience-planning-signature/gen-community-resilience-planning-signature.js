(function(){'use strict';
/* JAH The Community Resilience Planning Signature Database generator — jahdb-community-resilience-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRP-";
var FIELDS=["preparedness-planning","mutual-aid-systems","recovery-coordination"];
var TOPICS={"preparedness-planning":["Signature What Is Resilience (Signature Edition) \u2014 preparedness-planning","Signature The Resilience Playbook (Signature Edition) \u2014 preparedness-planning","Signature Community Emergency Teams (Signature Edition) \u2014 preparedness-planning","Signature Community Hubs (Signature Edition) \u2014 preparedness-planning","Signature School Resilience (Signature Edition) \u2014 preparedness-planning","Signature Food Security Networks (Signature Edition) \u2014 preparedness-planning","Signature Cooling Centers (Signature Edition) \u2014 preparedness-planning","Signature Firewise Communities (Signature Edition) \u2014 preparedness-planning","Signature Hurricane Prep (Signature Edition) \u2014 preparedness-planning","Signature Donations Management (Signature Edition) \u2014 preparedness-planning","Signature Funding Resilience (Signature Edition) \u2014 preparedness-planning","Signature Annual Resilience Review (Signature Edition) \u2014 preparedness-planning"],"mutual-aid-systems":["Signature Hazard Assessment (Signature Edition) \u2014 mutual-aid-systems","Signature Neighborhood Mapping (Signature Edition) \u2014 mutual-aid-systems","Signature Mutual Aid Networks (Signature Edition) \u2014 mutual-aid-systems","Signature Faith Community Roles (Signature Edition) \u2014 mutual-aid-systems","Signature Elder Check-Ins (Signature Edition) \u2014 mutual-aid-systems","Signature Water Resilience (Signature Edition) \u2014 mutual-aid-systems","Signature Warming Centers (Signature Edition) \u2014 mutual-aid-systems","Signature Earthquake Prep (Signature Edition) \u2014 mutual-aid-systems","Signature Drills and Exercises (Signature Edition) \u2014 mutual-aid-systems","Signature Volunteer Coordination (Signature Edition) \u2014 mutual-aid-systems","Signature Youth Engagement (Signature Edition) \u2014 mutual-aid-systems"],"recovery-coordination":["Signature Vulnerability Mapping (Signature Edition) \u2014 recovery-coordination","Signature Communication Trees (Signature Edition) \u2014 recovery-coordination","Signature Supply Caches (Signature Edition) \u2014 recovery-coordination","Signature Business Continuity (Community) (Signature Edition) \u2014 recovery-coordination","Signature Pet Preparedness (Signature Edition) \u2014 recovery-coordination","Signature Energy Resilience (Signature Edition) \u2014 recovery-coordination","Signature Flood Community Prep (Signature Edition) \u2014 recovery-coordination","Signature Tornado Prep (Signature Edition) \u2014 recovery-coordination","Signature Recovery Coordination (Signature Edition) \u2014 recovery-coordination","Signature Mental Health (Community) (Signature Edition) \u2014 recovery-coordination","Signature The Resilient Neighborhood (Signature Edition) \u2014 recovery-coordination"]};
var KINDS="security and resilience record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Community Resilience Planning Signature Database — generated study\n"
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
   + "    print('kind: security and resilience record')\n"
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
    standards:['security and resilience record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Community Resilience Planning Signature Database.',
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
var gen={version:'jahdb-community-resilience-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-resilience-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
