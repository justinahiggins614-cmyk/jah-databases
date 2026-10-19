(function(){'use strict';
/* JAH The Misinformation Verification Database generator — jahdb-misinformation-verification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MV-";
var FIELDS=["fact-checking-methods","source-evaluation","correction-strategies"];
var TOPICS={"fact-checking-methods":["Why Misinformation Spreads \u2014 fact-checking-methods","The Verification Playbook \u2014 fact-checking-methods","Checking Quotes \u2014 fact-checking-methods","Correlation vs Causation \u2014 fact-checking-methods","Preprint Caution \u2014 fact-checking-methods","Bot Detection \u2014 fact-checking-methods","Conspiracy Thinking \u2014 fact-checking-methods","Media Literacy Education \u2014 fact-checking-methods","Echo Chambers \u2014 fact-checking-methods","Election Information \u2014 fact-checking-methods","Family Group Chats \u2014 fact-checking-methods","Annual Literacy Refresh \u2014 fact-checking-methods"],"source-evaluation":["Lateral Reading \u2014 source-evaluation","Fact-Check Sites \u2014 source-evaluation","Statistics Scrutiny \u2014 source-evaluation","Expert Consensus \u2014 source-evaluation","Deepfake Detection \u2014 source-evaluation","Astroturfing \u2014 source-evaluation","Correcting Others \u2014 source-evaluation","News Diet Design \u2014 source-evaluation","Verifying Health Claims \u2014 source-evaluation","Crisis Information \u2014 source-evaluation","Workplace Rumors \u2014 source-evaluation"],"correction-strategies":["Reverse Image Search \u2014 correction-strategies","Primary Sources \u2014 correction-strategies","Cherry-Picking Detection \u2014 correction-strategies","Predatory Journals \u2014 correction-strategies","AI-Generated Text Signs \u2014 correction-strategies","Emotional Manipulation \u2014 correction-strategies","Prebunking \u2014 correction-strategies","Algorithm Awareness \u2014 correction-strategies","Verifying Financial Claims \u2014 correction-strategies","Teaching Verification \u2014 correction-strategies","The Truth-Seeker's Oath \u2014 correction-strategies"]};
var KINDS="communication record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Misinformation Verification Database — generated study\n"
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
    provenance:'Generated structural sample for the The Misinformation Verification Database.',
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
var gen={version:'jahdb-misinformation-verification-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('misinformation-verification',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
