(function(){'use strict';
/* JAH The Cloud and Internet Things Signature Database generator — jahdb-cloud-internet-things-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CITS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Cloud Computing (Signature Edition) - Foundations",
  "The Internet: How Packets Travel (Signature Edition) - Foundations",
  "DNS: The Internet Phone Book (Signature Edition) - Foundations",
  "IP Addresses and Subnetting (Signature Edition) - Foundations",
  "HTTP and the Web Request (Signature Edition) - Foundations",
  "TLS and HTTPS: Encryption in Transit (Signature Edition) - Foundations",
  "Virtualization: One Machine, Many (Signature Edition) - Foundations",
  "Cloud Service Models: IaaS, PaaS, and SaaS (Signature Edition) - Foundations",
  "Cloud Deployment Models: Public, Private, and Hybrid (Signature Edition) - Foundations",
  "Data Centers, Regions, and Availability Zones (Signature Edition) - Foundations",
  "Cloud Storage: Object, File, and Block (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Containers and Container Images (Signature Edition) - Compounded",
  "Kubernetes: Container Orchestration (Signature Edition) - Compounded",
  "Load Balancers and Auto Scaling (Signature Edition) - Compounded",
  "Content Delivery Networks (Signature Edition) - Compounded",
  "Virtual Networks, Subnets, and Firewalls (Signature Edition) - Compounded",
  "Cloud Databases: Relational and NoSQL (Signature Edition) - Compounded",
  "Serverless Computing and Functions as a Service (Signature Edition) - Compounded",
  "Identity and Access Management in the Cloud (Signature Edition) - Compounded",
  "Message Queues and Event Streams (Signature Edition) - Compounded",
  "CI and CD: Cloud Deployment Pipelines (Signature Edition) - Compounded",
  "Caching: Redis and Memcached (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Edge Computing (Signature Edition) - Advanced",
  "IoT Connectivity: MQTT and Device Fleets (Signature Edition) - Advanced",
  "Cloud Security: The Shared Responsibility Model (Signature Edition) - Advanced",
  "DDoS Defense and Web Application Firewalls (Signature Edition) - Advanced",
  "Zero Trust Network Architecture (Signature Edition) - Advanced",
  "Multi-Cloud and Hybrid Architecture (Signature Edition) - Advanced",
  "Observability: Logs, Metrics, and Traces (Signature Edition) - Advanced",
  "Cloud Cost Engineering and FinOps (Signature Edition) - Advanced",
  "Disaster Recovery and Cloud Backups (Signature Edition) - Advanced",
  "Infrastructure as Code (Signature Edition) - Advanced",
  "Service Mesh (Signature Edition) - Advanced",
  "The Future Internet: IPv6, QUIC, and Beyond (Signature Edition) - Advanced"
 ]
};
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
var gen={version:'jahdb-cloud-internet-things-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cloud-internet-things-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
