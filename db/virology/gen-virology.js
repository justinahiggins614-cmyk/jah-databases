(function(){'use strict';
/* JAH The Virology Database generator — jahdb-virology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VIR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Virus: The Minimal Infectious Agent \u2014 Foundations",
  "Virus Structure: Capsids, Envelopes, and Genomes \u2014 Foundations",
  "Viruses Are Not Cells: Viruses vs Bacteria vs Living Cells \u2014 Foundations",
  "Viral Genomes: DNA, RNA, Single and Double Stranded \u2014 Foundations",
  "The Baltimore Classification: Seven Ways to Be a Virus \u2014 Foundations",
  "Measuring Viruses: Size, Scale, and Microscopy \u2014 Foundations",
  "Virus Taxonomy: The ICTV Orders and Families \u2014 Foundations",
  "Host Range and Tropism: Why Viruses Infect What They Infect \u2014 Foundations",
  "How Viruses Spread: Transmission Routes \u2014 Foundations",
  "The Lytic Cycle: Hijack, Copy, Burst \u2014 Foundations",
  "The Lysogenic Cycle: The Quiet Integration \u2014 Foundations",
  "Viral Entry: Attachment, Fusion, and Uncoating \u2014 Foundations"
 ],
 "Compounded": [
  "Replication Strategies of the Seven Baltimore Classes \u2014 Compounded",
  "Reverse Transcription: RNA Turned Back into DNA \u2014 Compounded",
  "RNA-Dependent RNA Polymerase: The Virus's Copy Machine \u2014 Compounded",
  "Viral Assembly and Budding: Building New Virions \u2014 Compounded",
  "Bacteriophages: Viruses That Hunt Bacteria \u2014 Compounded",
  "Plant Viruses: TMV and the Green World \u2014 Compounded",
  "Animal Viruses: From Pets to Livestock to Wildlife \u2014 Compounded",
  "Human Respiratory Viruses: Flu, Coronaviruses, and Colds \u2014 Compounded",
  "Emerging Viruses and Zoonotic Spillover \u2014 Compounded",
  "Viral Evolution and Quasispecies \u2014 Compounded",
  "Viral Latency: Herpesviruses and the Long Game \u2014 Compounded",
  "Oncogenic Viruses: When Viruses Cause Cancer \u2014 Compounded"
 ],
 "Advanced": [
  "Virus Diagnostics: PCR, Serology, Culture, and Sequencing \u2014 Advanced",
  "Viral Vaccines: Platforms from Inactivated to mRNA \u2014 Advanced",
  "Antivirals: Drugs That Stop Viruses \u2014 Advanced",
  "Epidemiology of Viral Disease: R0 and Herd Immunity \u2014 Advanced",
  "Virology Lab Techniques: Plaque Assays, Culture, and Biosafety \u2014 Advanced",
  "Viral Vectors and Gene Therapy \u2014 Advanced",
  "Giant Viruses and Virophages \u2014 Advanced",
  "Endogenous Retroviruses: Viral Fossils in Our DNA \u2014 Advanced",
  "Viral Metagenomics: Discovering Viruses by Sequencing \u2014 Advanced",
  "Pandemic Preparedness and Viral Surveillance \u2014 Advanced"
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
var gen={version:'jahdb-virology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('virology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
