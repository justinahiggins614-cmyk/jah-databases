(function(){'use strict';
/* JAH The Military Family Support Database generator — jahdb-military-family-support-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MFS-";
var FIELDS=["benefits-navigation","deployment-support","family-resources"];
var TOPICS={"benefits-navigation":["TRICARE Basics \u2014 benefits-navigation","PCS Move Support \u2014 benefits-navigation","Family Readiness Groups \u2014 benefits-navigation","Spouse Employment Help \u2014 benefits-navigation","VA Home Loans \u2014 benefits-navigation","VA Disability Claims \u2014 benefits-navigation","Deployment Kids Support \u2014 benefits-navigation","Military Legal Assistance \u2014 benefits-navigation","Sexual Assault (SAPR) \u2014 benefits-navigation","Spouse Licensure Portability \u2014 benefits-navigation","Emergency Family Assistance \u2014 benefits-navigation","Overseas Station Life (OCONUS) \u2014 benefits-navigation"],"deployment-support":["DEERS Enrollment \u2014 deployment-support","Deployment Financial Prep \u2014 deployment-support","Military OneSource \u2014 deployment-support","Education: GI Bill Transfer \u2014 deployment-support","SGLI and Family Coverage \u2014 deployment-support","Gold Star Family Support \u2014 deployment-support","Reintegration After Deployment \u2014 deployment-support","Financial Counseling (Military) \u2014 deployment-support","Mental Health Resources \u2014 deployment-support","Voting While Military \u2014 deployment-support","Retirement (BRS) \u2014 deployment-support"],"family-resources":["BAH (Housing Allowance) \u2014 family-resources","SCRA Protections \u2014 family-resources","Child Care (CDC/FCC) \u2014 family-resources"," commissary/PX Benefits \u2014 family-resources","Transition Assistance (TAP) \u2014 family-resources","EFMP (Special Needs) \u2014 family-resources","Reserve/Guard Family Support \u2014 family-resources","Domestic Abuse (FAP) \u2014 family-resources","Child and Youth Programs \u2014 family-resources","Tax Benefits (Military) \u2014 family-resources","The Military Family Binder \u2014 family-resources"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Military Family Support Database — generated study\n"
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
   + "    print('kind: government-assistance record')\n"
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
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Military Family Support Database.',
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
var gen={version:'jahdb-military-family-support-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('military-family-support',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
