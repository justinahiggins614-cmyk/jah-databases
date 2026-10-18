/* ✳ SIGNATURE — JAH Aviation Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic client-side generator: same seed + same version => same record.
   Anchor facts (aircraft, engines, avionics, procedures) verified from published
   aviation sources; application studies are Signature-generated and labeled. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['commercial-airliners','propulsion','avionics','flight-operations','military-aviation','general-aviation','helicopters','unmanned-systems','airports-infrastructure','aviation-history'];
var PREFIX='JAH-AVI-';
/* [subject, category, type, key specification text, specs object, [related x3], year (0 = none)] */
var ANCH=[
['Boeing 747','commercial-airliners','aircraft','the original jumbo jet: four turbofan engines, first flight 1969, nicknamed the Queen of the Skies',{first_flight:1969,engines:'4x turbofan',nickname:'Queen of the Skies'},['widebody','long-haul','freighter'],1969],
['Airbus A380','commercial-airliners','aircraft','the world\u2019s largest passenger airliner: full double deck, four turbofan engines, first flight 2005',{first_flight:2005,decks:2,engines:'4x turbofan'},['superjumbo','double-deck','widebody'],2005],
['Boeing 707','commercial-airliners','aircraft','the airliner that launched the commercial jet age; first flight 1957',{first_flight:1957,engines:'4x turbojet'},['jet age','narrowbody','pioneering'],1957],
['de Havilland Comet','commercial-airliners','aircraft','the world\u2019s first commercial jet airliner; first flight 1949',{first_flight:1949,engines:'4x turbojet'},['first jet airliner','pioneering','fatigue lessons'],1949],
['Concorde','commercial-airliners','aircraft','the supersonic airliner cruising at Mach 2; first flight 1969, retired 2003',{first_flight:1969,cruise:'Mach 2',retired:2003},['supersonic','delta wing','SST'],1969],
['Boeing 787 Dreamliner','commercial-airliners','aircraft','a composite-structure long-haul twinjet powered by GEnx or Trent 1000 turbofans',{engines:'2x turbofan',structure:'composite'},['fuel efficiency','long-haul','twinjet'],0],
['GE90-115B','propulsion','engine','the world\u2019s most powerful jet engine: 115,300 lbf maximum thrust with a 3.25 m fan; powers the Boeing 777-300ER and 777-200LR',{thrust_lbf:115300,record_lbf:127900,fan_diameter_m:3.25},['turbofan','Boeing 777','high-bypass'],0],
['Turbofan engine','propulsion','engine-type','a gas turbine with a large front fan bypassing air around the core; quieter and more fuel-efficient than turbojets, it powers modern airliners',{bypass:'high',use:'commercial aviation'},['bypass ratio','fan','core'],0],
['Turbojet engine','propulsion','engine-type','the simplest gas turbine: all air passes through the core; designed by Frank Whittle in 1930 and first flown in the Heinkel He 178 in 1939',{designed:1930,first_flight:1939,designer:'Frank Whittle'},['Whittle','He 178','Me 262'],1930],
['Turboprop engine','propulsion','engine-type','a turbine driving a propeller; efficient for regional and short-haul flight at lower speeds',{drive:'propeller',use:'regional aircraft'},['propeller','regional','efficiency'],0],
['Turboshaft engine','propulsion','engine-type','a gas turbine delivering shaft power rather than thrust; the standard helicopter engine',{output:'shaft power',use:'helicopters'},['helicopter','shaft','power turbine'],0],
['Ramjet engine','propulsion','engine-type','a duct with no moving parts that compresses air by forward motion; needs about Mach 0.5 to start and is efficient beyond Mach 3',{moving_parts:0,efficient_above:'Mach 3'},['supersonic','scramjet','duct'],0],
['Instrument Landing System (ILS)','avionics','system','radio beams \u2014 localizer and glideslope \u2014 guiding aircraft to the runway in low visibility',{components:'localizer + glideslope'},['precision approach','low visibility','runway'],0],
['TCAS','avionics','system','Traffic Collision Avoidance System: interrogates nearby transponders and commands evasive climbs or descents',{function:'collision avoidance'},['transponder','resolution advisory','safety'],0],
['ADS-B','avionics','system','Automatic Dependent Surveillance-Broadcast: aircraft broadcast GPS-derived position to controllers and other aircraft',{function:'surveillance broadcast'},['GPS','surveillance','NextGen'],0],
['Flight data recorder','avionics','system','the crash-survivable recorder of flight parameters, paired with the cockpit voice recorder',{records:'parameters + cockpit audio'},['black box','accident investigation','CVR'],0],
['Autopilot','avionics','system','automatically controls heading, altitude, and speed; standard equipment on airliners',{controls:'heading, altitude, speed'},['automation','cruise','flight management'],0],
['Fly-by-wire','avionics','system','electronic flight controls replacing mechanical linkages; pioneered on the Airbus A320',{pioneer:'Airbus A320',control:'electronic'},['A320','computers','envelope protection'],0],
['VFR and IFR','flight-operations','procedure','Visual Flight Rules versus Instrument Flight Rules: flying by outside reference or by instruments inside cloud',{rules:'VFR / IFR'},['weather minimums','instruments','flight plan'],0],
['Takeoff and landing','flight-operations','procedure','the highest-workload flight phases: rotation, climb-out, approach, flare, and touchdown',{phases:'takeoff, approach, landing'},['runway','V-speeds','flare'],0],
['Runway numbering','flight-operations','concept','runways are numbered by magnetic heading in tens of degrees: runway 27 points west, 270 degrees',{basis:'magnetic heading / 10'},['magnetic heading','airport','orientation'],0],
['Flight levels','flight-operations','concept','cruise altitudes expressed in hundreds of feet: FL350 means 35,000 feet on standard pressure',{example:'FL350 = 35,000 ft'},['altimetry','cruise','ATC'],0],
['Wake turbulence','flight-operations','concept','wingtip vortices trailing heavy aircraft; lighter aircraft must keep separation behind them',{source:'wingtip vortices'},['separation','heavy aircraft','vortices'],0],
['SR-71 Blackbird','military-aviation','aircraft','the fastest air-breathing crewed aircraft, cruising above Mach 3 at extreme altitude',{cruise:'Mach 3+',role:'reconnaissance'},['reconnaissance','speed record','titanium'],0],
['Messerschmitt Me 262','military-aviation','aircraft','the first operational jet fighter, entering Luftwaffe service in 1943',{service_entry:1943,engines:'2x turbojet'},['jet fighter','WWII','pioneering'],1943],
['Aerial refueling','military-aviation','procedure','tanker aircraft transfer fuel in flight through a boom or drogue, extending range and endurance',{method:'boom or drogue'},['tanker','range','endurance'],0],
['Cessna 172','general-aviation','aircraft','the most produced aircraft in history, over 44,000 built; the classic four-seat trainer',{built:'44,000+',seats:4,role:'trainer'},['trainer','piston','high-wing'],0],
['Piston aircraft engine','general-aviation','engine-type','reciprocating engines driving propellers on light aircraft, in inline, V-type, radial, or opposed layouts',{layouts:'inline, V, radial, opposed'},['propeller','light aircraft','avgas'],0],
['Helicopter rotor system','helicopters','system','a powered main rotor provides lift and thrust while the tail rotor counters torque',{lift:'main rotor',anti_torque:'tail rotor'},['rotor','collective','autorotation'],0],
['Autorotation','helicopters','procedure','the unpowered descent in which upward airflow keeps the rotor spinning, allowing a controlled landing after engine failure',{use:'engine-out landing'},['emergency','rotor','descent'],0],
['Uncrewed aircraft (UAVs)','unmanned-systems','aircraft','uncrewed aircraft flown remotely or autonomously, from quadcopters to high-altitude surveillance platforms',{control:'remote or autonomous'},['quadcopter','surveillance','regulations'],0],
['Air traffic control','airports-infrastructure','system','controllers sequence departures, en-route traffic, and arrivals to keep safe separation',{phases:'tower, approach, en-route'},['tower','separation','radar'],0],
['Airport runway','airports-infrastructure','facility','paved strips built to the length and strength their aircraft require, with lighting, markings, and approach aids',{features:'markings, lighting, approach aids'},['pavement','lighting','markings'],0],
['Wright Flyer','aviation-history','aircraft','the first powered, controlled airplane, flown at Kitty Hawk in 1903',{first_flight:1903,place:'Kitty Hawk'},['Wright brothers','first flight','1903'],1903],
['Lindbergh\u2019s Atlantic crossing','aviation-history','event','Charles Lindbergh\u2019s 1927 solo nonstop flight from New York to Paris in the Spirit of St. Louis',{year:1927,route:'New York to Paris'},['solo flight','Atlantic','Spirit of St. Louis'],1927]
];
var ASPECTS=['overview','technical deep-dive','operational use','historical timeline','safety relevance','comparative analysis'];
var CONTEXTS=['operations study','engineering review','training module','safety case','historical survey','fleet planning study'];
var TYPELBL={'aircraft':'aircraft','engine':'aircraft engine','engine-type':'engine type','system':'aviation system','procedure':'flight procedure','concept':'aviation concept','facility':'airport facility','event':'aviation event'};
function specText(o){return Object.keys(o).map(function(k){return k.replace(/_/g,' ')+': '+o[k];}).join('; ')+'.';}
/* Expansion anchors: aircraft-maintenance, airline-scheduling, weather-impacts.
   Same row format as ANCH: [subject, category, type, key fact, measures object, [related x3], year] */
var NEW_CATS=['aircraft-maintenance','airline-scheduling','weather-impacts'];
var ALLCATS=CATS.concat(NEW_CATS);
var NEW_ANCH=[
['A-check maintenance','aircraft-maintenance','procedure','overnight line-maintenance checks performed every 400 to 600 flight hours',{interval_fh:'400-600',duration:'overnight',setting:'line station'},['line maintenance','transit check','MRO'],0],
['C-check heavy maintenance','aircraft-maintenance','procedure','deep structural inspections every 20 to 24 months with the aircraft out of service for weeks',{interval:'20-24 months',downtime:'weeks',setting:'hangar'},['heavy maintenance','structural inspection','MRO'],0],
['Engine borescope inspection','aircraft-maintenance','procedure','internal turbine inspection with optical probes to detect blade damage without teardown',{tool:'borescope',finds:'blade damage',setting:'on-wing'},['turbine','non-destructive testing','on-wing'],0],
['Corrosion prevention program','aircraft-maintenance','program','scheduled inspections and treatments protecting airframes from structural corrosion',{method:'inspection plus treatment',scope:'airframe'},['airframe','corrosion','aging aircraft'],0],
['Fleet assignment optimization','airline-scheduling','process','matching aircraft types to routes by demand, range, and turnaround constraints',{goal:'right aircraft on the right route'},['scheduling','fleet planning','utilization'],0],
['Crew rostering','airline-scheduling','process','building legal crew pairings under duty-time regulations and union agreements',{constraint:'duty-time limits'},['pairings','rosters','regulations'],0],
['Airport slot management','airline-scheduling','process','securing takeoff and landing slots at congested airports under IATA coordination rules',{rule:'IATA slot conference'},['airports','congestion','grandfather rights'],0],
['Irregular operations recovery','airline-scheduling','process','rebuilding schedules after disruptions through rebooking, aircraft swaps, and ferry flights',{trigger:'disruption'},['IROPS','recovery','rebooking'],0],
['Thunderstorm avoidance','weather-impacts','procedure','rerouting around convective cells using onboard radar and controller guidance',{tool:'weather radar'},['convection','reroute','turbulence'],0],
['Aircraft icing conditions','weather-impacts','hazard','supercooled-droplet icing on airframes; anti-ice systems and holdover times manage the risk',{hazard:'airframe ice'},['de-icing','holdover time','freezing rain'],0],
['Volcanic ash avoidance','weather-impacts','hazard','ash clouds that can flame out engines; advisories and notices close affected airspace',{hazard:'engine flameout'},['VAAC','NOTAM','ash cloud'],0],
['Crosswind landing limits','weather-impacts','procedure','maximum demonstrated crosswinds by aircraft type, flown with crab and sideslip techniques',{technique:'crab and sideslip'},['landing','wind limits','runway'],0]
];
/* 24 unique (anchor, aspect) pairs: each anchor twice, with two different aspects */
var NEW_PAIRS=[];
for(var _a=0;_a<NEW_ANCH.length;_a++){NEW_PAIRS.push([_a,_a%ASPECTS.length]);NEW_PAIRS.push([_a,(_a+3)%ASPECTS.length]);}
var EXPAND_AFTER=10002;
function genExpansion(seed,opts){
  var i=seed-EXPAND_AFTER-1, pr=NEW_PAIRS[i%NEW_PAIRS.length];
  var a=NEW_ANCH[pr[0]], aspect=ASPECTS[pr[1]];
  var id=PREFIX+String(seed).padStart(6,'0');
  var serial='R-'+(10000+seed);
  var title,desc,src,code=null,rel=a[5].slice();
  if(i%2===0){
    code=serial;
    title=a[0]+': '+aspect+' ('+serial+')';
    var s1=a[0]+' is a '+(TYPELBL[a[2]]||a[2])+(a[6]>0?', first recorded in '+a[6]:'')+'. '+a[3]+'.';
    var s2='Key specifications: '+specText(a[4]);
    var s3='Related topics: '+a[5][0]+', '+a[5][1]+', '+a[5][2]+'.';
    if(aspect==='technical deep-dive')desc=s1+' '+s2+' These specifications define what '+a[0]+' can and cannot do. '+s3;
    else if(aspect==='operational use')desc=s1+' '+s3+' In service, '+a[0]+' is applied where these characteristics matter most. '+s2;
    else if(aspect==='historical timeline')desc=(a[6]>0?'In '+a[6]+', ':'In aviation history, ')+a[0]+' entered the record. '+s1+' '+s2;
    else if(aspect==='safety relevance')desc=s1+' '+s2+' Safety practice around '+a[0]+' follows directly from these characteristics. '+s3;
    else if(aspect==='comparative analysis')desc=s1+' Compared with its contemporaries, '+a[0]+' stands out as follows: '+a[3]+' '+s2;
    else desc=s1+' '+s2+' '+s3;
    src='online';
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=CONTEXTS[seed%CONTEXTS.length];
    var n=20+((seed*7919)%1981), yr=2016+(seed%11);
    title=a[0]+' \u2014 '+ctx+' '+code;
    desc='This generated study ('+code+', compiled '+yr+') examines '+n.toLocaleString('en-US')+' documented records concerning '+a[0]+' in a '+ctx+' setting. '+
      'The established facts remain: '+a[3]+' '+
      'The study focuses on '+a[5][0]+' and '+a[5][1]+', reporting patterns consistent with published aviation references. '+
      'As a Signature-generated study record, the scenario is illustrative; the core facts about '+a[0]+' come from published aviation sources.';
    src='signature';rel=[a[5][0],a[5][1],ctx+' (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{subject:a[0],subject_type:a[2],category:a[1],key_spec:a[3],specs:a[4],related:rel,year:a[6]||null,aspect:aspect,study_code:code},
    src:src,_seed:seed};
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>EXPAND_AFTER)return genExpansion(seed,opts);
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
    var s2='Key specifications: '+specText(a[4]);
    var s3='Related topics: '+a[5][0]+', '+a[5][1]+', '+a[5][2]+'.';
    if(aspect==='technical deep-dive')desc=s1+' '+s2+' These specifications define what '+a[0]+' can and cannot do. '+s3;
    else if(aspect==='operational use')desc=s1+' '+s3+' In service, '+a[0]+' is applied where these characteristics matter most. '+s2;
    else if(aspect==='historical timeline')desc=(a[6]>0?'In '+a[6]+', ':'In aviation history, ')+a[0]+' entered the record. '+s1+' '+s2;
    else if(aspect==='safety relevance')desc=s1+' '+s2+' Safety practice around '+a[0]+' follows directly from these characteristics. '+s3;
    else if(aspect==='comparative analysis')desc=s1+' Compared with its contemporaries, '+a[0]+' stands out as follows: '+a[3]+' '+s2;
    else desc=s1+' '+s2+' '+s3;
    src='online';
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=pick(CONTEXTS,rnd);
    var n=ri(rnd,20,2000),yr=ri(rnd,2016,2026);
    title=a[0]+' \u2014 '+ctx+' '+code;
    desc='This generated study ('+code+', compiled '+yr+') examines '+n.toLocaleString('en-US')+' documented records concerning '+a[0]+' in a '+ctx+' setting. '+
      'The established facts remain: '+a[3]+' '+
      'The study focuses on '+a[5][0]+' and '+a[5][1]+', reporting patterns consistent with published aviation references. '+
      'As a Signature-generated study record, the scenario is illustrative; the core facts about '+a[0]+' come from published aviation sources.';
    src='signature';rel=[a[5][0],a[5][1],ctx+' (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{subject:a[0],subject_type:a[2],category:a[1],key_spec:a[3],specs:a[4],related:rel,year:a[6]||null,aspect:aspect,study_code:code},
    src:src,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-AVI-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>160)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  else{var parts=r.description.split('. ');if(parts.length<2)e.push('description-sentences');if(!/\.$/.test(r.description.trim()))e.push('description-period');}
  if(ALLCATS.indexOf(r.category)<0)e.push('category');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(!s.subject||typeof s.subject!=='string')e.push('spec.subject');
    if(!s.subject_type||typeof s.subject_type!=='string')e.push('spec.subject_type');
    if(!s.key_spec||typeof s.key_spec!=='string')e.push('spec.key_spec');
    if(!s.specs||typeof s.specs!=='object'||!Object.keys(s.specs).length)e.push('spec.specs');
    if(!Array.isArray(s.related)||s.related.length<2||s.related.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.related');
    if(!(s.year===null||(Number.isInteger(s.year)&&s.year>=1500&&s.year<=2026)))e.push('spec.year');
  }
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-aviation-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('aviation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
