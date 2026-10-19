#!/usr/bin/env python3
"""Entries for The Unsolved Cryptography Database (unsolved-cryptography) and its
Signature half (unsolved-cryptography-signature).

34 famous unsolved problems in cryptography, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USCR- / JAH-USCRS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "cryptography",
 "disp": "cryptography",
 "name": "The Unsolved Cryptography Database",
 "sig_name": "The Unsolved Cryptography Signature Database",
 "prefix": "JAH-USCR-",
 "sig_prefix": "JAH-USCRS-",
 "ai": "JAH Unsolved Cryptography Archivist",
 "tagline": ("Thirty-four famous open problems in cryptography, from factoring to the unified theory of secrets: "
             "real, fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of cryptography: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in cryptography, real and fact-checked: integer "
              "factorization, discrete logarithms, RSA, Diffie-Hellman, elliptic curves, hash collisions, random "
              "oracles, key distribution, perfect secrecy, pseudorandom generators, and zero knowledge - every "
              "record carrying the problem statement, background, why it matters, key points, requirements, "
              "standards, citations, and a working solution-explorer demonstration, organized in the Signature "
              "system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "cryptography problems approached as a covenant between the known and the unknown, each carrying "
              "the full Signature-generated proposed solution with its assumptions declared, its confirm and "
              "refute conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never "
              "presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (factorization, discrete log, RSA, "
                 "Diffie-Hellman, elliptic curves, hash collisions, random oracles, key distribution, perfect "
                 "secrecy, pseudorandom generators, zero knowledge) -> Compounded (post-quantum, lattice "
                 "problems, learning with errors, homomorphic encryption, obfuscation, multilinear maps, "
                 "functional encryption, multiparty computation, zk scalability, quantum key distribution, side "
                 "channels, randomness generation) -> Advanced (one-way functions, public-key existence, "
                 "minicrypt vs cryptomania, white-box crypto, searchable encryption, blockchain scalability, "
                 "Byzantine consensus, proof-of-stake security, cryptographic agility, unified cryptography)."),
 "search_ph": ("Search factoring, RSA, zero knowledge, post-quantum, homomorphic encryption, obfuscation, "
               "blockchain..."),
 "chat_ph": "Ask about the great open problems of cryptography...",
 "greet_pub": ("I am the JAH Unsolved Cryptography Archivist. Ask me about the great open problems of "
               "cryptography - from factoring, RSA, and zero knowledge through post-quantum and homomorphic "
               "encryption, to blockchains, consensus, and the unified theory of secrets."),
 "greet_sig": ("I am the JAH Unsolved Cryptography Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of cryptography - every approach labeled as a proposal, "
               "never established science."),
 "role_pub": ("unsolved cryptography archivist - the great open problems of cryptography, from factoring, RSA, "
              "and zero knowledge through post-quantum and homomorphic encryption, to blockchains, consensus, "
              "and the unified theory of secrets; teaches progressively along the ladder from foundations "
              "through compounded to advanced; answers from many angles - definition, example, analogy, "
              "application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved cryptography archivist - Signature editions: his original Signature solution method "
              "applied to the 34 great open problems of cryptography, each carrying the full Signature-generated "
              "proposed solution, clearly labeled Signature-made and never presented as established science; "
              "teaches progressively along the ladder from foundations through compounded to advanced; answers "
              "from many angles - definition, example, analogy, application, history, math - using only archive "
              "data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved cryptography studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Katz and Lindell, Introduction to Modern Cryptography; Menezes, van Oorschot, and Vanstone, Handbook of Applied Cryptography).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "cr-factoring",
 "name": "The Integer Factorization Problem",
 "group": "Foundations",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Multiplying primes is easy, factoring the product is hard - but how hard, exactly, and is there a faster classical algorithm?",
 "background": "The factoring problem - the RSA security assumption - has the number-field sieve (subexponential) as the best classical algorithm; no polynomial classical algorithm is known, but none is proven impossible. Shor's quantum algorithm factors in polynomial time - the quantum threat. The hardness is assumed, not proven: factoring might be easy classically (unlikely but unproven). RSA's security rests on the unproven hardness.",
 "why_it_matters": "RSA secures the internet. Its unproven hardness assumption is the ecommerce foundation's unproven lemma.",
 "sig_lens": "The Signature lens reads factoring as the locked safe: the protocol must know the lock's true strength - by cryptanalysis, not assumption.",
 "sig_solution": LABEL + " Assumptions: (1) no polynomial classical algorithm known or ruled out; (2) Shor threatens quantumly. Reasoning path: quantify the hardness - continued cryptanalysis plus quantum-readiness migration. Proposed mechanism: a safe protocol with factoring-challenge cryptanalysis, hardness-assumption monitoring, and post-quantum migration for long-lived secrets. Confirm: the hardness holds or falls by analysis. Kill: a classical polynomial algorithm appears. Does NOT claim: factoring hard - it tests the lock.",
 "pointer": "The Signature system's proposed approach quantifies factoring hardness with cryptanalysis and migration; the companion Signature Edition record specifies the safe protocol.",
 "key_points": [
  "Number-field sieve: best classical, subexponential.",
  "No polynomial classical algorithm known or excluded.",
  "Shor's quantum algorithm is polynomial.",
  "RSA rests on unproven hardness.",
 ],
 "requirements": [
  "Continued factoring cryptanalysis.",
  "Hardness-assumption monitoring.",
  "Post-quantum migration planning.",
 ],
 "citations": [
  "Rivest RL et al. (1978) A method for obtaining digital signatures and public-key cryptosystems. CACM 21.",
 ],
 "demo": {"p": 23, "g": 5, "a": 6, "b": 15},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "cr-dlog",
 "name": "The Discrete Logarithm Problem",
 "group": "Foundations",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Exponentiation is easy, the discrete log is hard - but in which groups, and how do the index-calculus advances change the parameters?",
 "background": "The discrete-log problem - Diffie-Hellman's foundation - varies by group: finite-field DLP fell to quasi-polynomial advances (Joux's work on small characteristic); prime-field DLP needs ever-larger keys (NFS-DL); elliptic-curve DLP stands (no subexponential attack). The group choice is the security: the same problem, different hardness. The parameter guidance (key sizes) chases the cryptanalysis.",
 "why_it_matters": "Diffie-Hellman and ElGamal rest on discrete logs. The group-dependent hardness is the parameter bible.",
 "sig_lens": "The Signature lens reads discrete logs as the group-dependent lock: the protocol must pick the group whose lock has survived the cryptanalysts - and size it ahead of them.",
 "sig_solution": LABEL + " Assumptions: (1) hardness group-dependent; (2) index calculus advanced on finite fields. Reasoning path: standardize on the surviving groups (elliptic curves, large prime fields) with ahead-of-cryptanalysis sizing. Proposed mechanism: a lock protocol with group-hardness monitoring, conservative parameter standards, and elliptic-curve migration. Confirm: the chosen groups resist. Kill: an elliptic-curve subexponential attack. Does NOT claim: discrete logs hard - it picks the surviving locks.",
 "pointer": "The Signature system's proposed approach standardizes discrete-log groups ahead of cryptanalysis; the companion Signature Edition record specifies the lock protocol.",
 "key_points": [
  "Finite-field DLP weakened by index calculus.",
  "Prime-field DLP needs growing keys.",
  "Elliptic-curve DLP: no subexponential attack.",
  "Same problem, group-dependent hardness.",
 ],
 "requirements": [
  "Group-hardness cryptanalysis monitoring.",
  "Conservative parameter standards.",
  "Elliptic-curve migration.",
 ],
 "citations": [
  "Diffie W, Hellman M (1976) New directions in cryptography. IEEE Trans. Info. Theory 22.",
 ],
 "demo": {"p": 29, "g": 2, "a": 8, "b": 12},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "cr-rsa-problem",
 "name": "The RSA Problem",
 "group": "Foundations",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Breaking RSA might be easier than factoring - but is the RSA problem (eth roots mod N) really as hard as factoring?",
 "background": "The RSA problem - computing e-th roots modulo N without the factors - might be easier than factoring: no reduction from factoring to RSA-breaking is known (beyond special cases). The assumption (RSA hard even if factoring easy-ish) is standard but unproven. The padding schemes (OAEP) add their assumptions. RSA's exact hardness is the unproven middle: harder than nothing, possibly easier than factoring.",
 "why_it_matters": "RSA encryption's precise assumption is unproven. The gap between RSA-breaking and factoring is the security's gray zone.",
 "sig_lens": "The Signature lens reads the RSA problem as the gray zone: the protocol must not assume the zone is safe - it must bound it by the factoring it can measure.",
 "sig_solution": LABEL + " Assumptions: (1) no factoring-to-RSA reduction; (2) OAEP adds assumptions. Reasoning path: bound RSA security by factoring hardness - size keys for the factoring threat, the measurable one. Proposed mechanism: a zone protocol with RSA-key sizing on factoring estimates, padding-scheme provable-security requirements, and RSA-phaseout planning. Confirm: the bounds hold. Kill: an RSA-break below factoring. Does NOT claim: RSA as hard as factoring - it bounds the gray zone.",
 "pointer": "The Signature system's proposed approach bounds RSA security on factoring hardness; the companion Signature Edition record specifies the zone protocol.",
 "key_points": [
  "RSA problem: e-th roots mod N.",
  "May be easier than factoring; unproven either way.",
  "No general factoring-to-RSA reduction.",
  "OAEP padding adds assumptions.",
 ],
 "requirements": [
  "RSA sizing on factoring estimates.",
  "Provable-security padding requirements.",
  "RSA phaseout planning.",
 ],
 "citations": [
  "Boneh D, Venkatesan R (1998) Breaking RSA may not be equivalent to factoring. Eurocrypt.",
 ],
 "demo": {"p": 31, "g": 3, "a": 7, "b": 11},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "cr-dh-problem",
 "name": "The Diffie Hellman Problem",
 "group": "Foundations",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Diffie-Hellman key exchange might be breakable without solving discrete logs - but is the computational Diffie-Hellman assumption tight?",
 "background": "The DH problem - computing g^ab from g^a, g^b - sits between discrete log and decisional DH: the CDH assumption (hard) underlies key exchange; the DDH assumption (indistinguishability) underlies ElGamal. The gaps (CDH easier than DLP? DDH vs CDH separations) are mostly unproven. The key exchange's exact assumption is the unproven middle - like RSA's.",
 "why_it_matters": "Diffie-Hellman is the key-exchange workhorse. Its assumption's tightness is the exchange's gray zone.",
 "sig_lens": "The Signature lens reads DH as the gray zone again: the protocol must size for the discrete log (measurable) - and prefer the assumptions with proofs.",
 "sig_solution": LABEL + " Assumptions: (1) CDH/DDH gaps unproven; (2) DLP the measurable hardness. Reasoning path: size on DLP, prefer DDH-proven constructions where available. Proposed mechanism: a zone protocol with DLP-based parameter sizing, assumption-explicit protocol design, and quantum-migration for key exchange. Confirm: the assumptions hold. Kill: a CDH-break below DLP. Does NOT claim: DH tight - it sizes on the measurable.",
 "pointer": "The Signature system's proposed approach sizes Diffie-Hellman on discrete-log hardness; the companion Signature Edition record specifies the zone protocol.",
 "key_points": [
  "CDH: computing g^ab; DDH: distinguishing.",
  "Gaps between CDH, DDH, DLP unproven.",
  "Key exchange rests on CDH.",
  "ElGamal rests on DDH.",
 ],
 "requirements": [
  "DLP-based parameter sizing.",
  "Assumption-explicit protocol design.",
  "Post-quantum key-exchange migration.",
 ],
 "citations": [
  "Boneh D (1998) The decision Diffie-Hellman problem. ANTS.",
 ],
 "demo": {"p": 37, "g": 2, "a": 9, "b": 14},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "cr-ecdlp",
 "name": "The Elliptic Curve Discrete Log Problem",
 "group": "Foundations",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Elliptic curves give the hardest discrete logs per bit - but are the standard curves trustworthy, and is the ECDLP really exponential?",
 "background": "The ECDLP problem - no subexponential attack known - makes ECC efficient: but the standard curves (NIST P-256's unexplained seeds) raised trust questions; the twist-security and invalid-curve attacks exploited implementations; and the quantum threat (Shor) breaks ECC too. The curve generation (verifiably random vs performance) is the trust debate. The hardest-per-bit lock has the most-trusted-curve question.",
 "why_it_matters": "ECC secures mobile and embedded systems. The curve-trust question is the efficient lock's legitimacy.",
 "sig_lens": "The Signature lens reads ECC as the efficient lock with trust issues: the protocol must use verifiably-generated curves - and plan the quantum exit.",
 "sig_solution": LABEL + " Assumptions: (1) ECDLP exponential classically; (2) curve seeds questioned. Reasoning path: standardize verifiably-random curves (the SafeCurves criteria) with quantum-migration plans. Proposed mechanism: a trust protocol with rigid-curve standards, implementation-security requirements, and post-quantum ECC migration. Confirm: the rigid curves trusted and used. Kill: an ECDLP subexponential attack. Does NOT claim: ECDLP hard - it trusts but verifies the curves.",
 "pointer": "The Signature system's proposed approach standardizes rigid elliptic curves with quantum migration; the companion Signature Edition record specifies the trust protocol.",
 "key_points": [
  "ECDLP: no subexponential attack known.",
  "NIST curve seeds unexplained; trust questioned.",
  "Twist/invalid-curve attacks hit implementations.",
  "Shor breaks ECC quantumly.",
 ],
 "requirements": [
  "Verifiably-random (rigid) curve standards.",
  "Implementation-security requirements.",
  "Post-quantum migration planning.",
 ],
 "citations": [
  "Bernstein DJ, Lange T: SafeCurves criteria.",
 ],
 "demo": {"p": 41, "g": 6, "a": 5, "b": 17},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "cr-hash-collision",
 "name": "The Hash Collision Problem",
 "group": "Foundations",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Hash functions must be collision-resistant - but how can the resistance be assured when MD5 and SHA-1 both fell?",
 "background": "The collision problem - MD5 broken (2004), SHA-1 shattered (2017, SHAttered) - is the hash-function lifecycle: the Merkle-Damgard construction's weaknesses, the cryptanalysis advances, and the SHA-3 competition (Keccak's sponge) as the response. The collision-resistance is assumed until broken; the migration (SHA-1 deprecation) took a decade. The hash's trust is provisional.",
 "why_it_matters": "Hashes secure signatures, blockchains, and passwords. The provisional trust is the infrastructure's expiry date.",
 "sig_lens": "The Signature lens reads hashes as the expiring trust: the protocol must migrate before the break - crypto-agility, not crypto-loyalty.",
 "sig_solution": LABEL + " Assumptions: (1) collision resistance assumed until broken; (2) migrations take a decade. Reasoning path: build agility - hash-agile systems with SHA-3/BLAKE3 readiness and break-monitoring. Proposed mechanism: an expiry protocol with hash-agility requirements, cryptanalysis monitoring, and pre-planned migration paths. Confirm: the migrations complete pre-break. Kill: a SHA-3 break. Does NOT claim: the hashes unbreakable - it migrates before expiry.",
 "pointer": "The Signature system's proposed approach builds hash agility with pre-planned migration; the companion Signature Edition record specifies the expiry protocol.",
 "key_points": [
  "MD5 broken (2004); SHA-1 shattered (2017).",
  "Merkle-Damgard weaknesses exploited.",
  "SHA-3 (Keccak sponge) the response.",
  "Migrations take a decade.",
 ],
 "requirements": [
  "Hash-agility in system design.",
  "Cryptanalysis monitoring programs.",
  "Pre-planned migration paths.",
 ],
 "citations": [
  "Stevens M et al. (2017) The first collision for full SHA-1 (SHAttered).",
 ],
 "demo": {"p": 43, "g": 3, "a": 10, "b": 13},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "cr-rom",
 "name": "The Random Oracle Problem",
 "group": "Foundations",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Security proofs assume ideal random oracles - but real hash functions are not random oracles, so do the proofs mean anything?",
 "background": "The random-oracle problem - the ROM/standard-model gap - is cryptography's foundational unease: the proofs (OAEP, PSS) assume the hash is a random oracle; Canetti-Goldreich-Halevi showed schemes secure in ROM but insecure with any real hash. The standard-model proofs (fewer, harder) are the gold standard; the ROM proofs are the working standard. The proofs prove - about an idealization.",
 "why_it_matters": "Most practical proofs are ROM proofs. The idealization gap is the proof's fine print.",
 "sig_lens": "The Signature lens reads the ROM as the ideal witness: the protocol must prefer standard-model proofs - and mark the ROM proofs' fine print.",
 "sig_solution": LABEL + " Assumptions: (1) ROM proofs assume idealization; (2) CGH separations exist. Reasoning path: prefer standard-model proofs; label ROM reliance explicitly. Proposed mechanism: a witness protocol with proof-model labeling (ROM vs standard), standard-model preference in standards, and ROM-instantiation cryptanalysis. Confirm: the labeled proofs guide correctly. Kill: a ROM proof's instantiation breaks. Does NOT claim: the ROM proofs meaningless - it marks the fine print.",
 "pointer": "The Signature system's proposed approach labels proof models and prefers standard-model proofs; the companion Signature Edition record specifies the witness protocol.",
 "key_points": [
  "ROM proofs assume ideal hash behavior.",
  "CGH: ROM-secure but concretely insecure schemes exist.",
  "Standard-model proofs fewer and harder.",
  "Most practical proofs are ROM.",
 ],
 "requirements": [
  "Proof-model (ROM/standard) labeling.",
  "Standard-model preference in standards.",
  "ROM-instantiation monitoring.",
 ],
 "citations": [
  "Canetti R et al. (2004) The random oracle methodology, revisited. JACM 51.",
 ],
 "demo": {"p": 47, "g": 5, "a": 8, "b": 19},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "cr-key-dist",
 "name": "The Key Distribution Problem",
 "group": "Foundations",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Symmetric crypto needs shared secrets - but how can the keys be distributed at internet scale without trusted third parties?",
 "background": "The key-distribution problem - solved in principle by public-key crypto, in practice by PKI - is the trust infrastructure's problem: the certificate authorities (DigiNotar's hack, misissuance) are the weak points; the web-of-trust did not scale; and the post-quantum migration must redistribute everything. The key distribution works - on trusted third parties that get hacked.",
 "why_it_matters": "PKI secures the web. The CA weak points are the web's trust single-points-of-failure.",
 "sig_lens": "The Signature lens reads key distribution as the trust chain: the protocol must strengthen every link (transparency, pinning) - and plan the quantum reissue.",
 "sig_solution": LABEL + " Assumptions: (1) CAs are hackable single points; (2) PQ migration redistributes all. Reasoning path: harden the PKI - certificate transparency, pinning, multi-perspective validation - and execute the PQ migration. Proposed mechanism: a chain protocol with CT-log requirements, CA-accountability measures, and post-quantum PKI migration. Confirm: the hardened PKI resists. Kill: a systemic CA compromise. Does NOT claim: the trust solved - it strengthens the chain.",
 "pointer": "The Signature system's proposed approach hardens PKI with transparency and migrates post-quantum; the companion Signature Edition record specifies the chain protocol.",
 "key_points": [
  "PKI rests on certificate authorities.",
  "DigiNotar hack showed the CA risk.",
  "Certificate Transparency logs issuance.",
  "Post-quantum migration redistributes keys.",
 ],
 "requirements": [
  "Certificate-Transparency enforcement.",
  "CA accountability measures.",
  "Post-quantum PKI migration.",
 ],
 "citations": [
  "Laurie B et al. (2014) Certificate Transparency. RFC 6962.",
 ],
 "demo": {"p": 53, "g": 2, "a": 11, "b": 16},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "cr-perfect-secrecy",
 "name": "The Perfect Secrecy Problem",
 "group": "Foundations",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "The one-time pad is perfectly secure - but how can perfect secrecy be practical when the key must be as long as the message?",
 "background": "The perfect-secrecy problem - Shannon's theorem (key >= message entropy) - makes the OTP impractical: the key distribution is the message-transmission problem again. The stream ciphers approximate it; the quantum key distribution promises the key exchange. The perfect secrecy is achievable and unusable - the theory's beautiful impracticality.",
 "why_it_matters": "Perfect secrecy is the security gold standard. Its impracticality is the gap between provable and usable.",
 "sig_lens": "The Signature lens reads perfect secrecy as the gold standard in the vault: the protocol must use it where the message justifies the key (diplomatic, strategic) - and approximate honestly elsewhere.",
 "sig_solution": LABEL + " Assumptions: (1) OTP key-length = message-length; (2) QKD promises the exchange. Reasoning path: deploy OTP where justified, QKD where feasible, and honest computational security elsewhere. Proposed mechanism: a vault protocol with OTP-for-critical traffic, QKD deployment programs, and labeled computational-security elsewhere. Confirm: the critical traffic perfectly secured. Kill: QKD stays impractical. Does NOT claim: perfect secrecy practical - it uses the vault wisely.",
 "pointer": "The Signature system's proposed approach deploys perfect secrecy where justified; the companion Signature Edition record specifies the vault protocol.",
 "key_points": [
  "Shannon: perfect secrecy needs key >= message.",
  "OTP key distribution = the original problem.",
  "Stream ciphers approximate; QKD promises.",
  "Perfect but impractical.",
 ],
 "requirements": [
  "OTP deployment for critical traffic.",
  "QKD feasibility programs.",
  "Honest computational-security labeling.",
 ],
 "citations": [
  "Shannon CE (1949) Communication theory of secrecy systems. Bell System Technical Journal 28.",
 ],
 "demo": {"p": 59, "g": 2, "a": 12, "b": 21},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "cr-prg",
 "name": "The Pseudorandom Generator Problem",
 "group": "Foundations",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Crypto needs randomness from short seeds - but which generators are truly pseudorandom, and how can backdoors be excluded?",
 "background": "The PRG problem - Dual_EC_DRBG's backdoored constants (Snowden revelations) - is the trust crisis: the standardized generator had a suspected NSA backdoor; the constants' generation was unexplained. The provable PRGs (Blum-Blum-Shub: slow; AES-CTR-DRBG: fast, heuristic) trade proof for speed. The randomness that seeds everything must itself be trustworthy - the Dual_EC lesson is the unexplained constants.",
 "why_it_matters": "PRGs seed all crypto randomness. The backdoored standard was the seeds' betrayal.",
 "sig_lens": "The Signature lens reads PRGs as the seeds: the protocol must plant verifiable seeds (nothing-up-my-sleeve constants) - and never trust the unexplained.",
 "sig_solution": LABEL + " Assumptions: (1) Dual_EC's constants unexplained; (2) provable PRGs slow. Reasoning path: standardize verifiable randomness - nothing-up-my-sleeve generation with provable backing where affordable. Proposed mechanism: a seeds protocol with verifiable-constant standards, backdoor-resistant designs, and PRG-health monitoring. Confirm: the standards trusted. Kill: a new backdoor found. Does NOT claim: the PRGs backdoor-free - it plants verifiable seeds.",
 "pointer": "The Signature system's proposed approach standardizes verifiable randomness generation; the companion Signature Edition record specifies the seeds protocol.",
 "key_points": [
  "Dual_EC_DRBG: suspected backdoored constants.",
  "Unexplained constants were the betrayal.",
  "Blum-Blum-Shub provable but slow.",
  "AES-CTR-DRBG fast but heuristic.",
 ],
 "requirements": [
  "Nothing-up-my-sleeve constant standards.",
  "Backdoor-resistant PRG designs.",
  "PRG implementation health monitoring.",
 ],
 "citations": [
  "Checkoway S et al. (2014) On the practical exploitability of Dual EC. USENIX Security.",
 ],
 "demo": {"p": 61, "g": 2, "a": 13, "b": 18},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "cr-zk-found",
 "name": "The Zero Knowledge Foundations Problem",
 "group": "Foundations",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Proving without revealing - but what can be proven in zero knowledge, and what are the minimal assumptions?",
 "background": "The ZK foundations - Goldwasser-Micali-Rackoff (1985): everything in NP has a zero-knowledge proof - is the completeness triumph: but the minimal assumptions (one-way functions suffice), the round complexity, and the knowledge-vs-membership distinctions are the theory's fine points. The foundations are solid; their efficiency (the next entries) is not.",
 "why_it_matters": "Zero knowledge is the privacy primitive. Its foundations' solidity is the privacy's bedrock.",
 "sig_lens": "The Signature lens reads ZK foundations as the bedrock: the protocol must build on the proven completeness - and push the efficiency frontier.",
 "sig_solution": LABEL + " Assumptions: (1) NP-complete ZK from OWFs; (2) efficiency the open frontier. Reasoning path: deploy the foundations - standardize ZK from minimal assumptions - while researching efficiency. Proposed mechanism: a bedrock protocol with assumption-minimal ZK standards, completeness-based protocol design, and efficiency research programs. Confirm: the foundations deployed widely. Kill: the assumptions prove insufficient. Does NOT claim: the efficiency solved - it builds on bedrock.",
 "pointer": "The Signature system's proposed approach standardizes zero knowledge on minimal assumptions; the companion Signature Edition record specifies the bedrock protocol.",
 "key_points": [
  "GMR 1985: all of NP has ZK proofs.",
  "One-way functions suffice.",
  "Round complexity and knowledge distinctions refined.",
  "Foundations solid; efficiency open.",
 ],
 "requirements": [
  "Assumption-minimal ZK standards.",
  "Completeness-based protocol designs.",
  "Efficiency research programs.",
 ],
 "citations": [
  "Goldwasser S et al. (1989) The knowledge complexity of interactive proof systems. SIAM J. Computing 18.",
 ],
 "demo": {"p": 67, "g": 2, "a": 14, "b": 22},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "cr-pqc",
 "name": "The Post Quantum Cryptography Problem",
 "group": "Quantum Resistance",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Quantum computers will break RSA and ECC - but which post-quantum schemes are secure, and how can the world migrate in time?",
 "background": "The PQC problem - NIST's standardization (Kyber/Dilithium/Falcon/SPHINCS+ selected; SIKE broken dramatically) - is the migration race: the harvest-now-decrypt-later threat means long-lived secrets are already vulnerable; the new schemes' cryptanalysis is young (SIKE's fall warns); and the migration (protocols, PKI, embedded) takes a decade. The quantum computer's timeline is uncertain; the migration's deadline is now.",
 "why_it_matters": "Harvest-now-decrypt-later makes the quantum threat current. The decade-long migration is the race.",
 "sig_lens": "The Signature lens reads PQC as the race: the protocol must migrate now (hybrid schemes) - not when the quantum computer arrives.",
 "sig_solution": LABEL + " Assumptions: (1) harvest-now-decrypt-later current; (2) new schemes' cryptanalysis young. Reasoning path: migrate hybrid-first - classical+PQC hybrids with crypto-agility. Proposed mechanism: a race protocol with hybrid-deployment mandates, PQC cryptanalysis programs, and agility requirements. Confirm: the migration completes pre-quantum. Kill: a standardized scheme breaks. Does NOT claim: the PQC schemes secure - it races with hybrids.",
 "pointer": "The Signature system's proposed approach migrates post-quantum with hybrid schemes; the companion Signature Edition record specifies the race protocol.",
 "key_points": [
  "NIST selected Kyber, Dilithium, Falcon, SPHINCS+.",
  "SIKE broken after selection (cautionary).",
  "Harvest-now-decrypt-later threatens current secrets.",
  "Migration takes a decade.",
 ],
 "requirements": [
  "Hybrid classical+PQC deployment.",
  "Continued PQC cryptanalysis.",
  "Crypto-agility requirements.",
 ],
 "citations": [
  "NIST Post-Quantum Cryptography Standardization (2022 selections).",
 ],
 "demo": {"p": 71, "g": 7, "a": 9, "b": 25},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "cr-lattice",
 "name": "The Lattice Hardness Problem",
 "group": "Quantum Resistance",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Post-quantum crypto rests on lattice problems (SVP, CVP) - but how hard are they really, and do the reductions hold?",
 "background": "The lattice problem - SVP/CVP worst-case hardness, Ajtai's worst-to-average reduction - is PQC's foundation: but the approximation factors in the reductions are loose; the concrete hardness (BKZ block sizes vs security) is estimated, not proven; and the algebraic structure (Ring-LWE's ideal lattices) might enable attacks. The foundation is the best-studied - and still heuristic at the concrete level.",
 "why_it_matters": "Lattice crypto is the PQC frontrunner. Its concrete hardness estimates are the standards' security claims.",
 "sig_lens": "The Signature lens reads lattices as the new bedrock: the protocol must test the bedrock's depth (concrete cryptanalysis) - continuously.",
 "sig_solution": LABEL + " Assumptions: (1) reductions loose; (2) concrete hardness estimated. Reasoning path: cryptanalyze continuously - lattice-challenge programs informing parameter selection. Proposed mechanism: a bedrock protocol with concrete lattice cryptanalysis, conservative parameter margins, and reduction-tightening research. Confirm: the estimates hold. Kill: a lattice attack breaks parameters. Does NOT claim: lattices hard - it tests the bedrock.",
 "pointer": "The Signature system's proposed approach cryptanalyzes lattice hardness continuously; the companion Signature Edition record specifies the bedrock protocol.",
 "key_points": [
  "SVP/CVP: worst-case hardness foundation.",
  "Ajtai worst-to-average reduction.",
  "Concrete (BKZ) hardness estimated, not proven.",
  "Ring-LWE structure might aid attacks.",
 ],
 "requirements": [
  "Concrete lattice cryptanalysis programs.",
  "Conservative parameter margins.",
  "Reduction-tightening research.",
 ],
 "citations": [
  "Ajtai M (1996) Generating hard instances of lattice problems. STOC.",
 ],
 "demo": {"p": 73, "g": 5, "a": 10, "b": 20},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "cr-lwe",
 "name": "The Learning With Errors Problem",
 "group": "Quantum Resistance",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "LWE underlies Kyber and Dilithium - but is the learning-with-errors problem really as hard as the worst-case lattices?",
 "background": "The LWE problem - Regev's reduction from worst-case lattice problems - is the PQC workhorse: but the reduction's parameters are loose; the Ring-LWE/Module-LWE variants add algebraic structure (with debated risk); and the concrete security (Kyber's parameters) rests on cryptanalytic estimates. The workhorse's strength is estimated.",
 "why_it_matters": "Kyber/Dilithium - the PQC standards - rest on LWE. The workhorse's estimated strength is the standards' claim.",
 "sig_lens": "The Signature lens reads LWE as the workhorse: the protocol must monitor its health (cryptanalysis) - and keep the classical backup (hybrids).",
 "sig_solution": LABEL + " Assumptions: (1) reductions loose; (2) algebraic variants debated. Reasoning path: monitor LWE health - cryptanalysis plus hybrid deployment. Proposed mechanism: a workhorse protocol with LWE cryptanalysis programs, hybrid PQC deployment, and variant-risk assessment. Confirm: LWE stands. Kill: an LWE break. Does NOT claim: LWE hard - it monitors the workhorse.",
 "pointer": "The Signature system's proposed approach monitors LWE cryptanalysis with hybrid deployment; the companion Signature Edition record specifies the workhorse protocol.",
 "key_points": [
  "Regev's worst-case to LWE reduction.",
  "Ring/Module-LWE add algebraic structure.",
  "Kyber/Dilithium parameters cryptanalytically estimated.",
  "Reductions loose at concrete levels.",
 ],
 "requirements": [
  "LWE cryptanalysis programs.",
  "Hybrid deployment mandates.",
  "Algebraic-variant risk assessment.",
 ],
 "citations": [
  "Regev O (2009) On lattices, learning with errors, random linear codes, and cryptography. JACM 56.",
 ],
 "demo": {"p": 79, "g": 3, "a": 11, "b": 23},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "cr-fhe",
 "name": "The Fully Homomorphic Encryption Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Computing on encrypted data (FHE) is possible - but how can it be made fast enough for real use?",
 "background": "The FHE problem - Gentry's 2009 breakthrough, now BGV/BFV/CKKS/TFHE schemes - is the efficiency gap: the overhead (1000x-1000000x) limits applications; the bootstrapping (refreshing ciphertexts) is the bottleneck; and the standardization (HomomorphicEncryption.org) is young. The private computation is possible; its practicality is half-built.",
 "why_it_matters": "FHE enables private cloud computation. The efficiency gap is the privacy's price.",
 "sig_lens": "The Signature lens reads FHE as the private computer: the protocol must make it fast (hardware, algorithms) - and standardize the interfaces.",
 "sig_solution": LABEL + " Assumptions: (1) overhead 1e3-1e6x; (2) bootstrapping the bottleneck. Reasoning path: accelerate - hardware (FPGA/ASIC), algorithmic (bootstrapping), and application-targeted schemes. Proposed mechanism: a computer protocol with FHE acceleration programs, scheme-standardization, and pilot private-computation deployments. Confirm: the overhead reaches practicality. Kill: the overhead stays prohibitive. Does NOT claim: FHE practical - it builds the private computer.",
 "pointer": "The Signature system's proposed approach accelerates fully homomorphic encryption; the companion Signature Edition record specifies the computer protocol.",
 "key_points": [
  "Gentry 2009: first FHE scheme.",
  "BGV/BFV/CKKS/TFHE: current generations.",
  "Overhead 1000x-1000000x.",
  "Bootstrapping is the bottleneck.",
 ],
 "requirements": [
  "FHE hardware acceleration.",
  "Bootstrapping algorithm research.",
  "Scheme standardization.",
 ],
 "citations": [
  "Gentry C (2009) Fully homomorphic encryption using ideal lattices. STOC.",
 ],
 "demo": {"p": 83, "g": 2, "a": 12, "b": 27},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "cr-io",
 "name": "The Indistinguishability Obfuscation Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Obfuscating programs while preserving function (iO) would be crypto-complete - but can it be built efficiently and on solid assumptions?",
 "background": "The iO problem - Garg et al.'s 2013 candidate, then the Jain-Lin-Sahai 2020 construction from standard assumptions - is the feasibility-vs-efficiency gap: the constructions exist (from LWE + PRGs) but are astronomically inefficient; the multilinear-map candidates broke repeatedly. iO implies nearly everything (functional encryption, deniable encryption). The crypto-complete primitive is proven possible and practically impossible.",
 "why_it_matters": "iO would imply most advanced crypto. Its inefficiency is the completeness' price.",
 "sig_lens": "The Signature lens reads iO as the philosopher's stone: the protocol must transmute it (efficiency) - or use its implications as the guide.",
 "sig_solution": LABEL + " Assumptions: (1) constructions from standard assumptions exist; (2) astronomically inefficient. Reasoning path: pursue efficiency - and use iO's implications to guide feasible constructions. Proposed mechanism: a stone protocol with iO-efficiency research, implication-guided protocol design, and assumption-monitoring. Confirm: the efficiency reaches usability. Kill: iO stays theoretical. Does NOT claim: iO practical - it transmutes the stone.",
 "pointer": "The Signature system's proposed approach pursues obfuscation efficiency via implication-guided design; the companion Signature Edition record specifies the stone protocol.",
 "key_points": [
  "Garg et al. 2013: first iO candidate.",
  "Jain-Lin-Sahai 2020: from standard assumptions.",
  "Multilinear-map candidates broke repeatedly.",
  "iO implies functional encryption and more.",
 ],
 "requirements": [
  "iO efficiency research.",
  "Implication-guided protocol design.",
  "Assumption monitoring.",
 ],
 "citations": [
  "Jain A et al. (2021) Indistinguishability obfuscation from well-founded assumptions. STOC.",
 ],
 "demo": {"p": 89, "g": 3, "a": 13, "b": 29},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "cr-maps",
 "name": "The Multilinear Maps Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Multilinear maps would enable powerful crypto - but can secure maps be built after the candidates kept breaking?",
 "background": "The maps problem - GGH13, CLT13, GGH15 candidates, all broken (zeroizing attacks) - is the broken-dream: the powerful applications (iO, multipartite DH) motivated them; the cryptanalysis destroyed them. The current status: no secure multilinear map candidate stands. The dream's applications were built on sand.",
 "why_it_matters": "Multilinear maps would unlock iO and more. Their repeated breaking is the cautionary tale.",
 "sig_lens": "The Signature lens reads multilinear maps as the broken bridge: the protocol must not rebuild on the same sand - it must find bedrock (standard assumptions).",
 "sig_solution": LABEL + " Assumptions: (1) all candidates broken; (2) applications built on sand. Reasoning path: build on bedrock - standard-assumption constructions (like JLS iO) instead of new maps. Proposed mechanism: a bridge protocol with map-candidate moratorium, bedrock-construction preference, and application migration. Confirm: the bedrock constructions deliver. Kill: the applications stay unrealizable. Does NOT claim: secure maps - it builds on bedrock.",
 "pointer": "The Signature system's proposed approach builds advanced crypto on standard assumptions, not broken maps; the companion Signature Edition record specifies the bridge protocol.",
 "key_points": [
  "GGH13, CLT13, GGH15: all broken.",
  "Zeroizing attacks destroyed candidates.",
  "No secure candidate stands.",
  "iO now from standard assumptions instead.",
 ],
 "requirements": [
  "Moratorium on map-based constructions.",
  "Standard-assumption preference.",
  "Application migration to bedrock.",
 ],
 "citations": [
  "Albrecht M et al.: survey of multilinear map cryptanalysis.",
 ],
 "demo": {"p": 97, "g": 5, "a": 14, "b": 31},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "cr-fe",
 "name": "The Functional Encryption Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Decrypting only the function of the data (FE) - but how can it be built efficiently for useful functions?",
 "background": "The FE problem - keys for functions f, decrypting f(m) only - has feasibility (from iO) but the efficient constructions cover limited functions (inner products, quadratics); the general FE is iO-inefficient. The applications (privacy-preserving analytics) need the efficient general case. The function-revealing encryption is half-built.",
 "why_it_matters": "FE enables computing on encrypted data by function. The limited efficient functions are the application gap.",
 "sig_lens": "The Signature lens reads FE as the selective reveal: the protocol must expand the revealed functions - efficiently - to the useful ones.",
 "sig_solution": LABEL + " Assumptions: (1) feasibility from iO; (2) efficient only for limited functions. Reasoning path: expand efficient FE - new constructions for richer function classes. Proposed mechanism: a reveal protocol with FE function-class expansion, application-driven construction, and efficiency benchmarking. Confirm: the useful functions covered efficiently. Kill: FE stays limited. Does NOT claim: general efficient FE - it expands the reveal.",
 "pointer": "The Signature system's proposed approach expands efficient functional encryption; the companion Signature Edition record specifies the reveal protocol.",
 "key_points": [
  "FE: keys reveal f(m) only.",
  "Feasibility from indistinguishability obfuscation.",
  "Efficient for inner products, quadratics.",
  "General FE iO-inefficient.",
 ],
 "requirements": [
  "Richer function-class FE constructions.",
  "Application-driven design.",
  "Efficiency benchmarking.",
 ],
 "citations": [
  "Boneh D et al. (2011) Functional encryption: definitions and challenges. TCC.",
 ],
 "demo": {"p": 101, "g": 2, "a": 15, "b": 33},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "cr-mpc",
 "name": "The Secure Multiparty Computation Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Computing jointly without revealing inputs (MPC) - but how can it scale to internet-sized problems?",
 "background": "The MPC problem - Yao's garbled circuits, GMW, SPDZ - is the scalability gap: the protocols work but the communication/computation overhead limits scale; the malicious-security costs more; and the real deployments (auctions, statistics) are small. The joint computation is possible; its internet scale is not.",
 "why_it_matters": "MPC enables private joint computation. The scale gap is the deployment barrier.",
 "sig_lens": "The Signature lens reads MPC as the private meeting: the protocol must host bigger meetings (scale) - without leaking the minutes.",
 "sig_solution": LABEL + " Assumptions: (1) overhead limits scale; (2) malicious security costly. Reasoning path: scale up - protocol optimization, preprocessing, and honest-majority tradeoffs where valid. Proposed mechanism: a meeting protocol with MPC efficiency research, preprocessing-based deployments, and scale benchmarking. Confirm: the meetings scale. Kill: the overhead stays prohibitive. Does NOT claim: internet-scale MPC - it hosts bigger meetings.",
 "pointer": "The Signature system's proposed approach scales secure multiparty computation; the companion Signature Edition record specifies the meeting protocol.",
 "key_points": [
  "Yao, GMW, SPDZ: protocol families.",
  "Communication/computation overhead limits.",
  "Malicious security more costly.",
  "Real deployments small-scale.",
 ],
 "requirements": [
  "MPC efficiency research.",
  "Preprocessing-based deployments.",
  "Scale benchmarking.",
 ],
 "citations": [
  "Yao AC (1986) How to generate and exchange secrets. FOCS.",
 ],
 "demo": {"p": 103, "g": 5, "a": 16, "b": 35},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "cr-zk-scale",
 "name": "The Zero Knowledge Scalability Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "zk-SNARKs prove succinctly - but how can the trusted setup be removed and the provers made fast?",
 "background": "The zk-scalability problem - SNARKs' trusted setup (toxic waste), STARKs' larger proofs, the prover time - is the blockchain-privacy bottleneck: the ceremonies (Zcash's) manage trust; the transparent alternatives (STARKs, Bulletproofs) trade size for trustlessness; and the prover acceleration (hardware) is young. The succinct proofs are trusted-setup-bound.",
 "why_it_matters": "ZK proofs enable private blockchains and scaling. The setup trust is the privacy's fine print.",
 "sig_lens": "The Signature lens reads zk-SNARKs as the succinct witness with a secret ceremony: the protocol must remove the secret (transparent setups) - and speed the witness.",
 "sig_solution": LABEL + " Assumptions: (1) trusted setup the trust issue; (2) transparent alternatives larger. Reasoning path: go transparent - STARKs/Bulletproofs with prover acceleration. Proposed mechanism: a witness protocol with transparent-proof standardization, prover-hardware acceleration, and ceremony-risk disclosure. Confirm: the transparent proofs practical. Kill: the transparent proofs stay too large. Does NOT claim: the setup eliminated everywhere - it removes the secret.",
 "pointer": "The Signature system's proposed approach standardizes transparent zero-knowledge proofs; the companion Signature Edition record specifies the witness protocol.",
 "key_points": [
  "SNARKs: succinct, trusted setup.",
  "STARKs/Bulletproofs: transparent, larger.",
  "Ceremonies manage the toxic waste.",
  "Prover time the bottleneck.",
 ],
 "requirements": [
  "Transparent-proof standardization.",
  "Prover acceleration programs.",
  "Ceremony-risk disclosure.",
 ],
 "citations": [
  "Ben-Sasson E et al. (2014) Zerocash. IEEE S&P.",
 ],
 "demo": {"p": 107, "g": 2, "a": 17, "b": 37},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "cr-qkd",
 "name": "The Quantum Key Distribution Problem",
 "group": "Quantum Resistance",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "QKD promises physics-based key exchange - but can it be practical, and do the implementation loopholes break the promise?",
 "background": "The QKD problem - BB84's theoretical security vs implementation attacks (photon-number-splitting, detector blinding) - is the practice gap: the device-independent QKD closes loopholes in theory; the distances (fiber limits, satellite: Micius) constrain deployment; and the cost exceeds PQC's. The physics promise is real; its engineering is expensive.",
 "why_it_matters": "QKD is the physics-based alternative to PQC. The implementation loopholes are the promise's fine print.",
 "sig_lens": "The Signature lens reads QKD as the physics promise: the protocol must close the loopholes (device-independence) - and price the promise against PQC.",
 "sig_solution": LABEL + " Assumptions: (1) implementation attacks break naive QKD; (2) distance/cost constrain. Reasoning path: close loopholes and compare honestly - device-independent QKD with PQC cost-benefit. Proposed mechanism: a promise protocol with implementation-security certification, satellite/fiber deployment where justified, and QKD-vs-PQC decision frameworks. Confirm: the loopholes closed practically. Kill: QKD stays niche. Does NOT claim: QKD practical everywhere - it prices the promise.",
 "pointer": "The Signature system's proposed approach certifies QKD implementations and compares with PQC; the companion Signature Edition record specifies the promise protocol.",
 "key_points": [
  "BB84: theoretically secure key exchange.",
  "Detector-blinding and PNS attacks hit implementations.",
  "Device-independent QKD closes loopholes theoretically.",
  "Micius satellite demonstrated space QKD.",
 ],
 "requirements": [
  "Implementation-security certification.",
  "Justified deployment (satellite/fiber).",
  "QKD-vs-PQC decision frameworks.",
 ],
 "citations": [
  "Bennett CH, Brassard G (1984) Quantum cryptography. Proc. IEEE ICCSS.",
 ],
 "demo": {"p": 109, "g": 6, "a": 18, "b": 39},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "cr-side-channel",
 "name": "The Side Channel Problem",
 "group": "Implementation",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Crypto leaks through timing, power, and cache - but how can implementations be made side-channel-free?",
 "background": "The side-channel problem - Kocher's timing attacks, power analysis (DPA), Spectre/Meltdown (microarchitectural) - is the implementation's leak: the constant-time coding, masking, and the formal verification are the defenses; the new channels (speculative execution) keep appearing. The math is secure; the physics leaks.",
 "why_it_matters": "Side channels break real crypto without breaking the math. The leaking physics is the deployment's vulnerability.",
 "sig_lens": "The Signature lens reads side channels as the whispering walls: the protocol must soundproof the implementation - and keep listening for new whispers.",
 "sig_solution": LABEL + " Assumptions: (1) new channels keep appearing; (2) defenses exist per channel. Reasoning path: defend systematically - constant-time/masked baselines with continuous channel monitoring. Proposed mechanism: a walls protocol with side-channel-secure coding standards, leakage-testing requirements, and new-channel response programs. Confirm: the implementations resist known channels. Kill: the channels outpace defenses. Does NOT claim: the implementations leak-free - it soundproofs systematically.",
 "pointer": "The Signature system's proposed approach standardizes side-channel-secure implementation; the companion Signature Edition record specifies the walls protocol.",
 "key_points": [
  "Timing, power (DPA), cache attacks.",
  "Spectre/Meltdown: microarchitectural channels.",
  "Constant-time coding and masking defend.",
  "New channels keep appearing.",
 ],
 "requirements": [
  "Side-channel-secure coding standards.",
  "Leakage-testing requirements.",
  "New-channel response programs.",
 ],
 "citations": [
  "Kocher PC (1996) Timing attacks on implementations of Diffie-Hellman, RSA, DSS. Crypto.",
 ],
 "demo": {"p": 113, "g": 3, "a": 19, "b": 41},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "cr-rng",
 "name": "The Random Number Generation Problem",
 "group": "Implementation",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Crypto needs true randomness - but how can random-number generators be built and verified trustworthy?",
 "background": "The RNG problem - entropy sources (ring oscillators, quantum), health testing (NIST SP 800-90B), and the verification - is the trust root: the Intel RDRAND trust debate; the entropy failures (Debian OpenSSL, embedded devices); and the QRNG promises. The randomness that seeds everything is the hardest to verify.",
 "why_it_matters": "Bad randomness breaks crypto silently. The unverifiable entropy is the silent failure.",
 "sig_lens": "The Signature lens reads RNGs as the wells: the protocol must test the water (entropy) continuously - and never trust a single well.",
 "sig_solution": LABEL + " Assumptions: (1) entropy failures silent; (2) single sources untrustworthy. Reasoning path: diversify and monitor - multiple entropy sources with continuous health testing. Proposed mechanism: a wells protocol with multi-source entropy designs, continuous health-test requirements, and entropy-failure response. Confirm: the generators trustworthy. Kill: the entropy stays unverifiable. Does NOT claim: the randomness true - it tests the wells.",
 "pointer": "The Signature system's proposed approach diversifies entropy sources with health testing; the companion Signature Edition record specifies the wells protocol.",
 "key_points": [
  "Entropy sources: oscillators, quantum.",
  "NIST SP 800-90B health testing.",
  "Debian/embedded entropy failures.",
  "RDRAND trust debated.",
 ],
 "requirements": [
  "Multi-source entropy designs.",
  "Continuous health-test requirements.",
  "Entropy-failure response plans.",
 ],
 "citations": [
  "NIST SP 800-90 series: random number generation.",
 ],
 "demo": {"p": 127, "g": 3, "a": 20, "b": 43},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "cr-owf",
 "name": "The One Way Function Existence Problem",
 "group": "Theory",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "All cryptography assumes one-way functions exist - but can their existence be proven, or is it equivalent to P != NP?",
 "background": "The OWF problem - existence unproven; implied by P != NP but not known equivalent - is crypto's foundation gap: the candidates (factoring, discrete log, lattice) are assumed; the proof would need P != NP (unproven). The minimal assumption is unproven. Crypto stands on the unproven.",
 "why_it_matters": "One-way functions are crypto's minimal assumption. Their unproven existence is the field's foundation gap.",
 "sig_lens": "The Signature lens reads OWFs as the foundation stone: the protocol must build on the best candidates - while the proof waits on P vs NP.",
 "sig_solution": LABEL + " Assumptions: (1) existence unproven; (2) P != NP needed. Reasoning path: diversify candidates - multiple independent OWF families so no single break collapses crypto. Proposed mechanism: a stone protocol with candidate-diversity requirements, assumption-monitoring, and P-vs-NP progress tracking. Confirm: the candidates stand. Kill: all candidates break. Does NOT claim: OWFs exist - it builds on the best stones.",
 "pointer": "The Signature system's proposed approach diversifies one-way-function candidates; the companion Signature Edition record specifies the stone protocol.",
 "key_points": [
  "OWF existence unproven.",
  "Implied by P != NP; equivalence unknown.",
  "Candidates: factoring, DLP, lattices.",
  "Minimal assumption unproven.",
 ],
 "requirements": [
  "Candidate-diversity in standards.",
  "Assumption monitoring.",
  "P-vs-NP progress tracking.",
 ],
 "citations": [
  "Goldreich O (2001) Foundations of Cryptography, Vol. 1. Cambridge.",
 ],
 "demo": {"p": 131, "g": 2, "a": 21, "b": 45},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "cr-pke-exist",
 "name": "The Public Key Existence Problem",
 "group": "Theory",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Public-key crypto needs trapdoors - but do trapdoor functions exist, and are they strictly stronger than one-way functions?",
 "background": "The PKE problem - trapdoor predicates vs OWFs: the separation (OWFs might not imply PKE) is Impagliazzo's world structure; the candidates (RSA, ElGamal, lattices) are assumed trapdoors. The public-key primitive might need strictly more than one-wayness. The trapdoor's existence is the public-key gap.",
 "why_it_matters": "Public-key crypto needs trapdoors. The unproven trapdoor existence is the asymmetric gap.",
 "sig_lens": "The Signature lens reads trapdoors as the secret passages: the protocol must verify the passages exist (candidates) - in multiple independent architectures.",
 "sig_solution": LABEL + " Assumptions: (1) trapdoors might need more than OWFs; (2) candidates assumed. Reasoning path: diversify trapdoor candidates - factoring, DLP, lattice families. Proposed mechanism: a passages protocol with trapdoor-candidate diversity, separation research (OWF vs PKE), and assumption-explicit standards. Confirm: the candidates stand. Kill: the trapdoors all break. Does NOT claim: trapdoors exist - it verifies the passages.",
 "pointer": "The Signature system's proposed approach diversifies trapdoor candidates; the companion Signature Edition record specifies the passages protocol.",
 "key_points": [
  "Trapdoor functions: PKE's need.",
  "Might be strictly stronger than OWFs.",
  "Impagliazzo's worlds structure the question.",
  "Candidates: RSA, ElGamal, lattices.",
 ],
 "requirements": [
  "Trapdoor-candidate diversity.",
  "OWF-vs-PKE separation research.",
  "Assumption-explicit standards.",
 ],
 "citations": [
  "Impagliazzo R (1995) A personal view of average-case complexity. Structure in Complexity Theory.",
 ],
 "demo": {"p": 137, "g": 3, "a": 22, "b": 47},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "cr-worlds",
 "name": "The Minicrypt vs Cryptomania Problem",
 "group": "Theory",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Impagliazzo's worlds ask which crypto is possible - but do we live in Cryptomania (public-key possible) or Minicrypt (only symmetric)?",
 "background": "The worlds problem - Algorithmica, Heuristica, Pessiland, Minicrypt, Cryptomania - maps crypto's possibility to complexity: we do not know which world we inhabit; the evidence (no PKE break, no OWF proof) is consistent with Cryptomania but proves nothing. The worlds are the field's cosmology - unobservable but structuring.",
 "why_it_matters": "The worlds structure crypto's possibility. The uninhabited-unknown world is the field's cosmology.",
 "sig_lens": "The Signature lens reads the worlds as the map of possibility: the protocol must navigate by the evidence - building for Cryptomania, hedging for Minicrypt.",
 "sig_solution": LABEL + " Assumptions: (1) world unknown; (2) evidence consistent with Cryptomania. Reasoning path: build for Cryptomania, hedge for Minicrypt - symmetric-crypto strength as the hedge. Proposed mechanism: a map protocol with world-hedged standards (strong symmetric baselines), possibility research, and evidence monitoring. Confirm: the evidence keeps favoring Cryptomania. Kill: PKE breaks (Minicrypt). Does NOT claim: the world known - it navigates by evidence.",
 "pointer": "The Signature system's proposed approach hedges cryptographic worlds with strong symmetric baselines; the companion Signature Edition record specifies the map protocol.",
 "key_points": [
  "Five worlds: Algorithmica to Cryptomania.",
  "World determines crypto's possibility.",
  "Evidence consistent with Cryptomania.",
  "Nothing proven about the world.",
 ],
 "requirements": [
  "World-hedged standards.",
  "Strong symmetric baselines.",
  "Possibility research.",
 ],
 "citations": [
  "Impagliazzo R (1995) A personal view of average-case complexity.",
 ],
 "demo": {"p": 139, "g": 2, "a": 23, "b": 49},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "cr-whitebox",
 "name": "The White Box Cryptography Problem",
 "group": "Implementation",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Software crypto runs on hostile devices - but can white-box implementations resist key extraction?",
 "background": "The white-box problem - hiding keys in software against the white-box attacker (full visibility) - is the DRM/mobile-payments need: the academic constructions break (differential computation analysis); the commercial white-box is obscurity; and the theory (impossible in general? useful in practice?) is unsettled. The hostile device is the deployment reality; the protection is half-built.",
 "why_it_matters": "Mobile payments and DRM run on hostile devices. The half-built protection is the key-extraction risk.",
 "sig_lens": "The Signature lens reads white-box as the glass safe: the protocol must harden the glass (obfuscation, leakage-resistance) - while preferring hardware where possible.",
 "sig_solution": LABEL + " Assumptions: (1) academic constructions break; (2) commercial is obscurity. Reasoning path: harden and prefer hardware - white-box hardening with TEE/secure-element preference. Proposed mechanism: a glass protocol with white-box hardening standards, leakage-testing, and hardware-backed preference. Confirm: the hardened implementations resist. Kill: white-box proves impossible. Does NOT claim: the keys hidden - it hardens the glass.",
 "pointer": "The Signature system's proposed approach hardens white-box crypto preferring hardware roots; the companion Signature Edition record specifies the glass protocol.",
 "key_points": [
  "White-box attacker: full implementation visibility.",
  "Academic constructions broken (DCA).",
  "Commercial white-box is obscurity.",
  "Theory: impossible generally?",
 ],
 "requirements": [
  "White-box hardening standards.",
  "Leakage-testing requirements.",
  "Hardware-backed preference.",
 ],
 "citations": [
  "Chow S et al. (2002) White-box cryptography and an AES implementation. SAC.",
 ],
 "demo": {"p": 149, "g": 2, "a": 24, "b": 51},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "cr-searchable",
 "name": "The Searchable Encryption Problem",
 "group": "Advanced Crypto",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Searching encrypted data leaks access patterns - but how can search be both efficient and leakage-free?",
 "background": "The searchable-encryption problem - the leakage (search/access patterns) vs efficiency tradeoff - is the encrypted-database dilemma: the leakage enables attacks (file-injection, count attacks); the ORAM solution is expensive; and the practical schemes accept defined leakage. The efficient search leaks; the leak-free search is expensive.",
 "why_it_matters": "Encrypted databases need search. The leakage is the query-privacy gap.",
 "sig_lens": "The Signature lens reads searchable encryption as the whispered query: the protocol must quiet the whisper (leakage) - affordably.",
 "sig_solution": LABEL + " Assumptions: (1) leakage enables attacks; (2) ORAM expensive. Reasoning path: minimize leakage affordably - leakage-defined schemes with ORAM where justified. Proposed mechanism: a whisper protocol with leakage-profile standards, ORAM deployment where justified, and leakage-attack monitoring. Confirm: the leakage minimized practically. Kill: the attacks defeat the schemes. Does NOT claim: the search leak-free - it quiets the whisper.",
 "pointer": "The Signature system's proposed approach minimizes searchable-encryption leakage affordably; the companion Signature Edition record specifies the whisper protocol.",
 "key_points": [
  "Search/access-pattern leakage enables attacks.",
  "ORAM: leak-free but expensive.",
  "Practical schemes accept defined leakage.",
  "File-injection and count attacks demonstrated.",
 ],
 "requirements": [
  "Leakage-profile standards.",
  "ORAM where justified.",
  "Leakage-attack monitoring.",
 ],
 "citations": [
  "Cash D et al. (2013) Highly-scalable searchable symmetric encryption. Crypto.",
 ],
 "demo": {"p": 151, "g": 6, "a": 25, "b": 53},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "cr-blockchain-scale",
 "name": "The Blockchain Scalability Problem",
 "group": "Distributed",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Blockchains are slow - but how can throughput scale without sacrificing decentralization or security?",
 "background": "The scalability problem - the trilemma (decentralization, security, scalability: pick two) - has layer-2 answers (rollups, channels) and sharding, each with tradeoffs: the rollups' data-availability, the sharding's complexity, and the base layer's limits. The throughput scales; the trilemma persists.",
 "why_it_matters": "Blockchain adoption needs throughput. The trilemma is the scaling ceiling.",
 "sig_lens": "The Signature lens reads the trilemma as the three-legged stool: the protocol must lengthen each leg (layers) - without sawing the others.",
 "sig_solution": LABEL + " Assumptions: (1) trilemma structures tradeoffs; (2) L2/sharding each tradeoff. Reasoning path: scale in layers - base-layer security with L2 throughput, honestly accounting tradeoffs. Proposed mechanism: a stool protocol with layered-scaling architectures, tradeoff-disclosed designs, and decentralization monitoring. Confirm: the layers scale. Kill: the trilemma proves binding. Does NOT claim: the trilemma solved - it lengthens the legs.",
 "pointer": "The Signature system's proposed approach scales blockchains in layers with disclosed tradeoffs; the companion Signature Edition record specifies the stool protocol.",
 "key_points": [
  "Trilemma: decentralization, security, scalability.",
  "Rollups: data-availability tradeoffs.",
  "Sharding: complexity tradeoffs.",
  "Base layers throughput-limited.",
 ],
 "requirements": [
  "Layered-scaling architectures.",
  "Tradeoff-disclosed designs.",
  "Decentralization monitoring.",
 ],
 "citations": [
  "Nakamoto S (2008) Bitcoin: A Peer-to-Peer Electronic Cash System.",
  "Croman K et al. (2016) On Scaling Decentralized Blockchains. Proc. Financial Cryptography.",
 ],
 "demo": {"p": 157, "g": 5, "a": 26, "b": 55},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "cr-byzantine",
 "name": "The Byzantine Consensus Problem",
 "group": "Distributed",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Distributed systems must agree despite traitors - but how can consensus be fast, scalable, and secure under adaptive adversaries?",
 "background": "The Byzantine problem - FLP impossibility (no deterministic async consensus), the 3f+1 bound - has practical protocols (PBFT, HotStuff) but the scalability (communication quadratic), the adaptivity (adversary corrupting over time), and the finality-vs-availability (CAP) tradeoffs persist. The agreement is possible; its scale and speed are bounded.",
 "why_it_matters": "Consensus underlies blockchains and distributed trust. The scale bounds are the agreement's ceiling.",
 "sig_lens": "The Signature lens reads Byzantine consensus as the loyal generals: the protocol must keep them agreeing - fast - despite the traitors' adaptation.",
 "sig_solution": LABEL + " Assumptions: (1) FLP and 3f+1 bound; (2) communication quadratic. Reasoning path: scale the agreement - linear-communication protocols with adaptive-adversary models. Proposed mechanism: a generals protocol with scalable BFT research, adaptive-security models, and finality-clarity standards. Confirm: the protocols scale. Kill: the bounds prove binding. Does NOT claim: the bounds beaten - it scales within them.",
 "pointer": "The Signature system's proposed approach scales Byzantine consensus within proven bounds; the companion Signature Edition record specifies the generals protocol.",
 "key_points": [
  "FLP: no deterministic async consensus.",
  "3f+1 bound on Byzantine tolerance.",
  "PBFT/HotStuff: practical but quadratic.",
  "Adaptive adversaries stronger.",
 ],
 "requirements": [
  "Linear-communication BFT research.",
  "Adaptive-adversary security models.",
  "Finality-clarity standards.",
 ],
 "citations": [
  "Lamport L, Shostak R, Pease M (1982) The Byzantine Generals Problem. ACM TOPLAS 4.",
  "Castro M, Liskov B (1999) Practical Byzantine Fault Tolerance. OSDI.",
 ],
 "demo": {"p": 163, "g": 2, "a": 27, "b": 57},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "cr-pos",
 "name": "The Proof of Stake Security Problem",
 "group": "Distributed",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Proof-of-stake replaces mining with staking - but is it as secure as proof-of-work against long-range and grinding attacks?",
 "background": "The PoS problem - nothing-at-stake, long-range attacks, stake grinding - has protocol answers (slashing, weak subjectivity, VRFs) but the security arguments are younger than PoW's decade of battle-testing; the centralization (exchange staking, Lido) is the practical concern. The energy savings are real; the security equivalence is debated.",
 "why_it_matters": "PoS secures Ethereum's hundreds of billions. The younger security argument is the stake's risk.",
 "sig_lens": "The Signature lens reads PoS as the new guard: the protocol must prove the guard's vigilance - against the long-range and grinding attacks - by analysis and time.",
 "sig_solution": LABEL + " Assumptions: (1) protocol answers exist; (2) battle-testing younger. Reasoning path: prove the vigilance - formal security analyses plus incident monitoring plus decentralization. Proposed mechanism: a guard protocol with PoS formal-verification programs, attack-monitoring, and staking-decentralization measures. Confirm: the analyses and time vindicate. Kill: a fundamental attack succeeds. Does NOT claim: PoS as secure as PoW - it proves the guard.",
 "pointer": "The Signature system's proposed approach verifies proof-of-stake security formally and operationally; the companion Signature Edition record specifies the guard protocol.",
 "key_points": [
  "Nothing-at-stake, long-range, grinding attacks.",
  "Slashing, weak subjectivity, VRFs answer.",
  "Security arguments younger than PoW's.",
  "Staking centralization practical concern.",
 ],
 "requirements": [
  "PoS formal-verification programs.",
  "Attack monitoring.",
  "Staking-decentralization measures.",
 ],
 "citations": [
  "King S, Nadal S (2012) PPCoin: Peer-to-Peer Crypto-Currency with Proof-of-Stake.",
  "Kiayias A et al. (2017) Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol. Crypto.",
 ],
 "demo": {"p": 167, "g": 3, "a": 28, "b": 59},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "cr-agility",
 "name": "The Cryptographic Agility Problem",
 "group": "Implementation",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Algorithms break and standards change - but how can systems switch crypto quickly without breaking?",
 "background": "The agility problem - the SHA-1 and TLS migrations' decade-long pain - is the infrastructure's rigidity: the hard-coded algorithms, the protocol negotiation, and the embedded devices that cannot update. The PQC migration is the agility test. The rigid systems are the breakage's hostages.",
 "why_it_matters": "The PQC migration needs agility. The rigid infrastructure is the decade-long migration.",
 "sig_lens": "The Signature lens reads agility as the quick change: the protocol must build the changing rooms (abstraction, negotiation) - before the break.",
 "sig_solution": LABEL + " Assumptions: (1) migrations take a decade; (2) embedded unupdatable. Reasoning path: build agility in - algorithm abstraction, negotiated suites, updatable firmware. Proposed mechanism: a change protocol with agility-by-design standards, migration drills, and embedded-update requirements. Confirm: the migrations quicken. Kill: the rigidity persists. Does NOT claim: the systems agile - it builds the changing rooms.",
 "pointer": "The Signature system's proposed approach builds cryptographic agility by design; the companion Signature Edition record specifies the change protocol.",
 "key_points": [
  "SHA-1/TLS migrations took a decade.",
  "Hard-coded algorithms resist change.",
  "Embedded devices often unupdatable.",
  "PQC migration is the agility test.",
 ],
 "requirements": [
  "Agility-by-design standards.",
  "Migration drills.",
  "Embedded-update requirements.",
 ],
 "citations": [
  "NIST (2024) Post-Quantum Cryptography Standards (FIPS 203, 204, 205).",
  "Ott D et al. (2019) Identifying Research Challenges in Post Quantum Cryptography Migration. NIST.",
 ],
 "demo": {"p": 173, "g": 2, "a": 29, "b": 61},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "cr-unified",
 "name": "The Unified Cryptography Problem",
 "group": "Theory",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Cryptography is fragmented into primitives and proofs - but can the science of secrets be unified as one theory?",
 "background": "The unified-crypto problem - from Shannon to the provable-security paradigm to the worlds - is the field's synthesis: the primitives (encryption, signatures, ZK) are separate; the assumptions (factoring, lattices) are separate; the unification (iO's completeness, the worlds) is partial. The science of secrets is one; its theory is many.",
 "why_it_matters": "The fragmented theory misses the connections. The unification is the science's maturity.",
 "sig_lens": "The Signature lens reads cryptography as the one art of secrets: the protocol must unite it - completeness results to assumption hierarchies - in the coherent theory.",
 "sig_solution": LABEL + " Assumptions: (1) primitives and assumptions fragmented; (2) partial unifications exist. Reasoning path: unify via completeness - iO-like completeness results and assumption hierarchies. Proposed mechanism: an art protocol with completeness-driven theory, assumption-hierarchy mapping, and unified security frameworks. Confirm: the unified theory predicts and connects. Kill: the fragments resist. Does NOT claim: cryptography unified - it practices the one art.",
 "pointer": "The Signature system's proposed approach unifies cryptography via completeness results; the companion Signature Edition record specifies the art protocol.",
 "key_points": [
  "Primitives: encryption, signatures, ZK separate.",
  "Assumptions: factoring, lattices separate.",
  "iO completeness unifies partially.",
  "Impagliazzo's worlds structure possibility.",
 ],
 "requirements": [
  "Completeness-driven theoretical research.",
  "Assumption-hierarchy mapping.",
  "Unified security frameworks.",
 ],
 "citations": [
  "Goldreich O (2001-2009) Foundations of Cryptography, Vols. 1-2. Cambridge.",
 ],
 "demo": {"p": 179, "g": 3, "a": 30, "b": 63},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "cr-future",
 "name": "The Cryptography After Quantum Problem",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Beyond post-quantum: what does cryptography look like in a world with large quantum computers - and what new primitives become possible?",
 "background": "The after-quantum problem - quantum cryptography's positive side (quantum money, quantum ZK, uncloneable crypto) - is the opportunity: the quantum computer breaks classical assumptions but enables quantum primitives (Wiesner's quantum money, quantum lightning). The theory (quantum provable security) is young; the implementations distant. The quantum threat is also the quantum promise.",
 "why_it_matters": "Quantum computers enable new crypto, not just break old. The unbuilt primitives are the quantum promise.",
 "sig_lens": "The Signature lens reads the quantum future as the double-edged sword: the protocol must blunt the edge (PQC) - and wield it (quantum primitives).",
 "sig_solution": LABEL + " Assumptions: (1) quantum breaks classical; (2) quantum enables new primitives. Reasoning path: do both - PQC migration plus quantum-primitive research. Proposed mechanism: a sword protocol with quantum-cryptography research programs, quantum-money/lightning development, and quantum-safe-plus-quantum-advantage strategies. Confirm: the primitives built. Kill: the quantum advantage stays theoretical. Does NOT claim: the quantum crypto built - it wields the sword.",
 "pointer": "The Signature system's proposed approach develops quantum cryptographic primitives alongside PQC; the companion Signature Edition record specifies the sword protocol.",
 "key_points": [
  "Quantum breaks RSA/ECC (Shor).",
  "Quantum enables: money, lightning, uncloneable crypto.",
  "Wiesner's quantum money: the origin.",
  "Quantum provable security young.",
 ],
 "requirements": [
  "Quantum-cryptography research programs.",
  "Quantum-money/lightning development.",
  "Quantum-safe-plus-advantage strategies.",
 ],
 "citations": [
  "Wiesner S (1983) Conjugate coding. SIGACT News 15.",
 ],
 "demo": {"p": 181, "g": 2, "a": 31, "b": 65},
},
]
