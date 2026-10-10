(function(){'use strict';
/* JAH Cryptography Database generator — jahdb-cryptography-1.0.
   Deterministic client-side generator: same seed + same version = same record.
   Online-sourced profiles carry src:"online"; Signature-authored comparative
   studies carry src:"signature". All anchor facts are verifiable public facts. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['symmetric-cipher','asymmetric-cipher','hash-function','key-exchange','digital-signature','protocol','mode-of-operation','key-derivation','classical-cipher','post-quantum'];
var PREFIX='JAH-CRY-';
/* anchors: [title, cat, year, by(designer/origin), standard, fact sentences...] */
var ANCH=[
["AES","symmetric-cipher",2001,"Joan Daemen and Vincent Rijmen","FIPS-197",
 "AES (Advanced Encryption Standard) is a symmetric block cipher that works on 128-bit blocks with key sizes of 128, 192, or 256 bits.",
 "It was designed by Joan Daemen and Vincent Rijmen as Rijndael and adopted by NIST as FIPS-197 in 2001, replacing DES as the United States federal standard.",
 "The cipher runs 10, 12, or 14 rounds depending on key size, each round applying byte substitution, row shifting, column mixing, and round-key addition.",
 "AES is the most widely deployed block cipher in the world, protecting TLS web traffic, full-disk encryption, and wireless networks.",
 "No practical attack breaks full-round AES; the best known cryptanalysis only reaches reduced-round variants."],
["DES","symmetric-cipher",1977,"IBM (Horst Feistel's Lucifer team)","FIPS-46",
 "DES (Data Encryption Standard) is a 64-bit block cipher with a 56-bit effective key, built as a 16-round Feistel network.",
 "Developed from IBM's Lucifer cipher by Horst Feistel's team, it became the US federal standard FIPS-46 in 1977.",
 "Its short 56-bit key made brute-force attacks practical by the late 1990s: the EFF's Deep Crack machine broke a DES key in 56 hours in 1998.",
 "DES was withdrawn as a federal standard and survives only inside Triple-DES constructions in legacy systems."],
["Triple-DES","symmetric-cipher",1998,"ANSI X9.52 working group","FIPS-46-3",
 "Triple-DES applies the DES cipher three times in an encrypt-decrypt-encrypt sequence, giving an effective key strength of about 112 bits.",
 "It was standardized as a stopgap in FIPS-46-3 (1998) to extend the life of DES hardware while AES was being selected.",
 "NIST deprecated Triple-DES for new applications and disallowed it after 2023, directing migration to AES."],
["RSA","asymmetric-cipher",1977,"Ron Rivest, Adi Shamir, Leonard Adleman","PKCS#1",
 "RSA is a public-key cryptosystem whose security rests on the difficulty of factoring large integers.",
 "It was invented in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman at MIT and published in 1978.",
 "Typical key sizes are 2048, 3072, or 4096 bits; RSA is used for encryption, digital signatures, and certificate authentication.",
 "A 1994 paper by the inventors and the PKCS#1 standard defined padding schemes such as OAEP that keep RSA secure in practice."],
["Diffie-Hellman key exchange","key-exchange",1976,"Whitfield Diffie and Martin Hellman","RFC 2631 / RFC 7919",
 "The Diffie-Hellman protocol lets two parties agree on a shared secret over an insecure channel without any prior shared key.",
 "Published in 1976 in 'New Directions in Cryptography', it was the first public-key technique ever described.",
 "Its security depends on the discrete logarithm problem in a chosen group; standardized parameter sets appear in RFC 7919."],
["ElGamal","asymmetric-cipher",1985,"Taher Elgamal","—",
 "The ElGamal cryptosystem provides public-key encryption and signatures based on the discrete logarithm problem.",
 "Taher Elgamal published it in 1985; its signature variant directly inspired the US Digital Signature Standard (DSS).",
 "Encryption under ElGamal is randomized, so the same message encrypts to different ciphertexts each time."],
["Elliptic-curve cryptography","asymmetric-cipher",1985,"Neal Koblitz and Victor Miller","FIPS-186-4 / SEC 2",
 "Elliptic-curve cryptography (ECC) builds public-key systems on the algebraic structure of elliptic curves over finite fields.",
 "Proposed independently by Neal Koblitz and Victor Miller in 1985, it delivers RSA-equivalent security with far smaller keys: 256-bit ECC matches roughly 3072-bit RSA.",
 "Standard curves such as NIST P-256 and secp256k1 underpin TLS, Bitcoin, and modern secure messaging."],
["Ed25519","digital-signature",2011,"Daniel J. Bernstein and co-authors","RFC 8032",
 "Ed25519 is a digital signature scheme using the Edwards-curve Digital Signature Algorithm over Curve25519.",
 "Designed by Daniel J. Bernstein and colleagues and published in 2011, it produces compact 64-byte signatures with fast, side-channel-resistant implementations.",
 "It is standardized in RFC 8032 and widely used in OpenSSH, TLS 1.3, and software signing."],
["DSA","digital-signature",1991,"NIST","FIPS-186 (DSS)",
 "The Digital Signature Algorithm (DSA) was proposed by NIST in 1991 as part of the Digital Signature Standard.",
 "It is based on the discrete logarithm problem and the ElGamal signature scheme, using standardized domain parameters.",
 "DSA signatures are 320 bits for the classic 1024-bit parameter set; ECDSA extends the same idea to elliptic curves."],
["ChaCha20","symmetric-cipher",2008,"Daniel J. Bernstein","RFC 8439",
 "ChaCha20 is a stream cipher using a 256-bit key, a 96-bit nonce, and 20 rounds of ARX operations.",
 "Daniel J. Bernstein published it in 2008 as an improvement over Salsa20, with better diffusion per round.",
 "Paired with the Poly1305 authenticator, ChaCha20-Poly1305 is a mandatory cipher suite in TLS 1.3 and the default in WireGuard."],
["Blowfish","symmetric-cipher",1993,"Bruce Schneier","—",
 "Blowfish is a 64-bit block cipher with a variable key length from 32 to 448 bits and a 16-round Feistel structure.",
 "Bruce Schneier designed it in 1993 as a fast, unpatented alternative to DES, with an expensive key schedule that slows brute-force attacks.",
 "Its password-hashing derivative bcrypt remains a respected choice for storing password verifiers."],
["Twofish","symmetric-cipher",1998,"Bruce Schneier and co-authors","AES finalist",
 "Twofish is a 128-bit block cipher with 128, 192, or 256-bit keys and a 16-round Feistel network.",
 "Designed by Bruce Schneier's team, it was one of five finalists in the AES competition in 1998.",
 "It features key-dependent S-boxes and a maximum-distance-separable matrix for strong diffusion."],
["Serpent","symmetric-cipher",1998,"Ross Anderson, Eli Biham, Lars Knudsen","AES finalist",
 "Serpent is a 128-bit block cipher with 32 rounds, designed by Ross Anderson, Eli Biham, and Lars Knudsen.",
 "An AES finalist in 1998, it was judged the most conservative security margin of the candidates, trading speed for safety.",
 "Its 32 rounds give it a large cushion against differential and linear cryptanalysis."],
["Camellia","symmetric-cipher",2000,"Mitsubishi and NTT","RFC 3713 / ISO",
 "Camellia is a 128-bit block cipher with 128, 192, or 256-bit keys, jointly developed by Mitsubishi and NTT and published in 2000.",
 "It offers security and performance comparable to AES and is standardized in RFC 3713 and by ISO/IEC.",
 "Camellia is widely deployed in Japan and appears in TLS cipher suites and OpenSSL."],
["RC4","symmetric-cipher",1987,"Ron Rivest","—",
 "RC4 is a stream cipher designed by Ron Rivest in 1987, famous for its simplicity and speed in software.",
 "Statistical biases in its keystream led to practical attacks, most notably against WEP wireless encryption in 2001.",
 "RC4 is now prohibited in TLS (RFC 7465, 2015) and considered broken for security use."],
["SHA-1","hash-function",1993,"NSA","FIPS-180",
 "SHA-1 is a 160-bit cryptographic hash function published by the NSA as FIPS-180 in 1993.",
 "Theoretical weaknesses found in 2005 became practical in 2017, when Google and CWI Amsterdam demonstrated the SHAttered collision attack.",
 "SHA-1 is deprecated for digital signatures and certificates; migration to SHA-2 or SHA-3 is required."],
["SHA-2","hash-function",2001,"NSA","FIPS-180-4",
 "SHA-2 is a family of hash functions with 224, 256, 384, and 512-bit digests, published by the NSA in 2001 as FIPS-180.",
 "SHA-256 secures Bitcoin's proof of work, TLS certificates, and countless software integrity checks.",
 "No practical collision attack on full SHA-2 is known, though SHA-256 and SHA-512 share structure with the broken SHA-1."],
["SHA-3","hash-function",2015,"Guido Bertoni and co-authors (Keccak team)","FIPS-202",
 "SHA-3 is the Keccak sponge-construction hash function, selected by NIST in 2012 and standardized as FIPS-202 in 2015.",
 "Unlike SHA-2's Merkle-Damgard design, Keccak absorbs input into a state and squeezes out output, with variants SHA3-224 through SHA3-512.",
 "Its sponge design also yields the SHAKE extendable-output functions."],
["MD5","hash-function",1991,"Ron Rivest","RFC 1321",
 "MD5 is a 128-bit hash function designed by Ron Rivest in 1991 and specified in RFC 1321.",
 "Xiaoyun Wang's team demonstrated practical collisions in 2004, and chosen-prefix collisions followed in 2007.",
 "MD5 must not be used for security purposes such as signatures or certificates, though it survives as a non-cryptographic checksum."],
["BLAKE2","hash-function",2012,"Jean-Philippe Aumasson and co-authors","RFC 7693",
 "BLAKE2 is a cryptographic hash function designed for speed without sacrificing security, published in 2012.",
 "It runs faster than MD5 and SHA-2 in software while offering a security margin comparable to SHA-3 finalists.",
 "BLAKE2b and BLAKE2s are standardized in RFC 7693 and used in WireGuard and password-hashing designs."],
["HMAC","hash-function",1996,"Mihir Bellare, Ran Canetti, Hugo Krawczyk","RFC 2104 / FIPS-198",
 "HMAC is a construction that turns any cryptographic hash function into a message authentication code using a secret key.",
 "Proposed by Bellare, Canetti, and Krawczyk in 1996, it mixes the key with inner and outer padding around two hash passes.",
 "HMAC-SHA-256 remains a standard choice for API authentication and key derivation."],
["PBKDF2","key-derivation",2000,"RSA Laboratories (PKCS#5)","RFC 2898 / RFC 8018",
 "PBKDF2 is a password-based key derivation function that applies a pseudorandom function thousands of times to slow down guessing attacks.",
 "Published in PKCS#5 v2.0 (2000) and RFC 2898, it takes a password, salt, iteration count, and output length.",
 "High iteration counts (hundreds of thousands) are recommended since PBKDF2 is not memory-hard."],
["bcrypt","key-derivation",1999,"Niels Provos and David Mazieres","—",
 "bcrypt is an adaptive password-hashing function based on the Blowfish cipher's expensive key schedule.",
 "Designed by Niels Provos and David Mazieres in 1999 for OpenBSD, its cost factor scales the work as hardware improves.",
 "A unique salt per password defeats rainbow-table attacks, and bcrypt remains a respected default for password storage."],
["scrypt","key-derivation",2009,"Colin Percival","RFC 7914",
 "scrypt is a memory-hard password-based key derivation function designed by Colin Percival and presented in 2009.",
 "It deliberately requires large amounts of RAM, raising the cost of custom ASIC brute-force hardware.",
 "Standardized in RFC 7914, scrypt is used in Litecoin mining and several password managers."],
["Argon2","key-derivation",2015,"Alex Biryukov, Daniel Dinu, Dmitry Khovratovich","RFC 9106",
 "Argon2 won the Password Hashing Competition in 2015 and is the modern recommended password-hashing algorithm.",
 "Designed by Biryukov, Dinu, and Khovratovich, it offers data-dependent (Argon2d), data-independent (Argon2i), and hybrid (Argon2id) variants.",
 "It is standardized in RFC 9106 and resists both GPU and side-channel attacks when configured as Argon2id."],
["TLS 1.3","protocol",2018,"IETF TLS working group","RFC 8446",
 "TLS 1.3 is the 2018 revision of the Transport Layer Security protocol that encrypts web traffic, specified in RFC 8446.",
 "It removed insecure options including RSA key exchange, static Diffie-Hellman, RC4, and SHA-1, and mandates forward secrecy.",
 "The handshake completes in one round trip (or zero with resumption), cutting connection latency significantly."],
["IPsec","protocol",1998,"IETF IPsec working group","RFC 4301 series",
 "IPsec is a suite of protocols that encrypts and authenticates IP packets, forming the basis of most VPNs.",
 "Its Encapsulating Security Payload (ESP) provides confidentiality while the Internet Key Exchange (IKE) negotiates keys.",
 "The RFC 4301 series standardizes the architecture; IKEv2 (RFC 7296) simplified the key exchange."],
["PGP / OpenPGP","protocol",1991,"Phil Zimmermann","RFC 4880",
 "Pretty Good Privacy (PGP), written by Phil Zimmermann in 1991, brought strong public-key encryption to ordinary email users.",
 "Its web-of-trust model lets users certify each other's keys without a central authority.",
 "The OpenPGP format is standardized in RFC 4880 and implemented by GnuPG."],
["X.509 certificates","protocol",1988,"ITU-T","RFC 5280",
 "X.509 defines the format of public-key certificates binding an identity to a public key, first published in 1988.",
 "Certificate profiles for the internet are specified in RFC 5280; browsers validate chains up to trusted root authorities.",
 "Certificate Transparency (RFC 6962, 2013) requires public logging of certificates to detect mis-issuance."],
["One-time pad","classical-cipher",1917,"Gilbert Vernam","—",
 "The one-time pad encrypts each message bit with a random key bit used exactly once, a scheme patented by Gilbert Vernam in 1917.",
 "Claude Shannon proved in 1949 that it offers perfect secrecy when the key is truly random, as long as the message, and never reused.",
 "Its impractical key-distribution demands confine it to ultra-high-security links such as diplomatic hotlines."],
["Enigma","classical-cipher",1918,"Arthur Scherbius","—",
 "The Enigma was a rotor-based cipher machine patented by Arthur Scherbius in 1918 and adopted by the German military.",
 "Polish mathematicians broke early versions in 1932; at Bletchley Park, Alan Turing's team mechanized the break with the Bombe.",
 "The Ultra intelligence from broken Enigma traffic is credited with shortening World War II by years."],
["Vigenere cipher","classical-cipher",1553,"Giovan Battista Bellaso","—",
 "The Vigenere cipher encrypts text with a repeating keyword, shifting each letter by the corresponding key letter.",
 "Described by Giovan Battista Bellaso in 1553 and misattributed to Blaise de Vigenere, it resisted cryptanalysis for 300 years.",
 "Charles Babbage broke it around 1854 and Friedrich Kasiski published the method in 1863, ending its use for serious secrecy."],
["Caesar cipher","classical-cipher",-50,"Gaius Julius Caesar","—",
 "The Caesar cipher shifts each letter of the alphabet by a fixed number of positions, the classic example being a shift of three.",
 "Suetonius records that Julius Caesar used it for military correspondence around 50 BCE.",
 "With only 25 possible shifts it is trivially broken, but it remains the standard first example in cryptography teaching."],
["Playfair cipher","classical-cipher",1854,"Charles Wheatstone","—",
 "The Playfair cipher encrypts pairs of letters (digraphs) using a 5x5 key square, invented by Charles Wheatstone in 1854.",
 "Named for Lord Playfair who promoted it, it was used by British forces in the Boer War and World War I for tactical messages.",
 "Encrypting digraphs instead of single letters defeats simple frequency analysis."],
["Kerckhoffs's principle","classical-cipher",1883,"Auguste Kerckhoffs","—",
 "Kerckhoffs's principle states that a cryptosystem must remain secure even if everything about it is public except the key.",
 "Auguste Kerckhoffs published it in 1883 in 'La Cryptographie Militaire'; Claude Shannon restated it as 'the enemy knows the system'.",
 "It is the philosophical foundation of modern open cryptographic standards."],
["AES-GCM","mode-of-operation",2007,"John Viega and David McGrew","NIST SP 800-38D",
 "Galois/Counter Mode (GCM) turns AES into an authenticated encryption scheme providing both confidentiality and integrity.",
 "Proposed by John Viega and David McGrew, it was standardized by NIST in SP 800-38D (2007).",
 "GCM is the dominant mode in TLS 1.3 because it is fast, parallelizable, and produces an authentication tag with each message."],
["CBC mode","mode-of-operation",1976,"IBM / NIST","FIPS-81 / SP 800-38A",
 "Cipher Block Chaining (CBC) xors each plaintext block with the previous ciphertext block before encryption.",
 "Standardized in FIPS-81, CBC needs an unpredictable initialization vector; predictable IVs enabled the BEAST attack on TLS.",
 "CBC provides no integrity on its own and must be paired with a MAC in an encrypt-then-MAC construction."],
["CTR mode","mode-of-operation",1979,"—","SP 800-38A",
 "Counter mode turns a block cipher into a stream cipher by encrypting successive counter values.",
 "It is fully parallelizable for both encryption and decryption and needs no padding.",
 "A nonce must never repeat under the same key, or the keystream repeats and confidentiality collapses."],
["ECB mode","mode-of-operation",1976,"—","FIPS-81",
 "Electronic Codebook (ECB) encrypts each block independently with the same key.",
 "Identical plaintext blocks produce identical ciphertext blocks, famously leaking image patterns in the ECB penguin demonstration.",
 "ECB is unsuitable for encrypting more than one block of structured data."],
["Shor's algorithm","post-quantum",1994,"Peter Shor","—",
 "Shor's algorithm factors integers and solves discrete logarithms in polynomial time on a quantum computer.",
 "Published by Peter Shor in 1994, it would break RSA, Diffie-Hellman, and elliptic-curve cryptography if a large fault-tolerant quantum computer existed.",
 "The threat of 'harvest now, decrypt later' attacks is driving migration to post-quantum cryptography today."],
["Grover's algorithm","post-quantum",1996,"Lov Grover","—",
 "Grover's algorithm searches an unsorted database of N items in about sqrt(N) quantum steps, a quadratic speedup over classical brute force.",
 "Published by Lov Grover in 1996, it halves the effective security of symmetric keys: AES-128 offers about 64 bits of quantum security.",
 "Doubling key sizes (AES-256) restores the margin, which is why symmetric cryptography is considered quantum-survivable."],
["ML-KEM","post-quantum",2024,"NIST (from CRYSTALS-Kyber team)","FIPS-203",
 "ML-KEM is NIST's post-quantum key-encapsulation standard, published as FIPS-203 on 13 August 2024.",
 "Derived from the CRYSTALS-Kyber submission, it is based on the module learning-with-errors lattice problem.",
 "It offers ML-KEM-512, 768, and 1024 parameter sets at NIST security levels 1, 3, and 5, and is the default PQC choice for key establishment."],
["ML-DSA","post-quantum",2024,"NIST (from CRYSTALS-Dilithium team)","FIPS-204",
 "ML-DSA is NIST's post-quantum digital signature standard, published as FIPS-204 on 13 August 2024.",
 "Derived from CRYSTALS-Dilithium, it rests on module lattice problems (Module-LWE and Module-SIS).",
 "With parameter sets ML-DSA-44, 65, and 87, it is the default post-quantum signature for new systems."],
["SLH-DSA","post-quantum",2024,"NIST (from SPHINCS+ team)","FIPS-205",
 "SLH-DSA is NIST's stateless hash-based signature standard, published as FIPS-205 on 13 August 2024.",
 "Derived from SPHINCS+, its security depends only on hash functions, making it a conservative hedge if lattice assumptions ever weaken.",
 "Signatures are larger and slower than ML-DSA's, so it serves as a backup rather than the default."],
["NIST PQC competition","post-quantum",2024,"NIST","FIPS-203/204/205",
 "NIST's post-quantum cryptography standardization ran from a 2016 call for proposals through final standards in August 2024.",
 "Eighty-two submissions entered; after three rounds, Kyber, Dilithium, Falcon, and SPHINCS+ were selected in 2022.",
 "The process famously eliminated SIKE in 2022 after a classical attack broke it completely, proving the value of long public review."],
["Curve25519","asymmetric-cipher",2006,"Daniel J. Bernstein","RFC 7748",
 "Curve25519 is an elliptic curve designed by Daniel J. Bernstein in 2006 for fast, secure Diffie-Hellman key exchange.",
 "It offers about 128 bits of security with 32-byte keys and was engineered to avoid implementation pitfalls.",
 "Its Diffie-Hellman function X25519 is standardized in RFC 7748 and used in TLS 1.3, Signal, and SSH."],
["Poly1305","hash-function",2005,"Daniel J. Bernstein","RFC 8439",
 "Poly1305 is a one-time message authenticator designed by Daniel J. Bernstein, evaluated modulo the prime 2^130-5.",
 "Paired with ChaCha20, it forms the ChaCha20-Poly1305 authenticated encryption suite in RFC 8439.",
 "It is fast in software and avoids the timing side channels that plague some table-driven MACs."],
["Let's Encrypt","protocol",2016,"Internet Security Research Group","—",
 "Let's Encrypt is a free, automated certificate authority run by the Internet Security Research Group, launched in 2016.",
 "Its ACME protocol automates domain validation and issuance, removing cost and manual effort from TLS deployment.",
 "It has issued billions of certificates and pushed HTTPS adoption past 90 percent of web traffic."],
["Merkle tree","hash-function",1979,"Ralph Merkle","—",
 "A Merkle tree hashes data blocks pairwise up a tree so a single root hash commits to the entire dataset.",
 "Ralph Merkle patented the structure in 1979; it lets verifiers check one block with only logarithmic proof size.",
 "Merkle trees underpin blockchains, Certificate Transparency logs, and distributed file systems."],
["Zero-knowledge proofs","asymmetric-cipher",1985,"Shafi Goldwasser, Silvio Micali, Charles Rackoff","—",
 "Zero-knowledge proofs let one party prove a statement true without revealing anything beyond the statement itself.",
 "Introduced by Goldwasser, Micali, and Rackoff in 1985, the concept underlies zk-SNARKs used in privacy-preserving blockchains.",
 "Practical systems now prove correct computation for rollups, identity, and confidential transactions."],
["Homomorphic encryption","asymmetric-cipher",2009,"Craig Gentry","—",
 "Homomorphic encryption allows computation directly on encrypted data without decrypting it first.",
 "Craig Gentry published the first fully homomorphic scheme in his 2009 Stanford dissertation, based on ideal lattices.",
 "Modern schemes like BGV, BFV, and CKKS make private cloud computation and encrypted machine learning practical research areas."]
];
var ANGLES=["technical profile","historical profile","deployment profile","security analysis"];
var SYNREL=[
 ["compared with","This Signature comparative study sets the two side by side on design, security margin, and real-world use."],
 ["contrasted against","This Signature contrast study highlights where the two designs diverge in assumptions and guarantees."],
 ["as predecessor and successor to","This Signature lineage study traces how the later design answers the earlier one's weaknesses."],
 ["alongside","This Signature pairing study examines the two together as complementary tools in real systems."]
];
function filedLine(id){return "Filed as "+id+" in the JAH Cryptography Database archive.";}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var pool=ANCH;
  if(opts.category){var f=ANCH.filter(function(a){return a[1]===opts.category;});if(f.length)pool=f;}
  var synth=!opts.category&&rnd()<0.38;
  if(synth){
    var A=pick(pool,rnd),B=pick(pool,rnd),guard=0;
    while(B===A&&guard++<20)B=pick(pool,rnd);
    var rel=pick(SYNREL,rnd);
    var title="Signature study: "+A[0]+" "+rel[0]+" "+B[0];
    var d=A[2]+" — "+A[0]+": "+A[5]+" "+rel[0]+" "+B[0]+" ("+B[2]+"), "+rel[1]+" "+B[5];
    var rec={id:id,title:title,description:d+" "+filedLine(id),category:"post-quantum"===A[1]||"post-quantum"===B[1]?"post-quantum":A[1],
      spec:{kind:"study",pair:[A[0],B[0]],relation:rel[0],years:[A[2],B[2]],src:"signature"},
      year:Math.max(A[2],B[2]),src:"signature"};
    return rec;
  }
  var A=pick(pool,rnd);
  var ang=pick(ANGLES,rnd);
  var facts=A.slice(5);
  var d=facts[0]+" "+pick(facts.slice(1),rnd);
  if(rnd()<0.6)d+=" "+pick(facts.slice(1),rnd);
  var title=A[0]+" — "+ang;
  return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
    spec:{kind:A[1],year:A[2],by:A[3],std:A[4],src:"online"},year:A[2],src:"online",_facts:facts,_an:A[0]};
}
function sentences(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>10;}).length;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-CRY-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  else if(sentences(r.description)<2)e.push('description-sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  if(typeof r.year!=='number'||r.year<-3000||r.year>2026)e.push('year');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(s.src!=='online'&&s.src!=='signature')e.push('spec.src');
    if(s.src!==r.src)e.push('spec.src-mismatch');
    if(s.src==='online'){
      if(typeof s.year!=='number'||s.year<-3000||s.year>2026)e.push('spec.year');
      if(typeof s.by!=='string'||!s.by.length)e.push('spec.by');
      if(typeof s.std!=='string')e.push('spec.std');
    }else if(s.kind==='signature-version'){
      if(typeof s.of!=='string'||!s.of.length)e.push('spec.of');
    }else{
      if(!Array.isArray(s.pair)||s.pair.length!==2)e.push('spec.pair');
      if(typeof s.relation!=='string'||!s.relation.length)e.push('spec.relation');
    }
  }
  return{ok:!e.length,errors:e};
}

var SIG_T=[
 "Signature reading of {N}: {F1}",
 "Held in the Signature system as a governed Signature version, this record preserves the fact-checked core whole \u2014 nothing is reduced. {F2}",
 "Signature assessment: {N} is cross-referenced against the archive's related records, so the fact-checked original and its Signature version travel together. Property of Justin Addam Higgins."
];
function sigFill(t,m){return t.replace(/\{N\}|\{F1\}|\{F2\}/g,function(k){return m[k]||'';});}
function signatureVersion(seed){
  var base=generate(seed,{},prng(seed));
  if(!base||base.src!=='online')return null;
  var facts=(base._facts&&base._facts.length)?base._facts:[base.description];
  var N=base._an||base.title;
  var F1=facts[0],F2=facts.length>1?facts[1+((seed%(facts.length-1))|0)]:facts[0];
  var map={'{N}':N,'{F1}':F1,'{F2}':F2};
  var d=sigFill(SIG_T[0],map)+" "+sigFill(SIG_T[1],map)+" "+sigFill(SIG_T[2],map);
  var sv={id:base.id,_seed:seed,title:"Signature version: "+N,description:d,category:base.category,
    spec:{kind:"signature-version",of:base.id,src:"signature"},src:"signature"};
  Object.keys(base).forEach(function(k){
    if(k.charAt(0)==='_'||k==='id'||k==='title'||k==='description'||k==='category'||k==='spec'||k==='src')return;
    sv[k]=base[k];
  });
  return sv;
}
var gen={version:'jahdb-cryptography-1.0',generate:generate,validate:validate,signatureVersion:signatureVersion};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cryptography',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
