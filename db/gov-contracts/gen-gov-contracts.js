/* ✳ JAH Government Contract Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) contract award generator: jahdb-gov-contracts-1.0.
   All agencies, companies and awards are synthetically generated. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['defense','it','construction','healthcare','research','services'];
var AGENCIES=['Department of Civic Works','National Infrastructure Bureau','Federal Health Services Authority','Defense Logistics Office','Bureau of Public Technology','National Research Grants Office','Department of Transportation Safety','Environmental Protection Directorate','Office of Emergency Management','National Energy Regulatory Board'];
var COMP1=['Apex','Meridian','Blue','Summit','Corner','Iron','Liberty','North','Quantum','Pioneer','Red','Silver','True','United','Vantage'];
var COMP2=['Systems','Solutions','Industries','Technologies','Services','Group','Works','Dynamics','Associates','Partners'];
var COUNTRIES=['United States','Canada','United Kingdom','Australia','Germany'];
var REGIONS=['Northeast','Southeast','Midwest','Southwest','Northwest','Central','Pacific','Atlantic'];

var TITLE_T=[
'Procurement of {i} for {p}',
'{s} Support Services — {r} Region',
'{i} Modernization Program, Phase {n}',
'Supply and Maintenance Contract: {i}',
'{p} Infrastructure Upgrade: {r} Corridor',
'Advisory Services for {p} Operations',
'{i} Lifecycle Replacement Program',
'Turnkey Delivery of {i} for {a} Facilities'
];
var ITEMS={defense:['radar components','field communications kits','logistics vehicles','protective systems'],it:['server clusters','cybersecurity tooling','cloud migration services','network hardware'],construction:['bridge steel','roadway aggregates','modular housing units','water treatment plants'],healthcare:['imaging equipment','clinic furnishings','cold-chain units','telemedicine kits'],research:['lab instrumentation','survey equipment','compute time grants','sensor arrays'],services:['facilities maintenance','fleet operations','records digitization','call center operations']};
var PURPOSES={defense:['readiness operations','training exercises','base support'],it:['digital services','data center consolidation','citizen portals'],construction:['public works','transit expansion','flood mitigation'],healthcare:['rural clinics','veterans care','public health response'],research:['climate monitoring','materials science','public health studies'],services:['agency operations','field offices','disaster response']};

function isoDate(rnd){
  var y=ri(rnd,2020,2026),mo=ri(rnd,1,12),d=ri(rnd,1,28);
  function z(n){return (n<10?'0':'')+n;}
  return y+'-'+z(mo)+'-'+z(d);
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var agency=pick(rnd,AGENCIES);
  var company=pick(rnd,COMP1)+' '+pick(rnd,COMP2);
  var title=pick(rnd,TITLE_T)
    .replace('{i}',pick(rnd,ITEMS[cat]))
    .replace('{p}',pick(rnd,PURPOSES[cat]))
    .replace('{r}',pick(rnd,REGIONS))
    .replace('{s}',pick(rnd,['Technical','Operational','Logistics','Advisory']))
    .replace('{n}',String(ri(rnd,1,4)))
    .replace('{a}',agency.split(' ').slice(-1)[0]);
  var year=ri(rnd,2020,2026);
  var value=ri(rnd,50000,500000000);
  return {
    id:'JAH-GOV-'+pad(seed),
    contract_id:'GS-'+year+'-'+String(10000+(seed%89999)),
    agency:agency,
    title:title,
    award_date:isoDate(rnd),
    winner:company,
    value_usd:value,
    category:cat,
    country:pick(rnd,COUNTRIES)
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-GOV-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.contract_id!=='string'||!/^GS-\d{4}-\d{5}$/.test(r.contract_id))e.push('contract_id');
  if(typeof r.agency!=='string'||!r.agency.length)e.push('agency');
  if(typeof r.title!=='string'||!r.title.length||r.title.length>160)e.push('title');
  if(typeof r.award_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.award_date))e.push('award_date');
  if(typeof r.winner!=='string'||!r.winner.length)e.push('winner');
  if(typeof r.value_usd!=='number'||r.value_usd<=0)e.push('value_usd');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.country!=='string'||!r.country.length)e.push('country');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-gov-contracts-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gov-contracts',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
