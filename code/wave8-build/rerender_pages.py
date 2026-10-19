#!/usr/bin/env python3
"""Re-render only index.html for all wave-8 databases (fast: no demos, no JS regen).
Property of Justin Addam Higgins (JAH)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import TIERS
from engine_page import render_page
import entries_home_1, entries_home_2, entries_home_3, entries_creator_1, entries_creator_2

ROOT_DB = os.path.expanduser('~/workspace/jah-databases/db')
PREFIXES = json.load(open(os.path.expanduser('~/workspace/hidden_files/wave8-prefixes.json')))
ITEMS = (entries_home_1.ITEMS + entries_home_2.ITEMS + entries_home_3.ITEMS
         + entries_creator_1.ITEMS + entries_creator_2.ITEMS)
n = 0
for item in ITEMS:
    item['prefix'] = PREFIXES[item['slug']]
    item['prefix_sig'] = PREFIXES[item['slug'] + '-signature']
    item.setdefault('fields', TIERS)
    for sig in (False, True):
        ds = item['slug'] + ('-signature' if sig else '')
        html = render_page(item, ds, sig)
        assert 'id="stCount"' in html and 'All Database Merger' in html
        open(os.path.join(ROOT_DB, ds, 'index.html'), 'w', encoding='utf-8').write(html)
        n += 1
print('pages re-rendered:', n)
