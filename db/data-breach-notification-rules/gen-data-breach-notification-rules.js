(function(){'use strict';
/* JAH The Data Breach Notification Rules Database generator — jahdb-data-breach-notification-rules-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DBNR-";
var FIELDS=["notification-timelines","notice-content-rules","regulator-coordination"];
var TOPICS={"notification-timelines":["The 50-State Patchwork \u2014 notification-timelines","The Notification Playbook \u2014 notification-timelines","AG Notifications \u2014 notification-timelines","HHS Portal Filing \u2014 notification-timelines","FTC Safeguards \u2014 notification-timelines","Delayed Notification (Law Enforcement) \u2014 notification-timelines","Call Center Prep \u2014 notification-timelines","Internal Notifications \u2014 notification-timelines","Penalty Avoidance \u2014 notification-timelines","Ransomware Notification \u2014 notification-timelines","Tabletop: Notification Drill \u2014 notification-timelines","The Compliant Notifier \u2014 notification-timelines"],"notice-content-rules":["Notification Triggers \u2014 notice-content-rules","Content Requirements \u2014 notice-content-rules","Credit Bureau Notice \u2014 notice-content-rules","GDPR 72-Hour Rule \u2014 notice-content-rules","State-Specific Quirks \u2014 notice-content-rules","Vendor Breach Notices \u2014 notice-content-rules","Website Notice Pages \u2014 notice-content-rules","Board Notifications \u2014 notice-content-rules","Multi-State Matrix \u2014 notice-content-rules","Phishing-Related Notices \u2014 notice-content-rules","Post-Notification Monitoring \u2014 notice-content-rules"],"regulator-coordination":["Timeline Rules \u2014 regulator-coordination","Plain Language Notices \u2014 regulator-coordination","HIPAA 60-Day Rule \u2014 regulator-coordination","SEC 4-Day Rule \u2014 regulator-coordination","Substitute Notice \u2014 regulator-coordination","Consumer Remedies Offered \u2014 regulator-coordination","Media Strategy \u2014 regulator-coordination","Documenting Compliance \u2014 regulator-coordination","International Notices \u2014 regulator-coordination","Notice Templates \u2014 regulator-coordination","Annual Notification Review \u2014 regulator-coordination"]};
var KINDS="security and resilience record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Breach Notification Rules Database — generated study\n"
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
   + "    print('kind: security and resilience record')\n"
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
    standards:['security and resilience record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Data Breach Notification Rules Database.',
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
var gen={version:'jahdb-data-breach-notification-rules-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-breach-notification-rules',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
