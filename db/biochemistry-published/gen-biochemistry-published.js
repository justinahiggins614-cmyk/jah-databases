(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="biochemistry";
var SLUG="biochemistry-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-biochemistry-published-P-";
var FIELD="Biochemistry";
var GENVER="jahdb-biochemistry-published-1.0";
var CATS=["Enzymology", "Metabolism", "Structural Biology", "Bioenergetics", "Signal Transduction", "Proteins", "Nucleic Acids", "Methods"];
var L1=[["Protein measurement with the Folin phenol reagent", ["Oliver H. Lowry", "Nira J. Rosebrough", "A. Lewis Farr", "Rose J. Randall"], "Journal of Biological Chemistry, Vol. 193", 1951, 7, "The most-cited paper in scientific history — a simple, sensitive colorimetric protein assay. The Lowry method became every biochemistry lab's workhorse. Citations number in the hundreds of thousands."], ["Cleavage of structural proteins during the assembly of the head of bacteriophage T4", ["Ulrich K. Laemmli"], "Nature, Vol. 227", 1970, 7, "Laemmli's SDS-polyacrylamide gel electrophoresis method for separating proteins by size. SDS-PAGE became the universal protein analysis tool. One of the most cited methods papers ever."], ["DNA sequencing with chain-terminating inhibitors", ["Frederick Sanger", "Steven Nicklen", "Alan R. Coulson"], "Proceedings of the National Academy of Sciences, Vol. 74", 1977, 7, "Sanger's dideoxy sequencing method — the technique that sequenced the first genomes and won him a second Nobel Prize. Elegant in its simplicity. It powered the genomic era."], ["Molecular Cloning: A Laboratory Manual", ["Tom Maniatis", "Edward F. Fritsch", "Joseph Sambrook"], "Cold Spring Harbor Laboratory", 1982, 7, "The bible of recombinant DNA technique — the protocols every molecular biology lab ran. Dog-eared copies sat on every bench. It standardized the molecular revolution."], ["Specific enzymatic amplification of DNA in vitro: the polymerase chain reaction", ["Kary B. Mullis", "Fred Faloona"], "Cold Spring Harbor Symposia on Quantitative Biology, Vol. 51", 1986, 7, "Mullis's description of PCR — exponential DNA amplification from tiny samples. It won the 1993 Nobel Prize and transformed diagnostics, forensics, and research. The most consequential method in modern biology."], ["The fluid mosaic model of the structure of cell membranes", ["Seymour J. Singer", "Garth L. Nicolson"], "Science, Vol. 175", 1972, 2, "Singer and Nicolson proposed membranes as fluid lipid bilayers with embedded proteins drifting laterally. The model organized decades of membrane research. Every textbook figure of a membrane descends from it."], ["Studies on the chemical nature of the substance inducing transformation of pneumococcal types", ["Oswald T. Avery", "Colin M. MacLeod", "Maclyn McCarty"], "Journal of Experimental Medicine, Vol. 79", 1944, 6, "Avery's team showed DNA — not protein — transforms pneumococci, identifying the hereditary material. Met with skepticism, then vindicated. The experiment that pointed to DNA."], ["Independent functions of viral protein and nucleic acid in growth of bacteriophage", ["Alfred D. Hershey", "Martha Chase"], "Journal of General Physiology, Vol. 36", 1952, 6, "The blender experiment: labeled phage DNA enters bacteria while protein stays out — confirming DNA as genetic material. Elegant and decisive. It closed the case Avery opened."], ["The amino-acid sequence in the phenylalanyl chain of insulin", ["Frederick Sanger", "Hans Tuppy"], "Biochemical Journal, Vol. 49", 1951, 5, "Sanger's determination of insulin's amino acid sequence — the first protein ever sequenced, proving proteins have defined chemical structures. It won the 1958 Nobel Prize. Protein chemistry begins here."], ["Genetic regulatory mechanisms in the synthesis of proteins", ["François Jacob", "Jacques Monod"], "Journal of Molecular Biology, Vol. 3", 1961, 6, "Jacob and Monod's operon model — the repressor, the operator, messenger RNA — founding molecular gene regulation. The lac operon became biology's paradigm circuit. It won the 1965 Nobel Prize."], ["General nature of the genetic code for proteins", ["Francis H.C. Crick", "Leslie Barnett", "Sydney Brenner", "Richard J. Watts-Tobin"], "Nature, Vol. 192", 1961, 6, "Crick's team used frameshift mutations to prove the genetic code is read in triplets. A masterpiece of genetic logic. The code's triplet nature was established without sequencing a base."], ["Allosteric proteins and cellular control systems", ["Jacques Monod", "Jeffries Wyman", "Jean-Pierre Changeux"], "Journal of Molecular Biology, Vol. 12", 1965, 0, "The MWC model of allostery — proteins flipping between tense and relaxed states, regulated at sites distant from active centers. It explained hemoglobin cooperativity and enzyme regulation. A landmark of theoretical biochemistry."], ["A rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein-dye binding", ["Marion M. Bradford"], "Analytical Biochemistry, Vol. 72", 1976, 7, "Bradford's Coomassie dye-binding assay — faster and simpler than Lowry's, run in minutes. The Bradford assay became the quick standard. Another endlessly cited methods paper."], ["Electrophoretic transfer of proteins from polyacrylamide gels to nitrocellulose sheets", ["Harry Towbin", "Theophil Staehelin", "Julian Gordon"], "Proceedings of the National Academy of Sciences, Vol. 76", 1979, 7, "The western blot — transferring separated proteins to membranes for antibody detection. Named by analogy to Southern's DNA blot. It became immunodetection's standard."], ["The Nature of the Chemical Bond", ["Linus Pauling"], "Cornell University Press", 1939, 2, "Pauling's masterwork applying quantum mechanics to chemistry — hybridization, resonance, electronegativity. It won him the 1954 Nobel Prize in Chemistry. The book that made modern structural chemistry."], ["Principles of Biochemistry", ["Albert L. Lehninger"], "Worth Publishers", 1970, 1, "Lehninger's magisterial textbook organizing biochemistry around bioenergetics and molecular logic. The first great modern biochemistry text. Generations learned metabolism from Lehninger."], ["Biochemistry", ["Lubert Stryer"], "W. H. Freeman", 1975, 1, "Stryer's textbook — lucid, mechanism-focused, beautifully illustrated — dominated biochemistry teaching for decades. The standard against which others were judged. Its clarity set a new bar."], ["Molecular Biology of the Gene", ["James D. Watson"], "W. A. Benjamin", 1965, 6, "Watson's textbook that taught the first generation of molecular biologists — the phage group's bible in book form. Crisp, opinionated, current. It defined the new field's curriculum."], ["The ATP synthase — a splendid molecular machine", ["Paul D. Boyer"], "Annual Review of Biochemistry, Vol. 66", 1997, 3, "Boyer's review of his binding-change mechanism for ATP synthesis — the rotary engine of life. It shared the 1997 Nobel Prize. The clearest exposition of bioenergetics' crown jewel."], ["Introduction to Protein Structure", ["Carl Branden", "John Tooze"], "Garland Publishing", 1991, 2, "The classic visual introduction to protein architecture — folds, motifs, domains — that taught structural biology to non-crystallographers. Its ribbon diagrams became iconic. The field's most borrowed book."], ["Enzyme Structure and Mechanism", ["Alan R. Fersht"], "W. H. Freeman", 1977, 0, "Fersht's rigorous treatment of how enzymes achieve their enormous rate enhancements — transition-state theory made quantitative. The enzymologist's handbook. It set the mechanistic standard."], ["Molecular Cell Biology", ["Harvey Lodish", "David Baltimore", "Arnold Berk", "S. Lawrence Zipursky", "Paul Matsudaira", "James Darnell"], "W. H. Freeman", 1986, 6, "The comprehensive molecular cell biology text from leading practitioners — authoritative across the central dogma and beyond. A bench-side encyclopedia. It defined the advanced course."], ["Biochemistry", ["Donald Voet", "Judith G. Voet"], "John Wiley & Sons", 1990, 1, "The Voets' encyclopedic, chemically rigorous biochemistry text — beloved for depth and precision. The reference text of the field. Its mechanisms are drawn with unusual care."], ["The Cell: A Molecular Approach", ["Geoffrey M. Cooper"], "ASM Press", 1997, 6, "Cooper's focused text on the molecular biology of the cell — signaling, cancer, the cell cycle. Clear and current through many editions. A favorite of the molecular-minded."], ["Molecular Biology of the Cell — Alberts", ["Bruce Alberts", "Alexander Johnson", "Julian Lewis", "Martin Raff", "Keith Roberts", "Peter Walter"], "Garland Science", 2002, 6, "The fourth edition of the definitive cell biology reference, integrating genomics into cell biology. The standard remains the standard. No lab is complete without it."], ["Three-dimensional structure of myoglobin", ["John C. Kendrew", "G. Bodo", "H. M. Dintzis", "R. G. Parrish", "H. Wyckoff", "D. C. Phillips"], "Nature, Vol. 181", 1958, 2, "Kendrew's team published the first atomic structure of a protein — myoglobin at 6 angstroms, later refined. It won the 1962 Nobel Prize. Structural biology was born."], ["Structure of haemoglobin", ["Max F. Perutz", "M. G. Rossmann", "A. F. Cullis", "H. Muirhead", "G. Will", "A. C. T. North"], "Nature, Vol. 185", 1960, 2, "Perutz's hemoglobin structure at 5.5 angstroms — revealing the oxygen-carrying tetramer. Shared the 1962 Nobel Prize with Kendrew. It showed allostery in atomic detail."], ["A structure for deoxyribose nucleic acid", ["James D. Watson", "Francis H.C. Crick"], "Nature, Vol. 171", 1953, 6, "The double helix paper — base-paired antiparallel strands suggesting a copying mechanism. The most famous page in biology. Everything in molecular biology flows from it."], ["On the nature of allosteric transitions: a plausible model", ["Jacques Monod", "Jeffries Wyman", "Jean-Pierre Changeux"], "Journal of Molecular Biology, Vol. 12", 1965, 0, "The formal MWC allostery paper — concerted transitions between T and R states. Quantitative and predictive. The theoretical core of regulation."], ["The operon: a group of genes with expression coordinated by an operator", ["François Jacob", "David Perrin", "Carmen Sanchez", "Jacques Monod"], "Comptes Rendus de l'Académie des Sciences, Vol. 250", 1960, 6, "The first announcement of the operon concept — coordinated gene regulation. A short note that remade genetics. The 1960 Comptes Rendus note."], ["Isolation of the lac repressor", ["Walter Gilbert", "Benno Müller-Hill"], "Proceedings of the National Academy of Sciences, Vol. 56", 1966, 6, "Gilbert and Müller-Hill isolated the lac repressor protein — the first gene regulatory protein ever purified. The operon made tangible. A triumph of biochemistry over genetics."], ["Enzymatic synthesis of deoxyribonucleic acid", ["Arthur Kornberg"], "Nobel Lecture", 1959, 0, "Kornberg's Nobel lecture on DNA polymerase — the enzyme that copies DNA. The 1959 Prize in Physiology or Medicine. It proved replication was chemistry."]];
var L1_TITLES=["Protein measurement with the Folin phenol reagent", "Cleavage of structural proteins during the assembly of the head of bacteriophage T4", "DNA sequencing with chain-terminating inhibitors", "Molecular Cloning: A Laboratory Manual", "Specific enzymatic amplification of DNA in vitro: the polymerase chain reaction", "The fluid mosaic model of the structure of cell membranes", "Studies on the chemical nature of the substance inducing transformation of pneumococcal types", "Independent functions of viral protein and nucleic acid in growth of bacteriophage", "The amino-acid sequence in the phenylalanyl chain of insulin", "Genetic regulatory mechanisms in the synthesis of proteins", "General nature of the genetic code for proteins", "Allosteric proteins and cellular control systems", "A rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein-dye binding", "Electrophoretic transfer of proteins from polyacrylamide gels to nitrocellulose sheets", "The Nature of the Chemical Bond", "Principles of Biochemistry", "Biochemistry", "Molecular Biology of the Gene", "The ATP synthase — a splendid molecular machine", "Introduction to Protein Structure", "Enzyme Structure and Mechanism", "Molecular Cell Biology", "Biochemistry", "The Cell: A Molecular Approach", "Molecular Biology of the Cell — Alberts", "Three-dimensional structure of myoglobin", "Structure of haemoglobin", "A structure for deoxyribose nucleic acid", "On the nature of allosteric transitions: a plausible model", "The operon: a group of genes with expression coordinated by an operator", "Isolation of the lac repressor", "Enzymatic synthesis of deoxyribonucleic acid"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["catalysis fundamentals", "Michaelis-Menten kinetics", "inhibition", "coenzymes", "regulation of enzyme activity", "industrial enzymes"], ["glycolysis", "the citric acid cycle", "oxidative phosphorylation", "photosynthesis", "lipid metabolism", "nitrogen metabolism"], ["X-ray crystallography", "protein folds", "membrane proteins", "nucleic acid structures", "molecular dynamics", "structure validation"], ["the chemiosmotic theory", "electron transport", "ATP synthesis", "energy coupling", "mitochondrial biology", "thermodynamics of life"], ["receptors", "G proteins", "second messengers", "kinase cascades", "apoptosis signaling", "crosstalk and integration"], ["amino acids", "protein structure levels", "folding and misfolding", "post-translational modification", "proteomics", "protein engineering"], ["the double helix", "replication", "repair", "transcription", "RNA processing", "the genetic code"], ["chromatography", "electrophoresis", "spectroscopy", "centrifugation", "sequencing", "blotting techniques"]];
var FRAMES=["defined the experimental standard for a generation", "revealed the chemical logic of life", "made an invisible process measurable", "is still the paper everyone cites first", "turned technique into discovery", "gave the field its central metaphor"];
var T2_TOPICS=["enzyme design by computation", "metabolic network rewiring", "cryo-EM of membrane complexes", "ATP synthase engineering", "allosteric drug design", "RNA structure prediction", "protein folding in cells", "single-molecule enzymology", "synthetic cofactors", "metabolomics of disease", "redox signaling", "phase-separated condensates"];
var T2_ANGLES=["mechanistic dissection", "structure-function mapping", "kinetic modeling", "comparative enzymology", "pathway forecasting", "method benchmarking"];
var T2_METHODS=["time-resolved crystallography", "cryo-electron microscopy", "isothermal titration calorimetry", "flux-balance analysis", "NMR dynamics", "high-throughput kinetics"];
var T2_OUTCOMES=["a complete catalytic mechanism", "a druggable allosteric site", "a rewired high-yield pathway", "a validated kinetic model", "a new assay standard", "an engineered hyperstable enzyme"];
var PROJ_BY="JAH Biochemistry Projection Unit";
function idOk(id){return new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$').test(id||'');}
function sigOk(s){return new RegExp('^\\.\\./'+STUDYSLUG+'/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{6}$').test(s||'');}
function sigLink(addr){var n=1+((addr*13)%5000);return '../'+STUDYSLUG+'/index.html?sig=JAH-'+BASE+'-STUDY-S-'+String(n).padStart(6,'0');}
function buildL1(addr,rnd,catOv){
  var w=pick(rnd,L1);
  var cat=(catOv!==undefined)?catOv:CATS[w[4]];
  var ed=pick(rnd,EDITIONS),ol=pick(rnd,OUTLINES[w[4]]),frame=pick(rnd,FRAMES);
  var id=PREFIX+pad7(addr),auth=w[1].join(', ');
  var fc='This is the full published record for \u201c'+w[0]+'\u201d by '+auth+' ('+fmtYear(w[3])+'), published in '+w[2]+'. '+w[5]
   +' This archival entry preserves the '+ed+' of the work. Its contents are organized around: '+ol+'.'
   +' Its lasting contribution: '+frame+'.'
   +' Archival note: record '+id+' is preserved in the JAH '+FIELD+' Published Archive Database as a Level 1 real published work. Data may be augmented by the archive but never reduced below the original published file.';
  return {id:id,title:w[0],authors:w[1].slice(),publication:w[2],year:w[3],category:cat,full_content:fc,
   source_ref:'Published work catalog: '+w[2]+', '+fmtYear(w[3])+'. Verifiable via WorldCat, the Library of Congress catalog, and publisher records.',
   signature_link:sigLink(addr),level:1};
}
function buildL2(addr,rnd,catOv){
  var topic=pick(rnd,T2_TOPICS),angle=pick(rnd,T2_ANGLES),method=pick(rnd,T2_METHODS),out=pick(rnd,T2_OUTCOMES);
  var cat=(catOv!==undefined)?catOv:pick(rnd,CATS);
  var yr=ri(rnd,2027,2045);
  var bAddr=((addr*7)%500)*10;if(bAddr<10)bAddr=10;
  var b1=buildL1(bAddr,prng(bAddr*31+7)),baseId=PREFIX+pad7(bAddr),id=PREFIX+pad7(addr);
  var title='Level 2 \u2014 Projected '+angle+' in '+topic+': '+method+' outlook to '+yr;
  var fc='Level 2 projection record for the JAH '+FIELD+' Published Archive Database. Projected research direction: '+angle+' in '+topic+'.'
   +' Projected methodology: '+method+', carried through to '+yr+'. Expected findings: '+out+'.'
   +' This projection extends the Level 1 published record \u201c'+b1.title+'\u201d ('+baseId+') into the '+yr+' horizon. It is a model-derived projection of where the field is heading, not a record of an already-published work.'
   +' Archival note: record '+id+' is a Level 2 projection. Projections regenerate deterministically from seed '+addr+' via generator '+GENVER+'.';
  return {id:id,title:title,authors:[PROJ_BY],publication:'JAH Published Archive \u2014 Projection Series',year:yr,category:cat,full_content:fc,
   source_ref:'JAH Archive projection model v1.0 \u2014 projected from Level 1 record '+baseId+'. Reproducible via generator '+GENVER+' seed '+addr+'.',
   signature_link:sigLink(addr),level:2};
}
function generate(seed,opts,rnd){
  seed=(seed>>>0)||1;opts=opts||{};rnd=rnd||prng(seed);
  var addr=((seed-1)%1000000)+1;
  var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:undefined;
  return (addr%10===0)?buildL1(addr,rnd,cat):buildL2(addr,rnd,cat);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!idOk(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<1||r.title.length>220)e.push('title');
  if(!Array.isArray(r.authors)||!r.authors.length)e.push('authors');
  else r.authors.forEach(function(a){if(typeof a!=='string'||!a.length)e.push('author');});
  if(typeof r.publication!=='string'||!r.publication.length||r.publication.length>160)e.push('publication');
  if(!Number.isInteger(r.year)||r.year<-1000||r.year>2045)e.push('year');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.full_content!=='string'||r.full_content.length<400||r.full_content.length>4000)e.push('full_content');
  if(typeof r.source_ref!=='string'||r.source_ref.length<20)e.push('source_ref');
  if(!sigOk(r.signature_link))e.push('signature_link');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===2&&r.title.indexOf('Level 2')!==0)e.push('l2prefix');
  if(r.level===1&&r.title.indexOf('Level 2')===0)e.push('l1prefix');
  var keys=Object.keys(r).sort().join('|');
  if(keys!=='authors|category|full_content|id|level|publication|signature_link|source_ref|title|year')e.push('keys');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];(sample||[]).forEach(function(s){
   if(s&&s.id===rec.id)e.push('duplicate id in archive sample');
   if(s&&s.full_content===rec.full_content)e.push('duplicate content in archive sample');});
  return {ok:!e.length,errors:e};
}
var CHECKS=[
 {n:"id_format",f:function(r,x){try{return !!(idOk(r.id));}catch(e){return false;}}},
 {n:"id_matches_seed",f:function(r,x){try{return !!(r.id===PREFIX+pad7(x.seed));}catch(e){return false;}}},
 {n:"level_value",f:function(r,x){try{return !!(r.level===1||r.level===2);}catch(e){return false;}}},
 {n:"l2_title_starts_level2",f:function(r,x){try{return !!(r.level!==2||r.title.indexOf('Level 2')===0);}catch(e){return false;}}},
 {n:"l1_title_no_level2",f:function(r,x){try{return !!(r.level!==1||r.title.indexOf('Level 2')!==0);}catch(e){return false;}}},
 {n:"title_length",f:function(r,x){try{return !!(typeof r.title==='string'&&r.title.length>=1&&r.title.length<=220);}catch(e){return false;}}},
 {n:"authors_array",f:function(r,x){try{return !!(Array.isArray(r.authors)&&r.authors.length>=1);}catch(e){return false;}}},
 {n:"authors_strings",f:function(r,x){try{return !!(r.authors.every(function(a){return typeof a==='string'&&a.length>0;}));}catch(e){return false;}}},
 {n:"publication_length",f:function(r,x){try{return !!(typeof r.publication==='string'&&r.publication.length>=1&&r.publication.length<=160);}catch(e){return false;}}},
 {n:"year_integer_range",f:function(r,x){try{return !!(Number.isInteger(r.year)&&r.year>=-1000&&r.year<=2045);}catch(e){return false;}}},
 {n:"content_min_length",f:function(r,x){try{return !!(typeof r.full_content==='string'&&r.full_content.length>=400);}catch(e){return false;}}},
 {n:"content_max_length",f:function(r,x){try{return !!(r.full_content.length<=4000);}catch(e){return false;}}},
 {n:"content_sentences",f:function(r,x){try{return !!((r.full_content.match(/\.\s/g)||[]).length>=3);}catch(e){return false;}}},
 {n:"content_no_html",f:function(r,x){try{return !!(!/<[a-zA-Z][^>]*>/.test(r.full_content));}catch(e){return false;}}},
 {n:"title_no_html",f:function(r,x){try{return !!(!/<[a-zA-Z][^>]*>/.test(r.title));}catch(e){return false;}}},
 {n:"source_ref_length",f:function(r,x){try{return !!(typeof r.source_ref==='string'&&r.source_ref.length>=20);}catch(e){return false;}}},
 {n:"sig_link_format",f:function(r,x){try{return !!(sigOk(r.signature_link));}catch(e){return false;}}},
 {n:"sig_link_range",f:function(r,x){try{return !!((function(){var m=/S-(\d{6})$/.exec(r.signature_link);var n=m?+m[1]:0;return n>=1&&n<=5000;})());}catch(e){return false;}}},
 {n:"category_valid",f:function(r,x){try{return !!(CATS.indexOf(r.category)>=0);}catch(e){return false;}}},
 {n:"category_option_honored",f:function(r,x){try{return !!(generate(x.seed,{category:CATS[2]}).category===CATS[2]);}catch(e){return false;}}},
 {n:"deterministic",f:function(r,x){try{return !!(JSON.stringify(generate(x.seed,{}))===JSON.stringify(r));}catch(e){return false;}}},
 {n:"l2_contains_projection",f:function(r,x){try{return !!(r.level!==2||/projection/i.test(r.full_content));}catch(e){return false;}}},
 {n:"l1_contains_level1_marker",f:function(r,x){try{return !!(r.level!==1||/Level 1/.test(r.full_content));}catch(e){return false;}}},
 {n:"no_data_base_two_words",f:function(r,x){try{return !!(!/database/i.test(r.title+' '+r.full_content));}catch(e){return false;}}},
 {n:"no_original_website_refs",f:function(r,x){try{return !!(!/(JAH Wiki|Signature Math|cyber-patent|spec catalog|mega-mall|AI Olympics|Signature Llama|Wikileaks)/i.test(JSON.stringify(r)));}catch(e){return false;}}},
 {n:"l1_title_in_corpus",f:function(r,x){try{return !!(r.level!==1||L1_TITLES.indexOf(r.title)>=0);}catch(e){return false;}}},
 {n:"word_length_sane",f:function(r,x){try{return !!((r.title+' '+r.full_content).split(/\s+/).every(function(w){return w.length<=60;}));}catch(e){return false;}}},
 {n:"exact_keys",f:function(r,x){try{return !!(Object.keys(r).sort().join('|')==='authors|category|full_content|id|level|publication|signature_link|source_ref|title|year');}catch(e){return false;}}},
 {n:"json_roundtrip",f:function(r,x){try{return !!(JSON.stringify(JSON.parse(JSON.stringify(r)))===JSON.stringify(r));}catch(e){return false;}}},
 {n:"content_substantive",f:function(r,x){try{return !!(r.full_content.length>r.title.length+200);}catch(e){return false;}}},
 {n:"validate_ok",f:function(r,x){try{return !!(validate(r).ok);}catch(e){return false;}}},
 {n:"drift_ok_empty",f:function(r,x){try{return !!(driftCheck(r,[]).ok);}catch(e){return false;}}},
 {n:"addr_space_top",f:function(r,x){try{return !!(generate(1000000,{}).id===PREFIX+'1000000');}catch(e){return false;}}},
 {n:"seed_one_id",f:function(r,x){try{return !!(generate(1,{}).id===PREFIX+'0000001');}catch(e){return false;}}},
 {n:"l2_year_future",f:function(r,x){try{return !!(r.level!==2||(r.year>=2027&&r.year<=2045));}catch(e){return false;}}},
 {n:"l1_year_past",f:function(r,x){try{return !!(r.level!==1||(r.year>=-1000&&r.year<=2026));}catch(e){return false;}}},
 {n:"l2_source_ref_model",f:function(r,x){try{return !!(r.level!==2||/projection model/.test(r.source_ref));}catch(e){return false;}}},
 {n:"l1_source_ref_catalog",f:function(r,x){try{return !!(r.level!==1||/WorldCat/.test(r.source_ref));}catch(e){return false;}}},
 {n:"content_mentions_id",f:function(r,x){try{return !!(r.full_content.indexOf(r.id)>=0);}catch(e){return false;}}},
 {n:"l2_publication_series",f:function(r,x){try{return !!(r.level!==2||/Projection Series/.test(r.publication));}catch(e){return false;}}},
];
function selfTest(){
  var fails=[],total=0,passed=0,ids={},levels={1:0,2:0};
  for(var seed=1;seed<=40;seed++){
    var r=generate(seed,{});
    levels[r.level]++;
    if(ids[r.id])fails.push('suite duplicate id '+r.id);ids[r.id]=1;
    for(var i=0;i<CHECKS.length;i++){total++;
      var ok=false;try{ok=CHECKS[i].f(r,{seed:seed});}catch(e){ok=false;}
      if(ok)passed++;else fails.push('seed '+seed+' ['+CHECKS[i].n+']');}
  }
  if(levels[1]===0)fails.push('suite: no level-1 records in 40 seeds');
  if(levels[2]===0)fails.push('suite: no level-2 records in 40 seeds');
  return {seeds:40,checksPerSeed:CHECKS.length,total:total,passed:passed,
    failed:total-passed+((levels[1]===0||levels[2]===0)?1:0),
    suite:{uniqueIds:Object.keys(ids).length===40,levels:levels},
    failures:fails.slice(0,25),ok:fails.length===0};
}
var api={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,api);
if(typeof module!=='undefined'&&module.exports)module.exports=api;
})();
