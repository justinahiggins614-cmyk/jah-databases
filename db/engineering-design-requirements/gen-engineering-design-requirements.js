(function(){'use strict';
/* JAH The Engineering Design Requirements Database generator — jahdb-engineering-design-requirements-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EDR-";
var FIELDS=["requirements-elicitation","specification-writing","verification-planning"];
var TOPICS={"requirements-elicitation":["What Makes a Good Requirement \u2014 requirements-elicitation","Writing Shall Statements \u2014 requirements-elicitation","Verification Methods \u2014 requirements-elicitation","Managing Changes \u2014 requirements-elicitation","Use Cases \u2014 requirements-elicitation","Constraint Requirements \u2014 requirements-elicitation","Reliability Requirements \u2014 requirements-elicitation","Derived Requirements \u2014 requirements-elicitation","Requirements Tools \u2014 requirements-elicitation","Coverage Analysis \u2014 requirements-elicitation","A/B Requirements \u2014 requirements-elicitation","The Elicitation Workshop \u2014 requirements-elicitation"],"specification-writing":["Functional vs Non-Functional \u2014 specification-writing","Quantifying Requirements \u2014 specification-writing","Validation vs Verification \u2014 specification-writing","The Requirements Playbook \u2014 specification-writing","User Stories (Agile) \u2014 specification-writing","Interface Requirements \u2014 specification-writing","Environmental Requirements \u2014 specification-writing","Assumptions and Dependencies \u2014 specification-writing","Baselining \u2014 specification-writing","Requirements Metrics \u2014 specification-writing","Legacy Requirements Mining \u2014 specification-writing"],"verification-planning":["Stakeholder Elicitation \u2014 verification-planning","Traceability Matrix \u2014 verification-planning","Requirements Reviews \u2014 verification-planning","SMART Requirements \u2014 verification-planning","Acceptance Criteria \u2014 verification-planning","Safety Requirements \u2014 verification-planning","Regulatory Requirements \u2014 verification-planning","Glossary and Definitions \u2014 verification-planning","Bidirectional Traceability \u2014 verification-planning","Prototyping Requirements \u2014 verification-planning","Requirements Reuse \u2014 verification-planning"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Engineering Design Requirements Database — generated study\n"
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
   + "    print('kind: engineering record')\n"
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
    standards:['engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Engineering Design Requirements Database.',
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
var gen={version:'jahdb-engineering-design-requirements-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineering-design-requirements',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
