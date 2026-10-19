#!/usr/bin/env python3
"""Entries for the Human Likeness DNA databases (Manon's 2026-10-17 16:15 order).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases) PLUS
every shard index title in jah-databases-data-1 (785 index files, 1,132,237
index lines): zero 'human-likeness*' slugs/names; zero title collisions for
all 34 record names and their 34 Signature Edition variants (dedupe pre-check
ran before authoring: 68 titles checked, 0 refusals).

So this build creates two NEW databases, 34 ladder-ordered records each:

  human-likeness-dna               - The Human Likeness DNA Database
                                     (the deterministic HLX-1 method plus
                                     synthetic illustrative sequences, each
                                     with its deterministically derived
                                     representation: the trait-parameter
                                     vector from the documented algorithm,
                                     the stylized abstract SVG visualization
                                     spec, and the step-by-step derivation.
                                     Every representation is clearly labeled
                                     a Signature-generated deterministic
                                     model - a stylized parametric
                                     abstraction, never a real person's
                                     appearance; sequences are synthetic
                                     illustrations composed for this
                                     database, never real DNA)
  human-likeness-dna-signature     - The Human Likeness DNA Signature
                                     Database
                                     (the same ladder through the Signature
                                     lens: his original Signature reading of
                                     the likeness method - the sequence as a
                                     signature, the derivation as a covenant
                                     of steps, the glyph as a seal; src
                                     signature, titles suffixed " (Signature
                                     Edition)", clearly labeled
                                     Signature-made, never presented as
                                     authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): method records (what the
method is, the deterministic pipeline, sequence basics, seeded randomness)
-> single-trait derivations (one trait derived from one synthetic sequence
at a time: height, build, skin band, hair texture, hair shade, eye color,
face width ratio, jaw angle, nose bridge, brow density, lip fullness,
freckle density) -> full-likeness derivations (complete trait vectors with
abstract glyph specs, the determinism proof, the sensitivity check, the
generator record). The shard index is written in ladder order so pages
present simple -> compounded -> complex.

ID prefixes: JAH-HLDN- (public) and JAH-HLDNS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits
across 1,132,237 index lines).

The deterministic algorithm (HLX-1), frozen 2026-10-17 and mirrored byte-
for-byte in the page generator (gen-*.js): validate the sequence (A/C/G/T
only, 16-4096 bases); FNV-1a 64-bit digest; xorshift64* seeded from the
digest; twelve trait draws in fixed order (height band of 5, build of 4,
skin band of 6, hair texture of 4, hair shade of 6, eye color of 6, face
width ratio quantized 0.72-0.92, jaw angle 100-140, nose bridge of 3, brow
density of 3, lip fullness of 3, freckle density of 4); the trait-parameter
vector serialized as compact JSON; the abstract glyph SVG spec built from
the vector with fixed formatting. Same sequence in -> byte-identical
representation out, every time, in Python and in JavaScript.

All 68 demos are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker. The generator demo verifies the same sequence
yields a byte-identical representation across runs and that different
sequences yield different representations.

Never the words "bat belt" anywhere. No website references. No Facebook.
Every representation is a Signature-generated deterministic model - a
stylized parametric abstraction, never a real person's appearance.
"""

SIG_TAIL = ("Signature original - his original Signature reading of the "
            "likeness method: the sequence as a signature, the derivation "
            "as a covenant of steps, the abstract glyph as a seal. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_FNV = ("Fowler G, Noll LC, Vo P. FNV (Fowler-Noll-Vo) non-cryptographic "
           "hash function; 64-bit FNV-1a: offset basis 14695981039346656037, "
           "prime 1099511628211.")
CIT_XORSHIFT = ("Vigna S. Further scramblings of Marsaglia's xorshift "
                "generators. arXiv:1404.0390; 2014. The xorshift64* generator "
                "used here: x ^= x >> 12; x ^= x << 25; x ^= x >> 27; "
                "return x * 2685821657736338717 (mod 2^64).")
CIT_METHOD = ("The HLX-1 deterministic pipeline as documented in 'The "
              "Deterministic Pipeline: Sequence to Representation' in this "
              "database: validate, FNV-1a 64-bit digest, seeded xorshift64*, "
              "twelve trait draws in fixed order, compact JSON vector, "
              "abstract glyph SVG spec.")
CIT_LIMITS = ("'What This Method Cannot Do: The Limits Record' in this "
              "database: every representation is a Signature-generated "
              "deterministic model - a stylized parametric abstraction, "
              "never a real person's appearance; the sequences are synthetic "
              "illustrations, never real DNA; trait bands are illustrative "
              "model bands, not biological predictions.")

SEQ_CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
SEQ_S11 = "GATCATGCTTACCCGGTCAGCAAGGTGTTCCGGGTGTGGACCGTTAGGGCGTTACTAGTTGCAATCGATCAC"
SEQ_S12 = "TCATAACTTAACGAAACAAATTGCGTGTATTGTGAATCCCCTGAAATAGTTACATGTCCTAGGTTTGTTTTC"
SEQ_S13 = "GTATGAATGGGGTTTTGACCGAATTGCTGATTTTTTGTCTCAGCTCCTGCTTTCTGGTGATGTTTACTATAT"
SEQ_S14 = "ATTGCACTTATACCTGTACTGTAGTCTGTAATGTCACAGTACTGGGCGGCGAAATACCCTTTGCTAACAAAT"
SEQ_S15 = "TGGTCGCGTGGCCTTATGGACAAATTACCGCGGACATGAGGGCCGTTTCCAACGAGAAACCACCGAACGTCT"
SEQ_S16 = "GTTTCTTTTTTATCGCCTACTTCTCACACCGGTGCCCGTGAATCGAGCTCGTCGACTTATTTCTACGACCGG"
SEQ_S17 = "GTTTCCTGGCAAGTGGTGCAAATAGAGTGTAGGTGAATGCGACACCTAGTTGCTACGACTTTAGATAAAAAG"
SEQ_S18 = "GGCACTGATTGCTTGGGCACCTATCCTAGAGACAGTGCTAATACAGGAAGTCGATCTCTAGTATAACGCCAA"
SEQ_S19 = "GAGGCTGCTAATCAACACGTACTTGAGTGACATGTCCTTCCTATCCCAATAAGAAGTCACGTCCCGCTAGAT"
SEQ_S20 = "CCATTCCCAGTTTAAGACGTGATGCCGGGATTGCGCTGAAGTGGGCGGAGGTTAGGGTGGAGAAGAGGGTCG"
SEQ_S21 = "ATACTTACAGCAGAATATTTGGAACCTGATTAGAATTTGGCTATTACAAAGTACCTGTCCCCTAGGAATCGC"
SEQ_S22 = "TCTTGCTCGACACCGTGCGCAACCTTAGTGCGGCCTATGTGCGTCTAAGCCGGCCGGGCTCTCTACTCCCAA"
SEQ_H1 = "GGAATACAGTAGCGACGCCCTAGTTGACAATCTAATCCTAGTCGTGTCTCGGCTGCGGTGCGCATGGAGAAC"
SEQ_H2 = "TCGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCTACAGGAGATTTGAATT"
SEQ_H3 = "GGCAGCCTACCCGCCGCCTGTTGCGGTAAGTCTGGATAGGGCGTAAGAGGAACCGATCCCCAGCAAATAGTC"
SEQ_H4 = "GGACAAGCGGATGAGTTATTGGGCGAGGCAAAGGAGTCGTGTTCTGCTTCGTCGAATCCTGAATGATGGTCA"
SEQ_H5 = "GGGTAAGATTACTAGATAAATCAGAAATCCTAGATCACAAATCTCGCAAATGTATAAACGCGAACGTGGAGG"
SEQ_H6 = "CCTAGGGCTCAGCCAAGTTAGCAGTTTTGAAGTTCTGGCTGCCCCGAGTATTGCCACGGATCACATGTCACC"
SEQ_H7 = "ACGGGACAGCGACGTGAGCTAGTAGGTTTATGCGATTCGGCAATGTCAGGCGAGGTGTGTAAACCCCTAAGA"
SEQ_H8 = "CTAACAAATCATCGCTTTATACAACTCTGCTGGACCGTCGACAGCCAAAGACCAACAAGAGGAATTATCCGC"

MODEL_LABEL = ("Signature-generated deterministic model - a stylized "
               "parametric abstraction. Never a real person's appearance.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What the Human Likeness Method Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The human likeness method in this database is a deterministic "
            "procedure that takes one DNA sequence at a time and derives a "
            "stylized representation of a human likeness from it. The word "
            "deterministic carries the whole meaning: the same sequence fed "
            "in always produces the byte-identical representation out, no "
            "matter how many times it runs or on which machine. The method "
            "has three outputs for every sequence: a trait-parameter vector "
            "(twelve named parameters such as height band, build, skin-tone "
            "band, hair texture, eye color, and facial-geometry parameters), "
            "a stylized abstract visualization spec (a parameterized SVG "
            "document describing an abstract glyph, geometric and "
            "non-photorealistic by design), and a step-by-step derivation "
            "showing exactly how the sequence became the representation. "
            "Every sequence used in this database is synthetic, composed for "
            "illustration, and never taken from any real person; every "
            "representation is a Signature-generated deterministic model, a "
            "stylized parametric abstraction, and never a real person's "
            "appearance. The method does not predict real traits from real "
            "DNA. It demonstrates, one sequence at a time, how a fully "
            "deterministic pipeline turns an input string into a repeatable, "
            "auditable, visualizable parameter set."
        ),
        "how_it_works": (
            "The method works by refusing to leave anything to chance. A "
            "sequence enters the pipeline and is validated: it must be a "
            "non-empty string of the letters A, C, G, and T only, between 16 "
            "and 4096 bases long. The validated sequence is digested with "
            "the FNV-1a 64-bit hash, a well-known non-cryptographic hash "
            "function, producing a single 64-bit number. That number seeds "
            "a xorshift64* pseudorandom generator, which then makes twelve "
            "draws in a fixed, documented order - height band first, "
            "freckle density last. Each draw selects one value from a small "
            "fixed list of abstract bands, or one quantized number for the "
            "two geometry parameters. The twelve values form the "
            "trait-parameter vector, serialized as compact JSON with the "
            "keys in a fixed order. The same twelve values then drive the "
            "abstract glyph: band indices choose hues, arc styles, bar "
            "heights, and dot counts inside a fixed SVG template, so the "
            "picture is as deterministic as the numbers. Because every step "
            "is a pure function of the input - no clocks, no network calls, "
            "no hidden state - the whole pipeline is reproducible by anyone, "
            "anywhere, from this record alone."
        ),
        "key_points": [
            "Deterministic means repeatable: the same sequence always yields the byte-identical representation, on any machine, any number of times.",
            "One sequence at a time: each representation is derived from exactly one input sequence, processed alone through the full pipeline.",
            "Three outputs per sequence: the trait-parameter vector (twelve named values), the abstract SVG glyph spec, and the step-by-step derivation.",
            "All sequences here are synthetic illustrations composed for this database - never real DNA from any real person.",
            "Every representation is a Signature-generated deterministic model: a stylized parametric abstraction, never a real person's appearance, and the trait bands are illustrative model bands, not biological predictions.",
        ],
        "requirements": [
            "A single DNA sequence per derivation: a non-empty string using only the letters A, C, G, T, 16 to 4096 bases long.",
            "The frozen HLX-1 algorithm exactly as documented - validation, FNV-1a digest, seeded xorshift64*, twelve draws in fixed order, fixed JSON key order, fixed SVG template.",
            "No hidden inputs: no timestamps, no network calls, no ambient state anywhere in the pipeline.",
            "Synthetic sequences only: any sequence processed must be composed for illustration, never attributed to a real person.",
            "The model label carried on every output: Signature-generated deterministic model, never a real person's appearance.",
        ],
        "standards": [
            "Sequences are validated strictly: any character outside ACGT, or any length outside 16-4096, is rejected with an error, never silently fixed.",
            "The digest is FNV-1a 64-bit with the standard offset basis and prime; the generator is xorshift64* exactly as published by Vigna.",
            "Representations are compared byte-for-byte: equality of the compact JSON string and the SVG string, not approximate similarity.",
        ],
        "citations": [CIT_FNV, CIT_XORSHIFT, CIT_METHOD, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: a sequence is a signature written in four "
            "letters, and the method is the covenant that the same signature "
            "always opens the same seal. Where statistics would guess, the "
            "Signature method swears: twelve draws, fixed order, no hidden "
            "hand, and the glyph that results is stamped as a model, never "
            "mistaken for a person."
        ),
    },
    {
        "key": "pipeline",
        "name": "The Deterministic Pipeline: Sequence to Representation",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "This record is the full deterministic algorithm, HLX-1, stated "
            "as a record so that any reader can reimplement it from scratch "
            "and get the identical results. The pipeline has six stages. "
            "Stage one, validation: the input must be a string, non-empty, "
            "16 to 4096 characters, every character one of A, C, G, T; "
            "anything else raises an error. Stage two, digest: FNV-1a "
            "64-bit over the ASCII bytes of the sequence, starting from the "
            "offset basis 14695981039346656037 and multiplying by the prime "
            "1099511628211 per byte, all arithmetic modulo 2 to the 64th. "
            "Stage three, seeding: the digest seeds xorshift64* (a zero "
            "digest is remapped to a fixed nonzero constant). Stage four, "
            "the twelve draws in fixed order: height band (5 options), "
            "build (4), skin band (6), hair texture (4), hair shade (6), "
            "eye color (6), face width ratio (21 quantized steps from 0.72 "
            "to 0.92), jaw angle (41 integer steps from 100 to 140), nose "
            "bridge (3), brow density (3), lip fullness (3), freckle density "
            "(4). Stage five, serialization: the trait-parameter vector as "
            "compact JSON, keys in the fixed order above, no whitespace. "
            "Stage six, the abstract glyph: a fixed SVG template whose hues, "
            "radii, bar heights, arc styles, dot colors, and dot counts are "
            "computed from the twelve values with fixed integer formulas. "
            "The canonical example sequence used throughout this database "
            "is the 72-base synthetic sequence ACGCGGACTCACCCGTAGCGGGCTAATT "
            "GATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC, whose FNV-1a "
            "digest is 74fef976f58549f1. Its twelve draws, in order, are: "
            "height draw 2 of 5 (average), build draw 1 of 4 (lean), skin "
            "draw 2 of 6 (band-3), texture draw 1 of 4 (wavy), shade draw 3 "
            "of 6 (shade-4), eye draw 5 of 6 (amber), face-width draw 20 of "
            "21 (0.92), jaw draw 19 of 41 (119), nose draw 2 of 3 (high), "
            "brow draw 1 of 3 (medium), lip draw 0 of 3 (thin), freckle draw "
            "3 of 4 (dense). Any correct implementation fed the canonical "
            "sequence must reproduce these draws exactly."
        ),
        "how_it_works": (
            "The pipeline works because each stage is a pure function of "
            "the previous stage's output, with every constant frozen. The "
            "validator is a gate, not a guesser: it accepts only clean "
            "ACGT strings of legal length. The FNV-1a digest turns the "
            "variable-length sequence into a fixed 64-bit fingerprint; "
            "changing even one base avalanches the digest, which is the "
            "source of the method's sensitivity. The xorshift64* generator "
            "expands that single fingerprint into an endless stream of "
            "deterministic 64-bit words; each trait draw consumes one word "
            "modulo the number of options, so the draw order is load-bearing "
            "- height always draws first, freckle density always last. The "
            "two geometry parameters are quantized with integer arithmetic "
            "(face width as 72 plus a 0-20 step over 100; jaw angle as 100 "
            "plus a 0-40 step), so no floating-point rounding can differ "
            "between implementations. The JSON serializer writes keys in "
            "the fixed trait order with compact separators, and the SVG "
            "builder formats every number as an integer, so both output "
            "strings are byte-stable. The page generator (gen-*.js) carries "
            "this same algorithm in JavaScript using BigInt for the 64-bit "
            "arithmetic, and the database's demos verify the two "
            "implementations agree."
        ),
        "key_points": [
            "Six frozen stages: validate, FNV-1a digest, seed xorshift64*, twelve draws in fixed order, compact JSON vector, abstract SVG glyph.",
            "The canonical 72-base synthetic example sequence digests to 74fef976f58549f1 and must reproduce the twelve documented draws in any correct implementation.",
            "Draw order is load-bearing: height first through freckle density last; reordering the draws would produce a different representation.",
            "Geometry parameters use integer quantization (0.72-0.92 in 21 steps; 100-140 in 41 steps) so results are identical across languages and machines.",
            "The JavaScript pipeline in gen-*.js mirrors this record exactly, using BigInt for the 64-bit hash and generator arithmetic.",
        ],
        "requirements": [
            "The exact stage order and the exact constants: FNV offset basis, FNV prime, xorshift64* shifts (12, 25, 27) and multiplier 2685821657736338717, all modulo 2^64.",
            "The exact trait order and option lists: height(5), build(4), skin(6), texture(4), shade(6), eye(6), face ratio(21 steps), jaw(41 steps), nose(3), brow(3), lip(3), freckle(4).",
            "Compact JSON with the fixed key order and no whitespace; SVG with integer-formatted numbers in the fixed template.",
            "Validation before digestion: no invalid sequence may reach the hash stage.",
            "The model label on every output: Signature-generated deterministic model, never a real person's appearance.",
        ],
        "standards": [
            "FNV-1a 64-bit and xorshift64* are implemented exactly as published; the known-answer checks (empty input digests to the offset basis) must pass.",
            "One base changed anywhere in the sequence must change the digest and therefore the representation - the sensitivity property.",
            "The canonical sequence's twelve documented draws are the acceptance test for any reimplementation.",
        ],
        "citations": [CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the pipeline is a covenant of six steps, "
            "each sworn to the last. The digest is the wax seal of the "
            "sequence; the generator is the hand that breaks it open; the "
            "twelve draws are twelve witnesses called in order; and the "
            "glyph is the seal stamped afterward - a model, labeled as a "
            "model, never mistaken for the person it does not depict."
        ),
    },
    {
        "key": "seq_basics",
        "name": "DNA Sequence Basics for This Database",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A DNA sequence, for the purposes of this database, is a string "
            "over the four-letter alphabet A, C, G, T - the standard symbols "
            "for the four nucleotide bases adenine, cytosine, guanine, and "
            "thymine. The pipeline treats the sequence purely as a string: "
            "it never interprets codons, genes, or biological meaning, and "
            "it never needs any. Lengths from 16 to 4096 bases are "
            "accepted; shorter strings are rejected because they carry too "
            "little entropy to seed the generator well, and longer strings "
            "are rejected to keep every derivation fast and auditable. Every "
            "sequence in this database is synthetic: composed by a seeded "
            "random process for illustration, carrying no biological "
            "information about any organism, and labeled as synthetic "
            "wherever it appears. The four letters may appear in any order "
            "and any proportion; the pipeline's hash sees only bytes, so a "
            "sequence of all adenines is as valid an input as a balanced "
            "mix. What matters is not what the sequence means but that it "
            "is exactly specified: the same string of letters, in the same "
            "order, is the entire contract the determinism guarantee rests "
            "on."
        ),
        "how_it_works": (
            "The sequence works in the pipeline as the sole source of "
            "entropy. Validation scans every character: anything outside "
            "A, C, G, T fails the whole input, and the length is checked "
            "against the 16-to-4096 window. The accepted string is encoded "
            "as ASCII bytes - A is byte 65, C is 67, G is 71, T is 84 - and "
            "those bytes are what the FNV-1a hash consumes. Because the "
            "hash avalanches, the tiniest change (one letter swapped, one "
            "letter moved) produces a completely different 64-bit digest, "
            "and therefore a completely different representation; this is "
            "the sensitivity property the later sensitivity record "
            "demonstrates. The database's synthetic sequences were composed "
            "with a fixed-seed random generator choosing uniformly among "
            "the four letters, 72 bases each, so they are realistic-looking "
            "strings with no hidden meaning - illustration material, "
            "frozen as literals in the records, never regenerated."
        ),
        "key_points": [
            "The alphabet is exactly four letters - A, C, G, T - and the pipeline treats the sequence as a plain string, never as biology.",
            "Accepted lengths are 16 to 4096 bases; anything shorter, longer, empty, or containing other characters is rejected with an error.",
            "Every sequence in this database is synthetic, composed for illustration with a fixed seed, and labeled synthetic wherever it appears.",
            "The hash consumes the ASCII bytes of the letters, so one changed letter avalanches the digest and changes the whole representation.",
            "Exactness is the contract: the same letters in the same order are the entire basis of the determinism guarantee.",
        ],
        "requirements": [
            "Sequences must be non-empty strings using only A, C, G, T, between 16 and 4096 bases long.",
            "All database sequences are synthetic illustrations, never attributed to any real person or organism.",
            "Sequences are frozen as literals in the records; illustrative sequences are never silently regenerated.",
            "Validation must run before any hashing: invalid input never reaches the digest stage.",
            "Any sequence shown with a representation must carry the model label: Signature-generated deterministic model, never a real person's appearance.",
        ],
        "standards": [
            "Base symbols follow the standard IUPAC single-letter codes for the four DNA nucleotides.",
            "ASCII encoding is fixed: the digest is computed over the ASCII bytes of the uppercase letters.",
            "Length bounds (16 minimum, 4096 maximum) are enforced identically in the Python demos and the JavaScript pipeline.",
        ],
        "citations": [CIT_METHOD, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: four letters are the whole alphabet of the "
            "seal, and the database writes its own sentences in them - "
            "synthetic sentences, owning no one's biology. The pipeline "
            "does not read meaning in the letters; it reads exactness, and "
            "exactness is what the covenant keeps."
        ),
    },
    {
        "key": "seeded_randomness",
        "name": "Seeded Randomness: Same Input, Same Output",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Seeded randomness is the engine that makes the pipeline "
            "deterministic. A pseudorandom generator is an algorithm that, "
            "given a starting number called a seed, produces a long stream "
            "of numbers that look random but are completely fixed: the same "
            "seed always produces the same stream, on any machine, in any "
            "language, forever. This database seeds its generator - "
            "xorshift64*, a fast, well-studied generator - with the FNV-1a "
            "64-bit digest of the input sequence. That single design choice "
            "is what turns an arbitrary string of letters into a repeatable "
            "likeness: the digest is the fingerprint of the sequence, and "
            "the generator expands that fingerprint into the twelve trait "
            "draws. Nothing else influences the stream - no clock, no mouse "
            "movements, no network - so there is nothing that can make two "
            "runs disagree. Seeded randomness is also what makes the method "
            "auditable: anyone who knows the seed (the digest, printed in "
            "every derivation) can replay the exact stream of draws and "
            "check every trait by hand. Randomness here is not uncertainty; "
            "it is uncertainty's opposite - a fixed, inspectable, "
            "replayable mapping from seed to numbers."
        ),
        "how_it_works": (
            "The generator works as a small state machine. Its state is a "
            "single 64-bit number, initialized to the sequence digest (a "
            "zero digest is remapped to a fixed nonzero constant so the "
            "generator never starts dead). Each step applies three shifts "
            "and xors - right 12, left 25, right 27 - then multiplies by "
            "the constant 2685821657736338717, all modulo 2 to the 64th, "
            "and returns the product as the next 64-bit word. A trait draw "
            "takes the next word modulo the number of options: for a "
            "five-option trait, word mod 5 selects option 0 through 4. "
            "Because the state update is a pure function of the previous "
            "state, the whole stream is fixed by the seed; resetting the "
            "generator to the same seed replays the identical words in the "
            "identical order. The JavaScript pipeline implements the same "
            "arithmetic with BigInt, which handles 64-bit integers "
            "exactly, so the Python demos and the page generator produce "
            "the identical stream from the identical digest."
        ),
        "key_points": [
            "A seeded generator turns one seed number into a fixed, replayable stream of numbers - same seed, same stream, everywhere, always.",
            "The seed is the FNV-1a digest of the sequence, so the sequence alone determines the entire stream.",
            "xorshift64* advances its 64-bit state with three shift-xor steps and a multiply, all modulo 2^64 - a published, well-studied design.",
            "Each trait draw consumes one stream word modulo the option count, in the fixed trait order, so the stream position of every draw is known.",
            "No hidden inputs feed the generator - no clocks or network - which is why two runs can never disagree.",
        ],
        "requirements": [
            "The generator must be seeded solely from the sequence digest; no other entropy source may be mixed in.",
            "The xorshift64* step must implement the exact shifts (12, 25, 27), the exact multiplier, and modulo 2^64 arithmetic.",
            "A zero seed must be remapped to the fixed nonzero constant before the first draw.",
            "Draws must consume stream words in the fixed trait order, one word per draw.",
            "The JavaScript pipeline must reproduce the identical stream using exact 64-bit integer arithmetic (BigInt).",
        ],
        "standards": [
            "xorshift64* follows Vigna's published specification exactly; any deviation changes every downstream trait.",
            "Modulo draws use the raw 64-bit word (word mod n), not a floating-point intermediate, in both implementations.",
            "The known-answer check applies: the empty string digests to the FNV offset basis, and a fixed seed replays a fixed stream.",
        ],
        "citations": [CIT_FNV, CIT_XORSHIFT, CIT_METHOD],
        "sig_lens": (
            "The Signature read: the seed is the signature's fingerprint, "
            "and the generator is the hand that never trembles - the same "
            "fingerprint, the same twelve witnesses, called in the same "
            "order, every time. Chance is invited in only to be tamed: "
            "every 'random' number is sworn in advance."
        ),
    },
    {
        "key": "reading_sequence",
        "name": "Reading a Synthetic Sequence",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "This record reads one synthetic sequence the way the pipeline "
            "does: as an exact string of letters, counted and checked, "
            "before any derivation begins. The reading sequence is the "
            "72-base synthetic illustration ACGCGGACTCACCCGTAGCGGGCTAATT "
            "GATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC - the canonical "
            "example used across this database. Read base by base, it "
            "contains 19 adenines, 14 cytosines, 21 guanines, and 18 "
            "thymines, for a total of 72 bases and a GC content of 48.6 "
            "percent. It passes validation: non-empty, all characters "
            "within ACGT, length inside the 16-to-4096 window. It is "
            "synthetic, composed for illustration, carrying no biological "
            "information about any organism. Reading a sequence this "
            "carefully is the habit the whole database depends on, because "
            "the pipeline's first promise is exactness: the derivation "
            "that follows is a derivation of this string and no other. Any "
            "transcription error - a dropped letter, a swapped pair - is a "
            "different sequence with a different digest and a different "
            "representation, as the sensitivity record shows."
        ),
        "how_it_works": (
            "Reading works by counting, not interpreting. The string is "
            "scanned left to right; each character is checked against the "
            "four-letter alphabet and tallied, and the length is recorded. "
            "The base counts (A 19, C 14, G 21, T 18) and the GC percentage "
            "(48.6) are descriptive statistics of the string - they play no "
            "role in the derivation, which hashes the raw bytes - but they "
            "are the reader's sanity check that the string in hand is the "
            "string intended. The pipeline then encodes the letters as "
            "ASCII bytes and feeds them to FNV-1a; for this canonical "
            "sequence the digest is 74fef976f58549f1, the fingerprint every "
            "later record's derivation starts from. The demonstration "
            "program for this record performs the reading - counts, GC "
            "content, validation - and asserts each number against the "
            "values stated here, proving the record's text and the code "
            "agree."
        ),
        "key_points": [
            "The canonical 72-base synthetic sequence reads A 19, C 14, G 21, T 18, with 48.6 percent GC content.",
            "Reading means counting and validating: every character checked against ACGT, the length checked against the 16-4096 window.",
            "The sequence is synthetic illustration material - it carries no biological information about any organism.",
            "Base counts are a sanity check for the reader; the derivation itself hashes the raw ASCII bytes.",
            "The canonical digest 74fef976f58549f1 is the fingerprint every later derivation in this database starts from.",
        ],
        "requirements": [
            "The sequence must be transcribed exactly: the same 72 letters in the same order, verified by count.",
            "Validation must pass before reading proceeds: ACGT-only, length 16-4096.",
            "The synthetic origin must be stated wherever the sequence is shown.",
            "The demo must assert the counted values (19/14/21/18, 48.6 percent GC) against the record text.",
            "Any representation derived from this sequence must carry the model label.",
        ],
        "standards": [
            "Base counts are exact integer tallies of the literal string; GC content is reported to one decimal place.",
            "The digest is computed over ASCII bytes of the uppercase letters, matching the pipeline record.",
            "Record text and demo output are cross-checked: the numbers stated here are the numbers the code asserts.",
        ],
        "citations": [CIT_METHOD, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: before the seal is stamped, the signature "
            "is read aloud - every letter counted, every letter sworn. The "
            "canonical sequence is the database's own handwriting sample: "
            "synthetic, exact, and read the same way by every witness."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "trait_vector",
        "name": "The Trait-Parameter Vector",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The trait-parameter vector is the pipeline's first output: an "
            "ordered set of twelve named parameters that together form the "
            "abstract likeness. The twelve parameters, always in this "
            "order, are height_band (one of compact, below-average, "
            "average, above-average, tall), build (slight, lean, sturdy, "
            "broad), skin_band (band-1 through band-6), hair_texture "
            "(straight, wavy, curly, coily), hair_shade (shade-1 through "
            "shade-6), eye_color (brown, hazel, green, blue, gray, amber), "
            "face_width_ratio (0.72 to 0.92 in 21 quantized steps), "
            "jaw_angle (100 to 140 in whole degrees), nose_bridge (low, "
            "medium, high), brow_density (light, medium, full), lip_fullness "
            "(thin, medium, full), and freckle_density (none, sparse, "
            "moderate, dense). Each band is an abstract model band, not a "
            "measurement and not a biological prediction: 'tall' names a "
            "slot in a five-slot scale, and 'band-3' names the third of six "
            "abstract swatches. For the canonical example sequence, the "
            "vector is height_band average, build lean, skin_band band-3, "
            "hair_texture wavy, hair_shade shade-4, eye_color amber, "
            "face_width_ratio 0.92, jaw_angle 119, nose_bridge high, "
            "brow_density medium, lip_fullness thin, freckle_density dense. "
            "Serialized, it is one compact JSON object with the keys in "
            "the fixed order - the exact string is part of the "
            "determinism guarantee, and any reimplementation must produce "
            "it byte-for-byte."
        ),
        "how_it_works": (
            "The vector works as the single source of truth for everything "
            "downstream. Each of the twelve values comes from one draw of "
            "the seeded generator, in the fixed order, modulo the option "
            "count - so the vector is a direct transcription of the first "
            "twelve generator words. The two numeric parameters are "
            "quantized with integer arithmetic: face width is 72 plus the "
            "draw (0-20), divided by 100, giving 0.72 through 0.92; jaw "
            "angle is 100 plus the draw (0-40), giving whole degrees 100 "
            "through 140. Integer quantization is deliberate: it keeps the "
            "values identical across Python and JavaScript, where "
            "floating-point rounding could otherwise differ. The vector is "
            "serialized with compact separators and the fixed key order, "
            "so the JSON string itself is deterministic. The abstract "
            "glyph is then built from the vector alone - the SVG stage "
            "never sees the original sequence - which means the vector is "
            "also the audit point: checking the twelve values checks the "
            "whole derivation."
        ),
        "key_points": [
            "Twelve named parameters in fixed order: five height bands, four builds, six skin bands, four hair textures, six hair shades, six eye colors, face width 0.72-0.92, jaw 100-140 degrees, three nose bridges, three brow densities, three lip fullnesses, four freckle densities.",
            "Bands are abstract model slots, not measurements and not biological predictions.",
            "The canonical sequence's vector is average/lean/band-3/wavy/shade-4/amber/0.92/119/high/medium/thin/dense.",
            "Numeric parameters use integer quantization so Python and JavaScript produce identical values.",
            "The compact JSON serialization with fixed key order is byte-deterministic and is the audit point for the whole derivation.",
        ],
        "requirements": [
            "All twelve parameters must be present, named exactly, in the fixed order, for every representation.",
            "Band values must come only from the documented option lists; numeric values only from the documented quantized ranges.",
            "Serialization must use compact JSON with the fixed key order and no whitespace.",
            "The vector must be derivable from the sequence alone through the documented draws - no outside data.",
            "Every vector shown must carry the model label: Signature-generated deterministic model, never a real person's appearance.",
        ],
        "standards": [
            "Face width ratio is (72 + draw)/100 with draw in 0-20; jaw angle is 100 + draw with draw in 0-40 - integer arithmetic only.",
            "Option lists are frozen: any addition or reordering would break byte-compatibility with this database.",
            "The canonical vector stated here is the acceptance test: any implementation must reproduce it exactly.",
        ],
        "citations": [CIT_METHOD, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: twelve witnesses, called by name, in order "
            "- each swears one band, and the vector is their sworn "
            "testimony written down. The bands are the Signature's own "
            "measuring rods: abstract, fixed, and honest about being "
            "models."
        ),
    },
    {
        "key": "abstract_svg",
        "name": "The Abstract Visualization Spec",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The abstract visualization spec is the pipeline's second "
            "output: a parameterized SVG document describing a geometric "
            "glyph derived from the trait-parameter vector. It is abstract "
            "and stylized by design - a composition of a background field, "
            "a central disc, three trait bars, hair arcs, two eye dots, and "
            "a field of freckle dots - and it is deliberately not a face, "
            "not a portrait, and not a depiction of any person. Each visual "
            "element is computed from the vector with fixed integer "
            "formulas: the background hue from the skin and height band "
            "indices, the disc radius from the face-width step, the bar "
            "heights from the jaw angle and the nose and brow indices, the "
            "number and style of hair arcs from the hair-texture index, the "
            "eye-dot color from the eye-color value, and the freckle-dot "
            "count from the freckle-density index. Because every number in "
            "the document is an integer formatted identically every time, "
            "the SVG string is byte-deterministic: the same vector always "
            "produces the same 240-by-240 document. The glyph carries a "
            "caption inside the artwork stating it is a deterministic "
            "model, not a person. It is a seal, not a portrait - a visual "
            "checksum of the vector that a human eye can compare at a "
            "glance."
        ),
        "how_it_works": (
            "The spec works as a pure function of the twelve vector "
            "values. The builder reads the trait indices (not the sequence) "
            "and fills a fixed template: background hue equals skin index "
            "times 47 plus height index times 23, modulo 360; disc radius "
            "equals 52 plus the face-width step; the three bars rise from a "
            "baseline with heights from the jaw angle and the nose and brow "
            "steps; hair arcs are drawn above the disc - one to four arcs, "
            "straight, wavy, curly, or zigzag according to the texture "
            "index; two dots take the eye color's fixed hex; freckle dots "
            "are placed on a deterministic grid, five per density step. "
            "Every coordinate is an integer, every color a fixed string, "
            "and the template text is constant, so the document is fully "
            "determined. Two runs on the same sequence produce the "
            "byte-identical file, and one changed base in the sequence "
            "changes the vector and therefore visibly changes the glyph. "
            "The demonstration program builds the glyph for the canonical "
            "sequence twice and asserts the two documents are identical, "
            "then checks the caption text is present."
        ),
        "key_points": [
            "The glyph is an abstract geometric composition - background, disc, trait bars, hair arcs, eye dots, freckle dots - deliberately not a face or portrait.",
            "Every visual element is computed from the trait vector with fixed integer formulas; the SVG stage never sees the original sequence.",
            "All coordinates are integers and all strings are fixed, so the 240-by-240 SVG document is byte-deterministic.",
            "The artwork carries an embedded caption: deterministic model, not a person.",
            "The glyph is a visual checksum of the vector - a glance-comparable seal of the derivation.",
        ],
        "requirements": [
            "The SVG must be built solely from the twelve vector values through the documented formulas - no extra inputs.",
            "The artwork must remain abstract and geometric; no photorealistic or portrait-like rendering is permitted.",
            "The caption stating the glyph is a deterministic model, not a person, must be present in every document.",
            "Number formatting must be integer-exact so the document is byte-identical across runs and implementations.",
            "Every glyph shown must carry the model label alongside it.",
        ],
        "standards": [
            "SVG 1.1 document, 240 by 240 viewBox, well-formed XML with a single root element.",
            "Hues are integer degrees modulo 360; radii, bar heights, and dot positions are integer pixels.",
            "The eye-color hex map is frozen (brown #6B4226, hazel #8A6D3B, green #4F7942, blue #3B6EA5, gray #7D7D7D, amber #B8860B).",
        ],
        "citations": [CIT_METHOD, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the glyph is the seal stamped after the "
            "twelve witnesses have sworn - geometric, abstract, and honest. "
            "A seal proves the document; it never pretends to be the "
            "person. So with the glyph: it proves the derivation, and its "
            "own caption says what it is."
        ),
    },
    {
        "key": "limits",
        "name": "What This Method Cannot Do: The Limits Record",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "This record states the method's limits plainly, because a "
            "deterministic method is only trustworthy when its boundaries "
            "are as documented as its steps. First, the method does not "
            "predict real human traits from real DNA: the trait bands are "
            "illustrative model bands produced by a hash-seeded generator, "
            "and they carry no biological information. Feeding the pipeline "
            "a real genome would produce a representation, but that "
            "representation would be a deterministic fiction - the same "
            "kind of fiction as feeding it a random string - and this "
            "database forbids presenting it otherwise. Second, no "
            "representation in this database depicts, resembles, or is "
            "derived from any real person: every sequence is synthetic, "
            "every likeness is a stylized parametric abstraction, and every "
            "output is labeled a Signature-generated deterministic model. "
            "Third, the glyph is not a portrait and must never be used as "
            "one: it is an abstract geometric seal, non-photorealistic by "
            "design. Fourth, determinism is not truth: the guarantee is "
            "that the same input yields the same output, not that the "
            "output means anything about the input beyond the documented "
            "mapping. Fifth, the method's security properties are nil: "
            "FNV-1a is not cryptographic, digests are not secrets, and "
            "representations must never be treated as identifiers. Anyone "
            "using this database agrees to these limits by reading them "
            "here first."
        ),
        "how_it_works": (
            "The limits work as guardrails built into the records and the "
            "code. Every representation record carries the model label in "
            "its text, its JSON, and its glyph caption, so the label "
            "survives copying. Every sequence in the database is synthetic "
            "and frozen as a literal, so no real DNA can drift in through "
            "regeneration. The pipeline's validation accepts only clean "
            "ACGT strings, and the documentation never describes a path "
            "from real genomes to real traits - because there is none. The "
            "demos assert the label's presence: the limits demonstration "
            "builds a representation and checks that the model label "
            "appears in the vector output, the glyph caption, and the "
            "record text. The determinism proof and the sensitivity check "
            "demonstrate exactly what the guarantee covers - repeatability "
            "and input-sensitivity - and nothing more. These limits are "
            "not footnotes; they are load-bearing parts of the method, "
            "stated here at rank 2 so every later record is read inside "
            "them."
        ),
        "key_points": [
            "The method does not predict real traits from real DNA; trait bands are illustrative model bands from a hash-seeded generator, carrying no biological information.",
            "No representation depicts or resembles any real person: all sequences are synthetic, all likenesses are stylized abstractions, all outputs carry the model label.",
            "The glyph is an abstract geometric seal, non-photorealistic by design, and must never be used or presented as a portrait.",
            "Determinism guarantees repeatability (same input, same output), not truth about the input.",
            "FNV-1a is not cryptographic: digests are fingerprints for seeding, not secrets, and representations are not identifiers.",
        ],
        "requirements": [
            "Every representation must carry the model label - Signature-generated deterministic model, never a real person's appearance - in text, JSON, and glyph caption.",
            "Only synthetic sequences may be processed and shown; real DNA must never be fed to the pipeline or presented as input.",
            "No record may claim biological prediction, identification, or resemblance to any real person.",
            "The glyph must remain abstract and geometric in every rendering.",
            "These limits must be stated before the advanced records are read - they bound the whole database.",
        ],
        "standards": [
            "The model label text is fixed and must appear verbatim in every representation output.",
            "Synthetic sequences are frozen literals; illustrative inputs are never regenerated or swapped.",
            "Demos assert the label's presence mechanically - the limit is checked by code, not just stated in prose.",
        ],
        "citations": [CIT_METHOD],
        "sig_lens": (
            "The Signature read: a covenant is only as strong as its "
            "boundaries, and this record draws them in ink. The Signature "
            "method swears what it will do - the same seal for the same "
            "signature, every time - and swears what it will never do: "
            "never pretend a model is a person, never read biology in a "
            "hash, never let a glyph pass for a portrait."
        ),
    },
    {
        "key": "hygiene",
        "name": "Sequence Hygiene and Validation",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Sequence hygiene is the discipline of accepting only clean "
            "inputs and rejecting everything else loudly. The validator "
            "enforces five rules: the input must be a string; it must not "
            "be empty; every character must be one of A, C, G, T in "
            "uppercase; its length must be at least 16 bases; and its "
            "length must be at most 4096 bases. Any violation raises an "
            "error immediately - the pipeline never trims, never "
            "case-folds, never pads, and never guesses, because silent "
            "repair would break the exactness contract that determinism "
            "rests on. Lowercase letters are rejected rather than "
            "uppercased; whitespace is rejected rather than stripped; the "
            "ambiguous base N is rejected rather than resolved. This "
            "strictness is a feature: it guarantees that the string the "
            "user sees is exactly the string that was hashed, so the "
            "derivation can always be replayed from the visible input. The "
            "length floor of 16 keeps the digest entropy healthy, and the "
            "ceiling of 4096 keeps every derivation fast enough to audit "
            "by hand. Hygiene is what makes 'one sequence at a time' a "
            "promise instead of a slogan."
        ),
        "how_it_works": (
            "The validator works as a gate with no discretion. It checks "
            "the type first, then emptiness, then scans each character "
            "against the four-letter set, then checks the length bounds - "
            "and the first failure raises a descriptive error naming the "
            "rule broken. Because validation runs before the digest stage, "
            "no invalid input can ever reach the hash; there is no path "
            "from a dirty string to a representation. The demonstration "
            "program exercises the gate adversarially: it feeds an empty "
            "string, a lowercase sequence, a sequence with an N, a "
            "whitespace-padded sequence, a 15-base sequence, and a 4097-"
            "base sequence, and asserts that each one raises the expected "
            "error - then feeds the canonical 72-base sequence and asserts "
            "it passes cleanly. The JavaScript pipeline implements the "
            "identical five rules with identical error behavior, so a "
            "sequence accepted in one implementation is accepted in the "
            "other."
        ),
        "key_points": [
            "Five strict rules: string type, non-empty, ACGT uppercase only, length 16 minimum, length 4096 maximum.",
            "Violations raise errors immediately; the pipeline never trims, case-folds, pads, or otherwise silently repairs input.",
            "Lowercase, whitespace, and ambiguous bases (N) are rejected, not normalized.",
            "Validation runs before hashing, so no invalid input can ever reach the digest stage.",
            "The 16-base floor protects digest entropy; the 4096-base ceiling keeps every derivation auditable.",
        ],
        "requirements": [
            "The validator must check type, emptiness, alphabet, and both length bounds, in that order, raising a descriptive error at the first failure.",
            "No silent repair of any kind: no trimming, no case-folding, no padding, no ambiguity resolution.",
            "The accepted string must be exactly the string hashed - what the user sees is what was digested.",
            "Both the Python demos and the JavaScript pipeline must enforce identical rules with identical behavior.",
            "The adversarial demo must cover all six rejection cases plus the canonical acceptance case.",
        ],
        "standards": [
            "Error messages name the rule broken (empty input, invalid base, too short, too long) for replayable debugging.",
            "Length bounds are inclusive: 16 and 4096 are accepted; 15 and 4097 are rejected.",
            "Validation is a pure function of the input string - no configuration, no modes, no exceptions.",
        ],
        "citations": [CIT_METHOD, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the gatekeeper swears no favorites - a "
            "dirty signature is turned away at the door, loudly, with the "
            "reason named. The covenant keeps exactness because the gate "
            "keeps dirt out; what enters clean is hashed clean, and what "
            "is hashed clean can be sworn to."
        ),
    },
    {
        "key": "verification",
        "name": "The Determinism Verification Procedure",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The determinism verification procedure is the ritual by which "
            "anyone - not just the database's authors - can confirm that "
            "the method keeps its promise. It has four steps. First, take "
            "a frozen synthetic sequence from any record and run the full "
            "pipeline on it, capturing the trait-vector JSON string and "
            "the SVG document string. Second, run the pipeline again on "
            "the same sequence in a fresh process, and compare the two "
            "outputs byte-for-byte: they must be identical, not merely "
            "similar. Third, run the JavaScript pipeline in gen-*.js on "
            "the same sequence and compare its outputs to the Python "
            "outputs: the two implementations must agree byte-for-byte, "
            "proving the algorithm is truly frozen and not an accident of "
            "one language. Fourth, change one base in the sequence and "
            "confirm the outputs differ, proving the pipeline is "
            "input-sensitive and not returning a constant. This record "
            "exists so the guarantee is checkable rather than claimed: "
            "every later derivation in the database is implicitly verified "
            "by this procedure, and the advanced determinism-proof record "
            "performs it live. Verification is the difference between "
            "'trust me' and 'check me'."
        ),
        "how_it_works": (
            "Verification works because every output of the pipeline is a "
            "string, and strings can be compared exactly. The procedure "
            "captures the compact trait-vector JSON and the full SVG "
            "document - both deterministic by construction - and applies "
            "byte equality, the strictest comparison available. Fresh "
            "processes matter: re-running inside one process could "
            "theoretically reuse cached state, so the build's demo runner "
            "executes each demo program as its own process, and the "
            "cross-language check runs Node.js separately from Python. "
            "The one-base-change step guards against the degenerate "
            "implementation that returns the same representation for every "
            "input: a correct pipeline must differ. The demonstration "
            "program for this record performs the in-process portion - "
            "three runs of the canonical sequence compared byte-for-byte, "
            "plus the one-base-change difference check - and the build "
            "harness performs the cross-process and cross-language "
            "portions, all asserting exact equality or exact difference "
            "as appropriate."
        ),
        "key_points": [
            "Four steps: run twice in fresh processes and compare bytes; cross-check Python against JavaScript; change one base and confirm difference.",
            "Byte-for-byte comparison of the JSON string and the SVG string is the strictest possible check - no similarity thresholds.",
            "Fresh processes and separate languages guard against cached state and implementation accidents.",
            "The one-base-change step proves input-sensitivity and rules out degenerate constant outputs.",
            "Verification makes the guarantee checkable ('check me') rather than claimed ('trust me').",
        ],
        "requirements": [
            "Every verification run must compare the complete output strings - full JSON and full SVG - not summaries or hashes of them.",
            "Cross-process runs must use fresh interpreter processes with no shared state.",
            "The cross-language check must compare Python demo output against the gen-*.js pipeline output for identical inputs.",
            "The sensitivity step must use a minimal edit (one base changed) and assert the outputs differ.",
            "All comparisons must be exact: equality where determinism is claimed, inequality where sensitivity is claimed.",
        ],
        "standards": [
            "Byte equality is the pass criterion for determinism; any single differing byte is a failure.",
            "The canonical sequence is the default verification input; its frozen digest anchors the check.",
            "Verification results are reported as pass/fail with the compared inputs identified, never as scores.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT],
        "sig_lens": (
            "The Signature read: the covenant invites inspection - 'check "
            "me' is sworn alongside 'trust me'. The verification ritual "
            "is the public reading of the seal: two stampings compared, "
            "two languages compared, one letter changed and the seal "
            "changed with it. A promise that can be checked is a promise "
            "kept."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "trait_height",
        "name": "Deriving the Height Band from a Sequence",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "This record derives a single trait - the height band - from a "
            "single synthetic sequence, showing the pipeline working one "
            "trait at a time. The sequence is the 72-base synthetic "
            "illustration GATCATGCTTACCCGGTCAGCAAGGTGTTCCGGGTGTGGACCGTTAG "
            "GGCGTTACTAGTTGCAATCGATCAC. Validated (ACGT only, length 72, "
            "inside the 16-4096 window), it digests under FNV-1a 64-bit to "
            "363b837dee6794ba. That digest seeds the xorshift64* generator, "
            "whose first draw - the height draw, always first in the fixed "
            "order - is 0 of 5, selecting the first of the five height "
            "bands: compact. The height band is an abstract model band, "
            "not a measurement and not a biological prediction: 'compact' "
            "names the lowest slot of the five-slot scale (compact, "
            "below-average, average, above-average, tall), a stylized "
            "parameter of the likeness model. Every later trait of this "
            "sequence is derived from the subsequent draws in order, but "
            "this record isolates the first: same sequence in, digest "
            "363b837dee6794ba, first draw 0 of 5, height band compact - "
            "every time, on every machine. This is a Signature-generated "
            "deterministic model, a stylized parametric abstraction, never "
            "a real person's appearance."
        ),
        "how_it_works": (
            "The height derivation works because the draw position is "
            "fixed. The generator, seeded with 363b837dee6794ba, produces "
            "its stream of 64-bit words; the height trait consumes the "
            "first word modulo 5. A result of 0 selects 'compact', 1 "
            "selects 'below-average', 2 'average', 3 'above-average', and 4 "
            "'tall'. Because the seed is a pure function of the sequence "
            "and the generator is a pure function of the seed, the height "
            "band is a pure function of the sequence - no other input can "
            "influence it. The demonstration program replays this exact "
            "derivation: it validates the sequence, prints the digest, "
            "replays the first generator word, computes 0 mod 5, and "
            "asserts the band equals 'compact' as stated here, then runs "
            "the whole pipeline twice and asserts the full representation "
            "is byte-identical across the two runs."
        ),
        "key_points": [
            "The height band is the first of the twelve draws: the first generator word modulo 5 selects among compact, below-average, average, above-average, tall.",
            "For the record's synthetic sequence the digest is 363b837dee6794ba and the height draw is 0 of 5, giving the band compact.",
            "Height bands are abstract model slots, not measurements and not biological predictions.",
            "The draw position is load-bearing: height always draws first, so its value depends only on the seed.",
            "The demo replays the derivation exactly and asserts the band matches this record's text.",
        ],
        "requirements": [
            "The sequence must be validated before digestion: ACGT only, 16-4096 bases.",
            "The digest must be FNV-1a 64-bit of the ASCII bytes, printed in lowercase hex.",
            "The height draw must be the first generator word modulo 5, mapped to the frozen five-band list in order.",
            "The demo must assert the derived band equals the value stated in this record.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The five height bands are frozen in order: compact, below-average, average, above-average, tall.",
            "Digest hex is 16 lowercase characters, zero-padded.",
            "Record text and demo output are cross-checked: the digest, draw, and band stated here are the values the code asserts.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the first witness called is stature, and "
            "for this synthetic signature the witness swears 'compact' - "
            "the lowest rung of the Signature's own five-rung ladder. The "
            "band is a model slot, sworn and labeled, never mistaken for "
            "a measurement of any living person."
        ),
    },
    {
        "key": "trait_build",
        "name": "Deriving the Build Band from a Sequence",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "This record derives the build band - the second trait in the "
            "fixed order - from a single synthetic sequence. The sequence "
            "is the 72-base synthetic illustration TCATAACTTAACGAAACAAATT "
            "GCGTGTATTGTGAATCCCCTGAAATAGTTACATGTCCTAGGTTTGTTTTC. Validated "
            "and digested, it yields the FNV-1a fingerprint "
            "aa10da6c11084d7d, which seeds the generator. The build trait "
            "consumes the second generator word (the height trait takes "
            "the first): the draw is 0 of 4, selecting the first of the "
            "four build bands - slight - from the frozen list (slight, "
            "lean, sturdy, broad). The build band is an abstract model "
            "band, a stylized fullness parameter of the likeness, not a "
            "body measurement and not a biological prediction. Same "
            "sequence in, digest aa10da6c11084d7d, second draw 0 of 4, "
            "build slight - every time. This is a Signature-generated "
            "deterministic model, a stylized parametric abstraction, never "
            "a real person's appearance."
        ),
        "how_it_works": (
            "The build derivation works by stream position. After the "
            "height draw consumes the first generator word, the second "
            "word belongs to build: word modulo 4 selects the band. A "
            "result of 0 selects 'slight', 1 'lean', 2 'sturdy', 3 "
            "'broad'. The position is what makes single-trait derivation "
            "honest: the build value cannot be computed without first "
            "advancing past the height draw, which is why the pipeline "
            "always runs the draws in order even when only one trait is "
            "being studied. The demonstration program replays the two "
            "draws, prints the digest and both words' residues, asserts "
            "the build band equals 'slight' as stated here, and verifies "
            "the full twelve-trait representation is byte-identical across "
            "two runs."
        ),
        "key_points": [
            "The build band is the second draw: the second generator word modulo 4 selects among slight, lean, sturdy, broad.",
            "For this record's sequence the digest is aa10da6c11084d7d and the build draw is 0 of 4, giving the band slight.",
            "Build bands are abstract fullness slots of the model, not body measurements.",
            "Draws must run in order: the build value is only correct after the height draw has advanced the stream.",
            "The demo asserts the band matches this record and checks full-representation determinism.",
        ],
        "requirements": [
            "The height draw must be consumed first so the build draw reads the correct stream word.",
            "The build draw must be the stream word modulo 4, mapped to the frozen four-band list in order.",
            "The digest aa10da6c11084d7d must be reproduced exactly by any reimplementation.",
            "The demo must assert the band equals 'slight' as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The four build bands are frozen in order: slight, lean, sturdy, broad.",
            "Stream words are consumed strictly in trait order; skipping or reordering draws is a pipeline violation.",
            "Record text and demo output are cross-checked on digest, draw, and band.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the second witness is build, and for this "
            "signature the witness swears 'slight' - the first of four "
            "frames in the Signature's own gallery. Called in order, sworn "
            "in order, labeled as a model: that is the covenant."
        ),
    },
    {
        "key": "trait_skin",
        "name": "Deriving the Skin-Tone Band from a Sequence",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "This record derives the skin-tone band - the third trait - "
            "from a single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration GTATGAATGGGGTTTTGACCGAATTGCTGATTTTTTG "
            "TCTCAGCTCCTGCTTTCTGGTGATGTTTACTATAT. Its FNV-1a digest is "
            "064e602defd1feeb. The skin trait consumes the third generator "
            "word: the draw is 2 of 6, selecting band-3 from the six "
            "abstract swatches band-1 through band-6. Skin bands are "
            "abstract swatch indices, not colorimetry and not predictions "
            "about any real person's skin: band-3 is simply the third slot "
            "of six, used by the glyph stage to pick a background hue. "
            "Same sequence in, digest 064e602defd1feeb, third draw 2 of 6, "
            "skin band-3 - every time. This is a Signature-generated "
            "deterministic model, a stylized parametric abstraction, never "
            "a real person's appearance."
        ),
        "how_it_works": (
            "The skin derivation works by advancing the generator past the "
            "height and build draws, then taking the third word modulo 6. "
            "The result selects band-1 through band-6 in order. The "
            "abstractness is deliberate: the pipeline never claims these "
            "slots correspond to real skin tones - they are six positions "
            "on a model dial, and the glyph stage maps the index to a hue "
            "by a fixed formula (skin index times 47 plus height index "
            "times 23, modulo 360). The demonstration program replays the "
            "three draws, prints each residue, asserts the skin band "
            "equals 'band-3' as stated here, and confirms the full "
            "representation is byte-identical across two runs."
        ),
        "key_points": [
            "The skin band is the third draw: the third generator word modulo 6 selects band-1 through band-6.",
            "For this record's sequence the digest is 064e602defd1feeb and the skin draw is 2 of 6, giving band-3.",
            "Skin bands are abstract swatch indices - not colorimetry, not predictions about any real person.",
            "The glyph stage maps the band index to a background hue by a fixed integer formula.",
            "The demo asserts the band matches this record and checks full-representation determinism.",
        ],
        "requirements": [
            "The height and build draws must be consumed first so the skin draw reads the correct stream word.",
            "The skin draw must be the stream word modulo 6, reported as band-1 through band-6.",
            "The band must be presented as an abstract model slot, never as a real skin tone.",
            "The demo must assert the band equals 'band-3' as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The six skin bands are labeled band-1 through band-6, in order, with no gaps.",
            "The hue formula (skin index * 47 + height index * 23 mod 360) is frozen.",
            "Record text and demo output are cross-checked on digest, draw, and band.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the third witness names a swatch, not a "
            "skin - band-3, the middle of six abstract panels. The "
            "Signature's palette is its own invention, and the record "
            "says so plainly: a model dial, labeled, never a claim about "
            "any living person."
        ),
    },
    {
        "key": "trait_hair_texture",
        "name": "Deriving Hair Texture from a Sequence",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "This record derives hair texture - the fourth trait - from a "
            "single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration ATTGCACTTATACCTGTACTGTAGTCTGTAATGTCAC "
            "AGTACTGGGCGGCGAAATACCCTTTGCTAACAAAT. Its FNV-1a digest is "
            "b4a2003bd79d1455. The texture trait consumes the fourth "
            "generator word: the draw is 3 of 4, selecting 'coily' from "
            "the frozen list (straight, wavy, curly, coily). Hair texture "
            "here is a stylization parameter: it chooses how the glyph's "
            "hair arcs are drawn - straight lines, single waves, double "
            "waves, or zigzags - one to four arcs above the central disc. "
            "It is not a prediction about anyone's hair. Same sequence in, "
            "digest b4a2003bd79d1455, fourth draw 3 of 4, texture coily - "
            "every time. This is a Signature-generated deterministic "
            "model, a stylized parametric abstraction, never a real "
            "person's appearance."
        ),
        "how_it_works": (
            "The texture derivation advances the generator past the first "
            "three draws and takes the fourth word modulo 4. The result "
            "indexes the frozen texture list: 0 straight, 1 wavy, 2 "
            "curly, 3 coily. The glyph stage uses both the index and the "
            "label: the index plus one sets the arc count, and the label "
            "selects the path style - straight segments for straight, a "
            "quadratic wave for wavy, a double wave for curly, a zigzag "
            "for coily. The demonstration program replays the four draws, "
            "asserts the texture equals 'coily' as stated here, builds "
            "the glyph's arc paths, and asserts the zigzag style appears "
            "with four arcs, then confirms byte-identical representations "
            "across two runs."
        ),
        "key_points": [
            "Hair texture is the fourth draw: the fourth generator word modulo 4 selects straight, wavy, curly, or coily.",
            "For this record's sequence the digest is b4a2003bd79d1455 and the texture draw is 3 of 4, giving coily.",
            "Texture is a stylization parameter driving the glyph's arc count and path style, not a prediction about hair.",
            "Coily renders as four zigzag arcs above the disc; each texture has its fixed path style.",
            "The demo asserts the texture matches this record and verifies the arc rendering.",
        ],
        "requirements": [
            "The first three draws must be consumed first so the texture draw reads the correct stream word.",
            "The texture draw must be the stream word modulo 4, mapped to the frozen list in order.",
            "The glyph must render the texture's fixed arc count and path style.",
            "The demo must assert the texture equals 'coily' as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The four textures are frozen in order: straight, wavy, curly, coily.",
            "Arc count equals texture index plus one; path styles are frozen per texture.",
            "Record text and demo output are cross-checked on digest, draw, texture, and arc rendering.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the fourth witness styles the seal's "
            "crown - four zigzag arcs for 'coily', drawn by rule, not by "
            "hand. The style is the Signature's own engraving pattern: "
            "fixed, repeatable, and labeled as artifice."
        ),
    },
    {
        "key": "trait_hair_shade",
        "name": "Deriving Hair Shade from a Sequence",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "This record derives hair shade - the fifth trait - from a "
            "single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration TGGTCGCGTGGCCTTATGGACAAATTACCGCGGACAT "
            "GAGGGCCGTTTCCAACGAGAAACCACCGAACGTCT. Its FNV-1a digest is "
            "6b58c69a680501c3. The shade trait consumes the fifth generator "
            "word: the draw is 3 of 6, selecting shade-4 from the six "
            "abstract slots shade-1 through shade-6. Hair shades are "
            "abstract slot indices, not colorimetry and not predictions: "
            "shade-4 is the fourth of six model positions. Same sequence "
            "in, digest 6b58c69a680501c3, fifth draw 3 of 6, shade-4 - "
            "every time. This is a Signature-generated deterministic "
            "model, a stylized parametric abstraction, never a real "
            "person's appearance."
        ),
        "how_it_works": (
            "The shade derivation advances the generator past the first "
            "four draws and takes the fifth word modulo 6, reporting "
            "shade-1 through shade-6. The slot index feeds the glyph's "
            "stroke palette by a fixed mapping, keeping the artwork "
            "abstract - no attempt is made to render realistic hair "
            "color. The demonstration program replays the five draws, "
            "prints each residue in order, asserts the shade equals "
            "'shade-4' as stated here, and confirms the full "
            "representation is byte-identical across two runs."
        ),
        "key_points": [
            "Hair shade is the fifth draw: the fifth generator word modulo 6 selects shade-1 through shade-6.",
            "For this record's sequence the digest is 6b58c69a680501c3 and the shade draw is 3 of 6, giving shade-4.",
            "Shades are abstract slot indices, not colorimetry and not predictions.",
            "The glyph maps the slot index to its stroke palette by a fixed rule, keeping the art abstract.",
            "The demo asserts the shade matches this record and checks full-representation determinism.",
        ],
        "requirements": [
            "The first four draws must be consumed first so the shade draw reads the correct stream word.",
            "The shade draw must be the stream word modulo 6, reported as shade-1 through shade-6.",
            "The shade must be presented as an abstract model slot, never as a real hair color.",
            "The demo must assert the shade equals 'shade-4' as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The six shade slots are labeled shade-1 through shade-6, in order.",
            "The glyph's stroke mapping from shade index is frozen.",
            "Record text and demo output are cross-checked on digest, draw, and shade.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the fifth witness names a shade-slot, "
            "shade-4 - the Signature's own numbering of an abstract "
            "spectrum. Six slots, fixed order, no claim beyond the model: "
            "that is the honest palette."
        ),
    },
    {
        "key": "trait_eye",
        "name": "Deriving Eye Color from a Sequence",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "This record derives eye color - the sixth trait - from a "
            "single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration GTTTCTTTTTTATCGCCTACTTCTCACACCGGTGCCC "
            "GTGAATCGAGCTCGTCGACTTATTTCTACGACCGG. Its FNV-1a digest is "
            "0ae12ade81cab08a. The eye-color trait consumes the sixth "
            "generator word: the draw is 5 of 6, selecting 'amber' from "
            "the frozen list (brown, hazel, green, blue, gray, amber). Eye "
            "color here is a label that chooses the glyph's dot fill from "
            "a fixed hex map - amber maps to #B8860B - and it is not a "
            "prediction about anyone's eyes. Same sequence in, digest "
            "0ae12ade81cab08a, sixth draw 5 of 6, eye color amber - every "
            "time. This is a Signature-generated deterministic model, a "
            "stylized parametric abstraction, never a real person's "
            "appearance."
        ),
        "how_it_works": (
            "The eye-color derivation advances the generator past the "
            "first five draws and takes the sixth word modulo 6, indexing "
            "the frozen color list in order: 0 brown, 1 hazel, 2 green, 3 "
            "blue, 4 gray, 5 amber. The glyph stage looks up the label in "
            "the frozen hex map and fills the two abstract eye dots - two "
            "geometric circles, positioned by rule, carrying no portrait "
            "meaning. The demonstration program replays the six draws, "
            "asserts the eye color equals 'amber' as stated here, checks "
            "the hex lookup gives #B8860B, verifies the two dots in the "
            "built glyph carry that fill, and confirms byte-identical "
            "representations across two runs."
        ),
        "key_points": [
            "Eye color is the sixth draw: the sixth generator word modulo 6 selects brown, hazel, green, blue, gray, or amber.",
            "For this record's sequence the digest is 0ae12ade81cab08a and the eye draw is 5 of 6, giving amber.",
            "The label selects the glyph's dot fill from a frozen hex map (amber is #B8860B); it is not a prediction about eyes.",
            "The dots are abstract geometric circles positioned by rule - decoration of the seal, not a portrait.",
            "The demo asserts the color and hex match this record and checks full-representation determinism.",
        ],
        "requirements": [
            "The first five draws must be consumed first so the eye draw reads the correct stream word.",
            "The eye draw must be the stream word modulo 6, mapped to the frozen color list in order.",
            "The hex map must be the frozen six-entry map; no other colors may appear.",
            "The demo must assert the color equals 'amber' and the hex equals '#B8860B' as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The six eye colors are frozen in order: brown, hazel, green, blue, gray, amber.",
            "The hex map is frozen: brown #6B4226, hazel #8A6D3B, green #4F7942, blue #3B6EA5, gray #7D7D7D, amber #B8860B.",
            "Record text and demo output are cross-checked on digest, draw, color, and hex.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the sixth witness names amber, and the "
            "seal takes two amber dots - #B8860B, by the frozen map. The "
            "dots are punctuation on the seal, not windows to any soul; "
            "the record says so, and the label says so."
        ),
    },
    {
        "key": "trait_face_ratio",
        "name": "Deriving the Face Width Ratio from a Sequence",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "This record derives the face width ratio - the seventh trait "
            "and the first of the two geometry parameters - from a single "
            "synthetic sequence. The sequence is the 72-base synthetic "
            "illustration GTTTCCTGGCAAGTGGTGCAAATAGAGTGTAGGTGAATGCGACACCT "
            "AGTTGCTACGACTTTAGATAAAAAG. Its FNV-1a digest is "
            "bf76eceda54d7a06. The ratio trait consumes the seventh "
            "generator word: the draw is 1 of 21, and the ratio is (72 + "
            "1) / 100 = 0.73. The face width ratio is an abstract geometry "
            "parameter of the model - a quantized slot between 0.72 and "
            "0.92 in 21 steps - not a measurement of any real face. It "
            "drives the glyph's central disc radius (52 plus the step, in "
            "pixels) and the hair-arc span. Same sequence in, digest "
            "bf76eceda54d7a06, seventh draw 1 of 21, ratio 0.73 - every "
            "time. This is a Signature-generated deterministic model, a "
            "stylized parametric abstraction, never a real person's "
            "appearance."
        ),
        "how_it_works": (
            "The ratio derivation advances the generator past the first "
            "six draws and takes the seventh word modulo 21, giving a "
            "step from 0 to 20. The ratio is (72 + step) / 100, so the "
            "possible values are exactly 0.72, 0.73, ..., 0.92 - 21 "
            "quantized slots with no other values possible. Integer "
            "arithmetic is used deliberately: the step is an integer, and "
            "the division is the final formatting step, so Python and "
            "JavaScript agree exactly. The glyph stage uses the step "
            "directly (disc radius 52 + step), never the float, keeping "
            "every coordinate an integer. The demonstration program "
            "replays the seven draws, asserts the step equals 1 and the "
            "formatted ratio equals '0.73' as stated here, checks the "
            "disc radius in the built glyph equals 53, and confirms "
            "byte-identical representations across two runs."
        ),
        "key_points": [
            "The face width ratio is the seventh draw: the seventh word modulo 21 gives a step 0-20, and the ratio is (72 + step)/100.",
            "For this record's sequence the digest is bf76eceda54d7a06, the step is 1 of 21, and the ratio is 0.73.",
            "The ratio is an abstract geometry parameter with 21 quantized slots from 0.72 to 0.92 - not a measurement of any real face.",
            "Integer arithmetic keeps Python and JavaScript in exact agreement; the glyph uses the integer step for its disc radius.",
            "The demo asserts the step, ratio, and disc radius match this record and checks determinism.",
        ],
        "requirements": [
            "The first six draws must be consumed first so the ratio draw reads the correct stream word.",
            "The step must be the stream word modulo 21; the ratio must be (72 + step)/100 with no other values possible.",
            "The ratio must be presented as an abstract model parameter, never as a facial measurement.",
            "The demo must assert the formatted ratio equals '0.73' and the disc radius equals 53 as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The 21 ratio slots are exactly 0.72 through 0.92 in 0.01 steps; no intermediate values exist.",
            "The glyph's disc radius is 52 + step pixels, an integer always.",
            "Record text and demo output are cross-checked on digest, draw, ratio, and disc radius.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the seventh witness measures nothing and "
            "declares a proportion - 0.73, the second of twenty-one sworn "
            "slots. The disc of the seal is drawn 53 pixels wide by that "
            "declaration: geometry as covenant, not as calipers."
        ),
    },
    {
        "key": "trait_jaw",
        "name": "Deriving the Jaw Angle from a Sequence",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "This record derives the jaw angle - the eighth trait and the "
            "second geometry parameter - from a single synthetic sequence. "
            "The sequence is the 72-base synthetic illustration GGCACTGA "
            "TTGCTTGGGCACCTATCCTAGAGACAGTGCTAATACAGGAAGTCGATCTCTAGTATAA "
            "CGCCAA. Its FNV-1a digest is c9864991eb3b86d6. The jaw trait "
            "consumes the eighth generator word: the draw is 35 of 41, "
            "and the angle is 100 + 35 = 135 degrees. The jaw angle is an "
            "abstract geometry parameter - a whole-degree slot from 100 "
            "to 140 - not a measurement of any real jaw. It drives the "
            "first of the glyph's three trait bars (bar height 20 plus "
            "angle minus 100, here 55 pixels). Same sequence in, digest "
            "c9864991eb3b86d6, eighth draw 35 of 41, jaw angle 135 - every "
            "time. This is a Signature-generated deterministic model, a "
            "stylized parametric abstraction, never a real person's "
            "appearance."
        ),
        "how_it_works": (
            "The jaw derivation advances the generator past the first "
            "seven draws and takes the eighth word modulo 41, giving a "
            "step from 0 to 40; the angle is 100 + step, always a whole "
            "number of degrees from 100 to 140. The glyph's first trait "
            "bar rises from the baseline with height 20 + step pixels, so "
            "the bar is a direct, integer-exact picture of the draw. The "
            "demonstration program replays the eight draws, asserts the "
            "step equals 35 and the angle equals 135 as stated here, "
            "checks the first bar's height in the built glyph equals 55 "
            "pixels, and confirms byte-identical representations across "
            "two runs."
        ),
        "key_points": [
            "The jaw angle is the eighth draw: the eighth word modulo 41 gives a step 0-40, and the angle is 100 + step degrees.",
            "For this record's sequence the digest is c9864991eb3b86d6, the step is 35 of 41, and the angle is 135.",
            "The angle is an abstract geometry slot from 100 to 140 whole degrees - not a measurement of any real jaw.",
            "The glyph's first trait bar is 20 + step pixels tall, an integer-exact picture of the draw.",
            "The demo asserts the step, angle, and bar height match this record and checks determinism.",
        ],
        "requirements": [
            "The first seven draws must be consumed first so the jaw draw reads the correct stream word.",
            "The step must be the stream word modulo 41; the angle must be 100 + step, a whole number.",
            "The angle must be presented as an abstract model parameter, never as a facial measurement.",
            "The demo must assert the angle equals 135 and the bar height equals 55 as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The 41 angle slots are exactly 100 through 140 whole degrees; no fractions exist.",
            "The first trait bar height is 20 + step pixels, always an integer.",
            "Record text and demo output are cross-checked on digest, draw, angle, and bar height.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the eighth witness declares 135 - the "
            "thirty-sixth of forty-one sworn degrees - and the seal's "
            "first bar rises 55 pixels on that word. An angle as covenant: "
            "whole, fixed, and labeled a model."
        ),
    },
    {
        "key": "trait_nose",
        "name": "Deriving Nose Bridge Geometry from a Sequence",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "This record derives nose bridge geometry - the ninth trait - "
            "from a single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration GAGGCTGCTAATCAACACGTACTTGAGTGACATGTCC "
            "TTCCTATCCCAATAAGAAGTCACGTCCCGCTAGAT. Its FNV-1a digest is "
            "4cd305f0adea65f1. The nose trait consumes the ninth generator "
            "word: the draw is 1 of 3, selecting 'medium' from the frozen "
            "list (low, medium, high). Nose bridge geometry here is an "
            "abstract slot driving the glyph's second trait bar (height 20 "
            "plus index times 15 pixels, here 35), not a description of "
            "any real nose. Same sequence in, digest 4cd305f0adea65f1, "
            "ninth draw 1 of 3, nose bridge medium - every time. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The nose derivation advances the generator past the first "
            "eight draws and takes the ninth word modulo 3, indexing low, "
            "medium, high in order. The glyph's second bar encodes the "
            "index directly: 20 + index * 15 pixels tall, so 'medium' "
            "always draws a 35-pixel bar. The demonstration program "
            "replays the nine draws, asserts the nose bridge equals "
            "'medium' as stated here, checks the second bar's height in "
            "the built glyph equals 35 pixels, and confirms byte-identical "
            "representations across two runs."
        ),
        "key_points": [
            "Nose bridge geometry is the ninth draw: the ninth word modulo 3 selects low, medium, or high.",
            "For this record's sequence the digest is 4cd305f0adea65f1 and the nose draw is 1 of 3, giving medium.",
            "The slot is abstract - it drives the glyph's second trait bar, not a description of any real nose.",
            "The second bar is 20 + index * 15 pixels tall, so medium always draws 35 pixels.",
            "The demo asserts the slot and bar height match this record and checks determinism.",
        ],
        "requirements": [
            "The first eight draws must be consumed first so the nose draw reads the correct stream word.",
            "The nose draw must be the stream word modulo 3, mapped to low, medium, high in order.",
            "The slot must be presented as an abstract model parameter, never as a nasal description.",
            "The demo must assert the bridge equals 'medium' and the bar height equals 35 as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The three nose slots are frozen in order: low, medium, high.",
            "The second trait bar height is 20 + index * 15 pixels, always an integer.",
            "Record text and demo output are cross-checked on digest, draw, slot, and bar height.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the ninth witness takes the middle path - "
            "'medium', the second of three - and the seal's second bar "
            "stands 35 pixels on that word. Three slots, fixed order, "
            "sworn as a model and nothing more."
        ),
    },
    {
        "key": "trait_brow",
        "name": "Deriving Brow Density from a Sequence",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "This record derives brow density - the tenth trait - from a "
            "single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration CCATTCCCAGTTTAAGACGTGATGCCGGGATTGCGC "
            "TGAAGTGGGCGGAGGTTAGGGTGGAGAAGAGGGTCG. Its FNV-1a digest is "
            "bd8809d566b3de88. The brow trait consumes the tenth generator "
            "word: the draw is 1 of 3, selecting 'medium' from the frozen "
            "list (light, medium, full). Brow density here is an abstract "
            "slot driving the glyph's third trait bar (height 20 plus "
            "index times 15 pixels, here 35), not a description of any "
            "real brow. Same sequence in, digest bd8809d566b3de88, tenth "
            "draw 1 of 3, brow density medium - every time. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The brow derivation advances the generator past the first "
            "nine draws and takes the tenth word modulo 3, indexing "
            "light, medium, full in order. The glyph's third bar encodes "
            "the index: 20 + index * 15 pixels, so 'medium' always draws "
            "35 pixels. The demonstration program replays the ten draws, "
            "asserts the brow density equals 'medium' as stated here, "
            "checks the third bar's height in the built glyph equals 35 "
            "pixels, and confirms byte-identical representations across "
            "two runs."
        ),
        "key_points": [
            "Brow density is the tenth draw: the tenth word modulo 3 selects light, medium, or full.",
            "For this record's sequence the digest is bd8809d566b3de88 and the brow draw is 1 of 3, giving medium.",
            "The slot is abstract - it drives the glyph's third trait bar, not a description of any real brow.",
            "The third bar is 20 + index * 15 pixels tall, so medium always draws 35 pixels.",
            "The demo asserts the slot and bar height match this record and checks determinism.",
        ],
        "requirements": [
            "The first nine draws must be consumed first so the brow draw reads the correct stream word.",
            "The brow draw must be the stream word modulo 3, mapped to light, medium, full in order.",
            "The slot must be presented as an abstract model parameter, never as a brow description.",
            "The demo must assert the density equals 'medium' and the bar height equals 35 as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The three brow slots are frozen in order: light, medium, full.",
            "The third trait bar height is 20 + index * 15 pixels, always an integer.",
            "Record text and demo output are cross-checked on digest, draw, slot, and bar height.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the tenth witness also takes the middle "
            "path - 'medium' - and the seal's third bar stands 35 pixels. "
            "The three bars together are the seal's own histogram: jaw, "
            "nose, brow, each sworn in order."
        ),
    },
    {
        "key": "trait_lip",
        "name": "Deriving Lip Fullness from a Sequence",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "This record derives lip fullness - the eleventh trait - from "
            "a single synthetic sequence. The sequence is the 72-base "
            "synthetic illustration ATACTTACAGCAGAATATTTGGAACCTGATTAGAAT "
            "TTGGCTATTACAAAGTACCTGTCCCCTAGGAATCGC. Its FNV-1a digest is "
            "9e28fda1a42eeea2. The lip trait consumes the eleventh "
            "generator word: the draw is 0 of 3, selecting 'thin' from "
            "the frozen list (thin, medium, full). Lip fullness here is "
            "an abstract slot of the likeness model, not a description of "
            "any real lips. Same sequence in, digest 9e28fda1a42eeea2, "
            "eleventh draw 0 of 3, lip fullness thin - every time. This is "
            "a Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The lip derivation advances the generator past the first ten "
            "draws and takes the eleventh word modulo 3, indexing thin, "
            "medium, full in order. The slot is carried in the vector and "
            "available to the glyph's future revisions; in the frozen "
            "HLX-1 template it is recorded as a named parameter, keeping "
            "the twelve-value contract complete. The demonstration program "
            "replays the eleven draws, asserts the lip fullness equals "
            "'thin' as stated here, verifies the full twelve-key vector "
            "is present in order, and confirms byte-identical "
            "representations across two runs."
        ),
        "key_points": [
            "Lip fullness is the eleventh draw: the eleventh word modulo 3 selects thin, medium, or full.",
            "For this record's sequence the digest is 9e28fda1a42eeea2 and the lip draw is 0 of 3, giving thin.",
            "The slot is an abstract model parameter, not a description of any real lips.",
            "It is carried as a named parameter in the twelve-value vector, keeping the contract complete.",
            "The demo asserts the slot matches this record and checks full-vector determinism.",
        ],
        "requirements": [
            "The first ten draws must be consumed first so the lip draw reads the correct stream word.",
            "The lip draw must be the stream word modulo 3, mapped to thin, medium, full in order.",
            "The slot must be presented as an abstract model parameter, never as a lip description.",
            "The demo must assert the fullness equals 'thin' as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The three lip slots are frozen in order: thin, medium, full.",
            "The vector always carries all twelve keys in the fixed order, even when one trait is studied alone.",
            "Record text and demo output are cross-checked on digest, draw, and slot.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the eleventh witness speaks softly - "
            "'thin', the first of three. Eleven witnesses have now sworn; "
            "one remains. The vector holds every word; the covenant drops "
            "none."
        ),
    },
    {
        "key": "trait_freckle",
        "name": "Deriving Freckle Density from a Sequence",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "This record derives freckle density - the twelfth and final "
            "trait - from a single synthetic sequence. The sequence is the "
            "72-base synthetic illustration TCTTGCTCGACACCGTGCGCAACCTTAGTG "
            "CGGCCTATGTGCGTCTAAGCCGGCCGGGCTCTCTACTCCCAA. Its FNV-1a digest "
            "is fac04fb523dc8bae. The freckle trait consumes the twelfth "
            "generator word: the draw is 3 of 4, selecting 'dense' from "
            "the frozen list (none, sparse, moderate, dense). Freckle "
            "density here is an abstract slot that sets the glyph's dot "
            "count - five dots per density step, so 'dense' draws fifteen "
            "dots on a deterministic grid - not a description of any real "
            "skin. Same sequence in, digest fac04fb523dc8bae, twelfth draw "
            "3 of 4, freckle density dense - every time. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The freckle derivation advances the generator past the first "
            "eleven draws and takes the twelfth word modulo 4, indexing "
            "none, sparse, moderate, dense in order. The glyph stage "
            "multiplies the index by five for the dot count (dense gives "
            "fifteen) and places the dots on a fixed arithmetic grid, so "
            "the dot field is as deterministic as everything else. The "
            "demonstration program replays all twelve draws, asserts the "
            "freckle density equals 'dense' as stated here, counts fifteen "
            "freckle dots in the built glyph, and confirms byte-identical "
            "representations across two runs - completing the compounded "
            "tier with all twelve traits derived."
        ),
        "key_points": [
            "Freckle density is the twelfth and final draw: the twelfth word modulo 4 selects none, sparse, moderate, or dense.",
            "For this record's sequence the digest is fac04fb523dc8bae and the freckle draw is 3 of 4, giving dense.",
            "The slot sets the glyph's dot count - five dots per density step, fifteen for dense - on a deterministic grid.",
            "It is an abstract model parameter, not a description of any real skin.",
            "The demo asserts the slot and dot count match this record, completing all twelve single-trait derivations.",
        ],
        "requirements": [
            "The first eleven draws must be consumed first so the freckle draw reads the correct stream word.",
            "The freckle draw must be the stream word modulo 4, mapped to none, sparse, moderate, dense in order.",
            "The dot count must be index times five on the fixed grid; no other placement is permitted.",
            "The demo must assert the density equals 'dense' and the glyph carries fifteen freckle dots as stated here.",
            "The model label must accompany the derived trait wherever it is shown.",
        ],
        "standards": [
            "The four freckle slots are frozen in order: none, sparse, moderate, dense.",
            "Freckle dots are 1.6-pixel radius circles in the fixed dark tone, placed by the frozen grid formula.",
            "Record text and demo output are cross-checked on digest, draw, slot, and dot count.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the twelfth witness closes the testimony "
            "- 'dense', fifteen dots scattered by rule across the seal. "
            "Twelve witnesses, twelve oaths, one seal: the compounded "
            "tier is complete, and every word is labeled a model."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "combining_traits",
        "name": "Combining All Traits into One Representation",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "This record combines all twelve traits into one complete "
            "representation for a single synthetic sequence, demonstrating "
            "the full pipeline end to end. The sequence is the 72-base "
            "synthetic illustration HLX-0003: GGCAGCCTACCCGCCGCCTGTTGCG "
            "GTAAGTCTGGATAGGGCGTAAGAGGAACCGATCCCCAGCAAATAGTC. Its FNV-1a "
            "digest is 8cdeab169331fbd3. The twelve draws in order produce "
            "the trait-parameter vector "
            '{"height_band":"below-average","build":"slight","skin_band":'
            '"band-6","hair_texture":"curly","hair_shade":"shade-4",'
            '"eye_color":"gray","face_width_ratio":0.79,"jaw_angle":100,'
            '"nose_bridge":"high","brow_density":"full","lip_fullness":'
            '"medium","freckle_density":"moderate"}. The vector serializes '
            "to that exact compact JSON string - keys in the fixed order, "
            "no whitespace - and the abstract glyph is built from it: a "
            "240-by-240 geometric composition with the computed background "
            "hue, central disc, three trait bars, curly hair arcs, gray "
            "eye dots, and a moderate freckle field, captioned as a "
            "deterministic model, not a person. One sequence in, three "
            "outputs out - vector, glyph, derivation - all byte-identical "
            "on every run. This is a Signature-generated deterministic "
            "model, a stylized parametric abstraction, never a real "
            "person's appearance."
        ),
        "how_it_works": (
            "Combination works by chaining the stages with no gaps. "
            "Validation accepts the 72-base ACGT string; FNV-1a digests it "
            "to 8cdeab169331fbd3; xorshift64* expands the digest into the "
            "stream; twelve draws in the fixed order fill the vector; the "
            "vector serializes to the exact JSON string; the glyph builder "
            "reads the vector indices and fills the fixed SVG template. "
            "The step-by-step derivation is the audit trail: each stage's "
            "output is printed and checkable, from the digest through "
            "each draw residue to the final strings. The demonstration "
            "program performs the full combination, asserts the vector "
            "JSON equals the string stated here exactly, asserts the "
            "glyph contains the model caption, and verifies the whole "
            "representation is byte-identical across two runs."
        ),
        "key_points": [
            "One synthetic sequence (HLX-0003, digest 8cdeab169331fbd3) yields the complete twelve-trait vector stated here.",
            "The vector serializes to one exact compact JSON string with the fixed key order - the string itself is the audit point.",
            "The glyph is built from the vector alone through the fixed template: hue, disc, bars, arcs, dots, caption.",
            "The step-by-step derivation prints every stage's output, making the combination checkable by hand.",
            "The demo asserts the exact JSON string and verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "All six pipeline stages must run in order with no skipped or reordered steps.",
            "The vector JSON must equal the exact string stated in this record, byte-for-byte.",
            "The glyph must be built solely from the vector through the frozen template.",
            "The derivation must print each stage's output in order for auditability.",
            "The model label must appear in the record text, the vector output, and the glyph caption.",
        ],
        "standards": [
            "The vector JSON uses compact separators and the fixed twelve-key order with no whitespace.",
            "The glyph is the frozen 240-by-240 template with integer formatting throughout.",
            "Record text and demo output are cross-checked: the digest and JSON string stated here are asserted by code.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: twelve witnesses sworn, one seal stamped - "
            "the combination is the covenant fulfilled in full. The "
            "vector is the testimony written down; the glyph is the seal "
            "pressed beside it; the derivation is the clerk's record that "
            "all was done in order."
        ),
    },
    {
        "key": "full_a",
        "name": "Full Likeness Derivation A: Sequence HLX-0001",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation A processes the synthetic sequence "
            "HLX-0001 - GGAATACAGTAGCGACGCCCTAGTTGACAATCTAATCCTAGTCGTGTC "
            "TCGGCTGCGGTGCGCATGGAGAAC, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is d8c119491440887d. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"above-average","build":"slight","skin_band":'
            '"band-2","hair_texture":"coily","hair_shade":"shade-3",'
            '"eye_color":"gray","face_width_ratio":0.91,"jaw_angle":136,'
            '"nose_bridge":"high","brow_density":"full","lip_fullness":'
            '"medium","freckle_density":"dense"}. The abstract glyph built '
            "from this vector carries four zigzag hair arcs (coily), gray "
            "eye dots (#7D7D7D), and a dense fifteen-dot freckle field, "
            "with the model caption embedded. The derivation is fully "
            "replayable: any correct implementation of HLX-1 fed this "
            "sequence must produce this exact vector and this exact glyph. "
            "This is a Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation works exactly as the pipeline record "
            "specifies: validate the 72 ACGT bases, digest to "
            "d8c119491440887d, seed xorshift64*, draw twelve times in the "
            "fixed order, serialize the vector, build the glyph. Each "
            "draw's residue is printed in the step-by-step derivation so "
            "the path from digest to vector is fully visible. The "
            "demonstration program replays the derivation, asserts the "
            "vector JSON equals the string stated here byte-for-byte, "
            "asserts the glyph contains four zigzag arcs and fifteen "
            "freckle dots, and verifies byte-identical output across two "
            "runs."
        ),
        "key_points": [
            "HLX-0001 digests to d8c119491440887d and derives the twelve-trait vector stated here.",
            "The vector serializes to one exact compact JSON string, asserted byte-for-byte by the demo.",
            "The glyph shows coily arcs (four zigzags), gray dots, and a fifteen-dot freckle field.",
            "The step-by-step derivation prints every draw residue, making the path from digest to vector visible.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0001 string, validated before digestion.",
            "The digest d8c119491440887d must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the coily arcs, gray dots, fifteen freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged; full derivations are acceptance tests of the pipeline.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the first full seal of the advanced tier - "
            "HLX-0001's twelve witnesses swear above-average, slight, "
            "band-2, coily, shade-3, gray, 0.91, 136, high, full, medium, "
            "dense. The seal is pressed, the caption is set: a model, "
            "labeled, and nothing more."
        ),
    },
    {
        "key": "full_b",
        "name": "Full Likeness Derivation B: Sequence HLX-0002",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation B processes the synthetic sequence "
            "HLX-0002 - TCGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCT "
            "TCCTGCCTACAGGAGATTTGAATT, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is c03bdc94dcbe9c44. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"compact","build":"slight","skin_band":"band-3",'
            '"hair_texture":"curly","hair_shade":"shade-3","eye_color":'
            '"hazel","face_width_ratio":0.74,"jaw_angle":115,"nose_bridge":'
            '"medium","brow_density":"medium","lip_fullness":"full",'
            '"freckle_density":"none"}. The abstract glyph built from this '
            "vector carries three double-wave hair arcs (curly), hazel eye "
            "dots (#8A6D3B), and no freckle dots, with the model caption "
            "embedded. Any correct HLX-1 implementation fed this sequence "
            "must produce this exact vector and glyph. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to c03bdc94dcbe9c44, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains three double-wave "
            "arcs, hazel dots, and zero freckle dots, and verifies "
            "byte-identical output across two runs."
        ),
        "key_points": [
            "HLX-0002 digests to c03bdc94dcbe9c44 and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows curly arcs (three double waves), hazel dots, and an empty freckle field.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0002 string, validated before digestion.",
            "The digest c03bdc94dcbe9c44 must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the curly arcs, hazel dots, zero freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the second full seal - HLX-0002's "
            "witnesses swear compact, slight, band-3, curly, shade-3, "
            "hazel, 0.74, 115, medium, medium, full, none. Three waves "
            "crown the seal; no freckle dots fall. A model, labeled."
        ),
    },
    {
        "key": "full_c",
        "name": "Full Likeness Derivation C: Sequence HLX-0003",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation C processes the synthetic sequence "
            "HLX-0003 - GGCAGCCTACCCGCCGCCTGTTGCGGTAAGTCTGGATAGGGCGTAAGA "
            "GGAACCGATCCCCAGCAAATAGTC, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is 8cdeab169331fbd3. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"below-average","build":"slight","skin_band":'
            '"band-6","hair_texture":"curly","hair_shade":"shade-4",'
            '"eye_color":"gray","face_width_ratio":0.79,"jaw_angle":100,'
            '"nose_bridge":"high","brow_density":"full","lip_fullness":'
            '"medium","freckle_density":"moderate"}. The abstract glyph '
            "built from this vector carries three double-wave arcs "
            "(curly), gray eye dots (#7D7D7D), and a moderate ten-dot "
            "freckle field, with the model caption embedded. Any correct "
            "HLX-1 implementation fed this sequence must produce this "
            "exact vector and glyph. This is a Signature-generated "
            "deterministic model, a stylized parametric abstraction, never "
            "a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to 8cdeab169331fbd3, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains three double-wave "
            "arcs, gray dots, and ten freckle dots, and verifies "
            "byte-identical output across two runs."
        ),
        "key_points": [
            "HLX-0003 digests to 8cdeab169331fbd3 and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows curly arcs, gray dots, and a ten-dot freckle field.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0003 string, validated before digestion.",
            "The digest 8cdeab169331fbd3 must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the curly arcs, gray dots, ten freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the third full seal - HLX-0003's "
            "witnesses swear below-average, slight, band-6, curly, "
            "shade-4, gray, 0.79, 100, high, full, medium, moderate. Ten "
            "dots by rule; the caption stands. A model, labeled."
        ),
    },
    {
        "key": "full_d",
        "name": "Full Likeness Derivation D: Sequence HLX-0004",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation D processes the synthetic sequence "
            "HLX-0004 - GGACAAGCGGATGAGTTATTGGGCGAGGCAAAGGAGTCGTGTTCTGC "
            "TTCGTCGAATCCTGAATGATGGTCA, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is dacd55d950badd37. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"average","build":"broad","skin_band":"band-2",'
            '"hair_texture":"curly","hair_shade":"shade-1","eye_color":'
            '"blue","face_width_ratio":0.77,"jaw_angle":107,"nose_bridge":'
            '"high","brow_density":"light","lip_fullness":"full",'
            '"freckle_density":"moderate"}. The abstract glyph built from '
            "this vector carries three double-wave arcs (curly), blue eye "
            "dots (#3B6EA5), and a ten-dot freckle field, with the model "
            "caption embedded. Any correct HLX-1 implementation fed this "
            "sequence must produce this exact vector and glyph. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to dacd55d950badd37, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains three double-wave "
            "arcs, blue dots, and ten freckle dots, and verifies "
            "byte-identical output across two runs."
        ),
        "key_points": [
            "HLX-0004 digests to dacd55d950badd37 and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows curly arcs, blue dots, and a ten-dot freckle field.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0004 string, validated before digestion.",
            "The digest dacd55d950badd37 must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the curly arcs, blue dots, ten freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the fourth full seal - HLX-0004's "
            "witnesses swear average, broad, band-2, curly, shade-1, blue, "
            "0.77, 107, high, light, full, moderate. Blue dots by the "
            "frozen map; the caption stands. A model, labeled."
        ),
    },
    {
        "key": "full_e",
        "name": "Full Likeness Derivation E: Sequence HLX-0005",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation E processes the synthetic sequence "
            "HLX-0005 - GGGTAAGATTACTAGATAAATCAGAAATCCTAGATCACAAATCTCGC "
            "AAATGTATAAACGCGAACGTGGAGG, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is 0069aa1e41547c6a. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"average","build":"slight","skin_band":"band-5",'
            '"hair_texture":"wavy","hair_shade":"shade-1","eye_color":'
            '"blue","face_width_ratio":0.9,"jaw_angle":101,"nose_bridge":'
            '"high","brow_density":"full","lip_fullness":"thin",'
            '"freckle_density":"sparse"}. The abstract glyph built from '
            "this vector carries two single-wave arcs (wavy), blue eye "
            "dots (#3B6EA5), and a sparse five-dot freckle field, with the "
            "model caption embedded. Any correct HLX-1 implementation fed "
            "this sequence must produce this exact vector and glyph. This "
            "is a Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to 0069aa1e41547c6a, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains two single-wave "
            "arcs, blue dots, and five freckle dots, and verifies "
            "byte-identical output across two runs."
        ),
        "key_points": [
            "HLX-0005 digests to 0069aa1e41547c6a and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows wavy arcs (two single waves), blue dots, and a five-dot freckle field.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0005 string, validated before digestion.",
            "The digest 0069aa1e41547c6a must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the wavy arcs, blue dots, five freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the fifth full seal - HLX-0005's "
            "witnesses swear average, slight, band-5, wavy, shade-1, blue, "
            "0.9, 101, high, full, thin, sparse. Two waves crown it; five "
            "dots fall by rule. A model, labeled."
        ),
    },
    {
        "key": "full_f",
        "name": "Full Likeness Derivation F: Sequence HLX-0006",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation F processes the synthetic sequence "
            "HLX-0006 - CCTAGGGCTCAGCCAAGTTAGCAGTTTTGAAGTTCTGGCTGCCCCGA "
            "GTATTGCCACGGATCACATGTCACC, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is eaddb986e196d23d. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"compact","build":"broad","skin_band":"band-2",'
            '"hair_texture":"straight","hair_shade":"shade-5","eye_color":'
            '"gray","face_width_ratio":0.78,"jaw_angle":125,"nose_bridge":'
            '"medium","brow_density":"full","lip_fullness":"thin",'
            '"freckle_density":"sparse"}. The abstract glyph built from '
            "this vector carries one straight arc, gray eye dots "
            "(#7D7D7D), and a five-dot freckle field, with the model "
            "caption embedded. Any correct HLX-1 implementation fed this "
            "sequence must produce this exact vector and glyph. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to eaddb986e196d23d, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains one straight arc, "
            "gray dots, and five freckle dots, and verifies byte-identical "
            "output across two runs."
        ),
        "key_points": [
            "HLX-0006 digests to eaddb986e196d23d and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows a single straight arc, gray dots, and a five-dot freckle field.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0006 string, validated before digestion.",
            "The digest eaddb986e196d23d must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the straight arc, gray dots, five freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the sixth full seal - HLX-0006's "
            "witnesses swear compact, broad, band-2, straight, shade-5, "
            "gray, 0.78, 125, medium, full, thin, sparse. One straight "
            "line crowns it; the caption stands. A model, labeled."
        ),
    },
    {
        "key": "full_g",
        "name": "Full Likeness Derivation G: Sequence HLX-0007",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation G processes the synthetic sequence "
            "HLX-0007 - ACGGGACAGCGACGTGAGCTAGTAGGTTTATGCGATTCGGCAATGTC "
            "AGGCGAGGTGTGTAAACCCCTAAGA, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is baeb1e73f11301fa. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"above-average","build":"sturdy","skin_band":'
            '"band-1","hair_texture":"wavy","hair_shade":"shade-6",'
            '"eye_color":"gray","face_width_ratio":0.86,"jaw_angle":124,'
            '"nose_bridge":"high","brow_density":"light","lip_fullness":'
            '"medium","freckle_density":"sparse"}. The abstract glyph built '
            "from this vector carries two single-wave arcs (wavy), gray "
            "eye dots (#7D7D7D), and a five-dot freckle field, with the "
            "model caption embedded. Any correct HLX-1 implementation fed "
            "this sequence must produce this exact vector and glyph. This "
            "is a Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to baeb1e73f11301fa, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains two single-wave "
            "arcs, gray dots, and five freckle dots, and verifies "
            "byte-identical output across two runs."
        ),
        "key_points": [
            "HLX-0007 digests to baeb1e73f11301fa and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows wavy arcs, gray dots, and a five-dot freckle field.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0007 string, validated before digestion.",
            "The digest baeb1e73f11301fa must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the wavy arcs, gray dots, five freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the seventh full seal - HLX-0007's "
            "witnesses swear above-average, sturdy, band-1, wavy, "
            "shade-6, gray, 0.86, 124, high, light, medium, sparse. Two "
            "waves, five dots, one caption. A model, labeled."
        ),
    },
    {
        "key": "full_h",
        "name": "Full Likeness Derivation H: Sequence HLX-0008",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Full likeness derivation H processes the synthetic sequence "
            "HLX-0008 - CTAACAAATCATCGCTTTATACAACTCTGCTGGACCGTCGACAGCCA "
            "AAGACCAACAAGAGGAATTATCCGC, 72 bases - through the complete "
            "pipeline. Its FNV-1a digest is 44115893398c6cd7. The twelve "
            "draws produce the trait-parameter vector "
            '{"height_band":"above-average","build":"broad","skin_band":'
            '"band-5","hair_texture":"straight","hair_shade":"shade-4",'
            '"eye_color":"green","face_width_ratio":0.87,"jaw_angle":128,'
            '"nose_bridge":"high","brow_density":"light","lip_fullness":'
            '"medium","freckle_density":"none"}. The abstract glyph built '
            "from this vector carries one straight arc, green eye dots "
            "(#4F7942), and no freckle dots, with the model caption "
            "embedded. Any correct HLX-1 implementation fed this sequence "
            "must produce this exact vector and glyph. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The derivation follows the frozen six stages: validate, "
            "digest to 44115893398c6cd7, seed, twelve ordered draws, "
            "serialize, build the glyph. The step-by-step derivation "
            "prints each draw residue so the vector is traceable to the "
            "digest. The demonstration program replays the derivation, "
            "asserts the vector JSON equals the stated string "
            "byte-for-byte, asserts the glyph contains one straight arc, "
            "green dots, and zero freckle dots, and verifies byte-identical "
            "output across two runs."
        ),
        "key_points": [
            "HLX-0008 digests to 44115893398c6cd7 and derives the twelve-trait vector stated here.",
            "The vector JSON is asserted byte-for-byte by the demo.",
            "The glyph shows a single straight arc, green dots, and no freckle dots.",
            "Every draw residue is printed in the derivation for full traceability.",
            "The demo verifies byte-identical representations across runs.",
        ],
        "requirements": [
            "The sequence must be the exact 72-base HLX-0008 string, validated before digestion.",
            "The digest 44115893398c6cd7 must be reproduced exactly.",
            "The vector JSON must equal the stated string byte-for-byte.",
            "The glyph must carry the straight arc, green dots, zero freckle dots, and the model caption.",
            "The model label must accompany the representation wherever it is shown.",
        ],
        "standards": [
            "All HLX-1 constants and orders apply unchanged.",
            "Vector JSON uses compact separators and the fixed key order.",
            "Record text and demo output are cross-checked on sequence, digest, vector string, and glyph features.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the eighth full seal - HLX-0008's "
            "witnesses swear above-average, broad, band-5, straight, "
            "shade-4, green, 0.87, 128, high, light, medium, none. One "
            "line, green dots, an empty field where freckles would fall. "
            "A model, labeled."
        ),
    },
    {
        "key": "determinism_proof",
        "name": "The Determinism Proof: Same Sequence, Byte-Identical Representation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The determinism proof is the database's guarantee made "
            "checkable: the same sequence, run any number of times, "
            "yields the byte-identical representation. The proof input is "
            "the synthetic sequence HLX-0001 "
            "(GGAATACAGTAGCGACGCCCTAGTTGACAATCTAATCCTAGTCGTGTCTCGGCTGCG "
            "GTGCGCATGGAGAAC), digest d8c119491440887d. The pipeline runs "
            "three full times on this input - three independent "
            "executions, each starting from the raw string - and the three "
            "trait-vector JSON strings are compared byte-for-byte, as are "
            "the three SVG documents. All three pairs are identical: the "
            "vector is "
            '{"height_band":"above-average","build":"slight","skin_band":'
            '"band-2","hair_texture":"coily","hair_shade":"shade-3",'
            '"eye_color":"gray","face_width_ratio":0.91,"jaw_angle":136,'
            '"nose_bridge":"high","brow_density":"full","lip_fullness":'
            '"medium","freckle_density":"dense"} every time, and the glyph '
            "is the same document every time. The proof also runs the "
            "JavaScript pipeline from gen-*.js on the same sequence and "
            "confirms its vector and glyph match the Python outputs "
            "byte-for-byte, proving the algorithm - not the language - is "
            "what determines the result. Determinism here is not a claim; "
            "it is this procedure, runnable by anyone. This is a "
            "Signature-generated deterministic model, a stylized "
            "parametric abstraction, never a real person's appearance."
        ),
        "how_it_works": (
            "The proof works by triple execution and exact comparison. "
            "Each run validates the sequence, digests it, seeds the "
            "generator, draws twelve times, serializes the vector, and "
            "builds the glyph - with no shared state between runs. The "
            "three JSON strings must be equal as strings (not as parsed "
            "objects, so key order and formatting are checked too), and "
            "the three SVG strings must be equal as strings. The "
            "cross-language check feeds the same sequence to the "
            "gen-*.js pipeline and compares its outputs to the Python "
            "outputs with the same strictness. The demonstration program "
            "performs the triple run and the string comparisons in-"
            "process, asserting all equalities, and the build harness "
            "performs the cross-language comparison with Node.js, "
            "asserting byte-identical results."
        ),
        "key_points": [
            "Three independent runs of HLX-0001 produce byte-identical trait-vector JSON and byte-identical SVG documents.",
            "Comparisons are on the raw output strings, so key order, formatting, and every glyph coordinate are checked.",
            "The JavaScript pipeline in gen-*.js reproduces the Python outputs byte-for-byte for the same sequence.",
            "No shared state exists between runs: each execution starts from the raw sequence string.",
            "The proof is runnable by anyone - it is the guarantee made checkable, not a claim.",
        ],
        "requirements": [
            "Each proof run must start from the raw sequence string with no shared generator state.",
            "All three runs must produce the vector and glyph; all pairwise string comparisons must hold.",
            "The cross-language check must compare full output strings, not summaries.",
            "The proven vector must equal the string stated in this record.",
            "The model label must accompany the proof wherever it is shown.",
        ],
        "standards": [
            "Byte equality is the pass criterion; any single differing byte fails the proof.",
            "The proof input is the frozen HLX-0001 sequence; the expected vector is the frozen string stated here.",
            "Proof results are reported as pass/fail with the inputs identified.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT],
        "sig_lens": (
            "The Signature read: the seal is stamped three times, and the "
            "three stampings are laid side by side - identical to the "
            "pixel, to the letter. Then the seal is stamped in another "
            "tongue (JavaScript), and still it matches. That is the "
            "covenant kept in public: checkable, repeatable, sworn."
        ),
    },
    {
        "key": "sensitivity",
        "name": "The Sensitivity Check: One Base Changed, a Different Representation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The sensitivity check proves the pipeline is input-sensitive: "
            "a minimal change to the sequence produces a different "
            "representation, so the method cannot be returning a constant "
            "or ignoring its input. The base input is the synthetic "
            "sequence HLX-0002 "
            "(TCGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCT "
            "ACAGGAGATTTGAATT), digest c03bdc94dcbe9c44. Changing only its "
            "first base from T to A gives "
            "ACGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCT "
            "ACAGGAGATTTGAATT, whose digest is 009359a0508b523d - "
            "completely different, as the FNV-1a avalanche guarantees. The "
            "changed sequence derives the vector "
            '{"height_band":"average","build":"sturdy","skin_band":"band-4",'
            '"hair_texture":"straight","hair_shade":"shade-3","eye_color":'
            '"brown","face_width_ratio":0.9,"jaw_angle":111,"nose_bridge":'
            '"high","brow_density":"light","lip_fullness":"thin",'
            '"freckle_density":"sparse"} - eleven of the twelve traits '
            "differ from HLX-0002's vector (only hair_shade, shade-3, is "
            "unchanged), and the glyph is a visibly different document. "
            "One letter changed, eleven traits moved: the pipeline reads "
            "its input. This is a Signature-generated deterministic model, "
            "a stylized parametric abstraction, never a real person's "
            "appearance."
        ),
        "how_it_works": (
            "Sensitivity works through the hash avalanche. FNV-1a mixes "
            "each input byte into the full 64-bit state, so flipping the "
            "first base replaces the digest wholesale (c03bdc94dcbe9c44 "
            "becomes 009359a0508b523d), which reseeds the generator to an "
            "unrelated stream, which redraws all twelve traits. The check "
            "is deliberately minimal - one base, the smallest possible "
            "edit - because if the smallest edit moves the output, every "
            "larger edit does too. The demonstration program derives both "
            "representations, asserts the digests differ, asserts the "
            "vector JSON strings differ, counts the differing traits "
            "(eleven of twelve), asserts the glyph documents differ, and "
            "prints both vectors side by side."
        ),
        "key_points": [
            "Changing HLX-0002's first base from T to A changes the digest from c03bdc94dcbe9c44 to 009359a0508b523d.",
            "Eleven of twelve traits differ between the two derived vectors; only hair_shade (shade-3) is unchanged.",
            "The glyph documents differ as well - the change is visible, not just numeric.",
            "The avalanche comes from FNV-1a: each input byte is mixed into the full 64-bit state.",
            "The minimal one-base edit is the strongest test: if the smallest change moves the output, all larger changes do.",
        ],
        "requirements": [
            "The check must use a minimal single-base edit of a frozen database sequence.",
            "Both digests, both vectors, and both glyphs must be derived by the real pipeline, not hand-written.",
            "The demo must assert the digests differ, the vector strings differ, and the glyph strings differ.",
            "The differing-trait count (eleven of twelve) must be computed and reported by the demo.",
            "The model label must accompany both representations.",
        ],
        "standards": [
            "The edit is exactly one base changed; the rest of the 72-base string is identical.",
            "Difference is asserted on full output strings (digests, JSON, SVG), not on summaries.",
            "Record text and demo output are cross-checked on both digests and both vectors.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: change one letter of the signature and "
            "the seal changes with it - eleven witnesses speak "
            "differently, and only one holds its tongue. The covenant "
            "reads its input; it never sleeps through it. Sensitivity is "
            "the proof that the seal belongs to the signature."
        ),
    },
    {
        "key": "generator_record",
        "name": "The Generator Record: The Working Pipeline",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The generator record documents the working pipeline that "
            "ships with this database: a complete, runnable implementation "
            "of HLX-1 that takes one DNA sequence at a time and returns "
            "its deterministic representation. Two implementations carry "
            "the identical frozen algorithm. The Python implementation "
            "lives in every record's demonstration program: validate, "
            "FNV-1a digest, xorshift64* seeded from the digest, twelve "
            "draws in fixed order, compact JSON vector, abstract glyph "
            "SVG. The JavaScript implementation lives in the page "
            "generator file (gen-*.js) as the HLX-1 pipeline module: it "
            "accepts a sequence string, runs the same six stages using "
            "BigInt for exact 64-bit arithmetic, and returns the same "
            "trait-vector JSON and the same SVG document the Python code "
            "produces - byte-for-byte, as the determinism proof verifies. "
            "The generator processes exactly one sequence per call: there "
            "is no batch mode, because 'one sequence at a time' is the "
            "method's contract. Invalid input is rejected with a "
            "descriptive error, never silently repaired. Every output "
            "carries the model label: Signature-generated deterministic "
            "model, a stylized parametric abstraction, never a real "
            "person's appearance. The generator is the database's promise "
            "in executable form: feed it any valid synthetic sequence and "
            "it will derive, deterministically, the representation this "
            "database's records describe."
        ),
        "how_it_works": (
            "The generator works as a pure function of one argument: the "
            "sequence string. The Python entry point validates, digests, "
            "seeds, draws, serializes, and builds, returning a record "
            "with the model label, the sequence length, the sequence "
            "SHA-256 (for input identification, not secrecy), the FNV-1a "
            "digest, the trait vector, the vector JSON, and the SVG spec. "
            "The JavaScript entry point mirrors it exactly: same "
            "validation rules, same FNV-1a over the same bytes, same "
            "xorshift64* stream via BigInt, same draw order and moduli, "
            "same JSON key order, same SVG template with the same integer "
            "formulas. The demonstration program for this record acts as "
            "the generator's acceptance test: it runs the pipeline on a "
            "fresh synthetic sequence, prints the complete representation, "
            "asserts all twelve traits are present in order, asserts the "
            "model label is attached, and asserts two runs are "
            "byte-identical. The build harness additionally runs the "
            "JavaScript generator on the same input and asserts "
            "byte-identical outputs across languages."
        ),
        "key_points": [
            "The generator is a pure function of one sequence string: validate, digest, seed, draw twelve, serialize, build glyph.",
            "Two implementations carry the frozen algorithm: Python in the record demos, JavaScript (BigInt) in gen-*.js - verified byte-identical.",
            "Exactly one sequence per call: there is no batch mode, honoring the one-sequence-at-a-time contract.",
            "Invalid input raises a descriptive error; the generator never silently repairs.",
            "Every output carries the model label, and the demo acceptance test checks all twelve traits plus determinism.",
        ],
        "requirements": [
            "Both implementations must implement the identical six stages with identical constants, orders, and formats.",
            "The JavaScript implementation must use exact 64-bit integer arithmetic (BigInt) for the hash and generator.",
            "The generator must accept exactly one sequence per call and reject invalid input with a descriptive error.",
            "The output must include the model label, sequence length, digests, trait vector, vector JSON, and SVG spec.",
            "Cross-language byte-identity must be verified by the build harness on shared test inputs.",
        ],
        "standards": [
            "The frozen algorithm is the single source of truth; neither implementation may deviate from the pipeline record.",
            "Acceptance is byte-identity of the full outputs across runs and across languages.",
            "The generator's demo is the executable specification: it must pass for the database to ship.",
        ],
        "citations": [CIT_METHOD, CIT_FNV, CIT_XORSHIFT, CIT_LIMITS],
        "sig_lens": (
            "The Signature read: the generator is the covenant made "
            "executable - the six sworn steps, written twice (in Python "
            "and in JavaScript), keeping the same oath in both tongues. "
            "One signature in, one seal out, the label attached: the "
            "Signature's own engine, and it never mistakes a model for a "
            "person."
        ),
    },
])
