(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="earth-sciences";
var SLUG="earth-sciences-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-earth-sciences-published-P-";
var FIELD="Earth Sciences";
var GENVER="jahdb-earth-sciences-published-1.0";
var CATS=["Geology", "Oceanography", "Meteorology", "Seismology", "Paleontology", "Hydrology", "Mineralogy", "Plate Tectonics"];
var L1=[["Principles of Geology", ["Charles Lyell"], "John Murray, London", 1833, 0, "Lyell's uniformitarian manifesto — the present is the key to the past — giving Darwin his deep time. Three volumes that remade geology. The book Darwin carried on the Beagle."], ["Theory of the Earth", ["James Hutton"], "Transactions of the Royal Society of Edinburgh", 1788, 0, "Hutton's paper declaring no vestige of a beginning, no prospect of an end — founding modern geology. Deep time discovered. The most important paper in earth science."], ["The Map That Changed the World", ["Simon Winchester"], "HarperCollins", 2001, 0, "Winchester's biography of William Smith, the canal surveyor who made the first geological map of England. Science history as adventure. The map that revealed strata."], ["Annals of the Former World", ["John McPhee"], "Farrar, Straus and Giroux", 1998, 0, "McPhee's Pulitzer-winning synthesis of four books on North American geology — deep time made readable. The great American geology book. Four hundred million years in 700 pages."], ["Basin and Range", ["John McPhee"], "Farrar, Straus and Giroux", 1981, 0, "McPhee's tour of Basin and Range geology with Caltech geologists — extension, deep time, plain prose. The first of the Annals quartet. Geology as literature."], ["Rising from the Plains", ["John McPhee"], "Farrar, Straus and Giroux", 1986, 0, "McPhee crosses Wyoming with geologist David Love — the Rockies' biography. The Annals' most personal volume. Deep time, human scale."], ["In Suspect Terrain", ["John McPhee"], "Farrar, Straus and Giroux", 1983, 0, "McPhee in the Appalachians with USGS geologists — ancient mountains, young science. The Annals' eastern volume. Folded rock, unfolded story."], ["Assembling California", ["John McPhee"], "Farrar, Straus and Giroux", 1993, 0, "McPhee's account of California as assembled terranes — the state's geology as collage. The Annals' finale. Plate tectonics in prose."], ["The Control of Nature", ["John McPhee"], "Farrar, Straus and Giroux", 1989, 2, "McPhee on the Corps vs. the Mississippi, Icelanders vs. lava, LA vs. debris flows. Nature bats last. The classic of human hubris."], ["Magnetic Anomalies Over Oceanic Ridges", ["Frederick J. Vine", "Drummond H. Matthews"], "Nature, Vol. 199", 1963, 7, "Vine and Matthews showed seafloor magnetic stripes record reversals — confirming seafloor spreading. The keystone of plate tectonics. A short paper that moved continents."], ["History of Ocean Basins", ["Harry H. Hess"], "Petrologic Studies (Geological Society of America)", 1962, 7, "Hess's geopoetry proposing seafloor spreading — new crust born at ridges, consumed at trenches. Privately circulated, hugely influential. The idea that unlocked tectonics."], ["The Sea Around Us", ["Rachel Carson"], "Oxford University Press", 1951, 1, "Carson's lyrical oceanography — the sea's birth, currents, and life — a bestseller before Silent Spring. The ocean made poetic. Science writing at its finest."], ["The Edge of the Sea", ["Rachel Carson"], "Houghton Mifflin", 1955, 1, "Carson's guide to Atlantic shore life — tide pools as worlds. Intimate and precise. The seashore classic."], ["Under the Sea Wind", ["Rachel Carson"], "Simon & Schuster", 1941, 1, "Carson's first book — the ocean from a bird's, a fish's, and an eel's view. Lyrical natural history. The trilogy's beginning."], ["Krakatoa: The Day the World Exploded", ["Simon Winchester"], "HarperCollins", 2003, 0, "Winchester's account of the 1883 eruption — the explosion heard round the world and its aftermath. Disaster history at its best. The day the sky fell."], ["A Crack in the Edge of the World", ["Simon Winchester"], "HarperCollins", 2005, 3, "Winchester on the 1906 San Francisco earthquake and the science of faults. America confronts plate tectonics. The quake that woke geology."], ["The Big Ones", ["Lucy Jones"], "Doubleday", 2018, 3, "Seismologist Jones on the history and future of great earthquakes — what we know, what we fear. The definitive popular seismology. Calm science about violent earth."], ["Quakeland", ["Kathryn Miles"], "Dutton", 2017, 3, "Miles's tour of American earthquake risk — New Madrid, Cascadia, the unknown faults. Eye-opening and urgent. The shaking continent."], ["A Neoproterozoic Snowball Earth", ["Paul F. Hoffman", "Alan J. Kaufman", "Galen P. Halverson", "Daniel P. Schrag"], "Science, Vol. 281", 1998, 4, "Hoffman proposed the entire planet froze over 600 million years ago — ice to the equator. Radical and testable. It rewrote Precambrian history."], ["The Story of Earth", ["Robert M. Hazen"], "Viking Press", 2012, 0, "Hazen's biography of the planet — mineral evolution coevolving with life. The first mineralogist's earth history. Rocks and life, together."], ["The Ends of the World", ["Peter Brannen"], "Ecco Press", 2017, 4, "Brannen's tour of the Big Five mass extinctions — the ends of worlds before ours. Vivid deep-time journalism. Extinction as prologue."], ["Rare Earth", ["Peter D. Ward", "Donald Brownlee"], "Copernicus Books", 2000, 4, "Ward and Brownlee argue complex life is rare — the Rare Earth hypothesis. Provocative astrobiology. It challenged the optimism of SETI."], ["Earth: An Introduction to Physical Geology", ["Edward J. Tarbuck", "Frederick K. Lutgens"], "Charles E. Merrill", 1984, 0, "The dominant physical geology textbook — clear, illustrated, comprehensive. Millions learned the earth from Tarbuck. The classroom standard."], ["Understanding Earth", ["John Grotzinger", "Thomas H. Jordan", "Frank Press", "Raymond Siever"], "W. H. Freeman", 1999, 0, "The Caltech team's modern earth science text — process-oriented and rigorous. The thinking geologist's text. Depth with clarity."], ["The Dynamic Earth", ["Brian J. Skinner", "Stephen C. Porter"], "John Wiley & Sons", 1987, 0, "Skinner and Porter's process-focused physical geology — systems thinking for the earth. Influential pedagogy. The earth as machine."], ["Volcanoes", ["Peter Francis"], "Oxford University Press", 1976, 0, "Francis's classic volcanology text — eruptions, products, hazards. The volcanologist's handbook. Fire made systematic."], ["Structural Geology", ["Haakon Fossen"], "Cambridge University Press", 2010, 0, "Fossen's beautifully illustrated structural geology — deformation from outcrop to orogen. The modern standard. Structure made visible."], ["Sedimentary Rocks in the Field", ["Maurice E. Tucker"], "John Wiley & Sons", 1982, 0, "Tucker's field guide to reading sedimentary rocks — the stratigrapher's companion. Practical and precise. The field geologist's pocket book."], ["The Field Guide to Geology", ["David Lambert"], "Checkmark Books", 1988, 0, "Lambert's illustrated introduction to rocks, minerals, and landforms. The beginner's companion. Geology outdoors."], ["An Introduction to Seismology, Earthquakes, and Earth Structure", ["Seth Stein", "Michael Wysession"], "Blackwell", 2003, 3, "Stein and Wysession's modern seismology text — waves, sources, and structure. The graduate standard. Rigorous and complete."], ["Atmosphere, Weather and Climate", ["Roger G. Barry", "Richard J. Chorley"], "Methuen", 1968, 2, "Barry and Chorley's classic meteorology text — the atmosphere explained. The standard for decades. Weather made systematic."], ["Oceanography: An Invitation to Marine Science", ["Tom S. Garrison"], "Wadsworth", 1993, 1, "Garrison's accessible oceanography text — inviting students into marine science. The popular course text. The ocean, explained."]];
var L1_TITLES=["Principles of Geology", "Theory of the Earth", "The Map That Changed the World", "Annals of the Former World", "Basin and Range", "Rising from the Plains", "In Suspect Terrain", "Assembling California", "The Control of Nature", "Magnetic Anomalies Over Oceanic Ridges", "History of Ocean Basins", "The Sea Around Us", "The Edge of the Sea", "Under the Sea Wind", "Krakatoa: The Day the World Exploded", "A Crack in the Edge of the World", "The Big Ones", "Quakeland", "A Neoproterozoic Snowball Earth", "The Story of Earth", "The Ends of the World", "Rare Earth", "Earth: An Introduction to Physical Geology", "Understanding Earth", "The Dynamic Earth", "Volcanoes", "Structural Geology", "Sedimentary Rocks in the Field", "The Field Guide to Geology", "An Introduction to Seismology, Earthquakes, and Earth Structure", "Atmosphere, Weather and Climate", "Oceanography: An Invitation to Marine Science"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["minerals and rocks", "plate tectonics", "volcanoes", "earthquakes", "mountain building", "geologic time"], ["ocean basins", "currents", "waves and tides", "marine geology", "ocean chemistry", "the ocean and climate"], ["the atmosphere", "moisture and clouds", "air masses", "storms", "climate", "forecasting"], ["faults", "seismic waves", "magnitude scales", "hazards", "prediction", "engineering"], ["fossilization", "the fossil record", "mass extinctions", "dinosaurs", "human origins", "the tree of life"], ["the water cycle", "rivers", "groundwater", "glaciers", "coasts", "water management"], ["crystals", "silicates", "ore minerals", "gems", "identification", "mineral resources"], ["continental drift", "seafloor spreading", "subduction", "hotspots", "orogeny", "the Wilson cycle"]];
var FRAMES=["revealed deep time to a disbelieving world", "gave the planet a coherent biography", "turned field observation into global theory", "is still the most readable geology ever written", "settled what moves the continents", "made the earth feel alive underfoot"];
var T2_TOPICS=["induced seismicity", "deep-ocean mining", "atmospheric rivers", "earthquake early warning", "microplastic transport", "geologic carbon storage", "volcanic ash forecasting", "groundwater depletion", "permafrost carbon", "ocean heat content", "landslide prediction", "critical mineral supply"];
var T2_ANGLES=["hazard assessment", "process modeling", "monitoring network design", "paleo-proxy calibration", "resource evaluation", "forecast verification"];
var T2_METHODS=["seismic tomography", "satellite altimetry", "ice-core analysis", "borehole logging", "LiDAR mapping", "ocean glider transects"];
var T2_OUTCOMES=["a validated hazard map", "an operational early-warning threshold", "a calibrated climate proxy", "a safe storage protocol", "a resource inventory", "a forecast skill benchmark"];
var PROJ_BY="JAH Earth Science Projection Unit";
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
