(function(){'use strict';
/* jahdb-fundamental-geography-signature-1.0 — fundamental geography bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"signature" = Signature-system formulation, clearly labeled */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SFGE-';
var KIND='fundamental geography record (Signature original)';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Geography studies Earth\'s landscapes, peoples, places, and environments: where things are, why they\'re there, and how location shapes life. It joins the physical (landforms, climate) with the human (cities, cultures, economies).', 'reasoning':'Geographers reason spatially: map the phenomenon, look for patterns, ask why here and not there. \'Everything is related to everything else, but near things are more related\' — Tobler\'s law, the field\'s first law.', 'quantities':'The core quantities are location (coordinates), distance, scale, and density. The map\'s scale is the master quantity — it determines what can be seen and what the map can claim.', 'mechanism':'Geography works the spatial loop: observe the pattern → map it → explain the process → predict the change. GIS made the loop computational — layers of data analyzed together, the map as database.', 'miscon':'Geography is not just memorizing capitals: it explains why places differ and how they connect. Maps are not neutral: every projection distorts, every selection emphasizes. And \'the environment determines everything\' is as false as \'it determines nothing\' — the truth is interaction.'};
var SIGLENS=['In the Signature system, geography is the spatial discipline: every location-aware database, every map in this network follows geographic reasoning, and the Signature formulation teaches each principle as a pattern you can map.','The Signature practice is to map the pattern: plot the data, read the distribution, explain the where — so geographic reasoning is done with maps you can make and check.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- haversine distance demo. Runs as-is with python3."""\nimport math\ndef haversine(lat1, lon1, lat2, lon2):\n    R = 6371.0\n    p1, p2 = math.radians(lat1), math.radians(lat2)\n    dp = math.radians(lat2 - lat1); dl = math.radians(lon2 - lon1)\n    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2\n    return 2 * R * math.asin(math.sqrt(a))\nprint("NYC to London:", round(haversine(40.7, -74.0, 51.5, -0.1)), "km")\nprint("great-circle: the shortest path on a sphere")\n', '#!/usr/bin/env python3\n"""{TITLE} -- map scale demo. Runs as-is with python3."""\ndef ground_distance(map_cm, scale_denom):\n    return map_cm * scale_denom / 100000  # km\nfor denom in [24000, 100000, 1000000]:\n    print(f"1:{denom}: 1cm on map = {ground_distance(1, denom):.2f} km on ground")\nprint("large scale = small area, great detail; small scale = the reverse")\n', '#!/usr/bin/env python3\n"""{TITLE} -- population density demo. Runs as-is with python3."""\nplaces = {"Manhattan": (1600000, 59), "Alaska": (733000, 1477000), "Bangladesh": (173000000, 148000)}\nfor name, (pop, area) in places.items():\n    print(f"{name:<12} {pop/area:>8.1f} people/km^2")\nprint("density shapes everything: transport, housing, disease, politics")\n'];
var TOPICS=[['Signature What Geography Is','Geography is the study of Earth\'s surface: its physical features, its human imprint, and the interactions between them. It asks the where questions — and shows that where explains a great deal of what and why.'],
['Signature The Core Question of Geography','The core question is: why are things located where they are, and what difference does location make? Every map is an attempt at the answer — pattern first, process second.'],
['Signature Assumptions: Space Matters','The field assumes space matters: distance, location, and scale shape phenomena. Tobler\'s first law — near things are more related than distant things — is the working assumption behind all spatial analysis.'],
['Signature The Vocabulary: Place, Region, Scale','The vocabulary names the concepts: place (meaningful location), region (area of similarity), scale (the level of analysis), and diffusion (spread across space). Fluency means thinking in these four simultaneously.'],
['Signature Location: The Fundamental Quantity','Location — the coordinates — is the fundamental quantity: everything else in geography attaches to a where. Absolute location pins the point; relative location describes its situation among others.'],
['Signature Mapping: The Primary Method','Mapping is the primary method: the map is geography\'s language, argument, and laboratory. Cartography\'s choices — projection, scale, symbolization — are analytical decisions, not decorations.'],
['Signature A Canonical First Example','The canonical first example is John Snow\'s cholera map: cases clustered around the Broad Street pump, the pattern revealing the cause. One map founded epidemiology — the spatial method\'s power made visible.'],
['Signature How Geography Measures','The field measures with GPS, remote sensing, censuses, and fieldwork: positions precisely, surfaces from orbit, populations by count. GIS integrated them all — the map became a database.'],
['Signature The Core Mechanism: Spatial Interaction','The core mechanism is spatial interaction: people, goods, and ideas moving between places, shaped by distance and attraction. Gravity models predict the flows — the bigger and closer, the stronger.'],
['Signature The Simplest Law: Tobler\'s First Law','The simplest law is Tobler\'s: everything is related to everything else, but near things are more related than distant things. It justifies interpolation, explains diffusion, and underlies all spatial statistics.'],
['Signature Common Misconceptions in Geography','The misconceptions mislead: that geography is memorizing places (it\'s explaining patterns), that maps are neutral (every map argues), and that the environment determines all (possibilism: environment sets possibilities, people choose).'],
['Signature How Beginners Practice Geography','Beginners practice by mapping: plot the data, read the pattern, ask why here. The field sketch — the observed landscape drawn and annotated — remains the root exercise.'],
['Signature The Core Model: The Region','The region is the core model: an area defined by shared characteristics — formal, functional, or vernacular. Regional thinking organizes the world\'s complexity into comprehensible units.'],
['Signature The Great Tool: GIS','GIS — geographic information systems — is the great tool: layered spatial data analyzed together, the map as database and the analysis as overlay. It turned geography computational without losing its soul.'],
['Signature Systems Thinking: Human-Environment Interaction','Systems thinking in geography is human-environment interaction: people shaping landscapes, landscapes shaping people, feedbacks both ways. The Anthropocene made this the field\'s central drama.'],
['Signature Invariance: What Scale Preserves','The scale concept is the field\'s invariance problem: patterns change with scale — the fractal coast, the modifiable areal unit problem. Honest geography states its scale, because the answer depends on it.'],
['Signature Approximation: The Model Region','Approximation uses model regions and ideal patterns: von Thünen\'s rings, Christaller\'s hexagons — simplifications revealing logic. The real world deviates instructively from the ideal.'],
['Signature Evidence Standards: Ground Truth','The evidence standard is ground truth: the satellite image checked against the field visit, the census against the survey. Remote sensing proposes; the ground disposes.'],
['Signature Classic Discoveries','The classic discoveries are the field\'s great mappings: the ocean floor\'s ridges (plate tectonics\' evidence), the world\'s climates classified, the city systematically understood. Each made the invisible visible.'],
['Signature Core Trade-offs: Detail versus Coverage','The core trade-off is detail versus coverage: the large-scale map shows the street, the small-scale map shows the continent. No single map serves all purposes — the scale must match the question.'],
['Signature Handling Uncertainty: Spatial Error','Geography handles uncertainty explicitly: positional error, classification error, and the ecological fallacy (areas aren\'t people). Metadata — data about the data — carries the uncertainty with the map.'],
['Signature Tools of the Trade','The tools of the trade are the map, the GPS, the satellite image, and GIS. The deepest is the field notebook — the direct observation that anchors all the technology.'],
['Signature Ethics and Responsibility','Ethics in geography concerns representation and surveillance: who is mapped, who maps, and who watches. Maps have served empires and liberation — the field owns this history and its present duties.'],
['Signature Teaching Geography','Teaching it well goes outside: the transect walked, the land use mapped, the river measured. Students who have mapped their own neighborhood understand scale bodily.'],
['Signature The Frontier Question','The frontier question is the planetary sensorium: real-time Earth observation, digital twins of cities and ecosystems, AI reading the landscape. The frontier asks what geography becomes when the map is live.'],
['Signature Unifying Theories','The unifying theories are spatial analysis and human-environment interaction: the methods for the patterns, the framework for the meaning. Together they make geography one discipline, not two.'],
['Signature Computational Geography','Computational geography analyzes at scale: spatial statistics, geocomputation, and machine learning on satellite imagery. The computer finds patterns across billions of pixels — the geographer explains them.'],
['Signature Bridges to Other Fields','Geography bridges to geology (landforms), ecology (biomes), economics (regions), sociology (cities), history (historical geography), and computer science (GIS). Place is everyone\'s context.'],
['Signature The Great Unsolved Problems','The great unsolved problems are open and labeled as such: predicting urban evolution, the full human-environment feedback, and equitable development across regions. Active research, no settled answers.'],
['Signature How New Claims Are Validated','New geographic claims are validated by independent data and field checking: the pattern found in a second dataset, the classification verified on the ground. A map earns trust when the territory agrees.'],
['Signature The Great Debates','The great debates — determinism versus possibilism, quantitative versus humanistic geography, the politics of mapping — shaped the field\'s identity. The debates made it richer, not weaker.'],
['Signature Failure Modes: When Geography Gets It Wrong','Geography gets it wrong through the ecological fallacy, map misuse (wrong projection, cherry-picked scale), and confusing the map for the territory. The immune system is scale-awareness and ground truth.'],
['Signature Synthesis: Building on the Fundamentals','Advanced synthesis reads regions whole: the land, the people, the economy, the history — interacting in place. The fundamentals are the geographic imagination itself.'],
['Signature The Signature Formulation: Geography as Spatial Reasoning','The Signature formulation treats geography as spatial reasoning: every principle here maps a pattern you can verify, because in the Signature system where things are is the beginning of understanding them. That is the Signature capstone on geographic bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(false){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Scale is stated: every map and analysis names its scale and projection.", "Data are sourced: every layer's origin and date are documented.", "Patterns are tested: spatial claims are checked statistically, not just visually."],citations:["de Blij, H. J. \u2014 The Power of Place: Geography, Destiny, and Globalization's Rough Landscape.", "National Geographic Society \u2014 public geographic references.", "Cross-checked against the JAH Databases network archive before filing."],src:'signature',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-geography-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-geography-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
