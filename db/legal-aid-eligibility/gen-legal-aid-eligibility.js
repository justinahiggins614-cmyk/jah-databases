(function(){'use strict';
/* JAH The Legal Aid Eligibility Database generator — jahdb-legal-aid-eligibility-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LAE-";
var FIELDS=["eligibility-rules","finding-help","self-help-resources"];
var TOPICS={"eligibility-rules":["Who Qualifies for Legal Aid \u2014 eligibility-rules","Legal Aid Case Priorities \u2014 eligibility-rules","Unbundled Legal Services \u2014 eligibility-rules","Domestic Violence Legal Help \u2014 eligibility-rules","Elder Law Legal Aid \u2014 eligibility-rules","Disability Rights Help \u2014 eligibility-rules","Court Self-Help Centers \u2014 eligibility-rules","Police Interaction Rights \u2014 eligibility-rules","Bankruptcy Legal Aid \u2014 eligibility-rules","Language Access Rights \u2014 eligibility-rules","The Legal Emergency Plan \u2014 eligibility-rules","Fee Agreements Explained \u2014 eligibility-rules"],"finding-help":["Finding Your Local Legal Aid \u2014 finding-help","The Application Process \u2014 finding-help","Small Claims Court Guide \u2014 finding-help","Public Benefits Appeals \u2014 finding-help","Veterans Legal Help \u2014 finding-help","Family Law Low-Cost Options \u2014 finding-help","Legal Document Preparers \u2014 finding-help","Employment Legal Aid \u2014 finding-help","Expungement Help \u2014 finding-help","Disability Accommodations in Court \u2014 finding-help","Tracking Your Case \u2014 finding-help"],"self-help-resources":["Pro Bono Programs \u2014 self-help-resources","What If You're Over Income \u2014 self-help-resources","Tenant Legal Aid \u2014 self-help-resources","Consumer Fraud Help \u2014 self-help-resources","Immigration Legal Aid \u2014 self-help-resources","Mediation as Alternative \u2014 self-help-resources","Know-Your-Rights Basics \u2014 self-help-resources","Debt Collection Defense \u2014 self-help-resources","Wills for Low-Income \u2014 self-help-resources","Appealing Legal Aid Denials \u2014 self-help-resources","Evaluating Lawyer Quality \u2014 self-help-resources"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Legal Aid Eligibility Database — generated study\n"
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
   + "    print('kind: law and rights record')\n"
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
    standards:['law and rights record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Legal Aid Eligibility Database.',
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
var gen={version:'jahdb-legal-aid-eligibility-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('legal-aid-eligibility',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
