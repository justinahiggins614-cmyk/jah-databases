(function(){'use strict';
/* JAH The Knowledge Transfer at Work Database generator — jahdb-knowledge-transfer-at-work-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KTW-";
var FIELDS=["knowledge-capture","transfer-methods","knowledge-systems"];
var TOPICS={"knowledge-capture":["The Bus Factor Audit \u2014 knowledge-capture","Shadowing Programs \u2014 knowledge-capture","Recording Walkthrough Videos \u2014 knowledge-capture","Post-Project Knowledge Capture \u2014 knowledge-capture","Expert Interviews (Knowledge Harvest) \u2014 knowledge-capture","Onboarding Knowledge Paths \u2014 knowledge-capture","Knowledge Retention Interviews \u2014 knowledge-capture","Pairing for Transfer \u2014 knowledge-capture","Succession Knowledge Packets \u2014 knowledge-capture","The Corporate Memory Map \u2014 knowledge-capture","The Knowledge Transfer Calendar \u2014 knowledge-capture","The Knowledge Handover Checklist \u2014 knowledge-capture"],"transfer-methods":["Exit Knowledge Transfer Plan \u2014 transfer-methods","Lunch-and-Learn Series \u2014 transfer-methods","Mentoring for Transfer \u2014 transfer-methods","The 'How We Do X' Playbook \u2014 transfer-methods","Decision Logs \u2014 transfer-methods","Tacit Knowledge Elicitation \u2014 transfer-methods","FAQ Cultivation \u2014 transfer-methods","Documentation Sprints \u2014 transfer-methods","Learning From Departures \u2014 transfer-methods","Transfer Metrics \u2014 transfer-methods","AI-Assisted Knowledge Capture \u2014 transfer-methods"],"knowledge-systems":["Process Documentation Templates \u2014 knowledge-systems","The Team Wiki That Lives \u2014 knowledge-systems","Communities of Practice \u2014 knowledge-systems","Cross-Training Rotations \u2014 knowledge-systems","Code and Work Handover Standards \u2014 knowledge-systems","The Second-in-Command System \u2014 knowledge-systems","Brown-Bag Demos \u2014 knowledge-systems","The 'Hit by a Bus' Drill \u2014 knowledge-systems","Knowledge-Sharing Incentives \u2014 knowledge-systems","Storytelling for Culture Transfer \u2014 knowledge-systems","The Transfer-Ready Team \u2014 knowledge-systems"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Knowledge Transfer at Work Database — generated study\n"
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
    provenance:'Generated structural sample for the The Knowledge Transfer at Work Database.',
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
var gen={version:'jahdb-knowledge-transfer-at-work-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('knowledge-transfer-at-work',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
