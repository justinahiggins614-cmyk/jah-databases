(function(){'use strict';
/* JAH The Audience Research Methods Signature Database generator — jahdb-audience-research-methods-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARM-";
var FIELDS=["research-design","data-collection","insight-activation"];
var TOPICS={"research-design":["Signature Research Questions (Signature Edition) \u2014 research-design","Signature The Research Playbook (Signature Edition) \u2014 research-design","Signature Ethnographic Research (Signature Edition) \u2014 research-design","Signature Search Data Mining (Signature Edition) \u2014 research-design","Signature Sales Call Analysis (Signature Edition) \u2014 research-design","Signature Empathy Mapping (Signature Edition) \u2014 research-design","Signature Quant vs Qual (Signature Edition) \u2014 research-design","Signature Incentives (Signature Edition) \u2014 research-design","Signature Analysis Methods (Signature Edition) \u2014 research-design","Signature Stakeholder Buy-In (Signature Edition) \u2014 research-design","Signature Unmoderated Testing (Signature Edition) \u2014 research-design","Signature The Insight Engine (Signature Edition) \u2014 research-design"],"data-collection":["Signature Survey Design (Signature Edition) \u2014 data-collection","Signature Focus Groups (Signature Edition) \u2014 data-collection","Signature Analytics Deep Dives (Signature Edition) \u2014 data-collection","Signature Review Mining (Signature Edition) \u2014 data-collection","Signature Segmentation (Signature Edition) \u2014 data-collection","Signature Journey Mapping (Signature Edition) \u2014 data-collection","Signature Sampling (Signature Edition) \u2014 data-collection","Signature Recruiting Participants (Signature Edition) \u2014 data-collection","Signature Affinity Diagramming (Signature Edition) \u2014 data-collection","Signature Research Repositories (Signature Edition) \u2014 data-collection","Signature Card Sorting (Signature Edition) \u2014 data-collection"],"insight-activation":["Signature Interview Techniques (Signature Edition) \u2014 insight-activation","Signature Diary Studies (Signature Edition) \u2014 insight-activation","Signature Social Listening (Signature Edition) \u2014 insight-activation","Signature Support Ticket Analysis (Signature Edition) \u2014 insight-activation","Signature Jobs to Be Done (Signature Edition) \u2014 insight-activation","Signature Persona Validation (Signature Edition) \u2014 insight-activation","Signature Survey Bias (Signature Edition) \u2014 insight-activation","Signature Research Ethics (Signature Edition) \u2014 insight-activation","Signature Insight Writing (Signature Edition) \u2014 insight-activation","Signature Continuous Discovery (Signature Edition) \u2014 insight-activation","Signature Tree Testing (Signature Edition) \u2014 insight-activation"]};
var KINDS="communication record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Audience Research Methods Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Audience Research Methods Signature Database.',
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
var gen={version:'jahdb-audience-research-methods-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('audience-research-methods-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
