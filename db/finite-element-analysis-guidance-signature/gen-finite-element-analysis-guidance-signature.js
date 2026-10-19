(function(){'use strict';
/* JAH The Finite Element Analysis Guidance Signature Database generator — jahdb-finite-element-analysis-guidance-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FEAG-";
var FIELDS=["fea-fundamentals","meshing-and-solving","result-validation"];
var TOPICS={"fea-fundamentals":["Signature What FEA Does (Signature Edition) \u2014 fea-fundamentals","Signature Element Types (Signature Edition) \u2014 fea-fundamentals","Signature Convergence Studies (Signature Edition) \u2014 fea-fundamentals","Signature The FEA Playbook (Signature Edition) \u2014 fea-fundamentals","Signature Buckling Analysis (Signature Edition) \u2014 fea-fundamentals","Signature Thermal Analysis (Signature Edition) \u2014 fea-fundamentals","Signature Bolt Preload Modeling (Signature Edition) \u2014 fea-fundamentals","Signature Topology Optimization (Signature Edition) \u2014 fea-fundamentals","Signature Explicit Dynamics (Signature Edition) \u2014 fea-fundamentals","Signature Solver Choices (Signature Edition) \u2014 fea-fundamentals","Signature Safety Factors from FEA (Signature Edition) \u2014 fea-fundamentals","Signature Free FEA Tools (Signature Edition) \u2014 fea-fundamentals"],"meshing-and-solving":["Signature When to Use FEA (Signature Edition) \u2014 meshing-and-solving","Signature Boundary Conditions (Signature Edition) \u2014 meshing-and-solving","Signature Stress Singularities (Signature Edition) \u2014 meshing-and-solving","Signature Linear Static Analysis (Signature Edition) \u2014 meshing-and-solving","Signature Modal (Vibration) Analysis (Signature Edition) \u2014 meshing-and-solving","Signature Thermal-Stress Coupling (Signature Edition) \u2014 meshing-and-solving","Signature Symmetry in FEA (Signature Edition) \u2014 meshing-and-solving","Signature Fatigue Analysis (FEA) (Signature Edition) \u2014 meshing-and-solving","Signature CFD Coupling Basics (Signature Edition) \u2014 meshing-and-solving","Signature Units Consistency (Signature Edition) \u2014 meshing-and-solving","Signature FEA Report Writing (Signature Edition) \u2014 meshing-and-solving"],"result-validation":["Signature Meshing Basics (Signature Edition) \u2014 result-validation","Signature Material Models (Signature Edition) \u2014 result-validation","Signature Validating Results (Signature Edition) \u2014 result-validation","Signature Nonlinear Analysis (Signature Edition) \u2014 result-validation","Signature Harmonic Response (Signature Edition) \u2014 result-validation","Signature Contact Modeling (Signature Edition) \u2014 result-validation","Signature Submodeling (Signature Edition) \u2014 result-validation","Signature Composite Modeling (Signature Edition) \u2014 result-validation","Signature Mesh Quality Metrics (Signature Edition) \u2014 result-validation","Signature Result Interpretation (Signature Edition) \u2014 result-validation","Signature Common FEA Mistakes (Signature Edition) \u2014 result-validation"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Finite Element Analysis Guidance Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Finite Element Analysis Guidance Signature Database.',
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
var gen={version:'jahdb-finite-element-analysis-guidance-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('finite-element-analysis-guidance-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
