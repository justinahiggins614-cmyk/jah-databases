(function(){'use strict';
/* JAH The Continuous Integration and Delivery Signature Database generator — jahdb-continuous-integration-and-delivery-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CIADS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Continuous Integration and Delivery (Signature): How It Works, Simply — foundations",
  "Continuous Integration and Delivery (Signature): Setting It Up Right — foundations",
  "Continuous Integration and Delivery (Signature): The 5-Minute Health Check — foundations",
  "Continuous Integration and Delivery (Signature): Reading Error Messages — foundations",
  "Continuous Integration and Delivery (Signature): Logs: Finding Truth — foundations",
  "Continuous Integration and Delivery (Signature): Backups Before Changes — foundations",
  "Continuous Integration and Delivery (Signature): Updates and Patching — foundations",
  "Continuous Integration and Delivery (Signature): Access Control Basics — foundations",
  "Continuous Integration and Delivery (Signature): Multi-Factor Everywhere — foundations",
  "Continuous Integration and Delivery (Signature): Common Failure Modes — foundations",
  "Continuous Integration and Delivery (Signature): Performance Basics — foundations",
  "Continuous Integration and Delivery (Signature): Security Hygiene — foundations"
 ],
 "compounded": [
  "Continuous Integration and Delivery (Signature): Automation That Pays — compounded",
  "Continuous Integration and Delivery (Signature): Documentation That Survives — compounded",
  "Continuous Integration and Delivery (Signature): Testing Changes Safely — compounded",
  "Continuous Integration and Delivery (Signature): Monitoring and Alerts — compounded",
  "Continuous Integration and Delivery (Signature): Disaster Recovery — compounded",
  "Continuous Integration and Delivery (Signature): Cost Control — compounded",
  "Continuous Integration and Delivery (Signature): Working With Vendors — compounded",
  "Continuous Integration and Delivery (Signature): Training Your Team — compounded",
  "Continuous Integration and Delivery (Signature): Compliance Basics — compounded",
  "Continuous Integration and Delivery (Signature): Incident Response — compounded",
  "Continuous Integration and Delivery (Signature): Advanced: Architecture Decisions — compounded",
  "Continuous Integration and Delivery (Signature): Advanced: Scaling Under Load — compounded"
 ],
 "advanced": [
  "Continuous Integration and Delivery (Signature): Advanced: Zero-Downtime Changes — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Advanced Troubleshooting — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Building the Platform — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Chaos and Resilience — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Cost Optimization Deep — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Leading Technical Teams — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Build vs Buy — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Technical Debt Strategy — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: The 10x Reliability Plan — advanced",
  "Continuous Integration and Delivery (Signature): Advanced: Teaching the Craft — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Continuous Integration and Delivery Signature Database — structural study\n"
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
var gen={version:'jahdb-continuous-integration-and-delivery-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('continuous-integration-and-delivery-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
