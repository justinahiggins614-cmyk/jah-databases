(function(){'use strict';
/* JAH The Finite Element Analysis Guidance Database generator — jahdb-finite-element-analysis-guidance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FEAG-";
var FIELDS=["fea-fundamentals","meshing-and-solving","result-validation"];
var TOPICS={"fea-fundamentals":["What FEA Does \u2014 fea-fundamentals","Element Types \u2014 fea-fundamentals","Convergence Studies \u2014 fea-fundamentals","The FEA Playbook \u2014 fea-fundamentals","Buckling Analysis \u2014 fea-fundamentals","Thermal Analysis \u2014 fea-fundamentals","Bolt Preload Modeling \u2014 fea-fundamentals","Topology Optimization \u2014 fea-fundamentals","Explicit Dynamics \u2014 fea-fundamentals","Solver Choices \u2014 fea-fundamentals","Safety Factors from FEA \u2014 fea-fundamentals","Free FEA Tools \u2014 fea-fundamentals"],"meshing-and-solving":["When to Use FEA \u2014 meshing-and-solving","Boundary Conditions \u2014 meshing-and-solving","Stress Singularities \u2014 meshing-and-solving","Linear Static Analysis \u2014 meshing-and-solving","Modal (Vibration) Analysis \u2014 meshing-and-solving","Thermal-Stress Coupling \u2014 meshing-and-solving","Symmetry in FEA \u2014 meshing-and-solving","Fatigue Analysis (FEA) \u2014 meshing-and-solving","CFD Coupling Basics \u2014 meshing-and-solving","Units Consistency \u2014 meshing-and-solving","FEA Report Writing \u2014 meshing-and-solving"],"result-validation":["Meshing Basics \u2014 result-validation","Material Models \u2014 result-validation","Validating Results \u2014 result-validation","Nonlinear Analysis \u2014 result-validation","Harmonic Response \u2014 result-validation","Contact Modeling \u2014 result-validation","Submodeling \u2014 result-validation","Composite Modeling \u2014 result-validation","Mesh Quality Metrics \u2014 result-validation","Result Interpretation \u2014 result-validation","Common FEA Mistakes \u2014 result-validation"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Finite Element Analysis Guidance Database — generated study\n"
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
    provenance:'Generated structural sample for the The Finite Element Analysis Guidance Database.',
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
var gen={version:'jahdb-finite-element-analysis-guidance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('finite-element-analysis-guidance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
