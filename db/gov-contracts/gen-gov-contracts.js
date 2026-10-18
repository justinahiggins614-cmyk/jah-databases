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
  opts=opts||{};
  if(opts.family==='spending')return generateSpending(seed,opts,rnd);
  if(opts.family==='preaward')return generatePreaward(seed,opts,rnd);
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
  if(r.record_family==='spending'||r.record_family==='preaward')return validateFamily(r,e);
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
/* ============ EXPANSION 2026-10-17 (audit items 32+33) ============
   New record families: public budgets/spending (appropriations, expenditures,
   grants spending, performance) and pre-award procurement (solicitations,
   specifications, vendor requirements, deadlines). Opt-in via
   opts.family='spending'|'preaward'; existing award path untouched. */
var SPEND_KINDS=['appropriation','expenditure','grant-spending','performance'];
var PRE_KINDS=['solicitation','specification','vendor-requirement','deadline'];
var FY=[2022,2023,2024,2025,2026];
var SPEND_PURPOSES={appropriation:['operations and maintenance funding','capital improvement funding','program operations funding','facility sustainment funding','technology refresh funding','emergency reserve funding'],
 expenditure:['quarterly contract outlays','program disbursement tranche','operations expenditure batch','capital project drawdown','grant reimbursement payout','service delivery payment run'],
 'grant-spending':['community resilience grant round','research partnership grant cycle','workforce training grant awards','infrastructure matching grants','public health grant disbursement','small business support grants'],
 performance:['obligation rate review','spend-plan variance analysis','grant performance assessment','contract delivery scorecard','budget execution audit','program outcome evaluation']};
var SPEND_DESC={
 appropriation:'Congressional appropriation providing budget authority to the agency for the stated purpose. Funds are apportioned by quarter and obligated against contracts, grants, and interagency agreements; unobligated balances may carry forward subject to the terms of the appropriation language.',
 expenditure:'Recorded federal expenditure: an outlay against obligated budget authority. Each expenditure batch is reconciled to the agency financial system, matched to the originating award or grant, and reported in the agency\'s monthly budget execution review.',
 'grant-spending':'Federal grant spending under a published assistance program. Awards are made competitively or by formula, disbursed on a reimbursement or advance basis, and monitored for allowable costs, performance milestones, and single-audit compliance.',
 performance:'Performance review of budget execution: compares planned versus actual obligations and outlays, scores delivery timeliness and cost control, and flags variances for corrective action in the next quarterly spend plan.'};
var SOL_TOPICS=['nationwide facilities maintenance','cloud hosting consolidation','field communications refresh','flood barrier construction','telemedicine kit deployment','records digitization services'];
var SPEC_ITEMS=['statement of work and deliverables','technical specifications and standards','inspection and acceptance criteria','packaging and delivery instructions','warranty and support terms','security and compliance requirements'];
var VENDOR_REQS=['active SAM.gov registration with current representations','past performance references for comparable work','financial capability documentation','key personnel resumes and labor categories','small business subcontracting plan where applicable','cybersecurity maturity attestation for IT buys'];
function generateSpending(seed,opts,rnd){
  rnd=rnd||prng((opts&&opts.salt)?(seed^opts.salt):seed);
  var kind=(opts&&opts.kind&&SPEND_KINDS.indexOf(opts.kind)>=0)?opts.kind:pick(rnd,SPEND_KINDS);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var agency=pick(rnd,AGENCIES), fy=pick(rnd,FY);
  var purpose=pick(rnd,SPEND_PURPOSES[kind]);
  var amount=ri(rnd,1000000,900000000);
  var title='FY'+fy+' '+kind.charAt(0).toUpperCase()+kind.slice(1)+' — '+agency+': '+purpose;
  var desc='Public budget/spending record ('+kind+'). In fiscal year '+fy+', the '+agency+' recorded '+purpose+' totaling $'+amount.toLocaleString('en-US')+' in the '+cat+' portfolio. '+SPEND_DESC[kind];
  return {id:'JAH-GOV-'+pad(seed),record_family:'spending',record_kind:kind,
    agency:agency,title:title,fiscal_year:fy,amount_usd:amount,category:cat,
    country:pick(rnd,COUNTRIES),description:desc,
    source:'synthetic',creation_mode:'SIGNATURE-GENERATED'};
}
function generatePreaward(seed,opts,rnd){
  rnd=rnd||prng((opts&&opts.salt)?(seed^opts.salt):seed);
  var kind=(opts&&opts.kind&&PRE_KINDS.indexOf(opts.kind)>=0)?opts.kind:pick(rnd,PRE_KINDS);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var agency=pick(rnd,AGENCIES), topic=pick(rnd,SOL_TOPICS);
  var yr=ri(rnd,2024,2026), solId='SOL-'+yr+'-'+String(10000+(seed%89999));
  var issue=yr+'-'+String(ri(rnd,1,12)).padStart(2,'0')+'-'+String(ri(rnd,1,28)).padStart(2,'0');
  var dl=yr+'-'+String(ri(rnd,1,12)).padStart(2,'0')+'-'+String(ri(rnd,1,28)).padStart(2,'0');
  var title,desc;
  if(kind==='solicitation'){title='Solicitation '+solId+' — '+topic+' ('+agency+')';desc='Pre-award procurement notice: the '+agency+' solicits proposals for '+topic+' ('+cat+' portfolio). Solicitation '+solId+' issued '+issue+'; proposals due '+dl+'. Offerors must meet all instructions in Section L and will be evaluated under the stated Section M criteria.';}
  else if(kind==='specification'){var sp=pick(rnd,SPEC_ITEMS);title='Specification package '+solId+' — '+sp;desc='Pre-award specification record for '+topic+' at the '+agency+'. This package defines the '+sp+', including measurable acceptance thresholds, applicable standards, and the verification method the government will use before acceptance.';}
  else if(kind==='deadline'){title='Procurement deadline — '+solId+' proposals due '+dl;desc='Pre-award deadline record: proposals responding to '+agency+' solicitation '+solId+' ('+topic+') are due no later than '+dl+'. Late submissions are handled per the late-proposal rules stated in the solicitation; amendments may extend this date.';}
  else{var vr=pick(rnd,VENDOR_REQS);title='Vendor requirement — '+solId+': '+vr;desc='Pre-award vendor requirement for '+agency+' solicitation '+solId+' ('+topic+'). Requirement: '+vr+'. Failure to demonstrate compliance at time of award may render an offeror ineligible.';}
  return {id:'JAH-GOV-'+pad(seed),record_family:'preaward',record_kind:kind,
    agency:agency,title:title,solicitation_id:solId,issue_date:issue,deadline_date:dl,
    category:cat,country:pick(rnd,COUNTRIES),description:desc,
    source:'synthetic',creation_mode:'SIGNATURE-GENERATED'};
}
function validateFamily(r,e){
  if(r.record_family!=='spending'&&r.record_family!=='preaward')e.push('record_family');
  if(r.record_family==='spending'&&SPEND_KINDS.indexOf(r.record_kind)<0)e.push('record_kind');
  if(r.record_family==='preaward'&&PRE_KINDS.indexOf(r.record_kind)<0)e.push('record_kind');
  if(typeof r.agency!=='string'||!r.agency.length)e.push('agency');
  if(typeof r.title!=='string'||!r.title.length||r.title.length>200)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(r.record_family==='spending'){
    if(FY.indexOf(r.fiscal_year)<0)e.push('fiscal_year');
    if(typeof r.amount_usd!=='number'||r.amount_usd<=0)e.push('amount_usd');
  }else{
    if(typeof r.solicitation_id!=='string'||!/^SOL-\d{4}-\d{5}$/.test(r.solicitation_id))e.push('solicitation_id');
    if(typeof r.issue_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.issue_date))e.push('issue_date');
    if(typeof r.deadline_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.deadline_date))e.push('deadline_date');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-gov-contracts-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gov-contracts',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
