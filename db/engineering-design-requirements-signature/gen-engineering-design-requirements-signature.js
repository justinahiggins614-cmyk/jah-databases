(function(){'use strict';
/* JAH The Engineering Design Requirements Signature Database generator — jahdb-engineering-design-requirements-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EDR-";
var FIELDS=["requirements-elicitation","specification-writing","verification-planning"];
var TOPICS={"requirements-elicitation":["Signature What Makes a Good Requirement (Signature Edition) \u2014 requirements-elicitation","Signature Writing Shall Statements (Signature Edition) \u2014 requirements-elicitation","Signature Verification Methods (Signature Edition) \u2014 requirements-elicitation","Signature Managing Changes (Signature Edition) \u2014 requirements-elicitation","Signature Use Cases (Signature Edition) \u2014 requirements-elicitation","Signature Constraint Requirements (Signature Edition) \u2014 requirements-elicitation","Signature Reliability Requirements (Signature Edition) \u2014 requirements-elicitation","Signature Derived Requirements (Signature Edition) \u2014 requirements-elicitation","Signature Requirements Tools (Signature Edition) \u2014 requirements-elicitation","Signature Coverage Analysis (Signature Edition) \u2014 requirements-elicitation","Signature A/B Requirements (Signature Edition) \u2014 requirements-elicitation","Signature The Elicitation Workshop (Signature Edition) \u2014 requirements-elicitation"],"specification-writing":["Signature Functional vs Non-Functional (Signature Edition) \u2014 specification-writing","Signature Quantifying Requirements (Signature Edition) \u2014 specification-writing","Signature Validation vs Verification (Signature Edition) \u2014 specification-writing","Signature The Requirements Playbook (Signature Edition) \u2014 specification-writing","Signature User Stories (Agile) (Signature Edition) \u2014 specification-writing","Signature Interface Requirements (Signature Edition) \u2014 specification-writing","Signature Environmental Requirements (Signature Edition) \u2014 specification-writing","Signature Assumptions and Dependencies (Signature Edition) \u2014 specification-writing","Signature Baselining (Signature Edition) \u2014 specification-writing","Signature Requirements Metrics (Signature Edition) \u2014 specification-writing","Signature Legacy Requirements Mining (Signature Edition) \u2014 specification-writing"],"verification-planning":["Signature Stakeholder Elicitation (Signature Edition) \u2014 verification-planning","Signature Traceability Matrix (Signature Edition) \u2014 verification-planning","Signature Requirements Reviews (Signature Edition) \u2014 verification-planning","Signature SMART Requirements (Signature Edition) \u2014 verification-planning","Signature Acceptance Criteria (Signature Edition) \u2014 verification-planning","Signature Safety Requirements (Signature Edition) \u2014 verification-planning","Signature Regulatory Requirements (Signature Edition) \u2014 verification-planning","Signature Glossary and Definitions (Signature Edition) \u2014 verification-planning","Signature Bidirectional Traceability (Signature Edition) \u2014 verification-planning","Signature Prototyping Requirements (Signature Edition) \u2014 verification-planning","Signature Requirements Reuse (Signature Edition) \u2014 verification-planning"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Engineering Design Requirements Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Engineering Design Requirements Signature Database.',
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
var gen={version:'jahdb-engineering-design-requirements-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineering-design-requirements-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
