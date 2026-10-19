(function(){'use strict';
/* JAH The Habit Development Database generator — jahdb-habit-development-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HD-";
var FIELDS=["habit-formation-methods","behavior-tracking-systems","habit-recovery-tools"];
var TOPICS={"habit-formation-methods":["Habit Stacking \u2014 habit-formation-methods","Habit Tracking (Don't Break the Chain) \u2014 habit-formation-methods","The Seinfeld Strategy (Advanced Chains) \u2014 habit-formation-methods","Identity-Based Habits \u2014 habit-formation-methods","Habit Replacement (Not Elimination) \u2014 habit-formation-methods","Morning Routine Architecture \u2014 habit-formation-methods","Habit Contracts \u2014 habit-formation-methods","Breaking Bad Habits (Inversion) \u2014 habit-formation-methods","Meditation Habit Ladder \u2014 habit-formation-methods","The 5-Minute Journal Habit \u2014 habit-formation-methods","The Fresh Start Effect \u2014 habit-formation-methods","Habit Troubleshooting Matrix \u2014 habit-formation-methods"],"behavior-tracking-systems":["The Two-Minute Rule \u2014 behavior-tracking-systems","Environment Design for Habits \u2014 behavior-tracking-systems","Friction Auditing \u2014 behavior-tracking-systems","The 21/90 Myth Correction \u2014 behavior-tracking-systems","Social Accountability Systems \u2014 behavior-tracking-systems","Evening Shutdown Ritual \u2014 behavior-tracking-systems","The Paperclip Method \u2014 behavior-tracking-systems","The Two-Day Rule for Exercise \u2014 behavior-tracking-systems","Savings Habit Automation \u2014 behavior-tracking-systems","Habit Relapse Protocol \u2014 behavior-tracking-systems","Habit Maintenance Mode \u2014 behavior-tracking-systems"],"habit-recovery-tools":["Implementation Intentions \u2014 habit-recovery-tools","Temptation Bundling \u2014 habit-recovery-tools","Habit Shaping (Successive Approximation) \u2014 habit-recovery-tools","Cue-Routine-Reward Loop \u2014 habit-recovery-tools","The Never-Miss-Twice Rule \u2014 habit-recovery-tools","Weekly Review for Habits \u2014 habit-recovery-tools","Habit Pairing for Couples/Families \u2014 habit-recovery-tools","Reading Habit Systems \u2014 habit-recovery-tools","Digital Sunset Habit \u2014 habit-recovery-tools","Keystone Habits \u2014 habit-recovery-tools","The Aggregation of Marginal Gains \u2014 habit-recovery-tools"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Habit Development Database — generated study\n"
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
   + "    print('kind: everyday problem-solving record')\n"
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
    standards:['everyday problem-solving record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Habit Development Database.',
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
var gen={version:'jahdb-habit-development-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('habit-development',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
