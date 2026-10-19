#!/usr/bin/env python3
"""Render per-pair build.py files from the govf2 template + per-pair configs."""
import os
import re
import sys

CODE = "/home/hatch/workspace/jah-databases/code"
sys.path.insert(0, CODE)
from _govf2_configs import PAIRS

TEMPLATE = os.path.join(CODE, "_govf2_build_template.py")

CFG_CALL = '''DBCFG[SLUG_PUB] = _cfg(
    SLUG_PUB, {pub_name},
    {pub_tagline},
    {pub_record_kind}, {pub_prefix}, {pub_ai},
    {pub_role},
    "public",
    {pub_search_ph},
    {pub_chat_ph},
    {pub_archive_blurb},
    {pub_fields},
    {pub_gen_desc},
    {pub_gen_kind}, {pub_gen_demo_kind},
    {pub_greet},
    @@PUB_LINE@@, @@SIG_LINE@@, @@LADDER@@)
DBCFG[SLUG_SIG] = _cfg(
    SLUG_SIG, {sig_name},
    {sig_tagline},
    {sig_record_kind}, {sig_prefix}, {sig_ai},
    {sig_role},
    "signature",
    {sig_search_ph},
    {sig_chat_ph},
    {sig_archive_blurb},
    {sig_fields},
    {sig_gen_desc},
    {sig_gen_kind}, {sig_gen_demo_kind},
    {sig_greet},
    @@PUB_LINE@@, @@SIG_LINE@@, @@LADDER@@)
'''


def _q(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def render(slug_pub, cfg):
    tpl = open(TEMPLATE).read()
    # docstring: replace first """...""" block
    i = tpl.index('"""')
    j = tpl.index('"""', i + 3)
    tpl = tpl[:i] + cfg["docstring"] + tpl[j + 3:]
    # DBCFG blocks
    q = {k: _q(v) for k, v in cfg.items() if k not in ("docstring",)}
    blocks = CFG_CALL.format(**q)
    tpl = tpl.replace("{{DBCFG_BLOCKS}}", blocks)
    # remaining scalar tokens
    mod = slug_pub.replace("-", "_")
    tpl = tpl.replace("{{ENTRIES_MOD}}", "entries_" + mod)
    tpl = tpl.replace("{{DEMOS_MOD}}", "demos_" + mod)
    tpl = tpl.replace("{{SLUG_PUB}}", slug_pub)
    tpl = tpl.replace("{{SLUG_SIG}}", slug_pub + "-signature")
    tpl = tpl.replace("@@PUB_LINE@@", _q(cfg["pub_line"]))
    tpl = tpl.replace("{{PUB_LINE}}", _q(cfg["pub_line"]))
    tpl = tpl.replace("@@SIG_LINE@@", _q(cfg["sig_line"]))
    tpl = tpl.replace("{{SIG_LINE}}", _q(cfg["sig_line"]))
    tpl = tpl.replace("@@LADDER@@", _q(cfg["ladder"]))
    tpl = tpl.replace("{{LADDER}}", _q(cfg["ladder"]))
    leftover = set(re.findall(r"{{[A-Z_]+}}", tpl))
    assert not leftover, "unfilled tokens: %s" % leftover
    compile(tpl, slug_pub, "exec")
    outdir = os.path.join(CODE, slug_pub + "-build")
    os.makedirs(outdir, exist_ok=True)
    outp = os.path.join(outdir, "build.py")
    with open(outp, "w") as f:
        f.write(tpl)
    print("rendered", outp)
    return outp


if __name__ == "__main__":
    only = sys.argv[1:] or None
    for slug_pub, cfg in PAIRS.items():
        if only and slug_pub not in only:
            continue
        render(slug_pub, cfg)
