(function(){'use strict';
/* JAH The AI Human Handoff Database generator — jahdb-ai-human-handoff-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AHH-";
var FIELDS=["handoff-triggers","context-transfer","human-takeover-design"];
var TOPICS={"handoff-triggers":["Why Handoffs Matter \u2014 handoff-triggers","Context Transfer \u2014 handoff-triggers","Human Response Time \u2014 handoff-triggers","Training Human Operators \u2014 handoff-triggers","Handoff in Chatbots \u2014 handoff-triggers","Handoff in Content Moderation \u2014 handoff-triggers","Measuring Handoff Quality \u2014 handoff-triggers","Graceful Degradation \u2014 handoff-triggers","Continuous Improvement \u2014 handoff-triggers","Cost of Handoffs \u2014 handoff-triggers","Partial Handoffs \u2014 handoff-triggers","Post-Handoff Follow-Up \u2014 handoff-triggers"],"context-transfer":["Handoff Trigger Design \u2014 context-transfer","The Handoff Card \u2014 context-transfer","Takeover Interfaces \u2014 context-transfer","Automation Bias Defense \u2014 context-transfer","Handoff in Autonomous Vehicles \u2014 context-transfer","Escalation Queues \u2014 context-transfer","Failure Mode: Silent Failure \u2014 context-transfer","User Communication \u2014 context-transfer","Multi-AI Handoffs \u2014 context-transfer","The Handoff Playbook \u2014 context-transfer","Handoff in Robotics \u2014 context-transfer"],"human-takeover-design":["Confidence Thresholds \u2014 human-takeover-design","Alert Fatigue Prevention \u2014 human-takeover-design","Shared Mental Models \u2014 human-takeover-design","Liability and Handoffs \u2014 human-takeover-design","Handoff in Healthcare AI \u2014 human-takeover-design","Staffing the Handoff \u2014 human-takeover-design","Failure Mode: Handoff Storm \u2014 human-takeover-design","Handoff Logging \u2014 human-takeover-design","Regulatory View \u2014 human-takeover-design","Handoff Drills \u2014 human-takeover-design","Emotional Handoffs \u2014 human-takeover-design"]};
var KINDS="AI-systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The AI Human Handoff Database — generated study\n"
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
   + "    print('kind: AI-systems record')\n"
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
    standards:['AI-systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The AI Human Handoff Database.',
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
var gen={version:'jahdb-ai-human-handoff-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-human-handoff',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
