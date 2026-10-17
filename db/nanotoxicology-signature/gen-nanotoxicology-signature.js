(function(){'use strict';
/* JAH The Nanotoxicology Signature Database generator — jahdb-nanotoxicology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Nanotoxicology: The Engineering of Nanoscale Hazard and Safety (Signature Edition) - Foundations",
  "Dose Metrics: Mass, Surface Area, and Particle Number (Signature Edition) - Foundations",
  "Exposure Routes: Inhalation, Dermal, and Ingestion (Signature Edition) - Foundations",
  "The Nanoparticle's Journey: Translocation From Contact to Target Organ (Signature Edition) - Foundations",
  "Oxidative Stress and ROS: The Common Toxicity Pathway (Signature Edition) - Foundations",
  "Titanium Dioxide Nanoparticles: The Most Studied Case (Signature Edition) - Foundations",
  "Silver Nanoparticles: Ion Release and the Antimicrobial Trade-Off (Signature Edition) - Foundations",
  "Zinc Oxide Nanoparticles: Sunscreens, Band Gaps, and Dissolution (Signature Edition) - Foundations",
  "Quantum Dots: Capped Heavy Metals in Bright Packages (Signature Edition) - Foundations",
  "Nanoplastics: Fragmentation and the Particle-Number Explosion (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Carbon Nanotubes: The Fiber Paradigm and the Asbestos Analogy (Signature Edition) - Compounded",
  "Graphene and Graphene Oxide: Sheets With Sharp Edges (Signature Edition) - Compounded",
  "The Protein Corona: A Nanoparticle's Biological Identity (Signature Edition) - Compounded",
  "In Vitro Screening: The Tier-1 Assay Toolbox (Signature Edition) - Compounded",
  "When Nanoparticles Lie to the Assay: Interference and Artifacts (Signature Edition) - Compounded",
  "In Vivo Testing: Biokinetics and Lung Burden in Animal Models (Signature Edition) - Compounded",
  "Pulmonary Clearance: Macrophages and the Overload Line (Signature Edition) - Compounded",
  "Genotoxicity: DNA Damage at the Nanoscale (Signature Edition) - Compounded",
  "The Immune Response: Inflammation Cascades and the Cytokine Signal (Signature Edition) - Compounded",
  "Dermal Exposure: What Crosses the Skin Barrier (Signature Edition) - Compounded",
  "Oral Exposure: The Gut Barrier and Food Contact (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Biomarkers and Omics: Reading the Molecular Response (Signature Edition) - Advanced",
  "NIOSH CIB 65: The Carbon Nanotube Exposure Limit (Signature Edition) - Advanced",
  "OECD Test Guidelines: The Harmonized Testing Suite (Signature Edition) - Advanced",
  "REACH Nanoforms: Europe's Registration Rules (Signature Edition) - Advanced",
  "EPA TSCA: America's Nanoscale Reporting Rules (Signature Edition) - Advanced",
  "ISO/TS 12901: The Control Banding Standard (Signature Edition) - Advanced",
  "Safer by Design: Engineering the Hazard Out (Signature Edition) - Advanced",
  "Surface Chemistry as the Safety Dial: Coatings, Charge, and PEGylation (Signature Edition) - Advanced",
  "Exposure Modeling: From Emission to Breathing Zone (Signature Edition) - Advanced",
  "PPE and Engineering Controls: Hoods, Respirators, and Containment (Signature Edition) - Advanced",
  "Lifecycle Thinking: From Synthesis to End of Life (Signature Edition) - Advanced",
  "Risk Assessment Arithmetic: Hazard Times Exposure (Signature Edition) - Advanced",
  "The Future of Nanotoxicology: Pathways and New Approach Methods (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nanotoxicology Study — "+safe+"\n"
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
    name:topic+' — nanotoxicology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nanotoxicology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nanotoxicology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-nanotoxicology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanotoxicology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
