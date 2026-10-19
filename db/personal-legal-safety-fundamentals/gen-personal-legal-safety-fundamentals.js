(function(){'use strict';
/* JAH The Personal Legal Safety Fundamentals Database generator — jahdb-personal-legal-safety-fundamentals-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PLSF-";
var FIELDS=["essential-documents","everyday-protections","legal-hygiene"];
var TOPICS={"essential-documents":["The Essential Document Set \u2014 essential-documents","Durable Power of Attorney \u2014 essential-documents","Identity Protection Habits \u2014 essential-documents","Renting Safely \u2014 essential-documents","Employment Paperwork \u2014 essential-documents","Neighbor Dispute Basics \u2014 essential-documents","Statutes of Limitations \u2014 essential-documents","Guardianship Avoidance \u2014 essential-documents","Travel Legal Prep \u2014 essential-documents","Parenting Legal Basics \u2014 essential-documents","The Annual Legal Checkup \u2014 essential-documents","Notarization Basics \u2014 essential-documents"],"everyday-protections":["Wills: The Minimum \u2014 everyday-protections","Beneficiary Designations \u2014 everyday-protections","What To Do If Arrested \u2014 everyday-protections","Buying a Car Safely \u2014 everyday-protections","Freelancer Legal Basics \u2014 everyday-protections","Insurance You Actually Need \u2014 everyday-protections","Keeping Legal Records \u2014 everyday-protections","Digital Asset Planning \u2014 everyday-protections","Marriage Legal Checklist \u2014 everyday-protections","Aging Parent Legal Prep \u2014 everyday-protections","When to Call a Lawyer \u2014 everyday-protections"],"legal-hygiene":["Healthcare Proxy \u2014 legal-hygiene","Document Storage and Access \u2014 legal-hygiene","Traffic Stop Protocol \u2014 legal-hygiene","Home Buying Legal Basics \u2014 legal-hygiene","Social Media Legal Risks \u2014 legal-hygiene","Lawsuit Basics (If Sued) \u2014 legal-hygiene","Power of Attorney Misuse \u2014 legal-hygiene","Family Emergency Plan \u2014 legal-hygiene","Divorce Protection Basics \u2014 legal-hygiene","Scam Immunity Habits \u2014 legal-hygiene","Jury Duty Basics \u2014 legal-hygiene"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Personal Legal Safety Fundamentals Database — generated study\n"
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
    provenance:'Generated structural sample for the The Personal Legal Safety Fundamentals Database.',
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
var gen={version:'jahdb-personal-legal-safety-fundamentals-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-legal-safety-fundamentals',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
