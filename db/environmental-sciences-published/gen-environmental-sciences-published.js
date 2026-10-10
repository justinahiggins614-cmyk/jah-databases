(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="environmental-sciences";
var SLUG="environmental-sciences-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-environmental-sciences-published-P-";
var FIELD="Environmental Sciences";
var GENVER="jahdb-environmental-sciences-published-1.0";
var CATS=["Climate Science", "Conservation", "Pollution Control", "Sustainability", "Water Resources", "Ecosystems", "Environmental Policy", "Energy"];
var L1=[["Silent Spring", ["Rachel Carson"], "Houghton Mifflin", 1962, 2, "Carson's exposé of DDT and pesticide damage to wildlife and ecosystems — the book that launched the modern environmental movement. Chemical companies attacked her; the public believed her. The EPA's creation traces directly to it."], ["The Limits to Growth", ["Donella H. Meadows", "Dennis L. Meadows", "Jørgen Randers", "William W. Behrens III"], "Universe Books", 1972, 3, "The Club of Rome's World3 computer model projecting overshoot and collapse under business-as-usual growth. Controversial, mocked, then partly vindicated. It put sustainability modeling on the map."], ["A Sand County Almanac", ["Aldo Leopold"], "Oxford University Press", 1949, 1, "Leopold's Land Ethic extended moral community to soils, waters, plants, and animals. Part memoir, part philosophy. The founding text of conservation ethics."], ["Our Common Future", ["World Commission on Environment and Development"], "Oxford University Press", 1987, 6, "The Brundtland Report defined sustainable development — meeting present needs without compromising future generations. It framed Rio 1992. The definition every policy still quotes."], ["Small Is Beautiful", ["E. F. Schumacher"], "Blond & Briggs", 1973, 3, "Schumacher's economics as if people mattered — appropriate technology, Buddhist economics, against gigantism. A countercultural classic. It made smallness a virtue."], ["The Closing Circle", ["Barry Commoner"], "Alfred A. Knopf", 1971, 2, "Commoner's four laws of ecology — everything is connected, everything must go somewhere — indicting technology's assault on the ecosphere. The other 1971 environmental manifesto. It stressed production, not just population."], ["Gaia: A New Look at Life on Earth", ["James Lovelock"], "Oxford University Press", 1979, 5, "Lovelock's hypothesis that Earth functions as a self-regulating system — life maintaining conditions for life. Dismissed, then partially absorbed. It changed how scientists see the planet."], ["The Sixth Extinction", ["Elizabeth Kolbert"], "Henry Holt", 2014, 1, "Kolbert travels from the Panamanian frog to the Great Barrier Reef documenting the human-driven extinction crisis. Winner of the Pulitzer Prize. The definitive contemporary account."], ["Field Notes from a Catastrophe", ["Elizabeth Kolbert"], "Bloomsbury", 2006, 0, "Kolbert's New Yorker reporting on climate change — from Arctic villages to climate models — made warming vivid before it was fashionable. Prescient and humane. It brought the science to the public."], ["The Tragedy of the Commons", ["Garrett Hardin"], "Science, Vol. 162", 1968, 6, "Hardin's parable of herders overgrazing shared pasture argued that unregulated commons invite ruin. Immensely influential and much critiqued — Ostrom answered it. The most cited environmental essay ever."], ["Thinking in Systems", ["Donella H. Meadows"], "Chelsea Green", 2008, 3, "Meadows's posthumous primer on stocks, flows, feedbacks, and leverage points — systems thinking for citizens. Clear and wise. The best introduction to the discipline."], ["Collapse", ["Jared Diamond"], "Viking Press", 2005, 5, "Diamond compares societies that failed — Easter Island, the Maya, the Norse Greenlanders — with those that survived, extracting lessons. A natural experiment in ecocide. It made collapse a serious subject."], ["The End of Nature", ["Bill McKibben"], "Random House", 1989, 0, "McKibben's meditation on what climate change means: nature as independent force is over. The first popular book on global warming. It named the grief of the Anthropocene."], ["Eaarth", ["Bill McKibben"], "Times Books", 2010, 0, "McKibben argues we inhabit a new, tougher planet — Eaarth — and must adapt with relocalized, resilient economies. A sequel in a darker key. It shifted the movement toward adaptation."], ["The Weather Makers", ["Tim Flannery"], "Text Publishing", 2005, 0, "Flannery's tour of climate science and solutions by Australia's leading ecologist. Accessible and urgent. It internationalized the climate conversation."], ["Cradle to Cradle", ["William McDonough", "Michael Braungart"], "North Point Press", 2002, 3, "McDonough and Braungart's manifesto for waste-equals-food design — technical and biological nutrients cycling endlessly. It launched circular design. Industry took notice."], ["The Population Bomb", ["Paul R. Ehrlich"], "Ballantine Books", 1968, 5, "Ehrlich's alarm about population outrunning food — overstated in timing, right about pressure. The most controversial environmental bestseller. It forced the population question."], ["Cadillac Desert", ["Marc Reisner"], "Viking Press", 1986, 4, "Reisner's history of water development in the American West — dams, aqueducts, and the Bureau of Reclamation's empire. Definitive and devastating. Western water politics starts here."], ["The Control of Nature", ["John McPhee"], "Farrar, Straus and Giroux", 1989, 4, "McPhee's triptych — the Army Corps vs. the Mississippi, Icelanders vs. lava, Los Angeles vs. debris flows — on humanity's doomed war with geology. Masterful reporting. Nature bats last."], ["Desert Solitaire", ["Edward Abbey"], "McGraw-Hill", 1968, 1, "Abbey's season as a park ranger in Utah's canyon country — lyrical, furious, anarchic. The bible of wilderness defenders. Industrial tourism, he wrote, is paving paradise."], ["Walden", ["Henry David Thoreau"], "Ticknor and Fields", 1854, 5, "Thoreau's account of two years at Walden Pond — simplicity, self-reliance, and civil disobedience's seedbed. The founding text of American environmental thought. I went to the woods to live deliberately."], ["Man and Nature", ["George Perkins Marsh"], "Charles Scribner", 1864, 5, "Marsh's documentation of humanity's destructive transformation of the earth — deforestation, erosion, extinction. The first great work of environmental history. It warned before the damage was done."], ["Kyoto Protocol", ["United Nations Framework Convention on Climate Change"], "United Nations", 1997, 6, "The first binding international treaty limiting greenhouse gases — Annex I targets, emissions trading, the Clean Development Mechanism. Ratified by 192 parties. The architecture all climate diplomacy builds on."], ["Paris Agreement", ["United Nations Framework Convention on Climate Change"], "United Nations", 2015, 6, "The 2015 accord committing nations to hold warming well below 2°C through nationally determined contributions. Universal where Kyoto was partial. The current framework of climate action."], ["IPCC First Assessment Report", ["Intergovernmental Panel on Climate Change"], "Cambridge University Press", 1990, 0, "The IPCC's first consensus — warming is real, humans contribute, action is warranted. It launched the negotiations leading to Rio. The scientific foundation of climate policy."], ["The Uninhabitable Earth", ["David Wallace-Wells"], "Tim Duggan Books", 2019, 0, "Wallace-Wells's tour of warming's cascading horrors — heat, hunger, drowning, conflict — expanded from his viral essay. Bleak and galvanizing. It reset the public's sense of stakes."], ["Drawdown", ["Paul Hawken"], "Penguin Books", 2017, 7, "Hawken's ranked compendium of 80 climate solutions by impact — from refrigerant management to girls' education. Solutions-oriented and rigorous. The playbook of what works."], ["An Inconvenient Truth", ["Al Gore"], "Rodale Press", 2006, 0, "Gore's slide-show-turned-book and film making the climate case to millions. The documentary won an Oscar. It mainstreamed the hockey stick."], ["Hot, Flat, and Crowded", ["Thomas L. Friedman"], "Farrar, Straus and Giroux", 2008, 7, "Friedman's argument that energy technology is the defining project of the age — green as the new red, white, and blue. Journalistic and sweeping. It framed clean energy as geopolitics."], ["The Omnivore's Dilemma", ["Michael Pollan"], "Penguin Press", 2006, 3, "Pollan traces four meals — industrial, organic, local, hunted — through the food system. Eat food, not too much, mostly plants. It changed how America eats."], ["Encounters with the Archdruid", ["John McPhee"], "Farrar, Straus and Giroux", 1971, 1, "McPhee stages three debates between conservationist David Brower and his development-minded opponents. Even-handed and revealing. The classic portrait of the environmentalist's dilemma."], ["Plan B: Rescuing a Planet Under Stress and a Civilization in Trouble", ["Lester R. Brown"], "W. W. Norton", 2003, 3, "Brown's mobilization plan — stabilizing population, eradicating poverty, restoring ecosystems. The Earth Policy Institute's blueprint. Urgent and concrete."]];
var L1_TITLES=["Silent Spring", "The Limits to Growth", "A Sand County Almanac", "Our Common Future", "Small Is Beautiful", "The Closing Circle", "Gaia: A New Look at Life on Earth", "The Sixth Extinction", "Field Notes from a Catastrophe", "The Tragedy of the Commons", "Thinking in Systems", "Collapse", "The End of Nature", "Eaarth", "The Weather Makers", "Cradle to Cradle", "The Population Bomb", "Cadillac Desert", "The Control of Nature", "Desert Solitaire", "Walden", "Man and Nature", "Kyoto Protocol", "Paris Agreement", "IPCC First Assessment Report", "The Uninhabitable Earth", "Drawdown", "An Inconvenient Truth", "Hot, Flat, and Crowded", "The Omnivore's Dilemma", "Encounters with the Archdruid", "Plan B: Rescuing a Planet Under Stress and a Civilization in Trouble"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["the greenhouse effect", "climate feedbacks", "paleoclimate", "models and projections", "impacts", "mitigation pathways"], ["biodiversity hotspots", "protected areas", "restoration ecology", "invasive species", "captive breeding", "conservation genetics"], ["air quality", "water pollution", "hazardous waste", "the precautionary principle", "remediation", "environmental monitoring"], ["the triple bottom line", "circular economy", "green design", "corporate reporting", "sustainable agriculture", "degrowth debates"], ["the hydrologic cycle", "watersheds", "groundwater", "water law", "desalination", "water and conflict"], ["ecosystem services", "trophic cascades", "resilience theory", "disturbance regimes", "biomes", "novel ecosystems"], ["NEPA and impact assessment", "command and control", "market instruments", "international regimes", "environmental justice", "compliance"], ["fossil fuels", "nuclear power", "solar and wind", "grid integration", "energy storage", "the energy transition"]];
var FRAMES=["put the crisis into words the public could feel", "moved the issue from the margins to the agenda", "gave activists the evidence they needed", "forced governments to answer", "defined the vocabulary of the debate", "is still the benchmark every new book is measured against"];
var T2_TOPICS=["carbon removal verification", "climate adaptation finance", "biodiversity credits", "plastic treaty implementation", "urban heat resilience", "rewilding corridors", "green hydrogen scale-up", "ocean alkalinity enhancement", "food-system decarbonization", "environmental justice mapping", "wetland restoration", "circular materials"];
var T2_ANGLES=["policy gap analysis", "scenario modeling", "cost-benefit synthesis", "treaty compliance tracking", "community impact assessment", "technology readiness review"];
var T2_METHODS=["integrated assessment modeling", "satellite time-series analysis", "life-cycle assessment", "stakeholder surveys", "watershed monitoring", "scenario ensemble comparison"];
var T2_OUTCOMES=["a verified mitigation pathway", "enforceable treaty benchmarks", "a funded adaptation plan", "quantified co-benefits", "a community consent framework", "a monitoring standard"];
var PROJ_BY="JAH Environmental Projection Unit";
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
