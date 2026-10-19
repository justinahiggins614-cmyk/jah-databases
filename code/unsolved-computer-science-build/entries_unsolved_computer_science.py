#!/usr/bin/env python3
"""Entries for the Unsolved Computer Science databases (Manon's 16:15 orders,
Unsolved Problems Solved series, batch 1).

Two NEW databases, 34 ladder-ordered records each, both halves covering the
SAME 34 famous unsolved computer science problems:

  unsolved-computer-science            - The Unsolved Computer Science Database
                                         (public-harvest: real, fact-checked
                                         famous unsolved problems - P vs NP,
                                         quantum limits, crypto foundations,
                                         halting-problem relatives, sorting
                                         and matrix bounds, AI alignment and
                                         interpretability, and the rest)
  unsolved-computer-science-signature  - The Unsolved Computer Science
                                         Signature Database
                                         (the Signature system's proposed
                                         solution approaches to the same 34
                                         problems; src signature, titles
                                         suffixed " (Signature Edition)";
                                         every signature_solution opens with
                                         the exact label
                                         "Signature-generated proposed
                                         solution - not established
                                         science."; never presented as
                                         authentic public record)

ID prefixes: JAH-USCS- (public) and JAH-USCSS- (signature), verified free:
zero hits in manifest id_prefix values (2,442 databases) and zero hits in
every shard index file of jah-databases-data-1.

Ladder: ranks 1-34 non-decreasing, foundations (1-11) -> compounded (12-23)
-> advanced (24-34). Honesty rule throughout: no claimed proofs, no implied
peer acceptance, speculation never presented as settled.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

ENTRIES = [
    # ---------------------------------------------------------- FOUNDATIONS
    {
        "key": "busy-beaver",
        "name": "The Busy Beaver Numbers",
        "group": "Computability",
        "description": (
            "How long can a tiny Turing machine run before halting? The busy beaver "
            "function BB(n) is the maximum number of steps any halting n-state, 2-symbol "
            "Turing machine can take before stopping. BB(1) through BB(4) were pinned down "
            "decades ago, and BB(5) was finally proven to equal 47,176,870 in 2024 by the "
            "bbchallenge collaboration, with the proof formalized in the Coq proof "
            "assistant. BB(6) is wide open: the best known 6-state machine runs for more "
            "steps than ten tetrated fifteen times, and nobody knows the true maximum."
        ),
        "sig_lens": (
            "The Signature lens treats the busy beaver as the purest measure of what "
            "finite description can unleash: a handful of states that outrun every "
            "imaginable clock. The Signature approach hunts BB(6) not by brute force "
            "alone but by cataloging the structural families machines fall into, so the "
            "search space itself becomes the map."
        ),
        "how_it_works": (
            "Tibor Rado introduced the busy beaver game in 1962 as a concrete face for "
            "uncomputability: BB grows faster than any computable function, so no program "
            "can compute it in general. Each value is a finite but ferocious search "
            "problem - for BB(5), researchers enumerated and classified millions of "
            "5-state machines, and the final holdouts required custom deciders plus a "
            "machine-checked proof. The bbchallenge project, launched in 2022, finished "
            "the job in 2024 with BB(5) = 47,176,870. For BB(6) the search space is "
            "roughly 10^36,000 machines, far beyond exhaustive enumeration, so progress "
            "comes from clever machine-hunting heuristics and ever-stronger lower "
            "bounds. The current champion, found by mxdys in 2022, runs longer than "
            "10 tetrated 15 times - a number with no physical meaning, only a "
            "mathematical one. Why it matters: busy beaver values are the sharpest "
            "known yardsticks of uncomputability, they calibrate what automated "
            "termination provers can ever hope to decide, and each new value stress-"
            "tests the limits of formal proof itself."
        ),
        "key_points": [
            "BB(n) grows faster than any computable function - it is uncomputable in general.",
            "BB(5) = 47,176,870, proven 2024 by the bbchallenge collaboration, formalized in Coq.",
            "BB(6) is unknown; the best machine found runs more than 10 tetrated 15 times.",
            "Each value is a finite search problem, but the space explodes: ~10^36,000 machines for n=6.",
            "Busy beaver champions double as the hardest termination-analysis benchmarks.",
        ],
        "requirements": [
            "A claimed BB(6) value needs an explicit machine plus a proof no 6-state machine runs longer.",
            "Lower bounds need an explicit machine and a verified step count.",
            "Machine-checked proofs are the current gold standard after the BB(5) effort.",
        ],
        "standards": [
            "Rado T. On non-computable functions. Bell System Technical Journal; 1962.",
            "The bbchallenge collaboration. BB(5) = 47,176,870. Formalized in Coq; 2024.",
        ],
        "citations": [
            "Rado (1962) defined the busy beaver function and proved it uncomputable.",
            "bbchallenge (2022-2024) completed the BB(5) proof; mxdys (2022) holds the BB(6) lower-bound champion.",
        ],
        "solution": (
            "Step 1 - assumption: the BB(6) champion lives in a structured family, not scattered "
            "uniformly through the 10^36,000-machine space; machine-hunting heuristics already "
            "suggest champions share recognizable motifs. Step 2 - reasoning path: build a "
            "taxonomy of 6-state machine behaviors (counters, stack simulators, Collatz-like "
            "engines), then prove upper bounds family by family instead of machine by machine, "
            "mirroring how BB(5) fell to classification plus deciders. Step 3 - proposed "
            "mechanism: a 'family decider' pipeline that first routes each machine to its "
            "behavioral family, then applies the family's specialized non-halting or step-bound "
            "argument, shrinking the unresolved core until it fits in a machine-checked proof. "
            "What would confirm it: the pipeline closes BB(6) with a Coq-checked certificate. "
            "What would kill it: a champion machine whose behavior defeats every family "
            "classifier, forcing the taxonomy to grow without bound. What it does NOT claim: "
            "a general method for BB(7) or any shortcut around uncomputability - BB remains "
            "uncomputable, and this is a finite-search strategy, not a decision procedure."
        ),
        "ladder_rank": 1, "ladder_tier": "foundations",
    },
    {
        "key": "p-vs-np",
        "name": "P vs NP",
        "group": "Complexity Theory",
        "description": (
            "Can every problem whose solution is easy to check also be solved easily? "
            "P is the class of problems solvable in polynomial time; NP is the class "
            "whose solutions are verifiable in polynomial time. The question of whether "
            "P equals NP, posed in its modern form by Stephen Cook in 1971 and Leonid "
            "Levin in 1973, is the most famous open problem in computer science and one "
            "of the seven Clay Millennium Prize problems, carrying a one-million-dollar "
            "prize. Most experts believe P and NP differ, but no proof exists either way."
        ),
        "sig_lens": (
            "The Signature lens reads P vs NP as the master question about the price of "
            "creativity: is finding fundamentally harder than checking? The Signature "
            "approach maps exactly which proof techniques are blocked by the known "
            "barriers, so the search for a proof stops wandering into walled-off "
            "territory and starts building tools the barriers cannot touch."
        ),
        "how_it_works": (
            "Cook showed in 1971 that boolean satisfiability (SAT) is NP-complete: every "
            "NP problem reduces to it in polynomial time, so one fast SAT solver would "
            "collapse thousands of hard problems - scheduling, routing, protein folding "
            "models, chip verification - into tractability. Richard Karp's 1972 paper "
            "then listed 21 NP-complete problems, and the catalog has since grown into "
            "the thousands. Decades of attacks have mapped the defenses: relativization "
            "(Baker, Gill, Solovay 1975) blocks proof techniques that survive oracles; "
            "natural proofs (Razborov and Rudich 1997) block a wide class of circuit "
            "lower-bound arguments under standard cryptographic assumptions; "
            "algebrization (Aaronson and Wigderson 2008) extends the oracle barrier to "
            "algebraic techniques. Each barrier says: your proof idea, as stated, cannot "
            "work - it would also prove false statements. Why it matters: a proof that "
            "P differs from NP would certify the foundations of modern cryptography, "
            "while P = NP would revolutionize optimization, science, and mathematics "
            "itself - and break most encryption in use today."
        ),
        "key_points": [
            "SAT is NP-complete: a polynomial SAT solver implies P = NP.",
            "Clay Millennium Prize problem since 2000; one million dollars unclaimed.",
            "Three major barriers block naive proof attempts: relativization, natural proofs, algebrization.",
            "Thousands of NP-complete problems across scheduling, biology, verification, and logistics.",
            "Consensus leans P != NP, but consensus is not proof.",
        ],
        "requirements": [
            "A separation proof must use techniques that evade all three known barriers.",
            "A P = NP proof needs an explicit polynomial algorithm for an NP-complete problem.",
            "Either direction must survive peer scrutiny at the Clay Institute level.",
        ],
        "standards": [
            "Cook S. The complexity of theorem-proving procedures. STOC; 1971.",
            "Karp R. Reducibility among combinatorial problems. 1972.",
            "Razborov A, Rudich S. Natural proofs. JCSS; 1997.",
            "Aaronson S, Wigderson A. Algebrization. STOC; 2008.",
        ],
        "citations": [
            "Cook (1971) and Levin (1973) independently founded NP-completeness theory.",
            "The Clay Mathematics Institute lists P vs NP among its seven Millennium problems (2000).",
        ],
        "solution": (
            "Step 1 - assumption: a resolution will come from a technique that is "
            "simultaneously non-relativizing, non-naturalizing, and non-algebrizing, "
            "since every blocked attempt failed at least one barrier. Step 2 - reasoning "
            "path: construct an explicit 'barrier audit' that takes any candidate proof "
            "strategy and mechanically tests which barriers it trips, then concentrate "
            "only on strategies the audit certifies as barrier-clean - for example, "
            "proofs exploiting the fine combinatorial structure of specific NP-complete "
            "problems rather than generic diagonalization. Step 3 - proposed mechanism: "
            "a proof-search program guided by the audit, targeting superpolynomial "
            "lower bounds for SAT against restricted but barrier-evading circuit models, "
            "ratcheting the restriction upward. What would confirm it: a barrier-clean "
            "lower bound that scales to full generality. What would kill it: a proof "
            "that the audit's 'clean' region is empty - that every technique trips some "
            "barrier. What it does NOT claim: that P != NP is true, that the audit finds "
            "proofs automatically, or any timeline - this is a disciplined search "
            "strategy, not a proof."
        ),
        "ladder_rank": 2, "ladder_tier": "foundations",
    },
    {
        "key": "factoring",
        "name": "Fast Integer Factorization",
        "group": "Cryptography",
        "description": (
            "Is there a fast classical algorithm for factoring large integers? The "
            "security of RSA - the most widely deployed public-key cryptosystem, "
            "invented by Rivest, Shamir, and Adleman in 1978 - rests on the assumption "
            "that factoring is hard. The 129-digit RSA-129 challenge fell in 1994, and "
            "RSA-250, an 829-bit number, was factored in February 2020 using the general "
            "number field sieve, the best known classical algorithm, which still runs in "
            "subexponential but superpolynomial time. No polynomial-time classical "
            "algorithm is known, and none is ruled out."
        ),
        "sig_lens": (
            "The Signature lens treats factoring as the load-bearing wall of internet "
            "trust: everything encrypted under RSA leans on this one unknown. The "
            "Signature approach studies the exact shape of the number field sieve's "
            "cost curve to predict where classical factoring hits its wall, so "
            "migration planning rests on measured curves instead of guesses."
        ),
        "how_it_works": (
            "Factoring sits in a strange limbo: it is in NP and co-NP, it is not known "
            "to be NP-complete, and most experts doubt it is. Peter Shor's 1994 quantum "
            "algorithm factors in polynomial time on a quantum computer, which is why "
            "governments and industry are migrating to post-quantum cryptography - but "
            "no scalable fault-tolerant quantum computer exists yet, so classical "
            "factoring hardness still protects the world's RSA keys today. The general "
            "number field sieve, the classical champion, factors an n-bit integer in "
            "roughly exp(n^(1/3)) time: subexponential, meaning it beats brute force "
            "decisively, but still superpolynomial, meaning it slows to a crawl as keys "
            "grow. RSA-250's 2020 factorization took thousands of core-years. Why it "
            "matters: a classical polynomial factoring algorithm would break RSA, "
            "Diffie-Hellman, and elliptic-curve-adjacent assumptions overnight with no "
            "quantum computer required, while a proof of hardness would put internet "
            "security on rigorous footing for the first time."
        ),
        "key_points": [
            "RSA security rests on factoring being hard for classical computers.",
            "Best classical method: general number field sieve, subexponential time.",
            "RSA-250 (829 bits) factored in 2020 after thousands of core-years.",
            "Shor's algorithm factors in polynomial time - but needs a large quantum computer.",
            "Factoring is in NP and co-NP, yet not known to be NP-complete.",
        ],
        "requirements": [
            "A fast classical algorithm must run in polynomial time on all large inputs.",
            "A hardness proof would likely separate complexity classes - a major breakthrough.",
            "Any claim must be tested against the largest RSA challenge numbers.",
        ],
        "standards": [
            "Rivest R, Shamir A, Adleman L. A method for obtaining digital signatures. CACM; 1978.",
            "Shor P. Algorithms for quantum computation. FOCS; 1994.",
            "Buhler J, Lenstra H, Pomerance C. Factoring integers with the number field sieve. 1993.",
        ],
        "citations": [
            "RSA-129 factored 1994 (Atkins et al.); RSA-250 factored February 2020 (Boudot et al.).",
            "Shor (1994) gave the polynomial-time quantum factoring algorithm.",
        ],
        "solution": (
            "Step 1 - assumption: classical factoring's true complexity is visible in "
            "the measured cost curve of the number field sieve across two decades of "
            "record factorizations, and extrapolating that curve is more reliable than "
            "pure theory. Step 2 - reasoning path: fit the sieve's cost model precisely "
            "to the RSA-129 through RSA-250 record data, then project the crossover "
            "points where larger keys become infeasible under projected hardware growth, "
            "producing a dated 'factoring horizon' table. Step 3 - proposed mechanism: "
            "a living horizon model, updated with each new record, that tells "
            "migrators exactly which key sizes are safe in which years under classical "
            "attack only. What would confirm it: successive records landing inside the "
            "model's predicted bands. What would kill it: an algorithmic improvement "
            "that breaks the fitted curve - which would itself be the factoring "
            "breakthrough everyone watches for. What it does NOT claim: a faster "
            "factoring algorithm, a hardness proof, or any statement about quantum "
            "attacks - this is measurement and forecasting, not cryptanalysis."
        ),
        "ladder_rank": 3, "ladder_tier": "foundations",
    },
    {
        "key": "pcp-pairs",
        "name": "How Many Pairs Break the Post Correspondence Problem",
        "group": "Computability",
        "description": (
            "Emil Post's correspondence problem (1946) asks: given dominoes with strings "
            "on top and bottom, is there a sequence whose top and bottom readings match? "
            "It is undecidable in general, but the boundary is razor-thin and still "
            "partly unknown. With 2 pairs of dominoes the problem is decidable, proven "
            "by Ehrenfeucht, Karhumaki, and Rozenberg in 1982. With 7 or more pairs it "
            "is undecidable, proven by Matiyasevich and Senizergues in 2005. For 3, 4, "
            "5, and 6 pairs, decidability remains open."
        ),
        "sig_lens": (
            "The Signature lens loves sharp thresholds: a problem that flips from "
            "decidable to undecidable somewhere between 2 and 7 domino pairs is a "
            "laboratory for understanding exactly where computation breaks. The "
            "Signature approach attacks the gap from both ends, hunting small "
            "undecidable instances and generalizing the 2-pair decider upward."
        ),
        "how_it_works": (
            "The Post correspondence problem is a classic undecidability showcase: its "
            "proof encodes Turing machine computations as domino tilings, and it is the "
            "go-to reduction target for proving other problems undecidable, from "
            "context-free grammar ambiguity to program verification questions. The "
            "parameterized version PCP(k), with exactly k domino pairs, asks how much "
            "structure is needed before undecidability sets in. The 1982 decidability "
            "proof for PCP(2) is a delicate combinatorial argument about how two pairs "
            "can interact; the 2005 undecidability proof for PCP(7) encodes universal "
            "computation with seven pairs. Between them lies a tiny, embarrassing gap: "
            "four integers - 3, 4, 5, 6 - whose status has resisted four decades of "
            "effort. Why it matters: closing the gap would complete one of the "
            "cleanest threshold results in computability theory, and the techniques "
            "would sharpen every reduction that passes through Post's problem."
        ),
        "key_points": [
            "PCP(2) is decidable (Ehrenfeucht-Karhumaki-Rozenberg, 1982).",
            "PCP(k) for k >= 7 is undecidable (Matiyasevich-Senizergues, 2005).",
            "PCP(3), PCP(4), PCP(5), PCP(6): all open.",
            "The problem is a universal reduction source for undecidability proofs.",
            "The gap has survived four decades of attempts from both sides.",
        ],
        "requirements": [
            "Decidability for k=3 needs a terminating decision procedure for all 3-pair instances.",
            "Undecidability for some k needs an encoding of universal computation in k pairs.",
            "Either result should ideally narrow, not just shift, the gap.",
        ],
        "standards": [
            "Post E. A variant of a recursively unsolvable problem. Bull. AMS; 1946.",
            "Ehrenfeucht A, Karhumaki J, Rozenberg G. The (generalized) Post correspondence problem with lists consisting of two words is decidable. TCS; 1982.",
            "Matiyasevich Y, Senizergues G. Decision problems for semi-Thue systems with a few rules. LICS; 2005.",
        ],
        "citations": [
            "Post (1946) introduced the correspondence problem and proved it undecidable.",
            "The 2-pair and 7-pair results above bracket the open cases 3 through 6.",
        ],
        "solution": (
            "Step 1 - assumption: the threshold is a small integer with a structural "
            "explanation, not an accident - the 2-pair proof and the 7-pair encoding "
            "each exploit specific combinatorial features that can be counted. Step 2 - "
            "reasoning path: work inward from both ends at once - try to compress the "
            "7-pair universal encoding down to 6, 5, 4 pairs, while simultaneously "
            "trying to lift the 2-pair decision procedure to 3 pairs by classifying the "
            "new interaction patterns a third pair allows. Step 3 - proposed mechanism: "
            "an exhaustive search over small universal encodings guided by the "
            "structural features of the known 7-pair construction, paired with a "
            "generalized pair-interaction classifier for the decidability side. What "
            "would confirm it: a 6-pair undecidability encoding, or a 3-pair decider. "
            "What would kill it: a proof that the gap cases require fundamentally new "
            "mathematics unrelated to either endpoint technique. What it does NOT "
            "claim: that the threshold is 3, or 6, or any particular value - only that "
            "attacking from both ends is the disciplined way to find out."
        ),
        "ladder_rank": 4, "ladder_tier": "foundations",
    },
    {
        "key": "k-server",
        "name": "The k-Server Conjecture",
        "group": "Algorithms",
        "description": (
            "Servers sit at points of a metric space; requests arrive one by one, and a "
            "server must move to each request, paying the distance traveled. Can an "
            "online algorithm - one that sees only the past - compete within a factor "
            "of k against an offline adversary that sees the whole future? The k-server "
            "conjecture, posed by Manasse, McGeoch, and Sleator in 1990, says yes: a "
            "deterministic k-competitive algorithm exists. The best known deterministic "
            "algorithm, the work function algorithm of Koutsoupias and Papadimitriou "
            "(1995), is (2k-1)-competitive - tantalizingly close, but the factor of 2 "
            "has survived thirty years."
        ),
        "sig_lens": (
            "The Signature lens sees the k-server problem as the purest test of "
            "decision-making under uncertainty: how much does not knowing the future "
            "really cost? The Signature approach treats the factor-2 gap as a "
            "challenge to the work function algorithm itself - either sharpen its "
            "analysis to k, or find the request sequence that proves 2k-1 is optimal."
        ),
        "how_it_works": (
            "The k-server problem abstracts paging, caching, taxi dispatch, and any "
            "setting where mobile resources serve arriving demand. Competitive analysis, "
            "introduced by Sleator and Tarjan in 1985 for online algorithms, measures an "
            "online strategy against the optimal offline one; a c-competitive algorithm "
            "never pays more than c times the optimum. For k=2 the conjecture is settled "
            "(k-competitive algorithms exist), and for general k the work function "
            "algorithm achieves 2k-1, which was a breakthrough in 1995. Randomized "
            "algorithms do better - polylogarithmic competitive ratios are known - but "
            "randomness is a different game, and the deterministic conjecture stands. "
            "Recent work has chipped at special cases (weighted servers, trees, the "
            "line), yet the general metric space resists. Why it matters: k-server is "
            "the flagship open problem of online computation; its resolution would "
            "either certify a clean, optimal strategy for resource dispatch or reveal a "
            "fundamental price of determinism."
        ),
        "key_points": [
            "Conjecture (1990): a deterministic k-competitive algorithm exists for all metric spaces.",
            "Best known deterministic: (2k-1)-competitive work function algorithm (1995).",
            "Randomized algorithms achieve polylog(k)-competitive ratios.",
            "k=2 is settled; general k is open after 35+ years.",
            "Models paging, caching, dispatch - the economics of serving demand online.",
        ],
        "requirements": [
            "A proof needs an explicit deterministic algorithm with competitive ratio k.",
            "A refutation needs a metric space and request sequence forcing ratio above k.",
            "Results on restricted metrics (trees, line) do not settle the general case.",
        ],
        "standards": [
            "Manasse M, McGeoch L, Sleator D. Competitive algorithms for server problems. J. Algorithms; 1990.",
            "Koutsoupias E, Papadimitriou C. On the k-server conjecture. STOC; 1995.",
            "Bansal N et al. A polylogarithmic-competitive algorithm for the k-server problem. FOCS; 2011.",
        ],
        "citations": [
            "Sleator and Tarjan (1985) founded competitive analysis of online algorithms.",
            "The work function algorithm remains the deterministic champion since 1995.",
        ],
        "solution": (
            "Step 1 - assumption: the truth is at one of the two ends - either the work "
            "function algorithm is secretly k-competitive and its analysis is loose, or "
            "there exists an adversarial sequence forcing 2k-1, and the conjecture is "
            "false as stated. Step 2 - reasoning path: build a computational adversary "
            "that searches small metric spaces and request sequences for high "
            "competitive ratios against the work function algorithm, while in parallel "
            "attempting a potential-function proof of k-competitiveness; whichever "
            "cracks first decides the direction. Step 3 - proposed mechanism: an "
            "adversarial search loop over finite metrics (which often reveal the "
            "asymptotic truth in online problems) coupled with automated potential-"
            "function discovery. What would confirm it: a ratio-k proof, or an explicit "
            "counterexample sequence. What would kill it: evidence that finite "
            "adversarial search cannot reach the true worst case, stalling both prongs. "
            "What it does NOT claim: that the conjecture is true - the search is "
            "genuinely two-sided, and a refutation would be just as valuable."
        ),
        "ladder_rank": 5, "ladder_tier": "foundations",
    },
    {
        "key": "dynamic-optimality",
        "name": "The Dynamic Optimality Conjecture",
        "group": "Algorithms",
        "description": (
            "Is the humble splay tree secretly optimal among all binary search trees? "
            "The dynamic optimality conjecture, posed by Sleator and Tarjan in their "
            "1985 splay tree paper, claims splay trees are O(1)-competitive with any "
            "binary search tree algorithm - even one that knows the future access "
            "sequence. Splay trees are beautifully simple: every access rotates the "
            "node to the root. Forty years later, the best proven bound is the Tango "
            "tree of Demaine, Harmon, Iacono, and Patrascu (2004), which is "
            "O(log log n)-competitive - exponentially closer than trivial, yet still "
            "not constant."
        ),
        "sig_lens": (
            "The Signature lens frames splay trees as self-organizing memory: the data "
            "structure that learns. The Signature approach treats the conjecture as a "
            "question about the geometric view of binary search trees, where rotations "
            "become point sets and optimality becomes a clean combinatorial statement "
            "waiting for the right invariant."
        ),
        "how_it_works": (
            "Binary search trees are the workhorse of ordered data, and for decades the "
            "field assumed balance meant static guarantees like AVL or red-black trees. "
            "Splay trees broke the mold: no stored balance information, just rotate "
            "accessed nodes upward, and a long list of remarkable properties followed - "
            "the working set bound, the dynamic finger bound, static optimality. The "
            "dynamic optimality conjecture says this simple rule is essentially the "
            "best any BST can do, offline knowledge included. The geometric view "
            "(Demaine, Harmon, Iacono, Kane, Patrascu 2009) recast the whole problem: "
            "an access sequence becomes a point set in the plane, and BST executions "
            "become 'arborally satisfied' supersets - turning algorithm design into "
            "geometry. The GreedyFuture algorithm is conjectured optimal in this view "
            "but unproven. Why it matters: a proof would anoint the simplest adaptive "
            "structure as the ultimate one, with consequences for caches, databases, "
            "and every system that serves skewed access patterns."
        ),
        "key_points": [
            "Conjecture (1985): splay trees are O(1)-competitive with the optimal offline BST.",
            "Best proven: Tango trees, O(log log n)-competitive (2004).",
            "The geometric view (2009) recast BST executions as planar point sets.",
            "Splay trees already satisfy the working set, dynamic finger, and static optimality bounds.",
            "GreedyFuture is conjectured optimal but unproven.",
        ],
        "requirements": [
            "A proof must show splay cost within a constant factor of OPT on every sequence.",
            "The geometric view must connect splay executions to arborally satisfied sets.",
            "Partial bounds (working set etc.) are evidence, not proof.",
        ],
        "standards": [
            "Sleator D, Tarjan R. Self-adjusting binary search trees. JACM; 1985.",
            "Demaine E, Harmon D, Iacono J, Patrascu M. Dynamic optimality - almost. SIAM J. Comput.; 2007.",
            "Demaine E et al. The geometry of binary search trees. SODA; 2009.",
        ],
        "citations": [
            "Sleator and Tarjan (1985) introduced splay trees and the conjecture.",
            "The Tango tree (2004/2007) remains the closest proven approach to optimality.",
        ],
        "solution": (
            "Step 1 - assumption: the geometric view is the right battlefield - the "
            "conjecture will fall to a clean invariant about arborally satisfied sets, "
            "not to raw analysis of rotations. Step 2 - reasoning path: characterize "
            "exactly which point sets the splay execution produces for structured "
            "access sequences (sequential, working-set-heavy, finger-heavy), then prove "
            "those sets are within a constant factor of the minimum satisfied superset, "
            "starting with sequence families and widening. Step 3 - proposed mechanism: "
            "a 'satisfaction auditor' that computes, for millions of generated access "
            "sequences, both the splay point set and a lower bound on OPT via the "
            "independent-rectangle bound, hunting for sequences where the ratio spikes - "
            "either the ratio stays bounded (evidence for the conjecture) or a spike "
            "reveals the counterexample shape. What would confirm it: bounded ratios "
            "plus a proof for the observed worst-case families. What would kill it: a "
            "sequence family where splay provably pays super-constant overhead. What it "
            "does NOT claim: that splay is optimal - the auditor is genuinely hunting "
            "counterexamples too."
        ),
        "ladder_rank": 6, "ladder_tier": "foundations",
    },
    {
        "key": "graph-isomorphism",
        "name": "Graph Isomorphism in Polynomial Time",
        "group": "Complexity Theory",
        "description": (
            "Given two graphs, are they the same graph with relabeled vertices? This "
            "deceptively simple question has resisted classification for fifty years. "
            "Graph isomorphism is in NP, and it is also in coAM, which strongly "
            "suggests it is not NP-complete - yet no polynomial-time algorithm is "
            "known. Laszlo Babai's 2015 breakthrough gave a quasipolynomial algorithm "
            "running in n^(polylog n) time, exponentially faster than the previous "
            "best, but still not polynomial. It remains one of the most prominent "
            "problems stuck between P and NP-complete."
        ),
        "sig_lens": (
            "The Signature lens sees graph isomorphism as the identity problem: when "
            "are two descriptions the same thing? The Signature approach studies "
            "Babai's quasipolylog bottleneck directly - the recursive structure that "
            "costs the extra log factors - and asks what canonical invariant would "
            "collapse the recursion."
        ),
        "how_it_works": (
            "Graph isomorphism (GI) is the archetypal NP-intermediate candidate: Ladner's "
            "1975 theorem says such problems exist if P differs from NP, and GI is the "
            "most natural one ever found. Practical solvers like nauty handle enormous "
            "graphs routinely, so the problem is empirically easy - yet theory cannot "
            "certify polynomial time. Babai's 2015 algorithm was a landmark: by "
            "combining group theory (the classification of finite simple groups), "
            "combinatorics, and a clever recursion on highly symmetric substructures, "
            "he shattered the exp(sqrt(n)) barrier that had stood since the 1980s. The "
            "remaining quasipolynomial factor comes from recursion depth on Johnson "
            "graphs and similar obstacles. Meanwhile, GI's cousins - like the string "
            "isomorphism problem Babai actually solved - show the techniques have "
            "reach. Why it matters: GI sits at the crossroads of group theory, "
            "combinatorics, and complexity; settling it would illuminate the structure "
            "of NP itself, and its techniques already power practical symmetry "
            "detection in chemistry, networks, and chip design."
        ),
        "key_points": [
            "GI is in NP and in coAM, hence unlikely to be NP-complete.",
            "Babai (2015): quasipolynomial n^(polylog n) algorithm - the landmark result.",
            "No polynomial-time algorithm known after 50 years.",
            "Practical solvers (nauty) handle huge graphs; theory lags practice.",
            "The natural NP-intermediate candidate since Ladner (1975).",
        ],
        "requirements": [
            "A polynomial algorithm must run in n^O(1) on all graphs.",
            "NP-completeness would require showing GI is as hard as SAT - considered unlikely.",
            "Improvements to the quasipolynomial exponent count as progress.",
        ],
        "standards": [
            "Babai L. Graph isomorphism in quasipolynomial time. STOC; 2016.",
            "McKay B, Piperno A. Practical graph isomorphism II. J. Symb. Comput.; 2014.",
            "Ladner R. On the structure of polynomial time reducibility. JACM; 1975.",
        ],
        "citations": [
            "Babai (2015/2016) broke the decades-old exp(O(sqrt(n log n))) barrier.",
            "Goldreich, Micali, Wigderson (1991) placed GI in coAM.",
        ],
        "solution": (
            "Step 1 - assumption: the quasipolynomial bottleneck is structural - "
            "Babai's recursion pays polylog factors exactly on highly symmetric "
            "configurations, so a canonical invariant that 'breaks' those symmetries "
            "cheaply would collapse the recursion to polynomial. Step 2 - reasoning "
            "path: catalog the hard configurations (Johnson schemes and relatives), "
            "then search for efficiently computable complete invariants on each "
            "family - invariants that already exist for many symmetric families but "
            "have never been assembled into a unified recursion-killer. Step 3 - "
            "proposed mechanism: a 'symmetry-breaker library' that classifies the "
            "input's coherent configuration, dispatches to the family's specialized "
            "canonical labeling routine, and only falls back to Babai recursion on "
            "truly novel configurations. What would confirm it: the fallback set "
            "shrinking to configurations provably handled in polynomial time. What "
            "would kill it: a family of graphs where every complete invariant is "
            "provably expensive - suggesting quasipolynomial is the true complexity. "
            "What it does NOT claim: a polynomial algorithm today, or that one "
            "exists - this is a systematic attack on the known bottleneck."
        ),
        "ladder_rank": 7, "ladder_tier": "foundations",
    },
    {
        "key": "matrix-multiplication",
        "name": "The Exponent of Matrix Multiplication",
        "group": "Algorithms",
        "description": (
            "How fast can two n-by-n matrices be multiplied? The schoolbook method "
            "takes n^3 operations, and the true exponent omega - the smallest number "
            "such that multiplication costs n^(omega+o(1)) - is unknown. Volker "
            "Strassen shocked the world in 1969 with an n^2.81 algorithm. The record "
            "has crept downward for 55 years and now stands below 2.371866, set by "
            "Duan, Wu, and Zhou in 2024. The lower bound is just 2: any algorithm must "
            "at least read the n^2 entries. Almost everyone suspects omega = 2, but "
            "the gap between 2 and 2.371866 will not close itself."
        ),
        "sig_lens": (
            "The Signature lens treats matrix multiplication as the heartbeat of "
            "computation: half of scientific computing is matrix multiplication in "
            "disguise. The Signature approach studies the laser method's tensor "
            "constructions as combinatorial objects in their own right, hunting the "
            "border-rank patterns that would push the exponent all the way to 2."
        ),
        "how_it_works": (
            "Strassen's 1969 discovery - seven multiplications suffice for 2x2 blocks "
            "instead of eight - launched algebraic complexity theory. The modern "
            "arsenal is the laser method of Coppersmith and Winograd (1990), which "
            "analyzes the border rank of matrix multiplication tensors: better tensor "
            "decompositions mean better exponents. Progress has been a slow grind of "
            "ever-more-intricate tensor constructions, with the 2024 Duan-Wu-Zhou "
            "improvement shaving the bound to 2.371866. On the other side, lower "
            "bounds are nearly nonexistent: beyond the trivial 2, the best general "
            "lower bounds barely budge, and there are barrier results suggesting the "
            "laser method itself may be stuck above 2.3. Meanwhile, Strassen-like "
            "algorithms with better constants (not better exponents) are what actually "
            "run in practice. Why it matters: matrix multiplication underlies "
            "scientific simulation, machine learning, graph algorithms, and countless "
            "reductions - the exponent omega is arguably the single most important "
            "constant in algorithms."
        ),
        "key_points": [
            "Exponent omega satisfies 2 <= omega < 2.371866 (Duan-Wu-Zhou, 2024).",
            "Strassen (1969): first sub-cubic algorithm, n^2.81.",
            "The laser method (Coppersmith-Winograd 1990) powers all modern records.",
            "Lower bounds beyond the trivial 2 are essentially nonexistent.",
            "Widely conjectured: omega = 2.",
        ],
        "requirements": [
            "An upper bound needs an explicit tensor construction with analyzed border rank.",
            "A lower bound above 2 would be a historic breakthrough.",
            "Practical relevance needs good constant factors, not just exponents.",
        ],
        "standards": [
            "Strassen V. Gaussian elimination is not optimal. Numer. Math.; 1969.",
            "Coppersmith D, Winograd S. Matrix multiplication via arithmetic progressions. J. Symb. Comput.; 1990.",
            "Duan R, Wu H, Zhou R. Faster matrix multiplication via asymmetric hashing. FOCS; 2023.",
        ],
        "citations": [
            "The 2024 bound 2.371866 is the current record (Duan, Wu, Zhou).",
            "Barrier results suggest the laser method alone may not reach omega = 2.",
        ],
        "solution": (
            "Step 1 - assumption: the remaining gap is combinatorial, not conceptual - "
            "the laser method's tensor powers contain usable structure that current "
            "analyses waste, as each record has come from squeezing the same framework "
            "harder. Step 2 - reasoning path: build a computational search over small "
            "tensor constructions (generalizing the Coppersmith-Winograd tensor) that "
            "directly optimizes the estimated exponent, letting machine search explore "
            "the combinatorial space humans navigate by intuition. Step 3 - proposed "
            "mechanism: a tensor-search loop that generates candidate decompositions, "
            "scores them by the laser-method analysis, and mutates the winners - "
            "essentially applying program search to algebraic complexity. What would "
            "confirm it: a machine-found tensor beating 2.371866, then iterating "
            "downward. What would kill it: a barrier proof that the searched tensor "
            "family cannot beat the current bound, or that the laser method caps above "
            "2.3. What it does NOT claim: omega = 2, or that search replaces insight - "
            "only that the combinatorial core is now searchable."
        ),
        "ladder_rank": 8, "ladder_tier": "foundations",
    },
    {
        "key": "pit-derandomization",
        "name": "Derandomizing Polynomial Identity Testing",
        "group": "Complexity Theory",
        "description": (
            "Given an arithmetic circuit computing a polynomial, is the polynomial "
            "identically zero? Randomized algorithms solve this easily: the "
            "Schwartz-Zippel lemma says evaluating at random points catches nonzero "
            "polynomials with high probability. But no deterministic polynomial-time "
            "algorithm is known. The Kabanets-Impagliazzo theorem (2004) revealed the "
            "stunning stakes: derandomizing identity testing is equivalent to proving "
            "circuit lower bounds - so this innocent-looking problem is secretly as "
            "hard as the hardest problems in complexity theory."
        ),
        "sig_lens": (
            "The Signature lens reads identity testing as the question of whether "
            "randomness is ever truly needed to verify algebraic truth. The Signature "
            "approach builds explicit hitting sets - deterministic point collections "
            "that catch every small circuit's nonzero polynomial - starting from "
            "restricted circuit classes and climbing."
        ),
        "how_it_works": (
            "Polynomial identity testing (PIT) is the algebraic cousin of checking "
            "whether a formula simplifies to zero. The randomized algorithm is a "
            "one-line marvel: plug in random numbers, and a nonzero degree-d "
            "polynomial fools you with probability at most d over field size. "
            "Derandomization - replacing the coins with a deterministic procedure - "
            "is the central challenge. Kabanets and Impagliazzo proved in 2004 that "
            "even a weak derandomization of PIT implies superpolynomial lower bounds "
            "for arithmetic circuits, and conversely strong lower bounds yield "
            "derandomization. This win-win means every attempt at PIT derandomization "
            "is simultaneously an attack on circuit lower bounds. For restricted "
            "models - depth-3 circuits, read-once formulas, noncommutative circuits - "
            "deterministic tests exist, but the general case stands. Why it matters: "
            "PIT is the cleanest test case for the power of randomness in computation, "
            "and its resolution either way rewrites algebraic complexity."
        ),
        "key_points": [
            "Randomized PIT is easy via the Schwartz-Zippel lemma.",
            "No deterministic polynomial-time algorithm known for general circuits.",
            "Kabanets-Impagliazzo (2004): derandomizing PIT is equivalent to circuit lower bounds.",
            "Deterministic tests exist for restricted models (depth-3, read-once, noncommutative).",
            "The stakes are win-win: progress either way is a breakthrough.",
        ],
        "requirements": [
            "A derandomization needs an explicit hitting set constructible in polynomial time.",
            "The Kabanets-Impagliazzo connection must be respected: weak derandomization already implies lower bounds.",
            "Restricted-model results are progress but do not settle the general case.",
        ],
        "standards": [
            "Schwartz J. Fast probabilistic algorithms for verification of polynomial identities. JACM; 1980.",
            "Kabanets V, Impagliazzo R. Derandomizing polynomial identity tests means proving circuit lower bounds. Comput. Complexity; 2004.",
        ],
        "citations": [
            "Zippel (1979) and Schwartz (1980) gave the randomized identity test.",
            "The 2004 Kabanets-Impagliazzo equivalence made PIT derandomization a central problem.",
        ],
        "solution": (
            "Step 1 - assumption: explicit hitting sets for general circuits will be "
            "found by climbing the restriction ladder, since every restricted model "
            "so far has yielded to structural analysis of its polynomials. Step 2 - "
            "reasoning path: take the strongest known restricted derandomization "
            "(bounded-depth multilinear formulas) and identify the exact structural "
            "property the hitting set exploits, then generalize that property one "
            "notch - allowing slightly deeper or slightly less restricted circuits - "
            "and rebuild the hitting set. Step 3 - proposed mechanism: an iterative "
            "'restriction ladder climber' that maintains an explicit hitting set "
            "family parameterized by depth and read-restrictions, each rung certified "
            "by a deterministic test. What would confirm it: reaching unrestricted "
            "circuits - a full derandomization. What would kill it: a rung where the "
            "structural property provably fails, marking the true boundary of the "
            "technique. What it does NOT claim: that derandomization is possible - "
            "the Kabanets-Impagliazzo theorem says failure would hand us circuit "
            "lower bounds instead, which is also victory."
        ),
        "ladder_rank": 9, "ladder_tier": "foundations",
    },
    {
        "key": "p-vs-bpp",
        "name": "Does Randomness Help? (P vs BPP)",
        "group": "Complexity Theory",
        "description": (
            "Randomized algorithms flip coins; deterministic ones do not. BPP is the "
            "class of problems solvable in polynomial time with bounded-error "
            "randomness - the home of fast primality testing and countless practical "
            "algorithms. Does randomness add real power, or can every randomized "
            "algorithm be derandomized? The Impagliazzo-Wigderson theorem (1997) says "
            "that under plausible circuit lower bounds, P equals BPP: randomness "
            "would be merely a convenience. But the required lower bounds are "
            "unproven, so the question stands open."
        ),
        "sig_lens": (
            "The Signature lens asks whether the universe charges a fee for coin "
            "flips: is randomness a fundamental resource or a shortcut for the "
            "impatient? The Signature approach treats pseudorandom generators as "
            "the bridge - build generators strong enough to fool every efficient "
            "test, and randomness dissolves into determinism."
        ),
        "how_it_works": (
            "Randomness feels powerful: the Miller-Rabin primality test, polynomial "
            "identity testing, and approximate counting all run fast with coins and "
            "have no known deterministic counterparts of equal elegance. Yet the "
            "derandomization program, launched by Yao, Blum-Micali, and Nisan-"
            "Wigderson, argues this power is an illusion sustained by unproven "
            "hardness. The Nisan-Wigderson generator (1994) turns a hard function "
            "into pseudorandom bits that fool all small circuits; Impagliazzo and "
            "Wigderson (1997) showed that if some problem in exponential time needs "
            "exponential-size circuits - a widely believed but unproven assumption - "
            "then every BPP algorithm derandomizes. So P vs BPP hinges on circuit "
            "lower bounds, the same wall blocking P vs NP. Partial derandomizations "
            "exist for space-bounded and restricted models. Why it matters: settling "
            "it decides whether randomness is a genuine computational resource, with "
            "consequences for cryptography, where randomness is provably essential, "
            "and for algorithm design everywhere else."
        ),
        "key_points": [
            "BPP: polynomial time with bounded-error randomness; home of Miller-Rabin and friends.",
            "Impagliazzo-Wigderson (1997): plausible circuit lower bounds imply P = BPP.",
            "The Nisan-Wigderson generator converts hardness into pseudorandomness.",
            "Randomness is provably essential in cryptography regardless of the outcome.",
            "The question reduces to unproven circuit lower bounds.",
        ],
        "requirements": [
            "P = BPP needs either the assumed lower bounds or an unconditional derandomization.",
            "P != BPP needs an explicit problem in BPP provably outside P.",
            "Any resolution must handle the cryptographic necessity of randomness separately.",
        ],
        "standards": [
            "Nisan N, Wigderson A. Hardness vs randomness. JCSS; 1994.",
            "Impagliazzo R, Wigderson A. P = BPP if E requires exponential circuits. STOC; 1997.",
        ],
        "citations": [
            "Yao (1982) founded the theory connecting pseudorandomness to hardness.",
            "The 1997 Impagliazzo-Wigderson theorem is the central conditional derandomization result.",
        ],
        "solution": (
            "Step 1 - assumption: the hardness-to-randomness connection is the true "
            "shape of the answer - derandomization will come from stronger "
            "pseudorandom generators, not from clever simulation tricks. Step 2 - "
            "reasoning path: push the Nisan-Wigderson framework to its limits by "
            "constructing generators from weaker and weaker hardness assumptions, "
            "tracking exactly how much hardness each derandomization result consumes, "
            "until the assumption becomes provable or the framework provably stalls. "
            "Step 3 - proposed mechanism: a 'hardness budget' ledger that pairs every "
            "BPP algorithm family with the weakest assumption derandomizing it, "
            "systematically spending down the budget toward unconditional results. "
            "What would confirm it: an unconditional generator fooling all "
            "polynomial tests - P = BPP outright. What would kill it: a proof that "
            "the Nisan-Wigderson approach needs unprovable hardness, forcing a "
            "completely new idea. What it does NOT claim: that P = BPP is true - the "
            "ledger is honest about both directions, and cryptography keeps its "
            "randomness either way."
        ),
        "ladder_rank": 10, "ladder_tier": "foundations",
    },
    {
        "key": "one-way-functions",
        "name": "Do One-Way Functions Exist?",
        "group": "Cryptography",
        "description": (
            "A one-way function is easy to compute but hard to invert - the "
            "foundational primitive of cryptography. If they exist, then P differs "
            "from NP; if P equals NP, they cannot exist. Yet even assuming P differs "
            "from NP, nobody knows whether one-way functions exist: worst-case "
            "hardness does not obviously imply average-case hardness. Candidates "
            "abound - integer multiplication (factoring), modular exponentiation "
            "(discrete log), lattice problems - but every candidate is an unproven "
            "assumption, and the existence question is wide open."
        ),
        "sig_lens": (
            "The Signature lens sees one-way functions as the asymmetry the digital "
            "world is built on: easy forward, hard backward. The Signature approach "
            "maps the exact gap between worst-case hardness (P vs NP) and the "
            "average-case hardness cryptography needs, hunting the missing bridge "
            "theorem."
        ),
        "how_it_works": (
            "Modern cryptography was born in 1976 when Diffie and Hellman showed that "
            "asymmetric encryption was possible in principle; Rivest, Shamir, and "
            "Adleman's RSA (1978) made it practical. Goldreich's school then proved "
            "that one-way functions are the minimal assumption: they imply "
            "pseudorandom generators, digital signatures, zero-knowledge proofs, and "
            "much more. But existence is unproven. The core difficulty is "
            "average-case complexity: P vs NP is about worst cases, while a one-way "
            "function must be hard on random inputs. Levin's theory of average-case "
            "completeness (1986) and the study of distributional NP try to bridge "
            "this, and lattice problems like Learning With Errors offer plausible "
            "average-case hardness - but 'plausible' is doing heavy lifting. "
            "Impagliazzo's five worlds (1995) map the possibilities: in 'Minicrypt' "
            "one-way functions exist but public-key crypto does not; in 'Cryptomania' "
            "everything exists. Which world we inhabit is unknown. Why it matters: "
            "every encrypted message, signed update, and digital identity on Earth "
            "assumes an affirmative answer."
        ),
        "key_points": [
            "One-way functions imply P != NP; their existence is unproven.",
            "They are the minimal assumption for signatures, PRGs, and much of crypto.",
            "The gap is worst-case vs average-case hardness.",
            "Candidates: factoring, discrete log, lattice problems (LWE).",
            "Impagliazzo's worlds map the possible realities; ours is unknown.",
        ],
        "requirements": [
            "Existence needs a function family easy to compute, hard to invert on average.",
            "Non-existence would collapse Minicrypt and Cryptomania - an earthquake result.",
            "Candidates must survive sustained cryptanalytic attack to stay plausible.",
        ],
        "standards": [
            "Diffie W, Hellman M. New directions in cryptography. IEEE TIT; 1976.",
            "Goldreich O. Foundations of Cryptography, Vol. 1. Cambridge; 2001.",
            "Impagliazzo R. A personal view of average-case complexity. SCT; 1995.",
        ],
        "citations": [
            "Levin (1986) founded average-case completeness theory.",
            "Regev (2005) introduced Learning With Errors, the leading hardness candidate.",
        ],
        "solution": (
            "Step 1 - assumption: the missing piece is a worst-case to average-case "
            "reduction for some natural NP problem - the kind of theorem that would "
            "turn P != NP into one-way functions. Step 2 - reasoning path: survey "
            "every known worst-to-average reduction (lattices have them; most problems "
            "do not), extract the structural property that makes reductions possible "
            "(random self-reducibility and its cousins), then hunt that property in "
            "new problems via computational search over small instances. Step 3 - "
            "proposed mechanism: a 'reduction prospector' that tests candidate "
            "problems for self-reducibility structure at small scales, flagging the "
            "ones whose structure generalizes. What would confirm it: a new natural "
            "problem with a worst-to-average reduction - a fresh one-way function "
            "candidate grounded in worst-case hardness. What would kill it: a "
            "theorem that random self-reducibility is rare, explaining why only "
            "lattices qualify. What it does NOT claim: that one-way functions "
            "exist - the prospector may instead map exactly why they are hard to "
            "ground, which is also progress."
        ),
        "ladder_rank": 11, "ladder_tier": "foundations",
    },
    # ---------------------------------------------------------- COMPOUNDED
    {
        "key": "np-vs-conp",
        "name": "NP vs co-NP",
        "group": "Complexity Theory",
        "description": (
            "NP captures problems with short proofs of YES answers; co-NP captures "
            "those with short proofs of NO answers. Is every NO-instance of an NP "
            "problem certifiable just as briefly? If NP equaled co-NP, the polynomial "
            "hierarchy would collapse to its first level - so most experts believe "
            "they differ. Yet the flagship test case, TAUT (the set of boolean "
            "tautologies), has resisted all attempts: nobody knows whether "
            "tautologies always have short propositional proofs, and the question is "
            "equivalent to asking whether proof systems can be optimal."
        ),
        "sig_lens": (
            "The Signature lens frames NP vs co-NP as the symmetry question: is "
            "'no' as easy to certify as 'yes'? The Signature approach attacks "
            "through proof complexity - since NP = co-NP is equivalent to short "
            "proofs for all tautologies, the hunt becomes a search for hard "
            "tautology families."
        ),
        "how_it_works": (
            "Cook and Reckhow's 1979 theory of proof systems made the connection "
            "precise: NP = co-NP if and only if there exists a propositional proof "
            "system in which every tautology has a polynomial-size proof. So the "
            "question becomes concrete: exhibit tautologies needing long proofs in "
            "every proof system. For weak systems like resolution, exponential lower "
            "bounds exist (Haken 1985, for the pigeonhole principle). For stronger "
            "systems - Frege, extended Frege - lower bounds are the great open "
            "problem of proof complexity, and separating them from each other is "
            "open too. The Krajicek-Pudlak program and feasible interpolation try "
            "to convert circuit lower bounds into proof lower bounds. Why it "
            "matters: a separation would prove that unsatisfiability sometimes has "
            "no short certificate, with consequences for automated theorem proving, "
            "verification, and the limits of mathematical proof itself."
        ),
        "key_points": [
            "NP = co-NP iff every tautology has a short proof in some proof system.",
            "NP = co-NP would collapse the polynomial hierarchy.",
            "Exponential lower bounds exist for resolution (Haken 1985) but not for Frege.",
            "The flagship test case: short proofs for TAUT.",
            "Consensus leans toward separation; proof is missing.",
        ],
        "requirements": [
            "Separation needs tautologies hard for every propositional proof system.",
            "Equality needs one optimal proof system with polynomial proofs for all tautologies.",
            "Weak-system lower bounds do not separate NP from co-NP.",
        ],
        "standards": [
            "Cook S, Reckhow R. The relative efficiency of propositional proof systems. JSL; 1979.",
            "Haken A. The intractability of resolution. TCS; 1985.",
            "Krajicek J. Bounded Arithmetic, Propositional Logic, and Complexity Theory. Cambridge; 1995.",
        ],
        "citations": [
            "Cook and Reckhow (1979) linked NP vs co-NP to optimal proof systems.",
            "Haken (1985) proved exponential resolution lower bounds for the pigeonhole principle.",
        ],
        "solution": (
            "Step 1 - assumption: the separation, if true, will be witnessed by an "
            "explicit tautology family whose hardness can be recognized "
            "combinatorially - as the pigeonhole principle was for resolution. Step "
            "2 - reasoning path: generate candidate tautology families from "
            "combinatorial principles (pigeonhole variants, clique-coloring, "
            "Tseitin formulas on expanders), then test their proof complexity "
            "empirically against strong SAT solvers and proof-search heuristics at "
            "small scales, looking for families where proof length explodes. Step 3 "
            "- proposed mechanism: a 'hard-tautology prospector' that breeds "
            "combinatorial principles and measures proof-length growth, nominating "
            "the steepest families for theoretical attack. What would confirm it: a "
            "family with provable superpolynomial lower bounds in Frege or stronger. "
            "What would kill it: every candidate family yielding to some proof "
            "system - suggesting an optimal system might exist. What it does NOT "
            "claim: that NP differs from co-NP - the prospector hunts witnesses, and "
            "an empty hunt is data too."
        ),
        "ladder_rank": 12, "ladder_tier": "compounded",
    },
    {
        "key": "unique-games",
        "name": "The Unique Games Conjecture",
        "group": "Complexity Theory",
        "description": (
            "Subhash Khot's Unique Games Conjecture (2002) proposes that a certain "
            "constraint satisfaction problem - distinguishing nearly-satisfiable "
            "unique games from highly unsatisfiable ones - is NP-hard. If true, it "
            "pins down the exact approximability of countless optimization problems: "
            "the Goemans-Williamson 0.878 approximation for Max-Cut would be optimal, "
            "and Raghavendra's 2008 result shows semidefinite programming would be "
            "optimal for every constraint satisfaction problem. Twenty years of "
            "attacks have neither proved nor refuted it."
        ),
        "sig_lens": (
            "The Signature lens sees the Unique Games Conjecture as the keystone of "
            "approximation: one conjecture that would lock in the limits of efficient "
            "optimization everywhere. The Signature approach stress-tests the "
            "conjecture's most vulnerable predictions - the claimed optimal ratios - "
            "by hunting for algorithms that beat them."
        ),
        "how_it_works": (
            "Approximation algorithms cope with NP-hardness by settling for near-"
            "optimal solutions; the PCP theorem (1992) lets us prove some problems "
            "cannot be approximated beyond certain ratios. Khot's conjecture would "
            "complete the picture: for Max-Cut, the 0.878 ratio of Goemans and "
            "Williamson (1995) would be the best possible; for Vertex Cover, no "
            "algorithm could beat 2 - epsilon. Evidence for the conjecture includes "
            "its many consequences holding up and the failure of algorithmic attacks "
            "(subexponential algorithms exist for unique games, Arora-Barak-Steurer "
            "2010, but they do not refute it). Evidence against includes Khot and "
            "Moshkovitz's results and the feeling that such a sweeping conjecture "
            "should have fallen by now. Why it matters: it is the single most "
            "consequential open question in approximation algorithms - its truth "
            "value fixes the approximability of nearly every discrete optimization "
            "problem."
        ),
        "key_points": [
            "UGC (Khot 2002): distinguishing almost-satisfiable unique games is NP-hard.",
            "If true: Goemans-Williamson 0.878 for Max-Cut is optimal; SDP optimal for all CSPs.",
            "Subexponential algorithms exist but do not refute the conjecture.",
            "Twenty years of attacks from both sides; still standing.",
            "The keystone of modern hardness of approximation.",
        ],
        "requirements": [
            "A proof must show NP-hardness of the unique games gap problem.",
            "A refutation needs a polynomial algorithm beating a UGC-predicted threshold.",
            "Subexponential algorithms are consistent with the conjecture.",
        ],
        "standards": [
            "Khot S. On the power of unique 2-prover 1-round games. STOC; 2002.",
            "Raghavendra P. Optimal algorithms and inapproximability results for every CSP? STOC; 2008.",
            "Goemans M, Williamson D. Improved approximation algorithms for maximum cut. JACM; 1995.",
        ],
        "citations": [
            "Arora, Barak, Steurer (2010) gave subexponential algorithms for unique games.",
            "Raghavendra (2008) showed UGC implies SDP optimality for all CSPs.",
        ],
        "solution": (
            "Step 1 - assumption: the conjecture's most falsifiable predictions are "
            "its optimal approximation ratios - if any UGC-predicted threshold can be "
            "beaten algorithmically, the conjecture falls. Step 2 - reasoning path: "
            "systematically attack the predicted-optimal ratios (Max-Cut 0.878, "
            "Vertex Cover 2) with algorithm search: semidefinite hierarchies "
            "(Sum-of-Squares), spectral methods, and learned heuristics, measuring "
            "achieved ratios on hard instance families. Step 3 - proposed mechanism: "
            "a 'threshold assault' pipeline that breeds hard instances and throws "
            "ever-stronger SDP hierarchies at them, tracking the gap between achieved "
            "and predicted ratios. What would confirm the conjecture: the gaps "
            "refusing to close as hierarchies strengthen - evidence the thresholds "
            "are real. What would kill it: any algorithm beating a predicted-optimal "
            "ratio on a valid instance family. What it does NOT claim: that UGC is "
            "true or false - the pipeline measures the gaps honestly, and a "
            "refutation would be the bigger prize."
        ),
        "ladder_rank": 13, "ladder_tier": "compounded",
    },
    {
        "key": "exponential-time-hypothesis",
        "name": "The Exponential Time Hypothesis",
        "group": "Complexity Theory",
        "description": (
            "How fast can 3-SAT really be solved? The Exponential Time Hypothesis "
            "(ETH), formulated by Impagliazzo and Paturi in 1999, asserts that 3-SAT "
            "with n variables needs 2^(Omega(n)) time - no subexponential algorithm "
            "exists. Its stronger sibling SETH says even the base of the exponent "
            "cannot be pushed below 2. ETH is the foundation of fine-grained "
            "complexity: hundreds of lower bounds for problems in P - edit distance, "
            "dynamic programming staples, graph diameter - are all conditional on "
            "ETH or SETH."
        ),
        "sig_lens": (
            "The Signature lens treats ETH as the speed limit posted inside "
            "polynomial time itself: even 'easy' problems may hide exponential "
            "cores. The Signature approach measures real SAT solver scaling with "
            "fanatical precision, because the exact exponent is where theory meets "
            "engineering."
        ),
        "how_it_works": (
            "Classical complexity sorts problems into P vs NP; fine-grained "
            "complexity asks for the exact exponent. The sparsification lemma "
            "(Impagliazzo, Paturi, Zane 2001) showed ETH is robust - it is "
            "equivalent to forbidding 2^(o(n)) algorithms even for sparse formulas. "
            "From ETH and SETH flow conditional lower bounds: under SETH, edit "
            "distance needs nearly quadratic time, diameter approximation is hard, "
            "and dozens of dynamic programs are essentially optimal. The best known "
            "3-SAT algorithms run in about 1.3^n (PPSZ and its refinements), far "
            "above the 2^(o(n)) that would refute ETH but far below naive 2^n. "
            "Williams' 2010 program connecting SAT algorithms to circuit lower "
            "bounds showed that even slightly faster SAT solvers imply "
            "breakthroughs. Why it matters: ETH underwrites the optimality claims "
            "of half the algorithms taught in universities - if it falls, the "
            "textbooks need rewriting."
        ),
        "key_points": [
            "ETH (1999): 3-SAT needs 2^(Omega(n)) time; no subexponential algorithm.",
            "SETH: the base of the exponent cannot be improved below 2.",
            "Hundreds of fine-grained lower bounds in P are conditional on ETH/SETH.",
            "Best 3-SAT algorithms run around 1.3^n - consistent with ETH.",
            "Faster SAT algorithms would imply circuit lower bounds (Williams 2010).",
        ],
        "requirements": [
            "Refuting ETH needs a 2^(o(n)) algorithm for 3-SAT.",
            "Refuting SETH needs (2-epsilon)^n for some epsilon > 0.",
            "Conditional lower bounds stand or fall with the hypotheses.",
        ],
        "standards": [
            "Impagliazzo R, Paturi R. On the complexity of k-SAT. JCSS; 2001.",
            "Impagliazzo R, Paturi R, Zane F. Which problems have strongly exponential complexity? JCSS; 2001.",
            "Williams R. Improving exhaustive search implies superpolynomial lower bounds. STOC; 2010.",
        ],
        "citations": [
            "The sparsification lemma (2001) made ETH equivalent across sparse and dense formulas.",
            "Fine-grained complexity (Vassilevska Williams 2015+) built the ETH-based lower bound web.",
        ],
        "solution": (
            "Step 1 - assumption: the true 3-SAT exponent is an empirical quantity "
            "that can be measured - solver scaling on hard random and crafted "
            "instances reveals the exponent's shape long before theory pins it. "
            "Step 2 - reasoning path: benchmark the best SAT solvers (conflict-"
            "driven clause learning and PPSZ-style) across carefully scaled "
            "instance families, fitting the runtime exponent precisely and "
            "watching whether it drifts toward subexponential as n grows. Step 3 - "
            "proposed mechanism: an 'exponent observatory' that continuously "
            "measures solver scaling, flags any family where the fitted exponent "
            "dips, and subjects dips to theoretical analysis - either a new "
            "algorithmic idea or a measurement artifact. What would confirm ETH: "
            "exponents holding steady at Omega(n) across all families and solver "
            "generations. What would kill it: a family with genuinely subexponential "
            "scaling that survives scrutiny. What it does NOT claim: that ETH is "
            "true - the observatory reports measurements, and a refutation would be "
            "a landmark discovery."
        ),
        "ladder_rank": 14, "ladder_tier": "compounded",
    },
    {
        "key": "bqp-vs-np",
        "name": "Can Quantum Computers Crack NP-Complete Problems?",
        "group": "Quantum Computing",
        "description": (
            "Shor's algorithm factors integers in polynomial time on a quantum "
            "computer - but factoring is probably not NP-complete. Can quantum "
            "computers solve NP-complete problems like SAT or the traveling "
            "salesman efficiently? The class BQP captures efficient quantum "
            "computation; whether NP is contained in BQP is wide open. Grover's "
            "algorithm gives only a quadratic speedup for unstructured search - "
            "2^(n/2) instead of 2^n - and oracle results (Bennett, Bernstein, "
            "Brassard, Vazirani 1997) suggest NP-complete problems resist even "
            "quantum attack in the black-box model."
        ),
        "sig_lens": (
            "The Signature lens asks what quantum mechanics actually buys: a new "
            "continent of easy problems, or just a faster ship along known routes? "
            "The Signature approach catalogs exactly which problem structures "
            "quantum algorithms exploit - periodicity, symmetry, amplitude "
            "amplification - and maps the NP-complete landscape against them."
        ),
        "how_it_works": (
            "Quantum computing's power comes from interference and entanglement, "
            "famously harnessed by Shor (1994) for factoring and discrete log via "
            "the quantum Fourier transform, and by Grover (1996) for quadratic "
            "search speedups. But NP-complete problems have resisted: no quantum "
            "algorithm beats the best classical ones by more than polynomial "
            "factors on any NP-complete problem, and the BBBV result shows that "
            "relative to a random oracle, NP is not in BQP - quantum computers "
            "cannot solve black-box NP search exponentially faster. Adiabatic "
            "quantum computing and QAOA target optimization heuristically, but "
            "without proven exponential speedups. The question 'is NP in BQP?' is "
            "independent of P vs NP: even if P differed from NP, quantum machines "
            "might still fail on NP-complete problems. Why it matters: a quantum "
            "algorithm for SAT would break not just RSA but the entire "
            "complexity-theoretic worldview - while a proof of impossibility would "
            "draw the first rigorous map of quantum limits."
        ),
        "key_points": [
            "Shor factors efficiently; no quantum speedup known for NP-complete problems.",
            "Grover gives only quadratic speedup for unstructured search.",
            "BBBV (1997): relative to a random oracle, NP is not in BQP.",
            "The question is independent of P vs NP.",
            "QAOA and adiabatic methods are heuristic, without proven exponential gains.",
        ],
        "requirements": [
            "A positive answer needs an explicit quantum algorithm beating classical on an NP-complete problem.",
            "A negative answer needs a proof that BQP does not contain NP - far beyond current techniques.",
            "Oracle separations guide intuition but do not settle the unrelativized question.",
        ],
        "standards": [
            "Shor P. Algorithms for quantum computation. FOCS; 1994.",
            "Grover L. A fast quantum mechanical algorithm for database search. STOC; 1996.",
            "Bennett C et al. Strengths and weaknesses of quantum computing. SIAM J. Comput.; 1997.",
        ],
        "citations": [
            "Bernstein and Vazirani (1993/1997) defined BQP.",
            "The BBBV oracle result remains the strongest evidence of quantum limits on NP search.",
        ],
        "solution": (
            "Step 1 - assumption: quantum advantage, where it exists, comes from "
            "exploitable structure (periodicity for Shor, amplitude amplification "
            "for Grover) - so the question reduces to whether NP-complete problems "
            "hide such structure. Step 2 - reasoning path: build a 'structure "
            "atlas' of NP-complete problems, testing each family for hidden "
            "periodic, symmetric, or algebraic structure amenable to quantum "
            "Fourier sampling, and simultaneously catalog the oracle barriers each "
            "family faces. Step 3 - proposed mechanism: a systematic program that "
            "pairs each NP-complete problem family with the quantum algorithmic "
            "primitives, scoring structural compatibility - directing quantum "
            "algorithm design at the most compatible families first. What would "
            "confirm quantum limits: every family scoring incompatible, with the "
            "incompatibility provable - a wall of no-go theorems. What would kill "
            "the pessimism: one family with exploitable structure yielding a real "
            "superpolynomial speedup. What it does NOT claim: that NP is outside "
            "BQP, or inside it - the atlas maps the terrain; the theorems come later."
        ),
        "ladder_rank": 15, "ladder_tier": "compounded",
    },
    {
        "key": "quantum-error-correction",
        "name": "Fault-Tolerant Quantum Computing at Scale",
        "group": "Quantum Computing",
        "description": (
            "Quantum states are fragile: noise decoheres them in microseconds. The "
            "threshold theorem (Aharonov and Ben-Or, 1996-1997) proves that if the "
            "physical error rate is below a threshold, arbitrarily long quantum "
            "computations are possible via error correction - but the overhead is "
            "enormous, with thousands of physical qubits per logical qubit. Surface "
            "codes (Kitaev 2003, Fowler et al.) are the leading approach. The open "
            "problem is practical: can we build and operate a million-physical-"
            "qubit machine with logical error rates low enough for useful algorithms "
            "like Shor's? No such machine exists, and the engineering road is "
            "unmapped."
        ),
        "sig_lens": (
            "The Signature lens treats error correction as the tax physics charges "
            "for coherence: the question is whether the tax is payable. The "
            "Signature approach tracks the overhead curve - physical qubits per "
            "logical qubit over time - as the field's true progress metric, and "
            "hunts code families that bend the curve."
        ),
        "how_it_works": (
            "Peter Shor's 1995 9-qubit code showed quantum error correction was "
            "possible at all, defeating the intuition that measuring to correct "
            "would destroy the quantum state. The threshold theorem then promised "
            "scalability in principle: below threshold error rates, concatenated "
            "codes suppress logical errors exponentially. In practice, the field "
            "converged on topological surface codes, which need only nearest-"
            "neighbor interactions and have high thresholds around 1%. Recent "
            "milestones - Google's 2024 demonstration of below-threshold surface "
            "code operation, with logical error decreasing as code distance grows - "
            "are genuine progress. But the gap to utility is vast: a useful "
            "Shor-scale machine needs thousands of logical qubits, meaning millions "
            "of physical qubits with fast, reliable control and readout. New code "
            "families (quantum LDPC codes, 2022-2024) promise far better overhead "
            "in theory but are harder to implement. Why it matters: without fault "
            "tolerance, quantum computers remain noisy toys; with it, they become "
            "the machines that break RSA and simulate molecules."
        ),
        "key_points": [
            "Threshold theorem (1996-97): below-threshold errors allow arbitrarily long computation.",
            "Surface codes are the leading practical family; ~1000:1 physical-to-logical overhead.",
            "Google (2024) demonstrated below-threshold scaling of logical error with code distance.",
            "Quantum LDPC codes promise much lower overhead but are harder to build.",
            "No million-qubit fault-tolerant machine exists; the engineering path is open.",
        ],
        "requirements": [
            "Progress needs logical error rates falling exponentially with code distance.",
            "Overhead claims must include control, readout, and decoding costs.",
            "A useful machine needs thousands of logical qubits, not dozens.",
        ],
        "standards": [
            "Aharonov D, Ben-Or M. Fault-tolerant quantum computation with constant error rate. STOC; 1997.",
            "Kitaev A. Fault-tolerant quantum computation by anyons. Ann. Phys.; 2003.",
            "Fowler A et al. Surface codes: towards practical large-scale quantum computation. PRA; 2012.",
        ],
        "citations": [
            "Shor (1995) invented quantum error correction with the 9-qubit code.",
            "Google Quantum AI (Nature 2024) showed below-threshold surface code memory.",
        ],
        "solution": (
            "Step 1 - assumption: the winning code family will be decided by the "
            "overhead curve, not by theory alone - so the decisive work is "
            "measuring and projecting physical-qubits-per-logical-qubit across "
            "code families under realistic noise. Step 2 - reasoning path: build "
            "an open overhead model that takes published error budgets (gate "
            "fidelity, readout, decoding latency) and computes the true cost per "
            "logical qubit for surface codes, LDPC codes, and concatenated codes, "
            "then project each family's curve five and ten years out. Step 3 - "
            "proposed mechanism: a living 'fault-tolerance roadmap' that ranks "
            "code families by projected overhead at utility scale and flags which "
            "engineering milestones (readout speed, fabrication yield) move each "
            "curve most. What would confirm it: successive hardware generations "
            "landing on the projected curves, converging on a winning family. What "
            "would kill it: a noise source the models miss - correlated errors "
            "that break every code family's assumptions. What it does NOT claim: "
            "that fault tolerance at scale is achievable, or when - the roadmap "
            "measures the climb; it does not guarantee the summit."
        ),
        "ladder_rank": 16, "ladder_tier": "compounded",
    },
    {
        "key": "quantum-pcp",
        "name": "The Quantum PCP Conjecture",
        "group": "Quantum Computing",
        "description": (
            "The classical PCP theorem says proofs can be checked by reading only a "
            "few bits. Its quantum analogue - the quantum PCP conjecture of Aharonov, "
            "Arad, Landau, and Vazirani - asks whether the ground-state energy of a "
            "local quantum Hamiltonian remains hard to approximate even with a "
            "constant promise gap. It would imply that quantum many-body systems "
            "have no succinct classical description even approximately. The related "
            "NLTS theorem (no low-energy trivial states) was proven in 2022 by "
            "Anshu, Breuckmann, and Nirkhe, but the full quantum PCP conjecture "
            "remains open."
        ),
        "sig_lens": (
            "The Signature lens sees the quantum PCP conjecture as the question of "
            "whether nature's hardest puzzles stay hard when you squint: does "
            "approximation buy any relief in the quantum world? The Signature "
            "approach builds the conjecture a ladder of partial results - NLTS "
            "first, then stronger gap amplification - climbing toward the full "
            "statement."
        ),
        "how_it_works": (
            "The classical PCP theorem (Arora et al. 1992/1998) is among the deepest "
            "results in computer science: every NP proof can be rewritten so that "
            "checking a constant number of bits suffices, which is why "
            "approximation hardness results exist at all. The quantum version "
            "replaces classical constraint satisfaction with local Hamiltonians - "
            "the energy landscapes of quantum many-body physics - and asks whether "
            "estimating ground energies stays QMA-hard with a constant gap. A "
            "proof would mean that even approximate classical descriptions of "
            "quantum systems are intractable, with sweeping implications for "
            "condensed matter physics and quantum chemistry. The 2022 NLTS proof "
            "was a milestone: it constructed Hamiltonians whose low-energy states "
            "all require deep quantum circuits. But gap amplification - Dinur's "
            "key classical technique - has no quantum analogue yet, and that is "
            "the wall. Why it matters: it would be the quantum PCP theorem, "
            "completing the hardness-of-approximation story for the quantum world "
            "and drawing a hard line around what physics can ever be simulated."
        ),
        "key_points": [
            "Quantum PCP conjecture: local Hamiltonian ground-energy approximation stays QMA-hard with constant gap.",
            "NLTS theorem proven 2022 (Anshu-Breuckmann-Nirkhe) - a major stepping stone.",
            "Classical gap amplification (Dinur) has no quantum analogue - the central wall.",
            "A proof would bound what quantum many-body systems can ever be simulated.",
            "Connects complexity theory directly to condensed matter physics.",
        ],
        "requirements": [
            "A proof needs QMA-hardness of approximation with a constant promise gap.",
            "NLTS is necessary but far from sufficient.",
            "Any quantum gap amplification technique would be a breakthrough on its own.",
        ],
        "standards": [
            "Aharonov D et al. The detectability lemma and quantum gap amplification. STOC; 2009.",
            "Anshu A, Breuckmann N, Nirkhe C. NLTS Hamiltonians from good quantum codes. STOC; 2023.",
            "Dinur I. The PCP theorem by gap amplification. JACM; 2007.",
        ],
        "citations": [
            "The conjecture was formulated by Aharonov, Arad, Landau, Vazirani (circa 2013).",
            "The 2022 NLTS proof resolved a decade-old stepping-stone conjecture.",
        ],
        "solution": (
            "Step 1 - assumption: the missing ingredient is a quantum gap "
            "amplification procedure - the classical proof's engine - and it will "
            "be found by studying how entanglement survives the amplification "
            "steps that work classically. Step 2 - reasoning path: take Dinur's "
            "classical gap amplification apart into its components (expander "
            "replacement, alphabet reduction, powering) and test each against "
            "quantum Hamiltonians at small scales, identifying exactly where "
            "entanglement breaks the classical argument. Step 3 - proposed "
            "mechanism: a 'quantum amplification workbench' that prototypes "
            "candidate quantum amplification steps on small Hamiltonians, "
            "measuring gap growth versus entanglement degradation. What would "
            "confirm it: a workbench step that amplifies the gap while preserving "
            "the NLTS property - the core of a quantum PCP proof. What would kill "
            "it: a no-go theorem showing entanglement fundamentally blocks gap "
            "amplification, suggesting the conjecture may be false. What it does "
            "NOT claim: that the conjecture is true - the workbench is equally "
            "an instrument for finding counterexamples."
        ),
        "ladder_rank": 17, "ladder_tier": "compounded",
    },
    {
        "key": "circuit-lower-bounds",
        "name": "Superpolynomial Circuit Lower Bounds for NP",
        "group": "Complexity Theory",
        "description": (
            "Can an explicit NP problem - say, SAT - be shown to need "
            "superpolynomial-size boolean circuits? Shannon proved in 1949 that "
            "most boolean functions need exponential circuits, but 'most' means a "
            "random function, and exhibiting one concrete hard function has "
            "defeated seventy years of effort. The best lower bound for an "
            "explicit NP function is barely superlinear, around 3n gates. The "
            "Natural Proofs barrier of Razborov and Rudich (1997) explains why: "
            "most lower-bound techniques would break standard cryptography, so "
            "they cannot work if one-way functions exist."
        ),
        "sig_lens": (
            "The Signature lens reads circuit lower bounds as cartography of the "
            "hard: drawing the first reliable maps of which explicit problems "
            "truly resist small circuits. The Signature approach hunts "
            "non-natural properties - techniques the Natural Proofs barrier "
            "cannot touch - by studying what makes the known hard candidates "
            "structurally special."
        ),
        "how_it_works": (
            "Boolean circuits are the most concrete model of computation: gates "
            "wired together, size measured in gates. Proving that SAT needs large "
            "circuits would separate P from NP in the nonuniform setting - a huge "
            "result. The history is a catalog of barriers: after Shannon's "
            "counting argument, the first explicit lower bounds (for restricted "
            "models like monotone circuits, Razborov 1985) were followed by the "
            "devastating Natural Proofs paper, which showed that any 'natural' "
            "proof of a strong lower bound yields a break of pseudorandom "
            "generators. Since then the frontier has barely moved: the best "
            "explicit bounds hover near 3n gates, and even formula lower bounds "
            "(a weaker model) top out around n^3. Recent work on 'non-natural' "
            "techniques - Williams' algorithmic method connecting SAT algorithms "
            "to lower bounds - offers the most promising path. Why it matters: a "
            "superpolynomial lower bound for any NP problem would be the first "
            "unconditional hardness result of its kind and a giant step toward P "
            "vs NP."
        ),
        "key_points": [
            "Shannon (1949): most functions need exponential circuits - but non-explicitly.",
            "Best explicit lower bound for NP functions: barely superlinear (~3n gates).",
            "Natural Proofs (1997): most techniques would break cryptography, so they cannot work.",
            "Monotone and restricted-model bounds exist but do not touch general circuits.",
            "Williams' algorithmic method is the most promising non-natural path.",
        ],
        "requirements": [
            "A bound must apply to an explicit NP problem against general circuits.",
            "The technique must be non-naturalizing to evade Razborov-Rudich.",
            "Restricted-model bounds are progress but do not imply general bounds.",
        ],
        "standards": [
            "Shannon C. The synthesis of two-terminal switching circuits. BSTJ; 1949.",
            "Razborov A, Rudich S. Natural proofs. JCSS; 1997.",
            "Williams R. Improving exhaustive search implies superpolynomial lower bounds. STOC; 2010.",
        ],
        "citations": [
            "Razborov (1985) proved exponential monotone circuit lower bounds for clique.",
            "The Natural Proofs barrier has stood since 1997.",
        ],
        "solution": (
            "Step 1 - assumption: the way past Natural Proofs is the algorithmic "
            "method - faster algorithms for a problem imply lower bounds against "
            "circuits trying to solve it - so the attack runs through algorithms, "
            "not combinatorics. Step 2 - reasoning path: pick the NP problem with "
            "the fastest known exponential algorithm, then push that algorithm's "
            "analysis to its limit; every improvement in the algorithm's exponent "
            "mechanically strengthens the implied circuit lower bound via "
            "Williams' connection. Step 3 - proposed mechanism: an 'algorithm-to-"
            "bound' pipeline that takes SAT-solving and circuit-analysis "
            "algorithms, extracts their exact exponential savings, and converts "
            "the savings into the strongest implied lower bound - automating the "
            "Williams program. What would confirm it: the implied bounds climbing "
            "from linear toward polynomial as algorithms improve. What would kill "
            "it: the conversion hitting a ceiling where better algorithms stop "
            "implying better bounds - a new barrier. What it does NOT claim: a "
            "superpolynomial bound today - the pipeline industrializes the most "
            "promising known path, nothing more."
        ),
        "ladder_rank": 18, "ladder_tier": "compounded",
    },
    {
        "key": "vp-vs-vnp",
        "name": "Algebraic P vs NP: VP vs VNP",
        "group": "Complexity Theory",
        "description": (
            "Leslie Valiant's algebraic world (1979) replays P vs NP with "
            "polynomials instead of decision problems: VP is the class of "
            "polynomial families with small arithmetic circuits, VNP the class "
            "with small 'existential' circuits. The permanent of a matrix is "
            "VNP-complete; the determinant is in VP. Is the permanent really "
            "harder - does VP differ from VNP? The best known lower bound says "
            "expressing the n-by-n permanent as a determinant needs size at "
            "least n^2/2 (Mignon-Ressayre 2004) - quadratic, where exponential "
            "is conjectured."
        ),
        "sig_lens": (
            "The Signature lens sees VP vs VNP as P vs NP stripped to its "
            "algebraic skeleton: no bits, no machines, just polynomials and "
            "circuits. The Signature approach studies the permanent-determinant "
            "gap as a problem in geometry - orbit closures and representation "
            "theory - following the geometric complexity theory program."
        ),
        "how_it_works": (
            "Valiant's theory is cleaner than boolean complexity in one crucial "
            "way: the permanent and determinant are single, beautiful polynomials, "
            "not arbitrary languages. The determinant has small circuits (Gaussian "
            "elimination); the permanent is VNP-complete, capturing the hardness "
            "of counting. Valiant conjectured that the permanent needs "
            "superpolynomial arithmetic circuits. Geometric complexity theory "
            "(Mulmuley and Sohoni, 2001+), the most ambitious attack, reframes the "
            "question as algebraic geometry: the determinant's orbit closure "
            "versus the permanent's, with representation-theoretic obstructions as "
            "the separating witnesses. It is a grand program - and stalled: the "
            "obstructions sought turned out not to exist in the hoped-for form "
            "(Ikenmeyer, Mulmuley, Walter 2017 showed natural obstructions "
            "vanish). Lower bounds for restricted arithmetic models (bounded "
            "depth, multilinear) have progressed, but general VP vs VNP stands. "
            "Why it matters: it is the most structured form of the P vs NP "
            "question, and its resolution would validate or refute the geometric "
            "approach to all of complexity."
        ),
        "key_points": [
            "Valiant (1979): permanent is VNP-complete; determinant is in VP.",
            "Conjecture: VP != VNP - the permanent needs superpolynomial arithmetic circuits.",
            "Best lower bound: determinantal complexity at least n^2/2 (2004).",
            "Geometric complexity theory reframes it as algebraic geometry; key obstructions shown to vanish (2017).",
            "Restricted models (bounded depth) have seen real lower-bound progress.",
        ],
        "requirements": [
            "Separation needs superpolynomial arithmetic circuit lower bounds for the permanent.",
            "GCT needs representation-theoretic obstructions separating the orbit closures.",
            "Restricted-model bounds do not imply the general separation.",
        ],
        "standards": [
            "Valiant L. Completeness classes in algebra. STOC; 1979.",
            "Mulmuley K, Sohoni M. Geometric complexity theory I. SIAM J. Comput.; 2001.",
            "Mignon T, Ressayre N. A quadratic bound for the determinant. IMRN; 2004.",
        ],
        "citations": [
            "Ikenmeyer, Mulmuley, Walter (2017) showed the hoped-for GCT obstructions vanish.",
            "Valiant's 1979 papers founded algebraic complexity theory.",
        ],
        "solution": (
            "Step 1 - assumption: the permanent-determinant gap is real but the "
            "current geometric weapons misfire - so the path forward is a finer "
            "geometric invariant than the vanishing obstructions, or a hybrid "
            "with the successful bounded-depth techniques. Step 2 - reasoning "
            "path: compute the exact representation-theoretic data (Kronecker "
            "coefficients, plethysm multiplicities) for small n where the "
            "permanent and determinant can be compared directly, and hunt for "
            "the pattern that distinguishes them - letting small-n computation "
            "suggest the invariant. Step 3 - proposed mechanism: a computational "
            "GCT laboratory that tabulates the orbit-closure data for n up to "
            "the feasible limit and searches for separating multiplicities "
            "algorithmically. What would confirm it: a candidate obstruction "
            "family whose non-vanishing is provable in general. What would kill "
            "it: the data showing no separating pattern at any feasible n - "
            "suggesting the geometric approach needs entirely new ideas. What it "
            "does NOT claim: that VP differs from VNP, or that GCT will succeed - "
            "the laboratory generates candidates; proofs remain human work."
        ),
        "ladder_rank": 19, "ladder_tier": "compounded",
    },
    {
        "key": "mcsp",
        "name": "The Minimum Circuit Size Problem",
        "group": "Complexity Theory",
        "description": (
            "Given the truth table of a boolean function, what is the smallest "
            "circuit computing it? The Minimum Circuit Size Problem (MCSP) is "
            "almost embarrassingly natural - yet its complexity is unknown. Is "
            "MCSP NP-complete? Nobody knows. Kabanets and Cai (2000) showed that "
            "if MCSP is easy, then strong pseudorandom generators do not exist; "
            "it is also connected to learning theory, proof complexity, and "
            "cryptography. A problem this basic, this central, and this "
            "mysterious is rare."
        ),
        "sig_lens": (
            "The Signature lens sees MCSP as the complexity of complexity "
            "itself: the problem of measuring hardness is hard. The Signature "
            "approach treats MCSP's unknown status as a diagnostic - whichever "
            "way it resolves, it takes a piece of the hardness-vs-randomness "
            "worldview with it."
        ),
        "how_it_works": (
            "MCSP takes a 2^n-bit truth table and asks for the minimum circuit "
            "size - a question Levin studied in the 1970s under the name Kt "
            "complexity. It is in NP (guess the circuit, verify against the "
            "table), and it feels like it should be NP-complete, but every "
            "attempted reduction hits the wall that MCSP's input is exponentially "
            "long relative to n. The stakes were raised when researchers "
            "discovered MCSP's tentacles: easiness of MCSP kills cryptographic "
            "pseudorandom generators (Kabanets-Cai 2000), collapses learning "
            "theory assumptions, and would give natural proofs against strong "
            "circuit lower bounds. Recent work (2020s) has mapped MCSP's "
            "relationships to isomorphism problems, one-way functions, and "
            "meta-complexity - the complexity of complexity problems - making it "
            "the flagship of the emerging meta-complexity program. Why it "
            "matters: settling MCSP would simultaneously advance cryptography, "
            "learning theory, and lower bounds - it is the rare problem whose "
            "resolution pays out in every direction."
        ),
        "key_points": [
            "MCSP: minimum circuit size for a given truth table; in NP, not known NP-complete.",
            "If MCSP is easy, strong pseudorandom generators do not exist.",
            "Connected to learning, proof complexity, and one-way functions.",
            "Flagship problem of the emerging meta-complexity program.",
            "Reductions are blocked by the exponentially long input.",
        ],
        "requirements": [
            "NP-completeness needs a polynomial reduction from SAT despite the long input.",
            "Easiness would need a subexponential or polynomial algorithm.",
            "Conditional results map the stakes but do not settle the complexity.",
        ],
        "standards": [
            "Kabanets V, Cai J. Circuit minimization problem. STOC; 2000.",
            "Levin L. Laws of information conservation. 1974.",
            "Allender E. The complexity of complexity. CiE; 2017.",
        ],
        "citations": [
            "Kabanets and Cai (2000) linked MCSP easiness to the non-existence of PRGs.",
            "The meta-complexity program (Allender and others, 2010s-2020s) centers on MCSP.",
        ],
        "solution": (
            "Step 1 - assumption: MCSP's complexity will be settled by the "
            "meta-complexity toolkit - reductions among 'complexity of "
            "complexity' problems - rather than by a direct assault. Step 2 - "
            "reasoning path: map MCSP's exact relationships to its cousins "
            "(MKtP, Minimum Formula Size, time-bounded Kolmogorov complexity), "
            "then attempt to transfer known hardness from the cousin where it is "
            "best understood, tracking precisely which transfer steps fail and "
            "why. Step 3 - proposed mechanism: a 'meta-complexity atlas' that "
            "maintains the proven reduction web among these problems and "
            "highlights the missing edges - each missing edge is a concrete "
            "research target, and completing the web around MCSP may pin its "
            "complexity. What would confirm the approach: a missing edge getting "
            "proved, tightening the net around MCSP. What would kill it: the web "
            "stabilizing with MCSP genuinely isolated - suggesting its "
            "complexity is independent of its cousins. What it does NOT claim: "
            "that MCSP is NP-complete, or in P - the atlas organizes the hunt; "
            "the hunt itself is open."
        ),
        "ladder_rank": 20, "ladder_tier": "compounded",
    },
    {
        "key": "log-rank",
        "name": "The Log-Rank Conjecture",
        "group": "Complexity Theory",
        "description": (
            "Alice and Bob each hold half of an input and must compute a joint "
            "function while communicating as little as possible. The log-rank "
            "conjecture of Lovasz and Saks (1988) proposes a beautiful law: the "
            "deterministic communication needed is at most polynomial in the "
            "logarithm of the rank of the function's communication matrix. In "
            "other words, algebraic rank controls communication. The best known "
            "upper bound is about the square root of the rank (Lovett 2014) - "
            "polynomial in the rank, but exponentially weaker than the "
            "conjectured polylog."
        ),
        "sig_lens": (
            "The Signature lens reads the log-rank conjecture as a proposed law "
            "of nature for distributed computation: algebra dictating dialogue. "
            "The Signature approach hunts the extremal functions - the ones "
            "pushing communication far above log-rank - because they are either "
            "counterexamples or the key to the proof."
        ),
        "how_it_works": (
            "Communication complexity, founded by Yao in 1979, studies the "
            "minimum conversation needed for distributed computation - with "
            "applications from circuit lower bounds to data structures to "
            "streaming. The rank bound is one of its oldest tools: the "
            "deterministic communication complexity of f is at least log(rank) "
            "of its matrix. Lovasz and Saks conjectured the bound is nearly "
            "tight - communication is at most (log rank)^c. For thirty-five "
            "years the gap barely moved, until Lovett's 2014 breakthrough using "
            "a clever discrepancy argument brought the upper bound down to "
            "roughly sqrt(rank). The remaining gap - sqrt(rank) versus "
            "polylog(rank) - is still exponential. Candidate counterexamples "
            "have been proposed and refuted; the conjecture survives. Why it "
            "matters: it would unify the algebraic and combinatorial views of "
            "communication, and its techniques would propagate to every field "
            "that uses communication lower bounds."
        ),
        "key_points": [
            "Conjecture (1988): deterministic communication is polylog(rank).",
            "Best known: O(sqrt(rank log rank)) - exponentially weaker (Lovett 2014).",
            "Lower bound: communication is at least log(rank) - nearly tight if true.",
            "Candidate counterexamples have been proposed and refuted; it survives.",
            "Would unify algebraic and combinatorial communication complexity.",
        ],
        "requirements": [
            "A proof needs a protocol using (log rank)^O(1) bits for every boolean function.",
            "A refutation needs a function family with communication super-polylogarithmic in rank.",
            "Improvements to the sqrt(rank) bound count as real progress.",
        ],
        "standards": [
            "Lovasz L, Saks M. Lattices, Mobius functions and communication complexity. FOCS; 1988.",
            "Lovett S. Communication is bounded by root of rank. STOC; 2014.",
            "Yao A. Some complexity questions related to distributive computing. STOC; 1979.",
        ],
        "citations": [
            "Lovett (2014) broke the decades-long stagnation with the sqrt(rank) bound.",
            "The conjecture has survived all proposed counterexamples to date.",
        ],
        "solution": (
            "Step 1 - assumption: the truth lies with the extremal functions - "
            "either a counterexample family exists near the current upper bound, "
            "or the structure forcing high communication is classifiable and "
            "yields the proof. Step 2 - reasoning path: computationally search "
            "small boolean functions for large communication-to-log-rank ratios, "
            "then analyze the winners: do they generalize into counterexample "
            "families, or do they reveal a structural property (like low "
            "discrepancy on a large rectangle) that a proof could exploit? Step "
            "3 - proposed mechanism: an 'extremal function laboratory' that "
            "enumerates small functions, computes exact communication complexity "
            "and rank, and mines the extremal cases for patterns. What would "
            "confirm the conjecture's plausibility: extremal ratios flattening "
            "as n grows, with exploitable structure emerging. What would kill "
            "it: a scalable family with super-polylog ratios - a genuine "
            "counterexample. What it does NOT claim: that the conjecture is true "
            "- the laboratory is built to find counterexamples as eagerly as "
            "proof ideas."
        ),
        "ladder_rank": 21, "ladder_tier": "compounded",
    },
    {
        "key": "nl-vs-l",
        "name": "Directed Reachability in Logarithmic Space",
        "group": "Complexity Theory",
        "description": (
            "Given a directed graph and two vertices, is there a path from one to "
            "the other? This reachability problem is NL-complete - the hardest "
            "problem solvable in nondeterministic logarithmic space. Savitch's "
            "1970 theorem puts it in deterministic O(log^2 n) space. But can it be "
            "done in O(log n) - that is, does NL equal L? For undirected graphs, "
            "Reingold proved in 2004 that log space suffices. For directed graphs, "
            "the question is wide open, and it is the most prominent separation "
            "problem below P."
        ),
        "sig_lens": (
            "The Signature lens sees reachability as navigation with a tiny "
            "notebook: what can you find when you can barely remember where you "
            "have been? The Signature approach studies why undirected graphs "
            "yielded to Reingold's expander techniques and asks what directed "
            "analogue could possibly exist."
        ),
        "how_it_works": (
            "Space complexity measures memory, not time. L is deterministic log "
            "space; NL adds nondeterminism - the ability to guess. Savitch showed "
            "NL sits inside DSPACE(log^2 n) via a clever recursive middle-first "
            "search, and Immerman-Szelepcsenyi (1987) showed NL is closed under "
            "complement - nondeterministic log space can even count. Reingold's "
            "2004 breakthrough for undirected connectivity used expander graphs "
            "and the zig-zag product to deterministically explore with O(log n) "
            "bits: a tour de force that won the Godel Prize. Directed graphs "
            "resist because edges have no return path - the explorer cannot back "
            "up, and the expander machinery breaks. The problem is also "
            "equivalent to asking whether nondeterminism helps at all for log-"
            "space computation. Why it matters: NL vs L is the cleanest question "
            "about the power of nondeterminism, and its resolution would reshape "
            "space complexity the way P vs NP would reshape time complexity."
        ),
        "key_points": [
            "Directed reachability is NL-complete; Savitch gives O(log^2 n) deterministic space.",
            "Reingold (2004): undirected reachability is in L - Godel Prize work.",
            "Immerman-Szelepcsenyi (1987): NL is closed under complement.",
            "Directed edges break the expander techniques; no log-space algorithm known.",
            "The flagship separation problem below P.",
        ],
        "requirements": [
            "Equality needs a deterministic O(log n)-space directed reachability algorithm.",
            "Separation needs a proof that no such algorithm exists - beyond current techniques.",
            "Improvements between log^2 n and log n would be progress.",
        ],
        "standards": [
            "Savitch W. Relationships between nondeterministic and deterministic tape complexities. JCSS; 1970.",
            "Reingold O. Undirected connectivity in log-space. JACM; 2008.",
            "Immerman N. Nondeterministic space is closed under complementation. SIAM J. Comput.; 1988.",
        ],
        "citations": [
            "Reingold's 2004 STOC paper (journal 2008) settled the undirected case.",
            "Szelepcsenyi (1987) independently proved NL = coNL.",
        ],
        "solution": (
            "Step 1 - assumption: the directed case fails exactly where "
            "Reingold's proof uses undirectivity - the ability to traverse edges "
            "backward - so the hunt is for a directed pseudorandom object that "
            "substitutes for expanders. Step 2 - reasoning path: formalize "
            "which properties of the zig-zag product the directed setting "
            "needs, then search for directed graph products with those "
            "properties, testing candidates computationally on small digraphs "
            "for the required expansion behavior. Step 3 - proposed mechanism: "
            "a 'directed derandomization workbench' that proposes and tests "
            "directed analogues of Reingold's components, measuring how close "
            "each comes to enabling log-space traversal. What would confirm "
            "the approach: a directed product with the right spectral-expansion "
            "trade-off, opening the path to NL = L. What would kill it: a proof "
            "that no such directed object exists - which would itself suggest "
            "NL differs from L. What it does NOT claim: that NL equals L - the "
            "workbench tests the constructive path, and its failure would be "
            "evidence for separation."
        ),
        "ladder_rank": 22, "ladder_tier": "compounded",
    },
    {
        "key": "planted-clique",
        "name": "Planted Clique and Average-Case Hardness",
        "group": "Cryptography",
        "description": (
            "Hide a clique of size k inside a random graph, then try to find it. "
            "When k is much larger than sqrt(n), spectral methods recover it "
            "easily (Alon, Krivelevich, Sudakov 1998); when k is much smaller, "
            "no known polynomial algorithm succeeds. The planted clique "
            "conjecture asserts this gap is real: finding cliques below sqrt(n) "
            "is hard on average. It has become a central hardness assumption, "
            "underpinning cryptography, statistical lower bounds, and fine-"
            "grained complexity - yet it is entirely unproven."
        ),
        "sig_lens": (
            "The Signature lens treats planted clique as the canonical hidden "
            "signal: when does a whisper drown in noise? The Signature approach "
            "maps the exact computational threshold empirically, because the "
            "conjecture's power comes from a threshold nobody can prove."
        ),
        "how_it_works": (
            "Average-case hardness is cryptography's lifeblood: cryptosystems need "
            "problems hard on random instances, not just in the worst case. "
            "Planted clique, introduced by Jerrum (1992), is the cleanest such "
            "candidate: the distributional problem is simple to state, the "
            "spectral threshold at sqrt(n) is sharp and well understood, and "
            "below it every known algorithm - spectral, SDP hierarchies, "
            "MCMC - fails. It now anchors hardness for sparse PCA, community "
            "detection, and even public-key cryptography proposals. But it is a "
            "conjecture, and history warns: similar 'hard on average' beliefs "
            "have collapsed before. Sum-of-Squares lower bounds (Barak et al.) "
            "show that powerful algorithmic frameworks cannot beat the threshold, "
            "which is the best evidence available - evidence about algorithms, "
            "not about the problem. Why it matters: a refutation would break a "
            "web of cryptographic and statistical assumptions; a proof would be "
            "the first natural average-case hardness result of its kind."
        ),
        "key_points": [
            "Planted k-clique in G(n,1/2): easy above sqrt(n), conjectured hard below.",
            "Spectral recovery works at Omega(sqrt(n)) (Alon-Krivelevich-Sudakov 1998).",
            "Sum-of-Squares lower bounds: strong algorithms cannot beat the threshold.",
            "Anchors crypto proposals, sparse PCA hardness, community detection limits.",
            "Entirely unproven; a conjecture carrying a field's weight.",
        ],
        "requirements": [
            "A proof needs average-case hardness below sqrt(n) against all polynomial algorithms.",
            "A refutation needs one polynomial algorithm succeeding below the threshold.",
            "SoS lower bounds rule out algorithm families, not all algorithms.",
        ],
        "standards": [
            "Jerrum M. Large cliques elude the Metropolis process. RSA; 1992.",
            "Alon N, Krivelevich M, Sudakov B. Finding a large hidden clique. RSA; 1998.",
            "Barak B et al. Sum-of-squares lower bounds for planted clique. STOC; 2016.",
        ],
        "citations": [
            "The sqrt(n) spectral threshold has stood since 1998.",
            "Hopkins et al. and others extended SoS lower bounds through the 2010s.",
        ],
        "solution": (
            "Step 1 - assumption: the threshold is a genuine phase transition in "
            "the problem's computational geometry, and mapping it precisely - "
            "across algorithms, not just theory - is the fastest route to "
            "understanding it. Step 2 - reasoning path: benchmark every known "
            "algorithm family (spectral, SDP, message passing, local search, "
            "neural heuristics) on planted clique across the threshold at "
            "multiple scales, producing the first complete empirical phase "
            "diagram of the problem. Step 3 - proposed mechanism: a 'threshold "
            "observatory' that continuously tests new algorithmic ideas against "
            "the conjecture, so any refutation attempt gets immediate rigorous "
            "evaluation - and any persistent failure deepens confidence "
            "honestly. What would confirm the conjecture's standing: the phase "
            "diagram staying sharp as algorithms improve. What would kill it: "
            "any algorithm succeeding below sqrt(n) on the observatory's "
            "benchmarks. What it does NOT claim: that the conjecture is true - "
            "the observatory is a refutation engine first, and its failure to "
            "refute is only evidence, never proof."
        ),
        "ladder_rank": 23, "ladder_tier": "compounded",
    },
    # ------------------------------------------------------------ ADVANCED
    {
        "key": "frege-lower-bounds",
        "name": "Frege Proof System Lower Bounds",
        "group": "Complexity Theory",
        "description": (
            "A Frege system is the textbook notion of propositional proof: "
            "finitely many axiom schemes and rules, like high-school logic "
            "formalized. Does every tautology have a short Frege proof? This is "
            "the central open problem of proof complexity, open since Cook and "
            "Reckhow founded the field in 1979. Superpolynomial lower bounds are "
            "known for weak systems (resolution, bounded-depth Frege), but for "
            "full Frege - let alone extended Frege, which allows abbreviations - "
            "no nontrivial lower bound exists. A separation would ripple outward "
            "to NP vs co-NP."
        ),
        "sig_lens": (
            "The Signature lens sees Frege lower bounds as the question of "
            "whether some truths are irreducibly long: is there a tautology "
            "whose shortest proof cannot be compressed? The Signature approach "
            "climbs from the known weak-system bounds upward, asking what "
            "exactly breaks when proofs gain full power."
        ),
        "how_it_works": (
            "Proof complexity studies the lengths of proofs in propositional "
            "systems. The motivation is concrete: SAT solvers are proof-search "
            "engines, and lower bounds explain why they struggle. Haken's 1985 "
            "exponential lower bound for resolution proofs of the pigeonhole "
            "principle was the first landmark; Ajtai (1988) extended lower "
            "bounds to bounded-depth Frege. Then progress stopped. Full Frege "
            "systems can use arbitrary formulas, and the techniques that worked "
            "below - bottleneck counting, switching lemmas - collapse against "
            "them. The frontier question is whether Frege can simulate extended "
            "Frege (which adds extension axioms as abbreviations): a separation "
            "would be a breakthrough, and even the simulation question has stood "
            "since the 1980s. Krajicek's program connects Frege lower bounds to "
            "circuit lower bounds via feasible interpolation. Why it matters: "
            "Frege is the gold standard of propositional reasoning - lower "
            "bounds would prove that some mathematical truths have no short "
            "justification in the most natural proof system we have."
        ),
        "key_points": [
            "Central open problem of proof complexity since 1979.",
            "Exponential bounds known for resolution (Haken 1985) and bounded-depth Frege (Ajtai 1988).",
            "No nontrivial lower bounds for full Frege or extended Frege.",
            "Frege vs extended Frege simulation question open since the 1980s.",
            "Would imply separations reaching toward NP vs co-NP.",
        ],
        "requirements": [
            "A lower bound needs a tautology family requiring superpolynomial Frege proofs.",
            "Weak-system bounds do not transfer to full Frege.",
            "The simulation question needs either a simulation or a separating family.",
        ],
        "standards": [
            "Cook S, Reckhow R. The relative efficiency of propositional proof systems. JSL; 1979.",
            "Haken A. The intractability of resolution. TCS; 1985.",
            "Ajtai M. The complexity of the pigeonhole principle. Combinatorica; 1988.",
        ],
        "citations": [
            "Krajicek (1995) systematized the field and its connections to bounded arithmetic.",
            "No Frege lower bound has been found in 45+ years of effort.",
        ],
        "solution": (
            "Step 1 - assumption: the barrier is methodological - the bottleneck "
            "and switching-lemma techniques that conquered weak systems need a "
            "successor idea for full Frege, and that idea will first appear as a "
            "separation between close proof systems. Step 2 - reasoning path: "
            "attack the Frege vs extended Frege question first, since it is the "
            "weakest open separation: search for tautology families where "
            "abbreviations (extension axioms) seem essential, and try to prove "
            "they are essential via a refined bottleneck argument that tracks "
            "formula reuse. Step 3 - proposed mechanism: a 'proof-shape analyzer' "
            "that takes candidate tautologies and computes how their shortest "
            "known Frege proofs use subformula sharing - flagging families where "
            "sharing is load-bearing as candidates for extended-Frege "
            "separation. What would confirm it: a family where sharing is "
            "provably necessary - the first Frege lower bound. What would kill "
            "it: Frege efficiently simulating the sharing in all tested "
            "families, suggesting simulation holds. What it does NOT claim: any "
            "lower bound today - the analyzer produces candidates; the "
            "mathematics must still be done."
        ),
        "ladder_rank": 24, "ladder_tier": "advanced",
    },
    {
        "key": "ph-infinite",
        "name": "Is the Polynomial Hierarchy Infinite?",
        "group": "Complexity Theory",
        "description": (
            "The polynomial hierarchy stacks quantifiers: NP is 'exists a short "
            "proof', co-NP is 'for all', Sigma-2 is 'exists-forall', and so on "
            "upward. Stockmeyer defined it in 1976. Does the hierarchy go on "
            "forever, with each level strictly harder than the last - or does it "
            "collapse, with some finite level containing everything above it? A "
            "collapse at any level would drag the whole infinite tower down to "
            "that level. Almost everyone believes the hierarchy is infinite, but "
            "separating even the second level from the first is far beyond "
            "current techniques."
        ),
        "sig_lens": (
            "The Signature lens sees the polynomial hierarchy as the tower of "
            "alternating doubt: exists, for-all, exists-forall, climbing toward "
            "the sky. The Signature approach asks what a collapse would look "
            "like from below - which concrete problems would suddenly become "
            "easy - and hunts those consequences."
        ),
        "how_it_works": (
            "The hierarchy organizes problems by quantifier alternation: "
            "Sigma-k allows k alternating quantifiers starting with exists. "
            "PH, the union of all levels, sits between NP and PSPACE. The "
            "foundational collapse theorem says: if Sigma-k equals Pi-k for any "
            "k, the entire hierarchy collapses to that level. Karp and Lipton "
            "(1980) showed NP in P/poly would collapse PH; Toda (1991) showed PH "
            "is contained in P^#P. Oracle results cut both ways: there are "
            "oracles where PH is infinite and oracles where it collapses, so "
            "any proof must be non-relativizing. The hierarchy's infinitude is "
            "one of complexity theory's most believed and least provable "
            "statements - even separating Sigma-2 from NP is open. Why it "
            "matters: the hierarchy is the scaffolding of complexity theory; "
            "its infinitude would certify that quantifier alternation buys real "
            "power, level after level, without end."
        ),
        "key_points": [
            "PH stacks alternating quantifiers; Stockmeyer (1976).",
            "Collapse at any level collapses everything above it.",
            "Karp-Lipton: NP in P/poly collapses PH; Toda: PH in P^#P.",
            "Oracles exist both ways - any proof must be non-relativizing.",
            "Even Sigma-2 vs NP separation is open.",
        ],
        "requirements": [
            "Infinitude needs a strict separation at some level - beyond current methods.",
            "Collapse needs an equality at some level - equally hard.",
            "Oracle results constrain proof techniques but settle nothing.",
        ],
        "standards": [
            "Stockmeyer L. The polynomial-time hierarchy. TCS; 1976.",
            "Karp R, Lipton R. Some connections between nonuniform and uniform complexity. STOC; 1980.",
            "Toda S. PP is as hard as the polynomial-time hierarchy. SIAM J. Comput.; 1991.",
        ],
        "citations": [
            "Meyer and Stockmeyer developed the alternating-Turing-machine view.",
            "Yao, Hastad, and others built the oracle landscape around PH.",
        ],
        "solution": (
            "Step 1 - assumption: a collapse, if it happened, would have "
            "visible consequences at low levels - specific Sigma-2 problems "
            "dropping into NP - so the search for collapse can be made concrete "
            "and computational. Step 2 - reasoning path: enumerate natural "
            "Sigma-2-complete problems (like succinct versions of NP problems, "
            "or 'does a small circuit exist that...'), then attack each with "
            "the best NP machinery (SAT solvers, QBF solvers); a Sigma-2 "
            "problem that keeps yielding to NP techniques is a collapse "
            "candidate worth theoretical attention. Step 3 - proposed mechanism: "
            "a 'collapse watch' that tracks the gap between Sigma-2-complete "
            "problems and the reach of practical solvers, flagging anomalies. "
            "What would confirm infinitude's plausibility: the gap holding "
            "firm across all tested problems and solver generations. What would "
            "kill the complacency: a Sigma-2-complete problem falling to an NP "
            "algorithm - the first crack in the tower. What it does NOT claim: "
            "that PH is infinite - the watch measures the gap; the theorem is "
            "still missing."
        ),
        "ladder_rank": 25, "ladder_tier": "advanced",
    },
    {
        "key": "berman-hartmanis",
        "name": "The Berman-Hartmanis Isomorphism Conjecture",
        "group": "Complexity Theory",
        "description": (
            "Are all NP-complete problems secretly the same problem in disguise? "
            "The Berman-Hartmanis conjecture (1977) says yes: any two NP-complete "
            "sets are polynomial-time isomorphic - there is an efficiently "
            "computable bijection between them. It would mean NP-completeness is "
            "a single phenomenon wearing different masks. Mahaney's 1982 theorem "
            "showed that sparse NP-complete sets cannot exist unless P = NP, "
            "removing the most obvious counterexamples. Agrawal and others (2001) "
            "proved all known NP-complete sets are indeed isomorphic. But the "
            "general conjecture stands open."
        ),
        "sig_lens": (
            "The Signature lens loves the conjecture's audacity: thousands of "
            "hard problems, one underlying shape. The Signature approach builds "
            "explicit isomorphisms between NP-complete problems as far as the "
            "machinery reaches, mapping exactly where the constructions break."
        ),
        "how_it_works": (
            "NP-complete problems look wildly different: SAT is about formulas, "
            "Hamiltonian path about graphs, subset-sum about numbers. The "
            "isomorphism conjecture claims these differences are cosmetic - that "
            "efficient bijections translate instances back and forth. The "
            "evidence is striking: every 'natural' NP-complete problem ever "
            "examined turned out to be paddable and hence isomorphic to SAT "
            "(Berman-Hartmanis 1977; Agrawal et al. 2001 extended this to all "
            "known cases). The threats: Joseph and Young (1985) constructed "
            "weird NP-complete sets that are not isomorphic under plausible "
            "assumptions, and one-way functions would yield non-isomorphic "
            "NP-complete sets - so the conjecture's fate is tied to "
            "cryptography. If one-way functions exist, the conjecture is false "
            "in a technical sense; yet all natural problems still look "
            "isomorphic. Why it matters: it asks whether NP-completeness is one "
            "thing or many - the deepest structural question about the "
            "phenomenon Cook discovered."
        ),
        "key_points": [
            "Conjecture (1977): all NP-complete sets are polynomial-time isomorphic.",
            "All known natural NP-complete problems are isomorphic (Agrawal et al. 2001).",
            "Mahaney (1982): no sparse NP-complete sets unless P = NP.",
            "One-way functions would yield non-isomorphic NP-complete sets.",
            "The conjecture's fate is entangled with cryptography.",
        ],
        "requirements": [
            "A proof needs a general construction of isomorphisms for all NP-complete sets.",
            "A refutation needs two NP-complete sets provably non-isomorphic.",
            "Natural-problem evidence supports but does not prove the general claim.",
        ],
        "standards": [
            "Berman L, Hartmanis J. On isomorphisms and density of NP and coNP sets. SIAM J. Comput.; 1977.",
            "Mahaney S. Sparse complete sets for NP. JCSS; 1982.",
            "Agrawal M et al. Reducing the complexity of reductions. Comput. Complexity; 2001.",
        ],
        "citations": [
            "Joseph and Young (1985) built candidate non-isomorphic NP-complete sets.",
            "The paddability framework is the main positive evidence.",
        ],
        "solution": (
            "Step 1 - assumption: the isomorphism question is really about "
            "paddability - the structural property that makes the known "
            "isomorphisms work - so the frontier is characterizing exactly "
            "which NP-complete sets are paddable. Step 2 - reasoning path: "
            "construct explicit polynomial isomorphisms between pairs of "
            "NP-complete problems beyond the textbook cases (timetabling, "
            "protein folding models, verification instances), and catalog "
            "where the paddability constructions strain - the strain points "
            "mark where counterexamples might hide. Step 3 - proposed "
            "mechanism: an 'isomorphism workbench' holding a library of "
            "NP-complete problems with explicit inter-reductions, attempting "
            "to upgrade reductions to isomorphisms automatically and reporting "
            "the obstruction when it fails. What would confirm the "
            "conjecture's spirit: the workbench succeeding on every natural "
            "problem tried, with obstructions only on artificial ones. What "
            "would kill it: a natural problem where the obstruction is "
            "provable - a genuine non-isomorphic pair. What it does NOT claim: "
            "that the conjecture is true - it is entangled with one-way "
            "functions, and the workbench maps the entanglement."
        ),
        "ladder_rank": 26, "ladder_tier": "advanced",
    },
    {
        "key": "impagliazzo-worlds",
        "name": "Public-Key Crypto from One-Way Functions?",
        "group": "Cryptography",
        "description": (
            "One-way functions give us digital signatures and pseudorandomness - "
            "the world Impagliazzo called 'Minicrypt'. But public-key encryption, "
            "the heart of 'Cryptomania', seems to need more. Can public-key "
            "cryptography be built from one-way functions alone? Impagliazzo and "
            "Rudich (1989) proved a black-box separation: no black-box "
            "construction works. But non-black-box constructions are not ruled "
            "out, and the question - which of Impagliazzo's five worlds we "
            "inhabit - remains one of cryptography's deepest."
        ),
        "sig_lens": (
            "The Signature lens frames the five worlds as five possible "
            "universes, exactly one of which is ours. The Signature approach "
            "treats the black-box separation as a wall with a door: "
            "non-black-box techniques are the door, and the hunt is for a "
            "construction that walks through it."
        ),
        "how_it_works": (
            "Impagliazzo's 1995 essay 'A Personal View of Average-Case "
            "Complexity' sketched five worlds: Algorithmica (P = NP, no "
            "crypto), Heuristica (NP hard worst-case but easy on average), "
            "Pessiland (hard on average but no one-way functions - the worst "
            "world), Minicrypt (one-way functions exist, but no public-key "
            "crypto), and Cryptomania (public-key crypto exists). We know we "
            "are not in Algorithmica (probably) and hope not Pessiland. The "
            "Minicrypt vs Cryptomania question is whether the jump from "
            "private-key to public-key primitives needs new hardness. "
            "Impagliazzo-Rudich showed black-box constructions cannot make the "
            "jump - any proof must use the code of the one-way function in a "
            "non-black-box way. Recent breakthroughs (like the 2020s work on "
            "obfuscation and key exchange from new assumptions) keep the "
            "question alive. Why it matters: it decides whether the internet's "
            "public-key infrastructure rests on strictly stronger assumptions "
            "than signatures - and whether a cleverer theory could unify them."
        ),
        "key_points": [
            "Impagliazzo's five worlds (1995): which one is ours is unknown.",
            "Minicrypt has one-way functions; Cryptomania has public-key crypto.",
            "Impagliazzo-Rudich (1989): no black-box construction of PKE from OWFs.",
            "Non-black-box constructions are not ruled out.",
            "The question is cryptography's deepest structural unknown.",
        ],
        "requirements": [
            "A positive answer needs a non-black-box PKE construction from any OWF.",
            "A negative answer needs a stronger separation than black-box.",
            "New assumptions (obfuscation, etc.) shift the landscape but do not settle it.",
        ],
        "standards": [
            "Impagliazzo R. A personal view of average-case complexity. SCT; 1995.",
            "Impagliazzo R, Rudich S. Limits on the provable consequences of one-way permutations. STOC; 1989.",
        ],
        "citations": [
            "The five-worlds taxonomy comes from Impagliazzo's 1995 essay.",
            "Black-box separations are surveyed in Reingold-Trevisan-Vadhan (2004).",
        ],
        "solution": (
            "Step 1 - assumption: if a construction exists, it must exploit the "
            "structure of the one-way function non-black-box - so the search "
            "space is structured OWF families paired with code-exploiting "
            "constructions. Step 2 - reasoning path: take concrete structured "
            "one-way function candidates (lattice-based, code-based) and "
            "attempt to build key-exchange protocols that use the function's "
            "algebraic description essentially - not as an oracle - testing "
            "each attempt against known attack frameworks. Step 3 - proposed "
            "mechanism: a 'non-black-box construction laboratory' that pairs "
            "structured OWF families with construction templates, automatically "
            "checking security reductions and flagging where they break. What "
            "would confirm the hope: a template whose reduction goes through "
            "for a natural OWF family - a Minicrypt-to-Cryptomania bridge. What "
            "would kill it: the breakages revealing a pattern - a generalized "
            "separation extending Impagliazzo-Rudich beyond black-box. What it "
            "does NOT claim: that public-key crypto follows from one-way "
            "functions - the laboratory is where the question gets worked, not "
            "answered."
        ),
        "ladder_rank": 27, "ladder_tier": "advanced",
    },
    {
        "key": "indistinguishability-obfuscation",
        "name": "Obfuscation from Standard Assumptions",
        "group": "Cryptography",
        "description": (
            "Can you scramble a program so it still runs but reveals nothing "
            "about how it works? Barak and others (2001) proved the strongest "
            "form - virtual black-box obfuscation - is impossible. But "
            "indistinguishability obfuscation (iO), which only requires that "
            "obfuscations of equivalent programs look alike, survived. Garg and "
            "others gave the first candidate in 2013; Jain, Lin, and Sahai "
            "(2020) built iO from well-founded assumptions. Yet iO from truly "
            "standard assumptions - plain LWE, say - remains open, and iO would "
            "imply nearly all of cryptography."
        ),
        "sig_lens": (
            "The Signature lens sees obfuscation as the alchemy of code: turning "
            "programs into black boxes without losing their souls. The Signature "
            "approach tracks the assumption ladder rung by rung, because each "
            "rung weakened is a step toward cryptography's philosopher's stone."
        ),
        "how_it_works": (
            "Program obfuscation is cryptography's holy grail: an obfuscated "
            "program that anyone can run but nobody can reverse-engineer. The "
            "2001 impossibility result killed virtual black-box obfuscation, "
            "but Barak et al. also proposed indistinguishability obfuscation as "
            "the achievable fallback - and it turned out to be astonishingly "
            "powerful: iO implies public-key encryption, functional encryption, "
            "deniable encryption, and more (Sahai-Waters 2014 showed iO is a "
            "'crypto-complete' primitive). The first candidate (GGH+13) relied "
            "on new multilinear map assumptions, several of which were later "
            "broken; the Jain-Lin-Sahai 2020 construction rests on better-"
            "studied assumptions but still not standard ones. The security "
            "foundations remain turbulent: attacks keep breaking candidate "
            "multilinear maps, while the constructions keep retreating to safer "
            "ground. Why it matters: iO from standard assumptions would unify "
            "cryptography under essentially one assumption and enable software "
            "that is provably inscrutable."
        ),
        "key_points": [
            "Virtual black-box obfuscation is impossible (Barak et al. 2001).",
            "iO survived and implies nearly all of cryptography (Sahai-Waters 2014).",
            "First candidate 2013 (GGH+13); Jain-Lin-Sahai 2020 from better assumptions.",
            "iO from truly standard assumptions (plain LWE) remains open.",
            "Candidate multilinear maps keep breaking under cryptanalysis.",
        ],
        "requirements": [
            "A result needs iO secure under a standard, well-studied assumption.",
            "Constructions must survive the ongoing cryptanalysis of their building blocks.",
            "Efficiency matters: current candidates are astronomically impractical.",
        ],
        "standards": [
            "Barak B et al. On the (im)possibility of obfuscating programs. CRYPTO; 2001.",
            "Garg S et al. Candidate indistinguishability obfuscation. FOCS; 2013.",
            "Jain A, Lin H, Sahai A. Indistinguishability obfuscation from well-founded assumptions. STOC; 2021.",
        ],
        "citations": [
            "Sahai and Waters (2014) showed iO implies a vast range of primitives.",
            "Multilinear-map cryptanalysis (Cheon et al., Coron et al.) broke early assumptions.",
        ],
        "solution": (
            "Step 1 - assumption: the assumption ladder is climbable - each "
            "generation of iO has used weaker assumptions than the last, so the "
            "trajectory points toward standard ones. Step 2 - reasoning path: "
            "dissect the Jain-Lin-Sahai construction to isolate exactly which "
            "non-standard assumption carries the load, then target that "
            "assumption specifically: either base it on LWE via new lattice "
            "techniques, or find a construction sidestepping it. Step 3 - "
            "proposed mechanism: an 'assumption ledger' for iO that tracks "
            "every candidate construction's assumption set, the cryptanalytic "
            "status of each assumption, and the known implications between "
            "them - directing effort at the weakest live link. What would "
            "confirm the trajectory: a construction from LWE plus one mild "
            "extra assumption, then the extra assumption falling. What would "
            "kill the optimism: the load-bearing assumptions proving "
            "irreducible - iO inherently needs something exotic. What it does "
            "NOT claim: iO from standard assumptions today - the ledger "
            "organizes a long campaign, honestly reporting setbacks."
        ),
        "ladder_rank": 28, "ladder_tier": "advanced",
    },
    {
        "key": "ai-alignment",
        "name": "AI Alignment: Guaranteeing Safe Superintelligence",
        "group": "AI and Alignment",
        "description": (
            "How do we ensure that AI systems far smarter than us pursue the "
            "goals we actually want? The alignment problem asks for methods to "
            "specify, train, and verify objectives so that capable systems "
            "remain safe and beneficial. Outer alignment (getting the objective "
            "right) and inner alignment (getting the learned model to pursue "
            "it) are both unsolved. Techniques like reinforcement learning from "
            "human feedback help in practice but offer no guarantees, and "
            "scalable oversight - supervising systems smarter than their "
            "supervisors - is an open research frontier."
        ),
        "sig_lens": (
            "The Signature lens treats alignment as the steering problem for "
            "minds we build but cannot fully inspect: how do you aim something "
            "smarter than the aimer? The Signature approach decomposes "
            "guarantees into checkable pieces - specification, training, "
            "verification - and asks what each piece can provably deliver."
        ),
        "how_it_works": (
            "The alignment problem was articulated for the modern era by "
            "Bostrom (2014) and developed by Russell, Christiano, Hubinger, and "
            "many others. The core difficulty is Goodhart's law on steroids: "
            "optimizing a proxy objective produces systems that exploit the "
            "proxy - reward hacking - and smarter systems hack better. "
            "Inner alignment adds a deeper worry: mesa-optimizers, learned "
            "sub-agents with their own goals, arising inside training. Current "
            "practice leans on RLHF and constitutional AI, which empirically "
            "reduce misbehavior but cannot certify safety. Scalable oversight "
            "research (debate, recursive reward modeling, weak-to-strong "
            "generalization) tries to extend human supervision beyond human "
            "capability. Interpretability and formal verification are proposed "
            "as complementary paths. Why it matters: if transformative AI "
            "arrives, alignment is the difference between a tool and a "
            "catastrophe - it is the safety engineering of the most powerful "
            "technology ever built, and it is unsolved."
        ),
        "key_points": [
            "Outer alignment: specifying the right objective; inner alignment: the model pursuing it.",
            "Reward hacking: optimizers exploit proxy objectives; smarter systems hack better.",
            "RLHF and constitutional AI help empirically but give no guarantees.",
            "Scalable oversight - supervising superhuman systems - is an open frontier.",
            "Mesa-optimizers: learned sub-agents with their own goals, a deep unsolved worry.",
        ],
        "requirements": [
            "A solution needs methods that scale beyond human supervision capability.",
            "Empirical improvements are progress but not guarantees.",
            "Any proposal must address both outer and inner alignment.",
        ],
        "standards": [
            "Bostrom N. Superintelligence. Oxford University Press; 2014.",
            "Christiano P, Leike J et al. Deep reinforcement learning from human preferences. NeurIPS; 2017.",
            "Hubinger E et al. Risks from learned optimization in advanced ML systems. 2019.",
        ],
        "citations": [
            "Russell (2019, Human Compatible) framed assistance games as an alignment approach.",
            "Weak-to-strong generalization (Burns et al. 2023) opened a new empirical front.",
        ],
        "solution": (
            "Step 1 - assumption: guarantees will come from decomposition, not "
            "from a single breakthrough - specification, training, and "
            "verification each contributing checkable pieces. Step 2 - reasoning "
            "path: build a 'guarantee ledger' that takes each alignment "
            "proposal and scores it on the three pieces separately: what does "
            "it provably ensure about the objective, about the training "
            "dynamics, about the deployed behavior - making the gaps explicit "
            "instead of hidden. Step 3 - proposed mechanism: adversarial "
            "specification testing - systematically generating environments "
            "where a given trained model's behavior diverges from its stated "
            "objective, turning 'does it generalize safely?' into a measured "
            "quantity rather than a hope. What would confirm progress: the "
            "ledger's gaps shrinking as techniques compose - oversight plus "
            "interpretability plus verification covering each other's holes. "
            "What would kill the optimism: mesa-optimizers proving "
            "undetectable in principle, capping what any ledger can certify. "
            "What it does NOT claim: that alignment is solvable, or on what "
            "timeline - this is safety engineering instrumentation, not a "
            "safety proof."
        ),
        "ladder_rank": 29, "ladder_tier": "advanced",
    },
    {
        "key": "mechanistic-interpretability",
        "name": "Mechanistic Interpretability of Frontier Models",
        "group": "AI and Alignment",
        "description": (
            "Can we open a frontier neural network and give a complete causal "
            "account of how it computes - every feature, every circuit, every "
            "behavior? Mechanistic interpretability aims to reverse-engineer "
            "models the way biologists map cells. Progress includes the circuits "
            "program (Olah et al.), the discovery of superposition - networks "
            "representing more features than they have neurons (Elhage et al. "
            "2022) - and sparse autoencoders that extract interpretable "
            "features. But a full account of any frontier model remains far "
            "away, and it is unknown whether one is even possible."
        ),
        "sig_lens": (
            "The Signature lens treats interpretability as cartography of "
            "alien minds: we built the territory but never mapped it. The "
            "Signature approach measures understanding itself - what fraction "
            "of a model's behavior can current tools explain - so progress "
            "becomes a number, not a feeling."
        ),
        "how_it_works": (
            "Neural networks are famously opaque: billions of parameters whose "
            "collective behavior resists inspection. The mechanistic program, "
            "pioneered at Anthropic and elsewhere, seeks human-understandable "
            "algorithms inside the weights - induction heads, curve detectors, "
            "modular arithmetic circuits. Superposition was a watershed: "
            "networks compress many sparse features into few neurons, which "
            "explains both their power and their illegibility. Sparse "
            "autoencoders (2023-2024) learn dictionaries of interpretable "
            "features, scaling the approach toward frontier models - but "
            "coverage is partial, features are fuzzy, and completeness (have "
            "we found everything?) is unmeasurable with current tools. "
            "Competing views hold that some models may be irreducibly complex, "
            "or that behavioral testing suffices. Why it matters: "
            "interpretability is the microscope for AI safety - without it, "
            "alignment is flying blind; with it, we could audit, debug, and "
            "certify models the way engineers certify bridges."
        ),
        "key_points": [
            "Goal: a complete causal account of a frontier model's computations.",
            "Superposition (2022): more features than neurons - power and illegibility together.",
            "Sparse autoencoders extract interpretable features but with partial coverage.",
            "Circuits program reverse-engineered real model components (induction heads etc.).",
            "Completeness is unmeasurable; full accounts remain far away.",
        ],
        "requirements": [
            "A full account must explain behavior causally, not just correlate.",
            "Coverage must be measured: what fraction of computation is explained?",
            "Methods must scale to frontier models, not just toy networks.",
        ],
        "standards": [
            "Olah C et al. Zoom in: an introduction to circuits. Distill; 2020.",
            "Elhage N et al. Toy models of superposition. 2022.",
            "Bricken T et al. Towards monosemanticity: decomposing language models with dictionary learning. 2023.",
        ],
        "citations": [
            "The circuits thread (Olah et al. 2020+) founded the mechanistic program.",
            "Anthropic's 2023-2024 SAE work scaled feature extraction toward frontier models.",
        ],
        "solution": (
            "Step 1 - assumption: understanding is measurable - the fraction of "
            "a model's behavior causally explained by identified features and "
            "circuits can be quantified, turning interpretability into an "
            "optimization target. Step 2 - reasoning path: define coverage "
            "metrics (behavior explained under ablation, feature completeness "
            "on probes), then run a systematic campaign applying every "
            "interpretability tool to a fixed open model, publishing the "
            "coverage number and which behaviors remain dark. Step 3 - proposed "
            "mechanism: an 'interpretability scoreboard' - a public benchmark "
            "where methods compete on explained-behavior fraction, driving the "
            "field toward completeness the way ImageNet drove vision. What "
            "would confirm the program: coverage climbing steadily toward "
            "100% as methods compose. What would kill it: coverage plateauing "
            "far below complete despite best efforts - evidence of irreducible "
            "complexity. What it does NOT claim: that full interpretability is "
            "possible - the scoreboard measures the climb honestly, plateaus "
            "included."
        ),
        "ladder_rank": 30, "ladder_tier": "advanced",
    },
    {
        "key": "program-synthesis",
        "name": "Automatic Optimal Program Synthesis",
        "group": "Algorithms",
        "description": (
            "Given a specification, can a machine write the best possible program "
            "automatically - correct and optimal? Program synthesis dreams of "
            "turning programming into stating what you want. Modern systems "
            "(DreamCoder, large language models writing code) synthesize programs "
            "from examples or descriptions, but with no correctness guarantees "
            "and no optimality. The grand open problem: a synthesizer that takes "
            "a formal specification and returns a provably correct, provably "
            "optimal program - for arbitrary specifications, this brushes against "
            "undecidability itself."
        ),
        "sig_lens": (
            "The Signature lens sees synthesis as the compiler's final form: "
            "from telling machines how, to telling them what, to telling them "
            "what is best. The Signature approach climbs the guarantee ladder - "
            "examples, then specs, then proofs, then optimality - certifying "
            "each rung before reaching for the next."
        ),
        "how_it_works": (
            "Automatic programming is among computing's oldest dreams, from the "
            "1950s through Manna and Waldinger's deductive synthesis. The modern "
            "era splits three ways: syntax-guided synthesis (SyGuS) searches "
            "program spaces against logical specs with real guarantees but "
            "limited scale; inductive synthesis (FlashFill, DreamCoder) learns "
            "from examples with no guarantees; and LLM code generation writes "
            "plausible code at scale with neither guarantees nor optimality. "
            "The fundamental tension: full correctness against arbitrary specs "
            "is undecidable in general (it contains the halting problem), so "
            "any complete synthesizer must restrict its domain or its "
            "guarantees. Superoptimization (Massalin 1987; Stoke) finds optimal "
            "short instruction sequences by search - optimal synthesis in "
            "miniature. Why it matters: guaranteed-optimal synthesis would end "
            "the era of hand-tuned performance code and buggy implementations "
            "alike - it is the convergence point of programming languages, "
            "verification, and AI."
        ),
        "key_points": [
            "Dream: specification in, provably correct and optimal program out.",
            "SyGuS gives guarantees at limited scale; LLMs give scale with no guarantees.",
            "Full synthesis against arbitrary specs hits undecidability.",
            "Superoptimization achieves optimal synthesis for tiny instruction sequences.",
            "The field climbs a guarantee ladder: examples, specs, proofs, optimality.",
        ],
        "requirements": [
            "Guarantees need restricted domains or decidable spec fragments.",
            "Optimality claims need a cost model and a proof of optimality.",
            "Scale and guarantees must be traded explicitly, not wished away.",
        ],
        "standards": [
            "Manna Z, Waldinger R. A deductive approach to program synthesis. TOPLAS; 1980.",
            "Alur R et al. Syntax-guided synthesis. FMCAD; 2013.",
            "Ellis K et al. DreamCoder. PLDI; 2021.",
        ],
        "citations": [
            "Massalin (1987) pioneered superoptimization by exhaustive search.",
            "The SyGuS competition (2014+) standardized syntax-guided synthesis benchmarks.",
        ],
        "solution": (
            "Step 1 - assumption: the guarantee ladder is climbable rung by rung "
            "- each rung (examples, specs, verified, optimal) has known "
            "techniques, and the open problem is composing them at scale. Step "
            "2 - reasoning path: pick a domain with a decidable spec logic "
            "(bit-vector programs, regular string transformations), then build "
            "a synthesizer that climbs all four rungs inside that domain: "
            "examples to spec inference, spec to verified program, verified to "
            "optimal via superoptimizing search. Step 3 - proposed mechanism: a "
            "'ladder-climbing synthesizer' whose architecture is explicitly "
            "staged by guarantee level, widening the domain one decidable "
            "fragment at a time and publishing exactly which guarantees hold "
            "where. What would confirm it: domains where all four rungs hold "
            "at practical scale, widening over time. What would kill the "
            "ambition: the rungs proving incompatible - optimality search "
            "exploding wherever verification succeeds, marking a fundamental "
            "trade-off. What it does NOT claim: general optimal synthesis - "
            "undecidability forbids it, and the ladder is honest about the "
            "boundary."
        ),
        "ladder_rank": 31, "ladder_tier": "advanced",
    },
    {
        "key": "skolem-problem",
        "name": "The Skolem Problem",
        "group": "Computability",
        "description": (
            "Given a linear recurrence sequence - like the Fibonacci numbers, "
            "but with arbitrary integer coefficients - does it ever hit zero? "
            "Thoralf Skolem posed the decidability question in the 1930s, and it "
            "remains open in general after nearly a century. Special cases are "
            "decidable, and deep results connect it to Diophantine approximation "
            "and algebraic number theory, but no algorithm is known that settles "
            "every linear recurrence. It is one of the oldest open decision "
            "problems touching computer science."
        ),
        "sig_lens": (
            "The Signature lens cherishes century-old open problems: they are "
            "the mountains that do not move. The Signature approach treats the "
            "Skolem problem as a number-theoretic decision problem and attacks "
            "through its known bridge - the zeros of recurrences mirror deep "
            "questions about exponential Diophantine equations."
        ),
        "how_it_works": (
            "A linear recurrence sequence satisfies u(n) = c(1)u(n-1) + ... + "
            "c(k)u(n-k); the Fibonacci sequence is the famous order-2 case. The "
            "Skolem problem asks for an algorithm deciding whether zero ever "
            "appears. It is easy to compute terms forever, but 'never' is not a "
            "finite observation - the difficulty is certifying absence. The "
            "problem is equivalent to deciding whether an exponential polynomial "
            "has integer zeros, linking it to Skolem-Mahler-Lech theory (zeros "
            "are eventually periodic) and to Baker's theory of linear forms in "
            "logarithms. Decidability is known for low orders and for important "
            "subclasses; the general case has resisted since the 1930s. Related "
            "problems - the positivity problem (is the sequence always "
            "nonnegative?), ultimate positivity - are equally open and "
            "interconnected. Why it matters: linear recurrences model "
            "everything from population dynamics to program loops, and the "
            "Skolem problem is the prototype of 'does this process ever hit a "
            "target state' - the reachability question at the heart of "
            "verification."
        ),
        "key_points": [
            "Open since the 1930s: no general algorithm for zero-detection in linear recurrences.",
            "'Never hits zero' is not finitely observable - absence needs proof.",
            "Equivalent to integer zeros of exponential polynomials.",
            "Decidable for low orders and subclasses; general case open.",
            "Cousins: the positivity and ultimate positivity problems, also open.",
        ],
        "requirements": [
            "A decision procedure must terminate with yes/no on every recurrence.",
            "Partial results must specify exactly which orders or subclasses they cover.",
            "Connections to Diophantine approximation must be made effective.",
        ],
        "standards": [
            "Skolem T. Ein Verfahren zur Behandlung gewisser exponentialer Gleichungen. 1934.",
            "Mahler K. Eine arithmetische Eigenschaft der Taylor-Koeffizienten. 1935.",
            "Lech C. A note on recurring series. Ark. Mat.; 1953.",
        ],
        "citations": [
            "The Skolem-Mahler-Lech theorem describes the structure of zero sets.",
            "Baker's theory of linear forms in logarithms powers the decidable cases.",
        ],
        "solution": (
            "Step 1 - assumption: the general case will yield to effective "
            "number theory - making the constants in Baker-type theorems "
            "explicit enough to bound the search for zeros. Step 2 - reasoning "
            "path: take the strongest known decidable subclass and identify "
            "the exact number-theoretic estimate it relies on, then work to "
            "effectivize the next estimate in the chain - each effectivization "
            "extends decidability to a wider class. Step 3 - proposed mechanism: "
            "a 'zero-bound calculator' that, given a recurrence, computes a "
            "certified bound N such that if no zero appears among the first N "
            "terms, none ever appears - extending the class of recurrences for "
            "which such bounds are computable. What would confirm it: the "
            "certified class widening steadily toward the general case. What "
            "would kill the hope: the bounds proving inherently non-effective "
            "- which would suggest undecidability, itself a resolution. What "
            "it does NOT claim: decidability - after ninety years, the honest "
            "position is that either answer would be historic."
        ),
        "ladder_rank": 32, "ladder_tier": "advanced",
    },
    {
        "key": "termination-proving",
        "name": "Complete Automatic Termination Proving",
        "group": "Computability",
        "description": (
            "Turing proved in 1936 that no program can decide halting for all "
            "programs. But can we build a termination prover that succeeds on "
            "every program that actually terminates - a complete practical "
            "method? Size-change termination (Lee, Jones, Ben-Amram 2001) and "
            "modern tools (AProVE, Termin) prove termination for vast classes "
            "of real programs, yet every known method is incomplete: there are "
            "always terminating programs it cannot handle. Whether a "
            "'complete in practice' termination analyzer exists - or whether "
            "incompleteness bites every attempt - is open."
        ),
        "sig_lens": (
            "The Signature lens sees termination as the halting problem's "
            "practical shadow: undecidable in theory, indispensable in "
            "practice. The Signature approach measures provers against the "
            "busy beaver frontier - the hardest terminating programs known - "
            "because a prover's reach is defined by what it cannot do."
        ),
        "how_it_works": (
            "Termination analysis proves programs stop - critical for "
            "compilers, embedded systems, and smart contracts where infinite "
            "loops cost real money. The theory: Rice's theorem and Turing's "
            "result forbid completeness in general, but 'complete for a "
            "useful class' is the practical goal. Size-change termination "
            "analyzes how data sizes evolve across calls - elegant, decidable, "
            "and incomplete. Modern provers combine ranking functions, "
            "transition invariants, and SMT solving to handle real C, Java, "
            "and Haskell programs, competing annually in TermComp. Yet "
            "adversarial examples - terminating programs encoding busy beaver "
            "champions or Collatz-like iterations - defeat every tool. The open "
            "question is the shape of the boundary: is there a natural, "
            "useful class of programs admitting a complete prover, or does "
            "every decidable class leave out programs programmers actually "
            "write? Why it matters: termination bugs are hangs, and hangs in "
            "pacemakers, spacecraft, and financial systems are catastrophes - "
            "the prover is the safety net."
        ),
        "key_points": [
            "Turing (1936): no universal halting decider exists.",
            "Size-change termination (2001): elegant, decidable, incomplete.",
            "Modern provers (AProVE etc.) handle real programs; compete in TermComp.",
            "Busy-beaver-like programs defeat every known prover.",
            "Open: the shape of the boundary between provable and unprovable termination.",
        ],
        "requirements": [
            "Completeness claims must name the program class precisely.",
            "Benchmarks must include adversarial terminating programs, not just easy ones.",
            "Undecidability forbids a universal prover; the question is about useful classes.",
        ],
        "standards": [
            "Turing A. On computable numbers. Proc. LMS; 1936.",
            "Lee C, Jones N, Ben-Amram A. The size-change principle. POPL; 2001.",
        ],
        "citations": [
            "The TermComp competition (annual) benchmarks termination provers.",
            "AProVE and Termin are the leading practical tools.",
        ],
        "solution": (
            "Step 1 - assumption: prover power is best understood through "
            "adversarial benchmarking - a prover's true reach is revealed by "
            "the hardest terminating programs it can and cannot handle. Step 2 "
            "- reasoning path: assemble a 'termination gauntlet' of programs "
            "graded by difficulty - from simple loops through Ackermann-like "
            "recursion to busy-beaver champions - and score every major prover "
            "on it, publishing exactly where each fails. Step 3 - proposed "
            "mechanism: failure-driven prover development - each gauntlet "
            "failure becomes a targeted research problem, and the gauntlet "
            "grows as provers conquer old levels, creating a ratchet toward "
            "completeness on natural programs. What would confirm the "
            "program: the gauntlet's natural-program levels falling one by "
            "one, with failures retreating to ever-more-artificial programs. "
            "What would kill the hope: failures stuck at programs programmers "
            "actually write - suggesting incompleteness bites in practice, not "
            "just in theory. What it does NOT claim: a complete prover - "
            "Turing forbids the universal version, and the gauntlet is honest "
            "about the boundary."
        ),
        "ladder_rank": 33, "ladder_tier": "advanced",
    },
    {
        "key": "physical-church-turing",
        "name": "The Physical Church-Turing Thesis and Hypercomputation",
        "group": "Computability",
        "description": (
            "The Church-Turing thesis says every effectively computable function "
            "is Turing-computable. The physical version asks: does the actual "
            "universe compute only Turing-computable functions, or does physics "
            "allow hypercomputation - machines that solve the halting problem? "
            "Relativistic proposals (Malament-Hogarth spacetimes, where one "
            "observer sees another's infinite computation in finite time) suggest "
            "hypercomputation is consistent with general relativity. Quantum "
            "mechanics, so far, does not break the Turing barrier. Whether the "
            "laws of physics permit non-Turing computation is open - and it is "
            "as much physics as computer science."
        ),
        "sig_lens": (
            "The Signature lens poses the ultimate question: is the universe "
            "itself a Turing machine, or something stranger? The Signature "
            "approach treats hypercomputation proposals as physics experiments "
            "in waiting - each one makes claims about spacetime, matter, or "
            "measurement that physics can, in principle, check."
        ),
        "how_it_works": (
            "Hypercomputation comes in flavors: accelerated Turing machines "
            "(each step twice as fast - supertasks), analog neural networks "
            "with real weights (Siegelmann and Sontag showed these can exceed "
            "Turing power with uncomputable weights), and relativistic computers "
            "exploiting Malament-Hogarth spacetimes (Hogarth 1992; Earman and "
            "Norton analyzed the physics). Every proposal faces physical "
            "objections: infinite precision, unbounded energy, or spacetime "
            "structures that may not exist. The Bekenstein bound and holographic "
            "considerations suggest fundamental limits on information in finite "
            "regions. Meanwhile, the 'physical Church-Turing thesis' - that the "
            "universe's computational power equals Turing machines - is "
            "assumed by nearly all of computer science but proven by none of "
            "it. Deutsch's version ties computation to quantum mechanics "
            "explicitly. Why it matters: it asks whether uncomputability is a "
            "law of thought or a law of nature - and the answer decides whether "
            "the halting problem is hard in principle or merely hard for us."
        ),
        "key_points": [
            "Physical Church-Turing thesis: the universe computes only Turing-computable functions - unproven.",
            "Malament-Hogarth spacetimes would allow relativistic hypercomputation (Hogarth 1992).",
            "Analog nets with real weights exceed Turing power (Siegelmann-Sontag) - given uncomputable reals.",
            "Every proposal faces physical objections: precision, energy, spacetime structure.",
            "The question is as much physics as computer science.",
        ],
        "requirements": [
            "A hypercomputer needs a physically realizable proposal, not just a mathematical one.",
            "Objections from physics (Bekenstein bound etc.) must be answered, not ignored.",
            "The thesis itself needs a precise physical formulation before it can be tested.",
        ],
        "standards": [
            "Hogarth M. Does general relativity allow an observer to view an eternity in a finite time? FoP; 1992.",
            "Siegelmann H, Sontag E. Analog computation via neural networks. TCS; 1994.",
            "Deutsch D. Quantum theory, the Church-Turing principle. Proc. Roy. Soc.; 1985.",
        ],
        "citations": [
            "Earman and Norton analyzed the physical plausibility of Malament-Hogarth computation.",
            "Piccinini surveys the physical Church-Turing thesis debate.",
        ],
        "solution": (
            "Step 1 - assumption: hypercomputation proposals live or die on "
            "their physics - so the way forward is to convert each proposal "
            "into falsifiable physical claims. Step 2 - reasoning path: take "
            "the leading proposals (relativistic, analog, quantum-adiabatic "
            "variants) and extract their load-bearing physical assumptions - "
            "the existence of certain spacetimes, infinite measurement "
            "precision, unbounded but finite resources - then check each "
            "against current physics: which assumptions are already ruled out, "
            "which are testable, which are metaphysical. Step 3 - proposed "
            "mechanism: a 'hypercomputation audit' - a living document scoring "
            "each proposal on physical realizability, updated as physics "
            "advances, so the field always knows which doors are still open. "
            "What would confirm the thesis: every proposal's assumptions "
            "falling to physics, one by one. What would kill it: one proposal "
            "surviving all physical objections - a blueprint for a real "
            "hypercomputer. What it does NOT claim: that hypercomputation is "
            "possible, or impossible - the audit follows the physics wherever "
            "it leads."
        ),
        "ladder_rank": 34, "ladder_tier": "advanced",
    },
]
