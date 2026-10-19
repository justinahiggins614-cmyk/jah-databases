(function(){'use strict';
/* JAH The Environmental Regulation Navigation Signature Database generator — jahdb-environmental-regulation-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ERN-";
var FIELDS=["rule-identification","permit-navigation","compliance-systems"];
var TOPICS={"rule-identification":["Signature Which Rules Apply (Signature Edition) \u2014 rule-identification","Signature Clean Air Act Basics (Signature Edition) \u2014 rule-identification","Signature NPDES Permits (Signature Edition) \u2014 rule-identification","Signature RCRA Basics (Signature Edition) \u2014 rule-identification","Signature Endangered Species Act (Signature Edition) \u2014 rule-identification","Signature EPCRA Reporting (Signature Edition) \u2014 rule-identification","Signature State vs Federal (Signature Edition) \u2014 rule-identification","Signature Voluntary Disclosure (Signature Edition) \u2014 rule-identification","Signature Permitting Timelines (Signature Edition) \u2014 rule-identification","Signature Agricultural Exemptions (Signature Edition) \u2014 rule-identification","Signature Record Keeping (Env) (Signature Edition) \u2014 rule-identification","Signature Staying Current (Signature Edition) \u2014 rule-identification"],"permit-navigation":["Signature EPA Organization (Signature Edition) \u2014 permit-navigation","Signature Air Permits (Title V) (Signature Edition) \u2014 permit-navigation","Signature Stormwater Permits (Signature Edition) \u2014 permit-navigation","Signature CERCLA/Superfund (Signature Edition) \u2014 permit-navigation","Signature TSCA (Chemicals) (Signature Edition) \u2014 permit-navigation","Signature SPCC Plans (Signature Edition) \u2014 permit-navigation","Signature Working with Inspectors (Signature Edition) \u2014 permit-navigation","Signature Citizen Suits (Signature Edition) \u2014 permit-navigation","Signature Hiring Env Consultants (Signature Edition) \u2014 permit-navigation","Signature Manure Management Rules (Signature Edition) \u2014 permit-navigation","Signature Training (Env Compliance) (Signature Edition) \u2014 permit-navigation"],"compliance-systems":["Signature The Compliance Playbook (Signature Edition) \u2014 compliance-systems","Signature Clean Water Act Basics (Signature Edition) \u2014 compliance-systems","Signature Wetlands (Section 404) (Signature Edition) \u2014 compliance-systems","Signature NEPA Reviews (Signature Edition) \u2014 compliance-systems","Signature FIFRA (Pesticides) (Signature Edition) \u2014 compliance-systems","Signature Underground Storage Tanks (Signature Edition) \u2014 compliance-systems","Signature Self-Audits (Signature Edition) \u2014 compliance-systems","Signature Penalties (Signature Edition) \u2014 compliance-systems","Signature Small Business Help (Signature Edition) \u2014 compliance-systems","Signature Pesticide Applicator Licensing (Signature Edition) \u2014 compliance-systems","Signature The Env Compliance Calendar (Signature Edition) \u2014 compliance-systems"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Environmental Regulation Navigation Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['agriculture and environment record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Environmental Regulation Navigation Signature Database.',
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
var gen={version:'jahdb-environmental-regulation-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('environmental-regulation-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
