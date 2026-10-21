(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["access", "monitoring", "integrity", "response", "governance"];
var PREFIX='JAH-SSCV-S-';
var USE="Used by security assessors, auditors, and system owners preparing for authorization.";
var FLD=[["control", "Control"], ["family", "Family"], ["method", "Method"]];
var DEMO="# {title} - control coverage (python3)\nimpl={d1}\ntotal={d2}\ntarget={d3}\npct=100.0*impl/total\nprint(\"controls implemented: %d/%d (%.1f%%)\" % (impl, total, pct))\nprint(\"AUTHORIZATION-READY\" if pct >= target else \"GAPS REMAIN\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["access", "Access Control Policy", "Defines who can access what, enforced by technical, administrative, and physical means.", "Access Control Policy", "AC", "examine policy, test enforcement", "18", "20", "90.0"], ["monitoring", "Audit Logging", "Records security-relevant events with tamper-evident storage and regular review.", "Audit Logging", "AU", "examine logs, interview admins", "14", "16", "85.0"], ["integrity", "Configuration Management", "Baselines configurations and controls changes to prevent drift and shadow IT.", "Configuration Management", "CM", "examine baselines, test change tickets", "16", "18", "85.0"], ["response", "Contingency Planning", "Maintains backup, recovery, and continuity plans tested on schedule.", "Contingency Planning", "CP", "examine plans, test restore", "9", "12", "75.0"], ["governance", "Identification and Authentication", "Verifies identities with MFA before granting access to systems.", "Identification and Authentication", "IA", "test login flows", "12", "14", "85.0"], ["access", "Incident Response", "Detects, contains, and learns from security incidents with defined roles.", "Incident Response", "IR", "examine playbooks, tabletop test", "10", "12", "80.0"], ["monitoring", "Maintenance", "Controls who services systems and what tools they may introduce.", "Maintenance", "MA", "examine records", "6", "8", "75.0"], ["integrity", "Media Protection", "Protects backup and removable media from disclosure and tampering.", "Media Protection", "MP", "examine handling logs", "7", "9", "75.0"], ["response", "Physical Protection", "Secures facilities with barriers, monitoring, and visitor control.", "Physical Protection", "PE", "inspect site", "15", "18", "80.0"], ["governance", "Planning", "Documents security architecture and rules of behavior for the system.", "Planning", "PL", "examine plan", "5", "6", "80.0"], ["access", "Personnel Security", "Screens personnel and manages onboarding, transfer, and termination.", "Personnel Security", "PS", "examine HR records", "7", "8", "85.0"], ["monitoring", "Risk Assessment", "Identifies and evaluates risks on a defined cadence and after changes.", "Risk Assessment", "RA", "examine assessments", "6", "7", "85.0"], ["integrity", "System Services Acquisition", "Bakes security requirements into procurement and development contracts.", "System Services Acquisition", "SA", "examine contracts", "8", "10", "80.0"], ["response", "Communications Protection", "Protects data in transit and at rest with approved cryptography.", "Communications Protection", "SC", "test TLS configs", "19", "22", "85.0"], ["governance", "Information Integrity", "Detects and corrects unauthorized changes with integrity checking.", "Information Integrity", "SI", "test file integrity", "16", "19", "80.0"], ["access", "Awareness Training", "Trains users to recognize phishing and handle data safely.", "Awareness Training", "AT", "examine training records", "4", "5", "80.0"], ["monitoring", "Assessment and Authorization", "Performs independent assessment before authorizing system operation.", "Assessment and Authorization", "CA", "examine SAR", "8", "9", "85.0"], ["integrity", "Program Management", "Runs the organization-wide security program with metrics and oversight.", "Program Management", "PM", "examine metrics", "13", "15", "85.0"], ["response", "PII Processing", "Minimizes and protects personally identifiable information.", "PII Processing", "PT", "examine data flows", "6", "8", "75.0"], ["governance", "Supply Chain Protection", "Vets suppliers and components against tampering and counterfeits.", "Supply Chain Protection", "SR", "examine SBOMs", "11", "14", "75.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-software-security-control-verification-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('software-security-control-verification-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
