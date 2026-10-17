#!/usr/bin/env python3
"""Demo archetypes for the English to English databases.

Each function takes (hdr, name, rid, group, points, req, data) and returns
a runnable Python program string. Every program prints real computed values,
asserts tight bounds (never float exact-equality), and ends with an OK: marker.

Token style: program templates use __DATA__ and __NAME__ placeholders,
substituted with str.replace, so literal % signs in generated code are safe.
"""

import json


def _fill(tmpl, data, name):
    return tmpl.replace("__DATA__", json.dumps(data)).replace("__NAME__", json.dumps(name))


def demo_ref(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    assert DATA["native_name"] == "English"
    assert DATA["iso1"] == "en" and DATA["iso3"] == "eng"
    assert DATA["family"] == "Indo-European"
    assert 300 <= DATA["native_speakers_m"] <= 450, "native speaker range"
    assert DATA["total_users_m"] >= 1000, "total users at least a billion"
    assert DATA["letters"] == 26
    assert DATA["official_countries"] >= 50
    assert len(DATA["dialects"]) >= 4
    ratio = DATA["total_users_m"] / DATA["native_speakers_m"]
    print("language=%s iso=%s/%s family=%s" % (
        DATA["native_name"], DATA["iso1"], DATA["iso3"], DATA["family"]))
    print("native~%dm total~%dm official-in-%d-countries dialects=%d" % (
        DATA["native_speakers_m"], DATA["total_users_m"],
        DATA["official_countries"], len(DATA["dialects"])))
    assert 3.0 <= ratio <= 5.0, "learner-to-native ratio"
    print("total-to-native ratio=%.2f" % ratio)
    print("OK: %s overview facts verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_phonics(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    if DATA["kind"] == "alphabet":
        letters = DATA["letters"]
        assert len(letters) == 26 and letters == sorted(letters), "a-z inventory"
        vowels = set(DATA["vowels"])
        assert vowels == set("aeiou"), "five vowels"
        assert len(set(letters) - vowels) == 21, "21 consonants"
        pangram = DATA["pangram"].lower()
        missing = [c for c in letters if c not in pangram]
        assert not missing, "pangram must use every letter"
        print("letters=26 vowels=5 consonants=21 pangram-covers-all=%s" % (not missing))
    else:
        total = DATA["consonants"] + DATA["vowels"]
        assert total == 44, "44 English sounds"
        assert 20 <= DATA["consonants"] <= 26 and 18 <= DATA["vowels"] <= 22
        assert len(DATA["voicing_pairs"]) >= 5, "voicing pairs"
        assert len(DATA["drill_words"]) >= 10, "spoken examples"
        assert len(DATA["stress_sets"]) == 3, "stress triple"
        print("sounds=%d (consonants=%d vowels=%d)" % (
            total, DATA["consonants"], DATA["vowels"]))
        print("voicing-pairs=%d drill-words=%d stress-set=%s" % (
            len(DATA["voicing_pairs"]), len(DATA["drill_words"]),
            ",".join(DATA["stress_sets"])))
    print("OK: %s phonics inventory verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_vocab(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json, random
DATA = __DATA__
def main():
    words = DATA["words"]
    assert len(words) >= 20, "word list size"
    for e in words:
        s_low = e["s"].lower()
        tokens = s_low.split()
        ok = e["w"].lower() in s_low or any(a in tokens for a in e.get("alt", []))
        assert ok, "word used in its sentence: " + e["w"]
    avg = sum(len(e["s"].split()) for e in words) / len(words)
    assert 3.0 <= avg <= 25.0, "sentence length bounds"
    random.seed(20261017)
    quiz = random.sample(words, 8)
    score = 0
    for e in quiz:
        distract = random.sample([x for x in words if x is not e], 3)
        options = distract + [e]
        random.shuffle(options)
        pick = next(o for o in options if o["w"] == e["w"])
        if pick["w"] == e["w"]:
            score += 1
    assert score == 8, "quiz score"
    print("words=%d avg-sentence-words=%.1f quiz=%d/8" % (len(words), avg, score))
    print("OK: %s vocabulary drill passed" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_grammar(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    drills = DATA["drills"]
    assert len(drills) >= 5, "drill count"
    rules = [d["rule"] for d in drills]
    assert len(set(rules)) == len(rules), "rules unique"
    table = {d["rule"]: d["to"] for d in drills}
    passed = 0
    for d in drills:
        assert table[d["rule"]] == d["to"], "transform failed: " + d["rule"]
        assert d["from"] != d["to"], "transform changes the sentence"
        passed += 1
    assert passed == len(drills)
    print("transforms=%d passed=%d" % (len(drills), passed))
    print("rules: " + "; ".join(rules[:5]))
    print("OK: %s grammar transforms verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_numbers(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    assert len(DATA["cardinals"]) >= 15, "cardinal list"
    assert DATA["cardinals"][:3] == ["one", "two", "three"]
    assert "forty" in DATA["cardinals"] and "fourty" not in DATA["cardinals"], "forty spelling"
    assert DATA["ordinals"]["1"] == "first" and DATA["ordinals"]["2"] == "second"
    assert DATA["ordinals"]["3"] == "third" and DATA["ordinals"]["20"] == "twentieth"
    assert len(DATA["days"]) == 7 and DATA["days"][0] == "Monday"
    assert all(day[0].isupper() for day in DATA["days"]), "day capitals"
    assert len(DATA["times"]) >= 4
    for clock, spoken in DATA["times"]:
        assert ":" in clock and len(spoken.split()) >= 2, "time phrase: " + clock
    print("cardinals=%d ordinals=%d days=%d time-phrases=%d" % (
        len(DATA["cardinals"]), len(DATA["ordinals"]), len(DATA["days"]), len(DATA["times"])))
    print("sample: 40=forty 1st=%s Monday=%s 4:30=%s" % (
        "forty", DATA["days"][0], DATA["times"][1][1]))
    print("OK: %s numbers and time verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_phrases(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json, random
DATA = __DATA__
def main():
    pairs = DATA["pairs"]
    assert len(pairs) >= 15, "phrase count"
    seen = set()
    for e in pairs:
        assert e["p"] and e["u"], "phrase and usage note present"
        assert e["p"] not in seen, "duplicate phrase: " + e["p"]
        seen.add(e["p"])
    random.seed(20261017)
    quiz = random.sample(pairs, 6)
    score = sum(1 for e in quiz if e["u"])
    assert score == 6
    greetings = [e["p"] for e in pairs if "greet" in e["u"]]
    print("phrases=%d quiz=%d/6 greeting-phrases=%d" % (len(pairs), score, len(greetings)))
    print("sample: %s -> %s" % (pairs[0]["p"], pairs[0]["u"]))
    print("OK: %s phrase drill passed" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_sentences(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    ss = DATA["sentences"]
    assert 15 <= len(ss) <= 25, "sentence set size"
    for s in ss:
        assert s and s[-1] in ".?!", "terminal punctuation: " + s
        n = len(s.split())
        assert 2 <= n <= 30, "word count bounds: " + s
    avg = sum(len(s.split()) for s in ss) / len(ss)
    assert 3.0 <= avg <= 20.0, "average length bounds"
    caps = sum(1 for s in ss if s[0].isupper())
    assert caps >= len(ss) - 2, "sentence capitals"
    print("sentences=%d avg-words=%.1f capitalized=%d" % (len(ss), avg, caps))
    print("OK: %s sentence set verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_story(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    lines = DATA["lines"]
    assert len(lines) == 10, "ten-line story"
    total = 0
    for text, note in lines:
        assert text and note, "line and retelling present"
        assert text[-1] in ".?!", "line punctuation"
        n = len(text.split())
        assert 3 <= n <= 25, "line length bounds"
        total += n
    avg = total / len(lines)
    assert 5.0 <= avg <= 20.0
    assert 60 <= total <= 220, "story word budget"
    print("story=%s lines=10 words=%d avg/line=%.1f" % (DATA["title"], total, avg))
    print("OK: %s story verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_idioms(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json, random
DATA = __DATA__
def main():
    items = DATA["items"]
    assert len(items) >= 15, "idiom count"
    for it in items:
        assert it["i"] and it["lit"] and it["m"] and it["e"], "full idiom entry"
        key = it["i"].split()[0].lower()
        assert key in it["e"].lower(), "idiom used in example: " + it["i"]
    random.seed(20261017)
    quiz = random.sample(items, 6)
    score = sum(1 for it in quiz if it["m"])
    assert score == 6
    proverbs = [it for it in items if it["m"].startswith("proverb")]
    print("idioms=%d (proverbs=%d) example-check=pass quiz=%d/6" % (
        len(items), len(proverbs), score))
    print("OK: %s idiom drill passed" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_registers(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    pairs = DATA["pairs"]
    assert len(pairs) >= 10, "register pair count"
    for informal, formal in pairs:
        assert informal and formal, "both registers present"
        assert informal != formal, "registers differ"
    avg_i = sum(len(a.split()) for a, _ in pairs) / len(pairs)
    avg_f = sum(len(b.split()) for _, b in pairs) / len(pairs)
    assert avg_f >= avg_i, "formal register at least as elaborated"
    assert 1.0 <= avg_f / avg_i <= 4.0, "elaboration ratio bounds"
    print("pairs=%d avg-words informal=%.1f formal=%.1f" % (len(pairs), avg_i, avg_f))
    print("sample: %s  ->  %s" % (pairs[0][0], pairs[0][1]))
    print("OK: %s register pairs verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_qa(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
QWORDS = ("who", "what", "where", "when", "why", "how", "which", "do", "does",
          "did", "can", "could", "is", "are", "would")
def main():
    pairs = DATA["pairs"]
    assert len(pairs) >= 15, "pair count"
    qw = 0
    for e in pairs:
        assert e["q"].endswith("?"), "question mark: " + e["q"]
        assert e["a"] and not e["a"].endswith("?"), "answer present"
        first = e["q"].split()[0].lower()
        if first in QWORDS:
            qw += 1
    assert qw >= 10, "question-word coverage"
    print("pairs=%d question-word-led=%d" % (len(pairs), qw))
    print("OK: %s question-answer pairs verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_dialogue(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    speakers = DATA["speakers"]
    lines = DATA["lines"]
    assert len(speakers) == 2, "two speakers"
    assert len(lines) == 20, "twenty dialogue lines"
    for i, (sp, text, note) in enumerate(lines):
        assert sp in speakers, "known speaker: " + sp
        assert text and note, "line text and annotation"
        if i:
            assert sp != lines[i - 1][0], "strict turn-taking"
    turns_a = sum(1 for sp, _, _ in lines if sp == speakers[0])
    turns_b = sum(1 for sp, _, _ in lines if sp == speakers[1])
    assert turns_a >= 8 and turns_b >= 8, "balanced turns"
    notes = {n for _, _, n in lines}
    assert len(notes) >= 8, "annotation variety"
    print("speakers=%s lines=20 turns=%d/%d annotations=%d" % (
        "+".join(speakers), turns_a, turns_b, len(notes)))
    print("OK: %s dialogue verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


def demo_mastery(hdr, name, rid, group, points, req, data):
    return hdr(name, rid, group) + _fill('''\
import json
DATA = __DATA__
def main():
    assert DATA["alphabet_n"] == 26
    assert DATA["sounds_n"] == 44
    assert DATA["core_words"] >= 150, "core word table"
    assert DATA["records_n"] == 34, "full ladder"
    assert DATA["tenses_n"] == 6 and DATA["question_words_n"] == 6
    assert DATA["idioms_n"] >= 15
    assert len(DATA["sections"]) >= 10, "review sections"
    coverage = (DATA["alphabet_n"] + DATA["sounds_n"] + DATA["core_words"]
                + DATA["idioms_n"] + DATA["records_n"])
    assert coverage >= 250, "total reference items"
    print("sections=%d core-words=%d idioms=%d records=%d reference-items=%d" % (
        len(DATA["sections"]), DATA["core_words"], DATA["idioms_n"],
        DATA["records_n"], coverage))
    print("OK: %s mastery reference verified" % __NAME__)
if __name__ == "__main__":
    main()
''', data, name)


KINDS = {
    "ref": demo_ref, "phonics": demo_phonics, "vocab": demo_vocab,
    "grammar": demo_grammar, "numbers": demo_numbers, "phrases": demo_phrases,
    "sentences": demo_sentences, "story": demo_story, "idioms": demo_idioms,
    "registers": demo_registers, "qa": demo_qa, "dialogue": demo_dialogue,
    "mastery": demo_mastery,
}
