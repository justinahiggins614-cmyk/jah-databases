(function(){'use strict';
/* JAH The Meeting Effectiveness Database generator — jahdb-meeting-effectiveness-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ME-";
var FIELDS=["meeting-design","facilitation-methods","meeting-recovery"];
var TOPICS={"meeting-design":["The Meeting Cost Calculator \u2014 meeting-design","The 25-Minute Default \u2014 meeting-design","Pre-Reads That Get Read \u2014 meeting-design","Timeboxing Segments \u2014 meeting-design","Minutes People Read \u2014 meeting-design","Killing Recurring Meetings \u2014 meeting-design","Difficult Meeting Personalities \u2014 meeting-design","The One-on-One Meeting \u2014 meeting-design","Interview Meetings (Panels) \u2014 meeting-design","Board Meeting Preparation \u2014 meeting-design","Post-Meeting Follow-Through \u2014 meeting-design","The Annual Meeting Audit \u2014 meeting-design"],"facilitation-methods":["The Agenda Rule \u2014 facilitation-methods","Standup That Works \u2014 facilitation-methods","Facilitation: Round-Robin \u2014 facilitation-methods","The Last-5-Minutes Close \u2014 facilitation-methods","Virtual Meeting Excellence \u2014 facilitation-methods","The Walking Meeting \u2014 facilitation-methods","Meeting-Free Blocks \u2014 facilitation-methods","Retrospective Meetings \u2014 facilitation-methods","Conflict Resolution Meetings \u2014 facilitation-methods","Meeting Energy Management \u2014 facilitation-methods","Meeting Metrics Dashboard \u2014 facilitation-methods"],"meeting-recovery":["Right-Sizing Attendance \u2014 meeting-recovery","Decision Meetings vs Status Meetings \u2014 meeting-recovery","Parking Lot Discipline \u2014 meeting-recovery","Action Items That Happen \u2014 meeting-recovery","Hybrid Meeting Fairness \u2014 meeting-recovery","Brainstorming That Produces \u2014 meeting-recovery","Async-First Culture \u2014 meeting-recovery","All-Hands That Don't Waste Time \u2014 meeting-recovery","Sales and Client Meetings \u2014 meeting-recovery","The 'Could This Be an Email' Filter \u2014 meeting-recovery","Facilitator Rotation \u2014 meeting-recovery"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Meeting Effectiveness Database — generated study\n"
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
   + "    print('kind: employment and workplace record')\n"
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
    standards:['employment and workplace record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Meeting Effectiveness Database.',
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
var gen={version:'jahdb-meeting-effectiveness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('meeting-effectiveness',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
