(function(){'use strict';
/* JAH The Socratic Tutoring Methods Signature Database generator — jahdb-socratic-tutoring-methods-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STM-";
var FIELDS=["questioning-techniques","dialogue-structures","tutoring-sessions"];
var TOPICS={"questioning-techniques":["Signature The Elenchus (Refutation) (Signature Edition) \u2014 questioning-techniques","Signature Probing Assumptions (Signature Edition) \u2014 questioning-techniques","Signature Probing Implications (Signature Edition) \u2014 questioning-techniques","Signature Think-Pair-Share (Signature Edition) \u2014 questioning-techniques","Signature The Funnel vs Focusing (Signature Edition) \u2014 questioning-techniques","Signature Diagnosing Misconceptions (Signature Edition) \u2014 questioning-techniques","Signature Counterexample Technique (Signature Edition) \u2014 questioning-techniques","Signature Socratic Tutoring for Math (Signature Edition) \u2014 questioning-techniques","Signature Handling 'I Don't Know' (Signature Edition) \u2014 questioning-techniques","Signature Group Tutoring Socratically (Signature Edition) \u2014 questioning-techniques","Signature The Tutor's Question Bank (Signature Edition) \u2014 questioning-techniques","Signature The Session Close (Signature Edition) \u2014 questioning-techniques"],"dialogue-structures":["Signature Maieutics (Midwifery of Ideas) (Signature Edition) \u2014 dialogue-structures","Signature Probing Reasons and Evidence (Signature Edition) \u2014 dialogue-structures","Signature Questioning the Question (Signature Edition) \u2014 dialogue-structures","Signature Cold Calling Done Right (Signature Edition) \u2014 dialogue-structures","Signature Socratic Seminar Setup (Signature Edition) \u2014 dialogue-structures","Signature Scaffolding Questions (Signature Edition) \u2014 dialogue-structures","Signature Analogical Questioning (Signature Edition) \u2014 dialogue-structures","Signature Socratic Tutoring for Writing (Signature Edition) \u2014 dialogue-structures","Signature Praise in Socratic Tutoring (Signature Edition) \u2014 dialogue-structures","Signature Online Socratic Tutoring (Signature Edition) \u2014 dialogue-structures","Signature Socratic Method Limits (Signature Edition) \u2014 dialogue-structures"],"tutoring-sessions":["Signature Clarifying Questions (Signature Edition) \u2014 tutoring-sessions","Signature Questioning Viewpoints (Signature Edition) \u2014 tutoring-sessions","Signature The Harkness Discussion (Signature Edition) \u2014 tutoring-sessions","Signature Wait Time Practice (Signature Edition) \u2014 tutoring-sessions","Signature One-on-One Tutoring Arc (Signature Edition) \u2014 tutoring-sessions","Signature The 'Why' Chain (Signature Edition) \u2014 tutoring-sessions","Signature Devil's Advocate in Tutoring (Signature Edition) \u2014 tutoring-sessions","Signature Socratic Tutoring for Science (Signature Edition) \u2014 tutoring-sessions","Signature Session Notes for Tutors (Signature Edition) \u2014 tutoring-sessions","Signature Measuring Tutoring Effectiveness (Signature Edition) \u2014 tutoring-sessions","Signature Training New Socratic Tutors (Signature Edition) \u2014 tutoring-sessions"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Socratic Tutoring Methods Signature Database — generated study\n"
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
   + "    print('kind: education and learning record')\n"
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
    standards:['education and learning record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Socratic Tutoring Methods Signature Database.',
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
var gen={version:'jahdb-socratic-tutoring-methods-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('socratic-tutoring-methods-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
