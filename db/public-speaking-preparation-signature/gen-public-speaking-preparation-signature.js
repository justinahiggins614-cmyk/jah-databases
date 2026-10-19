(function(){'use strict';
/* JAH The Public Speaking Preparation Signature Database generator — jahdb-public-speaking-preparation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSP-";
var FIELDS=["speech-structure","delivery-skills","anxiety-management"];
var TOPICS={"speech-structure":["Signature Overcoming Stage Fright (Signature Edition) \u2014 speech-structure","Signature The Speaker's Playbook (Signature Edition) \u2014 speech-structure","Signature Storytelling (Signature Edition) \u2014 speech-structure","Signature No-Slide Speaking (Signature Edition) \u2014 speech-structure","Signature Eye Contact (Signature Edition) \u2014 speech-structure","Signature Handling Q&A (Signature Edition) \u2014 speech-structure","Signature Stage Movement (Signature Edition) \u2014 speech-structure","Signature Keynotes (Signature Edition) \u2014 speech-structure","Signature Pitches (Signature Edition) \u2014 speech-structure","Signature Recording Yourself (Signature Edition) \u2014 speech-structure","Signature The Night Before (Signature Edition) \u2014 speech-structure","Signature The Confident Speaker (Signature Edition) \u2014 speech-structure"],"delivery-skills":["Signature Speech Structure (Signature Edition) \u2014 delivery-skills","Signature Knowing Your Audience (Signature Edition) \u2014 delivery-skills","Signature Data in Speeches (Signature Edition) \u2014 delivery-skills","Signature Voice Training (Signature Edition) \u2014 delivery-skills","Signature Pacing (Signature Edition) \u2014 delivery-skills","Signature Hostile Questions (Signature Edition) \u2014 delivery-skills","Signature Virtual Presentations (Signature Edition) \u2014 delivery-skills","Signature Wedding Toasts (Signature Edition) \u2014 delivery-skills","Signature Impromptu Speaking (Signature Edition) \u2014 delivery-skills","Signature Breathing Exercises (Signature Edition) \u2014 delivery-skills","Signature Day-Of Checklist (Signature Edition) \u2014 delivery-skills"],"anxiety-management":["Signature Opening Hooks (Signature Edition) \u2014 anxiety-management","Signature Core Message (Signature Edition) \u2014 anxiety-management","Signature Slide Design (Signature Edition) \u2014 anxiety-management","Signature Body Language (Signature Edition) \u2014 anxiety-management","Signature The Pause (Signature Edition) \u2014 anxiety-management","Signature Microphone Technique (Signature Edition) \u2014 anxiety-management","Signature Panel Discussions (Signature Edition) \u2014 anxiety-management","Signature Eulogies (Signature Edition) \u2014 anxiety-management","Signature Toastmasters (Signature Edition) \u2014 anxiety-management","Signature Visualization (Signature Edition) \u2014 anxiety-management","Signature Speaking Fees (Signature Edition) \u2014 anxiety-management"]};
var KINDS="communication record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Public Speaking Preparation Signature Database — generated study\n"
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
   + "    print('kind: communication record')\n"
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
    standards:['communication record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Public Speaking Preparation Signature Database.',
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
var gen={version:'jahdb-public-speaking-preparation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-speaking-preparation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
