(function(){'use strict';
/* JAH The Software Registries Database generator — jahdb-software-registries-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-REG-";
var FIELDS=["repository"];
var TOPICS={
 "repository": [
  "Package Registries \u2014 repository",
  "Container Registries \u2014 repository",
  "Model Registries \u2014 repository",
  "Schema Registries \u2014 repository",
  "Artifact Repositories \u2014 repository",
  "Source Repositories \u2014 repository",
  "Binary Repositories \u2014 repository",
  "Helm Repositories \u2014 repository",
  "Terraform Registries \u2014 repository",
  "Secret Vaults \u2014 repository",
  "Key Vaults \u2014 repository",
  "Certificate Stores \u2014 repository",
  "Dataset Registries \u2014 repository",
  "Font Registries \u2014 repository",
  "Icon Libraries \u2014 repository",
  "Theme Registries \u2014 repository",
  "Plugin Marketplaces \u2014 repository",
  "Template Galleries \u2014 repository",
  "Snippet Libraries \u2014 repository",
  "Documentation Hubs \u2014 repository",
  "API Catalogs \u2014 repository",
  "Service Catalogs \u2014 repository",
  "Data Catalogs \u2014 repository",
  "Feature Stores \u2014 repository",
  "Experiment Registries \u2014 repository",
  "Pipeline Registries \u2014 repository",
  "Workflow Registries \u2014 repository",
  "Policy Libraries \u2014 repository",
  "Compliance Repositories \u2014 repository",
  "Backup Catalogs \u2014 repository",
  "Archive Repositories \u2014 repository",
  "Media Libraries \u2014 repository",
  "Asset Managers \u2014 repository",
  "Configuration Repositories \u2014 repository",
  "Infrastructure Registries \u2014 repository",
  "Network Inventories \u2014 repository",
  "License Repositories \u2014 repository",
  "Vulnerability Databases \u2014 repository",
  "Threat Intel Feeds \u2014 repository",
  "Signature Databases \u2014 repository",
  "Benchmark Suites \u2014 repository",
  "Test Data Repositories \u2014 repository",
  "Localization Repositories \u2014 repository",
  "Release Repositories \u2014 repository",
  "Staging Repositories \u2014 repository",
  "Snapshot Repositories \u2014 repository",
  "Mirror Repositories \u2014 repository",
  "Cache Repositories \u2014 repository",
  "Proxy Repositories \u2014 repository",
  "Virtual Repositories \u2014 repository",
  "Federated Registries \u2014 repository",
  "Air-Gapped Registries \u2014 repository",
  "SBOM Repositories \u2014 repository",
  "Provenance Repositories \u2014 repository",
  "Attestation Stores \u2014 repository",
  "Notary Services \u2014 repository"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Software Registries — "+safe+"\n"
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
    name:topic+' — registry record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A registry record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-software-registries-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('software-registries',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
