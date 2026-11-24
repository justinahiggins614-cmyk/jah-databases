# Combo Builder — AI spec (Combo Router)

Generator: word-combo-gen 1.0.4 / 2026-11-23. Router site: signature-word-combos.
Home of the combos/ namespace: https://justinahiggins614-cmyk.github.io/jah-databases/combos/

## Purpose

The Combo Builder generates a combo's full page, spec and demo from the template in REVIEW §3.4, deterministically: the same combo in always produces byte-identical output.

## Template (10 sections)

1. What the combo means. 2. Math proof (deterministic rank + space sizes). 3. Science proof (Dictionary linguistics only; speculative material labelled design-study). 4. Relevant data (Dictionary links, related live sites). 5. Spec (words, order, length class, demand source, generator version, verification stamp). 6. Working demo that genuinely executes. 7. Two AIs, downloadable with specs. 8. Use. 9. Sources. 10. Accessible zero-script version.

## Resolution rule (the Router's core promise)

- Every combo has the stable URL combos/<slug>/.
- Stored combos (Waves 1, 2, 3 and 4: all 450 List 03 items plus all 191 List 04 items of 2 to 7 words, 641 in all) serve their pre-rendered page.
- Unstored combos (every other 2–7-word combo) resolve through the repo-level 404.html fallback, which loads combos/combo-page.js and renders the same 10-section page in the browser from the combo's words. Never a dead link, never a "not built yet" page. The 39 eight-plus-word List 04 items are outside the 7-word cap.
- combo-page.js fetches combos/data/wave1-index.json, combos/data/wave2-index.json, combos/data/wave3-index.json and combos/data/wave4-index.json (plus combos/data/list04-bold-201-208.json, which completes the 230-item List 04); a slug found in any index is stored, and its stored note names the right wave and the right list.
- The fallback is served by GitHub Pages with HTTP status 404 even though the rendered content is a working combo page; only stored pages are listed in the sitemap and directory, because only stored pages are indexable files.

## Rules

- Deterministic output; the slug is the identity; never duplicate a combo.
- Boundary refusal with a recorded reason; never generate around a refusal.
- Tool-like combos get a small working tool built only from held data; otherwise the combo explorer, with an honest statement that no genuine tool could be built from held data. Never a fake tool.
- Definitions: authored as written, template-filled labelled, pending labelled pending, non-headwords labelled, never faked.
- Space sizes: use the verified math.perm values (see the Librarian spec). The generator's combo-lib.js SPACE constants are computed at runtime from exact BigInt arithmetic (fixed in v1.0.1; the verified math.perm values are in data/space-sizes.json).
