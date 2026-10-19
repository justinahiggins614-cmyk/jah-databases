#!/usr/bin/env python3
"""Emit code/<slug>-build/{build.py, entries_<f>.py-stub, demos_<f>.py} for all 15 batch-3 fields.
Entries content is written separately by hand; this only scaffolds.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fields import FIELDS

REPO = "/home/hatch/workspace/jah-databases"

bt = open(os.path.join(HERE, "build_template.py"), encoding="utf-8").read()
dt = open(os.path.join(HERE, "demos_template.py"), encoding="utf-8").read()

for f in FIELDS:
    slug = f["slug"]
    sigslug = slug + "-signature"
    fmod = "entries_" + slug.replace("-", "_")
    dmod = "demos_" + slug.replace("-", "_")
    aishort = f["short"].title().replace(" ", "")
    ddir = os.path.join(REPO, "code", slug + "-build")
    os.makedirs(ddir, exist_ok=True)

    b = bt
    subs = {
        "@@SLUG@@": slug, "@@SIGSLUG@@": sigslug,
        "@@ENTMOD@@": fmod, "@@DEMOMOD@@": dmod,
        "@@NAME_PUB@@": f["name_pub"], "@@NAME_SIG@@": f["name_sig"],
        "@@TAGLINE_PUB@@": f["tagline_pub"], "@@TAGLINE_SIG@@": f["tagline_sig"],
        "@@PREFIX_PUB@@": f["prefix_pub"], "@@PREFIX_SIG@@": f["prefix_sig"],
        "@@SEARCH_PH@@": f["search_ph"], "@@CHAT_PH@@": f["chat_ph"],
        "@@GREET_PUB@@": f["greet_pub"], "@@SHORT@@": f["short"],
        "@@AISHORT@@": aishort, "@@CIT_PUB@@": f["cit"],
    }
    for k, v in subs.items():
        b = b.replace(k, v)
    assert "@@" not in b, "unsubstituted placeholder in %s" % slug
    with open(os.path.join(ddir, "build.py"), "w", encoding="utf-8") as fh:
        fh.write(b)
    compile(b, slug + "/build.py", "exec")

    d = dt.replace("@@DBNAME@@", f["name_pub"]).replace("@@ENTMOD@@", fmod)
    assert "@@" not in d
    with open(os.path.join(ddir, dmod + ".py"), "w", encoding="utf-8") as fh:
        fh.write(d)
    compile(d, slug + "/" + dmod + ".py", "exec")

    # entries stub so imports resolve; content appended by hand later
    stub = ('#!/usr/bin/env python3\n"""Entries for %s.\n\nCONTENT PENDING - staged by builder.\n"""\n\n'
            'LABEL = "Signature-generated proposed solution \\u2014 not established science."\n\n'
            'SIG_TAIL = "Signature editions carry the Signature system\'s proposed solution approaches."\n\n'
            'ENTRIES = []\n') % f["name_pub"]
    sp = os.path.join(ddir, fmod + ".py")
    if not os.path.exists(sp):
        with open(sp, "w", encoding="utf-8") as fh:
            fh.write(stub)
    print("scaffolded", ddir)
print("done")
