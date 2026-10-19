(function(){'use strict';
/* JAH Fundamentals of Bioinformatics Database generator — jahdb-fundamental-bioinformatics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIO-";
var FIELDS=["sequences", "alignment", "genome assembly", "phylogenetics", "gene finding", "protein structure"];
var TOPICS=[
    {t: "DNA as a String", b: "Genomes are strings over a 4-letter alphabet; bioinformatics is string algorithms plus statistics applied to biology's text."},
    {t: "Pairwise Alignment", b: "Needleman-Wunsch (global) and Smith-Waterman (local) use dynamic programming to find optimal alignments with gaps and mismatches."},
    {t: "Scoring Matrices", b: "BLOSUM and PAM matrices score amino-acid substitutions by evolutionary likelihood \u2014 chemistry-aware alignment."},
    {t: "BLAST: Fast Searching", b: "BLAST seeds short exact matches then extends: heuristic speed that made the world's sequence databases searchable."},
    {t: "Multiple Sequence Alignment", b: "Aligning families together reveals conserved columns \u2014 functional sites evolution refuses to change."},
    {t: "Genome Assembly", b: "Overlap-layout-consensus and de Bruijn graphs stitch billions of short reads into chromosomes; repeats are the fundamental obstacle."},
    {t: "Variant Calling", b: "Comparing reads to a reference finds SNPs and indels; quality scores, depth, and strand balance separate real variants from errors."},
    {t: "Phylogenetic Trees", b: "Distance, parsimony, and likelihood methods reconstruct evolutionary history; bootstrapping measures branch confidence."},
    {t: "Gene Finding", b: "Hidden Markov models spot start codons, splice sites, and coding regions in raw genomic text \u2014 annotation's core engine."},
    {t: "RNA-seq Analysis", b: "Counting transcripts per gene across conditions reveals differential expression; normalization removes sequencing-depth bias."},
    {t: "Protein Structure Prediction", b: "From homology modeling to deep-learning folders: predicting 3-D shape from sequence, once biology's grand challenge."},
    {t: "Databases and Formats", b: "GenBank, UniProt, and PDB store the world's sequences and structures; FASTA, FASTQ, SAM, and VCF are the working file formats."}
];
var PRINCIPLES=[
    {n: "Sequence identity", e: "identity = matches/length", s: "The fraction of aligned positions that match quantifies similarity."},
    {n: "E-value (BLAST)", e: "E = K\u00b7m\u00b7n\u00b7e^(\u2212\u03bbS)", s: "Expected random hits of a score \u2014 the statistical significance of a match."},
    {n: "Jukes-Cantor distance", e: "d = \u2212\u00be\u00b7ln(1 \u2212 \u2074\u2044\u2083p)", s: "Corrects observed differences for multiple hidden substitutions."}
];
var USES=["Annotating newly sequenced genomes", "Finding disease mutations in patients", "Tracing pathogen outbreak evolution", "Predicting protein drug targets"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Bioinformatics"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Bioinformatics demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-bioinformatics-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-bioinformatics-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-bioinformatics",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
