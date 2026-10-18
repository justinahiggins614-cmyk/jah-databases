(function(){'use strict';
/* JAH The Data Exchange and Interoperability Standards Signature Database generator — jahdb-data-exchange-interoperability-standards-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEISS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Interoperability Is: Systems That Talk (Signature Edition) \u2014 Foundations",
  "Data Formats for Exchange: JSON, XML, CSV (Signature Edition) \u2014 Foundations",
  "Character Encodings: UTF-8 Everywhere (Signature Edition) \u2014 Foundations",
  "Identifiers: UUIDs, DOIs, and URIs (Signature Edition) \u2014 Foundations",
  "Schemas: Contracts for Data Shape (Signature Edition) \u2014 Foundations",
  "JSON Schema in Practice (Signature Edition) \u2014 Foundations",
  "Serialization: Bytes on the Wire (Signature Edition) \u2014 Foundations",
  "Delimited Text Done Right: CSV Rules (Signature Edition) \u2014 Foundations",
  "Timestamps and Timezones in Exchange (ISO 8601) (Signature Edition) \u2014 Foundations",
  "Units in Data Exchange: QUDT (Signature Edition) \u2014 Foundations",
  "Nulls and Missing Values Across Systems (Signature Edition) \u2014 Foundations",
  "Versioning Data Formats (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "REST API Contracts (Signature Edition) \u2014 Compounded",
  "OpenAPI: Describing the Contract (Signature Edition) \u2014 Compounded",
  "Identifiers That Last: DOI, ORCID, ARK (Signature Edition) \u2014 Compounded",
  "XML, XSD, and Namespaces (Signature Edition) \u2014 Compounded",
  "Binary Serialization: Avro and Protocol Buffers (Signature Edition) \u2014 Compounded",
  "ETL: Extract, Transform, Load (Signature Edition) \u2014 Compounded",
  "Field Mapping and Compatibility Tables (Signature Edition) \u2014 Compounded",
  "API Versioning Strategies (Signature Edition) \u2014 Compounded",
  "Error Handling and Status Codes (Signature Edition) \u2014 Compounded",
  "Pagination for Large Result Sets (Signature Edition) \u2014 Compounded",
  "Authentication for Data Exchange (Signature Edition) \u2014 Compounded",
  "Webhooks and Event-Driven Exchange (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Ontologies and Shared Vocabularies (Signature Edition) \u2014 Advanced",
  "Linked Data and RDF (Signature Edition) \u2014 Advanced",
  "Schema Evolution: Compatible Changes (Signature Edition) \u2014 Advanced",
  "Compatibility Mappings Between Standards (Signature Edition) \u2014 Advanced",
  "Data Quality Gates in Pipelines (Signature Edition) \u2014 Advanced",
  "Master Data Management (Signature Edition) \u2014 Advanced",
  "Exchange Auditing and Provenance (Signature Edition) \u2014 Advanced",
  "High-Volume Streaming Exchange (Signature Edition) \u2014 Advanced",
  "FHIR: Healthcare Exchange Case Study (Signature Edition) \u2014 Advanced",
  "The Interoperability Test Suite: Proving It Works (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Data Exchange — "+safe+"\n"
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
    name:topic+' — interoperability standard record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A interoperability standard record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"data-exchange-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-data-exchange-interoperability-standards-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-exchange-interoperability-standards-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
