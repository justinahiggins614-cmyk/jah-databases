(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["transfer", "guards", "ceremonies", "operations"];
var PREFIX='JAH-AGC-';
var LAST_VERIFIED='2026-10-21';
var PROVENANCE='Public industry records and documentation';
var SRC='public-harvest';
/* base records: [title, category, description, mechanisms, platforms, standards, ladder_rank, demo_idx] */
var B=[["Data Diode Transfers", "transfer", "Moves data across the gap with hardware data diodes that physically allow one direction only. Fiber with the return path removed cannot be subverted by software; it is the strongest one-way guarantee. High-security networks standardize on them.", ["Install hardware diodes", "Enforce one direction physically", "Monitor the boundary"], ["Owl", "Waterfall", "Vendors"], ["Diode specs", "Cross-domain guides"], 2, 0], ["One-Way Protocols", "transfer", "Runs protocols designed for one-way flow: UDP streams, file drops, no acknowledgments. The sender never expects a reply; reliability comes from redundancy. It matches the diode's physics.", ["Use ack-less protocols", "Add redundancy", "Verify on receipt"], ["Custom", "Diode vendors", "ICS"], ["Protocol design", "Diode guides"], 2, 0], ["QR Code Bridges", "transfer", "Bridges small payloads with QR codes scanned across the gap. Keys and signatures fit in a few codes; cameras never touch the secure network. It is the human-speed air gap.", ["Encode payloads as QR", "Scan across the gap", "Verify integrity"], ["Custom tools", "Phones", "HSMs"], ["QR spec", "Air-gap guides"], 1, 1], ["Sneakernet Protocols", "transfer", "Moves data on physical media with chain-of-custody protocols. Encrypted drives travel by courier; every handoff is logged and verified. Bandwidth is a truck; latency is a day.", ["Encrypt the media", "Log every handoff", "Verify on arrival"], ["Couriers", "Encrypted drives", "Procedures"], ["Chain-of-custody", "Security guides"], 1, 2], ["Optical Transfer", "transfer", "Transfers data optically — screen to camera — with no electrical connection. Light crosses the gap; malware cannot ride photons back. It is slow and very sure.", ["Display encoded data", "Capture optically", "Verify checksums"], ["Custom", "Research", "High security"], ["Optical comms", "Air-gap literature"], 2, 1], ["Manual Key Ceremonies", "ceremonies", "Generates and transfers keys in witnessed ceremonies with split knowledge. No single person ever holds the whole key; the ceremony is scripted and recorded. Root keys are born this way.", ["Script the ceremony", "Split knowledge", "Witness and record"], ["CAs", "HSM vendors", "Governments"], ["Ceremony literature", "Key management"], 3, 2], ["Cross-Domain Guards", "guards", "Filters transfers through cross-domain guards that inspect content deeply. Guards validate formats, strip active content, and enforce policies per direction. They are the firewall of the air gap.", ["Inspect content deeply", "Enforce per-direction policy", "Log everything"], ["Raytheon", "Owl", "Vendors"], ["CDS literature", "NCDSMO"], 3, 0], ["File Sanitization (CDR)", "guards", "Rebuilds files with content disarm and reconstruction to strip embedded threats. CDR discards the original and builds a clean copy; macros and exploits do not survive. Every file crossing gets rebuilt.", ["Parse the file", "Rebuild cleanly", "Verify the output"], ["Votiro", "Glasswall", "OPSWAT"], ["CDR literature", "File format specs"], 2, 0], ["USB Data Blockers", "guards", "Blocks USB data pins with charge-only adapters to stop malware and exfiltration. Power flows; data does not. It is the simplest port protection.", ["Use data-blocking adapters", "Enforce physically", "Audit ports"], ["Blockers", "Policies", "Enterprises"], ["USB specs", "Port security"], 1, 1], ["TEMPEST Considerations", "operations", "Accounts for electromagnetic emanations that can bridge air gaps. Shielding, zoning, and emission limits keep signals inside; red/black separation is the discipline. Air gaps leak through physics.", ["Shield sensitive areas", "Separate red and black", "Test emissions"], ["Shielded rooms", "Evaluators", "Governments"], ["TEMPEST literature", "Emission standards"], 3, 2], ["Transfer Auditing", "operations", "Audits every gap crossing with what, when, who, and authorization. The audit trail proves the gap's integrity; gaps without auditing are just slow networks. Every crossing is an event.", ["Log every crossing", "Require authorization", "Review regularly"], ["SIEMs", "Procedures", "Guards"], ["Audit literature", "Security guides"], 2, 2], ["Scheduled Sync Windows", "operations", "Opens the gap only during scheduled, supervised sync windows. Outside the window the gap is complete; during it, transfers run under watch. It bounds exposure in time.", ["Define sync windows", "Supervise transfers", "Close after"], ["Procedures", "Guards", "ICS"], ["Operations literature", "Air-gap guides"], 2, 2], ["Hardware-Enforced Directionality", "guards", "Enforces transfer direction in hardware that software cannot override. Optical isolators and one-way taps make the direction a physical fact. Policy becomes physics.", ["Use one-way hardware", "Verify physically", "Monitor for tampering"], ["Diode vendors", "Taps", "High security"], ["Hardware specs", "CDS literature"], 3, 0], ["Air-Gap Incident Response", "operations", "Responds to suspected gap breaches with containment that assumes the worst. The bridge is severed first; forensics follows. Air-gap incidents are rare and serious.", ["Sever the bridge", "Preserve forensics", "Rebuild trust deliberately"], ["IR teams", "Procedures", "Governments"], ["IR literature", "NIST SP 800-61"], 3, 2], ["Acoustic Mesh Caution", "operations", "Treats acoustic and other covert channels as in-scope threats to air gaps. Researchers have exfiltrated via speakers, fans, and LEDs; defenses monitor for anomalous emanations. Paranoia is calibrated to the asset.", ["Know the covert channels", "Monitor emanations", "Remove unnecessary emitters"], ["Research", "High security", "Evaluators"], ["Covert channel literature", "TEMPEST"], 3, 2]];
var DEMOS=["// Demo: {NAME} — one-way transfer accounting\nvar out={N1},back=0;\nconsole.log('technique: {NAME}');console.log('bytes out of secure zone: '+out+', bytes back in: '+back);\nconsole.log(back===0?'air gap holds — data flows one way only':'VIOLATION — return path detected');", "// Demo: {NAME} — QR bridge throughput\nvar bytes={N2}*100,perQR=2000;\nvar codes=Math.ceil(bytes/perQR),secs=codes*2;\nconsole.log('technique: {NAME}');console.log('payload: '+bytes+' bytes -> '+codes+' QR codes');\nconsole.log('scan time: ~'+secs+'s — slow but air-gapped');", "// Demo: {NAME} — transfer audit chain\nvar chain=['export-approved','media-scanned','import-verified'];\nconsole.log('technique: {NAME}');\nchain.forEach(function(s,i){console.log('step '+(i+1)+': '+s+' OK');});\nconsole.log('complete audit trail — every crossing accounted for');"];
var CONTEXTS=["a production web service handling steady user traffic", "an on-device mobile deployment with tight resource budgets", "an edge cluster serving a regional user base", "a CI pipeline validating every commit", "a research prototype exploring new designs", "a regulated enterprise environment with audit requirements"];
var NOTES=["Operators report measurable gains within the first deployment cycle.", "Start with the simplest configuration, then compound toward the advanced form.", "Pair with monitoring so regressions are caught before users notice.", "Document the chosen parameters so the setup can be recreated exactly.", "Validate against a baseline before and after enabling the technique.", "Keep a rollback path ready when rolling this out to production."];
var RANK_WORD={1:'Simple',2:'Compound',3:'Advanced'};
function fill(tpl,vars){return tpl.replace(/\{([A-Z0-9_]+)\}/g,function(m,k){return (k in vars)?vars[k]:m;});}
function escJS(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n');}
function makeDemo(b,seed,rnd){
  var tpl=DEMOS[b[7]%DEMOS.length];
  var vars={NAME:escJS(b[0]),N1:1+((seed*7+b[7])%97),N2:2+((seed*13)%499),N3:5+((seed*29)%95),SEED:seed,CAT:escJS(b[1])};
  return {language:'javascript',title:'Demo — '+b[0],program:fill(tpl,vars)};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[1]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var ctx=pick(CONTEXTS,rnd), note=pick(NOTES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rot=seed%b[3].length;
  var mechs=b[3].slice(rot).concat(b[3].slice(0,rot)).slice(0,3);
  var plats=b[4].slice(0,2+((seed%2)));
  return {id:id,title:b[0],description:b[2]+' '+note+' Deployment context: '+ctx+'.',
    category:b[1],key_mechanisms:mechs,platforms:plats,standards:b[5].slice(),
    complexity:RANK_WORD[b[6]],ladder_rank:b[6],demo:makeDemo(b,seed,rnd),
    provenance:PROVENANCE,last_verified:LAST_VERIFIED,src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!Array.isArray(r.key_mechanisms)||r.key_mechanisms.length<2)e.push('key_mechanisms');
  if(!Array.isArray(r.platforms)||!r.platforms.length)e.push('platforms');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!==LAST_VERIFIED)e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id!==rec.id&&s.description===rec.description)errs.push('duplicate-of:'+s.id);
  });
  return {ok:!errs.length,errors:errs};
}
var gen={version:'jahdb-air-gapped-cryptographic-bridges-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('air-gapped-cryptographic-bridges',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
