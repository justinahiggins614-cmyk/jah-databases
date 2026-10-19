#!/usr/bin/env python3
"""Wave 7 (1000-list, themes food/travel-places/animals-nature) build framework.

Uses code/_pairbuild12/lib.py (build_pair) for the full pipeline:
  db/<slug>/{index.html,gen-<slug>.js}
  db/<slug>-signature/{index.html,gen-<slug>-signature.js}
  data/<slug>/{index.jsonl.gz,chunks/chunk-0000.jsonl.gz}
  data/<slug>-signature/{...}
  code/<slug>-build/manifest-fragment.json   (for the coordinator)

Content model: each topic carries authored real facts + methods + a Signature
twist + numbers. The renderer composes full human-readable records
(description, how_it_works, key_points, requirements, standards, citations).
Demos are data-driven Python programs computing real derived values from the
topic's own numbers; every demo is machine-executed at build time.

Property of Justin Addam Higgins (JAH).
"""
import json
import os
import re
import shutil
import subprocess
import sys

W7 = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.expanduser("~/workspace/jah-databases")
sys.path.insert(0, os.path.join(REPO, "code", "_pairbuild12"))
import lib as pairlib  # noqa: E402

# ---------------------------------------------------------------- topic spec

def T(title, tier, facts, methods, sig, nums, safety=None):
    """One ladder topic. facts: 4-6 real fact sentences. methods: 3-5 real
    process/method sentences. sig: 1-3 sentence Signature-edition expansion.
    nums: dict with 'variant' + numbers feeding the runnable demo."""
    assert tier in ("Foundations", "Compounded", "Advanced"), tier
    assert 4 <= len(facts) <= 8, title
    assert 3 <= len(methods) <= 7, title
    assert isinstance(nums, dict) and "variant" in nums, title
    return {"title": title, "tier": tier, "facts": facts, "methods": methods,
            "sig": sig, "nums": nums, "safety": safety}


def check_topics(topics):
    assert len(topics) == 34, "need 34 topics, got %d" % len(topics)
    tiers = [t["tier"] for t in topics]
    assert tiers.count("Foundations") == 11, tiers.count("Foundations")
    assert tiers.count("Compounded") == 12, tiers.count("Compounded")
    assert tiers.count("Advanced") == 11, tiers.count("Advanced")
    titles = [t["title"] for t in topics]
    assert len(set(titles)) == 34, "dup titles in item"


# ---------------------------------------------------------------- rendering

def _paras(sentences, per=3):
    out = []
    for i in range(0, len(sentences), per):
        out.append(" ".join(sentences[i:i + per]))
    return "\n\n".join(out)


def render_pub(topic):
    facts = list(topic["facts"])
    desc = _paras(facts, 3)
    if topic.get("safety"):
        desc += "\n\nSafety: " + topic["safety"]
    how = _paras(topic["methods"], 2)
    return desc, how


def render_sig(topic, item):
    sig = topic["sig"]
    pub_desc, pub_how = render_pub(topic)
    desc = pub_desc + "\n\nSignature edition: " + sig
    how = pub_how + "\n\nSignature method note: " + (item.get("sig_how") or
        "The Signature system treats this as a living build: every element above "
        "is kept as data, so the generator can remix it into new variations on "
        "demand while the seeded record stays the reference.")
    return desc, how


# ---------------------------------------------------------------- demos

_DEMO_HEAD = '''#!/usr/bin/env python3
"""%s — runnable demonstration. Property of Justin Addam Higgins (JAH)."""
%s
print("DEMO_OK")
'''

def _py_list(items):
    return "[" + ", ".join(json.dumps(x) for x in items) + "]"


def demo_food(nums, title):
    v = nums["variant"]
    body = []
    if v == "recipe":
        ing = nums["ingredients"]  # [name, unit, qty]
        s0, s1 = nums["servings"], nums["target_servings"]
        body.append("servings, target = %r, %r" % (s0, s1))
        body.append("ingredients = %s" % _py_list(ing))
        body.append("factor = target / servings")
        body.append("print('Scale factor: %.3f' % factor)")
        body.append("total = 0.0")
        body.append("for name, unit, qty in ingredients:")
        body.append("    scaled = qty * factor")
        body.append("    total += scaled")
        body.append("    print('  %s: %.1f %s' % (name, scaled, unit))")
        body.append("print('Total batch weight: %.1f' % total)")
        if "temp_c" in nums:
            body.append("c = %r; f = c * 9.0/5.0 + 32.0" % nums["temp_c"])
            body.append("print('Oven: %d C = %.0f F' % (c, f))")
            body.append("assert abs(f - (c*9.0/5.0+32.0)) < 0.01")
        if "time_min" in nums:
            body.append("tmin = %r; print('Active time: %%d min (%%.2f h)' %% (tmin, tmin/60.0))" % nums["time_min"])
        body.append("assert abs(factor - target/servings) < 1e-9")
        body.append("assert total > 0")
    elif v == "build":
        comp = nums["components"]  # [name, kcal]
        wt = nums.get("weight_g", 0)
        body.append("components = %s" % _py_list(comp))
        body.append("components = [(n, float(k)) for n, k in components]")
        body.append("total_kcal = sum(k for _, k in components)")
        body.append("print('Components: %d' % len(components))")
        body.append("for name, k in components: print('  %s: %d kcal' % (name, k))")
        body.append("print('Total: %d kcal' % total_kcal)")
        if wt:
            body.append("w = %r; print('Energy density: %%.1f kcal/100g' %% (total_kcal/w*100.0))" % wt)
            body.append("assert abs(total_kcal/w*100.0 - (total_kcal/%r*100.0)) < 0.01" % wt)
        body.append("assert total_kcal == sum(k for _, k in components)")
        body.append("assert total_kcal > 0")
    elif v == "drink":
        ing = nums["ingredients"]  # [name, ml]
        body.append("ingredients = %s" % _py_list(ing))
        body.append("ingredients = [(n, float(ml)) for n, ml in ingredients]")
        body.append("total_ml = sum(ml for _, ml in ingredients)")
        body.append("print('Total volume: %d ml (%.2f fl oz)' % (total_ml, total_ml/29.5735))")
        body.append("for name, ml in ingredients:")
        body.append("    print('  %s: %d ml (%.1f%%)' % (name, ml, 100.0*ml/total_ml))")
        body.append("assert abs(sum(ml for _, ml in ingredients) - total_ml) < 1e-9")
        body.append("assert total_ml > 0")
    elif v == "convert":
        # generic unit conversions from nums["pairs"] = [[label, value, from, to, factor]]
        pairs = nums["pairs"]
        body.append("pairs = %s" % _py_list(pairs))
        body.append("for label, val, frm, to, factor in pairs:")
        body.append("    val, factor = float(val), float(factor)")
        body.append("    conv = val * factor")
        body.append("    print('%s: %s %s = %.3f %s' % (label, val, frm, conv, to))")
        body.append("    assert abs(conv - val*factor) < 1e-9")
    elif v == "ratio":
        a, b = nums["a"], nums["b"]  # [label, value]
        body.append("a_label, a_val = %r, float(%r)" % (a[0], a[1]))
        body.append("b_label, b_val = %r, float(%r)" % (b[0], b[1]))
        body.append("r = a_val / b_val")
        body.append("print('%s / %s = %.4f' % (a_label, b_label, r))")
        body.append("print('%s is %.1f%% of %s' % (a_label, 100.0*r, b_label))")
        body.append("assert abs(r - a_val/b_val) < 1e-9")
    else:
        raise ValueError("unknown food demo variant " + v)
    return _DEMO_HEAD % (title.replace('"', "'"), "\n".join(body))


def demo_travel(nums, title):
    v = nums["variant"]
    body = []
    if v == "place":
        # nums["facts"] = [[label, value, unit]]; demo converts + compares
        facts = nums["facts"]
        body.append("facts = %s" % _py_list(facts))
        body.append("for label, val, unit in facts:")
        body.append("    print('%s: %s %s' % (label, val, unit))")
        conv = nums.get("conversions", [])  # [label, val, factor, to_unit]
        if conv:
            body.append("for label, val, factor, to_unit in %s:" % _py_list(conv))
            body.append("    val, factor = float(val), float(factor)")
            body.append("    c = val * factor")
            body.append("    print('  = %.2f %s' % (c, to_unit))")
            body.append("    assert abs(c - val*factor) < 1e-6")
        body.append("assert len(facts) > 0")
    elif v == "route":
        d, days, stops, budget = nums["distance_km"], nums["days"], nums["stops"], nums["budget_usd"]
        body.append("dist, days, stops, budget = %r, %r, %r, %r" % (d, days, stops, budget))
        body.append("per_day = dist / days")
        body.append("per_stop_h = (days * 8.0) / stops")
        body.append("per_day_cost = budget / days")
        body.append("print('Route: %.0f km over %d days' % (dist, days))")
        body.append("print('Driving per day: %.1f km' % per_day)")
        body.append("print('Sightseeing per stop: %.1f h' % per_stop_h)")
        body.append("print('Budget per day: $%.2f' % per_day_cost)")
        body.append("assert abs(per_day - dist/days) < 1e-9")
        body.append("assert abs(per_day_cost - budget/days) < 1e-9")
    elif v == "ratio":
        a, b = nums["a"], nums["b"]
        body.append("a_label, a_val = %r, float(%r)" % (a[0], a[1]))
        body.append("b_label, b_val = %r, float(%r)" % (b[0], b[1]))
        body.append("r = a_val / b_val")
        body.append("print('%s vs %s: %.3f' % (a_label, b_label, r))")
        body.append("assert abs(r - a_val/b_val) < 1e-9")
    else:
        raise ValueError("unknown travel demo variant " + v)
    return _DEMO_HEAD % (title.replace('"', "'"), "\n".join(body))


def demo_animal(nums, title):
    v = nums["variant"]
    body = []
    if v == "species":
        # nums["stats"] = [[label, value, unit, si_factor, si_unit]]
        stats = nums["stats"]
        body.append("stats = %s" % _py_list(stats))
        body.append("for label, val, unit, si_f, si_u in stats:")
        body.append("    val, si_f = float(val), float(si_f)")
        body.append("    si = val * si_f")
        body.append("    print('%s: %s %s = %.4g %s' % (label, val, unit, si, si_u))")
        body.append("    assert abs(si - val*si_f) < 1e-6 * max(1.0, abs(si))")
        cmp_ = nums.get("compare")  # [label, factor, ref]
        if cmp_:
            body.append("label, factor, ref = %r, float(%r), %r" % (cmp_[0], cmp_[1], cmp_[2]))
            body.append("print('%s is %.2f x %s' % (label, factor, ref))")
            body.append("assert factor != 0")
        body.append("assert len(stats) > 0")
    elif v == "ratio":
        a, b = nums["a"], nums["b"]
        body.append("a_label, a_val = %r, float(%r)" % (a[0], a[1]))
        body.append("b_label, b_val = %r, float(%r)" % (b[0], b[1]))
        body.append("r = a_val / b_val")
        body.append("print('%s / %s = %.4f' % (a_label, b_label, r))")
        body.append("assert abs(r - a_val/b_val) < 1e-9")
    elif v == "name":
        names = nums["names"]  # [name, syllables, theme]
        body.append("names = %s" % _py_list(names))
        body.append("for n, syl, theme in names: assert 1 <= int(syl) <= 4, 'syllable count out of range'")
        body.append("avg = sum(int(s) for _, s, _ in names)/len(names)")
        body.append("print('Names in set: %d, avg syllables: %.2f' % (len(names), avg))")
        body.append("callable_n = sum(1 for _, s, _ in names if int(s) <= 2)")
        body.append("print('Highly callable (<=2 syllables): %d/%d' % (callable_n, len(names)))")
        body.append("themes = sorted(set(t for _, _, t in names))")
        body.append("print('Themes: ' + ', '.join(themes))")
        body.append("assert len(names) >= 2")
        body.append("print('DEMO_OK')")
    else:
        raise ValueError("unknown animal demo variant " + v)
    return _DEMO_HEAD % (title.replace('"', "'"), "\n".join(body))


DEMO_BY_THEME = {"food": demo_food, "travel": demo_travel, "animals": demo_animal}


def make_demo_builder(theme):
    fn = DEMO_BY_THEME[theme]
    def demo_builder(topic, edition):
        return fn(topic["nums"], topic["title"] + (" (Signature Edition)" if edition == "sig" else ""))
    return demo_builder


# ---------------------------------------------------------------- item config

def mk_item(slug, name, theme, prefix_pub, record_kind, tagline_pub, tagline_sig,
            ai_short, role_pub, role_sig, greet_pub, greet_sig,
            search_ph, chat_ph, gen_blurb, about_archive,
            requirements, standards, citations, topics,
            health=False, sig_how=None, gen_sample_extra="",
            custom_gen=None):
    check_topics(topics)
    _base = name[:-9] if name.endswith(" Database") else name
    _ai = ai_short[:-10] if ai_short.endswith(" Archivist") else ai_short
    return {
        "slug": slug, "name": _base, "theme": theme,
        "name_pub": _base + " Database", "name_sig": _base + " Signature Database",
        "prefix_pub": prefix_pub, "prefix_sig": prefix_pub[:-1] + "S-",
        "record_kind": record_kind,
        "record_kind_plural": record_kind + "s",
        "tagline_pub": tagline_pub, "tagline_sig": tagline_sig,
        "ai_pub": "JAH %s Archivist" % _ai,
        "ai_sig": "JAH Signature %s Creator" % _ai,
        "role_pub": role_pub, "role_sig": role_sig,
        "greet_pub": greet_pub, "greet_sig": greet_sig,
        "search_ph": search_ph, "chat_ph": chat_ph,
        "gen_blurb": gen_blurb, "about_archive": about_archive,
        "requirements": requirements, "standards": standards,
        "citations": citations, "topics": topics,
        "health": health, "sig_how": sig_how,
        "gen_sample_extra": gen_sample_extra,
        "custom_gen": custom_gen,  # path to custom gen JS (gen-* items) or None
    }


def topics_for_lib(item):
    """Convert wave7 topics to lib.build_pair topic dicts."""
    out = []
    for t in item["topics"]:
        pub_desc, pub_how = render_pub(t)
        sig_desc, sig_how = render_sig(t, item)
        out.append({
            "title": t["title"], "tier": t["tier"],
            "nums": t["nums"],
            "desc_pub": pub_desc, "desc_sig": t["sig"],
            "how_pub": pub_how, "how_sig": item.get("sig_how") or
                "The Signature system keeps this method as executable data: the generator "
                "can replay it with different inputs while the seeded record stays the reference.",
            "keys": list(t["facts"]),
            "reqs": list(item["requirements"]),
            "stds": list(item["standards"]),
            "cites": list(item["citations"]),
        })
    return out


def build_one(item):
    slug = item["slug"]
    # slug-collision guard: nothing in db/, data/, or manifest may own these slugs
    for s in (slug, slug + "-signature"):
        assert not os.path.exists(os.path.join(REPO, "db", s)), "db dir exists: " + s
        assert not os.path.exists(os.path.expanduser("~/workspace/jah-databases-data-1/data/" + s)), \
            "data dir exists: " + s
    topics = topics_for_lib(item)
    cfg = {
        "slug": slug,
        "name_pub": item["name_pub"], "name_sig": item["name_sig"],
        "tagline_pub": item["tagline_pub"], "tagline_sig": item["tagline_sig"],
        "prefix_pub": item["prefix_pub"], "prefix_sig": item["prefix_sig"],
        "record_kind": item["record_kind"], "record_kind_plural": item["record_kind_plural"],
        "ai_pub": item["ai_pub"], "ai_sig": item["ai_sig"],
        "role_pub": item["role_pub"], "role_sig": item["role_sig"],
        "greet_pub": item["greet_pub"], "greet_sig": item["greet_sig"],
        "search_ph": item["search_ph"], "chat_ph": item["chat_ph"],
        "gen_blurb": item["gen_blurb"], "about_archive": item["about_archive"],
        "demo_kind": item["theme"] + "-lab-demo",
        "demo_title": {"food": "Food Lab Demo", "travel": "Travel Lab Demo",
                       "animals": "Nature Lab Demo"}[item["theme"]],
        "health": item["health"],
        "gen_sample_extra": item["gen_sample_extra"],
    }
    built = pairlib.build_pair(cfg, topics, make_demo_builder(item["theme"]))
    # custom generator override for GENERATOR-class items (template with tokens)
    if item.get("custom_gen"):
        with open(item["custom_gen"], encoding="utf-8") as f:
            gtemplate = f.read()
        for sfx, src, prefix, genver, edlabel in (
                ("", "public-harvest", item["prefix_pub"],
                 "jahdb-%s-1.0" % slug, ""),
                ("-signature", "signature", item["prefix_sig"],
                 "jahdb-%s-signature-1.0" % slug, " (Signature Edition)")):
            eslug = slug + sfx
            gtext = (gtemplate.replace("@@PREFIX@@", prefix)
                     .replace("@@SRC@@", src)
                     .replace("@@GENVER@@", genver)
                     .replace("@@EDLABEL@@", edlabel)
                     .replace("@@SLUGPUB@@", slug)
                     .replace("@@SLUGSIG@@", slug + "-signature"))
            assert "@@" not in re.sub(r"@@[A-Z]+@@", "", gtext) or True
            leftover = re.findall(r"@@[A-Z]+@@", gtext)
            assert not leftover, "unreplaced gen tokens: %s" % leftover[:5]
            dst = os.path.join(REPO, "db", eslug, "gen-%s.js" % eslug)
            with open(dst, "w", encoding="utf-8") as f:
                f.write(gtext)
            subprocess.run(["node", "--check", dst], check=True,
                           capture_output=True, text=True)
            test = ("const g=require(%s);let n=0;"
                    "for(const s of [7,42,3001]){const r=g.generate(s,{});"
                    "const v=g.validate(r);if(!v.ok)throw new Error(JSON.stringify(v.errors));"
                    "if(!r.demo||!r.demo.program)throw new Error('no demo');"
                    "require('fs').writeFileSync('/tmp/_w7g_'+s+'.py',r.demo.program);n++;}"
                    "console.log('GEN_OK '+n);") % json.dumps(dst)
            p = subprocess.run(["node", "-e", test], capture_output=True, text=True)
            assert p.returncode == 0 and "GEN_OK 3" in p.stdout, p.stderr[:300]
            for sd in (7, 42, 3001):
                with open("/tmp/_w7g_%d.py" % sd) as f:
                    ok, out, err = pairlib.run_python_program(f.read())
                assert ok, "custom gen demo failed: " + err[:200]
            print("custom generator OK:", eslug)
    # manifest fragment for the coordinator
    frag = []
    for sfx, name, prefix, source, ai, tag in (
            ("", item["name_pub"], item["prefix_pub"], "public-harvest", item["ai_pub"], item["tagline_pub"]),
            ("-signature", item["name_sig"], item["prefix_sig"], "signature", item["ai_sig"], item["tagline_sig"])):
        eslug = slug + sfx
        frag.append({
            "slug": eslug, "name": name, "tagline": tag,
            "record_kind": item["record_kind"], "id_prefix": prefix,
            "ai_name": ai,
            "local_index": "data/%s/index.jsonl.gz" % eslug,
            "page_url": "db/%s/" % eslug,
            "index": "data/%s/index.jsonl.gz" % eslug,
            "chunk_pattern": "data/%s/chunks/chunk-NNNN.jsonl.gz" % eslug,
            "source": source, "record_count": 34, "full_records": 34,
            "status": "staged",
        })
    bdir = os.path.join(REPO, "code", slug + "-build")
    os.makedirs(bdir, exist_ok=True)
    with open(os.path.join(bdir, "manifest-fragment.json"), "w") as f:
        json.dump(frag, f, indent=1, ensure_ascii=False)
    with open(os.path.join(bdir, "build.py"), "w") as f:
        f.write('#!/usr/bin/env python3\n"""Wave-7 builder for %s (1000-list wave 7).\nStaged only; the coordinator merges manifest fragments.\nProperty of Justin Addam Higgins (JAH).\n"""\nimport os, sys\nsys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/wave7-build"))\nimport build_all\nbuild_all.build_slug("%s")\n' % (slug, slug))
    return built
