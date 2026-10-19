(function(){'use strict';
/* JAH Industrial Control Security Database generator — jahdb-industrial-control-security-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ICS-";
var FIELDS=["OT networks", "PLCs", "segmentation", "monitoring", "incident response", "safety"];
var TOPICS=[
    {t: "IT vs OT", b: "Confidentiality-first vs availability-first: the culture clash every industrial security program navigates."},
    {t: "The Purdue Model", b: "Levels 0\u20135 from sensors to enterprise: the reference architecture for segmenting plant networks."},
    {t: "PLCs and RTUs", b: "The controllers running processes: legacy protocols (Modbus, DNP3), hardcoded credentials, and 20-year lifespans."},
    {t: "Network Segmentation", b: "Conduits, zones (ISA/IEC 62443), data diodes, and firewalls: containing breaches to single process areas."},
    {t: "Passive Monitoring", b: "IDS that listens without touching: Nozomi/Claroty-class visibility into protocols IT tools can't parse."},
    {t: "Patching in OT", b: "Test beds, vendor qualification, and maintenance windows: the careful choreography of updating what can't go down."},
    {t: "Incident Response", b: "Isolating without tripping the plant: OT-specific playbooks, backups of PLC logic, and safety-first containment."},
    {t: "Supply Chain", b: "Compromised vendors and firmware: procurement requirements and SBOMs for control systems."},
    {t: "Notable Attacks", b: "Stuxnet, Triton, Colonial Pipeline: the case studies shaping regulation and budgets."},
    {t: "Standards", b: "ISA/IEC 62443 lifecycle, NIST 800-82, NERC CIP: the frameworks auditors check."},
    {t: "Safety Instrumented Systems", b: "Keeping SIS separate and secure: the last line of defense must survive cyber compromise of the BPCS."},
    {t: "Building the Program", b: "Governance, risk assessment, and the roadmap from chaos to maturity without boiling the ocean."}
];
var PRINCIPLES=[
    {n: "Safety overrides security", e: "", s: "No security control may prevent a safety shutdown: the safety instrumented system stays independent."},
    {n: "Availability is the crown jewel", e: "", s: "Patching reboots that stop production need planned windows: OT security works around uptime, not against it."},
    {n: "You can't secure what you can't see", e: "", s: "Asset inventory and passive network mapping precede every other control."}
];
var USES=["Segmenting plant networks", "Hardening PLC systems", "Planning OT incident response", "Auditing against 62443"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Industrial Control Security"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Industrial Security Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-industrial-control-security-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-industrial-control-security-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("industrial-control-security",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
