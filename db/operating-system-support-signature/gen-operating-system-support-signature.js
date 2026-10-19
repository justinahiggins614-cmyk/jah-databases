(function(){'use strict';
/* JAH The Operating System Support Signature Database generator — jahdb-operating-system-support-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OSS-";
var FIELDS=["os-installation","troubleshooting","system-maintenance"];
var TOPICS={"os-installation":["Signature Choosing an Operating System (Signature Edition) \u2014 os-installation","Signature OS Update Strategy (Signature Edition) \u2014 os-installation","Signature RAM Upgrades (Signature Edition) \u2014 os-installation","Signature Boot Failure Recovery (Signature Edition) \u2014 os-installation","Signature Disk Space Management (Signature Edition) \u2014 os-installation","Signature Firewall Basics (Signature Edition) \u2014 os-installation","Signature Windows Maintenance (Signature Edition) \u2014 os-installation","Signature Wi-Fi vs OS Issues (Signature Edition) \u2014 os-installation","Signature Encryption (BitLocker/FileVault) (Signature Edition) \u2014 os-installation","Signature OS End-of-Life Planning (Signature Edition) \u2014 os-installation","Signature Multi-Monitor Setup (Signature Edition) \u2014 os-installation","Signature OS Support Cheat Sheet (Signature Edition) \u2014 os-installation"],"troubleshooting":["Signature Clean OS Installation (Signature Edition) \u2014 troubleshooting","Signature Slow Computer Diagnosis (Signature Edition) \u2014 troubleshooting","Signature Driver Management (Signature Edition) \u2014 troubleshooting","Signature Malware Removal (Signature Edition) \u2014 troubleshooting","Signature Startup Program Control (Signature Edition) \u2014 troubleshooting","Signature Linux for Beginners (Signature Edition) \u2014 troubleshooting","Signature Mobile OS Care (Signature Edition) \u2014 troubleshooting","Signature File Recovery Basics (Signature Edition) \u2014 troubleshooting","Signature Remote Desktop Setup (Signature Edition) \u2014 troubleshooting","Signature Accessibility Settings (Signature Edition) \u2014 troubleshooting","Signature Power Management (Signature Edition) \u2014 troubleshooting"],"system-maintenance":["Signature Dual Booting (Signature Edition) \u2014 system-maintenance","Signature SSD Upgrade Guide (Signature Edition) \u2014 system-maintenance","Signature Blue Screen / Kernel Panic (Signature Edition) \u2014 system-maintenance","Signature Backup Systems (3-2-1) (Signature Edition) \u2014 system-maintenance","Signature User Account Security (Signature Edition) \u2014 system-maintenance","Signature macOS Maintenance (Signature Edition) \u2014 system-maintenance","Signature Printer Troubleshooting (Signature Edition) \u2014 system-maintenance","Signature Password Manager Setup (Signature Edition) \u2014 system-maintenance","Signature Virtual Machines (Signature Edition) \u2014 system-maintenance","Signature Parental Controls (Signature Edition) \u2014 system-maintenance","Signature The Annual OS Tune-Up (Signature Edition) \u2014 system-maintenance"]};
var KINDS="software and IT-support record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Operating System Support Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['software and IT-support record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Operating System Support Signature Database.',
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
var gen={version:'jahdb-operating-system-support-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('operating-system-support-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
