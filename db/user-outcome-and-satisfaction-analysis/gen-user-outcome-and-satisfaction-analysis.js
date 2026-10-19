(function(){'use strict';
/* JAH The User Outcome and Satisfaction Analysis Database generator — jahdb-user-outcome-and-satisfaction-analysis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UOSA-";
var FIELDS=["outcome-metrics","satisfaction-methods","improvement-systems"];
var TOPICS={"outcome-metrics":["Outcomes vs Outputs \u2014 outcome-metrics","The Analysis Playbook \u2014 outcome-metrics","HEART Framework \u2014 outcome-metrics","OKRs for Outcomes \u2014 outcome-metrics","Churn Analysis \u2014 outcome-metrics","Review Analytics \u2014 outcome-metrics","Time on Task \u2014 outcome-metrics","Outcome Harvesting \u2014 outcome-metrics","Dashboards \u2014 outcome-metrics","Closing the Loop \u2014 outcome-metrics","Ethics of Measurement \u2014 outcome-metrics","Annual Outcome Review \u2014 outcome-metrics"],"satisfaction-methods":["CSAT \u2014 satisfaction-methods","CES \u2014 satisfaction-methods","AARRR Metrics \u2014 satisfaction-methods","Cohort Analysis \u2014 satisfaction-methods","Voice of Customer \u2014 satisfaction-methods","Support Analytics \u2014 satisfaction-methods","Error Rates \u2014 satisfaction-methods","Theory of Change \u2014 satisfaction-methods","Reporting Cadence \u2014 satisfaction-methods","Prioritization (RICE) \u2014 satisfaction-methods","Survey Fatigue \u2014 satisfaction-methods"],"improvement-systems":["NPS \u2014 improvement-systems","SUS (Usability) \u2014 improvement-systems","North Star Metric \u2014 improvement-systems","Retention Analysis \u2014 improvement-systems","Sentiment Analysis \u2014 improvement-systems","Task Success Rate \u2014 improvement-systems","Qualitative Outcomes \u2014 improvement-systems","Logic Models \u2014 improvement-systems","Benchmarking \u2014 improvement-systems","Experimentation Culture \u2014 improvement-systems","The Outcome-Driven Org \u2014 improvement-systems"]};
var KINDS="advanced planning and systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The User Outcome and Satisfaction Analysis Database — generated study\n"
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
   + "    print('kind: advanced planning and systems record')\n"
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
    standards:['advanced planning and systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The User Outcome and Satisfaction Analysis Database.',
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
var gen={version:'jahdb-user-outcome-and-satisfaction-analysis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('user-outcome-and-satisfaction-analysis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
