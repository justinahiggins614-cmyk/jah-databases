(function(){'use strict';
/* JAH The Archival Preservation and Digital Obsolescence Database generator — jahdb-archival-preservation-digital-obsolescence-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-APDO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Digital Preservation Is: Keeping Bits Meaningful \u2014 Foundations",
  "Bit Rot and Media Decay: The Slow Enemies \u2014 Foundations",
  "Checksums and Fixity: Proving Nothing Changed \u2014 Foundations",
  "The Checksum Manifest: SHA-256 Inventories \u2014 Foundations",
  "File Formats: Open Beats Proprietary \u2014 Foundations",
  "Format Registries: PRONOM and Identification \u2014 Foundations",
  "The OAIS Model: ISO 14721 Reference \u2014 Foundations",
  "SIPs, AIPs, DIPs: Packages Through the Lifecycle \u2014 Foundations",
  "Redundancy: Multiple Copies, Multiple Places \u2014 Foundations",
  "Backup vs Archiving: Last Tuesday vs 2076 \u2014 Foundations",
  "Metadata for Preservation: PREMIS Basics \u2014 Foundations",
  "The Designated Community: Preserving For Whom \u2014 Foundations"
 ],
 "Compounded": [
  "Format Obsolescence: How Formats Die \u2014 Compounded",
  "Obsolescence Risk Scoring \u2014 Compounded",
  "Migration: Moving Content to New Formats \u2014 Compounded",
  "Emulation: Running Old Software Forever \u2014 Compounded",
  "Normalization: One Archival Format Per Type \u2014 Compounded",
  "Fixity Checking Schedules \u2014 Compounded",
  "Repair from Redundant Copies \u2014 Compounded",
  "LOCKSS: Lots of Copies Keep Stuff Safe \u2014 Compounded",
  "PREMIS in Depth: Objects, Events, Agents, Rights \u2014 Compounded",
  "Preservation Metadata in Practice \u2014 Compounded",
  "Disaster Planning for Archives \u2014 Compounded",
  "Succession Planning: Surviving the Founders \u2014 Compounded"
 ],
 "Advanced": [
  "Format-Migration Plans: The Full Playbook \u2014 Advanced",
  "Significant Properties: What Must Survive Migration \u2014 Advanced",
  "Validation After Migration: Proving Fidelity \u2014 Advanced",
  "Checksum Manifests at Scale \u2014 Advanced",
  "Recovery Procedures: The Full Drill \u2014 Advanced",
  "Forensic Recovery: Reading Dead Media \u2014 Advanced",
  "Cryptographic Timestamping: Proving When \u2014 Advanced",
  "Preservation Cost Modeling \u2014 Advanced",
  "Auditing Archives: TRAC and ISO 16363 \u2014 Advanced",
  "The 100-Year Archive: Designing for Deep Time \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Digital Preservation — "+safe+"\n"
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
    name:topic+' — digital preservation record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A digital preservation record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"digital-preservation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-archival-preservation-digital-obsolescence-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archival-preservation-digital-obsolescence',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
