(function(){'use strict';
/* JAH The Virology Signature Database generator — jahdb-virology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Virus: The Minimal Infectious Agent (Signature Edition) \u2014 Foundations",
  "Virus Structure: Capsids, Envelopes, and Genomes (Signature Edition) \u2014 Foundations",
  "Viruses Are Not Cells: Viruses vs Bacteria vs Living Cells (Signature Edition) \u2014 Foundations",
  "Viral Genomes: DNA, RNA, Single and Double Stranded (Signature Edition) \u2014 Foundations",
  "The Baltimore Classification: Seven Ways to Be a Virus (Signature Edition) \u2014 Foundations",
  "Measuring Viruses: Size, Scale, and Microscopy (Signature Edition) \u2014 Foundations",
  "Virus Taxonomy: The ICTV Orders and Families (Signature Edition) \u2014 Foundations",
  "Host Range and Tropism: Why Viruses Infect What They Infect (Signature Edition) \u2014 Foundations",
  "How Viruses Spread: Transmission Routes (Signature Edition) \u2014 Foundations",
  "The Lytic Cycle: Hijack, Copy, Burst (Signature Edition) \u2014 Foundations",
  "The Lysogenic Cycle: The Quiet Integration (Signature Edition) \u2014 Foundations",
  "Viral Entry: Attachment, Fusion, and Uncoating (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Replication Strategies of the Seven Baltimore Classes (Signature Edition) \u2014 Compounded",
  "Reverse Transcription: RNA Turned Back into DNA (Signature Edition) \u2014 Compounded",
  "RNA-Dependent RNA Polymerase: The Virus's Copy Machine (Signature Edition) \u2014 Compounded",
  "Viral Assembly and Budding: Building New Virions (Signature Edition) \u2014 Compounded",
  "Bacteriophages: Viruses That Hunt Bacteria (Signature Edition) \u2014 Compounded",
  "Plant Viruses: TMV and the Green World (Signature Edition) \u2014 Compounded",
  "Animal Viruses: From Pets to Livestock to Wildlife (Signature Edition) \u2014 Compounded",
  "Human Respiratory Viruses: Flu, Coronaviruses, and Colds (Signature Edition) \u2014 Compounded",
  "Emerging Viruses and Zoonotic Spillover (Signature Edition) \u2014 Compounded",
  "Viral Evolution and Quasispecies (Signature Edition) \u2014 Compounded",
  "Viral Latency: Herpesviruses and the Long Game (Signature Edition) \u2014 Compounded",
  "Oncogenic Viruses: When Viruses Cause Cancer (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Virus Diagnostics: PCR, Serology, Culture, and Sequencing (Signature Edition) \u2014 Advanced",
  "Viral Vaccines: Platforms from Inactivated to mRNA (Signature Edition) \u2014 Advanced",
  "Antivirals: Drugs That Stop Viruses (Signature Edition) \u2014 Advanced",
  "Epidemiology of Viral Disease: R0 and Herd Immunity (Signature Edition) \u2014 Advanced",
  "Virology Lab Techniques: Plaque Assays, Culture, and Biosafety (Signature Edition) \u2014 Advanced",
  "Viral Vectors and Gene Therapy (Signature Edition) \u2014 Advanced",
  "Giant Viruses and Virophages (Signature Edition) \u2014 Advanced",
  "Endogenous Retroviruses: Viral Fossils in Our DNA (Signature Edition) \u2014 Advanced",
  "Viral Metagenomics: Discovering Viruses by Sequencing (Signature Edition) \u2014 Advanced",
  "Pandemic Preparedness and Viral Surveillance (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Virology Study — "+safe+"\n"
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
    name:topic+' — virology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A virology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"virology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-virology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('virology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
