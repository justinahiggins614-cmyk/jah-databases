(function(){'use strict';
/* JAH The Taxonomy Signature Database generator — jahdb-taxonomy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Taxonomy: The Science of Naming and Classifying Life (Signature Edition) \u2014 Foundations",
  "The Taxonomic Ranks: From Domain to Subspecies (Signature Edition) \u2014 Foundations",
  "Binomial Nomenclature: The Two-Name Rule (Signature Edition) \u2014 Foundations",
  "Carl Linnaeus and the Systema Naturae (Signature Edition) \u2014 Foundations",
  "Kingdoms and Domains: The Deepest Branches (Signature Edition) \u2014 Foundations",
  "Type Specimens: The Physical Anchor of a Name (Signature Edition) \u2014 Foundations",
  "Synonymy and Priority: One Name to Rule Them (Signature Edition) \u2014 Foundations",
  "How to Read a Scientific Name (Signature Edition) \u2014 Foundations",
  "Monographs, Floras, and Faunas: The Reference Shelf (Signature Edition) \u2014 Foundations",
  "Natural History Museums: The Archives of Life (Signature Edition) \u2014 Foundations",
  "Common Names vs Scientific Names (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Phylogenetics: Trees from Data (Signature Edition) \u2014 Compounded",
  "Cladistics: Shared Derived Characters (Signature Edition) \u2014 Compounded",
  "Monophyly, Paraphyly, Polyphyly: The Three Kinds of Groups (Signature Edition) \u2014 Compounded",
  "Morphology-Based Systematics: Reading Bodies (Signature Edition) \u2014 Compounded",
  "Molecular Systematics: DNA Tells the Tree (Signature Edition) \u2014 Compounded",
  "DNA Barcoding: A Scanner for Species (Signature Edition) \u2014 Compounded",
  "The Nomenclature Codes: ICZN, ICNafp, ICNP (Signature Edition) \u2014 Compounded",
  "Taxonomic Revisions: Splits, Lumps, and Moves (Signature Edition) \u2014 Compounded",
  "Species Concepts: What Counts as a Species (Signature Edition) \u2014 Compounded",
  "Dichotomous Keys: Identification by Decision Tree (Signature Edition) \u2014 Compounded",
  "Biodiversity Informatics: GBIF, Darwin Core, and the Data Layer (Signature Edition) \u2014 Compounded",
  "Reading Phylogenetic Trees: Nodes, Branches, and Roots (Signature Edition) \u2014 Compounded",
  "Tree Inference: Parsimony, Likelihood, and Bayesian Methods (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Phylogenomics: Trees from Hundreds of Genes (Signature Edition) \u2014 Advanced",
  "The Molecular Clock: Dating the Tree (Signature Edition) \u2014 Advanced",
  "Cryptic Species: Hidden Diversity in Plain Sight (Signature Edition) \u2014 Advanced",
  "Taxonomic Splits and Conservation: Counting What Counts (Signature Edition) \u2014 Advanced",
  "Integrative Taxonomy: Many Lines of Evidence (Signature Edition) \u2014 Advanced",
  "ZooBank and Digital Registration: Names on the Record (Signature Edition) \u2014 Advanced",
  "Describing a New Species: Alpha Taxonomy in Practice (Signature Edition) \u2014 Advanced",
  "The Taxonomic Impediment: Too Few Taxonomists, Too Many Species (Signature Edition) \u2014 Advanced",
  "Automated Identification: Machine Vision for Taxonomy (Signature Edition) \u2014 Advanced",
  "eDNA and Metagenomics: Taxonomy Without Specimens (Signature Edition) \u2014 Advanced",
  "The PhyloCode: Naming Clades Instead of Ranks (Signature Edition) \u2014 Advanced",
  "Building Taxonomic Databases: Standards and Schemas (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Taxonomy Study — "+safe+"\n"
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
    name:topic+' — taxonomy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A taxonomy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"taxonomy-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-taxonomy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('taxonomy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
