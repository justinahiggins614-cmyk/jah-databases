(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="wildlife";
var SLUG="wildlife-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-wildlife-published-P-";
var FIELD="Natural Environments and Wildlife";
var GENVER="jahdb-wildlife-published-1.0";
var CATS=["Mammals", "Birds", "Marine Life", "Reptiles and Amphibians", "Insects", "Habitats", "Conservation", "Endangered Species"];
var L1=[["Life on Earth", ["David Attenborough"], "William Collins", 1979, 5, "The companion to the landmark BBC series — a 3.5-billion-year tour of life's diversity. It made Attenborough the world's naturalist. Natural history television's founding text."], ["The Living Planet", ["David Attenborough"], "William Collins", 1984, 5, "Attenborough's ecology series in book form — how animals fit their habitats, from tundra to rainforest. The sequel that deepened the story. A masterclass in ecological thinking."], ["The Trials of Life", ["David Attenborough"], "William Collins", 1990, 5, "The life-cycle series — birth, growth, courtship, parenthood — across the animal kingdom. Behavior made epic. Attenborough at his most intimate."], ["The Life of Mammals", ["David Attenborough"], "BBC Books", 2002, 0, "Ten programs on mammalian ingenuity — insectivores to primates, ten design solutions. The mammal book to end mammal books. Comprehensive and warm."], ["The Serengeti Lion", ["George B. Schaller"], "University of Chicago Press", 1972, 0, "Schaller's landmark study of lion social behavior and predator-prey dynamics in the Serengeti. The foundation of modern carnivore ecology. Field biology's gold standard."], ["The Year of the Gorilla", ["George B. Schaller"], "University of Chicago Press", 1964, 0, "Schaller's pioneering year with mountain gorillas in the Virungas — the first scientific study, dispelling the monster myth. It made gorilla research possible. Fossey followed his trail."], ["Gorillas in the Mist", ["Dian Fossey"], "Houghton Mifflin", 1983, 0, "Fossey's account of 13 years with Rwanda's mountain gorillas — habituation, poaching wars, and murder. Passionate and tragic. It made gorillas individuals to the world."], ["In the Shadow of Man", ["Jane Goodall"], "Houghton Mifflin", 1971, 0, "Goodall's Gombe chimpanzee study — tool use, warfare, personalities — overturning human uniqueness. The most famous field study ever. It redefined the primate."], ["Through a Window", ["Jane Goodall"], "Houghton Mifflin", 1990, 0, "Goodall's 30-year retrospective on the Gombe chimps — generations, politics, and grief. Deeper and sadder than the first book. A lifetime's observation distilled."], ["The Snow Leopard", ["Peter Matthiessen"], "Viking Press", 1978, 5, "Matthiessen's trek in the Himalayas seeking the snow leopard — part natural history, part grief memoir. Winner of the National Book Award. The rarest cat, the deepest book."], ["Never Cry Wolf", ["Farley Mowat"], "McClelland & Stewart", 1963, 0, "Mowat's subversive account of studying Arctic wolves for the Canadian government — finding they ate mice, not caribou. It changed predator policy. The book that saved the wolf's reputation."], ["A Whale for the Killing", ["Farley Mowat"], "McClelland & Stewart", 1972, 2, "Mowat's furious account of a fin whale trapped and tormented in Newfoundland. It galvanized the save-the-whales movement. Activism in book form."], ["The Peregrine", ["J. A. Baker"], "Harper & Row", 1967, 1, "Baker's obsessive winter following peregrines over East Anglian marshes — prose of hallucinatory intensity. The cult classic of bird writing. It documented DDT's toll on raptors."], ["H is for Hawk", ["Helen Macdonald"], "Jonathan Cape", 2014, 1, "Macdonald's memoir of training a goshawk while grieving her father — falconry, T.H. White, and wildness. Winner of the Samuel Johnson Prize. The modern classic of the genre."], ["The Song of the Dodo", ["David Quammen"], "Scribner", 1996, 5, "Quammen's epic on island biogeography and extinction — Wallace, Darwin, and the modern fragmentation crisis. The best book on why fragments lose species. Deeply reported, beautifully written."], ["Ring of Bright Water", ["Gavin Maxwell"], "E. P. Dutton", 1960, 0, "Maxwell's memoir of raising otters at a remote Scottish cottage — Mij the otter became famous. Charming and melancholy. It made otters beloved."], ["Born Free", ["Joy Adamson"], "Pantheon Books", 1960, 0, "Adamson's story of raising Elsa the orphaned lioness and returning her to the wild. A global sensation. It launched wildlife rehabilitation as a public cause."], ["The Last Panda", ["George B. Schaller"], "University of Chicago Press", 1993, 0, "Schaller's definitive panda study in Sichuan — the science behind the symbol. Rigorous and unsentimental. It grounded panda conservation in ecology."], ["The Tiger", ["John Vaillant"], "Alfred A. Knopf", 2010, 0, "Vaillant's account of a man-eating Amur tiger in the Russian Far East — natural history, indigenous knowledge, and a murder mystery. Gripping and profound. The great tiger book."], ["The Birds of America", ["John James Audubon"], "Self-published, London", 1838, 1, "Audubon's double-elephant-folio engravings of 435 North American bird species — the greatest ornithological art ever made. Subscribed across two continents. America's founding natural history monument."], ["A Field Guide to the Birds", ["Roger Tory Peterson"], "Houghton Mifflin", 1934, 1, "Peterson's revolutionary field guide — identification by field marks, arrows pointing to what matters. It democratized birding. Every modern guide descends from it."], ["The Sibley Guide to Birds", ["David Allen Sibley"], "Alfred A. Knopf", 2000, 1, "Sibley's 6,600-painting masterwork covering North American birds in exhaustive detail. The birder's bible. A lifetime of fieldwork in one volume."], ["The Behavior Guide to African Mammals", ["Richard D. Estes"], "University of California Press", 1991, 0, "Estes's comprehensive guide to the behavior of Africa's large mammals — the safari-goer's ethology text. Definitive and practical. The standard reference."], ["Whales, Dolphins and Porpoises", ["Mark Carwardine"], "Dorling Kindersley", 1995, 2, "Carwardine's handbook to the world's cetaceans — identification, behavior, conservation. The whale-watcher's companion. Authoritative and accessible."], ["IUCN Red List of Threatened Species", ["International Union for Conservation of Nature"], "IUCN, Gland", 1964, 7, "The global inventory of species' extinction risk — the categories from Least Concern to Extinct that govern conservation. Updated continuously since 1964. The barometer of biodiversity."], ["Convention on International Trade in Endangered Species (CITES)", ["United Nations"], "United Nations", 1973, 6, "The 1973 treaty regulating international wildlife trade through three appendices of protection. 184 parties strong. The legal backbone of anti-trafficking."], ["Endangered Species Act", ["U.S. Congress"], "U.S. Statutes", 1973, 6, "America's 1973 species-protection law — listing, critical habitat, and the duty to avoid jeopardy. The strongest conservation law ever written. Bald eagles and gray wolves recovered under it."], ["The Deer and the Tiger", ["George B. Schaller"], "University of Chicago Press", 1967, 0, "Schaller's study of tiger predation in Kanha, India — the ecology of the great cat. The foundation of tiger science. Field craft at its finest."], ["Grizzly Years: In Search of the American Wilderness", ["Doug Peacock"], "Henry Holt", 1990, 0, "Peacock's memoir of years among Yellowstone's grizzlies as a Green Beret veteran healing from Vietnam. Raw and reverent. It made the grizzly a symbol of wilderness itself."], ["The Wolf: The Ecology and Behavior of an Endangered Species", ["L. David Mech"], "Natural History Press", 1970, 0, "Mech's landmark Isle Royale wolf-moose study — the scientific foundation of wolf ecology. Decades of fieldwork distilled. The wolf book against which all others are measured."], ["Cry of the Kalahari", ["Mark Owens", "Delia Owens"], "Houghton Mifflin", 1984, 5, "The Owenses' seven years in Botswana's Kalahari studying lions, hyenas, and jackals — adventure and science. A bestseller of field biology. The desert's predators, revealed."], ["The Elephant Whisperer", ["Lawrence Anthony", "Graham Spence"], "Thomas Dunne Books", 2009, 0, "Anthony's account of rescuing a traumatized elephant herd in Zululand — and their farewell after his death. Moving and controversial. The human-elephant bond, tested."]];
var L1_TITLES=["Life on Earth", "The Living Planet", "The Trials of Life", "The Life of Mammals", "The Serengeti Lion", "The Year of the Gorilla", "Gorillas in the Mist", "In the Shadow of Man", "Through a Window", "The Snow Leopard", "Never Cry Wolf", "A Whale for the Killing", "The Peregrine", "H is for Hawk", "The Song of the Dodo", "Ring of Bright Water", "Born Free", "The Last Panda", "The Tiger", "The Birds of America", "A Field Guide to the Birds", "The Sibley Guide to Birds", "The Behavior Guide to African Mammals", "Whales, Dolphins and Porpoises", "IUCN Red List of Threatened Species", "Convention on International Trade in Endangered Species (CITES)", "Endangered Species Act", "The Deer and the Tiger", "Grizzly Years: In Search of the American Wilderness", "The Wolf: The Ecology and Behavior of an Endangered Species", "Cry of the Kalahari", "The Elephant Whisperer"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["orders of mammals", "adaptations", "social behavior", "predators and prey", "migration", "mammals and humans"], ["flight and feathers", "song and communication", "migration routes", "breeding biology", "raptors", "waterbirds"], ["ocean zones", "marine mammals", "coral reefs", "fisheries", "the deep sea", "marine conservation"], ["amphibian life cycles", "reptile diversity", "venom", "thermoregulation", "nesting", "declines and disease"], ["metamorphosis", "pollination", "social insects", "pest management", "biodiversity", "insect declines"], ["forests", "grasslands", "wetlands", "deserts", "mountains", "fragmentation"], ["the conservation ethic", "protected areas", "restoration", "captive programs", "funding", "success stories"], ["the Red List", "recovery plans", "critical habitat", "captive breeding", "reintroduction", "extinction"]];
var FRAMES=["made readers fall in love with a species", "proved field science could read like literature", "changed how the public saw predators", "became the handbook a generation carried outdoors", "forced a reckoning with extinction", "still defines the genre"];
var T2_TOPICS=["corridor connectivity", "anti-poaching technology", "marine protected areas", "urban carnivores", "pollinator recovery", "amphibian disease", "trophy-hunting economics", "rewilding predators", "migratory flyways", "wildlife disease surveillance", "habitat banking", "community conservancies"];
var T2_ANGLES=["population viability analysis", "threat mapping", "intervention trials", "policy evaluation", "traditional knowledge integration", "corridor design"];
var T2_METHODS=["camera-trap grids", "GPS telemetry", "environmental DNA", "mark-recapture studies", "acoustic monitoring", "aerial surveys"];
var T2_OUTCOMES=["a delisting-ready recovery plan", "a funded corridor network", "a poaching early-warning system", "quantified population targets", "a community stewardship model", "a disease response protocol"];
var PROJ_BY="JAH Wildlife Projection Unit";
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
