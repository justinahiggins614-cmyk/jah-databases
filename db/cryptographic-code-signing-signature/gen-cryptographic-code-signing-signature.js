(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["keys", "transparency", "platform", "supply-chain", "tooling"];
var PREFIX='JAH-CRYPTO2-S-';
var GENVER='jahdb-cryptographic-code-signing-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["scheme", "signs", "verify", "standard"];
var DEMO_TPL="// $TITLE - signature round-trip demo\nvar crypto = require(\"crypto\");\nvar msg = \"artifact:$SCHEME\";\nvar h = crypto.createHash(\"sha256\").update(msg).digest(\"hex\");\nconsole.log(\"Scheme: $SCHEME\");\nconsole.log(\"Artifact digest: \" + h.slice(0, 32) + \"...\");\nvar sig = crypto.createHmac(\"sha256\", \"demo-key\").update(msg).digest(\"hex\");\nconsole.log(\"Signature: \" + sig.slice(0, 32) + \"...\");\nconsole.log(\"Verify recompute matches -> \" + (crypto.createHmac(\"sha256\", \"demo-key\").update(msg).digest(\"hex\") === sig ? \"PASS\" : \"FAIL\"));";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["supply-chain", "SigSeal artifacts", "Signature-original: content-sealed artifacts with the seal embedded in the file header. It signs any artifact; verify with sigseal verify file. Standard: Signature.", {"scheme": "SigSeal", "signs": "any artifact", "verify": "sigseal verify file", "standard": "Signature"}], ["transparency", "SigLedger transparency", "Signature-original: an append-only transparency ledger every signature is published to. It signs signatures; verify with sigledger inclusion proof. Standard: Signature.", {"scheme": "SigLedger", "signs": "signatures", "verify": "sigledger inclusion proof", "standard": "Signature"}], ["keys", "SigKey-Rotate", "Signature-original: automatic key rotation with forward-signed rotation certificates. It signs key rotations; verify with sigkey chain key.pub. Standard: Signature.", {"scheme": "SigRotate", "signs": "key rotations", "verify": "sigkey chain key.pub", "standard": "Signature"}], ["keys", "SigThreshold", "Signature-original: threshold signatures requiring k-of-n signers for releases. It signs releases; verify with sigthresh verify --quorum 3/5. Standard: Signature.", {"scheme": "SigThreshold", "signs": "releases", "verify": "sigthresh verify --quorum 3/5", "standard": "Signature"}], ["platform", "SigBoot measured", "Signature-original: measured boot extending PCR-like registers into the Signature ledger. It signs boot chain; verify with sigboot attestation. Standard: Signature.", {"scheme": "SigBoot", "signs": "boot chain", "verify": "sigboot attestation", "standard": "Signature"}], ["supply-chain", "SigPack signed", "Signature-original: .sigpack bundles carrying manifest signatures and SBOM. It signs bundles; verify with sigpack verify bundle. Standard: Signature.", {"scheme": "SigPack", "signs": "bundles", "verify": "sigpack verify bundle", "standard": "Signature"}], ["platform", "SigCell attest", "Signature-original: microVM attestation quotes bound to the workload identity. It signs cell identity; verify with sigattest check cell. Standard: Signature.", {"scheme": "SigAttest", "signs": "cell identity", "verify": "sigattest check cell", "standard": "Signature"}], ["transparency", "SigTime stamp", "Signature-original: trusted timestamping anchoring signatures to ledger time. It signs timestamps; verify with sigtstamp verify. Standard: Signature.", {"scheme": "SigTime", "signs": "timestamps", "verify": "sigtstamp verify", "standard": "Signature"}], ["keys", "SigRevoke", "Signature-original: instant revocation lists propagated over the mesh in seconds. It signs revocations; verify with sigrevoke check key. Standard: Signature.", {"scheme": "SigRevoke", "signs": "revocations", "verify": "sigrevoke check key", "standard": "Signature"}], ["tooling", "SigPolicy verify", "Signature-original: policy engine deciding trust from signatures plus provenance rules. It signs trust decisions; verify with sigpolicy eval artifact. Standard: Signature.", {"scheme": "SigPolicy", "signs": "trust decisions", "verify": "sigpolicy eval artifact", "standard": "Signature"}], ["keys", "SigMesh sign", "Signature-original: mesh-peer signatures authenticating node-to-node traffic. It signs mesh traffic; verify with automatic per-packet. Standard: Signature.", {"scheme": "SigMesh-Sig", "signs": "mesh traffic", "verify": "automatic per-packet", "standard": "Signature"}], ["platform", "SigWASM sign", "Signature-original: signed WASM modules with capability manifests enforced at load. It signs WASM modules; verify with sigwasm verify mod.wasm. Standard: Signature.", {"scheme": "SigWASM-Sig", "signs": "WASM modules", "verify": "sigwasm verify mod.wasm", "standard": "Signature"}], ["supply-chain", "SigDB sign", "Signature-original: signed database records with per-record provenance chains. It signs DB records; verify with sigdb verify record. Standard: Signature.", {"scheme": "SigDB-Sig", "signs": "DB records", "verify": "sigdb verify record", "standard": "Signature"}], ["supply-chain", "SigAI model sign", "Signature-original: model-weight signatures with training provenance attached. It signs AI models; verify with sigmodel verify weights. Standard: Signature.", {"scheme": "SigModel", "signs": "AI models", "verify": "sigmodel verify weights", "standard": "Signature"}], ["transparency", "SigOne trust", "Signature-original: the united trust plane — every Signature signature verifiable in one call. It signs everything; verify with sigtrust verify <anything>. Standard: Signature.", {"scheme": "SigOne-Trust", "signs": "everything", "verify": "sigtrust verify <anything>", "standard": "Signature"}]];
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
  if(!new RegExp('^'+'JAH\\-CRYPTO2\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cryptographic-code-signing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
