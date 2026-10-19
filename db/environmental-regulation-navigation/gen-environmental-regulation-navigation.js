(function(){'use strict';
/* JAH The Environmental Regulation Navigation Database generator — jahdb-environmental-regulation-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ERN-";
var FIELDS=["rule-identification","permit-navigation","compliance-systems"];
var TOPICS={"rule-identification":["Which Rules Apply \u2014 rule-identification","Clean Air Act Basics \u2014 rule-identification","NPDES Permits \u2014 rule-identification","RCRA Basics \u2014 rule-identification","Endangered Species Act \u2014 rule-identification","EPCRA Reporting \u2014 rule-identification","State vs Federal \u2014 rule-identification","Voluntary Disclosure \u2014 rule-identification","Permitting Timelines \u2014 rule-identification","Agricultural Exemptions \u2014 rule-identification","Record Keeping (Env) \u2014 rule-identification","Staying Current \u2014 rule-identification"],"permit-navigation":["EPA Organization \u2014 permit-navigation","Air Permits (Title V) \u2014 permit-navigation","Stormwater Permits \u2014 permit-navigation","CERCLA/Superfund \u2014 permit-navigation","TSCA (Chemicals) \u2014 permit-navigation","SPCC Plans \u2014 permit-navigation","Working with Inspectors \u2014 permit-navigation","Citizen Suits \u2014 permit-navigation","Hiring Env Consultants \u2014 permit-navigation","Manure Management Rules \u2014 permit-navigation","Training (Env Compliance) \u2014 permit-navigation"],"compliance-systems":["The Compliance Playbook \u2014 compliance-systems","Clean Water Act Basics \u2014 compliance-systems","Wetlands (Section 404) \u2014 compliance-systems","NEPA Reviews \u2014 compliance-systems","FIFRA (Pesticides) \u2014 compliance-systems","Underground Storage Tanks \u2014 compliance-systems","Self-Audits \u2014 compliance-systems","Penalties \u2014 compliance-systems","Small Business Help \u2014 compliance-systems","Pesticide Applicator Licensing \u2014 compliance-systems","The Env Compliance Calendar \u2014 compliance-systems"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Environmental Regulation Navigation Database — generated study\n"
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
   + "    print('kind: agriculture and environment record')\n"
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
    standards:['agriculture and environment record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Environmental Regulation Navigation Database.',
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
var gen={version:'jahdb-environmental-regulation-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('environmental-regulation-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
