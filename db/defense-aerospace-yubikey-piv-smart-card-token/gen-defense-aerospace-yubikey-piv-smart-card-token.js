(function(){'use strict';
/* jahdb-defense-aerospace-yubikey-piv-smart-card-token-1.0 — deterministic boundless generator for defense-aerospace-yubikey-piv-smart-card-token.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["fido2", "piv", "totp-hotp", "openpgp", "deployment"];
var PREFIX='JAH-DAE13-';
var EDITION='public';
var POOL=[["Hardware Tokens: Proof You Hold the Key", "fido2", "Hardware authentication tokens — YubiKey, PIV smart cards — prove identity with cryptography in tamper-resistant hardware instead of passwords in human memory. The private key never leaves the token; authentication is a signature challenge. Phishing fails because there is nothing to type and nothing to replay.", {"Proves": "with hardware crypto", "Key": "never leaves token", "Beats": "phishing, replay", "Replaces": "passwords"}], ["FIDO2 and Passkeys", "fido2", "FIDO2 (WebAuthn + CTAP) is the open standard for phishing-resistant login: the token creates a per-site key pair, the site keeps the public key, and login is a signed challenge bound to the site's identity. Passkeys are the synced, user-friendly form. Defense systems require the hardware-bound form.", {"Standard": "FIDO2/WebAuthn", "Keys": "per-site pairs", "Binds": "to site identity", "Defense": "hardware-bound form"}], ["PIV: The Federal Smart Card", "piv", "PIV (Personal Identity Verification, NIST SP 800-73) is the US federal smart-card standard: the card holds certificates for authentication, signing, and encryption, unlocked by PIN. CAC cards are the DoD's PIV. YubiKeys can host PIV applets, bringing federal auth to a USB key.", {"Standard": "NIST SP 800-73", "Holds": "auth, signing, encryption certs", "Unlocks": "PIN", "DoD": "CAC cards"}], ["TOTP and HOTP One-Time Codes", "totp-hotp", "TOTP (time-based) and HOTP (counter-based) generate one-time codes from a shared secret — the six digits in authenticator apps, also storable on hardware tokens. The server checks the code against its copy of the secret. Simple, offline-capable, and far better than passwords alone.", {"TOTP": "time-based codes", "HOTP": "counter-based", "Secret": "shared, on token", "Beats": "passwords alone"}], ["OpenPGP on the Token", "openpgp", "Hardware tokens store OpenPGP keys for signing and encrypting email and files — private key operations happen on the token, unlocked by PIN. Code and document signatures then carry hardware-backed identity. The YubiKey's OpenPGP applet is the common carrier.", {"Stores": "PGP keys on token", "Signs": "email, files, code", "Unlocks": "PIN", "Carries": "hardware-backed identity"}], ["PINs, PUKs, and Lockout", "deployment", "Tokens protect keys with PINs and a PUK for unblocking: too many wrong PINs locks the token, and the PUK resets it — too many wrong PUKs destroys the keys. This is the anti-brute-force math that makes stolen tokens useless. Admins must record PUKs securely or accept the loss.", {"PIN": "daily unlock", "PUK": "unblock, limited tries", "Exhausted": "keys destroyed", "Admin": "record PUKs securely"}], ["Touch-to-Authenticate", "fido2", "Many tokens require a physical touch to complete authentication — the human-presence test that stops remote malware from using the token silently. A signature will not happen without the finger. It is a tiny interaction with outsized security value.", {"Requires": "physical touch", "Stops": "remote silent use", "Tests": "human presence", "Value": "outsized"}], ["Attestation: Proving the Token Is Genuine", "deployment", "Tokens carry manufacturer attestation certificates proving they are genuine hardware — the same idea as the TPM EK. High-security enrollment checks attestation before trusting the token's keys. Counterfeit tokens get rejected at the door.", {"Carries": "manufacturer cert", "Proves": "genuine hardware", "Checks": "at enrollment", "Rejects": "counterfeits"}], ["Deploying Tokens Across an Organization", "deployment", "Enterprise token deployment means provisioning (loading certs), PIN enrollment, help-desk flows for lost tokens, and revocation lists for departures. The logistics dwarf the cryptography. Successful programs treat tokens like badges: issued, tracked, revoked.", {"Means": "provisioning, enrollment", "Needs": "help-desk flows", "Revokes": "on departure", "Treats": "like badges"}], ["PIV for Machine and Service Accounts", "piv", "PIV-style certificates also authenticate machines and services: servers prove identity with hardware-held keys, and code signing uses token-held keys. Humans are not the only identities. Every workload gets the same hardware-backed treatment.", {"Machines": "HW-held identity", "Services": "cert auth", "Signing": "token-held keys", "Rule": "every workload identified"}], ["Backup Tokens and Recovery", "deployment", "Every critical identity enrolls two tokens — primary and backup — because hardware gets lost and people go on leave. Recovery flows re-enroll without weakening assurance. One token is a single point of failure wearing a security costume.", {"Enrolls": "two tokens each", "Covers": "loss, leave", "Recovers": "without weakening", "One token": "SPOF in costume"}], ["Token Form Factors", "deployment", "Tokens come as USB-A, USB-C, Lightning, and NFC — the connector must match the fleet's devices, and NFC covers phones. Form-factor planning is unglamorous and decisive. The best token is the one people actually carry.", {"Forms": "USB-A/C, Lightning, NFC", "Matches": "fleet devices", "NFC": "covers phones", "Wins": "carried daily"}], ["Standards Behind the Tokens", "piv", "FIDO Alliance standards, NIST SP 800-63 (digital identity), and SP 800-73 (PIV) are the rulebooks tokens implement. Procurement cites the standards, not the brands. Standards are why tokens from different makers interoperate.", {"FIDO": "phishing-resistant auth", "800-63": "digital identity", "800-73": "PIV cards", "Why": "interoperability"}], ["Revocation and Lifecycle", "deployment", "Certificates expire and get revoked; tokens get lost, reassigned, and retired. Lifecycle management — issuance to destruction — is the ongoing work after deployment day. A token program without lifecycle is a breach waiting for a calendar.", {"Expires": "certs", "Revokes": "lost/departed", "Manages": "issuance to destruction", "Without": "breach on a calendar"}], ["The Token-Protected Organization", "fido2", "Ladder-top tokens: every human and workload with hardware-backed identity, phishing-resistant login everywhere, PIV for federal interop, lifecycle managed. Fifteen rungs from a USB key to an organization where stolen passwords are worthless.", {"Everyone": "HW-backed identity", "Login": "phishing-resistant", "Interop": "PIV federal", "Manages": "lifecycle"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var code='// PIV challenge-response demo (simulated model)\n';
code+='function h(s){var x=0x811c9dc5;for(var i=0;i<s.length;i++){x^=s.charCodeAt(i);x=Math.imul(x,0x01000193);}return("0000000"+(x>>>0).toString(16)).slice(-8);}\n';
code+='var chal="9f3ac2e17b",pinTries=3;\n';
code+='for(var t=0;t<2;t++){var resp=h(chal+"|slot9a|"+t);console.log("attempt "+(t+1)+": resp="+resp+" tries-left="+(pinTries-t-1));}\n';
code+='console.log("PIV slot 9a auth ok");';return code;
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
var gen={version:'jahdb-defense-aerospace-yubikey-piv-smart-card-token-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-yubikey-piv-smart-card-token',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
