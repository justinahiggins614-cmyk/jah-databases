(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="biology-study";
var SLUG="biology-study-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-biology-study-published-P-";
var FIELD="Biology";
var GENVER="jahdb-biology-study-published-1.0";
var CATS=["Cell Biology", "Genetics", "Ecology", "Microbiology", "Physiology", "Evolution", "Molecular Biology", "Natural History"];
var L1=[["On the Origin of Species", ["Charles Darwin"], "John Murray, London", 1859, 5, "Darwin presents natural selection as the mechanism of evolution, marshalling evidence from breeding, biogeography, fossils, and anatomy. One of the most important books ever written, it made evolution the organizing principle of biology. The single long argument changed humanity's self-understanding."], ["Molecular structure of nucleic acids", ["James D. Watson", "Francis H.C. Crick"], "Nature, Vol. 171", 1953, 6, "The one-page paper proposing the double-helical structure of DNA, with base pairing suggesting a copying mechanism. It has not escaped our notice, they wrote, that the structure suggests how heredity works. Molecular biology begins here."], ["The Double Helix", ["James D. Watson"], "Atheneum", 1968, 6, "Watson's candid, gossipy memoir of the race for DNA's structure — the rivalries, the X-ray photographs, the eureka moments. Controversial for its portraits of colleagues, it humanized science. It remains the most famous insider account of a discovery."], ["Silent Spring", ["Rachel Carson"], "Houghton Mifflin", 1962, 2, "Carson documented how DDT and pesticides devastated birds and ecosystems, indicting the chemical industry and government. The book catalyzed the modern environmental movement and led to the EPA's creation. Few books have moved policy so directly."], ["The Selfish Gene", ["Richard Dawkins"], "Oxford University Press", 1976, 5, "Dawkins argues that evolution is best understood from the gene's-eye view: organisms are survival machines built by replicators. The meme concept was coined here. It reframed evolutionary thinking for the public and professionals alike."], ["Molecular Biology of the Cell", ["Bruce Alberts", "Alexander Johnson", "Julian Lewis", "Martin Raff", "Keith Roberts", "Peter Walter"], "Garland Science", 1983, 0, "The definitive cell biology textbook — comprehensive, beautifully illustrated, rigorously current through six editions. Generations of biologists learned the cell from its pages. It set the standard for what a science textbook can be."], ["Experiments in Plant Hybridisation", ["Gregor Mendel"], "Proceedings of the Natural History Society of Brunn", 1866, 1, "Mendel's pea-plant experiments deriving the laws of segregation and independent assortment — the foundation of genetics. Ignored for 34 years until rediscovered in 1900. It is the founding paper of a science."], ["The Beak of the Finch", ["Jonathan Weiner"], "Alfred A. Knopf", 1994, 5, "Weiner follows Peter and Rosemary Grant's decades studying Darwin's finches on Daphne Major, showing evolution happening in real time. Winner of the Pulitzer Prize. It made natural selection visible and immediate."], ["Your Inner Fish", ["Neil Shubin"], "Pantheon Books", 2008, 5, "Shubin traces the human body back to ancient fish — the discoverer of Tiktaalik shows how our limbs, heads, and genes carry 3.5 billion years of history. A paleontologist's tour of deep homology. It makes evolution personal."], ["The Blind Watchmaker", ["Richard Dawkins"], "W. W. Norton", 1986, 5, "Dawkins's full-throated defense of Darwinism against design arguments, introducing the blind watchmaker and the biomorph computer models. Elegant and combative, it defined the adaptationist program. The title became shorthand for natural selection."], ["Genetics and the Origin of Species", ["Theodosius Dobzhansky"], "Columbia University Press", 1937, 5, "Dobzhansky fused Mendelian genetics with Darwinian selection, founding the modern evolutionary synthesis. Nothing in biology makes sense except in the light of evolution. It united field naturalists and laboratory geneticists."], ["What Is Life?", ["Erwin Schrödinger"], "Cambridge University Press", 1944, 6, "The physicist's lectures asking how order persists in organisms, predicting an aperiodic crystal carrying heredity — inspiring Watson, Crick, and Wilkins toward DNA. A slim book that redirected biology. Negentropy entered the vocabulary here."], ["The Eighth Day of Creation", ["Horace Freeland Judson"], "Simon & Schuster", 1979, 6, "Judson's magisterial oral history of molecular biology's heroic age — the phage group, the double helix, the genetic code. Based on hundreds of interviews, it reads like a novel. The definitive chronicle of the revolution."], ["The Lives of a Cell", ["Lewis Thomas"], "Viking Press", 1974, 0, "Thomas's luminous essays — on mitochondria as symbionts, on ants and humans as social organisms — won the National Book Award. A physician celebrates biology's interconnectedness. The title essay is an American classic."], ["The Diversity of Life", ["Edward O. Wilson"], "Harvard University Press", 1992, 2, "Wilson's synthesis of biodiversity science and his warning about the extinction crisis, introducing biophilia. Written with a naturalist's love and a prophet's urgency. It founded conservation biology's public case."], ["Sociobiology: The New Synthesis", ["Edward O. Wilson"], "Harvard University Press", 1975, 5, "Wilson's massive synthesis arguing social behavior, including human, has evolutionary foundations. The final chapter on humans ignited fierce controversy. It launched sociobiology and evolutionary psychology."], ["The Voyage of the Beagle", ["Charles Darwin"], "Henry Colburn, London", 1839, 7, "Darwin's journal of the five-year circumnavigation — fossils in Argentina, finches in the Galapagos, earthquakes in Chile. The observations that seeded the Origin. The greatest travel book in science."], ["Wonderful Life", ["Stephen Jay Gould"], "W. W. Norton", 1989, 5, "Gould's account of the Burgess Shale fossils argues that contingency, not progress, rules evolution — replay the tape and humans vanish. Decimation and disparity became watchwords. It challenged adaptationist orthodoxy."], ["The Panda's Thumb", ["Stephen Jay Gould"], "W. W. Norton", 1980, 5, "Gould's essays on the panda's makeshift thumb, Mickey Mouse's neoteny, and evolution's imperfections — natural history as moral philosophy. The title essay is the classic statement that evolution works with what it has. Science writing at its most humane."], ["The Extended Phenotype", ["Richard Dawkins"], "Oxford University Press", 1982, 5, "Dawkins's technical sequel to The Selfish Gene, arguing genes' effects extend beyond bodies — beaver dams, caddis houses, parasites manipulating hosts. His most rigorous book. It expanded the unit of selection."], ["The Red Queen", ["Matt Ridley"], "Macmillan", 1993, 5, "Ridley explains sex as an evolutionary arms race against parasites — it takes all the running you can do to stay in place. Lively and provocative, it made the paradox of sex famous. The Red Queen hypothesis entered popular science."], ["Genome", ["Matt Ridley"], "HarperCollins", 1999, 1, "Ridley tours the human genome chromosome by chromosome, one story per pair, from disease genes to behavior. Written just before the genome project's completion. It humanized the double helix's sequel."], ["A Sand County Almanac", ["Aldo Leopold"], "Oxford University Press", 1949, 2, "Leopold's year on a Wisconsin farm and his Land Ethic — enlarging the community to include soils, waters, plants, and animals. The bible of conservation. A thing is right when it preserves the integrity of the biotic community."], ["The Descent of Man", ["Charles Darwin"], "John Murray, London", 1871, 5, "Darwin applied evolution to humans and introduced sexual selection, arguing our moral sense evolved. More controversial than the Origin in its day. It completed the Darwinian revolution."], ["Micrographia", ["Robert Hooke"], "Royal Society, London", 1665, 0, "Hooke's illustrated observations through the microscope — coining the word cell from cork tissue, drawing fleas and lice in magnificent detail. The first great microscopy book. It opened the microscopic world."], ["The Theory of the Gene", ["Thomas Hunt Morgan"], "Yale University Press", 1926, 1, "Morgan's synthesis of fly-room experiments locating genes on chromosomes, founding classical genetics. The white-eyed fly changed biology. It made the chromosome theory rigorous."], ["An Essay on the Principle of Population", ["Thomas Robert Malthus"], "J. Johnson, London", 1798, 2, "Malthus argued population grows geometrically while food grows arithmetically, predicting inevitable checks. It influenced Darwin's struggle for existence and all demography since. The most debated pamphlet in economics and ecology."], ["The Structure and Distribution of Coral Reefs", ["Charles Darwin"], "Smith, Elder and Co., London", 1842, 2, "Darwin's first major book explained atolls as coral growing on subsiding volcanic islands — confirmed a century later by drilling. Written from Beagle observations. It made his reputation as a geologist."], ["Campbell Biology", ["Neil A. Campbell", "Jane B. Reece"], "Benjamin Cummings", 1987, 0, "The dominant general biology textbook for decades — clear, comprehensive, richly illustrated, spanning molecules to ecosystems. Millions of students met biology through Campbell. The gold standard of the introductory course."], ["Life on Earth", ["David Attenborough"], "William Collins", 1979, 7, "Attenborough's companion to the landmark BBC series — a grand tour of life's diversity and history. It brought natural history to hundreds of millions. The book that made him the world's naturalist."], ["The Song of the Dodo", ["David Quammen"], "Scribner", 1996, 2, "Quammen's epic on island biogeography and extinction — from Wallace and Darwin to modern fragmentation science. Deeply reported and beautifully written. The best book on why islands, and fragments, lose species."], ["The Mismeasure of Man", ["Stephen Jay Gould"], "W. W. Norton", 1981, 1, "Gould's demolition of biological determinism — craniometry, IQ testing, and the misuse of statistics to rank human worth. A landmark of science criticism. It showed how bias enters measurement."]];
var L1_TITLES=["On the Origin of Species", "Molecular structure of nucleic acids", "The Double Helix", "Silent Spring", "The Selfish Gene", "Molecular Biology of the Cell", "Experiments in Plant Hybridisation", "The Beak of the Finch", "Your Inner Fish", "The Blind Watchmaker", "Genetics and the Origin of Species", "What Is Life?", "The Eighth Day of Creation", "The Lives of a Cell", "The Diversity of Life", "Sociobiology: The New Synthesis", "The Voyage of the Beagle", "Wonderful Life", "The Panda's Thumb", "The Extended Phenotype", "The Red Queen", "Genome", "A Sand County Almanac", "The Descent of Man", "Micrographia", "The Theory of the Gene", "An Essay on the Principle of Population", "The Structure and Distribution of Coral Reefs", "Campbell Biology", "Life on Earth", "The Song of the Dodo", "The Mismeasure of Man"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["the cell theory", "membranes and transport", "the cytoskeleton", "cell division", "signal reception", "the cell cycle"], ["Mendel's laws", "chromosomes and linkage", "the genetic code", "mutation and repair", "population genetics", "genetic engineering"], ["populations and communities", "energy flow", "nutrient cycles", "succession", "biodiversity", "biomes of the world"], ["the microbial world", "bacterial genetics", "viruses", "the immune response", "microbial ecology", "applied microbiology"], ["homeostasis", "the nervous system", "circulation and respiration", "digestion and metabolism", "endocrine control", "reproduction"], ["natural selection", "speciation", "the fossil record", "molecular evolution", "coevolution", "human evolution"], ["DNA replication", "transcription", "translation", "gene regulation", "recombinant DNA", "genomics"], ["the voyage tradition", "island biogeography", "the great naturalists", "field observation methods", "species accounts", "the web of life"]];
var FRAMES=["launched a research program that ran for a century", "gave biology its central organizing theory", "turned a curiosity into a rigorous discipline", "remains the clearest exposition of its subject", "changed what it means to study life", "is still assigned because nothing has replaced it"];
var T2_TOPICS=["synthetic cell design", "gene-drive containment", "microbiome therapeutics", "de-extinction ethics", "ocean ecosystem restoration", "CRISPR crop regulation", "neurobiology of behavior", "pandemic early warning", "soil biodiversity", "urban wildlife adaptation", "longevity pathways", "photosynthesis engineering"];
var T2_ANGLES=["comparative genomic analysis", "field-experiment synthesis", "mechanistic modeling", "evolutionary forecasting", "systems-level mapping", "conservation triage"];
var T2_METHODS=["multi-omics integration", "long-term field plots", "phylogenetic reconstruction", "controlled mesocosm trials", "single-cell sequencing", "meta-analysis of published studies"];
var T2_OUTCOMES=["a predictive model of ecosystem response", "a validated intervention protocol", "a revised evolutionary timeline", "quantified conservation priorities", "a mechanistic pathway map", "a field-ready diagnostic"];
var PROJ_BY="JAH Biology Projection Unit";
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
