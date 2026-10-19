#!/usr/bin/env python3
"""One-shot fixer: convert ASCII Scandinavian (ae/oe/aa) to proper
orthography in the LANGUAGE column only, keeping the romanization
column ASCII. Applied to d_danish.py and d_norwegian.py.
"""
import re
import sys


def conv(s):
    s = s.replace("Ae", "\u00c6").replace("ae", "\u00e6")
    s = s.replace("Oe", "\u00d8").replace("oe", "\u00f8")
    s = s.replace("Aa", "\u00c5").replace("aa", "\u00e5")
    return s


STR = r'"(?P<s1>(?:[^"\\]|\\.)*)"'
ROW3 = re.compile(r'^(?P<ind>\s*)\[' + STR + r', "(?P<s2>(?:[^"\\]|\\.)*)", "(?P<s3>(?:[^"\\]|\\.)*)')
ROW4 = re.compile(r'^(?P<ind>\s*)\[' + STR + r', "(?P<s2>(?:[^"\\]|\\.)*)", "(?P<s3>(?:[^"\\]|\\.)*)", "(?P<s4>(?:[^"\\]|\\.)*)')
TITLE = re.compile(r'^(?P<ind>\s*)\(' + STR + r', \[$')


def sub_span(line, start, end, new):
    return line[:start] + new + line[end:]


def fix_line(line):
    m = ROW4.match(line)
    if m:
        s1, s2, s3 = m.group("s1"), m.group("s2"), m.group("s3")
        if s2 == s3:
            # conversation turn ["Name", "lang", "lang", "en"]: convert lang (s3)
            return sub_span(line, m.start("s3"), m.end("s3"), conv(s3)), "turn"
        # alphabet row ["glyph", "name", "example", "en"]: convert example;
        # convert glyph only for Ae/Oe/Aa rows
        ng = conv(s1) if s1 in ("Ae ae", "Oe oe", "Aa aa") else s1
        line = sub_span(line, m.start("s1"), m.end("s1"), ng)
        m2 = ROW4.match(line)
        line = sub_span(line, m2.start("s3"), m2.end("s3"), conv(s3))
        return line, "alpha"
    m = ROW3.match(line)
    if m:
        s1, s2, s3 = m.group("s1"), m.group("s2"), m.group("s3")
        if s1 == s2:
            # triple ["X", "X", "en"]: convert language (s1) only
            return sub_span(line, m.start("s1"), m.end("s1"), conv(s1)), "triple"
        # phonology row ["sym", "desc", "example"]: convert sym + example
        line = sub_span(line, m.start("s1"), m.end("s1"), conv(s1))
        m2 = ROW3.match(line)
        line = sub_span(line, m2.start("s3"), m2.end("s3"), conv(s3))
        return line, "phon"
    m = TITLE.match(line)
    if m:
        return sub_span(line, m.start("s1"), m.end("s1"), conv(m.group("s1"))), "title"
    return line, None


def main(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    counts = {}
    out = []
    for ln in lines:
        nl, kind = fix_line(ln.rstrip("\n"))
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
        out.append(nl + "\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    print("converted in %s: %s" % (path, counts))


if __name__ == "__main__":
    main(sys.argv[1])
