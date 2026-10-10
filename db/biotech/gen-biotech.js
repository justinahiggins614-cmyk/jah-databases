/* ✳ SIGNATURE — JAH Biotechnology Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic client-side generator: same seed + same version => same record.
   Anchor facts (names, years, discoverers, mechanisms) verified from published
   histories of biotechnology; application studies are Signature-generated. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['gene-editing','dna-sequencing','amplification','cloning','gene-therapy','biomanufacturing','synthetic-biology','diagnostics','cell-biology','bioinformatics'];
var PREFIX='JAH-BIO-';
/* [name, category, discoverer, year (0 = era described in text), mechanism, [applications], notable fact] */
var ANCH=[
['CRISPR-Cas9','gene-editing','Emmanuelle Charpentier and Jennifer Doudna',2012,'a bacterial immune system repurposed for editing: a guide RNA leads the Cas9 enzyme to a matching DNA sequence, where Cas9 cuts both DNA strands',['correcting disease-causing mutations','engineering improved crops','building precise disease models'],'Landmark 2012 Science paper; 2020 Nobel Prize in Chemistry.'],
['RNA interference','gene-editing','Andrew Fire and Craig Mello',1998,'double-stranded RNA triggers the destruction of matching messenger RNA, silencing the targeted gene',['functional genomics screens','pest-resistant crops','experimental RNA therapeutics'],'2006 Nobel Prize in Physiology or Medicine.'],
['Sanger sequencing','dna-sequencing','Frederick Sanger',1977,'chain termination: dideoxynucleotides halt DNA synthesis at each base, and the fragment lengths reveal the sequence',['the Human Genome Project','clinical mutation screening','forensic identification'],'Sanger earned his second Nobel Prize in Chemistry in 1980.'],
['Next-generation sequencing','dna-sequencing','field advance (Solexa/Illumina reversible-terminator chemistry)',0,'millions of DNA fragments are sequenced in parallel on a flow cell and assembled by software; emerged in the mid-2000s',['whole-genome sequencing','cancer mutation profiling','pathogen surveillance'],'Drove the cost of a human genome from millions of dollars toward one thousand.'],
['Maxam-Gilbert sequencing','dna-sequencing','Allan Maxam and Walter Gilbert',1977,'chemical cleavage of DNA at specific bases; the pattern of fragments reveals the sequence',['early gene mapping','foundational sequencing research'],'Published alongside Sanger sequencing in 1977.'],
['Polymerase chain reaction','amplification','Kary Mullis',1983,'repeated heating and cooling cycles with primers and DNA polymerase double a target DNA segment each cycle, yielding exponential amplification',['medical diagnostics','forensic DNA analysis','pathogen detection'],'1993 Nobel Prize in Chemistry; invented at Cetus Corporation.'],
['Taq polymerase','amplification','isolated from Thermus aquaticus (Saiki et al.)',1988,'a heat-stable DNA polymerase that survives the high-temperature denaturation step of PCR',['routine PCR','real-time PCR','high-throughput genotyping'],'Its discovery automated PCR and sparked the PCR revolution.'],
['Real-time PCR','amplification','(Higuchi and colleagues)',1992,'fluorescent dyes or probes measure DNA amplification as it happens, quantifying the starting amount of template',['viral load testing','gene expression studies','food safety testing'],'Also called quantitative PCR (qPCR).'],
['Recombinant DNA','cloning','Stanley Cohen and Herbert Boyer',1973,'restriction enzymes cut DNA and DNA ligase joins the fragments, inserting foreign genes into bacterial plasmids',['human insulin production','genetically modified crops','recombinant protein drugs'],'The founding experiment of genetic engineering.'],
['Dolly the sheep','cloning','Ian Wilmut and colleagues, Roslin Institute',1996,'somatic cell nuclear transfer: the nucleus of an adult cell is placed into an enucleated egg, producing a genetic copy',['mammalian developmental biology','livestock breeding research','therapeutic cloning studies'],'The first mammal cloned from an adult somatic cell.'],
['pBR322 plasmid vector','cloning','(Bolivar and Rodriguez)',1977,'an early engineered plasmid carrying antibiotic-resistance markers used to select transformed bacteria',['molecular cloning','gene libraries','recombinant protein expression'],'One of the first widely used cloning vectors.'],
['Gene therapy (ADA-SCID trial)','gene-therapy','(Blaese and Culver, U.S. NIH)',1990,'a working copy of the ADA gene was delivered into the cells of a patient with severe combined immunodeficiency',['inherited immune disorders','hemophilia programs','inherited blindness programs'],'The first federally approved human gene-therapy trial.'],
['mRNA vaccines','gene-therapy','Katalin Kariko and Drew Weissman',2005,'nucleoside-modified messenger RNA instructs human cells to make a target protein, training the immune system without live virus',['COVID-19 vaccines','personalized cancer vaccine trials','protein-replacement research'],'2023 Nobel Prize in Physiology or Medicine.'],
['Prime editing','gene-therapy','(Liu laboratory)',2019,'a Cas9 nickase fused to reverse transcriptase writes a new DNA sequence directly from an RNA template, without double-strand breaks',['precise correction of point mutations','disease modeling','crop trait editing'],'Described as a "search-and-replace" genome editor.'],
['Recombinant human insulin (Humulin)','biomanufacturing','Genentech and Eli Lilly',1982,'the human insulin gene expressed in engineered bacteria; the first recombinant-DNA drug approved by the FDA',['diabetes treatment worldwide','biopharmaceutical manufacturing','protein engineering research'],'The first biotechnology drug to reach the market.'],
['Monoclonal antibodies','biomanufacturing','Georges Kohler and Cesar Milstein',1975,'hybridoma cells, made by fusing antibody-producing B cells with myeloma cells, secrete one identical antibody type in bulk',['cancer immunotherapy','diagnostic tests','preventing organ transplant rejection'],'1984 Nobel Prize; first therapeutic antibody approved by the FDA in 1986.'],
['Industrial fermentation','biomanufacturing','(Aspergillus niger citric-acid process)',1919,'the first large-scale aerobic fermentation process, supplying sterile air to microbial cultures',['food acids','antibiotics','biofuels and enzymes'],'The birth of industrial biotechnology.'],
['BioBricks','synthetic-biology','Tom Knight',2003,'standardized DNA parts with compatible ends that assemble in a defined order, like bricks',['genetic circuit design','biosensors','synthetic biology education'],'Launched the Registry of Standard Biological Parts.'],
['Golden Gate assembly','synthetic-biology','(Engler and colleagues)',2003,'Type IIS restriction enzymes cut outside their recognition sites, allowing scarless one-pot assembly of many DNA parts',['metabolic pathway engineering','plasmid construction','synthetic genomes'],'A cornerstone method of modern DNA assembly.'],
['DNA fingerprinting','diagnostics','Alec Jeffreys',1984,'variable repetitive DNA sequences form a banding pattern effectively unique to each individual',['forensic casework','paternity testing','wildlife identification'],'First criminal conviction on DNA evidence came in 1987.'],
['Southern blot','diagnostics','Edwin Southern',1975,'DNA fragments separated by size are transferred to a membrane and detected with a labeled complementary probe',['gene mapping','disease mutation detection','transgene verification'],'The first blot technique; Northern and Western blots followed.'],
['ELISA','diagnostics','(Engvall and Perlmann)',1971,'antibodies linked to enzymes produce a color signal proportional to the amount of target molecule captured',['infectious disease testing','allergy panels','pregnancy tests'],'Enzyme-linked immunosorbent assay; a workhorse of clinical labs.'],
['Induced pluripotent stem cells','cell-biology','Shinya Yamanaka',2006,'four transcription factors reprogram adult cells back to an embryonic-like pluripotent state',['regenerative medicine','disease modeling','drug screening'],'2012 Nobel Prize in Physiology or Medicine, shared with John Gurdon.'],
['HeLa cell line','cell-biology','(cells of Henrietta Lacks)',1951,'the first immortal human cell line, dividing indefinitely in laboratory culture',['vaccine development','cancer research','cell biology foundations'],'The most widely used human cell line in history.'],
['Human Genome Project','bioinformatics','international consortium',2003,'the full three-billion-letter human genome sequenced, assembled, and released by coordinated laboratories',['personalized medicine','disease-gene discovery','human ancestry studies'],'Declared complete in 2003; first drafts published in 2001.'],
['BLAST','bioinformatics','(Altschul and colleagues)',1990,'a fast heuristic algorithm comparing a DNA or protein sequence against huge databases to find matches',['gene identification','evolutionary studies','metagenomics'],'Basic Local Alignment Search Tool; among the most cited methods in biology.'],
['GenBank','bioinformatics','(U.S. NIH)',1982,'the public archive of all published DNA sequences, maintained as an open annotated collection',['sequence lookup','comparative genomics','primer design'],'The central sequence repository of molecular biology.']
];
var ASPECTS=['overview','mechanism deep-dive','applications survey','historical timeline','safety and ethics','comparative analysis'];
var CONTEXTS=['clinical translation','agricultural deployment','industrial scale-up','research laboratory','diagnostic service','educational program','field trial','manufacturing quality'];
var CATLBL={'gene-editing':'gene-editing method','dna-sequencing':'DNA sequencing method','amplification':'DNA amplification method','cloning':'cloning method','gene-therapy':'gene-therapy approach','biomanufacturing':'biomanufacturing process','synthetic-biology':'synthetic-biology method','diagnostics':'diagnostic method','cell-biology':'cell-biology technique','bioinformatics':'bioinformatics resource'};
function yrText(y){return y>0?String(y):'the mid-2000s era';}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ANCH.filter(function(a){return a[1]===cat;});
  if(!pool.length)pool=ANCH;
  var a=pick(pool,rnd);
  var mode=rnd()<0.45?'profile':'study';
  var aspect=pick(ASPECTS,rnd);
  var apps=a[5];
  var id=PREFIX+String(seed).padStart(6,'0');
  var serial='R-'+(10000+seed);
  var title,desc,specApps,src,code=null;
  if(mode==='profile'){
    code=serial;
    title=a[0]+': '+aspect+' ('+serial+')';
    var s1=a[0]+' is a '+CATLBL[a[1]]+' first reported in '+yrText(a[3])+' by '+a[2]+'.';
    var s2='How it works: '+a[4]+'.';
    var s3='It is used for '+apps[0]+', '+apps[1]+', and '+apps[2]+'.';
    var s4='Notable: '+a[6];
    if(aspect==='mechanism deep-dive')desc=s2+' '+s1+' The mechanism matters because every application of '+a[0]+' depends on this exact molecular behavior. '+s4;
    else if(aspect==='applications survey')desc=s1+' '+s3+' Practitioners choose '+a[0]+' when these applications demand its specific strengths. '+s2;
    else if(aspect==='historical timeline')desc=s1+' The work emerged in '+yrText(a[3])+'. '+s4+' '+s3;
    else if(aspect==='safety and ethics')desc=s1+' '+s2+' Responsible use requires containment, consent, and oversight appropriate to '+a[1].replace(/-/g,' ')+'. '+s4;
    else if(aspect==='comparative analysis')desc=s1+' Compared with older approaches, '+a[0]+' is distinguished by its mechanism: '+a[4]+'. '+s3;
    else desc=s1+' '+s2+' '+s3+' '+s4;
    src='online';specApps=apps.slice();
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=pick(CONTEXTS,rnd);
    var n=ri(rnd,40,9000),yr=ri(rnd,2016,2026);
    title=a[0]+' \u2014 '+ctx+' study '+code;    desc='This application study ('+code+', compiled '+yr+') documents a '+ctx+' deployment of '+a[0]+', the '+CATLBL[a[1]]+' reported in '+yrText(a[3])+' by '+a[2]+'. '+
      'The underlying mechanism is unchanged: '+a[4]+'. '+
      'Across '+n.toLocaleString('en-US')+' documented runs in this generated study, operators applied the method to '+apps[0]+' and '+apps[1]+', with outcomes consistent with the published mechanism. '+
      'As a Signature-generated study record, the deployment scenario is illustrative; the core facts about '+a[0]+' come from the published record.';
    src='signature';specApps=[apps[0],apps[1],ctx+' deployment (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{technique:a[0],discoverer:a[2],year:a[3]||null,category:a[1],mechanism:a[4],applications:specApps,notable:a[6],study_code:code,aspect:aspect},
    src:src,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-BIO-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>160)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  else{var parts=r.description.split('. ');if(parts.length<2)e.push('description-sentences');if(!/\.$/.test(r.description.trim()))e.push('description-period');}
  if(CATS.indexOf(r.category)<0)e.push('category');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(!s.technique||typeof s.technique!=='string')e.push('spec.technique');
    if(!s.discoverer||typeof s.discoverer!=='string')e.push('spec.discoverer');
    if(!(s.year===null||(Number.isInteger(s.year)&&s.year>=1500&&s.year<=2026)))e.push('spec.year');
    if(!s.mechanism||typeof s.mechanism!=='string')e.push('spec.mechanism');
    if(!Array.isArray(s.applications)||s.applications.length<2||s.applications.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.applications');
    if(!s.notable||typeof s.notable!=='string')e.push('spec.notable');
  }
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-biotech-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('biotech',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
