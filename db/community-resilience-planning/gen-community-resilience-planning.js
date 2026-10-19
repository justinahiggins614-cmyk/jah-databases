(function(){'use strict';
/* JAH The Community Resilience Planning Database generator — jahdb-community-resilience-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRP-";
var FIELDS=["preparedness-planning","mutual-aid-systems","recovery-coordination"];
var TOPICS={"preparedness-planning":["What Is Resilience \u2014 preparedness-planning","The Resilience Playbook \u2014 preparedness-planning","Community Emergency Teams \u2014 preparedness-planning","Community Hubs \u2014 preparedness-planning","School Resilience \u2014 preparedness-planning","Food Security Networks \u2014 preparedness-planning","Cooling Centers \u2014 preparedness-planning","Firewise Communities \u2014 preparedness-planning","Hurricane Prep \u2014 preparedness-planning","Donations Management \u2014 preparedness-planning","Funding Resilience \u2014 preparedness-planning","Annual Resilience Review \u2014 preparedness-planning"],"mutual-aid-systems":["Hazard Assessment \u2014 mutual-aid-systems","Neighborhood Mapping \u2014 mutual-aid-systems","Mutual Aid Networks \u2014 mutual-aid-systems","Faith Community Roles \u2014 mutual-aid-systems","Elder Check-Ins \u2014 mutual-aid-systems","Water Resilience \u2014 mutual-aid-systems","Warming Centers \u2014 mutual-aid-systems","Earthquake Prep \u2014 mutual-aid-systems","Drills and Exercises \u2014 mutual-aid-systems","Volunteer Coordination \u2014 mutual-aid-systems","Youth Engagement \u2014 mutual-aid-systems"],"recovery-coordination":["Vulnerability Mapping \u2014 recovery-coordination","Communication Trees \u2014 recovery-coordination","Supply Caches \u2014 recovery-coordination","Business Continuity (Community) \u2014 recovery-coordination","Pet Preparedness \u2014 recovery-coordination","Energy Resilience \u2014 recovery-coordination","Flood Community Prep \u2014 recovery-coordination","Tornado Prep \u2014 recovery-coordination","Recovery Coordination \u2014 recovery-coordination","Mental Health (Community) \u2014 recovery-coordination","The Resilient Neighborhood \u2014 recovery-coordination"]};
var KINDS="security and resilience record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Community Resilience Planning Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['security and resilience record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Community Resilience Planning Database.',
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
var gen={version:'jahdb-community-resilience-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-resilience-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
