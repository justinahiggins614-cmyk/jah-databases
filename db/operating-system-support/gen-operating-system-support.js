(function(){'use strict';
/* JAH The Operating System Support Database generator — jahdb-operating-system-support-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OSS-";
var FIELDS=["os-installation","troubleshooting","system-maintenance"];
var TOPICS={"os-installation":["Choosing an Operating System \u2014 os-installation","OS Update Strategy \u2014 os-installation","RAM Upgrades \u2014 os-installation","Boot Failure Recovery \u2014 os-installation","Disk Space Management \u2014 os-installation","Firewall Basics \u2014 os-installation","Windows Maintenance \u2014 os-installation","Wi-Fi vs OS Issues \u2014 os-installation","Encryption (BitLocker/FileVault) \u2014 os-installation","OS End-of-Life Planning \u2014 os-installation","Multi-Monitor Setup \u2014 os-installation","OS Support Cheat Sheet \u2014 os-installation"],"troubleshooting":["Clean OS Installation \u2014 troubleshooting","Slow Computer Diagnosis \u2014 troubleshooting","Driver Management \u2014 troubleshooting","Malware Removal \u2014 troubleshooting","Startup Program Control \u2014 troubleshooting","Linux for Beginners \u2014 troubleshooting","Mobile OS Care \u2014 troubleshooting","File Recovery Basics \u2014 troubleshooting","Remote Desktop Setup \u2014 troubleshooting","Accessibility Settings \u2014 troubleshooting","Power Management \u2014 troubleshooting"],"system-maintenance":["Dual Booting \u2014 system-maintenance","SSD Upgrade Guide \u2014 system-maintenance","Blue Screen / Kernel Panic \u2014 system-maintenance","Backup Systems (3-2-1) \u2014 system-maintenance","User Account Security \u2014 system-maintenance","macOS Maintenance \u2014 system-maintenance","Printer Troubleshooting \u2014 system-maintenance","Password Manager Setup \u2014 system-maintenance","Virtual Machines \u2014 system-maintenance","Parental Controls \u2014 system-maintenance","The Annual OS Tune-Up \u2014 system-maintenance"]};
var KINDS="software and IT-support record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Operating System Support Database — generated study\n"
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
    provenance:'Generated structural sample for the The Operating System Support Database.',
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
var gen={version:'jahdb-operating-system-support-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('operating-system-support',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
