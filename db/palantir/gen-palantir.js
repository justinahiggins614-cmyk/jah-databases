(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='palantir';
var VERSION='jahdb-palantir-1.0';
var PREFIX='JAH-PLTR-';
var SHIFT=4;
var CATS=["data-platforms", "ai-platform", "defense-ops", "commercial-ops", "deployment"];
var CATLBL={"data-platforms": "data platform", "ai-platform": "AI platform", "defense-ops": "defense operations", "commercial-ops": "commercial operations", "deployment": "deployment system"};
var DOMAIN="data and AI platforms";
var W1=["Apex", "Meridian", "Vanguard", "Quantum", "Nova", "Zenith", "Atlas", "Beacon", "Cipher", "Delta", "Ember", "Flux", "Granite", "Halcyon", "Ion", "Kepler", "Lumen", "Matrix", "Nebula", "Onyx", "Prism", "Quasar", "Ridgeline", "Sable", "Titan", "Umbra", "Vector", "Willow", "Xenon", "Zephyr", "Aurora", "Blaze", "Cinder", "Drift", "Echo", "Falcon", "Glacier", "Harbor", "Ivory", "Juniper", "Krypton", "Lotus", "Mesa", "Nimbus", "Obsidian", "Pinnacle", "Quartz", "Raven", "Summit", "Tundra", "Vesper", "Warden", "Yonder", "Zinc", "Amber", "Brisk", "Cobalt", "Dune", "Elm", "Fern", "Grove", "Halo", "Indigo", "Jasper", "Kite", "Lark", "Maple", "Northstar", "Opal", "Peregrine", "Quill", "Rook", "Slate", "Thistle", "Union", "Vireo", "Wren", "Alder", "Birch", "Cedar", "Dawn", "Eagle", "Flint", "Gale", "Heath", "Iris", "Jade", "Kestrel", "Lynx", "Moss", "Nomad", "Orion", "Pioneer", "Solstice", "Talon", "Ursa", "Vale", "Wisp", "Ozone", "Tempo"];var W2=["Cruiser", "Runner", "Forge", "Works", "Line", "Systems", "Craft", "Engine", "Prime", "Core", "Wing", "Shield", "Bridge", "Scope", "Drive", "Path", "Mark", "Strider", "Sentinel", "Sparrow", "Anchor", "Furnace", "Lathe", "Anvil", "Compass", "Turbine", "Piston", "Gear", "Rotor", "Lantern", "Spire", "Arch", "Pillar", "Buttress", "Dome", "Vault", "Atrium", "Plaza", "Terrace", "Colonnade", "Port", "Jetty", "Dock", "Pier", "Quay", "Marina", "Channel", "Strait", "Estuary", "Meadow", "Prairie", "Savanna", "Steppe", "Fjord", "Canyon", "Basin", "Plateau", "Icefield", "Comet", "Meteor", "Corona", "Eclipse", "Supernova", "Pulsar", "Galaxy", "Orbit", "Apogee", "Dynamo", "Relay", "Circuit", "Array", "Module", "Console", "Terminal", "Tensor", "Lattice", "Grid", "Foundry", "Crucible", "Kiln", "Smelter", "Refinery", "Mill", "Press", "Die", "Cast", "Mold", "Scepter", "Crown", "Throne", "Standard", "Banner", "Pennant", "Emblem", "Insignia", "Medal", "Laurel", "Sentry", "Rampart", "Citadel"];var W3=["Platform", "Station", "Suite", "Unit", "Array", "Module", "Console", "Hub", "Node", "Gate", "Series", "Edition", "Family", "Generation", "Heritage", "Legacy", "Vintage", "Classic", "Modern", "Future", "Select", "One", "Duo", "Trio", "Quad", "Penta", "Hexa", "Septa", "Octa", "Nona", "Deca", "Alpha", "Beta", "Gamma", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega", "Mark", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "Elite", "Pro", "Max", "Ultra", "Turbo", "Super", "Hyper", "Mega", "Giga", "Tera", "Aero", "Auto", "Agro", "Naval", "Terra", "Stellar", "Lunar", "Solar", "Polar", "Equatorial", "Sprint", "Marathon", "Relay", "Dash", "Bolt", "Flash", "Surge", "Wave", "Tide", "Current", "Crest", "Peak", "Vertex", "Coronet", "Regalia"];
var CLASS1=[["Gotham", "defense-ops", 2008, {"role": "intelligence analysis", "data": "entity graph", "users": "defense / intel"}, "Gotham, released in 2008, is the original defense and intelligence analysis platform built on linked entity data."], ["Foundry", "data-platforms", 2016, {"role": "data operations", "core": "ontology", "users": "commercial / government"}, "Foundry, launched in 2016, is the enterprise data platform organized around the Ontology."], ["Apollo", "deployment", 2016, {"role": "continuous delivery", "environments": "any, incl. air-gapped", "scope": "all platforms"}, "Apollo, from 2016, continuously delivers Palantir software to any environment, including air-gapped networks."], ["AIP", "ai-platform", 2023, {"role": "AI platform", "models": "LLM-connected", "launched": "2023"}, "The Artificial Intelligence Platform, launched in 2023, connects large language models to customer ontologies."], ["AIP Logic", "ai-platform", 2023, {"role": "AI logic builder", "interface": "no-code", "runs on": "AIP"}, "AIP Logic, from 2023, lets users build AI logic without code on the platform."], ["Agent Studio", "ai-platform", 2024, {"role": "agent builder", "output": "AI agents", "runs on": "AIP"}, "Agent Studio, from 2024, builds AI agents on enterprise data."], ["AIP Evals", "ai-platform", 2024, {"role": "AI evaluation", "function": "automated testing", "runs on": "AIP"}, "AIP Evals, from 2024, automatically tests AI logic for reliability."], ["AIP Agents", "ai-platform", 2024, {"role": "autonomous agents", "guardrails": "human-approved", "runs on": "AIP"}, "AIP Agents execute workflows autonomously within human-approved guardrails."], ["Foundry Ontology", "data-platforms", 2016, {"role": "data model", "features": "write-back, access control", "core": "Foundry"}, "The Foundry Ontology models an organization's world with governed, write-back objects."], ["Pipeline Builder", "data-platforms", 2017, {"role": "data pipelines", "interface": "visual", "runs on": "Foundry"}, "Pipeline Builder, from 2017, builds data pipelines visually on Foundry."], ["Code Workspaces", "data-platforms", 2018, {"role": "notebooks", "languages": "Python, SQL", "runs on": "Foundry"}, "Code Workspaces, from 2018, bring notebooks and code to Foundry data."], ["Contour", "data-platforms", 2015, {"role": "analysis", "interface": "visual", "runs on": "Foundry"}, "Contour, from 2015, is the visual analysis path builder on Foundry."], ["Workshop", "data-platforms", 2019, {"role": "operational apps", "interface": "drag-and-drop", "runs on": "Foundry"}, "Workshop, from 2019, builds operational applications on the Ontology."], ["Slate", "data-platforms", 2016, {"role": "data integration", "interface": "visual", "runs on": "Foundry"}, "Slate, from 2016, integrates and transforms data visually."], ["Quiver", "data-platforms", 2017, {"role": "time series", "interface": "visual", "runs on": "Foundry"}, "Quiver, from 2017, analyzes time-series data visually on Foundry."], ["Maven Smart System", "defense-ops", 2024, {"role": "AI targeting support", "data": "multi-source", "users": "defense"}, "The Maven Smart System, from 2024, fuses multi-source data for defense AI workflows."], ["TITAN", "defense-ops", 2024, {"role": "ground station", "data": "space / intel feeds", "users": "Army"}, "TITAN ground stations, from 2024, bring space and intelligence data to Army units."], ["Skykit", "defense-ops", 2022, {"role": "mission manager", "form": "portable", "users": "tactical"}, "Skykit, from 2022, is the portable mission manager for tactical edge users."], ["MetaConstellation", "commercial-ops", 2021, {"role": "satellite data", "data": "commercial imagery", "runs on": "Foundry"}, "MetaConstellation, from 2021, orchestrates commercial satellite tasking and data."], ["Bootcamp", "commercial-ops", 2023, {"role": "deployment program", "length": "days", "output": "working AI apps"}, "The Bootcamp program, from 2023, stands up working AI applications with customers in days."], ["Warp Speed", "commercial-ops", 2024, {"role": "manufacturing OS", "industry": "industrial", "runs on": "Foundry"}, "Warp Speed, from 2024, is the manufacturing operating system on Foundry."], ["Apollo Edge", "deployment", 2020, {"role": "edge delivery", "environments": "tactical edge", "scope": "disconnected"}, "Apollo edge delivery pushes software to disconnected tactical environments."], ["FedStart", "deployment", 2022, {"role": "compliance", "standard": "FedRAMP", "scope": "federal cloud"}, "FedStart, from 2022, accelerates federal compliance for Palantir cloud offerings."]];
var SPECGEN={"data-platforms": [["capability", ["pick", ["ontology", "pipelines", "dashboards", "notebooks", "data integration"]]], ["deployment", ["pick", ["cloud", "on-premises", "classified", "edge"]]]], "ai-platform": [["capability", ["pick", ["LLM agents", "evals", "copilots", "workflow automation", "prompt governance"]]], ["models", ["pick", ["bring your own model", "managed models", "open models"]]]], "defense-ops": [["mission", ["pick", ["intelligence fusion", "targeting", "logistics", "command and control", "ISR"]]], ["network", ["pick", ["classified", "tactical edge", "coalition"]]]], "commercial-ops": [["industry", ["pick", ["manufacturing", "healthcare", "energy", "finance", "aviation"]]], ["use", ["pick", ["supply chain", "digital twin", "operations", "maintenance"]]]], "deployment": [["environment", ["pick", ["air-gapped", "commercial cloud", "hybrid", "tactical edge"]]], ["update", ["pick", ["continuous", "scheduled", "on-demand"]]]]};
var T1="{name} is a Class 2 {cat} entry in the Signature archive, a future-facing {domain} concept built to extend the lineup toward {year}.";var T2="Its archived specification calls for {specs}.";var T3="Every value is produced deterministically from the record seed, so this entry rebuilds byte-for-byte from the generator at any time.";var T4="It is filed in the {cat} group of the archive, one of the boundless Class 2 concepts marching toward the million-record target.";
var C1T1="The {name} is this archive's Signature-line edition of the real-world {cat} product known as {alludes_to}.";var C1T3="Specifications on file: {specs}.";
function sigName(n){var a=((n/10000)|0)%100;var b=(((n/100)|0)+SHIFT)%100;var c=(n+SHIFT*3)%100;return W1[a]+' '+W2[b]+' '+W3[c];}
function catLabel(c){return CATLBL[c]||c;}
function sub(t,m){return String(t).replace(/\{(\w+)\}/g,function(_,k){return m[k];});}
function specPhrase(specs){return Object.keys(specs).map(function(k){return k+': '+specs[k];}).join('; ');}
function mkId(n){return PREFIX+String(n+1).padStart(6,'0');}
function genClass1(n){
  var e=CLASS1[n],name=sigName(n);
  return {id:mkId(n),signature_name:name,alludes_to:e[0],'class':1,category:e[1],specs:e[3],
    description:sub(C1T1,{name:name,cat:catLabel(e[1]),alludes_to:e[0]})+' '+e[4]+' '+sub(C1T3,{specs:specPhrase(e[3])}),
    year:e[2]};
}
function genClass2(n,forceCat){
  var rnd=prng(n);
  var cat=forceCat||CATS[(n*7+SHIFT)%CATS.length];
  var name=sigName(n);
  var sg=SPECGEN[cat]||[],specs={},i,k,kind;
  for(i=0;i<sg.length;i++){k=sg[i][0];kind=sg[i][1];
    if(kind[0]==='pick'){specs[k]=kind[1][(rnd()*kind[1].length)|0];}
    else{specs[k]=(kind[1][0]+((rnd()*(kind[1][1]-kind[1][0]+1))|0))+' '+kind[1][2];}}
  var year=2027+((rnd()*9)|0);
  var tail=(n%2===0)?T3:sub(T4,{cat:catLabel(cat)});
  var desc=sub(T1,{name:name,cat:catLabel(cat),domain:DOMAIN,year:String(year)})+' '+sub(T2,{specs:specPhrase(specs)})+' '+tail;
  return {id:mkId(n),signature_name:name,alludes_to:'','class':2,category:cat,specs:specs,description:desc,year:year};
}
function generate(seed,opts){
  opts=opts||{};
  var s=parseInt(seed,10);if(isNaN(s)||s<1)s=1;if(s>1000000)s=1000000;
  var n=s-1,rec,fc=null;
  if(opts.category&&CATS.indexOf(opts.category)>=0)fc=opts.category;
  if(opts['class']===1||(opts['class']!==2&&n<CLASS1.length))rec=genClass1(n);
  else rec=genClass2(n,fc);
  rec._seed=s;rec._gen_version=VERSION;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.signature_name!=='string'||!r.signature_name.length)e.push('signature_name');
  if(typeof r.alludes_to!=='string')e.push('alludes_to');
  if(r['class']!==1&&r['class']!==2)e.push('class');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!r.specs||typeof r.specs!=='object'||Array.isArray(r.specs)||!Object.keys(r.specs).length)e.push('specs');
  else Object.keys(r.specs).forEach(function(k){if(typeof r.specs[k]!=='string'||!r.specs[k].length)e.push('specs.'+k);});
  if(typeof r.description!=='string')e.push('description');
  else{var parts=r.description.split(/(?<=[.!?])\s+/).filter(function(p){return p.trim().length>0;});if(parts.length<2)e.push('description-sentences');}
  if(typeof r.year!=='number'||r.year<1800||r.year>2040)e.push('year');
  if(r['class']===1&&!r.alludes_to.length)e.push('alludes_to-empty');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];(sample||[]).forEach(function(s){if(s&&s.id===rec.id)e.push('duplicate-id');});
  return{ok:!e.length,errors:e};
}
var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
