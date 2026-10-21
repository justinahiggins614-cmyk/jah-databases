(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["server", "password-manager", "cloud", "file-based", "tooling"];
var PREFIX='JAH-ECV-';
var GENVER='jahdb-encrypted-credential-vaults-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["vault", "stores", "crypto", "access"];
var DEMO_TPL="// $TITLE - envelope encryption demo\nvar crypto = require(\"crypto\");\nfunction seal(secret, key) {\n  var iv = crypto.randomBytes(12);\n  var c = crypto.createCipheriv(\"aes-256-gcm\", crypto.createHash(\"sha256\").update(key).digest(), iv);\n  var ct = Buffer.concat([c.update(secret, \"utf8\"), c.final()]);\n  return { iv: iv.toString(\"hex\"), ct: ct.toString(\"hex\"), tag: c.getAuthTag().toString(\"hex\") };\n}\nfunction open(env, key) {\n  var d = crypto.createDecipheriv(\"aes-256-gcm\", crypto.createHash(\"sha256\").update(key).digest(), Buffer.from(env.iv, \"hex\"));\n  d.setAuthTag(Buffer.from(env.tag, \"hex\"));\n  return Buffer.concat([d.update(Buffer.from(env.ct, \"hex\")), d.final()]).toString(\"utf8\");\n}\nvar env = seal(\"db-password-42\", \"vault-key\");\nconsole.log(\"Vault model: $VAULT | Crypto: $CRYPTO\");\nconsole.log(\"Sealed bytes: \" + env.ct.length);\nconsole.log(\"Unseal round-trip: \" + (open(env, \"vault-key\") === \"db-password-42\" ? \"PASS\" : \"FAIL\"));";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["server", "HashiCorp Vault", "The reference secrets server with dynamic credentials, leasing, and revocation. It stores API keys, certs, dynamic DB creds using AES-256-GCM / Shamir seal; access via HTTP API, CLI, agents.", {"vault": "HashiCorp Vault", "stores": "API keys, certs, dynamic DB creds", "crypto": "AES-256-GCM / Shamir seal", "access": "HTTP API, CLI, agents"}], ["password-manager", "1Password", "End-to-end encrypted password management with Secret Automation for teams. It stores passwords, keys, notes using AES-256-GCM, XChaCha20; access via apps, CLI (op), Connect API.", {"vault": "1Password", "stores": "passwords, keys, notes", "crypto": "AES-256-GCM, XChaCha20", "access": "apps, CLI (op), Connect API"}], ["password-manager", "Bitwarden", "Open-source password manager with self-hostable server and audited clients. It stores passwords, cards, identities using AES-256-CBC + PBKDF2; access via apps, CLI (bw), web.", {"vault": "Bitwarden", "stores": "passwords, cards, identities", "crypto": "AES-256-CBC + PBKDF2", "access": "apps, CLI (bw), web"}], ["password-manager", "KeePass", "Offline-first encrypted database files (.kdbx) with Argon2 key derivation. It stores password databases using AES/ChaCha20 + Argon2; access via desktop apps.", {"vault": "KeePass", "stores": "password databases", "crypto": "AES/ChaCha20 + Argon2", "access": "desktop apps"}], ["cloud", "AWS Secrets Manager", "Managed rotation for RDS and custom secrets with IAM-scoped access. It stores DB creds, API keys using KMS envelope encryption; access via AWS SDK, IAM.", {"vault": "AWS Secrets Manager", "stores": "DB creds, API keys", "crypto": "KMS envelope encryption", "access": "AWS SDK, IAM"}], ["cloud", "Azure Key Vault", "FIPS-validated HSM-backed vault for keys, secrets, and certificates. It stores keys, secrets, certs using HSM-backed AES/RSA; access via Azure SDK, RBAC.", {"vault": "Azure Key Vault", "stores": "keys, secrets, certs", "crypto": "HSM-backed AES/RSA", "access": "Azure SDK, RBAC"}], ["cloud", "GCP Secret Manager", "Global secret storage with versioning and rotation schedules built in. It stores API keys, configs using Google KMS envelope; access via gcloud, SDK, IAM.", {"vault": "GCP Secret Manager", "stores": "API keys, configs", "crypto": "Google KMS envelope", "access": "gcloud, SDK, IAM"}], ["file-based", "age", "A modern, minimal file-encryption tool by Filippo Valsorda replacing PGP for files. It stores encrypted files using X25519 + ChaCha20-Poly1305; access via CLI.", {"vault": "age", "stores": "encrypted files", "crypto": "X25519 + ChaCha20-Poly1305", "access": "CLI"}], ["file-based", "sops", "Encrypts values inside YAML/JSON so configs stay diffable while secrets stay sealed. It stores encrypted config values using PGP/age/KMS envelope; access via CLI, editor plugins.", {"vault": "sops (Mozilla)", "stores": "encrypted config values", "crypto": "PGP/age/KMS envelope", "access": "CLI, editor plugins"}], ["file-based", "pass", "The standard unix password manager: GPG-encrypted files in a git repo. It stores password files using GPG; access via CLI.", {"vault": "pass", "stores": "password files", "crypto": "GPG", "access": "CLI"}], ["server", "Doppler", "Secrets-as-a-service syncing to CI, Kubernetes, and serverless with audit logs. It stores env secrets using AES-256-GCM envelope; access via dashboard, CLI, API.", {"vault": "Doppler", "stores": "env secrets", "crypto": "AES-256-GCM envelope", "access": "dashboard, CLI, API"}], ["server", "Infisical", "Open-source secrets platform with Kubernetes operators and dynamic secrets. It stores env secrets, certs using AES-256-GCM; access via dashboard, CLI, API.", {"vault": "Infisical", "stores": "env secrets, certs", "crypto": "AES-256-GCM", "access": "dashboard, CLI, API"}], ["server", "CyberArk", "Enterprise privileged-access vaulting with session isolation and rotation. It stores privileged creds using AES-256, HSM option; access via PVWA, API.", {"vault": "CyberArk", "stores": "privileged creds", "crypto": "AES-256, HSM option", "access": "PVWA, API"}], ["tooling", "Smallstep step-ca", "An open-source private CA issuing short-lived certs instead of long-lived secrets. It stores certificates using ECDSA/Ed25519; access via step CLI, ACME.", {"vault": "step-ca", "stores": "certificates", "crypto": "ECDSA/Ed25519", "access": "step CLI, ACME"}], ["tooling", "teller", "A secrets-to-environment injector pulling from many vaults into process env. It stores env injection using provider-native; access via CLI.", {"vault": "teller", "stores": "env injection", "crypto": "provider-native", "access": "CLI"}]];
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
  if(!new RegExp('^'+'JAH\\-ECV\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('encrypted-credential-vaults',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
