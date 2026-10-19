(function(){'use strict';
/* JAH The Portable Computing Compatibility Database generator — jahdb-portable-computing-compatibility-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCC-";
var FIELDS=["cross-platform-compatibility","peripheral-compatibility","mobile-workflows"];
var TOPICS={"cross-platform-compatibility":["OS Compatibility Basics \u2014 cross-platform-compatibility","The Compatibility Playbook \u2014 cross-platform-compatibility","Virtual Machines Portable \u2014 cross-platform-compatibility","PWAs \u2014 cross-platform-compatibility","External Monitors \u2014 cross-platform-compatibility","Storage Compatibility \u2014 cross-platform-compatibility","Battery Optimization \u2014 cross-platform-compatibility","VPN on the Go \u2014 cross-platform-compatibility","Device Encryption \u2014 cross-platform-compatibility","Tablet Workflows \u2014 cross-platform-compatibility","Security on the Road \u2014 cross-platform-compatibility","Future-Proofing \u2014 cross-platform-compatibility"],"peripheral-compatibility":["App Compatibility Layers \u2014 peripheral-compatibility","ARM vs x86 \u2014 peripheral-compatibility","Containers Portable \u2014 peripheral-compatibility","USB-C Everything \u2014 peripheral-compatibility","Bluetooth Peripherals \u2014 peripheral-compatibility","Cloud Sync \u2014 peripheral-compatibility","Power Banks \u2014 peripheral-compatibility","Mobile Hotspots \u2014 peripheral-compatibility","Find My Devices \u2014 peripheral-compatibility","Phone as Computer \u2014 peripheral-compatibility","The Portable Setup \u2014 peripheral-compatibility"],"mobile-workflows":["File Format Compatibility \u2014 mobile-workflows","Apple Silicon Transition \u2014 mobile-workflows","Web Apps Everywhere \u2014 mobile-workflows","Docking Stations \u2014 mobile-workflows","Printer Compatibility \u2014 mobile-workflows","Offline Workflows \u2014 mobile-workflows","Travel Adapters \u2014 mobile-workflows","eSIM Travel \u2014 mobile-workflows","Backup on the Go \u2014 mobile-workflows","Ergonomics Portable \u2014 mobile-workflows","Compatibility Testing \u2014 mobile-workflows"]};
var KINDS="advanced planning and systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Portable Computing Compatibility Database — generated study\n"
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
   + "    print('kind: advanced planning and systems record')\n"
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
    standards:['advanced planning and systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Portable Computing Compatibility Database.',
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
var gen={version:'jahdb-portable-computing-compatibility-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('portable-computing-compatibility',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
