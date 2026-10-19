(function(){'use strict';
/* JAH The Audience Research Methods Database generator — jahdb-audience-research-methods-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARM-";
var FIELDS=["research-design","data-collection","insight-activation"];
var TOPICS={"research-design":["Research Questions \u2014 research-design","The Research Playbook \u2014 research-design","Ethnographic Research \u2014 research-design","Search Data Mining \u2014 research-design","Sales Call Analysis \u2014 research-design","Empathy Mapping \u2014 research-design","Quant vs Qual \u2014 research-design","Incentives \u2014 research-design","Analysis Methods \u2014 research-design","Stakeholder Buy-In \u2014 research-design","Unmoderated Testing \u2014 research-design","The Insight Engine \u2014 research-design"],"data-collection":["Survey Design \u2014 data-collection","Focus Groups \u2014 data-collection","Analytics Deep Dives \u2014 data-collection","Review Mining \u2014 data-collection","Segmentation \u2014 data-collection","Journey Mapping \u2014 data-collection","Sampling \u2014 data-collection","Recruiting Participants \u2014 data-collection","Affinity Diagramming \u2014 data-collection","Research Repositories \u2014 data-collection","Card Sorting \u2014 data-collection"],"insight-activation":["Interview Techniques \u2014 insight-activation","Diary Studies \u2014 insight-activation","Social Listening \u2014 insight-activation","Support Ticket Analysis \u2014 insight-activation","Jobs to Be Done \u2014 insight-activation","Persona Validation \u2014 insight-activation","Survey Bias \u2014 insight-activation","Research Ethics \u2014 insight-activation","Insight Writing \u2014 insight-activation","Continuous Discovery \u2014 insight-activation","Tree Testing \u2014 insight-activation"]};
var KINDS="communication record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Audience Research Methods Database — generated study\n"
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
    provenance:'Generated structural sample for the The Audience Research Methods Database.',
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
var gen={version:'jahdb-audience-research-methods-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('audience-research-methods',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
