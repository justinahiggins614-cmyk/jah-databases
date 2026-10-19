(function(){'use strict';
/* JAH The Data Breach Response Database generator — jahdb-data-breach-response-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DBR-";
var FIELDS=["personal-breach-response","organizational-response","prevention-systems"];
var TOPICS={"personal-breach-response":["First 24 Hours After Discovery \u2014 personal-breach-response","Credit Freeze How-To \u2014 personal-breach-response","Password Reset Protocol \u2014 personal-breach-response","Forensics Preservation \u2014 personal-breach-response","Credit Monitoring Offers \u2014 personal-breach-response","HIPAA Breach Specifics \u2014 personal-breach-response","Breach Tabletop Exercises \u2014 personal-breach-response","Communication During Breach \u2014 personal-breach-response","Small Business Breach Basics \u2014 personal-breach-response","Breach Cost Benchmarks \u2014 personal-breach-response","The Annual Breach Drill \u2014 personal-breach-response","Breach Response for Families \u2014 personal-breach-response"],"organizational-response":["Breach Notification Laws \u2014 organizational-response","Fraud Alert vs Freeze \u2014 organizational-response","Phishing Surge After Breaches \u2014 organizational-response","Breach Coach and Legal Privilege \u2014 organizational-response","Ransomware Response \u2014 organizational-response","GDPR Breach (72 Hours) \u2014 organizational-response","Cyber Insurance Claims \u2014 organizational-response","Dark Web Monitoring \u2014 organizational-response","Breach Prevention Controls \u2014 organizational-response","Regulatory Investigation Prep \u2014 organizational-response","Personal Data Minimization \u2014 organizational-response"],"prevention-systems":["Personal Breach Checklist \u2014 prevention-systems","Identity Theft Recovery Plan \u2014 prevention-systems","Organizational IR Plan \u2014 prevention-systems","Customer Notification Letters \u2014 prevention-systems","Third-Party Breach (Vendor) \u2014 prevention-systems","State AG Coordination \u2014 prevention-systems","Post-Breach Remediation \u2014 prevention-systems","Insider Breach Response \u2014 prevention-systems","Incident Log Template \u2014 prevention-systems","Customer Trust Rebuilding \u2014 prevention-systems","Breach News: Reading It Right \u2014 prevention-systems"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Breach Response Database — generated study\n"
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
    provenance:'Generated structural sample for the The Data Breach Response Database.',
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
var gen={version:'jahdb-data-breach-response-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-breach-response',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
