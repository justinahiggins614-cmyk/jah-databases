(function(){'use strict';
/* JAH The Knowledge Transfer at Work Signature Database generator — jahdb-knowledge-transfer-at-work-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KTW-";
var FIELDS=["knowledge-capture","transfer-methods","knowledge-systems"];
var TOPICS={"knowledge-capture":["Signature The Bus Factor Audit (Signature Edition) \u2014 knowledge-capture","Signature Shadowing Programs (Signature Edition) \u2014 knowledge-capture","Signature Recording Walkthrough Videos (Signature Edition) \u2014 knowledge-capture","Signature Post-Project Knowledge Capture (Signature Edition) \u2014 knowledge-capture","Signature Expert Interviews (Knowledge Harvest) (Signature Edition) \u2014 knowledge-capture","Signature Onboarding Knowledge Paths (Signature Edition) \u2014 knowledge-capture","Signature Knowledge Retention Interviews (Signature Edition) \u2014 knowledge-capture","Signature Pairing for Transfer (Signature Edition) \u2014 knowledge-capture","Signature Succession Knowledge Packets (Signature Edition) \u2014 knowledge-capture","Signature The Corporate Memory Map (Signature Edition) \u2014 knowledge-capture","Signature The Knowledge Transfer Calendar (Signature Edition) \u2014 knowledge-capture","Signature The Knowledge Handover Checklist (Signature Edition) \u2014 knowledge-capture"],"transfer-methods":["Signature Exit Knowledge Transfer Plan (Signature Edition) \u2014 transfer-methods","Signature Lunch-and-Learn Series (Signature Edition) \u2014 transfer-methods","Signature Mentoring for Transfer (Signature Edition) \u2014 transfer-methods","Signature The 'How We Do X' Playbook (Signature Edition) \u2014 transfer-methods","Signature Decision Logs (Signature Edition) \u2014 transfer-methods","Signature Tacit Knowledge Elicitation (Signature Edition) \u2014 transfer-methods","Signature FAQ Cultivation (Signature Edition) \u2014 transfer-methods","Signature Documentation Sprints (Signature Edition) \u2014 transfer-methods","Signature Learning From Departures (Signature Edition) \u2014 transfer-methods","Signature Transfer Metrics (Signature Edition) \u2014 transfer-methods","Signature AI-Assisted Knowledge Capture (Signature Edition) \u2014 transfer-methods"],"knowledge-systems":["Signature Process Documentation Templates (Signature Edition) \u2014 knowledge-systems","Signature The Team Wiki That Lives (Signature Edition) \u2014 knowledge-systems","Signature Communities of Practice (Signature Edition) \u2014 knowledge-systems","Signature Cross-Training Rotations (Signature Edition) \u2014 knowledge-systems","Signature Code and Work Handover Standards (Signature Edition) \u2014 knowledge-systems","Signature The Second-in-Command System (Signature Edition) \u2014 knowledge-systems","Signature Brown-Bag Demos (Signature Edition) \u2014 knowledge-systems","Signature The 'Hit by a Bus' Drill (Signature Edition) \u2014 knowledge-systems","Signature Knowledge-Sharing Incentives (Signature Edition) \u2014 knowledge-systems","Signature Storytelling for Culture Transfer (Signature Edition) \u2014 knowledge-systems","Signature The Transfer-Ready Team (Signature Edition) \u2014 knowledge-systems"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Knowledge Transfer at Work Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Knowledge Transfer at Work Signature Database.',
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
var gen={version:'jahdb-knowledge-transfer-at-work-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('knowledge-transfer-at-work-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
