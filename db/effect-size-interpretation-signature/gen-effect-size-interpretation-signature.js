(function(){'use strict';
/* JAH The Effect Size Interpretation Signature Database generator — jahdb-effect-size-interpretation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ESI-";
var FIELDS=["effect-size-measures","interpretation-standards","practical-significance"];
var TOPICS={"effect-size-measures":["Signature Why Effect Sizes Matter (Signature Edition) \u2014 effect-size-measures","Signature Odds Ratios (Signature Edition) \u2014 effect-size-measures","Signature Practical Significance (Signature Edition) \u2014 effect-size-measures","Signature Converting Between Measures (Signature Edition) \u2014 effect-size-measures","Signature Publication Bias (Signature Edition) \u2014 effect-size-measures","Signature The Interpretation Playbook (Signature Edition) \u2014 effect-size-measures","Signature Hedges' g (Signature Edition) \u2014 effect-size-measures","Signature AUC as Effect Size (Signature Edition) \u2014 effect-size-measures","Signature Omega-Squared (Signature Edition) \u2014 effect-size-measures","Signature Mediation Effect Sizes (Signature Edition) \u2014 effect-size-measures","Signature Bayesian Effect Sizes (Signature Edition) \u2014 effect-size-measures","Signature Teaching Effect Sizes (Signature Edition) \u2014 effect-size-measures"],"interpretation-standards":["Signature Cohen's d (Signature Edition) \u2014 interpretation-standards","Signature Eta-Squared (Signature Edition) \u2014 interpretation-standards","Signature Small Effects That Matter (Signature Edition) \u2014 interpretation-standards","Signature Meta-Analytic Thinking (Signature Edition) \u2014 interpretation-standards","Signature P-Hacking and Effect Inflation (Signature Edition) \u2014 interpretation-standards","Signature Cohen's Conventions Critique (Signature Edition) \u2014 interpretation-standards","Signature Risk Ratios (Signature Edition) \u2014 interpretation-standards","Signature R\u00b2 Interpretation (Signature Edition) \u2014 interpretation-standards","Signature Standardized Mean Change (Signature Edition) \u2014 interpretation-standards","Signature Smallest Effect of Interest (Signature Edition) \u2014 interpretation-standards","Signature Visualizing Effects (Signature Edition) \u2014 interpretation-standards"],"practical-significance":["Signature Correlation r (Signature Edition) \u2014 practical-significance","Signature Confidence Intervals for Effects (Signature Edition) \u2014 practical-significance","Signature Large Effects That Don't (Signature Edition) \u2014 practical-significance","Signature Heterogeneity (I\u00b2) (Signature Edition) \u2014 practical-significance","Signature Power and Effect Size (Signature Edition) \u2014 practical-significance","Signature Glass's Delta (Signature Edition) \u2014 practical-significance","Signature Number Needed to Treat (Signature Edition) \u2014 practical-significance","Signature Partial Eta-Squared (Signature Edition) \u2014 practical-significance","Signature Effect Sizes in Regression (Signature Edition) \u2014 practical-significance","Signature Equivalence Testing (TOST) (Signature Edition) \u2014 practical-significance","Signature Reporting Checklist (Signature Edition) \u2014 practical-significance"]};
var KINDS="science and research record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Effect Size Interpretation Signature Database — generated study\n"
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
   + "    print('kind: science and research record')\n"
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
    standards:['science and research record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Effect Size Interpretation Signature Database.',
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
var gen={version:'jahdb-effect-size-interpretation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('effect-size-interpretation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
