(function(){'use strict';
/* JAH The Nanotoxicology Database generator — jahdb-nanotoxicology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NTX-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Nanotoxicology: The Engineering of Nanoscale Hazard and Safety - Foundations",
  "Dose Metrics: Mass, Surface Area, and Particle Number - Foundations",
  "Exposure Routes: Inhalation, Dermal, and Ingestion - Foundations",
  "The Nanoparticle's Journey: Translocation From Contact to Target Organ - Foundations",
  "Oxidative Stress and ROS: The Common Toxicity Pathway - Foundations",
  "Titanium Dioxide Nanoparticles: The Most Studied Case - Foundations",
  "Silver Nanoparticles: Ion Release and the Antimicrobial Trade-Off - Foundations",
  "Zinc Oxide Nanoparticles: Sunscreens, Band Gaps, and Dissolution - Foundations",
  "Quantum Dots: Capped Heavy Metals in Bright Packages - Foundations",
  "Nanoplastics: Fragmentation and the Particle-Number Explosion - Foundations"
 ],
 "Compounded": [
  "Carbon Nanotubes: The Fiber Paradigm and the Asbestos Analogy - Compounded",
  "Graphene and Graphene Oxide: Sheets With Sharp Edges - Compounded",
  "The Protein Corona: A Nanoparticle's Biological Identity - Compounded",
  "In Vitro Screening: The Tier-1 Assay Toolbox - Compounded",
  "When Nanoparticles Lie to the Assay: Interference and Artifacts - Compounded",
  "In Vivo Testing: Biokinetics and Lung Burden in Animal Models - Compounded",
  "Pulmonary Clearance: Macrophages and the Overload Line - Compounded",
  "Genotoxicity: DNA Damage at the Nanoscale - Compounded",
  "The Immune Response: Inflammation Cascades and the Cytokine Signal - Compounded",
  "Dermal Exposure: What Crosses the Skin Barrier - Compounded",
  "Oral Exposure: The Gut Barrier and Food Contact - Compounded"
 ],
 "Advanced": [
  "Biomarkers and Omics: Reading the Molecular Response - Advanced",
  "NIOSH CIB 65: The Carbon Nanotube Exposure Limit - Advanced",
  "OECD Test Guidelines: The Harmonized Testing Suite - Advanced",
  "REACH Nanoforms: Europe's Registration Rules - Advanced",
  "EPA TSCA: America's Nanoscale Reporting Rules - Advanced",
  "ISO/TS 12901: The Control Banding Standard - Advanced",
  "Safer by Design: Engineering the Hazard Out - Advanced",
  "Surface Chemistry as the Safety Dial: Coatings, Charge, and PEGylation - Advanced",
  "Exposure Modeling: From Emission to Breathing Zone - Advanced",
  "PPE and Engineering Controls: Hoods, Respirators, and Containment - Advanced",
  "Lifecycle Thinking: From Synthesis to End of Life - Advanced",
  "Risk Assessment Arithmetic: Hazard Times Exposure - Advanced",
  "The Future of Nanotoxicology: Pathways and New Approach Methods - Advanced"
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
var gen={version:'jahdb-nanotoxicology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanotoxicology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
