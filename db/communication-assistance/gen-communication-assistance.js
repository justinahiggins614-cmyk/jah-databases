(function(){'use strict';
/* JAH The Communication Assistance Database generator — jahdb-communication-assistance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CA-";
var FIELDS=["difficult-conversations","clear-expression-methods","listening-and-feedback"];
var TOPICS={"difficult-conversations":["The SBI Feedback Model \u2014 difficult-conversations","The DESC Script \u2014 difficult-conversations","Difficult Conversation Opener \u2014 difficult-conversations","Small Talk That Works \u2014 difficult-conversations","Meeting People Where They Are \u2014 difficult-conversations","De-escalation Phrases \u2014 difficult-conversations","Listening in Conflict \u2014 difficult-conversations","Saying Thank You That Lands \u2014 difficult-conversations","BLUF Communication \u2014 difficult-conversations","Cross-Cultural Communication Basics \u2014 difficult-conversations","Communicating Decisions to a Team \u2014 difficult-conversations","The Listening Tour \u2014 difficult-conversations"],"clear-expression-methods":["Active Listening Practice \u2014 clear-expression-methods","Clear Request Formula \u2014 clear-expression-methods","The Apology Framework \u2014 clear-expression-methods","Email Clarity Rules \u2014 clear-expression-methods","The Feedback Sandwich (Fixed) \u2014 clear-expression-methods","Communicating Boundaries \u2014 clear-expression-methods","The Check-In Question \u2014 clear-expression-methods","Communicating When You're Wrong \u2014 clear-expression-methods","Communicating with Kids \u2014 clear-expression-methods","Communicating Under Stress \u2014 clear-expression-methods","The Compliment That Builds \u2014 clear-expression-methods"],"listening-and-feedback":["Nonviolent Communication (NVC) \u2014 listening-and-feedback","Saying No Gracefully \u2014 listening-and-feedback","Asking Better Questions \u2014 listening-and-feedback","Texting Without Misunderstanding \u2014 listening-and-feedback","Negotiating Everyday Deals \u2014 listening-and-feedback","Storytelling for Everyday Persuasion \u2014 listening-and-feedback","Communicating Change \u2014 listening-and-feedback","The One-Breath Update \u2014 listening-and-feedback","Communicating with Aging Parents \u2014 listening-and-feedback","The Repair Attempt \u2014 listening-and-feedback","Communicating Expectations Upfront \u2014 listening-and-feedback"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Communication Assistance Database — generated study\n"
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
    provenance:'Generated structural sample for the The Communication Assistance Database.',
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
var gen={version:'jahdb-communication-assistance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('communication-assistance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
