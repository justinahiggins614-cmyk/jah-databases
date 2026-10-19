(function(){'use strict';
/* JAH The Systems Thinking Case Library Database generator — jahdb-systems-thinking-case-library-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STCL-";
var FIELDS=["systems-cases","leverage-analysis","systems-tools"];
var TOPICS={"systems-cases":["What Is Systems Thinking \u2014 systems-cases","The Case Method \u2014 systems-cases","Shifting the Burden \u2014 systems-cases","Eroding Goals \u2014 systems-cases","Stock and Flow \u2014 systems-cases","Case: Traffic Congestion \u2014 systems-cases","Case: Urban Sprawl \u2014 systems-cases","Case: Climate Feedbacks \u2014 systems-cases","Case: Public Health Campaigns \u2014 systems-cases","Systems Interviewing \u2014 systems-cases","Systems in Strategy \u2014 systems-cases","Annual Systems Review \u2014 systems-cases"],"leverage-analysis":["Feedback Loops \u2014 leverage-analysis","Tragedy of the Commons \u2014 leverage-analysis","Limits to Growth \u2014 leverage-analysis","Escalation \u2014 leverage-analysis","Delays in Systems \u2014 leverage-analysis","Case: Antibiotic Resistance \u2014 leverage-analysis","Case: Healthcare Queues \u2014 leverage-analysis","Case: Organizational Silos \u2014 leverage-analysis","Simulation Tools \u2014 leverage-analysis","Writing Case Studies \u2014 leverage-analysis","Personal Systems \u2014 leverage-analysis"],"systems-tools":["Leverage Points \u2014 systems-tools","Fixes That Fail \u2014 systems-tools","Success to the Successful \u2014 systems-tools","Causal Loop Diagrams \u2014 systems-tools","Mental Models \u2014 systems-tools","Case: Fisheries Collapse \u2014 systems-tools","Case: Software Bugs \u2014 systems-tools","Case: Supply Chains \u2014 systems-tools","Group Model Building \u2014 systems-tools","Teaching Systems Thinking \u2014 systems-tools","The Systems Library Index \u2014 systems-tools"]};
var KINDS="advanced planning and systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Systems Thinking Case Library Database — generated study\n"
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
    provenance:'Generated structural sample for the The Systems Thinking Case Library Database.',
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
var gen={version:'jahdb-systems-thinking-case-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('systems-thinking-case-library',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
