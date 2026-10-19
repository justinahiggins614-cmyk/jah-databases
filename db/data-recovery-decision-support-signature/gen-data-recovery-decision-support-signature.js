(function(){'use strict';
/* JAH The Data Recovery Decision Support Signature Database generator — jahdb-data-recovery-decision-support-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DRDSS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Data Recovery Decision Support (Signature): How It Works, Simply — foundations",
  "Data Recovery Decision Support (Signature): Setting It Up Right — foundations",
  "Data Recovery Decision Support (Signature): The 5-Minute Health Check — foundations",
  "Data Recovery Decision Support (Signature): Reading Error Messages — foundations",
  "Data Recovery Decision Support (Signature): Logs: Finding Truth — foundations",
  "Data Recovery Decision Support (Signature): Backups Before Changes — foundations",
  "Data Recovery Decision Support (Signature): Updates and Patching — foundations",
  "Data Recovery Decision Support (Signature): Access Control Basics — foundations",
  "Data Recovery Decision Support (Signature): Multi-Factor Everywhere — foundations",
  "Data Recovery Decision Support (Signature): Common Failure Modes — foundations",
  "Data Recovery Decision Support (Signature): Performance Basics — foundations",
  "Data Recovery Decision Support (Signature): Security Hygiene — foundations"
 ],
 "compounded": [
  "Data Recovery Decision Support (Signature): Automation That Pays — compounded",
  "Data Recovery Decision Support (Signature): Documentation That Survives — compounded",
  "Data Recovery Decision Support (Signature): Testing Changes Safely — compounded",
  "Data Recovery Decision Support (Signature): Monitoring and Alerts — compounded",
  "Data Recovery Decision Support (Signature): Disaster Recovery — compounded",
  "Data Recovery Decision Support (Signature): Cost Control — compounded",
  "Data Recovery Decision Support (Signature): Working With Vendors — compounded",
  "Data Recovery Decision Support (Signature): Training Your Team — compounded",
  "Data Recovery Decision Support (Signature): Compliance Basics — compounded",
  "Data Recovery Decision Support (Signature): Incident Response — compounded",
  "Data Recovery Decision Support (Signature): Advanced: Architecture Decisions — compounded",
  "Data Recovery Decision Support (Signature): Advanced: Scaling Under Load — compounded"
 ],
 "advanced": [
  "Data Recovery Decision Support (Signature): Advanced: Zero-Downtime Changes — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Advanced Troubleshooting — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Building the Platform — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Chaos and Resilience — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Cost Optimization Deep — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Leading Technical Teams — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Build vs Buy — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Technical Debt Strategy — advanced",
  "Data Recovery Decision Support (Signature): Advanced: The 10x Reliability Plan — advanced",
  "Data Recovery Decision Support (Signature): Advanced: Teaching the Craft — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Data Recovery Decision Support Signature Database — structural study\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-data-recovery-decision-support-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-recovery-decision-support-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
