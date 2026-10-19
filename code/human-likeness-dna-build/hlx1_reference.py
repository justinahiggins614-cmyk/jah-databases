#!/usr/bin/env python3
"""HLX-1 reference implementation: synthetic DNA sequence -> deterministic
human-likeness representation. Frozen spec; mirrored in JS in gen-*.js."""
import json

MASK64 = (1 << 64) - 1
FNV_OFFSET = 14695981039346656037
FNV_PRIME = 1099511628211
M64F = 18446744073709551616.0  # 2**64

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
            raise ValueError("invalid base %r: only A, C, G, T allowed" % ch)
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
    return {
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
    }, {
        "height_idx": hi, "skin_idx": si, "texture_idx": ti,
        "eye_idx": ei, "face_q": fq, "jaw_angle": 100 + ja,
        "nose_idx": ni, "brow_idx": br, "freckle_idx": fi,
    }


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
    return "\n".join(lines)


def represent(seq):
    traits, idx = derive_traits(seq)
    vec = {k: traits[k] for k in TRAIT_ORDER}
    vec_json = json.dumps(vec, separators=(",", ":"), ensure_ascii=True)
    svg = svg_spec(seq, traits, idx)
    return {
        "model_label": MODEL_LABEL,
        "sequence_length": len(seq),
        "sequence_sha": __import__("hashlib").sha256(seq.encode("ascii")).hexdigest(),
        "digest_fnv1a64": "%016x" % fnv1a64(seq.encode("ascii")),
        "trait_vector": vec,
        "trait_vector_json": vec_json,
        "svg_spec": svg,
    }


if __name__ == "__main__":
    import random
    rnd = random.Random(20261017)
    seqs = {}
    labels = (["S%d" % i for i in range(11, 23)] +
              ["HLX-%04d" % i for i in range(1, 9)] + ["CANON"])
    for lab in labels:
        seqs[lab] = "".join(rnd.choice("ACGT") for _ in range(72))
    for lab, s in seqs.items():
        print("%s %s" % (lab, s))
    print("=" * 70)
    for lab, s in seqs.items():
        r = represent(s)
        print("%s digest=%s" % (lab, r["digest_fnv1a64"]))
        print("%s vector=%s" % (lab, r["trait_vector_json"]))
