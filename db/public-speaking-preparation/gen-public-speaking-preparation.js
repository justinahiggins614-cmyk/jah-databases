(function(){'use strict';
/* JAH The Public Speaking Preparation Database generator — jahdb-public-speaking-preparation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSP-";
var FIELDS=["speech-structure","delivery-skills","anxiety-management"];
var TOPICS={"speech-structure":["Overcoming Stage Fright \u2014 speech-structure","The Speaker's Playbook \u2014 speech-structure","Storytelling \u2014 speech-structure","No-Slide Speaking \u2014 speech-structure","Eye Contact \u2014 speech-structure","Handling Q&A \u2014 speech-structure","Stage Movement \u2014 speech-structure","Keynotes \u2014 speech-structure","Pitches \u2014 speech-structure","Recording Yourself \u2014 speech-structure","The Night Before \u2014 speech-structure","The Confident Speaker \u2014 speech-structure"],"delivery-skills":["Speech Structure \u2014 delivery-skills","Knowing Your Audience \u2014 delivery-skills","Data in Speeches \u2014 delivery-skills","Voice Training \u2014 delivery-skills","Pacing \u2014 delivery-skills","Hostile Questions \u2014 delivery-skills","Virtual Presentations \u2014 delivery-skills","Wedding Toasts \u2014 delivery-skills","Impromptu Speaking \u2014 delivery-skills","Breathing Exercises \u2014 delivery-skills","Day-Of Checklist \u2014 delivery-skills"],"anxiety-management":["Opening Hooks \u2014 anxiety-management","Core Message \u2014 anxiety-management","Slide Design \u2014 anxiety-management","Body Language \u2014 anxiety-management","The Pause \u2014 anxiety-management","Microphone Technique \u2014 anxiety-management","Panel Discussions \u2014 anxiety-management","Eulogies \u2014 anxiety-management","Toastmasters \u2014 anxiety-management","Visualization \u2014 anxiety-management","Speaking Fees \u2014 anxiety-management"]};
var KINDS="communication record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Public Speaking Preparation Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['communication record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Public Speaking Preparation Database.',
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
var gen={version:'jahdb-public-speaking-preparation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-speaking-preparation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
