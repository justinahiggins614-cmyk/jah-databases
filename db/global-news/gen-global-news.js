(function(){'use strict';
/* JAH Global News Database generator — jahdb-global-news-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record.
   SEED-COUNT RULE: seeds must exceed the seeded archive count (60), so generated
   sample IDs never collide with archive records JAH-NEWS-000001..000060. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-NEWS-';
var ARCHIVE_COUNT=60;
var CATEGORIES=["politics","science","technology","health","environment","economy","sports","culture"];
var REGIONS=["North America","Europe","Asia","Africa","Latin America","Middle East","Oceania","Global"];
var SAMPLE_TOPICS={
 "politics":["Summit Communiqué Study","Election Cycle Briefing","Treaty Review Exercise","Diplomatic Cable Drill"],
 "science":["Breakthrough Summary Drill","Peer Review Exercise","Lab Notebook Study","Field Observation Briefing"],
 "technology":["Product Launch Drill","Protocol Review Exercise","Infrastructure Study","Security Advisory Briefing"],
 "health":["Trial Results Drill","Public Health Briefing","Clinical Guideline Study","Outbreak Response Exercise"],
 "environment":["Storm Track Drill","Climate Data Study","Conservation Briefing","Disaster Response Exercise"],
 "economy":["Markets Recap Drill","Trade Policy Study","Central Bank Briefing","Jobs Report Exercise"],
 "sports":["Match Report Drill","Tournament Bracket Study","Season Preview Briefing","Record Chase Exercise"],
 "culture":["Festival Preview Drill","Release Calendar Study","Exhibition Briefing","Performance Review Exercise"]
};
/* ============ EXPANSION 2026-10-17 (audit item 45) ============
   Operational-status dashboards and service-interruption timelines.
   Generated samples, clearly labeled like the existing sample path;
   opt-in via opts.family='status'. Seed-count rule preserved (seed>60). */
var STATUS_SERVICES=[['Meridian Cloud','us-east region'],['BlueLine Payments','card processing network'],['NorthStar DNS','global anycast DNS'],['Harbor CDN','content delivery edge'],['Civic Transit API','real-time arrivals feed'],['Apex Mobile Network','voice and data core'],['Summit Power Grid','regional transmission'],['Clearwater Water Telemetry','sensor uplink network']];
var STATUS_LEVELS=['operational','degraded','partial outage','major outage','maintenance'];
var STATUS_TIMELINES={
 'operational':['All systems nominal; routine monitoring continues.'],
 'degraded':['09:12 UTC — elevated error rates detected on edge nodes.','09:40 UTC — traffic shifted to healthy capacity; errors declining.','10:05 UTC — error rates back within normal bounds; monitoring.'],
 'partial outage':['08:02 UTC — partial service disruption detected in one region.','08:25 UTC — incident declared; failover to secondary region underway.','09:50 UTC — service restored for most customers; residual queue draining.','10:30 UTC — fully recovered; post-incident review scheduled.'],
 'major outage':['07:15 UTC — major service interruption detected across regions.','07:40 UTC — all-hands incident response activated.','09:20 UTC — root cause isolated to a faulty configuration rollout.','10:45 UTC — rollback complete; service recovering progressively.','12:00 UTC — service fully restored; public postmortem to follow.'],
 'maintenance':['Scheduled maintenance window announced 72 hours in advance.','Maintenance completed within the announced window.','No customer impact observed; verification checks passed.']};
function statusDemoProgram(seed,service,status,timeline){
  var payload=JSON.stringify({headline:'STATUS SAMPLE (seed '+seed+')',service:service,status:status,timeline:timeline,note:'Generated sample — not an archive record'});
  return '// Service Status — SAMPLE (seed '+seed+')\n'
   + '// Not an archive record. Seeded archive records are authoritative.\n'
   + 'var rec = '+payload+';\n'
   + 'function statusBoard(r){\n'
   + '  var out=["=== SERVICE STATUS ===","Service: "+r.service,"Status: "+r.status,"","Timeline:"];\n'
   + '  r.timeline.forEach(function(e,i){ out.push("  "+(i+1)+". "+e); });\n'
   + '  out.push("",r.note);\n'
   + '  return out.join("\\n");\n'
   + '}\n'
   + 'console.log(statusBoard(rec));\n';
}
function generateStatus(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  seed=parseInt(seed,10)||1;
  var sv=STATUS_SERVICES[(seed-61)%STATUS_SERVICES.length];
  var service=sv[0], scope=sv[1];
  var status=(opts.status&&STATUS_LEVELS.indexOf(opts.status)>=0)?opts.status:STATUS_LEVELS[(seed-61)%STATUS_LEVELS.length];
  var region=opts.region&&REGIONS.indexOf(opts.region)>=0?opts.region:pick(REGIONS,rnd);
  var timeline=STATUS_TIMELINES[status].slice();
  var id=PREFIX+String(seed).padStart(6,'0');
  var day=String(1+((seed*7)%28)).padStart(2,'0');
  return {
    id:id,
    name:'STATUS — '+service+' ('+status+')',
    title:'STATUS — '+service+': '+status,
    description:'GENERATED SAMPLE (operational status record). '+service+' ('+scope+') reported status "'+status+'" in the '+region+' region. Timeline: '+timeline.join(' ')+' Generated samples are clearly labeled and never presented as archive records.',
    date:'2026-10-'+day,
    source_name:'Generated sample — not an archive record',
    source_url:'',
    region:region,
    category:'status',
    g:'status',
    key_facts:timeline.slice(),
    citation:'Generated sample — no external source.',
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'status-board',language:'javascript',program:statusDemoProgram(seed,service,status,timeline),note:'Structural sample demo.'},
    _seed:seed
  };
}
CATEGORIES.push('status');
function demoProgram(seed,category,region){
  var payload=JSON.stringify({headline:"SAMPLE NEWS BRIEF (seed "+seed+")",date:"—",region:region,category:category,source:"Generated sample — not an archive record",sourceUrl:"",facts:["Structural sample only.","Seeded archive records are the authoritative entries."]});
  return "// News Brief — SAMPLE (seed "+seed+", "+category+"/"+region+")\n"
   + "// Not an archive record. Seeded archive records are authoritative.\n"
   + "var rec = "+payload+";\n"
   + "function newsBrief(r){\n"
   + "  var out=['=== NEWS BRIEF ===','Headline: '+r.headline,'Date: '+r.date+' | Region: '+r.region+' | Category: '+r.category,'','Key facts:'];\n"
   + "  r.facts.forEach(function(f,i){ out.push('  '+(i+1)+'. '+f); });\n"
   + "  out.push('','Read the original: '+r.source);\n"
   + "  return out.join('\\n');\n"
   + "}\n"
   + "console.log(newsBrief(rec));\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  if(opts.family==='status')return generateStatus(seed,opts,rnd);
  seed=parseInt(seed,10)||1;
  var category=opts.category&&CATEGORIES.indexOf(opts.category)>=0?opts.category:pick(CATEGORIES,rnd);
  var region=opts.region&&REGIONS.indexOf(opts.region)>=0?opts.region:pick(REGIONS,rnd);
  var topic=pick(SAMPLE_TOPICS[category]||["General Study"],rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:'SAMPLE — '+topic+' ('+category+')',
    title:'SAMPLE — '+topic,
    description:'SAMPLE RECORD (generated — structural sample). A news-brief study of "'+topic+'" in '+category+' ('+region+'). Generated samples are clearly labeled and never presented as archive records.',
    date:'—',
    source_name:'Generated sample — not an archive record',
    source_url:'',
    region:region,
    category:category,
    g:category,
    key_facts:['Structural sample only.','Seeded archive records are the authoritative entries.'],
    citation:'Generated sample — no external source.',
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'news-brief',language:'javascript',program:demoProgram(seed,category,region),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-NEWS-\d{6}$/.test(r.id||''))e.push('id');
  var seedNum=parseInt(String(r.id||'').slice(9),10)||0;
  if(!(seedNum>ARCHIVE_COUNT))e.push('seed-count-rule (seed must exceed archive count '+ARCHIVE_COUNT+')');
  if(CATEGORIES.indexOf(r.category)<0)e.push('category');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.category===record.category;});
  return dups.length?{ok:false,errors:['duplicate topic+category in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-global-news-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:CATEGORIES,regions:REGIONS,archiveCount:ARCHIVE_COUNT};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('global-news',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
