(function(){'use strict';
/* JAH The Leadership Competency Development Database generator — jahdb-leadership-competency-development-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCD-";
var FIELDS=["core-competencies","leadership-practices","leadership-assessment"];
var TOPICS={"core-competencies":["The 5 Core Leadership Competencies \u2014 core-competencies","Receiving Feedback Like a Leader \u2014 core-competencies","Setting Clear Expectations \u2014 core-competencies","Building Psychological Safety \u2014 core-competencies","Leading Through Change \u2014 core-competencies","Firing Fairly \u2014 core-competencies","Succession Planning \u2014 core-competencies","Executive Presence \u2014 core-competencies","Time Management for Leaders \u2014 core-competencies","Difficult Conversations Cadence \u2014 core-competencies","Leading in Crisis \u2014 core-competencies","Your Leadership Development Plan \u2014 core-competencies"],"leadership-practices":["Situational Leadership \u2014 leadership-practices","Delegation That Develops \u2014 leadership-practices","Accountability Without Micromanagement \u2014 leadership-practices","Trust-Building Behaviors \u2014 leadership-practices","Conflict Resolution for Leaders \u2014 leadership-practices","Performance Reviews That Work \u2014 leadership-practices","Leading Remote Teams \u2014 leadership-practices","Strategic Thinking \u2014 leadership-practices","Leading Up (Managing Your Boss) \u2014 leadership-practices","Leadership Self-Assessment \u2014 leadership-practices","Ethical Leadership \u2014 leadership-practices"],"leadership-assessment":["Giving Hard Feedback \u2014 leadership-assessment","Running Effective 1:1s \u2014 leadership-assessment","Coaching vs Directing \u2014 leadership-assessment","Decision-Making as a Leader \u2014 leadership-assessment","Hiring Well \u2014 leadership-assessment","Developing High Potentials \u2014 leadership-assessment","Influence Without Authority \u2014 leadership-assessment","Financial Literacy for Leaders \u2014 leadership-assessment","Building Team Culture \u2014 leadership-assessment","Mentoring Others \u2014 leadership-assessment","The Leadership Reading List \u2014 leadership-assessment"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Leadership Competency Development Database — generated study\n"
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
    provenance:'Generated structural sample for the The Leadership Competency Development Database.',
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
var gen={version:'jahdb-leadership-competency-development-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('leadership-competency-development',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
