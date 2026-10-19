(function(){'use strict';
/* JAH The Secure Configuration Baselines Database generator — jahdb-secure-configuration-baselines-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCB-";
var FIELDS=["os-hardening","network-hardening","baseline-maintenance"];
var TOPICS={"os-hardening":["What Is a Baseline \u2014 os-hardening","Linux Hardening Baseline \u2014 os-hardening","MFA Everywhere Baseline \u2014 os-hardening","Patching Baseline \u2014 os-hardening","Wireless Security Baseline \u2014 os-hardening","Browser Hardening \u2014 os-hardening","Backup Security Baseline \u2014 os-hardening","Encryption Baseline \u2014 os-hardening","Incident Response Mini-Plan \u2014 os-hardening","Compliance Mapping \u2014 os-hardening","The Annual Hardening Review \u2014 os-hardening","IoT Device Hardening \u2014 os-hardening"],"network-hardening":["CIS Benchmarks Intro \u2014 network-hardening","macOS Hardening Baseline \u2014 network-hardening","Account Lockout Policy \u2014 network-hardening","Antivirus/EDR Baseline \u2014 network-hardening","Router Hardening \u2014 network-hardening","USB and Removable Media \u2014 network-hardening","Cloud Config Baseline \u2014 network-hardening","Physical Security Baseline \u2014 network-hardening","Vulnerability Scanning \u2014 network-hardening","Hardening New Devices \u2014 network-hardening","SSH Hardening Deep Dive \u2014 network-hardening"],"baseline-maintenance":["Windows Hardening Baseline \u2014 baseline-maintenance","Password Policy Baseline \u2014 baseline-maintenance","Unnecessary Services Audit \u2014 baseline-maintenance","Firewall Rules Baseline \u2014 baseline-maintenance","Email Security Baseline \u2014 baseline-maintenance","Logging Baseline \u2014 baseline-maintenance","Default Credential Purge \u2014 baseline-maintenance","User Training Baseline \u2014 baseline-maintenance","Baseline Documentation \u2014 baseline-maintenance","Decommissioning Securely \u2014 baseline-maintenance","RDP Hardening \u2014 baseline-maintenance"]};
var KINDS="software and IT-support record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Secure Configuration Baselines Database — generated study\n"
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
   + "    print('kind: software and IT-support record')\n"
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
    standards:['software and IT-support record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Secure Configuration Baselines Database.',
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
var gen={version:'jahdb-secure-configuration-baselines-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('secure-configuration-baselines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
