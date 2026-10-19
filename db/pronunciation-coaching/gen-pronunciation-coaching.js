(function(){'use strict';
/* JAH The Pronunciation Coaching Database generator — jahdb-pronunciation-coaching-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PC-";
var FIELDS=["sound-production","stress-and-rhythm","accent-coaching"];
var TOPICS={"sound-production":["The IPA Crash Course \u2014 sound-production","Word Stress Rules \u2014 sound-production","Connected Speech \u2014 sound-production","Vowel Length Matters \u2014 sound-production","Tongue Twisters as Drills \u2014 sound-production","Coaching Without Shame \u2014 sound-production","Phone Call Clarity \u2014 sound-production","Breathing for Speech \u2014 sound-production","Children's Speech Sounds \u2014 sound-production","Pronunciation Apps Ranked \u2014 sound-production","Maintaining Gains \u2014 sound-production","The Mirror Drill \u2014 sound-production"],"stress-and-rhythm":["Minimal Pairs Training \u2014 stress-and-rhythm","Sentence Stress and Rhythm \u2014 stress-and-rhythm","The 'Th' Sounds \u2014 stress-and-rhythm","Shadowing Technique \u2014 stress-and-rhythm","Public Speaking Pronunciation \u2014 stress-and-rhythm","The Phonetic Alphabet for Names \u2014 stress-and-rhythm","Presenting Numbers Aloud \u2014 stress-and-rhythm","Vocal Warm-Ups \u2014 stress-and-rhythm","Singing for Pronunciation \u2014 stress-and-rhythm","Giving Pronunciation Feedback \u2014 stress-and-rhythm","When to See a Speech Therapist \u2014 stress-and-rhythm"],"accent-coaching":["Mouth Mechanics \u2014 accent-coaching","Intonation Patterns \u2014 accent-coaching","R vs L Distinction \u2014 accent-coaching","Recording and Self-Review \u2014 accent-coaching","Accent vs Intelligibility \u2014 accent-coaching","Interview Pronunciation Prep \u2014 accent-coaching","Storytelling Voice \u2014 accent-coaching","Regional Accent Coaching \u2014 accent-coaching","The 30-Day Pronunciation Plan \u2014 accent-coaching","Pronunciation for Presentations \u2014 accent-coaching","Celebrating Pronunciation Wins \u2014 accent-coaching"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Pronunciation Coaching Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['education and learning record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Pronunciation Coaching Database.',
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
var gen={version:'jahdb-pronunciation-coaching-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pronunciation-coaching',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
