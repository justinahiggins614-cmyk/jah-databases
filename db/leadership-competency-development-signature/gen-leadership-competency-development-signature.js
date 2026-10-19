(function(){'use strict';
/* JAH The Leadership Competency Development Signature Database generator — jahdb-leadership-competency-development-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LCD-";
var FIELDS=["core-competencies","leadership-practices","leadership-assessment"];
var TOPICS={"core-competencies":["Signature The 5 Core Leadership Competencies (Signature Edition) \u2014 core-competencies","Signature Receiving Feedback Like a Leader (Signature Edition) \u2014 core-competencies","Signature Setting Clear Expectations (Signature Edition) \u2014 core-competencies","Signature Building Psychological Safety (Signature Edition) \u2014 core-competencies","Signature Leading Through Change (Signature Edition) \u2014 core-competencies","Signature Firing Fairly (Signature Edition) \u2014 core-competencies","Signature Succession Planning (Signature Edition) \u2014 core-competencies","Signature Executive Presence (Signature Edition) \u2014 core-competencies","Signature Time Management for Leaders (Signature Edition) \u2014 core-competencies","Signature Difficult Conversations Cadence (Signature Edition) \u2014 core-competencies","Signature Leading in Crisis (Signature Edition) \u2014 core-competencies","Signature Your Leadership Development Plan (Signature Edition) \u2014 core-competencies"],"leadership-practices":["Signature Situational Leadership (Signature Edition) \u2014 leadership-practices","Signature Delegation That Develops (Signature Edition) \u2014 leadership-practices","Signature Accountability Without Micromanagement (Signature Edition) \u2014 leadership-practices","Signature Trust-Building Behaviors (Signature Edition) \u2014 leadership-practices","Signature Conflict Resolution for Leaders (Signature Edition) \u2014 leadership-practices","Signature Performance Reviews That Work (Signature Edition) \u2014 leadership-practices","Signature Leading Remote Teams (Signature Edition) \u2014 leadership-practices","Signature Strategic Thinking (Signature Edition) \u2014 leadership-practices","Signature Leading Up (Managing Your Boss) (Signature Edition) \u2014 leadership-practices","Signature Leadership Self-Assessment (Signature Edition) \u2014 leadership-practices","Signature Ethical Leadership (Signature Edition) \u2014 leadership-practices"],"leadership-assessment":["Signature Giving Hard Feedback (Signature Edition) \u2014 leadership-assessment","Signature Running Effective 1:1s (Signature Edition) \u2014 leadership-assessment","Signature Coaching vs Directing (Signature Edition) \u2014 leadership-assessment","Signature Decision-Making as a Leader (Signature Edition) \u2014 leadership-assessment","Signature Hiring Well (Signature Edition) \u2014 leadership-assessment","Signature Developing High Potentials (Signature Edition) \u2014 leadership-assessment","Signature Influence Without Authority (Signature Edition) \u2014 leadership-assessment","Signature Financial Literacy for Leaders (Signature Edition) \u2014 leadership-assessment","Signature Building Team Culture (Signature Edition) \u2014 leadership-assessment","Signature Mentoring Others (Signature Edition) \u2014 leadership-assessment","Signature The Leadership Reading List (Signature Edition) \u2014 leadership-assessment"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Leadership Competency Development Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['employment and workplace record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Leadership Competency Development Signature Database.',
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
var gen={version:'jahdb-leadership-competency-development-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('leadership-competency-development-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
