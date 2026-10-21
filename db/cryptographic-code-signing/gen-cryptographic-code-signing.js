(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["keys", "transparency", "platform", "supply-chain", "tooling"];
var PREFIX='JAH-CRYPTO2-';
var GENVER='jahdb-cryptographic-code-signing-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["scheme", "signs", "verify", "standard"];
var DEMO_TPL="// $TITLE - signature round-trip demo\nvar crypto = require(\"crypto\");\nvar msg = \"artifact:$SCHEME\";\nvar h = crypto.createHash(\"sha256\").update(msg).digest(\"hex\");\nconsole.log(\"Scheme: $SCHEME\");\nconsole.log(\"Artifact digest: \" + h.slice(0, 32) + \"...\");\nvar sig = crypto.createHmac(\"sha256\", \"demo-key\").update(msg).digest(\"hex\");\nconsole.log(\"Signature: \" + sig.slice(0, 32) + \"...\");\nconsole.log(\"Verify recompute matches -> \" + (crypto.createHmac(\"sha256\", \"demo-key\").update(msg).digest(\"hex\") === sig ? \"PASS\" : \"FAIL\"));";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["keys", "GPG detached signatures", "The classic .asc/.sig sidecar: gpg --detach-sign, verified against the author’s public key. It signs release tarballs; verify with gpg --verify file.sig file. Standard: RFC 4880.", {"scheme": "GPG/OpenPGP", "signs": "release tarballs", "verify": "gpg --verify file.sig file", "standard": "RFC 4880"}], ["transparency", "Sigstore cosign", "Keyless signing binding artifacts to OIDC identity with signatures logged in Rekor. It signs container images; verify with cosign verify --certificate-identity .... Standard: Sigstore spec.", {"scheme": "Sigstore", "signs": "container images", "verify": "cosign verify --certificate-identity ...", "standard": "Sigstore spec"}], ["platform", "Authenticode", "Windows’ PE signing; SmartScreen and driver policies gate on valid signatures. It signs EXE/DLL/sys drivers; verify with signtool verify /pa file.exe. Standard: Microsoft Authenticode.", {"scheme": "Authenticode", "signs": "EXE/DLL/sys drivers", "verify": "signtool verify /pa file.exe", "standard": "Microsoft Authenticode"}], ["platform", "Apple notarization", "Apple staples a notarization ticket to signed macOS software for Gatekeeper approval. It signs macOS apps; verify with spctl -a -vv app.app. Standard: Apple TN2206.", {"scheme": "Apple code signing", "signs": "macOS apps", "verify": "spctl -a -vv app.app", "standard": "Apple TN2206"}], ["keys", "minisign", "A dead-simple Ed25519 signing tool by Frank Denis with tiny trusted-comment signatures. It signs any file; verify with minisign -V -p key.pub -m file. Standard: Ed25519 (RFC 8032).", {"scheme": "minisign", "signs": "any file", "verify": "minisign -V -p key.pub -m file", "standard": "Ed25519 (RFC 8032)"}], ["keys", "OpenBSD signify", "signify signs base releases with short base64 keys designed for easy human verification. It signs OS releases; verify with signify -V -p key.pub -m file. Standard: Ed25519.", {"scheme": "signify", "signs": "OS releases", "verify": "signify -V -p key.pub -m file", "standard": "Ed25519"}], ["supply-chain", "RPM package signing", "RPMs embed GPG signatures; rpm -K checks the package against imported keys. It signs RPM packages; verify with rpm -K pkg.rpm. Standard: RPM spec.", {"scheme": "RPM GPG", "signs": "RPM packages", "verify": "rpm -K pkg.rpm", "standard": "RPM spec"}], ["supply-chain", "Debian debsig-verify", "debsig-verify checks .deb signatures against per-origin policies for archive trust. It signs Debian packages; verify with debsig-verify policy.pol pkg.deb. Standard: Debian policy.", {"scheme": "debsig", "signs": "Debian packages", "verify": "debsig-verify policy.pol pkg.deb", "standard": "Debian policy"}], ["platform", "Android APK signing", "APK Signature Scheme v2 signs the whole APK; v4 enables fs-verity incremental verification. It signs Android APKs; verify with apksigner verify app.apk. Standard: Android docs.", {"scheme": "APK Signature v2/v3", "signs": "Android APKs", "verify": "apksigner verify app.apk", "standard": "Android docs"}], ["platform", "UEFI Secure Boot", "Firmware verifies bootloader signatures against keys in the signature database (db). It signs bootloaders/shims; verify with firmware db/dbx check. Standard: UEFI spec.", {"scheme": "Secure Boot", "signs": "bootloaders/shims", "verify": "firmware db/dbx check", "standard": "UEFI spec"}], ["platform", "dm-verity", "The kernel verifies block-device reads against a Merkle tree — Android’s verified boot core. It signs system partitions; verify with kernel Merkle verification. Standard: Linux kernel docs.", {"scheme": "dm-verity", "signs": "system partitions", "verify": "kernel Merkle verification", "standard": "Linux kernel docs"}], ["supply-chain", "TUF", "The Update Framework defines roles (root, targets, snapshot, timestamp) so key compromise is contained. It signs update repositories; verify with tuf client workflow. Standard: TUF spec.", {"scheme": "TUF", "signs": "update repositories", "verify": "tuf client workflow", "standard": "TUF spec"}], ["supply-chain", "in-toto attestations", "in-toto records each supply-chain step’s signed evidence so verifiers check the whole pipeline. It signs build steps; verify with in-toto-verify. Standard: in-toto spec.", {"scheme": "in-toto", "signs": "build steps", "verify": "in-toto-verify", "standard": "in-toto spec"}], ["supply-chain", "SLSA provenance", "SLSA levels rate build integrity; provenance attestations describe exactly how artifacts were built. It signs build provenance; verify with slsa-verifier. Standard: SLSA spec.", {"scheme": "SLSA", "signs": "build provenance", "verify": "slsa-verifier", "standard": "SLSA spec"}], ["tooling", "SSH commit signing", "git commit -S with SSH keys (not just GPG) ties commits to the developer’s SSH identity. It signs git commits/tags; verify with git log --show-signature. Standard: OpenSSH PROTOCOL.sshsig.", {"scheme": "SSH signatures", "signs": "git commits/tags", "verify": "git log --show-signature", "standard": "OpenSSH PROTOCOL.sshsig"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-CRYPTO2\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cryptographic-code-signing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
