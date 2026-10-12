(function(){'use strict';
/* Captain Planet Universal System Database generator — jahdb-captain-planet-1.0.
   Property of Justin Addam Higgins (JAH). Signature system.
   TWO record kinds:
   (1) application — green token (CO2) applications: what it does, how it earns
       tokens, scale, tokens generated.
   (2) tracking — THE GRAND TRACKING SYSTEM: components that track all tokens
       (ledger, verification, aggregation).
   CORE: idle hardware earns environmental tokens. Start simple, compound to
   space and back: phone -> ... -> planetary -> ... -> phone.
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
function sha(s){var h=5381;for(var i=0;i<s.length;i++){h=((h<<5)+h+s.charCodeAt(i))|0;}return ('0000000'+(h>>>0).toString(16)).slice(-8);}
var PREFIX='JAH-CPCT-';
var SCALES=['phone','pc','house','community','town','city','region','super-company','planetary'];
var COMPLEX=['simple','moderate','complex','boundless'];
var SCALE_HW={phone:'a phone',pc:'an idle PC',house:'a home hub',community:'a community server',town:'a town cluster',city:'a city data room',region:'a regional cluster','super-company':'a super-company compute fleet',planetary:'a planetary node mesh'};
var SCALE_ROLE={phone:'leaf node',pc:'leaf node',house:'leaf node',community:'relay',town:'relay',city:'hub',region:'hub','super-company':'orchestrator',planetary:'planetary aggregator'};
var MODULES=[
 ['env-modeling','environmental modeling'],['token-accounting','token accounting'],
 ['distributed-nodes','distributed nodes'],['drone-sim','drone survey sim'],
 ['orbital-mechanics','orbital mechanics'],['climate','climate modeling'],
 ['biodiversity','biodiversity indexing'],['hydrology','hydrology'],
 ['soil-chemistry','soil chemistry'],['renewable-energy','renewable energy'],
 ['carbon-cycle','carbon cycle'],['ledger','tamper-evident ledger'],
 ['identity','quad-helix identity'],['self-upgrade','self-upgrade evaluator'],
 ['app-functions','endless application functions']
];
var SCENARIOS=[
 'Rooftop Solar Balancing','Night-Shift Compute Harvest','River Water Watch','Backyard Biodiversity Count',
 'School Lab Ledger','Clinic Cold-Chain Guard','Farm Soil Mapping','Neighborhood Mesh Relay',
 'Library Digitization Drive','Shuttle Fleet Tracker','Well Level Sentinel','Workshop Job Tokens',
 'Blackout Comms Mesh','Seed Vault Archive','Storm Drain Monitor','Community Fridge Ledger',
 'Idle Laptop Render Farm','Church Hall Scheduler','Park Tree Census','Beach Cleanup Ledger',
 'Greenhouse Climate Loop','Bike Share Balancer','Food Bank Inventory','Senior Check-In Net',
 'Playground Air Quality','Rooftop Garden Irrigation','Trail Camera Wildlife Log','Historic Photo Archive',
 'Tool Library Tokens','Repair Cafe Queue','Solar Co-op Dividends','Rain Barrel Network',
 'Compost Heat Tracker','Night Sky Light Audit','Pollinator Corridor Map','Flood Gauge Network',
 'Elder Meal Routes','Youth Code Sandbox','River Cleanup Crew','Wind Turbine Watch',
 'Battery Swap Station','E-Waste Collection','Textile Recycling Loop','Orchard Frost Guard',
 'Wetland Bird Survey','Alley Greening Project','Farmers Market Ledger','Heat Wave Check-In'
];
var TRACKING=[
 ['Token Ledger','every token ever minted','append-only hashed chain, anyone can verify'],
 ['MRV Verifier','measurement, reporting, verification','impact measured, reported, verified before any token issues'],
 ['Token Minter','token issuance','mints CO2/BIO/H2O/NRG/PROFIT only for verified work'],
 ['Network Aggregator','rollup across scales','deterministic aggregation leaf → relay → hub → planetary'],
 ['Identity Registry','quad-helix identities','name × signature × dna × legacy, one id per node'],
 ['Upgrade Evaluator','module candidates','sandbox-tests each candidate; only proven upgrades applied'],
 ['Impact Oracle','idle-hours to CO2 math','converts verified compute into carbon figures'],
 ['Green Exchange','token swap and valuation','live rates between the five token types'],
 ['Node Directory','live node registry','every active node, its scale, role, and heartbeat'],
 ['Audit Trail','verification history','human-readable log of every verification event'],
 ['Carbon Calculator','CO2 arithmetic','the math engine behind carbon tokens'],
 ['Biodiversity Index','species scoring','habitat scores from survey data'],
 ['Water Ledger','hydrology tracking','watershed flow and aquifer levels, tokenized'],
 ['Energy Forecaster','renewable output models','solar and wind forecasts per node'],
 ['Profit Distributor','profit payouts','routes PROFIT tokens to contributors'],
 ['Compliance Monitor','rules enforcement','idle-only, sandboxed, user-reclaimable — always'],
 ['Reputation Score','node trust','uptime and honesty ratings per node'],
 ['Dispute Resolver','verification challenges','handles contested verifications deterministically'],
 ['Archive Vault','permanent storage','checksummed, never silently lost'],
 ['API Gateway','external access','lets outside systems read the ledger'],
 ['Alert Engine','threshold alerts','pages humans before tanks run dry or grids overload'],
 ['Report Builder','impact reports','builds the one-page proof of impact'],
 ['Sync Protocol','cross-node state','conflict-free deterministic merges'],
 ['Genesis Registry','network bootstrap','the founding records of the network']
];
var ENV_DOMAINS=['carbon cycle','soil chemistry','hydrology','biodiversity','renewable energy'];
/* CO2 saving tools — PC/computer-focused, direct USER savings.
   [name, what it is, how it works, kWh/yr saved, $/yr saved, kg CO2/yr avoided] */
var SAVING_TOOLS=[
 ['Power Plan Optimizer','an auto power-profile switcher','drops the PC to low-power states the moment you stop typing',180,27,76],
 ['Idle CPU Harvester','an idle-cycle redirector','sends spare CPU to verified green work instead of spinning idle',220,33,92],
 ['Sleep Timer Enforcer','a strict sleep enforcer','forces sleep after 10 idle minutes, no exceptions',140,21,59],
 ['Monitor Dimmer','an ambient-aware dimmer','dims and sleeps displays based on room light and presence',90,14,38],
 ['Vampire Load Killer','a PC-controlled smart strip','cuts standby power to printer, speakers and chargers',110,17,46],
 ['Fan Curve Tuner','a smart fan controller','runs fans only as fast as thermals demand',45,7,19],
 ['SSD Migrator','an HDD-to-SSD upgrade guide','SSDs draw a fraction of spinning-disk power',60,9,25],
 ['Bloatware Remover','a background-app cleaner','kills vendor bloat eating CPU in the background',70,11,29],
 ['Update Scheduler','an off-peak update timer','patches and backs up only on clean-grid hours',40,6,17],
 ['Cloud Sync Throttler','a sync traffic shaper','batches uploads instead of trickling all day',35,5,15],
 ['E-Waste Refurbisher','a hardware life extender','refurb guides keep machines alive 3 extra years',300,120,210],
 ['Battery Health Guard','a charge limiter','caps charge at 80%, doubling battery lifespan',25,40,11],
 ['Thermal Repaster','a cooling restore guide','fresh thermal paste drops temps and fan power',30,5,13],
 ['RAM Optimizer','a memory pressure reliever','fewer page faults means less disk and CPU churn',20,3,8],
 ['Green Browser','a tab-throttling browser','freezes idle tabs instead of burning CPU on them',55,8,23],
 ['Dark Mode Enforcer','an OLED saver','dark pixels draw near-zero power on OLED screens',40,6,17],
 ['Peripheral Sleeper','a USB power manager','sleeps idle webcams, drives and hubs',25,4,11],
 ['NIC Power Saver','a network adapter tuner','drops the network chip to low-power between packets',15,2,6],
 ['VM Consolidator','a server combiner','packs five idle servers into one efficient host',2400,360,1008],
 ['Container Packer','a workload densifier','containers share one OS instead of five',900,135,378],
 ['Phone Repurposer','an old-phone server kit','turns a retired phone into a home server, no new hardware',120,90,84],
 ['Charger Reminder','an unplug nagger','reminds you to unplug full chargers',15,2,6],
 ['Efficient Codec Pack','a transcode optimizer','hardware-accelerated codecs slash encode energy',80,12,34],
 ['Carbon-Aware Scheduler','a grid-aware job runner','heavy jobs wait for the cleanest grid hour',160,24,67]
];

/* NON-PC methods — branching outward from the PC core.
   [name, category, how it works, tonnes CO2/yr] */
var NON_PC=[
 ['Enhanced Rock Weathering','weathering','spreading crushed basalt on fields pulls CO2 from the air as it weathers',4],
 ['Reforestation Project','reforestation','planting native trees on degraded land, verified per hectare',300],
 ['Direct Air Capture','direct-air-capture','fans plus filters pull CO2 straight from ambient air',1000],
 ['Soil Carbon Program','soil','cover crops and no-till build carbon in farmland soils',150],
 ['Ocean Alkalinity','ocean','adding alkaline minerals to seawater boosts CO2 uptake',500],
 ['Kelp Farming','ocean','farmed kelp absorbs CO2, then sinks or is harvested',80],
 ['Biochar Kilns','soil','pyrolyzed waste biomass locks carbon in soil for centuries',60],
 ['Wetland Restoration','wetland','rewetted peatlands stop emitting and resume storing carbon',200],
 ['Mangrove Planting','ocean','mangroves store 4x the carbon of rainforest per hectare',120],
 ['Agroforestry Rows','soil','trees between crops stack food and carbon on the same acre',90],
 ['Urban Tree Canopy','reforestation','street trees shade buildings and store carbon',40],
 ['Peatland Rewetting','wetland','blocking drainage ditches restores the carbon sink',180],
 ['Seagrass Meadows','ocean','restored seagrass beds bury carbon in marine soils',70],
 ['Mineral Carbonation','weathering','industrial CO2 reacted into solid carbonate rock',800],
 ['BECCS Plant','direct-air-capture','bioenergy with carbon capture, net-negative power',1200],
 ['Grassland Stewardship','soil','managed grazing rebuilds prairie root carbon',110],
 ['Bamboo Groves','reforestation','fast-growing bamboo harvested into durable goods',95],
 ['Algae Bioreactors','ocean','algae tubes convert flue CO2 into biomass',45],
 ['Charcoal Water Filters','soil','biochar filters that retire into farm soil',15],
 ['Living Shorelines','ocean','oyster reefs plus marsh grass buffer coasts and store carbon',55],
 ['Forest Fire Prevention','reforestation','thinning plus prescribed burns avoid megafire emissions',400],
 ['Mycelium Packaging','soil','mushroom packaging replaces foam, then composts',25],
 ['Salt Marsh Recovery','wetland','reconnected tidal flow restores blue carbon burial',85],
 ['Rock Dust Rail','weathering','rail-spread mineral dust over farmland corridors',350]
];
function tokensFor(s,idleHrs){
  var t={co2:+(idleHrs*0.42).toFixed(1),bio:ri(s,1,60),water:ri(s,10,900),energy:+(idleHrs*1.7).toFixed(1)};
  t.profit=+((t.co2*2.5+t.energy*0.8)).toFixed(2);
  return t;
}
function buildApp(s,seed,scen,scale,cx,leg,topic){
  var idleHrs=ri(s,4,400);
  var tokens=tokensFor(s,idleHrs);
  var domains=shuffle(s,ENV_DOMAINS).slice(0,ri(s,2,4));
  var nmod=ri(s,3,5), mods=[], used={}, i, m;
  for(i=0;i<nmod;i++){ m=pick(MODULES,s); if(!used[m[0]]){used[m[0]]=1;mods.push(m[1]);} }
  var title='Captain Planet: '+scen+' @ '+scale+' — '+leg+' leg'+(topic?' — '+topic:'');
  var desc='A green token (CO2) APPLICATION: "'+scen+'" ('+leg+' leg of the space-and-back arc) on '+SCALE_HW[scale]+' — '+cx+' complexity. How it earns: idle hardware becomes an environmental compute node (sandboxed, never touching the user), modeling '+domains.join(', ')+'. MRV verified '+idleHrs+' idle hours before minting: '+tokens.co2+' kg CO2, '+tokens.bio+' bio points, '+tokens.water+' L water, '+tokens.energy+' kWh renewable — profit $'+tokens.profit+'. Network role: '+SCALE_ROLE[scale]+'.'+(topic?' Focus: '+topic+'.':'');
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    title:title,
    description:desc,
    kind:'application',
    scale:scale,
    complexity:cx,
    leg:leg,
    application:{name:scen,does:'earns green tokens through verified environmental modeling',how_earned:'MRV-verified idle compute → tokens',hardware:SCALE_HW[scale]},
    tokens_generated:tokens,
    network_role:SCALE_ROLE[scale],
    systems:{modeling:domains,mrv:'verified '+idleHrs+' idle hours · additionality traced per token',upgrade:'candidates sandbox-tested · only proven upgrades applied',identity:'quad-helix qh-'+sha(scen+scale+seed),modules:mods},
    demo:{kind:'token-sandbox',
      program:'function sandboxCycle(idleHours){var t={co2:+(idleHours*0.42).toFixed(1),nrg:+(idleHours*1.7).toFixed(1)};t.profit=+((t.co2*2.5+t.nrg*0.8)).toFixed(2);return {verified_hours:idleHours,tokens:t};}\n// sandboxCycle(120) — deterministic: same input, same tokens.',
      note:'JS: paste into any console — mint tokens from verified idle hours.'},
    src:'signature',
    _seed:seed
  };
}
function buildTracking(s,seed,comp,scale,cx,leg){
  var idleHrs=ri(s,40,4000);
  var tokens=tokensFor(s,idleHrs);
  var title='Captain Planet Tracker: '+comp[0]+' @ '+scale+' — '+leg+' leg';
  var desc='A GRAND TRACKING SYSTEM component: the '+comp[0]+' ('+leg+' leg). What it tracks: '+comp[1]+'. How: '+comp[2]+'. Operating at '+scale+' scale ('+SCALE_HW[scale]+', '+cx+' complexity) as '+SCALE_ROLE[scale]+', it watches '+tokens.co2+' kg CO2-equivalent flow across '+ri(s,2,9000)+' tracked deployments. Every observation is ledger-recorded before any token moves.';
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    title:title,
    description:desc,
    kind:'tracking-system',
    scale:scale,
    complexity:cx,
    leg:leg,
    tracker:{component:comp[0],tracks:comp[1],method:comp[2]},
    tokens_watched:tokens,
    network_role:SCALE_ROLE[scale],
    systems:{mrv:'continuous verification stream',upgrade:'self-monitoring · upgrades ledger-recorded',identity:'quad-helix qh-'+sha(comp[0]+scale+seed),aggregation:'deterministic rollup to planetary'},
    demo:{kind:'tracker-probe',
      program:'function trackerProbe(component){return {component:component,status:"watching",ledger_tip:"sha:"+("0000000"+component.length.toString(16)).slice(-8)};}\n// trackerProbe("Token Ledger")',
      note:'JS: probe any tracking component.'},
    src:'signature',
    _seed:seed
  };
}
function buildSavingTool(s,seed,tool,scale,cx,leg,scope){
  var isPC = scope==='pc';
  var title='Captain Planet Saver: '+tool[0]+' @ '+scale+' — '+leg+' leg';
  var desc, savings, demoProg;
  if(isPC){
    var tokenVal=+(tool[5]*0.42/100).toFixed(1);
    desc='A CO2 SAVING TOOL (PC core): the '+tool[0]+' — '+tool[1]+' ('+leg+' leg). How it works: '+tool[2]+'. Direct USER savings: '+tool[3]+' kWh/yr, $'+tool[4]+'/yr, '+tool[5]+' kg CO2/yr avoided — at '+scale+' scale ('+cx+' complexity), worth about '+tokenVal+' CO2 tokens a year once MRV-verified.';
    savings={kwh_yr:tool[3],dollars_yr:tool[4],co2_kg_yr:tool[5],co2_tokens_per_yr:tokenVal};
    demoProg='function yearlySavings(kwh,price,co2){return {kwh:kwh,dollars:+(kwh*price).toFixed(2),co2_kg:co2,tokens:+(co2*0.42/100).toFixed(1)}};\n// yearlySavings('+tool[3]+',0.15,'+tool[5]+')';
  } else {
    desc='A CO2 SAVING TOOL (branched outward — '+tool[1]+'): '+tool[0]+' ('+leg+' leg). How it works: '+tool[2]+'. Removes roughly '+tool[3].toLocaleString()+' tonnes CO2/yr at '+scale+' scale ('+cx+' complexity). Beyond-PC method, tracked on the same ledger.';
    savings={co2_tonnes_yr:tool[3],note:'non-PC environmental method'};
    demoProg='function tonnesToTokens(tonnes){return +(tonnes*1000*0.42/100).toFixed(1);}\n// tonnesToTokens('+tool[3]+')';
  }
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    title:title,
    description:desc,
    kind:'saving-tool',
    method_scope:scope,
    non_pc_category:isPC?undefined:tool[1],
    scale:scale,
    complexity:cx,
    leg:leg,
    tool:{name:tool[0],what:isPC?tool[1]:tool[1]+' method',how_it_works:tool[2]},
    user_savings:savings,
    network_role:SCALE_ROLE[scale],
    demo:{kind:isPC?'savings-calc':'removal-calc',program:demoProg,note:'JS: project savings.'},
    src:'signature',
    _seed:seed
  };
}
function normScale(x){
  if(!x)return null;
  var t=String(x).toLowerCase().trim().replace(/[^a-z]+/g,'-').replace(/^-+|-+$/g,'');
  if(SCALES.indexOf(t)>=0)return t;
  if(t==='supercompany')return 'super-company';
  return null;
}
function normComplex(x){
  if(!x)return null;
  var t=String(x).toLowerCase().trim();
  if(COMPLEX.indexOf(t)>=0)return t;
  return null;
}
function arcFor(seed){
  var leg=seed<=150?'outbound':'return';
  var q=leg==='outbound'?(seed-1)/149:(seed-151)/149;
  var r=leg==='outbound'?q:1-q;
  var scaleIdx=Math.min(8,Math.round(r*8));
  return {leg:leg,scale:SCALES[scaleIdx],cx:COMPLEX[Math.min(3,Math.round(scaleIdx/8*3))]};
}
function generate(seed,opts){
  opts=opts||{};
  var s=prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120);
  var kind=opts.kind==='tracking-system'?'tracking-system':(opts.kind==='saving-tool'?'saving-tool':'application');
  var scale=normScale(opts.scale)||SCALES[(s()*SCALES.length)|0];
  var cx=normComplex(opts.complexity)||pick(COMPLEX,s);
  var leg=s()<0.5?'outbound':'return';
  if(kind==='tracking-system'){
    return buildTracking(s,seed,pick(TRACKING,s),scale,cx,leg);
  }
  if(kind==='saving-tool'){
    return buildSavingTool(s,seed,pick(SAVING_TOOLS,s),scale,cx,leg,'pc');
  }
  return buildApp(s,seed,pick(SCENARIOS,s),scale,cx,leg,topic||null);
}
function generateIndexed(seed){
  /* arc across 300 seeds; thirds: tracking / saving-tool / application */
  var s=prng(seed*7919+13);
  var a=arcFor(seed);
  var m3=seed%3;
  if(m3===0){
    var comp=TRACKING[(((seed/3)|0)-1)%TRACKING.length];
    return buildTracking(s,seed,comp,a.scale,a.cx,a.leg);
  }
  if(m3===1){
    var k6=((seed-1)/3)|0;
    if(k6%2===0){
      var tool=SAVING_TOOLS[(k6/2|0)%SAVING_TOOLS.length];
      return buildSavingTool(s,seed,tool,a.scale,a.cx,a.leg,'pc');
    }
    var npc=NON_PC[(((k6-1)/2)|0)%NON_PC.length];
    return buildSavingTool(s,seed,npc,a.scale,a.cx,a.leg,'non-pc');
  }
  var scen=SCENARIOS[(seed-1)%SCENARIOS.length];
  return buildApp(s,seed,scen,a.scale,a.cx,a.leg,null);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-CPCT-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<60)e.push('description');
  if(r.kind!=='application'&&r.kind!=='tracking-system'&&r.kind!=='saving-tool')e.push('kind');
  if(SCALES.indexOf(r.scale)<0)e.push('scale');
  if(COMPLEX.indexOf(r.complexity)<0)e.push('complexity');
  if(r.leg!=='outbound'&&r.leg!=='return')e.push('leg');
  if(r.kind==='application'&&!r.tokens_generated)e.push('tokens_generated');
  if(r.kind==='tracking-system'&&!r.tokens_watched)e.push('tokens_watched');
  if(r.kind==='saving-tool'){if(r.method_scope!=='pc'&&r.method_scope!=='non-pc')e.push('method_scope');if(!r.tool||!r.tool.name)e.push('tool');if(!r.user_savings)e.push('user_savings');}
  if(typeof r.network_role!=='string'||!r.network_role)e.push('network_role');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-captain-planet-1.0',generate:generate,generateIndexed:generateIndexed,validate:validate,driftCheck:driftCheck,scales:SCALES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('captain-planet-co2-token-trackers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
