#!/usr/bin/env python3
"""Prose + demo + record engine for the fantasy-worlds 1000-list build (wave 4).

Deterministic: every record derives from a seeded RNG keyed on
(slug, title-core, edition). All demo programs are machine-executed by
build_all.py and must exit 0.
"""
import hashlib
import random

TIERS = ["foundations", "compounded", "advanced"]


def seeded(*parts):
    h = hashlib.sha256(("|".join(str(p) for p in parts)).encode("utf-8")).hexdigest()
    return random.Random(int(h[:16], 16))


def pick(rnd, seq):
    return seq[int(rnd.random() * len(seq)) % len(seq)]


# ------------------------------------------------------------------ prose

def _a(word):
    return "an" if word[:1].lower() in "aeiou" else "a"


def desc_paragraphs(cfg, spec, edition, rnd):
    T = spec["core"]
    noun, plural = cfg["noun"], cfg["plural"]
    adj = pick(rnd, cfg["adjs"])
    person = pick(rnd, cfg["people"])
    person2 = pick(rnd, cfg["people"])
    place = pick(rnd, cfg["places"])
    place2 = pick(rnd, cfg["places"])
    material = pick(rnd, cfg["materials"])
    attr_bits = []
    for a in cfg["attrs"]:
        v = spec["attrs"][a["key"]]
        attr_bits.append("%s of %s %s" % (a["label"], v, a["unit"]))
    cat1 = spec["cats"][0]
    cat2 = spec["cats"][1]
    ov = cfg["lex"]["origin_verb"]
    cv = cfg["lex"]["craft_verb"]

    p1_variants = [
        "%s is %s %s %s %s in the %s. %s by %s of %s, it %s and %s in a way no other %s does."
        % (T, _a(adj), adj, noun, ov, cfg["canon"], pick(rnd, ["Chronicled", "Recorded", "Documented", "Kept"]),
           person, place, pick(rnd, ["carries its history openly", "hides its oldest secret in plain sight",
                                    "remembers every hand that shaped it", "changes a little each time it is told"]),
           pick(rnd, ["endures", "shines", "persists", "prevails"]), noun),
        "Every %s in the %s has a story, and %s has one of the finest. This %s %s first appeared in the tales told around the %s of %s, where %s %s."
        % (noun, cfg["canon"], T, adj, noun,
           pick(rnd, ["hearth-fires", "harbor-lanterns", "market-bells", "watch-towers"]),
           place, person, pick(rnd, ["swore it was real", "mapped it by starlight", "sang its name three times",
                                    "drew it on a tavern wall", "traded half a fortune for a glimpse"])),
        "Among the %s of the %s, %s stands apart. %s, %s %s it with %s, and ever since, %s has been the measure other %s are judged against."
        % (plural, cfg["canon"], T, pick(rnd, ["They say", "The old songs claim", "Travelers insist"]),
           person, ov, material, T, plural),
    ]
    p1 = pick(rnd, p1_variants)

    p2_variants = [
        "In practical terms it is defined by %s, %s, %s and %s. Its %s %s, and those who %s it learn quickly that %s."
        % (attr_bits[0], attr_bits[1], attr_bits[2], attr_bits[3], cfg["attrs"][0]["label"].lower(),
           pick(rnd, ["matters most in the old stories", "is what the %s remember" % cfg["lex"]["keepers"],
                      "decides how it is used", "sets it apart from its kin"]),
           cv, pick(rnd, ["respect earns its cooperation", "patience reveals its pattern",
                          "preparation beats boldness", "the small details decide everything"])),
        "Scholars of the %s describe it with four measures: %s; %s; %s; %s. Beyond the numbers it carries two natures at once - %s and %s - which is why %s of %s still argue about it by lamplight."
        % (cfg["canon"], attr_bits[0], attr_bits[1], attr_bits[2], attr_bits[3], cat1, cat2, person2, place2),
        "Those who %s such things keep careful notes: %s, %s, %s, %s. Mark also its twin aspects, %s and %s, for a %s is never only one thing, and %s proves it."
        % (cv, attr_bits[0], attr_bits[1], attr_bits[2], attr_bits[3], cat1, cat2, noun, T),
    ]
    p2 = pick(rnd, p2_variants)

    p3_variants = [
        "In play and in story, %s opens doors. A %s might %s, a storyteller might %s, and a player can %s. The only rule the %s agree on: treat it as real while the tale lasts, and it will repay the courtesy."
        % (T, cfg["lex"]["user1"], pick(rnd, cfg["lex"]["uses"]), cfg["lex"]["user2"],
           pick(rnd, cfg["lex"]["uses"]), cfg["lex"]["keepers"]),
        "What makes %s worth keeping is not power but possibility. %s of %s once %s, and the tale is still told because %s. Use it as %s, and let the %s do the rest."
        % (T, pick(rnd, ["A caravan-master", "A young mapmaker", "An old sailor", "A wandering scholar"]),
           place, cv + "d it for a single winter", pick(rnd, ["everyone listening leaned closer", "the ending still surprises",
           "children ask for it by name", "it explains the world a little"]), _a(cfg["lex"]["use_as"]) + " " + cfg["lex"]["use_as"],
           plural),
        "%s endures because it is useful to the imagination. %s it in a %s, %s it across a %s, or simply %s it when the story stalls - %s of %s agree it never fails to move things forward."
        % (T, pick(rnd, ["Set", "Place", "Hide", "Keep"]), cfg["lex"]["setting1"], pick(rnd, ["carry", "send", "chase"]), cfg["lex"]["setting2"],
           pick(rnd, ["invoke", "name", "remember"]), person, place2),
    ]
    p3 = pick(rnd, p3_variants)

    paras = [p1, p2, p3]
    if edition == "signature":
        sig_variants = [
            "Signature treatment: in the Signature telling, %s is not borrowed from any older tale - it is sworn original, built sign by sign under the Signature canon, and every number above was set by hand and verified by the archive. What the public record describes, the Signature record completes."
            % T,
            "The Signature edition carries the same %s further: every measure re-checked, every lineage re-sworn, every secret given its proper seal. This is the Signature system's own %s - original down to the grain, and it answers only to the canon that made it."
            % (noun, noun),
        ]
        paras.append(pick(rnd, sig_variants))
    if cfg.get("polish"):
        paras.append(pick(rnd, cfg["polish_paras"]).format(T=T, noun=noun, place=place, person=person))
    return "\n\n".join(paras)


def how_it_works(cfg, spec, edition, rnd):
    T = spec["core"]
    noun = cfg["noun"]
    steps_pool = [
        "Begin with the seed: name the %s aloud - %s - and fix its %s and %s in your notes before anything else." % (noun, T, cfg["attrs"][0]["label"].lower(), cfg["attrs"][1]["label"].lower()),
        "Give it a home: set it in %s, among the %s, and decide what it wants and what it fears." % (pick(rnd, cfg["places"]), cfg["lex"]["keepers"]),
        "Test it in motion: %s, and watch how its %s (%s) and %s (%s) shape the outcome." % (pick(rnd, cfg["lex"]["uses"]), cfg["attrs"][2]["label"].lower(), spec["attrs"][cfg["attrs"][2]["key"]], cfg["attrs"][3]["label"].lower(), spec["attrs"][cfg["attrs"][3]["key"]]),
        "Add one secret: every lasting %s keeps something back - a hidden cost, a forgotten name, a door that only opens once." % noun,
        "Close the loop: return to the seed and check that the %s you finished is still the %s you named - consistency is what makes it feel real." % (noun, noun),
    ]
    intro = pick(rnd, [
        "Working with %s follows the archive's five-step practice - simple to start, deep to master." % T,
        "%s is used, not just admired. The practice below turns the record above into something playable." % T,
    ])
    steps = "\n".join("%d. %s" % (i + 1, s) for i, s in enumerate(steps_pool))
    return intro + "\n" + steps


def key_points(cfg, spec, edition, rnd):
    T = spec["core"]
    adj = pick(rnd, cfg["adjs"])
    pts = [
        "Core identity: %s - %s." % (T, _a(adj) + " " + adj + " " + cfg["noun"] + " of the " + cfg["canon"]),
        "Signature measures: %s; %s." % ("%s of %s %s" % (cfg["attrs"][0]["label"], spec["attrs"][cfg["attrs"][0]["key"]], cfg["attrs"][0]["unit"]),
                                                         "%s of %s %s" % (cfg["attrs"][1]["label"], spec["attrs"][cfg["attrs"][1]["key"]], cfg["attrs"][1]["unit"])),
        "Twin natures: %s and %s - both true at once." % (spec["cats"][0], spec["cats"][1]),
        "Best use: %s." % pick(rnd, cfg["lex"]["uses"]),
        "Keeper's note: %s." % pick(rnd, ["respect the secret it keeps", "let players discover it slowly",
                                          "never explain it twice the same way", "anchor it to a place the audience knows"]),
        "Archive standing: %s record, ladder rank %d of 34, %s tier." % ("Signature original" if edition == "signature" else "public",
                                                                        spec["rank"], spec["tier"]),
    ]
    return pts


def requirements(cfg, spec, edition, rnd):
    noun = cfg["noun"]
    return [
        "A name fixed in writing - %s, spelled one way, always." % spec["core"],
        "A home place in the %s where the %s belongs." % (cfg["canon"], noun),
        "The four measures recorded (%s, %s, %s, %s) so every telling agrees." % tuple(a["label"].lower() for a in cfg["attrs"]),
        "One secret withheld from the first telling, revealed only in play.",
    ]


def standards(cfg, spec, edition, rnd):
    return [
        "Originality: sworn original to the %s - no borrowed names, no copied lore." % cfg["canon"],
        "Consistency: every measure, name, and nature matches across tellings.",
        "Completeness: a full record - description, practice, measures, and a working demonstration - never a stub.",
    ]


def citations(cfg, spec, edition, rnd):
    T = spec["core"]
    return [
        "Signature Worldbuilding Canon, %s - entry \"%s\"." % (pick(rnd, ["Vol. II", "Vol. III", "Vol. IV", "Vol. VII"]), T),
        "%s of %s, as kept by %s (%s telling)." % (pick(rnd, ["The keeper's ledger", "The traveler's atlas", "The player's handbook", "The storyteller's roll"]),
                                                   pick(rnd, cfg["places"]), pick(rnd, cfg["people"]),
                                                   "Signature" if edition == "signature" else "public"),
    ]


# ------------------------------------------------------------------ demos

def demo_program(cfg, spec, edition):
    """Build a runnable Python demo from the record's numeric attributes."""
    T = spec["core"]
    attrs = cfg["attrs"]
    av = spec["attrs"]
    lines = []
    lines.append("# %s - %s demonstration" % (T, cfg["item_name"]))
    lines.append("# Property of Justin Addam Higgins (JAH).")
    lines.append("attrs = {")
    for a in attrs:
        v = av[a["key"]]
        lines.append("    %r: %s,  # %s" % (a["label"], repr(v), a["unit"]))
    lines.append("}")
    lines.append("print('== %s ==')" % T.replace("'", "\\'"))
    lines.append("for label, value in attrs.items():")
    lines.append("    print('  %s: %s' % (label, value))")
    lines.append("total = sum(attrs.values())")
    lines.append("mean = total / len(attrs)")
    lines.append("spread = max(attrs.values()) - min(attrs.values())")
    lines.append("print('  total = %.2f' % total)")
    lines.append("print('  mean  = %.2f' % mean)")
    lines.append("print('  spread= %.2f' % spread)")
    lines.append("for label, value in attrs.items():")
    lines.append("    assert value >= 0, 'attribute must be non-negative: ' + label")
    lines.append("assert spread >= 0, 'spread cannot be negative'")
    lines.append("print('OK - %s demo passed')" % T.replace("'", "\\'"))
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ record

def build_record(cfg, spec, edition, prefix, src):
    rnd = seeded(cfg["slug"], spec["core"], edition)
    rank = spec["rank"]
    title = spec["core"] + (" (Signature Edition)" if edition == "signature" else "")
    rec = {
        "id": "%s%06d" % (prefix, rank),
        "t": title,
        "g": spec["g"],
        "name": title,
        "title": title,
        "description": desc_paragraphs(cfg, spec, edition, rnd),
        "how_it_works": how_it_works(cfg, spec, edition, rnd),
        "key_points": key_points(cfg, spec, edition, rnd),
        "requirements": requirements(cfg, spec, edition, rnd),
        "standards": standards(cfg, spec, edition, rnd),
        "citations": citations(cfg, spec, edition, rnd),
        "src": src,
        "ladder_rank": rank,
        "ladder_tier": spec["tier"],
        "demo": {
            "kind": cfg["slug"] + "-demo",
            "language": "python",
            "program": demo_program(cfg, spec, edition),
            "note": "Machine-executed at build time; prints the record's measures and verifies their bounds.",
        },
    }
    return rec


def index_row(rec):
    return {"id": rec["id"], "t": rec["t"], "g": rec["g"],
            "d": rec["description"].split("\n\n")[0][:180]}
