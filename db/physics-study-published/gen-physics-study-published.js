(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="physics-study";
var SLUG="physics-study-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-physics-study-published-P-";
var FIELD="Physics";
var GENVER="jahdb-physics-study-published-1.0";
var CATS=["Classical Mechanics", "Electromagnetism", "Quantum Mechanics", "Thermodynamics", "Relativity", "Particle Physics", "Optics", "Cosmology"];
var L1=[["Philosophiae Naturalis Principia Mathematica", ["Isaac Newton"], "Royal Society, London", 1687, 0, "Newton's Principia — the laws of motion and universal gravitation, the calculus of nature. The founding text of modern physics. The greatest scientific book ever written."], ["On the Electrodynamics of Moving Bodies", ["Albert Einstein"], "Annalen der Physik, Vol. 17", 1905, 4, "Einstein's special relativity paper — time dilation, length contraction, the relativity of simultaneity. The miracle year's crown. Physics was never the same."], ["Does the Inertia of a Body Depend Upon Its Energy Content?", ["Albert Einstein"], "Annalen der Physik, Vol. 18", 1905, 4, "The three-page sequel deriving mass-energy equivalence — E=mc². The most famous equation's birth certificate. A footnote that changed the world."], ["The Feynman Lectures on Physics", ["Richard P. Feynman", "Robert B. Leighton", "Matthew Sands"], "Addison-Wesley", 1964, 0, "Feynman's Caltech lectures — the most famous physics course ever taught, in three volumes. Insight on every page. The physicist's bible."], ["Surely You're Joking, Mr. Feynman!", ["Richard P. Feynman", "Ralph Leighton"], "W. W. Norton", 1985, 0, "Feynman's picaresque memoir — safecracking at Los Alamos, bongo drums, the Nobel. Irreverent genius. The human behind the lectures."], ["The Character of Physical Law", ["Richard P. Feynman"], "MIT Press", 1965, 0, "Feynman's Messenger Lectures on gravitation, symmetry, and the arrow of time. The deepest short book in physics. Lawfulness itself, examined."], ["QED: The Strange Theory of Light and Matter", ["Richard P. Feynman"], "Princeton University Press", 1985, 1, "Feynman's lay exposition of quantum electrodynamics — arrows, mirrors, and the strange theory. The jewel of physics, explained. Nobody explains like Feynman."], ["A Brief History of Time", ["Stephen Hawking"], "Bantam Books", 1988, 7, "Hawking's cosmology bestseller — black holes, the Big Bang, the quest for a theory of everything. Ten million copies. The book that made cosmology famous."], ["The Universe in a Nutshell", ["Stephen Hawking"], "Bantam Books", 2001, 7, "Hawking's illustrated sequel — branes, holography, and the future of theory. Richly visual. Cosmology's picture book."], ["The Elegant Universe", ["Brian Greene"], "W. W. Norton", 1999, 2, "Greene's superstring theory exposition — extra dimensions, vibrating strings, the quest for unity. The string theory bible. Elegant indeed."], ["The Fabric of the Cosmos", ["Brian Greene"], "Alfred A. Knopf", 2004, 4, "Greene on space, time, and the texture of reality — from Newton to quantum teleportation. Ambitious and clear. Reality's weave, examined."], ["Relativity: The Special and General Theory", ["Albert Einstein"], "Henry Holt", 1916, 4, "Einstein's own popular exposition of relativity — the master explaining himself. Remarkably readable. The theory from its author."], ["The Principles of Quantum Mechanics", ["Paul A. M. Dirac"], "Clarendon Press, Oxford", 1930, 2, "Dirac's austere, logical formulation of quantum mechanics — bras, kets, and the relativistic electron. The theorist's scripture. Beauty as method."], ["The Physical Principles of the Quantum Theory", ["Werner Heisenberg"], "University of Chicago Press", 1930, 2, "Heisenberg's lectures on uncertainty and the Copenhagen interpretation. The quantum revolution's manifesto. Uncertainty, explained by its author."], ["The Road to Reality", ["Roger Penrose"], "Jonathan Cape", 2004, 2, "Penrose's 1,000-page guided tour from mathematics to cosmology — twistors, entropy, and consciousness. Monumental ambition. The complete journey."], ["Black Holes and Time Warps", ["Kip S. Thorne"], "W. W. Norton", 1994, 7, "Thorne's history of relativity's golden age — black holes, wormholes, and time travel. Einstein's legacy, dramatized. The definitive account."], ["The First Three Minutes", ["Steven Weinberg"], "Basic Books", 1977, 7, "Weinberg's modern view of the universe's origin — particle physics meets cosmology. The Big Bang's first popular account. Precision cosmology's prologue."], ["Dreams of a Final Theory", ["Steven Weinberg"], "Pantheon Books", 1992, 5, "Weinberg's meditation on reductionism and the search for ultimate laws. The particle physicist's credo. Final theories, considered."], ["The Trouble with Physics", ["Lee Smolin"], "Houghton Mifflin", 2006, 5, "Smolin's critique of string theory's dominance — the fall of a science. Controversial and influential. Physics' midlife crisis."], ["The Grand Design", ["Stephen Hawking", "Leonard Mlodinow"], "Bantam Books", 2010, 7, "Hawking and Mlodinow on M-theory, the multiverse, and why the universe exists. Model-dependent realism. The late Hawking's vision."], ["Six Easy Pieces", ["Richard P. Feynman"], "Perseus Books", 1994, 0, "The most accessible Feynman lectures — atoms, basic physics, gravitation. The perfect introduction. Physics' greatest hits."], ["Hyperspace", ["Michio Kaku"], "Oxford University Press", 1994, 2, "Kaku's tour of higher dimensions — from Flatland to string theory. The public's first hyperspace. Dimensions beyond seeing."], ["Physics of the Impossible", ["Michio Kaku"], "Doubleday", 2008, 2, "Kaku ranks science-fiction technologies by physical plausibility — phasers to time travel. Playful rigor. The future, graded."], ["The Dancing Wu Li Masters", ["Gary Zukav"], "William Morrow", 1979, 2, "Zukav's New Age-tinged tour of quantum mechanics — the 1979 bestseller that brought the quantum to the counterculture. Of its time. Wu Li: patterns of organic energy."], ["Mr Tompkins in Paperback", ["George Gamow"], "Cambridge University Press", 1965, 4, "Gamow's tales of a bank clerk dreaming through relativity and quantum worlds. The classic popularization. Dreams that teach."], ["One Two Three... Infinity", ["George Gamow"], "Viking Press", 1947, 0, "Gamow's tour of numbers, space, and time for the lay reader. The book that started many physicists. Infinity, made friendly."], ["Thirty Years That Shook Physics", ["George Gamow"], "Doubleday", 1966, 2, "Gamow's insider history of the quantum revolution — the heroic age retold. Warm and personal. The revolution, remembered."], ["In Search of Schrodinger's Cat", ["John Gribbin"], "Bantam Books", 1984, 2, "Gribbin's history of quantum mechanics — the puzzles that won't die. The standard popular history. The cat, explained."], ["The Quantum Universe", ["Brian Cox", "Jeff Forshaw"], "Allen Lane", 2011, 2, "Cox and Forshaw's quantum mechanics for everyone — why the subject matters. Modern and clear. The quantum, demystified."], ["Dialogue Concerning the Two Chief World Systems", ["Galileo Galilei"], "Florence", 1632, 0, "Galileo's dialogue defending Copernicus — the book that got him condemned. Science's most famous trial. The dialogue that moved the earth."], ["Discourses Concerning Two New Sciences", ["Galileo Galilei"], "Leiden", 1638, 0, "Galileo's final book — the science of motion and materials, written under house arrest. Modern physics' true birth. The two new sciences."], ["The Meaning of Relativity", ["Albert Einstein"], "Princeton University Press", 1922, 4, "Einstein's Princeton lectures — the Stafford Little lectures on relativity. The master's own summary. Concise authority."]];
var L1_TITLES=["Philosophiae Naturalis Principia Mathematica", "On the Electrodynamics of Moving Bodies", "Does the Inertia of a Body Depend Upon Its Energy Content?", "The Feynman Lectures on Physics", "Surely You're Joking, Mr. Feynman!", "The Character of Physical Law", "QED: The Strange Theory of Light and Matter", "A Brief History of Time", "The Universe in a Nutshell", "The Elegant Universe", "The Fabric of the Cosmos", "Relativity: The Special and General Theory", "The Principles of Quantum Mechanics", "The Physical Principles of the Quantum Theory", "The Road to Reality", "Black Holes and Time Warps", "The First Three Minutes", "Dreams of a Final Theory", "The Trouble with Physics", "The Grand Design", "Six Easy Pieces", "Hyperspace", "Physics of the Impossible", "The Dancing Wu Li Masters", "Mr Tompkins in Paperback", "One Two Three... Infinity", "Thirty Years That Shook Physics", "In Search of Schrodinger's Cat", "The Quantum Universe", "Dialogue Concerning the Two Chief World Systems", "Discourses Concerning Two New Sciences", "The Meaning of Relativity"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["Newton's laws", "work and energy", "momentum", "rotation", "oscillations", "gravitation"], ["electric fields", "Gauss's law", "circuits", "magnetism", "Maxwell's equations", "electromagnetic waves"], ["wave-particle duality", "the Schrodinger equation", "operators", "the hydrogen atom", "spin", "entanglement"], ["temperature and heat", "the laws of thermodynamics", "entropy", "statistical mechanics", "phase transitions", "engines"], ["special relativity", "spacetime", "general relativity", "black holes", "gravitational waves", "cosmology"], ["the Standard Model", "quarks", "symmetries", "accelerators", "neutrinos", "beyond the Standard Model"], ["reflection and refraction", "lenses", "interference", "diffraction", "polarization", "lasers"], ["the expanding universe", "the Big Bang", "dark matter", "dark energy", "structure formation", "the fate of the universe"]];
var FRAMES=["rewrote what the universe is made of", "is still the clearest path into the subject", "changed the meaning of space and time", "gave experimenters their marching orders", "remains the benchmark popularization", "turned paradox into principle"];
var T2_TOPICS=["quantum error correction", "fusion ignition", "gravitational-wave astronomy", "topological qubits", "dark matter detection", "room-temperature superconductivity", "attosecond imaging", "neutrino mass", "quantum networks", "plasma propulsion", "exoplanet atmospheres", "time crystals"];
var T2_ANGLES=["theoretical consolidation", "experimental design", "anomaly investigation", "cross-domain synthesis", "precision measurement", "computational verification"];
var T2_METHODS=["interferometry", "particle collider runs", "quantum simulation", "precision spectroscopy", "numerical relativity", "cryogenic detection"];
var T2_OUTCOMES=["a five-sigma discovery", "a validated theoretical prediction", "an order-of-magnitude precision gain", "a working prototype device", "a resolved anomaly", "a new observational window"];
var PROJ_BY="JAH Physics Projection Unit";
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
