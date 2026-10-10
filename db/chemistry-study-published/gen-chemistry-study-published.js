(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="chemistry-study";
var SLUG="chemistry-study-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-chemistry-study-published-P-";
var FIELD="Chemistry";
var GENVER="jahdb-chemistry-study-published-1.0";
var CATS=["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Analytical Chemistry", "Materials Chemistry", "Chemical History", "Spectroscopy", "Electrochemistry"];
var L1=[["The Nature of the Chemical Bond", ["Linus Pauling"], "Cornell University Press", 1939, 5, "Pauling's masterwork applying quantum mechanics to chemistry — hybridization, resonance, electronegativity scales. It won the 1954 Nobel Prize. The book that made modern structural chemistry."], ["General Chemistry", ["Linus Pauling"], "W. H. Freeman", 1947, 5, "Pauling's introductory text — the first to teach chemistry through quantum mechanics and the chemical bond. Revolutionary pedagogy. It reset the freshman course."], ["On the Relationship of the Properties of the Elements to their Atomic Weights", ["Dmitri Mendeleev"], "Journal of the Russian Chemical Society, Vol. 1", 1869, 5, "Mendeleev's periodic table — elements ordered by weight with gaps predicted for undiscovered elements. Gallium and germanium arrived on schedule. The most successful prediction in science."], ["A New System of Chemical Philosophy", ["John Dalton"], "Manchester", 1808, 5, "Dalton's atomic theory — elements as atoms of characteristic weight combining in simple ratios. The foundation of quantitative chemistry. Atoms became real."], ["Traité Élémentaire de Chimie", ["Antoine Lavoisier"], "Cuchet, Paris", 1789, 5, "Lavoisier's textbook of the chemical revolution — conservation of mass, oxygen theory of combustion, modern nomenclature. Chemistry's founding document. It ended phlogiston."], ["Organic Chemistry", ["John D. Roberts", "Marjorie C. Caserio"], "W. A. Benjamin", 1964, 0, "The Roberts-Caserio text that modernized organic chemistry teaching with physical-organic rigor. A generation's standard. Mechanism-first pedagogy."], ["March's Advanced Organic Chemistry", ["Jerry March"], "McGraw-Hill", 1968, 0, "The encyclopedic reference on organic reactions, mechanisms, and structure — the organic chemist's desk bible through five editions. Exhaustive and precise. No lab shelf lacked it."], ["The Logic of Chemical Synthesis", ["E. J. Corey", "Xue-Min Cheng"], "John Wiley & Sons", 1989, 0, "Corey's exposition of retrosynthetic analysis — the logic that won the 1990 Nobel Prize. Synthesis as chess played backwards. It systematized the art."], ["Physical Chemistry", ["Peter Atkins"], "Oxford University Press", 1978, 2, "Atkins's physical chemistry text — thermodynamics, kinetics, and quantum chemistry with unusual clarity. The global standard. Its explanations are legendary."], ["Quantitative Chemical Analysis", ["Daniel C. Harris"], "W. H. Freeman", 1982, 3, "Harris's analytical chemistry text — rigorous, practical, and humane. The analytical chemist's companion. Clarity in measurement."], ["Vogel's Textbook of Quantitative Chemical Analysis", ["Arthur I. Vogel"], "Longmans, Green", 1939, 3, "Vogel's exhaustive manual of classical analytical methods — gravimetry and titrimetry done right. The bench bible of wet chemistry. Precision codified."], ["Spectrometric Identification of Organic Compounds", ["Robert M. Silverstein", "G. Clayton Bassler", "Terence C. Morrill"], "John Wiley & Sons", 1963, 6, "The first systematic guide to identifying organics by IR, NMR, and mass spec — solving structures from spectra. It taught a generation to read molecules. Spectroscopy's Rosetta stone."], ["The Chemical History of a Candle", ["Michael Faraday"], "Griffin, Bohn", 1860, 5, "Faraday's Christmas lectures for young people — a candle's flame revealing combustion, gases, and the conservation of matter. The most beloved science lectures ever. Wonder as pedagogy."], ["Uncle Tungsten", ["Oliver Sacks"], "Alfred A. Knopf", 2001, 5, "Sacks's memoir of his chemical boyhood — home experiments, the periodic table as adventure. A love letter to chemistry. It made readers want a laboratory."], ["The Disappearing Spoon", ["Sam Kean"], "Little, Brown", 2010, 5, "Kean's tales from the periodic table — mad scientists, poisonings, and the elements' secret lives. Popular science at its most fun. The table as drama."], ["Napoleon's Buttons", ["Penny Le Couteur", "Jay Burreson"], "Jeremy P. Tarcher", 2003, 5, "Seventeen molecules that changed history — from tin buttons to contraceptives. Chemistry as world history. Molecules with consequences."], ["The Poisoner's Handbook", ["Deborah Blum"], "Penguin Press", 2010, 5, "Blum's account of Jazz Age New York's forensic chemists — Gettler and Norris inventing toxicology case by case. Murder and molecules. Forensic chemistry's origin story."], ["The Elements: A Visual Exploration", ["Theodore Gray"], "Black Dog & Leventhal", 2009, 5, "Gray's photographic periodic table — every element in stunning images and objects. A visual feast. It made the table tangible."], ["Molecules: The Elements and the Architecture of Everything", ["Theodore Gray"], "Black Dog & Leventhal", 2014, 5, "Gray's sequel on compounds — the architecture of everything from water to DNA. Gorgeous and deep. Chemistry you can see."], ["Chemistry: The Central Science", ["Theodore L. Brown", "H. Eugene LeMay Jr."], "Prentice-Hall", 1977, 5, "The dominant general chemistry text for decades — comprehensive and carefully scaffolded. Millions learned chemistry from Brown and LeMay. The central science's central text."], ["Shriver and Atkins' Inorganic Chemistry", ["Duward F. Shriver", "Peter Atkins"], "W. H. Freeman", 1990, 1, "The modern inorganic text — bonding, coordination, organometallics, materials. Authoritative and current. The inorganic standard."], ["Periodic Tales", ["Hugh Aldersey-Williams"], "Ecco Press", 2011, 5, "A cultural history of the elements — where they were found, what they meant. Science meets storytelling. The human side of the table."], ["Inorganic Chemistry", ["Gary L. Miessler", "Donald A. Tarr"], "HarperCollins", 1991, 1, "Miessler and Tarr's symmetry-driven inorganic text — group theory made usable. The classroom favorite. Elegant and thorough."], ["The Principles of Chemistry", ["Dmitri Mendeleev"], "St. Petersburg", 1870, 5, "Mendeleev's two-volume textbook expounding the periodic law for students. The table's first full exposition. Pedagogy that changed science."], ["Crucibles: The Story of Chemistry", ["Bernard Jaffe"], "Simon & Schuster", 1930, 5, "Jaffe's biographical history of chemistry through its great discoverers. The classic popular history. Generations met chemistry through its heroes."], ["The Development of Modern Chemistry", ["Aaron J. Ihde"], "Harper & Row", 1964, 5, "Ihde's scholarly history of chemistry from Boyle to the 20th century. The standard academic history. Thorough and balanced."], ["What Is Chemistry?", ["Peter Atkins"], "Oxford University Press", 2013, 5, "Atkins's short, sharp meditation on chemistry's nature — matter, change, and explanation. Philosophy of chemistry for everyone. A gem."], ["The Chemistry of the Actinide and Transactinide Elements", ["Lester R. Morss", "Norman M. Edelstein", "Jean Fuger"], "Springer", 2006, 1, "The definitive reference on the heaviest elements — synthesis, properties, handling. The specialist's bible. Heavy science, literally."], ["Chemical Kinetics and Reaction Dynamics", ["Paul L. Houston"], "McGraw-Hill", 2001, 2, "Houston's modern treatment of reaction rates — from collision theory to laser dynamics. Clear and current. Kinetics made physical."], ["Electrochemical Methods", ["Allen J. Bard", "Larry R. Faulkner"], "John Wiley & Sons", 1980, 7, "Bard and Faulkner's definitive electrochemistry text — fundamentals and applications. The electrochemist's bible. Exhaustive authority."], ["NMR Spectroscopy", ["Harald Günther"], "John Wiley & Sons", 1973, 6, "Günther's classic introduction to nuclear magnetic resonance — theory made practical. The spectroscopist's first book. Still assigned."], ["Organic Chemistry", ["Jonathan Clayden", "Nick Greeves", "Stuart Warren"], "Oxford University Press", 2001, 0, "Clayden's mechanism-first organic text — curly arrows from page one, problems that teach thinking. The modern standard. Organic chemistry, reimagined."]];
var L1_TITLES=["The Nature of the Chemical Bond", "General Chemistry", "On the Relationship of the Properties of the Elements to their Atomic Weights", "A New System of Chemical Philosophy", "Traité Élémentaire de Chimie", "Organic Chemistry", "March's Advanced Organic Chemistry", "The Logic of Chemical Synthesis", "Physical Chemistry", "Quantitative Chemical Analysis", "Vogel's Textbook of Quantitative Chemical Analysis", "Spectrometric Identification of Organic Compounds", "The Chemical History of a Candle", "Uncle Tungsten", "The Disappearing Spoon", "Napoleon's Buttons", "The Poisoner's Handbook", "The Elements: A Visual Exploration", "Molecules: The Elements and the Architecture of Everything", "Chemistry: The Central Science", "Shriver and Atkins' Inorganic Chemistry", "Periodic Tales", "Inorganic Chemistry", "The Principles of Chemistry", "Crucibles: The Story of Chemistry", "The Development of Modern Chemistry", "What Is Chemistry?", "The Chemistry of the Actinide and Transactinide Elements", "Chemical Kinetics and Reaction Dynamics", "Electrochemical Methods", "NMR Spectroscopy", "Organic Chemistry"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["bonding and structure", "alkanes", "stereochemistry", "substitution and elimination", "spectroscopy", "synthesis strategy"], ["the periodic table", "coordination chemistry", "organometallics", "solid state", "descriptive chemistry", "bioinorganic chemistry"], ["thermodynamics", "kinetics", "quantum chemistry", "statistical mechanics", "surfaces", "photochemistry"], ["statistics of measurement", "gravimetry", "titrimetry", "chromatography", "mass spectrometry", "quality assurance"], ["polymers", "ceramics", "semiconductors", "nanomaterials", "composites", "materials selection"], ["alchemy", "the chemical revolution", "atomic theory", "the periodic law", "the rise of synthesis", "chemistry and industry"], ["IR and Raman", "NMR", "UV-visible", "mass spec", "X-ray methods", "surface analysis"], ["galvanic cells", "electrolysis", "corrosion", "batteries", "fuel cells", "electroanalysis"]];
var FRAMES=["gave chemists a new way to see molecules", "turned a laboratory art into a predictive science", "is still the text students annotate most", "settled a debate that had run for decades", "made the invisible measurable", "defined what counts as proof in chemistry"];
var T2_TOPICS=["machine-learned retrosynthesis", "solid-state batteries", "CO2 electrocatalysis", "programmable matter", "green solvents", "quantum-dot displays", "self-healing polymers", "nitrogen fixation", "metal-organic frameworks", "flow chemistry", "single-atom catalysis", "biodegradable plastics"];
var T2_ANGLES=["mechanistic elucidation", "materials screening", "reaction optimization", "sustainability assessment", "scale-up modeling", "safety evaluation"];
var T2_METHODS=["density functional theory", "high-throughput screening", "in-situ spectroscopy", "electrochemical testing", "crystallographic analysis", "life-cycle modeling"];
var T2_OUTCOMES=["a room-temperature catalyst", "a recyclable high-performance polymer", "a validated reaction mechanism", "a battery chemistry at scale", "a green process standard", "a new materials class"];
var PROJ_BY="JAH Chemistry Projection Unit";
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
