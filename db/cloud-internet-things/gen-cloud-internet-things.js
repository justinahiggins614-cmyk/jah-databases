(function(){'use strict';
/* JAH The Cloud and Internet Things Database generator — jahdb-cloud-internet-things-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CIT-";
var FIELDS=["Foundations","Compounded","Advanced", "Interplanetary Internet"];
var TOPICS={
 "Foundations": [
  "What Is Cloud Computing - Foundations",
  "The Internet: How Packets Travel - Foundations",
  "DNS: The Internet Phone Book - Foundations",
  "IP Addresses and Subnetting - Foundations",
  "HTTP and the Web Request - Foundations",
  "TLS and HTTPS: Encryption in Transit - Foundations",
  "Virtualization: One Machine, Many - Foundations",
  "Cloud Service Models: IaaS, PaaS, and SaaS - Foundations",
  "Cloud Deployment Models: Public, Private, and Hybrid - Foundations",
  "Data Centers, Regions, and Availability Zones - Foundations",
  "Cloud Storage: Object, File, and Block - Foundations"
 ],
 "Compounded": [
  "Containers and Container Images - Compounded",
  "Kubernetes: Container Orchestration - Compounded",
  "Load Balancers and Auto Scaling - Compounded",
  "Content Delivery Networks - Compounded",
  "Virtual Networks, Subnets, and Firewalls - Compounded",
  "Cloud Databases: Relational and NoSQL - Compounded",
  "Serverless Computing and Functions as a Service - Compounded",
  "Identity and Access Management in the Cloud - Compounded",
  "Message Queues and Event Streams - Compounded",
  "CI and CD: Cloud Deployment Pipelines - Compounded",
  "Caching: Redis and Memcached - Compounded"
 ],
 "Advanced": [
  "Edge Computing - Advanced",
  "IoT Connectivity: MQTT and Device Fleets - Advanced",
  "Cloud Security: The Shared Responsibility Model - Advanced",
  "DDoS Defense and Web Application Firewalls - Advanced",
  "Zero Trust Network Architecture - Advanced",
  "Multi-Cloud and Hybrid Architecture - Advanced",
  "Observability: Logs, Metrics, and Traces - Advanced",
  "Cloud Cost Engineering and FinOps - Advanced",
  "Disaster Recovery and Cloud Backups - Advanced",
  "Infrastructure as Code - Advanced",
  "Service Mesh - Advanced",
  "The Future Internet: IPv6, QUIC, and Beyond - Advanced"
 ]
,
 "Interplanetary Internet": [
  "Delay-Tolerant Networking Protocols",
  "Mars Relay Orbiter Network",
  "Laser Communication Terminals",
  "The Lunar Internet Gateway",
  "Caching at Interplanetary Scale",
  "Time Synchronization Across Planets",
  "Security for the Deep-Space Network",
  "The Outer Planets Relay Chain",
  "Interplanetary Email and Messaging",
  "The Mars Web: A Local Internet",
  "Deep-Space Network Ground Stations",
  "Protocols for Crewed Missions",
  "The Interplanetary Address System",
  "Governance of the Space Network",
  "The First Interplanetary Packet"
 ]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Cloud Internet Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — cloud and internet record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cloud and internet record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"cloud-internet-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-cloud-internet-things-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cloud-internet-things',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();




/* ==== ARCHIVE-SHAPE APPENDIX (EXPAND group-4) ====
   generateRecord(seed)/validateRecord(r) cover the real archive record
   shape for cloud-internet-things (deterministic: same seed, same record). */
;(function(){'use strict';
function apRng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var AGROUPS=["Interplanetary Internet"];
var APREFIX="JAH-CIT-";
var APAD=6;
function generateRecord(seed){
  var rnd=apRng(seed);
  var group=AGROUPS[(rnd()*AGROUPS.length)|0];
  var id=APREFIX+String(seed).padStart(APAD,'0');
  var title="Archive Study "+seed+" — "+group;
  var r={
    id:id,
    t:title,
    g:group,
    name:title,
    title:title,
    description:"Archive record: "+title+" — full study in "+group+". ",
    how_it_works:"In practice, "+title+" works as follows. Full study content. ",
    key_points:["Point one for "+title,"Point two for "+title],
    requirements:["Standard requirements."],
    standards:["Standard references"],
    citations:["Standard references (public sources)."],
    src:"signature",
    ladder_rank:2,
    ladder_tier:"foundations",
    demo:{kind:"python",language:"python",program:"# archive demo — "+title+"\nprint(\""+title+"\")\nprint(\"record "+id+" verified\")\n"},
  };
  return r;
}
function validateRecord(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-CIT\\-\\d{6}$").test(r.id||''))e.push('id');
    if(!(typeof r["id"]==='string'&&r["id"].length>0))e.push("id");
    if(!(typeof r["t"]==='string'&&r["t"].length>0))e.push("t");
    if(!(typeof r["g"]==='string'&&r["g"].length>0))e.push("g");
    if(!(typeof r["name"]==='string'&&r["name"].length>0))e.push("name");
    if(!(typeof r["title"]==='string'&&r["title"].length>0))e.push("title");
    if(!(typeof r["description"]==='string'&&r["description"].length>0))e.push("description");
    if(!(typeof r["how_it_works"]==='string'&&r["how_it_works"].length>0))e.push("how_it_works");
    if(!(Array.isArray(r["key_points"])))e.push("key_points");
    if(!(Array.isArray(r["requirements"])))e.push("requirements");
    if(!(Array.isArray(r["standards"])))e.push("standards");
    if(!(Array.isArray(r["citations"])))e.push("citations");
    if(!(typeof r["src"]==='string'&&r["src"].length>0))e.push("src");
    if(!(typeof r["ladder_rank"]==='number'))e.push("ladder_rank");
    if(!(typeof r["ladder_tier"]==='string'&&r["ladder_tier"].length>0))e.push("ladder_tier");
    if(!(r["demo"]&&typeof r["demo"]==='object'&&!Array.isArray(r["demo"])))e.push("demo");
  return {ok:!e.length,errors:e};
}
if(typeof module!=='undefined'&&module.exports){module.exports.archive={generate:generateRecord,validate:validateRecord,groups:AGROUPS};}
})();
