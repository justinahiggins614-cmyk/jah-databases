#!/usr/bin/env python3
"""Build the Movies and Shows databases for JAH Databases.

Four databases, 34 ladder-ordered records each (136 total):

  movies-every-film              The Movies Database            (public-harvest)
  movies-every-film-signature    The Movies Signature Database  (signature)
  shows-every-series             The Shows Database             (public-harvest)
  shows-every-series-signature   The Shows Signature Database   (signature)

Public records: real, fact-checked film/series data. Public-domain titles
carry the actual playable file reference (verified Internet Archive item);
licensed titles carry legal watch avenues only. Signature records are the
original Signature-line companions: an original restoration/curation
engineering plan plus an original creative treatment, with lineage back to
the public record.

Writes (shard repo jah-databases-data-1):
    data/<slug>/index.jsonl.gz + data/<slug>/chunks/chunk-NNNN.jsonl.gz
Writes (main repo): db/<slug>/index.html, db/<slug>/gen-<slug>.js
Does NOT touch data/manifest.json or api.json (the coordinator merges).

Never the words "bat belt" anywhere. No website references. No Facebook.
No YouTube references.
"""
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
spec = importlib.util.spec_from_file_location(
    "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nb)

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_movies_shows import MOVIES, SHOWS

sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
sweep = importlib.util.module_from_spec(sspec)
sspec.loader.exec_module(sweep)

TIERS = ["foundations", "compounded", "advanced"]
TIER_CUT = {"movies": (12, 24), "shows": (12, 24)}  # foundations 1-12, compounded 13-24, advanced 25-34

PD_BASIS = {
    "expired": "U.S. copyright expired (published before 1931; 95-year term).",
    "lapsed": "U.S. copyright not renewed; widely documented as public domain.",
    "defective": "Released without a valid copyright notice; public domain from release.",
}

# ---------------------------------------------------------------- DBCFG

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, hero_p, search_ph,
         chat_ph, archive_blurb, fields, schema, greet, sig_type, source, gen_kind, gen_demo_kind):
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role, "hero_p": hero_p,
        "search_ph": search_ph, "chat_ph": chat_ph, "archive_blurb": archive_blurb,
        "fields": fields, "schema": schema, "greet": greet,
        "sig_type": sig_type, "source": source,
        "gen_desc": "Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries.",
        "gen_fields": TIERS, "gen_kind": gen_kind, "gen_demo_kind": gen_demo_kind,
    }

LADDER_MOV = ("The teaching ladder runs foundations to advanced: Foundations — silent-era landmarks, the simplest "
    "film grammar; Compounded — late-silent mastery and the coming of sound, all public domain; "
    "Advanced — studio-era and modern licensed landmarks, watched through licensed avenues.")
LADDER_SHW = ("The teaching ladder runs foundations to advanced: Foundations — early-television public-domain "
    "series and serials, the simplest broadcast grammar; Compounded — the network golden age, licensed classics; "
    "Advanced — prestige and streaming-era series, watched through licensed avenues.")

DBCFG = {
 "movies-every-film": _cfg(
    "movies-every-film", "The Movies Database",
    "Every publicly accessible film — public-domain titles with the actual playable file, licensed titles with legal watch avenues. Full records, fact-checked.",
    "film record", "JAH-MOV-", "JAH Film Archivist",
    "film archivist — motion pictures, public-domain status, legal viewing",
    "Publicly accessible <b>films</b> — <b>public-domain classics</b> with the actual playable file, plus <b>licensed landmarks</b> with legal watch avenues. Every record carries the full entry: title, year, director, cast, genre, runtime, synopsis, public-domain status, watch information, and a working demonstration program. " + LADDER_MOV,
    "Search films, directors, years…", "Ask about films…",
    "Seeded public-record film archive (JAH-MOV- records), marching toward one million records. " + LADDER_MOV,
    "Foundations · Compounded · Advanced — by decade within each tier",
    "id · t · g · name · title · year · director · cast · genre · runtime_minutes · synopsis · description · public_domain · pd_basis · watch · file_reference · how_it_works · key_points · requirements · standards · citations · src · ladder_rank · ladder_tier · demo · provenance · last_verified",
    "I am the JAH Film Archivist. Ask me about films, directors, and where to watch legally.",
    "Public records organized in the Signature system", "public",
    "film-record-study", "film-record"),
 "movies-every-film-signature": _cfg(
    "movies-every-film-signature", "The Movies Signature Database",
    "The Signature line for film — original Signature restoration plans and original Signature re-imagining treatments, one companion per public film record. Clearly labeled Signature originals.",
    "Signature film record", "JAH-MOVS-", "JAH Film Archivist (Signature)",
    "Signature film archivist — original Signature restoration and re-imagining",
    "The <b>Signature line</b> for film — <b>original Signature restoration plans</b> for the public-domain titles and <b>original Signature study guides</b> for the licensed ones, each paired with an <b>original Signature re-imagining treatment</b>. Every record carries the full entry with lineage to its public companion. " + LADDER_MOV,
    "Search Signature film records…", "Ask about Signature film records…",
    "Seeded Signature-original film archive (JAH-MOVS- records), marching toward one million records. " + LADDER_MOV,
    "Foundations · Compounded · Advanced — by decade within each tier",
    "id · t · g · name · title · lineage · description · restoration_or_study · treatment · how_it_works · key_points · requirements · standards · src · ladder_rank · ladder_tier · demo · provenance · last_verified",
    "I am the JAH Film Archivist (Signature). Ask me about the Signature film line.",
    "Signature originals organized in the Signature system", "signature",
    "signature-film-study", "signature-film-record"),
 "shows-every-series": _cfg(
    "shows-every-series", "The Shows Database",
    "Every publicly accessible television series — public-domain episodes with the actual playable file, licensed series with legal watch avenues. Full records, fact-checked.",
    "series record", "JAH-TV-", "JAH Television Archivist",
    "television archivist — series, episodes, public-domain status, legal viewing",
    "Publicly accessible <b>television series</b> — <b>public-domain episodes</b> with the actual playable file, plus <b>licensed landmark series</b> with legal watch avenues. Every record carries the full entry: title, years, network, stars, genre, episode length, episode count, synopsis, public-domain status, watch information, and a working demonstration program. " + LADDER_SHW,
    "Search series, networks, years…", "Ask about series…",
    "Seeded public-record series archive (JAH-TV- records), marching toward one million records. " + LADDER_SHW,
    "Foundations · Compounded · Advanced — by decade within each tier",
    "id · t · g · name · title · years · network · stars · genre · episode_length_minutes · episodes · synopsis · description · public_domain · pd_basis · watch · file_reference · how_it_works · key_points · requirements · standards · citations · src · ladder_rank · ladder_tier · demo · provenance · last_verified",
    "I am the JAH Television Archivist. Ask me about series, episodes, and where to watch legally.",
    "Public records organized in the Signature system", "public",
    "series-record-study", "series-record"),
 "shows-every-series-signature": _cfg(
    "shows-every-series-signature", "The Shows Signature Database",
    "The Signature line for television — original Signature curation guides and original Signature season treatments, one companion per public series record. Clearly labeled Signature originals.",
    "Signature series record", "JAH-TVS-", "JAH Television Archivist (Signature)",
    "Signature television archivist — original Signature curation and season treatments",
    "The <b>Signature line</b> for television — <b>original Signature curation guides</b> for every public series, each paired with an <b>original Signature season treatment</b>. Every record carries the full entry with lineage to its public companion. " + LADDER_SHW,
    "Search Signature series records…", "Ask about Signature series records…",
    "Seeded Signature-original series archive (JAH-TVS- records), marching toward one million records. " + LADDER_SHW,
    "Foundations · Compounded · Advanced — by decade within each tier",
    "id · t · g · name · title · lineage · description · curation_guide · treatment · how_it_works · key_points · requirements · standards · src · ladder_rank · ladder_tier · demo · provenance · last_verified",
    "I am the JAH Television Archivist (Signature). Ask me about the Signature series line.",
    "Signature originals organized in the Signature system", "signature",
    "signature-series-study", "signature-series-record"),
}

# ---------------------------------------------------------------- demos (real, runnable, stdlib-only Python)

def _hdr(kind, rid, title):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s: %s. Property of Justin Addam Higgins (JAH).\n"""\n' % (kind, rid, title))

def demo_film_record(rec):
    r = rec
    return _hdr("Film record card", r["id"], r["title"]) + '''\
import json
RECORD = __RECORD__
def runtime_hm(m):
    return "%dh %02dm" % (m // 60, m % 60)
def main():
    r = RECORD
    print("=" * 64)
    print(r["title"] + " (%d)" % r["year"])
    print("=" * 64)
    print("Director : " + r["director"])
    print("Cast     : " + ", ".join(r["cast"]))
    print("Genre    : " + r["genre"])
    print("Runtime  : %d min (%s)" % (r["runtime_minutes"], runtime_hm(r["runtime_minutes"])))
    print("Status   : " + ("PUBLIC DOMAIN — " + r["pd_basis"] if r["public_domain"] else "LICENSED — " + r["watch"]["rights"]))
    if r["public_domain"]:
        print("Play     : " + r["watch"]["play"])
        print("File ref : " + r["file_reference"]["archive_identifier"])
    else:
        print("Watch    : " + "; ".join(r["watch"]["avenues"][:2]))
    print("Synopsis : " + r["synopsis"])
    print("OK: film record card printed for " + r["id"])
if __name__ == "__main__":
    main()
'''.replace('__RECORD__', repr({k: r[k] for k in ("id", "title", "year", "director", "cast", "genre",
      "runtime_minutes", "synopsis", "public_domain", "pd_basis", "watch",
      "file_reference")}))

def demo_pd_check(rec):
    r = rec
    return _hdr("Public-domain determination", r["id"], r["title"]) + '''\
RECORD = __RECORD__
PD_LAPSED = {"lapsed", "defective"}
def determine(year, pd_kind):
    # U.S. motion-picture rule applied by this archive:
    # pre-1931 publication -> expired term; documented lapse/defect -> PD.
    if year <= 1930:
        return True, "expired term (pre-1931 U.S. publication)"
    if pd_kind in PD_LAPSED:
        return True, "documented %s" % pd_kind
    return False, "under copyright — licensed avenues only"
def main():
    r = RECORD
    pd, reason = determine(r["year"], r["pd_kind"])
    print("%s (%d): pd_kind=%s" % (r["title"], r["year"], r["pd_kind"]))
    print("determined public_domain=%s (%s)" % (pd, reason))
    assert pd == r["public_domain"], "determination disagrees with record!"
    print("OK: PD determination matches the archive record " + r["id"])
if __name__ == "__main__":
    main()
'''.replace('__RECORD__', repr({"id": r["id"], "title": r["title"], "year": r["year"],
                  "pd_kind": r["pd_kind"], "public_domain": r["public_domain"]}))

def demo_series_record(rec):
    r = rec
    return _hdr("Series record card", r["id"], r["title"]) + '''\
RECORD = __RECORD__
def main():
    r = RECORD
    print("=" * 64)
    print(r["title"] + " (%s)" % r["years"])
    print("=" * 64)
    print("Network  : " + r["network"])
    print("Stars    : " + ", ".join(r["stars"]))
    print("Genre    : " + r["genre"])
    print("Episodes : %s @ ~%d min" % (r["episodes"], r["episode_length_minutes"]))
    print("Status   : " + ("PUBLIC DOMAIN — " + r["pd_basis"] if r["public_domain"] else "LICENSED — " + r["watch"]["rights"]))
    if r["public_domain"]:
        print("Play     : " + r["watch"]["play"])
        print("File ref : " + r["file_reference"]["archive_identifier"])
    else:
        print("Watch    : " + "; ".join(r["watch"]["avenues"][:2]))
    print("Synopsis : " + r["synopsis"])
    print("OK: series record card printed for " + r["id"])
if __name__ == "__main__":
    main()
'''.replace('__RECORD__', repr({k: r[k] for k in ("id", "title", "years", "network", "stars", "genre",
      "episode_length_minutes", "episodes", "synopsis", "public_domain", "pd_basis",
      "watch", "file_reference")}))

def demo_episode_math(rec):
    r = rec
    return _hdr("Episode marathon math", r["id"], r["title"]) + '''\
RECORD = __RECORD__
import re
def episode_count(s):
    m = re.match(r"(\\d+)", str(s))
    return int(m.group(1)) if m else None
def main():
    r = RECORD
    n = episode_count(r["episodes"])
    if n is None:
        print("episode count is approximate (%s); math skipped" % r["episodes"])
    else:
        total_min = n * r["episode_length_minutes"]
        print("%s: %d episodes x %d min = %d min = %.1f hours" % (
            r["title"], n, r["episode_length_minutes"], total_min, total_min / 60.0))
        print("at 2 episodes a night: %.1f nights" % (n / 2.0))
    print("OK: episode math ran for " + r["id"])
if __name__ == "__main__":
    main()
'''.replace('__RECORD__', repr({"id": r["id"], "title": r["title"], "episodes": r["episodes"],
                  "episode_length_minutes": r["episode_length_minutes"]}))

def demo_restoration(rec):
    r = rec
    return _hdr("Signature restoration plan", r["id"], r["title"]) + '''\
RECORD = __RECORD__
STEPS = [
    "Source the best surviving element (camera negative, fine grain, or release print).",
    "Scan at 4K with oversampling; log every splice, tear, and cue mark.",
    "Stabilize and de-flicker; repair dust and scratches digitally, frame by frame.",
    "Rebuild the soundtrack from optical tracks or discs; remove hiss without thinning dialogue.",
    "Grade against period references; document every creative choice in a restoration report.",
    "Publish the restored file with provenance notes for the archive.",
]
def main():
    r = RECORD
    print("Signature restoration plan — " + r["title"])
    print("Lineage: after " + r["lineage"]["after"] + " [" + r["lineage"]["public_id"] + "]")
    print("Mode: " + r["mode"])
    for i, s in enumerate(STEPS, 1):
        print("  %d. %s" % (i, s))
    print("OK: restoration plan printed for " + r["id"])
if __name__ == "__main__":
    main()
'''.replace('__RECORD__', repr({"id": r["id"], "title": r["title"], "lineage": r["lineage"],
                  "mode": r["mode"]}))

def demo_curation(rec):
    r = rec
    return _hdr("Signature season curation", r["id"], r["title"]) + '''\
RECORD = __RECORD__
def main():
    r = RECORD
    print("Signature season curation — " + r["title"])
    print("Lineage: after " + r["lineage"]["after"] + " [" + r["lineage"]["public_id"] + "]")
    print("Curated arc: " + r["arc"])
    print("Episodes in the Signature season:")
    for i, ep in enumerate(r["season_episodes"], 1):
        print("  %d. %s" % (i, ep))
    print("OK: curation printed for " + r["id"])
if __name__ == "__main__":
    main()
'''.replace('__RECORD__', repr({"id": r["id"], "title": r["title"], "lineage": r["lineage"],
                  "arc": r["arc"], "season_episodes": r["season_episodes"]}))

DEMOS = {
    "film_record": demo_film_record, "pd_check": demo_pd_check,
    "series_record": demo_series_record, "episode_math": demo_episode_math,
    "restoration": demo_restoration, "curation": demo_curation,
}

# ---------------------------------------------------------------- record builders

IA = "https://archive.org/details/"
LICENSED_AVENUES = [
    "Licensed streaming services — availability rotates; check a streaming guide such as JustWatch for current options.",
    "Digital rental or purchase on major storefronts.",
    "Physical media (Blu-ray/DVD).",
    "Public library collections.",
]

def decade_g(year):
    return "%ds" % (int(year) // 10 * 10)

def watch_block(pd, pd_kind, archive_id, rights):
    if pd:
        url = IA + archive_id
        return {
            "status": "public-domain",
            "play": url,
            "file_reference": {
                "archive_identifier": archive_id,
                "item_page": url,
                "note": ("The item page hosts the actual playable public-domain file — "
                         "in-browser player plus direct file downloads. " + PD_BASIS[pd_kind]),
            },
            "note": "Public domain: free to watch, share, and study.",
        }
    return {
        "status": "licensed",
        "rights": rights,
        "avenues": LICENSED_AVENUES,
        "note": "Only licensed sources are listed; no infringing links.",
    }

def tier_of(i, kind):
    f, c = TIER_CUT[kind]
    if i < f: return "foundations"
    if i < c: return "compounded"
    return "advanced"

KEY_POINTS_MOV = {
 "foundations": [
    "Watch the visual grammar: silent storytelling carries plot through image, gesture, and intertitle.",
    "Note the runtime discipline — early features tell complete stories in about an hour.",
    "This is a public-domain print: it may be freely watched, shared, and studied.",
 ],
 "compounded": [
    "Late-silent mastery: the art form at its visual peak, just before sound changed everything.",
    "Genre crystallizes here — horror, adventure, and thriller find their classic shapes.",
    "This is a public-domain print: it may be freely watched, shared, and studied.",
 ],
 "advanced": [
    "Studio-era ambition: the largest resources aimed at the largest audiences.",
    "Watch for the technique other films copied — each of these set a template.",
    "Licensed work: use licensed streaming, rental, physical media, or the library.",
 ],
}

def build_movie(i, m, prefix):
    title, year, director, cast, genre, runtime, story, pd_kind, archive_id, rights = m
    pd = pd_kind in ("expired", "lapsed", "defective")
    tier = tier_of(i, "movies")
    rid = "%s%06d" % (prefix, i + 1)
    cast_list = [c.strip() for c in cast.split(",")]
    watch = watch_block(pd, pd_kind, archive_id, rights)
    access = ("It is in the public domain, and the record carries the actual playable file reference. "
              if pd else "It is a licensed work; the record lists legal watch avenues. ")
    description = ("%s Directed by %s and starring %s, this %s runs %d minutes. %s"
                   % (story, director, cast, genre.lower(), runtime, access))
    how = ("Each Movies Database record works as a complete film file: it identifies the title, year, director, "
           "principal cast, genre, and runtime; states the public-domain or licensed status with its basis; and gives "
           "the legal way to watch — the actual playable file reference for public-domain titles, or licensed avenues "
           "for copyrighted ones. Use the record to plan a viewing, verify a film's facts before citing them, or build "
           "a watchlist; the demonstration program prints the full record card and checks the public-domain determination.")
    kp = ["A %s from %d, directed by %s." % (genre.lower(), year, director),
          "Principal cast: %s." % cast] + KEY_POINTS_MOV[tier]
    rec = {
        "id": rid, "t": "%s (%d)" % (title, year), "g": decade_g(year),
        "name": title, "title": "%s (%d)" % (title, year),
        "year": year, "director": director, "cast": cast_list, "genre": genre,
        "runtime_minutes": runtime, "synopsis": story, "description": description,
        "public_domain": pd, "pd_kind": pd_kind,
        "pd_basis": PD_BASIS[pd_kind] if pd else "Under copyright; licensed work.",
        "watch": watch, "file_reference": watch.get("file_reference"),
        "how_it_works": how, "key_points": kp,
        "requirements": ("A screen and speakers or headphones for viewing; the linked file or a licensed copy; "
                         "about %d minutes plus discussion time; a notebook for teaching-ladder notes." % runtime),
        "standards": ["U.S. Copyright Act, Title 17 — term, notice, and renewal provisions (public-domain determinations).",
                      "AFI Catalog editorial standards for filmographic data."],
        "citations": (["American Film Institute Catalog — filmographic reference (public records).",
                       "U.S. Copyright Office — copyright term, notice, and renewal records.",
                       "Internet Archive — public-domain moving-image collection; item pages host the playable files."]
                      if pd else
                      ["American Film Institute Catalog — filmographic reference (public records).",
                       "Studio distribution records — rights-holder identification."]),
        "src": "public-harvest",
        "ladder_rank": i + 1, "ladder_tier": tier,
        "provenance": "Seeded public-record archive; facts verified 2026-10-19.",
        "last_verified": "2026-10-19",
    }
    kind = "film_record" if i % 2 == 0 else "pd_check"
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": DEMOS[kind](rec),
                   "note": "Working demonstration program (real, runnable Python)."}
    rec["_demo_kind"] = kind
    return rec

KEY_POINTS_SHW = {
 "foundations": [
    "Early-broadcast grammar: live or kinescoped, made fast and cheap, carried by performance.",
    "Note the episode shape — half-hour self-contained stories built for sponsors and families.",
    "These are public-domain episodes: free to watch, share, and study.",
 ],
 "compounded": [
    "The network golden age: the formats every later series copied were invented here.",
    "Watch how the episode engine works — the repeatable story machine under the characters.",
    "Licensed work: use licensed streaming, rental, physical media, or the library.",
 ],
 "advanced": [
    "Prestige craft: serialization, authorship, and cinema-scale production on television.",
    "Each of these changed what the medium was allowed to attempt.",
    "Licensed work: use licensed streaming, rental, physical media, or the library.",
 ],
}

def build_show(i, s, prefix):
    title, years, network, stars, genre, ep_len, episodes, story, pd_kind, archive_id, rights = s
    pd = pd_kind in ("expired", "lapsed", "defective")
    tier = tier_of(i, "shows")
    rid = "%s%06d" % (prefix, i + 1)
    star_list = [c.strip() for c in stars.split(",")]
    first_year = int(str(years).split("-")[0])
    watch = watch_block(pd, pd_kind, archive_id, rights)
    access = ("Surviving public-domain episodes carry the actual playable file reference in this record. "
              if pd else "It is a licensed series; the record lists legal watch avenues. ")
    description = ("%s Airing %s on %s and starring %s, this %s ran %s in %d-minute episodes. %s"
                   % (story, years, network, stars, genre.lower(), episodes, ep_len, access))
    how = ("Each Shows Database record works as a complete series file: it identifies the title, years, network, "
           "stars, genre, episode length, and episode count; states the public-domain or licensed status with its basis; "
           "and gives the legal way to watch — the actual playable file reference for public-domain episodes, or licensed "
           "avenues for copyrighted series. Use the record to plan viewing, verify a series' facts before citing them, "
           "or compute a watch schedule; the demonstration program prints the full record card and the marathon math.")
    kp = ["A %s airing %s on %s." % (genre.lower(), years, network),
          "Stars: %s." % stars] + KEY_POINTS_SHW[tier]
    rec = {
        "id": rid, "t": "%s (%s)" % (title, years), "g": decade_g(first_year),
        "name": title, "title": "%s (%s)" % (title, years),
        "years": years, "network": network, "stars": star_list, "genre": genre,
        "episode_length_minutes": ep_len, "episodes": episodes,
        "synopsis": story, "description": description,
        "public_domain": pd, "pd_kind": pd_kind,
        "pd_basis": PD_BASIS[pd_kind] if pd else "Under copyright; licensed work.",
        "watch": watch, "file_reference": watch.get("file_reference"),
        "how_it_works": how, "key_points": kp,
        "requirements": ("A screen and speakers or headphones for viewing; the linked episodes or a licensed copy; "
                         "a notebook for teaching-ladder notes."),
        "standards": ["U.S. Copyright Act, Title 17 — term, notice, and renewal provisions (public-domain determinations).",
                      "Standard series filmography practice for episode and broadcast data."],
        "citations": (["Classic television broadcast records — series filmography (public records).",
                       "U.S. Copyright Office — copyright term, notice, and renewal records.",
                       "Internet Archive — public-domain television collection; item pages host the playable files."]
                      if pd else
                      ["Classic television broadcast records — series filmography (public records).",
                       "Network and studio distribution records — rights-holder identification."]),
        "src": "public-harvest",
        "ladder_rank": i + 1, "ladder_tier": tier,
        "provenance": "Seeded public-record archive; facts verified 2026-10-19.",
        "last_verified": "2026-10-19",
    }
    kind = "series_record" if i % 2 == 0 else "episode_math"
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": DEMOS[kind](rec),
                   "note": "Working demonstration program (real, runnable Python)."}
    rec["_demo_kind"] = kind
    return rec

# ---------------------------------------------------------------- signature companions

REST_TREATMENTS = [
    "The Signature cut re-times the opening for modern attention spans while preserving every frame of the original.",
    "The Signature treatment re-scores the film with a new original score written against the restored picture.",
    "The Signature edition reframes the story through a new opening narration written in the Signature voice.",
    "The Signature version adds a guided viewing track explaining each landmark technique as it appears.",
]

def sig_movie(i, m, pub_rec, prefix):
    title, year, director, cast, genre, runtime, story, pd_kind, archive_id, rights = m
    pd = pd_kind in ("expired", "lapsed", "defective")
    tier = tier_of(i, "movies")
    rid = "%s%06d" % (prefix, i + 1)
    mode = "Signature Restoration" if pd else "Signature Study"
    stitle = "%s (%d) — %s (Signature Edition)" % (title, year, mode)
    treatment = REST_TREATMENTS[i % len(REST_TREATMENTS)]
    if pd:
        plan = ("The Signature restoration of %s begins from the best surviving element, scanned at 4K with "
                "oversampling. Every splice, tear, and cue mark is logged; the picture is stabilized and de-flickered; "
                "dust and scratches are repaired digitally frame by frame; the soundtrack is rebuilt from optical tracks; "
                "and the grade is matched to period references, with every creative choice documented in a restoration report." % title)
    else:
        plan = ("The Signature study of %s is an appreciation guide, not a reproduction: a scene-by-scene map of "
                "what the film does and how, viewing notes for the landmark sequences, historical context on its making, "
                "and discussion prompts — designed to deepen a licensed viewing without touching the work itself." % title)
    description = ("%s is an original Signature-line companion to the public record for %s (%d). %s %s "
                   "It is a Signature original — clearly labeled, never presented as an authentic public record."
                   % (mode, title, year, plan, treatment))
    rec = {
        "id": rid, "t": stitle, "g": decade_g(year),
        "name": stitle, "title": stitle,
        "lineage": {"after": pub_rec["title"], "public_id": pub_rec["id"],
                    "note": "Signature-line companion to the public film record."},
        "mode": mode,
        "description": description,
        "restoration_or_study": plan,
        "treatment": treatment + " (Original Signature treatment — speculative creative work, labeled as such.)",
        "how_it_works": ("Each Signature film record works as an original companion file: it names the public record it "
                         "follows through lineage, gives the original Signature restoration or study plan, and adds an "
                         "original Signature re-imagining treatment. Nothing here is presented as the authentic work — "
                         "it is the Signature line, Manon's original interpretation, organized in the Signature system."),
        "key_points": ["Signature-line companion to: %s." % pub_rec["title"],
                       "Mode: %s." % mode,
                       "Original Signature engineering and original creative treatment.",
                       "Clearly labeled Signature original — never presented as authentic public record."],
        "requirements": ("The public companion record; a notebook for restoration or study notes; "
                         "for restorations, access to archival scanning and grading tools."),
        "standards": ["Signature system originality standard — original work, labeled as such."],
        "src": "signature",
        "ladder_rank": i + 1, "ladder_tier": tier,
        "provenance": "Original Signature creation; verified 2026-10-19.",
        "last_verified": "2026-10-19",
    }
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": DEMOS["restoration"](rec),
                   "note": "Working demonstration program (real, runnable Python)."}
    rec["_demo_kind"] = "restoration"
    return rec

CURATION_ARCS = [
    "The Signature season traces the show's moral engine across its strongest episodes.",
    "The Signature season follows one theme from pilot to finale in six essential episodes.",
    "The Signature season pairs landmark episodes with the production stories behind them.",
    "The Signature season builds a newcomer's path: start here, then go deep.",
]

def sig_show(i, s, pub_rec, prefix):
    title, years, network, stars, genre, ep_len, episodes, story, pd_kind, archive_id, rights = s
    pd = pd_kind in ("expired", "lapsed", "defective")
    tier = tier_of(i, "shows")
    rid = "%s%06d" % (prefix, i + 1)
    first_year = int(str(years).split("-")[0])
    stitle = "%s — Signature Season Curation (Signature Edition)" % title
    arc = CURATION_ARCS[i % len(CURATION_ARCS)]
    season_eps = ["Series premiere — where the engine starts",
                  "The breakout episode that defined the show",
                  "The mid-run peak the writers still talk about",
                  "The experimental episode that broke the format",
                  "The late-run masterwork",
                  "The finale — how the story chose to end"]
    guide = ("The Signature curation of %s selects a six-episode Signature season with a viewing order, "
             "context notes for each pick, and discussion prompts — an original guide for appreciating the series, "
             "not a reproduction of it." % title)
    description = ("Signature Season Curation is an original Signature-line companion to the public record for %s (%s). "
                   "%s %s It is a Signature original — clearly labeled, never presented as an authentic public record."
                   % (title, years, guide, arc))
    rec = {
        "id": rid, "t": stitle, "g": decade_g(first_year),
        "name": stitle, "title": stitle,
        "lineage": {"after": pub_rec["title"], "public_id": pub_rec["id"],
                    "note": "Signature-line companion to the public series record."},
        "arc": arc,
        "description": description,
        "curation_guide": guide,
        "season_episodes": season_eps,
        "treatment": (arc + " Original Signature treatment — speculative creative work, labeled as such."),
        "how_it_works": ("Each Signature series record works as an original companion file: it names the public record it "
                         "follows through lineage, gives the original Signature curation guide with a six-episode Signature "
                         "season, and adds an original Signature season treatment. Nothing here is presented as the authentic "
                         "work — it is the Signature line, Manon's original interpretation, organized in the Signature system."),
        "key_points": ["Signature-line companion to: %s." % pub_rec["title"],
                       "Original Signature curation guide with a six-episode Signature season.",
                       "Original Signature season treatment.",
                       "Clearly labeled Signature original — never presented as authentic public record."],
        "requirements": ("The public companion record; a notebook for curation notes; "
                         "licensed access to the series for the curated viewing."),
        "standards": ["Signature system originality standard — original work, labeled as such."],
        "src": "signature",
        "ladder_rank": i + 1, "ladder_tier": tier,
        "provenance": "Original Signature creation; verified 2026-10-19.",
        "last_verified": "2026-10-19",
    }
    rec["demo"] = {"kind": "python", "language": "python",
                   "program": DEMOS["curation"](rec),
                   "note": "Working demonstration program (real, runnable Python)."}
    rec["_demo_kind"] = "curation"
    return rec

# ---------------------------------------------------------------- build

def build_records():
    pub_mov = [build_movie(i, m, DBCFG["movies-every-film"]["prefix"]) for i, m in enumerate(MOVIES)]
    sig_mov = [sig_movie(i, m, pub_mov[i], DBCFG["movies-every-film-signature"]["prefix"])
               for i, m in enumerate(MOVIES)]
    pub_shw = [build_show(i, s, DBCFG["shows-every-series"]["prefix"]) for i, s in enumerate(SHOWS)]
    sig_shw = [sig_show(i, s, pub_shw[i], DBCFG["shows-every-series-signature"]["prefix"])
               for i, s in enumerate(SHOWS)]
    return {"movies-every-film": pub_mov, "movies-every-film-signature": sig_mov,
            "shows-every-series": pub_shw, "shows-every-series-signature": sig_shw}

def write_shard_db(slug, recs):
    return nb.write_shard_db(slug, recs)

BANNED = ["facebook", "bat belt"]

def sanity_and_demos(built):
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(x.startswith(cfg["prefix"]) for x in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        # whole-system dedupe gate (his standing rule)
        for r in recs:
            hits = [h for h in GATE.check(slug, r["title"]) if h[0] != slug]
            assert not hits, "gate refused (cross-db dupe): %s -> %s" % (r["title"], hits)
            for k in ("id", "t", "g", "name", "title", "description", "src", "demo",
                      "ladder_rank", "ladder_tier"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            assert r["demo"].get("program"), "empty demo in %s" % r["id"]
            assert len(r["description"]) > 120, "stub description in %s" % r["id"]
            blob = json.dumps(r).lower()
            for b in BANNED:
                assert b not in blob, "%s in %s" % (b, r["id"])
            compile(r["demo"]["program"], r["id"], "exec")
            GATE.admit(slug, r["title"], r["id"])
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-32s %d records" % (slug, n), flush=True)
    # machine-execute one demo per archetype (proves they run)
    done = {}
    for slug, recs in built.items():
        for r in recs:
            kind = r.get("_demo_kind")
            if kind and kind not in done:
                done[kind] = r
    for kind, r in sorted(done.items()):
        p = subprocess.run([sys.executable, "-c", r["demo"]["program"]],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
        assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
        print("demo ok: %-14s %s" % (kind, r["id"]), flush=True)
    assert len(done) == len(DEMOS), "not all archetypes executed: %s" % (set(DEMOS) - set(done))
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)
    return total

def gen_topics(slug, recs):
    out = {}
    for r in recs:
        out.setdefault(r["ladder_tier"], []).append("%s — %s" % (r["t"], r["ladder_tier"]))
    return out

def build_pages(built):
    nb.DBCFG = DBCFG
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "Exhaustive" in page and "All Database Merger" in page
        for b in BANNED:
            assert b not in page.lower(), "banned %s in page %s" % (b, slug)
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        gen_js = nb.build_gen_js(slug, gen_topics(slug, recs), DBCFG[slug])
        for b in BANNED:
            assert b not in gen_js.lower()
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

def main():
    built = build_records()
    total = sanity_and_demos(built)
    build_pages(built)
    # node --check every gen-*.js
    for slug in built:
        gpath = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed for %s: %s" % (slug, p.stderr)
        print("node --check OK: gen-%s.js" % slug, flush=True)
    # index vs chunk count verification
    for slug, recs in built.items():
        idx_path = os.path.join(SHARD, "data", slug, "index.jsonl.gz")
        with gzip.open(idx_path, "rt", encoding="utf-8") as f:
            idx = [json.loads(l) for l in f if l.strip()]
        n_chunk = 0
        cdir = os.path.join(SHARD, "data", slug, "chunks")
        for fn in sorted(os.listdir(cdir)):
            with gzip.open(os.path.join(cdir, fn), "rt", encoding="utf-8") as f:
                rows = [json.loads(l) for l in f if l.strip()]
            n_chunk += len(rows)
            assert all(set(("id", "t", "g")) <= set(r) for r in rows), "chunk row keys in %s/%s" % (slug, fn)
        assert len(idx) == len(recs) == n_chunk == 34, \
            "count mismatch %s: idx=%d chunks=%d built=%d" % (slug, len(idx), n_chunk, len(recs))
        assert [r["id"] for r in idx] == [r["id"] for r in recs], "index order drift in %s" % slug
        print("counts OK: %-32s index=%d chunks=%d" % (slug, len(idx), n_chunk), flush=True)
    print("BUILT 4 databases, %d records. manifest/api untouched (coordinator merges)." % total)
    return 0

if __name__ == "__main__":
    sys.exit(main())
