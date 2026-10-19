(function(){'use strict';
/* JAH Fundamentals of Cryptography Database generator — jahdb-fundamental-cryptography-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRY-";
var FIELDS=["classical ciphers", "symmetric encryption", "public-key cryptography", "hash functions", "digital signatures", "protocols"];
var TOPICS=[
    {t: "What Cryptography Promises", b: "Cryptography delivers confidentiality (no reading), integrity (no altering), and authenticity (right sender) \u2014 three distinct promises needing different tools."},
    {t: "Classical Ciphers", b: "Caesar shifts and substitution ciphers fall to frequency analysis: in English, E appears ~13% of the time, betraying every simple substitution."},
    {t: "Kerckhoffs's Principle", b: "A system must stay secure even when everything except the key is public \u2014 security through obscurity is not security."},
    {t: "Symmetric Encryption and AES", b: "One shared secret key encrypts and decrypts; AES-128/256 is the world standard, fast in hardware and trusted after decades of attack attempts."},
    {t: "Why Key Length Matters", b: "Each added bit doubles brute-force work: 128-bit keys need ~3.4\u00d710\u00b3\u2078 tries, physically infeasible even for planet-scale attackers."},
    {t: "Public-Key Cryptography", b: "Two mathematically linked keys \u2014 public for encrypting, private for decrypting \u2014 solve the key-distribution problem that symmetric crypto cannot."},
    {t: "RSA from First Principles", b: "RSA rests on the hardness of factoring: multiplying two large primes is easy, but recovering them from the product is believed infeasible."},
    {t: "Diffie-Hellman Key Exchange", b: "Two strangers can agree on a secret over a public channel by exchanging exponentiated values \u2014 eavesdroppers see only the public pieces."},
    {t: "Hash Functions", b: "SHA-256 compresses any input to 256 unpredictable bits; one-wayness and collision resistance make hashes the backbone of integrity checks."},
    {t: "Digital Signatures", b: "Sign with your private key, verify with your public key: signatures prove authorship and integrity for software, contracts, and certificates."},
    {t: "Certificates and PKI", b: "Certificate authorities bind public keys to identities, forming the trust chains that make HTTPS padlocks meaningful."},
    {t: "Quantum Threats and Post-Quantum Crypto", b: "Quantum computers threaten RSA and Diffie-Hellman; lattice-based and hash-based schemes are the standardized replacements being deployed now."}
];
var PRINCIPLES=[
    {n: "One-time pad", e: "C = P \u2295 K (|K| \u2265 |P|)", s: "A truly random key as long as the message gives mathematically unbreakable secrecy."},
    {n: "RSA relation", e: "c = m^e mod n; m = c^d mod n", s: "Encryption with the public exponent reverses exactly with the private exponent."},
    {n: "Hash avalanche", e: "flip 1 input bit \u2192 ~50% output bits change", s: "A secure hash scrambles every output bit when any input bit changes."}
];
var USES=["Securing web traffic with TLS", "Signing software updates", "Protecting stored passwords with salted hashes", "Building end-to-end encrypted messaging"];
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
    id:id, t:tp.t, g:field, name:"Cryptography"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Cryptography demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-cryptography-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-cryptography-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-cryptography",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
