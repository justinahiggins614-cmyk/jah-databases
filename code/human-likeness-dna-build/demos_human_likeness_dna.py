#!/usr/bin/env python3
"""Demo programs for the Human Likeness DNA databases.

Every demo is real, runnable, stdlib-only Python implementing the frozen
HLX-1 deterministic pipeline (embedded verbatim in each program so the
record's demo is self-contained): validate, FNV-1a 64-bit digest,
xorshift64* seeded from the digest, twelve trait draws in fixed order,
compact JSON trait vector, abstract glyph SVG spec. All are machine-executed
by build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality - geometry parameters are compared as formatted
strings or integers), and ends with the OK marker. Cross-checks: the frozen
expected values asserted here are the values stated in
entries_human_likeness_dna.py, computed by the reference implementation.
"""

import json as _json

_HLX1_SRC = '''\
import hashlib
import json
MASK64 = (1 << 64) - 1
FNV_OFFSET = 14695981039346656037
FNV_PRIME = 1099511628211
HEIGHT = ["compact", "below-average", "average", "above-average", "tall"]
BUILD = ["slight", "lean", "sturdy", "broad"]
HAIR_TEX = ["straight", "wavy", "curly", "coily"]
EYE = ["brown", "hazel", "green", "blue", "gray", "amber"]
NOSE = ["low", "medium", "high"]
BROW = ["light", "medium", "full"]
LIP = ["thin", "medium", "full"]
FRECKLE = ["none", "sparse", "moderate", "dense"]
EYE_HEX = {"brown": "#6B4226", "hazel": "#8A6D3B", "green": "#4F7942",
           "blue": "#3B6EA5", "gray": "#7D7D7D", "amber": "#B8860B"}
TRAIT_ORDER = ["height_band", "build", "skin_band", "hair_texture",
               "hair_shade", "eye_color", "face_width_ratio", "jaw_angle",
               "nose_bridge", "brow_density", "lip_fullness", "freckle_density"]
MODEL_LABEL = ("Signature-generated deterministic model - a stylized "
               "parametric abstraction. Never a real person's appearance.")
def validate(seq):
    if not isinstance(seq, str) or not seq:
        raise ValueError("sequence must be a non-empty string")
    if len(seq) < 16:
        raise ValueError("sequence too short (minimum 16 bases)")
    if len(seq) > 4096:
        raise ValueError("sequence too long (maximum 4096 bases)")
    for ch in seq:
        if ch not in "ACGT":
            raise ValueError("invalid base: only A, C, G, T allowed")
    return seq
def fnv1a64(data):
    h = FNV_OFFSET
    for b in data:
        h ^= b
        h = (h * FNV_PRIME) & MASK64
    return h
class Rng:
    def __init__(self, seed):
        self.s = (seed & MASK64) or 0x9E3779B97F4A7C15
    def next64(self):
        x = self.s
        x ^= (x >> 12)
        x &= MASK64
        x ^= (x << 25) & MASK64
        x ^= (x >> 27)
        self.s = x & MASK64
        return (self.s * 2685821657736338717) & MASK64
    def int(self, n):
        return self.next64() % n
def derive_traits(seq):
    validate(seq)
    rng = Rng(fnv1a64(seq.encode("ascii")))
    hi = rng.int(5); bi = rng.int(4); si = rng.int(6); ti = rng.int(4)
    sh = rng.int(6); ei = rng.int(6); fq = rng.int(21); ja = rng.int(41)
    ni = rng.int(3); br = rng.int(3); li = rng.int(3); fi = rng.int(4)
    traits = {
        "height_band": HEIGHT[hi],
        "build": BUILD[bi],
        "skin_band": "band-%d" % (si + 1),
        "hair_texture": HAIR_TEX[ti],
        "hair_shade": "shade-%d" % (sh + 1),
        "eye_color": EYE[ei],
        "face_width_ratio": (72 + fq) / 100.0,
        "jaw_angle": 100 + ja,
        "nose_bridge": NOSE[ni],
        "brow_density": BROW[br],
        "lip_fullness": LIP[li],
        "freckle_density": FRECKLE[fi],
    }
    idx = {"height_idx": hi, "skin_idx": si, "texture_idx": ti,
           "eye_idx": ei, "face_q": fq, "jaw_angle": 100 + ja,
           "nose_idx": ni, "brow_idx": br, "freckle_idx": fi}
    return traits, idx
def svg_spec(seq, traits, idx):
    bg_hue = (idx["skin_idx"] * 47 + idx["height_idx"] * 23) % 360
    disc_r = 52 + idx["face_q"]
    disc_hue = (bg_hue + 180) % 360
    jaw_h = 20 + (idx["jaw_angle"] - 100)
    nose_h = 20 + idx["nose_idx"] * 15
    brow_h = 20 + idx["brow_idx"] * 15
    n_arcs = idx["texture_idx"] + 1
    n_freck = idx["freckle_idx"] * 5
    eye_hex = EYE_HEX[traits["eye_color"]]
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">',
        '<rect width="240" height="240" fill="hsl(%d,45%%,88%%)"/>' % bg_hue,
        '<circle cx="120" cy="112" r="%d" fill="hsl(%d,40%%,72%%)" stroke="#333333" stroke-width="2"/>' % (disc_r, disc_hue),
        '<rect x="56" y="%d" width="18" height="%d" fill="#555555"/>' % (214 - jaw_h, jaw_h),
        '<rect x="86" y="%d" width="18" height="%d" fill="#777777"/>' % (214 - nose_h, nose_h),
        '<rect x="116" y="%d" width="18" height="%d" fill="#999999"/>' % (214 - brow_h, brow_h),
    ]
    top = 112 - disc_r - 8
    for a in range(n_arcs):
        y = top - a * 9
        style = idx["texture_idx"]
        if style == 0:
            d = "M %d %d L %d %d" % (120 - disc_r, y, 120 + disc_r, y)
        elif style == 1:
            d = "M %d %d Q %d %d %d %d" % (120 - disc_r, y, 120, y - 10, 120 + disc_r, y)
        elif style == 2:
            d = "M %d %d Q %d %d %d %d Q %d %d %d %d" % (
                120 - disc_r, y, 120 - disc_r // 2, y - 12, 120, y,
                120 + disc_r // 2, y + 12, 120 + disc_r, y)
        else:
            d = "M %d %d L %d %d L %d %d L %d %d" % (
                120 - disc_r, y, 120 - disc_r // 3, y - 10,
                120 + disc_r // 3, y + 10, 120 + disc_r, y)
        lines.append('<path d="%s" stroke="#222222" stroke-width="2" fill="none"/>' % d)
    lines.append('<circle cx="104" cy="106" r="6" fill="%s"/>' % eye_hex)
    lines.append('<circle cx="136" cy="106" r="6" fill="%s"/>' % eye_hex)
    for f in range(n_freck):
        fx = 84 + (f * 37) % 72
        fy = 96 + (f * 53) % 40
        lines.append('<circle cx="%d" cy="%d" r="1.6" fill="#4a3220"/>' % (fx, fy))
    lines.append('<text x="120" y="232" text-anchor="middle" font-size="8" fill="#333333">'
                 'HLX-1 abstract glyph - deterministic model, not a person</text>')
    lines.append('</svg>')
    return "\\n".join(lines)
def represent(seq):
    traits, idx = derive_traits(seq)
    vec = {k: traits[k] for k in TRAIT_ORDER}
    vec_json = json.dumps(vec, separators=(",", ":"), ensure_ascii=True)
    return {
        "model_label": MODEL_LABEL,
        "sequence_length": len(seq),
        "sequence_sha": hashlib.sha256(seq.encode("ascii")).hexdigest(),
        "digest_fnv1a64": "%016x" % fnv1a64(seq.encode("ascii")),
        "trait_vector": vec,
        "trait_vector_json": vec_json,
        "svg_spec": svg_spec(seq, traits, idx),
    }
'''

CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
CANON_VEC = ('{"height_band":"average","build":"lean","skin_band":"band-3",'
             '"hair_texture":"wavy","hair_shade":"shade-4","eye_color":"amber",'
             '"face_width_ratio":0.92,"jaw_angle":119,"nose_bridge":"high",'
             '"brow_density":"medium","lip_fullness":"thin",'
             '"freckle_density":"dense"}')


def _mk(hdr, name, rid, group, body):
    return hdr(name, rid, group) + _HLX1_SRC + body.replace("NAME", _json.dumps(name))


def demo_hldn_what_is(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
def main():
    r = represent(CANON)
    print("sequence length:", r["sequence_length"])
    print("digest:", r["digest_fnv1a64"])
    print("trait vector:", r["trait_vector_json"])
    print("svg bytes:", len(r["svg_spec"]))
    assert r["sequence_length"] == 72
    assert len(r["trait_vector"]) == 12
    assert list(r["trait_vector"].keys()) == TRAIT_ORDER
    assert "never a real person's appearance" in r["model_label"].lower()
    assert r["svg_spec"].startswith("<svg")
    print("model label:", r["model_label"][:60] + "...")
    print("OK: %s derived the full likeness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_pipeline(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
EXPECTED_DRAWS = [2, 1, 2, 1, 3, 5, 20, 19, 2, 1, 0, 3]
EXPECTED_VEC = '{"height_band":"average","build":"lean","skin_band":"band-3","hair_texture":"wavy","hair_shade":"shade-4","eye_color":"amber","face_width_ratio":0.92,"jaw_angle":119,"nose_bridge":"high","brow_density":"medium","lip_fullness":"thin","freckle_density":"dense"}'
def main():
    validate(CANON)
    print("stage 1 validate: pass (72 ACGT bases)")
    digest = fnv1a64(CANON.encode("ascii"))
    print("stage 2 digest: %016x" % digest)
    assert "%016x" % digest == "74fef976f58549f1"
    rng = Rng(digest)
    moduli = [5, 4, 6, 4, 6, 6, 21, 41, 3, 3, 3, 4]
    draws = [rng.int(m) for m in moduli]
    print("stage 3-4 draws:", draws)
    assert draws == EXPECTED_DRAWS, "draw mismatch"
    for tname, d, m in zip(TRAIT_ORDER, draws, moduli):
        print("  draw %-16s %2d of %-2d" % (tname, d, m))
    r = represent(CANON)
    print("stage 5 vector:", r["trait_vector_json"])
    assert r["trait_vector_json"] == EXPECTED_VEC, "vector mismatch"
    print("stage 6 svg bytes:", len(r["svg_spec"]))
    assert "not a person" in r["svg_spec"]
    print("OK: %s replayed all six stages" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_seq_basics(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
def main():
    validate(CANON)
    counts = {b: CANON.count(b) for b in "ACGT"}
    print("length:", len(CANON))
    for b in "ACGT":
        print("  base %s: %d" % (b, counts[b]))
    assert len(CANON) == 72
    assert counts == {"A": 19, "C": 14, "G": 21, "T": 18}, counts
    gc = (counts["G"] + counts["C"]) / len(CANON) * 100.0
    print("GC content: %.1f %%" % gc)
    assert 48.5 < gc < 48.7
    digest = "%016x" % fnv1a64(CANON.encode("ascii"))
    print("digest:", digest)
    assert digest == "74fef976f58549f1"
    print("OK: %s read the canonical sequence" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_seeded_randomness(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
def main():
    d0 = fnv1a64(b"")
    print("fnv1a64(empty) = %d" % d0)
    assert d0 == 14695981039346656037, "FNV offset basis known-answer failed"
    da = "%016x" % fnv1a64(b"a")
    print("fnv1a64('a') = %s" % da)
    assert da == "af63dc4c8601ec8c", "FNV 'a' known-answer failed"
    r1, r2 = Rng(123456789), Rng(123456789)
    s1 = [r1.int(1000) for _ in range(5)]
    s2 = [r2.int(1000) for _ in range(5)]
    print("seed 123456789 stream:", s1)
    assert s1 == s2, "same seed must replay the same stream"
    r3 = Rng(987654321)
    s3 = [r3.int(1000) for _ in range(5)]
    assert s3 != s1, "different seed must give a different stream"
    r0 = Rng(0)
    w = r0.next64()
    print("zero-seed first word:", w)
    assert w != 0, "zero seed must be remapped"
    print("OK: %s proved seeded replay" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_reading_sequence(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
def main():
    seq = validate(CANON)
    print("validated: %d bases, ACGT-only" % len(seq))
    assert len(seq) == 72
    a, c, g, t = (seq.count(b) for b in "ACGT")
    print("A=%d C=%d G=%d T=%d" % (a, c, g, t))
    assert (a, c, g, t) == (19, 14, 21, 18)
    gc = (g + c) / len(seq) * 100.0
    print("GC%%: %.1f" % gc)
    assert 48.5 < gc < 48.7
    print("digest: %016x" % fnv1a64(seq.encode("ascii")))
    assert "%016x" % fnv1a64(seq.encode("ascii")) == "74fef976f58549f1"
    print("synthetic: yes - composed illustration, no biological meaning")
    print("OK: %s read the sequence exactly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_vector(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
def main():
    r = represent(CANON)
    vec = r["trait_vector"]
    print("trait count:", len(vec))
    assert len(vec) == 12
    assert list(vec.keys()) == TRAIT_ORDER, "key order drift"
    for k in TRAIT_ORDER:
        print("  %-16s %s" % (k, vec[k]))
    print("json:", r["trait_vector_json"])
    assert r["trait_vector_json"] == ('{"height_band":"average","build":"lean",'
        '"skin_band":"band-3","hair_texture":"wavy","hair_shade":"shade-4",'
        '"eye_color":"amber","face_width_ratio":0.92,"jaw_angle":119,'
        '"nose_bridge":"high","brow_density":"medium","lip_fullness":"thin",'
        '"freckle_density":"dense"}')
    assert "%.2f" % vec["face_width_ratio"] == "0.92"
    assert vec["jaw_angle"] == 119
    print("OK: %s checked all twelve traits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_abstract_svg(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
def main():
    a = represent(CANON)
    b = represent(CANON)
    assert a["svg_spec"] == b["svg_spec"], "glyph not byte-identical"
    svg = a["svg_spec"]
    print("svg bytes:", len(svg))
    assert svg.startswith("<svg")
    assert svg.rstrip().endswith("</svg>")
    assert "not a person" in svg, "model caption missing"
    assert "photoreal" not in svg.lower()
    print("caption present: deterministic model, not a person")
    print("paths (hair arcs):", svg.count("<path"))
    print("eye dots:", svg.count('r="6"'))
    print("freckle dots:", svg.count('fill="#4a3220"'))
    assert svg.count("<path") == 2, "wavy texture must draw 2 arcs"
    assert svg.count('fill="#4a3220"') == 15, "dense freckle must draw 15 dots"
    print("OK: %s built the abstract glyph" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_limits(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
LIMITS = [
    "does not predict real traits from real DNA - bands are illustrative model bands",
    "no representation depicts or resembles any real person - all sequences synthetic",
    "the glyph is an abstract geometric seal, never a portrait",
    "determinism guarantees repeatability, not truth about the input",
    "FNV-1a is not cryptographic - digests are not secrets, representations are not identifiers",
]
def main():
    r = represent(CANON)
    print("the five limits:")
    for i, lim in enumerate(LIMITS, 1):
        print("  %d. %s" % (i, lim))
    assert "never a real person's appearance" in r["model_label"].lower()
    assert "not a person" in r["svg_spec"]
    blob = (r["trait_vector_json"] + r["svg_spec"]).lower()
    assert "predict" not in blob and "real person" not in blob
    print("model label attached:", r["model_label"][:50] + "...")
    print("OK: %s stated the limits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_hygiene(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
def expect_reject(seq, why):
    try:
        validate(seq)
    except ValueError as e:
        print("  rejected (%s): %s" % (why, e))
        return
    raise AssertionError("should have rejected: %s" % why)
def main():
    print("adversarial validation:")
    expect_reject("", "empty string")
    expect_reject("acgtacgtacgtacgt", "lowercase letters")
    expect_reject("ACGTACGTACGTACGN", "ambiguous base N")
    expect_reject("ACGT ACGTACGTACGT", "whitespace inside")
    expect_reject("ACGTACGTACGTACG", "15 bases - too short")
    expect_reject("A" * 4097, "4097 bases - too long")
    print("boundary acceptance:")
    assert validate("A" * 16) == "A" * 16
    print("  16 bases accepted (minimum)")
    assert validate("T" * 4096) == "T" * 4096
    print("  4096 bases accepted (maximum)")
    print("OK: %s kept the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_verification(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
CANON = "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC"
def main():
    runs = [represent(CANON) for _ in range(3)]
    j0, s0 = runs[0]["trait_vector_json"], runs[0]["svg_spec"]
    for i, r in enumerate(runs[1:], 2):
        assert r["trait_vector_json"] == j0, "run %d vector differs" % i
        assert r["svg_spec"] == s0, "run %d svg differs" % i
    print("3 runs: trait-vector JSON byte-identical (%d bytes)" % len(j0))
    print("3 runs: SVG document byte-identical (%d bytes)" % len(s0))
    flipped = "T" + CANON[1:]
    rf = represent(flipped)
    assert rf["trait_vector_json"] != j0, "one-base change must differ"
    assert rf["svg_spec"] != s0, "one-base change must differ in glyph"
    print("one-base flip: digest %s -> %s (differ)" % (
        runs[0]["digest_fnv1a64"], rf["digest_fnv1a64"]))
    print("OK: %s verified determinism" % NAME)
if __name__ == "__main__":
    main()
''')

def _single(hdr, name, rid, group, seq, digest, trait_key, expected, extra_checks=""):
    return _mk(hdr, name, rid, group, '''\
SEQ = "%s"
def main():
    r = represent(SEQ)
    print("sequence length:", r["sequence_length"])
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "%s", "digest mismatch"
    val = r["trait_vector"]["%s"]
    shown = ("%%.2f" %% val) if isinstance(val, float) else str(val)
    print("derived %s: %%s" %% "%s", shown)
    assert shown == "%s", "trait mismatch"
%s
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"], "not deterministic"
    assert b["svg_spec"] == r["svg_spec"], "glyph not deterministic"
    print("two runs: byte-identical")
    print("OK: %%s derived the trait" %% NAME)
if __name__ == "__main__":
    main()
''' % (seq, digest, trait_key, trait_key, expected, expected, extra_checks))


def demo_hldn_trait_height(hdr, name, rid, group, points, req):
    return _single(hdr, name, rid, group,
        "GATCATGCTTACCCGGTCAGCAAGGTGTTCCGGGTGTGGACCGTTAGGGCGTTACTAGTTGCAATCGATCAC",
        "363b837dee6794ba", "height_band", "compact")


def demo_hldn_trait_build(hdr, name, rid, group, points, req):
    return _single(hdr, name, rid, group,
        "TCATAACTTAACGAAACAAATTGCGTGTATTGTGAATCCCCTGAAATAGTTACATGTCCTAGGTTTGTTTTC",
        "aa10da6c11084d7d", "build", "slight")


def demo_hldn_trait_skin(hdr, name, rid, group, points, req):
    return _single(hdr, name, rid, group,
        "GTATGAATGGGGTTTTGACCGAATTGCTGATTTTTTGTCTCAGCTCCTGCTTTCTGGTGATGTTTACTATAT",
        "064e602defd1feeb", "skin_band", "band-3")


def demo_hldn_trait_hair_texture(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "ATTGCACTTATACCTGTACTGTAGTCTGTAATGTCACAGTACTGGGCGGCGAAATACCCTTTGCTAACAAAT"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "b4a2003bd79d1455"
    tex = r["trait_vector"]["hair_texture"]
    print("derived hair_texture:", tex)
    assert tex == "coily"
    svg = r["svg_spec"]
    print("hair arcs:", svg.count("<path"))
    assert svg.count("<path") == 4, "coily must draw 4 arcs"
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_hair_shade(hdr, name, rid, group, points, req):
    return _single(hdr, name, rid, group,
        "TGGTCGCGTGGCCTTATGGACAAATTACCGCGGACATGAGGGCCGTTTCCAACGAGAAACCACCGAACGTCT",
        "6b58c69a680501c3", "hair_shade", "shade-4")


def demo_hldn_trait_eye(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "GTTTCTTTTTTATCGCCTACTTCTCACACCGGTGCCCGTGAATCGAGCTCGTCGACTTATTTCTACGACCGG"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "0ae12ade81cab08a"
    eye = r["trait_vector"]["eye_color"]
    print("derived eye_color:", eye)
    assert eye == "amber"
    svg = r["svg_spec"]
    print("amber dots:", svg.count("#B8860B"))
    assert svg.count("#B8860B") == 2, "two eye dots must carry the amber hex"
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_face_ratio(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "GTTTCCTGGCAAGTGGTGCAAATAGAGTGTAGGTGAATGCGACACCTAGTTGCTACGACTTTAGATAAAAAG"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "bf76eceda54d7a06"
    ratio = r["trait_vector"]["face_width_ratio"]
    shown = "%.2f" % ratio
    print("derived face_width_ratio:", shown)
    assert shown == "0.73", "ratio mismatch"
    svg = r["svg_spec"]
    assert 'r="53"' in svg, "disc radius must be 52 + step(1) = 53"
    print("disc radius 53 confirmed in glyph")
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_jaw(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "GGCACTGATTGCTTGGGCACCTATCCTAGAGACAGTGCTAATACAGGAAGTCGATCTCTAGTATAACGCCAA"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "c9864991eb3b86d6"
    jaw = r["trait_vector"]["jaw_angle"]
    print("derived jaw_angle:", jaw)
    assert jaw == 135, "jaw mismatch"
    svg = r["svg_spec"]
    assert 'height="55"' in svg, "first trait bar must be 20 + 35 = 55"
    print("first trait bar height 55 confirmed in glyph")
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_nose(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "GAGGCTGCTAATCAACACGTACTTGAGTGACATGTCCTTCCTATCCCAATAAGAAGTCACGTCCCGCTAGAT"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "4cd305f0adea65f1"
    nose = r["trait_vector"]["nose_bridge"]
    print("derived nose_bridge:", nose)
    assert nose == "medium"
    svg = r["svg_spec"]
    assert 'height="35"' in svg, "second trait bar must be 20 + 1*15 = 35"
    print("second trait bar height 35 confirmed in glyph")
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_brow(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "CCATTCCCAGTTTAAGACGTGATGCCGGGATTGCGCTGAAGTGGGCGGAGGTTAGGGTGGAGAAGAGGGTCG"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "bd8809d566b3de88"
    brow = r["trait_vector"]["brow_density"]
    print("derived brow_density:", brow)
    assert brow == "medium"
    svg = r["svg_spec"]
    assert 'x="116" y="179" width="18" height="35"' in svg, \
        "third trait bar (brow, medium) must be 35 tall at y=179"
    print("third trait bar height 35 confirmed in glyph")
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_trait_lip(hdr, name, rid, group, points, req):
    return _single(hdr, name, rid, group,
        "ATACTTACAGCAGAATATTTGGAACCTGATTAGAATTTGGCTATTACAAAGTACCTGTCCCCTAGGAATCGC",
        "9e28fda1a42eeea2", "lip_fullness", "thin")


def demo_hldn_trait_freckle(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "TCTTGCTCGACACCGTGCGCAACCTTAGTGCGGCCTATGTGCGTCTAAGCCGGCCGGGCTCTCTACTCCCAA"
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "fac04fb523dc8bae"
    fr = r["trait_vector"]["freckle_density"]
    print("derived freckle_density:", fr)
    assert fr == "dense"
    svg = r["svg_spec"]
    dots = svg.count('fill="#4a3220"')
    print("freckle dots:", dots)
    assert dots == 15, "dense must draw 15 dots"
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s derived the trait" % NAME)
if __name__ == "__main__":
    main()
''')

def _full(hdr, name, rid, group, seq, digest, vec, arcs, eye_hex, freckles):
    return _mk(hdr, name, rid, group, '''\
SEQ = "%s"
EXPECTED_VEC = '%s'
def main():
    r = represent(SEQ)
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == "%s", "digest mismatch"
    print("vector:", r["trait_vector_json"])
    assert r["trait_vector_json"] == EXPECTED_VEC, "vector mismatch"
    svg = r["svg_spec"]
    print("hair arcs:", svg.count("<path"), "| eye hex hits:", svg.count("%s"),
          "| freckle dots:", svg.count('fill="#4a3220"'))
    assert svg.count("<path") == %d, "arc count mismatch"
    assert svg.count("%s") == 2, "eye dot hex mismatch"
    assert svg.count('fill="#4a3220"') == %d, "freckle dot mismatch"
    assert "not a person" in svg, "model caption missing"
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %%s completed the full derivation" %% NAME)
if __name__ == "__main__":
    main()
''' % (seq, vec, digest, eye_hex, arcs, eye_hex, freckles))


def demo_hldn_combining_traits(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "GGCAGCCTACCCGCCGCCTGTTGCGGTAAGTCTGGATAGGGCGTAAGAGGAACCGATCCCCAGCAAATAGTC"
EXPECTED_VEC = '{"height_band":"below-average","build":"slight","skin_band":"band-6","hair_texture":"curly","hair_shade":"shade-4","eye_color":"gray","face_width_ratio":0.79,"jaw_angle":100,"nose_bridge":"high","brow_density":"full","lip_fullness":"medium","freckle_density":"moderate"}'
def main():
    print("stage 1 validate...")
    validate(SEQ)
    print("stage 2 digest: %016x" % fnv1a64(SEQ.encode("ascii")))
    assert "%016x" % fnv1a64(SEQ.encode("ascii")) == "8cdeab169331fbd3"
    r = represent(SEQ)
    print("stages 3-5 vector:", r["trait_vector_json"])
    assert r["trait_vector_json"] == EXPECTED_VEC, "vector mismatch"
    print("stage 6 svg bytes:", len(r["svg_spec"]))
    assert r["svg_spec"].startswith("<svg")
    assert "not a person" in r["svg_spec"]
    b = represent(SEQ)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    print("OK: %s combined all traits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_full_a(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "GGAATACAGTAGCGACGCCCTAGTTGACAATCTAATCCTAGTCGTGTCTCGGCTGCGGTGCGCATGGAGAAC",
        "d8c119491440887d",
        '{"height_band":"above-average","build":"slight","skin_band":"band-2","hair_texture":"coily","hair_shade":"shade-3","eye_color":"gray","face_width_ratio":0.91,"jaw_angle":136,"nose_bridge":"high","brow_density":"full","lip_fullness":"medium","freckle_density":"dense"}',
        4, "#7D7D7D", 15)


def demo_hldn_full_b(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "TCGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCTACAGGAGATTTGAATT",
        "c03bdc94dcbe9c44",
        '{"height_band":"compact","build":"slight","skin_band":"band-3","hair_texture":"curly","hair_shade":"shade-3","eye_color":"hazel","face_width_ratio":0.74,"jaw_angle":115,"nose_bridge":"medium","brow_density":"medium","lip_fullness":"full","freckle_density":"none"}',
        3, "#8A6D3B", 0)


def demo_hldn_full_c(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "GGCAGCCTACCCGCCGCCTGTTGCGGTAAGTCTGGATAGGGCGTAAGAGGAACCGATCCCCAGCAAATAGTC",
        "8cdeab169331fbd3",
        '{"height_band":"below-average","build":"slight","skin_band":"band-6","hair_texture":"curly","hair_shade":"shade-4","eye_color":"gray","face_width_ratio":0.79,"jaw_angle":100,"nose_bridge":"high","brow_density":"full","lip_fullness":"medium","freckle_density":"moderate"}',
        3, "#7D7D7D", 10)


def demo_hldn_full_d(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "GGACAAGCGGATGAGTTATTGGGCGAGGCAAAGGAGTCGTGTTCTGCTTCGTCGAATCCTGAATGATGGTCA",
        "dacd55d950badd37",
        '{"height_band":"average","build":"broad","skin_band":"band-2","hair_texture":"curly","hair_shade":"shade-1","eye_color":"blue","face_width_ratio":0.77,"jaw_angle":107,"nose_bridge":"high","brow_density":"light","lip_fullness":"full","freckle_density":"moderate"}',
        3, "#3B6EA5", 10)


def demo_hldn_full_e(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "GGGTAAGATTACTAGATAAATCAGAAATCCTAGATCACAAATCTCGCAAATGTATAAACGCGAACGTGGAGG",
        "0069aa1e41547c6a",
        '{"height_band":"average","build":"slight","skin_band":"band-5","hair_texture":"wavy","hair_shade":"shade-1","eye_color":"blue","face_width_ratio":0.9,"jaw_angle":101,"nose_bridge":"high","brow_density":"full","lip_fullness":"thin","freckle_density":"sparse"}',
        2, "#3B6EA5", 5)


def demo_hldn_full_f(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "CCTAGGGCTCAGCCAAGTTAGCAGTTTTGAAGTTCTGGCTGCCCCGAGTATTGCCACGGATCACATGTCACC",
        "eaddb986e196d23d",
        '{"height_band":"compact","build":"broad","skin_band":"band-2","hair_texture":"straight","hair_shade":"shade-5","eye_color":"gray","face_width_ratio":0.78,"jaw_angle":125,"nose_bridge":"medium","brow_density":"full","lip_fullness":"thin","freckle_density":"sparse"}',
        1, "#7D7D7D", 5)


def demo_hldn_full_g(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "ACGGGACAGCGACGTGAGCTAGTAGGTTTATGCGATTCGGCAATGTCAGGCGAGGTGTGTAAACCCCTAAGA",
        "baeb1e73f11301fa",
        '{"height_band":"above-average","build":"sturdy","skin_band":"band-1","hair_texture":"wavy","hair_shade":"shade-6","eye_color":"gray","face_width_ratio":0.86,"jaw_angle":124,"nose_bridge":"high","brow_density":"light","lip_fullness":"medium","freckle_density":"sparse"}',
        2, "#7D7D7D", 5)


def demo_hldn_full_h(hdr, name, rid, group, points, req):
    return _full(hdr, name, rid, group,
        "CTAACAAATCATCGCTTTATACAACTCTGCTGGACCGTCGACAGCCAAAGACCAACAAGAGGAATTATCCGC",
        "44115893398c6cd7",
        '{"height_band":"above-average","build":"broad","skin_band":"band-5","hair_texture":"straight","hair_shade":"shade-4","eye_color":"green","face_width_ratio":0.87,"jaw_angle":128,"nose_bridge":"high","brow_density":"light","lip_fullness":"medium","freckle_density":"none"}',
        1, "#4F7942", 0)


def demo_hldn_determinism_proof(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "GGAATACAGTAGCGACGCCCTAGTTGACAATCTAATCCTAGTCGTGTCTCGGCTGCGGTGCGCATGGAGAAC"
EXPECTED_VEC = '{"height_band":"above-average","build":"slight","skin_band":"band-2","hair_texture":"coily","hair_shade":"shade-3","eye_color":"gray","face_width_ratio":0.91,"jaw_angle":136,"nose_bridge":"high","brow_density":"full","lip_fullness":"medium","freckle_density":"dense"}'
def main():
    runs = [represent(SEQ) for _ in range(3)]
    print("digest:", runs[0]["digest_fnv1a64"])
    assert runs[0]["digest_fnv1a64"] == "d8c119491440887d"
    for i, r in enumerate(runs):
        assert r["trait_vector_json"] == EXPECTED_VEC, "run %d vector mismatch" % (i + 1)
    j0 = runs[0]["trait_vector_json"]
    s0 = runs[0]["svg_spec"]
    for i, r in enumerate(runs[1:], 2):
        assert r["trait_vector_json"] == j0, "run %d vector differs" % i
        assert r["svg_spec"] == s0, "run %d svg differs" % i
    print("3 independent runs: vector JSON byte-identical (%d bytes)" % len(j0))
    print("3 independent runs: SVG byte-identical (%d bytes)" % len(s0))
    print("OK: %s proved determinism" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_sensitivity(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
SEQ = "TCGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCTACAGGAGATTTGAATT"
FLIP = "ACGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCTACAGGAGATTTGAATT"
def main():
    a = represent(SEQ)
    b = represent(FLIP)
    print("original digest:", a["digest_fnv1a64"])
    print("flipped  digest:", b["digest_fnv1a64"])
    assert a["digest_fnv1a64"] == "c03bdc94dcbe9c44"
    assert b["digest_fnv1a64"] == "009359a0508b523d"
    assert a["digest_fnv1a64"] != b["digest_fnv1a64"]
    assert a["trait_vector_json"] != b["trait_vector_json"]
    assert a["svg_spec"] != b["svg_spec"]
    va, vb = a["trait_vector"], b["trait_vector"]
    diff = [k for k in va if va[k] != vb[k]]
    print("differing traits: %d of 12" % len(diff))
    for k in diff:
        print("  %-16s %s -> %s" % (k, va[k], vb[k]))
    assert len(diff) == 11, "expected 11 differing traits"
    same = [k for k in va if va[k] == vb[k]]
    assert same == ["hair_shade"], same
    print("unchanged trait: hair_shade (shade-3)")
    print("OK: %s proved sensitivity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hldn_generator_record(hdr, name, rid, group, points, req):
    return _mk(hdr, name, rid, group, '''\
FRESH = "ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT"
EXPECTED_DIGEST = "3f789625c4334a05"
EXPECTED_VEC = '{"height_band":"tall","build":"slight","skin_band":"band-4","hair_texture":"wavy","hair_shade":"shade-3","eye_color":"amber","face_width_ratio":0.92,"jaw_angle":123,"nose_bridge":"high","brow_density":"light","lip_fullness":"thin","freckle_density":"moderate"}'
def main():
    r = represent(FRESH)
    print("input: one 64-base synthetic sequence")
    print("digest:", r["digest_fnv1a64"])
    assert r["digest_fnv1a64"] == EXPECTED_DIGEST
    print("vector:", r["trait_vector_json"])
    assert r["trait_vector_json"] == EXPECTED_VEC
    assert list(r["trait_vector"].keys()) == TRAIT_ORDER, "twelve traits in order"
    assert "never a real person's appearance" in r["model_label"].lower()
    assert "not a person" in r["svg_spec"]
    print("svg bytes:", len(r["svg_spec"]))
    b = represent(FRESH)
    assert b["trait_vector_json"] == r["trait_vector_json"]
    assert b["svg_spec"] == r["svg_spec"]
    print("two runs: byte-identical")
    try:
        represent("ACGT")
        raise AssertionError("short input must be rejected")
    except ValueError as e:
        print("invalid input rejected:", e)
    print("OK: %s acceptance-tested the generator" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_hldn_what_is,
    "pipeline": demo_hldn_pipeline,
    "seq_basics": demo_hldn_seq_basics,
    "seeded_randomness": demo_hldn_seeded_randomness,
    "reading_sequence": demo_hldn_reading_sequence,
    "trait_vector": demo_hldn_trait_vector,
    "abstract_svg": demo_hldn_abstract_svg,
    "limits": demo_hldn_limits,
    "hygiene": demo_hldn_hygiene,
    "verification": demo_hldn_verification,
    "trait_height": demo_hldn_trait_height,
    "trait_build": demo_hldn_trait_build,
    "trait_skin": demo_hldn_trait_skin,
    "trait_hair_texture": demo_hldn_trait_hair_texture,
    "trait_hair_shade": demo_hldn_trait_hair_shade,
    "trait_eye": demo_hldn_trait_eye,
    "trait_face_ratio": demo_hldn_trait_face_ratio,
    "trait_jaw": demo_hldn_trait_jaw,
    "trait_nose": demo_hldn_trait_nose,
    "trait_brow": demo_hldn_trait_brow,
    "trait_lip": demo_hldn_trait_lip,
    "trait_freckle": demo_hldn_trait_freckle,
    "combining_traits": demo_hldn_combining_traits,
    "full_a": demo_hldn_full_a,
    "full_b": demo_hldn_full_b,
    "full_c": demo_hldn_full_c,
    "full_d": demo_hldn_full_d,
    "full_e": demo_hldn_full_e,
    "full_f": demo_hldn_full_f,
    "full_g": demo_hldn_full_g,
    "full_h": demo_hldn_full_h,
    "determinism_proof": demo_hldn_determinism_proof,
    "sensitivity": demo_hldn_sensitivity,
    "generator_record": demo_hldn_generator_record,
}
