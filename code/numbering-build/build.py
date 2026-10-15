#!/usr/bin/env python3
"""Build the 4 numbering-plan databases for JAH Databases.

Public: public-area-codes (NANP), public-country-calling-codes (ITU),
        public-zip-codes (USPS, seed block + drip pattern).
Signature: signature-numbering-plan (Manon's original Signature scheme).

Reads: nanp.json, countrycodes.json (research extraction),
       zip_seed.py, signature_plan.py (same directory).
Writes (shard repo jah-databases-data-1, Pages-enabled):
       data/<slug>/index.jsonl.gz + data/<slug>/chunks/chunk-NNNN.jsonl.gz
Writes (main repo): db/<slug>/index.html, db/<slug>/gen-<slug>.js
Updates (main repo): data/manifest.json (append 4), api.json (append 4).
After this runs, the parent runs code/restamp_counts.py, commits, and pushes.
"""
import gzip
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))  # ~/workspace/jah-databases
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"

sys.path.insert(0, HERE)
from zip_seed import CITY_BLOCKS, FAMOUS
from signature_plan import SIGNATURE_PLAN

STATE_TZ = {
    "AL": ["Central"], "AK": ["Alaska"], "AZ": ["Mountain"], "AR": ["Central"],
    "CA": ["Pacific"], "CO": ["Mountain"], "CT": ["Eastern"], "DE": ["Eastern"],
    "DC": ["Eastern"], "FL": ["Eastern", "Central"], "GA": ["Eastern"],
    "HI": ["Hawaii"], "ID": ["Mountain", "Pacific"], "IL": ["Central"],
    "IN": ["Eastern", "Central"], "IA": ["Central"], "KS": ["Central"],
    "KY": ["Eastern", "Central"], "LA": ["Central"], "ME": ["Eastern"],
    "MD": ["Eastern"], "MA": ["Eastern"], "MI": ["Eastern"], "MN": ["Central"],
    "MS": ["Central"], "MO": ["Central"], "MT": ["Mountain"], "NE": ["Central", "Mountain"],
    "NV": ["Pacific"], "NH": ["Eastern"], "NJ": ["Eastern"], "NM": ["Mountain"],
    "NY": ["Eastern"], "NC": ["Eastern"], "ND": ["Central"], "OH": ["Eastern"],
    "OK": ["Central"], "OR": ["Pacific"], "PA": ["Eastern"], "RI": ["Eastern"],
    "SC": ["Eastern"], "SD": ["Central", "Mountain"], "TN": ["Central", "Eastern"],
    "TX": ["Central", "Mountain"], "UT": ["Mountain"], "VT": ["Eastern"],
    "VA": ["Eastern"], "WA": ["Pacific"], "WV": ["Eastern"], "WI": ["Central"],
    "WY": ["Mountain"], "PR": ["Atlantic"], "VI": ["Atlantic"], "GU": ["Chamorro"],
    "AS": ["Samoa"], "MP": ["Chamorro"],
}
STATE_NAME = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "DC": "District of Columbia", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana",
    "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
    "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
    "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
    "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming", "PR": "Puerto Rico", "VI": "U.S. Virgin Islands",
    "GU": "Guam", "AS": "American Samoa", "MP": "Northern Mariana Islands",
}
# Area-code -> timezone overrides (region-specific, from the code's actual footprint)
AC_TZ_OVERRIDE = {
    "850": ["Central"], "448": ["Central"], "915": ["Mountain"],
    "219": ["Central"], "812": ["Eastern", "Central"], "270": ["Central"],
    "423": ["Eastern"], "208": ["Mountain", "Pacific"], "308": ["Mountain"],
    "605": ["Central", "Mountain"], "867": ["Mountain", "Central", "Eastern"],
    "242": ["Eastern"], "246": ["Atlantic"], "264": ["Atlantic"], "268": ["Atlantic"],
    "284": ["Atlantic"], "340": ["Atlantic"], "345": ["Eastern"], "441": ["Atlantic"],
    "473": ["Atlantic"], "649": ["Eastern"], "664": ["Atlantic"], "671": ["Chamorro"],
    "684": ["Samoa"], "721": ["Atlantic"], "767": ["Atlantic"], "784": ["Atlantic"],
    "787": ["Atlantic"], "939": ["Atlantic"], "809": ["Atlantic"], "829": ["Atlantic"],
    "849": ["Atlantic"], "868": ["Atlantic"], "869": ["Atlantic"], "876": ["Eastern"],
    "658": ["Eastern"], "758": ["Atlantic"],
}
CA_PROV_TZ = {
    "Ontario": ["Eastern"], "Quebec": ["Eastern"], "British Columbia": ["Pacific"],
    "Alberta": ["Mountain"], "Manitoba": ["Central"], "Saskatchewan": ["Central"],
    "Nova Scotia": ["Atlantic"], "New Brunswick": ["Atlantic"],
    "Newfoundland and Labrador": ["Newfoundland"], "Prince Edward Island": ["Atlantic"],
    "Yukon": ["Mountain"], "Northwest Territories": ["Mountain"], "Nunavut": ["Eastern", "Central", "Mountain"],
}
US_STATE_NAMES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii",
    "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
    "Wisconsin", "Wyoming"]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def tz_display(tzs):
    return tzs[0] if len(tzs) == 1 else ", ".join(tzs)


def ac_timezones(rec):
    code = rec["code"]
    if code in AC_TZ_OVERRIDE:
        return AC_TZ_OVERRIDE[code]
    country = rec.get("country", "")
    region = rec.get("region", "")
    if country == "Canada":
        for prov, tzs in CA_PROV_TZ.items():
            if prov in region:
                return tzs
        return ["Eastern"]
    for abbr, name in STATE_NAME.items():
        if name in region and abbr not in ("PR", "VI", "GU", "AS", "MP"):
            return STATE_TZ[abbr]
    return ["Eastern"]


def ac_place(region, country):
    if not region:
        return country
    if region == country or country in region:
        return region
    return "%s, %s" % (region, country)


def ac_group(rec):
    """Browse group for an area code record."""
    if rec["type"] in ("toll-free", "premium", "non-geographic", "special"):
        return "Toll-free & special"
    region = rec.get("region", "")
    country = rec.get("country", "")
    if country == "Canada":
        if "Northwest Territories" in region or "Nunavut" in region:
            return "Northern Territories"
        for prov in CA_PROV_TZ:
            if prov in region:
                return prov
        return "Canada — other"
    if country not in ("United States", "Canada"):
        return country
    if "D.C." in region or "District of Columbia" in region:
        return "District of Columbia"
    for name in US_STATE_NAMES:
        if name in region:
            return name
    return "United States — other"


CIT_NANP = ["North American Numbering Plan Administrator — area code assignment records (public numbering resources)."]
CIT_ITU = ["ITU-T E.164 — international public telecommunication numbering plan: country calling code assignments."]
CIT_USPS = ["United States Postal Service — ZIP Code system records."]

# ---------------------------------------------------------------- record builders

def ac_demo(code, region, country, tz, typ):
    r = {"code": code, "region": region, "country": country,
         "timezone": tz_display(tz) if tz else "—", "type": typ}
    prog = [
        "# Area Code Dialer — %s (%s)" % (code, region),
        "# Dialing summary and format check for this archive record.",
        "record = %r" % (r,),
        "def dial_summary(r):",
        "    return '1-' + r['code'] + '-XXX-XXXX | ' + r['region'] + ' (' + r['country'] + ')'",
        "def valid_npa(c):",
        "    return len(c) == 3 and c.isdigit() and c[0] in '23456789'",
        "print(dial_summary(record))",
        "print('NPA format valid:', valid_npa(record['code']))",
        "print('Type:', record['type'], '| Time zone:', record['timezone'])",
    ]
    return {"kind": "area-code-dialer", "language": "python",
            "program": "\n".join(prog) + "\n",
            "note": "Archive record dialer — prints this code's dialing summary."}


def build_area_codes(nanp):
    recs = []
    for i, e in enumerate(sorted(nanp, key=lambda x: x["code"])):
        code = e["code"]
        region = e.get("region") or ""
        country = e.get("country") or ""
        typ = e.get("type") or "geographic"
        tzs = ac_timezones(e) if typ == "geographic" else []
        ins = e.get("in_service")
        overlays = e.get("overlay_with") or []
        notes = e.get("notes") or ""
        place = ac_place(region, country)
        if typ == "geographic":
            desc = ("Area code %s is a geographic area code serving %s, in the %s Time Zone. "
                    % (code, place, tz_display(tzs)))
        elif typ == "toll-free":
            desc = ("Area code %s is a toll-free area code covering the whole North American Numbering Plan. "
                    "Calls to %s numbers are free to the caller; the called party pays. " % (code, code))
        elif typ == "premium":
            desc = ("Area code %s is a premium-rate area code. Calls to %s numbers are billed at premium rates "
                    "set by the service provider. " % (code, code))
        elif typ == "non-geographic":
            desc = ("Area code %s is a non-geographic area code used for personal communications services that "
                    "are not tied to a place. " % code)
        else:
            desc = ("Area code %s is a special-purpose code in the North American Numbering Plan. " % code)
        if ins:
            desc += "It has been in service since %s. " % ins
        else:
            desc += "The assignment records do not list an in-service date for this code. "
        if overlays:
            desc += ("It shares its region with area code%s %s; ten-digit dialing is used throughout the overlay. "
                     % ("s" if len(overlays) > 1 else "", ", ".join(overlays)))
        elif typ == "geographic":
            desc += "It is currently the only area code for its region. "
        if notes:
            desc += notes.strip()
            if not desc.endswith("."):
                desc += "."
        desc = desc.strip()
        if typ in ("toll-free", "premium", "non-geographic", "special"):
            dialing = "Dial 1 + %s + the seven-digit number." % code
        else:
            dialing = "Dial 1 + %s + the seven-digit number from outside the region." % code
        rec = {
            "id": "JAH-AC-%06d" % (i + 1),
            "t": "%s — %s" % (code, region or country),
            "g": ac_group({"type": typ, "region": region, "country": country}),
            "name": "Area code %s" % code,
            "title": "%s — %s" % (code, region or country),
            "code": code, "region": region, "country": country,
            "timezones": tzs, "overlay_with": overlays,
            "in_service": ins, "type": typ,
            "description": desc, "dialing": dialing,
            "citations": CIT_NANP, "src": "public-harvest",
            "demo": ac_demo(code, region, country, tzs, typ),
        }
        recs.append(rec)
    return recs


def cc_demo(code, country, trunk, region):
    r = {"code": code, "country": country, "trunk": trunk or "", "region": region or ""}
    prog = [
        "# Country Code Dialer — %s (%s)" % (code, country),
        "# International dialing format for this archive record.",
        "record = %r" % (r,),
        "def drop_trunk(national, trunk):",
        "    return national[len(trunk):] if trunk and national.startswith(trunk) else national",
        "def intl_dial(r, national):",
        "    return '+' + r['code'].lstrip('+') + ' ' + drop_trunk(national, r['trunk'])",
        "print(intl_dial(record, (record['trunk'] or '') + '5550134'))",
        "print('# 555-0134 is an illustrative number, not a real subscriber.')",
        "print('Country:', record['country'], '| Region:', record['region'] or '—')",
    ]
    return {"kind": "country-code-dialer", "language": "python",
            "program": "\n".join(prog) + "\n",
            "note": "Archive record dialer — prints this code's international format."}


def cc_region_group(region):
    r = (region or "").lower()
    for key, label in [("europe", "Europe"), ("asia", "Asia"), ("africa", "Africa"),
                       ("north america", "North America"), ("south america", "South America"),
                       ("central america", "Central America"), ("caribbean", "Caribbean"),
                       ("oceania", "Oceania"), ("middle east", "Middle East"),
                       ("antarctica", "Polar & special")]:
        if key in r:
            return label
    return "Other & special"


def build_country_codes(ccs):
    def sortkey(e):
        m = re.match(r"\+(\d+)", e["code"] or "+0")
        return int(m.group(1)) if m else 0
    recs = []
    for i, e in enumerate(sorted(ccs, key=sortkey)):
        code = e["code"]
        country = e.get("country") or ""
        region = e.get("region") or ""
        trunk = e.get("trunk_prefix")
        tstat = e.get("trunk_status", "unlisted")
        notes = e.get("notes") or ""
        desc = ("Country calling code %s is assigned to %s. To dial %s from abroad, dial your international "
                "access code, then %s, then the national number. "
                % (code, country, country, code.lstrip("+")))
        if code == "+1":
            desc = ("Country calling code +1 is shared by the North American Numbering Plan member countries "
                    "(the United States, Canada, and Caribbean NANP members; area codes are listed in the Area Code Database). "
                    "To dial a NANP country from abroad, dial your international access code, then 1, then the area code and number. "
                    "Within NANP countries, the domestic trunk prefix is '1'. ")
            if notes:
                desc += notes.strip()
                if not desc.endswith("."):
                    desc += "."
        elif trunk:
            desc += "Within %s, the domestic trunk prefix is '%s'. " % (country, trunk)
        elif tstat == "none":
            desc += "%s does not use a domestic trunk prefix. " % country
        else:
            desc += "No domestic trunk prefix is listed for %s in the reference records. " % country
        if region:
            desc += "Region: %s. " % region
        if notes:
            desc += notes.strip()
            if not desc.endswith("."):
                desc += "."
        rec = {
            "id": "JAH-CC-%06d" % (i + 1),
            "t": "%s — %s" % (code, country),
            "g": cc_region_group(region),
            "name": "Country calling code %s" % code,
            "title": "%s — %s" % (code, country),
            "code": code, "country": country, "region": region,
            "trunk_prefix": trunk,
            "description": desc.strip(),
            "dialing": "Dial international access + %s + the national number." % code.lstrip("+"),
            "citations": CIT_ITU, "src": "public-harvest",
            "demo": cc_demo(code, country, trunk, region),
        }
        recs.append(rec)
    return recs


def zip_demo(z, city, state, county_disp, ztype, tz):
    r = {"zip": z, "city": city, "state": state, "county": county_disp,
         "type": ztype, "timezone": tz}
    prog = [
        "# ZIP Zone Reader — %s (%s, %s)" % (z, city, state),
        "# Zone structure for this archive record.",
        "record = %r" % (r,),
        "def scf(z): return z[:3]",
        "def national_area(z): return z[0]",
        "print(record['zip'], '->', record['city'] + ',', record['state'], '|', record['county'])",
        "print('Sectional center (first 3 digits):', scf(record['zip']))",
        "print('National area (first digit):', national_area(record['zip']))",
        "print('Type:', record['type'], '| Time zone:', record['timezone'])",
    ]
    return {"kind": "zip-zone-reader", "language": "python",
            "program": "\n".join(prog) + "\n",
            "note": "Archive record reader — prints this ZIP's zone structure."}


def county_display(county, state):
    if state == "PR":
        return county
    if "City" in county or "District" in county:
        return county
    return county + " County"


def build_zips():
    seen = set()
    items = []
    for z, city, state, county, ztype, note in FAMOUS:
        if z in seen:
            continue
        seen.add(z)
        items.append((z, city, state, county, ztype, note))
    for city, state, county, zips in CITY_BLOCKS:
        for z in zips:
            if z in seen:
                continue
            seen.add(z)
            items.append((z, city, state, county, "standard", ""))
    recs = []
    for i, (z, city, state, county, ztype, note) in enumerate(items):
        tz = tz_display(STATE_TZ.get(state, ["Eastern"]))
        cdis = county_display(county, state)
        desc = ("ZIP code %s serves %s, %s, in %s, in the %s Time Zone. "
                % (z, city, state, cdis, tz))
        if ztype == "unique":
            desc += "It is a unique ZIP code assigned to a single entity. "
        elif ztype == "po-box":
            desc += "It is a PO Box ZIP code. "
        if note:
            desc += note.strip()
            if not desc.endswith("."):
                desc += "."
        rec = {
            "id": "JAH-ZIP-%06d" % (i + 1),
            "t": "%s — %s, %s" % (z, city, state),
            "g": STATE_NAME.get(state, state),
            "name": "ZIP code %s" % z,
            "title": "%s — %s, %s" % (z, city, state),
            "code": z, "city": city, "state": state, "county": cdis,
            "type": ztype, "timezone": tz,
            "description": desc.strip(),
            "citations": CIT_USPS, "src": "public-harvest",
            "demo": zip_demo(z, city, state, cdis, ztype, tz),
        }
        recs.append(rec)
    return recs


SIG_CAT_LABEL = {
    "region-code": "Region codes",
    "service-code": "Service codes",
    "exchange-code": "Exchange codes",
    "toll-info-code": "Toll & info codes",
    "offsite-relay-code": "Offsite relay codes",
}


def sig_demo(code, category, name):
    r = {"code": code, "category": category, "name": name}
    prog = [
        "# Signature Numbering Plan — %s (%s)" % (code, name),
        "# Original Signature numbering record.",
        "record = %r" % (r,),
        "def dial_plan(r):",
        "    return 'Dial ' + r['code'] + ' + local Signature number'",
        "print(record['code'], '-', record['name'])",
        "print(dial_plan(record))",
        "print('Category:', record['category'])",
    ]
    return {"kind": "signature-numbering", "language": "python",
            "program": "\n".join(prog) + "\n",
            "note": "Signature original — prints this code's dialing plan."}


def build_signature():
    recs = []
    for i, (code, category, name, purpose, dialing, notes) in enumerate(SIGNATURE_PLAN):
        desc = ("%s is part of the original Signature numbering plan. %s %s"
                % (name, purpose.strip(), dialing.strip()))
        if notes:
            desc += " " + notes.strip()
        rec = {
            "id": "JAH-SNP-%06d" % (i + 1),
            "t": "%s — %s" % (code, name),
            "g": SIG_CAT_LABEL[category],
            "name": name, "title": "%s — %s" % (code, name),
            "code": code, "category": category,
            "purpose": purpose, "dialing": dialing, "notes": notes,
            "description": desc.strip(),
            "src": "signature",
            "demo": sig_demo(code, category, name),
        }
        recs.append(rec)
    return recs

# ---------------------------------------------------------------- page + generator writers

DBCFG = {
    "public-area-codes": {
        "name": "Area Code Database",
        "tagline": "Every North American Numbering Plan area code — code, region, country, time zone, overlays, in-service date, and type. Full records, fact-checked. Public records organized in the Signature system.",
        "record_kind": "area code record",
        "prefix": "JAH-AC-",
        "ai": "JAH Area Code Archivist",
        "role": "area code archivist — NANP area codes, regions, overlays, dialing",
        "hero_p": "North American <b>area codes</b> — <b>regions</b>, <b>overlays</b>, <b>time zones</b>, and <b>dialing</b>. Every code in the North American Numbering Plan, organized in the Signature system. Every record carries the full entry: code, region, country, time zone, overlays, in-service date, type, and citations.",
        "search_ph": "Search area codes, regions, states…",
        "fields": "United States · Canada · Caribbean & territories · Toll-free & special",
        "schema": "id · code · name · title · region · country · timezones · overlay_with · in_service · type · description · dialing · citations · src · demo",
        "archive_blurb": "The Area Code archive (JAH-AC- records): every North American Numbering Plan area code — geographic, toll-free, premium, non-geographic, and special. Every record carries the full entry — code, region, country, time zone, overlays, in-service date, type, and citations — never a stub.",
        "gen_desc": "Generate structural area-code studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the JAH Area Code Archivist. Ask me about area codes, regions, and dialing.",
        "chat_ph": "Ask about area codes…",
        "sig_type": "Public records in Signature system",
        "source": "public",
        "gen_fields": ["geographic", "toll-free", "premium", "non-geographic", "special"],
        "gen_kind": "area-code-study",
        "gen_demo_kind": "area-code-dialer",
    },
    "public-country-calling-codes": {
        "name": "Country Calling Code Database",
        "tagline": "Every international country calling code — code, country, region, trunk prefix, and dialing notes. Full records, fact-checked. Public records organized in the Signature system.",
        "record_kind": "country calling code record",
        "prefix": "JAH-CC-",
        "ai": "JAH Country Code Librarian",
        "role": "country code librarian — international calling codes, trunk prefixes, dialing",
        "hero_p": "International <b>country calling codes</b> — <b>countries</b>, <b>regions</b>, <b>trunk prefixes</b>, and <b>dialing</b>. Every code in the international numbering plan, organized in the Signature system. Every record carries the full entry: code, country, region, trunk prefix, dialing notes, and citations.",
        "search_ph": "Search country codes, countries…",
        "fields": "Europe · Asia · Africa · North America · South America · Oceania · Caribbean · Other & special",
        "schema": "id · code · name · title · country · region · trunk_prefix · description · dialing · citations · src · demo",
        "archive_blurb": "The Country Calling Code archive (JAH-CC- records): every international country calling code. Every record carries the full entry — code, country, region, trunk prefix, dialing notes, and citations — never a stub.",
        "gen_desc": "Generate structural country-code studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the JAH Country Code Librarian. Ask me about country codes and international dialing.",
        "chat_ph": "Ask about country codes…",
        "sig_type": "Public records in Signature system",
        "source": "public",
        "gen_fields": ["Europe", "Asia", "Africa", "North America", "South America", "Oceania", "Caribbean", "Middle East", "Central America", "Polar & special", "Other & special"],
        "gen_kind": "country-code-study",
        "gen_demo_kind": "country-code-dialer",
    },
    "public-zip-codes": {
        "name": "US ZIP Code Database",
        "tagline": "United States ZIP codes — code, city, state, county, type, and time zone. Seed archive marching to full coverage. Full records, fact-checked. Public records organized in the Signature system.",
        "record_kind": "ZIP code record",
        "prefix": "JAH-ZIP-",
        "ai": "JAH ZIP Code Archivist",
        "role": "ZIP code archivist — postal zones, cities, counties, delivery types",
        "hero_p": "United States <b>ZIP codes</b> — <b>cities</b>, <b>counties</b>, <b>types</b>, and <b>time zones</b>. A seed archive marching to full coverage, organized in the Signature system. Every record carries the full entry: code, city, state, county, type, time zone, and citations.",
        "search_ph": "Search ZIP codes, cities, states…",
        "fields": "By state — each state group opens on demand and loads only what you open",
        "schema": "id · code · name · title · city · state · county · type · timezone · description · citations · src · demo",
        "archive_blurb": "The US ZIP Code archive (JAH-ZIP- records): a fact-checked seed of United States ZIP codes marching to full coverage. Every record carries the full entry — code, city, state, county, type, time zone, and citations — never a stub.",
        "gen_desc": "Generate structural ZIP-code studies. Seeded archive records are the authoritative entries; the archive marches to full coverage.",
        "greet": "I am the JAH ZIP Code Archivist. Ask me about ZIP codes, cities, and zones.",
        "chat_ph": "Ask about ZIP codes…",
        "sig_type": "Public records in Signature system",
        "source": "public",
        "gen_fields": None,  # filled from data (states)
        "gen_kind": "zip-code-study",
        "gen_demo_kind": "zip-zone-reader",
    },
    "signature-numbering-plan": {
        "name": "Signature Numbering Plan Database",
        "tagline": "The original Signature numbering plan — Signature region codes, service codes, exchange codes, toll & info codes, and offsite relay codes. Original Signature creations in the Signature system.",
        "record_kind": "Signature numbering record",
        "prefix": "JAH-SNP-",
        "ai": "JAH Signature Numbering Architect",
        "role": "Signature numbering architect — the original Signature numbering plan",
        "hero_p": "The original <b>Signature numbering plan</b> — <b>region codes</b>, <b>service codes</b>, <b>exchange codes</b>, <b>toll & info codes</b>, and <b>offsite relay codes</b>. Original Signature creations, organized in the Signature system. Every record carries the full entry: code, category, purpose, dialing, and notes.",
        "search_ph": "Search Signature codes, categories…",
        "fields": "Region codes · Service codes · Exchange codes · Toll & info codes · Offsite relay codes",
        "schema": "id · code · name · title · category · purpose · dialing · notes · description · src · demo",
        "archive_blurb": "The Signature Numbering Plan archive (JAH-SNP- records): the original Signature numbering scheme — region codes, service codes, exchange codes, toll & info codes, and offsite relay codes. Original Signature creations. Every record carries the full entry — never a stub.",
        "gen_desc": "Generate structural Signature numbering studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the JAH Signature Numbering Architect. Ask me about the Signature numbering plan.",
        "chat_ph": "Ask about Signature numbering…",
        "sig_type": "Signature originals in Signature system",
        "source": "signature",
        "gen_fields": ["Region codes", "Service codes", "Exchange codes", "Toll & info codes", "Offsite relay codes"],
        "gen_kind": "signature-numbering-study",
        "gen_demo_kind": "signature-numbering",
    },
}


def esc_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_page(slug, template):
    c = DBCFG[slug]
    p = template
    p = p.replace("<title>Public Synthetic Intelligence Database — JAH Databases</title>",
                  "<title>%s — JAH Databases</title>" % esc_html(c["name"]))
    p = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="%s Property of Justin Addam Higgins.">' % esc_html(c["tagline"]), p, count=1)
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Dataset",
        "name": c["name"], "description": c["tagline"],
        "creator": {"@type": "Person", "name": "Justin Addam Higgins"}})
    # NOTE: script content is raw text — do NOT HTML-escape the JSON.
    # Use a replacement function: the JSON contains \uXXXX escapes that
    # re.sub would misread as group escapes in a plain replacement string.
    ld_script = '<script type="application/ld+json">' + ld + '</script>'
    p = re.sub(r'<script type="application/ld\+json">.*?</script>',
               lambda m: ld_script, p, count=1, flags=re.S)
    p = p.replace("<h1>Public Synthetic Intelligence Database</h1>",
                  "<h1>%s</h1>" % esc_html(c["name"]))
    p = p.replace("Synthetic minds, <b>synthetic cognition</b>, <b>whole brain emulation</b>, <b>neuromorphic systems</b>, and <b>synthetic agents</b> — real-world research organized in the Signature system. Every record carries the full entry: description, history, key figures, how it works, and citations.",
                  c["hero_p"])
    p = p.replace("jahdb-public-synthetic-intelligence-1.0", "jahdb-%s-1.0" % slug)
    p = p.replace('<span class="stat">Type: <b>Public records in Signature system</b></span>',
                  '<span class="stat">Type: <b>%s</b></span>' % esc_html(c["sig_type"]))
    p = p.replace('placeholder="Search synthetic intelligence concepts, systems, history…"',
                  'placeholder="%s"' % esc_html(c["search_ph"]))
    p = p.replace('placeholder="Ask about synthetic intelligence…"',
                  'placeholder="%s"' % esc_html(c["chat_ph"]))
    about = '''  <section class="pane" id="p-about">
    <div class="card">
      <h3>About this data base</h3>
      <dl class="kv">
        <dt>Archive</dt><dd>%s</dd>
        <dt>Record schema</dt><dd class="mono">%s</dd>
        <dt>Fields</dt><dd>%s</dd>
        <dt>Generator</dt><dd>jahdb-%s-1.0 — %s</dd>
        <dt>Drift control</dt><dd>Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.</dd>
        <dt>Target</dt><dd>1,000,000 records. The archive marches toward the million mark with overload protection: 100-record chunks, lazy loading, and a collapsible per-field archive so no device ever renders everything at once.</dd>
        <dt>AI</dt><dd>%s — %s — and aware of the whole JAH Databases network through cross-database reasoning. On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured.</dd>
        <dt>Signature system</dt><dd>%s. Property of Justin Addam Higgins (JAH).</dd>
      </dl>
    </div>
  </section>''' % (esc_html(c["archive_blurb"]), esc_html(c["schema"]), esc_html(c["fields"]),
                   slug, esc_html(c["gen_desc"]), esc_html(c["ai"]), esc_html(c["role"]),
                   esc_html(c["sig_type"]))
    p = re.sub(r'  <section class="pane" id="p-about">.*?</section>', about, p, count=1, flags=re.S)
    p = p.replace("<h3>Public Synthetic Intelligence generator</h3>",
                  "<h3>%s generator</h3>" % esc_html(c["name"]))
    p = p.replace("<h3>JAH Synthetic Intelligence Archivist ",
                  "<h3>%s " % esc_html(c["ai"]))
    p = p.replace("var SLUG='public-synthetic-intelligence';", "var SLUG='%s';" % slug)
    p = p.replace('src="gen-public-synthetic-intelligence.js"', 'src="gen-%s.js"' % slug)
    p = p.replace("var LOCAL='../../data/public-synthetic-intelligence/';",
                  "var LOCAL='%s/data/%s/';" % (SHARD_BASE, slug))
    p = p.replace("name:'Public Synthetic Intelligence Database',ai_name:'JAH Synthetic Intelligence Archivist',record_kind:'synthetic intelligence record'",
                  "name:'%s',ai_name:'%s',record_kind:'%s'" % (c["name"], c["ai"], c["record_kind"]))
    p = p.replace("var ROLE='synthetic intelligence archivist — synthetic cognition, synthetic minds, whole brain emulation, synthetic agents';",
                  "var ROLE='%s';" % c["role"])
    p = p.replace("'I am the JAH Synthetic Intelligence Archivist. Ask me about synthetic intelligence.'",
                  "'%s'" % c["greet"].replace("'", "\\'"))
    p = p.replace('<div class="foot">JAH Databases. Public records organized in the Signature system. Property of Justin Addam Higgins (JAH).</div>',
                  '<div class="foot">JAH Databases. %s. Property of Justin Addam Higgins (JAH).</div>' % esc_html(c["sig_type"]))
    return p


def js_str(s):
    return json.dumps(s)


def build_gen_js(slug, topics, cfg):
    """topics: dict field -> list of 'code — label' strings."""
    fields = cfg["gen_fields"] or sorted(topics.keys())
    topics_js = ",\n".join(
        " %s: [\n%s\n ]" % (js_str(f), ",\n".join("  " + js_str(t) for t in topics.get(f, [])))
        for f in fields)
    demo_fn = '''function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# %s — "+safe+"\\n"
   + "# Field: "+field+"\\n"
   + "record = {'title': \\""+safe+"\\", 'field': \\""+field+"\\"}\\n"
   + "def summarize(r):\\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\\n"
   + "print(summarize(record))\\n"
   + "print('Sample record — structural sample, not an archive entry.')\\n";
}''' % cfg["gen_kind"].replace("-", " ").title()
    js = '''(function(){'use strict';
/* JAH %s generator — jahdb-%s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX=%s;
var FIELDS=[%s];
var TOPICS={
%s
};
%s
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — %s',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A %s of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:%s,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-%s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('%s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
''' % (cfg["name"], slug, js_str(cfg["prefix"]), ",".join(js_str(f) for f in fields),
       topics_js, demo_fn, cfg["record_kind"], cfg["record_kind"], js_str(cfg["gen_demo_kind"]),
       slug, slug)
    return js

# ---------------------------------------------------------------- writers

def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


def gen_topics(slug, recs):
    if slug == "public-area-codes":
        out = {}
        for r in recs:
            out.setdefault(r["type"], []).append("%s — %s" % (r["code"], r["region"] or r["country"]))
        return out
    if slug == "public-country-calling-codes":
        out = {}
        for r in recs:
            out.setdefault(r["g"], []).append("%s — %s" % (r["code"], r["country"]))
        return out
    if slug == "public-zip-codes":
        out = {}
        for r in recs:
            out.setdefault(r["g"], []).append("%s — %s" % (r["code"], r["city"]))
        return out
    out = {}
    for r in recs:
        out.setdefault(r["g"], []).append("%s — %s" % (r["code"], r["name"]))
    return out


def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }


def api_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "source": c["source"],
    }


def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")


def norm_country(s):
    s = (s or "").lower().strip()
    s = s.replace("the ", "")
    return s


TRUNK_ALIASES = {
    # wikipedia trunk-table name -> my CCS country name
    "united states": "North American Numbering Plan",
    "usa": "North American Numbering Plan",
    "canada": "North American Numbering Plan",
    "russian federation": "Russia and Kazakhstan",
    "russia": "Russia and Kazakhstan",
    "kazakhstan": "Russia and Kazakhstan",
    "korea, republic of": "South Korea",
    "korea, democratic people's republic of": "North Korea",
    "cote d'ivoire": "Ivory Coast",
    "ivory coast": "Ivory Coast",
    "cape verde": "Cape Verde",
    "caboverde": "Cape Verde",
    "eswatini (swaziland)": "Eswatini",
    "swaziland": "Eswatini",
    "czechia": "Czech Republic",
    "turkiye": "Turkey",
    "macedonia": "North Macedonia",
    "palestine, state of": "Palestine",
    "syrian arab republic": "Syria",
    "iran (islamic republic of)": "Iran",
    "venezuela (bolivarian republic of)": "Venezuela",
    "bolivia (plurinational state of)": "Bolivia",
    "tanzania, united republic of": "Tanzania",
    "moldova, republic of": "Moldova",
    "lao people's democratic republic": "Laos",
    "micronesia, federated states of": "Micronesia",
    "marshall islands": "Marshall Islands",
    "china (landlines only)": "China",
    "india (landlines only)": "India",
    "russia (change to 0 planned)": "Russia and Kazakhstan",
    "north american numbering plan countries": "North American Numbering Plan",
    "falkland islands (malvinas)": "Falkland Islands",
    "reunion": "Reunion and Mayotte",
    "mayotte": "Reunion and Mayotte",
    "curacao": "Curacao and Caribbean Netherlands",
    "bonaire, sint eustatius and saba": "Curacao and Caribbean Netherlands",
    "saint helena, ascension and tristan da cunha": "Saint Helena",
    "british indian ocean territory": "British Indian Ocean Territory",
    "hong kong": "Hong Kong",
    "macao": "Macau",
    "vatican city state": "Vatican City",
    "holy see": "Vatican City",
}


def lookup_trunk(trunks, key):
    """Returns (trunk_prefix_or_None, status). Status: listed | none | unlisted.
    'none' means the reference records state the country uses no trunk prefix;
    'unlisted' means the reference records do not cover it."""
    if key in trunks:
        v = trunks[key]
        return v, ("none" if v is None else "listed")
    for alias, target in TRUNK_ALIASES.items():
        if norm_country(target) == key and norm_country(alias) in trunks:
            v = trunks[norm_country(alias)]
            return v, ("none" if v is None else "listed")
    return None, "unlisted"


def load_country_data():
    """Authored CCS list + trunk prefixes merged from trunk.json when present."""
    from country_seed import CCS
    trunks = {}
    tpath = os.path.join(HERE, "trunk.json")
    if os.path.exists(tpath):
        raw = load_json(tpath)
        items = raw if isinstance(raw, list) else raw.get("trunks", raw.get("items", []))
        for e in items:
            if isinstance(e, dict):
                cn = e.get("country") or e.get("name")
                tp = e.get("trunk_prefix", e.get("trunk"))
                if cn:
                    trunks[norm_country(cn)] = tp
    out = []
    for code, country, region, notes in CCS:
        key = norm_country(TRUNK_ALIASES.get(norm_country(country), country))
        tp, tstat = lookup_trunk(trunks, key)
        out.append({"code": code, "country": country, "region": region,
                    "trunk_prefix": tp, "trunk_status": tstat, "notes": notes})
    matched = sum(1 for e in out if e["trunk_status"] == "listed")
    none_ct = sum(1 for e in out if e["trunk_status"] == "none")
    print("country trunk prefixes: %d listed, %d none, %d unlisted (of %d)"
          % (matched, none_ct, len(out) - matched - none_ct, len(out)))
    return out


def main():
    nanp_path = os.path.join(HERE, "nanp.json")
    if not os.path.exists(nanp_path):
        print("MISSING %s — NANP extraction not delivered yet" % nanp_path)
        return 2
    nanp = load_json(nanp_path)
    ccs = load_country_data()
    print("NANP rows: %d | country-code rows: %d" % (len(nanp), len(ccs)))

    built = {}
    built["public-area-codes"] = build_area_codes(nanp)
    built["public-country-calling-codes"] = build_country_codes(ccs)
    built["public-zip-codes"] = build_zips()
    built["signature-numbering-plan"] = build_signature()

    # sanity: ids unique + prefix + demo programs compile + required keys
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "src", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            assert r["demo"].get("program"), "empty demo in %s" % r["id"]
        for r in recs[:: max(1, len(recs) // 12)]:
            compile(r["demo"]["program"], r["id"], "exec")
        n = write_shard_db(slug, recs)
        print("shard: %-32s %d records -> %s/data/%s/" % (slug, n, SHARD_BASE, slug))

    with open(os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html"),
              "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = build_page(slug, template)
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        with open(os.path.join(ddir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        gen_js = build_gen_js(slug, gen_topics(slug, recs), DBCFG[slug])
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js" % (slug, slug))

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases" % len(built))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
