(function(){'use strict';
/* JAH The Systems Thinking Case Library Signature Database generator — jahdb-systems-thinking-case-library-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STCL-";
var FIELDS=["systems-cases","leverage-analysis","systems-tools"];
var TOPICS={"systems-cases":["Signature What Is Systems Thinking (Signature Edition) \u2014 systems-cases","Signature The Case Method (Signature Edition) \u2014 systems-cases","Signature Shifting the Burden (Signature Edition) \u2014 systems-cases","Signature Eroding Goals (Signature Edition) \u2014 systems-cases","Signature Stock and Flow (Signature Edition) \u2014 systems-cases","Signature Case: Traffic Congestion (Signature Edition) \u2014 systems-cases","Signature Case: Urban Sprawl (Signature Edition) \u2014 systems-cases","Signature Case: Climate Feedbacks (Signature Edition) \u2014 systems-cases","Signature Case: Public Health Campaigns (Signature Edition) \u2014 systems-cases","Signature Systems Interviewing (Signature Edition) \u2014 systems-cases","Signature Systems in Strategy (Signature Edition) \u2014 systems-cases","Signature Annual Systems Review (Signature Edition) \u2014 systems-cases"],"leverage-analysis":["Signature Feedback Loops (Signature Edition) \u2014 leverage-analysis","Signature Tragedy of the Commons (Signature Edition) \u2014 leverage-analysis","Signature Limits to Growth (Signature Edition) \u2014 leverage-analysis","Signature Escalation (Signature Edition) \u2014 leverage-analysis","Signature Delays in Systems (Signature Edition) \u2014 leverage-analysis","Signature Case: Antibiotic Resistance (Signature Edition) \u2014 leverage-analysis","Signature Case: Healthcare Queues (Signature Edition) \u2014 leverage-analysis","Signature Case: Organizational Silos (Signature Edition) \u2014 leverage-analysis","Signature Simulation Tools (Signature Edition) \u2014 leverage-analysis","Signature Writing Case Studies (Signature Edition) \u2014 leverage-analysis","Signature Personal Systems (Signature Edition) \u2014 leverage-analysis"],"systems-tools":["Signature Leverage Points (Signature Edition) \u2014 systems-tools","Signature Fixes That Fail (Signature Edition) \u2014 systems-tools","Signature Success to the Successful (Signature Edition) \u2014 systems-tools","Signature Causal Loop Diagrams (Signature Edition) \u2014 systems-tools","Signature Mental Models (Signature Edition) \u2014 systems-tools","Signature Case: Fisheries Collapse (Signature Edition) \u2014 systems-tools","Signature Case: Software Bugs (Signature Edition) \u2014 systems-tools","Signature Case: Supply Chains (Signature Edition) \u2014 systems-tools","Signature Group Model Building (Signature Edition) \u2014 systems-tools","Signature Teaching Systems Thinking (Signature Edition) \u2014 systems-tools","Signature The Systems Library Index (Signature Edition) \u2014 systems-tools"]};
var KINDS="advanced planning and systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Systems Thinking Case Library Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['advanced planning and systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Systems Thinking Case Library Signature Database.',
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
var gen={version:'jahdb-systems-thinking-case-library-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('systems-thinking-case-library-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
