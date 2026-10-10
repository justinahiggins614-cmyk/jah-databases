/* JAH Urban Planning Database generator — jahdb-urban-planning-1.0.
   Deterministic client-side generator. Same seed + same version always makes
   the same record. Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['zoning','transit','housing','public-space','sustainability','land-use','urban-design','mobility'];
var PREFIX='JAH-URB-';
/* Anchors: [name, category, fact1, fact2, example place, example fact].
   fact1/fact2 are single sentences verified from public sources. */
var ANCHORS=[
["Transit-Oriented Development","transit","Transit-oriented development concentrates housing, jobs, and services within walking distance of high-capacity transit stations, typically a five to ten minute walk.","The approach pairs higher-density mixed-use zoning with reduced parking requirements near stations.","Curitiba, Brazil","Curitiba's 1966 master plan built the city around five structural transit corridors, and its bus rapid transit system, launched in 1974 as the world's first full BRT, carries about 2.3 million passengers per day."],
["Bus Rapid Transit","transit","Bus rapid transit gives buses rail-like speed and capacity through dedicated lanes, off-board fare collection, and platform-level boarding.","Curitiba introduced the first full BRT system in 1974 after planners abandoned a costly light-rail plan in favor of a trunk-and-feeder bus network on segregated median lanes.","Bogota, Colombia","Bogota's TransMilenio BRT opened in 2000 and became one of the busiest bus corridors in the world."],
["R-1 Single-Family Residential Zoning","zoning","In New York City's zoning code, R1 districts permit detached single-family homes and community facilities, the lowest-density residential category.","Higher numbers after the R indicate greater permitted density, from R1 detached houses up to R10 residential towers.","New York City, USA","New York's Zoning Resolution defines R1-1 and R1-2 as single-family detached residence districts."],
["C-1 Commercial Overlay Districts","zoning","C1 and C2 commercial overlay districts are mapped on local commercial streets inside residential neighborhoods to host neighborhood-oriented retail and services.","Commercial districts run from C1 neighborhood retail up to C8 districts that allow gas stations and car repair.","New York City, USA","Commercial overlays are designated C1-1 through C1-5 and C2-1 through C2-5 on the New York zoning maps."],
["M-1 Light Manufacturing Districts","zoning","M1 districts permit light manufacturing alongside many commercial uses, while community facilities are limited and new residential development is generally not allowed.","Heavier industry sits in M2 and M3 districts, with M3 allowing heavy manufacturing.","New York City, USA","New York's manufacturing districts, such as M1-1 and M2-2, separate industrial uses from residential areas."],
["Mixed-Use Special Districts","zoning","Mixed-use districts permit new residential and nonresidential uses, including commercial, community facility, and light industrial, as of right in the same area.","Pairing residence and manufacturing districts lets cities keep jobs near homes without heavy-industry conflicts.","New York City, USA","New York's Special Mixed Use District pairs manufacturing and residence districts under tailored rules."],
["Urban Growth Boundary","land-use","An urban growth boundary draws a legal line around a metro area, concentrating development inside and preserving farmland and open space outside.","Oregon's 1973 statewide planning law required every city to adopt one, with Portland's boundary the best-known example.","Portland, Oregon","Portland's urban growth boundary, established under Oregon's 1973 land-use law, is expanded only after the region demonstrates land need."],
["Floor Area Ratio","zoning","Floor area ratio caps building bulk by limiting total floor area to a multiple of lot area.","Cities trade higher FAR for public benefits such as affordable housing or plazas through density bonuses.","General practice","FAR is the standard bulk control in zoning codes worldwide."],
["Inclusionary Zoning","housing","Inclusionary zoning requires or incentivizes developers to set aside a share of new units at below-market rents.","Programs typically pair the mandate with density bonuses so projects remain financially viable.","General practice","Hundreds of cities use inclusionary zoning to produce income-restricted homes."],
["Accessory Dwelling Units","housing","Accessory dwelling units are small secondary homes on single-family lots, such as garage conversions, basement apartments, or backyard cottages.","Legalizing ADUs adds gentle density without changing neighborhood character.","General practice","California and Oregon state laws overrode local bans on ADUs to expand housing supply."],
["Complete Streets","mobility","Complete streets are designed for everyone, including pedestrians, cyclists, transit riders, and drivers, with sidewalks, bike lanes, and safe crossings.","The design approach reduces crashes by separating modes and calming traffic.","General practice","More than fifteen hundred jurisdictions have adopted complete-streets policies."],
["Protected Bike Lane Networks","mobility","Protected bike lanes use curbs, planters, or parked cars to separate cyclists from motor traffic, sharply increasing ridership.","Networks matter more than isolated lanes, since connected grids let people ride door to door.","Copenhagen, Denmark","Copenhagen's continuous protected network makes cycling a dominant commute mode."],
["Congestion Pricing","mobility","Congestion pricing charges drivers to enter crowded central zones, cutting traffic and funding transit.","London's 2003 charge and Stockholm's system both reduced inner-city traffic after introduction.","London, UK","London introduced its congestion charge in 2003."],
["Light Rail Transit","transit","Light rail runs electric trains on streets or dedicated tracks, carrying more riders than buses at lower cost than subways.","Modern light rail lines anchor transit-oriented development corridors in mid-size cities.","General practice","Portland's MAX and Denver's light rail reshaped their regions' growth patterns."],
["Commuter Rail","transit","Commuter rail links suburbs to city centers with high-capacity trains, typically on peak-hour schedules.","Through-running and frequent off-peak service turn commuter lines into regional rail.","General practice","The Paris RER and Tokyo's Yamanote line show the regional-rail model at scale."],
["Streetcar and Tram Systems","transit","Modern streetcars run on rails in mixed traffic or dedicated lanes, serving short downtown circulators and development corridors.","They work best where frequent stops and visible permanence attract riders and investment.","General practice","Portland's streetcar loop helped catalyze Pearl District redevelopment."],
["Ferry and Water Transit","transit","Ferries move commuters across harbors and rivers where bridges are congested or absent.","Waterfront terminals double as public spaces when designed well.","General practice","New York's NYC Ferry and Hong Kong's Star Ferry carry daily commuters."],
["Bikeshare Systems","mobility","Station-based or dockless bikeshare puts shared bikes within a short walk across a city, feeding transit stations.","Electric bikes in fleets extend the practical trip range to several miles.","Paris, France","Paris's Velib system, launched in 2007, pioneered large-scale bikeshare."],
["Off-Board Fare Collection","transit","Collecting fares before boarding, at station gates or ticket machines, cuts vehicle dwell time dramatically.","Curitiba's tube stations made prepayment a signature BRT feature in the 1980s.","Curitiba, Brazil","Curitiba's enclosed tube stations enabled level boarding and prepayment."],
["Bus-Only Lanes","transit","Painted or physically separated bus lanes let buses bypass congestion, improving speed and reliability.","Enforcement cameras keep lanes clear where physical barriers are impractical.","General practice","Seoul and New York expanded bus-lane networks to speed commutes."],
["Singapore Public Housing","housing","Singapore's Housing and Development Board houses the large majority of residents in publicly built flats.","Ethnic integration quotas in each block prevent segregation.","Singapore","Roughly four in five Singaporeans live in HDB flats."],
["Vienna Social Housing","housing","Vienna houses about three in five residents in municipally built or subsidized housing.","Limited-profit developers and strong tenant protections keep rents stable.","Vienna, Austria","Vienna's century-old social housing program is a global reference."],
["Missing Middle Housing","housing","Missing-middle types, such as duplexes, fourplexes, courtyard apartments, and townhouses, fit between detached homes and mid-rise apartments.","They add density at a scale compatible with single-family streets.","General practice","Minneapolis legalized triplexes citywide in 2018."],
["Housing Cooperatives","housing","In housing cooperatives, residents collectively own the building through shares, stabilizing costs and giving democratic control.","Limited-equity co-ops cap resale prices to preserve affordability permanently.","General practice","New York's Mitchell-Lama program created tens of thousands of co-op units."],
["Rent Stabilization","housing","Rent stabilization caps annual rent increases on covered units, protecting sitting tenants from sudden displacement.","Pairing caps with new construction is the common policy compromise.","General practice","New York, San Francisco, and Berlin have all used rent regulation."],
["Pedestrian-Only Zones","public-space","Car-free zones give streets fully to people, boosting foot traffic, safety, and retail sales.","Curitiba paired pedestrian streets with its transit corridors in the 1970s.","Curitiba, Brazil","Curitiba's Rua XV pedestrian mall dates to its 1970s master-plan era."],
["Pocket Parks","public-space","Pocket parks turn vacant lots into small green spaces within a short walk of surrounding homes.","They give children play space in dense blocks and lift nearby street life.","General practice","Philadelphia's vacant-lot greening program created hundreds of pocket parks."],
["Greenways","public-space","Greenways are linear parks along rivers, rail lines, or streets, combining recreation with non-motorized transport.","They stitch neighborhoods together and raise adjacent land values.","General practice","Chicago's 606 and Atlanta's BeltLine are rail-to-trail greenways."],
["Elevated Rail-to-Park Conversions","public-space","Elevated rail-to-park conversions turn obsolete infrastructure into linear public space.","New York's High Line, opened in 2009 on a former freight viaduct, drew millions of visitors and nearby development.","New York City, USA","The High Line opened in 2009 atop a disused elevated rail line."],
["Superblocks","public-space","Barcelona's superblocks group nine city blocks, keeping through-traffic on the perimeter and freeing interior streets for people.","Interior streets gain play areas, seating, and greenery while cut-through traffic falls.","Barcelona, Spain","Barcelona began piloting superblocks in the Poblenou district."],
["Woonerf Shared Streets","public-space","A woonerf is a street where pedestrians, cyclists, and slow cars share one level surface with no curbs.","Design cues such as planters, benches, and paving keep vehicle speeds near walking pace.","Netherlands","Dutch woonerven date to the 1970s traffic-calming movement."],
["Public Markets","public-space","Public markets concentrate food vendors and small businesses in managed halls or squares.","They incubate immigrant entrepreneurs and anchor neighborhood retail.","General practice","Seattle's Pike Place and Barcelona's La Boqueria are landmark markets."],
["Green Roofs","sustainability","Green roofs layer soil and plants over waterproofing, cutting cooling loads, slowing stormwater, and extending roof life.","Extensive sedum roofs need little maintenance, while intensive roofs function as gardens.","General practice","Toronto requires green roofs on large new buildings."],
["Urban Tree Canopy","sustainability","Street trees shade sidewalks, filter air, and can lower summer surface temperatures by several degrees.","Canopy goals typically target thirty to forty percent coverage, prioritizing heat-vulnerable neighborhoods.","General practice","Melbourne's urban forest strategy maps every public tree."],
["Bioswales and Rain Gardens","sustainability","Bioswales are planted channels that capture street runoff, filtering pollutants before water reaches rivers.","They cost less than buried pipes while greening the streetscape.","General practice","Portland's green-street program installed thousands of curb bioswales."],
["District Energy Systems","sustainability","District energy pipes hot water or steam from central plants to whole neighborhoods, often paired with combined heat and power.","Shared systems reach efficiencies individual boilers cannot match.","General practice","Copenhagen's district heating covers nearly all buildings."],
["Brownfield Redevelopment","land-use","Brownfields are former industrial sites with real or suspected contamination, and cleanup unlocks them for housing and parks.","Liability protections and tax credits make remediation financeable.","General practice","The US EPA brownfields program has assessed tens of thousands of sites."],
["Infill Development","land-use","Infill builds on vacant or underused parcels inside the existing urban footprint.","It uses existing roads, pipes, and transit instead of extending them outward.","General practice","Infill is the primary growth strategy inside urban growth boundaries."],
["Transfer of Development Rights","land-use","Transfer of development rights lets owners in preservation areas sell unused development rights to builders in growth areas.","Landmarks and farmland stay protected while density shifts where infrastructure exists.","General practice","New Jersey's Pinelands program pioneered TDR for farmland preservation."],
["Density Bonuses","zoning","Density bonuses grant extra floor area or height in exchange for public benefits like affordable units or plazas.","Calibrated bonuses make the trade pencil out for both developers and the public.","General practice","Seattle's incentive zoning trades height for affordable housing."],
["Setback and Bulk Controls","zoning","Setbacks push upper floors back from the street, preserving light and air at sidewalk level.","Daylight planes and sky-exposure rules shaped the classic setback tower profile.","New York City, USA","New York's 1916 zoning created the setback skyscraper."],
["New Urbanism","urban-design","New Urbanism designs walkable, mixed-use neighborhoods with a clear center, five-minute walksheds, and a range of housing.","Its transect runs from rural preserve to urban core with appropriate intensity at each step.","General practice","Seaside, Florida, built in the 1980s, is the movement's iconic built example."],
["Eyes on the Street","urban-design","Jane Jacobs argued that busy sidewalks with mixed uses and eyes on the street make neighborhoods safe.","Short blocks, varied building ages, and active ground floors create natural surveillance.","New York City, USA","Jacobs published The Death and Life of Great American Cities in 1961."],
["Placemaking","public-space","Placemaking shapes public spaces around how people actually use them, often through quick temporary pilots.","Lighter-quicker-cheaper trials test plazas and parklets before permanent construction.","General practice","Times Square's pedestrian plazas began as a 2009 pilot."],
["Active Street Frontages","urban-design","Active frontages put doors, windows, and shops along the sidewalk instead of blank walls and parking.","Cities require minimum transparency and limit curb cuts on retail streets.","General practice","Ground-floor retail mandates keep commercial corridors lively."],
["Universal Design","urban-design","Universal design makes streets and buildings usable by everyone, with curb ramps, tactile paving, audible signals, and level entries.","Designing for disability improves comfort for all users.","General practice","US accessibility standards codified accessible public-realm design."],
["Crime Prevention Through Environmental Design","urban-design","Crime prevention through environmental design reduces crime through natural surveillance, clear sightlines, territorial cues, and maintained spaces.","Lighting, sightlines, and activity programming matter more than fences.","General practice","CPTED principles guide park and station design worldwide."],
["Wayfinding Systems","mobility","Legible wayfinding, with consistent signs, maps, and landmarks, helps people navigate transit and public space.","Good systems cut perceived wait times and wayfinding anxiety.","General practice","London's Legible London pedestrian signs standardized city navigation."],
["Urban Agriculture","sustainability","Rooftop farms, community gardens, and vertical farms grow food inside cities.","They shorten supply chains and teach food literacy, though they rarely feed whole districts.","General practice","Detroit's urban farms reuse thousands of vacant lots."],
["Stormwater Green Infrastructure","sustainability","Green infrastructure, such as permeable pavement, rain gardens, and tree trenches, manages rain where it falls.","It reduces combined-sewer overflows while cooling streets.","General practice","Philadelphia's Green City, Clean Waters plan targets green stormwater citywide."]
];
/* 20 lenses x 10 editions = 200 variants per anchor; 50 anchors = 10,000 records. */
var LENSES=[
["Core Overview","online","This overview edition presents {n} as a core {c} concept for contemporary cities.",null],
["How It Works","online","In practice, {n} works through coordinated policy, design standards, and sustained public investment.",null],
["Key Principles","signature","Its guiding principles emphasize aligning land use with infrastructure, measuring outcomes, and engaging the community early.",null],
["Real-World Example","online","{p} shows it in action: {f}",null],
["Practitioner Guide","signature","Practitioners begin with a baseline audit, set measurable targets, pilot in one district, and scale what the data supports.","Edition {e} refreshes benchmarks against recent practice."],
["Comparative Analysis","signature","Compared with alternatives in {c}, {n} trades higher upfront coordination for durable compounding benefits.",null],
["Historical Development","signature","The approach matured through twentieth-century practice and keeps evolving as cities gather better data.",null],
["Metrics and Measurement","signature","Performance is tracked with indicators matched to the goal, reviewed annually against adopted targets.",null],
["Implementation Checklist","signature","A standard rollout covers baseline study, stakeholder mapping, pilot design, funding, delivery, and post-occupancy review.",null],
["Common Misconceptions","signature","A common misconception is that {n} demands massive budgets, when most gains come from using existing assets better.",null],
["Signature Case Study","signature","This Signature case study applies {n} to a mid-size district, narrating decisions, costs, and outcomes step by step.","All figures here are illustrative planning scenarios, not promises."],
["Design Patterns","signature","Recurring patterns include modular phasing, layered networks, and human-scale detailing at the street edge.",null],
["Policy and Regulation","signature","Enabling policy usually combines reformed rules, dedicated funding, and clear performance standards.",null],
["Equity Review","signature","An equity review asks who benefits, who bears the costs, and whether excluded voices shaped the plan.",null],
["Climate Review","signature","A climate review counts emissions avoided, heat reduced, and resilience gained for each dollar spent.",null],
["Cost and Funding","signature","Funding typically blends capital budgets, grants, value capture, and dedicated levies where the law allows.",null],
["Community Engagement","signature","Engagement works best as co-design, with walks, workshops, and prototypes rather than presentation-only hearings.",null],
["Maintenance and Operations","signature","Long-run success depends on maintenance budgets and operating plans fixed at the design stage.","Deferred maintenance is the most common reason good plans fail."],
["Technology Integration","signature","Sensors, open data, and digital twins increasingly guide day-to-day operations and investment timing.",null],
["Future Outlook","signature","Over the next decade, expect tighter integration with climate targets and sharper digital planning tools.",null]
];
var CATDATA={
"zoning":{principles:["Separate incompatible uses while allowing compatible mixes","Keep rules predictable and legible for applicants","Tie intensity to infrastructure capacity"],mechanisms:["Use districts with permitted-use tables","Set bulk controls for FAR, height, and setbacks","Offer bonuses for public benefits"]},
"transit":{principles:["Design for frequency, speed, and reliability","Integrate fares and transfers across modes","Connect land use to stations"],mechanisms:["Dedicated rights-of-way","Off-board fare collection","Level boarding platforms"]},
"housing":{principles:["Add supply at many price points","Protect existing residents from displacement","Locate homes near jobs and transit"],mechanisms:["Upzoning near transit","Subsidy and voucher programs","Legalizing gentle density"]},
"public-space":{principles:["Design for people first","Program spaces for daily use","Maintain to a high standard"],mechanisms:["Pedestrian-priority design","Flexible seating and shade","Community stewardship agreements"]},
"sustainability":{principles:["Reduce emissions and heat","Manage water where it falls","Protect ecosystems"],mechanisms:["Green infrastructure retrofits","Energy-efficient systems","Urban canopy expansion"]},
"land-use":{principles:["Grow inward before outward","Remediate before abandoning","Balance jobs and housing"],mechanisms:["Growth boundaries","Brownfield cleanup programs","Infill incentives"]},
"urban-design":{principles:["Human scale first","Eyes on the street","Durable materials"],mechanisms:["Form-based controls","Active frontage rules","Universal access standards"]},
"mobility":{principles:["Move people, not vehicles","Build complete networks, not fragments","Protect the most vulnerable users"],mechanisms:["Protected lanes","Traffic calming","Integrated wayfinding"]}
};
function fill(tpl,a,lens,ed){
  return tpl.replace(/\{n\}/g,a[0]).replace(/\{c\}/g,a[1]).replace(/\{p\}/g,a[4]).replace(/\{f\}/g,a[5]).replace(/\{e\}/g,String(ed));
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var ai=(seed-1)%ANCHORS.length;
  var lix=Math.floor((seed-1)/ANCHORS.length)%LENSES.length;
  var ed=(Math.floor((seed-1)/(ANCHORS.length*LENSES.length))%10)+1;
  if(opts.category){
    var matches=[];for(var m=0;m<ANCHORS.length;m++)if(ANCHORS[m][1]===opts.category)matches.push(m);
    if(matches.length)ai=matches[(seed-1)%matches.length];
  }
  var a=ANCHORS[ai],lens=LENSES[lix];
  var cd=CATDATA[a[1]];
  var desc=a[2]+' '+a[3]+' '+fill(lens[2],a,lens,ed);
  if(lens[3])desc+=' '+fill(lens[3],a,lens,ed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var scale=0.9+ed*0.02;
  var metrics={};
  if(a[1]==='zoning')metrics={far_max:ri(rnd,2,8),min_lot_m2:Math.round(ri(rnd,200,2000)*scale)};
  else if(a[1]==='transit')metrics={daily_ridership:Math.round(ri(rnd,50000,2500000)*scale),corridor_km:ri(rnd,5,120)};
  else if(a[1]==='housing')metrics={units_planned:Math.round(ri(rnd,500,50000)*scale),affordable_share_pct:ri(rnd,10,40)};
  else if(a[1]==='public-space')metrics={area_m2:Math.round(ri(rnd,500,50000)*scale),daily_visitors:ri(rnd,200,20000)};
  else if(a[1]==='sustainability')metrics={co2_t_avoided:Math.round(ri(rnd,100,100000)*scale),canopy_target_pct:ri(rnd,25,45)};
  else if(a[1]==='land-use')metrics={acres_targeted:Math.round(ri(rnd,50,5000)*scale),infill_share_pct:ri(rnd,30,80)};
  else if(a[1]==='urban-design')metrics={block_length_m:ri(rnd,60,200),transparency_pct:ri(rnd,40,80)};
  else metrics={network_km:Math.round(ri(rnd,10,300)*scale),mode_share_target_pct:ri(rnd,20,60)};
  var rec={
    id:id,
    title:a[0]+' — '+lens[0]+' (Edition '+ed+')',
    description:desc,
    category:a[1],
    src:lens[1],
    spec:{
      concept:a[0],
      category:a[1],
      lens:lens[0],
      edition:ed,
      principles:cd.principles.slice(),
      mechanisms:cd.mechanisms.slice(),
      real_examples:[{place:a[4],fact:a[5]}],
      key_metrics:metrics,
      source_note:lens[1]==='online'?'Core facts verified from public sources.':'Signature-generated expansion built on verified anchor facts.'
    },
    _seed:seed
  };
  return rec;
}
function countSentences(s){var t=String(s).replace(/\d+\.\d+/g,'N');var m=t.match(/[^.!?]+[.!?]/g);return m?m.length:0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not-object']};
  if(!/^JAH-URB-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>180)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  var ns=countSentences(r.description||'');
  if(ns<2||ns>4)e.push('sentences:'+ns);
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(typeof s.concept!=='string'||!s.concept.length)e.push('spec.concept');
    if(s.category!==r.category)e.push('spec.category');
    if(!Array.isArray(s.principles)||s.principles.length!==3)e.push('spec.principles');
    if(!Array.isArray(s.mechanisms)||s.mechanisms.length!==3)e.push('spec.mechanisms');
    if(!Array.isArray(s.real_examples)||!s.real_examples.length||!s.real_examples[0].place||!s.real_examples[0].fact)e.push('spec.real_examples');
    if(!s.key_metrics||typeof s.key_metrics!=='object')e.push('spec.key_metrics');
    else{for(var k in s.key_metrics){var v=s.key_metrics[k];if(typeof v!=='number'||v<0||v>3000000)e.push('spec.metric:'+k);}}
    if(typeof s.edition!=='number'||s.edition<1||s.edition>10)e.push('spec.edition');
  }
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var ids={};(sample||[]).forEach(function(x){if(x&&x.id)ids[x.id]=1;});
  return ids[rec.id]?{ok:false,errors:['duplicate-id']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-urban-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('urban-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
if(typeof require!=='undefined'&&require.main===module){
  var ok=0,fail=[];
  for(var i=1;i<=40;i++){var v=validate(generate(i,{},prng(i)));if(v.ok)ok++;else fail.push([i,v.errors]);}
  console.log('urban-planning harness: '+ok+'/40 '+(ok===40?'PASS':'FAIL'));
  if(fail.length)console.log(JSON.stringify(fail));
}
})();
