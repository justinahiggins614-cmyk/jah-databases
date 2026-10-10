(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="mathematics-study";
var SLUG="mathematics-study-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-mathematics-study-published-P-";
var FIELD="Mathematics";
var GENVER="jahdb-mathematics-study-published-1.0";
var CATS=["Algebra", "Geometry", "Calculus", "Number Theory", "Topology", "Probability", "Logic", "History of Mathematics"];
var L1=[["Elements", ["Euclid"], "Alexandria", -300, 1, "Euclid's thirteen books — definitions, postulates, and proofs founding geometry for two millennia. The most successful textbook in history. Every proof since echoes it."], ["Arithmetica", ["Diophantus"], "Alexandria", 250, 0, "Diophantus's algebra — solving determinate and indeterminate equations, the Diophantine tradition. The father of algebra. Equations as puzzles."], ["Liber Abaci", ["Leonardo of Pisa (Fibonacci)"], "Pisa", 1202, 7, "Fibonacci's book introducing Hindu-Arabic numerals to Europe — and the rabbit problem yielding his sequence. It changed how Europe calculated. The West learns to count."], ["Ars Magna", ["Gerolamo Cardano"], "Nuremberg", 1545, 0, "Cardano's great art — solutions to cubic and quartic equations, the first printed algebra. Tartaglia's secret, published. The cubic, conquered."], ["La Geometrie", ["Rene Descartes"], "Leiden", 1637, 1, "Descartes's appendix founding analytic geometry — algebra married to curves. Coordinates changed mathematics. The plane becomes numbers."], ["Introductio in analysin infinitorum", ["Leonhard Euler"], "Lausanne", 1748, 2, "Euler's introduction to infinite analysis — functions, series, and e, i, pi in modern notation. The most influential textbook of the 18th century. Analysis begins here."], ["Disquisitiones Arithmeticae", ["Carl Friedrich Gauss"], "Leipzig", 1801, 3, "Gauss's number theory masterwork — congruences, quadratic reciprocity, cyclotomy. Written at 21. The queen of mathematics, crowned."], ["Principia Mathematica", ["Bertrand Russell", "Alfred North Whitehead"], "Cambridge University Press", 1913, 6, "The three-volume attempt to derive mathematics from logic — 379 pages to prove 1+1=2. Monumental and doomed. Logicism's great effort."], ["Grundlagen der Geometrie", ["David Hilbert"], "Teubner, Leipzig", 1899, 1, "Hilbert's axiomatic foundations of geometry — rigor replacing intuition. The axiomatic method's model. Geometry, rebuilt."], ["Godel, Escher, Bach", ["Douglas R. Hofstadter"], "Basic Books", 1979, 6, "Hofstadter's Pulitzer-winning fugue on self-reference — minds, machines, and meaning. The cult classic of cognitive science. Strange loops all the way down."], ["The Man Who Knew Infinity", ["Robert Kanigel"], "Charles Scribner's Sons", 1991, 7, "Kanigel's biography of Ramanujan — the self-taught Indian genius and Hardy. Mathematics' most moving story. Infinity, known."], ["Fermat's Enigma", ["Simon Singh"], "Walker & Company", 1997, 3, "Singh's account of Wiles's proof of Fermat's Last Theorem — 350 years to QED. The great mathematical detective story. The margin was too small; the proof was not."], ["The Music of the Primes", ["Marcus du Sautoy"], "HarperCollins", 2003, 3, "Du Sautoy's history of the Riemann hypothesis — the primes' secret music. The million-dollar problem, humanized. The zeta function's mystery."], ["Zero: The Biography of a Dangerous Idea", ["Charles Seife"], "Viking Press", 2000, 7, "Seife's history of zero — from Babylon to black holes. Nothing, made fascinating. The dangerous idea."], ["The Joy of x", ["Steven Strogatz"], "Houghton Mifflin Harcourt", 2012, 2, "Strogatz's guided tour from arithmetic to calculus — the New York Times columns in book form. Mathematics' friendliest guide. x marks the joy."], ["Infinite Powers", ["Steven Strogatz"], "Houghton Mifflin Harcourt", 2019, 2, "Strogatz's history of calculus — humanity's greatest idea, from Archimedes to the present. Calculus as civilization. The universe's language."], ["How Not to Be Wrong", ["Jordan Ellenberg"], "Penguin Press", 2014, 5, "Ellenberg's power of mathematical thinking — linearity, inference, and existence. Math for citizens. Wrongness, avoided."], ["Shape", ["Jordan Ellenberg"], "Penguin Press", 2021, 1, "Ellenberg's geometry — how it shapes politics, pandemics, and AI. The sequel's triumph. Geometry everywhere."], ["Flatland", ["Edwin A. Abbott"], "Seeley & Co., London", 1884, 1, "Abbott's romance of many dimensions — a square's journey through Lineland, Flatland, and Spaceland. The dimension classic. Satire in geometry."], ["A Mathematician's Apology", ["G. H. Hardy"], "Cambridge University Press", 1940, 7, "Hardy's melancholy defense of pure mathematics — beauty as justification. The mathematician's confession. Uselessness, celebrated."], ["Men of Mathematics", ["Eric Temple Bell"], "Simon & Schuster", 1937, 7, "Bell's biographical history — the lives behind the theorems. The book that recruited generations. Mathematics with heroes."], ["The Fractal Geometry of Nature", ["Benoit Mandelbrot"], "W. H. Freeman", 1982, 1, "Mandelbrot's manifesto — clouds are not spheres, mountains are not cones. Fractals everywhere. Roughness, geometrized."], ["Chaos", ["James Gleick"], "Viking Press", 1987, 5, "Gleick's history of chaos theory — the butterfly effect and strange attractors. The 1987 bestseller. Order within chaos."], ["What Is Mathematics?", ["Richard Courant", "Herbert Robbins"], "Oxford University Press", 1941, 7, "Courant and Robbins's panoramic introduction — the classic for the serious beginner. Einstein praised it. Mathematics, whole."], ["A Course of Modern Analysis", ["Edmund T. Whittaker", "George N. Watson"], "Cambridge University Press", 1902, 2, "Whittaker and Watson's rigorous analysis — the Cambridge Tripos bible. Generations of analysts trained on it. Rigor's reference."], ["The Mathematical Experience", ["Philip J. Davis", "Reuben Hersh"], "Birkhauser", 1981, 7, "Davis and Hersh on what mathematics is — philosophy through practice. The humanistic turn. Experience over formalism."], ["The Number Devil", ["Hans Magnus Enzensberger"], "Metropolitan Books", 1997, 3, "Enzensberger's mathematical adventure for young readers — Robert's dreams with the number devil. The children's classic. Nightmares that teach."], ["Prime Obsession", ["John Derbyshire"], "Joseph Henry Press", 2003, 3, "Derbyshire's Riemann hypothesis — alternating chapters of history and mathematics. The prime obsession. The hypothesis, humanized."], ["e: The Story of a Number", ["Eli Maor"], "Princeton University Press", 1994, 2, "Maor's biography of e — from compound interest to Euler's identity. The number's life story. e, explained."], ["Trigonometric Delights", ["Eli Maor"], "Princeton University Press", 1998, 1, "Maor's history of trigonometry — sines and chords through the ages, from Ptolemy to Fourier. Delightful indeed. Angles with a rich history."], ["Here's Looking at Euclid", ["Alex Bellos"], "Free Press", 2010, 7, "Bellos's global tour of mathematical cultures — from the Amazon to Japan. Math around the world. Numbers, everywhere."], ["Does God Play Dice?", ["Ian Stewart"], "Basil Blackwell", 1989, 5, "Stewart's mathematics of chaos — the new mathematics of nature. The sequel to the revolution. Dice, loaded by chaos."]];
var L1_TITLES=["Elements", "Arithmetica", "Liber Abaci", "Ars Magna", "La Geometrie", "Introductio in analysin infinitorum", "Disquisitiones Arithmeticae", "Principia Mathematica", "Grundlagen der Geometrie", "Godel, Escher, Bach", "The Man Who Knew Infinity", "Fermat's Enigma", "The Music of the Primes", "Zero: The Biography of a Dangerous Idea", "The Joy of x", "Infinite Powers", "How Not to Be Wrong", "Shape", "Flatland", "A Mathematician's Apology", "Men of Mathematics", "The Fractal Geometry of Nature", "Chaos", "What Is Mathematics?", "A Course of Modern Analysis", "The Mathematical Experience", "The Number Devil", "Prime Obsession", "e: The Story of a Number", "Trigonometric Delights", "Here's Looking at Euclid", "Does God Play Dice?"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["groups", "rings", "fields", "vector spaces", "polynomials", "Galois theory"], ["Euclidean geometry", "constructions", "analytic geometry", "non-Euclidean geometry", "differential geometry", "symmetry"], ["limits", "derivatives", "integrals", "series", "multivariable calculus", "differential equations"], ["divisibility", "primes", "congruences", "Diophantine equations", "the zeta function", "elliptic curves"], ["open and closed sets", "continuity", "compactness", "connectedness", "homotopy", "manifolds"], ["sample spaces", "random variables", "distributions", "limit theorems", "stochastic processes", "simulation"], ["propositional logic", "quantifiers", "proof methods", "sets", "incompleteness", "computability"], ["Babylon and Egypt", "the Greeks", "the Islamic golden age", "the calculus priority dispute", "the 19th century", "the modern era"]];
var FRAMES=["is where the modern subject begins", "proved what centuries could not", "gave the field its definitive exposition", "turned intuition into ironclad proof", "is still the book mathematicians press on students", "made the abstract feel inevitable"];
var T2_TOPICS=["automated theorem proving", "post-quantum cryptography", "topological data analysis", "Langlands program", "prime gaps", "machine conjectures", "higher category theory", "compressed sensing", "arithmetic dynamics", "proof assistants", "random matrices", "homotopy type theory"];
var T2_ANGLES=["conjecture formulation", "proof strategy", "computational exploration", "historical reconstruction", "pedagogical reframing", "cross-field transfer"];
var T2_METHODS=["computer-assisted proof", "large-scale computation", "formal verification", "heuristic search", "diagrammatic reasoning", "axiomatic analysis"];
var T2_OUTCOMES=["a verified proof of a long-standing conjecture", "a new invariant", "an efficient algorithm", "a unifying framework", "a counterexample", "a teachable exposition"];
var PROJ_BY="JAH Mathematics Projection Unit";
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
