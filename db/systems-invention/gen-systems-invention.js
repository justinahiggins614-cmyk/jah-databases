(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var CATS=['cross-domain','constraints','novelty','validation','concepts'];
var FEAS=['speculative','plausible','feasible','prototype-ready'];
var PREFIX='JAH-SYS-';

/* Original Signature invention candidates: novel cross-domain combinations,
   clearly marked as generated concepts — never presented as existing products. */
var T=[
{cat:'cross-domain',dom:['aerospace','biology'],t:'Owl-feather serrated drone propellers',
 prob:'Small delivery drones are too loud for residential routes; propeller tip noise is the dominant complaint and the main regulatory barrier.',
 concept:'Apply the owl\'s silent-flight trick — serrated leading-edge feathers that break up turbulence — to drone propeller geometry. 3D-printed serrated blade cuffs retrofit onto existing propellers; the serrations trip the boundary layer into smaller, quieter vortices instead of one loud tip vortex.',
 nov:'Propeller noise research focuses on blade count and RPM; leading-edge serration borrowed from owl feathers is an underexplored retrofit path for small multirotors.',
 cons:['Serrations add drag — lift efficiency must be re-measured','3D-printed cuffs must survive vibration fatigue','Noise regulations vary by jurisdiction'],
 val:['Anechoic chamber test: stock vs serrated propellers at equal thrust','Endurance test: 200 flight hours on cuff adhesion','Community noise survey on a test route'],
 feas:'plausible'},
{cat:'cross-domain',dom:['architecture','biology'],t:'Termite-mound stack ventilation for edge data rooms',
 prob:'Small server rooms burn energy on air conditioning; passive cooling designs exist for big buildings but not for closet-scale edge deployments.',
 concept:'A termite-mound-inspired stack: tall exhaust chimney plus low intake vents create continuous convection, with thermal-mass walls smoothing day/night swings. Sized for a single rack, the geometry drives airflow with zero fans most of the year.',
 nov:'Passive stack ventilation is proven at building scale (Eastgate Centre); miniaturizing the principle to a rack enclosure is the novel step.',
 cons:['Climate-dependent — weak in hot, still environments','Dust ingress needs filtering that adds resistance','Retrofit geometry may not fit existing rooms'],
 val:['CFD simulation of the chimney geometry','Instrumented prototype: temperature logs vs a fanned control','Dust accumulation measurement over 90 days'],
 feas:'plausible'},
{cat:'concepts',dom:['energy','materials'],t:'Lotus-textured self-cleaning solar glass',
 prob:'Dust on solar panels cuts output 5-30% in arid regions; manual cleaning costs water and labor the sites can least afford.',
 concept:'Micro-textured glass mimicking the lotus leaf\'s papillae makes water bead and roll, carrying dust away. The texture is embossed during glass manufacture; a hydrophobic coating refreshes the effect.',
 nov:'Lotus coatings exist as sprays; integrating the microtexture into the panel glass itself (not an add-on film) is the differentiation.',
 cons:['Texture must not scatter enough light to offset cleaning gains','Abrasion from sandstorms degrades microstructures','Manufacturing retooling cost'],
 val:['Soiling test: textured vs plain panels in a dusty chamber','Optical transmission measurement before/after texturing','Accelerated abrasion cycling'],
 feas:'feasible'},
{cat:'cross-domain',dom:['robotics','biology'],t:'Gecko-setae reusable climbing pads',
 prob:'Inspection robots for smooth surfaces (glass facades, solar farms) need grip without suction cups that fail on dust or magnets that need ferrous surfaces.',
 concept:'Directional dry-adhesive pads mimicking gecko setae: angled micro-wedges engage under shear load and release on lift. Arrays of pads on a climbing robot give residue-free, repeatable attachment on glass and polished metal.',
 nov:'Gecko adhesives are lab-proven; packaging them as swappable robot foot modules with shear-activated engagement is the product step.',
 cons:['Dust fouls the microstructures — self-cleaning cycles needed','Load capacity per pad limits robot weight','Wet surfaces defeat dry adhesion'],
 val:['Shear/pull-off testing on glass, tile, and dusty glass','10,000 engage-release cycle durability','Prototype climber on a 3-story glass facade'],
 feas:'plausible'},
{cat:'cross-domain',dom:['energy','biology'],t:'Tubercle leading edges for small wind turbines',
 prob:'Small wind turbines stall easily in gusty, low-speed urban wind, killing their capacity factor where they are most wanted.',
 concept:'Humpback-whale-inspired leading-edge tubercles (rounded bumps) delay stall and keep lift at high angles of attack. Applied to sub-10kW turbine blades, they widen the productive wind-speed envelope.',
 nov:'Tubercle blades are studied for large turbines and aircraft; the small-turbine, low-Reynolds-number application is underexplored.',
 cons:['Manufacturing complexity vs extruded straight blades','Benefit shrinks at high Reynolds numbers','Noise profile changes need measurement'],
 val:['Wind-tunnel lift/drag polars vs smooth blades','Field test on a rooftop turbine for one season','Acoustic comparison'],
 feas:'plausible'},
{cat:'concepts',dom:['logistics','materials'],t:'Woodpecker-inspired shock packaging',
 prob:'Fragile goods still break in transit despite foam; foam is bulky, single-use, and petroleum-based.',
 concept:'Packaging modeled on the woodpecker\'s shock system: a stiff outer shell, a compliant lattice middle (like spongy bone), and a close-fitting inner cradle. The lattice is 3D-printed from recycled polymer in a graded density.',
 nov:'Biomimetic packaging usually copies honeycomb; the graded three-layer woodpecker stack targets repeated-drop performance, not single impact.',
 cons:['3D printing cost vs die-cut foam at scale','Graded lattice design needs drop-test tuning per product','Recycled feedstock consistency'],
 val:['ISTA drop-test protocol vs foam baseline','Compression and vibration testing','Cost-per-unit at 10k scale'],
 feas:'feasible'},
{cat:'cross-domain',dom:['water','biology'],t:'Beetle-inspired fog harvesters for remote sensors',
 prob:'Remote environmental sensors in arid zones need water for cleaning and cooling, but trucking water to them defeats the purpose.',
 concept:'Namib-desert-beetle-inspired panels: hydrophilic bumps on a hydrophobic background condense fog and channel droplets to a collector. Mounted above a sensor station, they harvest its own cleaning water.',
 nov:'Fog nets exist at large scale; beetle-pattern micro-surfaces sized for a single sensor station are the miniaturization play.',
 cons:['Needs regular fog/dew — useless in true deserts','Yield per panel is milliliters per day','Dust coats the pattern and kills efficiency'],
 val:['Climate-chamber fog yield measurement','Field deployment for one fog season','Cleaning-water balance: harvest vs panel needs'],
 feas:'speculative'},
{cat:'concepts',dom:['manufacturing','biology'],t:'Mantis-shrimp multispectral inspection head',
 prob:'Quality inspection misses defects visible only outside human vision (UV stress marks, IR heat signatures); multiple cameras mean multiple calibrations.',
 concept:'A single inspection head modeled on the mantis shrimp\'s 12-channel vision: stacked filtered photodiodes capture UV, visible, and near-IR in one shot, fused into one defect map.',
 nov:'Multispectral cameras exist; the mantis-shrimp-inspired parallel-channel fusion tuned for defect classes (not pretty pictures) is the angle.',
 cons:['Channel count vs cost and data rate','Calibration across spectra is fiddly','Defect datasets per spectrum are scarce'],
 val:['Defect-detection rate vs RGB-only baseline on 500 samples','Calibration stability over temperature','Throughput test on a real line'],
 feas:'speculative'},
{cat:'cross-domain',dom:['robotics','biology'],t:'Octopus-sucker soft grippers',
 prob:'Rigid grippers crush soft produce and fumble irregular parts; suction cups need smooth surfaces and constant vacuum.',
 concept:'Soft silicone fingers studded with octopus-inspired suction micro-cups: conform to the object, then a slight pressure differential engages hundreds of tiny seals. Gentle, no continuous vacuum, works on rough surfaces.',
 nov:'Soft grippers usually rely on friction or single big suction cups; distributed micro-sucker arrays are the differentiator.',
 cons:['Silicone fatigue over thousands of cycles','Food-safety certification for produce handling','Control complexity: per-finger pressure'],
 val:['Grip force vs object fragility matrix (eggs to engine parts)','100k cycle durability','Washdown and food-contact compliance'],
 feas:'plausible'},
{cat:'concepts',dom:['architecture','biology'],t:'Pinecone hygromorphic facade vents',
 prob:'Buildings over-ventilate or under-ventilate because occupants never adjust vents; motors and sensors add cost and failure points.',
 concept:'Facade vents using pinecone-inspired hygromorphic bilayers: wood-polymer laminates that curl open when humid and close when dry — no power, no sensors, self-regulating airflow.',
 nov:'Hygromorphic materials are lab curiosities; productizing them as a standardized vent module is the step.',
 cons:['Response time is minutes, not seconds','UV and rain degrade organics — encapsulation needed','Limited force: small vents only'],
 val:['Humidity-chamber actuation cycling (1000 cycles)','Airflow measurement vs fixed vents','Accelerated weathering test'],
 feas:'speculative'},
{cat:'cross-domain',dom:['materials','biology'],t:'Nacre-layered impact panels',
 prob:'Lightweight armor and protective cases trade weight for protection linearly; nature\'s abalone shell breaks that tradeoff with brick-and-mortar layering.',
 concept:'Panels mimicking nacre: hard ceramic micro-tablets in a soft polymer mortar, layered at the microscale. Cracks deflect at every interface instead of running straight through.',
 nov:'Nacre mimics exist in labs; a manufacturable roll-to-roll or 3D-printed process for meter-scale panels is the gap.',
 cons:['Tablet alignment at scale is hard','Polymer mortar creeps under sustained load','Cost vs conventional composites'],
 val:['Ballistic/impact testing vs monolithic ceramic','Interlaminar shear and creep tests','Pilot roll-to-roll run'],
 feas:'speculative'},
{cat:'concepts',dom:['energy','biology'],t:'Firefly-inspired LED diffusers',
 prob:'LED fixtures waste light in hotspots and glare; conventional diffusers eat 15-30% of output.',
 concept:'Diffuser micro-optics modeled on the firefly lantern\'s asymmetric microstructures: extract more light per watt and spread it evenly. Injection-molded into the fixture lens.',
 nov:'Firefly optics research targets extraction efficiency; the diffuser-as-fixture-lens integration is the product angle.',
 cons:['Micro-molding tooling cost','Dust on microstructures dims output','Benefit varies by LED package'],
 val:['Integrating-sphere efficiency vs standard diffuser','Glare (UGR) measurement','Dust-aging test'],
 feas:'plausible'},
{cat:'cross-domain',dom:['logistics','biology'],t:'Ant-colony warehouse dispatch',
 prob:'Warehouse robot fleets waste travel on congested aisles; central schedulers choke as fleet size grows.',
 concept:'Decentralized dispatch using ant-colony pheromone logic: robots lay virtual pheromones on completed routes, and the fleet probabilistically follows strong trails. Congestion evaporates the pheromone, rerouting traffic organically.',
 nov:'Ant-colony optimization is classic for static routing; the live pheromone-evaporation dispatch for physical robot fleets is the twist.',
 cons:['Emergent behavior is hard to certify for safety','Cold start: no pheromones on day one','Debugging emergent systems is painful'],
 val:['Simulation: throughput vs central scheduler at 200 robots','Congestion recovery time after a blocked aisle','Safety audit of emergent edge cases'],
 feas:'speculative'},
{cat:'cross-domain',dom:['urban-planning','biology'],t:'Slime-mold transit sketching tool',
 prob:'Transit planners iterate slowly on network designs; optimization software needs clean data they don\'t have yet.',
 concept:'A sketching tool using slime-mold (Physarum) growth simulation: planners drop stations on a map, and the virtual slime mold grows efficient connecting networks. Fast, visual, surprisingly near-optimal — a thinking aid, not a final answer.',
 nov:'Physarum computing is a research demo; packaging it as a planner\'s sketching toy is the productization.',
 cons:['Not a substitute for real demand modeling','Results need engineer interpretation','Novelty may outshine utility'],
 val:['Compare generated networks vs human designs on 5 cities','Planner usability study','Runtime on metro-scale maps'],
 feas:'prototype-ready'},
{cat:'cross-domain',dom:['robotics','biology'],t:'Bat-echolocation indoor navigation',
 prob:'Indoor drones lose GPS and struggle in dark, featureless warehouses; lidar is expensive and cameras need light.',
 concept:'Ultrasonic echolocation arrays modeled on bat biosonar: chirp, listen, and build a 3D map from echo timing. Works in darkness, through dust, and costs a fraction of lidar.',
 nov:'Ultrasonic sensors exist as single-point rangers; bat-style phased-array echolocation imaging for drones is the leap.',
 cons:['Range limited to tens of meters','Multi-drone chirp interference','Resolution coarser than lidar'],
 val:['Mapping accuracy vs lidar ground truth in a warehouse','Darkness/dust robustness tests','Interference test with 5 drones'],
 feas:'speculative'},
{cat:'concepts',dom:['energy','biology'],t:'Electric-eel stacked soft batteries',
 prob:'Soft robots need soft power; rigid batteries are the stiffest component in an otherwise squishy machine.',
 concept:'Stacked electrocyte-inspired cells: thin ion-selective membranes layered like the eel\'s electric organ, producing voltage from stacked gradients. Flexible, safe chemistry, modest voltage per stack.',
 nov:'Bio-batteries usually chase capacity; the eel-stack form factor for soft-robotics integration is the niche.',
 cons:['Energy density far below lithium','Cycle life of membrane stacks unproven','Voltage per stack is low — many stacks needed'],
 val:['Energy density and cycle-life measurement','Flex-cycle durability (10k bends)','Integration demo in a soft gripper'],
 feas:'speculative'},
{cat:'concepts',dom:['materials','biology'],t:'Cuttlefish adaptive camouflage panels',
 prob:'Static camouflage fails when backgrounds change; active displays are power-hungry and fragile outdoors.',
 concept:'Panels with cuttlefish-inspired chromatophore pixels: elastomer sacs of pigment that expand/contract mechanically. Low power (hold state without energy), sunlight-readable, genuinely flexible.',
 nov:'E-ink is slow and monochrome; chromatophore pixels promise fast, colorful, bistable camouflage.',
 cons:['Pigment fade under UV','Pixel density vs mechanical complexity','Color gamut limited by available pigments'],
 val:['Switching speed and contrast measurement','UV aging of pigments','Outdoor readability test'],
 feas:'speculative'},
{cat:'cross-domain',dom:['civil-engineering','biology'],t:'Beaver-dam micro flood barriers',
 prob:'Flash floods overwhelm fixed drains; sandbags are slow, labor-intensive, and single-use.',
 concept:'Deployable barriers mimicking beaver dam construction: interlocking permeable modules that slow and pond water rather than blocking it outright. Slowing the flow cuts downstream peak height — the beaver\'s actual trick.',
 nov:'Flood barriers aim to block; the permeable slow-and-pond approach borrowed from beavers is the contrarian angle.',
 cons:['Permeable means some water passes — messaging challenge','Debris clogging changes behavior','Deployment speed vs sandbags'],
 val:['Flume test: peak-flow reduction vs sandbags','Deployment-time trial with a 4-person crew','Debris-loading test'],
 feas:'plausible'},
{cat:'cross-domain',dom:['civil-engineering','biology'],t:'Spider-web vibration structural monitors',
 prob:'Bridges and towers need continuous structural health data; wired sensor networks are expensive to install and maintain.',
 concept:'A web of tensioned fiber lines across a structure, monitored at anchor points like a spider reading its web: vibrations and tension changes reveal damage location. One interrogator watches the whole web.',
 nov:'Distributed fiber sensing exists; the spider-web topology with anchor-point-only electronics is the low-cost variant.',
 cons:['Temperature confounds tension readings','Anchor installation still needs access','Calibration per structure'],
 val:['Damage-localization accuracy on a test truss','Temperature-compensation validation','Cost comparison vs conventional SHM'],
 feas:'plausible'},
{cat:'cross-domain',dom:['aerospace','biology'],t:'Albatross dynamic-soaring glider drones',
 prob:'Long-endurance ocean monitoring needs weeks aloft; batteries and solar can\'t yet do it cheaply at small scale.',
 concept:'Glider drones that harvest energy via albatross-style dynamic soaring: climbing into wind gradients and diving to gain speed, extracting net energy from wind shear. No motor needed in the right conditions.',
 nov:'Dynamic soaring is proven in RC gliders; autonomous shear-seeking control for ocean monitoring missions is the step.',
 cons:['Needs consistent wind shear — not everywhere','Autonomy for shear-seeking is unsolved at small scale','Launch and recovery at sea'],
 val:['Simulation: energy budget in measured ocean wind fields','Autonomous soaring demo from a ship','Endurance comparison vs solar fixed-wing'],
 feas:'speculative'}
];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var pool=opts.category?T.filter(function(x){return x.cat===opts.category;}):T;
  if(!pool.length)pool=T;
  var t=pick(pool,rnd);
  var doms=shuffle(t.dom,rnd);
  if(rnd()<0.4)doms.push(pick(['sensors','manufacturing','agriculture','medicine'],rnd));
  doms=doms.slice(0,3);
  var cons=shuffle(t.cons,rnd).slice(0,3);
  var val=shuffle(t.val,rnd).slice(0,3);
  var feas=(opts.feasibility&&FEAS.indexOf(opts.feasibility)>=0)?opts.feasibility:t.feas;
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:t.t+' — invention candidate',category:t.cat,domains:doms,domain_count:doms.length,
    problem_statement:t.prob,
    concept:t.concept+' This is a Signature-generated invention candidate: an original concept sketch, not an existing product. Treat feasibility as a hypothesis to test, not a claim.',
    novelty_assessment:t.nov,constraints:cons,validation_plan:val,feasibility:feas,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-SYS-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.domains)||r.domains.length<2||r.domains.length>4)e.push('domains');
  else r.domains.forEach(function(x){if(typeof x!=='string'||!x.length)e.push('domain');});
  /* REAL invariant: domain_count must equal the domains array length. */
  if(r.domain_count!==r.domains.length)e.push('domain_count');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.problem_statement!=='string'||r.problem_statement.length<80)e.push('problem_statement');
  if(typeof r.concept!=='string'||r.concept.length<150)e.push('concept');
  if(typeof r.novelty_assessment!=='string'||!r.novelty_assessment.length)e.push('novelty_assessment');
  if(!Array.isArray(r.constraints)||r.constraints.length<2||r.constraints.length>5)e.push('constraints');
  if(!Array.isArray(r.validation_plan)||r.validation_plan.length<2||r.validation_plan.length>5)e.push('validation_plan');
  if(FEAS.indexOf(r.feasibility)<0)e.push('feasibility');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-systems-invention-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('systems-invention',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
