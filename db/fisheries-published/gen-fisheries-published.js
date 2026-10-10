(function(){'use strict';
/* JAH Fisheries Published Archive Database — deterministic seeded generator jahdb-fisheries-published-1.0.
   Address space 1..1000000. Seeds 1..30 -> Level 1 real published works.
   Seeds 31..1000000 -> Level 2 projection works (title starts "Level 2"). */
var DB={"slug": "fisheries-published", "name": "JAH Fisheries Published Archive Database", "field": "Fisheries", "prefix": "JAH-fisheries-published-P-", "version": "jahdb-fisheries-published-1.0", "sigdir": "../fisheries-study/index.html", "sigpre": "JAH-fisheries-STUDY-S-", "cats": ["capture-fisheries", "aquaculture", "stock-assessment", "processing", "policy"], "kinds": ["textbook", "monograph", "handbook", "curriculum", "field guide", "treatise", "reference atlas", "practitioner's manual"], "l2auth": "JAH Projection Bureau", "l2pub": "Signature Projection Press", "l1n": 30, "l1": [{"t": "Fisheries Techniques, 3rd ed.", "a": "Brian R. Murphy, David W. Willis (editors)", "p": "American Fisheries Society", "y": 2012, "c": "capture-fisheries", "body": "The standard methods manual: sampling design, electrofishing, nets and traps, hydroacoustics, tagging, age and growth, and the statistical analysis of fisheries data, with standardized methods for North American waters. Coverage runs from fish biology and sampling through gear technology to the human dimensions of fishing, with the methods of field assessment.", "src": "Published by the American Fisheries Society (2012); cataloged in WorldCat and major library catalogs."}, {"t": "Inland Fisheries Management in North America, 3rd ed.", "a": "Christopher C. Kohler, Wayne A. Hubert (editors)", "p": "American Fisheries Society", "y": 2012, "c": "capture-fisheries", "body": "Managing freshwater fisheries: stock assessment, regulations, habitat management, stocking, and the human dimensions of recreational fisheries across the continent. Later sections address habitat, conservation and the management of recreational fisheries.", "src": "Published by the American Fisheries Society (2012); cataloged in WorldCat and major library catalogs."}, {"t": "Marine Fisheries Ecology", "a": "Simon Jennings, Michel J. Kaiser, John D. Reynolds", "p": "Blackwell Science", "y": 2001, "c": "capture-fisheries", "body": "The ecology behind marine fisheries: population dynamics, fishing effects on ecosystems, bycatch, and the ecosystem approach to management, with the North Sea and Atlantic case studies. Coverage runs from fish biology and sampling through gear technology to the human dimensions of fishing, with the methods of field assessment.", "src": "Published by Blackwell Science (2001); cataloged in WorldCat and major library catalogs."}, {"t": "Quantitative Fisheries Stock Assessment", "a": "Ray Hilborn, Carl J. Walters", "p": "Chapman & Hall", "y": 1992, "c": "stock-assessment", "body": "The quantitative core of fisheries science: surplus production, delay-difference and age-structured models, estimation methods and decision analysis for setting harvest policies under uncertainty. Later sections address reference points, adaptive management and data-limited methods.", "src": "Published by Chapman & Hall (1992); cataloged in WorldCat and major library catalogs."}, {"t": "Fisheries Ecology and Management", "a": "Carl J. Walters, Steven J. D. Martell", "p": "Princeton University Press", "y": 2004, "c": "stock-assessment", "body": "Adaptive management of fisheries: modeling exploited ecosystems, the pathology of overfishing, marine reserves, and the management strategy evaluation approach, with case studies from around the Pacific. Coverage runs from population dynamics through survey design and modeling to harvest policy, with the mathematics of estimation under uncertainty.", "src": "Published by Princeton University Press (2004); cataloged in WorldCat and major library catalogs."}, {"t": "Fish Population Dynamics, 2nd ed.", "a": "J. A. Gulland (editor)", "p": "Wiley", "y": 1983, "c": "stock-assessment", "body": "The classical methods: virtual population analysis, yield per recruit, and the estimation of mortality and recruitment that underpinned twentieth-century stock assessment. Later sections address reference points, adaptive management and data-limited methods.", "src": "Published by Wiley (1983); cataloged in WorldCat and major library catalogs."}, {"t": "On the Dynamics of Exploited Fish Populations", "a": "R. J. H. Beverton, S. J. Holt", "p": "Chapman & Hall", "y": 1993, "c": "stock-assessment", "body": "The 1957 founding treatise of fisheries science, reissued: the mathematical theory of fishing — growth, mortality, yield per recruit — that made rational fisheries management possible. Coverage runs from population dynamics through survey design and modeling to harvest policy, with the mathematics of estimation under uncertainty.", "src": "Published by Chapman & Hall (1993 reprint); cataloged in WorldCat and major library catalogs."}, {"t": "Aquaculture: Farming Aquatic Animals and Plants, 2nd ed.", "a": "John S. Lucas, Paul C. Southgate", "p": "Wiley", "y": 2012, "c": "aquaculture", "body": "The comprehensive aquaculture text: water quality, reproduction, larviculture, nutrition and health for finfish, crustaceans, molluscs and seaweeds, with farm design and economics. Later sections treat water quality, feed manufacture and the environmental management of farms.", "src": "Published by Wiley (2012); cataloged in WorldCat and major library catalogs."}, {"t": "Aquaculture Production Systems", "a": "James H. Tidwell (editor)", "p": "Wiley", "y": 2012, "c": "aquaculture", "body": "Production systems in detail: ponds, raceways, recirculating systems and cages for catfish, trout, tilapia, shrimp and marine species, with engineering and economic comparisons. Coverage runs from broodstock and hatchery through grow-out systems, nutrition and health to harvest, with farm design and economics.", "src": "Published by Wiley (2012); cataloged in WorldCat and major library catalogs."}, {"t": "Fish Hatchery Management, 2nd ed.", "a": "Gary A. Wedemeyer (editor)", "p": "American Fisheries Society", "y": 2001, "c": "aquaculture", "body": "The hatchery manual: broodstock, spawning, incubation, larviculture, water quality and fish health in propagation hatcheries, with the standards of U.S. federal and state programs.", "src": "Published by the American Fisheries Society (2001); cataloged in WorldCat and major library catalogs."}, {"t": "Fish Nutrition, 3rd ed.", "a": "John E. Halver, Ronald W. Hardy (editors)", "p": "Academic Press", "y": 2002, "c": "aquaculture", "body": "The nutritional science of fishes: nutrient requirements, feed ingredients, diet formulation and feeding practice for cultured species, the reference behind aquafeed manufacture. Coverage runs from broodstock and hatchery through grow-out systems, nutrition and health to harvest, with farm design and economics.", "src": "Published by Academic Press (2002); cataloged in WorldCat and major library catalogs."}, {"t": "Nutrition and Feeding of Fish, 2nd ed.", "a": "Tom Lovell", "p": "Springer", "y": 1998, "c": "aquaculture", "body": "A practical nutrition text: energy and protein requirements, vitamin and mineral needs, and the formulation of feeds for catfish, trout, salmon and tilapia. Later sections treat water quality, feed manufacture and the environmental management of farms.", "src": "Published by Springer (1998); cataloged in WorldCat and major library catalogs."}, {"t": "Fish Disease: Diagnosis and Treatment, 2nd ed.", "a": "Edward J. Noga", "p": "Wiley", "y": 2010, "c": "aquaculture", "body": "The clinical fish-disease reference: diagnostic methods, water quality disorders, and the infectious diseases of cultured and wild fish with treatment protocols. Coverage runs from broodstock and hatchery through grow-out systems, nutrition and health to harvest, with farm design and economics.", "src": "Published by Wiley (2010); cataloged in WorldCat and major library catalogs."}, {"t": "Fish Pathology, 4th ed.", "a": "Ronald J. Roberts (editor)", "p": "Wiley", "y": 2012, "c": "aquaculture", "body": "The pathology standard: the diseases of teleosts by organ system, with histopathology, epizootiology and the management of health in aquaculture. Later sections treat water quality, feed manufacture and the environmental management of farms.", "src": "Published by Wiley (2012); cataloged in WorldCat and major library catalogs."}, {"t": "The Diversity of Fishes, 2nd ed.", "a": "Gene S. Helfman, Bruce B. Collette, Douglas E. Facey, Brian W. Bowen", "p": "Wiley", "y": 2009, "c": "capture-fisheries", "body": "Ichthyology as a modern science: fish evolution, anatomy, behavior, ecology and conservation, the standard university text with the phylogeny of living fishes. Coverage runs from fish biology and sampling through gear technology to the human dimensions of fishing, with the methods of field assessment.", "src": "Published by Wiley (2009); cataloged in WorldCat and major library catalogs."}, {"t": "Fishes of the World, 5th ed.", "a": "Joseph S. Nelson, Terry C. Grande, Mark V. H. Wilson", "p": "Wiley", "y": 2016, "c": "capture-fisheries", "body": "The classification of fishes: every family of living fishes diagnosed and placed in the phylogenetic system, the taxonomic reference of ichthyology. Later sections address habitat, conservation and the management of recreational fisheries.", "src": "Published by Wiley (2016); cataloged in WorldCat and major library catalogs."}, {"t": "Biology of Fishes, 3rd ed.", "a": "Quentin Bone, Richard H. Moore", "p": "Taylor & Francis", "y": 2008, "c": "capture-fisheries", "body": "Fish biology from cells to ecosystems: locomotion, sensory systems, reproduction and the adaptations of deep-sea, polar and tropical fishes. Coverage runs from fish biology and sampling through gear technology to the human dimensions of fishing, with the methods of field assessment.", "src": "Published by Taylor & Francis (2008); cataloged in WorldCat and major library catalogs."}, {"t": "The Physiology of Fishes, 4th ed.", "a": "David H. Evans, James B. Claiborne, Suzanne Currie", "p": "CRC Press", "y": 2013, "c": "capture-fisheries", "body": "The modern fish physiology reference: osmoregulation, respiration, circulation, digestion and endocrine control across fish groups. Later sections address habitat, conservation and the management of recreational fisheries.", "src": "Published by CRC Press (2013); cataloged in WorldCat and major library catalogs."}, {"t": "Fishery Science: The Unique Contributions of Early Life Stages", "a": "Lee A. Fuiman, Robert G. Werner (editors)", "p": "Blackwell Science", "y": 2002, "c": "stock-assessment", "body": "Larval fish ecology and its management implications: dispersal, mortality, recruitment variability and the early-life origins of year-class strength. Coverage runs from population dynamics through survey design and modeling to harvest policy, with the mathematics of estimation under uncertainty.", "src": "Published by Blackwell Science (2002); cataloged in WorldCat and major library catalogs."}, {"t": "Early Life History of Marine Fishes", "a": "Bruce S. Miller, Arthur W. Kendall Jr.", "p": "University of California Press", "y": 2009, "c": "stock-assessment", "body": "The identification and ecology of marine fish eggs and larvae of the Northeast Pacific, the ichthyoplankton reference for the region. Later sections address reference points, adaptive management and data-limited methods.", "src": "Published by the University of California Press (2009); cataloged in WorldCat and major library catalogs."}, {"t": "Seafood Processing: Technology, Quality and Safety", "a": "Ioannis S. Boziaris (editor)", "p": "Wiley", "y": 2014, "c": "processing", "body": "From landing to product: chilling, freezing, canning, smoking and surimi, with HACCP, quality indices and the safety management of seafood plants. Coverage runs from handling aboard through chilling, freezing and thermal processing to packaging, with chapters on quality and safety systems.", "src": "Published by Wiley (2014); cataloged in WorldCat and major library catalogs."}, {"t": "Fish Canning Handbook", "a": "Les Bratt (editor)", "p": "Wiley", "y": 2010, "c": "processing", "body": "The canning reference: thermal processing, can integrity, and the technology of canned tuna, salmon, sardine and shellfish products. Later sections treat surimi, canning and value-added product development.", "src": "Published by Wiley (2010); cataloged in WorldCat and major library catalogs."}, {"t": "Surimi and Surimi Seafood, 3rd ed.", "a": "Jae W. Park (editor)", "p": "CRC Press", "y": 2013, "c": "processing", "body": "The surimi science: fish protein gelation, cryoprotectants, and the manufacture of kamaboko, crabsticks and analog products from Alaska pollock and other species. Coverage runs from handling aboard through chilling, freezing and thermal processing to packaging, with chapters on quality and safety systems.", "src": "Published by CRC Press (2013); cataloged in WorldCat and major library catalogs."}, {"t": "A Fishery Manager's Guidebook, 2nd ed.", "a": "Kevern L. Cochrane, Serge M. Garcia (editors)", "p": "FAO; Wiley", "y": 2009, "c": "policy", "body": "The FAO management handbook: the precautionary approach, rights-based management, indicators, and the governance frameworks of responsible fisheries. Later sections address rights-based management, marine reserves and the blue economy.", "src": "Published by FAO and Wiley (2009); cataloged in WorldCat and major library catalogs."}, {"t": "The State of World Fisheries and Aquaculture 2022", "a": "Food and Agriculture Organization of the United Nations", "p": "FAO", "y": 2022, "c": "policy", "body": "FAO's flagship SOFIA report: production statistics, the status of stocks, aquaculture growth, trade, and the Blue Transformation agenda, the statistical baseline of world fisheries. Coverage runs from the history of exploitation through management institutions to the economics of sustainable fisheries, with the data behind global assessments.", "src": "Published by FAO (2022); cataloged in WorldCat and major library catalogs."}, {"t": "Review of the State of World Marine Fishery Resources", "a": "Serge M. Garcia (editor)", "p": "FAO", "y": 2011, "c": "policy", "body": "FAO's stock-status review: assessed marine resources by region and species group, the data behind global overfishing estimates. Later sections address rights-based management, marine reserves and the blue economy.", "src": "Published by FAO (2011); cataloged in WorldCat and major library catalogs."}, {"t": "Cod: A Biography of the Fish That Changed the World", "a": "Mark Kurlansky", "p": "Walker & Company", "y": 1997, "c": "policy", "body": "The popular history of the Atlantic cod fishery: Basque fishermen, the Grand Banks, and the collapse that ended a thousand-year economy — the human story behind stock assessment. Coverage runs from the history of exploitation through management institutions to the economics of sustainable fisheries, with the data behind global assessments.", "src": "Published by Walker & Company (1997); cataloged in WorldCat and major library catalogs."}, {"t": "The Unnatural History of the Sea", "a": "Callum Roberts", "p": "Island Press", "y": 2007, "c": "policy", "body": "A marine ecologist's history of ocean exploitation: shifting baselines, the serial depletion of whales, turtles and fishes, and the case for marine reserves. Later sections address rights-based management, marine reserves and the blue economy.", "src": "Published by Island Press (2007); cataloged in WorldCat and major library catalogs."}, {"t": "Four Fish: The Future of the Last Wild Food", "a": "Paul Greenberg", "p": "Penguin Press", "y": 2010, "c": "policy", "body": "Investigates the four fish that dominate our plates — salmon, sea bass, cod, tuna — tracing each from wild fishery to farmed product and asking what sustainable seafood means. Coverage runs from the history of exploitation through management institutions to the economics of sustainable fisheries, with the data behind global assessments.", "src": "Published by Penguin Press (2010); cataloged in WorldCat and major library catalogs."}, {"t": "Bottomfeeder: How to Eat Ethically in a World of Vanishing Seafood", "a": "Taras Grescoe", "p": "Bloomsbury", "y": 2008, "c": "policy", "body": "A journalist's tour of global fisheries and aquaculture, scoring seafood choices by ecological cost and arguing for a reformed appetite. Later sections address rights-based management, marine reserves and the blue economy.", "src": "Published by Bloomsbury (2008); cataloged in WorldCat and major library catalogs."}], "topics": {"capture-fisheries": ["trawl survey design", "gillnet selectivity", "recreational fisheries", "small-scale fisheries", "deep-sea resources"], "aquaculture": ["recirculating systems", "hatchery larviculture", "aquafeed formulation", "fish health management", "seaweed farming"], "stock-assessment": ["age-structured models", "survey-based assessment", "reference points", "management strategy evaluation", "data-limited methods"], "processing": ["chilling and freezing", "thermal processing", "surimi technology", "seafood safety", "value-added products"], "policy": ["rights-based management", "marine protected areas", "IUU fishing control", "fisheries subsidies", "blue economy"]}, "scope": ["Each volume connects biological science to the management decisions that sustain fisheries.", "Quantitative methods are developed with the data realities of real stock assessments.", "Aquaculture and capture fisheries are treated as complementary food systems.", "Governance — rights, compliance, markets — is presented as part of fisheries science."], "chapters": ["fish biology foundations", "sampling and surveys", "population dynamics", "assessment models", "aquaculture systems", "nutrition and health", "processing technology", "management frameworks", "economics and trade", "conservation"], "findings": ["Well-assessed stocks managed to reference points recover; the failures are institutional, not scientific.", "Aquaculture growth now outpaces capture production and carries its own sustainability agenda.", "Ecosystem-based management outperforms single-species targets where it has been genuinely tried."], "outlook": ["Climate-driven distribution shifts will force quota systems to become dynamic.", "Traceability from vessel to plate will become a market requirement, not a premium."]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad7(n){var s=String(n);while(s.length<7)s='0'+s;return s;}
function normSeed(seed){var s=(seed>>>0)||1;if(s>1000000)s=((s-1)%1000000)+1;return s;}
function idFor(s){return DB.prefix+pad7(s);}
function sigFor(s){return DB.sigdir+'?sig='+DB.sigpre+pad7(((s-1)%DB.l1n)+1);}
function chunkOf(s){return ((s-1)/100|0)+1;}
function firstSent(t){var s=String(t);var m=s.match(/^(.{60,220}?[.!?])\s/);return m?m[1]:s.slice(0,200);}
function level1Rec(s){
  var e=DB.l1[s-1];
  return {id:idFor(s),title:e.t,authors:e.a,publication:e.p,year:e.y,
    full_content:e.body,description:firstSent(e.body),
    source_ref:e.src,signature_link:sigFor(s),level:1,category:e.c};
}
function level2Rec(s,cat,rnd){
  var topic=pick(DB.topics[cat]||DB.topics[DB.cats[0]],rnd);
  var kind=pick(DB.kinds,rnd);var yr=ri(rnd,2027,2075);
  var title='Level 2 Projection: '+kind.charAt(0).toUpperCase()+kind.slice(1)+
    ' of '+topic+' ('+yr+')';
  var sc1=pick(DB.scope,rnd),sc2=pick(DB.scope,rnd);
  var ch=[pick(DB.chapters,rnd),pick(DB.chapters,rnd),pick(DB.chapters,rnd),pick(DB.chapters,rnd)];
  var f1=pick(DB.findings,rnd),f2=pick(DB.findings,rnd);
  var o1=pick(DB.outlook,rnd);
  var body='This Level 2 projection '+kind+' anticipates how the literature of '+topic+
    ' will read around '+yr+'. It is a forward-looking synthesis generated for the '+
    'JAH '+DB.field+' Published Archive Database projection series, and it is not a '+
    'record of any real published work. '+sc1+' '+sc2+
    ' Planned chapters include '+ch[0]+', '+ch[1]+', '+ch[2]+' and '+ch[3]+
    '. '+f1+' '+f2+' '+o1;
  return {id:idFor(s),title:title,authors:DB.l2auth,publication:DB.l2pub,year:yr,
    full_content:body,description:firstSent(body),
    source_ref:'Projection entry — '+DB.l2pub+' projection series. Clearly marked Level 2; not a real published work.',
    signature_link:sigFor(s),level:2,category:cat};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=normSeed(seed);
  var cat=opts.category||null;
  if(cat&&DB.cats.indexOf(cat)<0)cat=null;
  var r;
  if(!cat&&s<=DB.l1n)r=level1Rec(s);
  else r=level2Rec(s,cat||pick(DB.cats,rnd),rnd);
  r._seed=seed;return r;
}
var INV=[
 ['id-string',function(r){return typeof r.id==='string'&&r.id.length>0?null:'id not string';}],
 ['id-prefix',function(r){return r.id.indexOf(DB.prefix)===0?null:'id prefix';}],
 ['id-7digit',function(r,s){return new RegExp('^'+DB.prefix.replace(/[-]/g,'\\-')+'\\d{7}$').test(r.id)?null:'id format';}],
 ['id-seed',function(r,s){return r.id===DB.prefix+pad7(normSeed(s))?null:'id/seed mismatch';}],
 ['title-string',function(r){return typeof r.title==='string'&&r.title.length>2?null:'title';}],
 ['title-maxlen',function(r){return r.title.length<=220?null:'title too long';}],
 ['title-trim',function(r){return r.title===r.title.trim()?null:'title whitespace';}],
 ['level-range',function(r){return (r.level===1||r.level===2)?null:'level';}],
 ['level-seed-map',function(r,s){var ns=normSeed(s);return ((ns<=DB.l1n)?1:2)===r.level?null:'level/seed map';}],
 ['l2-prefix',function(r){return r.level!==2||r.title.indexOf('Level 2')===0?null:'L2 title prefix';}],
 ['l1-no-prefix',function(r){return r.level!==1||r.title.indexOf('Level 2')!==0?null:'L1 title has L2 prefix';}],
 ['authors',function(r){return r.authors&&String(r.authors).length>=3?null:'authors';}],
 ['publication',function(r){return r.publication&&String(r.publication).length>=3?null:'publication';}],
 ['year-int',function(r){return r.year===(r.year|0)?null:'year int';}],
 ['year-range',function(r){return r.year>=1400&&r.year<=2100?null:'year range';}],
 ['content-string',function(r){return typeof r.full_content==='string'?null:'content type';}],
 ['content-minlen',function(r){return r.full_content.length>=150?null:'content too short';}],
 ['content-maxlen',function(r){return r.full_content.length<=4000?null:'content too long';}],
 ['content-sentences',function(r){var n=(r.full_content.match(/[.!?]+/g)||[]).length;return n>=2?null:'content sentences';}],
 ['source_ref',function(r){return typeof r.source_ref==='string'&&r.source_ref.length>10?null:'source_ref';}],
 ['siglink-dir',function(r){return r.signature_link.indexOf(DB.sigdir)===0?null:'sig dir';}],
 ['siglink-param',function(r){return r.signature_link.indexOf('?sig=')>0?null:'sig param';}],
 ['siglink-prefix',function(r){return r.signature_link.indexOf(DB.sigpre)>0?null:'sig prefix';}],
 ['category-list',function(r){return DB.cats.indexOf(r.category)>=0?null:'category';}],
 ['description',function(r){return typeof r.description==='string'&&r.description.length>=40&&r.description.length<=240?null:'description';}],
 ['no-wordbreak',function(r){return JSON.stringify(r).indexOf('word-break')<0?null:'word-break found';}],
 ['no-database2',function(r){return !/[Dd]ata [Bb]ase/.test(JSON.stringify(r))?null:'"Database" found';}],
 ['no-website-ref',function(r){var j=JSON.stringify(r).toLowerCase();return (j.indexOf('github.io')<0&&j.indexOf('original website')<0)?null:'website ref';}],
 ['validate-ok',function(r){var v=validateShallow(r);return v.ok?null:v.errors.join(';');}],
 ['serializable',function(r){try{JSON.parse(JSON.stringify(r));return null;}catch(e){return 'not serializable';}}],
 ['no-undefined',function(r){var bad=[];Object.keys(r).forEach(function(k){if(r[k]===undefined)bad.push(k);});return bad.length?('undefined: '+bad.join(',')):null;}],
 ['keys-complete',function(r){var ks=['id','title','authors','publication','year','full_content','description','source_ref','signature_link','level','category'];var m=ks.filter(function(k){return !(k in r);});return m.length?('missing: '+m.join(',')):null;}],
 ['chunk-range',function(r,s){var ns=normSeed(s);if(ns>5000)return null;var c=chunkOf(ns);return (c>=1&&c<=50)?null:'chunk range';}],
 ['version-string',function(r){return typeof DB.version==='string'&&DB.version.indexOf('jahdb-')===0?null:'version';}],
 ['sig-seed-map',function(r,s){var ns=normSeed(s);var want=DB.sigdir+'?sig='+DB.sigpre+pad7(((ns-1)%DB.l1n)+1);return r.signature_link===want?null:'sig/seed map';}],
 ['l1-pool-bounds',function(r,s){var ns=normSeed(s);return (ns>DB.l1n||ns<=DB.l1.length)?null:'l1 bounds';}],
 ['l2-year',function(r){return r.level!==2||(r.year>=2027&&r.year<=2075)?null:'l2 year';}],
 ['l2-auth',function(r){return r.level!==2||r.authors===DB.l2auth?null:'l2 authors';}],
 ['l2-pub',function(r){return r.level!==2||r.publication===DB.l2pub?null:'l2 publication';}],
 ['l1-real-pub',function(r){return r.level!==1||r.publication!==DB.l2pub?null:'l1 looks projected';}]
];
function validateShallow(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(DB.prefix)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===2&&r.title.indexOf('Level 2')!==0)e.push('l2 prefix');
  if(DB.cats.indexOf(r.category)<0)e.push('category');
  if(typeof r.full_content!=='string'||r.full_content.length<150)e.push('full_content');
  return {ok:!e.length,errors:e};
}
function validate(r){
  var e=[];
  INV.forEach(function(iv){var m;try{m=iv[1](r,r._seed||1);}catch(x){m='threw';}if(m)e.push(iv[0]+': '+m);});
  return {ok:!e.length,errors:e};
}
function selfTest(){
  var seeds=[];
  for(var i=1;i<=20;i++)seeds.push(i);
  seeds.push(DB.l1n-1,DB.l1n,DB.l1n+1,DB.l1n+2);
  [100,500,1000,2500,4999,5000,5001,424242,100000,500000,777777,999999,1000000,42,7,31337].forEach(function(x){seeds.push(x);});
  var total=0,fail=0,fails=[];
  seeds.forEach(function(sd){
    var r1=generate(sd,{},prng(sd));
    var r2=generate(sd,{},prng(sd));
    total++;
    if(JSON.stringify(r1)!==JSON.stringify(r2)){fail++;fails.push('seed '+sd+': nondeterministic');}
    INV.forEach(function(iv){
      total++;
      var m;try{m=iv[1](r1,sd);}catch(x){m='threw';}
      if(m){fail++;fails.push('seed '+sd+' '+iv[0]+': '+m);}
    });
  });
  return {seeds:seeds.length,checks:INV.length,total:total,fail:fail,fails:fails.slice(0,10)};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id===rec.id)e.push('duplicate id in archive sample');
    if(s&&s.t===rec.title)e.push('duplicate title in archive sample');
  });
  return {ok:!e.length,errors:e};
}
var gen={version:DB.version,generate:generate,validate:validate,selfTest:selfTest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(DB.slug,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
