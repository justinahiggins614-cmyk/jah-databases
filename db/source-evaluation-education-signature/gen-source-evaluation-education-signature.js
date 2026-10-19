(function(){'use strict';
/* JAH The Source Evaluation Education Signature Database generator — jahdb-source-evaluation-education-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SEE-";
var FIELDS=["evaluation-frameworks","misinformation-defense","verification-workflows"];
var TOPICS={"evaluation-frameworks":["Signature The SIFT Method (Signature Edition) \u2014 evaluation-frameworks","Signature Identifying Author Expertise (Signature Edition) \u2014 evaluation-frameworks","Signature Reverse Image Search (Signature Edition) \u2014 evaluation-frameworks","Signature Recognizing Logical Fallacies (Signature Edition) \u2014 evaluation-frameworks","Signature Wikipedia: Use It Right (Signature Edition) \u2014 evaluation-frameworks","Signature Social Media Verification (Signature Edition) \u2014 evaluation-frameworks","Signature Preprints vs Published (Signature Edition) \u2014 evaluation-frameworks","Signature The Backfire Effect (Myth) (Signature Edition) \u2014 evaluation-frameworks","Signature Classroom Verification Exercises (Signature Edition) \u2014 evaluation-frameworks","Signature The Information Diet (Signature Edition) \u2014 evaluation-frameworks","Signature Assessing Source Evaluation Skills (Signature Edition) \u2014 evaluation-frameworks","Signature Triangulation Rule (Signature Edition) \u2014 evaluation-frameworks"],"misinformation-defense":["Signature Lateral Reading (Signature Edition) \u2014 misinformation-defense","Signature Publication Reputation Check (Signature Edition) \u2014 misinformation-defense","Signature Checking Dates and Context (Signature Edition) \u2014 misinformation-defense","Signature Bias Detection in Sources (Signature Edition) \u2014 misinformation-defense","Signature Fact-Checking Sites (Signature Edition) \u2014 misinformation-defense","Signature The 'Too Good/Too Bad' Heuristic (Signature Edition) \u2014 misinformation-defense","Signature Expert Consensus vs Mavericks (Signature Edition) \u2014 misinformation-defense","Signature Effective Debunking (Signature Edition) \u2014 misinformation-defense","Signature Building a Verification Habit (Signature Edition) \u2014 misinformation-defense","Signature Primary Document Reading (Signature Edition) \u2014 misinformation-defense","Signature Parent Guide to Media Literacy (Signature Edition) \u2014 misinformation-defense"],"verification-workflows":["Signature CRAAP Test (Signature Edition) \u2014 verification-workflows","Signature Spotting Fake News Patterns (Signature Edition) \u2014 verification-workflows","Signature Statistical Literacy Basics (Signature Edition) \u2014 verification-workflows","Signature Primary vs Secondary Sources (Signature Edition) \u2014 verification-workflows","Signature Deepfake Awareness (Signature Edition) \u2014 verification-workflows","Signature Evaluating Studies (Signature Edition) \u2014 verification-workflows","Signature Funding and Conflict Disclosure (Signature Edition) \u2014 verification-workflows","Signature Teaching Kids Source Evaluation (Signature Edition) \u2014 verification-workflows","Signature Evaluating AI-Generated Content (Signature Edition) \u2014 verification-workflows","Signature Correction Culture in Class (Signature Edition) \u2014 verification-workflows","Signature The Lifelong Verifier (Signature Edition) \u2014 verification-workflows"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Source Evaluation Education Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Source Evaluation Education Signature Database.',
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
var gen={version:'jahdb-source-evaluation-education-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('source-evaluation-education-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
