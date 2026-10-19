(function(){'use strict';
/* JAH The Data Anonymization Assessment Database generator — jahdb-data-anonymization-assessment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DAA-";
var FIELDS=["anonymization-techniques","reidentification-risk","compliant-sharing"];
var TOPICS={"anonymization-techniques":["Why Anonymize \u2014 anonymization-techniques","L-Diversity \u2014 anonymization-techniques","Epsilon Selection \u2014 anonymization-techniques","Masking and Tokenization \u2014 anonymization-techniques","Re-identification Attacks \u2014 anonymization-techniques","HIPAA Expert Determination \u2014 anonymization-techniques","Data Sharing Agreements \u2014 anonymization-techniques","The Anonymization Playbook \u2014 anonymization-techniques","Swapping \u2014 anonymization-techniques","Geographic Aggregation \u2014 anonymization-techniques","Location Data Caution \u2014 anonymization-techniques","Re-assessment Cadence \u2014 anonymization-techniques"],"reidentification-risk":["Identifiers Taxonomy \u2014 reidentification-risk","T-Closeness \u2014 reidentification-risk","Generalization Hierarchies \u2014 reidentification-risk","Perturbation \u2014 reidentification-risk","Risk Assessment Method \u2014 reidentification-risk","GDPR Anonymization Bar \u2014 reidentification-risk","Utility Measurement \u2014 reidentification-risk","Aggregation as Anonymization \u2014 reidentification-risk","Top/Bottom Coding \u2014 reidentification-risk","Longitudinal Data Risks \u2014 reidentification-risk","Differential Privacy in Practice \u2014 reidentification-risk"],"compliant-sharing":["K-Anonymity \u2014 compliant-sharing","Differential Privacy \u2014 compliant-sharing","Suppression \u2014 compliant-sharing","Synthetic Data \u2014 compliant-sharing","HIPAA Safe Harbor \u2014 compliant-sharing","Pseudonymization \u2014 compliant-sharing","Tooling (ARX, etc.) \u2014 compliant-sharing","Cell Suppression \u2014 compliant-sharing","Date Shifting \u2014 compliant-sharing","Genomic Data Caution \u2014 compliant-sharing","Anonymization Documentation \u2014 compliant-sharing"]};
var KINDS="data-engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Anonymization Assessment Database — generated study\n"
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
   + "    print('kind: data-engineering record')\n"
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
    standards:['data-engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Data Anonymization Assessment Database.',
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
var gen={version:'jahdb-data-anonymization-assessment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-anonymization-assessment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
