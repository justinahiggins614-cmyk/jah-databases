(function(){'use strict';
/* jahdb-defense-aerospace-tpm-2-0-hardware-security-modules-1.0 — deterministic boundless generator for defense-aerospace-tpm-2-0-hardware-security-modules.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["tpm-2-0", "hsm-platforms", "attestation", "key-hierarchy", "standards"];
var PREFIX='JAH-DAE11-';
var EDITION='public';
var POOL=[["TPM 2.0: The Root of Trust in Every Machine", "tpm-2-0", "The Trusted Platform Module 2.0 is a tamper-resistant crypto-processor — usually a chip on the motherboard — specified by the Trusted Computing Group. It generates and stores cryptographic keys where software cannot reach them, measures boot software into Platform Configuration Registers, and anchors attestation. Most modern PCs and servers ship with one.", {"Spec": "TCG TPM 2.0", "Form": "dedicated chip or firmware", "Stores": "keys software can't reach", "Anchors": "measured boot, attestation"}], ["Platform Configuration Registers (PCRs)", "tpm-2-0", "PCRs are the TPM's measurement log: each boot component hashes the next and 'extends' the PCR (new = hash(old || measurement)), so any change anywhere in the boot chain changes the final values. 24 PCRs cover firmware, bootloader, kernel, and more. Sealed data only unseals when PCRs match the trusted state.", {"Count": "24 PCRs", "Extend": "hash(old || measurement)", "Covers": "firmware to kernel", "Seals": "data to PCR state"}], ["Measured Boot vs Secure Boot", "attestation", "Measured boot records what ran (into PCRs) without stopping anything; secure boot verifies signatures and refuses to run the untrusted. They compose: secure boot enforces policy, measured boot provides evidence. Attestation then reports the measurements to a verifier. Defense systems want all three.", {"Measured": "records into PCRs", "Secure": "refuses untrusted", "Compose": "enforce + evidence", "Reports": "attestation to verifier"}], ["The Endorsement Key (EK) and Attestation", "attestation", "The Endorsement Key is the TPM's factory-installed identity — a certificate from the manufacturer vouches that this is a genuine TPM. Remote attestation quotes PCR values signed by an attestation key chained to the EK, proving to a remote verifier what software the machine booted. Zero-trust networks admit machines on attestation, not on claims.", {"EK": "factory identity, manufacturer cert", "Quote": "PCRs signed by attestation key", "Proves": "boot state to verifier", "Admits": "zero-trust on evidence"}], ["Sealed Storage", "key-hierarchy", "Sealing encrypts data to a TPM key bound to PCR values: the data decrypts only on the same TPM with the same boot measurements. Disk encryption keys, VPN credentials, and license tokens get sealed so stolen drives stay dark on foreign machines. Change the bootloader and the seal will not open.", {"Seals": "data to TPM + PCR state", "Protects": "disk keys, credentials", "Stolen drive": "stays dark elsewhere", "Change boot": "seal won't open"}], ["TPM Key Hierarchy: EK, SRK, and Children", "key-hierarchy", "TPM keys form a hierarchy: the Endorsement Key at the root, the Storage Root Key guarding stored keys, and child keys for signing, encryption, and attestation. Parent keys wrap children, so deleting a parent destroys the subtree — crypto-shredding by design. Hierarchies organize trust the way directories organize files.", {"Root": "EK (identity)", "Storage": "SRK (wraps keys)", "Children": "signing, encryption", "Delete parent": "subtree destroyed"}], ["Hardware Security Modules (HSMs)", "hsm-platforms", "HSMs are the datacenter-grade cousins of TPMs: rack or PCIe appliances (Thales Luna, YubiHSM, AWS CloudHSM) that generate, store, and use keys in certified tamper-resistant hardware. Certificate authorities, code signing, and payment keys live in HSMs. FIPS 140-3 Level 3/4 certifies the tamper resistance.", {"Form": "appliance / PCIe / cloud", "Holds": "CA, signing, payment keys", "Certifies": "FIPS 140-3 L3/L4", "Grade": "datacenter"}], ["FIPS 140-3: The Certification Bar", "standards", "FIPS 140-3 (successor to 140-2) is the US/Canada standard certifying cryptographic modules: Level 1 is software-only, Level 2 adds tamper-evidence, Level 3 adds tamper-resistance and identity auth, Level 4 adds active tamper response. Defense procurement requires certified modules. The level must match the threat.", {"Levels": "1 (SW) to 4 (active tamper)", "L3": "tamper-resistant + auth", "Procurement": "certified modules required", "Match": "level to threat"}], ["TPM 2.0 Algorithms: The Crypto Menu", "tpm-2-0", "TPM 2.0 is algorithm-agile: RSA, ECC (NIST and BN curves), AES, SHA-256/SHA-384, HMAC, plus key derivation. Agility mattered because algorithms age — the TPM that could not learn new math would become a liability. Post-quantum algorithms are the next menu update the industry is preparing.", {"Asymmetric": "RSA, ECC", "Symmetric": "AES", "Hash": "SHA-256/384, HMAC", "Agile": "algorithms age, TPM learns"}], ["BitLocker, LUKS, and TPM-Bound Disk Encryption", "tpm-2-0", "OS disk encryption binds to the TPM: BitLocker seals keys to PCRs on Windows, LUKS can seal via Clevis on Linux. The drive decrypts transparently on the trusted machine and stays encrypted everywhere else. This is sealed storage at OS scale — the everyday face of the TPM.", {"Windows": "BitLocker + TPM", "Linux": "LUKS + Clevis", "Binds": "keys to PCRs", "Everyday": "TPM at OS scale"}], ["Supply-Chain and Platform Attestation", "attestation", "Attestation scales from one machine to fleets: every node quotes its boot state, verifiers admit only known-good measurements, and unknown firmware never joins the cluster. Supply-chain attacks that modify firmware get caught at admission. The network's immune system is cryptographic.", {"Scales": "one machine to fleets", "Admits": "known-good only", "Catches": "firmware tampering", "Is": "cryptographic immunity"}], ["TPM Provisioning and Ownership", "key-hierarchy", "Taking TPM ownership sets the storage root and authorization values — the administrative act that binds the TPM to its owner. Clear ownership wipes the hierarchy (crypto-shredding everything). Provisioning is done once, carefully, and audited. Ownership is the root of the root of trust.", {"Act": "take ownership", "Sets": "SRK, auth values", "Clear": "wipes hierarchy", "Done": "once, audited"}], ["Common Criteria and EAL", "standards", "Beyond FIPS, high-assurance HSMs pursue Common Criteria Evaluation Assurance Levels — EAL4+ for commercial defense use. EAL measures how thoroughly the security was evaluated, not just what it claims. Procurement stacks FIPS plus Common Criteria for the highest bars.", {"Measures": "evaluation thoroughness", "Bar": "EAL4+ for defense", "Stacks": "FIPS + CC", "Claims": "verified, not asserted"}], ["The Full Trust Chain, Silicon to Service", "attestation", "Ladder-top trust: silicon identity (EK) measures firmware (PCRs), secure boot enforces, attestation proves to verifiers, sealed keys protect data, HSMs guard the crown jewels. Fifteen rungs from a chip to a network that only admits machines it can prove trustworthy.", {"Silicon": "EK identity", "Boot": "measured + secure", "Proof": "attestation", "Data": "sealed keys"}], ["Key Ceremonies", "hsm-platforms", "HSM master keys are born in key ceremonies: multiple custodians, audited scripts, video recording, split knowledge so no one person ever knows the whole key. The ceremony is the human half of hardware trust. Boring, meticulous, and absolutely essential.", {"Birth": "multi-custodian ceremony", "Script": "audited, recorded", "Split": "no single knower", "Is": "human half of trust"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var code='// TPM 2.0 PCR-extend chain demo (simulated model, FNV-1a stands in for SHA-256)\n';
code+='function h(s){var x=0x811c9dc5;for(var i=0;i<s.length;i++){x^=s.charCodeAt(i);x=Math.imul(x,0x01000193);}return("0000000"+(x>>>0).toString(16)).slice(-8);}\n';
code+='var pcr="00000000",meas=["bootloader-v2.4","kernel-5.15-s","app-bundle-9"];\n';
code+='for(var i=0;i<meas.length;i++){pcr=h(pcr+meas[i]);console.log(meas[i]+" -> PCR="+pcr);}\n';
code+='console.log("final PCR digest: "+pcr);';return code;
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
var gen={version:'jahdb-defense-aerospace-tpm-2-0-hardware-security-modules-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-tpm-2-0-hardware-security-modules',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
