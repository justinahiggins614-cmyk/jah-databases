/* ✳ SIGNATURE — JAH Maritime Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic client-side generator: same seed + same version => same record.
   Anchor facts (vessel types, tonnage classes, navigation, regulations) verified
   from published maritime sources; application studies are Signature-generated. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['merchant-vessels','tankers','navigation','ship-design','naval-vessels','ports-harbors','maritime-law','safety','cargo-operations','maritime-history'];
var PREFIX='JAH-MAR-';
/* [subject, category, type, key fact, measures object, [related terms x3], year (0 = none)] */
var ANCH=[
['Container ship','merchant-vessels','vessel','boxships carry standardized containers measured in TEU; the largest carry well over 20,000 TEU',{capacity:'20,000+ TEU',standard:'ISO container'},['TEU','intermodal','terminal'],0],
['Bulk carrier','merchant-vessels','vessel','carry unpackaged dry cargo in classes: Capesize above 80,000 DWT, Panamax 60,000-80,000 DWT, Handymax 40,000-60,000 DWT',{capesize_dwt:'80,000+',panamax_dwt:'60,000-80,000',handymax_dwt:'40,000-60,000'},['coal','grain','ore'],0],
['Roll-on/roll-off ship','merchant-vessels','vessel','vehicles are driven aboard via stern and side ramps; pure car carriers move thousands of automobiles',{cargo:'vehicles',loading:'ramps'},['car carrier','PCTC','ramps'],0],
['Cruise ship','merchant-vessels','vessel','floating resorts carrying thousands of passengers on leisure voyages',{passengers:'thousands'},['passengers','leisure','hospitality'],0],
['VLCC','tankers','vessel','Very Large Crude Carriers: 200,000-320,000 DWT supertankers moving crude oil worldwide',{dwt:'200,000-320,000',typical_length_m:330},['crude oil','supertanker','Suezmax'],0],
['ULCC','tankers','vessel','Ultra Large Crude Carriers exceed 320,000 DWT; the largest tankers ever built',{dwt:'320,000+',class:'largest tankers'},['supertanker','crude oil','size record'],0],
['LNG carrier','tankers','vessel','carry liquefied natural gas at about -162 C in insulated membrane or Moss tanks; Q-max class holds 266,000 cubic meters',{cargo_temp_c:-162,qmax_capacity_m3:266000},['liquefied gas','cryogenic','Q-max'],0],
['Aframax tanker','tankers','vessel','oil tankers of 80,000-120,000 DWT, sized under the Average Freight Rate Assessment scheme',{dwt:'80,000-120,000'},['AFRA','crude oil','products'],0],
['Suezmax tanker','tankers','vessel','the largest tankers able to transit the Suez Canal: 120,000-200,000 DWT',{dwt:'120,000-200,000'},['Suez Canal','crude oil','size limit'],0],
['The knot','navigation','unit','one knot is one nautical mile per hour; a nautical mile is 1,852 meters',{nautical_mile_m:1852,definition:'1 nm per hour'},['speed','nautical mile','ship log'],0],
['AIS','navigation','system','the Automatic Identification System: ships broadcast identity, position, course, and speed to avoid collisions',{function:'collision-avoidance broadcast'},['transponder','VTS','COLREGs'],0],
['ECDIS','navigation','system','the Electronic Chart Display and Information System: digital nautical charts with real-time positioning',{function:'digital charts'},['charts','GPS','navigation'],0],
['Celestial navigation','navigation','technique','fixing position from the sun, moon, and stars using a sextant and a nautical almanac',{instrument:'sextant'},['sextant','stars','almanac'],0],
['Marine radar','navigation','system','radio detection and ranging: finds other vessels, coastlines, and weather in darkness and fog',{function:'detection in low visibility'},['ARPA','collision avoidance','fog'],0],
['Gyrocompass','navigation','instrument','a fast-spinning gyroscope that finds true north regardless of magnetism',{finds:'true north'},['heading','true north','steering'],0],
['Deadweight tonnage','ship-design','measure','the total weight of cargo, fuel, and stores a ship can carry at its maximum permitted draught',{unit:'metric tons',measures:'carrying capacity'},['DWT','draught','capacity'],0],
['Gross tonnage','ship-design','measure','a measure of a ship\u2019s overall internal volume \u2014 not its weight',{measures:'internal volume'},['GT','volume','registration'],0],
['Port and starboard','ship-design','terminology','port is the left side and starboard the right side when facing toward the bow',{port:'left side',starboard:'right side'},['bow','helm','directions'],0],
['Draft, beam, and freeboard','ship-design','terminology','draft is the depth below the waterline, beam is the vessel\u2019s width, and freeboard is the height above water',{draft:'below waterline',beam:'width',freeboard:'above water'},['dimensions','stability','load line'],0],
['Ship anchors','ship-design','equipment','stockless, Danforth, and plow anchors dig into the seabed to hold a vessel in place',{types:'stockless, Danforth, plow'},['seabed','anchor chain','mooring'],0],
['Ballast water','ship-design','system','water taken aboard for stability; regulated internationally because it spreads invasive species',{purpose:'stability',risk:'invasive species'},['stability','regulation','discharge'],0],
['Submarine','naval-vessels','vessel','submersibles operating beneath the surface using ballast tanks, periscopes, and sonar',{propulsion:'nuclear or diesel-electric'},['sonar','periscope','stealth'],0],
['Aircraft carrier','naval-vessels','vessel','floating airbases that launch and recover aircraft with catapults and arresting gear',{role:'power projection'},['flight deck','catapult','naval aviation'],0],
['Destroyer','naval-vessels','vessel','fast warships escorting fleets with guns, missiles, and anti-submarine weapons',{role:'escort and defense'},['frigate','missiles','escort'],0],
['Container terminal','ports-harbors','facility','ports equipped with gantry cranes transferring containers between ships, trucks, and trains',{equipment:'gantry cranes'},['cranes','intermodal','berth'],0],
['Panama Canal','ports-harbors','waterway','links the Atlantic and Pacific oceans; Panamax vessels fit its original locks at 32.2 m beam',{opened:1914,panamax_beam_m:32.2},['locks','Panamax','transit'],1914],
['Suez Canal','ports-harbors','waterway','links the Mediterranean and Red Seas, shortcutting voyages between Europe and Asia',{opened:1869},['shortcut','Suezmax','Ever Given'],1869],
['COLREGs','maritime-law','regulation','the International Regulations for Preventing Collisions at Sea: the rules of the road for vessels',{scope:'international waters'},['right of way','lights','sound signals'],0],
['SOLAS','safety','regulation','the Safety of Life at Sea convention setting global standards for ship construction and safety',{scope:'global safety standards'},['lifeboats','drills','IMO'],0],
['MARPOL','maritime-law','regulation','the convention preventing pollution from ships: oil, chemicals, garbage, and air emissions',{scope:'pollution prevention'},['pollution','discharge','IMO'],0],
['International Maritime Organization','maritime-law','organization','the United Nations agency regulating shipping safety, security, and pollution',{type:'UN specialized agency'},['regulation','SOLAS','MARPOL'],0],
['Flags of convenience','maritime-law','practice','ships registered in states with light regulation, a long-debated industry practice',{practice:'open registries'},['registry','regulation','crewing'],0],
['Lifeboats and muster drills','safety','procedure','passenger ships must carry survival craft for all aboard and drill passengers in emergencies',{requirement:'SOLAS drills'},['survival craft','EPIRB','muster stations'],0],
['Piracy countermeasures','safety','practice','best management practices, citadels, and naval patrols defend merchant ships against piracy',{defense:'BMP, citadel, patrols'},['best management practices','citadel','Gulf of Aden'],0],
['Container standardization','cargo-operations','innovation','Malcolm McLean\u2019s 1956 container-shipping revolution standardized global freight around the box',{year:1956,unit:'TEU'},['intermodal','McLean','standardization'],1956],
['Breakbulk cargo','cargo-operations','cargo','non-containerized general cargo loaded piece by piece: crates, drums, and machinery',{handling:'piece by piece'},['general cargo','crates','stevedore'],0],
['Heavy-lift vessels','cargo-operations','vessel','ships with massive cranes for oversized cargo such as rigs and wind turbines',{cargo:'oversized project cargo'},['cranes','project cargo','semi-submersible'],0],
['Reefer transport','cargo-operations','vessel','refrigerated ships and containers carrying perishables at controlled temperatures',{cargo:'perishables'},['refrigeration','cold chain','produce'],0],
['Seawise Giant','maritime-history','vessel','completed in 1980 and later lengthened to 550,000 DWT, the largest ship ever built',{dwt:550000,completed:1980},['size record','ULCC','Knock Nevis'],1980],
['Titanic','maritime-history','vessel','the 1912 maiden-voyage sinking after striking an iceberg; a landmark maritime disaster',{year:1912,cause:'iceberg collision'},['iceberg','SOLAS legacy','White Star Line'],1912],
['Ever Given','maritime-history','event','in March 2021 the container ship blocked the Suez Canal for six days, disrupting world trade',{year:2021,days_blocked:6},['Suez Canal','blockage','salvage'],2021]
];
var ASPECTS=['overview','technical deep-dive','operational use','historical timeline','safety relevance','comparative analysis'];
var CONTEXTS=['operations study','fleet review','training module','safety case','historical survey','port planning study'];
var TYPELBL={'vessel':'vessel type','unit':'unit of measure','system':'maritime system','technique':'navigation technique','instrument':'navigation instrument','measure':'tonnage measure','terminology':'maritime terminology','equipment':'ship equipment','facility':'port facility','waterway':'waterway','regulation':'maritime regulation','organization':'maritime organization','practice':'maritime practice','procedure':'safety procedure','innovation':'cargo innovation','cargo':'cargo type','event':'maritime event'};
function measureText(o){return Object.keys(o).map(function(k){return k.replace(/_/g,' ')+': '+o[k];}).join('; ')+'.';}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ANCH.filter(function(a){return a[1]===cat;});
  if(!pool.length)pool=ANCH;
  var a=pick(pool,rnd);
  var mode=rnd()<0.45?'profile':'study';
  var aspect=pick(ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var serial='R-'+(10000+seed);
  var title,desc,src,code=null,rel=a[5].slice();
  if(mode==='profile'){
    code=serial;
    title=a[0]+': '+aspect+' ('+serial+')';
    var s1=a[0]+' is a '+(TYPELBL[a[2]]||a[2])+(a[6]>0?', first recorded in '+a[6]:'')+'. '+a[3]+'.';
    var s2='Key measures: '+measureText(a[4]);
    var s3='Related terms: '+a[5][0]+', '+a[5][1]+', '+a[5][2]+'.';
    if(aspect==='technical deep-dive')desc=s1+' '+s2+' These measures define what '+a[0]+' is and how it is used. '+s3;
    else if(aspect==='operational use')desc=s1+' '+s3+' At sea and in port, '+a[0]+' is handled according to these characteristics. '+s2;
    else if(aspect==='historical timeline')desc=(a[6]>0?'In '+a[6]+', ':'In maritime history, ')+a[0]+' entered the record. '+s1+' '+s2;
    else if(aspect==='safety relevance')desc=s1+' '+s2+' Safe operation around '+a[0]+' follows directly from these facts. '+s3;
    else if(aspect==='comparative analysis')desc=s1+' Compared with its counterparts, '+a[0]+' is distinguished as follows: '+a[3]+' '+s2;
    else desc=s1+' '+s2+' '+s3;
    src='online';
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=pick(CONTEXTS,rnd);
    var n=ri(rnd,20,2000),yr=ri(rnd,2016,2026);
    title=a[0]+' \u2014 '+ctx+' '+code;
    desc='This generated study ('+code+', compiled '+yr+') examines '+n.toLocaleString('en-US')+' documented records concerning '+a[0]+' in a '+ctx+' setting. '+
      'The established facts remain: '+a[3]+' '+
      'The study focuses on '+a[5][0]+' and '+a[5][1]+', reporting patterns consistent with published maritime references. '+
      'As a Signature-generated study record, the scenario is illustrative; the core facts about '+a[0]+' come from published maritime sources.';
    src='signature';rel=[a[5][0],a[5][1],ctx+' (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{subject:a[0],subject_type:a[2],category:a[1],key_fact:a[3],measures:a[4],related_terms:rel,year:a[6]||null,aspect:aspect,study_code:code},
    src:src,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MAR-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>160)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  else{var parts=r.description.split('. ');if(parts.length<2)e.push('description-sentences');if(!/\.$/.test(r.description.trim()))e.push('description-period');}
  if(CATS.indexOf(r.category)<0)e.push('category');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(!s.subject||typeof s.subject!=='string')e.push('spec.subject');
    if(!s.subject_type||typeof s.subject_type!=='string')e.push('spec.subject_type');
    if(!s.key_fact||typeof s.key_fact!=='string')e.push('spec.key_fact');
    if(!s.measures||typeof s.measures!=='object'||!Object.keys(s.measures).length)e.push('spec.measures');
    if(!Array.isArray(s.related_terms)||s.related_terms.length<2||s.related_terms.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.related_terms');
    if(!(s.year===null||(Number.isInteger(s.year)&&s.year>=1500&&s.year<=2026)))e.push('spec.year');
  }
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-maritime-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('maritime',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
