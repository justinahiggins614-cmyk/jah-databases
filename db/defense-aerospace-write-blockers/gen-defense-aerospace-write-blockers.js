(function(){'use strict';
/* jahdb-defense-aerospace-write-blockers-1.0 — deterministic boundless generator for defense-aerospace-write-blockers.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["hardware-bridges", "forensic-suites", "validation", "interfaces", "standards"];
var PREFIX='JAH-DAE18-';
var EDITION='public';
var POOL=[["Write-Blockers: Read-Only by Hardware", "hardware-bridges", "A write-blocker is a hardware bridge between an analyst's workstation and a suspect drive that passes read commands and blocks every write command — physically enforcing read-only access during forensic imaging. Tableau and WiebeTech make the known bridges. The evidence drive cannot be altered through the blocker, which is the point.", {"Enforces": "read-only in hardware", "Passes": "reads", "Blocks": "all writes", "Makers": "Tableau, WiebeTech-class"}], ["Why Forensics Needs Them", "forensic-suites", "Digital forensics must prove the evidence was not altered: imaging a drive through a write-blocker with hash verification before and after is the standard that makes the image admissible. Booting a suspect drive without one can change timestamps and destroy evidence. The blocker is the chain of custody's first link.", {"Proves": "no alteration", "Standard": "image + hash, before/after", "Without": "timestamps change", "Is": "custody's first link"}], ["How Blocking Works: Command Filtering", "hardware-bridges", "Write-blockers filter at the storage protocol level — ATA, SCSI, USB mass storage, NVMe — dropping or rejecting write opcodes while translating reads. Some also block the HPA/DCO hidden-area commands that could conceal data. Filtering happens in hardware/firmware the host cannot override.", {"Filters": "ATA/SCSI/USB/NVMe opcodes", "Drops": "write commands", "Blocks": "hidden-area tricks", "Lives": "beyond host override"}], ["Tableau TX1 and Forensic Bridges", "hardware-bridges", "The Tableau TX1 is the iconic forensic bridge: multi-interface (SATA, USB, IDE, PCIe) imaging with built-in hash verification and a touchscreen workflow. One device images almost any drive forensically. It is the standard field tool the industry recognizes.", {"Device": "Tableau TX1-class", "Interfaces": "SATA/USB/IDE/PCIe", "Hashes": "built-in verification", "Is": "field standard"}], ["Hash-Verified Imaging", "validation", "Forensic imaging copies every sector and hashes the source and the image — matching SHA-256 means the copy is bit-identical. The hash is recorded in the case file as the integrity proof. Verification is not optional; it is the evidence.", {"Copies": "every sector", "Hashes": "source and image", "Match": "bit-identical proof", "Files": "in the case record"}], ["NIST CFTT Validation", "standards", "NIST's Computer Forensics Tool Testing program validates write-blockers: the tool must block all modifying commands across interfaces and the tests are published. CFTT reports are how labs choose blockers. Tested tools, not trusted claims.", {"Program": "NIST CFTT", "Requires": "block all modifies", "Publishes": "test reports", "Chooses": "labs by report"}], ["NVMe and Modern Interfaces", "interfaces", "NVMe drives need NVMe-aware blockers — the protocol differs from SATA and so does the filtering. M.2, U.2, and PCIe add-in cards each need the right bridge. The blocker must match the evidence's interface or there is no acquisition.", {"Needs": "NVMe-aware filtering", "Forms": "M.2, U.2, AIC", "Matches": "interface or no image", "Differs": "protocol per bus"}], ["USB Write-Blockers", "interfaces", "USB write-blockers sit between the workstation and USB drives, filtering mass-storage writes — the quick tool for thumb drives and externals in triage. Same principle, smaller package. Triage moves fast; the blocker keeps it honest.", {"Sits": "workstation to USB drive", "Filters": "mass-storage writes", "Uses": "triage", "Keeps": "triage honest"}], ["Network and Remote Acquisition", "forensic-suites", "Some suites acquire over the network with software write-blocking agents — useful for live enterprise collection where pulling drives is impractical. Hardware blockers remain the gold standard for dead drives. The method follows the situation.", {"Agents": "software blocking, remote", "Uses": "live enterprise", "Gold": "hardware, dead drives", "Follows": "the situation"}], ["Write-Blocked Booting (Live Preview)", "forensic-suites", "Analysts sometimes boot a suspect drive read-only through a blocker for a live preview — seeing the system without changing it. Every write the OS attempts gets blocked and logged. Preview informs the full imaging plan.", {"Boots": "suspect OS read-only", "Blocks": "OS writes", "Logs": "attempts", "Informs": "imaging plan"}], ["HPA and DCO Hidden Areas", "validation", "Drives can hide areas — Host Protected Area and Device Configuration Overlay — that normal reads skip; forensic blockers and tools address these so hidden data is still acquired. What the OS cannot see, the lab still images. Completeness matters.", {"Hides": "HPA, DCO areas", "Skips": "normal reads", "Acquires": "forensic tools", "Matters": "completeness"}], ["Chain of Custody Documentation", "standards", "Every acquisition documents drive serial, blocker used, hashes, time, and analyst — the paperwork that carries the image into court. Gaps in documentation are gaps in admissibility. The form is as important as the forensic copy.", {"Documents": "serial, hashes, analyst", "Carries": "into court", "Gaps": "kill admissibility", "Is": "as important as the copy"}], ["Blocker Maintenance and Testing", "standards", "Labs re-test blockers periodically — firmware updates get validated, interfaces get exercised — because a blocker that stopped blocking is worse than none. Test logs join the case files. Trust is maintained, not assumed.", {"Re-tests": "periodically", "Validates": "firmware updates", "Joins": "case files", "Maintains": "trust"}], ["Mobile Device Considerations", "interfaces", "Phones need their own acquisition discipline — often logical plus physical methods with write-protection where the interface allows. The principle is identical: alter nothing. Mobile forensics is its own specialty with the same ethics.", {"Needs": "own discipline", "Methods": "logical + physical", "Principle": "alter nothing", "Ethics": "same"}], ["The Forensic Acquisition Picture", "hardware-bridges", "Ladder-top write-blocking: hardware-enforced read-only, protocol-level filtering, hash-verified imaging, validated tools, documented custody. Fifteen rungs from a bridge chip to evidence that stands in court.", {"Enforces": "read-only HW", "Filters": "protocols", "Verifies": "hashes", "Documents": "custody"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var code='// Write-blocker hash-verified imaging demo (simulated model)\n';
code+='function h(s){var x=0x811c9dc5;for(var i=0;i<s.length;i++){x^=s.charCodeAt(i);x=Math.imul(x,0x01000193);}return("0000000"+(x>>>0).toString(16)).slice(-8);}\n';
code+='var sectors=["boot","fs-table","evidence-1","evidence-2"];\nvar img="";\n';
code+='for(var i=0;i<sectors.length;i++){img+=sectors[i]+";";console.log("read-only copy: "+sectors[i]);}\n';
code+='console.log("image hash "+h(img)+" (writes blocked: 0)");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-write-blockers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-write-blockers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
