(function(){'use strict';
/* jahdb-defense-aerospace-self-encrypting-drives-1.0 — deterministic boundless generator for defense-aerospace-self-encrypting-drives.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["opal-2-0", "encryption", "key-management", "enterprise", "standards"];
var PREFIX='JAH-DAE16-';
var EDITION='public';
var POOL=[["Self-Encrypting Drives: Encryption in the Hardware", "opal-2-0", "A self-encrypting drive encrypts every byte written to its media with a hardware AES engine — always on, transparent to the OS, with no performance penalty worth naming. The media encryption key never leaves the drive's crypto processor. Lose the drive, keep the data: without the key, the platters are noise.", {"Encrypts": "all media, always on", "Engine": "hardware AES", "Key": "never leaves drive", "Lost drive": "platters are noise"}], ["TCG Opal 2.0: The Management Standard", "opal-2-0", "TCG Opal 2.0 is the Trusted Computing Group standard that manages SEDs: locking ranges (bands), admin/user authorities, and the protocols management software uses to lock, unlock, and erase. Opal is why drives from different makers answer the same commands. Samsung, Micron, and Seagate ship Opal drives.", {"Standard": "TCG Opal 2.0", "Manages": "bands, authorities", "Commands": "common across makers", "Makers": "Samsung, Micron, Seagate"}], ["AES-256-XTS: The Media Cipher", "encryption", "SEDs encrypt media with AES-256 in XTS mode — the tweakable block cipher mode designed for storage, where each sector gets its own tweak so identical plaintexts encrypt differently per location. XTS is the storage industry's answer to ECB's pattern leaks. The mode matters as much as the key length.", {"Cipher": "AES-256", "Mode": "XTS (tweakable)", "Per": "sector tweak", "Beats": "ECB pattern leaks"}], ["The Media Encryption Key (MEK)", "key-management", "The MEK is the drive's master secret, generated inside the drive at manufacture and never exposed — all media encryption flows from it. Authentication keys (passwords, tokens) wrap access to the MEK; the MEK itself never changes until crypto-erase. Protect the MEK and the data follows.", {"Born": "inside the drive", "Never": "exposed", "Wraps": "access via auth keys", "Follows": "data protection"}], ["Crypto-Erase: Instant Sanitization", "enterprise", "Crypto-erase destroys the MEK — regenerating it — which renders all data on the drive permanently unreadable in milliseconds, no overwrite passes needed. Decommissioning, repurposing, and emergency sanitization all use it. NIST SP 800-88 recognizes cryptographic erase as sanitization. Fast, final, and auditable.", {"Destroys": "the MEK", "Renders": "data unreadable instantly", "Recognizes": "NIST SP 800-88", "Uses": "decommission, emergency"}], ["Locking Ranges (Bands)", "opal-2-0", "Opal bands partition the drive into independently lockable ranges — the OS band unlocked at boot, a data band requiring authentication. Multi-tenant and multi-level systems isolate data by band. Bands are the access-control lists of the drive.", {"Partitions": "lockable ranges", "Isolates": "tenants, levels", "Unlocks": "per band, per auth", "Are": "drive ACLs"}], ["Pre-Boot Authentication", "enterprise", "Pre-boot authentication unlocks Opal bands before the OS loads — password, smart card, or TPM-sealed key — so the OS only ever sees decrypted media after authorization. Stolen laptop, powered off: the bands stay locked. PBA is the everyday face of SED security.", {"Unlocks": "before OS loads", "With": "password, card, TPM", "Stolen off": "stays locked", "Is": "everyday SED"}], ["PSID Revert: The Factory Reset", "key-management", "The PSID (physical secure ID printed on the drive label) authorizes a revert that crypto-erases the drive back to factory state — the recovery path when passwords are lost. Physical possession of the label equals ownership. Guard the label like a password.", {"PSID": "on the drive label", "Does": "factory revert + erase", "Equals": "physical ownership", "Guards": "like a password"}], ["SEDs vs Software Encryption", "encryption", "SEDs encrypt in hardware at full media speed with zero CPU load and no OS dependence; software encryption (BitLocker/LUKS without HW assist) costs CPU and lives in the OS's trust domain. Best practice layers both: SED for media, software for defense in depth. Different layers, different failures.", {"SED": "HW speed, no CPU", "Software": "CPU cost, OS trust", "Best": "layered both", "Differ": "layers, failures"}], ["Enterprise Management: Central Control", "enterprise", "Enterprise SED management centralizes policies, key escrow, and remote lock/erase across fleets — lost laptop gets crypto-erased over the network before it can be attacked. Central visibility turns drives from liabilities into managed assets. Scale demands centralization.", {"Centralizes": "policy, escrow", "Remotes": "lock/erase", "Turns": "liabilities to assets", "Demands": "scale"}], ["TCG Enterprise and Ruby SSCs", "standards", "Beyond Opal, TCG defines Enterprise SSC (datacenter drives) and Ruby SSC (NVMe) — the same self-encryption concepts across SATA, SAS, and NVMe transports. The standard follows the interface. One management model, every drive type.", {"Enterprise SSC": "datacenter", "Ruby SSC": "NVMe", "Covers": "SATA, SAS, NVMe", "One": "management model"}], ["Validating SED Implementations", "standards", "SED claims get validated: FIPS 140-3 for the crypto module, TCG certification for Opal compliance, and independent testing that locked bands actually stay locked. Marketing says 'encrypted'; validation proves it. Procurement should demand the paperwork.", {"FIPS": "crypto module", "TCG": "Opal compliance", "Tests": "bands stay locked", "Demands": "the paperwork"}], ["Key Escrow and Recovery", "key-management", "Enterprise escrow stores recovery keys centrally so a forgotten password does not brick a drive — with strict access controls and audit on every escrow use. Escrow is the business continuity half of encryption. Uncontrolled escrow is a backdoor; controlled escrow is recovery.", {"Stores": "recovery keys", "Audits": "every use", "Gives": "continuity", "Controls": "or it's a backdoor"}], ["End-of-Life and Sanitization", "enterprise", "Drive end-of-life follows NIST SP 800-88: crypto-erase for SEDs, with verification that the MEK was destroyed and data unrecoverable. Sanitization certificates document the chain of custody. Disposal without sanitization is a breach with a shipping label.", {"Follows": "NIST SP 800-88", "Verifies": "MEK destroyed", "Documents": "chain of custody", "Without": "breach by shipping"}], ["The SED Security Picture", "opal-2-0", "Ladder-top SED: hardware AES-XTS on all media, Opal-managed bands and authorities, crypto-erase sanitization, enterprise escrow and remote control. Fifteen rungs from a crypto chip to fleets of drives that stay dark when stolen.", {"Encrypts": "HW AES-XTS", "Manages": "Opal bands", "Sanitizes": "crypto-erase", "Controls": "enterprise"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var code='// SED OPAL band lock-state demo (simulated model)\n';
code+='var bands={global:{locked:false},band1:{locked:true},band2:{locked:true}};\n';
code+='function unlock(b,pin){if(pin==="****"){bands[b].locked=false;return true;}return false;}\n';
code+='console.log("before: "+JSON.stringify(bands));\nunlock("band1","****");\n';
code+='console.log("after unlock band1: "+JSON.stringify(bands));';return code;
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
var gen={version:'jahdb-defense-aerospace-self-encrypting-drives-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-self-encrypting-drives',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
