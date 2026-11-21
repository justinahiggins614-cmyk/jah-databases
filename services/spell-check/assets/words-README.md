# Word list — how it was built

Source: the live spelling archive's own word list,
`jah-databases/data/spelling/words.txt` — 99,226 entries, 96,088 plain
lowercase headwords after filtering to letters only. This file holds
exactly those headwords, nothing added, nothing removed.

The headwords alone are NOT enough for a checker: they are dictionary
headwords, so plurals (words, cats), past forms (walked, checked) and
-ing forms (checking) are missing. The checker therefore does NOT ship
an expanded list. Instead the page itself applies the regular English
rules at check time (see `isWord` in index.html):

- strip -s / -es / -ies (to -y) and look up the stem
- strip -ed / -d, undo doubled letters (stopped -> stop), -e words (baked -> bake)
- strip -ing, undo doubling (running -> run), restore -e (making -> make)
- strip -ly / -ily, -ness / -iness, -ment, -er / -est (with the same
  -y / doubling / -e rules)

Plus a short fixed list of standard contractions (don't, can't, won't, ...)
and standard irregular forms (made, took, went, men, women, feet, ...)
kept in the page's script.

Every accepted form traces to a listed headword by one of those rules,
or is on the fixed contraction/irregular list. A word the rules cannot
reach is flagged, and the page says so plainly.

## Blocked words (in index.html, BLOCKED)

21 words the rules above would wrongly accept, so the page blocks them
outright, each with its correction. Found by testing classic misspellings
against the rules on 2026-11-21:

- the archive lists them as variant headwords: mispell, calender, grammer
  (and mispelled, their regular form)
- the -ing rule accepts forms that keep a silent e: makeing, useing,
  haveing, liveing, danceing, writting, comming, geting, prefering,
  refering (all skip the e-drop or the doubling)
- the -ly rule accepts forms that skip -ally: accidently, basicly
- the -ness rule accepts happyness (skips the y-to-i change)
- the -ier rule accepts thier (thy + ier)
- withing (with + ing) and truely / arguement (kept e)

Each blocked word's correction is one edit away and is itself accepted
by the rules, so the checker always offers the right fix.
