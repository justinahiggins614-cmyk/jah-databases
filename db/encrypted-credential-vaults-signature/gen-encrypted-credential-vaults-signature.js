(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["server", "password-manager", "cloud", "file-based", "tooling"];
var PREFIX='JAH-ECV-S-';
var GENVER='jahdb-encrypted-credential-vaults-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["vault", "stores", "crypto", "access"];
var DEMO_TPL="// $TITLE - envelope encryption demo\nvar crypto = require(\"crypto\");\nfunction seal(secret, key) {\n  var iv = crypto.randomBytes(12);\n  var c = crypto.createCipheriv(\"aes-256-gcm\", crypto.createHash(\"sha256\").update(key).digest(), iv);\n  var ct = Buffer.concat([c.update(secret, \"utf8\"), c.final()]);\n  return { iv: iv.toString(\"hex\"), ct: ct.toString(\"hex\"), tag: c.getAuthTag().toString(\"hex\") };\n}\nfunction open(env, key) {\n  var d = crypto.createDecipheriv(\"aes-256-gcm\", crypto.createHash(\"sha256\").update(key).digest(), Buffer.from(env.iv, \"hex\"));\n  d.setAuthTag(Buffer.from(env.tag, \"hex\"));\n  return Buffer.concat([d.update(Buffer.from(env.ct, \"hex\")), d.final()]).toString(\"utf8\");\n}\nvar env = seal(\"db-password-42\", \"vault-key\");\nconsole.log(\"Vault model: $VAULT | Crypto: $CRYPTO\");\nconsole.log(\"Sealed bytes: \" + env.ct.length);\nconsole.log(\"Unseal round-trip: \" + (open(env, \"vault-key\") === \"db-password-42\" ? \"PASS\" : \"FAIL\"));";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["server", "SigVault-Core", "Signature-original: mesh-replicated vault with Shamir-shared master keys. It stores all secret classes using XChaCha20-Poly1305; access via sigvault CLI, API.", {"vault": "SigVault-Core", "stores": "all secret classes", "crypto": "XChaCha20-Poly1305", "access": "sigvault CLI, API"}], ["server", "SigVault-Edge", "Signature-original: edge vault replicas serving secrets with 5 ms latency budgets. It stores edge secrets using XChaCha20-Poly1305; access via local socket, mTLS.", {"vault": "SigVault-Edge", "stores": "edge secrets", "crypto": "XChaCha20-Poly1305", "access": "local socket, mTLS"}], ["file-based", "SigSeal-File", "Signature-original: file sealing with per-file keys wrapped by the vault master. It stores sealed files using envelope XChaCha20; access via sigseal CLI.", {"vault": "SigSeal-File", "stores": "sealed files", "crypto": "envelope XChaCha20", "access": "sigseal CLI"}], ["password-manager", "SigPass", "Signature-original: offline password database with mesh backup and duress codes. It stores passwords using Argon2id + XChaCha20; access via SigPass apps.", {"vault": "SigPass", "stores": "passwords", "crypto": "Argon2id + XChaCha20", "access": "SigPass apps"}], ["server", "SigRotate", "Signature-original: automatic rotation for DB and API credentials with dual-active windows. It stores rotated creds using provider-native; access via policy engine.", {"vault": "SigRotate", "stores": "rotated creds", "crypto": "provider-native", "access": "policy engine"}], ["server", "SigLease", "Signature-original: leased credentials expiring automatically with renewal workflows. It stores leased creds using ephemeral keys; access via lease API.", {"vault": "SigLease", "stores": "leased creds", "crypto": "ephemeral keys", "access": "lease API"}], ["tooling", "SigAudit", "Signature-original: every secret access logged to the append-only transparency ledger. It stores access logs using hash-chained; access via ledger queries.", {"vault": "SigAudit", "stores": "access logs", "crypto": "hash-chained", "access": "ledger queries"}], ["tooling", "SigBreakGlass", "Signature-original: break-glass access with multi-party approval and full recording. It stores emergency access using threshold shares; access via approval workflow.", {"vault": "SigBreakGlass", "stores": "emergency access", "crypto": "threshold shares", "access": "approval workflow"}], ["server", "SigHSM", "Signature-original: virtual HSM interface over enclave-backed key operations. It stores HSM keys using enclave ECDSA/Ed25519; access via PKCS#11.", {"vault": "SigHSM", "stores": "HSM keys", "crypto": "enclave ECDSA/Ed25519", "access": "PKCS#11"}], ["tooling", "SigCert", "Signature-original: 5-minute-lived certificates replacing most static secrets. It stores short-lived certs using Ed25519; access via ACME-like API.", {"vault": "SigCert", "stores": "short-lived certs", "crypto": "Ed25519", "access": "ACME-like API"}], ["tooling", "SigEnv", "Signature-original: secrets injected as memory-only env, never touching disk. It stores process secrets using memory-sealed; access via launcher.", {"vault": "SigEnv", "stores": "process secrets", "crypto": "memory-sealed", "access": "launcher"}], ["tooling", "SigShare", "Signature-original: secret sharing via Shamir splits across trusted devices. It stores shared secrets using Shamir + XChaCha20; access via device quorum.", {"vault": "SigShare", "stores": "shared secrets", "crypto": "Shamir + XChaCha20", "access": "device quorum"}], ["tooling", "SigDetect", "Signature-original: leaked-secret scanning across repos with automatic rotation. It stores detections using n/a; access via CI hooks.", {"vault": "SigDetect", "stores": "detections", "crypto": "n/a", "access": "CI hooks"}], ["server", "SigPolicy", "Signature-original: policy engine granting secrets by workload identity, not IP. It stores policies using signed policies; access via policy API.", {"vault": "SigPolicy", "stores": "policies", "crypto": "signed policies", "access": "policy API"}], ["server", "SigVault-One", "Signature-original: the united vault plane — one API for every secret class. It stores everything using unified envelope; access via sigvault one.", {"vault": "SigVault-One", "stores": "everything", "crypto": "unified envelope", "access": "sigvault one"}]];
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
  if(!new RegExp('^'+'JAH\\-ECV\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('encrypted-credential-vaults-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
