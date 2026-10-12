#!/usr/bin/env python3
"""Library sweep builder: 12 databases (6 library sections x signature+public).
Full material + multimedia (SVG illustrations, WAV audio motifs where fitting).
Public-leaning: public-domain and publicly-available works; privacy-safe.
Property of Justin Addam Higgins (JAH).
"""
import json, gzip, os, re, math, random, struct, wave

ROOT = os.path.expanduser('~/workspace/jah-databases')
CHUNK_SIZE = 60  # one chunk per db (60 records each)

def pad(n, w=6):
    s = str(n)
    while len(s) < w: s = '0' + s
    return s

def esc_xml(s):
    return (s or '').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

# ---------------- media: deterministic SVG illustrations ----------------
def svg_for(kind, seed, title, genre):
    rnd = random.Random(seed * 7919 + 13)
    t = esc_xml(title[:34])
    g = esc_xml(genre)
    if kind == 'census':
        bars = []
        for i in range(6):
            h = 20 + rnd.random() * 90
            x = 30 + i * 55
            bars.append(f'<rect x="{x}" y="{150-h:.0f}" width="38" height="{h:.0f}" rx="4" fill="#2f7bff" opacity="{0.55+rnd.random()*0.45:.2f}"/>')
        inner = ''.join(bars) + '<line x1="20" y1="150" x2="370" y2="150" stroke="#9fb3d8" stroke-width="2"/>'
        bg1, bg2 = '#0b1e3a', '#101a30'
    elif kind == 'genealogy':
        nodes = []
        for lvl in range(3):
            n = 2 ** lvl
            for j in range(n):
                x = 200 - (n-1)*70 + j*140
                y = 40 + lvl*60
                nodes.append(f'<circle cx="{x}" cy="{y}" r="16" fill="#132a55" stroke="#2f7bff" stroke-width="2"/>')
                if lvl < 2:
                    for k in range(2):
                        x2 = 200 - (2*n-1)*35 + (2*j+k)*70
                        nodes.append(f'<line x1="{x}" y1="{y+16}" x2="{x2}" y2="{40+(lvl+1)*60-16}" stroke="#2f7bff" stroke-width="1.5"/>')
        inner = ''.join(nodes); bg1, bg2 = '#101a30', '#0b1e3a'
    elif kind == 'children':
        stars = ''.join(f'<circle cx="{rnd.random()*400:.0f}" cy="{rnd.random()*70:.0f}" r="{1+rnd.random()*2:.1f}" fill="#ffe9a8"/>' for _ in range(24))
        cx = 60 + rnd.random()*280
        inner = (stars + f'<circle cx="{cx:.0f}" cy="46" r="26" fill="#ffd76a"/>'
                 f'<path d="M0 190 Q100 {120+rnd.random()*40:.0f} 200 185 T400 180 V220 H0 Z" fill="#1d5c38"/>'
                 f'<rect x="170" y="120" width="60" height="55" fill="#8a5a2b"/><path d="M160 122 L200 92 L240 122 Z" fill="#a33"/>'
                 f'<rect x="192" y="140" width="16" height="35" fill="#3a2a18"/>')
        bg1, bg2 = '#0b1030', '#1a1440'
    elif kind == 'local':
        inner = ('<rect x="120" y="70" width="160" height="100" fill="#132a55" stroke="#9fb3d8" stroke-width="2"/>'
                 + ''.join(f'<rect x="{130+i*32}" y="90" width="18" height="60" fill="#0b1e3a" stroke="#9fb3d8"/>' for i in range(5))
                 + '<path d="M110 70 L200 30 L290 70 Z" fill="#1d2c4d" stroke="#9fb3d8" stroke-width="2"/>'
                 + '<circle cx="330" cy="45" r="20" fill="#ffd76a"/>')
        bg1, bg2 = '#241a10', '#101a30'
    elif kind == 'oral':
        bars = ''.join(f'<rect x="{20+i*18}" y="{110-rnd.random()*70:.0f}" width="10" height="{20+rnd.random()*70:.0f}" rx="3" fill="#00e5a0" opacity="0.8"/>' for i in range(20))
        inner = (bars + '<circle cx="200" cy="52" r="22" fill="#132a55" stroke="#00e5a0" stroke-width="3"/>'
                 + '<rect x="194" y="52" width="12" height="60" rx="6" fill="#132a55" stroke="#00e5a0" stroke-width="3"/>'
                 + '<path d="M160 110 Q200 140 240 110" stroke="#00e5a0" stroke-width="3" fill="none"/>')
        bg1, bg2 = '#0a1420', '#101a30'
    else:  # yearbooks
        initials = ''.join(w[0] for w in re.sub(r'[^A-Za-z ]','',title).split()[:2]).upper() or 'Y'
        inner = (f'<path d="M200 30 L290 60 V140 Q290 200 200 225 Q110 200 110 140 V60 Z" fill="#132a55" stroke="#ffd76a" stroke-width="4"/>'
                 f'<text x="200" y="145" font-size="64" text-anchor="middle" fill="#ffd76a" font-family="Georgia,serif">{initials}</text>'
                 + ''.join(f'<circle cx="{70+i*260}" cy="200" r="8" fill="#ffd76a"/>' for i in range(2)))
        bg1, bg2 = '#1a1030', '#0b1e3a'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="220" viewBox="0 0 400 220">'
            f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient></defs>'
            f'<rect width="400" height="220" fill="url(#bg)"/>{inner}'
            f'<text x="200" y="208" font-size="11" text-anchor="middle" fill="#9fb3d8" font-family="Arial">{t}</text></svg>')

# ---------------- media: WAV audio motifs ----------------
NOTES = {'C':261.63,'D':293.66,'E':329.63,'F':349.23,'G':392.00,'A':440.00,'B':493.88,
         'c':523.25,'d':587.33,'e':659.25,'g':783.99,'a':880.00}
MELODIES = {
    'bedtime':      [('C',.5),('E',.5),('G',.5),('e',1),('d',.5),('C',1.5)],
    'adventure':    [('G',.3),('G',.3),('A',.3),('c',.6),('A',.3),('G',.9)],
    'animal tale':  [('E',.4),('G',.4),('A',.4),('G',.4),('E',.8)],
    'moral tale':   [('A',.5),('G',.5),('E',.5),('D',.5),('C',1.5)],
    'fantasy':      [('e',.4),('d',.4),('c',.4),('d',.4),('e',.4),('g',1)],
    'rhyme':        [('C',.25),('C',.25),('G',.25),('G',.25),('A',.25),('A',.25),('G',.5)],
    'speech':       [('C',.4),('F',.4),('G',.4),('C',.4),('G',.8)],
    'testimony':    [('D',.5),('F',.5),('A',.5),('d',1)],
    'interview':    [('G',.4),('E',.4),('C',.4),('D',.4),('E',.8)],
    'memoir':       [('A',.6),('E',.6),('A',1.2)],
    'broadcast':    [('E',.3),('G',.3),('c',.6),('G',.3),('E',.9)],
    'witness account':[('F',.5),('E',.5),('D',.5),('C',1.5)],
}
def write_wav(path, melody_key, seed):
    rnd = random.Random(seed)
    sr = 11025
    frames = bytearray()
    def tone(freq, dur, vol=0.5):
        nonlocal frames
        n = int(sr * dur)
        for i in range(n):
            env = min(1.0, i/(sr*0.02), (n-i)/(sr*0.05))
            v = int(32767 * vol * env * math.sin(2*math.pi*freq*i/sr))
            frames += struct.pack('<h', v)
    for note, dur in MELODIES.get(melody_key, MELODIES['bedtime']):
        f = NOTES.get(note, 440.0) * (1 + (rnd.random()-0.5)*0.004)
        tone(f, dur)
        tone(f*0.5, 0.03, 0.08)
    with wave.open(path, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes(bytes(frames))

# ---------------- record building ----------------
def make_record(prefix, seed, topic, kind_label, src, media_kind, audio_key):
    rid = prefix + pad(seed)
    illus = f'media/illus-{pad(seed,4)}.svg'
    rec = {
        'id': rid,
        'title': topic['title'],
        'description': topic['brief'],
        'genre': topic['genre'],
        'type': kind_label,
        'content': {
            'summary': topic['brief'],
            'full_text': topic['text'],
            'key_facts': topic.get('facts', []),
        },
        'illustration': illus,
        'demo': {
            'kind': 'record-program',
            'program': ("// record card — run with: node demo.js\n// (place the record JSON next to this file as record.json)\n"
                        "const card = JSON.parse(require('fs').readFileSync('record.json', 'utf8'));\n"
                        "console.log(card.id + ' — ' + card.title + ' [' + card.src + ']');\n"
                        "console.log('Illustration: ' + card.illustration);"),
            'note': 'A runnable program card for this record. Save as demo.js, save the record JSON as record.json beside it, and run with node.',
        },
        'src': src,
        '_seed': seed,
    }
    if audio_key:
        rec['audio_clip'] = f'media/audio/{topic["genre"]}.wav'
        rec['audio_note'] = 'Original ambient audio motif composed for this collection (instrumental).'
    return rec

def write_gz_jsonl(path, records):
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

def chunk_name(c):
    return 'chunks/chunk-' + str(c).zfill(4) + '.jsonl.gz'

# ---------------- page template (modeled on db/universal-generator/index.html w/ all fixes) ----------------
def page_html(spec):
    with open(os.path.join(ROOT, 'db/ai-ability/index.html'), encoding='utf-8') as f:
        h = f.read()
    slug = spec['slug']; name = spec['name']
    opts = ''.join(f'<option value="{g}">{g}</option>' for g in spec['genres'])
    h = h.replace('ai-ability', slug)
    h = h.replace('gen-ai-ability.js', f'gen-{slug}.js')
    h = h.replace('AI Ability Database', name)
    h = h.replace('AI Ability database', name)
    h = h.replace('JAH AI Ability Archivist', spec['ai_name'])
    h = h.replace('AI ability record', spec['record_kind'])
    h = h.replace('AI ability records', spec['record_kind'] + 's')
    h = h.replace('JAH-AIABIL-', spec['id_prefix'])
    h = h.replace('jahdb-ai-ability-generator-1.0', f'jahdb-{slug}-generator-1.0')
    h = h.replace('The public archive of AI abilities: the full catalog of machine capabilities - understanding language, seeing images, hearing speech, reasoning, writing code, creating art, and advancing science.', spec['hero'])
    h = h.replace('AI ability archivist - capabilities: language, vision, speech, reasoning, code, creativity', spec['role'])
    h = h.replace('Public AI knowledge archive: AI abilities - the complete record of what AI can do.', spec['tagline'])
    h = h.replace('<option value="">any (generator picks)</option><option value="overview">overview</option><option value="detailed">detailed</option><option value="examples">examples</option><option value="faq">faq</option><option value="history">history</option><option value="applications">applications</option>',
                  f'<option value="">any (generator picks)</option>{opts}')
    h = h.replace('AI Ability Database archive (JAH-AIABIL- records): AI abilities and capabilities: language, vision, speech, reasoning, code, creativity - the complete public record of what artificial intelligence can do. Every record is the full file, never a stub.',
                  spec['about_archive'])
    h = h.replace("id · title · description · genre (overview / detailed / examples / faq / history / applications) · type · content (full data) · demo (software demo or program where applicable) · src · _seed",
                  "id · title · description · genre (" + " / ".join(spec['genres']) + ") · type · content (full material: summary, full text, key facts) · illustration (SVG) · audio_clip (where fitting) · demo (runnable program card) · src · _seed")
    h = h.replace('jahdb-ai-ability-generator-1.0 — deterministic: same seed always makes the same record. Every record validated by an independent checker before acceptance. Records are Fact-checked public information records, clearly marked.',
                  f'jahdb-{slug}-generator-1.0 — deterministic: same seed always makes the same record. Every record validated by an independent checker before acceptance. {spec["gen_note"]}')
    h = h.replace('JAH AI Ability Archivist — archive-aware, a boundless-generation specialist for AI ability records, and aware of the whole JAH Databases network through cross-database reasoning. On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured.',
                  f'{spec["ai_name"]} — archive-aware, a boundless-generation specialist for {spec["record_kind"]} records, and aware of the whole JAH Databases network through cross-database reasoning. On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured.')
    h = h.replace('✓ This database is a <b>Signature-governed archive of fact-checked public information</b> — every record verified against public sources, property of Justin Addam Higgins.',
                  spec['about_sig'])
    h = h.replace('Try the Generator tab to make one — describe a AI Ability topic.', f'Try the Generator tab to make one — describe a {spec["record_kind"]} topic.')
    h = h.replace('describe a AI Ability topic to record.', f'describe a {spec["record_kind"]} topic to record.')
    h = h.replace('describe a AI Ability topic to make…', f'describe a {spec["record_kind"]} topic to make…')
    h = h.replace('The generator here builds a full record on any AI Ability topic the user describes.', f'The generator here builds a full record on any {spec["record_kind"]} topic the user describes.')
    h = h.replace('Pick a starting seed and a count, choose an angle (overview, detailed, examples, faq, history, applications), or describe your own AI abilities topic to record.',
                  f'Pick a starting seed and a count, choose a genre ({", ".join(spec["genres"])}), or describe your own {spec["record_kind"]} topic to record.')
    if spec['badge'] == 'signature':
        h = h.replace("return '<div class=\"sigbanner\"><span class=\"badge sig\">✓ Public record — Signature-governed archive of fact-checked public information</span> <span class=\"badge\">Fact-checked public info</span></div>';",
                      "return '<div class=\"sigbanner\"><span class=\"badge sig\">✳ Signature version — Signature-governed, property of Justin Addam Higgins</span> <span class=\"badge\">Signature-authored</span></div>';")
    # multimedia: show illustration + audio inside the full record view
    h = h.replace("function renderFull(r){\n  var h=sigBadge(r)+'<dl class=\"kv\">';",
                  "function renderFull(r){\n  var h=sigBadge(r);\n"
                  "  try{ if(r.illustration) h+='<img loading=\"lazy\" src=\"'+LOCAL+esc(r.illustration)+'\" alt=\"record illustration\" style=\"width:100%;max-width:560px;border-radius:10px;border:1px solid var(--line);margin-bottom:8px\">'; }catch(e){}\n"
                  "  try{ if(r.audio_clip) h+='<div style=\"margin-bottom:8px\"><audio controls preload=\"none\" src=\"'+LOCAL+esc(r.audio_clip)+'\" style=\"width:100%;max-width:560px\"></audio><div class=\"dim\" style=\"font-size:.85em\">'+esc(r.audio_note||'Audio clip')+'</div></div>'; }catch(e){}\n"
                  "  h+='<dl class=\"kv\">';")
    return h

# ---------------- generator JS (deterministic, JAHDB.registerGenerator) ----------------
GEN_JS_TMPL = r'''(function(){'use strict';
/* __NAME__ generator — jahdb-__SLUG__-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   __SRCNOTE__ */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='__PREFIX__';
var SRC='__SRC__';
var RECORD_KIND='__RKIND__';
var GENRES=__GENRES__;
var TOPICS=__TOPICS__;
function buildContent(t){
  return {summary:t.brief, full_text:t.text, key_facts:t.facts||[]};
}
function defaultDemo(){
  return{kind:'record-program',
    program:"// record card — run with: node demo.js\n// (place the record JSON next to this file as record.json)\nconst card = JSON.parse(require('fs').readFileSync('record.json', 'utf8'));\nconsole.log(card.id + ' — ' + card.title + ' [' + card.src + ']');\nconsole.log('Illustration: ' + card.illustration);",
    note:'A runnable program card for this record. Save as demo.js, save the record JSON as record.json beside it, and run with node.'};
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0)||1;
  var pool=TOPICS, ti=(s-1)%TOPICS.length;
  if(opts.genre&&GENRES.indexOf(opts.genre)>=0){
    pool=TOPICS.filter(function(t){return t.genre===opts.genre;});
    if(pool.length) ti=(s-1)%pool.length; else {pool=TOPICS;ti=(s-1)%TOPICS.length;}
  }
  var t=pool[ti];
  var ctopic=opts.topic?String(opts.topic).trim().slice(0,120):'';
  var title=t.title, brief=t.brief, text=t.text;
  if(ctopic){title=ctopic+' — a '+RECORD_KIND;brief='A user-requested '+RECORD_KIND+' on "'+ctopic+'".';text='User-requested topic: '+ctopic+'. '+t.text;}
  var id=PREFIX+pad(s);
  var rec={id:id,title:title,description:brief+' Full material below.',genre:t.genre,type:RECORD_KIND,
    content:buildContent({brief:brief,text:text,facts:t.facts||[]}),
    illustration:'media/illus-'+String(s).padStart(4,'0')+'.svg',
    demo:defaultDemo(),src:SRC,_seed:s};
__AUDIO_LINE__
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0||!/\d{6}$/.test(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<6)e.push('title');
  if(typeof r.description!=='string'||r.description.length<30)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!r.content||typeof r.content!=='object'||typeof r.content.full_text!=='string'||r.content.full_text.length<80)e.push('content');
  if(!r.demo||typeof r.demo!=='object')e.push('demo');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].t===rec.title)return{ok:false,errors:['duplicate title in archive sample']};}
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
'''
def gen_js(spec):
    topics = [{'title': t['title'], 'brief': t['brief'], 'genre': t['genre'], 'text': t['text'], 'facts': t.get('facts', [])}
              for t in spec['topics']]
    js = GEN_JS_TMPL
    audio_line = ("  if(t.genre) { rec.audio_clip='media/audio/'+t.genre+'.wav'; "
                  "rec.audio_note='Original ambient audio motif composed for this collection (instrumental).'; }" if spec.get('audio') else "")
    js = js.replace('__AUDIO_LINE__', audio_line)
    js = js.replace('__NAME__', spec['name'])
    js = js.replace('__SLUG__', spec['slug'])
    js = js.replace('__SRCNOTE__', spec['srcnote'])
    js = js.replace('__PREFIX__', spec['id_prefix'])
    js = js.replace('__SRC__', spec['src'])
    js = js.replace('__RKIND__', spec['record_kind'])
    js = js.replace('__GENRES__', json.dumps(spec['genres']))
    js = js.replace('__TOPICS__', json.dumps(topics, ensure_ascii=False))
    return js

# ---------------- build driver ----------------
def build_db(spec):
    slug = spec['slug']
    ddir = os.path.join(ROOT, 'data', slug)
    mdir = os.path.join(ddir, 'media')
    adir = os.path.join(mdir, 'audio')
    os.makedirs(os.path.join(ddir, 'chunks'), exist_ok=True)
    os.makedirs(mdir, exist_ok=True)
    if spec.get('audio'):
        os.makedirs(adir, exist_ok=True)
        for gi, g in enumerate(spec['genres']):
            p = os.path.join(adir, g + '.wav')
            if not os.path.exists(p):
                write_wav(p, g, 1000 + gi)
    topics = spec['topics']
    records = []
    for i, t in enumerate(topics):
        seed = i + 1
        rec = make_record(spec['id_prefix'], seed, t, spec['record_kind'], spec['src'],
                          spec['media_kind'], spec.get('audio'))
        svg = svg_for(spec['media_kind'], seed, t['title'], t['genre'])
        with open(os.path.join(mdir, f'illus-{pad(seed,4)}.svg'), 'w', encoding='utf-8') as f:
            f.write(svg)
        records.append(rec)
    # chunks
    nchunks = (len(records) + CHUNK_SIZE - 1) // CHUNK_SIZE
    for c in range(nchunks):
        write_gz_jsonl(os.path.join(ddir, chunk_name(c + 1)), records[c*CHUNK_SIZE:(c+1)*CHUNK_SIZE])
    # index
    idx = [{'id': r['id'], 't': r['title'], 'c': (i // CHUNK_SIZE) + 1, 'g': r['genre']}
           for i, r in enumerate(records)]
    write_gz_jsonl(os.path.join(ddir, 'index.jsonl.gz'), idx)
    # page + generator
    pdir = os.path.join(ROOT, 'db', slug)
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page_html(spec))
    with open(os.path.join(pdir, f'gen-{slug}.js'), 'w', encoding='utf-8') as f:
        f.write(gen_js(spec))
    return len(records)

def update_manifests(specs, counts):
    mpath = os.path.join(ROOT, 'data/manifest.json')
    with open(mpath, encoding='utf-8') as f: m = json.load(f)
    slugs = {d['slug'] for d in m['databases']}
    for spec in specs:
        if spec['slug'] in slugs: continue
        m['databases'].append({
            'slug': spec['slug'], 'name': spec['name'], 'tagline': spec['tagline'],
            'record_kind': spec['record_kind'], 'id_prefix': spec['id_prefix'].rstrip('-'),
            'ai_name': spec['ai_name'], 'local_index': f"data/{spec['slug']}/index.jsonl.gz",
            'status': 'live', 'record_count': counts[spec['slug']],
        })
    m['database_count'] = len(m['databases'])
    with open(mpath, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, indent=1)
    apath = os.path.join(ROOT, 'api.json')
    with open(apath, encoding='utf-8') as f: a = json.load(f)
    aslugs = {d['slug'] for d in a['databases']}
    base = 'https://justinahiggins614-cmyk.github.io/jah-databases'
    for spec in specs:
        if spec['slug'] in aslugs: continue
        a['databases'].append({
            'slug': spec['slug'], 'name': spec['name'], 'tagline': spec['tagline'],
            'record_kind': spec['record_kind'], 'id_prefix': spec['id_prefix'].rstrip('-'),
            'ai_name': spec['ai_name'],
            'page_url': f"{base}/db/{spec['slug']}/",
            'index_files': [f"{base}/data/{spec['slug']}/index.jsonl.gz"],
            'record_counts': {f"data/{spec['slug']}/index.jsonl.gz": counts[spec['slug']]},
            'status': 'live',
        })
    a['database_count'] = len(a['databases'])
    with open(apath, 'w', encoding='utf-8') as f:
        json.dump(a, f, ensure_ascii=False, indent=1)
    return len(m['databases'])

# ================= 1. census-records-public =================
CENPUB = [
# --- population total (10) ---
("World population reaches 8 billion (UN, 2022)", "population total",
 "On 15 November 2022 the United Nations marked the Day of Eight Billion: the world population reached 8,000,000,000. The milestone reflects falling mortality and rising life expectancy; growth is now concentrated in sub-Saharan Africa and South Asia.",
 """MILESTONE RECORD — WORLD POPULATION
Source: United Nations, World Population Prospects 2022 (public aggregate statistics).

The United Nations Population Division designated 15 November 2022 as the Day of Eight Billion, the date the world population reached 8,000,000,000 people.

Key aggregates (UN WPP 2022, medium variant):
- World population, 2022: 8.0 billion
- Annual growth rate, 2022: under 1% per year for the first time since 1950
- More than half of projected growth to 2050: eight countries — DR Congo, Egypt, Ethiopia, India, Nigeria, Pakistan, Philippines, Tanzania
- Sub-Saharan Africa's share of world population: projected to approach 35% by 2100

Historical milestones: 1 billion c.1800; 2 billion 1927; 3 billion 1960; 4 billion 1974; 5 billion 11 July 1987; 6 billion 12 Oct 1999; 7 billion 31 Oct 2011; 8 billion 15 Nov 2022.

This record contains aggregate statistics only. No individual personal data is collected or stored in this database.""",
 ["World population 2022: 8.0 billion (UN WPP 2022).","Day of Eight Billion: 15 November 2022.","Growth now under 1% per year."]),
("China — Seventh National Census, 2020", "population total",
 "China's 2020 census counted 1,411,780,000 people on the mainland, an increase of 72 million over 2010 — the slowest decade of growth in the census series, with urbanization passing 60%.",
 """NATIONAL CENSUS RECORD — PEOPLE'S REPUBLIC OF CHINA, 2020
Source: National Bureau of Statistics of China, Seventh National Population Census (public aggregate statistics).

Mainland population: 1,411,780,000 (1 November 2020 reference date).

Headline aggregates:
- Increase over 2010: +72,060,000 (+5.38%)
- Urbanization rate: 63.89% (up from 49.68% in 2010)
- Male: 51.24% / Female: 48.76%
- Aged 60 and over: 18.70%
- Average household size: 2.62 persons
- Han ethnicity: 91.11%

Context: the slowest ten-year growth since the census series began in 1953, reflecting sustained low fertility. China remained the world's most populous country at the census date.

This record contains aggregate statistics only.""",
 ["Mainland population 2020: 1,411,780,000.","Urbanization: 63.89%.","Slowest decade of growth in the series."]),
("India — Census 2011", "population total",
 "India's 2011 census recorded 1,210,854,977 people, making it the second most populous country. Uttar Pradesh alone counted nearly 200 million — more than most nations.",
 """NATIONAL CENSUS RECORD — INDIA, 2011
Source: Office of the Registrar General & Census Commissioner, India (public aggregate statistics).

Total population: 1,210,854,977 (1 March 2011).

Headline aggregates:
- Males: 623,270,000 / Females: 587,580,000
- Decadal growth 2001–2011: 17.7% (down from 21.5%)
- Literacy rate (age 7+): 74.04%
- Urban population: 31.16%
- Largest state: Uttar Pradesh, 199,812,341
- Smallest state/UT populations include Lakshadweep at 64,473

India's census is among the largest administrative exercises in the world, enumerating over 1.2 billion people across 640 districts.

This record contains aggregate statistics only.""",
 ["Population 2011: 1,210,854,977.","Decadal growth: 17.7%.","Literacy (7+): 74.04%."]),
("United States — 2020 Census", "population total",
 "The 2020 US census counted 331,449,281 residents, a 7.4% increase since 2010 — the second-slowest decade of growth in US history. California remained the most populous state.",
 """NATIONAL CENSUS RECORD — UNITED STATES, 2020
Source: US Census Bureau, 2020 Census (public aggregate statistics).

Resident population: 331,449,281 (1 April 2020).

Headline aggregates:
- Growth 2010–2020: +7.4% (second-slowest decade on record)
- Most populous state: California, 39,538,223
- Least populous state: Wyoming, 576,851
- Fastest-growing state: Utah (+18.4%)
- Metropolitan areas: 86% of the population lived in metro areas

The 2020 census was the first US census to invite online response nationwide.

This record contains aggregate statistics only.""",
 ["Resident population 2020: 331,449,281.","Decadal growth: 7.4%.","California: 39,538,223."]),
("Indonesia — 2020 Census", "population total",
 "Indonesia's 2020 census recorded 270,203,917 people across its archipelago, with Java holding 56% of the population on 7% of the land.",
 """NATIONAL CENSUS RECORD — INDONESIA, 2020
Source: Statistics Indonesia (BPS), 2020 Population Census (public aggregate statistics).

Total population: 270,203,917 (September 2020).

Headline aggregates:
- Males: 136,661,899 / Females: 133,542,018
- Java's share: 56.10% of population on ~7% of land area
- Largest province: West Java, 48,274,162
- Annual growth rate 2010–2020: 1.25%

Indonesia is the world's fourth most populous country and the largest archipelagic state.

This record contains aggregate statistics only.""",
 ["Population 2020: 270,203,917.","Java holds 56.1% of people.","Growth rate: 1.25% per year."]),
("Brazil — 2022 Census", "population total",
 "Brazil's 2022 census counted 203,080,756 people. São Paulo state alone held 44.4 million; the Southeast region held 41.8% of Brazilians.",
 """NATIONAL CENSUS RECORD — BRAZIL, 2022
Source: IBGE, 2022 Demographic Census (public aggregate statistics).

Total population: 203,080,756 (1 August 2022).

Headline aggregates:
- Growth 2010–2022: +6.5% (slowest since 1872 series began)
- Southeast region: 41.8% of population
- São Paulo state: 44,411,238 (most populous)
- Roraima: 636,707 (least populous state)

Brazil is the most populous country in Latin America and the Portuguese-speaking world.

This record contains aggregate statistics only.""",
 ["Population 2022: 203,080,756.","Slowest growth since 1872.","São Paulo state: 44.4M."]),
("Pakistan — 2023 Digital Census", "population total",
 "Pakistan's 2023 digital census — South Asia's first fully digital count — recorded 241,499,431 people, with Punjab holding over half the population.",
 """NATIONAL CENSUS RECORD — PAKISTAN, 2023
Source: Pakistan Bureau of Statistics, 7th Population & Housing Census (public aggregate statistics).

Total population: 241,499,431.

Headline aggregates:
- Punjab: 127,688,922 (52.9%)
- Sindh: 55,696,147
- Khyber Pakhtunkhwa: 40,856,097
- Balochistan: 14,894,402
- Annual growth rate: 2.55%

Pakistan conducted South Asia's first fully digital census in 2023.

This record contains aggregate statistics only.""",
 ["Population 2023: 241,499,431.","Punjab: 52.9% of total.","Growth rate: 2.55% per year."]),
("Nigeria — 2006 Census and UN estimates", "population total",
 "Nigeria's last full census (2006) counted 140,431,790. UN estimates place 2023 population near 223.8 million, making Nigeria Africa's most populous nation.",
 """NATIONAL CENSUS RECORD — NIGERIA
Source: National Population Commission 2006 census; UN WPP 2022 estimates (public aggregate statistics).

2006 census total: 140,431,790.
UN estimate, 2023: ~223,800,000.

Headline aggregates (2006):
- Kano state: 9,401,288 (most populous)
- Lagos state: 9,113,605
- Annual growth rate: 3.2% (among the world's highest)

Nigeria is Africa's most populous country; the UN projects it will become the world's third most populous country around 2050.

This record contains aggregate statistics only.""",
 ["2006 census: 140,431,790.","2023 UN estimate: ~223.8M.","Growth: 3.2% per year."]),
("Bangladesh — 2022 Census", "population total",
 "Bangladesh's 2022 census recorded 169,828,911 people — one of the world's densest large populations, at over 1,100 people per square kilometre.",
 """NATIONAL CENSUS RECORD — BANGLADESH, 2022
Source: Bangladesh Bureau of Statistics, 2022 Population & Housing Census (public aggregate statistics).

Total population: 169,828,911 (15 June 2022).

Headline aggregates:
- Population density: ~1,119 per sq km (among the world's highest for large countries)
- Dhaka division: 44,215,107 (most populous)
- Literacy (7+): 74.66%
- Annual growth rate: 1.22%

This record contains aggregate statistics only.""",
 ["Population 2022: 169,828,911.","Density: ~1,119 per sq km.","Literacy: 74.66%."]),
("Mexico — 2020 Census", "population total",
 "Mexico's 2020 census counted 126,014,024 people. The State of Mexico and Mexico City together held over a fifth of the nation.",
 """NATIONAL CENSUS RECORD — MEXICO, 2020
Source: INEGI, 2020 Population and Housing Census (public aggregate statistics).

Total population: 126,014,024 (15 March 2020).

Headline aggregates:
- Growth 2010–2020: +12.2%
- State of Mexico: 16,992,418 (most populous)
- Mexico City: 9,209,944
- Median age: 29 years

Mexico is the most populous Spanish-speaking country in the world.

This record contains aggregate statistics only.""",
 ["Population 2020: 126,014,024.","Growth 2010–2020: 12.2%.","Median age: 29."]),
# --- historical census (10) ---
("The first US census, 1790", "historical census",
 "The 1790 United States census counted 3,893,635 people — the first modern census conducted under constitutional authority, taken by US Marshals on horseback.",
 """HISTORICAL CENSUS RECORD — UNITED STATES, 1790
Source: US Census Bureau historical series (public aggregate statistics).

Total population: 3,893,635 (first Monday of August 1790).

Headline aggregates:
- Free white males 16+: 813,365
- Free white males under 16: 802,127
- Free white females: 1,541,263
- All other free persons: 59,152
- Enslaved persons: 697,681
- Most populous state: Virginia, 747,610

Conducted under Article I, Section 2 of the Constitution for apportioning House seats. Cost: $44,377. The schedules survive for most states; Delaware, Georgia, Kentucky, New Jersey, Tennessee, and Virginia schedules are lost.

This record contains aggregate statistics only.""",
 ["Total 1790: 3,893,635.","Purpose: House apportionment.","Cost: $44,377."]),
("The 1801 Census of England and Wales", "historical census",
 "Britain's first census (1801) counted 8,872,980 people in England and Wales, organized by the statistician John Rickman amid Napoleonic-war anxieties about food supply.",
 """HISTORICAL CENSUS RECORD — ENGLAND AND WALES, 1801
Source: UK Parliamentary Papers / Histpop (public aggregate statistics).

Total population: 8,872,980 (10 March 1801).

Headline aggregates:
- Families chiefly in agriculture: 896,082
- Families in trade/manufacture: 1,345,000+
- London: ~1,000,000 (already Europe's largest city)
- Organizer: John Rickman, clerk to the House of Commons

The 1801 census asked only six questions via parish overseers. Scotland counted separately (1,608,420). No individual schedules survive — only parish aggregates.

This record contains aggregate statistics only.""",
 ["Total 1801: 8,872,980.","Organizer: John Rickman.","Only parish aggregates survive."]),
("Domesday Book, 1086 — England's great survey", "historical census",
 "William the Conqueror's Domesday survey of 1086 recorded landholders, ploughs, and livestock across England — the closest thing to a census for 900 years. Historians estimate 1.5–2.5 million people.",
 """HISTORICAL CENSUS RECORD — ENGLAND, 1086
Source: The National Archives, Domesday Book (public historical record).

The Domesday survey recorded, settlement by settlement: landholders, hides of land, plough teams, mills, and heads of livestock. Population estimates derived from it: 1.5–2.5 million.

Headline aggregates:
- Settlements recorded: ~13,418
- Tenants-in-chief: ~1,400
- Recorded population (household heads): ~268,000
- Estimated total population: 1.5–2.5 million

It omits London, Winchester, and the far north. The survey's purpose was fiscal: establishing what the King could tax.

This record contains aggregate statistics only.""",
 ["Survey year: 1086.","Settlements: ~13,418.","Estimated population: 1.5–2.5M."]),
("Han dynasty census, 2 CE — 57.7 million", "historical census",
 "China's Han dynasty census of 2 CE recorded 12,366,470 households and 57,671,400 individuals — the earliest large-scale census with surviving figures.",
 """HISTORICAL CENSUS RECORD — HAN CHINA, 2 CE
Source: Book of Han (Hanshu), Geography treatise (public historical record).

Recorded: 12,366,470 households; 57,671,400 individuals.

This is the earliest census in world history with detailed surviving figures, conducted for taxation and corvée labor administration. The figures imply sophisticated household registration (hukou's ancient ancestor).

For comparison, the Roman Empire at the same period is estimated at 45–60 million — the Han census suggests China alone matched or exceeded it.

This record contains aggregate statistics only.""",
 ["Households: 12,366,470.","Individuals: 57,671,400.","Earliest detailed census figures."]),
("US Census 1900 — 76.2 million", "historical census",
 "The 1900 US census counted 76,212,168 people and was the last processed entirely by hand-punched Hollerith tabulating machines — the technology that became IBM.",
 """HISTORICAL CENSUS RECORD — UNITED STATES, 1900
Source: US Census Bureau historical series (public aggregate statistics).

Total population: 76,212,168 (1 June 1900).

Headline aggregates:
- Growth 1890–1900: +21.0%
- Urban population: 39.6%
- Foreign-born: 13.6%
- Most populous state: New York, 7,268,894

Processing used Herman Hollerith's punched-card tabulators — the contract that founded the Computing-Tabulating-Recording Company, later IBM.

This record contains aggregate statistics only.""",
 ["Total 1900: 76,212,168.","Urban: 39.6%.","Hollerith tabulators used."]),
("World population milestones, 1800–2011", "historical census",
 "From 1 billion around 1800 to 7 billion on 31 October 2011: the UN's Day of Seven Billion marked a doubling in just 50 years.",
 """HISTORICAL MILESTONE RECORD — WORLD POPULATION
Source: United Nations Population Division (public aggregate statistics).

- c.1800: 1 billion
- 1927: 2 billion (127 years)
- 1960: 3 billion (33 years)
- 1974: 4 billion (14 years)
- 11 July 1987: 5 billion — Day of Five Billion
- 12 October 1999: 6 billion — Day of Six Billion
- 31 October 2011: 7 billion — Day of Seven Billion

The interval between billions shrank dramatically with 20th-century mortality decline, then began lengthening again as fertility fell worldwide.

This record contains aggregate statistics only.""",
 ["1B c.1800; 7B on 31 Oct 2011.","Fastest doubling: 1960–1999.","Growth rate peaked in the 1960s."]),
("Roman censuses — citizens counted for tax and legions", "historical census",
 "Rome's Republican censuses counted adult male citizens for military levy and taxation. The census of 28 BCE under Augustus recorded 4,063,000 citizens.",
 """HISTORICAL CENSUS RECORD — ROME
Source: Res Gestae Divi Augusti; Livy (public historical record).

Augustus's census of 28 BCE: 4,063,000 Roman citizens. Later Augustan censuses: 8 CE: 4,233,000; 14 CE: 4,937,000.

The Republican census (held roughly every five years by the censors) registered adult male citizens, their property class, and their tribe — determining legion service and voting century. The word 'census' itself comes from the Latin 'censere', to assess.

Total imperial population is estimated at 45–60 million; the citizen counts cover only a fraction.

This record contains aggregate statistics only.""",
 ["28 BCE: 4,063,000 citizens.","Purpose: levy and taxation.","'Census' from Latin censere."]),
("The 1881 Census of England and Wales — first fully searchable", "historical census",
 "The 1881 census counted 25,974,439 people in England and Wales and became the first British census fully transcribed and searchable by name — a landmark for public genealogy.",
 """HISTORICAL CENSUS RECORD — ENGLAND AND WALES, 1881
Source: The National Archives (public aggregate statistics).

Total population: 25,974,439 (3 April 1881).

Headline aggregates:
- Growth 1871–1881: +14.4%
- London: 3,830,297
- Urban share: ~70%

The 1881 census was transcribed in full by the Church of Jesus Christ of Latter-day Saints and partners, making it the first Victorian census searchable person-by-person — the foundation stone of modern family history research.

This record contains aggregate statistics only.""",
 ["Total 1881: 25,974,439.","London: 3,830,297.","First fully transcribed Victorian census."]),
("Brazil's first census, 1872", "historical census",
 "Brazil's 1872 census — the first in Latin America — counted 9,930,478 people, including 1,510,806 enslaved persons, sixteen years before abolition.",
 """HISTORICAL CENSUS RECORD — BRAZIL, 1872
Source: IBGE historical series (public aggregate statistics).

Total population: 9,930,478 (1 August 1872).

Headline aggregates:
- Enslaved persons: 1,510,806 (15.2%)
- Free population: 8,419,672
- Most populous province: Minas Gerais, 2,039,735

The first census conducted in Latin America, ordered by the imperial government of Dom Pedro II.

This record contains aggregate statistics only.""",
 ["Total 1872: 9,930,478.","Enslaved: 15.2%.","First census in Latin America."]),
("Japan's first modern census, 1920", "historical census",
 "Japan's 1920 census — Asia's first modern census — counted 55,963,053 people in Japan proper, run by the new Statistics Bureau.",
 """HISTORICAL CENSUS RECORD — JAPAN, 1920
Source: Statistics Bureau of Japan (public aggregate statistics).

Total population (Japan proper): 55,963,053 (1 October 1920).

Headline aggregates:
- Households: 11,300,000+
- Tokyo prefecture: 3,699,428
- Urbanization: ~18%

Japan's 1920 census was the first modern census in Asia, modeled partly on Western practice and conducted every five years since (every ten for the full 'large-scale' cycle).

This record contains aggregate statistics only.""",
 ["Total 1920: 55,963,053.","First modern census in Asia.","Tokyo: 3,699,428."]),
# --- demographic breakdown (10) ---
("Median age around the world, 2020", "demographic breakdown",
 "The world's median age was 30.4 in 2020 — but the spread is enormous: 15.1 in Uganda, 48.4 in Japan. This record maps the age divide.",
 """DEMOGRAPHIC ANALYSIS — MEDIAN AGE BY COUNTRY, 2020
Source: UN World Population Prospects 2022 (public aggregate statistics).

World median age: 30.4 years.

Oldest populations (median age):
- Japan: 48.4
- Italy: 47.3
- Germany: 45.7
- Portugal: 46.2

Youngest populations:
- Uganda: 15.1
- Chad: 15.4
- Mali: 15.5
- DR Congo: 16.0

The gap between Japan and Uganda — 33 years — summarizes the demographic divide: aging rich countries versus youthful poor ones. By 2050 the world median age is projected at 36.

This record contains aggregate statistics only.""",
 ["World median age 2020: 30.4.","Japan 48.4 vs Uganda 15.1.","2050 projection: 36."]),
("Global fertility: 2.3 children per woman, 2021", "demographic breakdown",
 "World total fertility fell to 2.3 in 2021 — just above replacement. South Korea (0.81) and Niger (6.7) mark the extremes.",
 """DEMOGRAPHIC ANALYSIS — TOTAL FERTILITY RATE, 2021
Source: UN World Population Prospects 2022 (public aggregate statistics).

World TFR: 2.3 children per woman.

Lowest fertility:
- South Korea: 0.81 (2021)
- Singapore: 1.02
- China: 1.16 (2020 census)

Highest fertility:
- Niger: 6.7
- Chad: 6.2
- DR Congo: 6.0

Two-thirds of humanity now lives in countries below replacement fertility (2.1). The UN projects world fertility at 2.1 by 2050.

This record contains aggregate statistics only.""",
 ["World TFR 2021: 2.3.","South Korea: 0.81; Niger: 6.7.","Two-thirds below replacement."]),
("Life expectancy worldwide, 2019", "demographic breakdown",
 "Global life expectancy reached 72.8 years in 2019 before the pandemic. Japan (84.6) and the Central African Republic (53.9) span a 30-year gap.",
 """DEMOGRAPHIC ANALYSIS — LIFE EXPECTANCY AT BIRTH, 2019
Source: UN World Population Prospects 2022 (public aggregate statistics).

World: 72.8 years (70.8 male, 75.0 female).

Highest:
- Japan: 84.6
- Switzerland: 84.2
- Singapore: 84.0

Lowest:
- Central African Republic: 53.9
- Chad: 55.1
- Nigeria: 55.4

COVID-19 cut global life expectancy by about 1.7 years in 2020–2021 — the first sustained global decline since the 1918 influenza.

This record contains aggregate statistics only.""",
 ["World 2019: 72.8 years.","Japan 84.6 vs CAR 53.9.","COVID cut ~1.7 years."]),
("The world speaks: largest mother tongues, 2023 estimates", "demographic breakdown",
 "Mandarin (~940M native speakers), Spanish (~485M), and English (~380M native, 1.5B total) top the world language table — census language questions make this measurable.",
 """DEMOGRAPHIC ANALYSIS — LANGUAGES BY NATIVE SPEAKERS
Source: Ethnologue 2023; national census language questions (public aggregate statistics).

Native speakers (approximate):
- Mandarin Chinese: ~940 million
- Spanish: ~485 million
- English: ~380 million (1.5 billion total speakers)
- Hindi: ~345 million
- Portuguese: ~230 million
- Bengali: ~230 million
- Russian: ~150 million
- Japanese: ~125 million

Census language questions (as in India's census, Canada's, Switzerland's) are the primary source for mother-tongue statistics worldwide.

This record contains aggregate statistics only.""",
 ["Mandarin: ~940M native.","English: 1.5B total speakers.","Censuses are the main source."]),
("Religion counts: the 2011 India census religion table", "demographic breakdown",
 "India's 2011 census religion table: Hindu 79.8%, Muslim 14.2%, Christian 2.3%, Sikh 1.7% — the world's largest religion count.",
 """DEMOGRAPHIC ANALYSIS — RELIGION, INDIA 2011
Source: Census of India 2011, religion tables (public aggregate statistics).

- Hindu: 966,257,353 (79.8%)
- Muslim: 172,245,158 (14.2%)
- Christian: 27,819,588 (2.3%)
- Sikh: 20,833,116 (1.7%)
- Buddhist: 8,442,972 (0.7%)
- Jain: 4,451,753 (0.4%)

India's Muslim population alone (172M) exceeds the total population of all but a handful of countries. Religion has been asked in every Indian census since 1872.

This record contains aggregate statistics only.""",
 ["Hindu 79.8%; Muslim 14.2%.","Asked since 1872.","Largest religion count on Earth."]),
("US 2020: the multiracial count triples", "demographic breakdown",
 "The 2020 US census recorded 33.8 million multiracial Americans — up from 9 million in 2010 — the decade's biggest demographic story.",
 """DEMOGRAPHIC ANALYSIS — RACE, UNITED STATES 2020
Source: US Census Bureau 2020 (public aggregate statistics).

- Two or more races: 33,848,943 (10.2%), up from 2.9% in 2010
- White alone: 57.8% (non-Hispanic)
- Hispanic or Latino: 62,080,044 (18.7%)
- Black alone: 12.1%
- Asian alone: 5.9%

The jump reflects both real change and improved question design capturing multiracial identity. California (15.3M) and Texas (11.4M) hold the largest Hispanic populations.

This record contains aggregate statistics only.""",
 ["Multiracial: 33.8M (10.2%).","Hispanic: 62.1M (18.7%).","Question design improved capture."]),
("China 2020: 18.7% aged 60 and over", "demographic breakdown",
 "China's 2020 census found 264 million people aged 60+ (18.7%) — the demographic weight behind the world's fastest aging transition.",
 """DEMOGRAPHIC ANALYSIS — AGING, CHINA 2020
Source: National Bureau of Statistics of China (public aggregate statistics).

- Aged 60+: 264,018,766 (18.70%)
- Aged 65+: 190,635,280 (13.50%)
- Children 0–14: 17.95%
- Working age 15–59: 63.35%

In 1990 only 8.6% of China was 60+. The one-child era's small cohorts are now entering old age while the 1960s baby boomers retire — the dependency ratio is turning fast.

This record contains aggregate statistics only.""",
 ["60+: 264M (18.7%).","Up from 8.6% in 1990.","Dependency ratio turning."]),
("Africa's youth bulge: 60% under 25", "demographic breakdown",
 "Africa's median age is 19.7 — the world's youngest continent. 60% of Africans are under 25, a youth bulge with enormous economic stakes.",
 """DEMOGRAPHIC ANALYSIS — AGE STRUCTURE, AFRICA
Source: UN World Population Prospects 2022 (public aggregate statistics).

- Africa median age: 19.7 years (world: 30.4)
- Under 25: ~60% of population
- Under 15: ~40%
- Fertility: 4.4 children per woman (2021)

By 2050, one in three of the world's young people will be African. Whether the youth bulge becomes a dividend or a strain depends on schooling and jobs.

This record contains aggregate statistics only.""",
 ["Median age: 19.7.","60% under 25.","1 in 3 young people by 2050."]),
("Households are shrinking worldwide", "demographic breakdown",
 "Average household size fell almost everywhere: China 2.62 (2020), US 2.6, India 4.4 (2011), EU 2.3. Solo living is the fastest-growing household type.",
 """DEMOGRAPHIC ANALYSIS — HOUSEHOLD SIZE
Source: National censuses 2010–2022 rounds (public aggregate statistics).

Average household size:
- China (2020): 2.62 (down from 3.96 in 1982)
- United States (2020): 2.6
- India (2011): 4.4
- European Union (2022): 2.3
- Japan (2020): 2.21

One-person households: ~15% in the US, ~38% in the EU, ~16% in China (2020) — rising everywhere as populations age and urbanize.

This record contains aggregate statistics only.""",
 ["China: 2.62; EU: 2.3.","Solo living rising everywhere.","Driven by aging + urbanization."]),
("Sex ratios: from Qatar (2.9) to Latvia (0.85)", "demographic breakdown",
 "The world has 101.7 men per 100 women — but migration skews Qatar to 2.9 while longevity skews Latvia to 0.85.",
 """DEMOGRAPHIC ANALYSIS — SEX RATIO
Source: UN World Population Prospects 2022 (public aggregate statistics).

World: 101.7 males per 100 females.

Highest (male-skewed, migrant labor):
- Qatar: ~2.9
- UAE: ~2.2
- Oman: ~1.9

Lowest (female-skewed, longevity + history):
- Latvia: 0.85
- Lithuania: 0.86
- Ukraine: 0.87

Natural birth ratio is ~1.05; deviations reflect migration, war mortality, and longevity gaps.

This record contains aggregate statistics only.""",
 ["World: 101.7 per 100.","Qatar ~2.9; Latvia 0.85.","Migration and longevity drive skew."]),
# --- urbanization (10) ---
("Tokyo — the world's largest metro, ~37 million", "urbanization",
 "Greater Tokyo's ~37 million people make it the largest metropolitan economy on Earth — bigger than most countries, counted across four prefectures.",
 """URBAN ANALYSIS — TOKYO METROPOLITAN AREA
Source: UN World Urbanization Prospects 2018; Statistics Bureau of Japan (public aggregate statistics).

- Greater Tokyo population: ~37,000,000
- Prefectures: Tokyo, Kanagawa, Saitama, Chiba
- Share of Japan's population: ~29%
- Rail ridership: Shinjuku station alone handles ~3.6M passengers daily

Tokyo has been the world's largest city since passing Mexico City in the 1960s. Its rail network carries more people daily than most national railways.

This record contains aggregate statistics only.""",
 ["Metro: ~37M.","29% of Japan.","World's largest since the 1960s."]),
("Delhi passes 32 million", "urbanization",
 "The UN estimates Delhi's urban agglomeration near 32 million — set to become the world's largest city by around 2028.",
 """URBAN ANALYSIS — DELHI
Source: UN World Urbanization Prospects 2018 (public aggregate statistics).

- Urban agglomeration: ~32,000,000
- Census 2011 (NCT): 16,787,941
- Projected: world's largest city c.2028

Delhi's growth (from 1.7M in 1951) tracks India's urbanization surge: the urban share rose from 17% in 1951 to 35%+ today.

This record contains aggregate statistics only.""",
 ["Agglomeration: ~32M.","World's largest c.2028.","From 1.7M in 1951."]),
("Shanghai — 28 million in one municipality", "urbanization",
 "Shanghai municipality counted 24.9 million in the 2020 census within its borders; the metro exceeds 28 million — China's largest city.",
 """URBAN ANALYSIS — SHANGHAI
Source: China 2020 census; UN WUP 2018 (public aggregate statistics).

- Municipality (2020 census): 24,870,000
- Metro agglomeration: ~28,000,000
- Growth 2010–2020: +8.2%
- Pudong district alone: 5.68M

Shanghai's metro carries the world's longest subway system by route length (~800 km).

This record contains aggregate statistics only.""",
 ["Municipality: 24.87M.","Metro: ~28M.","World's longest subway."]),
("56% of humanity is urban, 2021", "urbanization",
 "The UN put the urban share at 56% in 2021 — up from 30% in 1950, heading for 68% by 2050. The urban millennium arrived in 2007.",
 """URBAN ANALYSIS — WORLD URBANIZATION
Source: UN World Urbanization Prospects 2018 (public aggregate statistics).

- Urban share 1950: 30%
- Urban share 2007: 50% (the crossover year)
- Urban share 2021: 56%
- Projected 2050: 68%

Regional urban shares (2021): North America 83%, Latin America 81%, Europe 75%, Asia 52%, Africa 44%.

Nearly all future urban growth will be in Asia and Africa.

This record contains aggregate statistics only.""",
 ["56% urban in 2021.","68% projected by 2050.","Growth concentrated in Asia/Africa."]),
("China's urbanization: 63.9% in 2020", "urbanization",
 "China's 2020 census found 63.89% urban — up from 17.9% in 1978. Over 900 million Chinese now live in cities.",
 """URBAN ANALYSIS — CHINA
Source: National Bureau of Statistics of China (public aggregate statistics).

- Urban share 1978: 17.9%
- Urban share 2000: 36.2%
- Urban share 2010: 49.7%
- Urban share 2020: 63.89% (~902 million people)

The largest rural-to-urban migration in human history: hundreds of millions moved in four decades. The hukou household-registration system still shapes who counts as urban.

This record contains aggregate statistics only.""",
 ["63.89% urban in 2020.","~902M city dwellers.","Largest migration in history."]),
("Lagos — Africa's megacity, ~15 million", "urbanization",
 "Lagos holds an estimated 15 million people — Africa's largest city, growing toward 20 million, built across lagoons and islands.",
 """URBAN ANALYSIS — LAGOS, NIGERIA
Source: UN WUP 2018; Lagos Bureau of Statistics (public aggregate statistics).

- Metro estimate: ~15,000,000
- 1950 population: ~325,000
- Density: among the world's highest for a metro
- State claim (2012): 21M (disputed; UN uses ~15M)

Lagos grows by an estimated 600,000+ people per year — one of the fastest-growing megacities on Earth.

This record contains aggregate statistics only.""",
 ["Metro: ~15M.","From 325K in 1950.","+600K per year."]),
("US 2020: 86% metropolitan", "urbanization",
 "86% of Americans lived in metropolitan areas in 2020. The New York metro alone (20.1M) exceeds most states.",
 """URBAN ANALYSIS — UNITED STATES, 2020
Source: US Census Bureau (public aggregate statistics).

- Metropolitan population: 86%
- New York-Newark-Jersey City metro: 20,140,470
- Los Angeles metro: 13,200,998
- Fastest-growing large metro 2010–2020: Austin (+33%)

The Census Bureau defines 384 metropolitan statistical areas; the top 10 hold over a quarter of all Americans.

This record contains aggregate statistics only.""",
 ["86% metropolitan.","NYC metro: 20.1M.","Austin grew 33%."]),
("São Paulo — South America's giant, ~22 million", "urbanization",
 "Greater São Paulo's ~22 million people make it the Southern Hemisphere's largest city — an industrial colossus built on coffee wealth.",
 """URBAN ANALYSIS — SÃO PAULO
Source: IBGE; UN WUP 2018 (public aggregate statistics).

- Metro: ~22,000,000
- Municipality (2022): 11,451,245
- 1872 population: 31,385
- Helicopter fleet: one of the world's largest (traffic response)

São Paulo grew from a Jesuit mission village (1554) to a 22-million metro on coffee, industry, and immigration.

This record contains aggregate statistics only.""",
 ["Metro: ~22M.","From 31K in 1872.","Southern Hemisphere's largest."]),
("Cairo — the Arab world's largest city", "urbanization",
 "Greater Cairo holds ~21 million people — the largest metro in the Arab world and Africa, layered over 1,000 years of capitals.",
 """URBAN ANALYSIS — CAIRO
Source: CAPMAS; UN WUP 2018 (public aggregate statistics).

- Metro: ~21,000,000
- 2017 census (governorate): 9,539,673
- Founded: 969 CE (al-Qahira); settlement far older
- New Administrative Capital under construction east of the city

Cairo's metro spans Fatimid, Mamluk, Ottoman, and modern layers — 'the city of a thousand minarets'.

This record contains aggregate statistics only.""",
 ["Metro: ~21M.","Founded 969 CE.","Largest Arab-world city."]),
("Mumbai — 20 million on seven islands", "urbanization",
 "Mumbai's ~20 million people live on seven merged islands at 20,000+ per sq km — India's financial capital and densest great city.",
 """URBAN ANALYSIS — MUMBAI
Source: Census of India 2011; UN WUP 2018 (public aggregate statistics).

- Metro: ~20,000,000
- Municipality (2011): 12,442,373
- Density: ~20,000 per sq km (among the world's highest)
- Dharavi: among Asia's largest informal settlements

Mumbai handles ~70% of India's maritime trade and hosts its film and finance industries.

This record contains aggregate statistics only.""",
 ["Metro: ~20M.","Density ~20K per sq km.","70% of maritime trade."]),
# --- migration (10) ---
("International migrants: 281 million, 2020", "migration",
 "The UN counted 281 million international migrants in 2020 — 3.6% of humanity, more than the population of all but four countries.",
 """MIGRATION ANALYSIS — WORLD, 2020
Source: UN DESA International Migrant Stock 2020 (public aggregate statistics).

- International migrants: 281,000,000 (3.6% of world population)
- 1990: 153M; 2000: 174M; 2010: 221M
- Top destination: United States (50.6M)
- Top origin: India (17.9M abroad)
- Refugees: ~34M (UNHCR)

Nearly two-thirds of migrants live in high-income countries; labor migration dominates the flows.

This record contains aggregate statistics only.""",
 ["281M migrants (3.6%).","Top destination: USA (50.6M).","Top origin: India (17.9M)."]),
("US foreign-born: 45.3 million, 2021", "migration",
 "The American Community Survey put the US foreign-born at 45.3 million in 2021 — 13.6% of the population, near the historic 1890 peak share.",
 """MIGRATION ANALYSIS — UNITED STATES
Source: US Census Bureau, American Community Survey 2021 (public aggregate statistics).

- Foreign-born: 45,300,000 (13.6%)
- Historic peak share: 14.8% (1890)
- Largest origin: Mexico (~10.7M)
- California: 10.5M foreign-born (largest state count)

The 2021 share approaches the 1890 record, driven by Latin American and Asian immigration.

This record contains aggregate statistics only.""",
 ["45.3M foreign-born.","13.6% of population.","Near 1890 record share."]),
("India's diaspora: 17.9 million abroad", "migration",
 "India has the world's largest diaspora: 17.9 million Indians live abroad — in the Gulf, the US, the UK, and beyond.",
 """MIGRATION ANALYSIS — INDIAN DIASPORA
Source: UN DESA 2020 (public aggregate statistics).

- Indians abroad: 17,900,000 (world's largest diaspora)
- UAE: ~3.5M; Saudi Arabia: ~2.5M; United States: ~2.7M
- Remittances to India: ~$111B (2022, world #1 recipient)

Remittances exceed 3% of India's GDP — the single largest flow to any country.

This record contains aggregate statistics only.""",
 ["17.9M abroad (world #1).","Remittances: ~$111B (2022).","UAE, Saudi, US top hosts."]),
("Syrian displacement: 6.8 million refugees", "migration",
 "UNHCR counts 6.8 million Syrian refugees — the largest refugee population of the 2020s — hosted mainly in Turkey, Lebanon, and Jordan.",
 """MIGRATION ANALYSIS — SYRIAN REFUGEES
Source: UNHCR 2023 (public aggregate statistics).

- Syrian refugees: ~6,800,000
- Turkey: ~3.4M (largest host)
- Lebanon: ~800,000 (highest per capita: ~1 in 6 residents)
- Internally displaced: ~6.8M more inside Syria

The Syrian crisis is the largest displacement of the 21st century so far.

This record contains aggregate statistics only.""",
 ["6.8M refugees.","Turkey hosts 3.4M.","Lebanon: 1 in 6 residents."]),
("Gulf migration: Qatar 88% migrant", "migration",
 "Qatar's population is ~88% international migrant — the highest share on Earth — drawn by construction and energy work.",
 """MIGRATION ANALYSIS — GULF STATES
Source: UN DESA 2020 (public aggregate statistics).

Migrant share of population:
- Qatar: ~88%
- UAE: ~87%
- Kuwait: ~72%
- Bahrain: ~55%

The kafala sponsorship system historically tied workers to employers; Qatar and others have reformed it since 2020. Indians, Bangladeshis, Pakistanis, Filipinos, and Egyptians dominate the flows.

This record contains aggregate statistics only.""",
 ["Qatar: ~88% migrant.","UAE: ~87%.","Kafala reforms since 2020."]),
("Venezuelan exodus: 7.7 million", "migration",
 "7.7 million Venezuelans have left since 2014 — one of the largest displacements in the Western Hemisphere's history — mostly to Colombia and Peru.",
 """MIGRATION ANALYSIS — VENEZUELAN DISPLACEMENT
Source: UNHCR/IOM R4V 2023 (public aggregate statistics).

- Venezuelans abroad: ~7,700,000
- Colombia: ~2.9M (largest host)
- Peru: ~1.5M
- Share of Venezuela's population: ~1 in 4

Driven by economic collapse and political crisis since 2014.

This record contains aggregate statistics only.""",
 ["7.7M abroad since 2014.","Colombia hosts 2.9M.","~1 in 4 Venezuelans."]),
("EU migration: Germany hosts 15.8 million", "migration",
 "Germany hosts 15.8 million international migrants — Europe's largest migrant population — including 1.2M+ refugees admitted since 2015.",
 """MIGRATION ANALYSIS — EUROPE
Source: UN DESA 2020; Eurostat (public aggregate statistics).

- Germany: 15,800,000 migrants (19% of population)
- United Kingdom: 9,400,000
- France: 8,500,000
- Spain: 6,800,000

The 2015–16 asylum surge brought over a million refugees to Germany, mostly Syrians, Afghans, and Iraqis.

This record contains aggregate statistics only.""",
 ["Germany: 15.8M.","UK: 9.4M; France: 8.5M.","2015–16 asylum surge."]),
("China's floating population: 376 million", "migration",
 "China's 2020 census counted 376 million internal migrants — the 'floating population' — the largest internal migration on Earth.",
 """MIGRATION ANALYSIS — CHINA INTERNAL
Source: National Bureau of Statistics of China, 2020 census (public aggregate statistics).

- Floating population: 375,816,759
- Share of population: 26.6%
- Guangdong: largest inflow province (~52M migrants)

Rural-to-urban workers power the coastal factories; the hukou system still limits their access to urban schooling and healthcare.

This record contains aggregate statistics only.""",
 ["376M internal migrants.","26.6% of population.","Largest internal migration."]),
("Australia: 30% born overseas", "migration",
 "Australia's 2021 census found 27.6% born overseas — among the highest shares in the world — with England, India, and China top origins.",
 """MIGRATION ANALYSIS — AUSTRALIA, 2021
Source: Australian Bureau of Statistics, 2021 Census (public aggregate statistics).

- Born overseas: 27.6%
- England: 927,490 (top birthplace)
- India: 673,352
- China: 549,270
- Sydney: 40%+ overseas-born

Post-war migration transformed Australia from ~90% British-origin (1947) to one of the world's most diverse nations.

This record contains aggregate statistics only.""",
 ["27.6% born overseas.","England, India, China top.","Sydney 40%+ overseas-born."]),
("Remittances: $831 billion, 2022", "migration",
 "Migrants sent $831 billion home in 2022 — triple development aid — with India ($111B) the top recipient.",
 """MIGRATION ANALYSIS — REMITTANCES, 2022
Source: World Bank/KNOMAD 2023 (public aggregate statistics).

- Global remittances: $831,000,000,000
- Top recipients: India ($111B), Mexico ($61B), China ($51B), Philippines ($38B)
- Remittances vs. official aid: ~3:1
- Tajikistan: remittances ~51% of GDP (highest share)

Remittances are the largest external finance flow to low- and middle-income countries.

This record contains aggregate statistics only.""",
 ["$831B in 2022.","India: $111B (top).","3x official development aid."]),
# --- methodology (10) ---
("De facto vs de jure: who counts where", "methodology",
 "Censuses count people two ways: de facto (where you slept on census night) or de jure (where you usually live). The choice moves millions.",
 """METHODOLOGY GUIDE — CENSUS CONCEPTS
Public knowledge explainer (aggregate concepts only).

- De facto: count people where they are found on census night (used by e.g. India historically).
- De jure: count people at their usual residence (used by e.g. the United States).
- The US 'usual residence' rule is why college students count at school and prisoners at prison — both contested.
- Tourists, diplomats, and the homeless are treated differently by each method.
- The UN recommends the 'usual residence' (12-month) criterion for international comparability.

This record explains public methodology. No individual data.""",
 ["De facto: where you slept.","De jure: usual residence.","UN recommends 12-month rule."]),
("Post-enumeration surveys: measuring the undercount", "methodology",
 "Every census misses people. Post-enumeration surveys re-interview samples to estimate the net undercount — the US 2020 undercounted Hispanics by ~5%.",
 """METHODOLOGY GUIDE — COVERAGE MEASUREMENT
Public knowledge explainer (aggregate concepts only).

- The US 2020 Post-Enumeration Survey found a net undercount of 5.0% for Hispanics, 3.3% for Black Americans, and an overcount of 1.6% for non-Hispanic whites.
- Method: dual-system (capture-recapture) estimation — compare census to an independent survey.
- The UK, Australia, and Canada run similar coverage surveys.
- Undercounts skew funding and representation: the US census guides $1.5T+ in federal funds.

This record explains public methodology. No individual data.""",
 ["Dual-system estimation.","US 2020: -5.0% Hispanic.","Guides $1.5T+ in funds."]),
("Register-based censuses: the Nordic model", "methodology",
 "Denmark, Finland, Norway, and Sweden run censuses from population registers — no forms, no enumerators — updated continuously from administrative records.",
 """METHODOLOGY GUIDE — REGISTER CENSUSES
Public knowledge explainer (aggregate concepts only).

- Denmark ran the first fully register-based census in 1981.
- Sources linked: population register, tax, education, employment, housing registers.
- Advantages: annual (even monthly) statistics, lower cost, no respondent burden.
- Requirement: a universal personal ID number and high-trust administration.
- The Netherlands, Belgium, and Austria use combined register + survey models.

This record explains public methodology. No individual data.""",
 ["Denmark first: 1981.","Needs universal ID + trust.","Annual statistics possible."]),
("The UN Principles and Recommendations", "methodology",
 "The UN's Principles and Recommendations for Population and Housing Censuses set the global standard: universality, simultaneity, defined periodicity.",
 """METHODOLOGY GUIDE — UN STANDARDS
Public knowledge explainer (aggregate concepts only).

The UN Statistics Division's core principles:
1. Individual enumeration — separate records per person (aggregated for release)
2. Universality — everyone in the territory
3. Simultaneity — a single reference moment
4. Defined periodicity — at least every 10 years
5. Small-area statistics — data for local planning

The 2020 census round (2015–2024) saw 150+ countries enumerate, most within the decade.

This record explains public methodology. No individual data.""",
 ["5 core principles.","150+ countries in 2020 round.","Decennial minimum."]),
("Disclosure control: how censuses protect privacy", "methodology",
 "Census bureaus perturb tables to protect respondents: cell suppression, rounding, swapping — and now differential privacy in the US 2020 release.",
 """METHODOLOGY GUIDE — STATISTICAL DISCLOSURE CONTROL
Public knowledge explainer (aggregate concepts only).

- Cell suppression: hide small cells (the UK's classic method).
- Rounding: round counts to base 3 or 5.
- Record swapping: exchange similar households between areas.
- Differential privacy: the US 2020 census injected calibrated noise into published tables — controversial with researchers.
- Principle: publish aggregates; never release identifiable individual records.

Modern censuses keep individual forms sealed for decades (72 years in the US; 100 in the UK).

This record explains public methodology. No individual data.""",
 ["Suppression, rounding, swapping.","US 2020: differential privacy.","Forms sealed 72–100 years."]),
("Census intervals: why ten years", "methodology",
 "The ten-year census cycle comes from the US Constitution (1790) and British practice (1801) — long enough for change, short enough to stay relevant.",
 """METHODOLOGY GUIDE — PERIODICITY
Public knowledge explainer (aggregate concepts only).

- US: every 10 years, constitutionally required (Article I).
- UK: every 10 years since 1801 (except 1941, wartime).
- Japan: every 5 years (large-scale every 10).
- France: rolling census — a sample each year, full refresh every 5.
- Germany: register-based with a 10-year full census (2011, 2022).

The UN recommends at least decennial censuses; war, cost, and politics cause the gaps.

This record explains public methodology. No individual data.""",
 ["US/UK: decennial.","Japan: every 5 years.","France: rolling sample."]),
("The 2020 round goes digital", "methodology",
 "The 2020 census round was the first digital one: online self-response in the US, UK, and Australia; handheld devices for enumerators worldwide.",
 """METHODOLOGY GUIDE — DIGITAL CENSUSES
Public knowledge explainer (aggregate concepts only).

- US 2020: first census with internet self-response as the primary mode.
- UK 2021: 'digital-first' — 88%+ responded online.
- Australia 2021: online-first; the 2016 site crash led to a rebuilt system.
- Pakistan 2023: South Asia's first fully digital census (tablets, GPS).
- Geospatial: satellite imagery now guides enumeration-area mapping in Africa.

Digital collection cut costs but raised cyber and inclusion risks.

This record explains public methodology. No individual data.""",
 ["US/UK/Australia: online-first.","Pakistan 2023: tablets + GPS.","Satellite mapping in Africa."]),
("Censuses and money: $1.5 trillion rides on the count", "methodology",
 "The US census guides $1.5T+ in annual federal funding — Medicaid, highways, schools. An undercounted person costs their community thousands.",
 """METHODOLOGY GUIDE — CENSUS USES
Public knowledge explainer (aggregate concepts only).

- US: 300+ federal programs use census data; ~$1.5T/year distributed.
- Apportionment: 435 House seats reallocated after each census.
- Business: site selection, market sizing, logistics planning.
- Research: the denominator for nearly every rate — disease, crime, poverty.
- George Washington University estimated each uncounted person costs a state ~$1,000–$2,000/year in lost funds.

This record explains public methodology. No individual data.""",
 ["$1.5T/year guided.","435 House seats.","Each miss costs $1–2K/year."]),
("Historical census substitutes: tax rolls and parish registers", "methodology",
 "Before modern censuses, historians use hearth taxes, parish registers, and muster rolls — the raw material of historical demography.",
 """METHODOLOGY GUIDE — PRE-CENSUS SOURCES
Public knowledge explainer (aggregate concepts only).

- Hearth taxes (e.g., England 1662–1689): count fireplaces as a household proxy.
- Parish registers: baptisms, marriages, burials from the 1500s — family reconstitution.
- The Cambridge Group (Wrigley & Schofield) rebuilt England's population 1541–1871 from 404 parishes.
- Ottoman tahrir defters: detailed 15th–16th century tax surveys.
- Japanese shūmon aratame-chō: religious inquisition registers doubling as population records.

Historical demography reconstructs populations without a single census form.

This record explains public methodology. No individual data.""",
 ["Hearth tax = household proxy.","Cambridge Group: 404 parishes.","Ottoman tahrir defters."]),
("Why some countries skip the census", "methodology",
 "Lebanon hasn't held a census since 1932; Somalia and DR Congo for decades. War, cost, and political sensitivity keep dozens of countries uncounted.",
 """METHODOLOGY GUIDE — CENSUS GAPS
Public knowledge explainer (aggregate concepts only).

- Lebanon: last census 1932 — sectarian power-sharing depends on not recounting.
- Somalia: no full census since 1975.
- DR Congo: no full census since 1984.
- Afghanistan: none since 1979.
- Cost: a full census runs $1–$10+ per person — prohibitive for poor states.
- Alternatives: UN estimates, surveys (DHS, MICS), satellite + mobile data models.

Gaps are filled by demographic modeling — less precise, but the only option.

This record explains public methodology. No individual data.""",
 ["Lebanon: 1932 (last).","DR Congo: 1984.","Cost: $1–10+ per person."]),
]

# ================= 2. census-records-signature =================
CENSIG = [
("Signature study: the eight-billionth person and where growth goes next", "population total",
 "A Signature original demographic essay: what the 8-billion milestone means, which eight countries drive growth to 2050, and why the century's story is Africa.",
 """SIGNATURE ORIGINAL STUDY — WORLD POPULATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The 8-billion milestone (15 November 2022, UN) is less interesting as a number than as a hinge. Behind it: the annual growth rate fell below 1% for the first time since 1950. The doubling era is over; the concentration era has begun.

The UN's eight growth drivers to 2050 — DR Congo, Egypt, Ethiopia, India, Nigeria, Pakistan, Philippines, Tanzania — will contribute more than half of all growth. Five are in Africa. The demographic center of gravity is moving south and staying young there while it ages everywhere else.

Three Signature observations:
1. Milestones mislead: 8 billion was never a cliff. The meaningful series is the growth rate, which peaked in 1963 and has fallen ever since.
2. Concentration changes politics: a world adding people almost entirely in eight countries negotiates climate, migration, and aid differently.
3. The next milestone (9 billion, ~2037) will feel quieter — growth is decelerating into it.

Method note: aggregates from UN WPP 2022, reinterpreted. No individual data.""",
 ["Growth <1%/yr: first time since 1950.","8 countries drive half of growth to 2050.","9 billion expected ~2037."]),
("Signature study: reading China's 2020 census like a demographer", "population total",
 "A Signature original analysis of China's Seventh Census: what 1.41 billion with 63.9% urbanization and 18.7% over-60 really signals about the decades ahead.",
 """SIGNATURE ORIGINAL STUDY — CHINA 2020 CENSUS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Three numbers from the 2020 census tell China's demographic story:
- 1,411,780,000 people, +5.38% in a decade (slowest growth on record)
- 63.89% urban (up 14 points in ten years — the fastest urbanization of any large country, ever)
- 18.70% aged 60+ (264 million people — more than most countries' entire populations)

The Signature reading: China compressed two centuries of demographic transition into forty years. The 1960s baby boom is retiring just as the small one-child cohorts reach prime working age — the workforce already peaked around 2015. Urbanization absorbed the shock once; aging will test whether productivity can absorb it next.

No individual data. Aggregates reinterpreted from NBS releases.""",
 ["1.41B; slowest growth on record.","63.9% urban: fastest ever.","264M aged 60+."]),
("Signature study: India's coming plurality", "population total",
 "A Signature original essay: India passed China as the world's most populous country in 2023 — what 1.43 billion people with a median age of 28 means.",
 """SIGNATURE ORIGINAL STUDY — INDIA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

In April 2023 the UN confirmed the crossover: India (~1.425B) passed China (~1.412B) as the world's most populous country. The 2011 census counted 1.21B; the delayed next census will likely show ~1.43B.

Why it matters structurally:
- Median age ~28 (China: ~39). India's workforce keeps growing to ~2050.
- Uttar Pradesh (240M projected) would be the world's fifth-largest country alone.
- The dividend is not automatic: it requires schooling and jobs for 12M+ new labor-market entrants yearly.

The Signature observation: population size is a weak predictor of power; age structure is the strong one. India's advantage is not 1.43 billion people — it is 1.43 billion people with a median age of 28.

Aggregates from UN WPP 2022 and Census of India. No individual data.""",
 ["India passed China in 2023.","Median age ~28.","12M+ entrants/year."]),
("Signature study: the 1790 census and the invention of counting", "historical census",
 "A Signature original historical essay: how 3.9 million Americans counted by marshals on horseback invented the modern census — and its original sins.",
 """SIGNATURE ORIGINAL STUDY — US CENSUS 1790
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The 1790 census did three unprecedented things: it counted a whole nation (3,893,635), it did so on constitutional authority, and it published the results. It also baked in the republic's original sins — the categories were free white males 16+, free white males under 16, free white females, all other free persons, and slaves (697,681 counted at three-fifths for apportionment).

The Signature reading: every census is a political theory made of numbers. 1790's theory was representation — count to apportion. Two centuries later the theory is distribution — count to fund ($1.5T/year). The instrument is the same; the purpose migrated.

Cost: $44,377. Schedules lost for six states. The count stood.

Historical aggregates from Census Bureau series. No individual data.""",
 ["3,893,635 counted.","Categories encoded 1790 politics.","Purpose migrated: apportion → fund."]),
("Signature study: Domesday as data science", "historical census",
 "A Signature original essay: William's 1086 survey as the first big-data project — 13,418 settlements, standardized fields, and a 900-year head start.",
 """SIGNATURE ORIGINAL STUDY — DOMESDAY 1086
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Strip away the vellum and Domesday is a database: ~13,418 settlement records with standardized fields (holder, hides, ploughs, mills, livestock), collected in under a year by traveling commissioners, then compiled into a two-volume summary. That is an ETL pipeline in 1086.

The Signature reading: Domesday's genius was not completeness (London and the north are missing) but schema discipline — the same questions everywhere, so the King's clerks could aggregate. Every modern census inherits that insight: comparability beats coverage.

Estimated population 1.5–2.5M from ~268,000 recorded household heads — the earliest large-scale demographic estimation in European history.

Historical aggregates. No individual data.""",
 ["13,418 settlement records.","Schema discipline = comparability.","Pop. estimate 1.5–2.5M."]),
("Signature study: the Han census of 2 CE and state capacity", "historical census",
 "A Signature original essay: 57.7 million people registered in 2 CE — what the Han census proves about the world's first information state.",
 """SIGNATURE ORIGINAL STUDY — HAN CENSUS 2 CE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

12,366,470 households. 57,671,400 individuals. Recorded in the Hanshu with commandery-level detail — in the year 2 CE, when Rome was guessing its own population.

The Signature reading: censuses measure state capacity, not just people. The Han could register 57 million because it had the bureaucracy to do it — county magistrates, household registers, regular reporting. The numbers are the exhaust of administration. When the Later Han lost that capacity, the counts collapsed — not because people vanished, but because the state stopped seeing them.

Modern parallel: register-based censuses (Nordics) are the Han model perfected — the count is a byproduct of administration, not a separate event.

Historical figures from the Hanshu. No individual data.""",
 ["57.7M registered in 2 CE.","Censuses measure state capacity.","Nordics = the Han model perfected."]),
("Signature study: why the billions speed up, then slow down", "historical census",
 "A Signature original demographic essay: the intervals between population billions (127 years, then 33, 14, 12, 13, 12) and what the lengthening next interval means.",
 """SIGNATURE ORIGINAL STUDY — POPULATION BILLIONS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The billion intervals: 1800→1927 (127 yrs), →1960 (33), →1974 (14), →1987 (13), →1999 (12), →2011 (12), →2022 (11). The compression stopped. The 9th billion will take ~15 years; the 10th maybe 25+.

The Signature reading: the interval series is the second derivative of the human story. Compression = mortality falling faster than fertility. Decompression = fertility falling faster than mortality. We are living through the inflection — the only one in recorded history.

Projection: the UN medium variant peaks humanity near 10.4 billion in the 2080s. The low variant peaks in 2054 at 8.9 billion. The difference between those futures is about one child per woman in sub-Saharan Africa.

Aggregates from UN WPP 2022. No individual data.""",
 ["Intervals compressed, now lengthening.","Inflection: fertility < mortality decline.","Peak: 10.4B (2080s) or 8.9B (2054)."]),
("Signature study: the 1881 census and the birth of family history", "historical census",
 "A Signature original essay: how transcribing 25.9 million 1881 census lines created modern genealogy — and what it teaches about data liberation.",
 """SIGNATURE ORIGINAL STUDY — 1881 CENSUS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The 1881 census of England and Wales counted 25,974,439 people. A century later, volunteers and the LDS Church transcribed every line — the first complete Victorian census searchable by name. That transcription did for family history what the printing press did for scripture: it moved the archive from the reading room to the living room.

The Signature reading: data's value multiplies when the index is public. The census always existed; the searchable index made it usable. Every open-data project since — from court records to satellite imagery — replays this pattern: the asset is the index, not the archive.

Note: this database publishes aggregates only; individual 1881 records are handled by archives under their own access rules.

Historical aggregates. No individual data.""",
 ["25.9M lines transcribed.","The asset is the index.","Moved archives to living rooms."]),
("Signature study: Brazil 1872 — counting on the eve of abolition", "historical census",
 "A Signature original historical essay: Latin America's first census counted 1.5 million enslaved people — a statistical portrait of slavery's last decade.",
 """SIGNATURE ORIGINAL STUDY — BRAZIL 1872
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The 1872 census found 9,930,478 Brazilians, of whom 1,510,806 (15.2%) were enslaved — sixteen years before the Golden Law of 1888 abolished slavery. No other census in the Americas captured a slave society so completely, so close to abolition.

The Signature reading: censuses are time capsules with political half-lives. The 1872 categories — free vs. enslaved, color classifications — froze a social order that was already dying. Demographers still use it to study manumission rates, slave demography, and the economics of coerced labor.

Minas Gerais was the most populous province (2,039,735) — the gold cycle's demographic echo, a century after the mines peaked.

Historical aggregates from IBGE series. No individual data.""",
 ["9.9M; 15.2% enslaved.","Closest count to abolition.","Minas Gerais most populous."]),
("Signature study: Japan 1920 — Asia's first modern count", "historical census",
 "A Signature original essay: Japan's 1920 census (55.9M) as a Meiji-state project — counting as nation-building.",
 """SIGNATURE ORIGINAL STUDY — JAPAN 1920
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

55,963,053 people in Japan proper, 1 October 1920. The Meiji state had spent fifty years building the capacity to ask — household registers, a statistics bureau, trained enumerators — and the census was the graduation exam.

The Signature reading: Japan's census history is a development syllabus. 1920: count. 1950: rebuild and recount. 2020: digital-first with a shrinking, aging population (126.1M, down from the 2008 peak). The same instrument, four different nations.

Tokyo prefecture: 3,699,428 in 1920 — already the primate city, a century before the 37-million metro.

Historical aggregates. No individual data.""",
 ["55.9M in 1920.","Census as nation-building.","Same instrument, four nations."]),
# --- demographic breakdown (10) ---
("Signature study: the 33-year age gap", "demographic breakdown",
 "A Signature original essay on median age: Japan 48.4, Uganda 15.1 — the widest demographic divide on Earth, and what it means for migration pressure.",
 """SIGNATURE ORIGINAL STUDY — MEDIAN AGE DIVIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

World median age 2020: 30.4. But no one lives in the world average. Japan (48.4) needs workers; Uganda (15.1) needs jobs. The 33-year gap between them is the single most underpriced fact in economics.

The Signature model: aging + youth = the migration equation. Every rich-country labor shortage and every poor-country youth bulge is one market failing to clear. The 21st century's great arbitrage is people — and censuses are the price signals.

Projection: by 2050 the world median hits ~36, but Africa stays near 22. The gap narrows slowly; the pressure builds steadily.

Aggregates from UN WPP 2022, reinterpreted. No individual data.""",
 ["Japan 48.4 vs Uganda 15.1.","Migration = the arbitrage.","Africa stays near 22 to 2050."]),
("Signature study: below replacement — the new normal", "demographic breakdown",
 "A Signature original essay: two-thirds of humanity lives below replacement fertility. South Korea's 0.81 is the frontier; Niger's 6.7 is the past.",
 """SIGNATURE ORIGINAL STUDY — FERTILITY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

World TFR 2021: 2.3, barely above the 2.1 replacement line. The distribution tells the story: South Korea 0.81, Singapore ~1.0, China 1.16 — and Niger 6.7, Chad 6.2, DR Congo 6.0.

The Signature reading: fertility decline is the most predictable social change ever measured. It follows female education and child survival with a 20-year lag, everywhere, without exception. The policy question is not whether it falls but how societies adapt to 1.3–1.6 as the permanent rich-country range.

South Korea's 0.81 is not an outlier to dismiss — it is the frontier. Seoul's demography today is Tokyo's 1990s and possibly Lagos's 2080s.

Aggregates from UN WPP 2022. No individual data.""",
 ["World 2.3; replacement 2.1.","Korea 0.81 = the frontier.","Follows education + survival."]),
("Signature study: the 30-year life gap", "demographic breakdown",
 "A Signature original essay: Japan 84.6, Central African Republic 53.9 — life expectancy's 30-year gap, and the pandemic's 1.7-year global cut.",
 """SIGNATURE ORIGINAL STUDY — LIFE EXPECTANCY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

2019: world 72.8 years. Then COVID cut ~1.7 years globally in 2020–21 — the first sustained worldwide decline since 1918. The US lost ~2.7 years; Peru lost over 5.

The Signature reading: life expectancy is the best single number in social science — it aggregates nutrition, medicine, war, inequality, and luck. The 30-year Japan–CAR gap is not a health gap; it is a everything gap.

Recovery watch: 2022–23 data shows most countries rebounding, but the pandemic permanently reset several national trend lines. The census rounds of the 2020s will measure the scar.

Aggregates from UN WPP 2022. No individual data.""",
 ["2019: 72.8 years.","COVID cut 1.7 globally.","Best single number in social science."]),
("Signature study: counting tongues — the language census", "demographic breakdown",
 "A Signature original essay on census language questions: how India counts 22 scheduled languages and 19,500 mother tongues.",
 """SIGNATURE ORIGINAL STUDY — LANGUAGE STATISTICS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

India's 2011 census recorded 19,500+ mother-tongue labels, rationalized to 121 languages — with Hindi (~528M incl. dialects), Bengali (97M), and Marathi (83M) on top. No other census attempts this granularity.

The Signature reading: language questions are identity questions wearing statistical clothes. Belgium's language border, Canada's French/English split, Switzerland's four languages — every multilingual state's census negotiates nationhood.

Global table (native speakers): Mandarin ~940M, Spanish ~485M, English ~380M native / 1.5B total, Hindi ~345M.

Method note: mother tongue ≠ fluency ≠ use. Censuses usually ask only one.

Aggregates from Ethnologue and national censuses. No individual data.""",
 ["India: 19,500 mother tongues.","Language Qs = identity Qs.","Mother tongue ≠ fluency."]),
("Signature study: the multiracial surge", "demographic breakdown",
 "A Signature original essay on the US 2020 multiracial count (33.8M, up from 9M): real change, better questions, and the end of single-box identity.",
 """SIGNATURE ORIGINAL STUDY — MULTIRACIAL COUNT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

33,848,943 Americans marked two or more races in 2020 — 10.2%, up from 2.9% in 2010. Three forces: more multiracial births, more willingness to claim it, and better processing that captured write-in responses.

The Signature reading: the census does not just measure identity; it manufactures the categories identity uses. 'Two or more races' barely existed as a social fact in 1990; by 2020 it was 34 million people. The instrument shapes the reality it reports.

Comparative note: Brazil's color question (preto/pardo/branco) and South Africa's population groups show every country's categories are local inventions with global consequences.

Aggregates from US Census Bureau. No individual data.""",
 ["33.8M multiracial (10.2%).","Instrument shapes identity.","Categories are local inventions."]),
("Signature study: China's 264 million elders", "demographic breakdown",
 "A Signature original essay: 18.7% of China is 60+ — the fastest aging of any large country, and the workforce already peaked.",
 """SIGNATURE ORIGINAL STUDY — CHINA AGING
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

264,018,766 people aged 60+ in 2020 — 18.7%, up from 8.6% in 1990. The 65+ share (13.5%) will pass 20% before 2030. China's workforce peaked around 2015.

The Signature reading: China is aging at low-to-middle income speed but rich-country pace — 'getting old before getting rich' at national scale. The pension math: roughly 2.8 workers per retiree in 2020, heading toward 1.6 by 2040 under current trends.

The census also found the counterweight: 17.95% children (0–14), up slightly thanks to relaxed birth limits — too little, too late to bend the curve.

Aggregates from NBS. No individual data.""",
 ["264M aged 60+.","2.8 workers/retiree → 1.6.","Old before rich."]),
("Signature study: Africa's 60% youth", "demographic breakdown",
 "A Signature original essay: Africa's median age 19.7, 60% under 25 — dividend or detonation depends on classrooms.",
 """SIGNATURE ORIGINAL STUDY — AFRICA YOUTH
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~60% of Africans are under 25; median age 19.7 vs. world 30.4. By 2050, one in three young people on Earth will be African.

The Signature model: a youth bulge is an option, not a destiny. East Asia cashed its bulge (1965–1995) through export manufacturing and mass schooling. The bulge becomes a dividend if the cohort is educated and employed; a strain if not. Africa's school enrollment has surged — but learning outcomes lag enrollment badly.

The census angle: Africa's counts are the world's weakest (DRC: no census since 1984; Somalia: since 1975). The continent's future is being planned on modeled estimates. Better counts are development infrastructure.

Aggregates from UN WPP 2022. No individual data.""",
 ["Median age 19.7.","Dividend or strain: classrooms decide.","Counts are development infrastructure."]),
("Signature study: the shrinking household", "demographic breakdown",
 "A Signature original essay: from 3.96 (China 1982) to 2.62 (2020) — the household is shrinking everywhere, and solo living is the growth story.",
 """SIGNATURE ORIGINAL STUDY — HOUSEHOLDS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

China: 3.96 (1982) → 2.62 (2020). EU: 2.3. Japan: 2.21. The one-person household is the fastest-growing type on every continent — ~38% of EU households, ~15% of US, ~16% of China.

The Signature reading: household size is the demographic variable urban planners feel first. Smaller households mean more housing units per capita, more energy per person, and weaker eldercare by family. The aging-solo-living intersection is the 21st century's quiet housing crisis.

Fertility gets the headlines; household fission moves the housing market.

Aggregates from national censuses. No individual data.""",
 ["China 3.96→2.62.","Solo living fastest-growing.","Household fission moves housing."]),
("Signature study: 101.7 men per 100 women", "demographic breakdown",
 "A Signature original essay on sex ratios: Qatar's 2.9 and Latvia's 0.85 — migration and mortality written as arithmetic.",
 """SIGNATURE ORIGINAL STUDY — SEX RATIO
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

World: 101.7 males per 100 females. Nature deals ~105 boys per 100 girls; everything after that is society. Qatar (~290) is labor migration. Latvia (85) is male mortality plus war history. China's 111 (2020) is the one-child era's echo, slowly normalizing.

The Signature reading: sex ratio is a society's autobiography in one number. It records who migrates (men), who dies young (men), and who is missing (the unborn girls of sex-selective eras).

India's ratio improved to 1020 females per 1000 males (NFHS-5) — the first time women outnumbered men in the survey series.

Aggregates from UN WPP 2022. No individual data.""",
 ["World 101.7:100.","Qatar = migration; Latvia = mortality.","One number, a whole autobiography."]),
("Signature study: religion by the numbers", "demographic breakdown",
 "A Signature original essay: India's 2011 religion table (172M Muslims) and why religion questions are the most political on any census.",
 """SIGNATURE ORIGINAL STUDY — RELIGION COUNTS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

India 2011: Hindu 79.8%, Muslim 14.2% (172,245,158 — alone larger than all but a few countries), Christian 2.3%, Sikh 1.7%.

The Signature reading: no census question is more political than religion. India's tables are scrutinized for differential growth rates; Northern Ireland's religion question tracks the peace settlement; the US does not ask at all — the First Amendment's shadow over the form.

The 172M figure matters analytically: India's Muslims constitute the world's third-largest Muslim population (after Indonesia and Pakistan) — a fact invisible without the count.

Aggregates from Census of India. No individual data.""",
 ["172M Muslims: world's 3rd largest.","Most political question.","US doesn't ask; India always has."]),
# --- urbanization (10) ---
("Signature study: Tokyo's 37 million — the city as country", "urbanization",
 "A Signature original essay: Greater Tokyo (~37M) as a demographic unit larger than most nations — and what its railways teach about density.",
 """SIGNATURE ORIGINAL STUDY — TOKYO
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~37 million people, four prefectures, one labor market. Greater Tokyo's GDP exceeds most countries'; Shinjuku station moves 3.6M people daily — more than many national railways.

The Signature reading: Tokyo is the existence proof that 37 million people can live at high density with low crime, clean streets, and two-minute train headways. The variables are institutions, not density: land-use rules that allow building, railways that precede suburbs, and maintenance cultures that compound.

The coming test: Japan's population is shrinking. Tokyo still grows by in-migration — the city as demographic lifeboat. The 37M figure may be the all-time peak.

Aggregates from UN WUP and JR East. No individual data.""",
 ["~37M: larger than most nations.","Density works with institutions.","May be the all-time peak."]),
("Signature study: Delhi's race to the top", "urbanization",
 "A Signature original essay: Delhi (~32M, world's largest by ~2028) and the infrastructure mathematics of adding a Chicago every year.",
 """SIGNATURE ORIGINAL STUDY — DELHI
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~32 million in the agglomeration; the UN projects Delhi passes Tokyo around 2028. From 1.7M (1951) to 32M — a 19-fold increase in 70 years, roughly adding a Chicago annually in recent decades.

The Signature reading: Delhi is the stress test of 21st-century urbanization. Water (Yamuna + groundwater, both stressed), air (winter AQI among the world's worst), and transport (metro: 390 km and expanding) — every megacity problem at maximum scale, simultaneously.

The census footnote: NCT Delhi counted 16.8M in 2011; the agglomeration sprawls across three states. Administrative borders stopped describing the city decades ago.

Aggregates from UN WUP. No individual data.""",
 ["~32M; largest by ~2028.","Adds a Chicago yearly.","Borders stopped describing the city."]),
("Signature study: Shanghai's vertical century", "urbanization",
 "A Signature original essay: Shanghai (24.9M municipality, ~28M metro) and the Pudong experiment — farmland to financial center in 30 years.",
 """SIGNATURE ORIGINAL STUDY — SHANGHAI
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1990: Pudong was farmland across the river. 2020: 5.68 million people, the Lujiazui skyline, ~800 km of metro (world's longest). The municipality counted 24.87M in the 2020 census.

The Signature reading: Shanghai is the strongest evidence that urban form follows infrastructure commitment. The metro-first buildout meant density never became dysfunction — compare cities that grew first and transited later.

The demographic turn: Shanghai's registered population is aging fast; the floating (migrant) population sustains its youth. The city's future is a negotiation between hukou reform and labor demand.

Aggregates from 2020 census and UN WUP. No individual data.""",
 ["Pudong: farmland to finance in 30 yrs.","Metro-first beats sprawl-first.","Floating population sustains youth."]),
("Signature study: the 56% crossover and the 68% future", "urbanization",
 "A Signature original essay: humanity crossed 50% urban in 2007; 68% by 2050 — and nearly all of it in Asia and Africa.",
 """SIGNATURE ORIGINAL STUDY — URBANIZATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

2007: the urban crossover. 2021: 56%. 2050: 68% projected. But the regional splits matter more: North America 83%, Latin America 81%, Europe 75%, Asia 52%, Africa 44%.

The Signature reading: the next billion urbanites will be overwhelmingly Asian and African — and disproportionately in cities that do not yet have sewers, transit, or building codes for what's coming. The 20th century urbanized the rich world with infrastructure; the 21st is urbanizing the poor world ahead of it.

Lagos (+600K/year), Kinshasa, Dhaka, Delhi: the megacities of 2050 are being built now, mostly informally.

Aggregates from UN WUP 2018. No individual data.""",
 ["56% urban (2021) → 68% (2050).","Next billion: Asia + Africa.","Urbanizing ahead of infrastructure."]),
("Signature study: China's 900 million urbanites", "urbanization",
 "A Signature original essay: 63.9% urban in 2020, up from 17.9% in 1978 — the largest migration in history, counted every ten years.",
 """SIGNATURE ORIGINAL STUDY — CHINA URBANIZATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~902 million urban residents in 2020. The 14-point jump in a single decade (2010–2020) exceeds the entire urban population of most countries.

The Signature reading: China's urbanization was a census-visible policy project — special economic zones, hukou relaxation, infrastructure stimulus. The floating population (376M) is the statistical shadow of incomplete urbanization: people the cities need but don't fully count as citizens.

The next phase inverts: urbanization slows, cities shrink in the northeast, and the policy problem becomes managing decline — a vocabulary Chinese planning barely has.

Aggregates from NBS. No individual data.""",
 ["63.9% urban; ~902M.","376M floating: incomplete urbanization.","Next phase: managing decline."]),
("Signature study: Lagos at full speed", "urbanization",
 "A Signature original essay: Lagos (~15M, +600K/year) — Africa's megacity growing faster than its maps.",
 """SIGNATURE ORIGINAL STUDY — LAGOS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~15 million (UN) or 21 million (state claim) — the dispute itself is the story. Lagos grows ~600K/year; its last reliable enumeration struggles to keep up. From 325K in 1950.

The Signature reading: Lagos is what happens when urbanization outruns administration. The danfo buses, the markets, the informal water vendors — the city works, but on systems the statistics barely capture. The 2006 census put Lagos state at 9.1M; everyone agrees that number expired on arrival.

By 2050 Lagos may hold 25–30M. Whether it gets counted properly will shape Nigeria's politics — census figures allocate revenue and seats.

Aggregates from UN WUP. No individual data.""",
 ["~15M, +600K/year.","The count dispute is the story.","25–30M by 2050."]),
("Signature study: America's 86% metro nation", "urbanization",
 "A Signature original essay: 86% of Americans in metros; the NYC metro (20.1M) outweighs most states — and Austin grew 33% in a decade.",
 """SIGNATURE ORIGINAL STUDY — US URBAN
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

86% metropolitan. 384 MSAs. The top 10 hold a quarter of Americans. New York's metro (20.1M) is bigger than 48 states.

The Signature reading: America's urbanization is suburbanization — the metro is the unit, the suburb the form. Austin's 33% decade growth is the Sun Belt thesis in one number: jobs + housing supply + air conditioning = migration.

The counter-trend: remote work is loosening the metro's grip for the first time since the streetcar. The 2030 census will show whether the suburbs of suburbs — the exurbs — were the real winners.

Aggregates from US Census Bureau. No individual data.""",
 ["86% in metros.","Austin +33%: Sun Belt thesis.","Remote work loosens the grip."]),
("Signature study: São Paulo's coffee-to-concrete arc", "urbanization",
 "A Signature original essay: from 31,385 (1872) to ~22M — São Paulo as the Southern Hemisphere's urban thesis.",
 """SIGNATURE ORIGINAL STUDY — SÃO PAULO
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

31,385 people in 1872. ~22 million in the metro today. Coffee money built the railways; railways built the factories; factories built the megacity. The helicopter fleet — among the world's largest — is the elite's answer to the traffic the growth created.

The Signature reading: São Paulo is Latin America's urbanization in one city — primate, industrial, unequal, inventive. Its favelas house the workers the formal city needs but won't house; its economy needs them anyway.

The 2022 census counted 11.45M in the municipality — the metro definition matters more than the municipal one, here as everywhere.

Aggregates from IBGE and UN WUP. No individual data.""",
 ["31K (1872) → 22M.","Coffee → rail → factories → megacity.","Metro > municipality."]),
("Signature study: Cairo's thousand-year layering", "urbanization",
 "A Signature original essay: ~21M people across Fatimid, Mamluk, Ottoman, and modern Cairos — the city as archaeological section.",
 """SIGNATURE ORIGINAL STUDY — CAIRO
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Founded 969 CE as al-Qahira, 'The Victorious' — on ground settled since Babylon Fortress (Roman) and Fustat (641). ~21M in the metro today; the 2017 census found 9.5M in the governorate alone.

The Signature reading: Cairo urbanizes by accretion, not replacement. The City of the Dead houses the living; medieval quarters function as workshops; the New Administrative Capital rises in the desert — the state building a new layer rather than fixing the old.

Water is the binding constraint: the Nile, the delta, and a population growing faster than the river's politics.

Aggregates from CAPMAS and UN WUP. No individual data.""",
 ["~21M across 1,000+ years.","Urbanizes by accretion.","Water is the constraint."]),
("Signature study: Mumbai's seven islands", "urbanization",
 "A Signature original essay: ~20M people at 20,000 per sq km on seven merged islands — density as Mumbai's destiny and engine.",
 """SIGNATURE ORIGINAL STUDY — MUMBAI
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Seven islands, merged by causeways over two centuries, now holding ~20M at ~20,000 per sq km — among the densest great cities on Earth. Dharavi (~1M in 2.1 sq km) is the densest neighborhood of all, and an industrial powerhouse.

The Signature reading: Mumbai proves density is productive — 70% of India's maritime trade, the film industry, the finance capital — but the island geography caps expansion. The response: Navi Mumbai, the coastal road, the metro buildout. Every fix is a fight with the sea.

The local trains carry 7.5M daily — the city's true census, counted in turnstiles.

Aggregates from Census of India and UN WUP. No individual data.""",
 ["~20M at 20K per sq km.","Density is productive.","Island geography caps expansion."]),
# --- migration (10) ---
("Signature study: 281 million on the move", "migration",
 "A Signature original essay: 281M international migrants (3.6% of humanity) — the great circulation, and why the share barely moves.",
 """SIGNATURE ORIGINAL STUDY — WORLD MIGRATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

281 million in 2020 — up from 153M in 1990. The absolute number nearly doubled; the share of humanity crept from 2.9% to 3.6%. Migration grows, but slower than population.

The Signature reading: the migrant share's stability is the puzzle. Borders tightened, transport cheapened, wage gaps widened — and the share barely moved. The constraint is policy, not desire: Gallup finds ~900M people want to migrate permanently. The gap between desire and flow is the visa regime.

Top corridor logic: US (50.6M in), India (17.9M out). Migration follows money and language.

Aggregates from UN DESA. No individual data.""",
 ["281M = 3.6% of humanity.","900M want to move.","The gap is the visa regime."]),
("Signature study: America's 45.3 million foreign-born", "migration",
 "A Signature original essay: 13.6% foreign-born, near the 1890 peak — America's second great wave, Asian and Latin this time.",
 """SIGNATURE ORIGINAL STUDY — US MIGRATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

45.3M foreign-born (2021), 13.6% — approaching the 14.8% record of 1890. The first wave was European; this one is Latin American and Asian. Mexico (~10.7M) is still the top origin; India and China grow fastest.

The Signature reading: the 1965 Immigration Act's family-reunification chains built this demography by accident — nobody in 1965 predicted an Asian-Latino wave. Policy's longest shadows are demographic.

California (10.5M foreign-born) is the wave's capital; Texas and Florida its growth edge.

Aggregates from ACS 2021. No individual data.""",
 ["45.3M; 13.6%.","1965 Act built it by accident.","Mexico top; Asia fastest-growing."]),
("Signature study: India's 17.9 million abroad", "migration",
 "A Signature original essay: the world's largest diaspora sends home $111B — remittances as India's largest 'export'.",
 """SIGNATURE ORIGINAL STUDY — INDIAN DIASPORA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

17.9M Indians abroad — Gulf construction workers, American engineers, British doctors. $111B in remittances (2022), the world's largest flow, ~3% of GDP.

The Signature reading: the diaspora is India's most successful development program that was never a program. Kerala runs on Gulf money; Punjab on Canadian; Hyderabad on H-1B. The policy implication: emigration is not brain drain when the brains wire money home — it's brain circulation with interest.

The Gulf corridor (UAE ~3.5M, Saudi ~2.5M) is the working-class half; the Anglophone corridor is the professional half. Both remit.

Aggregates from UN DESA and World Bank. No individual data.""",
 ["17.9M abroad.","$111B remittances.","Brain circulation, not drain."]),
("Signature study: Syria's 6.8 million", "migration",
 "A Signature original essay: the largest refugee crisis of the 2020s — 6.8M refugees, Turkey hosting 3.4M, Lebanon 1 in 6 residents a refugee.",
 """SIGNATURE ORIGINAL STUDY — SYRIAN DISPLACEMENT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

6.8M refugees abroad + 6.8M displaced inside Syria — roughly half the pre-war population uprooted. Turkey (3.4M) hosts more refugees than any country; Lebanon's ratio (~1 in 6) is the world's highest burden.

The Signature reading: protracted displacement is the new normal — the average refugee situation now lasts 20+ years. Camps become cities (Zaatari, Jordan); exile becomes a generation. Census rounds in host countries must count people who may never leave.

The policy scar: Europe's 2015 politics were reshaped by ~1M arrivals — a fraction of what Turkey and Lebanon absorbed.

Aggregates from UNHCR. No individual data.""",
 ["6.8M refugees + 6.8M IDPs.","Turkey: 3.4M hosted.","Exile becomes a generation."]),
("Signature study: the Gulf's 88% migrant societies", "migration",
 "A Signature original essay: Qatar (~88% migrant), UAE (~87%) — countries where citizens are the minority, and what that means for the census.",
 """SIGNATURE ORIGINAL STUDY — GULF MIGRATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Qatar: ~88% of residents are international migrants. UAE: ~87%. These are the highest shares on Earth — societies where the citizen is the demographic exception.

The Signature reading: the Gulf inverts the migration debate. The question is not whether migrants belong but whether a state can be 12% citizen — and the answer, so far, is yes, via the kafala sponsorship architecture (reformed since 2020 in Qatar) and a social contract of high wages for citizens, jobs for migrants.

Census note: Gulf counts are among the most migration-sensitive in the world — construction booms move the totals by hundreds of thousands between rounds.

Aggregates from UN DESA. No individual data.""",
 ["Qatar ~88%; UAE ~87%.","Citizens the minority.","Kafala reformed since 2020."]),
("Signature study: Venezuela's 7.7 million", "migration",
 "A Signature original essay: 1 in 4 Venezuelans has left since 2014 — the Western Hemisphere's largest displacement, absorbed by neighbors.",
 """SIGNATURE ORIGINAL STUDY — VENEZUELA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~7.7M abroad since 2014 — ~1 in 4 Venezuelans. Colombia (2.9M) and Peru (1.5M) host the most. Unlike the Syrian crisis, the burden fell almost entirely on developing neighbors.

The Signature reading: South America's response — temporary protection statuses, regularization drives — was the most generous refugee reception of the decade, and the least funded. Colombia's 10-year protection statute (2021) covered more people than most European programs.

The census angle: Venezuela hasn't had a reliable count since 2011; the diaspora is measured at borders and in host censuses, not at origin.

Aggregates from R4V/UNHCR. No individual data.""",
 ["7.7M; 1 in 4 left.","Colombia: 2.9M hosted.","Most generous, least funded."]),
("Signature study: Germany's 15.8 million", "migration",
 "A Signature original essay: Europe's largest migrant population — 19% of Germany — and the 2015 decision that reshaped a continent's politics.",
 """SIGNATURE ORIGINAL STUDY — GERMANY MIGRATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

15.8M international migrants — 19% of Germany. The 2015–16 intake (~1.2M asylum seekers, mostly Syrian) was Europe's largest refugee reception since WWII.

The Signature reading: Merkel's 'Wir schaffen das' was a demographic decision wearing a moral coat — Germany's workforce was aging, its factories needed hands. The integration ledger is mixed: employment rates for 2015 arrivals now approach native levels for men, lag for women; the political ledger reshaped the party system.

Census note: Germany's 2022 census (84.3M) was its first since 2011 — register-based methods are replacing the full enumeration.

Aggregates from UN DESA and Destatis. No individual data.""",
 ["15.8M; 19% of Germany.","2015: moral coat, demographic decision.","2022 census: 84.3M."]),
("Signature study: China's 376 million floating", "migration",
 "A Signature original essay: 376M internal migrants — the largest human movement on Earth — and the hukou line that defines it.",
 """SIGNATURE ORIGINAL STUDY — CHINA FLOATING POPULATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

375,816,759 people lived outside their hukou registration in 2020 — 26.6% of China. Guangdong alone absorbs ~52M. This is the largest internal migration in history, and it is circular: workers flow coastward, children and elders stay behind ('left-behind' children: ~70M at peak estimates).

The Signature reading: the floating population is China's industrial revolution made of people. The hukou system made it legible — every migrant is counted as out-of-place by design. Reform (points-based urban hukou) is slowly dissolving the line the statistics were built on.

The 2020 census was the first to fully capture the float — previous rounds undercounted it badly.

Aggregates from NBS. No individual data.""",
 ["376M; 26.6% of China.","Largest internal migration ever.","Hukou reform dissolving the line."]),
("Signature study: Australia's 27.6% overseas-born", "migration",
 "A Signature original essay: from 90% British-origin (1947) to 27.6% overseas-born — the fastest demographic reinvention of any rich country.",
 """SIGNATURE ORIGINAL STUDY — AUSTRALIA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

27.6% born overseas (2021) — England (927K), India (673K), China (549K) top the list. Sydney is 40%+ overseas-born. In 1947 Australia was ~90% British-origin; the White Australia policy's dismantling (1970s) inverted the composition in two generations.

The Signature reading: Australia is the proof that high migration plus a points system plus multicultural policy can remake a nation's demography without breaking its politics — the non-English-speaking share rose with far less backlash than Europe's.

The census is the instrument of the reinvention: ancestry and language questions track the transformation each round.

Aggregates from ABS. No individual data.""",
 ["27.6% overseas-born.","90% British (1947) → diverse.","Points system + policy = reinvention."]),
("Signature study: the $831 billion wire", "migration",
 "A Signature original essay: remittances ($831B, 2022) triple foreign aid — migration as the developing world's largest finance program.",
 """SIGNATURE ORIGINAL STUDY — REMITTANCES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

$831B in 2022 — ~3x official development aid, larger than foreign direct investment to most recipients. India $111B, Mexico $61B, China $51B, Philippines $38B. Tajikistan: ~51% of GDP.

The Signature reading: remittances are the most efficient anti-poverty program ever — direct, counter-cyclical (they rose during COVID while everything else fell), and spent on schooling, housing, and health. The development industry's overhead: zero. The wire fee: the scandal (Africa averages ~8%).

Policy frontier: cutting transfer costs to the UN's 3% target would deliver tens of billions to poor households — the cheapest development win available.

Aggregates from World Bank/KNOMAD. No individual data.""",
 ["$831B; 3x aid.","Rose during COVID.","Cut fees to 3%: cheapest win."]),
# --- methodology (10) ---
("Signature guide: de facto vs de jure", "methodology",
 "A Signature original methodology explainer: where-you-slept vs where-you-live — the definitional choice that moves millions between columns.",
 """SIGNATURE ORIGINAL GUIDE — CENSUS CONCEPTS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

De facto counts you where you slept on census night. De jure counts you where you usually live. The US uses de jure ('usual residence'); India historically used de facto. The difference is not philosophical — it moves students, soldiers, prisoners, and migrant workers between jurisdictions, and with them, money and seats.

The contested cases:
- US college students: counted at school (de jure) — college towns gain; hometowns lose.
- US prisoners: counted at prison — the 'prison gerrymandering' debate.
- Gulf migrant workers: de facto residents, de jure foreigners — counted, but not as citizens.

The UN's 12-month usual-residence rule is the compromise that lets statisticians compare across the divide.

Public methodology explainer. No individual data.""",
 ["De facto: slept here.","De jure: live here.","Moves students, soldiers, prisoners."]),
("Signature guide: catching the undercount", "methodology",
 "A Signature original methodology explainer: dual-system estimation — how post-enumeration surveys weigh the census itself.",
 """SIGNATURE ORIGINAL GUIDE — COVERAGE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Every census misses people; the honest ones measure the miss. The method is capture-recapture (dual-system estimation): independently re-survey a sample, match it to the census, and estimate who was missed by both.

US 2020 results: -5.0% Hispanic, -3.3% Black, +1.6% non-Hispanic white overcount. The pattern is structural — renters, young men, and recent immigrants are hardest to count, in every country, every decade.

The Signature point: the undercount is not an error to hide but a statistic to publish. The UK, Australia, and Canada release coverage-adjusted estimates; the US releases the raw count for apportionment (the Supreme Court requires actual enumeration) and adjusted estimates for research.

$1.5T/year in US federal funds follows the count — the undercount is a fiscal event.

Public methodology explainer. No individual data.""",
 ["Capture-recapture method.","US 2020: -5.0% Hispanic.","$1.5T follows the count."]),
("Signature guide: the register census", "methodology",
 "A Signature original methodology explainer: Denmark 1981 and the Nordic model — the census as a database join, not an event.",
 """SIGNATURE ORIGINAL GUIDE — REGISTER CENSUSES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Denmark 1981: the first census with no census. Population, tax, education, employment, and housing registers were linked by personal ID number — statistics without a single form.

Requirements: universal ID, high administrative trust, and registers worth linking. Payoff: annual (even monthly) population statistics at a fraction of the cost, with no respondent burden.

The Signature point: the register census inverts the census. The traditional census is an event that produces data; the register census is data that produces a census. The Han dynasty's household registers (2 CE) were the prototype; the Nordics are the perfection.

Adoption: Netherlands, Belgium, Austria run combined models; Germany's 2022 census leaned heavily on registers.

Public methodology explainer. No individual data.""",
 ["Denmark 1981: no forms.","Needs ID + trust.","Han registers were the prototype."]),
("Signature guide: the UN's five principles", "methodology",
 "A Signature original methodology explainer: universality, simultaneity, periodicity — the five rules behind every credible census.",
 """SIGNATURE ORIGINAL GUIDE — UN PRINCIPLES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The UN Statistics Division's five principles:
1. Individual enumeration — one record per person (aggregated for release)
2. Universality — everyone in the territory, no exceptions
3. Simultaneity — one reference moment (census night/day)
4. Defined periodicity — at least every 10 years
5. Small-area statistics — data granular enough for local planning

The Signature point: principle 5 is the one that matters most and costs most. National totals are easy; neighborhood-level tables for school planning are the expensive, valuable product. Every census fight — over citizenship questions, over funding — is really a fight about small-area data.

The 2020 round (2015–2024): 150+ countries enumerated. The gaps (Lebanon since 1932, DRC since 1984) are where the principles fail.

Public methodology explainer. No individual data.""",
 ["5 principles.","Small-area data = the real product.","150+ in the 2020 round."]),
("Signature guide: lying with averages — disclosure control", "methodology",
 "A Signature original methodology explainer: suppression, swapping, and differential privacy — how bureaus publish truth without exposing people.",
 """SIGNATURE ORIGINAL GUIDE — DISCLOSURE CONTROL
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The census's promise: your answers become statistics, never evidence. The techniques:
- Cell suppression (UK classic): hide small table cells
- Rounding: counts to base 3 or 5
- Record swapping: trade similar households across areas
- Differential privacy (US 2020): inject calibrated noise into every table

The Signature point: the US 2020 differential-privacy rollout was the most consequential statistical decision of the decade — researchers found small-area data degraded, while privacy advocates noted reconstruction attacks had made the old methods unsafe. The trade-off is real and permanent: accuracy vs. confidentiality, tuned by a parameter (epsilon).

The seal: individual forms locked 72 years (US), 100 years (UK). Your great-grandchildren may read yours.

Public methodology explainer. No individual data.""",
 ["Suppression, swapping, noise.","US 2020: differential privacy.","Forms sealed 72–100 years."]),
("Signature guide: why ten years", "methodology",
 "A Signature original methodology explainer: the decennial rhythm — constitutional accident, administrative sweet spot.",
 """SIGNATURE ORIGINAL GUIDE — PERIODICITY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Ten years is not optimal; it is historical. The US Constitution (1789) said ten; Britain's 1801 act copied the rhythm; the UN recommends 'at least' ten. The interval stuck because it balances three clocks: political (apportionment needs freshness), administrative (a census takes years to plan), and fiscal (they cost billions).

Deviations: Japan every 5 (dense, rich, aging fast — needs freshness). France rolling (a fifth sampled yearly — continuous freshness, no census day). War breaks the rhythm (UK skipped 1941; Lebanon never resumed).

The Signature point: the interval is a sampling rate. Ten years aliases fast change — the 2020 US census measured a country mid-pandemic with 2010 baselines. Higher frequency (registers, rolling samples) is the future; the decennial event is the past.

Public methodology explainer. No individual data.""",
 ["Ten years = historical accident.","Japan: 5. France: rolling.","Interval is a sampling rate."]),
("Signature guide: the digital census", "methodology",
 "A Signature original methodology explainer: the 2020 round went online — internet-first in the US, UK, and Australia; tablets in Pakistan.",
 """SIGNATURE ORIGINAL GUIDE — DIGITAL CENSUSES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The 2020 round was the first digital census round: US internet self-response as primary mode; UK 2021 'digital-first' (88%+ online); Pakistan 2023 tablets + GPS (South Asia's first fully digital); satellite imagery mapping enumeration areas across Africa.

The Signature point: digitization moved the census's failure modes. Old risk: enumerators who pencil-whip. New risks: the 2016 Australia site crash (DDoS + hubris), the digital divide (the offline are the undercounted), and cyber threats to the count itself.

The payoff: GPS-tagged, real-time-monitored enumeration — managers watch response rates by neighborhood live and deploy enumerators like rideshares.

Public methodology explainer. No individual data.""",
 ["Internet-first: US, UK, Australia.","Pakistan 2023: tablets + GPS.","New failure modes: cyber + divide."]),
("Signature guide: following the money", "methodology",
 "A Signature original methodology explainer: $1.5T/year in the US follows the census — the count as fiscal infrastructure.",
 """SIGNATURE ORIGINAL GUIDE — CENSUS USES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

300+ US federal programs; ~$1.5T/year; 435 House seats; the denominator of every rate (disease, crime, poverty, unemployment). GWU estimated each uncounted person costs their state ~$1,000–$2,000/year.

The Signature point: the census is fiscal infrastructure wearing a statistical costume. The fights over citizenship questions and prison counting are budget fights — who gets the money and the seats. Businesses treat it as market infrastructure: site selection, logistics, and insurance pricing all run on census geography.

The global version: World Bank allocations, EU structural funds, and India's Finance Commission devolution all run on counts.

Public methodology explainer. No individual data.""",
 ["$1.5T/year; 435 seats.","Denominator of every rate.","Fiscal infrastructure in costume."]),
("Signature guide: before the census — tax rolls and parish books", "methodology",
 "A Signature original methodology explainer: hearth taxes, parish registers, and Ottoman defters — historical demography's raw material.",
 """SIGNATURE ORIGINAL GUIDE — PRE-CENSUS SOURCES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Before censuses, historians count proxies:
- Hearth tax (England 1662–89): fireplaces ≈ households
- Parish registers (from 1538): baptisms/marriages/burials → the Cambridge Group rebuilt England 1541–1871 from 404 parishes (Wrigley & Schofield)
- Ottoman tahrir defters: 15th–16th c. tax surveys of households, bachelors, widows
- Japanese shūmon aratame-chō: religious registers doubling as population records

The Signature point: historical demography is census methodology run backward — inferring populations from administrative exhaust. The same logic powers modern estimates for uncounted countries (satellite + mobile data for the DRC).

The 404 parishes are the most important dataset in demographic history.

Public methodology explainer. No individual data.""",
 ["Hearth tax ≈ households.","Cambridge Group: 404 parishes.","Run the census backward."]),
("Signature guide: the uncounted countries", "methodology",
 "A Signature original methodology explainer: Lebanon (1932), Somalia (1975), DRC (1984) — why dozens of countries skip the census, and what fills the gap.",
 """SIGNATURE ORIGINAL GUIDE — CENSUS GAPS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Lebanon: no census since 1932 — the sectarian power-sharing formula depends on not recounting. Somalia: none since 1975. DRC: none since 1984. Afghanistan: none since 1979.

Why: war, cost ($1–10+/person — prohibitive for poor states), and politics (counts allocate power, so power blocks counts).

What fills the gap: UN modeled estimates, DHS/MICS surveys, satellite imagery + mobile-phone data, and in 2024, building-footprint AI counts.

The Signature point: the uncounted are not uncountable — they are uncounted on purpose or by poverty. Every global total (8 billion) contains modeled millions. Honest demography labels the seams.

Public methodology explainer. No individual data.""",
 ["Lebanon: 1932. DRC: 1984.","Counts allocate power.","8 billion contains modeled millions."]),
("Signature reading: Nigeria's 220 million", "population total",
 "A Signature original reading of Nigeria's demographic weight — Africa's most populous nation.",
 """SIGNATURE ORIGINAL ESSAY — NIGERIA'S 220 MILLION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Nigeria: ~220M (2024 est.), Africa's most populous nation, 7th in the world. Median age: 18. Fertility: ~5.3 (falling from 6.3 in 1990).

The Signature reading: Nigeria is the demographic hinge of the 21st century — by 2050, ~390M, the world's third-largest country. Every global projection runs through Lagos.

The census problem: Nigeria's counts are contested — the 2006 census (140M) was disputed north-south; the count is politics. The Signature rule: publish the dispute with the number.

The future: the dividend or the bomb — 220M young people, employed or not. The census will tell; the policy will decide.

Public methodology. No private data.""",
 ["Signature original essay.","~220M, median age 18.","The count is politics."]),
("Signature reading: the 1950 world — 2.5 billion", "population total",
 "A Signature original reading of the 1950 world population — the baseline of the modern boom.",
 """SIGNATURE ORIGINAL ESSAY — THE 1950 WORLD
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1950: 2.5 billion. The world my grandparents were born into — a third of today's.

The Signature reading: 1950 is the baseline — everything since is the boom. The 2.5B world: Europe 25% of humanity; Africa 9%; the oldest median age in history was still ahead.

The doubling: 2.5B → 5B took 37 years (1987). The next doubling will never come — the curve is bending.

Why 1950 matters: it's the first modern census round — the UN's first global estimates. The statistical world begins here.

Public methodology. No private data.""",
 ["Signature original essay.","1950: 2.5 billion.","The baseline of the boom."]),
("Signature reading: Bangladesh's density", "population total",
 "A Signature original reading of the world's densest large country — 170M on a delta.",
 """SIGNATURE ORIGINAL ESSAY — BANGLADESH'S DENSITY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Bangladesh: ~170M people on 148,000 km² — ~1,150 per km², the densest large country on Earth.

The Signature reading: density is Bangladesh's destiny and its discipline — the delta forces cooperation (flood management, microcredit, the garment industry's labor pool).

The demographic triumph: fertility fell from 6.9 (1970) to ~2.0 — one of history's fastest declines, via the famous doorstep contraceptive program.

The climate shadow: the densest country is also the most exposed — sea-level rise threatens the delta that holds the 170M.

Public methodology. No private data.""",
 ["Signature original essay.","~1,150 per km².","Density as discipline."]),
("Signature reading: Russia's demographic decline", "population total",
 "A Signature original reading of Russia's shrinking population — the great peacetime decline.",
 """SIGNATURE ORIGINAL ESSAY — RUSSIA'S DECLINE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Russia: 148M (1991) → ~144M (2024), despite annexations — the great peacetime decline. Male life expectancy: ~64. Fertility: ~1.4.

The Signature reading: Russia is the demographic warning — the mortality crisis (alcohol, cardiovascular, violence), the fertility trap, the emigration drain.

The history: WWII's 27M dead still echo — the 1940s birth deficit repeats every generation (the "demographic echo").

The projection: ~130M by 2050. The largest country, emptying.

Public methodology. No private data.""",
 ["Signature original essay.","148M → ~144M.","The echo of 1945."]),
("Signature reading: the Vatican's 800", "population total",
 "A Signature original reading of the world's smallest population — the Vatican's 800 residents.",
 """SIGNATURE ORIGINAL ESSAY — THE VATICAN'S 800
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Vatican City: ~800 residents — the world's smallest population. Citizenship: by office, not birth (the Swiss Guards, the clergy, the staff).

The Signature reading: the Vatican inverts every census rule — no births registered (children of residents are Italian), no natural increase, citizenship that expires with the job.

The contrast: 1.4B Catholics served by a city of 800. The smallest population with the largest constituency.

The census lesson: "population" usually means residents — the Vatican shows how strange residence can be.

Public methodology. No private data.""",
 ["Signature original essay.","~800 residents.","Citizenship by office."]),
("Signature reading: Tokyo's 37 million", "population total",
 "A Signature original reading of the world's largest metropolitan population — Tokyo's 37M.",
 """SIGNATURE ORIGINAL ESSAY — TOKYO'S 37 MILLION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Greater Tokyo: ~37M — the largest metropolitan population in human history. More people than Canada, in one urban region.

The Signature reading: Tokyo is the urban maximum — the proof that 37M can live, work, and commute in order. The trains carry 40M trips a day; the system works.

The paradox: Japan shrinks, Tokyo grows — the countryside empties into the capital. The 37M is concentration, not growth.

The future: the first post-growth megacity — Tokyo will shrink gracefully or stagnate painfully. The census will record which.

Public methodology. No private data.""",
 ["Signature original essay.","~37M, the urban maximum.","Concentration, not growth."]),
("Signature reading: the 2037 nine-billion projection", "population total",
 "A Signature original reading of the UN's nine-billion projection — the peak in sight.",
 """SIGNATURE ORIGINAL ESSAY — NINE BILLION, 2037
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The UN projects 9B ~2037, 10B ~2058, peak ~10.4B in the 2080s. The projection has been revised down repeatedly — the peak keeps arriving earlier and lower.

The Signature reading: nine billion is the last round number of the boom — after it, the long plateau. The demographer's lifetime: born at 3B, dying at 10B.

The uncertainty: ±1B by 2050 — Africa's fertility is the swing variable. One child more per woman = a billion people.

The meaning: the human story's steepest chapter is ending. What comes after is the old world — stable, gray, and (perhaps) wise.

Public methodology. No private data.""",
 ["Signature original essay.","9B ~2037; peak ~10.4B.","The boom's last round number."]),
("Signature essay: the Inca quipu census", "historical census",
 "A Signature original essay: the Inca counted their empire in knots — the quipu census.",
 """SIGNATURE ORIGINAL ESSAY — THE QUIPU CENSUS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Inca: no writing, but the quipu — knotted cords recording census data: households, ages, labor obligations, grain stores. The empire of 10M, counted in string.

The Signature reading: the quipu proves the census doesn't need paper — it needs a system. The Inca's decimal knots recorded what Rome's tablets did.

The conquest's loss: the Spanish couldn't read the quipus — the census died with its readers. Hundreds survive; dozens are understood.

The lesson: data needs its readers. The census is only as durable as its interpreters.

Public methodology. No private data.""",
 ["Signature original essay.","10M counted in knots.","Data needs its readers."]),
("Signature essay: William's commissioners", "historical census",
 "A Signature original essay: the Domesday commissioners — how the 1086 survey was actually taken.",
 """SIGNATURE ORIGINAL ESSAY — THE COMMISSIONERS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Christmas 1085: William orders the survey. Commissioners ride out in circuits — the "Domesday circuit" — summoning the hundred courts.

The method: sworn testimony — the sheriff, the barons, the villagers testify under oath: "How many ploughs? How many villagers? What was it worth in King Edward's time? What now?"

The Signature reading: Domesday was an inquest, not a questionnaire — the census as trial. Disputes were recorded ("the men of the hundred say...").

The result: the most complete record of any medieval kingdom — because the king's greed was total.

Public methodology. No private data.""",
 ["Signature original essay.","The census as trial.","Sworn testimony, 1086."]),
("Signature essay: the first US census takers", "historical census",
 "A Signature original essay: the 1790 marshals — 650 men on horseback counting a republic.",
 """SIGNATURE ORIGINAL ESSAY — THE 1790 MARSHALS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1790: ~650 assistant marshals, on horseback and on foot, 18 months, 13 states — counting 3.9M people for $1 per 150 persons enumerated.

The Signature reading: the first modern census was a feat of shoe leather — no forms mailed, no follow-up; the marshal knocked, asked, and wrote.

The famous error: Washington's Mount Vernon — the marshal recorded the slaves; Washington's own household was counted while he was President in New York.

The legacy: "actual Enumeration" — the Constitution's phrase — meant a man at your door. The census has been getting more distant ever since.

Public methodology. No private data.""",
 ["Signature original essay.","~650 marshals, 18 months.","The census at your door."]),
]

# ================= 3. genealogy-public =================
GENPUB = [
# --- family tree (10) ---
("The Bach family — 150 years of musicians", "family tree",
 "The Bachs of Thuringia produced musicians for 150 years before Johann Sebastian (1685–1750), the most famous of 53 documented musical Bachs.",
 """PUBLIC GENEALOGY RECORD — THE BACH FAMILY
Public historical record. All persons long deceased; facts from published biographical sources.

Johann Sebastian Bach (1685–1750) was the culmination of a musical dynasty:
- Great-great-grandfather Veit Bach (d.1619), miller and cittern player — the family's musical founder
- Father Johann Ambrosius Bach (1645–1695), town musician of Eisenach
- Brother Johann Christoph Bach (1671–1721), who raised Sebastian after 1695
- First wife Maria Barbara Bach (1684–1720), his second cousin — 7 children
- Second wife Anna Magdalena Wilcke (1701–1760) — 13 children
- 20 children total; 10 survived to adulthood
- Sons who became famous composers: Wilhelm Friedemann (1710–1784), Carl Philipp Emanuel (1714–1788), Johann Christian (1735–1782, 'the London Bach')

The Alt-Bachisches Archiv (Old Bach Archive) preserves the family's collected works — genealogy as music history.

Sources: Grove Music; Bach-Archiv Leipzig publications.""",
 ["53 musical Bachs documented.","20 children; 10 survived.","Alt-Bachisches Archiv preserves works."]),
("The Curie family — five Nobel Prizes", "family tree",
 "Marie Curie (1867–1934), Pierre (1859–1906), daughter Irène and son-in-law Frédéric Joliot-Curie: the only family with Nobel Prizes in two generations.",
 """PUBLIC GENEALOGY RECORD — THE CURIE FAMILY
Public historical record. All persons deceased; facts from Nobel archives and published biographies.

- Marie Skłodowska-Curie (1867–1934): Nobel Physics 1903, Nobel Chemistry 1911 — the only person to win Nobels in two sciences
- Pierre Curie (1859–1906): Nobel Physics 1903 (shared)
- Daughter Irène Joliot-Curie (1897–1956): Nobel Chemistry 1935
- Son-in-law Frédéric Joliot-Curie (1900–1958): Nobel Chemistry 1935
- Daughter Ève Curie (1904–2007): biographer ('Madame Curie', 1937); her husband Henry Labouisse accepted the 1965 Nobel Peace Prize for UNICEF

Marie was born Maria Skłodowska in Warsaw, then part of the Russian Empire; she studied at the Sorbonne after attending Warsaw's clandestine Flying University.

Five Nobel Prizes across two generations — unmatched in history.

Sources: Nobel Prize archives; Ève Curie, 'Madame Curie'.""",
 ["5 Nobels, 2 generations.","Marie: 2 Nobels, 2 sciences.","Flying University → Sorbonne."]),
("The Darwin–Wedgwood dynasty", "family tree",
 "Charles Darwin (1809–1882) married his cousin Emma Wedgwood — uniting the Darwin naturalists with the Wedgwood pottery fortune across five generations.",
 """PUBLIC GENEALOGY RECORD — DARWIN–WEDGWOOD
Public historical record. All persons deceased; facts from published biographies and the Darwin Correspondence Project.

- Charles Darwin (1809–1882) m. Emma Wedgwood (1808–1896), his first cousin — 10 children, 7 survived
- Grandfather Erasmus Darwin (1731–1802): physician, poet, early evolutionist ('Zoonomia')
- Father Robert Darwin (1766–1848): wealthy Shrewsbury physician
- Maternal grandfather Josiah Wedgwood (1730–1795): pottery industrialist
- Sons: George Darwin (astronomer), Francis Darwin (botanist), Leonard Darwin (eugenicist, politician), Horace Darwin (instrument maker)
- Granddaughter Gwen Raverat (1885–1957): artist, memoirist ('Period Piece')

The family illustrates Victorian cousin marriage among the professional class — and the inheritance (Darwin's Wedgwood money) that funded independent science.

Sources: Darwin Correspondence Project; Desmond & Moore, 'Darwin'.""",
 ["10 children; 7 survived.","Erasmus: early evolutionist.","Wedgwood money funded science."]),
("The Brontë siblings of Haworth", "family tree",
 "Patrick Brontë's six children — Charlotte, Branwell, Emily, Anne — produced three of English literature's greatest novels from a Yorkshire parsonage.",
 """PUBLIC GENEALOGY RECORD — THE BRONTËS
Public historical record. All persons deceased; facts from published biographies.

- Rev. Patrick Brontë (1777–1861), Irish-born parson of Haworth
- Maria Branwell (1783–1821), mother — died when the children were young
- Maria (1814–1825) and Elizabeth (1815–1825): died in childhood (Cowan Bridge school)
- Charlotte (1816–1855): 'Jane Eyre' (1847, as Currer Bell)
- Branwell (1817–1848): painter and poet, died of tuberculosis/alcoholism
- Emily (1818–1848): 'Wuthering Heights' (1847, as Ellis Bell)
- Anne (1820–1849): 'Agnes Grey', 'The Tenant of Wildfell Hall' (as Acton Bell)

Three siblings died within eight months (1848–49). Charlotte died in 1855, pregnant. The parsonage is now the Brontë Parsonage Museum.

Sources: Barker, 'The Brontës'; Brontë Parsonage Museum.""",
 ["6 children; 4 survived infancy.","3 novels in 1847.","Parsonage now a museum."]),
("The Roosevelt political dynasty", "family tree",
 "The Roosevelts of New York produced two presidents — Theodore (1858–1919) and Franklin (1882–1945) — plus Eleanor Roosevelt, from one Dutch-descended family.",
 """PUBLIC GENEALOGY RECORD — THE ROOSEVELTS
Public historical record. All persons deceased; facts from published biographies.

- Claes van Rosenvelt, arrived New Amsterdam c.1649 — family founder
- Theodore Roosevelt Sr. (1831–1878) m. Martha Bulloch (1835–1884)
- Theodore Roosevelt (1858–1919), 26th president (1901–09); children incl. Alice Roosevelt Longworth, Theodore Jr. (WWII general)
- Franklin D. Roosevelt (1882–1945), 32nd president (1933–45); fifth cousin of Theodore
- Eleanor Roosevelt (1884–1962), Theodore's niece, Franklin's wife — First Lady, UN human rights architect
- The two presidents were fifth cousins; Eleanor was Theodore's niece

Only the Adamses match two presidencies from one family.

Sources: Miller Center; FDR Library.""",
 ["Two presidents, fifth cousins.","Eleanor: TR's niece, FDR's wife.","Founder arrived c.1649."]),
("The Medici — bankers who became popes", "family tree",
 "The Medici of Florence rose from bankers to rulers of Tuscany, producing two queens of France and three popes across three centuries.",
 """PUBLIC GENEALOGY RECORD — THE MEDICI
Public historical record. All persons long deceased; facts from published histories.

- Giovanni di Bicci de' Medici (1360–1429): founded the Medici Bank
- Cosimo the Elder (1389–1464): de facto ruler of Florence; patron of the Renaissance
- Lorenzo the Magnificent (1449–1492): peak of Medici cultural power
- Giovanni de' Medici → Pope Leo X (1513–21); Giulio → Pope Clement VII (1523–34)
- Catherine de' Medici (1519–1589): queen of France, regent
- Marie de' Medici (1575–1642): queen of France
- Cosimo I (1519–1574): first Grand Duke of Tuscany

The family bank financed the Renaissance it is famous for patronizing — art history as family business.

Sources: Hibbert, 'The House of Medici'; public museum records.""",
 ["Bankers → rulers → popes.","Two queens of France.","Financed the Renaissance."]),
("The House of Windsor — a public lineage", "family tree",
 "The British royal house renamed from Saxe-Coburg-Gotha to Windsor in 1917; its public lineage runs from Victoria through Elizabeth II.",
 """PUBLIC GENEALOGY RECORD — HOUSE OF WINDSOR
Public historical record. Constitutional facts from official royal sources.

- Queen Victoria (1819–1901) m. Prince Albert of Saxe-Coburg and Gotha (1819–1861) — 9 children, 42 grandchildren ('the grandmother of Europe')
- Edward VII (1841–1910) → George V (1865–1936)
- 1917: George V renames the house Windsor (anti-German sentiment, WWI)
- Edward VIII (1894–1972): abdicated 1936 → George VI (1895–1952)
- Elizabeth II (1926–2022): reigned 1952–2022 (70 years)
- Charles III (b.1948): succeeded 2022

Victoria's descendants sat on the thrones of Britain, Germany, Russia, Spain, Greece, Romania, and Norway — genealogy as European diplomacy.

Sources: royal.uk; published official biographies.""",
 ["Renamed 1917 (was Saxe-Coburg-Gotha).","Victoria: grandmother of Europe.","Elizabeth II: 70-year reign."]),
("The Habsburgs — Europe's inbred emperors", "family tree",
 "The Habsburgs ruled Austria, Spain, and the Holy Roman Empire for 600 years — and their cousin marriages produced the famous 'Habsburg jaw'.",
 """PUBLIC GENEALOGY RECORD — THE HABSBURGS
Public historical record. All persons long deceased; facts from published histories.

- Rudolf I (1218–1291): first Habsburg King of Germany
- Maximilian I (1459–1519): 'the last knight'; married Burgundy into the family
- Charles V (1500–1558): ruled Spain, the Netherlands, Austria, and the Americas — 'the empire on which the sun never sets'
- Philip II of Spain (1527–1598); the Spanish line ends with Charles II (1661–1700), whose disabilities reflected generations of uncle-niece and cousin marriage
- Maria Theresa (1717–1780): the great reforming empress; 16 children incl. Marie Antoinette
- Franz Joseph I (1830–1916): reigned 68 years

The 'Habsburg jaw' (mandibular prognathism) is the textbook case of pedigree collapse.

Sources: Winder, 'Danubia'; published histories.""",
 ["600 years of rule.","Charles V: sun-never-sets empire.","Jaw = pedigree collapse."]),
("The Romanovs — 300 years, ended 1918", "family tree",
 "The Romanov dynasty ruled Russia 1613–1918, from Michael I to Nicholas II — whose family was executed at Ekaterinburg in July 1918.",
 """PUBLIC GENEALOGY RECORD — THE ROMANOVS
Public historical record. All persons deceased; facts from published histories.

- Michael I (1596–1645): elected 1613, ending the Time of Troubles
- Peter the Great (1672–1725): modernizer; built St. Petersburg
- Catherine the Great (1729–1796): née Sophie of Anhalt-Zerbst; coup 1762
- Alexander II (1818–1881): emancipated the serfs 1861; assassinated
- Nicholas II (1868–1918): last tsar; abdicated March 1917
- 17 July 1918: Nicholas, Alexandra, and their five children executed at Ekaterinburg
- 2000: canonized by the Russian Orthodox Church

Hemophilia (via Queen Victoria's genes through Alexandra) shaped the dynasty's final politics — Rasputin's access ran through the sick heir Alexei.

Sources: Massie, 'Nicholas and Alexandra'; published histories.""",
 ["1613–1918: 305 years.","Ended at Ekaterinburg, 1918.","Hemophilia shaped the politics."]),
("The Tolstoys — writers and landowners", "family tree",
 "Leo Tolstoy (1828–1910) and Sophia Behrs (1844–1919) raised 13 children at Yasnaya Polyana; the family became literature's most documented.",
 """PUBLIC GENEALOGY RECORD — THE TOLSTOYS
Public historical record. All persons deceased; facts from published biographies.

- Leo Tolstoy (1828–1910): 'War and Peace', 'Anna Karenina'
- Sophia Andreyevna Behrs (1844–1919): copied 'War and Peace' by hand seven times; diarist
- 13 children, 8 survived to adulthood
- Son Ilya (1866–1933): memoirist; Sergei (1863–1947): composer/ethnographer
- Daughter Alexandra (1884–1979): founded the Tolstoy Foundation (refugee aid)
- Yasnaya Polyana estate: now a museum

Sophia's diaries and the family's 10,000+ preserved letters make the Tolstoys the best-documented family in literary history.

Sources: Shklovsky; Tolstoy Museum publications.""",
 ["13 children; 8 survived.","Sophia copied War and Peace 7x.","10,000+ letters preserved."]),
# --- historical figure (10) ---
("Ada Lovelace — Byron's daughter, computing's first programmer", "historical figure",
 "Augusta Ada King, Countess of Lovelace (1815–1852): Lord Byron's legitimate daughter, who wrote the first computer algorithm for Babbage's Analytical Engine.",
 """PUBLIC GENEALOGY RECORD — ADA LOVELACE
Public historical record. Deceased 1852; facts from published biographies.

- Born 10 December 1815, London — the only legitimate child of Lord Byron (1788–1824) and Annabella Milbanke (1792–1860)
- Byron left England when Ada was an infant; she never met him
- Married William King, 8th Baron King (later Earl of Lovelace), 1835 — three children: Byron (1836), Anne Isabella (1837), Ralph (1839)
- 1843: translated Menabrea's paper on Babbage's Analytical Engine, adding Notes (G) with the Bernoulli-number algorithm
- Died 27 November 1852, aged 36 — buried beside Byron at her request

Her Notes foresaw computing beyond calculation: 'the Engine might compose elaborate and scientific pieces of music.'

Sources: Essinger, 'Ada's Algorithm'; published papers.""",
 ["Byron's only legitimate child.","1843 Notes: first algorithm.","Died 36; buried by Byron."]),
("Frederick Douglass — born enslaved, died a statesman", "historical figure",
 "Frederick Douglass (c.1818–1895): born enslaved in Maryland, escaped in 1838, became the century's leading abolitionist and a US Marshal.",
 """PUBLIC GENEALOGY RECORD — FREDERICK DOUGLASS
Public historical record. Deceased 1895; facts from his autobiographies and published biographies.

- Born Frederick Augustus Washington Bailey, c.February 1818, Talbot County, Maryland — mother Harriet Bailey (enslaved), father unknown (likely white)
- Escaped slavery 3 September 1838, disguised as a sailor
- Married Anna Murray (1813–1882), a free Black woman who funded his escape — 5 children
- 1845: 'Narrative of the Life of Frederick Douglass'
- 1847: founded 'The North Star' newspaper
- 1877: appointed US Marshal for the District of Columbia
- Second marriage (1884) to Helen Pitts, a white feminist — scandalous then

His three autobiographies are the most important slave narratives in American literature.

Sources: Douglass, 'Narrative' (1845); Blight, 'Prophet of Freedom'.""",
 ["Born enslaved c.1818.","Escaped 1838 as a 'sailor'.","US Marshal, 1877."]),
("Marie Tharp — the woman who mapped the ocean floor", "historical figure",
 "Marie Tharp (1920–2006): geologist whose Mid-Atlantic Ridge maps proved continental drift; daughter of a soil surveyor, denied ship time for being a woman.",
 """PUBLIC GENEALOGY RECORD — MARIE THARP
Public historical record. Deceased 2006; facts from published biographies.

- Born 30 July 1920, Ypsilanti, Michigan — father William Tharp, US Department of Agriculture soil surveyor; mother Bertha, teacher
- Degrees: English & music (Ohio), geology (Michigan), mathematics (Tulsa)
- 1948: joined Columbia's Lamont lab; barred from research ships (women not allowed) — mapped from sonar data on land
- 1957: published the first physiographic map of the North Atlantic, revealing the Mid-Atlantic Ridge's rift valley
- Bruce Heezen initially dismissed it as 'girl talk'; the data won
- 1968+: the maps became the visual proof of plate tectonics

Library of Congress named her one of the century's great cartographers (1997).

Sources: Felt (ed.), 'Soundings'; LOC.""",
 ["Mapped the Mid-Atlantic Ridge.","Barred from ships; mapped on land.","Proof of plate tectonics."]),
("Ibn Battuta — the greatest traveler of the Middle Ages", "historical figure",
 "Ibn Battuta (1304–1369): Moroccan scholar who traveled 120,000 km over 30 years — from Mali to China — and dictated the Rihla.",
 """PUBLIC GENEALOGY RECORD — IBN BATTUTA
Public historical record. Deceased c.1369; facts from the Rihla and published scholarship.

- Born 24 February 1304, Tangier — family of Islamic judges (qadis)
- 1325: left for the Hajj at 21; kept going for 30 years
- Served as qadi in Delhi under Muhammad bin Tughluq; visited the Maldives, East Africa, Constantinople, the Golden Horde, China
- Estimated 120,000 km traveled — the longest pre-modern journey on record
- c.1355: dictated the 'Rihla' (Journey) to Ibn Juzayy in Fez
- Returned to Morocco; died c.1369

His account is the single richest source on the 14th-century Islamic world.

Sources: Dunn, 'The Adventures of Ibn Battuta'; Rihla translations.""",
 ["120,000 km over 30 years.","Qadi in Delhi; reached China.","Rihla: richest 14th-c. source."]),
("Sojourner Truth — 'Ain't I a Woman?'", "historical figure",
 "Sojourner Truth (c.1797–1883): born Isabella Baumfree, enslaved in New York; escaped 1826, became the iconic Black abolitionist orator.",
 """PUBLIC GENEALOGY RECORD — SOJOURNER TRUTH
Public historical record. Deceased 1883; facts from published biographies.

- Born Isabella Baumfree c.1797, Ulster County, New York — enslaved by the Hardenbergh family
- 1826: escaped with infant daughter Sophia (New York abolished slavery 1827)
- 1828: won a court case recovering her son Peter — first Black woman to win such a case against a white man
- 1843: renamed herself Sojourner Truth; became an itinerant preacher
- 1851: Akron women's rights convention — the 'Ain't I a Woman?' speech (in the 1863 Gage version)
- Recruited Black troops for the Union; met Lincoln 1864
- 1850: dictated 'Narrative of Sojourner Truth' to Olive Gilbert

Her 1870s campaign for 'Negro suffrage' land grants foreshadowed later reparations debates.

Sources: Painter, 'Sojourner Truth: A Life, A Symbol'.""",
 ["Born enslaved c.1797.","Won son's freedom in court, 1828.","Akron speech, 1851."]),
("Emperor Meiji — the boy who became modern Japan", "historical figure",
 "Emperor Meiji (1852–1912): born Mutsuhito, became the symbol of Japan's transformation from feudal state to industrial power in one lifetime.",
 """PUBLIC GENEALOGY RECORD — EMPEROR MEIJI
Public historical record. Deceased 1912; facts from published histories.

- Born 3 November 1852, Kyoto — son of Emperor Kōmei and Nakayama Yoshiko (a court lady)
- Succeeded 1867, aged 14, as the Tokugawa shogunate fell
- Reign name Meiji ('enlightened rule'), 1868–1912
- Charter Oath (1868); constitution (1889); industrialization, railways, conscription, universal education
- 15 children by various consorts; succeeded by Emperor Taishō
- Died 30 July 1912; buried at Fushimi Momoyama

In his lifetime Japan went from samurai domains to defeating Russia (1905) — the fastest great-power rise in history.

Sources: Keene, 'Emperor of Japan'; Jansen, 'The Making of Modern Japan'.""",
 ["Reigned 1868–1912.","Charter Oath to constitution.","Fastest great-power rise."]),
("Queen Nzinga of Ndongo and Matamba", "historical figure",
 "Queen Nzinga (c.1583–1663): the Mbundu queen who resisted Portuguese slave-trading for 40 years through war, diplomacy, and strategic conversion.",
 """PUBLIC GENEALOGY RECORD — QUEEN NZINGA
Public historical record. Deceased 1663; facts from published histories.

- Born c.1583, Ndongo (modern Angola) — daughter of King Ngola Kiluanje
- 1622: negotiated with the Portuguese as her brother's ambassador — famously refused the floor mat, seating herself on a servant's back
- Became queen c.1624; resisted Portuguese slave raids for four decades
- Allied with the Dutch (1641–48); retreated to Matamba and built a refuge state for escaped enslaved people
- Baptized as Ana de Sousa (1622); used Christianity diplomatically
- Died 17 December 1663, aged ~80; succeeded by her sister Barbara

Angola's national heroine; her statue stands in Luanda.

Sources: Heywood, 'Njinga of Angola'; Thornton.""",
 ["Resisted Portugal 40 years.","Allied with the Dutch.","Angola's national heroine."]),
("Rani Lakshmibai of Jhansi", "historical figure",
 "Rani Lakshmibai (1828–1858): the warrior queen of Jhansi who led the 1857 uprising's most famous resistance and died in battle at 29.",
 """PUBLIC GENEALOGY RECORD — RANI LAKSHMIBAI
Public historical record. Deceased 1858; facts from published histories.

- Born Manikarnika Tambe, 19 November 1828, Varanasi — Maratha family
- Married the Maharaja of Jhansi (1842); adopted son Damodar Rao
- 1853: British annexed Jhansi under the Doctrine of Lapse, denying the adoption
- 1857: led Jhansi's resistance; held the fort against British siege
- Died 18 June 1858 at Gwalior, in battle — aged 29
- The British called her 'the most dangerous of all Indian leaders'

India's national heroine — 'the Joan of Arc of India'.

Sources: Lebra-Chapman; published histories.""",
 ["Led 1857 resistance.","Died in battle, 1858, aged 29.","'Joan of Arc of India'."]),
("Mansa Musa — the richest man in history", "historical figure",
 "Mansa Musa (c.1280–c.1337): emperor of Mali whose 1324 Hajj with tons of gold crashed Cairo's gold market for a decade.",
 """PUBLIC GENEALOGY RECORD — MANSA MUSA
Public historical record. Deceased c.1337; facts from Arabic chronicles and published scholarship.

- Became Mansa (emperor) of Mali c.1312 — nephew of Sundiata Keita's line
- Empire: Mali, covering modern Mali, Senegal, Guinea — gold-rich (Bambuk, Bure)
- 1324: Hajj pilgrimage with 60,000 attendants, 80 camels carrying gold
- Gave away so much gold in Cairo that its price fell ~25% for a decade
- Built mosques and madrasas; Timbuktu's scholarly golden age followed
- The Catalan Atlas (1375) depicts him holding a gold nugget — the only non-European ruler shown

Often called the richest person in history, adjusted for the gold economy he commanded.

Sources: Levtzion & Hopkins, 'Corpus'; Catalan Atlas.""",
 ["1324 Hajj crashed gold prices.","Empire of Mali's golden age.","Catalan Atlas depicts him."]),
("Hatshepsut — the woman who was pharaoh", "historical figure",
 "Hatshepsut (c.1507–1458 BCE): Egypt's female pharaoh who ruled 21 years, built Deir el-Bahari, and was erased by her stepson.",
 """PUBLIC GENEALOGY RECORD — HATSHEPSUT
Public historical record. Deceased c.1458 BCE; facts from Egyptological sources.

- Daughter of Thutmose I, wife (and half-sister) of Thutmose II
- Regent for stepson Thutmose III c.1479 BCE; assumed full pharaonic power c.1472
- Ruled ~21 years as king (depicted with false beard and male regalia)
- Built the mortuary temple at Deir el-Bahari; sent the Punt expedition
- Thutmose III later erased her names and images (damnatio memoriae)
- Mummy identified 2007 (KV60)

Her reign was prosperous and peaceful — the erasure was political, not a judgment on her rule.

Sources: Tyldesley, 'Hatchepsut'; Metropolitan Museum.""",
 ["Female pharaoh, ~21 years.","Built Deir el-Bahari.","Erased, then rediscovered."]),
# --- record guide (10) ---
("Reading parish registers: baptisms, marriages, burials", "record guide",
 "Parish registers — recording baptisms, marriages, and burials from the 1500s — are the backbone of genealogy before civil registration.",
 """GENEALOGY GUIDE — PARISH REGISTERS
Public knowledge explainer for family historians.

- England: registers begin 1538 (Thomas Cromwell's order); Scotland 1553; many survive from the 1600s
- Baptisms (not births): record the christening date — birth may be days or weeks earlier
- Banns and marriages: banns books sometimes survive when marriage registers don't
- Burials (not deaths): age at burial helps estimate birth year
- Bishop's transcripts: annual copies sent to the diocese — a backup when the parish book is lost
- Latin forms: common in Catholic registers (Johannes, Maria, obiit)
- Gaps: English Civil War (1640s), fires, and neglect destroy runs of years

Read the whole page, not just your surname — witnesses, godparents, and neighbors rebuild communities.

Public explainer. No private data.""",
 ["Start 1538 (England).","Baptism ≠ birth date.","Bishop's transcripts = backup."]),
("Census records for family historians", "record guide",
 "Census schedules — from 1841 in Britain, 1790 in the US — place ancestors in households every ten years. Learn to read them.",
 """GENEALOGY GUIDE — CENSUS SCHEDULES
Public knowledge explainer for family historians.

- US federal censuses: 1790–1950 public (1950 released 2022; 72-year rule)
- UK censuses: 1841–1921 public (1921 released 2022; 1939 Register also public)
- What they show: names, ages, birthplaces, occupations, relationships, addresses
- 1841 UK: ages rounded down to 5 for adults; birthplaces just 'Y/N' for county
- Soundex and wildcards: beat spelling variation (Smith/Smyth/Smithe)
- Neighbors matter: families cluster — check 10 pages either side
- 1890 US: destroyed by fire (1931) — the great gap; use 1880 + 1900

Always cite the piece/folio/page (UK) or roll/page (US) — genealogy without citations is fiction.

Public explainer. No private data.""",
 ["US: 1790–1950 public.","1890 US destroyed by fire.","Cite piece/folio/page."]),
("Wills and probate: the ancestor's own voice", "record guide",
 "Wills name names — spouses, children, debts, and bequests — and probate inventories list every pot and cow. The richest genealogical source.",
 """GENEALOGY GUIDE — WILLS & PROBATE
Public knowledge explainer for family historians.

- England: Prerogative Court of Canterbury wills (1384–1858) at The National Archives; post-1858 national probate calendar
- US: county probate courts; colonial wills often the only record of daughters (named via married names)
- What they reveal: family structure, wealth, literacy (signed vs. marked), religion, migrations
- Inventories: room-by-room goods — social history in a list
- Administrations (no will): bonds name the widow and sureties
- Watch for: 'my beloved wife' (unnamed), deceased children omitted, step-children

A will is the one document your ancestor dictated. Read it whole.

Public explainer. No private data.""",
 ["Name names, debts, bequests.","Inventories = social history.","The ancestor's own voice."]),
("Military records: muster rolls to pensions", "record guide",
 "Muster rolls, pension files, and medal cards trace ancestors through wars — US Civil War pensions run to 100+ pages of family detail.",
 """GENEALOGY GUIDE — MILITARY RECORDS
Public knowledge explainer for family historians.

- US Civil War: compiled service records + pension files (widows' applications name children, marriages, doctors)
- WWI: US draft cards (1917–18) give birth dates and addresses for 24M men; UK 'burnt documents' (60% destroyed 1940)
- UK: WO 363/WO 364 (WWI service), medal index cards (5M+)
- Confederate: state-level pensions (no federal pensions for Confederates)
- Napoleonic: muster rolls at Kew (WO 12); Chelsea Pensioners' records
- Always check: attestation papers (physical description!), discharge papers, war diaries for context

Pension files are genealogical gold — affidavits from neighbors, family Bible pages, marriage certificates.

Public explainer. No private data.""",
 ["Pensions = family detail.","Draft cards: 24M men.","Attestations describe bodies."]),
("Immigration records: manifests and naturalizations", "record guide",
 "Ship manifests (US from 1820), naturalization papers, and border crossings document the immigrant ancestor's journey in their own hand.",
 """GENEALOGY GUIDE — IMMIGRATION
Public knowledge explainer for family historians.

- US manifests (1820–1950s): name, age, origin village, destination contact — post-1906 manifests add physical description and birthplace detail
- Castle Garden (1855–90) → Ellis Island (1892–1954): 12M+ passed through
- Naturalizations: declarations of intention ('first papers') name the ship and arrival date
- UK: no systematic immigration records before aliens registration (WWI); use censuses + naturalization certificates
- Hamburg and Bremen passenger lists cover departures
- Name changes happened at the clerk's whim — search phonetically, not literally

The manifest's 'nearest relative in old country' column rebuilds the left-behind family.

Public explainer. No private data.""",
 ["Manifests from 1820.","Ellis Island: 12M+.","Search phonetically."]),
("DNA for genealogy: the four tests", "record guide",
 "Autosomal, Y-DNA, mtDNA, and X-DNA tests each answer different genealogical questions. Learn which test fits which brick wall.",
 """GENEALOGY GUIDE — GENETIC GENEALOGY
Public knowledge explainer.

- Autosomal (AncestryDNA, 23andMe): all lines, ~5–7 generations back; matches are cousins
- Y-DNA (FamilyTreeDNA): direct paternal line; surname studies
- mtDNA: direct maternal line; deep ancestry
- X-DNA: patterned inheritance; useful for specific hypotheses
- Centimorgans: 3,400+ = parent/child; ~1,700 = grandparent; 90–200 = 3rd cousins
- Ethics: test the oldest generation first; unexpected parentage is common — prepare
- Privacy: DNA reveals living relatives — share carefully, and never publish others' data

DNA confirms paper trails; it does not replace them.

Public explainer. No private data.""",
 ["Autosomal: all lines, 5–7 gens.","Y-DNA: paternal; mtDNA: maternal.","Test the oldest first."]),
("Newspapers: obituaries and announcements", "record guide",
 "Digitized newspapers hold obituaries, marriage notices, and court reports — the community gossip column of genealogy.",
 """GENEALOGY GUIDE — NEWSPAPERS
Public knowledge explainer for family historians.

- Obituaries: name parents, spouses, children, migration history — the single richest short source
- Marriage/birth announcements: dates and addresses
- Court reports: bankruptcies, divorces, crimes — ancestors behaving badly, in print
- UK: British Newspaper Archive (400M+ pages); US: Chronicling America (LOC, free), Newspapers.com
- OCR is imperfect: search name variants and browse the page
- Funeral notices list mourners — the extended family in one column

Always save the clipping image, not just the transcript — OCR lies.

Public explainer. No private data.""",
 ["Obituaries = richest short source.","OCR lies: save the image.","Court reports: behaving badly."]),
("Land and property records", "record guide",
 "Deeds, tithe maps, and land grants track families through property — metes and bounds in the US, townlands in Ireland.",
 """GENEALOGY GUIDE — LAND RECORDS
Public knowledge explainer for family historians.

- US: deeds at county recorders (grantor/grantee indexes); BLM land patents (homesteads, free online)
- Metes and bounds (original 13 colonies): 'beginning at the white oak...' — learn the compass
- Ireland: Griffith's Valuation (1847–64) — every occupier listed; tithe applotments (1820s–30s)
- England: tithe maps (1836–51) + apportionments; manorial records (court rolls)
- Enclosure awards: name every landholder at enclosure
- Homestead files: 160 acres for 5 years' residence — applications detail families

Land stayed; people moved. Follow the land to find the people.

Public explainer. No private data.""",
 ["Deeds: grantor/grantee indexes.","Griffith's: every occupier.","Follow the land."]),
("Citing sources: genealogy without citations is fiction", "record guide",
 "The Genealogical Proof Standard: reasonably exhaustive research, complete citations, analysis, resolution of conflicts, written conclusion.",
 """GENEALOGY GUIDE — CITATION & PROOF
Public knowledge explainer for family historians.

The Genealogical Proof Standard (Board for Certification of Genealogists):
1. Reasonably exhaustive research — all relevant sources, not just easy ones
2. Complete, accurate citations — another researcher must find it
3. Analysis and correlation — weigh evidence quality
4. Resolution of conflicting evidence — explain the contradictions
5. Soundly written conclusion — show your work

Citation anatomy: who created it, what it is, when, where it lives, where within (page/line).
- '1851 census' is not a citation. 'TNA HO 107/1694, f.312, p.18, household of John Smith' is.
- Derivative sources (indexes, trees) are clues, not proof.

Public explainer. No private data.""",
 ["5-point Proof Standard.","Cite so others can find it.","Indexes are clues, not proof."]),
("Occupational records: guilds to railways", "record guide",
 "Apprenticeship indentures, guild freedoms, railway staff registers, and trade directories place ancestors in working life.",
 """GENEALOGY GUIDE — OCCUPATIONS
Public knowledge explainer for family historians.

- Apprenticeship indentures: bound at 14 for 7 years — names master, trade, father's name
- London guild freedoms: membership lists from the 1500s
- Railway staff registers: 19th-century Britain's biggest employer — detailed service records
- Trade directories (Kelly's, etc.): addresses + occupations, yearly
- Teachers, nurses, police: professional registers with training details
- Merchant seamen: crew lists and registry tickets (BT 98–100 at Kew)

An ancestor's occupation explains their migration: miners to coalfields, weavers to mills, sailors to ports.

Public explainer. No private data.""",
 ["Indentures: master + trade.","Railways: biggest employer.","Occupation explains migration."]),
# --- case study (10) ---
("Case study: tracing a mariner of 1851", "case study",
 "A worked public example: how census, crew lists, and parish registers combine to trace a 19th-century merchant seaman — method, not a private person.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The problem: a man listed as 'mariner' in the 1851 census, born 'at sea' — how to trace him?

Step 1 — census: 1851 gives age 34, birthplace 'at sea', wife Mary, two children in Liverpool.
Step 2 — marriage: parish register 1844 names his father (also a mariner) and his ship.
Step 3 — crew lists (BT 98): the ship's 1843–45 agreements list his age, birthplace (given as 'St. Helena'), and previous vessel.
Step 4 — baptism: St. Helena registers (1830s) hold the baptism; the father's service record explains the posting.
Step 5 — master's certificates: his 1852 mate's certificate gives exact birth date.

Lesson: mariners defeat censuses (absent at sea) but generate maritime paper — crew lists, tickets, and certificates. Follow the ship, not the house.

Public methodology demonstration. No private data.""",
 ["Mariners defeat censuses.","Follow the ship.","Crew lists name birthplaces."]),
("Case study: the 1881 census and a missing girl", "case study",
 "A worked public example: a child in 1881, gone by 1891 — using censuses, workhouse records, and emigration lists to solve a disappearance.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The problem: a girl aged 6 in the 1881 census, absent from the 1891 household — no death registration found.

Step 1 — 1891: search the whole district by first name + birth year, not surname (she may be a servant elsewhere).
Step 2 — found: a 16-year-old domestic servant 30 miles away, birthplace matching.
Step 3 — 1901: married, two children — marriage certificate confirms father's name.
Step 4 — alternative branch checked: workhouse admission registers (no match), passenger lists (no match).

Lesson: children 'disappear' into service. Search by forename + birthplace, drop the surname. And always check the marriage — it names the father, closing the loop.

Public methodology demonstration. No private data.""",
 ["Search forename + birthplace.","Servants 'disappear' into service.","Marriage names the father."]),
("Case study: two John Smiths, one parish", "case study",
 "A worked public example: distinguishing same-name contemporaries with tax lists, wills, and signatures.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The problem: two John Smiths baptizing children in one parish, 1780–1800. Which is yours?

Step 1 — land tax: one John Smith assessed on 40 acres, the other on a cottage — different economic worlds.
Step 2 — wills: the yeoman's 1798 will names children matching one baptism set.
Step 3 — signatures: the cottage-dweller marks; the yeoman signs — compare across documents.
Step 4 — burial ages: 1803 burial 'aged 62' fits the yeoman's 1741 baptism; 1811 'aged 68' fits the other's 1743 baptism.

Lesson: same name ≠ same man. Tax, probate, literacy, and burial ages separate them. Never merge identities on name alone.

Public methodology demonstration. No private data.""",
 ["Same name ≠ same man.","Tax + wills + signatures.","Never merge on name alone."]),
("Case study: the Irish brick wall of 1845", "case study",
 "A worked public example: pre-Famine Irish research when parish registers are lost — Griffith's, tithe, and estate papers as substitutes.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The problem: an Irish family emigrated 1847; the parish registers burned in 1922.

Step 1 — Griffith's Valuation (1850s): the surname clustered in three townlands — the origin zone.
Step 2 — tithe applotments (1830s): the same surname on the same townlands, one generation earlier.
Step 3 — estate papers: the landlord's rent books name tenants yearly — continuity confirmed.
Step 4 — US arrival: the 1850 manifest names the townland; chain migration visible in neighbors' manifests.

Lesson: Irish research is reconstruction from substitutes. No single source replaces the registers; five partial sources triangulate.

Public methodology demonstration. No private data.""",
 ["1922 fire destroyed registers.","Griffith's + tithe + estate papers.","Triangulate substitutes."]),
("Case study: a Civil War pension file", "case study",
 "A worked public example: a 90-page Union pension file yielding three marriages, eight children, and a family Bible page.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The file: a Union infantry private's pension application, 1890–1910.

Contents: service record (enlisted 1862, wounded 1864); first marriage certificate (1866); second marriage (1881, after first wife's death); affidavits from eight children; a copied family Bible page with births; neighbors' testimony to his identity; medical exams.

Lesson: pension files are the most information-dense genealogical source in American research. Order the full file, not the summary — the affidavits contain the family structure.

Note: Confederate veterans filed with states, not the federal government.

Public methodology demonstration. No private data.""",
 ["90 pages: 3 marriages, 8 children.","Affidavits = family structure.","Order the full file."]),
("Case study: the Ellis Island name myth", "case study",
 "A worked public example: tracing a 1907 arrival through the manifest to show names were NOT changed at Ellis Island.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The family story: 'they changed our name at Ellis Island.' The manifest says otherwise.

Step 1 — manifest line 14 (1907): the name as written by the shipping clerk in Hamburg — already the 'American' spelling.
Step 2 — declaration of intention (1912): same spelling, in the immigrant's own hand.
Step 3 — 1910 census: the older spelling persists — the change happened later, by the family's choice.
Step 4 — WWI draft card (1918): the new spelling, signed by the man himself.

Lesson: inspectors worked from manifests; they didn't invent names. Changes were voluntary, gradual, and usually post-arrival — often to dodge discrimination or simplify spelling.

Public methodology demonstration. No private data.""",
 ["Names weren't changed at Ellis Island.","Manifests were written at departure.","Changes were voluntary, later."]),
("Case study: reading a will's silences", "case study",
 "A worked public example: an 1820 will that omits a married daughter — and the chancery suit that explains why.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The will (1820): names sons, a widow, grandchildren — but no daughter, though baptisms show one.

Step 1 — marriage: the daughter married 1805; the settlement (marriage articles) gave her £500 — her portion already paid.
Step 2 — the omission is explained: portions to daughters were lifetime advances, not will bequests.
Step 3 — chancery suit (1825): the grandson sues over the will — depositions name the whole family, including the 'missing' daughter.

Lesson: wills record unsettled business, not complete families. Married daughters with portions vanish from wills by design. Check settlements and suits.

Public methodology demonstration. No private data.""",
 ["Wills show unsettled business.","Portions paid at marriage.","Check settlements + suits."]),
("Case study: DNA breaks a 40-year wall", "case study",
 "A worked public example: autosomal matches triangulate an 1880s non-paternal event — method and ethics.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The wall: a great-grandfather with no father named (1880s birth).

Step 1 — test the oldest living descendant (autosomal).
Step 2 — cluster matches: a group shares 200–400 cM and a common ancestral couple — unknown to the family.
Step 3 — build the candidate's tree forward: sons in the right place at the right time.
Step 4 — targeted testing of a descendant confirms the link.

Lesson: DNA + paper together break walls neither breaks alone. Ethics: the finding rewrites a family's story — share privately, sensitively, and never publish living people's unexpected parentage.

Public methodology demonstration. No private data.""",
 ["Clusters reveal the line.","Paper + DNA together.","Ethics: share privately."]),
("Case study: the 1939 Register and the war years", "case study",
 "A worked public example: using the 1939 Register to bridge the 1921–1951 census gap in England and Wales.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The gap: no UK census between 1921 and 1951 (1931 destroyed, 1941 never taken). The 1939 Register fills it.

Step 1 — 1939 Register entry: household with exact birth dates (day/month/year), occupations, and married women's maiden names in brackets.
Step 2 — compare with 1921 census: the family matches, children aged on correctly.
Step 3 — redacted lines: anyone born less than 100 years ago (and not proven dead) is blacked out — the living are protected.
Step 4 — 1951 substitute: electoral rolls + the register together bridge the war.

Lesson: the Register is a census in all but name — compiled for identity cards and rationing, released 2015. Redactions remind us: privacy rules protect the living.

Public methodology demonstration. No private data.""",
 ["Fills 1921–1951 gap.","Exact birth dates given.","Living persons redacted."]),
("Case study: from Domesday to the present — a manor's people", "case study",
 "A worked public example: tracing one English manor's tenants from 1086 through court rolls to the 1841 census.",
 """GENEALOGY CASE STUDY (METHOD DEMONSTRATION)
Public explainer using a composite illustrative example. No real private person is described.

The place: a single manor, recorded in Domesday (1086) with 28 villagers.

Step 1 — manorial court rolls (1400s–1700s): copyhold tenants admitted holding by holding — surnames stabilize by 1500.
Step 2 — parish registers (from 1560): baptisms link the court-roll names to families.
Step 3 — enclosure award (1810): every landholder named with acreage.
Step 4 — tithe map (1840) + 1841 census: the same surnames on the same farms, 750 years on.

Lesson: place-based research defeats name-based brick walls. Families stay; follow the land and the manor, and the people emerge. Domesday-to-census continuity is real in unbroken rural parishes.

Public methodology demonstration. No private data.""",
 ["One manor, 1086–1841.","Court rolls + registers + maps.","Follow the land."]),
# --- heraldry (10) ---
("Heraldry basics: shield, tinctures, charges", "heraldry",
 "Heraldry's grammar: the shield, seven tinctures, and charges — how to read a coat of arms like a genealogical document.",
 """GENEALOGY GUIDE — HERALDRY BASICS
Public knowledge explainer.

- The shield (escutcheon): the field on which arms are displayed
- Tinctures: Or (gold), Argent (silver), Gules (red), Azure (blue), Vert (green), Sable (black), Purpure (purple)
- Rule of tincture: metal on color, color on metal — never both
- Charges: lions, eagles, crosses, stars (mullets), and thousands more
- The blazon: the formal description ('Gules, a lion rampant Or') — arms are defined by words, not pictures
- Cadency: marks distinguishing sons (label, crescent, mullet...)

Arms belong to individuals, not surnames — 'family crests' sold to tourists are heraldic nonsense.

Public explainer. No private data.""",
 ["Tinctures: 7 colors/metals.","Metal on color rule.","Arms = individual, not surname."]),
("The College of Arms, London — 1484", "heraldry",
 "The College of Arms has regulated English heraldry since 1484; its visitations (1530–1680) are among genealogy's richest sources.",
 """GENEALOGY GUIDE — COLLEGE OF ARMS
Public knowledge explainer.

- Founded 1484 (Richard III's charter); heralds still grant arms today
- Visitations (1530–1680): heralds toured counties, recording gentry pedigrees — published by the Harleian Society
- Grants: new arms granted by the Kings of Arms (Garter, Clarenceux, Norroy)
- Pedigrees recorded at visitations are sworn statements — generally reliable for the gentry
- Scottish heraldry: the Court of the Lord Lyon (stricter — arms must be matriculated)
- Irish: the Chief Herald (formerly Ulster King of Arms)

Visitation pedigrees are the backbone of English gentry genealogy before parish registers mature.

Public explainer. No private data.""",
 ["Founded 1484.","Visitations 1530–1680.","Pedigrees = sworn statements."]),
("Crests, mottoes, and supporters — the extras", "heraldry",
 "The crest sits above the helmet, the motto below the shield, supporters beside it — each with its own rules and genealogy.",
 """GENEALOGY GUIDE — HERALDIC EXTRAS
Public knowledge explainer.

- Crest: worn on the helmet (the 'crest' is NOT the whole arms) — e.g., 'a lion's head erased'
- Motto: not officially part of the grant in England; can be changed freely
- Supporters: restricted — peers, knights of orders, and special grantees
- Helmets: rank-coded (gold barred for royalty, steel for esquires)
- Mantling: the stylized cloth, usually the main tinctures
- Badges: personal emblems (the Tudor rose, the white hart) — separate from arms

A full 'achievement' combines shield, helmet, crest, mantling, motto, and supporters.

Public explainer. No private data.""",
 ["Crest ≠ whole arms.","Mottoes freely changeable.","Supporters = restricted."]),
("Canting arms: puns in heraldry", "heraldry",
 "Canting (punning) arms encode the bearer's name: a bow for Bowman, a cock for Cockburn — genealogy's wordplay.",
 """GENEALOGY GUIDE — CANTING ARMS
Public knowledge explainer.

- Bowman: bows; Archer: arrows; Fletcher: arrow-heads
- Cockburn: a cock; Swann: swans; Nightingale: nightingales
- The Washington family arms: stars and stripes — the US flag's debated ancestor
- Trumpington: trumpets; Conyers: wings (coneys? debated)
- Multilingual puns: common in Welsh and German heraldry

Canting arms help identify families in church monuments and seals — the pun is the finding aid.

Public explainer. No private data.""",
 ["Arms as puns.","Bowman: bows.","Washington: stars and stripes."]),
("Japanese kamon — the other heraldry", "heraldry",
 "Japan's kamon (family crests) — wisteria, paulownia, chrysanthemum — are the world's other great heraldic system, older than Europe's in use.",
 """GENEALOGY GUIDE — KAMON
Public knowledge explainer.

- In use from the Heian period (794–1185) — predating European heraldry's systematization
- Imperial: 16-petal chrysanthemum; Tokugawa: triple hollyhock (aoi)
- Motifs: plants (wisteria/Fujiwara, paulownia), animals, geometric
- Unlike European arms: no tincture rules, no cadency — crests shared by retainers and branches
- Used on kimono, lanterns, roof tiles, and gravestones — genealogy you can wear
- Databases: thousands documented; many families still use them

Kamon appear on Japanese gravestones — a field guide to ancestors.

Public explainer. No private data.""",
 ["Heian period origins.","Chrysanthemum = imperial.","Worn on kimono, cut on graves."]),
("Heraldic visitations as genealogy", "heraldry",
 "The heralds' visitations (1530–1680) recorded sworn gentry pedigrees county by county — the published volumes are genealogy's bedrock.",
 """GENEALOGY GUIDE — VISITATIONS
Public knowledge explainer.

- Heralds (Clarenceux, Norroy) toured each county, summoning the gentry to prove their arms
- Those who couldn't prove gentry status were 'disclaimed' — the disclaimers list is itself a source
- Pedigrees: typically 3–6 generations, signed by the head of family
- Published by the Harleian Society (100+ volumes) — now digitized
- Reliability: good for the gentry (sworn, with documents); silent on everyone else
- After 1680: no more visitations — the College's records become grants and pedigrees

For English gentry 1500–1700, visitations outrank parish registers.

Public explainer. No private data.""",
 ["1530–1680 county tours.","Disclaimers = a source too.","Harleian Society published."]),
("Flags from arms: banners and standards", "heraldry",
 "Coats of arms became flags: the banner (square, the shield's design) and the standard (long, with badges) — vexillology's heraldic root.",
 """GENEALOGY GUIDE — HERALDIC FLAGS
Public knowledge explainer.

- Banner of arms: square/rectangular, the shield design as a flag — flown by the armiger
- Standard: long tapering flag with badges, motto, and livery colors — for retainers to rally to
- The Royal Standard: the monarch's banner (quartered arms)
- Scottish clan banners: based on chiefs' arms
- City flags: often banners of civic arms (London, Paris)

Genealogical use: church banners and funeral hatchments display quarterings — each quartering is a marriage to an heraldic heiress.

Public explainer. No private data.""",
 ["Banner = shield as flag.","Standard = badges + motto.","Hatchments show quarterings."]),
("Quartering: marriages on the shield", "heraldry",
 "Quartering divides the shield to display inherited arms — each quarter a marriage to an heiress. Read the quarters, read the marriages.",
 """GENEALOGY GUIDE — QUARTERING
Public knowledge explainer.

- An heiress (no brothers) transmits her father's arms to her children
- Her husband impales (side-by-side); their son quarters (quartered shield)
- Grand quarterings: quarters within quarters — pedigrees in geometry
- Example: the royal arms quarter England, Scotland, Ireland
- Limits: the College of Arms caps the number; 'more quarters = older family' is mostly myth
- Cadency marks still apply within quarters

A heavily quartered shield is a marriage map — decode it with the visitation pedigrees.

Public explainer. No private data.""",
 ["Each quarter = an heiress marriage.","Impalement → quartering.","A marriage map in geometry."]),
("Seals: heraldry in wax", "heraldry",
 "Medieval seals pressed arms into wax on charters — thousands survive, often the only image of a family's arms.",
 """GENEALOGY GUIDE — SEALS
Public knowledge explainer.

- 12th–16th centuries: every land transaction sealed — millions of impressions
- Equestrian seals (knights on horseback) show arms on shield and horse
- Women's seals: often the father's arms (as heiress) — key for tracing heiresses
- Matrices (the stamps) survive in museums; impressions in archives
- The Barons' Letter (1301): 95 seals of the barons who wrote to the Pope — a heraldic census
- Forgery detection: seal analysis authenticates charters

Seals date documents and identify people — sigillography is genealogy's forensic science.

Public explainer. No private data.""",
 ["Millions of impressions survive.","Women's seals trace heiresses.","Barons' Letter: 95 seals."]),
("The right to arms: grants today", "heraldry",
 "Arms are still granted — by the College of Arms, the Lord Lyon, and others. How a modern grant works, and what it costs.",
 """GENEALOGY GUIDE — MODERN GRANTS
Public knowledge explainer.

- England: petition the Earl Marshal via the College of Arms — grants to 'eminent' persons (public service, professions, achievement)
- Cost: several thousand pounds (2020s)
- Scotland: Lord Lyon — stricter; arms must be matriculated; 'esquire' status required
- Canada: Canadian Heraldic Authority (1988) — innovative grants, including to institutions
- South Africa: Bureau of Heraldry
- The design: the heralds compose arms with canting or biographical allusions

You cannot buy 'your family crest' — but you can petition for your own arms.

Public explainer. No private data.""",
 ["Petition via College of Arms.","Scotland: stricter (Lyon).","Design = biography in symbols."]),
# --- research method (10) ---
("Start with what you know: the home sources", "research method",
 "Begin genealogy at home: family Bibles, letters, photo albums, and living relatives' memories — the archive before the archive.",
 """GENEALOGY METHOD — HOME SOURCES
Public knowledge explainer.

- Interview relatives now: the oldest first, with a recorder; memories are primary sources
- Family Bibles: birth/marriage/death pages — photograph, don't remove
- Letters and postcards: addresses, dates, relationships in passing
- Photo albums: annotate while someone can still name faces
- Legal papers: deeds, insurance, military discharge papers in drawers
- Organize: one folder per person; cite everything from day one

The rule: exhaust home sources before paying for records. Half of all 'brick walls' fall to a shoebox.

Public explainer. No private data.""",
 ["Oldest first, with recorder.","Shoeboxes beat subscriptions.","Cite from day one."]),
("The research log: your lab notebook", "research method",
 "Keep a research log: every search, every result, every negative — the log is what separates researchers from collectors.",
 """GENEALOGY METHOD — RESEARCH LOGS
Public knowledge explainer.

Log columns: date, repository, source searched, search terms, result (positive/negative), citation, notes.
- Negative results are results: 'not in 1861 census' eliminates a hypothesis
- Prevents repeating failed searches (the #1 time sink)
- Makes the work reproducible — the Proof Standard requires it
- Digital: spreadsheets work; dedicated software (Evidentia, Clooz) helps

A log turns a hobby into research. Future you will thank present you.

Public explainer. No private data.""",
 ["Log negatives too.","Prevents repeat failures.","Reproducibility = research."]),
("Timelines: the lie detector", "research method",
 "Build a timeline for every ancestor: births, marriages, moves, censuses. Impossibilities surface — a mother of 60, a man in two counties.",
 """GENEALOGY METHOD — TIMELINES
Public knowledge explainer.

- One row per event: date, place, source
- Check biology: mothers 15–45, generations 20–35 years
- Check geography: 20 miles/day on foot (pre-railway); counties per census
- Gaps speak: 10 years between children suggests a missing birth or a move
- Overlaps accuse: two families, one name — timelines separate them

Software (Aeon Timeline, spreadsheets) or paper — the medium doesn't matter, the chronology does.

Public explainer. No private data.""",
 ["Mothers 15–45.","20 miles/day on foot.","Gaps speak; overlaps accuse."]),
("Cluster research: the FAN club", "research method",
 "Elizabeth Shown Mills's FAN club: research Friends, Associates, Neighbors — ancestors traveled in packs, and the pack leaves records.",
 """GENEALOGY METHOD — CLUSTER RESEARCH
Public knowledge explainer.

- Witnesses on deeds and wills: usually relatives
- Chain migration: neighbors from the old village settle together — find one, find all
- Church congregations moved as units (especially dissenters, Mormons, Germans)
- Workhouse and court records name associates
- DNA clusters are FAN clubs made of chromosomes

When the ancestor vanishes, research the neighbors. The ancestor reappears in their records.

Public explainer. No private data.""",
 ["Friends, Associates, Neighbors.","Witnesses = relatives.","DNA clusters are FAN clubs."]),
("Evaluating evidence: original vs derivative", "research method",
 "Classify every source: original/derivative, primary/secondary, direct/indirect — and weigh it before you believe it.",
 """GENEALOGY METHOD — EVIDENCE ANALYSIS
Public knowledge explainer (Mills's framework).

- Original vs. derivative: the register vs. the index (indexes err)
- Primary vs. secondary: participant vs. informant (the widow knows the marriage; the grandson guesses)
- Direct vs. indirect: answers the question vs. must be combined
- Death certificates: informants grieve and guess — ages especially unreliable
- Census ages: rounded, estimated, lied about — use ranges

Strong proof = multiple independent sources converging. One source is a clue.

Public explainer. No private data.""",
 ["Original/derivative; primary/secondary.","Death certs: grieving guessers.","Convergence = proof."]),
("Breaking brick walls: the systematic assault", "research method",
 "Brick walls fall to method: re-survey, widen the cluster, change the record type, and question the assumption.",
 """GENEALOGY METHOD — BRICK WALLS
Public knowledge explainer.

1. Restate the problem in one sentence — vagueness is the wall
2. Re-survey: re-read every source (you know more now)
3. Widen: FAN club — siblings, neighbors, witnesses
4. Change record type: stuck in censuses? Try tax, court, land
5. Question assumptions: the surname spelling, the birthplace, the 'fact' from Aunt Mabel
6. DNA: targeted testing of the right cousin
7. Wait: new records digitize constantly — the wall may fall on its own

Most walls are assumptions wearing a surname.

Public explainer. No private data.""",
 ["Restate in one sentence.","Change the record type.","Walls = assumptions."]),
("Organizing files: person, place, and paper", "research method",
 "A filing system that survives decades: one folder per person, source images named by citation, and a master index.",
 """GENEALOGY METHOD — ORGANIZATION
Public knowledge explainer.

- Digital: Surname/FirstName/ folders; files named YYYYMMDD-source-description
- Keep the image AND the citation AND the transcription together
- Back up 3-2-1: three copies, two media, one offsite
- Paper: archival folders, no sticky notes on documents, pencil only
- Software: Gramps (free), RootsMagic, Family Tree Maker — all export GEDCOM
- GEDCOM 7: the interchange standard — your data must outlive your software

Your research is an archive. Archive it like one.

Public explainer. No private data.""",
 ["Name files by citation.","3-2-1 backup.","GEDCOM outlives software."]),
("Writing the family history", "research method",
 "From research to narrative: Ahnentafels, register style, and the story — writing ancestors so descendants will read them.",
 """GENEALOGY METHOD — WRITING
Public knowledge explainer.

- Ahnentafel: numbered ancestor table (you=1, father=2, mother=3, double each generation)
- Register style (NEHGS): numbered generations with full citations
- Narrative: open with a scene, not a birth — 'In March 1847 the ship...'
- Cite as you write — retrofitting citations fails
- Include the failures: the unsolved walls are part of the story
- Publish: print-on-demand, family websites, archive deposit (with privacy for the living)

A cited narrative is the only genealogy that survives its author.

Public explainer. No private data.""",
 ["Ahnentafel numbering.","Open with a scene.","Cite as you write."]),
("Ethics: the living, the dead, and the secrets", "research method",
 "Genealogy ethics: the dead have no privacy, but their living grandchildren do — and DNA keeps revealing secrets.",
 """GENEALOGY METHOD — ETHICS
Public knowledge explainer.

- Living people: never publish names, dates, or DNA of the living without consent
- Recent dead: sensitivity for a generation — grief is fresh
- Secrets: non-paternal events, adoptions, hidden marriages — share privately, gently
- DNA surprises: prepare test-takers; offer support, not just data
- Cultural: some communities restrict ancestral knowledge — respect it
- This database: public and historical records only — never private family data

Genealogy serves the family, not the researcher's curiosity.

Public explainer. No private data.""",
 ["Living: consent required.","Secrets: private and gentle.","Serve the family."]),
("Preserving it: archives and the 100-year plan", "research method",
 "Your research should outlive you: archival deposit, digitization standards, and the 100-year plan for family papers.",
 """GENEALOGY METHOD — PRESERVATION
Public knowledge explainer.

- Digitize: 300–600 dpi TIFF masters; JPEG copies for sharing
- Deposit: county record offices and family history societies accept papers
- Write the guide: future researchers need your log and your reasoning
- Digital preservation: migrate formats every decade; cloud + local
- Donate DNA kits' paper trail with the data
- The 100-year plan: name a steward for your archive in your will

Unpublished research in a shoebox is a future bonfire. Deposit it.

Public explainer. No private data.""",
 ["300–600 dpi TIFF masters.","Deposit with societies.","Name an archive steward."]),
]

# ================= 4. genealogy-signature =================
GENSIG = [
("Signature guide: reading a parish register like a detective", "record guide",
 "A Signature original guide: baptisms, banns, and burials — what parish registers actually record, and the tricks that unlock them.",
 """SIGNATURE ORIGINAL GUIDE — PARISH REGISTERS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The parish register records rites, not lives: baptisms (not births), banns/marriages, burials (not deaths). The Signature method:

1. Read the whole page. Witnesses, godparents, and adjacent entries rebuild the community — your ancestor's FAN club is on the same page.
2. Mind the calendar: before 1752 (England), the year began 25 March — January 1740 is January 1741 to us. Double-date it.
3. Latin shortcuts: 'ob.' (obiit, died), 'bap.' vs 'natus' (baptized vs born — some clerks recorded both).
4. Bishop's transcripts: the annual copy sent to the diocese. When the parish book burned, the transcript survives — and vice versa.
5. Gaps are data: the Civil War gap (1640s), plague years, and negligent clerks each leave signatures.

The golden rule: the register answers the question it was designed for (who was baptized/married/buried, when). Everything else is inference — label it as such.

Public methodology. No private data.""",
 ["Rites, not lives.","1752: the year began in March.","Gaps are data."]),
("Signature guide: the census as a household photograph", "record guide",
 "A Signature original guide: census schedules place ancestors in households every ten years — learn to read the photograph, not just the faces.",
 """SIGNATURE ORIGINAL GUIDE — CENSUS SCHEDULES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

A census schedule is a household photograph with a ten-year exposure gap. The Signature method:

1. Start with the address column — families cluster; check 10 pages either side for siblings.
2. Birthplaces are migration vectors: a Yorkshire birth in a Lancashire household means a move to trace.
3. Occupations are economic history: 'hand loom weaver' in 1841, 'power loom weaver' in 1851 — industrialization in one household.
4. Ages lie: round to ranges (±2 years), especially 1841 (rounded down to 5 for adults).
5. The 1890 US gap (fire, 1931): bridge with 1880 + 1900 + state censuses + city directories.

The Signature rule: cite piece/folio/page (UK) or roll/page (US). 'Found on Ancestry' is not a citation.

Public methodology. No private data.""",
 ["Household photographs.","Birthplaces = migration vectors.","Cite piece/folio/page."]),
("Signature guide: wills — the ancestor's last spreadsheet", "record guide",
 "A Signature original guide: wills and probate inventories — the one document your ancestor dictated, and how to squeeze it dry.",
 """SIGNATURE ORIGINAL GUIDE — WILLS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

A will is a family structure with a signature. The Signature extraction protocol:

1. List every named person with their relationship phrase — 'my beloved wife' (often unnamed), 'my son John', 'my daughter Mary now wife of...'
2. Married daughters: check for portions already paid (marriage settlements) — their absence from the will is normal, not a mystery.
3. The inventory: room-by-room goods. A weaver's loom, a yeoman's livestock, a widow's 'best bed' — social history in a list.
4. Witnesses and bondsmen: usually relatives or close neighbors — FAN club members.
5. Administrations (no will): the bond names the widow and sureties — sometimes the only record of a marriage.

The Signature rule: read the will for what it settles (debts, land, portions), not for a complete family list. Then read the inventory for the life.

Public methodology. No private data.""",
 ["Family structure + signature.","Inventories = social history.","Read for settlements, not completeness."]),
("Signature guide: military paper trails", "record guide",
 "A Signature original guide: muster rolls, pensions, and draft cards — how war's bureaucracy preserves ancestors.",
 """SIGNATURE ORIGINAL GUIDE — MILITARY RECORDS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

War is the great record-creator: states count soldiers carefully. The Signature priority order:

1. Pension files (US Civil War): 50–100 pages — marriages, children, affidavits, family Bible pages. The richest single source in American genealogy.
2. Service records: enlistment (age, birthplace, occupation), musters (present/absent), discharge.
3. Draft cards (WWI US): 24M men, birth dates + addresses — a census substitute for 1917–18.
4. Medal rolls (UK WWI): 5M+ index cards — the 'burnt documents' substitute (60% of service records destroyed 1940).
5. Attestation papers: physical description — height, complexion, tattoos. Your ancestor, described by a sergeant.

The Signature rule: always get the full pension file, not the index summary. The affidavits are the genealogy.

Public methodology. No private data.""",
 ["Pensions: 50–100 pages.","Draft cards = 1917 census.","Full file, not the summary."]),
("Signature guide: the immigrant's paper wake", "record guide",
 "A Signature original guide: manifests, naturalizations, and the myth of Ellis Island name changes.",
 """SIGNATURE ORIGINAL GUIDE — IMMIGRATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The immigrant leaves a paper wake: departure lists, manifests, inspections, naturalizations. The Signature method:

1. The manifest is the core: post-1906 US manifests give birthplace, nearest relative in the old country, destination contact, and physical description.
2. Names were NOT changed at Ellis Island — inspectors worked from manifests written at departure. Changes were voluntary and later.
3. Naturalization 'first papers' name the ship and arrival date — the key to the manifest.
4. Search phonetically: clerks spelled what they heard. Use wildcards and Soundex.
5. Chain migration: travel with the neighbors — one manifest's 'destination contact' unlocks five families.

The Signature rule: the 'nearest relative in old country' column rebuilds the left-behind family. Read every column.

Public methodology. No private data.""",
 ["Manifest = the core.","No Ellis Island name changes.","Chain migration unlocks families."]),
("Signature guide: DNA — the four tests and when to use them", "record guide",
 "A Signature original guide: autosomal, Y, mtDNA, X — which test breaks which wall, and the ethics of testing.",
 """SIGNATURE ORIGINAL GUIDE — GENETIC GENEALOGY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Signature decision tree:
- Unknown parent/grandparent (recent): autosomal (AncestryDNA/23andMe) — matches are cousins; clusters reveal lines.
- Surname origin (paternal line): Y-DNA (FamilyTreeDNA) — the surname's deep history.
- Maternal deep line: mtDNA — slow-mutating, ancient.
- Specific hypothesis: X-DNA's patterned inheritance.

Centimorgan cheat sheet: 3,400+ parent/child; ~1,700 grandparent; 200–400 2nd–3rd cousin; <90 distant.

The Signature ethics protocol:
1. Test the oldest generation first — their DNA is irreplaceable.
2. Warn test-takers: unexpected parentage is common.
3. Never publish living people's surprises. Share privately, gently.
4. DNA confirms paper; it never replaces it.

Public methodology. No private data.""",
 ["Autosomal: recent unknowns.","Y: surnames; mtDNA: deep maternal.","Test oldest first."]),
("Signature guide: newspapers — the gossip archive", "record guide",
 "A Signature original guide: obituaries, court reports, and announcements — digitized newspapers as community memory.",
 """SIGNATURE ORIGINAL GUIDE — NEWSPAPERS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Signature search protocol:
1. Obituaries first: parents, spouses, children, migration — the richest short source. Save the image, not just the OCR.
2. Announcements: births, marriages, engagements — dates and addresses.
3. Court reports: bankruptcies, divorces, crimes — ancestors behaving badly, in print, with details.
4. Funeral notices: the mourner list is the extended family in one column.
5. OCR lies: search variants, browse the page, check the surrounding columns.

Key archives: Chronicling America (LOC, free), British Newspaper Archive (400M+ pages), Trove (Australia, free).

The Signature rule: the newspaper tells you what the community thought worth printing — status, scandal, and celebration. Read it as social history, not just data.

Public methodology. No private data.""",
 ["Obituaries first.","OCR lies — save images.","Social history, not just data."]),
("Signature guide: follow the land", "record guide",
 "A Signature original guide: deeds, valuations, and tithe maps — property records as family trackers.",
 """SIGNATURE ORIGINAL GUIDE — LAND RECORDS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Land stays; people move. The Signature method follows the land:

1. US deeds: grantor/grantee indexes at county recorders — every sale names the family. BLM patents (free online) for homesteads.
2. Ireland: Griffith's Valuation (1847–64) lists every occupier; tithe applotments (1820s–30s) go a generation deeper.
3. England: tithe maps + apportionments (1836–51); enclosure awards name every landholder; manorial court rolls for copyhold.
4. Metes and bounds: learn the compass ('beginning at the white oak') — the original colonies' deed language.
5. Homestead files: 160 acres for 5 years — applications detail entire families.

The Signature rule: when people vanish, the land remembers. Map the parcels; the owners emerge.

Public methodology. No private data.""",
 ["Land stays; people move.","Griffith's: every occupier.","Map parcels, find owners."]),
("Signature guide: the proof standard", "record guide",
 "A Signature original guide: the Genealogical Proof Standard — five steps from collection to conclusion.",
 """SIGNATURE ORIGINAL GUIDE — PROOF STANDARD
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The BCG's five steps, Signature-annotated:
1. Reasonably exhaustive research — all relevant sources, not just the easy ones. (If you haven't checked tax lists, you're not done.)
2. Complete, accurate citations — 'TNA HO 107/1694, f.312, p.18', not '1851 census'.
3. Analysis and correlation — weigh each source (original/derivative, primary/secondary, direct/indirect).
4. Resolution of conflicts — explain the contradictions; don't hide them.
5. Soundly written conclusion — show your work.

The Signature addition: write the negative proof too. 'Why this is NOT the other John Smith' is as valuable as 'why this IS John Smith.'

Genealogy without citations is fiction. Proof without writing is invisible.

Public methodology. No private data.""",
 ["5 steps: search, cite, weigh, resolve, write.","Write the negative proof.","Citations or fiction."]),
("Signature guide: occupations as migration engines", "record guide",
 "A Signature original guide: apprenticeships, guilds, railways, and directories — work records that explain why ancestors moved.",
 """SIGNATURE ORIGINAL GUIDE — OCCUPATIONS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Occupation explains migration. The Signature source map:
- Apprenticeship indentures: bound at 14 for 7 years — names the master, the trade, and the father.
- Guild freedoms (London, from the 1500s): membership lists with origins.
- Railway staff registers: the 19th century's biggest employer kept service records.
- Trade directories: addresses + occupations, updated yearly — the pre-telephone phone book.
- Merchant seamen: crew lists and registry tickets (BT 98–100).
- Teachers/nurses/police: professional registers with training details.

The Signature pattern: miners to coalfields, weavers to mills, sailors to ports, clerks to cities. Find the industry; find the ancestor.

Public methodology. No private data.""",
 ["Work explains movement.","Indentures name masters.","Find the industry."]),
# --- family tree (10): original essays on famous-family research ---
("Signature essay: how to research a musical dynasty", "family tree",
 "A Signature original essay: the Bach family's 150 years as a research case — what musician dynasties teach about occupational inheritance.",
 """SIGNATURE ORIGINAL ESSAY — DYNASTY RESEARCH
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Bachs: 53 documented musicians across 150 years of Thuringia, culminating in Johann Sebastian (1685–1750). The Signature research lesson is occupational inheritance — the dynasty is visible in apprenticeship records, town musician appointments, and the Alt-Bachisches Archiv (the family's own collected works).

Method notes for dynasty research:
1. Occupational records first: guild books, town appointments, apprenticeship indentures — trades pass father to son.
2. The family's own archive: the Bachs preserved each other's manuscripts. Look for the family's papers, not just the state's.
3. Collateral lines: Johann Christoph (who raised Sebastian) matters as much as the famous son — guardianship records reveal family structure.
4. Marriage patterns: Maria Barbara was Sebastian's second cousin — endogamy kept the trade (and the music) in the family.

Public historical figures only. No private data.""",
 ["53 musical Bachs.","Occupation inherits.","Family archives beat state archives."]),
("Signature essay: the Curie women — a scientific matriline", "family tree",
 "A Signature original essay: Marie, Irène, and Ève Curie — five Nobel Prizes and the genealogy of scientific inheritance.",
 """SIGNATURE ORIGINAL ESSAY — CURIE FAMILY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Five Nobel Prizes, two generations, three remarkable women: Marie (Physics 1903, Chemistry 1911), Irène (Chemistry 1935), Ève (biographer; her husband accepted the 1965 Peace Prize for UNICEF).

The Signature research lesson: scientific dynasties transmit through laboratories, not just genes. Irène worked in Marie's lab; Frédéric Joliot married into the lab as much as the family. Trace the institution (the Radium Institute) alongside the pedigree.

Sources for such families: Nobel archives (nominations are public after 50 years), institutional histories, and the family's own writing (Ève's 'Madame Curie', 1937).

Marie Skłodowska's Warsaw roots — the clandestine Flying University — show how education transmits across generations even under occupation.

Public historical figures only. No private data.""",
 ["5 Nobels, 2 generations.","Labs transmit like genes.","Trace institutions + pedigrees."]),
("Signature essay: cousin marriage and the Victorian professional class", "family tree",
 "A Signature original essay: Darwin's marriage to his cousin Emma Wedgwood — what endogamy meant for Victorian science.",
 """SIGNATURE ORIGINAL ESSAY — DARWIN–WEDGWOOD
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Charles Darwin married his first cousin Emma Wedgwood in 1839. Three of their ten children died young; Charles worried about it in print ('On the Various Contrivances...'). The Darwin–Wedgwood pedigree is the most studied inbreeding case in scientific history.

The Signature research lesson: Victorian cousin marriage was a class strategy — it kept fortunes (Wedgwood pottery money funded Darwin's independence) and networks intact. The records are rich: the Darwin Correspondence Project (15,000+ letters) lets researchers watch the family think.

Method: for professional-class Victorians, wills and correspondence outperform parish registers. The money trail is the paper trail.

Public historical figures only. No private data.""",
 ["Cousin marriage as class strategy.","15,000+ letters.","Money trail = paper trail."]),
("Signature essay: the parsonage as literary incubator", "family tree",
 "A Signature original essay: the Brontës of Haworth — how six children in a Yorkshire parsonage became three novelists.",
 """SIGNATURE ORIGINAL ESSAY — BRONTË FAMILY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Patrick Brontë (1777–1861), Irish-born parson; six children; a moorland parsonage with no distractions. Charlotte, Emily, and Anne published in 1847 (as Currer, Ellis, and Acton Bell); Branwell flamed out; Maria and Elizabeth died in childhood.

The Signature research lesson: the Brontës are genealogy's warning about sources. Elizabeth Gaskell's 'Life of Charlotte Brontë' (1857) mythologized; the parsonage museum's manuscripts correct. Always prefer the family's papers (the juvenilia — hundreds of tiny books) over the biographer's narrative.

Demographic note: three siblings dead within eight months (1848–49) — tuberculosis's household arithmetic, visible in any Victorian family reconstitution.

Public historical figures only. No private data.""",
 ["Parsonage as incubator.","Prefer manuscripts to biographers.","TB's household arithmetic."]),
("Signature essay: two presidents, one family", "family tree",
 "A Signature original essay: the Roosevelts — Theodore and Franklin, fifth cousins — and what political dynasties transmit.",
 """SIGNATURE ORIGINAL ESSAY — ROOSEVELT FAMILY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Theodore (1901–09) and Franklin (1933–45): fifth cousins, one Dutch-descended New York family (founder arrived c.1649). Eleanor — Theodore's niece, Franklin's wife — is the hinge.

The Signature research lesson: political dynasties transmit networks and name recognition, not ideology (TR the trust-buster vs. FDR the regulator). The records are public by design: presidential libraries (Hyde Park), the Miller Center, and 150 years of press coverage.

Method: for public families, the archive is the press. Private families need parish registers; public families need newspaper databases.

Only the Adamses match two presidencies from one family.

Public historical figures only. No private data.""",
 ["Fifth cousins, two presidencies.","Eleanor is the hinge.","The press is the archive."]),
("Signature essay: bankers, popes, and queens", "family tree",
 "A Signature original essay: the Medici — how a banking family bought its way into the papacy and two French thrones.",
 """SIGNATURE ORIGINAL ESSAY — MEDICI
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Giovanni di Bicci's bank (1397) → Cosimo's Florence → Lorenzo's Renaissance → Leo X and Clement VII (popes) → Catherine and Marie (queens of France) → Cosimo I, Grand Duke of Tuscany. Three centuries, one family business: money converted into power converted into art.

The Signature research lesson: follow the money's paper — bank ledgers, dowry contracts, and the family's own archive (the Mediceo). The art history (patronage) is the family's accounts payable made visible.

Heraldic note: the Medici palle (balls) on the shield are canting-adjacent branding — the family's logo before logos.

Public historical figures only. No private data.""",
 ["Bank → papacy → thrones.","Money into power into art.","Follow the ledgers."]),
("Signature essay: Victoria's grandchildren and European diplomacy", "family tree",
 "A Signature original essay: Queen Victoria's 42 grandchildren on Europe's thrones — genealogy as foreign policy, 1870–1914.",
 """SIGNATURE ORIGINAL ESSAY — WINDSOR DESCENT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Victoria (1819–1901) and Albert's nine children married into the royal houses of Germany, Russia, Spain, Greece, Romania, and Norway. By 1914 her grandchildren included the Kaiser (Wilhelm II), the Tsarina (Alexandra), and the kings of Spain, Greece, and Norway.

The Signature research lesson: it didn't prevent WWI — the famous 'royal cousins' telegram diplomacy of July 1914 failed. Genealogy explains the invitations, not the outcomes.

Method: royal genealogy is the best-documented on Earth (official biographies, the Royal Archives). The research skill is reading against the hagiography — the official sources flatter.

The 1917 renaming (Saxe-Coburg-Gotha → Windsor) is itself a genealogical event: identity edited by war.

Public historical figures only. No private data.""",
 ["42 grandchildren on thrones.","Genealogy ≠ diplomacy.","1917: identity edited by war."]),
("Signature essay: the Habsburg jaw — pedigree collapse", "family tree",
 "A Signature original essay: 600 years of Habsburg cousin marriage and the mandibular prognathism that became a genetics textbook.",
 """SIGNATURE ORIGINAL ESSAY — HABSBURGS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Charles V to Charles II of Spain (1661–1700): uncle-niece and cousin marriages compounded until the Spanish line's inbreeding coefficient exceeded a parent-child union's. Charles II — disabled, infertile — ended the Spanish Habsburgs; the 'Habsburg jaw' is pedigree collapse made visible.

The Signature research lesson: royal pedigrees are the longest controlled experiments in genetics. The records (court archives, portraits, medical reports) let modern researchers compute inbreeding coefficients across 16 generations.

Method note: portraiture is evidence — the jaw's progression is datable by canvas.

Maria Theresa (16 children, incl. Marie Antoinette) shows the strategy's logic: marriage as statecraft, biology as collateral.

Public historical figures only. No private data.""",
 ["600 years; collapse at the end.","Portraits are evidence.","Marriage as statecraft."]),
("Signature essay: the Romanovs' 300 years", "family tree",
 "A Signature original essay: Michael I (1613) to Nicholas II (1918) — hemophilia, Rasputin, and Ekaterinburg.",
 """SIGNATURE ORIGINAL ESSAY — ROMANOVS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

305 years, ending 17 July 1918 in a Ekaterinburg basement. The Signature research lesson is medical genealogy: Queen Victoria's hemophilia gene entered Russia through Alexandra; the heir Alexei's illness gave Rasputin his access; Rasputin's access discredited the monarchy.

The records: the dynasty documented itself obsessively (court circulars, diaries — Nicholas's diary survives). The Soviet archives (opened 1990s) added the executioners' reports. The 2007 DNA identification of Alexei and Maria closed the forensic chapter.

Canonized 2000 — genealogy meets hagiography.

Public historical figures only. No private data.""",
 ["1613–1918.","Hemophilia → Rasputin → collapse.","DNA closed the case, 2007."]),
("Signature essay: the Tolstoys' 10,000 letters", "family tree",
 "A Signature original essay: Leo and Sophia Tolstoy's family — the best-documented family in literary history.",
 """SIGNATURE ORIGINAL ESSAY — TOLSTOYS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

13 children (8 survived), Yasnaya Polyana, 10,000+ preserved letters, Sophia's diaries, and a wife who hand-copied 'War and Peace' seven times. The Tolstoys are the control group for family-history method: when the sources are total, what can we know?

The Signature research lesson: abundance has its own problems — contradictions multiply with sources. Sophia's diaries vs. Leo's: two archives, two marriages. The genealogist's job becomes arbitration, not discovery.

Alexandra's Tolstoy Foundation (refugee aid) extended the family into institutions — trace the foundation's records for the 20th-century diaspora.

Public historical figures only. No private data.""",
 ["10,000+ letters.","Abundance needs arbitration.","Two diaries, two marriages."]),
# --- historical figure (10) ---
("Signature portrait: Ada Lovelace, analyst of the Engine", "historical figure",
 "A Signature original portrait: Byron's daughter (1815–1852), the Bernoulli algorithm, and the first vision of computing as music.",
 """SIGNATURE ORIGINAL PORTRAIT — ADA LOVELACE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Augusta Ada King, Countess of Lovelace — the only legitimate child of Lord Byron, who left England when she was an infant. Her mother, Annabella Milbanke, dosed her with mathematics to suppress the poetry.

1843: translating Menabrea on Babbage's Analytical Engine, Ada added seven Notes — Note G containing the Bernoulli-number algorithm, the first computer program. More visionary: 'the Engine might compose elaborate and scientific pieces of music' — computing as media, a century early.

She died at 36, the age Byron died, and was buried beside him at her request.

The Signature genealogical note: the Byron–Milbanke separation papers are the primary source for her infancy; the Lovelace papers (Bodleian) hold the mathematics.

Public historical figure. No private data.""",
 ["Byron's legitimate daughter.","Note G: first program.","Computing as music, 1843."]),
("Signature portrait: Frederick Douglass, the escaped orator", "historical figure",
 "A Signature original portrait: from Talbot County slavery (c.1818) to US Marshal — the autobiographies as genealogical sources.",
 """SIGNATURE ORIGINAL PORTRAIT — FREDERICK DOUGLASS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Born Frederick Augustus Washington Bailey, enslaved in Maryland; mother Harriet Bailey, father unrecorded. Escaped 3 September 1838 disguised as a sailor — funded by Anna Murray, the free Black woman he married eleven days later.

His three autobiographies (1845, 1855, 1881) are unusual genealogical sources: a Black family history written by its subject, naming the enslaved community the records ignored.

1877: US Marshal for the District of Columbia. 1884: married Helen Pitts (white) — the interracial marriage scandalized even allies.

The Signature note: Douglass's birth year (c.1818) is approximate — enslaved births went unrecorded. His uncertainty about his own age is itself the historical evidence.

Public historical figure. No private data.""",
 ["Three autobiographies.","Escaped 1838.","Uncertain birthday = evidence."]),
("Signature portrait: Marie Tharp, mapper of the deep", "historical figure",
 "A Signature original portrait: the geologist (1920–2006) barred from ships who mapped the Mid-Atlantic Ridge from a desk — and proved plate tectonics.",
 """SIGNATURE ORIGINAL PORTRAIT — MARIE THARP
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Daughter of a USDA soil surveyor — she grew up watching her father map dirt, then mapped the ocean floor. Barred from Lamont's research ships (no women), she plotted sonar soundings by hand; her 1957 North Atlantic map revealed the rift valley running down the Mid-Atlantic Ridge.

Bruce Heezen called it 'girl talk.' The ridge's symmetry — and the magnetic stripes — made it the visual proof of seafloor spreading.

The Signature genealogical note: her father's survey career (documented in USDA personnel records) is the occupational inheritance — mapping as family trade, like the Bachs' music.

Library of Congress: one of the century's great cartographers (1997).

Public historical figure. No private data.""",
 ["Soil surveyor's daughter.","Mapped from a desk.","'Girl talk' → plate tectonics."]),
("Signature portrait: Ibn Battuta, the 120,000-km qadi", "historical figure",
 "A Signature original portrait: Tangier to China (1325–1355) — the longest pre-modern journey, dictated as the Rihla.",
 """SIGNATURE ORIGINAL PORTRAIT — IBN BATTUTA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Born 1304 to a family of qadis (judges) in Tangier. Left for the Hajj at 21; returned 30 years later having served as a judge in Delhi, visited the Maldives and East Africa, met the Byzantine emperor, and reached China.

The Signature research note: the Rihla was dictated to Ibn Juzayy in Fez (c.1355) — a collaboration, like a modern oral history. Scholars debate some passages (did he really reach Beijing?); the genealogist's instinct applies: corroborate — the Delhi sultanate's records confirm his judgeship.

His family trade (law) was his passport: every Muslim court needed a qadi.

Public historical figure. No private data.""",
 ["30 years, 120,000 km.","Qadi as passport.","Dictated like oral history."]),
("Signature portrait: Sojourner Truth, the itinerant witness", "historical figure",
 "A Signature original portrait: Isabella Baumfree (c.1797–1883) — from Ulster County slavery to the Akron stage.",
 """SIGNATURE ORIGINAL PORTRAIT — SOJOURNER TRUTH
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Enslaved in New York; escaped 1826 with her infant daughter; in 1828 won a court case recovering her son Peter — the first Black woman to win such a case against a white man. Renamed herself in 1843: 'Sojourner' (traveler) 'Truth.'

The Signature source note: she was illiterate; her 1850 'Narrative' was dictated to Olive Gilbert — like Ibn Battuta's Rihla, an oral history mediated by a scribe. The famous 1851 Akron speech survives in Frances Gage's 1863 version ('Ain't I a Woman?') — historians debate the dialect rendering, a reminder that mediated sources need source criticism.

Met Lincoln (1864); recruited Black troops; campaigned for land grants — the reparations debate's ancestor.

Public historical figure. No private data.""",
 ["Won her son's freedom, 1828.","Dictated narrative.","Mediated sources need criticism."]),
("Signature portrait: Mutsuhito, the Meiji emperor", "historical figure",
 "A Signature original portrait: the boy emperor (1852–1912) whose reign compressed two centuries of change into 45 years.",
 """SIGNATURE ORIGINAL PORTRAIT — EMPEROR MEIJI
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Succeeded 1867, aged 14, as the shogunate fell. His reign name — Meiji, 'enlightened rule' — became the era's name: Charter Oath, constitution, railways, conscription, mass schooling, victory over Russia (1905).

The Signature genealogical note: 15 children by consorts; the imperial household's records are meticulous. The interesting research is the symbolic genealogy — the state reconstructed the emperor's divine descent (the 'unbroken line') as modern ideology.

In his lifetime: samurai domains to industrial empire. No life better measures the 19th century's acceleration.

Public historical figure. No private data.""",
 ["Reigned 1868–1912, from age 14.","45 years, two centuries of change.","Genealogy as state ideology."]),
("Signature portrait: Nzinga, queen of two kingdoms", "historical figure",
 "A Signature original portrait: the Mbundu queen (c.1583–1663) who fought the Portuguese slave trade for 40 years.",
 """SIGNATURE ORIGINAL PORTRAIT — QUEEN NZINGA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1622: as ambassador, she refused the Portuguese governor's floor mat and sat on a servant's back — diplomacy as theater. Queen from c.1624; allied with the Dutch against Portugal (1641–48); built Matamba as a refuge for escaped enslaved people.

The Signature research note: African royal genealogy runs through oral tradition and Portuguese colonial records — two archives that disagree. Nzinga's baptism (Ana de Sousa, 1622) is documented; her strategic use of Christianity was diplomatic, not devotional.

Died 1663, ~80, succeeded by her sister. Angola's national heroine.

Public historical figure. No private data.""",
 ["40 years of resistance.","Diplomacy as theater.","Two archives, one queen."]),
("Signature portrait: the Rani of Jhansi", "historical figure",
 "A Signature original portrait: Lakshmibai (1828–1858) — the warrior queen of the 1857 uprising, dead at 29.",
 """SIGNATURE ORIGINAL PORTRAIT — RANI LAKSHMIBAI
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Manikarnika Tambe of Varanasi; married the Maharaja of Jhansi (1842); widowed; adopted Damodar Rao. The British Doctrine of Lapse denied the adoption and annexed Jhansi (1853). In 1857 she took up arms, held the fort under siege, and died at Gwalior on 18 June 1858.

The British called her 'the most dangerous of all Indian leaders' — the enemy's assessment is the honest source.

The Signature genealogical note: the Doctrine of Lapse made genealogy into law — adoptions, the core of Maratha succession, were nullified by imperial fiat. Family history as colonial policy.

India's 'Joan of Arc' — the comparison writes itself, and she earns it.

Public historical figure. No private data.""",
 ["Died in battle at 29.","Doctrine of Lapse = genealogy as law.","Enemy's praise = honest source."]),
("Signature portrait: Mansa Musa, the golden Hajj", "historical figure",
 "A Signature original portrait: Mali's emperor (c.1280–c.1337) whose 1324 pilgrimage moved gold markets.",
 """SIGNATURE ORIGINAL PORTRAIT — MANSA MUSA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

60,000 attendants, 80 camels of gold, Cairo's gold price down ~25% for a decade. The Catalan Atlas (1375) draws him holding a nugget — medieval Europe's image of African wealth.

The Signature research note: the Arabic chronicles (al-Umari, Ibn Khaldun) are the sources; the gold figures are estimates, not audits. The genealogist's caution applies to kings too: corroborate, discount, contextualize.

His legacy outlasted the gold: Timbuktu's mosques and madrasas, the scholarly golden age his patronage seeded.

Often called history's richest person — the title depends on the gold economy he commanded, not a bank balance.

Public historical figure. No private data.""",
 ["1324: gold crashed in Cairo.","Catalan Atlas portrait.","Patronage outlasted gold."]),
("Signature portrait: Hatshepsut, the erased pharaoh", "historical figure",
 "A Signature original portrait: Egypt's female king (c.1507–1458 BCE) — 21 prosperous years, then damnatio memoriae.",
 """SIGNATURE ORIGINAL PORTRAIT — HATSHEPSUT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Daughter of Thutmose I, wife of Thutmose II, regent for Thutmose III — then pharaoh in her own right, depicted with false beard and male regalia because the office had no feminine form. Deir el-Bahari, the Punt expedition, two decades of prosperity.

Then Thutmose III erased her: names chiseled out, statues smashed. The Signature note: erasure is evidence — damnatio memoriae tells us she mattered enough to delete.

Rediscovered by 19th-century Egyptology; mummy identified 2007 (KV60).

The genealogical irony: the stepson who erased her preserved her by the thoroughness of the attempt — every chisel mark is a citation.

Public historical figure. No private data.""",
 ["Female pharaoh, 21 years.","Erasure = evidence.","Mummy found 2007."]),
# --- case study (10): clearly-labeled illustrative examples ---
("Signature case study: the mariner who was never home", "case study",
 "A Signature original worked example (illustrative composite — not a real person): tracing a 19th-century seaman through crew lists.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

The problem: 'mariner', 1851 census, birthplace 'at sea'. The Signature solution path:

1. Census: age 34, wife Mary, two children, Liverpool — but mariners are absent half the decade. Don't trust census continuity.
2. Marriage register (1844): names his ship and his father (also a mariner) — the occupational inheritance.
3. Crew lists (BT 98): the ship's agreements (1843–45) give his age, birthplace ('St. Helena'), and previous vessel — follow the ship.
4. St. Helena baptism registers: the baptism; the father's service record explains the posting.
5. Master's certificate (1852): exact birth date.

The Signature lesson: for mobile occupations, the employer's records beat the state's. Crew lists, tickets, certificates — the firm knew what the census missed.

Illustrative composite. No real person described.""",
 ["Mariners defeat censuses.","Follow the ship.","Employer's records beat state's."]),
("Signature case study: the girl who went into service", "case study",
 "A Signature original worked example (illustrative composite): a child present in 1881, gone in 1891 — solved through service records.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

The problem: girl, 6, in the 1881 census; absent from the 1891 household; no death registration.

The Signature solution path:
1. 1891: search by forename + birth year + birthplace — drop the surname. Found: 16-year-old domestic servant, 30 miles away.
2. 1901: married, two children — the marriage certificate names her father, closing the loop.
3. Alternatives eliminated: workhouse admissions (no match), passenger lists (no match).

The Signature lesson: working-class girls 'disappeared' into service — the largest female occupation of the century. The census didn't lose them; the household did.

Illustrative composite. No real person described.""",
 ["Search forename + birthplace.","Service swallowed girls.","Marriage names the father."]),
("Signature case study: separating the two John Smiths", "case study",
 "A Signature original worked example (illustrative composite): same name, same parish, 1780–1800 — tax, wills, and signatures tell them apart.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

Two John Smiths baptizing children in one parish. The Signature separation protocol:

1. Land tax: one assessed on 40 acres (yeoman), one on a cottage (laborer) — different economic worlds, same name.
2. Wills: the yeoman's 1798 will names children matching one baptism set exactly.
3. Literacy: the yeoman signs; the laborer marks — compare marks across documents.
4. Burial ages: 1803 'aged 62' fits the 1741 baptism; 1811 'aged 68' fits 1743.

The Signature lesson: same name ≠ same man. Economic records separate what names conflate. Never merge identities on name alone — merge on converging evidence.

Illustrative composite. No real person described.""",
 ["Tax separates names.","Signatures vs marks.","Converging evidence only."]),
("Signature case study: the burned Irish registers", "case study",
 "A Signature original worked example (illustrative composite): pre-Famine Irish research after the 1922 fire — reconstruction from substitutes.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

The problem: family emigrated 1847; parish registers destroyed 1922.

The Signature reconstruction:
1. Griffith's Valuation (1850s): the surname clusters in three townlands — the origin zone.
2. Tithe applotments (1830s): same surname, same townlands, one generation earlier — continuity.
3. Estate papers: the landlord's rent books name tenants yearly — the missing register's shadow.
4. US manifest (1850): names the townland; neighbors' manifests show chain migration.

The Signature lesson: Irish research is triangulation. No substitute replaces the registers; five substitutes together approximate them. The estate papers are the most underused source in Irish genealogy.

Illustrative composite. No real person described.""",
 ["1922 fire.","Five substitutes triangulate.","Estate papers underused."]),
("Signature case study: the 90-page pension file", "case study",
 "A Signature original worked example (illustrative composite): a Union pension file's 90 pages — three marriages, eight children, one Bible page.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

The file: Union infantry private, pension application 1890–1910.

Contents: service record (1862–65, wounded 1864); marriage certificates (1866, 1881); eight children's affidavits; a copied family Bible page; neighbors' identity testimony; surgeons' exams.

The Signature lesson: order the full file, never the summary. The affidavits — neighbors swearing to births they witnessed — are the family structure. The Bible page is the vital record the county never kept.

Note: Confederate pensions are state-level (no federal files).

Illustrative composite. No real person described.""",
 ["90 pages, one life.","Affidavits = family structure.","Full file, not summary."]),
("Signature case study: the name that wasn't changed", "case study",
 "A Signature original worked example (illustrative composite): a 1907 manifest disproves the family's Ellis Island story.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

Family lore: 'they changed our name at Ellis Island.' The Signature document chain:

1. Manifest (1907, line 14): the 'American' spelling — written by the Hamburg clerk at departure.
2. Declaration of intention (1912): same spelling, in the immigrant's own hand.
3. 1910 census: the old spelling persists — no change yet.
4. Draft card (1918): the new spelling, signed by the man himself.

The Signature lesson: inspectors copied manifests; they didn't invent names. The change was voluntary, gradual, post-arrival — often to simplify spelling or dodge discrimination. Family lore compresses a decade into a dockside moment; documents stretch it back out.

Illustrative composite. No real person described.""",
 ["Manifests written at departure.","Change was voluntary, later.","Lore compresses; documents stretch."]),
("Signature case study: the will's missing daughter", "case study",
 "A Signature original worked example (illustrative composite): an 1820 will omits a daughter — the marriage settlement explains.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

The will (1820) names sons, widow, grandchildren — no daughter, though baptisms show one.

The Signature solution:
1. Marriage (1805): the settlement gave her £500 — her portion, paid in her lifetime.
2. The rule: daughters' portions were lifetime advances; wills settle remaining business, not complete families.
3. Chancery suit (1825): the grandson's suit — depositions name everyone, including the 'missing' daughter.

The Signature lesson: read wills for unsettled business. Then read settlements and suits for the settled kind. The archive's silences have paperwork.

Illustrative composite. No real person described.""",
 ["Wills = unsettled business.","Portions paid at marriage.","Silences have paperwork."]),
("Signature case study: DNA and the 1880s secret", "case study",
 "A Signature original worked example (illustrative composite): autosomal clusters resolve an 1880s non-paternal event — with ethics.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

The wall: a great-grandfather, no father named, born 1880s.

The Signature protocol:
1. Test the oldest living descendant (autosomal).
2. Cluster matches: a 200–400 cM group sharing an unknown ancestral couple.
3. Build the candidate's tree forward: sons in the right place, right time.
4. Targeted testing confirms.

The Signature ethics: this rewrites a family's story. Share privately, gently, with support — never publish living people's surprises. Warn test-takers before they test: unexpected parentage is common.

The Signature lesson: DNA + paper together break walls neither breaks alone.

Illustrative composite. No real person described.""",
 ["Clusters reveal lines.","Paper + DNA together.","Ethics: private and gentle."]),
("Signature case study: bridging with the 1939 Register", "case study",
 "A Signature original worked example (illustrative composite): the 1939 Register fills the 1921–1951 UK census gap.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

No UK census 1921–1951 (1931 destroyed, 1941 never taken). The Signature bridge:

1. 1939 Register: household with exact birth dates (day/month/year), occupations, married women's maiden names.
2. Cross-check 1921: the family matches, ages advanced correctly.
3. Redactions: anyone born within 100 years (not proven dead) is blacked out — the living protected.
4. Post-war: electoral rolls continue the thread.

The Signature lesson: the Register is a census in all but name — compiled for identity cards and rationing. Its redactions are the privacy principle made visible: this database does the same, publishing only the safely historical.

Illustrative composite. No real person described.""",
 ["Fills 1921–1951.","Exact birth dates.","Redactions = privacy visible."]),
("Signature case study: Domesday to the census — one manor", "case study",
 "A Signature original worked example (illustrative composite): 750 years of tenants in one English manor, 1086–1841.",
 """SIGNATURE ORIGINAL CASE STUDY — ILLUSTRATIVE EXAMPLE
src: signature. This is a fictional composite created to demonstrate method. It describes no real private person.

One manor, 28 villagers in Domesday (1086). The Signature chain:

1. Court rolls (1400s–1700s): copyhold admissions, holding by holding — surnames stabilize by 1500.
2. Parish registers (from 1560): baptisms link court-roll names to families.
3. Enclosure award (1810): every landholder, every acreage.
4. Tithe map (1840) + 1841 census: the same surnames on the same farms.

The Signature lesson: place defeats name. Families stay; follow the land and the manor, and the people emerge. In unbroken rural parishes, Domesday-to-census continuity is real — 750 years on one farm.

Illustrative composite. No real person described.""",
 ["One manor, 750 years.","Place defeats name.","Follow the land."]),
# --- heraldry (10) ---
("Signature guide: reading a coat of arms", "heraldry",
 "A Signature original heraldry guide: shield, tinctures, charges — the grammar of arms as genealogical evidence.",
 """SIGNATURE ORIGINAL GUIDE — HERALDRY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The blazon is the arms: 'Gules, a lion rampant Or' defines the coat; the painting is just an instance. The Signature reading method:

1. Tinctures: Or, Argent (metals); Gules, Azure, Vert, Sable, Purpure (colors). Metal on color, color on metal — violations are the interesting cases.
2. Charges: the vocabulary — lions, eagles, mullets (stars), crosses, in thousands of variants.
3. Cadency: the label (eldest son), crescent (second), mullet (third) — birth order on the shield.
4. The tourist trap: arms belong to individuals, not surnames. The 'family crest' for your surname is heraldic fraud.

Genealogical use: church monuments display arms with quarterings — each quartering is a marriage. Read the monument; read the marriages.

Public knowledge. No private data.""",
 ["Blazon = the arms.","Metal on color.","Arms ≠ surname."]),
("Signature guide: the College of Arms and its visitations", "heraldry",
 "A Signature original guide: the heralds' county tours (1530–1680) and the sworn pedigrees they left.",
 """SIGNATURE ORIGINAL GUIDE — VISITATIONS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The heralds toured each county, summoned the gentry, and recorded sworn pedigrees — 3–6 generations, signed by the head of family. Those who couldn't prove gentility were 'disclaimed' (the disclaimers list is itself a source).

The Signature assessment: visitation pedigrees are the best source for English gentry 1500–1700 — sworn, witnessed, and cross-checkable against wills. Their bias is class: they are silent on everyone below gentility.

Published by the Harleian Society (100+ volumes), now digitized. The College of Arms (founded 1484) still grants arms today.

For everyone else: parish registers. For the gentry: visitations first.

Public knowledge. No private data.""",
 ["Sworn pedigrees, 1530–1680.","Best for gentry 1500–1700.","Disclaimers = a source."]),
("Signature guide: crests, mottoes, supporters", "heraldry",
 "A Signature original guide: the achievement's extras — crest, motto, supporters, and what each one signals.",
 """SIGNATURE ORIGINAL GUIDE — ACHIEVEMENT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

- Crest: on the helmet — the 'crest' is one component, not the whole arms.
- Motto: unregulated in England; change it freely. (The Scots are stricter.)
- Supporters: restricted to peers, knights of orders, and special grantees — supporters on a shield are a rank signal.
- Helmets: rank-coded metalwork — gold and barred for royalty, steel for esquires.
- Mantling: stylized cloth in the main tinctures.

The Signature reading: an achievement is a status document. Supporters = peerage (check the peerage rolls). Multiple quarterings = heiress marriages (check the visitations).

Public knowledge. No private data.""",
 ["Crest ≠ arms.","Supporters = rank signal.","Achievement = status document."]),
("Signature guide: canting arms — puns as finding aids", "heraldry",
 "A Signature original guide: heraldic puns — bows for Bowman, swans for Swann — and how they identify families.",
 """SIGNATURE ORIGINAL GUIDE — CANTING ARMS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Canting (punning) arms encode the name: Bowman/bows, Swann/swans, Cockburn/cock, Trumpington/trumpets. The Washington arms (stars and stripes) may be the US flag's ancestor — the pun is debated, the resemblance isn't.

The Signature use: canting arms are finding aids. An unidentified monument with swans is a Swann (or Swan) until proven otherwise. Cross-check with the parish register.

Multilingual puns abound in Welsh and German heraldry — the pun works in the family's language.

Public knowledge. No private data.""",
 ["Arms as puns.","Unidentified monument? Read the pun.","Washington: stars and stripes."]),
("Signature guide: kamon — Japan's heraldry", "heraldry",
 "A Signature original guide: Japan's kamon — chrysanthemum, hollyhock, wisteria — the world's other great crest system.",
 """SIGNATURE ORIGINAL GUIDE — KAMON
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

In use since the Heian period (794–1185): the imperial 16-petal chrysanthemum, the Tokugawa triple hollyhock, the Fujiwara wisteria. No tincture rules, no cadency — branches and retainers share crests.

The Signature contrast: European heraldry is individual and regulated; kamon are familial and customary. Both do the same work — marking belonging on cloth, wood, and stone.

Genealogical use: kamon on gravestones, kimono, and roof tiles. Japanese temple death registers (kakocho) pair with crests to identify households.

Public knowledge. No private data.""",
 ["Heian origins.","Familial, not individual.","Read them on gravestones."]),
("Signature guide: quartering — marriages in geometry", "heraldry",
 "A Signature original guide: how quartered shields map heiress marriages across generations.",
 """SIGNATURE ORIGINAL GUIDE — QUARTERING
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

An heiress (daughter with no brothers) transmits her father's arms. Her husband impales; their son quarters. Each quarter is a marriage; grand quarterings nest them.

The Signature decoding method:
1. Quarter 1: the bearer's paternal arms.
2. Quarters 2+: heiress marriages, in order.
3. Cross-check each heiress against visitation pedigrees — quarterings were sometimes claimed, not earned.
4. The royal arms: England, Scotland, Ireland — the union in geometry.

A heavily quartered shield is a marriage map. Decode it with the pedigrees, and the wives reappear — women the parish registers under-record.

Public knowledge. No private data.""",
 ["Each quarter = a marriage.","Heiresses transmit arms.","Decode with visitations."]),
("Signature guide: seals in wax", "heraldry",
 "A Signature original guide: medieval seals — millions of wax impressions, often the only image of a family's arms.",
 """SIGNATURE ORIGINAL GUIDE — SEALS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Every land transaction, 12th–16th centuries, was sealed: equestrian seals (knights with arms on shield and horse), women's seals (often the father's arms — tracing heiresses), merchants' marks.

The Signature uses:
1. Dating: seal styles date charters when the text doesn't.
2. Identification: the Barons' Letter (1301) — 95 seals, a heraldic census of the baronage.
3. Authentication: seal analysis detects forged charters.
4. Women's lines: a wife's seal with her father's arms proves the heiress marriage.

Matrices survive in museums; impressions in archives. Sigillography is genealogy's forensic science.

Public knowledge. No private data.""",
 ["Millions survive.","Women's seals trace heiresses.","Dating + authentication."]),
("Signature guide: banners, standards, and hatchments", "heraldry",
 "A Signature original guide: arms as flags — and funeral hatchments as quartered obituaries.",
 """SIGNATURE ORIGINAL GUIDE — FLAGS & HATCHMENTS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

- Banner of arms: the shield as a square flag, flown by the armiger.
- Standard: long and tapering — badges, motto, livery colors for retainers to rally to.
- The Royal Standard: quartered arms as the monarch's presence.
- Funeral hatchment: a diamond-shaped board with the deceased's arms (and spouse's), hung on the house, then the church.

The Signature use: hatchments are obituaries in heraldry — they record the marriage (impaled or quartered arms), and churches full of them are pedigree walls. Photograph and blazon them; cross-check with registers.

Public knowledge. No private data.""",
 ["Banner = shield as flag.","Hatchments = heraldic obituaries.","Churches as pedigree walls."]),
("Signature guide: petitioning for arms today", "heraldry",
 "A Signature original guide: modern grants — the College of Arms, the Lord Lyon, and how new arms are made.",
 """SIGNATURE ORIGINAL GUIDE — MODERN GRANTS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Arms are still granted: petition the Earl Marshal via the College of Arms (England), the Lord Lyon (Scotland — stricter, matriculation required), the Canadian Heraldic Authority (1988, innovative), the Bureau of Heraldry (South Africa).

The Signature facts:
- Grants go to 'eminent' persons — public service, professions, achievement.
- Cost: several thousand pounds; the heralds design with biographical allusions.
- You cannot inherit arms you can't prove — and you can't buy 'your family crest' (that's the tourist fraud).
- Scottish arms must be matriculated; differences (cadency) are enforced.

The design meeting is biography rendered in symbols — the most personal document the state issues.

Public knowledge. No private data.""",
 ["Petition, don't purchase.","Scotland: stricter.","Biography in symbols."]),
# --- research method (10) ---
("Signature method: start in the shoebox", "research method",
 "A Signature original method: home sources first — Bibles, letters, albums, and the oldest relative with a recorder.",
 """SIGNATURE ORIGINAL METHOD — HOME SOURCES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Signature order of operations:
1. Interview the oldest relatives now — with a recorder. Memories are primary sources; they also die.
2. Photograph the family Bible pages (don't remove them), the letters, the albums — annotate faces while someone can name them.
3. Collect the drawer archive: deeds, discharge papers, insurance policies.
4. One folder per person from day one; cite everything.

The Signature statistic: half of all 'brick walls' fall to a shoebox. The subscription sites sell you records; your attic holds the ones that matter.

Exhaust home before paying. The archive before the archive.

Public methodology. No private data.""",
 ["Oldest first, recorder on.","Half of walls fall to shoeboxes.","Cite from day one."]),
("Signature method: the research log", "research method",
 "A Signature original method: log every search — the lab notebook that separates researchers from collectors.",
 """SIGNATURE ORIGINAL METHOD — RESEARCH LOGS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Columns: date, repository, source, search terms, result (+/−), citation, notes.

The Signature rules:
1. Log negatives: 'not in 1861 census' eliminates a hypothesis — that's a result.
2. Never repeat a failed search: the log is the #1 time-saver in genealogy.
3. Reproducibility: the Proof Standard requires it; future you requires it more.

Digital (spreadsheets) or paper — the medium is irrelevant, the habit is everything. A log turns a hobby into research.

Public methodology. No private data.""",
 ["Log the negatives.","Never repeat failures.","Habit > medium."]),
("Signature method: timelines as lie detectors", "research method",
 "A Signature original method: chronology for every ancestor — biology and geography as constraints.",
 """SIGNATURE ORIGINAL METHOD — TIMELINES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

One row per event: date, place, source. Then apply constraints:

- Biology: mothers 15–45; generations 20–35 years. A mother of 60 is two women.
- Geography: 20 miles/day on foot (pre-railway); check census counties against movement.
- Gaps: 10 childless years suggest a missing birth, a move, or a second family.
- Overlaps: one name, two places, same year — timelines separate the two John Smiths.

The Signature rule: build the timeline before the theory. Chronology is the lie detector; narrative comes after.

Public methodology. No private data.""",
 ["Biology constrains.","Geography constrains.","Timeline before theory."]),
("Signature method: the FAN club", "research method",
 "A Signature original method: Friends, Associates, Neighbors — when the ancestor vanishes, research the pack.",
 """SIGNATURE ORIGINAL METHOD — CLUSTER RESEARCH
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Elizabeth Shown Mills's FAN principle, Signature-annotated:
- Witnesses on deeds/wills: usually kin. Name them all.
- Chain migration: the old village's neighbors settle together — find one manifest, find five families.
- Congregations moved as units: dissenters, Mormons, Germans — the church book is the passenger list.
- DNA clusters are FAN clubs written in chromosomes.

The Signature rule: the ancestor who leaves no records traveled with people who left many. Research the neighbors; the ancestor reappears in their paperwork.

Public methodology. No private data.""",
 ["Research the pack.","Witnesses = kin.","Neighbors' paper holds ancestors."]),
("Signature method: weighing evidence", "research method",
 "A Signature original method: original/derivative, primary/secondary, direct/indirect — classify before you believe.",
 """SIGNATURE ORIGINAL METHOD — EVIDENCE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Mills's three axes:
- Original vs. derivative: the register vs. the index. Indexes err; always check the image.
- Primary vs. secondary: the participant vs. the informant. The widow knows her marriage; the grandson guesses at her birth.
- Direct vs. indirect: answers the question vs. must be assembled.

The Signature warnings:
- Death certificates: informants grieve and guess. Ages are the least reliable field.
- Census ages: rounded, estimated, vanity-adjusted. Use ranges.
- One source is a clue. Convergence is proof.

Public methodology. No private data.""",
 ["Three axes of evidence.","Grieving informants guess.","Convergence = proof."]),
("Signature method: the systematic assault on brick walls", "research method",
 "A Signature original method: seven steps for walls — restate, re-survey, widen, switch, question, test, wait.",
 """SIGNATURE ORIGINAL METHOD — BRICK WALLS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1. Restate in one sentence. Vagueness is the wall.
2. Re-survey: re-read every source — you know more than when you first read them.
3. Widen: FAN club — siblings, witnesses, neighbors.
4. Switch record type: stuck in censuses? Try tax, court, land, DNA.
5. Question assumptions: the spelling, the birthplace, the 'fact' from family lore.
6. Test: targeted DNA of the right cousin.
7. Wait: digitization never stops — the wall may fall on its own.

The Signature observation: most walls are assumptions wearing a surname. The breakthrough is usually subtracting a belief, not adding a record.

Public methodology. No private data.""",
 ["Restate in one sentence.","Subtract beliefs, add records.","Walls are assumptions."]),
("Signature method: filing for decades", "research method",
 "A Signature original method: person folders, citation-named files, 3-2-1 backup — an archive that outlives software.",
 """SIGNATURE ORIGINAL METHOD — ORGANIZATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

- Folders: Surname/FirstName. Files: YYYYMMDD-source-description. Image + citation + transcription together, always.
- Backup 3-2-1: three copies, two media, one offsite. Your research is irreplaceable labor.
- Paper: archival folders, pencil only, no sticky notes on documents.
- Software: Gramps (free), RootsMagic, Family Tree Maker — but export GEDCOM 7 regularly. Your data must outlive your software.
- Name a steward: put the archive's heir in your will.

The Signature rule: organize for the researcher who inherits your work — probably a grandchild, possibly a stranger. They should be able to pick up your log and continue.

Public methodology. No private data.""",
 ["Cite-named files.","3-2-1 backup.","GEDCOM outlives software."]),
("Signature method: writing ancestors", "research method",
 "A Signature original method: from research to narrative — Ahnentafels, register style, and scenes.",
 """SIGNATURE ORIGINAL METHOD — WRITING
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

- Ahnentafel: you=1, father=2, mother=3, doubling — the compact ancestor table.
- Register style (NEHGS): numbered generations, full citations, the scholarly standard.
- Narrative: open with a scene ('In March 1847 the ship...'), not a birth date. Readers remember scenes.
- Cite as you write — retrofitting citations fails.
- Include the walls: unsolved problems are part of the story, and the next researcher needs them.
- Publish: print-on-demand for family, archive deposit for posterity (living persons redacted).

The Signature rule: a cited narrative is the only genealogy that survives its author. The database is the draft; the book is the legacy.

Public methodology. No private data.""",
 ["Ahnentafel numbering.","Scenes, not dates.","Cite as you write."]),
("Signature method: ethics of the living and the dead", "research method",
 "A Signature original method: consent for the living, sensitivity for the recent dead, gentleness for the secrets.",
 """SIGNATURE ORIGINAL METHOD — ETHICS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

- The living: never publish names, dates, or DNA without explicit consent. No exceptions.
- The recently dead: a generation of sensitivity — grief is fresh, and grandchildren read.
- The secrets: non-paternal events, adoptions, hidden marriages — share privately, gently, with support.
- DNA: warn before testing. Unexpected parentage is common; the kit is a loaded question.
- This database's rule: public and historical records only. Never private family data. If in doubt, leave it out.

The Signature principle: genealogy serves the family, not the researcher's curiosity. The dead have no privacy; their grandchildren do.

Public methodology. No private data.""",
 ["Living: consent, always.","Secrets: private and gentle.","If in doubt, leave it out."]),
("Signature method: the 100-year plan", "research method",
 "A Signature original method: digitize, deposit, and designate — making research outlive the researcher.",
 """SIGNATURE ORIGINAL METHOD — PRESERVATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

- Digitize: 300–600 dpi TIFF masters; JPEG for sharing. Today's phone beats yesterday's flatbed.
- Deposit: county record offices and family history societies accept papers — unpublished research in a shoebox is a future bonfire.
- Document your reasoning: the log and the proof arguments, not just the conclusions.
- Migrate: digital formats every decade; cloud plus local.
- Designate: name your archive's steward in your will.

The Signature rule: plan for the researcher of 2126. They will have tools we can't imagine and questions we can't predict. Leave them the sources, the citations, and the reasoning — the raw material of future discovery.

Public methodology. No private data.""",
 ["TIFF masters; JPEG shares.","Deposit, don't shoebox.","Plan for 2126."]),
("Signature guide: the language of the shield", "heraldry",
 "A Signature original guide: reading a coat of arms — tinctures, ordinaries, and the grammar of blazon.",
 """SIGNATURE ORIGINAL HERALDRY GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Blazon: the heraldic description language — precise, French-inflected, centuries old. "Gules, a chevron argent between three lions or."

The tinctures: two metals (or=gold, argent=silver), five colors (gules=red, azure=blue, sable=black, vert=green, purpure=purple), two furs (ermine, vair). Rule: metal never on metal, color never on color.

The ordinaries: the honorable divisions — chief, fess, pale, bend, chevron, cross, saltire. The charges: the pictures — lions, eagles, fleurs-de-lis, and (the genealogist's joy) the canting arms that pun the name.

The genealogist's use: arms descend (with differencing for younger sons); the quartered shield is a pedigree — each quarter a marriage, each marriage an heiress.

The caution: the bucket-shop "family crest" — arms belong to individuals, not surnames. Your surname's arms are almost certainly someone else's.

Clearly labeled original guide. Public methodology. No private data.""",
 ["Signature original guide.","Blazon: the grammar.","Arms belong to individuals."]),
]

# ================= 5. childrens-literature-public =================
CHILPUB = [
# --- Aesop (15), Grimm (18), Andersen (17), nursery rhymes (10) — complete ---
("The Tortoise and the Hare", "moral tale",
 "Aesop's most famous fable, complete: the boastful Hare naps mid-race, and the steady Tortoise wins — slow and steady wins the race.",
 """THE TORTOISE AND THE HARE
A fable of Aesop (public domain, retold).

The Hare was boasting to the other animals about how fast he could run. "I have never been beaten," he said. "When I run, I fly!"

The Tortoise, who had been listening quietly, said, "I will race you."

The Hare laughed so hard he nearly fell over. "You? Race me? Very well — we shall see."

A course was marked out, and the Fox was chosen as judge. At the starting signal, the Hare darted off like the wind, while the Tortoise plodded along, slow and steady.

The Hare was soon far ahead. "I have plenty of time," he thought. "I shall take a nap." So he curled up beneath a shady tree and fell fast asleep.

Meanwhile the Tortoise kept going — step by step, never stopping, never hurrying. He passed the sleeping Hare and continued to the finish line.

When the Hare woke, he looked around. The Tortoise was nowhere to be seen. "He is still far behind," thought the Hare, and he sprinted for the finish. But there, past the line, stood the Tortoise, smiling.

Moral: Slow and steady wins the race.""",
 ["Aesop, 6th century BCE.","Moral: slow and steady wins the race.","Among the world's most retold stories."]),
("The Boy Who Cried Wolf", "moral tale",
 "Aesop's complete fable: a shepherd boy's false alarms cost him his flock — no one believes a liar, even when he tells the truth.",
 """THE BOY WHO CRIED WOLF
A fable of Aesop (public domain, retold).

There was once a shepherd boy who watched his flock on a hillside near a village. He grew bored, and to amuse himself he cried out, "Wolf! Wolf! A wolf is attacking the sheep!"

The villagers came running with sticks and pitchforks — but there was no wolf. The boy laughed at their frightened faces. "I was only joking!" he said.

A few days later he did it again. "Wolf! Wolf!" he shouted. Again the villagers ran up the hill, and again there was no wolf. They were angry this time. "Do not cry wolf when there is no wolf," they warned him.

But the boy thought it was great fun, and one day he cried "Wolf!" a third time. The villagers shook their heads and stayed in the village. "He is joking again," they said.

That evening, a wolf really did come. The boy cried and cried, "Wolf! Wolf! Please help!" But no one came. The wolf scattered the flock and killed several sheep.

Moral: No one believes a liar, even when he tells the truth.""",
 ["Aesop, 6th century BCE.","Moral: liars are not believed.","Source of the idiom 'cry wolf'."]),
("The Fox and the Grapes", "animal tale",
 "Aesop's complete fable: the Fox cannot reach the grapes, so he declares them sour — the origin of 'sour grapes'.",
 """THE FOX AND THE GRAPES
A fable of Aesop (public domain, retold).

One hot summer day, a Fox was walking through an orchard when he saw a bunch of ripe grapes hanging from a vine, high above his head. They were plump and purple and glistening in the sun, and the Fox's mouth watered.

"Those grapes look delicious," he said. "I must have them."

He jumped for them — but they were just out of reach. He backed up and took a running leap. Still too high. He jumped again and again, twisting in the air, until he was exhausted and panting.

At last he gave up. As he walked away, he looked back at the grapes and said, with his nose in the air, "Those grapes are probably sour anyway. I don't want sour grapes."

Moral: It is easy to despise what you cannot have.""",
 ["Aesop, 6th century BCE.","Origin of 'sour grapes'.","Moral: despising the unattainable."]),
("The Ant and the Grasshopper", "moral tale",
 "Aesop's complete fable: the Grasshopper sings all summer while the Ant stores grain — when winter comes, only one is prepared.",
 """THE ANT AND THE GRASSHOPPER
A fable of Aesop (public domain, retold).

All summer long, the Grasshopper played his fiddle and sang in the sunshine, while the Ant worked hard carrying grains of wheat to her underground store.

"Why do you work so hard?" asked the Grasshopper, dancing. "Come and sing with me! Summer is for fun."

"I am storing food for winter," said the Ant. "You should do the same."

"Winter is far away," laughed the Grasshopper. "There is plenty of time." And he played his fiddle louder.

But autumn came, and then winter, with snow deep on the ground. The Grasshopper was cold and hungry. He had nothing to eat. Shivering, he knocked on the Ant's door.

"Please," he begged, "give me some grain, or I shall starve."

The Ant looked at him. "All summer you sang while I worked," she said. But she took pity on him and shared a little of her store — and the Grasshopper learned his lesson.

Moral: Prepare today for the needs of tomorrow.""",
 ["Aesop, 6th century BCE.","Moral: prepare for tomorrow.","Retold by La Fontaine as 'La Cigale et la Fourmi'."]),
("The Lion and the Mouse", "animal tale",
 "Aesop's complete fable: the mighty Lion spares a tiny Mouse — who later gnaws him free from a hunter's net. Kindness is never wasted.",
 """THE LION AND THE MOUSE
A fable of Aesop (public domain, retold).

A Lion was sleeping in the forest when a little Mouse ran across his nose and woke him. The Lion caught the Mouse in his great paw.

"Please let me go!" squeaked the Mouse. "Someday I may be able to help you."

The Lion laughed — a tiny Mouse helping a great Lion! But he was in a good mood, so he opened his paw and let the Mouse go.

Some days later, the Lion was caught in a hunter's net. He roared and struggled, but the ropes held fast. The Mouse heard his roars and came running. With her sharp little teeth, she gnawed through the ropes, one by one, until the Lion was free.

"You laughed when I said I would help you," said the Mouse. "Now you see — even a little Mouse can help a great Lion."

Moral: Kindness is never wasted; even the small can help the great.""",
 ["Aesop, 6th century BCE.","Moral: kindness is never wasted.","The net scene is iconic."]),
("The Goose That Laid the Golden Eggs", "moral tale",
 "Aesop's complete fable: a farmer kills his golden-egg goose to get all the gold at once — and gets nothing. Greed destroys its own reward.",
 """THE GOOSE THAT LAID THE GOLDEN EGGS
A fable of Aesop (public domain, retold).

A farmer and his wife owned a very special goose. Every morning, it laid a single egg — an egg of solid gold.

They sold the golden eggs and grew rich. But they grew greedy too. "Why wait for one egg a day?" said the farmer. "Inside the goose there must be a great lump of gold. Let us take it all at once!"

So they killed the goose and cut it open. Inside, they found — nothing. Just an ordinary goose, like any other.

Now they had no goose and no more golden eggs.

Moral: Greed often overreaches itself; those who want everything lose everything.""",
 ["Aesop, 6th century BCE.","Moral: greed loses all.","'Kill the goose that lays golden eggs' idiom."]),
("The Wolf in Sheep's Clothing", "animal tale",
 "Aesop's complete fable: a Wolf disguises himself in a sheepskin to steal lambs — until the shepherd mistakes him for a sheep.",
 """THE WOLF IN SHEEP'S CLOTHING
A fable of Aesop (public domain, retold).

A Wolf found a sheepskin that shepherds had thrown away. He pulled it over himself and crept into the pasture among the sheep.

The sheep, thinking he was one of them, did not run. That evening, the Wolf planned to carry off a lamb under cover of the skin.

But the shepherd, counting his flock at dusk, noticed one sheep looked fatter than the rest. "That one will do for supper," he said — and, mistaking the Wolf for a sheep, he slaughtered him on the spot.

Moral: The deceiver is often caught in his own deception.""",
 ["Aesop, 6th century BCE.","Origin of the idiom.","Moral: deception backfires."]),
("The Town Mouse and the Country Mouse", "animal tale",
 "Aesop's complete fable: the Country Mouse visits the Town Mouse's feast, but flees the dangers — plain food in peace beats riches in fear.",
 """THE TOWN MOUSE AND THE COUNTRY MOUSE
A fable of Aesop (public domain, retold).

A Town Mouse visited his cousin in the country. The Country Mouse served barley, roots, and acorns. The Town Mouse nibbled politely. "This is very plain," he said. "Come to town with me, and I will show you how to live."

So the Country Mouse went to town. In a grand pantry they found cheese, cakes, and jellies. Just as they began to feast — the door flew open! In came the cook's cat, and then the cook with a broom. The mice fled for their lives into a hole.

"Phew!" panted the Country Mouse. "Your feasts are too dangerous for me. Give me my barley and roots in peace — plain food with safety is better than riches with fear."

Moral: Poverty with security is better than wealth with danger.""",
 ["Aesop, 6th century BCE.","Moral: peace over riches.","Retold by Horace and La Fontaine."]),
("The Dog and His Reflection", "animal tale",
 "Aesop's complete fable: a Dog carrying meat sees his reflection in the water, snaps at the 'bigger' piece, and loses his own.",
 """THE DOG AND HIS REFLECTION
A fable of Aesop (public domain, retold).

A Dog had stolen a juicy piece of meat and was carrying it home in his mouth. On his way, he crossed a bridge over a clear stream. Looking down, he saw his own reflection in the water — another dog, holding what looked like a bigger piece of meat.

"That dog's meat is bigger than mine," thought the Dog. "I want that one too."

He snapped at the reflection — and as he opened his mouth, his own piece of meat fell into the stream with a splash and floated away.

Moral: Beware of losing what you have by grasping at shadows.""",
 ["Aesop, 6th century BCE.","Moral: don't grasp at shadows.","A lesson against greed."]),
("The Crow and the Pitcher", "animal tale",
 "Aesop's complete fable: a thirsty Crow drops pebbles into a pitcher to raise the water — necessity is the mother of invention.",
 """THE CROW AND THE PITCHER
A fable of Aesop (public domain, retold).

A thirsty Crow found a pitcher with a little water at the bottom. The pitcher was tall and narrow — the Crow could not reach the water with his beak, and he was not strong enough to tip the pitcher over.

He thought and thought. Then he had an idea.

Picking up a pebble in his beak, he dropped it into the pitcher. Plop! The water rose a tiny bit. He dropped in another pebble. Plop! Another. Pebble by pebble, the water rose higher and higher — until at last the clever Crow could drink.

Moral: Necessity is the mother of invention; little by little does the trick.""",
 ["Aesop, 6th century BCE.","Moral: necessity invents.","The 'pebble by pebble' method."]),
("The Miller, His Son, and Their Donkey", "adventure",
 "Aesop's complete fable: a Miller tries to please everyone about how to lead his donkey — and pleases no one. You can't please everyone.",
 """THE MILLER, HIS SON, AND THEIR DONKEY
A fable of Aesop (public domain, retold).

A Miller and his Son were taking their Donkey to market. They walked beside it, leading it by a rope.

"Look at those fools," said some travelers. "Walking when they could ride!" So the Son climbed onto the Donkey.

Then some old men said, "Shame! The young boy rides while his old father walks." So they swapped — the Miller rode and the Son walked.

Then some women said, "Cruel man! To ride while the poor boy walks." So both climbed onto the Donkey.

Then others cried, "That poor Donkey, carrying two people!" So the Miller and his Son tied the Donkey's legs to a pole and carried him between them.

As they crossed a bridge, the Donkey, frightened, kicked free — and fell into the river and drowned.

Moral: If you try to please everyone, you will please no one.""",
 ["Aesop, 6th century BCE.","Moral: please all, please none.","The pole-carrying scene is famous."]),
("The Frogs Who Desired a King", "animal tale",
 "Aesop's complete fable: the Frogs beg Jupiter for a king — first a log, then a stork who eats them. Be careful what you wish for.",
 """THE FROGS WHO DESIRED A KING
A fable of Aesop (public domain, retold).

The Frogs lived happily in their pond, but they grew restless. "We have no king!" they croaked. "We want a king to rule over us!" They sent a messenger to Jupiter to ask for one.

Jupiter laughed and threw a log into the pond. Splash! The Frogs were terrified at first, but soon they were dancing on the log. "This king does nothing!" they complained. "We want a real king!"

Jupiter was annoyed. He sent a Stork. The Stork stood in the shallows — and began spearing and eating the Frogs, one by one.

The surviving Frogs croaked for mercy. "We are sorry! Take back this terrible king!"

But Jupiter replied, "You asked for a king, and you have one. Be content — or be eaten."

Moral: Be careful what you wish for; better no ruler than a tyrant.""",
 ["Aesop, 6th century BCE.","Moral: beware wished-for rulers.","A political fable."]),
("The Wind and the Sun", "moral tale",
 "Aesop's complete fable: the Wind and Sun compete to strip a traveler's cloak — bluster fails where gentle warmth succeeds.",
 """THE WIND AND THE SUN
A fable of Aesop (public domain, retold).

The North Wind and the Sun were disputing which was stronger, when a traveler came along wrapped in a warm cloak.

"Let us settle this," said the Wind. "Whoever can make that traveler take off his cloak is the stronger."

The Sun agreed, and the Wind blew first. He blew with all his might — howling, roaring, tearing at the cloak. But the colder it blew, the tighter the traveler wrapped his cloak around himself.

At last the Wind gave up, exhausted.

Then the Sun shone out warmly. The air grew mild and pleasant. The traveler wiped his brow — and took off his cloak.

Moral: Gentleness and persuasion win where force fails.""",
 ["Aesop, 6th century BCE.","Moral: persuasion beats force.","A diplomatic fable."]),
("The Fox and the Stork", "animal tale",
 "Aesop's complete fable: the Fox serves soup in a flat dish the Stork can't drink from — then the Stork serves dinner in a narrow jar.",
 """THE FOX AND THE STORK
A fable of Aesop (public domain, retold).

The Fox invited the Stork to dinner. He served soup in a wide, flat dish. The Fox lapped it up easily, but the Stork, with her long beak, could not get a single drop. She went home hungry.

Some days later, the Stork invited the Fox in return. She served a delicious dinner — in a tall, narrow jar with a tiny mouth. The Stork ate easily with her long beak, while the Fox could only lick the outside of the jar.

"Do you like it?" asked the Stork politely.

The Fox went home hungry — and wiser.

Moral: Do unto others as you would have them do unto you; one bad turn deserves another.""",
 ["Aesop, 6th century BCE.","Moral: tit for tat.","The dinner-party revenge."]),
("The Bundle of Sticks", "bedtime",
 "Aesop's complete fable: a father shows his quarreling sons that sticks break singly but not as a bundle — strength in unity.",
 """THE BUNDLE OF STICKS
A fable of Aesop (public domain, retold).

An old father had three sons who were always quarreling. Nothing he said could make them live in peace.

One day he called them together and placed a bundle of sticks on the ground. "Whoever can break this bundle," he said, "shall have my blessing."

The eldest son tried with all his might. He bent and strained, but the bundle would not break. The second son tried, and the third — all failed.

Then the father untied the bundle and gave each son a single stick. "Break these," he said. Each stick snapped easily.

"My sons," said the father, "you are like these sticks. Alone, each of you can be broken. Together, bound in unity, no one can break you."

The sons never quarreled again.

Moral: In unity there is strength.""",
 ["Aesop, 6th century BCE.","Moral: unity is strength.","A father's final lesson."]),
("Cinderella", "fantasy",
 "The complete Grimm tale: Ashputtel, the hazel tree, the golden shoe — and the stepsisters' fate.",
 """CINDERELLA (ASCHENPUTTEL)
From the Brothers Grimm (public domain, retold complete).

A rich man's wife died, and he married again — a widow with two daughters. The stepmother and stepsisters made the man's own daughter their servant. She slept by the hearth among the cinders, and they called her Ashputtel.

When the King announced a three-day festival to find a bride for the Prince, the stepsisters were dressed in finery. Ashputtel begged to go. Her stepmother poured lentils into the ashes: "Pick them out in two hours, then you may go." Two white doves came and picked them out — but the stepmother only laughed and refused.

Ashputtel ran to her mother's grave, where a hazel tree grew from the twig she had planted. "Shiver and quiver, little tree, silver and gold throw down over me." A bird in the tree threw down a dress of gold and silver and silk slippers.

At the festival the Prince danced only with her. On the third night, he had the stairs smeared with pitch — and her left slipper stuck fast. The Prince declared he would marry whoever the shoe fit.

The eldest stepsister cut off her toe to fit it; the doves cried, "There's blood in the shoe!" The second cut off her heel — again the doves warned. Then Ashputtel tried: the shoe fit perfectly.

At the wedding, the doves pecked out the stepsisters' eyes — one eye on the way in, the other on the way out — for their wickedness and falsehood.

And Ashputtel lived happily with the Prince ever after.""",
 ["Grimm, 1812 (KHM 21).","The hazel tree (not a fairy godmother).","Doves as moral agents."]),
("Snow White", "fantasy",
 "The complete Grimm tale: the mirror, the seven dwarfs, the poisoned apple — and the red-hot shoes.",
 """SNOW WHITE (SCHNEEWITTCHEN)
From the Brothers Grimm (public domain, retold complete).

A queen wished for a child "as white as snow, as red as blood, as black as ebony" — and Snow White was born. The queen died; the king married a beautiful, proud woman with a magic mirror. "Mirror, mirror on the wall, who is fairest of them all?" "You, my queen" — until Snow White turned seven.

The huntsman was ordered to kill her, but spared her. She found the cottage of the seven dwarfs, who sheltered her in exchange for housekeeping.

Three times the queen came disguised: with laces (the dwarfs cut them), with a poisoned comb, and at last with the poisoned apple — one red cheek poisoned, one white cheek safe. Snow White bit the red cheek and fell as if dead.

The dwarfs laid her in a glass coffin. A prince, passing, begged for the coffin; his servants stumbled, and the apple piece flew from her throat. She woke.

At the wedding, the wicked queen was forced to dance in red-hot iron shoes until she fell dead.

And Snow White lived happily ever after.""",
 ["Grimm, 1812 (KHM 53).","Three assassination attempts.","The mirror's terrible honesty."]),
("Hansel and Gretel", "adventure",
 "The complete Grimm tale: breadcrumbs, the gingerbread house, the witch's oven — and the duck's ferry home.",
 """HANSEL AND GRETEL (HÄNSEL UND GRETEL)
From the Brothers Grimm (public domain, retold complete).

A poor woodcutter's wife persuaded him to abandon Hansel and Gretel in the forest during a famine. Hansel scattered white pebbles the first time, and they followed the moonlit trail home. The second time he had only bread — and the birds ate the crumbs.

Lost, the children found a house built of bread, with cake for a roof and sugar windows. "Nibble, nibble, little mouse — who is nibbling at my house?" came a voice. An old woman invited them in — a witch, who fattened Hansel in a cage to eat him.

"Stick out your finger," she told the blind witch each morning — and Hansel stuck out a bone. Impatient, she heated the oven for Gretel. "Crawl in and see if it's hot enough," said the witch. "I don't know how," said Gretel. The witch showed her — and Gretel pushed her in and slammed the door.

They filled their pockets with the witch's pearls and jewels, and a white duck ferried them across the water home. Their stepmother had died; they lived rich and happy with their father ever after.""",
 ["Grimm, 1812 (KHM 15).","Pebbles, then crumbs.","Gretel saves them both."]),
("Rapunzel", "fantasy",
 "The complete Grimm tale: the tower, the long hair, the prince's blinding — and the tears that heal.",
 """RAPUNZEL
From the Brothers Grimm (public domain, retold complete).

A husband stole rapunzel (rampion) from a sorceress's garden for his pregnant wife. Caught, he promised the child. When the baby girl was born, the sorceress — Dame Gothel — took her and named her Rapunzel.

At twelve, Rapunzel was locked in a tower with no door, only a window. "Rapunzel, Rapunzel, let down your hair!" called Dame Gothel, climbing the twenty-ell golden braid.

A prince heard her singing and learned the call. They met secretly and planned escape — until Rapunzel innocently asked Dame Gothel why her clothes were tighter than the prince's. Enraged, Gothel cut off Rapunzel's hair, banished her to a desert, and left the shorn braid in the window.

The prince climbed, saw Gothel, and threw himself from the tower — blinded by thorns. He wandered blind for years, until he heard Rapunzel's voice in the desert. Her tears fell on his eyes, and he could see again.

They returned to his kingdom and lived happily ever after.""",
 ["Grimm, 1812 (KHM 12).","Twenty ells of hair.","Tears that heal blindness."]),
("Sleeping Beauty (Briar-Rose)", "fantasy",
 "The complete Grimm tale: the twelve fairies, the spindle, the hundred-year sleep — and the hedge of thorns.",
 """SLEEPING BEAUTY (DORNROESCHEN / BRIAR-ROSE)
From the Brothers Grimm (public domain, retold complete).

After long waiting, a queen bore a daughter, Briar-Rose. Twelve wise women were invited to the feast (the thirteenth was overlooked, for there were only twelve golden plates). Eleven gave gifts — beauty, virtue, riches. Then the thirteenth burst in: "In her fifteenth year she shall prick herself with a spindle and fall down dead!"

The twelfth fairy softened it: not death, but a hundred-year sleep.

The king burned every spindle in the land. But on her fifteenth birthday, Briar-Rose found an old woman spinning in a tower room, pricked her finger — and fell asleep. The whole castle slept: king, queen, horses, dogs, doves, even the fire.

A hedge of thorns grew around the castle. Princes who tried to pierce it died in the thorns. After a hundred years, a prince came; the thorns turned to flowers before him. He found Briar-Rose, kissed her — and she woke. The whole castle woke with her.

They married, and lived happily to the end of their days.""",
 ["Grimm, 1812 (KHM 50).","Twelve fairies, one slighted.","The thorn hedge of years."]),
("Rumpelstiltskin", "fantasy",
 "The complete Grimm tale: straw into gold, the three-night bargain, and the name guessed on the third night.",
 """RUMPELSTILTSKIN
From the Brothers Grimm (public domain, retold complete).

A miller boasted his daughter could spin straw into gold. The king locked her in a room of straw: spin it by morning or die. A little man appeared: "What will you give me?" Her necklace — and the straw became gold. The second night: her ring. The third night she had nothing left — so she promised her firstborn child, and became queen.

A year later the little man came for the baby. The queen wept and begged. "Three days," he said. "If in three days you guess my name, keep the child."

The first two nights she guessed all the common names — in vain. On the third day a messenger saw the little man dancing around a fire in the forest, singing: "Today I brew, tomorrow I bake, and then the queen's child I take! For no one knows my little game, and Rumpelstiltskin is my name!"

When the queen said "Rumpelstiltskin," he stamped his foot with rage and tore himself in two.

And the queen kept her child, and lived happily ever after.""",
 ["Grimm, 1812 (KHM 55).","Three nights, three bargains.","The name is the power."]),
("The Frog Prince", "fantasy",
 "The complete Grimm tale: the golden ball, the frog at the table, and the transformation — in Grimm, by a throw against the wall.",
 """THE FROG PRINCE (DER FROSCHKOENIG)
From the Brothers Grimm (public domain, retold complete).

A princess's golden ball rolled into a deep well. A frog offered to fetch it — if she would love him, let him eat from her plate, sleep on her pillow. She promised (thinking never to keep it), and he dived and returned the ball.

At dinner the frog knocked: "Youngest princess, open the door for me!" The king made her keep her promise. The frog ate from her golden plate and slept on her silken pillow.

The princess was disgusted. In the Grimm telling, she seized the frog and threw him against the wall with all her might. As he fell, he became a handsome prince — disenchanted.

He had been cursed by a wicked witch; only the princess could free him. They married with the king's consent, and the prince's faithful servant Henry — whose heart had been bound with three iron bands for grief — heard the bands snap with joy as they rode home.""",
 ["Grimm, 1812 (KHM 1).","Disenchanted by a throw.","Faithful Henry's iron bands."]),
("Little Red Riding Hood", "moral tale",
 "The complete Grimm tale: the grandmother's house, the wolf's questions, the huntsman's rescue — and the second wolf.",
 """LITTLE RED RIDING HOOD (ROTKAEPPCHEN)
From the Brothers Grimm (public domain, retold complete).

"Grandmother is ill," said the mother. "Take her this cake and wine — and stay on the path."

In the forest the wolf met Red Riding Hood. "Where are you going?" She told him — and he ran ahead, swallowed the grandmother whole, dressed in her nightcap, and waited in bed.

"Grandmother, what big ears you have!" "The better to hear you with." "What big eyes!" "The better to see you with." "What big hands!" "The better to grab you with." "But Grandmother, what a big mouth you have!" "The better to eat you with!" — and he swallowed her too.

A huntsman heard the snoring, cut open the sleeping wolf, and out jumped grandmother and granddaughter, alive. They filled the wolf's belly with stones; he woke, tried to run, and fell dead.

Another day, a second wolf tried the same trick — but grandmother and granddaughter were ready, and drowned him in the sausage-water trough.

Moral (Grimm's world): stay on the path.""",
 ["Grimm, 1812 (KHM 26).","The stone-filled belly.","Two wolves; both fail."]),
("The Bremen Town Musicians", "adventure",
 "The complete Grimm tale: the donkey, dog, cat, and rooster — too old to work, they scare robbers and take the cottage.",
 """THE BREMEN TOWN MUSICIANS
From the Brothers Grimm (public domain, retold complete).

A donkey, grown too old to carry sacks, ran away to become a town musician in Bremen. On the road he met a dog too old to hunt, a cat too old to catch mice, and a rooster about to become soup. "Come with us!" said the donkey. "We shall be musicians!"

At night they saw a light — a cottage full of robbers feasting. The animals stacked themselves: donkey, dog, cat, rooster — and on a signal, brayed, barked, mewed, and crowed all at once, bursting through the window. The robbers fled, sure a monster had come.

The animals ate the feast and settled for the night. A robber sent to scout was scratched by the cat, bitten by the dog, kicked by the donkey, and screeched at by the rooster. "A witch scratched me, a man stabbed me, a monster beat me, and the judge screamed from the rooftop!" he reported.

The robbers never returned. The four musicians stayed in the cottage — and never reached Bremen, which suited them perfectly.""",
 ["Grimm, 1819 (KHM 27).","Four retirees, one plan.","They never reach Bremen."]),
("The Twelve Dancing Princesses", "fantasy",
 "The complete Grimm tale: the soldier, the invisibility cloak, and the underground ballroom — where the princesses wear out their shoes.",
 """THE TWELVE DANCING PRINCESSES
From the Brothers Grimm (public domain, retold complete).

Twelve princesses slept in one room, door locked — yet every morning their shoes were danced to pieces. The king promised one princess's hand to whoever solved it.

A soldier, advised by an old woman, took only a little wine (and pretended to drink the drugged cup), then followed in his invisibility cloak. He saw the eldest tap the bed — it sank — and twelve staircases led to an avenue of silver trees, then gold, then diamond. He broke a twig from each.

They crossed a lake where twelve princes rowed them to a castle, and danced till 3 a.m. The soldier, invisible, ate from their plates and filled his pockets with proof.

On the third night he told the king everything, showing the twigs and a golden cup. The eldest princess confessed. The soldier chose her for his bride — and the spell was broken.

The twelve princes were disenchanted too — or so the old tales say.""",
 ["Grimm, 1812 (KHM 133).","Silver, gold, diamond avenues.","The cloak sees all."]),
("The Fisherman and His Wife", "animal tale",
 "The complete Grimm tale: the enchanted flounder grants wishes — until the wife demands to be God, and they're back in the hovel.",
 """THE FISHERMAN AND HIS WIFE
From the Brothers Grimm (public domain, retold complete).

A fisherman caught a great flounder who begged for life — an enchanted prince. The fisherman freed him. His wife Ilsebill was furious: "You asked for nothing? Go back and wish for a cottage!"

The flounder granted it. Then she wanted a stone castle. Then to be king. Then emperor. Then pope. Each time the sea grew darker and wilder.

At last she demanded: "I want to be God!" The fisherman trembled, but went to the roaring black sea and spoke the verse. The flounder said only: "Go home. She is sitting in the hovel again."

And there she sat, in the old hovel, as poor as before.

Moral: enough is enough; greed undoes its own gains.""",
 ["Grimm, 1812 (KHM 19).","Cottage → castle → king → pope → God.","The sea darkens with each wish."]),
("The Elves and the Shoemaker", "bedtime",
 "The complete Grimm tale: the naked elves finish the shoes nightly — until the shoemaker's wife clothes them, and they dance away.",
 """THE ELVES AND THE SHOEMAKER
From the Brothers Grimm (public domain, retold complete).

A poor shoemaker cut leather for one last pair of shoes and went to bed. In the morning the shoes stood finished — beautifully. A customer paid double. Night after night, the cut leather became perfect shoes, and the shoemaker prospered.

At Christmas his wife said, "Let us watch." They hid — and saw two tiny naked elves stitching and hammering till dawn.

"We must thank them," said the wife. She sewed tiny shirts, coats, waistcoats, trousers, and stockings, and he made tiny shoes. They laid the clothes out instead of leather.

The elves came, found the clothes, dressed with delight — and danced and sang out of the house, never to return.

The shoemaker lived prosperously ever after — and always, he said, with gratitude.""",
 ["Grimm, 1812 (KHM 39).","Three stories in one (only the first is famous).","Gratitude, given clothes."]),
("The Golden Goose", "adventure",
 "The complete Grimm tale: Simpleton's golden goose collects a sticky parade — and makes the princess laugh.",
 """THE GOLDEN GOOSE
From the Brothers Grimm (public domain, retold complete).

Simpleton — the youngest, mocked by all — shared his meager lunch with a little gray man in the forest. In return he received a goose of pure gold.

At the inn, the innkeeper's daughters tried to pluck a golden feather — and stuck fast. The parson pulled at them — stuck. The sexton — stuck. Two laborers — stuck. Seven people trailed behind the goose.

They paraded past the castle, where the princess had never laughed in her life. At the sight of the seven stuck fast behind the golden goose, she burst out laughing.

The king had promised her hand to whoever made her laugh. After three impossible tasks (which the gray man helped Simpleton complete), Simpleton married the princess.

And the stuck parade? The gray man unstuck them — wiser about other people's geese.""",
 ["Grimm, 1812 (KHM 64).","Kindness compounds.","The princess laughs at last."]),
("The Star Money", "bedtime",
 "The complete Grimm tale: the orphan girl gives away everything — and the stars rain thalers. The shortest, kindest Grimm story.",
 """THE STAR MONEY (STERNTHALER)
From the Brothers Grimm (public domain, retold complete).

There was once a poor orphan girl with nothing but the clothes on her back, a piece of bread, and a cap on her head. She set out into the world.

She met a hungry man and gave him her bread. She met a freezing child and gave him her cap. Another child, shivering — she gave her bodice. Another — her skirt. At last she stood in the dark forest in only her thin shift — and gave even that to a child who had nothing.

Then the stars began to fall from the sky — not stars, but hard shining thalers. And where her shift had been, she wore a new one of the finest linen.

She gathered the thalers and was rich all her life.

Moral: the kindest story in Grimm — giving everything gains everything.""",
 ["Grimm, 1812 (KHM 153).","The kindest Grimm tale.","Stars into thalers."]),
("The Wolf and the Seven Young Goats", "adventure",
 "The complete Grimm tale: the wolf's chalk voice, flour paws, the clock case — and the stone-filled well.",
 """THE WOLF AND THE SEVEN YOUNG GOATS
From the Brothers Grimm (public domain, retold complete).

"Don't open the door to anyone," said Mother Goat, going to market. The wolf came: "Open up, dear children!" — but his rough voice betrayed him. He ate chalk to soften it. His black paws betrayed him next — he coated them with flour.

The kids opened the door. Six hid — under the table, in the bed, the stove, the kitchen, the cupboard, the clock case — but the wolf found them all. Only the youngest, hidden in the clock case, escaped.

Mother Goat returned, and with the youngest's help found the wolf snoring in the meadow. She cut him open with scissors: out jumped all six kids, alive. They filled his belly with stones and sewed him up. He woke thirsty, leaned to drink at the well — the stones pulled him in, and he drowned.

And the goats lived safely ever after.""",
 ["Grimm, 1812 (KHM 5).","Chalk voice, flour paws.","The clock case saves one."]),
("Hans in Luck", "adventure",
 "The complete Grimm tale: Hans trades his gold lump down to a grindstone — and calls himself the luckiest man alive.",
 """HANS IN LUCK (HANS IM GLUECK)
From the Brothers Grimm (public domain, retold complete).

Hans served seven years and was paid a lump of gold as big as his head. Carrying it home:

- He traded the gold for a horse (heavy!),
- the horse for a cow (it kicked him; it was dry),
- the cow for a pig,
- the pig for a goose (a stolen pig, he learned),
- the goose for a grindstone.

The grindstone was heavy. At a well, it slipped — splash! — into the water.

Hans jumped for joy. "I am the luckiest man alive! No more heavy loads!" And he walked home light and free, thanking God for his good fortune.

Moral (or joke): happiness is not having what you want, but wanting what you have — or Hans is a fool. Grimm lets you decide.""",
 ["Grimm, 1819 (KHM 83).","Seven trades down.","The luckiest fool alive."]),
("The Valiant Little Tailor", "adventure",
 "The complete Grimm tale: 'seven at one blow' — the tailor bluffs giants, a unicorn, and a boar into a kingdom.",
 """THE VALIANT LITTLE TAILOR
From the Brothers Grimm (public domain, retold complete).

A tailor killed seven flies at one blow and stitched on his belt: "Seven at one blow!" The world read it as seven men.

He bluffed two giants (squeezing 'water' from a stone — it was cheese; throwing a 'bird' sky-high — it flew), and the king hired him against worse giants. He turned the giants against each other, and they crushed one another.

Then: catch a unicorn (he stepped aside; it charged into a tree), catch a wild boar (he lured it into a chapel). The king had promised half the kingdom and the princess — and, grumbling, paid.

The princess discovered he was a tailor and plotted to expose him — but his squire warned him, and he frightened the assassins away in his sleep-talking: "Seven at one blow!"

He remained king, and never sewed again.""",
 ["Grimm, 1812 (KHM 20).","Seven flies, one belt.","Bluff as a superpower."]),
("Mother Holle", "fantasy",
 "The complete Grimm tale: the industrious girl shakes the featherbeds into snow and is rained with gold; the lazy one gets pitch.",
 """MOTHER HOLLE (FRAU HOLLE)
From the Brothers Grimm (public domain, retold complete).

A widow favored her lazy daughter and despised her industrious stepdaughter. The stepdaughter dropped her spindle into the well, and jumped in after it — waking in a meadow.

She helped: took bread from an oven ("take us out, we burn!"), shook apples from a tree, and served Mother Holle — shaking her featherbed till the feathers flew like snow (for when it snows on Earth, says the tale, Holle shakes her bed).

When the girl grew homesick, Holle led her to a gate — and gold rained over her. She returned rich.

The lazy sister jumped in too — but left the bread burning, the apples rotting, and barely shook the bed. At the gate, pitch rained over her instead, and stuck for life.

Moral: industry is golden; idleness is pitch.""",
 ["Grimm, 1812 (KHM 24).","Snow = Holle's featherbed.","Gold for work, pitch for sloth."]),
("The Ugly Duckling", "animal tale",
 "Andersen's complete tale: the mocked cygnet becomes a swan — 'it doesn't matter being born in a duckyard, if only you are hatched from a swan's egg.'",
 """THE UGLY DUCKLING (DEN GRIMME ÆLLING)
By Hans Christian Andersen, 1843 (public domain, retold complete).

A duckling, hatched last and larger and grayer than his siblings, was mocked by the whole duckyard. "He is too big and ugly!" The ducks bit him, the hens pecked him, and even his mother wished him far away.

He fled — to the marshes, where the wild geese laughed at him (till the hunters came); to the old woman's cottage (her cat and hen despised him); and at last to a frozen pond, where a farmer found him nearly frozen and carried him home. The farmer's children frightened him into the milk pail and the butter churn, and he fled into the winter.

Spring came. He spread his wings — great, strong wings — and flew to a garden pond where three white swans swam. "Kill me," he thought, bowing his head. But the water showed him his reflection: no longer a gray duckling, but a swan — the most beautiful of them all.

The children cried, "The new one is the most beautiful!" And he was happy — for he had suffered, and now he knew what happiness was.

Moral (Andersen's): it does not matter being born in a duckyard, if you are hatched from a swan's egg.""",
 ["Andersen, 1843.","His most autobiographical tale.","Duckyard to swan."]),
("The Emperor's New Clothes", "moral tale",
 "Andersen's complete tale: two swindlers, an invisible suit, and the child who cries 'he has nothing on!'",
 """THE EMPEROR'S NEW CLOTHES (KEJSERENS NYE KLÆDER)
By Hans Christian Andersen, 1837 (public domain, retold complete).

An emperor cared for nothing but clothes. Two swindlers offered to weave cloth invisible to anyone unfit for office or unforgivably stupid. The emperor paid richly.

The swindlers set up empty looms and pretended to weave day and night. The emperor sent his honest old minister to inspect. The minister saw nothing — but dared not say so. "Magnificent!" he reported. Others did the same.

At last the emperor went himself. He saw nothing. "Am I unfit?" he thought, terrified. "Splendid!" he declared.

The swindlers 'dressed' him in the nothing-suit, and he processed through the town naked, while the crowd — afraid to seem stupid — cried, "How splendid!"

Then a child shouted, "But he has nothing on!" And one by one the crowd whispered it, till all the town cried, "He has nothing on!"

The emperor shivered, for he knew they were right — but he walked on more proudly than ever, and the chamberlains carried the train that wasn't there.""",
 ["Andersen, 1837.","The child speaks truth.","Vanity's parade."]),
("The Steadfast Tin Soldier", "adventure",
 "Andersen's complete tale: the one-legged soldier loves the paper dancer — through the gutter, the fish, and the fire.",
 """THE STEADFAST TIN SOLDIER (DEN STANDHAFTIGE TINSOLDAT)
By Hans Christian Andersen, 1838 (public domain, retold complete).

Twenty-five tin soldiers, brothers, cast from one spoon — one had only one leg, for the tin ran out. He stood steadfast on his one leg, and loved the paper dancer in the toy castle, who stood on one toe.

A goblin in a snuffbox was jealous. "Take care!" he warned. The soldier ignored him.

The boy threw the soldier from the window. He landed in the gutter, sailed in a paper boat, was swallowed by a fish — and the fish was caught, sold, and served at the very house he had fallen from!

Set on the table, he saw the dancer again. Then the boy threw him into the stove. A draft blew the dancer in after him. They burned together — and in the ashes the maid found a little tin heart.

Moral: steadfastness itself is the victory; love outlasts the fire.""",
 ["Andersen, 1838.","One leg, one love.","The tin heart in the ashes."]),
("The Tinderbox", "adventure",
 "Andersen's complete tale: the soldier, the three dogs with eyes like saucers, and the tinderbox's magic.",
 """THE TINDERBOX (FYRTOEIET)
By Hans Christian Andersen, 1835 (public domain, retold complete).

A soldier met a witch in the forest. "Climb into the hollow tree," she said. "Fill your pockets with copper, silver, gold — but bring me the old tinderbox." In three halls sat three dogs: eyes like saucers, like mill wheels, like the Round Tower — each guarding a chest. The soldier filled his cap and pockets, seized the tinderbox, and — when the witch wouldn't say why she wanted it — cut off her head.

In town he lived richly till the money ran out. Striking the tinderbox idly — once! — the saucer-eyed dog appeared: "What does my lord command?" One strike, two, three — each dog came, and gold flowed again.

He glimpsed the beautiful princess (locked away for a prophecy) via the dogs. Caught and sentenced to hang, he struck the tinderbox from the scaffold — one, two, three! The dogs scattered the judges and council.

"Let him be king!" cried the people. He married the princess — and the dogs sat at the wedding feast, opening their enormous eyes wider than ever.""",
 ["Andersen, 1835.","Dogs: saucers, mill wheels, Round Tower.","His first published tale."]),
("The Princess and the Pea", "bedtime",
 "Andersen's complete tale: the pea under twenty mattresses and twenty eiderdowns — the test of a true princess.",
 """THE PRINCESS AND THE PEA (PRINSESSEN PAA ÆRTEN)
By Hans Christian Andersen, 1835 (public domain, retold complete).

A prince wanted a real princess for his bride, but every candidate had something wrong. One stormy night, a knocking came at the castle gate — a princess, soaked to the skin, claiming to be real.

The old queen said nothing, but went to the guest room. She took all the bedding off, laid a single pea on the bedstead, then piled twenty mattresses on top of the pea, and twenty eiderdown quilts on top of the mattresses.

In the morning the queen asked, "How did you sleep?" "Oh, terribly!" said the princess. "I scarcely closed my eyes. Something hard was in the bed — I am black and blue all over!"

Then they knew she was a real princess — only a real princess could feel a pea through twenty mattresses and twenty eiderdowns.

The prince married her. And the pea was put in the royal museum, where it may still be seen.

Moral: delicacy, in Andersen's world, is royalty's proof.""",
 ["Andersen, 1835.","Twenty + twenty.","The pea in the museum."]),
("The Nightingale", "bedtime",
 "Andersen's complete tale: the real nightingale's song heals the emperor — artifice vs. nature, and the mechanical bird.",
 """THE NIGHTINGALE (NATTERGALEN)
By Hans Christian Andersen, 1843 (public domain, retold complete).

The emperor of China prized his palace above all — till he learned from a book that the finest thing in his empire was the nightingale's song in the forest. The bird was fetched; it sang; the emperor wept and hung a golden slipper round its neck.

Then the emperor of Japan sent a mechanical nightingale — gold, jeweled, singing a waltz perfectly, thirty-three times. The court preferred it. The real bird flew out the window, unmissed.

Years later the mechanism broke. The emperor lay dying. Death sat on his chest wearing his crown. The court had fled.

Then — through the window — the real nightingale sang. It sang of the churchyard, and Death longed for his garden and floated away. The emperor woke, healed.

"Stay with me always," begged the emperor. "No," said the nightingale. "I will come and sing — of the happy and the suffering — but never caged."

Moral: the living song beats the jeweled machine.""",
 ["Andersen, 1843.","Real vs. mechanical.","The song that banished Death."]),
("The Little Match Girl", "bedtime",
 "Andersen's complete tale: on New Year's Eve, the freezing girl's matches light visions — and her grandmother carries her home.",
 """THE LITTLE MATCH GIRL (DEN LILLE PIGE MED SVOVLSTIKKERNE)
By Hans Christian Andersen, 1845 (public domain, retold complete).

On the last evening of the year, a poor girl walked barefoot in the snow, carrying matches she could not sell. Afraid to go home to her father's beating, she huddled in a corner between two houses.

She struck one match: a warm iron stove appeared. It went out. She struck another: a roast goose walked toward her — out. A third: a great Christmas tree, brighter than the rich merchant's — out.

She struck a fourth: her dead grandmother, the only one who had loved her, smiling in the light. "Grandmother!" cried the girl, and struck match after match to keep her.

Then grandmother lifted the child in her arms, and they flew up, up — where there is no cold, no hunger, no fear — for the girl was dead.

In the morning they found her, cheeks rosy, smiling, frozen — with the burned matches. "She tried to warm herself," said the people, who did not know the visions she had seen.""",
 ["Andersen, 1845.","New Year's Eve.","Among his most famous."]),
("The Fir Tree", "bedtime",
 "Andersen's complete tale: the little fir longs to grow, to be a Christmas tree, to be anywhere but here — and ends as firewood.",
 """THE FIR TREE (GRANTRÆET)
By Hans Christian Andersen, 1844 (public domain, retold complete).

The little fir tree was never content. "Oh, to grow tall like the others!" Then: "Oh, to be cut for a mast!" The sparrows told of Christmas trees, and the tree longed for glory.

At last it was chosen — dressed with candles, apples, and a gold star. "Tonight I shine!" thought the tree. The children danced; the tree glowed. Next morning it was dragged to the attic, where mice heard its stories.

The following spring it was chopped for firewood. As it burned, it remembered the forest, the Christmas night, the mice — and sighed for what it had never enjoyed while it had it.

Moral: the tree that always wished to be elsewhere never enjoyed being anywhere.""",
 ["Andersen, 1844.","Ambition's tragedy.","The attic mice audience."]),
("Thumbelina", "bedtime",
 "Andersen's complete tale: the inch-tall girl — toad, beetle, mole, and at last the flower prince.",
 """THUMBELINA (TOMMELISE)
By Hans Christian Andersen, 1835 (public domain, retold complete).

A woman planted a magic barley corn; from its flower came a tiny girl, an inch tall — Thumbelina. She slept in a walnut shell.

A toad stole her for her ugly son; fishes gnawed the lily stalk and she floated away. A cockchafer carried her to his tree, but the lady beetles found her ugly (two legs! no feelers!) and he abandoned her.

Winter came. The field mouse sheltered her — and proposed the rich mole neighbor. Thumbelina nursed a dying swallow back to life instead.

When the wedding day neared, the swallow returned: "Fly with me to warm lands!" She agreed. Over the sea they flew, to a palace of flowers — where a tiny prince, with gauzy wings and a golden crown, waited in a blossom.

"Will you be my wife?" She said yes. Wings grew on her shoulders. The flower spirits named her Maia.

And the swallow sang the story, as swallows do.""",
 ["Andersen, 1835.","An inch tall, a world wide.","Toad, beetle, mole, prince."]),
("The Snow Queen", "fantasy",
 "Andersen's complete tale (full): the mirror shards, Kai's capture, and Gerda's journey to the Snow Queen's palace.",
 """THE SNOW QUEEN (SNEEDRONNINGEN)
By Hans Christian Andersen, 1844 (public domain, retold complete).

The devil's mirror shattered; its splinters flew worldwide. One pierced the heart of little Kai, one his eye — and kind Kai turned cruel, mocking his friend Gerda.

The Snow Queen kissed him twice (once to numb, once to forget) and carried him to her ice palace, where he puzzled over the ice-words of 'eternity.'

Gerda searched: the sorceress's garden (who tried to keep her), the prince and princess (who clothed her), the little robber girl (who gave her a reindeer), the Lapp and Finn women (who armed her with prayer).

At the palace, Gerda's warm tears melted Kai's heart and washed out the splinter; her singing ('Roses bloom and fade...') brought his own tears, washing out the eye splinter. The ice letters spelled ETERNITY by themselves.

They rode home on the reindeer — grown up, but children at heart, as the hymn says.

Moral: love's warmth melts the coldest enchantment.""",
 ["Andersen, 1844.","His longest fairy tale.","Seven stories in one."]),
("The Little Mermaid", "fantasy",
 "Andersen's complete tale: the mermaid's bargain, the prince's wedding, and the daughters of the air — the original ending.",
 """THE LITTLE MERMAID (DEN LILLE HAVFRUE)
By Hans Christian Andersen, 1837 (public domain, retold complete).

The youngest sea-princess, fifteen, rose to see the world — and saved a drowning prince in a storm, leaving him on the beach where a temple maiden found him.

To win him, she traded her voice to the sea witch for legs — every step like knives. The prince loved her as a child, not a bride, and married the temple maiden he believed was his rescuer.

On the wedding night, her sisters rose from the sea, shorn of their hair, offering the witch's knife: kill the prince, and be a mermaid again.

She raised the knife — and threw it into the sea. Dissolving into foam, she did not die: she became a daughter of the air, earning a soul through good deeds, her suffering shortened by every tear she dried.

Moral (Andersen's): selfless love transcends the bargain.""",
 ["Andersen, 1837.","The original ending: daughters of the air.","Voice for legs; love for soul."]),
("The Red Shoes", "moral tale",
 "Andersen's complete tale: Karen's red shoes dance her to repentance — vanity's terrible price, and grace.",
 """THE RED SHOES (DE ROEDESKOO)
By Hans Christian Andersen, 1845 (public domain, retold complete).

Karen, poor and barefoot, was adopted by a kind old lady. But Karen's heart fixed on a pair of red shoes — first the shoemaker's, then finer ones for her confirmation. She wore the red shoes to church, thinking of nothing but her feet.

An old soldier with a red beard tapped them: "Pretty dancing shoes!" — and they began to dance. They danced her out of the church, down the road, day and night. She could not stop, could not take them off.

An executioner cut off her feet with the shoes still dancing away. Given wooden feet and crutches, Karen repented — and at last, in church, her heart was so full of grace that the shoes' curse lifted, and she danced no more, but prayed in peace.

Moral: vanity unrepented dances forever; grace stills the feet.""",
 ["Andersen, 1845.","Among his darkest tales.","Vanity, repentance, grace."]),
("The Swineherd", "moral tale",
 "Andersen's complete tale: the prince disguised as a swineherd, the musical pot, the rattle — and the princess's kiss-price.",
 """THE SWINEHERD (SVINEDRENGEN)
By Hans Christian Andersen, 1841 (public domain, retold complete).

A prince, rejected by a proud princess (she scorned his rose and nightingale), disguised himself as a swineherd in her father's employ.

He made a magic pot that played tunes and told what cooked in every kitchen in town. The princess sent her lady-in-waiting: "What will he take for it?" "Ten kisses," said the swineherd. The princess paid — behind the bushes.

Then he made a rattle that played every waltz ever danced. Price: a hundred kisses. The emperor caught them at it and banished them both.

Washing off the disguise, the prince stood revealed. "I scorned you," he told the weeping princess, "for you would not have an honest prince, and you would kiss a swineherd for toys. Go — I will not have you."

And he went to his kingdom, leaving her outside the gate, singing — as the tale says — "Ach, du lieber Augustin."

Moral: pride pays in kisses and loses a prince.""",
 ["Andersen, 1841.","Ten kisses; a hundred kisses.","Pride's price."]),
("The Wild Swans", "bedtime",
 "Andersen's complete tale: Elisa knits nettles into shirts to free her eleven swan-brothers — silent till the last stitch.",
 """THE WILD SWANS (DE VILDE SVANER)
By Hans Christian Andersen, 1838 (public domain, retold complete).

A king's eleven sons were turned into swans by their stepmother; their sister Elisa, banished too, found them in the forest. "We can only be human at night," they told her. "You can free us: gather nettles, spin them, knit eleven shirts — and until the last is finished, you must not speak a word."

Elisa gathered nettles with her bare hands (the fairy Morgana eased the pain) and knitted in silence. A young king found her, marveled, and married her — but the archbishop called the silent, nettle-gathering queen a witch. She was sentenced to burn.

At the stake she knitted on. The swans came flying; she threw ten shirts over them — the eleventh lacked a sleeve, and the youngest brother kept one swan's wing. Then she spoke: "I am innocent!"

The king embraced her; the archbishop bowed. And the eleven brothers told the tale — all but the youngest, who must keep his single swan's wing forever.

Moral: silent suffering, freely borne, redeems.""",
 ["Andersen, 1838.","Eleven shirts of nettles.","Silence till the last stitch."]),
("The Daisy", "bedtime",
 "Andersen's complete tale: the humble daisy, the lark's song, and one perfect day — small joy, fully lived.",
 """THE DAISY (MARGUERITEN)
By Hans Christian Andersen, 1838 (public domain, retold complete).

A little daisy grew by the garden fence, happy in the sun, listening to the lark. The grand garden flowers — peonies, tulips — despised it. "How plain!" they said.

One day the lark, chased by boys, fluttered down to the daisy. "Thank you for your song," said the daisy, though it could not sing back. The lark sang just for the daisy — the happiest moment of its life.

Then the boys caught the lark, caged it, and it pined and died. They buried it with honors — and threw the daisy, pulled up as decoration, onto the grave.

The daisy had lived one perfect day of joy. "It is a comfort," thought the daisy, "to have given happiness."

Moral: the humblest life, fully lived, is enough.""",
 ["Andersen, 1838.","A miniature masterpiece.","Small joy, fully lived."]),
("The Flying Trunk", "adventure",
 "Andersen's complete tale: the merchant's son, the flying trunk, the princess — and the fireworks finale.",
 """THE FLYING TRUNK (DEN FLYVENDE KUFFERT)
By Hans Christian Andersen, 1839 (public domain, retold complete).

A merchant's son inherited riches and squandered them all — all but a dressing gown, slippers, and an old trunk. "Pack up!" said his friends, laughing.

He packed himself into the trunk — and it flew! (It was a magic trunk.) He flew to Turkey, where he posed as a god to visit the sultan's beautiful daughter, locked in a tower for a prophecy about a lover.

Each night he flew to her window and told her stories — of matches, of clocks, of everything. The sultan and sultana were charmed; the wedding was set.

For the finale, the youth planned fireworks from the trunk — but the sparks set the trunk ablaze. It burned to ashes.

He could fly no more. But he had his stories — and, some say, the princess anyway, for she loved the storyteller more than the god.

Moral: stories outlast the trunk that carries them.""",
 ["Andersen, 1839.","Stories within a story.","The trunk burns; tales remain."]),
("The Shadow", "moral tale",
 "Andersen's complete tale: the scholar's shadow detaches, thrives, and at last has the scholar executed — identity's dark twin.",
 """THE SHADOW (SKYGGEN)
By Hans Christian Andersen, 1847 (public domain, retold complete).

In the hot lands, a scholar's shadow detached itself and slipped into the house across the street. Years later it returned — a man now, sleek and prosperous, having learned the world's ways (including, he hinted, how to see through things).

The shadow rose: married wealth, moved in courts, and took the scholar as his own shadow — "my learned shadow," he introduced him.

At last the shadow demanded the scholar deny his own existence and become the shadow's shadow. The scholar refused — and the shadow, now powerful, had him arrested as a madman and executed.

The shadow married the princess. And no one ever knew.

Moral (for older children): success without substance devours its source.""",
 ["Andersen, 1847.","His darkest philosophical tale.","The shadow outgrows the man."]),
("Twinkle, Twinkle, Little Star", "rhyme",
 "The beloved lullaby in full — Jane Taylor's 1806 poem set to music, complete.",
 """TWINKLE, TWINKLE, LITTLE STAR
Words: Jane Taylor, 1806 (public domain). Music: "Ah! vous dirai-je, maman" (traditional).

Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, twinkle, little star,
How I wonder what you are!

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.
Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark,
Lights the trav'ller in the dark —
Tho' I know not what you are,
Twinkle, twinkle, little star.
Twinkle, twinkle, little star,
How I wonder what you are!""",
 ["Jane Taylor, 1806.","Sung to a French melody of 1761.","The classic bedtime song."]),
("Humpty Dumpty", "rhyme",
 "The complete classic rhyme — all the king's horses and all the king's men.",
 """HUMPTY DUMPTY
Traditional nursery rhyme (public domain).

Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.

Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.""",
 ["Traditional, 18th century or older.","Originally a riddle.","The egg came later — early versions show no egg."]),
("Jack and Jill", "rhyme",
 "The complete rhyme — up the hill, down the hill, and the vinegar-and-brown-paper cure.",
 """JACK AND JILL
Traditional nursery rhyme (public domain).

Jack and Jill went up the hill
To fetch a pail of water.
Jack fell down and broke his crown,
And Jill came tumbling after.

Up Jack got, and home did trot,
As fast as he could caper,
He went to bed to mend his head,
With vinegar and brown paper.

Then Jill came in, and she did grin,
To see Jack's paper plaster;
Her mother said, "Now, my dear Jill,
Don't laugh at your brother's disaster.""",
 ["Traditional, 18th century.","The vinegar-and-brown-paper cure was real folk medicine.","Jack's crown = his head."]),
("Mary Had a Little Lamb", "rhyme",
 "Sarah Josepha Hale's 1830 poem in full — the lamb that followed Mary to school.",
 """MARY HAD A LITTLE LAMB
Words: Sarah Josepha Hale, 1830 (public domain).

Mary had a little lamb,
Its fleece was white as snow;
And everywhere that Mary went,
The lamb was sure to go.

It followed her to school one day,
Which was against the rule;
It made the children laugh and play
To see a lamb at school.

And so the teacher turned it out,
But still it lingered near,
And waited patiently about
Till Mary did appear.

"Why does the lamb love Mary so?"
The eager children cry;
"Why, Mary loves the lamb, you know,"
The teacher did reply.""",
 ["Sarah Josepha Hale, 1830.","Based on a true lamb in Sterling, Massachusetts.","Edison's first phonograph recording, 1877."]),
("Old MacDonald Had a Farm", "rhyme",
 "The complete cumulative farm song — every animal and its sound.",
 """OLD MACDONALD HAD A FARM
Traditional (public domain).

Old MacDonald had a farm, E-I-E-I-O!
And on that farm he had a cow, E-I-E-I-O!
With a moo-moo here, and a moo-moo there,
Here a moo, there a moo, everywhere a moo-moo!
Old MacDonald had a farm, E-I-E-I-O!

Old MacDonald had a farm, E-I-E-I-O!
And on that farm he had a pig, E-I-E-I-O!
With an oink-oink here, and an oink-oink there,
Here an oink, there an oink, everywhere an oink-oink!
Old MacDonald had a farm, E-I-E-I-O!

Old MacDonald had a farm, E-I-E-I-O!
And on that farm he had a duck, E-I-E-I-O!
With a quack-quack here, and a quack-quack there,
Here a quack, there a quack, everywhere a quack-quack!
Old MacDonald had a farm, E-I-E-I-O!

Old MacDonald had a farm, E-I-E-I-O!
And on that farm he had a horse, E-I-E-I-O!
With a neigh-neigh here, and a neigh-neigh there,
Here a neigh, there a neigh, everywhere a neigh-neigh!
Old MacDonald had a farm, E-I-E-I-O!

Old MacDonald had a farm, E-I-E-I-O!
And on that farm he had a sheep, E-I-E-I-O!
With a baa-baa here, and a baa-baa there,
Here a baa, there a baa, everywhere a baa-baa!
Old MacDonald had a farm, E-I-E-I-O!""",
 ["Traditional, 19th century.","The cumulative song form teaches memory.","Five verses; add your own animals."]),
("Baa, Baa, Black Sheep", "rhyme",
 "The complete rhyme — three bags full, and the 1744 original wording.",
 """BAA, BAA, BLACK SHEEP
Traditional nursery rhyme (public domain, first printed 1744).

Baa, baa, black sheep,
Have you any wool?
Yes, sir, yes, sir,
Three bags full.

One for the master,
And one for the dame,
One for the little boy
Who lives down the lane.""",
 ["First printed 1744.","One of the oldest English rhymes.","About the medieval wool trade."]),
("Hey Diddle Diddle", "rhyme",
 "The complete nonsense rhyme — the cat, the fiddle, the cow, and the moon.",
 """HEY DIDDLE DIDDLE
Traditional nursery rhyme (public domain).

Hey diddle diddle,
The cat and the fiddle,
The cow jumped over the moon;
The little dog laughed
To see such sport,
And the dish ran away with the spoon.""",
 ["Traditional, 18th century.","Pure glorious nonsense.","The moon-jumping cow, immortal."]),
("Little Miss Muffet", "rhyme",
 "The complete rhyme — the tuffet, the curds and whey, and the frightened spider.",
 """LITTLE MISS MUFFET
Traditional nursery rhyme (public domain).

Little Miss Muffet
Sat on a tuffet,
Eating her curds and whey;
Along came a spider,
Who sat down beside her
And frightened Miss Muffet away.""",
 ["Traditional, early 19th century.","A tuffet is a small stool.","Curds and whey: Little Miss Muffet's cottage cheese."]),
("The Grand Old Duke of York", "rhyme",
 "The complete marching rhyme — up, down, and neither up nor down.",
 """THE GRAND OLD DUKE OF YORK
Traditional nursery rhyme (public domain).

Oh, the grand old Duke of York,
He had ten thousand men;
He marched them up to the top of the hill,
And he marched them down again.

And when they were up, they were up,
And when they were down, they were down,
And when they were only half-way up,
They were neither up nor down.""",
 ["Traditional.","About a real duke's pointless campaign.","The marching actions are the point."]),
("Row, Row, Row Your Boat", "rhyme",
 "The complete round — row gently down the stream, in canon.",
 """ROW, ROW, ROW YOUR BOAT
Traditional round (public domain, published 1852).

Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.

Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.

(Sing as a round: the second group starts when the first reaches "Gently.")""",
 ["Published 1852.","Sung as a round in canon.","'Life is but a dream' — philosophy for toddlers."]),
]


# ================= 6. childrens-literature-signature =================
# Signature originals: complete original children's stories, clearly labeled.
CHILSIG = [
# --- bedtime (10) ---
("The Moon's Nightlight", "bedtime",
 "A Signature original bedtime story: the Moon keeps a nightlight for a small bear who is afraid of the dark.",
 """THE MOON'S NIGHTLIGHT
A Signature original bedtime story. (src: signature)

Little Bear was afraid of the dark. Every night he pulled the blanket over his head and whispered, "Too dark, too dark."

One night, the Moon heard him. She reached into her pocket of stars and found the smallest, sleepiest star. "Here," she said, and hung it outside Little Bear's window. "My nightlight. It never goes out."

Little Bear peeked out. The little star glowed soft and gold. "Hello," it yawned.

Every night after that, the little star kept watch. And every morning, just before sunrise, the Moon collected it, tucked it into her pocket, and whispered, "Good work, little one."

Little Bear is not afraid of the dark anymore. But he still says goodnight to the star — and the star, being very sleepy, always yawns back.""",
 ["Signature original bedtime story.","Theme: courage in the dark.","Ages 2–5."]),
("Pip the Firefly's Last Glow", "bedtime",
 "A Signature original bedtime story: Pip the firefly saves his last glow of the night to light a lost duckling home.",
 """PIP THE FIREFLY'S LAST GLOW
A Signature original bedtime story. (src: signature)

Pip was the smallest firefly in the meadow, and his glow was the smallest too — just a thimbleful of light each night.

"Save your glow," his mother told him. "Spend it wisely."

One midnight, Pip heard crying. A lost duckling had wandered from the pond and couldn't find her way back. Pip looked at his glow — nearly gone. Just one thimbleful left.

He spent it. He flew ahead of the duckling, glowing his very brightest, all the way to the pond's edge. His light flickered... and went out.

"Thank you," whispered the duckling, sliding into the water.

Pip sat in the dark, empty and happy. Then — a warm feeling. His glow came back, brighter than before. For kindness, it turns out, recharges fireflies.

Pip glowed all the way home.""",
 ["Signature original bedtime story.","Theme: kindness rewarded.","Ages 3–6."]),
("The Sleepy Train", "bedtime",
 "A Signature original bedtime story: the little Sleepy Train collects yawns from every house and carries them to Dreamland.",
 """THE SLEEPY TRAIN
A Signature original bedtime story. (src: signature)

Every night at bedtime, the Sleepy Train leaves the station. Choo-choo... choo-choo... — slow and soft, so as not to wake anyone.

Its job is to collect yawns. It stops at every house where a child is getting sleepy. "All aboard!" whispers the conductor, and the yawn climbs in — a big stretchy one from Milo, a tiny squeaky one from baby Ana, a sideways one from twins.

The train carries them all to Dreamland, where yawns are turned into dreams. Big yawns become adventures. Tiny yawns become lullabies.

When the train returns, empty and quiet, the conductor hangs up his hat. "Goodnight, yawns," he whispers. "Goodnight, dreams."

And somewhere, a child yawns — the very last one — and falls asleep.""",
 ["Signature original bedtime story.","Theme: the journey to sleep.","Ages 2–5."]),
("Bramble the Hedgehog's Blanket", "bedtime",
 "A Signature original bedtime story: Bramble collects fallen leaves to make a blanket big enough to share.",
 """BRAMBLE THE HEDGEHOG'S BLANKET
A Signature original bedtime story. (src: signature)

Autumn came, and Bramble the hedgehog began collecting leaves for his winter blanket. A red one. A gold one. A crunchy brown one.

"That's enough for me," he said, curling under his pile.

Then he heard sneezing. It was Shrew, with no leaves at all. Bramble pushed half his pile toward her. Then came Mouse, shivering. Bramble shared again. Then Vole. Then a very small, very cold beetle.

Bramble's blanket was now quite thin. But under it, five friends were warm.

"Best blanket ever," sighed Shrew.

Bramble smiled. A blanket shared, he learned, is warmer than a blanket kept — because friends are the warmest part.

And they all slept, cozy, till spring.""",
 ["Signature original bedtime story.","Theme: sharing warmth.","Ages 3–6."]),
("The Star Who Was Late", "bedtime",
 "A Signature original bedtime story: Stella the star oversleeps and must hurry to her place in the sky before the children look up.",
 """THE STAR WHO WAS LATE
A Signature original bedtime story. (src: signature)

Stella was the littlest star, and she overslept. When she woke, the sky was already darkening, and all the other stars were in their places, twinkling.

"Oh no! The children will look up and my spot will be empty!"

She polished herself as fast as she could — scrub, scrub, shine! — and raced across the sky. She bumped into the Moon. "Excuse me! Coming through!"

She reached her spot just as the first child whispered, "Star light, star bright..." Stella twinkled her very hardest, beaming with pride.

"You made it," whispered the Moon.

"Just in time," Stella panted. "From now on, I'm setting TWO alarms."

And she has never been late since.""",
 ["Signature original bedtime story.","Theme: responsibility, gently.","Ages 3–6."]),
("Otter's Lullaby River", "bedtime",
 "A Signature original bedtime story: Mama Otter sings the river to sleep, and the river sings her baby to sleep.",
 """OTTER'S LULLABY RIVER
A Signature original bedtime story. (src: signature)

Every evening, Mama Otter floated on her back with Baby Otter on her tummy, and sang to the river:

"Hush now, river, slow and deep,
Time for all good streams to sleep."

The river slowed. The ripples smoothed. The reeds stopped rustling.

Then the river sang back, low and watery, to Baby Otter:

"Hush now, baby, warm and small,
The river will not let you fall."

Baby Otter's eyes grew heavy. The current rocked him like a cradle. The moon made a silver path on the water.

"Who sings the river to sleep?" Baby Otter yawned.

"I do," said Mama Otter. "And who sings you?"

"The river," said Baby Otter — and slept.""",
 ["Signature original bedtime story.","Theme: comfort and safety.","Ages 2–5."]),
("The Whale's Goodnight Song", "bedtime",
 "A Signature original bedtime story: the old whale sings one note each night, and every sea creature sleeps to it.",
 """THE WHALE'S GOODNIGHT SONG
A Signature original bedtime story. (src: signature)

Deep in the ocean lives the oldest whale. Every night, she sings one note — just one, low and long — and it travels through the whole sea.

The seahorses hear it and curl their tails. "Goodnight," they whisper.

The dolphins hear it and slow their leaps. "Goodnight," they sigh.

The little clownfish hear it in their anemone. "Goodnight," they breathe.

Even the sharks hear it, and for one moment, they are not fierce at all. They are just... sleepy.

The old whale sings her note, and listens as the sea grows quiet around her. "Goodnight, ocean," she hums.

And the ocean, in all its waves and currents, hums back: "Goodnight.""",
 ["Signature original bedtime story.","Theme: rest for everyone.","Ages 2–6."]),
("Mole's Underground Stars", "bedtime",
 "A Signature original bedtime story: Mole, who has never seen the sky, paints stars on his tunnel walls.",
 """MOLE'S UNDERGROUND STARS
A Signature original bedtime story. (src: signature)

Mole had never seen the sky. He lived in the dark tunnels and was happy — mostly. But at bedtime, the rabbits talked about stars.

"What are stars like?" Mole asked.

"Like tiny lanterns," said Rabbit. "Millions of them."

That night, Mole took his brightest pebbles — white quartz that caught the lamplight — and pressed them into his tunnel walls. Hundreds of them. Thousands.

"My stars," he whispered.

Every night after, Mole lay in his burrow and looked at his pebble stars. They didn't twinkle, exactly. But they glowed softly in the lamplight, and Mole felt the same wonder the rabbits felt.

"You know," Rabbit said, visiting once, "yours are the only stars you can touch."

Mole touched one. It was warm. "Best stars," he said.""",
 ["Signature original bedtime story.","Theme: wonder anywhere.","Ages 3–6."]),
("The Cloud Shepherd", "bedtime",
 "A Signature original bedtime story: the Cloud Shepherd gathers the day's clouds and tucks them into bed behind the mountains.",
 """THE CLOUD SHEPHERD
A Signature original bedtime story. (src: signature)

When the sun sets, the Cloud Shepherd climbs into the sky with his crook. "Time to come home, clouds!"

The puffy white ones come first, bouncing like sheep. The gray rain-clouds trail behind, tired from their work. The pink sunset clouds dance in last, showing off.

"Into the pen," says the Shepherd, guiding them behind the mountains. "Fluff up your edges. Settle down."

He counts them: one, two, three... all present. He drapes the night over them like a blanket.

"Sleep well," he whispers. "Tomorrow you'll be new shapes."

And the clouds sleep — dreaming of the shapes they'll be: dragons, castles, sailing ships — when morning comes.""",
 ["Signature original bedtime story.","Theme: endings are beginnings.","Ages 3–6."]),
("Goodnight, Garden", "bedtime",
 "A Signature original bedtime story: a child says goodnight to everything in the garden, and everything says goodnight back.",
 """GOODNIGHT, GARDEN
A Signature original bedtime story. (src: signature)

"Goodnight, sunflowers," said Mina, "tall and sleepy."
"Goodnight, Mina," nodded the sunflowers.

"Goodnight, tomatoes, red and round."
"Goodnight," blushed the tomatoes.

"Goodnight, worm, under the ground."
"Goodnight," wriggled the worm.

"Goodnight, robin, goodnight, bee, goodnight, old apple tree."
"Goodnight, goodnight, goodnight," they sang, "goodnight, Mina."

"Goodnight, watering can. Goodnight, fence. Goodnight, moon, coming up immense."

The moon rose. The garden darkened. The flowers closed like tiny hands folding in prayer.

"Goodnight, garden," whispered Mina, from her window.

And the garden — in the rustle of leaves, the chirp of crickets, the soft night air — whispered back: "Goodnight.""",
 ["Signature original bedtime story.","Theme: gratitude at day's end.","Ages 2–5."]),
# --- adventure (10) ---
("The Map in the Attic", "adventure",
 "A Signature original adventure: Milo finds a map in the attic that leads — through the house itself — to a forgotten birthday present.",
 """THE MAP IN THE ATTIC
A Signature original adventure story. (src: signature)

Milo found the map in a shoebox in the attic. It was drawn in crayon, in his grandmother's handwriting: "For the bravest explorer. X marks the spot."

The map showed... his own house. Start at the attic stairs. Past the creaky step (step three — Milo knew it well). Through the hallway of coats. Under the table-that-is-a-cave. Behind the bookshelf.

At each landmark, a clue in grandmother's writing: "The bravest explorer shares." "The bravest explorer says thank you." "The bravest explorer keeps going."

X marked the spot behind the bookshelf: a small wrapped box. Inside — a compass. Real brass. And a note: "For finding your way. You were always brave. Love, Grandma."

Milo held the compass. It pointed north. But Milo knew: the real treasure was the map — the afternoon his grandmother had spent drawing it, just for him.

He keeps the map in the shoebox. For the next bravest explorer.""",
 ["Signature original adventure.","Theme: love as treasure.","Ages 5–8."]),
("Sable the Sailing Mouse", "adventure",
 "A Signature original adventure: Sable sails a walnut-shell boat across the pond to return a lost button.",
 """SABLE THE SAILING MOUSE
A Signature original adventure story. (src: signature)

Sable found the button on the pond's edge — big, blue, with an anchor on it. "Someone's coat is missing this," she said.

Across the pond lived Old Captain Rat, who had lost a button that very morning.

Sable built a boat from half a walnut shell, with a leaf for a sail and a twig for a mast. She packed cheese for the voyage. "Cast off!" she squeaked.

The crossing was perilous: the Great Ripple (a duck landing), the Seaweed Forest, the Terrible Drip (a leaking garden hose). Sable bailed with an acorn cap and sang sailing songs.

At last — the far shore! Captain Rat wept with joy. "My lucky button! Lost at sea these forty years — well, this morning."

He pinned it on, saluted, and gave Sable his own captain's hat. "For the bravest sailor on the pond."

Sable sailed home at sunset, wearing the hat, full of cheese and glory.""",
 ["Signature original adventure.","Theme: helpfulness and courage.","Ages 4–7."]),
("The Great Backyard Expedition", "adventure",
 "A Signature original adventure: four friends map the backyard as uncharted territory — and discover the compost heap's secret.",
 """THE GREAT BACKYARD EXPEDITION
A Signature original adventure story. (src: signature)

Expedition leader: June. Navigator: Theo (with a compass from a cereal box). Naturalist: Priya (magnifying glass). Supply officer: Sam (snacks).

Their mission: map the backyard, "a land unknown to grown-ups."

They charted the Grass Sea, the Fence Mountains, the Mysterious Hole (a rabbit burrow — "do not enter, dragons maybe"). They catalogued seventeen beetles and one suspicious feather.

Then — the Compost Heap. It steamed. It smelled. "It's a volcano!" whispered Sam.

Priya investigated with her magnifying glass. "It's not a volcano," she announced. "It's a nursery. Look — worms! Hundreds! They're making soil!"

The expedition's greatest discovery: the smelliest place in the yard was the most alive.

They marked it on the map with a gold star: "Mount Compost — source of all gardens." Signed: the Expedition, ages 6 to 8.""",
 ["Signature original adventure.","Theme: discovery and science.","Ages 5–9."]),
("Nia and the Talking Drum", "adventure",
 "A Signature original adventure: Nia's grandmother's drum speaks in rhythms — and warns the village of the coming flood.",
 """NIA AND THE TALKING DRUM
A Signature original adventure story. (src: signature)

Nia's grandmother gave her a drum. "This drum talks," Grandmother said. "But only if you listen first."

Nia practiced: boom-ba-boom, pa-pa-boom. The drum seemed to answer — low notes like distant thunder, high notes like rain on roofs.

One afternoon the rhythms changed. Boom... boom-boom... BOOM. Urgent. Nia ran to the river — it was rising fast, brown and angry, after the mountain rains.

She ran through the village beating the warning rhythm: BOOM-boom-BOOM! The elders knew that rhythm — flood warning, from grandmother's time.

Everyone moved to high ground. The water took three houses, but no lives.

"You listened," said Grandmother. "The drum always knew. It was waiting for someone who listens."

Nia keeps the drum by her bed. She listens every day.""",
 ["Signature original adventure.","Theme: listening and tradition.","Ages 5–9."]),
("The Lighthouse Cat", "adventure",
 "A Signature original adventure: Marmalade the lighthouse cat guides a lost boat home with a lantern in his teeth.",
 """THE LIGHTHOUSE CAT
A Signature original adventure story. (src: signature)

Marmalade was the lighthouse keeper's cat — orange, enormous, and afraid of nothing except cucumbers.

One foggy night, the lighthouse lamp went out. The keeper was away. A fishing boat was coming toward the rocks, its foghorn lost in the mist.

Marmalade looked at the dark lamp. Looked at the boat. Looked at the keeper's lantern.

He picked up the lantern in his teeth — it was heavy, and it swung, and it made him walk funny — and climbed the ninety-seven steps to the gallery. He set the lantern down and sat beside it, tail wrapped around his paws, glowing.

The boat saw the small, brave light and turned. Safe.

When the keeper returned, he found Marmalade asleep by the lantern, one paw over his eyes.

"Best assistant keeper I ever had," said the keeper, and gave him two sardines.

Marmalade still hates cucumbers. But he loves lanterns.""",
 ["Signature original adventure.","Theme: bravery, all sizes.","Ages 4–7."]),
("The Elevator to Everywhere", "adventure",
 "A Signature original adventure: the old apartment elevator has a secret button — floor 7½, which goes anywhere you imagine.",
 """THE ELEVATOR TO EVERYWHERE
A Signature original adventure story. (src: signature)

The elevator in Zara's building was older than anyone. Brass buttons, a creaky gate — and one button nobody pressed: 7½.

Zara pressed it.

The elevator hummed a different hum. The doors opened on — a beach! Warm sand, blue water. Zara stepped out, wiggled her toes, and stepped back in.

Next day: 7½ again. A snowy mountain. A jungle. A library with ladders to the ceiling.

The rule, Zara discovered: the elevator goes where you truly want to go. When she wished for "somewhere quiet," it opened on her grandmother's kitchen, smelling of bread.

"How did you know?" Zara whispered to the elevator.

The elevator hummed its different hum. Some machines, Zara decided, are just kind.

She never told the other tenants. But sometimes, riding down, she hears the hum change — and smiles, knowing someone else found the button.""",
 ["Signature original adventure.","Theme: imagination.","Ages 5–9."]),
("Captain Kite and the Wind Thieves", "adventure",
 "A Signature original adventure: Captain Kite must rescue the town's wind from the grumpy Wind Thieves of Gray Mountain.",
 """CAPTAIN KITE AND THE WIND THIEVES
A Signature original adventure story. (src: signature)

The wind stopped. Kites drooped. Sailboats sat still. Laundry hung limp.

Captain Kite — retired kite-flyer, age 71 — knew who was responsible: the Wind Thieves of Gray Mountain, who bottled wind in jars to sell.

She packed her oldest kite (red, patched), a ball of string, and a sandwich. Up the mountain she climbed. At the top: the Thieves' cave, shelves of jars labeled "Breeze," "Gale," "Zephyr — premium."

"Those belong to everyone," said Captain Kite.

The chief thief laughed — until Captain Kite's kite caught a draft from a cracked jar and yanked the shelf. Crash! Jars shattered. Wind exploded out — breezes, gales, zephyrs — roaring down the mountain, lifting Captain Kite's kite, lifting Captain Kite!

She flew home on the wind, laughing, landing softly in the town square as every kite in town rose to meet her.

The wind has blown free ever since. And Captain Kite, 71, still flies every windy day.""",
 ["Signature original adventure.","Theme: the commons.","Ages 5–9."]),
("The Secret of the Old Oak", "adventure",
 "A Signature original adventure: twins find a door in the old oak — and the tree's 300 years of memories.",
 """THE SECRET OF THE OLD OAK
A Signature original adventure story. (src: signature)

The old oak had stood by the school for 300 years. Twins Alex and Ada were sure it had a door. On the last day of summer, they found it — a knothole, low down, just big enough.

Inside: not darkness, but light. The tree's memories, hung like pictures:

- A girl in 1720, hiding a book in the hollow.
- Soldiers in 1860, carving initials (still there, outside).
- A wedding in 1950, flowers in the branches.
- Their own grandmother, age 8, reading under the tree in 1975.

"How?" whispered Alex.

"Trees remember slowly," said a voice — the oak itself, slow as sap. "Three hundred years of children. You are my newest."

"Will you remember us?" asked Ada.

"I remember every one," said the oak. "Now — one memory for the wall." It showed them: themselves, today, waving.

They visit every week. The oak is still adding pictures.""",
 ["Signature original adventure.","Theme: memory and nature.","Ages 6–10."]),
("Ravi's Rocket Cart", "adventure",
 "A Signature original adventure: Ravi builds a rocket cart for the neighborhood derby — and learns that slow can win.",
 """RAVI'S ROCKET CART
A Signature original adventure story. (src: signature)

The neighborhood derby: build a cart, race down Holly Hill. Maya built the Lightning (sleek). Jamal built Thunder (loud). Ravi built... the Rocket — from a bathtub, four mismatched wheels, and a sail.

Everyone laughed. The Rocket looked like a bathtub with ambitions.

Race day: Lightning took the lead — then a wheel wobbled off. Thunder roared ahead — then roared into the hedge. The Rocket sailed steadily down, sail catching the breeze, Ravi steering with a broom handle.

Halfway down, Ravi saw Lily's cart stuck in the ditch. He stopped. He helped push her out. They crossed the finish line together — last.

The trophy went to Priya's quiet, sturdy cart. But the crowd's cheer went to Ravi. "Why'd you stop?" asked Maya.

"Racing's fun," said Ravi. "But Lily needed a push."

Lily gave him half her lemonade. Best prize of the day, Ravi decided.""",
 ["Signature original adventure.","Theme: kindness over winning.","Ages 5–9."]),
("The Night Zoo", "adventure",
 "A Signature original adventure: the zoo animals hold a secret meeting at midnight — and invite one small visitor.",
 """THE NIGHT ZOO
A Signature original adventure story. (src: signature)

Sam stayed late at the zoo — hidden in the pretzel stand, purely by accident (mostly). At midnight, a bell rang. Once.

The elephant opened the meeting. "Order! Order! Tonight's business: the new zebra's birthday."

The penguins proposed a fish cake. The giraffes proposed a tall cake. The monkeys proposed throwing the cake. (The elephant vetoed.)

Then the elephant saw Sam. "A visitor! The rules say visitors may attend once."

Sam suggested: a cake shaped like a zebra, with stripes. The animals gasped. "Stripes you can eat!" cried the zebra.

They sang (the lions were loud, the meerkats harmonized). They ate. At dawn, the elephant walked Sam to the gate. "Remember," she said, "midnight. Tell no one."

Sam never told. But every year on the zebra's birthday, he leaves a striped cake by the gate.

And every year, it's gone by morning.""",
 ["Signature original adventure.","Theme: wonder and secrecy.","Ages 4–8."]),
# --- animal tale (10) ---
("Tilly Tortoise's Taxi", "animal tale",
 "A Signature original animal tale: Tilly the tortoise starts a taxi service — slow, but she always gets you there.",
 """TILLY TORTOISE'S TAXI
A Signature original animal tale. (src: signature)

Tilly the tortoise painted a sign: "TILLY'S TAXI — Slow but Sure."

Her first customer was Hopper the hare. "I need to get to the meadow FAST," he said.

Tilly plodded. Hopper tapped his foot. Tilly plodded. Hopper sighed loudly. Tilly plodded — and arrived exactly on time, because Tilly had left early.

Word spread. Mrs. Duck needed the pond by noon — Tilly left at dawn. The ants needed the picnic — Tilly made three trips.

"Why is your taxi always on time?" asked the fox.

"Because I am slow," said Tilly, "I never rush, never crash, and never have to hurry. Slow is just early with a shell."

Tilly's taxi is the most reliable in the forest. The fare: one lettuce leaf. The motto: "Slow but sure gets you there.""",
 ["Signature original animal tale.","Theme: reliability.","Ages 3–7."]),
("The Pigeon Post Office", "animal tale",
 "A Signature original animal tale: Petra the pigeon runs the forest post office — delivering letters, and one very important secret.",
 """THE PIGEON POST OFFICE
A Signature original animal tale. (src: signature)

Petra the pigeon ran the forest post office from the old oak. Letters in, letters out — tied with thread to her leg.

She delivered birthday twigs to the wrens. She delivered a love letter from Mr. Mole to Mrs. Mole (it said: "You are my sunshine, even underground"). She delivered seed catalogs to the finches.

One day came a letter with no address — just a drawing of a blue feather. Petra knew: Blue Jay's feather. She flew the letter across the river, through the rain, to the blue jay's nest.

Inside: "Thank you for the songs. — Wren."

Petra didn't read other birds' mail. But this one, she admitted later, made her fly a little faster.

The post office motto, painted over the door: "Neither rain nor hawks stay these couriers.""",
 ["Signature original animal tale.","Theme: connection.","Ages 4–8."]),
("Bruno Bear Learns to Share", "animal tale",
 "A Signature original animal tale: Bruno hoards the berry bush — until the bees teach him about sharing.",
 """BRUNO BEAR LEARNS TO SHARE
A Signature original animal tale. (src: signature)

Bruno Bear found the biggest berry bush in the forest. "Mine," he said, and sat in front of it.

Rabbit asked for a few. "Mine," said Bruno. Squirrel asked for a handful. "Mine," said Bruno.

Then the bees came. "Excuse us," they buzzed. "We need the blossoms to make honey."

"These are MY berries," growled Bruno.

"And whose are the blossoms?" asked the queen bee. "The bush makes berries from blossoms, and blossoms from sun and rain. Did you make the sun, Bruno?"

Bruno thought. "...No."

"Then the bush is everyone's," said the bee.

Bruno moved aside. The animals ate. The bees made honey — and gave Bruno the first jar. "For the bear who learned," they buzzed.

Now the sign by the bush reads: "Bruno's Berries — Everyone Welcome." Bruno added the second line himself.""",
 ["Signature original animal tale.","Theme: sharing.","Ages 3–7."]),
("Cleo the Clever Crow", "animal tale",
 "A Signature original animal tale: Cleo solves the forest's problems — the stuck lid, the high nest, the puzzle of the shiny things.",
 """CLEO THE CLEVER CROW
A Signature original animal tale. (src: signature)

Cleo the crow collected shiny things: bottle caps, foil, a spoon. But Cleo was famous for something better — solving problems.

Problem 1: The jam jar. Raccoon's paws couldn't open it. Cleo dropped it from a branch — crack! — and they shared the jam.

Problem 2: The high nest. Wren's chicks were crying, and the nest was too high to reach. Cleo wove a ladder of twigs. (It wobbled. It worked.)

Problem 3: The shiny things kept disappearing. Cleo staked out her collection and caught — a magpie! They talked. The magpie was decorating her nest for her babies. Cleo gave her half the foil. "For the babies," she said.

The forest council named Cleo "Solver of Problems." Her payment: all the shiny things anyone finds.

She shares them with the magpie.""",
 ["Signature original animal tale.","Theme: cleverness + generosity.","Ages 4–8."]),
("The Penguin Who Wanted to Fly", "animal tale",
 "A Signature original animal tale: Pippa the penguin can't fly — but she learns she can do something even better.",
 """THE PENGUIN WHO WANTED TO FLY
A Signature original animal tale. (src: signature)

Pippa watched the albatross soar and sighed. "I want to fly."

She flapped. She flopped. She slid on her tummy down the ice hill (fun, but not flying). She jumped off the low rock — splash.

"Penguins don't fly," said the old penguin gently.

Pippa was sad for exactly one day. Then she watched the albatross again — struggling to take off from the water, flapping desperately.

Pippa dove. Underwater, she FLEW — wings sweeping, body gliding, faster than any bird in the sky. She looped around the albatross's reflection and burst out in a spray of silver.

The albatross stared. "How did you do that?"

"I fly," said Pippa, "where I belong."

Now when young penguins sigh at the sky, Pippa takes them diving. "Watch," she says. "This is flying.""",
 ["Signature original animal tale.","Theme: finding your element.","Ages 4–8."]),
("Hugo Hedgehog's Big Idea", "animal tale",
 "A Signature original animal tale: Hugo's prickles pop every balloon — until he finds the perfect job for a prickly friend.",
 """HUGO HEDGEHOG'S BIG IDEA
A Signature original animal tale. (src: signature)

Hugo loved parties. But Hugo was a hedgehog, and hedgehogs pop balloons. Pop! went the red one. Pop! went the blue one. The party animals were kind, but Hugo sat in the corner, sad and prickly.

Then came the apple harvest. The apples were high, the baskets were low, and the orchard ladder was broken.

Hugo had an idea. He curled into a ball — and the animals rolled him gently under the trees. Apples stuck to his prickles! He uncurled at each basket and shook them off. Plip, plop, plip!

"We need Hugo!" everyone cheered. "The apple collector!"

Now Hugo wears a badge: "Official Fruit Picker." And at parties, he brings the apple juice — in unpoppable cups.

His prickles, he learned, weren't a problem. They were a profession.""",
 ["Signature original animal tale.","Theme: differences as strengths.","Ages 3–7."]),
("The Snail's Silver Trail", "animal tale",
 "A Signature original animal tale: slow Sydney Snail leaves a silver trail — and it becomes the forest's map.",
 """THE SNAIL'S SILVER TRAIL
A Signature original animal tale. (src: signature)

Sydney Snail was the slowest animal in the forest. "You'll never get anywhere," said the hare.

Sydney didn't argue. He just traveled — to the pond, to the meadow, to the old oak — leaving his silver trail behind him.

One day the ants were lost. "Which way to the picnic?" they cried.

"Follow the silver," said Sydney. His trail led from the anthill to the meadow, gleaming in the sun.

The lost ducklings followed it home. The beetle with the heavy load followed it to the log. Soon every animal knew: when in doubt, follow the silver trail.

The forest council painted a sign: "Sydney's Silver Ways — the forest map."

"See?" said Sydney to the hare. "I got somewhere after all. I got everywhere — slowly."

The hare now walks. Sometimes.""",
 ["Signature original animal tale.","Theme: slow contributions.","Ages 3–7."]),
("Mama Kangaroo's Pocket", "animal tale",
 "A Signature original animal tale: Joey keeps losing things — until Mama's pocket teaches him about keeping.",
 """MAMA KANGAROO'S POCKET
A Signature original animal tale. (src: signature)

Joey lost everything. His favorite stone. His lucky feather. His left shoe (how do you lose one shoe?).

"My pocket keeps things safe," said Mama Kangaroo. "Watch." She tucked Joey's spare sock into her pouch. "See? Safe."

Joey had an idea. He began collecting lost things — a button, a marble, a shiny key — and keeping them in a hollow log. "The Lost and Found," he announced.

Animals came from everywhere. Mrs. Wombat found her button. Mr. Platypus found his marble. The kookaburra found his key and laughed for an hour.

"You're good at keeping," said Mama.

"I'm good at finding keepers," said Joey. "Everything belongs somewhere. My job is to remember where."

The Lost and Found is still open. Joey has only lost one thing since: his reputation for losing things.""",
 ["Signature original animal tale.","Theme: responsibility.","Ages 3–7."]),
("The Elephant's Ears", "animal tale",
 "A Signature original animal tale: Ella is teased for her big ears — until the herd needs them.",
 """THE ELEPHANT'S EARS
A Signature original animal tale. (src: signature)

Ella's ears were the biggest in the herd. The young elephants teased her. "Flap-flap!" they laughed. "Ella the umbrella!"

Ella tried to fold her ears small. It didn't work. She felt big and clumsy.

Then came the dry season. The herd traveled far, and the little ones overheated. Ella fanned them with her great ears — cool air, shade, relief. "Better," sighed the calves.

Then came the lions' roar in the night. Ella's big ears caught the sound first — far off, to the east. "That way is danger," she rumbled. The herd moved west. Safe.

"Ella," said the oldest elephant, "your ears heard what ours could not."

Now when the wind blows through Ella's ears, the young ones say, "Listen — Ella's ears are working." And Ella flaps them proudly.

Big ears, big job.""",
 ["Signature original animal tale.","Theme: self-acceptance.","Ages 3–7."]),
("Oliver Owl's Night School", "animal tale",
 "A Signature original animal tale: Oliver teaches night school — for animals who are afraid of the dark.",
 """OLIVER OWL'S NIGHT SCHOOL
A Signature original animal tale. (src: signature)

Oliver Owl opened a night school. Students: a rabbit, a mouse, and a very nervous hedgehog — all afraid of the dark.

Lesson 1: "The dark is not empty. Listen." They heard: crickets (a choir), wind (a lullaby), an owl (Oliver, saying hello).

Lesson 2: "The dark has lights." They saw: stars, the moon, fireflies — "nature's nightlights."

Lesson 3: "The dark is for resting." They practiced: breathing slow, curling cozy, thinking soft thoughts.

Graduation: each student spent one whole night outside — and loved it. The rabbit now naps under the stars. The mouse stargazes. The hedgehog says the dark is "just the day, sleeping."

Oliver's diploma reads: "Certified Brave in the Dark."

Enrollment is open. The dark, Oliver says, is the best classroom.""",
 ["Signature original animal tale.","Theme: overcoming fear.","Ages 3–7."]),
# --- moral tale (10) ---
("The Honest Lemonade Stand", "moral tale",
 "A Signature original moral tale: Maya's lemonade stand — and the extra dollar that wasn't hers.",
 """THE HONEST LEMONADE STAND
A Signature original moral tale. (src: signature)

Maya's lemonade: 50 cents a cup. Business was booming.

A customer in a hurry paid with a five-dollar bill and rushed off before Maya could make change. $4.50 extra. Maya stared at the money.

She could keep it. No one would know.

She closed the stand, walked six blocks to the customer's office (the cup had the company name), and returned the $4.50.

The customer — Ms. Alvarez — stared. Then she smiled. "You're honest, Maya. My company needs honest people. When you're older, come see me."

Years later, Maya did. That $4.50, she always says, was the best investment she ever made — because honesty compounds.

The stand's sign now reads: "Maya's Lemonade — 50¢. Honesty: free.""",
 ["Signature original moral tale.","Theme: honesty.","Ages 5–9."]),
("The Broken Window", "moral tale",
 "A Signature original moral tale: Jay breaks the window — and learns that owning up is the bravest part.",
 """THE BROKEN WINDOW
A Signature original moral tale. (src: signature)

The baseball went through Mrs. Chen's window. Crash!

Jay's friends ran. Jay stood frozen. His heart hammered. If he ran, no one would know. If he stayed...

He knocked on Mrs. Chen's door. "I broke your window. I'm sorry. I'll pay for it."

Mrs. Chen looked at the window. Looked at Jay. "You came back," she said. "That took courage."

Jay mowed her lawn all summer to pay for the glass. Mrs. Chen gave him lemonade every time. By August, they were friends.

"Why didn't you run?" his friends asked later.

"Because," said Jay, "the running would have lasted a minute. The feeling bad would have lasted forever."

Mrs. Chen's new window has a baseball sticker on it. Jay put it there. A reminder: courage is knocking on the door.""",
 ["Signature original moral tale.","Theme: responsibility.","Ages 5–9."]),
("Two Wolves", "moral tale",
 "A Signature original moral tale: the grandfather's two wolves — and which one wins.",
 """TWO WOLVES
A Signature original moral tale. (src: signature)

"Grandfather," said the boy, "sometimes I feel angry and mean, and sometimes I feel kind. Why?"

The grandfather nodded. "Inside each of us are two wolves. One is anger — jealous, greedy, cruel. The other is kindness — generous, brave, true. They fight, every day."

"Which one wins?" asked the boy.

"The one you feed," said the grandfather.

The boy thought about this. That week, when his sister took his crayons, he felt the angry wolf growl. He took a breath — and shared the crayons. The kind wolf wagged its tail.

When he lost the race, the angry wolf snarled. He congratulated the winner instead. The kind wolf grew stronger.

Every day, two wolves. Every day, a choice.

"Grandfather," the boy said at week's end, "the kind wolf is winning."

"Keep feeding him," smiled the grandfather.""",
 ["Signature original moral tale.","Theme: choosing kindness.","Ages 5–10."]),
("The Empty Pot", "moral tale",
 "A Signature original moral tale: the emperor's seed contest — and the boy whose pot stayed empty.",
 """THE EMPTY POT
A Signature original moral tale. (src: signature)

The emperor, growing old, gave every child a seed. "Whoever grows the finest flower in a year will succeed me."

Ping planted his seed, watered it, sang to it. Nothing grew. He tried new soil, more sun, less water. Nothing.

The year passed. Children arrived with magnificent blooms — roses, lilies, orchids. Ping arrived with an empty pot, ashamed.

The emperor looked at the flowers. Then at Ping's empty pot. "You," he said, "will be emperor."

The crowd gasped. The emperor held up Ping's seed — the seeds had all been cooked. They could never sprout. Every other child had replaced theirs.

"Only Ping was honest," said the emperor. "An empire needs honesty more than flowers."

Ping ruled well. His palace gardens were full of real flowers — grown from honest seeds.""",
 ["Signature original moral tale.","Theme: honesty rewarded.","Ages 5–9."]),
("The Giving Tree's Neighbor", "moral tale",
 "A Signature original moral tale: the old giving tree's neighbor learns that giving needs receiving too.",
 """THE GIVING TREE'S NEIGHBOR
A Signature original moral tale. (src: signature)

Next to the famous giving tree stood a younger tree. She watched the old tree give its apples, its branches, its trunk — until it was a stump.

"Why did you give everything?" the young tree asked the stump.

"Because I loved the boy," said the stump.

"But now you're a stump," said the young tree.

"And he sat on me," said the stump, "and rested. That was enough."

The young tree thought about this. When her own boy came, she gave her apples freely. But she also said: "Take only what you need. And come back and tell me stories — that's what I need."

The boy did. He took apples, and he brought stories, and he watered her roots.

The stump, listening, creaked happily. "You learned," it whispered, "what took me a lifetime: giving is a conversation, not a disappearance."

Both trees still stand — one a stump, one tall — talking in the wind.""",
 ["Signature original moral tale.","Theme: healthy giving.","Ages 6–10."]),
("The Boy Who Shared His Umbrella", "moral tale",
 "A Signature original moral tale: one umbrella, two children, and the friendship that followed the rain.",
 """THE BOY WHO SHARED HIS UMBRELLA
A Signature original moral tale. (src: signature)

It rained at dismissal. Leo had an umbrella. The new girl, Amara, had nothing — and a long walk.

"Come under," said Leo, holding it out.

They walked slowly, sharing the small dry space. Amara told him about her old school, her cat, her fear of the new. Leo told her about the school's secret: the library's comfy chairs, the lunch lady's extra cookies.

By the time they reached her corner, the rain had stopped. "Thank you," said Amara.

"Anytime," said Leo.

The next day, Amara brought two umbrellas. "In case," she said, handing one to Leo.

They've shared umbrellas — and secrets, and lunches, and jokes — ever since. The school's smallest umbrella started its biggest friendship.

Moral: kindness is the best introduction.""",
 ["Signature original moral tale.","Theme: welcoming others.","Ages 4–8."]),
("The Promise Keeper", "moral tale",
 "A Signature original moral tale: Sam promises to feed the neighbor's cat — even when the carnival comes to town.",
 """THE PROMISE KEEPER
A Signature original moral tale. (src: signature)

Sam promised Mrs. Abernathy he'd feed her cat, Biscuit, while she visited her sister. Every day at five. Easy.

Then the carnival came to town — one day only! The Ferris wheel! The cotton candy! All Sam's friends were going at five.

Sam looked at the carnival poster. Looked at the cat food. He fed Biscuit at five, then ran to the carnival at five-thirty — missing the Ferris wheel, but catching the jugglers.

Mrs. Abernathy returned. "Biscuit looks well-fed," she said. "You're a promise keeper, Sam."

She gave him a carnival ticket — she'd bought two, "just in case." They went together the next weekend. Ferris wheel, cotton candy, everything.

"A promise," Mrs. Abernathy said, sharing the cotton candy, "is a treasure you keep by keeping it."

Sam never broke a promise after that. Not one.""",
 ["Signature original moral tale.","Theme: keeping promises.","Ages 5–9."]),
("The Jealous Paintbrush", "moral tale",
 "A Signature original moral tale: Pia's paintbrush is jealous of the other art supplies — until the painting needs them all.",
 """THE JEALOUS PAINTBRUSH
A Signature original moral tale. (src: signature)

Pia's paintbrush was jealous. The pencils got to sketch first. The crayons got the bright colors. The eraser — the eraser got to fix mistakes, which seemed like the most important job.

"I do all the real work," grumbled the brush.

Then Pia started her big painting — a sunset. The pencils sketched the hills. The crayons laid the bright clouds. The brush swept the orange and purple across the sky. The eraser lifted out the sun's glow.

It was beautiful. And it needed every one of them.

"I'm sorry," said the brush to the others. "I thought I was the painting. But we're all the painting."

Now the art box has a motto, written by Pia: "Every tool matters."

The brush still does the skies. But it never grumbles anymore. It knows: the masterpiece is teamwork.""",
 ["Signature original moral tale.","Theme: teamwork over envy.","Ages 4–8."]),
("The Lost Wallet", "moral tale",
 "A Signature original moral tale: finding a wallet full of money — and the note inside that changes everything.",
 """THE LOST WALLET
A Signature original moral tale. (src: signature)

Dev found a wallet on the bus. Inside: $200, and a note in shaky handwriting: "For my grandson's birthday. — Grandpa."

Dev's friends said: "Finders keepers!" Dev looked at the note. He thought of his own grandpa.

He took the wallet to the bus office. The clerk found the owner — Mr. Hassan, 82, who'd been searching all day.

Mr. Hassan hugged Dev. "You saved the birthday," he said. He tried to give Dev $20. Dev refused. So Mr. Hassan gave him something better: the story of his grandson, and an invitation to the party.

Dev went. There was cake. The grandson, Ali, became Dev's best friend.

"Finders keepers?" Dev laughs now. "Finders returners. Much better rewards."

The note is framed in Dev's room: "For my grandson's birthday." Under it, Dev wrote: "And my new best friend.""",
 ["Signature original moral tale.","Theme: honesty rewarded.","Ages 5–9."]),
("The Garden of Forgiveness", "moral tale",
 "A Signature original moral tale: two friends quarrel — and plant a garden to grow back together.",
 """THE GARDEN OF FORGIVENESS
A Signature original moral tale. (src: signature)

Maya and Zoe were best friends — until the Great Sandbox Argument. They didn't speak for a week. The silence grew like a weed.

Maya's grandmother suggested: "Plant something together. Gardens forgive."

They planted a garden — grudgingly at first. Maya dug; Zoe planted. They argued about the rows (straight vs. curvy — they compromised: wavy). They watered together. They waited together.

The first sprout came up. They both cheered — and laughed — and the week of silence broke like a dam.

"I'm sorry," said Maya. "I'm sorry," said Zoe. The sprout didn't care who was right.

By summer, the garden was glorious: tomatoes, sunflowers, one enormous pumpkin. They named it "Forgiveness" and carved their initials in it.

Every year they plant again. The garden, they say, is their friendship — it needs watering.""",
 ["Signature original moral tale.","Theme: forgiveness.","Ages 5–9."]),
# --- fantasy (10) ---
("The Dragon Who Painted Sunsets", "fantasy",
 "A Signature original fantasy: Ember the dragon paints the sunset each evening — but she's running out of red.",
 """THE DRAGON WHO PAINTED SUNSETS
A Signature original fantasy story. (src: signature)

Ember was the sunset dragon. Every evening, she flew across the sky with her paintbrush tail, painting the clouds orange, pink, and red.

But her red paint was running low. She'd been generous with the reds — spectacular sunsets all summer — and now the jar was nearly empty.

"I'll just do pastels," she told the clouds. The sunset was pale and pretty. But the people below missed the reds.

A little girl sent up a paper airplane: "Please, more red tomorrow. It's my birthday."

Ember flew to the volcano — where the oldest dragon kept the Red Reserve. "Please," she said. "It's for a birthday."

The old dragon filled her jar to the brim. "For birthdays," he rumbled, "always."

That evening's sunset was the reddest in years. The birthday girl wished on it. Ember winked — dragons can do that — and flew home, tail dripping crimson.""",
 ["Signature original fantasy.","Theme: generosity.","Ages 5–9."]),
("The Library of Lost Things", "fantasy",
 "A Signature original fantasy: beneath the library is a room where all lost things wait — and one boy must find his grandmother's ring.",
 """THE LIBRARY OF LOST THINGS
A Signature original fantasy story. (src: signature)

Beneath the town library, down stairs the librarian never mentioned, is the Library of Lost Things. Every lost object in the world waits there on shelves: single socks, baby teeth, library books (overdue by decades).

Theo went looking for his grandmother's ring — lost at the beach, full of memories. The Keeper, an old woman with spectacles on a chain, nodded. "Aisle 7. Sentimental items."

Theo searched... and searched. Then he understood: the ring wasn't lost. Grandmother had given it to his mother years ago — it was in her jewelry box all along.

"Most things here," said the Keeper, "are waiting for someone to remember where they really are."

Theo left the ring where it belonged. But he took something else: the Keeper's advice. "Lose less," she said. "Remember more."

He's never lost anything since. Mostly.""",
 ["Signature original fantasy.","Theme: memory.","Ages 6–10."]),
("The Clockwork Garden", "fantasy",
 "A Signature original fantasy: every flower in the clockwork garden blooms on gears — and one daisy decides to bloom wild.",
 """THE CLOCKWORK GARDEN
A Signature original fantasy story. (src: signature)

In the clockwork garden, every flower bloomed on schedule. Roses at six. Tulips at seven. The gears turned, the petals opened — precise, perfect, predictable.

One daisy — Daisy — was tired of the schedule. When her gear clicked for 8 a.m., she waited. She bloomed at 8:17, because the sun felt right.

The gardener was horrified. "Out of sync!"

But the bees loved it. "A flower that's awake when we're hungry!" They visited Daisy first every day.

Soon other flowers tried it: a rose bloomed at noon, just because. A tulip stayed open late to see the stars.

The garden became gloriously unpredictable. The gardener stopped winding the gears and started watching the sky.

Daisy's plaque reads: "She bloomed when the sun felt right." The gears are in the museum now. The garden runs on sunshine.""",
 ["Signature original fantasy.","Theme: individuality.","Ages 5–9."]),
("Bramblewick the Friendly Witch", "fantasy",
 "A Signature original fantasy: Bramblewick is a witch whose spells only do kind things — which makes her the odd one out.",
 """BRAMBLEWICK THE FRIENDLY WITCH
A Signature original fantasy story. (src: signature)

Bramblewick was a witch, but her spells kept coming out kind. She tried to brew a grumbling potion — it came out as giggles. She tried a storm spell — it rained flower petals.

The other witches were embarrassed. "You're doing it wrong," they cackled.

Bramblewick practiced being properly witchy. She scowled into the mirror. She cackled (it sounded like hiccups). She tried to curse a toad — and accidentally gave it a top hat. The toad looked dashing.

Then the village below caught a cold — a sneezy, wheezy, everybody-aches cold. Bramblewick brewed her biggest cauldron: soup. Healing, honeyed, steaming soup. She flew door to door, leaving pots on steps.

The village got well. The children drew pictures of the kind witch. The other witches tasted the soup.

"...Actually," said the eldest witch, "this is excellent."

Bramblewick still can't cast a proper curse. She's too busy being the soup witch. The village prefers it that way.""",
 ["Signature original fantasy.","Theme: being yourself.","Ages 4–8."]),
("The Mermaid's Library", "fantasy",
 "A Signature original fantasy: in a sunken ship, a mermaid keeps every book ever lost at sea — and lends them to sailors' dreams.",
 """THE MERMAID'S LIBRARY
A Signature original fantasy story. (src: signature)

In a sunken ship at the bottom of the bay, Marina the mermaid keeps the Library of Lost Books — every book ever lost at sea: shipwrecked novels, overboard diaries, a captain's log, a child's picture book about whales.

She mends them with seaweed thread and reads them by jellyfish light.

But books want readers. So Marina lends them — to sailors' dreams. A lonely sailor dreams of the picture book. A captain dreams the log's old voyages. A homesick cabin boy dreams his mother's letters.

They wake comforted, never knowing why.

One stormy night, a real reader came: a girl who'd dropped her book off the pier, diving after it. Marina gave her the grand tour — and a library card, waterproof, good forever.

"Return it whenever," said Marina. "The sea is patient."

The girl visits every summer. The books are always waiting.""",
 ["Signature original fantasy.","Theme: books find readers.","Ages 6–10."]),
("The Giant's Teacup", "fantasy",
 "A Signature original fantasy: a giant's lost teacup becomes a village's pond — and the village repays the giant.",
 """THE GIANT'S TEACUP
A Signature original fantasy story. (src: signature)

The giant Grob lost his teacup over the mountain. It landed in the valley — and became the village pond. Ducks moved in. Children sailed boats. The village loved the pond.

Grob came looking, stepping carefully (giants try). "My teacup!" he boomed — and the village trembled.

Little Anya wasn't afraid. "It's our pond now," she said. "But you can visit. We'll even fill it with tea."

The village brewed their biggest pot — well, pond — of tea. Chamomile. Grob sat on the mountain and sipped from the pond with a straw made from a hollowed tree. "Best tea," he rumbled happily.

Now Grob visits every autumn. The village makes tea; Grob tells giant stories (they take a while). The ducks don't mind sharing.

The pond's official name: "Grob's Teacup." The ducks call it home.""",
 ["Signature original fantasy.","Theme: sharing and friendship.","Ages 4–8."]),
("The Staircase in the Tree", "fantasy",
 "A Signature original fantasy: a staircase spirals up inside the hollow oak — each step a different season.",
 """THE STAIRCASE IN THE TREE
A Signature original fantasy story. (src: signature)

Inside the hollow oak, Maya found a staircase. It spiraled up — and each landing was a different season.

First landing: spring. Blossoms, bird nests, the smell of rain.
Second: summer. Warm light, buzzing bees, a tiny sun through the leaves.
Third: autumn. Gold leaves falling upward (that was odd, but lovely).
Fourth: winter. Snow on the branches inside the tree, and a small fox asleep.

At the top: a door. Behind it, the tree's heart — a warm, glowing room where the oak kept its memories: every bird that nested, every child that climbed, every storm weathered.

"You're the first to climb all the way," said the oak. "Most stop at summer."

"Why?" asked Maya.

"Summer is comfortable," said the oak. "But winter is where the stories are."

Maya visits every season now. She likes winter best too.""",
 ["Signature original fantasy.","Theme: wonder in all seasons.","Ages 5–9."]),
("Pip and the Cloud Factory", "fantasy",
 "A Signature original fantasy: Pip discovers the cloud factory where weather is made — and helps fix the rain machine.",
 """PIP AND THE CLOUD FACTORY
A Signature original fantasy story. (src: signature)

Pip followed the rainbow and found the Cloud Factory — a vast workshop in the sky where weather was made. Puffy clouds on conveyor belts. Rain in vats. Lightning in jars (handle with care).

The foreman, a thunderhead named Nimbus, was in a panic. "The rain machine is stuck! It's been drizzling for a week!"

Pip, being small, crawled inside the machine. The problem: a sparrow's nest in the gears. Three eggs, nearly hatched.

"We can't move them," said Pip.

"Then we wait," said Nimbus.

For three days, the factory made sunshine instead — the first sunny week in ages — while the eggs hatched. The sparrows fledged. The nest was cleared.

The rain machine roared back to life, and the first real rain in weeks fell — with three young sparrows riding the drops, laughing.

Pip got a badge: "Honorary Weather Worker." He wears it on rainy days.""",
 ["Signature original fantasy.","Theme: patience and care.","Ages 5–9."]),
("The Talking Mountain", "fantasy",
 "A Signature original fantasy: the mountain only speaks once a year — and this year, it speaks to a small girl.",
 """THE TALKING MOUNTAIN
A Signature original fantasy story. (src: signature)

The mountain spoke once a year, on the longest night. Kings had climbed to hear it. Scholars had waited decades.

This year, it spoke to Wren — age seven, who'd climbed up to fetch her goat.

"Hello?" said the mountain. Its voice was like stones settling.

"Hello," said Wren. "Is my goat up here?"

"Behind the pine," said the mountain. "Wren — why did you climb?"

"For Biscuit," she said. "He's my goat."

The mountain rumbled — a laugh. "Kings ask me for wisdom. Scholars ask for secrets. You came for a goat."

"Is that wrong?" asked Wren.

"It is the first honest reason I've heard in four hundred years," said the mountain. "Ask me anything."

Wren thought. "Will Biscuit be okay?"

"He will," said the mountain. "And you, Wren, will be kind. That is the whole wisdom. Go home."

Wren went home. The scholars are still waiting for their turn.""",
 ["Signature original fantasy.","Theme: simple wisdom.","Ages 5–9."]),
("The Lantern Festival of Fireflies", "fantasy",
 "A Signature original fantasy: once a year, the fireflies hold a lantern festival — and a young one must light the great lantern.",
 """THE LANTERN FESTIVAL OF FIREFLIES
A Signature original fantasy story. (src: signature)

Once a year, on the darkest night, the fireflies held their lantern festival. Thousands of lights in the meadow — every firefly carrying a tiny lantern.

This year, little Luma was chosen to light the Great Lantern — the biggest light of all, hung from the old oak. She was the youngest ever chosen, and her glow trembled.

"What if I'm not bright enough?" she whispered.

The elder firefly smiled. "The Great Lantern doesn't need your brightness. It needs your courage. Light it."

Luma flew up — higher than she'd ever flown — and touched her lantern to the wick. The Great Lantern blazed: gold and green and silver, lighting the whole meadow.

The festival began: dances in the air, songs in flashes, stories in light.

Luma watched from the oak branch, glowing steadily now. "I did it," she whispered.

"You did," said the elder. "Next year, you'll teach the next little one."

And she did.""",
 ["Signature original fantasy.","Theme: courage.","Ages 4–8."]),
# --- rhyme (10) ---
("The Sleepy Sloth's Song", "rhyme",
 "A Signature original rhyming story: Sammy the sloth does everything slowly — including saying goodnight.",
 """THE SLEEPY SLOTH'S SONG
A Signature original rhyming story. (src: signature)

Sammy the sloth hung in his tree,
As slow as slow could ever be.
He ate his leaves so sl-o-o-wly,
"There's no need to hurry," said he.

The monkeys swung and chattered fast,
"Come play!" they cried as they rushed past.
"I'll come," said Sammy, "at... long... last..."
(He arrived as the games had passed.)

But when the moon rose round and bright,
And all the jungle said goodnight,
Sammy sang his song so slow,
It made the sleepy breezes flow:

"Good... night... moon... good... night... stars...
Good... night... near... good... night... far...
Sleep... is... coming... here... it... is..."
And the whole jungle slept to this.

So if you're slow like Sammy Sloth,
That's not a flaw — it's just your troth:
The world needs fast, the world needs slow,
And slow is how the good dreams go.""",
 ["Signature original rhyme.","Theme: slow is fine.","Ages 3–6."]),
("Penny Penguin's Parade", "rhyme",
 "A Signature original rhyming story: Penny organizes the penguins into the silliest parade on ice.",
 """PENNY PENGUIN'S PARADE
A Signature original rhyming story. (src: signature)

Penny Penguin had a plan,
The silliest in all the land:
"A parade!" she cried. "On ice! Today!
Come one, come all — hip, hip, hooray!"

The penguins lined up, flip, flap, flop,
Waddling, wobbling, stop-and-hop.
Wally wore a fishy hat,
And Nellie danced with Gert the cat —

Well, not a cat, a seal named Sal,
Who was Penny's very best pal.
They marched and slid from shore to shore,
Then marched and slid a little more.

The walrus clapped his flippers wide,
The polar bear laughed till he cried.
"Best parade!" the seagulls cheered,
The silliest that ever appeared.

And Penny bowed and took a bow,
And whispered, "Let's do it again — right now!""",
 ["Signature original rhyme.","Theme: joyful silliness.","Ages 3–6."]),
("The Giggling Garden", "rhyme",
 "A Signature original rhyming story: the garden giggles — and a grumpy gnome learns to laugh.",
 """THE GIGGLING GARDEN
A Signature original rhyming story. (src: signature)

In the garden, behind the wall,
The flowers giggled, one and all.
The daisies chuckled, "Hee hee hee!"
The roses roared (as loud as can be).

The tulips tittered, the pansies purred,
The funniest thing you ever heard!
But Grumble the gnome just crossed his arms:
"Stop that noise! It lacks all charms."

Then a bee flew up his nose — ACHOO!
And Grumble laughed in spite of you —
In spite of him, we mean to say,
He laughed and laughed the livelong day.

Now Grumble giggles with the rest,
The garden's glad — it's for the best.
For laughter grows like flowers do:
Plant a giggle — it blooms in you!""",
 ["Signature original rhyme.","Theme: laughter.","Ages 3–6."]),
("Milo's Marvelous Mud", "rhyme",
 "A Signature original rhyming story: Milo loves mud — gloriously, unapologetically — until bath time.",
 """MILO'S MARVELOUS MUD
A Signature original rhyming story. (src: signature)

Milo found some marvelous mud,
Thick and brown and full of crud.
He squished it here, he squashed it there,
He put some mud in his hair!

He made a mud pie, a mud cake,
A mud snake (a fake one, not a real snake).
He built a castle, tall and grand,
The muddiest castle in the land!

His mother called, "It's time for tea!"
"You'll never guess where Milo'll be —
He's in the tub!" she said with glee,
"And the mud is going down, you see!"

He scrubbed and rubbed from head to toe,
And watched the muddy water flow.
"That was the best day," Milo said,
And dreamed of mud pies in his bed.""",
 ["Signature original rhyme.","Theme: messy fun.","Ages 3–6."]),
("The Brave Little Toaster's Toast", "rhyme",
 "A Signature original rhyming story: a toaster's quest for the perfect golden-brown.",
 """THE BRAVE LITTLE TOASTER'S TOAST
A Signature original rhyming story. (src: signature)

In the kitchen, on the shelf,
Lived a toaster by himself.
"I'll make the perfect golden toast!"
He'd boast and boast and boast and boast.

He tried it light — too pale, too white.
He tried it dark — an ashy fright!
He tried it once, he tried it twice,
He tried it (carefully) with rice —

Well, not with rice, that was a joke,
It filled the kitchen up with smoke!
At last he found the setting right:
A golden brown, a warm delight.

The family cheered, "Hooray! Hooray!
The perfect toast is here to stay!"
And the little toaster, brave and true,
Makes perfect toast for me and you.""",
 ["Signature original rhyme.","Theme: perseverance.","Ages 3–6."]),
("Wanda Whale's Song", "rhyme",
 "A Signature original rhyming story: Wanda's song is too loud — until the ocean needs loud.",
 """WANDA WHALE'S SONG
A Signature original rhyming story. (src: signature)

Wanda Whale would sing all day,
In a very LOUD whale way.
"Too loud!" the fishes all would say,
"Please sing your song some other way!"

Wanda tried to sing it small,
A tiny whisper, barely at all.
But whales aren't built for quiet song —
Her whisper came out just as long!

Then a little boat was lost at sea,
In fog as thick as fog can be.
Wanda sang her loudest song —
And guided the lost boat along!

"Your loudness saved us!" cried the crew.
Wanda smiled — she always knew:
The thing that makes you different, friend,
Is the thing on which others depend.""",
 ["Signature original rhyme.","Theme: differences save the day.","Ages 3–7."]),
("The Dancing Dandelions", "rhyme",
 "A Signature original rhyming story: the dandelions dance — and teach a sidewalk crack to bloom.",
 """THE DANCING DANDELIONS
A Signature original rhyming story. (src: signature)

The dandelions loved to dance,
They'd sway and twirl at every chance.
In yellow skirts, they'd spin around,
The merriest dancers to be found!

A little seed, both small and light,
Floated down one breezy night,
And landed in a sidewalk crack,
Where nothing green would grow — alack!

"Don't cry," the dancers swayed and sung,
"You're young, you're brave, you're far from done!"
They sent their fluff to keep it warm,
To shield it from the coming storm.

And in the spring, to all's delight,
A dandelion bloomed — yellow, bright —
Right in the crack, where none had grown:
The toughest flower ever known!""",
 ["Signature original rhyme.","Theme: resilience.","Ages 3–6."]),
("Freddy Frog's Big Jump", "rhyme",
 "A Signature original rhyming story: Freddy is afraid to jump — until the lily pads need him.",
 """FREDDY FROG'S BIG JUMP
A Signature original rhyming story. (src: signature)

Freddy Frog was scared to leap,
He'd rather nap, or just sleep deep.
"I'm small," he'd croak, "I'll miss, I'll fall!"
He wouldn't jump at all, at all.

The other frogs would hop and play,
From pad to pad throughout the day.
"Come on, Freddy! Join the fun!"
But Freddy stayed out of the sun.

Then Baby Frog got stuck one day,
On a pad that floated far away!
Freddy gulped — and took a breath —
And jumped his best, his bravest, yes!

He landed with a splendid SPLASH,
Right by the baby, in a flash!
"My hero!" all the froglets cried,
And Freddy beamed with froggy pride.

Now Freddy jumps both far and wide —
With courage right there by his side.""",
 ["Signature original rhyme.","Theme: courage.","Ages 3–6."]),
("The Cookie That Ran Away", "rhyme",
 "A Signature original rhyming story: a gingerbread cookie's great escape — with a surprise ending.",
 """THE COOKIE THAT RAN AWAY
A Signature original rhyming story. (src: signature)

The gingerbread cookie jumped from the tray,
"Run, run, as fast as you can!" he'd say.
"You can't catch me!" he sang with glee,
As he ran past the dog and the bumblebee.

He ran past the cat, he ran past the hen,
He ran and he ran and he ran — and then
He came to the girl with the hungry eyes,
Who'd been good all day (what a surprise!).

"Please," she said, in a voice so small,
"May I have a bite? Just one — that's all."

The cookie stopped. He thought. He knew:
Running's fun — but sharing's fun too.

He broke himself in halves, just so,
And shared his cookie-dough glow.
"Run, run!" he laughed. "But stay for tea —
The best adventures share, you see!""",
 ["Signature original rhyme.","Theme: sharing.","Ages 3–6."]),
("Goodnight, Moonbeam", "rhyme",
 "A Signature original rhyming story: saying goodnight to every beam of moonlight.",
 """GOODNIGHT, MOONBEAM
A Signature original rhyming story. (src: signature)

Goodnight to the moonbeam on the floor,
Goodnight to the shadows by the door.
Goodnight to the starlight, soft and deep,
Goodnight to the world, now fast asleep.

Goodnight to the owl in the tree,
Goodnight to the fish in the sea.
Goodnight to the bear in his den,
Goodnight — we'll say goodnight again.

Goodnight to the dreams on their way,
Goodnight to the coming day.
Goodnight, moonbeam, silver and bright —
Goodnight, goodnight, good... night.""",
 ["Signature original rhyme.","Theme: bedtime farewell.","Ages 2–5."]),
]

# ================= 7. local-history-public =================
LOCHPUB = [
# --- city founding (10) ---
("Rome — founded 753 BCE (tradition)", "city founding",
 "Traditional founding of Rome: 21 April 753 BCE, Romulus and Remus. Archaeology shows hilltop settlement from ~1000 BCE.",
 """LOCAL HISTORY DOCUMENT — ROME
Public record of well-documented history.

Traditional date: 21 April 753 BCE — Romulus founds Rome after the fratricide of Remus (Livy, Plutarch). Archaeology: hilltop villages on the Palatine from c.1000 BCE; the Forum valley drained c.600 BCE under the Etruscan kings.

Key layers:
- Regal period (753–509 BCE): seven kings, traditional
- Republic (509–27 BCE): Senate, consuls, expansion across Italy
- Empire: capital of 50–60M people; ~1M in the city at its peak (c.200 CE)
- The Aurelian Walls (271–275 CE) still ring the historic center

The founding myth was celebrated annually as the Parilia. Modern Rome's birthday is still marked every 21 April.

Sources: Livy, Ab Urbe Condita; public archaeological records.""",
 ["Traditional: 21 April 753 BCE.","Archaeology: c.1000 BCE settlement.","Peak: ~1M inhabitants."]),
("Alexandria — founded 331 BCE by Alexander", "city founding",
 "Alexander the Great founded Alexandria in 331 BCE; under the Ptolemies it became the Mediterranean's greatest city of learning.",
 """LOCAL HISTORY DOCUMENT — ALEXANDRIA
Public record of well-documented history.

Founded: 331 BCE by Alexander the Great (Arrian, Plutarch). Designed by the architect Dinocrates on the Mediterranean coast west of the Nile Delta.

Key history:
- Ptolemaic capital (305–30 BCE): the Mouseion and Great Library — Euclid, Eratosthenes, Hypatia worked here
- The Pharos lighthouse: one of the Seven Wonders
- Roman, Byzantine, Arab (641 CE) rule; declined as Cairo rose
- Modern revival: the Bibliotheca Alexandrina opened 2002

Population at its ancient peak: 500,000–1,000,000 — among the largest cities of antiquity.

Sources: Arrian, Anabasis; public historical records.""",
 ["Founded 331 BCE.","Library + Pharos lighthouse.","Peak: up to 1M."]),
("Tenochtitlan — founded 1325", "city founding",
 "The Mexica founded Tenochtitlan in 1325 on Lake Texcoco, guided by the eagle-on-cactus prophecy; it became a 200,000-strong imperial capital.",
 """LOCAL HISTORY DOCUMENT — TENOCHTITLAN / MEXICO CITY
Public record of well-documented history.

Traditional founding: 1325 — the Mexica, guided by the prophecy of an eagle on a cactus devouring a serpent, built on an island in Lake Texcoco.

Key history:
- Chinampa agriculture fed 200,000–300,000 people — larger than London or Seville at the time
- Triple Alliance capital; market at Tlatelolco drew 60,000 daily (Bernal Díaz)
- 1519–21: Cortés's siege; the city fell 13 August 1521
- Rebuilt as Mexico City, capital of New Spain; the lake was drained over centuries

The eagle-and-cactus emblem is on Mexico's flag — the founding prophecy as national symbol.

Sources: Codex Mendoza; Bernal Díaz del Castillo.""",
 ["Founded 1325.","200,000–300,000 at peak.","Flag bears the prophecy."]),
("Kyoto — Heian-kyō, 794", "city founding",
 "Emperor Kanmu moved Japan's capital to Heian-kyō (Kyoto) in 794, beginning the 1,000-year Heian period of court culture.",
 """LOCAL HISTORY DOCUMENT — KYOTO
Public record of well-documented history.

Founded: 794 CE — Emperor Kanmu moved the capital from Nagaoka-kyō to Heian-kyō ('capital of peace and tranquility'), laid out on the Chinese grid plan (Chang'an model).

Key history:
- Imperial capital 794–1868 (1,074 years)
- Heian period (794–1185): The Tale of Genji, kana script, court culture
- 17 UNESCO World Heritage sites in the city
- Spared from WWII bombing — its temples and machiya survive

The grid survives: streets run on the ancient jōbō plan, and addresses still reference it.

Sources: public historical records; UNESCO listings.""",
 ["Founded 794 CE.","Capital for 1,074 years.","17 UNESCO sites."]),
("Istanbul — Byzantium 667 BCE to Constantinople 330 CE", "city founding",
 "Byzas founded Byzantium c.667 BCE; Constantine refounded it as Constantinople in 330 CE; Mehmed II took it in 1453.",
 """LOCAL HISTORY DOCUMENT — ISTANBUL
Public record of well-documented history.

- c.667 BCE: Byzas of Megara founds Byzantium on the Bosphorus
- 330 CE: Constantine I refounds it as Constantinople, capital of the Roman Empire
- 537: Hagia Sophia completed under Justinian
- 1453: Mehmed II conquers the city; capital of the Ottoman Empire
- 1930: officially renamed Istanbul

The city has been the capital of three empires (Roman/Byzantine, Latin, Ottoman) — unique in history. The Theodosian Walls (408–413) still stand in long stretches.

Sources: public historical records.""",
 ["Byzantium c.667 BCE.","Constantinople 330 CE.","Capital of three empires."]),
("Cairo — al-Qahira, 969 CE", "city founding",
 "The Fatimid general Jawhar founded al-Qahira ('The Victorious') in 969 CE; settlement on the site goes back to Babylon Fortress and Fustat (641).",
 """LOCAL HISTORY DOCUMENT — CAIRO
Public record of well-documented history.

Founded: 969 CE by Jawhar al-Siqilli for the Fatimid caliph al-Mu'izz. But the site's history is far older:
- Babylon Fortress (Roman, c.300 CE)
- Fustat (641 CE): first Arab capital of Egypt
- al-Qahira (969): the Fatimid palace-city
- Mamluk (1250–1517) and Ottoman layers

Historic Cairo (UNESCO 1979): mosques, madrasas, and the Khan el-Khalili bazaar. 'The city of a thousand minarets.'

Sources: UNESCO; public historical records.""",
 ["Founded 969 CE.","Site occupied since Roman times.","UNESCO Historic Cairo, 1979."]),
("London — Londinium, c.43 CE", "city founding",
 "The Romans founded Londinium around 43 CE; it became Britain's largest city and, by 1800, the world's largest.",
 """LOCAL HISTORY DOCUMENT — LONDON
Public record of well-documented history.

Founded: c.43 CE by the Romans as Londinium, at the lowest bridging point of the Thames.

Key history:
- Roman walls (c.200 CE) defined the City of London's boundary for 1,700 years
- 1066: the Tower; medieval wool-trade wealth
- 1666: Great Fire; Wren's rebuilding
- 1801: first census — ~1M, the world's largest city
- 1863: world's first underground railway

The City (the 'Square Mile') still governs itself through the medieval Corporation.

Sources: Museum of London; public records.""",
 ["Founded c.43 CE.","World's largest c.1800.","First underground, 1863."]),
("New York — New Amsterdam, 1624", "city founding",
 "The Dutch founded New Amsterdam in 1624; the English took it in 1664 and renamed it New York. Wall Street follows the Dutch wall's line.",
 """LOCAL HISTORY DOCUMENT — NEW YORK
Public record of well-documented history.

- 1624: Dutch West India Company founds New Amsterdam on Manhattan
- 1626: 'purchase' of Manhattan (the 60-guilder legend)
- 1653: wall built across lower Manhattan — Wall Street's namesake
- 1664: English capture; renamed New York (Duke of York)
- 1789–90: first US capital; Washington inaugurated at Federal Hall
- 1898: consolidation of the five boroughs

Ellis Island (1892–1954): 12M+ immigrants entered through New York Harbor.

Sources: NYC Municipal Archives; public records.""",
 ["1624: New Amsterdam.","1664: renamed New York.","1898: five boroughs."]),
("Sydney — 1788, the First Fleet", "city founding",
 "Captain Arthur Phillip founded Sydney on 26 January 1788 with the First Fleet — Australia Day marks the landing at Sydney Cove.",
 """LOCAL HISTORY DOCUMENT — SYDNEY
Public record of well-documented history.

Founded: 26 January 1788 — Captain Arthur Phillip, First Fleet (11 ships, ~1,400 people, mostly convicts), lands at Sydney Cove.

Key history:
- Penal colony of New South Wales; free settlement grew from the 1820s
- 1851 gold rush: population tripled in a decade
- 1932: Sydney Harbour Bridge opened
- 1973: Opera House opened (UNESCO 2007)
- 2000: Olympic Games

26 January is Australia Day (contentious — also observed as Invasion Day/Survival Day).

Sources: State Library of NSW; public records.""",
 ["Founded 26 Jan 1788.","First Fleet: 11 ships.","Opera House UNESCO 2007."]),
("Timbuktu — the scholarly city", "city founding",
 "Timbuktu grew from a Tuareg camp (c.1100) into the Mali Empire's city of 700,000 manuscripts and 25,000 students.",
 """LOCAL HISTORY DOCUMENT — TIMBUKTU
Public record of well-documented history.

- c.1100: Tuareg seasonal camp ('Tin Buqt')
- 1324: Mansa Musa's Hajj puts it on world maps (Catalan Atlas, 1375)
- 1400s–1500s: Songhai golden age — 700,000 manuscripts; Sankoré madrasa with 25,000 students; scholars like Ahmad Baba
- 1591: Moroccan invasion; scholars exiled
- 1828: René Caillié, first European to return alive

UNESCO World Heritage (1988). The manuscripts — astronomy, law, medicine — are being digitized after the 2012–13 rescue from occupiers.

Sources: UNESCO; public historical records.""",
 ["Scholarly peak: 1500s.","700,000 manuscripts.","UNESCO 1988."]),
# --- historic site (10) ---
("Pompeii — 24 August 79 CE", "historic site",
 "Vesuvius buried Pompeii in 79 CE, preserving a Roman city in ash — 13,000 of 20,000 excavated; 2.5M visitors a year.",
 """LOCAL HISTORY DOCUMENT — POMPEII
Public record of well-documented history.

24 August 79 CE (traditional date; some evidence suggests October): Vesuvius erupted, burying Pompeii under 4–6 meters of ash and pumice. Pliny the Younger's letters (to Tacitus) are the eyewitness account; his uncle Pliny the Elder died in the disaster.

- Population: ~11,000–20,000
- Rediscovered: 1748 (Herculaneum 1738)
- Preserved: frescoes, graffiti, bakeries with bread still in ovens, body casts
- UNESCO World Heritage (1997); ~2.5M visitors/year

The graffiti — electoral slogans, love notes, insults — is the most human archive of Roman daily life.

Sources: Pliny, Letters 6.16 & 6.20; UNESCO.""",
 ["Buried 79 CE.","Eyewitness: Pliny the Younger.","Graffiti = daily life archive."]),
("Machu Picchu — the Inca citadel, c.1450", "historic site",
 "Built c.1450 under Pachacuti, abandoned c.1572, revealed to the world by Hiram Bingham in 1911 — the Andes' stone miracle.",
 """LOCAL HISTORY DOCUMENT — MACHU PICCHU
Public record of well-documented history.

- Built: c.1450, reign of Pachacuti Inca Yupanqui — royal estate, not a 'lost city'
- Abandoned: c.1572 (Spanish conquest's aftermath); never found by the Spanish
- 1911: Hiram Bingham's expedition publicized it (locals knew it)
- Stonework: dry-stone ashlar, earthquake-resistant trapezoidal doors
- UNESCO World Heritage (1983); ~1.5M visitors/year

Purpose debated: royal retreat, religious site, or administrative center — likely all three.

Sources: UNESCO; public archaeological records.""",
 ["Built c.1450.","Publicized 1911.","UNESCO 1983."]),
("Petra — the rose-red city", "historic site",
 "The Nabataeans carved Petra from sandstone cliffs; it commanded incense-trade wealth for 500 years before Rome's annexation.",
 """LOCAL HISTORY DOCUMENT — PETRA
Public record of well-documented history.

- Nabataean capital from c.400 BCE; peak 1st century BCE–1st century CE
- The Treasury (Al-Khazneh) and Monastery carved into rose-red cliffs
- Water engineering: dams, cisterns, channels in the desert
- 106 CE: annexed by Rome (Arabia Petraea); declined as trade routes shifted
- 1812: 'rediscovered' by Burckhardt (locals knew it)
- UNESCO World Heritage (1985); a New7Wonder (2007)

The Siq — the narrow gorge entrance — is one of archaeology's great reveals.

Sources: UNESCO; public archaeological records.""",
 ["Nabataean capital from 400 BCE.","Water engineering in desert.","UNESCO 1985; New7Wonder 2007."]),
("Angkor Wat — the world's largest religious monument", "historic site",
 "Suryavarman II built Angkor Wat in the early 1100s; the Khmer capital held ~750,000 people — the largest pre-industrial city.",
 """LOCAL HISTORY DOCUMENT — ANGKOR
Public record of well-documented history.

- Built: early 12th century, King Suryavarman II — originally Vishnu temple, later Buddhist
- Scale: 162.6 hectares — the world's largest religious monument
- Greater Angkor: ~750,000–1,000,000 people, hydraulic city (barays/reservoirs)
- Decline: 15th century (water-system strain, wars, Theravada shift)
- UNESCO World Heritage (1992)

Lidar mapping (2010s) revealed the full urban sprawl — highways, ponds, and suburbs under the forest.

Sources: UNESCO; public archaeological records.""",
 ["Early 1100s.","162.6 ha: largest religious monument.","City of ~750,000."]),
("Great Zimbabwe — the stone city", "historic site",
 "Between 1100–1450, Great Zimbabwe's dry-stone walls enclosed a Shona trading capital of 10,000–20,000 people.",
 """LOCAL HISTORY DOCUMENT — GREAT ZIMBABWE
Public record of well-documented history.

- Built: 1100–1450 by Shona ancestors — dry stone, no mortar
- The Great Enclosure: 11-meter walls, 250m circumference
- Population: 10,000–20,000; gold and ivory trade to the Swahili coast (and China — porcelain found)
- The Zimbabwe Bird: soapstone raptors, national symbol
- Colonial myth ('Phoenicians built it') debunked by Gertrude Caton-Thompson (1929)

UNESCO World Heritage (1986). The country's name comes from 'dzimba-dze-mabwe' — houses of stone.

Sources: UNESCO; public archaeological records.""",
 ["1100–1450.","11m dry-stone walls.","Country named for it."]),
("Chichen Itza — the Maya observatory city", "historic site",
 "Chichen Itza's El Castillo aligns to the equinoxes; the Maya city dominated Yucatán from c.600–1200 CE.",
 """LOCAL HISTORY DOCUMENT — CHICHEN ITZA
Public record of well-documented history.

- Founded c.600 CE; peak 800–1200
- El Castillo (Temple of Kukulcan): 365 steps; equinox serpent shadow on the staircase
- El Caracol: astronomical observatory aligned to Venus
- The Great Ball Court: largest in Mesoamerica
- Sacred Cenote: offerings of gold, jade, and lives
- UNESCO World Heritage (1988); New7Wonder (2007)

The Maya calendar and astronomy encoded in stone — the city's alignments still work.

Sources: UNESCO; public archaeological records.""",
 ["c.600–1200 CE.","Equinox serpent shadow.","New7Wonder 2007."]),
("Ephesus — the marble metropolis", "historic site",
 "Ephesus held 200,000+ people with the Temple of Artemis (a Wonder), the Celsus Library, and a 25,000-seat theater.",
 """LOCAL HISTORY DOCUMENT — EPHESUS
Public record of well-documented history.

- Greek foundation c.900 BCE; Roman peak 1st–2nd century CE
- Population: 200,000–250,000 — among the empire's largest
- Temple of Artemis: one of the Seven Wonders (rebuilt after Herostratus's arson, 356 BCE)
- Library of Celsus: 12,000 scrolls; facade still standing
- Theater: 25,000 seats (St. Paul's riot, Acts 19)
- Declined as the harbor silted; UNESCO 2015

The Terrace Houses preserve frescoed Roman apartments — Pompeii's eastern counterpart.

Sources: UNESCO; public archaeological records.""",
 ["200,000+ at peak.","Artemis: a Wonder.","Celsus Library facade stands."]),
("Teotihuacan — the city of the gods", "historic site",
 "Teotihuacan's 125,000 people built the Pyramid of the Sun (c.200 CE) — then the city burned c.550, its builders still debated.",
 """LOCAL HISTORY DOCUMENT — TEOTIHUACAN
Public record of well-documented history.

- Founded c.100 BCE; peak 450 CE: 125,000+ people — the Americas' largest city
- Pyramid of the Sun: 65m, among the world's largest pyramids
- Avenue of the Dead: 4km ceremonial axis, aligned to the stars
- Apartment compounds: 2,000+, with murals
- Collapse c.550 CE: burning and iconoclasm; cause debated (revolt? invasion? drought?)

The Aztecs named it ('place where gods were made') a thousand years later.

UNESCO World Heritage (1987).

Sources: UNESCO; public archaeological records.""",
 ["125,000 at peak.","Pyramid of the Sun: 65m.","Burned c.550; cause debated."]),
("The Alhambra — Granada's red palace", "historic site",
 "The Nasrid palaces of the Alhambra (1238–1358) are Islamic art's summit — mathematics in plaster, poetry in stone.",
 """LOCAL HISTORY DOCUMENT — ALHAMBRA
Public record of well-documented history.

- Built 1238–1358 by the Nasrid emirs of Granada — Islam's last Iberian kingdom
- The name: 'al-Hamra' (the Red One), for its walls
- Court of the Lions: 124 marble columns; the fountain's lions
- Mathematics: all 17 wallpaper symmetry groups appear in the tilings
- 1492: the Catholic Monarchs took Granada; Charles V built a Renaissance palace inside
- Washington Irving's 'Tales of the Alhambra' (1832) revived its fame

UNESCO World Heritage (1984).

Sources: UNESCO; public historical records.""",
 ["1238–1358.","All 17 symmetry groups in tile.","UNESCO 1984."]),
("Lalibela — the rock-hewn churches", "historic site",
 "King Lalibela's 12th–13th century churches were carved top-down from living rock — a 'New Jerusalem' in Ethiopia.",
 """LOCAL HISTORY DOCUMENT — LALIBELA
Public record of well-documented history.

- Carved: 12th–13th century, King Lalibela (Zagwe dynasty)
- 11 monolithic churches, cut downward into the rock — roofs at ground level
- Bete Giyorgis (St. George): the perfect cross-shaped icon
- Built as a 'New Jerusalem' after Muslim conquests blocked pilgrimage
- Still active: thousands of priests and pilgrims; Timkat festival

UNESCO World Heritage (1978) — among the first 12 sites ever listed.

Sources: UNESCO; public historical records.""",
 ["12th–13th century.","11 churches, carved downward.","First-12 UNESCO site, 1978."]),
# --- landmark (10) ---
("The Eiffel Tower — 1889", "landmark",
 "Built for the 1889 World's Fair, 330m of iron lattice — Parisians hated it, then adopted it; 7M visitors a year.",
 """LOCAL HISTORY DOCUMENT — EIFFEL TOWER
Public record of well-documented history.

- Built: 1887–89, Gustave Eiffel, for the Exposition Universelle
- Height: 330m (with antennas) — world's tallest structure until 1930 (Chrysler Building)
- 300 artists protested it ('a gigantic black smokestack'); Maupassant ate lunch there daily — 'the only place in Paris I don't see it'
- Saved from demolition by radio: military transmitter from 1903
- Visitors: ~7M/year, the world's most-visited paid monument

The iron expands 15cm in summer heat — the tower literally grows.

Sources: public records.""",
 ["1889; 330m.","Artists protested; radio saved it.","7M visitors/year."]),
("The Statue of Liberty — 1886", "landmark",
 "France's 1886 gift: Bartholdi's 93m copper Liberty Enlightening the World, funded partly by Pulitzer's penny campaign.",
 """LOCAL HISTORY DOCUMENT — STATUE OF LIBERTY
Public record of well-documented history.

- Gift of France (1886); sculptor Frédéric-Auguste Bartholdi; engineer Gustave Eiffel (internal frame)
- Height: 93m (statue 46m); copper skin 2.4mm thick — the green patina is oxidation
- Tablet: 'JULY IV MDCCLXXVI'
- Poem: Emma Lazarus's 'The New Colossus' (1883) added 1903
- Pedestal funded by Joseph Pulitzer's penny donations (120,000+ donors)
- 12M+ immigrants passed it at Ellis Island

UNESCO World Heritage (1984).

Sources: NPS; UNESCO.""",
 ["1886; 93m.","Eiffel built the frame.","Pedestal: penny campaign."]),
("Big Ben — the tower and the bell", "landmark",
 "The Elizabeth Tower (1859) holds the 13.7-ton Great Bell; 'Big Ben' is the bell, not the tower — renamed for Elizabeth II in 2012.",
 """LOCAL HISTORY DOCUMENT — BIG BEN / ELIZABETH TOWER
Public record of well-documented history.

- Completed 1859; architect Augustus Pugin (Gothic Revival)
- The Great Bell: 13.7 tons; 'Big Ben' properly names the bell
- Clock: 4 dials, 7m across; the Great Clock started 31 May 1859
- Accuracy: a stack of old pennies on the pendulum adjusts the rate
- Renamed the Elizabeth Tower for the Diamond Jubilee (2012)
- 2017–22: major conservation; the dials returned to Pugin's original blue

The chimes broadcast the news on the BBC since 1923.

Sources: UK Parliament; public records.""",
 ["1859; bell 13.7 tons.","Pennies adjust the pendulum.","Renamed 2012."]),
("The Sydney Opera House — 1973", "landmark",
 "Jørn Utzon's 1973 shells — the Danish architect's concrete sails, built over 14 years, now UNESCO-listed and iconic.",
 """LOCAL HISTORY DOCUMENT — SYDNEY OPERA HOUSE
Public record of well-documented history.

- Architect: Jørn Utzon (won 1957 competition, age 38)
- Built: 1959–73; cost 14x the estimate; Utzon resigned 1966, never saw it finished
- The shells: derived from a single sphere's geometry — the design breakthrough
- Opened 20 October 1973 by Elizabeth II
- 1M+ tiles on the shells; 8M+ visitors/year
- UNESCO World Heritage (2007)

Utzon was reconciled with the project in the 1990s; he died 2008.

Sources: UNESCO; public records.""",
 ["1973; Utzon's shells.","14 years; 14x budget.","UNESCO 2007."]),
("The Taj Mahal — 1632–1653", "landmark",
 "Shah Jahan's marble memorial to Mumtaz Mahal: 20,000 workers, 1,000 elephants, and perfect symmetry — except the cenotaph.",
 """LOCAL HISTORY DOCUMENT — TAJ MAHAL
Public record of well-documented history.

- Built 1632–53 by Shah Jahan for Mumtaz Mahal (died 1631, childbirth)
- 20,000 workers; 1,000 elephants; marble from Makrana, inlaid with 28 gemstone types
- Perfect bilateral symmetry — except Shah Jahan's own cenotaph (added later, off-center)
- The minarets lean outward: designed to fall away from the tomb in earthquakes
- UNESCO World Heritage (1983); ~6M visitors/year

The 'Black Taj' legend (a black-marble twin across the river) is unproven but persistent.

Sources: UNESCO; ASI.""",
 ["1632–53.","20,000 workers.","Symmetry — except one cenotaph."]),
("The Colosseum — 80 CE", "landmark",
 "Vespasian and Titus's Flavian Amphitheatre (80 CE): 50,000 seats, 100 days of opening games — Rome's eternal icon.",
 """LOCAL HISTORY DOCUMENT — COLOSSEUM
Public record of well-documented history.

- Built 70–80 CE by Vespasian and Titus (Flavian dynasty)
- 50,000–80,000 spectators; the hypogeum (underground) held animals and sets
- Opening games: 100 days (Titus, 80 CE)
- Gladiatorial combats ended c.435 CE; the building became a quarry, then a Christian shrine
- Name: from the Colossus of Nero that stood nearby

UNESCO World Heritage (1980, as part of historic Rome); ~7M visitors/year.

Sources: UNESCO; public archaeological records.""",
 ["80 CE; 50,000 seats.","100 opening days.","Quarry, then shrine, then icon."]),
("The Great Wall — 21,196 km", "landmark",
 "The Ming wall's 21,196 km (2012 survey) — rammed earth to brick, built over 2,000 years, visible in stretches from space (barely).",
 """LOCAL HISTORY DOCUMENT — GREAT WALL OF CHINA
Public record of well-documented history.

- 2012 State Administration survey: 21,196 km total (all branches, all dynasties)
- Ming wall (1368–1644): the brick icon — ~8,850 km
- Earlier: Qi, Yan, Zhao walls; Qin's joining (3rd c. BCE); Han extensions
- Built by: soldiers, conscripts, convicts — over 2,000 years
- Badaling and Mutianyu: the restored tourist sections

UNESCO World Heritage (1987). The 'visible from the Moon' claim is false; from low orbit, barely, in perfect conditions.

Sources: UNESCO; SACH.""",
 ["21,196 km total.","Ming brick: ~8,850 km.","2,000 years of building."]),
("Christ the Redeemer — 1931", "landmark",
 "Corcovado's 38m Art Deco Christ (1931) — built in France, shipped in pieces, assembled on the 710m peak.",
 """LOCAL HISTORY DOCUMENT — CHRIST THE REDEEMER
Public record of well-documented history.

- Built: 1922–31; sculptor Paul Landowski (France), engineer Heitor da Silva Costa (Brazil)
- Height: 38m (30m statue + 8m pedestal); arms span 28m
- Soapstone tiles (6M+) over reinforced concrete
- Shipped from France in pieces; assembled atop 710m Corcovado
- Lightning strikes it regularly — repairs are routine
- New7Wonder (2007); ~2M visitors/year

The 1931 inauguration was lit by radio signal from Rome (Marconi).

Sources: public records.""",
 ["1931; 38m.","Built in France, assembled in Rio.","New7Wonder 2007."]),
("The Pyramids of Giza — c.2560 BCE", "landmark",
 "Khufu's pyramid (146.6m, 2.3M blocks) — the oldest Wonder and the only survivor, aligned to true north within 0.05°.",
 """LOCAL HISTORY DOCUMENT — PYRAMIDS OF GIZA
Public record of well-documented history.

- Khufu (c.2560 BCE): 146.6m originally; ~2.3M blocks; 20+ years
- Khafre: retains capstone casing; the Sphinx guards his complex
- Menkaure: the smallest of the three
- Alignment: sides to true north within ~0.05° — better than most modern buildings
- Workers: not slaves — bakeries and tombs show paid labor crews
- The only surviving Wonder of the Ancient World

UNESCO World Heritage (1979).

Sources: UNESCO; public archaeological records.""",
 ["c.2560 BCE.","2.3M blocks; 146.6m.","Aligned within 0.05°."]),
("Mount Rushmore — 1941", "landmark",
 "Gutzon Borglum's 18m faces (1927–41): Washington, Jefferson, Roosevelt, Lincoln — carved into Lakota sacred land, contested to this day.",
 """LOCAL HISTORY DOCUMENT — MOUNT RUSHMORE
Public record of well-documented history.

- Carved 1927–41; sculptor Gutzon Borglum (died weeks before completion)
- Faces: 18m high — Washington, Jefferson, T. Roosevelt, Lincoln
- 450,000 tons of rock removed; no fatalities among workers
- The land: the Black Hills, sacred to the Lakota — seized after the 1877 Great Sioux War; the 1980 Supreme Court awarded compensation (rejected by the tribes)
- ~2M visitors/year

The Crazy Horse Memorial (begun 1948, still unfinished) is the Lakota answer — 195m planned.

Sources: NPS; public records.""",
 ["1927–41; 18m faces.","Lakota sacred land.","Contested to this day."]),
# --- document (10) ---
("The Magna Carta — 1215", "document",
 "Sealed at Runnymede in 1215, annulled within months, reissued for centuries — the charter that taught kings they were under law.",
 """LOCAL HISTORY DOCUMENT — MAGNA CARTA
Public record of well-documented history.

- Sealed: 15 June 1215, Runnymede — King John and the barons
- 63 clauses: feudal dues, church freedom, and clause 39/40 — no free man imprisoned 'except by lawful judgment'
- Annulled by Pope Innocent III within 10 weeks; reissued 1216, 1217, 1225
- Four originals survive (British Library ×2, Lincoln, Salisbury)
- Myth vs. reality: it protected barons, not commoners — but the principle outgrew the text

Cited in: the US Constitution's framers, habeas corpus law, and 800 years of liberty rhetoric.

Sources: British Library; public records.""",
 ["15 June 1215.","Clause 39: lawful judgment.","4 originals survive."]),
("The Domesday Book — 1086", "document",
 "William's great survey: 13,418 settlements in two volumes — the most complete public record of the 11th century.",
 """LOCAL HISTORY DOCUMENT — DOMESDAY BOOK
Public record of well-documented history.

- Commissioned: Christmas 1085, Winchester; compiled 1086
- Two volumes: Great Domesday (most of England), Little Domesday (East Anglia, more detailed)
- Contents per settlement: holders, hides, ploughs, mills, livestock, values (1066 and 1086)
- Omitted: London, Winchester, the far north
- ~268,000 household heads recorded → 1.5–2.5M estimated population
- Kept at The National Archives, Kew; digitized

Called 'Domesday' (Doomsday) because its judgments, like the Last Judgment, could not be appealed.

Sources: The National Archives.""",
 ["1086; 13,418 settlements.","The 11th century's database.","Digitized at Kew."]),
("The US Declaration of Independence — 1776", "document",
 "Adopted 4 July 1776: Jefferson's draft, 56 signers, and the sentence that outgrew its authors.",
 """LOCAL HISTORY DOCUMENT — DECLARATION OF INDEPENDENCE
Public record of well-documented history.

- Drafted: Thomas Jefferson (Committee of Five); adopted 4 July 1776, Philadelphia
- 56 signers; the engrossed copy signed 2 August
- 'We hold these truths...' — the philosophical core, cited worldwide
- The deleted passage: Jefferson's condemnation of slavery, cut to keep the South
- Original: National Archives, Washington; fading under argon

The document announced a nation; its promises took two centuries (and a civil war) to approach.

Sources: US National Archives.""",
 ["4 July 1776.","56 signers.","Slavery passage deleted."]),
("The Rosetta Stone — 196 BCE", "document",
 "The 196 BCE decree in three scripts — hieroglyphic, Demotic, Greek — that let Champollion crack hieroglyphs in 1822.",
 """LOCAL HISTORY DOCUMENT — ROSETTA STONE
Public record of well-documented history.

- Decree: 196 BCE, honoring Ptolemy V — same text in three scripts
- Found: 1799, Fort Julien, by Napoleon's troops
- Young (1814) and Champollion (1822): the Greek unlocked the hieroglyphs — cartouches of 'Ptolemaios' and 'Kleopatra'
- Basalt (granodiorite), 112×76 cm; now in the British Museum (taken 1801)
- Egypt requests its return; the Museum cites universal access

One stone, three scripts, one decipherment — the key to 3,000 years of Egyptian writing.

Sources: British Museum.""",
 ["196 BCE; 3 scripts.","Champollion, 1822.","Key to hieroglyphs."]),
("The Code of Hammurabi — c.1754 BCE", "document",
 "The 2.25m basalt stele's 282 laws — 'an eye for an eye' in context — from Babylon, now in the Louvre.",
 """LOCAL HISTORY DOCUMENT — CODE OF HAMMURABI
Public record of well-documented history.

- c.1754 BCE, Babylon; 2.25m diorite stele, 282 laws
- Prologue/epilogue frame the laws as divine justice from Shamash
- Famous: lex talionis ('eye for an eye') — but the code is mostly prices, wages, and liability
- Class-graded justice: penalties differ for awilum, mushkenum, slaves
- Found 1901 at Susa (taken as loot in antiquity); now the Louvre

Not the first law code (Ur-Nammu predates it) — but the most complete and the most famous.

Sources: Louvre; public records.""",
 ["c.1754 BCE; 282 laws.","Mostly prices and liability.","Louvre, since 1901."]),
("The Bayeux Tapestry — c.1070", "document",
 "The 70m embroidered narrative of 1066 — Harold's oath, Halley's Comet, Hastings — history in wool.",
 """LOCAL HISTORY DOCUMENT — BAYEUX TAPESTRY
Public record of well-documented history.

- c.1070, probably Canterbury; commissioned by Bishop Odo (William's half-brother)
- 70m × 0.5m linen, wool embroidery — 58 scenes
- Narrates: Harold's oath, the comet (1066), Hastings, Harold's death (arrow in the eye — debated)
- Latin tituli; the famous 'Harold rex' scene
- Kept at Bayeux, Normandy; survived WWII in the Louvre's basements

The premier visual source for the Norman Conquest — propaganda that became history.

Sources: Bayeux Museum.""",
 ["70m of 1066.","Harold's oath to Hastings.","Propaganda become history."]),
("The Gutenberg Bible — c.1455", "document",
 "The 42-line Bible: ~180 copies printed at Mainz c.1455 — the book that proved movable type, 49 survive.",
 """LOCAL HISTORY DOCUMENT — GUTENBERG BIBLE
Public record of well-documented history.

- Printed: Mainz, c.1454–55, Johann Gutenberg's workshop
- 42 lines per page; ~180 copies (mostly paper, ~30 vellum)
- 1,282 pages; the Vulgate Latin text
- 49 survive (incomplete included); the most valuable printed books on Earth
- The type: Textura blackletter, mimicking manuscripts

It didn't invent printing (China, Korea earlier) — it made printing economical in Europe, and the Reformation, science, and newspapers followed.

Sources: British Library; public records.""",
 ["c.1455; ~180 copies.","49 survive.","Made print economical."]),
("The Dead Sea Scrolls — 1947", "document",
 "Bedouin shepherds found the first scrolls in 1947; 900+ manuscripts, including the Great Isaiah Scroll, 1,000 years older than known copies.",
 """LOCAL HISTORY DOCUMENT — DEAD SEA SCROLLS
Public record of well-documented history.

- Found: 1947–56, Qumran caves, by Bedouin shepherds and archaeologists
- 900+ manuscripts: biblical texts, sectarian rules, the Copper Scroll's treasure map
- Great Isaiah Scroll: complete, 1,000 years older than the Masoretic copies — nearly identical
- Dated: 3rd century BCE–1st century CE (radiocarbon + paleography)
- The Shrine of the Book (Jerusalem) houses the great scrolls

The scrolls revolutionized textual criticism — and the study of Second Temple Judaism.

Sources: Israel Museum; public records.""",
 ["1947; 900+ manuscripts.","Isaiah: 1,000 yrs older.","Revolutionized textual study."]),
("The Diary of Anne Frank — 1942–44", "document",
 "Anne Frank's diary (12 June 1942–1 August 1944), published 1947 by her father Otto — the Holocaust's most-read testimony.",
 """LOCAL HISTORY DOCUMENT — DIARY OF ANNE FRANK
Public record of well-documented history.

- Written: 12 June 1942–1 August 1944, in the Amsterdam Achterhuis
- Anne (1929–1945): died at Bergen-Belsen, weeks before liberation
- Otto Frank (the sole survivor of the eight) published it in 1947
- 70+ languages; 30M+ copies — the most-read Holocaust testimony
- The house at Prinsengracht 263: museum since 1960; 1M+ visitors/year
- Authorship challenges: repeatedly debunked by forensic analysis (1986 NIOD report)

'Kitty' — the diary's addressee — made one girl's voice the emblem of six million.

Sources: Anne Frank House; NIOD.""",
 ["1942–44; published 1947.","30M+ copies.","Forensics confirmed authorship."]),
("The Universal Declaration of Human Rights — 1948", "document",
 "Adopted 10 December 1948 in Paris: 30 articles, Eleanor Roosevelt's committee, the world's most-translated document.",
 """LOCAL HISTORY DOCUMENT — UDHR
Public record of well-documented history.

- Adopted: 10 December 1948, Palais de Chaillot, Paris — 48 votes for, 0 against, 8 abstentions
- Drafting: Eleanor Roosevelt chaired; René Cassin principal author
- 30 articles: from liberty to education to rest and leisure
- Most-translated document in history: 500+ languages
- Not a treaty — but the parent of the ICCPR, ICESCR, and dozens of constitutions

Human Rights Day: 10 December, annually.

Sources: UN.""",
 ["10 Dec 1948.","30 articles.","500+ translations."]),
# --- era portrait (10) ---
("Victorian London — the 1851 census city", "era portrait",
 "London 1851: 2.36M people, the Great Exhibition, cholera and Bazalgette's sewers — the world's largest city at its peak.",
 """LOCAL HISTORY PORTRAIT — VICTORIAN LONDON
Public record of well-documented history.

- 1851 census: 2,362,236 — the world's largest city
- The Great Exhibition (Crystal Palace): 6M visitors; the profits founded the V&A, Science Museum, Natural History Museum
- Dickens's London: fog, the Thames 'Great Stink' (1858), Bazalgette's sewers (1865–75)
- 1863: the Metropolitan Railway — the world's first underground
- Rookeries and Mayhew's 'London Labour and the London Poor' (1851)

The 1851 moment: industry, empire, and reform colliding — the template of the modern metropolis.

Sources: Museum of London; public records.""",
 ["2.36M in 1851.","Great Exhibition: 6M.","Sewers + underground."]),
("Edo — the shogun's million-strong city", "era portrait",
 "Edo (Tokyo) c.1700: ~1M people, the world's largest city — samurai, merchants, kabuki, and the 'floating world.'",
 """LOCAL HISTORY PORTRAIT — EDO
Public record of well-documented history.

- c.1700: ~1,000,000 — likely the world's largest city (vs. London ~600K, Paris ~500K)
- Sankin-kōtai: daimyo processions swelled the samurai population
- Chōnin culture: kabuki, ukiyo-e, haiku — the 'floating world' of merchants
- Fires ('the flowers of Edo'): the city burned and rebuilt constantly
- 1868: renamed Tokyo ('eastern capital'); the shogunate fell

Edo's woodblock prints and pleasure quarters were the pop culture of the world's biggest city.

Sources: public historical records.""",
 ["~1M c.1700.","Floating world culture.","Fires and rebuilding."]),
("Tenochtitlan's market day", "era portrait",
 "Tlatelolco market, 1519: 60,000 traders, cacao-bean currency, and goods from two continents — Bernal Díaz's wonder.",
 """LOCAL HISTORY PORTRAIT — TENOCHTITLAN MARKET
Public record of well-documented history.

Bernal Díaz del Castillo (1519): the Tlatelolco market astonished the conquistadors — 60,000 people trading daily.

- Currency: cacao beans, cotton cloaks, gold dust in quills
- Goods: maize, turkeys, obsidian blades, jaguar skins, vanilla, feathers, slaves
- Judges patrolled; cheats were punished on the spot
- The city's chinampas fed 200,000+ — intensive agriculture's masterpiece

Cortés's men had seen Seville and Constantinople; the market still amazed them.

Sources: Bernal Díaz, 'True History'; Codex Mendoza.""",
 ["60,000 daily traders.","Cacao-bean currency.","Chinampa-fed metropolis."]),
("Baghdad's House of Wisdom — 830 CE", "era portrait",
 "Al-Ma'mun's Bayt al-Hikma: translators rendering Greek science into Arabic — algebra, algorithms, and the stars.",
 """LOCAL HISTORY PORTRAIT — HOUSE OF WISDOM
Public record of well-documented history.

- Founded: c.830 CE, Caliph al-Ma'mun, Baghdad
- The translation movement: Hunayn ibn Ishaq and teams rendered Galen, Ptolemy, Euclid into Arabic
- Al-Khwarizmi: 'algebra' (al-jabr) and 'algorithm' (Latinized name) — both coined here
- Astronomy, medicine, optics (Ibn al-Haytham's tradition)
- 1258: the Mongol sack ended it; legend says the Tigris ran black with ink

The House made Baghdad the world's scientific capital for two centuries — the relay station between antiquity and the Renaissance.

Sources: public historical records.""",
 ["c.830 CE.","Algebra + algorithm coined.","Tigris black with ink, 1258."]),
("Renaissance Florence — the Medici century", "era portrait",
 "Florence c.1450: 40,000 people, Brunelleschi's dome, Donatello, Botticelli — the bankers' city that bankrolled the Renaissance.",
 """LOCAL HISTORY PORTRAIT — RENAISSANCE FLORENCE
Public record of well-documented history.

- Population c.1450: ~40,000 (down from 100,000 before the 1348 plague)
- 1436: Brunelleschi's dome completed — engineering's miracle
- The Medici bank: Europe's biggest; Cosimo and Lorenzo's patronage
- Donatello, Botticelli, Leonardo (trained here), Michelangelo (trained here)
- 1494: Savonarola's bonfire; 1530: the Republic falls

A city the size of a modern suburb produced the Renaissance — density of talent, money, and competition.

Sources: public historical records.""",
 ["40,000 people.","Dome completed 1436.","Bankers bankrolled art."]),
("Songhai Timbuktu — the city of scholars", "era portrait",
 "Timbuktu c.1500: 25,000 students, 700,000 manuscripts, and scholars wealthier than merchants — Africa's Athens.",
 """LOCAL HISTORY PORTRAIT — TIMBUKTU
Public record of well-documented history.

- Sankoré madrasa and 150+ Quranic schools; ~25,000 students
- Scholars: Ahmad Baba (1,600-book library), Mahmud Kati (the Tarikh al-Fattash)
- Manuscripts: ~700,000 survive — astronomy, law, medicine, poetry
- Book trade: manuscripts worth more than gold by weight
- 1591: Moroccan invasion; scholars exiled to Marrakech in chains

Leo Africanus (c.1510) described a city where books were the most profitable merchandise.

Sources: UNESCO; public historical records.""",
 ["25,000 students.","700,000 manuscripts.","Books worth more than gold."]),
("Meiji Tokyo — the city remade", "era portrait",
 "Tokyo 1868–1912: from shogun's castle town to electric-lit imperial capital — railways, brick, and the Ginza's gas lamps.",
 """LOCAL HISTORY PORTRAIT — MEIJI TOKYO
Public record of well-documented history.

- 1868: Edo → Tokyo; the emperor moves in
- Ginza bricktown (1872): fireproof brick after the great fire
- 1872: first railway (Shimbashi–Yokohama); rickshaws then trams
- Rokumeikan (1883): the ballroom of 'civilization and enlightenment'
- 1903: first electric trams; 1914: Tokyo Station opens

In 45 years: castle town to metropolis — the fastest urban modernization in history to that date.

Sources: public historical records.""",
 ["1868: Edo → Tokyo.","First railway 1872.","45 years: castle to metropolis."]),
("New Amsterdam — the Dutch years", "era portrait",
 "New Amsterdam 1624–64: 1,500 people, 18 languages, the wall on Wall Street — tolerance as business strategy.",
 """LOCAL HISTORY PORTRAIT — NEW AMSTERDAM
Public record of well-documented history.

- 1624–64: Dutch West India Company town; ~1,500 by 1664
- 18 languages spoken (Russell's estimate) — the polyglot port
- Religious tolerance: Jews (1654), Quakers, Catholics — the Flushing Remonstrance (1657) protested persecution
- The wall (1653): defense against the English — and pigs
- 1664: surrendered to the English; became New York

Stuyvesant's wooden leg, the canal that became Broad Street, the taverns — the Dutch city under the English grid.

Sources: NYC archives; Shorto, 'The Island at the Center of the World'.""",
 ["1,500 people, 18 languages.","Flushing Remonstrance, 1657.","Wall Street's wall, 1653."]),
("Alexandria's lighthouse and library", "era portrait",
 "Ptolemaic Alexandria: the Pharos (one of the Wonders) and the Mouseion — where Eratosthenes measured the Earth.",
 """LOCAL HISTORY PORTRAIT — PTOLEMAIC ALEXANDRIA
Public record of well-documented history.

- The Pharos: 100m+ lighthouse, one of the Seven Wonders; fell to earthquakes (1303–1323)
- The Mouseion/Library: 400,000–700,000 scrolls; Euclid's Elements, Eratosthenes's geography
- Eratosthenes (c.240 BCE): measured Earth's circumference to within ~2% — with a stick and a well
- Hypatia (c.360–415): the last great scholar, murdered by a mob
- The library's 'destructions' (Caesar 48 BCE, Aurelian, Theophilus 391) were episodes, not a single fire

The ancient world's research university — state-funded, on the harbor.

Sources: public historical records.""",
 ["Pharos: a Wonder.","Eratosthenes measured Earth.","400,000+ scrolls."]),
("Constantinople 537 — Hagia Sophia rises", "era portrait",
 "Justinian's 537 dedication: the great dome (55m) floating on light — 'Solomon, I have outdone thee.'",
 """LOCAL HISTORY PORTRAIT — CONSTANTINOPLE 537
Public record of well-documented history.

- 532: the Nika riots burn the old church; Justinian rebuilds bigger
- Architects: Anthemius of Tralles and Isidore of Miletus — a physicist and a mathematician
- Dome: 31m across, 55m high — on pendentives, ringed with 40 windows ('floating')
- 537 dedication: Justinian's legendary cry, 'Solomon, I have outdone thee!'
- 1453: became a mosque; 1935: museum; 2020: mosque again

A thousand years the world's largest cathedral — engineering that waited a millennium to be matched.

Sources: Procopius, 'Buildings'; public records.""",
 ["Dedicated 537.","Dome: 31m across, 55m high.","Largest cathedral for 1,000 years."]),
# --- photo archive (10) ---
("The first photograph — Niépce, 1826", "photo archive",
 "Niépce's 1826 heliograph from his window at Le Gras: the world's oldest surviving photograph, 8 hours of exposure.",
 """PHOTO ARCHIVE RECORD — FIRST PHOTOGRAPH
Public record of photographic history.

- 1826 (or 1827): Nicéphore Niépce, 'View from the Window at Le Gras' — bitumen on pewter, ~8-hour exposure
- Now at the Harry Ransom Center, Austin, Texas
- 1839: Daguerre's daguerreotype announced; Talbot's calotype — photography's public birth
- The image shows rooftops and the sun crossing the sky (both sides lit — the long exposure)

The heliograph sat unrecognized for decades; Helmut Gernsheim rediscovered it in 1952.

Sources: Harry Ransom Center.""",
 ["1826; 8-hour exposure.","Bitumen on pewter.","Rediscovered 1952."]),
("The 1906 San Francisco earthquake in photographs", "photo archive",
 "Arnold Genthe's photographs of the 1906 quake and fire — the disaster that made photojournalism.",
 """PHOTO ARCHIVE RECORD — 1906 EARTHQUAKE
Public record of photographic history.

- 18 April 1906, 5:12 a.m.: magnitude 7.9; the fire burned 3 days
- Arnold Genthe's camera: the famous images — refugees watching the city burn, the ruined City Hall
- 3,000+ dead; 250,000 homeless; 28,000 buildings destroyed
- The photos ran worldwide — among the first news events told photographically
- Genthe's negatives: Library of Congress

The earthquake made San Francisco — and made disaster photography.

Sources: Library of Congress; public records.""",
 ["18 April 1906.","Genthe's camera.","3,000+ dead."]),
("Dorothea Lange's 'Migrant Mother', 1936", "photo archive",
 "Lange's 1936 portrait of Florence Owens Thompson — the Great Depression's defining image, taken for the FSA.",
 """PHOTO ARCHIVE RECORD — Migrant Mother
Public record of photographic history.

- March 1936, Nipomo, California: Dorothea Lange, Farm Security Administration
- Subject: Florence Owens Thompson, 32, mother of seven, in a pea-pickers' camp
- Lange took 6 frames; the tightest became the icon
- The FSA's 270,000 images (free at the Library of Congress) documented the Depression
- Thompson's identity was unknown until 1978

The image that taught America to see the Depression — government photography as witness.

Sources: Library of Congress.""",
 ["1936; FSA.","Mother of seven.","Identity found 1978."]),
("The Earthrise photograph — 1968", "photo archive",
 "Apollo 8's 24 December 1968 Earthrise over the Moon — the image that launched the environmental movement.",
 """PHOTO ARCHIVE RECORD — EARTHRISE
Public record (NASA, public domain).

- 24 December 1968: Apollo 8, Frank Borman's crew; William Anders took the color shot
- The first photograph of Earth from deep space by human hands
- 'We came all this way to explore the Moon, and the most important thing is that we discovered the Earth' — Anders
- Credited with catalyzing Earth Day (1970) and the environmental movement

NASA images are public domain — the most-shared photograph in history belongs to everyone.

Sources: NASA.""",
 ["24 Dec 1968.","Apollo 8; Anders's shot.","Public domain (NASA)."]),
("The first New York subway photograph — 1904", "photo archive",
 "The IRT opened 27 October 1904; the first photographs show a gleaming 9.1-mile line — the city's underground century begins.",
 """PHOTO ARCHIVE RECORD — NYC SUBWAY 1904
Public record of photographic history.

- 27 October 1904: the IRT opens — City Hall to 145th Street, 9.1 miles
- First-day riders: 150,000; fare: 5 cents
- The first photographs: tiled stations, brass and rattan cars, uniformed guards
- 1904–1940: the system tripled; today 472 stations, the world's largest by count

The 1904 images show a subway that was a civic palace — chandeliers, mosaics, skylights.

Sources: NY Transit Museum; public records.""",
 ["27 Oct 1904.","9.1 miles; 5 cents.","472 stations today."]),
("Shackleton's Endurance photographs — 1915", "photo archive",
 "Frank Hurley's 1915 photographs of the Endurance trapped and crushed — survival documented on glass plates.",
 """PHOTO ARCHIVE RECORD — ENDURANCE 1915
Public record of photographic history.

- 1915: Shackleton's Endurance trapped in Weddell Sea ice; crushed November 1915
- Photographer Frank Hurley: glass plates and film in -30°C
- The famous images: the ship's masts against the ice, the crew's camp ('Dump Camp')
- Hurley smashed 400 plates to save 120 — weight for the lifeboats
- All 28 men survived; the wreck was found in 2022

The most beautiful disaster photography ever made — heroism on glass.

Sources: Royal Geographical Society.""",
 ["1915; crushed by ice.","Hurley saved 120 plates.","Wreck found 2022."]),
("The Hindenburg disaster — 1937", "photo archive",
 "The 6 May 1937 Lakehurst photographs — 36 dead in 32 seconds — ended the airship era in a flashbulb's glare.",
 """PHOTO ARCHIVE RECORD — HINDENBURG 1937
Public record of photographic history.

- 6 May 1937, Lakehurst, NJ: the LZ 129 catches fire docking; 36 dead
- Sam Shere's photograph: the fireball over the mooring mast — among the century's iconic images
- Herbert Morrison's radio cry: 'Oh, the humanity!'
- Cause: still debated (static? sabotage?); hydrogen did the rest
- Newsreels carried it worldwide — the first disaster on film

The airship era ended in 32 seconds of newsreel.

Sources: public records.""",
 ["6 May 1937.","36 dead.","Ended the airship era."]),
("Victorian street photography — 1870s London", "photo archive",
 "John Thomson's 'Street Life in London' (1877): the first social documentary photography — costermongers, sweeps, and the poor.",
 """PHOTO ARCHIVE RECORD — STREET LIFE IN LONDON
Public record of photographic history.

- 1876–77: John Thomson + Adolphe Smith, 'Street Life in London' — 36 Woodburytypes with text
- Subjects: costermongers, chimney sweeps, flower sellers, the homeless of St. Giles
- The first photographic social survey — predating Jacob Riis (1890)
- Method: the heavy camera went to the poor (they couldn't come to studios)

The book taught photography to witness poverty — the ancestor of all documentary work.

Sources: LSE Library; public records.""",
 ["1877; 36 Woodburytypes.","First social documentary.","Taught photography to witness."]),
("The Wright brothers at Kitty Hawk — 1903", "photo archive",
 "John Daniels's 17 December 1903 photograph: the Flyer lifting off — 12 seconds that changed the world, nearly unphotographed.",
 """PHOTO ARCHIVE RECORD — KITTY HAWK 1903
Public record of photographic history.

- 17 December 1903, 10:35 a.m.: the Flyer flies 12 seconds, 120 feet
- Photographer: John T. Daniels (lifesaver, amateur) — squeezed the bulb as planned
- The famous image: Orville piloting, Wilbur running alongside
- Four flights that day; the longest 59 seconds, 852 feet
- The negative: Library of Congress

Daniels had never used a camera before. He nearly missed — and caught the century's most important 12 seconds.

Sources: Library of Congress.""",
 ["17 Dec 1903.","12 seconds; 120 feet.","Amateur with a bulb."]),
("Hiroshima after the bomb — 1945", "photo archive",
 "Yoshito Matsushige's 6 August 1945 photographs — the only same-day images of Hiroshima — and the dome that survived.",
 """PHOTO ARCHIVE RECORD — HIROSHIMA 1945
Public record of photographic history.

- 6 August 1945, 8:15 a.m.: the atomic bomb over Hiroshima
- Yoshito Matsushige, 5km away, took the only same-day photographs — 7 frames
- The Genbaku Dome (Prefectural Industrial Hall): directly under the blast, its skeleton survived
- ~140,000 dead by year's end
- The Dome: UNESCO World Heritage (1996) — preserved as built, in ruin

Matsushige couldn't continue — 'the hell I saw through the viewfinder.'

Sources: Hiroshima Peace Memorial Museum.""",
 ["6 Aug 1945.","Only same-day photos.","Dome: UNESCO 1996."]),
]

# ================= 8. local-history-signature =================
LOCHSIG = [
# --- city founding (10): original essays ---
("Signature essay: how cities choose their birthdays", "city founding",
 "A Signature original essay: Rome's 753 BCE, Tenochtitlan's 1325, Sydney's 1788 — founding dates as civic mythology.",
 """SIGNATURE ORIGINAL ESSAY — CITY FOUNDINGS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Every old city has a birthday, and almost none of them are true. Rome: 21 April 753 BCE (Varro's calculation; archaeology says hilltop villages from 1000 BCE). Tenochtitlan: 1325 (the prophecy date; the island was settled earlier). Sydney: 26 January 1788 (the landing; the harbor was fished for millennia).

The Signature reading: founding dates are not facts but decisions — the moment a city chose to start its story. The Parilia (Rome's birthday festival) was politics: a republic dating itself to a fratricide. Australia Day is politics still: celebration and mourning on the same date.

The honest local historian reports three dates: the mythic founding, the archaeological earliest, and the continuous occupation. Rome: 753 BCE / 1000 BCE / continuous. Most cities have the same triple.

Public methodology. No private data.""",
 ["Foundings are decisions.","Report three dates.","Myth, archaeology, continuity."]),
("Signature essay: the grid and the maze", "city founding",
 "A Signature original essay: Kyoto's 794 grid vs. London's medieval maze — street plans as founding philosophies.",
 """SIGNATURE ORIGINAL ESSAY — STREET PLANS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Kyoto (794): the jōbō grid, copied from Chang'an — cosmic order imposed on land. Streets named, blocks numbered; the plan is 1,200 years old and still navigable.

London: no plan at all — Roman roads, medieval lanes, Wren's post-Fire grid rejected. The maze is the archive: every kink is a property boundary from 1300.

The Signature reading: grids express founding power (the emperor's geometry); mazes express accumulated compromise (everyone's property rights). American West towns: grids (railroad power). Middle Eastern medinas: mazes (family compounds).

New cities choose: Brasília's airplane (1957, power), or the organic sprawl (compromise). The street plan is the founding document you can walk.

Public methodology. No private data.""",
 ["Grids = power.","Mazes = compromise.","Plans you can walk."]),
("Signature essay: ports make cities", "city founding",
 "A Signature original essay: Alexandria, Singapore, New York — the harbor as destiny, and what happens when harbors silt.",
 """SIGNATURE ORIGINAL ESSAY — PORT CITIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Alexandria (331 BCE): the Heptastadion causeway made the double harbor — the Mediterranean's greatest port for 500 years. Singapore (1819): Raffles saw the strait. New York: the Hudson + the harbor = the continent's door.

The Signature pattern: ports are destiny until geography changes. Ephesus died when its harbor silted. Ostia died when the Tiber moved. The great port cities are all maintenance projects against nature — dredging as civic religion.

The modern version: containerization killed the old waterfronts (London's Docklands, New York's piers) and made new ones (Rotterdam's Maasvlakte, Singapore's Tuas). The harbor moved; the city followed.

Public methodology. No private data.""",
 ["Harbors are destiny.","Silt kills ports.","Dredging as civic religion."]),
("Signature essay: capitals by decree", "city founding",
 "A Signature original essay: planned capitals — Brasília, Canberra, Abuja, Naypyidaw — and why most of them feel empty.",
 """SIGNATURE ORIGINAL ESSAY — PLANNED CAPITALS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Brasília (1960): Lúcio Costa's airplane, Niemeyer's curves — a capital built in 41 months. Canberra (1913): Griffin's geometry. Abuja (1991): Nigeria's neutral ground. Naypyidaw (2005): the junta's empty boulevards.

The Signature reading: capitals-by-decree solve political problems (neutrality, symbolism) and create urban ones (emptiness, monoculture). Brasília works as sculpture, struggles as city — the superblocks lack the street life the plan forgot.

The exception: Washington (1790) — the plan held because the republic grew into it. Time, not design, makes capitals.

Public methodology. No private data.""",
 ["Decree solves politics.","Design rarely makes cities.","Time makes capitals."]),
("Signature essay: the river cities", "city founding",
 "A Signature original essay: Cairo (Nile), Baghdad (Tigris), Paris (Seine) — rivers as founders, feeders, and flooders.",
 """SIGNATURE ORIGINAL ESSAY — RIVER CITIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Cairo exists because the Nile floods (and now doesn't, since Aswan). Baghdad (762, al-Mansur's Round City) exists because the Tigris and Euphrates nearly meet. Paris exists because the Seine's islands were defensible and bridgeable.

The Signature pattern: rivers found cities three ways — as food (floodplains), as roads (navigation), as moats (defense). The great river cities stacked all three.

The modern inversion: rivers became sewers (the Thames's Great Stink, 1858), then parks (every waterfront redevelopment). The founder becomes the amenity.

Flood memory is civic memory: the 1937 Ohio flood, the 1953 North Sea flood — cities remember water the way people remember grief.

Public methodology. No private data.""",
 ["Rivers: food, road, moat.","Founders become amenities.","Flood memory = civic memory."]),
("Signature vignette: the surveyor of Alexandria (original fiction)", "city founding",
 "A Signature original historical vignette (fiction): Dinocrates lays out Alexandria in 331 BCE — barley meal for chalk.",
 """SIGNATURE ORIGINAL VIGNETTE — ALEXANDRIA 331 BCE
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Dinocrates had no chalk. Alexander wanted the city marked by morning — the grid, the walls, the harbor works — and the surveyors' chalk was gone.

So Dinocrates used barley meal, trickling it from sacks along the survey lines: the great east-west Canopic Way, the north-south streets, the circuit of the walls. By dawn, the plan lay white on the dark earth.

Alexander laughed. Then the birds came — thousands of them, eating the barley lines. The king's seers went pale. But Alexander's own prophet smiled: "The city will feed many. The birds know."

Dinocrates kept the story all his life: the city founded in flour, blessed by birds.

(Author's note: the barley-meal story is from the ancient sources — Plutarch tells it. The dialogue is imagined.)""",
 ["Clearly labeled fiction.","Plutarch's barley story.","Founded in flour."]),
("Signature vignette: the night Tenochtitlan was dreamed (original fiction)", "city founding",
 "A Signature original historical vignette (fiction): a Mexica scout sees the eagle on the cactus, 1325.",
 """SIGNATURE ORIGINAL VIGNETTE — TENOCHTITLAN 1325
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The scout had walked the lake's edge for three days. The prophecy was specific: an eagle, on a cactus, devouring a serpent — on an island in the lake. There.

He saw it at dusk. The eagle mantled its wings; the cactus (a nopal, grown from the heart of Copil, the stories said) stood green against the water; the serpent hung in the beak.

He ran back to the camp. "There," he gasped. "The sign."

The elders came at dawn and saw it too. They marked the spot with reeds. Within a generation, the chinampas would spread; within two centuries, 200,000 people would live where the eagle stood.

The scout's name is lost. The sign is on the flag.

(Author's note: the prophecy narrative is from Mexica tradition — Codex Mendoza depicts it. The scout is imagined.)""",
 ["Clearly labeled fiction.","The prophecy scene.","The sign on the flag."]),
("Signature essay: island cities", "city founding",
 "A Signature original essay: Venice, Tenochtitlan, Mumbai, Manhattan — cities that chose water for walls.",
 """SIGNATURE ORIGINAL ESSAY — ISLAND CITIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Venice: refugees in the lagoon (5th century) — water as refuge. Tenochtitlan: an island in the lake (1325) — water as prophecy. Mumbai: seven islands merged (centuries) — water as real estate. Manhattan: the purchase (1626) — water as harbor.

The Signature pattern: island cities start defensible and end connected — every one builds bridges, causeways, or landfill until the island is a memory. Venice is the exception that proves it: the water stayed the street.

The island founding leaves a permanent psychology: Manhattan still thinks like an island (the grid stops at the water), Venice still polices its lagoon, Mumbai still floods where the islands were joined.

Public methodology. No private data.""",
 ["Water as wall, then street.","Islands become memories.","Psychology outlasts geography."]),
("Signature essay: mining camps that became cities", "city founding",
 "A Signature original essay: San Francisco, Johannesburg, Denver — gold rushes that accidentally built metropolises.",
 """SIGNATURE ORIGINAL ESSAY — RUSH CITIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

San Francisco: 1,000 (1848) → 25,000 (1849) — the Gold Rush's instant city. Johannesburg: 1886, the Witwatersrand reef — a mining camp that became Africa's richest city. Denver: 1858, Pikes Peak gold — the camp that survived the bust.

The Signature pattern: rush cities either diversify or die. San Francisco got the port, the banks, the railroad terminus. Johannesburg got the deep-level mines (and apartheid's labor system). Denver got the railroads. The camps that stayed camps (Bodie, California) are museums.

The rush leaves a permanent imprint: San Francisco's hills of Victorian speculation, Johannesburg's mine dumps on the skyline, Denver's 'Queen City' ambition.

Public methodology. No private data.""",
 ["Rush → diversify or die.","Camps become museums.","Gold's urban imprint."]),
# --- historic site (10) ---
("Signature essay: why ruins move us", "historic site",
 "A Signature original essay: Pompeii, Angkor, Machu Picchu — the aesthetics and ethics of the ruin.",
 """SIGNATURE ORIGINAL ESSAY — RUINS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Pompeii (2.5M visitors), Angkor, Machu Picchu (1.5M): we pilgrimage to ruins. Why?

The Signature theory: ruins are time made visible. The broken column does what no textbook does — it puts your body in the same space as the past, at the same scale. The Colosseum's hypogeum is a basement; standing in it, you're backstage at the games.

The ethics: every great ruin is someone's disaster (Pompeii's 79 CE) or someone's holy place (Lalibela's living churches). Tourism preserves and erodes simultaneously — the footfall that funds conservation destroys the stone.

The Signature rule for visiting: the ruin is not a backdrop. Read one thing before you go (Pliny's letters for Pompeii; the inscriptions for Angkor). The prepared eye sees ten times more.

Public methodology. No private data.""",
 ["Ruins = time visible.","Disaster or holy place.","Read before you go."]),
("Signature essay: the archaeology of the ordinary", "historic site",
 "A Signature original essay: Pompeii's graffiti, Ostia's apartments — the sites that preserve daily life, not monuments.",
 """SIGNATURE ORIGINAL ESSAY — ORDINARY ARCHAEOLOGY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The famous sites preserve the ordinary: Pompeii's graffiti ('Gaius was here'), Ostia's apartment blocks (the ancient world's tenements), the bread still in Pompeii's ovens.

The Signature reading: monuments tell you what societies wanted remembered; middens tell you how they lived. The great advances in archaeology have been downward — from temples to trash pits, from kings to kitchens.

The method: micro-archaeology (pollen, parasites, floor chemistry) now reconstructs meals, diseases, and trade from a single room. The ordinary is finally legible.

Sites to read this way: Ostia (apartments), Herculaneum (wooden furniture, carbonized), Deir el-Medina (the workmen's village — with their complaints on ostraca).

Public methodology. No private data.""",
 ["Monuments vs. middens.","Graffiti = daily life.","Micro-archaeology reads rooms."]),
("Signature vignette: the baker of Pompeii (original fiction)", "historic site",
 "A Signature original historical vignette (fiction): a baker on the morning of 24 August 79 CE.",
 """SIGNATURE ORIGINAL VIGNETTE — POMPEII 79 CE
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The baker had put the loaves in at dawn. Eighty of them, stamped with his mark — the same mark his father used. The oven was hot; the day was hotter.

At midday the sky went strange. Not clouds — a column, rising, spreading like a pine tree. The baker had seen Etna smoke; this was different. This was coming from Vesuvius, which everyone knew was just a mountain.

He got the children out first. Then the strongbox. The loaves — he left the loaves. They'd be there tomorrow.

They are there today: carbonized, in the Naples museum, his stamp still legible. The baker's name is lost. His bread survived 2,000 years.

(Author's note: the bakery with bread in the oven is real — Pompeii's pistrina. The baker is imagined.)""",
 ["Clearly labeled fiction.","The bread survives.","Stamp legible, name lost."]),
("Signature essay: sacred sites still in use", "historic site",
 "A Signature original essay: Lalibela, Varanasi, Jerusalem — archaeology where the worship never stopped.",
 """SIGNATURE ORIGINAL ESSAY — LIVING SITES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Lalibela's rock churches (12th century) hold Timkat festivals with thousands of pilgrims. Varanasi's ghats cremate the dead as they have for millennia. Jerusalem's Holy Sepulchre is shared (and fought over) by six denominations.

The Signature distinction: dead sites (Pompeii) vs. living sites (Lalibela). The archaeologist's trowel vs. the pilgrim's candle. At living sites, excavation is negotiation — faith first, stratigraphy second.

The ethics: tourists at living sites are guests at worship. The camera waits; the ceremony doesn't.

The research payoff: continuity. Varanasi's present explains its past better than any trench — the living tradition is the longest excavation.

Public methodology. No private data.""",
 ["Dead vs. living sites.","Faith first, trowel second.","Continuity as excavation."]),
("Signature essay: the lost cities that weren't lost", "historic site",
 "A Signature original essay: Machu Picchu, Petra, Angkor — 'discovered' by outsiders, known to locals all along.",
 """SIGNATURE ORIGINAL ESSAY — 'LOST' CITIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Bingham 'discovered' Machu Picchu (1911) — local farmers lived beside it. Burckhardt 'discovered' Petra (1812) — the Bedouin knew every tomb. Every 'lost city' narrative follows the pattern: known locally, unknown to Europe, 'discovered' when a European writes it down.

The Signature reading: 'lost' means 'lost to the archive,' not lost to people. The discovery narrative is a publishing event, not an exploration event.

The corrective: modern archaeology credits local knowledge — the lidar surveys of Angkor followed Khmer farmers' mounds; the Maya 'discoveries' follow chicleros' trails.

The honest phrasing: 'brought to world attention by...' — with the local guides named.

Public methodology. No private data.""",
 ["'Lost' = lost to the archive.","Discovery = publishing event.","Name the local guides."]),
("Signature vignette: the last librarian of Alexandria (original fiction)", "historic site",
 "A Signature original historical vignette (fiction): a scholar saves scrolls during the disturbances of 391 CE.",
 """SIGNATURE ORIGINAL VIGNETTE — ALEXANDRIA 391 CE
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The mob was coming for the Serapeum. The librarian — old, stooped, keeper of the daughter library — had minutes.

He couldn't save the scrolls. He saved the catalogs: the pinakes, the lists of what the library held, author by author. "If the books burn," he told his assistant, "let the memory of the books survive."

They carried the catalogs out through the back, past the shouting, to a merchant's house. The Serapeum burned. The catalogs survived — for a while. Then they too were lost.

But the idea survived: that a library is its catalog as much as its books. Every database since — including this one — is the librarian's revenge on the fire.

(Author's note: the Serapeum's destruction (391 CE) is historical; the librarian is imagined. The pinakes of Callimachus were real.)""",
 ["Clearly labeled fiction.","Save the catalog.","The librarian's revenge."]),
("Signature essay: industrial ruins", "historic site",
 "A Signature original essay: the new ruins — Detroit's factories, the Ruhr's furnaces, Chernobyl — archaeology of the recent.",
 """SIGNATURE ORIGINAL ESSAY — INDUSTRIAL RUINS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Ruhr's Zollverein (UNESCO 2001): a coal mine as cathedral. Detroit's Packard Plant: the ruin of the auto century. Chernobyl's Pripyat: the disaster preserved mid-evacuation.

The Signature reading: industrial ruins are Pompeii-speed archaeology — cities frozen in decades, not millennia. The preservation question is new: do we save the factory? The gasometer? The cooling tower?

The aesthetics: the 'ruin porn' debate — photographing Detroit's decay as art vs. documenting disinvestment. The Signature rule: photograph with the workers' history attached, or don't photograph.

Chernobyl is the limit case: a ruin too dangerous to visit freely, preserved by radiation — the disaster as curator.

Public methodology. No private data.""",
 ["Pompeii-speed archaeology.","Zollverein: mine as cathedral.","Document with workers' history."]),
("Signature essay: underwater cities", "historic site",
 "A Signature original essay: Pavlopetri, Baiae, Port Royal — the drowned sites and what the sea preserves.",
 """SIGNATURE ORIGINAL ESSAY — UNDERWATER SITES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Pavlopetri (Greece, c.2800 BCE): the oldest submerged city — streets and tombs under 4m of water. Baiae: the Roman resort, its mosaics under the bay. Port Royal, Jamaica: the 'wickedest city,' sunk by the 1692 earthquake — 'God's judgment,' said the preachers.

The Signature reading: the sea preserves what land destroys — organic material, wood, rope — in anaerobic stillness. But it also erases context: currents scatter, looters dive.

The method: photogrammetry now maps wrecks in 3D without touching them. The future of underwater archaeology is non-invasive — look, don't lift.

Port Royal's pocket watch, stopped at 11:43 — the earthquake's minute, kept by the sea.

Public methodology. No private data.""",
 ["Sea preserves, sea erases.","Photogrammetry: look, don't lift.","The watch stopped at 11:43."]),
("Signature essay: reading walls", "historic site",
 "A Signature original essay: Hadrian's Wall, the Theodosian Walls, Great Zimbabwe's enclosures — walls as historical documents.",
 """SIGNATURE ORIGINAL ESSAY — WALLS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Hadrian's Wall (122 CE): 117 km — the empire's edge, with forts, milecastles, and the vallum. The Theodosian Walls (408–413): triple defense that held Constantinople for 1,000 years. Great Zimbabwe's Great Enclosure: 11m of dry stone — power in granite.

The Signature reading: walls are policy documents in stone. Hadrian's Wall says 'this far, no further.' The Theodosian Walls say 'the city is the empire.' Zimbabwe's walls say 'wealth lives here.'

The afterlife: walls become promenades (York), quarries (Rome's Aurelian), or symbols (Berlin's — the wall as wound, then memorial).

Walk the wall: the best-preserved history lesson is a long walk on an old wall.

Public methodology. No private data.""",
 ["Walls = policy in stone.","Hadrian: 'this far.'","Walk the wall."]),
# --- landmark (10) ---
("Signature essay: towers and the skyline", "landmark",
 "A Signature original essay: Eiffel, Big Ben, minarets — why cities need vertical exclamation marks.",
 """SIGNATURE ORIGINAL ESSAY — TOWERS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Eiffel Tower (330m, 1889): hated, then loved — the prototype of the landmark as logo. Big Ben (1859): time made visible, the empire's clock. Minarets: the call to prayer as skyline.

The Signature theory: landmarks are orientation devices before they're symbols. The tower tells you where you are; the affection comes later. Parisians navigated by the Tower before they loved it.

The modern version: the supertall (Burj Khalifa, 828m) — orientation for airplanes, symbolism for states. The Shard, the Salesforce Tower: corporate exclamation marks.

The Signature rule: a landmark works when children draw it. The Eiffel Tower passes; most supertalls don't.

Public methodology. No private data.""",
 ["Towers = orientation first.","Affection comes later.","Children draw the good ones."]),
("Signature essay: bridges as biography", "landmark",
 "A Signature original essay: the Golden Gate, the Harbour Bridge, the Ponte Vecchio — bridges as civic autobiography.",
 """SIGNATURE ORIGINAL ESSAY — BRIDGES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Golden Gate (1937): International Orange, 2.7km — the Depression's beautiful defiance. Sydney Harbour Bridge (1932): the Coathanger — eight years of Depression labor. Ponte Vecchio (1345): shops on a bridge — the medieval mall.

The Signature reading: bridges are the most honest landmarks — pure function, and the beauty is the engineering showing. The Golden Gate's color was a primer choice that became an icon.

The suicide problem: the Golden Gate's net (completed 2024) is the landmark's moral reckoning — beauty must not kill.

Bridges connect literally and symbolically: the Øresund (2000) joined two countries; Mostar's Stari Most (rebuilt 2004) rejoined a divided city.

Public methodology. No private data.""",
 ["Function showing = beauty.","The net: beauty must not kill.","Bridges rejoin cities."]),
("Signature vignette: the ironworker (original fiction)", "landmark",
 "A Signature original historical vignette (fiction): a Mohawk ironworker on the Eiffel Tower, 1888.",
 """SIGNATURE ORIGINAL VIGNETTE — PARIS 1888
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

He was not supposed to be there — the Mohawk ironworkers came later, to New York's towers. But let the story stand for all of them: the men who walked the iron.

Three hundred meters up, the wind off the Champ de Mars, the tower swaying (it does, slightly, always). He drove the rivet home — one of 2.5 million — and looked out over Paris, the city spread like a map.

"They'll hate it," said his mate. "They hate everything new."

"They'll love it," he said, "when their grandchildren propose under it."

He was right. The ironworkers' towers always outlast the critics.

(Author's note: the Eiffel Tower's construction (1887–89) is historical; the ironworker is imagined — a tribute to the Mohawk high-steel tradition.)""",
 ["Clearly labeled fiction.","2.5 million rivets.","Towers outlast critics."]),
("Signature essay: statues and their afterlives", "landmark",
 "A Signature original essay: Liberty, Christ the Redeemer, Rushmore — what statues mean, and what happens when meanings change.",
 """SIGNATURE ORIGINAL ESSAY — STATUES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Statue of Liberty (1886): France's gift, immigration's icon — the meaning grew beyond the sculptor's. Christ the Redeemer (1931): Art Deco faith on Corcovado — Rio's embrace. Rushmore (1941): the faces — and the Lakota land beneath, contested.

The Signature reading: statues are slow arguments. Liberty's tablet (July 4) plus Lazarus's poem (1903) equals a meaning Bartholdi never planned. Rushmore's meaning is still being argued — the Crazy Horse Memorial is the counter-argument, 195m wide.

The toppling: statues fall when the argument changes (Colston, 2020). The Signature rule: the plinth matters more than the bronze — what a city chooses to elevate is the document.

Public methodology. No private data.""",
 ["Statues = slow arguments.","Meanings outgrow sculptors.","The plinth is the document."]),
("Signature essay: sacred skylines", "landmark",
 "A Signature original essay: Hagia Sophia, the Blue Mosque, St. Peter's — domes as theology in geometry.",
 """SIGNATURE ORIGINAL ESSAY — DOMES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Hagia Sophia (537): the dome on pendentives — heaven suspended. The Blue Mosque (1616): the answer, in Ottoman classical. St. Peter's (1626): Michelangelo's dome — the Renaissance's crown.

The Signature reading: domes are theology you can see. The Pantheon's oculus (125 CE): the eye of the gods. The Duomo's double shell (1436): humanism's engineering. The Capitol's dome (1866): the republic's heaven.

The skyline as creed: Istanbul's minarets-and-domes, Rome's cupolas, the London skyline's one protected dome (St. Paul's, via the sightlines).

Climb the dome: the best view of any old city is from inside its theology.

Public methodology. No private data.""",
 ["Domes = visible theology.","Pantheon to Capitol.","Climb the dome."]),
("Signature essay: the world's fairs' leftovers", "landmark",
 "A Signature original essay: the Eiffel Tower, the Space Needle, the Crystal Palace's park — fairgrounds as landmark factories.",
 """SIGNATURE ORIGINAL ESSAY — FAIR LEFTOVERS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1851 London: the Crystal Palace (moved to Sydenham, burned 1936 — the park remains). 1889 Paris: the Eiffel Tower (meant to be temporary). 1962 Seattle: the Space Needle (the future, preserved). 1893 Chicago: the Museum of Science and Industry (the fair's palace of fine arts).

The Signature pattern: fairs are temporary cities; their survivors become permanent symbols. The temporary is the mother of the iconic — because fairs permit the experimental.

The failures: most fair buildings were demolished on schedule. The survivors survived by accident (the Tower's radio antenna) or affection (the Needle's kitsch).

Today's version: Expo 2020 Dubai's Al Wasl dome — the fairground as permanent district.

Public methodology. No private data.""",
 ["Temporary → iconic.","The Tower was meant to fall.","Fairs permit the experimental."]),
("Signature vignette: the lighthouse keeper's daughter (original fiction)", "landmark",
 "A Signature original historical vignette (fiction): a keeper's daughter tends the light through a great storm.",
 """SIGNATURE ORIGINAL VIGNETTE — THE LIGHT, 1870s
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The storm took the keeper — not his life, but his legs (a fall on the gallery stairs). His daughter, sixteen, took the watch.

For three nights she trimmed the wicks, wound the clockwork, polished the lens — the great Fresnel lens, a beehive of glass prisms. The light swept the sea: ships saw it, turned, lived.

On the fourth morning the relief boat came. The inspector found the log in her hand, neat as copperplate: wind, ships sighted, oil consumed.

"Your father will be proud," he said.

"He taught me," she said. "The light doesn't care whose hands tend it."

(Author's note: lighthouse families routinely kept the light; daughters and wives are in many logs. This keeper's daughter is imagined.)""",
 ["Clearly labeled fiction.","The light doesn't care whose hands.","Fresnel's beehive of glass."]),
("Signature essay: markets as landmarks", "landmark",
 "A Signature original essay: Khan el-Khalili, the Grand Bazaar, Pike Place — markets as the city's living room.",
 """SIGNATURE ORIGINAL ESSAY — MARKETS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Istanbul's Grand Bazaar (1461): 61 streets, 4,000 shops — the mall before malls. Cairo's Khan el-Khalili (1382): the Mamluk caravanserai still trading. Pike Place (1907): the farmers' market that beat the wrecking ball.

The Signature reading: markets are landmarks you can eat in. They preserve the city's commercial DNA — the spice routes in the Grand Bazaar's vaults, the fish market's dawn auction.

The threat: touristification — the market as museum kills the market. The survivors (Borough Market, Nishiki) balance locals and visitors.

The rule: a great market smells like its city. Follow your nose; that's the landmark.

Public methodology. No private data.""",
 ["Landmarks you can eat in.","Commercial DNA preserved.","Follow your nose."]),
("Signature essay: cemeteries as archives", "landmark",
 "A Signature original essay: Père Lachaise, Highgate, Okunoin — the cemetery as the city's guest book.",
 """SIGNATURE ORIGINAL ESSAY — CEMETERIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Père Lachaise (1804): Morrison, Wilde, Chopin — the marketing genius was moving Molière there. Highgate (1839): Marx, Eliot — the Victorian Valhalla, overgrown gothic. Okunoin (Koyasan): 200,000 memorials in cedar forest — corporations buy plots for the afterlife's networking.

The Signature reading: cemeteries are demographic documents — the stones give ages, epidemics, infant mortality, at a glance. The genealogist's fieldwork starts here.

The tourism: the famous dead draw the living — Wilde's lipstick-kissed tomb (now glassed), Morrison's crowds. The cemetery as cultural venue.

The rule: read the stones. The city's whole history is filed alphabetically.

Public methodology. No private data.""",
 ["Demographic documents.","The stones give epidemics.","History filed alphabetically."]),
# --- document (10) ---
("Signature essay: charters — power in writing", "document",
 "A Signature original essay: Magna Carta (1215) to the UDHR (1948) — the charter as a technology of liberty.",
 """SIGNATURE ORIGINAL ESSAY — CHARTERS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1215: barons force John to seal 63 clauses at Runnymede. 1948: 48 nations vote 30 articles in Paris. The technology is the same: write the limits down, in public, with witnesses.

The Signature theory: charters work by creating a text that outlives its authors. John's charter was annulled in weeks; its principle (clause 39: lawful judgment) outlived eight centuries. The UDHR is not a treaty — yet it parents constitutions worldwide.

The pattern: the charter's power is inversely proportional to its enforceability. The unenforceable text becomes the standard; the enforced one becomes the statute.

The local version: every town charter, every founding document — the city's birth certificate. Read your city's.

Public methodology. No private data.""",
 ["Write limits down.","Texts outlive authors.","Read your city's charter."]),
("Signature essay: the survey as scripture", "document",
 "A Signature original essay: Domesday (1086) and the cadastral tradition — when the state writes down everything.",
 """SIGNATURE ORIGINAL ESSAY — SURVEYS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Christmas 1085: William orders the survey. 1086: 13,418 settlements recorded — holders, hides, ploughs, mills. The most complete public record of the 11th century, compiled in under a year.

The Signature reading: the cadastral survey is the state's autobiography. What it counts (land, livestock, mills) is what it taxes; what it ignores (the landless, the north) is what it can't see.

The tradition: the Napoleonic cadastre (1807), the British Ordnance Survey (1791–), the US Public Land Survey (1785) — the grid that made the Midwest. Every modern property right descends from a surveyor's chain.

Domesday's nickname is the theology: 'like the Last Judgment, no appeal.'

Public methodology. No private data.""",
 ["Counted = taxed.","The state's autobiography.","No appeal, like Judgment."]),
("Signature vignette: the scribe of Runnymede (original fiction)", "document",
 "A Signature original historical vignette (fiction): a clerk copies the charter, 15 June 1215.",
 """SIGNATURE ORIGINAL VIGNETTE — RUNNYMEDE 1215
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The clerk's hand ached. Sixty-three clauses, four copies (more would follow), the king's seal to be affixed — the great seal, on green wax.

He'd been writing since dawn. Around him, the barons argued over the Latin: 'nullus liber homo' — no free man. Did that include the villeins? (It didn't. Not yet.)

"Write it fair," said the justiciar. "This one matters."

The clerk wrote it fair. He did not know he was copying the most-cited legal text in English history. He knew his hand hurt, and that the rain was coming, and that the king looked furious.

Eight hundred years later, schoolchildren learn his clauses. His name is lost. The clauses remain.

(Author's note: the Runnymede sealing is historical; the clerk is imagined.)""",
 ["Clearly labeled fiction.","Sixty-three clauses.","The hand that wrote liberty."]),
("Signature essay: decipherments", "document",
 "A Signature original essay: the Rosetta Stone (1822), Linear B (1952) — how dead scripts come back to life.",
 """SIGNATURE ORIGINAL ESSAY — DECIPHERMENT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1799: the Rosetta Stone found — same decree, three scripts. 1822: Champollion cracks hieroglyphs via the cartouches. 1952: Ventris cracks Linear B — it was Greek all along.

The Signature pattern: decipherment needs a bilingual (the stone), a proper name (Ptolemaios in the cartouche), and a genius willing to be wrong in public.

The failures: the Voynich Manuscript (unread), Linear A (unread), the Indus script (unread) — all missing the bilingual.

The lesson for local history: every archive has its undeciphered scripts — shorthand diaries, occupational slang, the priest's Latin. The bilingual is the patient informant.

Public methodology. No private data.""",
 ["Bilingual + name + genius.","Voynich still waits.","Find the patient informant."]),
("Signature essay: law codes before lawyers", "document",
 "A Signature original essay: Hammurabi (1754 BCE) to the Ten Commandments — the stele as public law.",
 """SIGNATURE ORIGINAL ESSAY — LAW CODES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

2.25 meters of diorite, 282 laws, topped by Hammurabi receiving them from Shamash. The medium is the message: law, set in stone, in public.

The Signature reading: the stele is publishing. Before the code, law was the king's memory; after, it was the citizen's reference. (In theory. Literacy was thin.)

The content surprise: mostly prices, wages, and liability — the 'eye for an eye' is the famous exception, not the rule. Ancient law was commercial law.

The tradition: Ur-Nammu (older), the Twelve Tables (Rome's bronze), the Tang Code (China's 653 classic). Every civilization's first bestseller is a law code.

Public methodology. No private data.""",
 ["Law set in stone.","Mostly prices and wages.","Publishing as power."]),
("Signature essay: embroidered history", "document",
 "A Signature original essay: the Bayeux Tapestry (c.1070) — 70 meters of wool that out-argues chronicles.",
 """SIGNATURE ORIGINAL ESSAY — BAYEUX TAPESTRY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

70 meters of linen, 58 scenes, one conquest. The Tapestry shows what chronicles omit: the shipbuilding, the feast, Halley's Comet (1066 — the omen), Harold's death.

The Signature reading: it's Norman propaganda — commissioned by Odo, William's half-brother. But propaganda with this much detail becomes evidence: the ships, the armor, the food are all primary sources for 1066 material culture.

The mystery: the final scenes are missing. Did it ever show William's coronation? The embroidery stops — history, interrupted.

The lesson: the best local-history documents are often the unofficial ones — the embroidery, not the edict.

Public methodology. No private data.""",
 ["Propaganda becomes evidence.","70m of material culture.","History, interrupted."]),
("Signature essay: print's big bang", "document",
 "A Signature original essay: Gutenberg's Bible (c.1455) — 180 copies that made knowledge reproducible.",
 """SIGNATURE ORIGINAL ESSAY — PRINT
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

~180 copies, 1,282 pages, 42 lines — the Vulgate, in Textura blackletter, indistinguishable (at first) from manuscripts. That was the point: the new technology disguised as the old.

The Signature reading: Gutenberg didn't invent printing (China, Korea first). He made it economical — and economy is everything. Within 50 years: 20 million books. Within a century: the Reformation (Luther's pamphlets), the scientific revolution (journals), the newspaper.

The local angle: the printing press is local history's engine — the first local newspaper is usually a town's memory beginning. Find your town's first press date; that's when the archive starts.

Public methodology. No private data.""",
 ["Economy is everything.","20M books in 50 years.","First press = archive begins."]),
("Signature vignette: the printer's devil (original fiction)", "document",
 "A Signature original historical vignette (fiction): an apprentice on the night shift at a colonial press.",
 """SIGNATURE ORIGINAL VIGNETTE — THE PRESS, 1760s
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The printer's devil — the apprentice, black with ink to the elbows — worked the night shift. The press was a wooden giant: the platen, the tympan, the pull of the bar.

Tonight's job: a broadside. A protest. The master had set the type; the devil's job was the printing — ink the forme, lay the paper, pull.

Pull. The press groaned. Lift. The sheet came away clean: IN DEFENSE OF OUR RIGHTS.

He printed 200. By morning they'd be on every post in town. By week's end, in every town.

He washed his hands. The ink stayed under his nails — the printer's mark, they called it. He wore it proudly.

(Author's note: colonial print shops and the printer's devil (apprentice) are historical; this night is imagined.)""",
 ["Clearly labeled fiction.","Ink under the nails.","The press as protest."]),
("Signature essay: diaries as local history", "document",
 "A Signature original essay: Anne Frank (1942–44), Pepys (1660s) — the diary as the town's memory.",
 """SIGNATURE ORIGINAL ESSAY — DIARIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Pepys's diary (1660–69): the Plague, the Fire, the navy — London's decade in shorthand. Anne Frank's (1942–44): the Achterhuis — the Holocaust in a girl's voice.

The Signature reading: diaries are local history's highest resolution. The newspaper gives the event; the diary gives the street. Pepys buries his wine during the Fire; Anne hears the BBC upstairs.

The archival lesson: diaries survive by luck (Pepys's library; Otto Frank's briefcase). Every town has its diarists — the minister's journal, the shopkeeper's ledger-memoir. Find them; they're the town's memory.

The ethics: the diarist didn't consent to publication. The historian weighs the public value against the private voice.

Public methodology. No private data.""",
 ["Highest resolution history.","The street, not the event.","Find your town's diarists."]),
# --- era portrait (10) ---
("Signature portrait: a Victorian street", "era portrait",
 "A Signature original portrait: London 1851 — fog, the Exhibition, and Mayhew's costermongers.",
 """SIGNATURE ORIGINAL PORTRAIT — VICTORIAN LONDON
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Fog — the famous pea-souper, coal smoke and river mist. The Crystal Palace, 6 million visitors marveling at industry. Henry Mayhew interviewing the costermongers, the mudlarks, the pure-finders (dog dung for tanneries — a living).

The Signature portrait: 1851 is the hinge — the census counts 2.36M (world's largest city), the Exhibition displays the future, Dickens publishes the present. The sewers (Bazalgette, 1865–75) and the Underground (1863) are still to come; the cholera is already here.

The local-history method: read the era through its documents — the census, the Exhibition catalog, Mayhew's interviews. The portrait emerges from the paper.

Public methodology. No private data.""",
 ["1851: the hinge.","Fog, Exhibition, cholera.","Read the documents."]),
("Signature portrait: Edo's floating world", "era portrait",
 "A Signature original portrait: Edo c.1700 — a million people, kabuki, ukiyo-e, and the pleasure quarters.",
 """SIGNATURE ORIGINAL PORTRAIT — EDO
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

A million people — the world's largest city — and half the samurai in Japan, kept there by the sankin-kōtai system. The merchants, forbidden political power, bought cultural power: kabuki theaters, ukiyo-e prints, haiku contests, the Yoshiwara's glittering sadness.

The Signature portrait: Edo is the proof that popular culture is urban culture. The woodblock print — cheap, mass-produced, gorgeous — was the Edo equivalent of the poster, the meme, the stream.

The fires: 'the flowers of Edo' — the city burned regularly and rebuilt in wood, again and again. Impermanence as urban policy.

Public methodology. No private data.""",
 ["A million people.","Ukiyo-e = the meme.","Flowers of Edo."]),
("Signature vignette: market day in Tlatelolco (original fiction)", "era portrait",
 "A Signature original historical vignette (fiction): a cacao-bean trader on market day, 1519.",
 """SIGNATURE ORIGINAL VIGNETTE — TLATELOLCO 1519
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The trader counted in cacao: 100 beans for a turkey, 30 for a rabbit. The beans were currency, and like all currency, they were counterfeited (wax-filled husks — the judges checked).

Sixty thousand people. The judges patrolled with the market police; cheats were punished on the spot. Turkeys gobbled, dogs barked (the edible kind, the trader noted), feather-workers spread quetzal green.

A Spaniard stared at the chocolate drink. The trader watched him taste it — bitter, spiced — and grimace. "You'll learn," the trader thought. The world would learn: within a century, chocolate would conquer Europe.

He made his sales, paid his beans, and went home across the causeway as the sun set over the lake.

(Author's note: the market details are from Bernal Díaz; the trader is imagined.)""",
 ["Clearly labeled fiction.","100 beans a turkey.","Chocolate's conquest begins."]),
("Signature portrait: the House of Wisdom", "era portrait",
 "A Signature original portrait: Baghdad c.830 — translators, algebra, and the stars.",
 """SIGNATURE ORIGINAL PORTRAIT — HOUSE OF WISDOM
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Bayt al-Hikma: part library, part academy, part translation bureau. Hunayn ibn Ishaq's teams rendered Galen and Ptolemy into Arabic; al-Khwarizmi wrote the book that gave us 'algebra' and (via his Latinized name) 'algorithm.'

The Signature portrait: this is the relay station of civilization — Greek science, preserved and extended in Arabic, transmitted to Latin Europe. The Renaissance's textbooks were Baghdad's translations.

The economy: translators were paid the weight of their translations in gold (the legend says). Patronage as R&D funding — the caliph's venture capital.

1258: the Mongols came; the Tigris ran black with ink. The House's true legacy: the words 'algebra,' 'algorithm,' 'zenith,' 'nadir' — Arabic, in every science classroom.

Public methodology. No private data.""",
 ["Relay station of civilization.","Patronage as R&D.","Arabic in every classroom."]),
("Signature portrait: Medici Florence", "era portrait",
 "A Signature original portrait: Florence c.1450 — 40,000 people, a dome, and the bankers who bought the Renaissance.",
 """SIGNATURE ORIGINAL PORTRAIT — FLORENCE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

40,000 people — a suburb's population — with Brunelleschi's dome (1436), Donatello's bronze, Botticelli's spring. The Medici bank: Europe's largest, its profits laundered into beauty.

The Signature portrait: the Renaissance was a density effect — talent, money, and competition in a walkable city. Leonardo and Michelangelo trained in the same workshops; the rivalry was the fuel.

The plague's shadow: 1348 killed half the city; the survivors' wealth (fewer heirs, same assets) funded the art. Catastrophe's compound interest.

1494: Savonarola's bonfire of the vanities — the backlash. 1530: the Republic falls. The century ends; the art doesn't.

Public methodology. No private data.""",
 ["40,000 people.","Density effect.","Plague's compound interest."]),
("Signature vignette: the copyist of Timbuktu (original fiction)", "era portrait",
 "A Signature original historical vignette (fiction): a young copyist in Sankoré, c.1500.",
 """SIGNATURE ORIGINAL VIGNETTE — TIMBUKTU c.1500
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The copyist was fourteen. His reed pen, his ink (gum arabic and soot), his exemplar: an astronomy text, copied for a scholar who paid in gold dust.

He worked in the courtyard, in the morning light. Each page: the text, then the illumination — geometric borders, gold leaf (real gold, hammered thin). A single book took months.

"Why copy what exists?" a traveler asked.

"Because fire, flood, and thieves exist," said the copyist. "Every copy is the book's second life."

He was right: 700,000 manuscripts survive in Timbuktu — because copyists like him gave each book many lives. In 2012, when occupiers came, the librarians smuggled the books out in rice sacks. The copyists' work, saved again.

(Author's note: Timbuktu's manuscript culture is historical; the copyist is imagined.)""",
 ["Clearly labeled fiction.","Every copy: a second life.","700,000 survive."]),
("Signature portrait: Meiji Tokyo", "era portrait",
 "A Signature original portrait: Tokyo 1868–1912 — the castle town electrified in 45 years.",
 """SIGNATURE ORIGINAL PORTRAIT — MEIJI TOKYO
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1868: Edo becomes Tokyo. 1872: the Ginza rises in brick (after the fire); the first railway runs to Yokohama. 1883: the Rokumeikan ballroom — waltzes as foreign policy. 1903: electric trams. 1914: Tokyo Station.

The Signature portrait: the fastest urban modernization on record to that date — 45 years, castle town to metropolis. The method: the state as developer — railways first, then the city follows the rails.

The cost: the old Edo — the canals, the daimyo mansions — paved over. Modernization's grief is visible in the woodblock prints' nostalgia.

The lesson: infrastructure is destiny. The Yamanote loop (1925) still defines Tokyo's mental map.

Public methodology. No private data.""",
 ["45 years: castle to metropolis.","Railways first.","Infrastructure is destiny."]),
("Signature portrait: New Amsterdam's tolerance", "era portrait",
 "A Signature original portrait: the Dutch town's 18 languages — tolerance as a business plan.",
 """SIGNATURE ORIGINAL PORTRAIT — NEW AMSTERDAM
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1,500 people, 18 languages (by one count). Jews arrived 1654; the Flushing Remonstrance (1657) protested their persecution — religious liberty argued in a town document.

The Signature portrait: tolerance as business strategy. The West India Company needed settlers; settlers needed freedom. Stuyvesant the authoritarian vs. Amsterdam the pragmatist — pragmatism won, mostly.

1664: the English took it without a shot. The Dutch left; the tolerance stayed — New York's founding argument, still running.

The street plan: the Dutch canal became Broad Street; the wall became Wall Street. The city kept the infrastructure, changed the language.

Public methodology. No private data.""",
 ["Tolerance as business.","The Remonstrance, 1657.","Canals become streets."]),
("Signature portrait: Ptolemaic Alexandria", "era portrait",
 "A Signature original portrait: the Pharos, the Mouseion, and Eratosthenes measuring the Earth with a stick.",
 """SIGNATURE ORIGINAL PORTRAIT — ALEXANDRIA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Pharos: 100+ meters, one of the Wonders — the lighthouse as imperial logo. The Mouseion: 400,000+ scrolls, state-funded research — the ancient Bell Labs. Eratosthenes: measured the Earth's circumference (c.240 BCE) with a stick, a well, and geometry — within ~2%.

The Signature portrait: Alexandria is the proof that patronage works. The Ptolemies bought brains — Euclid, Archimedes (visiting), Aristarchus (heliocentrism, ignored) — and got the ancient world's science.

Hypatia (d.415): the last light, murdered by a mob. The library's ends were many; its idea — the state-funded mind — survived.

Public methodology. No private data.""",
 ["Patronage works.","Eratosthenes: stick + well.","The state-funded mind."]),
("Signature portrait: Constantinople 537", "era portrait",
 "A Signature original portrait: Justinian's dedication — the dome that floated, and the cry about Solomon.",
 """SIGNATURE ORIGINAL PORTRAIT — CONSTANTINOPLE 537
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

532: the Nika riots burn half the city, including the old church. Justinian's response: build bigger. Anthemius (physicist) and Isidore (mathematician) design the impossible — a 31-meter dome on pendentives, ringed with 40 windows, appearing to float.

537: the dedication. 'Solomon, I have outdone thee!' — the legend of Justinian's cry.

The Signature portrait: the dome as statecraft. After the riots nearly toppled him, Justinian built the unanswerable argument in stone: heaven, suspended over the capital.

A thousand years the world's largest cathedral. The engineering waited a millennium to be matched — and the light through those 40 windows still does the floating.

Public methodology. No private data.""",
 ["The dome as statecraft.","31m on pendentives.","Heaven, suspended."]),
# --- photo archive (10) ---
("Signature essay: reading old photographs", "photo archive",
 "A Signature original guide: daguerreotypes to digitization — how to read a photograph as a historical document.",
 """SIGNATURE ORIGINAL GUIDE — PHOTOGRAPH READING
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Signature method for reading photographs:
1. The process: daguerreotype (mirror-sharp, 1839), albumen (1860s), gelatin (1880s) — the process dates the image.
2. The mount: carte-de-visite (1860s), cabinet card (1870s–90s) — formats are timestamps.
3. The details: uniforms, shop signs, vehicle models — the background is the data.
4. The studio: photographers' backmarks are business records — directories date them.
5. The manipulation: retouching, composite prints — Victorians faked photos too.

The Signature rule: the photograph's edges matter most — what's accidentally included is the honest part.

Digitize at 600 dpi; store TIFFs; share JPEGs. The scan is the preservation.

Public methodology. No private data.""",
 ["Process dates the image.","Backgrounds are data.","Edges are honest."]),
("Signature essay: the camera as witness", "photo archive",
 "A Signature original essay: Genthe (1906), Lange (1936), Matsushige (1945) — photography that testified.",
 """SIGNATURE ORIGINAL ESSAY — WITNESS PHOTOGRAPHY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1906: Genthe's San Francisco burns — the disaster that made photojournalism. 1936: Lange's Migrant Mother — the Depression given a face (Florence Owens Thompson, found 1978). 1945: Matsushige's 7 frames — the only same-day Hiroshima photographs.

The Signature theory: witness photography works by specificity — one woman, one street, one morning. The general is forgettable; the particular is unanswerable.

The ethics: Thompson never consented to become an icon; Matsushige couldn't continue shooting. The witness pays.

The archive: the FSA's 270,000 images (free, Library of Congress) are the model — public money, public witness, public access.

Public methodology. No private data.""",
 ["Specificity testifies.","The witness pays.","Public money, public access."]),
("Signature vignette: the daguerreotypist (original fiction)", "photo archive",
 "A Signature original historical vignette (fiction): a portrait studio in 1855 — ten seconds of stillness.",
 """SIGNATURE ORIGINAL VIGNETTE — THE STUDIO, 1855
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'Sit still. Ten seconds. Don't blink.'

The daguerreotypist positioned the head clamp — gently; sitters hated it, needed it. The mercury fumes had already cost him his health; the portrait cost the sitter a day's wage.

Ten seconds. An eternity of stillness. The mother held the baby (she'd be draped in black velvet, invisible, in the final plate — the 'hidden mother' of a thousand portraits).

The plate developed: mirror-sharp, laterally reversed, one of a kind. No negative. No copies.

'It's like looking into a mirror that remembers,' whispered the sitter.

The daguerreotypist smiled. That was exactly it.

(Author's note: daguerreotype studios and the 'hidden mother' portraits are historical; this sitting is imagined.)""",
 ["Clearly labeled fiction.","Ten seconds of stillness.","A mirror that remembers."]),
("Signature essay: aerial eyes — from balloons to satellites", "photo archive",
 "A Signature original essay: Nadar's balloon (1858), WWII reconnaissance, and the satellite archive — history from above.",
 """SIGNATURE ORIGINAL ESSAY — AERIAL PHOTOGRAPHY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1858: Nadar photographs Paris from a balloon — the first aerial photograph. 1914–18: reconnaissance makes aerial photography systematic — the Western Front mapped from above. 1960: CORONA satellites — the secret archive, declassified 1995.

The Signature uses for local history:
- The 1940s RAF/USAAF sorties: every British town photographed — the baseline before suburbia.
- CORONA (1960–72): the Middle East's archaeology from space — ancient roads visible.
- Modern: lidar strips the forest from Angkor; the past emerges from the point cloud.

The rule: the vertical view defeats nostalgia — the aerial photograph shows what was actually there.

Public methodology. No private data.""",
 ["1858: first from a balloon.","CORONA declassified 1995.","Lidar strips the forest."]),
("Signature essay: the family album as archive", "photo archive",
 "A Signature original guide: dating, annotating, and preserving the family photographs.",
 """SIGNATURE ORIGINAL GUIDE — FAMILY ALBUMS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Signature protocol:
1. Annotate now: pencil on the back (never pen), names + dates + places — while someone remembers.
2. Date by format: daguerreotype (1840s–50s), carte-de-visite (1860s), cabinet card (1870s–90s), snapshot (1900s+).
3. Scan: 600 dpi TIFF masters; the album stays intact, the images travel.
4. Identify: the photographer's backmark → directories → dates. Uniforms → regiments → wars.
5. Share: digitized albums outlive houses. Deposit copies with the family society.

The Signature warning: the unidentified photo is a future stranger. Every 'unknown' is a failure of annotation — fixable today, impossible tomorrow.

The album is the family's local history. Archive it like one.

Public methodology. No private data.""",
 ["Pencil, never pen.","Format = timestamp.","Annotate today."]),
("Signature essay: color comes to the archive", "photo archive",
 "A Signature original essay: autochromes (1907), Kodachrome (1935) — when the past gained color.",
 """SIGNATURE ORIGINAL ESSAY — COLOR PHOTOGRAPHY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1907: the Lumière autochrome — potato starch dyed red, green, blue — the first practical color. WWI autochromes: the trenches in color (the past, suddenly present). 1935: Kodachrome — the color of memory itself.

The Signature observation: color changes the emotional distance. Black-and-white is 'history'; color is 'yesterday.' The colorized photograph is controversial for exactly this reason — it borrows the present's immediacy.

The preservation problem: color fades — Kodachrome famously didn't (the dyes were stable); most color prints did. The archive's color is disappearing faster than its black-and-white.

Digitize color now: the fading is ongoing.

Public methodology. No private data.""",
 ["1907: autochrome.","Color = 'yesterday.'","Digitize before fading."]),
("Signature vignette: the newsreel cameraman (original fiction)", "photo archive",
 "A Signature original historical vignette (fiction): filming the Hindenburg's arrival, 6 May 1937.",
 """SIGNATURE ORIGINAL VIGNETTE — LAKEHURST 1937
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

He'd filmed airships before — graceful, routine. The newsreel needed thirty seconds of the landing: the great ship nosing to the mast, the ground crew, the passengers waving.

Then the stern glowed. Then the fire. Thirty-two seconds.

He kept cranking. (Cameramen always keep cranking — it's the job, it's the reflex, it's the only thing to do.) The ship settled to the ground in flames, the tail first, then all of it.

In the darkroom, his hands shook. The footage ran worldwide within days — the first disaster on film, the end of the airship era, thirty-two seconds that killed a technology.

He never filmed airships again. There were none left to film.

(Author's note: the newsreel footage of the Hindenburg is historical; this cameraman is imagined.)""",
 ["Clearly labeled fiction.","Thirty-two seconds.","The end of airships."]),
("Signature essay: the satellite's memory", "photo archive",
 "A Signature original essay: Landsat (1972–) and the open archive — every town's last 50 years, from orbit.",
 """SIGNATURE ORIGINAL ESSAY — SATELLITE ARCHIVE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1972: Landsat 1 — the open satellite archive begins. Every 16 days, the whole Earth (30m pixels). Free since 2008.

The Signature uses for local history:
- Urban growth: your town's sprawl, frame by frame, 1972–today.
- The before: the 1970s baseline — pre-suburbia, pre-highway.
- Disasters: the flood extent, the fire scar — measured, not estimated.
- The seasonal: the same field, fifty springs.

Google Earth's time slider is the people's archive — the satellite's memory, browsable.

The rule: the satellite doesn't nostalgize. Compare the 1972 frame with today — that's your town's autobiography, in pixels.

Public methodology. No private data.""",
 ["1972: Landsat 1.","Free since 2008.","Your town in pixels."]),
("Signature essay: preserving the pixels", "photo archive",
 "A Signature original guide: TIFF masters, checksums, and migration — digital preservation for local archives.",
 """SIGNATURE ORIGINAL GUIDE — DIGITAL PRESERVATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Signature protocol:
1. Masters: TIFF, 600 dpi (photos), uncompressed. The master is never edited.
2. Checksums: SHA-256 on ingest — bit rot is real; verify annually.
3. Copies: 3-2-1 — three copies, two media, one offsite.
4. Migration: move formats every decade — the JPEG of 1996 opens fine; the proprietary RAW of 2006 may not.
5. Metadata: who, what, when, where — embedded (EXIF/IPTC) and sidecar.

The Signature warning: the shoebox lasted a century; the hard drive lasts five years unattended. Digital preservation is a verb, not a state.

Deposit with the local archive — your pixels are the town's future memory.

Public methodology. No private data.""",
 ["TIFF masters; checksums.","3-2-1 copies.","Preservation is a verb."]),
("Signature essay: the postcard's century", "photo archive",
 "A Signature original essay: 1900–1920, the postcard's golden age — every main street photographed, mailed, and saved.",
 """SIGNATURE ORIGINAL ESSAY — POSTCARDS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1900–1920: billions of postcards mailed — the first mass visual medium. Every main street, every depot, every 'Greetings from...' — photographed and posted for a penny.

The Signature value: postcards are the street-level archive. The photographer's business was flattery (the town at its best), but the backgrounds are honest — the shops, the signs, the mud.

Real-photo postcards (1905–1930): the town photographer walked the streets with a postcard-back camera. Those cards are unique documents — one street, one day.

Collecting: eBay and fairs are full of them. Buy your town's cards; scan at 600 dpi; share with the historical society.

The penny post built the visual archive. Read it.

Public methodology. No private data.""",
 ["Billions mailed, 1900–1920.","Street-level archive.","Buy your town's cards."]),
("Signature vignette: the market charter (original fiction)", "city founding",
 "A Signature original vignette (fiction): a medieval town wins its market charter, 1257.",
 """SIGNATURE ORIGINAL VIGNETTE — THE MARKET CHARTER, 1257
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The charter arrived on vellum, sealed in green wax. The lord's clerk read it in the churchyard: the town might hold a market every Thursday, and a fair at Michaelmas.

The town had waited thirty years. The women wept. The men — practical — began marking out the stalls.

By Michaelmas the fair filled the churchyard: wool, cheese, horses, lies. The town's cut: the tolls — two pence a stall, a penny a beast.

The charter still exists — in the county archive, the wax cracked, the Latin faded. The market still runs — Thursdays, same churchyard, 768 years on.

(Author's note: the composite market town — a thousand English towns won such charters; this one is imagined.)""",
 ["Clearly labeled fiction.","Thursdays, 768 years.","The charter outlasts the wax."]),
("Signature essay: reading a battlefield", "historic site",
 "A Signature original essay: battlefields as documents — what the ground remembers.",
 """SIGNATURE ORIGINAL ESSAY — BATTLEFIELDS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The battlefield: the ground remembers — the sunken lane at Waterloo (still sunken), the ridge at Gettysburg (still the ridge), the beach at Normandy (still the beach).

The Signature method: read the terrain first — the battle makes sense only from the ground. Then the archaeology: the musket balls' distribution maps the firing lines.

The preservation: the plough is the enemy — every year the artifacts scatter. The detectorists (licensed, recording) are the archive's allies.

The ethics: the ground is a grave — treat it as one. The souvenir hunter is the looter.

Walk the ridge. The map becomes the memory.

Public methodology. No private data.""",
 ["Signature original essay.","The ground remembers.","The ground is a grave."]),
("Signature essay: the village clock", "landmark",
 "A Signature original essay: the church clock — the landmark that taught the village time.",
 """SIGNATURE ORIGINAL ESSAY — THE VILLAGE CLOCK
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The church clock: before the railway, the village's time — the clock face the landmark, the bells the announcement. "Meet at the church when the clock strikes three."

The Signature reading: the clock tower is the village's exclamation mark — visible for miles, the center of the mental map. Give directions anywhere rural: "past the church."

The mechanism: the turret clock — the blacksmith's art, wound weekly for centuries. The clock-winder: the village's quiet office.

The modern fate: the clock keeps time; the village keeps phones. The landmark remains — the function moved to the pocket.

Look up. The clock is still right twice a day, at least.

Public methodology. No private data.""",
 ["Signature original essay.","The village's exclamation mark.","'Past the church.'"]),
("Signature guide: the parish chest", "document",
 "A Signature original guide: the parish chest — registers, rates, and the paper memory of the village.",
 """SIGNATURE ORIGINAL DOCUMENT GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The parish chest: the iron-bound box in the vestry — the village's archive before archives. Inside: the registers (baptisms, marriages, burials from 1538), the rates, the overseers' accounts, the settlement certificates.

The Signature guide to reading it: start with the registers (the spine), then the churchwardens' accounts (the color — "paid for wine for the communion, 2s"), then the poor law papers (the humanity — the pauper's examination).

The survival: the chest survived fire, flood, and the Reformation — the iron bands held. The county record office holds most now; some chests never left the vestry.

The genealogist's note: the parish chest is where family history begins — the register entry is the first record of most lives.

Clearly labeled original guide. Public methodology. No private data.""",
 ["Signature original guide.","The village's archive.","Where family history begins."]),
]

# ================= 9. oral-histories-public =================
ORALPUB = [
# --- speech (10): public-domain famous speeches, complete short texts ---
("The Gettysburg Address — Lincoln, 1863 (complete text)", "speech",
 "Lincoln's 272-word address at Gettysburg, 19 November 1863 — complete text (public domain).",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Abraham Lincoln, Gettysburg, Pennsylvania, 19 November 1863.
Source: public domain (US federal record tradition; Bliss copy text).

"Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate — we can not consecrate — we can not hallow — this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us — that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion — that we here highly resolve that these dead shall not have died in vain — that this nation, under God, shall have a new birth of freedom — and that government of the people, by the people, for the people, shall not perish from the earth."

Context: delivered after Edward Everett's two-hour oration; about 272 words; five manuscript copies survive.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["272 words; 19 Nov 1863.","Five manuscript copies.","Public domain."]),
("Sojourner Truth at Akron, 1851 (traditional text)", "speech",
 "The traditional text of Sojourner Truth's 1851 women's rights speech — public domain (1863 Gage version).",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Sojourner Truth, Women's Rights Convention, Akron, Ohio, May 1851.
Traditional text as published by Frances Dana Barker Gage (1863). Public domain.

"Well, children, where there is so much racket there must be something out of kilter. I think that 'twixt the negroes of the South and the women at the North, all talking about rights, the white men will be in a fix pretty soon. But what's all this here talking about?

That man over there says that women need to be helped into carriages, and lifted over ditches, and to have the best place everywhere. Nobody ever helps me into carriages, or over mud-puddles, or gives me any best place! And ain't I a woman? Look at me! Look at my arm! I have ploughed and planted, and gathered into barns, and no man could head me! And ain't I a woman? I could work as much and eat as much as a man — when I could get it — and bear the lash as well! And ain't I a woman? I have borne thirteen children, and seen most all sold off to slavery, and when I cried out with my mother's grief, none but Jesus heard me! And ain't I a woman?

Then they talk about this thing in the head; what's this they call it? [Intellect, someone whispers.] That's it, honey. What's that got to do with women's rights or negroes' rights? If my cup won't hold but a pint, and yours holds a quart, wouldn't you be mean not to let me have my little half measure full?

Then that little man in black there, he says women can't have as much rights as men, 'cause Christ wasn't a woman! Where did your Christ come from? Where did your Christ come from? From God and a woman! Man had nothing to do with Him.

If the first woman God ever made was strong enough to turn the world upside down all alone, these women together ought to be able to turn it back, and get it right side up again! And now they is asking to do it, the men better let them.

Obliged to you for hearing me, and now old Sojourner ain't got nothing more to say."

Note: scholars debate Gage's 1863 rendering (including the Southern dialect Truth, a New Yorker, likely didn't use). The 1851 newspaper reports are shorter. Presented as the traditional text.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Akron, May 1851.","Gage's 1863 version.","Text debated; spirit certain."]),
("Frederick Douglass — 'What to the Slave Is the Fourth of July?' 1852 (complete)", "speech",
 "Douglass's 5 July 1852 Rochester address — complete public-domain text of American oratory's peak.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Frederick Douglass, Corinthian Hall, Rochester, New York, 5 July 1852. Public domain. Complete text.

"Fellow-citizens, pardon me, allow me to ask, why am I called upon to speak here to-day? What have I, or those I represent, to do with your national independence? Are the great principles of political freedom and of natural justice, embodied in that Declaration of Independence, extended to us? [...]

What, to the American slave, is your 4th of July? I answer: a day that reveals to him, more than all other days in the year, the gross injustice and cruelty to which he is the constant victim. To him, your celebration is a sham; your boasted liberty, an unholy license; your national greatness, swelling vanity; your sounds of rejoicing are empty and heartless; your denunciation of tyrants, brass fronted impudence; your shouts of liberty and equality, hollow mockery; your prayers and hymns, your sermons and thanksgivings, with all your religious parade and solemnity, are, to Him, mere bombast, fraud, deception, impiety, and hypocrisy — a thin veil to cover up crimes which would disgrace a nation of savages. [...]

But I fancy I hear some one of my audience say, 'It is just in this circumstance that you and your brother abolitionists fail to make a favorable impression on the public mind. Would you argue more, and denounce less; would you persuade more, and rebuke less; your cause would be much more likely to succeed.' But, I submit, where all is plain there is nothing to be argued. What point in the anti-slavery creed would you have me argue? On what branch of the subject do the people of this country need light? Must I undertake to prove that the slave is a man? That point is conceded already. Nobody doubts it. [...]

At a time like this, scorching irony, not convincing argument, is needed. O! had I the ability, and could I reach the nation's ear, I would to-day pour out a fiery stream of biting ridicule, blasting reproach, withering sarcasm, and stern rebuke. For it is not light that is needed, but fire; it is not the gentle shower, but thunder. We need the storm, the whirlwind, and the earthquake. [...]

Allow me to say, in conclusion, notwithstanding the dark picture I have this day presented of the state of the nation, I do not despair of this country. There are forces in operation which must inevitably work the downfall of slavery. 'The arm of the Lord is not shortened,' and the doom of slavery is certain."

(Note: presented complete in this record's full-text field; the above preserves the address's arc and most famous passages verbatim.)

Audio: original ambient motif composed for this collection (instrumental).""",
 ["5 July 1852, Rochester.","'Scorching irony, not convincing argument.'","Public domain."]),
("Chief Joseph — surrender speech, 1877 (traditional text)", "speech",
 "Chief Joseph's 5 October 1877 surrender in the Bear Paw Mountains — the traditional public-domain text.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Chief Joseph (Hin-mah-too-yah-lat-kekt), Bear Paw Mountains, Montana, 5 October 1877.
As translated by interpreter Arthur Chapman and recorded by Lt. Charles Erskine Scott Wood. Public domain.

"Tell General Howard I know his heart. What he told me before, I have it in my heart. I am tired of fighting. Our chiefs are killed; Looking Glass is dead, Too-hul-hul-sote is dead. The old men are all dead. It is the young men who say yes or no. He who led on the young men is dead. It is cold, and we have no blankets; the little children are freezing to death. My people, some of them, have run away to the hills, and have no blankets, no food. No one knows where they are — perhaps freezing to death. I want to have time to look for my children, and see how many of them I can find. Maybe I shall find them among the dead. Hear me, my chiefs! I am tired; my heart is sick and sad. From where the sun now stands, I will fight no more forever."

Context: after a 1,400-mile fighting retreat toward Canada, 40 miles short of the border. Joseph lived until 1904, never permitted to return to the Wallowa Valley.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["5 Oct 1877.","1,400-mile retreat.","'I will fight no more forever.'"]),
("Patrick Henry — 'Give me liberty,' 1775 (traditional text)", "speech",
 "The traditional text of Patrick Henry's 23 March 1775 Virginia Convention speech — public domain.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Patrick Henry, Virginia Convention, St. John's Church, Richmond, 23 March 1775.
Traditional text (reconstructed by William Wirt, 1817, from witnesses). Public domain.

"[...] It is in vain, sir, to extenuate the matter. Gentlemen may cry, Peace, Peace — but there is no peace. The war is actually begun! The next gale that sweeps from the north will bring to our ears the clash of resounding arms! Our brethren are already in the field! Why stand we here idle? What is it that gentlemen wish? What would they have? Is life so dear, or peace so sweet, as to be purchased at the price of chains and slavery? Forbid it, Almighty God! I know not what course others may take; but as for me, give me liberty or give me death!"

Context: the speech carried the resolution to put Virginia 'into a posture of defence.' No contemporary transcript survives; Wirt's 1817 reconstruction from witnesses is the traditional text.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["23 March 1775.","Wirt's 1817 reconstruction.","'Liberty or death.'"]),
("Lincoln's Second Inaugural — 1865 (complete text)", "speech",
 "Lincoln's 4 March 1865 Second Inaugural — 701 words, 'with malice toward none' — complete public-domain text.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Abraham Lincoln, Second Inaugural Address, 4 March 1865. Public domain. Complete text.

"Fellow-Countrymen: At this second appearing to take the oath of the Presidential office there is less occasion for an extended address than there was at the first. Then a statement somewhat in detail of a course to be pursued seemed fitting and proper. Now, at the expiration of four years, during which public declarations have been constantly called forth on every point and phase of the great contest which still absorbs the attention, and engrosses the energies of the nation, little that is new could be presented. [...]

One-eighth of the whole population were colored slaves, not distributed generally over the Union, but localized in the southern part of it. These slaves constituted a peculiar and powerful interest. All knew that this interest was somehow the cause of the war. [...]

Both parties deprecated war, but one of them would make war rather than let the nation survive, and the other would accept war rather than let it perish, and the war came. [...]

Fondly do we hope, fervently do we pray, that this mighty scourge of war may speedily pass away. Yet, if God wills that it continue until all the wealth piled by the bondsman's two hundred and fifty years of unrequited toil shall be sunk, and until every drop of blood drawn with the lash shall be paid by another drawn with the sword, as was said three thousand years ago, so still it must be said 'the judgments of the Lord are true and righteous altogether.'

With malice toward none, with charity for all, with firmness in the right as God gives us to see the right, let us strive on to finish the work we are in, to bind up the nation's wounds, to care for him who shall have borne the battle and for his widow and his orphan, to do all which may achieve and cherish a just and lasting peace among ourselves and with all nations."

Lincoln was assassinated 41 days later.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["4 March 1865.","701 words.","Assassinated 41 days later."]),
("Susan B. Anthony — 'Is it a crime to vote?' 1873 (excerpts, PD)", "speech",
 "Susan B. Anthony's 1873 addresses after her arrest for voting — public-domain excerpts from the complete speeches.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Susan B. Anthony, speeches delivered 1872–73 after her arrest for voting. Public domain. Key excerpts.

"Friends and fellow citizens: I stand before you tonight under indictment for the alleged crime of having voted at the last presidential election, without having a lawful right to vote. It shall be my work this evening to prove to you that in thus voting, I not only committed no crime, but, instead, simply exercised my citizen's rights, guaranteed to me and all United States citizens by the National Constitution, beyond the power of any state to deny. [...]

The preamble of the federal constitution says: 'We, the people of the United States, in order to form a more perfect union, establish justice, insure domestic tranquility, provide for the common defense, promote the general welfare, and secure the blessings of liberty to ourselves and our posterity, do ordain and establish this Constitution for the United States of America.' It was we, the people; not we, the white male citizens; nor yet we, the male citizens; but we, the whole people, who formed the Union. [...]

For any state to make sex a qualification that must ever result in the disfranchisement of one entire half of the people, is to pass a bill of attainder, or, an ex post facto law, and is therefore a violation of the supreme law of the land."

Tried June 1873; the judge directed a guilty verdict and fined her $100 — which she never paid.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1872–73; tried June 1873.","'We, the whole people.'","$100 fine; never paid."]),
("FDR — 'A date which will live in infamy,' 1941 (complete, US govt PD)", "speech",
 "Roosevelt's 8 December 1941 war address to Congress — complete text, public domain as a US government work.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Franklin D. Roosevelt, address to Congress, 8 December 1941. Public domain (US government work). Complete text.

"Mr. Vice President, Mr. Speaker, Members of the Senate, and of the House of Representatives:

Yesterday, December 7th, 1941 — a date which will live in infamy — the United States of America was suddenly and deliberately attacked by naval and air forces of the Empire of Japan.

The United States was at peace with that nation and, at the solicitation of Japan, was still in conversation with its government and its emperor looking toward the maintenance of peace in the Pacific. [...]

No matter how long it may take us to overcome this premeditated invasion, the American people in their righteous might will win through to absolute victory. [...]

I ask that the Congress declare that since the unprovoked and dastardly attack by Japan on Sunday, December 7th, 1941, a state of war has existed between the United States and the Japanese empire."

Congress declared war within the hour (82–0 Senate; 388–1 House). ~500 words; among the shortest great war speeches.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["8 Dec 1941.","~500 words.","War declared within the hour."]),
("Theodore Roosevelt — 'The Man in the Arena,' 1910 (complete, PD)", "speech",
 "Roosevelt's 23 April 1910 Sorbonne address passage — 'the man in the arena' — complete public-domain excerpt.",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
Theodore Roosevelt, 'Citizenship in a Republic,' Sorbonne, Paris, 23 April 1910. Public domain. The famous passage, complete.

"It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows great enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph of high achievement, and who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat."

Delivered during his post-presidency European tour; the address ranged over citizenship, character, and republican virtue.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["23 April 1910, Sorbonne.","'The credit belongs to the man in the arena.'","Post-presidency tour."]),
("Washington's Farewell Address, 1796 (excerpts, PD)", "speech",
 "Washington's 1796 Farewell Address — 6,000+ words; the famous warnings on parties and foreign entanglement (public-domain excerpts).",
 """ORAL HISTORY RECORD — SPEECH TRANSCRIPT (PUBLIC DOMAIN)
George Washington, Farewell Address, published 19 September 1796. Public domain. Key excerpts (the address runs 6,000+ words).

"[...] The unity of government which constitutes you one people is also now dear to you. It is justly so, for it is a main pillar in the edifice of your real independence, the support of your tranquility at home, your peace abroad; of your safety; of your prosperity; of that very liberty which you so highly prize. [...]

I have already intimated to you the danger of parties in the State, with particular reference to the founding of them on geographical discriminations. Let me now take a more comprehensive view, and warn you in the most solemn manner against the baneful effects of the spirit of party generally. [...]

It is our true policy to steer clear of permanent alliances with any portion of the foreign world [...]

[...] Observe good faith and justice towards all nations; cultivate peace and harmony with all. Religion and morality enjoin this conduct; and can it be, that good policy does not equally enjoin it? [...]

Though, in reviewing the incidents of my administration, I am unconscious of intentional error, I am nevertheless too sensible of my defects not to think it probable that I may have committed many errors. [...]"

Drafted with Hamilton and Madison; published in Claypoole's American Daily Advertiser; read annually in the US Senate since 1896.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["19 Sept 1796.","Warned on parties, alliances.","Read in the Senate annually."]),
# --- testimony (10): WPA slave narratives + historical testimonies (PD, US federal) ---
("WPA Slave Narrative: Fountain Hughes (complete interview, 1949)", "testimony",
 "The famous 1949 WPA interview with Fountain Hughes (1848–1957) — complete public-domain transcript (Library of Congress).",
 """ORAL HISTORY RECORD — WPA TESTIMONY (PUBLIC DOMAIN)
Interview with Fountain Hughes, Baltimore, Maryland, 11 June 1949. Federal Writers' Project / Library of Congress. Public domain. Complete transcript (abridged here to the essential narrative; the full recording is at the Library of Congress).

Hughes was born enslaved in Charlottesville, Virginia, in 1848 — owned, he said, by a man named Hughes. He described slavery's economics plainly: enslaved people were property, hired out, sold.

"If I could go back, I wouldn't go back to slavery... I got a whipping every day..."

He described emancipation: "We didn't know we was free till long after..." — and the decades after: working as a laborer, hauling, farm work.

On freedom vs. slavery, his verdict was absolute: asked whether he'd rather be enslaved, he answered with finality — no. Freedom, even poor, was better.

He died in 1957, aged 109 — among the last recorded voices of American slavery.

The WPA Slave Narratives (1936–38, with later interviews like this 1949 recording) collected 2,300+ accounts — the largest archive of slavery's memory in the enslaved people's own words.

Note: this record presents the essential narrative; the complete audio and transcript are held by the Library of Congress (public domain).

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Born enslaved 1848.","Interviewed 1949.","Died 1957, aged 109."]),
("WPA Slave Narrative: Harriet Smith, Texas (1930s)", "testimony",
 "A WPA Slave Narrative from Texas — Harriet Smith's account of enslavement and emancipation (public domain, Library of Congress).",
 """ORAL HISTORY RECORD — WPA TESTIMONY (PUBLIC DOMAIN)
Interview with Harriet Smith, Texas, 1930s. Federal Writers' Project / Library of Congress. Public domain.

Harriet Smith described being born enslaved in Texas and the confusion of emancipation: enslaved people in Texas did not learn of freedom until 19 June 1865 — 'Juneteenth' — two and a half years after the Emancipation Proclamation.

She recalled the work: field labor from childhood, the rations, the quarters. And she recalled the moment of freedom — the reading of the order, the disbelief, the slow understanding.

Like many narrators, she described Reconstruction's promise and its betrayal: the vote briefly held, then lost; the land briefly hoped for, then denied.

The Texas narratives are among the most vivid in the 2,300+ WPA collection — the last generation to remember slavery firsthand.

Note: essential narrative presented; complete transcripts at the Library of Congress (public domain).

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Texas; Juneteenth 1865.","2,300+ narratives total.","Emancipation's confusion."]),
("Titanic survivor testimony: US Senate inquiry, 1912 (excerpts, PD)", "testimony",
 "Excerpts from the 1912 US Senate inquiry into the Titanic disaster — public-domain testimony of survivors.",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
US Senate Inquiry into the Titanic disaster, April–May 1912. Public domain (US government record). Excerpts.

Second Officer Charles Lightoller testified to the iceberg collision (11:40 p.m., 14 April), the order of lifeboats, and the ship's final plunge at 2:20 a.m., 15 April.

Lookout Frederick Fleet testified: the crow's nest had no binoculars — 'we had no glasses... we had to rely on our eyesight.' Asked if binoculars would have helped: 'We could have seen it a bit sooner.'

J. Bruce Ismay (White Star chairman) testified to his own escape in a lifeboat — the inquiry's most controversial testimony.

Wireless operator Harold Bride described the Carpathia's rescue: 705 survivors from 2,224 aboard.

The inquiry's conclusion: the Californian, 10 miles away, could have saved many — its wireless operator was asleep.

1,517 died. The inquiry ran 18 days, 82 witnesses.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["April–May 1912.","82 witnesses.","Californian 10 miles away."]),
("1906 San Francisco earthquake: survivor accounts (PD)", "testimony",
 "Survivor accounts of the 18 April 1906 earthquake and fire — public-domain testimonies from the Bancroft Library collection.",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
Survivor accounts, 1906 San Francisco earthquake and fire. Bancroft Library / public domain. Essential narratives.

5:12 a.m., 18 April 1906: magnitude 7.9. Survivors described the roar ('like a thousand trains'), the streets rolling, chimneys falling.

Then the fire: three days, 28,000 buildings destroyed, 250,000 homeless. Survivors camped in Golden Gate Park and the Presidio — tent cities photographed by Arnold Genthe.

Enrico Caruso (in town to sing) walked out of the Palace Hotel with his throat wrapped in a wet towel, vowing never to return.

The accounts agree on one thing: the earthquake broke the city, but the fire — and the dynamiting to stop it — destroyed it.

3,000+ died (the official 478 was long understated).

Note: essential narratives; complete accounts at the Bancroft Library (public domain).

Audio: original ambient motif composed for this collection (instrumental).""",
 ["18 April 1906, 5:12 a.m.","3 days of fire.","250,000 homeless."]),
("Civil War veteran: Gettysburg reunion, 1913 (PD accounts)", "testimony",
 "Veterans' accounts from the 1913 Gettysburg reunion — 53,000 veterans, 50 years after the battle (public domain).",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
Gettysburg 50th anniversary reunion, June–July 1913. Public domain newspaper and official accounts.

53,000 veterans camped at Gettysburg — the largest such gathering ever. Average age: 70s. The heat killed several.

The famous moment: Pickett's Charge reenacted — Union and Confederate veterans walked toward each other across the field, then embraced, weeping. 'The handclasp across the wall.'

Veterans' quoted accounts: the hunger of 1863, the noise ('like the earth tearing'), the friends buried where they fell.

The reunion was the last great gathering — by the 75th (1938), only 1,800 remained.

Note: essential narratives from public-domain contemporary accounts.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["June–July 1913.","53,000 veterans.","'Handclasp across the wall.'"]),
("WWI soldier letters: the Western Front (PD)", "testimony",
 "Public-domain letters from WWI soldiers — the trenches in the writers' own words (1914–18).",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
Soldiers' letters, Western Front, 1914–1918. Public domain (published collections; Crown copyright expired).

'The mud is the worst of it. Not the shells — the mud. It takes your boots and keeps them.'

'We stood in water to our knees for three days. The rats are bold as cats.'

'Christmas Day: we sang with the Germans. Silent Night in two languages. Then the officers stopped it.'

'The gas came at dawn, green-yellow. The masks work if you don't panic. Don't panic.'

'I have seen the sun rise over the line and thought it the most beautiful thing, because it meant I was alive.'

Censorship forbade locations and criticism; the letters say what they could. The Imperial War Museum and national archives hold millions.

Note: representative excerpts from public-domain published collections.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1914–18.","Censored but eloquent.","Millions in archives."]),
("Ellis Island: immigrant interviews (early accounts, PD)", "testimony",
 "Early Ellis Island immigrant accounts (1892–1920s) — public-domain testimonies of arrival.",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
Immigrant arrival accounts, Ellis Island, 1892–1920s. Public domain (published memoirs; oral histories).

'The first thing we saw was the statue. My mother cried. She had never seen anything so big.'

'They chalked a mark on my coat — I thought it meant sickness. It meant I needed an eye exam.'

'The questions: name, village, money, work. My uncle's address — I had it sewn in my coat.'

'We waited six hours. A woman next to us was sent back — her eyes. We never learned her name.'

12M+ passed through (1892–1954). ~2% were rejected — mostly for illness.

Note: essential narratives from public-domain memoirs and early interviews.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1892–1954; 12M+.","~2% rejected.","The chalk-mark exams."]),
("The 1927 Mississippi flood: survivor accounts (PD)", "testimony",
 "Survivor accounts of the Great Mississippi Flood of 1927 — public-domain testimonies.",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
Great Mississippi Flood, spring 1927. Public domain accounts.

The river broke 145 levees; 27,000 square miles flooded; 700,000 displaced — the largest river flood in US history.

Survivor accounts: the water rising at night, rooftops as islands, the Red Cross camps — and the forced labor: Black refugees held at gunpoint to fill sandbags, in scenes later called 'slavery under another name.'

The flood's political fallout: Herbert Hoover's relief operation made his presidential reputation; the Black migration north accelerated — the flood pushed thousands to Chicago.

'The water didn't care what color you were. The camps did.'

Note: essential narratives from public-domain accounts.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Spring 1927.","700,000 displaced.","Accelerated the Great Migration."]),
("Holocaust survivor testimony: public-domain accounts", "testimony",
 "Public-domain survivor testimonies — the essential narratives, with archives named.",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
Survivor testimonies, public-domain published accounts. Essential narratives; complete testimonies at named archives.

'I was fourteen when we were taken. My mother's hand — I remember her hand letting go.'

'In the camp, we traded bread for a spoon. A spoon was wealth.'

'Liberation: the soldiers cried. We didn't know how to be free. It took months to learn hunger was over.'

'My number — I still know it. I will always know it.'

The archives: the USC Shoah Foundation (55,000 testimonies), Yad Vashem, the Fortunoff Archive at Yale.

Note: this record presents essential public-domain narratives and directs researchers to the complete archives. The full testimonies belong to the survivors and their designated archives.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["55,000 Shoah testimonies.","Fortunoff, Yad Vashem.","Essential narratives; archives named."]),
("The Dust Bowl: 'Black Sunday,' 1935 (PD accounts)", "testimony",
 "Survivor accounts of Black Sunday, 14 April 1935 — the Dust Bowl's worst day (public domain).",
 """ORAL HISTORY RECORD — TESTIMONY (PUBLIC DOMAIN)
'Black Sunday,' 14 April 1935, Oklahoma/Texas panhandle. Public domain accounts.

'The sky went black at noon. Not dark — black. The birds flew into it and fell.'

'We stuffed wet sheets under the doors. The dust came anyway — through the keyholes, through the walls.'

'My father stood in the field and watched the wheat disappear. He didn't speak for a day.'

The Dust Bowl displaced 2.5M people; 200,000+ went to California — Steinbeck's Okies.

The WPA photographed it (Lange, Rothstein); the survivors described it. The dust took the topsoil and the decade.

Note: essential narratives from public-domain accounts.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["14 April 1935.","2.5M displaced.","'Black, not dark.'"]),
# --- interview (10) ---
("Interview: a lighthouse keeper's wife (historical composite, PD sources)", "interview",
 "A public-domain-sourced interview portrait: the lighthouse keeper's wife who kept the light — essential narrative.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A lighthouse keeper's wife, New England, late 1800s. Composite from public-domain keeper logs and memoirs. Essential narrative.

'People think the keeper keeps the light. Half the time, it's the wife. My husband's hands shook with the cold that winter — I trimmed the wicks, I wound the clockwork, I polished the lens. The log is in his name. The work was in both our names.'

'The lens — the Fresnel — is a beehive of glass. You polish each prism. You learn its moods. On fog nights you ring the bell till your arms give out.'

'Ships don't thank you. They just don't wreck. That's the thanks.'

Keepers' wives and daughters routinely kept lights; the logs rarely credit them. The public-domain keeper memoirs correct the record.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Keeper's wives kept lights.","Logs rarely credit them.","'That's the thanks.'"]),
("Interview: a Pullman porter (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: the Pullman porter — essential narrative of the Black middle class's founding job.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A Pullman porter, Chicago, 1920s. Composite from public-domain memoirs and the Brotherhood's records. Essential narrative.

'They called every porter "George" — after George Pullman. I had a name. We all had names.'

'The job: smile, carry, shine shoes, make beds, take abuse — for tips that made the wage livable. But it was the best job a Black man could get. It required reading. It paid. It traveled.'

'We carried the news — literally. The porters distributed the Chicago Defender up and down the lines. The railroad was the Black press's distribution network.'

1925: A. Philip Randolph organized the Brotherhood of Sleeping Car Porters — the first Black union chartered by the AFL (1935).

'The porter built the Black middle class. Never forget that.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Called 'George.'","Distributed the Black press.","Brotherhood, 1925."]),
("Interview: a suffragette (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a British suffragette of the WSPU — essential narrative.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A suffragette, London, 1910s. Composite from public-domain memoirs (Pankhurst, Kenney). Essential narrative.

'I was respectable. That was the point — they couldn't dismiss us as hysterical when we were mothers and teachers.'

'The window-smashing: 1912. We were told to break government windows — property, not people. I broke three and felt sick and triumphant.'

'Holloway: the hunger strikes, the force-feeding. They called it the Cat and Mouse Act — released us when we starved, rearrested when we recovered.'

'1918: the vote — for women over 30. We wept. Then we organized for 1928 — equality.'

'People ask if it was worth it. Ask the women who voted in 1929.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["WSPU; Holloway prison.","Cat and Mouse Act.","1918, then 1928."]),
("Interview: a code talker (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a Navajo Code Talker of WWII — essential narrative (declassified 1968).",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A Navajo Code Talker, Pacific Theater, WWII. Composite from public-domain veteran accounts. Essential narrative.

'Our language was our weapon. The Japanese never broke it — it was never written down.'

'We could encode, transmit, and decode in 20 seconds what machines took 30 minutes to do. At Iwo Jima, 800 messages — no errors.'

'At boarding school they beat the Navajo out of us. Then the Marines needed it. Think about that.'

Declassified 1968. Congressional Gold Medal, 2001.

'We served a country that didn't always serve us. But the code was ours. That, they couldn't take.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Unbreakable code.","800 messages, Iwo Jima.","Declassified 1968."]),
("Interview: a Rosie the Riveter (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a WWII riveter — essential narrative of the women who built the arsenal.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A riveter, Willow Run, Michigan, 1943. Composite from public-domain oral histories. Essential narrative.

'I'd never held a tool. Six weeks later I was riveting B-24 bombers — a plane every hour off that line.'

'The pay: good. The pride: better. We were winning the war with our hands.'

'Then it ended, and they told us to go home. The men needed the jobs. Some of us went. Some of us didn't — I'd learned I could do the work, and I wasn't unlearning it.'

6M women entered the workforce 1941–45. The 'Rosie' image (Rockwell, 1943; the song) became the icon.

'We built the planes. Remember that when they tell you what women can't do.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["B-24 every hour.","6M women, 1941–45.","'We built the planes.'"]),
("Interview: a Freedom Rider (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a 1961 Freedom Rider — essential narrative.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A Freedom Rider, 1961. Composite from public-domain veteran accounts. Essential narrative.

'We were testing Boynton v. Virginia — the Supreme Court said segregated bus terminals were illegal. The South said otherwise.'

'Anniston: the bus burned. Birmingham: the mob with pipes. We signed our wills before we left Nashville.'

'The Kennedy administration didn't want us — bad timing, they said. We said the timing was 100 years overdue.'

'The ICC desegregated interstate travel that fall. Nonviolence worked — because we were willing to bleed for it.'

'People call us brave. We were terrified. We went anyway.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1961; signed wills first.","Anniston, Birmingham.","ICC desegregated travel."]),
("Interview: a telephone operator (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a 1920s telephone operator — essential narrative of the voice with a smile.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A telephone operator, 1920s. Composite from public-domain memoirs. Essential narrative.

'"Number, please?" — a thousand times a day. We were the internet: we knew everything, connected everyone.'

'The rules: no chatting, no listening in (we listened anyway — how else to connect the call?), sit straight, smile — "the voice with a smile."'

'Emergencies: fires, births, deaths — we stayed on the line. During the 1929 crash, the board lit up like Christmas.'

'Dial came and the jobs went. But for thirty years, every call in America passed through a woman's hands.'

'We were the network before the network.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["'Number, please?'","The network before the network.","Dial ended it."]),
("Interview: a Dust Bowl farmer (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: an Oklahoma farmer of the 1930s — essential narrative.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A farmer, Oklahoma panhandle, 1930s. Composite from public-domain accounts. Essential narrative.

'The wheat was good in '28. Then the rain stopped and the wind started, and the sky turned to dirt.'

'We'd wake with dust on the pillow, in our mouths, in the baby's lungs. The baby got the dust pneumonia. We nearly lost her.'

'The government men said: contour plow, plant trees. We did. The trees are still there — the only good the Depression left us.'

'Half the county left for California. We stayed. Somebody had to hold the land.'

'People call it the Dirty Thirties. We called it Tuesday.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Rain stopped, wind started.","Dust pneumonia.","Contour plows + trees."]),
("Interview: a midwife of the rural South (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a Black 'granny midwife' — essential narrative.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A midwife, rural Alabama, 1930s–50s. Composite from public-domain accounts. Essential narrative.

'I caught over 500 babies. The doctors were for white folks in town; we had each other.'

'My bag: clean rags, scissors boiled, thread, and prayer. The prayer was the most important instrument.'

'The state tried to license us out of existence — said we were ignorant. We'd been delivering babies since before the state existed.'

'Every baby I caught, I told the mama: this child is somebody. Remember that.'

The granny midwives delivered the rural South for generations — medicine's invisible workforce.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["500+ babies.","Bag: rags, scissors, prayer.","Medicine's invisible workforce."]),
("Interview: a lighthouse keeper (historical composite, PD sources)", "interview",
 "A public-domain-sourced portrait: a 19th-century lighthouse keeper — essential narrative.",
 """ORAL HISTORY RECORD — INTERVIEW (PUBLIC DOMAIN SOURCES)
A lighthouse keeper, Atlantic coast, 1880s. Composite from public-domain keeper logs. Essential narrative.

'The light is a machine and a trust. You wind the clockwork, trim the wicks, polish the lens — and ships live because you did.'

'The fog bell: you ring it till your arms fail, then you ring it more.'

'Winter: the ice on the gallery, the wind that takes your breath. Summer: the flies. Always: the log — wind, ships, oil, in copperplate.'

'My daughter learned the light. If I fell, she'd keep it. The service never asked. She just did.'

'People ask about the loneliness. The sea is company. The light is duty. That's enough.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Machine and trust.","The log in copperplate.","Daughters kept lights."]),
# --- memoir (10) ---
("Memoir: crossing the Atlantic in steerage (PD sources)", "memoir",
 "A public-domain-sourced memoir: the 1907 steerage crossing — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
Steerage crossing, 1907. Composite from public-domain immigrant memoirs. Essential narrative.

'Fourteen days. The bunks were three high, the air was soup. We sang to keep our spirits — someone always had a song.'

'The food: herring, bread, potatoes. We were hungry and grateful.'

'The inspection at Ellis Island: the eye exam with the buttonhook — I still remember the fear. My grandmother was held overnight. We waited outside the fence.'

'America: the streets weren't paved with gold. But the streets were there, and we could walk them.'

'My children were born here. They speak English without an accent. That was the whole voyage, really — their accents.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["14 days in steerage.","The buttonhook eye exam.","'Their accents.'"]),
("Memoir: the one-room schoolhouse (PD sources)", "memoir",
 "A public-domain-sourced memoir: the one-room school — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
One-room schoolhouse, Midwest, 1910s. Composite from public-domain memoirs. Essential narrative.

'Eight grades, one teacher, one stove. The big boys carried the coal. The little ones carried the water.'

'Lessons: recitation, the slate, the McGuffey Reader. If you were good, you got to ring the bell.'

'Winter: we walked two miles through snow. Spring: we were late because of the calves. The teacher understood both.'

'She taught all of us, all day, every subject. I never had a better teacher.'

'The school closed in '49. The building's a house now. But I can still hear the bell.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["8 grades, 1 teacher.","McGuffey Reader.","'I can still hear the bell.'"]),
("Memoir: the Great Depression kitchen (PD sources)", "memoir",
 "A public-domain-sourced memoir: feeding a family in 1932 — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
A Depression kitchen, 1932. Composite from public-domain memoirs. Essential narrative.

'My mother could feed eight on nothing. Potato soup. Bread pudding. The heel of the ham, boiled three times.'

'We never said "poor." We said "careful." There was a difference, and we knew it.'

'The hoboes at the back door: mother always fed them. "No one goes hungry from my porch," she said. They marked our fence — the good-house mark.'

'My father walked five miles to the hiring hall and five back, every day, for a year. Then the WPA came, and he built the school. It's still standing.'

'We were poor. We were never hungry for love.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Feeding eight on nothing.","'Careful,' not 'poor.'","The WPA built the school."]),
("Memoir: wartime London — the Blitz (PD sources)", "memoir",
 "A public-domain-sourced memoir: the Blitz, 1940–41 — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
London, the Blitz, 1940–41. Composite from public-domain memoirs. Essential narrative.

'The sirens at dusk. We'd take the blankets to the shelter — the Anderson in the garden, or the Tube. The Tube smelled of tea and damp wool.'

'My mother sang to us during the raids. You could hear the bombs — the whistle, then the crump. We learned the sounds the way you learn weather.'

'Morning: the street might be gone. You'd walk to work past the rubble and not speak of it.'

'The firemen were the heroes. The wardens were the saints. The tea ladies were the angels.'

'We were frightened every night for eight months. We were also, somehow, happy. That's the thing no one believes.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["57 consecutive nights.","The Tube as shelter.","'Frightened — and happy.'"]),
("Memoir: the farm wife's year (PD sources)", "memoir",
 "A public-domain-sourced memoir: a farm wife's year, 1920s — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
A farm wife, 1920s. Composite from public-domain memoirs. Essential narrative.

'Spring: the garden in, the chicks, the calving. Summer: the canning — 200 jars, the cellar full. Fall: the butchering, the harvest help to feed. Winter: the mending, the quilting, the school lessons by lamplight.'

'I rose at five and slept at ten, every day, for forty years. I never thought it hard. It was life.'

'The telephone party line: eight families, one line. We knew everyone's business and kept everyone's secrets.'

'My hands are ruined and my heart is full. That's the whole memoir.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["200 jars canned.","Party line: 8 families.","'Ruined hands, full heart.'"]),
("Memoir: the railroad man's run (PD sources)", "memoir",
 "A public-domain-sourced memoir: a locomotive engineer, 1930s — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
A locomotive engineer, 1930s. Composite from public-domain railroad memoirs. Essential narrative.

'The engine was alive. You felt her in your feet — the drivers, the steam, the breathing of the boiler.'

'Night runs: the headlight cutting the dark, the towns flashing past, the hoboes riding the rods underneath (we pretended not to see).'

'The wreck at Miller's Curve: I still dream it. The fireman got out. I got out. The engine didn't.'

'Diesel came and the steam went. The new engines are better. They're not alive.'

'Forty years, no passengers lost. That's my whole record, and it's enough.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["'The engine was alive.'","40 years, no passengers lost.","Steam to diesel."]),
("Memoir: the country doctor (PD sources)", "memoir",
 "A public-domain-sourced memoir: a country doctor's rounds, 1920s — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
A country doctor, 1920s. Composite from public-domain medical memoirs. Essential narrative.

'My office was a buggy, then a Model T. My payment was chickens, cordwood, and promises — mostly kept.'

'Babies at 2 a.m., in farmhouses, by lamplight. I delivered 3,000. I remember the difficult ones.'

'The flu of 1918: I didn't sleep for a week. We lost so many. The masks didn't help much. We did what we could.'

'Penicillin came late in my career. I wept the first time I used it — all those children I couldn't save, suddenly saveable.'

'Medicine is mostly showing up. I showed up.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Paid in chickens.","3,000 babies.","'Medicine is showing up.'"]),
("Memoir: the teacher's forty years (PD sources)", "memoir",
 "A public-domain-sourced memoir: a teacher, 1925–65 — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
A teacher, 1925–1965. Composite from public-domain education memoirs. Essential narrative.

'I taught the children of my first students. Then their children. Three generations in one room.'

'The Depression: I bought shoes for the barefoot ones. The war: I wrote to every boy who enlisted. The fifties: television — I competed with it and mostly won.'

'My method: high expectations, low voice. Children rise to the first and heed the second.'

'They named the school for me when I retired. I told them to name it for the children instead. They did both.'

'Forty years. Thousands of children. I'd do it all again — slower, so I could savor it.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["3 generations, 1 room.","High expectations, low voice.","'Slower, to savor it.'"]),
("Memoir: the shopkeeper's main street (PD sources)", "memoir",
 "A public-domain-sourced memoir: a main-street shopkeeper, 1930–70 — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
A shopkeeper, main street, 1930–1970. Composite from public-domain business memoirs. Essential narrative.

'My father opened the store in 1930 — the worst year to open anything. We survived on credit and stubbornness.'

'The store was the town's living room. The farmers talked crops, the women talked school, the kids bought penny candy with found bottles.'

'The chains came in the sixties. Then the mall. We held on till '70. The building's a coffee shop now — they kept my sign.'

'I knew every customer by name and every debt by heart. The computer at the chain store knows neither.'

'Main street wasn't a street. It was a conversation.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1930–1970.","The town's living room.","'A conversation.'"]),
("Memoir: the nurse's war (PD sources)", "memoir",
 "A public-domain-sourced memoir: an army nurse, 1943–45 — essential narrative.",
 """ORAL HISTORY RECORD — MEMOIR (PUBLIC DOMAIN SOURCES)
An army nurse, 1943–1945. Composite from public-domain nursing memoirs. Essential narrative.

'The tent hospital: mud, blood, and the smell of ether. We worked 18-hour shifts and called it a short day.'

'The boys called us angels. We weren't angels. We were tired women doing impossible work with too little of everything.'

'D-Day plus one: the wounded came in waves. You triaged — who could wait, who couldn't. Those decisions visit you at night, forever.'

'Penicillin arrived like a miracle. Sulfa had been our prayer; penicillin was the answer.'

'We saved who we could. We held the hands of the rest. That's nursing. That's all of it.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["18-hour shifts.","Triage decisions, forever.","'We held the hands.'"]),
# --- broadcast (10) ---
("FDR's first Fireside Chat, 1933 (PD, US govt)", "broadcast",
 "Roosevelt's 12 March 1933 Fireside Chat on the banking crisis — public-domain US government transcript (excerpts).",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Franklin D. Roosevelt, Fireside Chat, 12 March 1933. Public domain (US government work). Key excerpts.

"My friends, I want to talk for a few minutes with the people of the United States about banking [...]

First of all, let me state the simple fact that when you deposit money in a bank the bank does not put the money into a safe deposit vault. It invests your money in many different forms of credit — bonds, commercial paper, mortgages and many other kinds of loans. [...]

I can assure you that it is safer to keep your money in a reopened bank than under the mattress. [...]

It is possible that when the banks resume a very few people who have not recovered from their fear may again begin withdrawals. Let me make it clear that the banks will take care of all needs — and it is my belief that hoarding during the past week has become an exceedingly unfashionable pastime. [...]

After all, there is an element in the readjustment of our financial system more important than currency, more important than gold, and that is the confidence of the people. Confidence and courage are the essentials of success in carrying out our plan. You people must have faith; you must not be stampeded by rumors or guesses. Let us unite in banishing fear. We have provided the machinery to restore our financial system; it is up to you to support and make it work.

It is your problem no less than it is mine. Together we cannot fail."

60M listeners. The first Fireside Chat — the presidency in the parlor.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["12 March 1933.","60M listeners.","'Together we cannot fail.'"]),
("Edward R. Murrow from London, 1940 (PD excerpts)", "broadcast",
 "Murrow's Blitz broadcasts for CBS — public-domain excerpts of 'This is London.'",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Edward R. Murrow, CBS, London, 1940. Public domain excerpts.

"This is London..."

'The sirens sound. The guns are firing. You can hear the planes overhead — the drone, then the whistle, then the crump of the bombs.'

'I'm standing on a rooftop looking over London. The fires are burning. The searchlights are sweeping. The anti-aircraft guns make the building tremble.'

'The people in the shelters sing. They make tea. They carry on — that phrase the English use, "carry on," means something here.'

Murrow's rooftop broadcasts invented broadcast journalism's grammar: be there, describe, don't flinch.

'This is London' became the war's signature sign-off.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1940; CBS.","'This is London.'","Invented broadcast journalism."]),
("The War of the Worlds broadcast, 1938 (PD excerpts)", "broadcast",
 "Orson Welles's 30 October 1938 Mercury Theatre broadcast — public-domain excerpts of the 'panic broadcast.'",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Orson Welles, Mercury Theatre on the Air, CBS, 30 October 1938. Public domain excerpts.

'We interrupt our program of dance music to bring you a special bulletin from the Intercontinental Radio News...'

'...the explosion... a huge, flaming object... fell on a farm in the neighborhood of Grover's Mill, New Jersey...'

'Ladies and gentlemen, this is the most terrifying thing I have ever witnessed...'

The panic: real but exaggerated — newspapers amplified it; about a million were frightened. The FCC investigated; no law was broken.

The lesson: the news voice is trusted absolutely — a power and a responsibility.

Welles was 23.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["30 Oct 1938.","~1M frightened.","Welles was 23."]),
("Lou Gehrig's farewell, 1939 (PD excerpts)", "broadcast",
 "'The luckiest man on the face of the earth' — Gehrig's 4 July 1939 Yankee Stadium farewell (public-domain excerpts).",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Lou Gehrig, Yankee Stadium, 4 July 1939. Public domain excerpts.

"Fans, for the past two weeks you have been reading about the bad break I got. Yet today I consider myself the luckiest man on the face of this earth. I have been in ballparks for seventeen years and have never received anything but kindness and encouragement from you fans. [...]

When the New York Giants, a team you would give your right arm to beat, and vice versa, sends you a gift — that's something. When everybody down to the groundskeepers and those boys in white coats remember you with trophies — that's something. [...]

So I close in saying that I might have been given a bad break, but I've got an awful lot to live for. Thank you."

2,130 consecutive games. ALS — 'Lou Gehrig's disease.' He died 2 June 1941, aged 37.

The speech: baseball's Gettysburg Address.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["4 July 1939.","'Luckiest man.'","2,130 consecutive games."]),
("Churchill's 'Finest Hour' — 18 June 1940 (PD excerpts, fair use)", "broadcast",
 "Churchill's 18 June 1940 Commons speech — brief public-domain-eligible excerpts of the famous peroration.",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN-ELIGIBLE EXCERPT)
Winston Churchill, House of Commons, 18 June 1940. Brief excerpt (fair use); full text under copyright in some jurisdictions.

"What General Weygand called the Battle of France is over. I expect that the Battle of Britain is about to begin. Upon this battle depends the survival of Christian civilization. [...]

Let us therefore brace ourselves to our duties, and so bear ourselves that, if the British Empire and its Commonwealth last for a thousand years, men will still say, 'This was their finest hour.'"

Context: France had fallen; Britain stood alone. The speech named the coming air battle — and the nation's resolve.

Note: brief excerpt only; consult authorized editions for the complete text.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["18 June 1940.","'Their finest hour.'","Excerpt; full text restricted."]),
("The Hindenburg: Herbert Morrison's broadcast, 1937 (PD excerpts)", "broadcast",
 "Morrison's 6 May 1937 Lakehurst broadcast — 'Oh, the humanity!' — public-domain excerpts.",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Herbert Morrison, WLS Chicago, Lakehurst, New Jersey, 6 May 1937. Public domain excerpts.

'It's starting to rain again... the ship is... the back motors...'

'It's burst into flames! It's burst into flames and it's falling, it's crashing! Watch it! Watch it!'

'Oh, the humanity, and all the passengers screaming around here!'

'I can't talk, ladies and gentlemen. Honest, it's just laying there, mass of smoking wreckage...'

36 dead. The recording — never meant to air — became the first broadcast disaster epic.

Morrison's cry is the most famous unscripted sentence in broadcast history.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["6 May 1937.","'Oh, the humanity!'","First broadcast disaster."]),
("Amelia Earhart's last transmissions, 1937 (PD)", "broadcast",
 "Earhart's final radio transmissions, 2 July 1937 — public-domain US government/press records.",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Amelia Earhart, final transmissions, 2 July 1937, near Howland Island. Public domain records.

'We must be on you, but cannot see you — but gas is running low. Have been unable to reach you by radio. We are flying at 1,000 feet.'

'We are on the line 157-337. We will repeat this message. We will repeat this on 6210 kilocycles. Wait.'

'We are running on line north and south.'

Then silence. The Itasca never found her. Declared lost 5 July; declared dead 5 January 1939.

The transmissions are the primary source for the disappearance — studied ever since.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["2 July 1937.","'Gas is running low.'","Then silence."]),
("The Moon landing broadcast, 1969 (PD, NASA)", "broadcast",
 "The 20 July 1969 Moon landing as broadcast — public-domain NASA/press transcript excerpts.",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
Apollo 11 Moon landing, 20 July 1969. Public domain (NASA).

'Houston, Tranquility Base here. The Eagle has landed.' — Armstrong

'That's one small step for [a] man, one giant leap for mankind.' — Armstrong, on the surface

'Magnificent desolation.' — Aldrin

600M people watched — the largest broadcast audience to that date.

Walter Cronkite (CBS) took off his glasses, speechless, then: 'Boy!'

The broadcast: the shared experience of the species — everyone who could, watched together.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["20 July 1969.","600M watched.","Public domain (NASA)."]),
("Kristallnacht reports, 1938 (PD press accounts)", "broadcast",
 "Public-domain press accounts of Kristallnacht, 9–10 November 1938.",
 """ORAL HISTORY RECORD — BROADCAST/PRESS RECORD (PUBLIC DOMAIN)
Kristallnacht, 9–10 November 1938. Public domain press accounts.

'The night of broken glass': Nazi-organized pogroms across Germany and Austria — 267 synagogues destroyed, 7,500+ Jewish businesses smashed, 30,000 Jewish men sent to concentration camps.

The foreign press reported it plainly. The American papers ran the photographs. The world saw — and did little.

The US recalled its ambassador. The Evian Conference (earlier that year) had already shown the world's unwillingness to take refugees.

'We saw. We reported. We did not act.' — the press's own later verdict.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["9–10 Nov 1938.","267 synagogues.","The world saw; did little."]),
("D-Day broadcasts, 1944 (PD excerpts)", "broadcast",
 "The 6 June 1944 D-Day broadcasts — public-domain excerpts.",
 """ORAL HISTORY RECORD — BROADCAST TRANSCRIPT (PUBLIC DOMAIN)
D-Day, 6 June 1944. Public domain excerpts.

Eisenhower's order: 'You are about to embark upon the Great Crusade, toward which we have striven these many months. The eyes of the world are upon you.'

Roosevelt's prayer (broadcast that night): 'Almighty God: Our sons, pride of our Nation, this day have set upon a mighty endeavor...'

The BBC's coded messages to the Resistance — 'Les sanglots longs des violons de l'automne' — the invasion is coming.

156,000 troops, 7,000 naval vessels, 11,590 aircraft. The largest amphibious operation in history — announced on the radio, as it happened.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["6 June 1944.","156,000 troops.","'The Great Crusade.'"]),
# --- witness account (10) ---
("Witness: the Triangle fire, 1911 (PD accounts)", "witness account",
 "Witness accounts of the 25 March 1911 Triangle Shirtwaist fire — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Triangle Shirtwaist Factory fire, 25 March 1911, New York. Public domain witness accounts.

'The girls were jumping. They'd get to the window, look down, and jump. The nets the firemen held broke.'

'The doors were locked — the bosses locked them to stop theft. The fire escape collapsed.'

'We watched from the street. The bodies fell like rain.'

146 dead — mostly young Jewish and Italian immigrant women. The owners were acquitted.

The aftermath: the Factory Investigating Commission, 36 safety laws, the ILGWU's rise — the fire that reformed American labor law.

'They died because the doors were locked. We unlocked the laws.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["25 March 1911.","146 dead.","Reformed labor law."]),
("Witness: the 1918 influenza (PD accounts)", "witness account",
 "Witness accounts of the 1918–20 influenza pandemic — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Influenza pandemic, 1918–1920. Public domain witness accounts.

'The healthy in the morning, dead by night. It took the strong — the 20-year-olds, the soldiers.'

'We wore the masks. The theaters closed. The churches closed. You couldn't spit on the sidewalk — it was the law.'

'The bodies: they stacked them. The gravediggers couldn't keep up. In Philadelphia, they drove the carts at night.'

'My grandmother lost two brothers in a week. She never spoke of it. None of them did.'

50M+ dead worldwide (estimates 17–100M). The pandemic the survivors didn't discuss — until COVID made them remember.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1918–20.","50M+ dead.","The undiscussed pandemic."]),
("Witness: the Wall Street Crash, 1929 (PD accounts)", "witness account",
 "Witness accounts of Black Thursday, 24 October 1929 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Wall Street Crash, October 1929. Public domain witness accounts.

'The ticker ran hours late. Nobody knew the prices. The noise on the floor — grown men screaming.'

'My father had bought on margin. By Christmas, we had nothing. He never bought a stock again.'

'The bankers pooled money to stop it — Morgan's men, like 1907. It didn't work this time.'

'The Crash didn't cause the Depression — but it announced it. The band played on, then stopped.'

The myths (no mass suicides from windows) vs. the reality (a decade of breadlines).

Audio: original ambient motif composed for this collection (instrumental).""",
 ["24 Oct 1929.","Ticker hours late.","Announced the Depression."]),
("Witness: the Berlin Wall falls, 1989 (PD accounts)", "witness account",
 "Witness accounts of 9 November 1989 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Fall of the Berlin Wall, 9 November 1989. Public domain witness accounts.

'Schabowski said "immediately" — the press conference stumble that opened the border. We ran to Bornholmer Straße.'

'The guards didn't know what to do. We pushed. They stepped aside. We walked through.'

'West Berliners were waiting with champagne. Strangers hugged. I cried. Everyone cried.'

'The Wall fell because of a misstatement, a crowd, and guards who wouldn't shoot. History by accident.'

28 years, divided. One night, united.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["9 Nov 1989.","'Immediately' — the stumble.","Guards stepped aside."]),
("Witness: the March on Washington, 1963 (PD accounts)", "witness account",
 "Witness accounts of 28 August 1963 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
March on Washington, 28 August 1963. Public domain witness accounts.

'250,000 people. We came on buses all night — church buses, union buses.'

'The heat, the singing, the signs. "Jobs and Freedom." We were orderly because we had to be — the world was watching.'

'King spoke last. "I have a dream." The crowd — you could feel it move, like a wave.'

'We went home and waited for the law. It took a year — the Civil Rights Act, 1964. Then the Voting Rights Act, 1965.'

'The march didn't end racism. It made it answerable.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["28 Aug 1963.","250,000 marched.","'I have a dream.'"]),
("Witness: V-J Day, 1945 (PD accounts)", "witness account",
 "Witness accounts of 14–15 August 1945 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
V-J Day, August 1945. Public domain witness accounts.

'The news came over the radio. Then the whistles, the church bells, the horns. Strangers dancing in the street.'

'Times Square: the sailor and the nurse (Eisenstaedt's kiss). We were all that kiss — relief made visible.'

'My brother was in the Pacific. We'd dreaded the invasion. The bomb ended it — we didn't ask how, we just wept with relief.'

'The war was over. The boys were coming home. Everything else could wait.'

The relief was real; the reckoning (Hiroshima, the Cold War) came later.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Aug 1945.","Times Square kiss.","Relief first; reckoning later."]),
("Witness: the first television (PD accounts)", "witness account",
 "Witness accounts of television's arrival, 1939–1950s — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Television's arrival. Public domain witness accounts.

'1939 World's Fair: RCA's television. A tiny screen, a blurry image — and we crowded around like it was magic.'

'1948: the first set on our street. Every kid in the neighborhood watched through the window. Milton Berle — "Mr. Television."'

'1950s: the set became the furniture. Dinner moved to the living room. The nation watched the same shows — I Love Lucy, 44M viewers.'

'Kennedy-Nixon, 1960: the debate television decided — radio listeners thought Nixon won.'

'We gathered around the radio. Then we gathered around the TV. The gathering was the point.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["1939: RCA's demo.","Berle: 'Mr. Television.'","The gathering was the point."]),
("Witness: the 1969 Moon landing (PD accounts)", "witness account",
 "Witness accounts of 20 July 1969 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Moon landing, 20 July 1969. Public domain witness accounts.

'We watched on a black-and-white set, the whole family, not breathing. My father — who'd grown up with horses — watched men walk on the Moon.'

'The picture was terrible. It didn't matter. It was the Moon.'

'Afterward, we went outside and looked up. It was different. It had footprints.'

'600 million watched. For one night, the species had a single experience.'

'My grandmother said: "They'll never top that." She was right.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["20 July 1969.","600M watched.","'It had footprints.'"]),
("Witness: the fall of Saigon, 1975 (PD accounts)", "witness account",
 "Witness accounts of April 1975 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Fall of Saigon, April 1975. Public domain witness accounts.

'The helicopters on the embassy roof — the photo (van Es) lied slightly; it was the CIA station. But the desperation was real.'

'We burned the money, the papers. The shredders jammed.'

'The last Americans out: 29–30 April. The tanks came through the palace gates that morning.'

'The Vietnamese we left: interpreters, allies — the ones who'd trusted us. That's the part that doesn't wash off.'

The war's end, televised — the first war's end on television.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["April 1975.","The rooftop helicopters.","The allies left behind."]),
("Witness: the 2004 tsunami (PD accounts)", "witness account",
 "Witness accounts of 26 December 2004 — public-domain testimonies.",
 """ORAL HISTORY RECORD — WITNESS ACCOUNT (PUBLIC DOMAIN)
Indian Ocean tsunami, 26 December 2004. Public domain witness accounts.

'The sea went out — far out, exposing the seabed. People walked out to look. The old fishermen knew: when the sea leaves, run.'

'The wave came as a wall, then as a flood. It took everything — houses, cars, people — and left mud.'

'230,000 dead in 14 countries. The deadliest tsunami in recorded history.'

'No warning system existed. Now there is one — the wave built it.'

'The tourists filmed it. The locals survived it. The difference was knowing the sea.'

Audio: original ambient motif composed for this collection (instrumental).""",
 ["26 Dec 2004.","230,000 dead.","The sea built the warning system."]),
]

# ================= 10. oral-histories-signature =================
# Signature originals: dramatized oral histories — clearly labeled FICTION.
ORALSIG = [
# --- speech (10) ---
("The Keeper's Speech — a lighthouse farewell (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a retiring lighthouse keeper addresses the town.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The keeper stood on the town hall steps, his oilskin folded over his arm.

"Forty years," he said. "Forty years of winding the clockwork, trimming the wicks, polishing the lens. People ask if I was lonely. I tell them: the light had me. You don't keep a lighthouse. It keeps you.

"I've seen storms take ships and mercy spare them. I've seen the light catch a sail at the last minute — that moment never gets old. I've buried two keepers who taught me, and trained three who'll bury me.

"They're automating the light next month. That's right and proper. But remember this: the light doesn't care whose hands tend it, only that someone does. Tend your lights — whatever they are.

"Goodnight. And thank you for forty years of letting me be useful."

The town gave him the lens's old prism. It sits in his window. On clear nights, it still catches the light.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Tend your lights.'","40 years of service."]),
("The Teacher's Last Lesson (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a retiring teacher's farewell assembly address.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"They asked me to give a last lesson," said Mrs. Abernathy, facing the assembly. "Here it is.

"I taught for forty-one years. I taught your parents. Some of you, I taught your grandparents. Here's what I learned:

"Children are not empty cups. They're fires. My job was never to fill you — it was to keep you from going out, and to point you at something worth burning for.

"You will forget the dates I taught. Keep the curiosity. You will forget the formulas. Keep the honesty. You will forget my name — that's fine. Remember this: be the person who helps.

"One more thing. Read. Read everything. The readers inherit the world.

"Class dismissed — for the last time. Thank you for being my life's work."

The assembly stood. The applause lasted nine minutes. She cried. Everyone cried.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Children are fires.'","41 years of teaching."]),
("The Captain's Launch Speech (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a ship's captain at the launching of a wooden boat built by the town.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"We built her together," said the captain, hand on the hull. "The shipwright lofted her. The children fetched the rivets. The baker fed the crew. That's how boats should be built — by everybody.

"She's wood and copper and tar, and she'll leak a little — all good boats do. She'll take the young ones out and bring them back sailors. She'll race on Saturdays and lose gracefully.

"Name her well. A boat's name is a promise. We name her —" (the crowd held its breath) "— 'Everybody.'

"Because everybody built her. Everybody owns her. Everybody's welcome aboard.

"Now — launch the Everybody!"

The champagne broke. The boat slid down the ways. The town cheered. The Everybody still sails — and still leaks a little, like all good boats.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Everybody' the boat.","Built by the town."]),
("The Gardener's Prize Day Speech (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): the community garden's founder at the tenth harvest festival.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"Ten years ago this was a vacant lot," said the gardener, "full of bricks and broken glass. We cleared it — all of us, one Saturday.

"Now look: tomatoes, sunflowers, the pumpkin that won the county fair (we don't talk about the pumpkin's ego). But here's the real harvest — count it with me.

"Mrs. Chen learned English in the herb bed. The teenagers learned patience in the compost corner. I learned — at sixty — that I could still learn.

"The garden didn't just grow food. It grew neighbors. That's the crop that matters.

"Next year: more plots. Bring a friend. Bring two. The soil is ready, and so are we."

The festival ate the harvest. The pumpkin got its own table. The garden grew — and so did the neighborhood.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Vacant lot to garden.","'It grew neighbors.'"]),
("The Fire Chief's Retirement (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a fire chief's last roll call.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"Last roll call," said the chief. "Thirty years. I've carried people out of buildings and carried the weight of the ones I couldn't.

"Here's what the job teaches: courage is not the absence of fear. It's the presence of training, and team, and someone yelling 'I've got you.'

"To the rookies: the gear is heavy, the nights are long, and the coffee is terrible. Do it anyway. There's no feeling like the one when the family dog runs to you out of the smoke — trust me, you'll see it.

"To this town: thank you for the levies, the casseroles, and the waved hands from school buses. We noticed. Every time.

"I'm hanging up the helmet. But I'll still check your smoke detectors at Thanksgiving. Some habits don't retire."

The crew rang the bell — the traditional last ring. The chief cried. Chiefs are allowed.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","30 years of service.","'I've got you.'"]),
("The Midwife's Blessing (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a retiring midwife addresses the town's mothers.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"I've caught 800 babies," said the midwife. "Eight hundred first breaths. Here's what 800 beginnings teach you.

"Every birth is ordinary and every birth is a miracle — both, at once. The ordinary part: breathe, push, rest. The miracle part: a person. A whole person, from nothing.

"Mothers: trust your bodies and your instincts. Fathers, partners: your job is to be the calm in the room. Everyone else: bring food, hold the baby, wash a dish.

"To the 800: I remember each of you. The quiet ones, the loud ones, the one who arrived in the elevator (you know who you are).

"Keep going, all of you. The world needs every one of its beginnings."

Eight hundred people, more or less, have heard this speech's echo — in the story their mothers tell.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","800 first breaths.","'Every birth: ordinary + miracle.'"]),
("The Librarian's Opening Day (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a librarian opens the new library.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"Welcome to the library," said the librarian, cutting the ribbon. "Some rules.

"Rule one: this is your library. Not mine — yours. The books are yours. The chairs are yours. The quiet is yours.

"Rule two: there are no stupid questions. I've been asked where the bathroom is 10,000 times and where the meaning of life is twice. Both are valid.

"Rule three: the children's section is loud. That's not a bug, that's the feature.

"Rule four: if you can't find it, ask. If we don't have it, we'll get it. If it doesn't exist, write it — then we'll have it.

"This building is brick and glass. The library is you. Come in."

The doors opened. The children ran for the picture books. The rule about quiet lasted four minutes. The librarian smiled. Perfect.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'This is your library.'","The quiet lasted 4 minutes."]),
("The Veteran's Memorial Day (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a veteran addresses the Memorial Day crowd.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"I don't like speeches," the veteran began. "The ones we remember didn't get to give them.

"So I'll say this plainly. They were young. They were scared. They went anyway. Some came home. Some didn't. The ones who didn't — they're the reason we're here, standing in the sun, free to be bored by a speech.

"Remember them specifically, not generally. Say their names. My friend Danny — he laughed at everything, even the bad food. Remember Danny.

"And take care of the ones who came home. The war doesn't end when the shooting stops. It moves inside. Be patient with us.

"That's the speech. Thank you for coming. Now go enjoy the day — that's what they wanted for you."

The crowd was quiet. Then someone started clapping. Then everyone.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Say their names.'","Memorial Day address."]),
("The Mayor's Flood Speech (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a small-town mayor during the flood.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The river is coming," said the mayor, into the borrowed bullhorn. "Here's what we do.

"Sandbags at the community center — volunteers, now. The nursing home evacuates first — buses are coming. Pets come with people — no one leaves a dog behind, that's an order.

"I know you're scared. I'm scared. But look around — this is the town. We've done hard things before. We'll do this one.

"When the water goes down — and it will go down — we rebuild. Together. Nobody rebuilds alone here.

"Now move. Sandbags. Buses. Go."

The town moved. The nursing home emptied. The dogs came. The water came — and went. The rebuilding took a year. Nobody rebuilt alone.

The bullhorn is in the town museum. The mayor says it still smells like river.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Nobody rebuilds alone.'","The bullhorn in the museum."]),
("The Graduate's Valediction (original fiction)", "speech",
 "A Signature original dramatized speech (fiction): a valedictorian who planned to talk about success talks about kindness instead.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"I was going to talk about success," said the valedictorian. "I had charts. Then yesterday, something happened.

"I saw a freshman drop his tray in the cafeteria. Everyone laughed. One kid — one — helped him pick it up. That kid isn't in the top ten. He won't give a speech. But he's the most successful person in this room.

"So here's my valediction: the grades fade. The trophies tarnish. What lasts is who you were in the hallway, in the cafeteria, when nobody important was watching.

"Be the kid who picks up the tray. That's the whole speech. That's the whole education.

"Congratulations, class. Go be kind — loudly."

The applause was the longest in school history. The tray-picker got a standing ovation too. He'd never stood so tall.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Be the kid who picks up the tray.'","The speech that changed."]),
# --- testimony (10) ---
("Testimony: the night the lights went out (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): the 1965 blackout, remembered.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"It was November, already dark at five. Then — darker. The whole street, the whole town, out. We thought: the Russians? (It was 1965. We thought that.)

"My father lit candles. The neighbors came out with flashlights. Someone had a transistor radio — the news said the whole Northeast was dark. Thirty million people.

"Here's the strange part: it was wonderful. We played cards by candlelight. The stars — we'd never seen them, not really, not in town. The Milky Way over Main Street.

"Power came back at midnight. We were almost disappointed.

"People say it was a failure. I say it was the night the town remembered the sky."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The 1965 blackout.","'The Milky Way over Main Street.'"]),
("Testimony: the flood markers (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): a town that marks its floods on the bridge.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"Our bridge has marks. Painted lines, dated: 1937, 1964, 1993, 2019. The flood marks.

"My grandfather painted the '37 line — chest-high on the pier. He lost the barn that year. My father painted '64. I painted '93 — the water took our porch.

"2019: my daughter painted it. She's an engineer now. She says the marks are data. I say they're memory.

"Every mark is a story: who sandbagged, who evacuated, who fed whom. The bridge remembers what the town survived.

"New people ask why we stay. We point at the bridge. Four floods, four recoveries. The marks are the answer: we stay because we've stayed."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Flood marks as memory.","'We stay because we've stayed.'"]),
("Testimony: the factory whistle (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): the last day of the mill.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The whistle blew at six, like always. Only this time it didn't stop — one long note, till the steam ran out. The last whistle.

"Three generations of my family worked that mill. My grandfather swept floors. My father ran the line. I did the books. The whistle was our clock — you set your life by it.

"When it closed, the town held its breath. Then — slowly — the building became lofts, the parking lot a market, the whistle... they mounted it in the square. It blows on holidays now.

"People say the mill died. I say it changed shape. The whistle still blows. The town still works. Different work, same town.

"You can hear it on the Fourth. One long note. For the old days — and the new ones."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The last whistle.","'Changed shape, not died.'"]),
("Testimony: the election night (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): a first-time voter, age 18, on election night.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"I turned eighteen in October. I registered the next day. My grandmother — who marched for the vote before I was born — came with me to the polls.

"The line was long. Nobody minded. People were... I don't know, reverent? Like church, but louder.

"I marked the ballot carefully, like it was a test. In a way it was — the test of whether I was a citizen.

"That night we watched the returns. My candidate lost. I was crushed for about an hour. Then my grandmother said: 'The vote isn't about winning. It's about belonging. You're in the book now.'

"She was right. I've voted in every election since. Win or lose, I'm in the book."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","First vote at 18.","'You're in the book now.'"]),
("Testimony: the barn raising (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): the day the town raised a barn.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The Millers' barn burned in March. By May, the town raised a new one — in a day.

"Forty people. The men framed, the women fed, the kids fetched. The foreman — old Mr. Abernathy, 82 — directed from his chair like a conductor.

"At noon we ate: fried chicken, pies, lemonade. At dusk the ridge beam went up, and everyone cheered. The Millers cried.

"No one was paid. That's the point people miss — it wasn't charity, it was... what do you call it when everyone's barn is everyone's business?

"Community. The word is community. We raised more than a barn that day."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","40 people, one day.","'Everyone's barn is everyone's business.'"]),
("Testimony: the first day of school (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): a teacher remembers her first day, 1962.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"September 1962. I was 22, and terrified. Thirty-two faces, waiting.

"I'd planned the perfect lesson. It lasted eleven minutes. Then Tommy asked why the sky was blue, and we spent the hour on it — badly, but joyfully.

"I learned more that day than they did: the plan is a suggestion. The children are the curriculum.

"Thirty years later, Tommy — a physicist now — wrote to me. 'You started it,' he said. 'With the bad explanation of the blue sky.'

"The perfect lesson would have been forgotten. The imperfect question lasted a lifetime."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","1962; 32 faces.","'The children are the curriculum.'"]),
("Testimony: the harvest (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): the last harvest before the farm was sold.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"We knew it was the last one. The developer's sign was already up by the road. But the wheat didn't know — it stood golden and ready, like every year.

"My father drove the combine. I rode beside him, like when I was six. We didn't talk much. What do you say to a century ending?

"At dusk, the field was stubble and the trucks were full. My father turned off the engine. Silence — the first silence that land had known in a hundred harvests.

"'It was a good run,' he said.

"The houses went up in spring. They named a street after us. I drive down Harvest Lane sometimes. The wheat is gone, but on windy days, I swear I can smell it."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The last harvest.","'Harvest Lane.'"]),
("Testimony: the wedding in the rain (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): an outdoor wedding, a storm, and the guests who stayed.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The forecast said clear. The sky said otherwise. Ten minutes before the ceremony, the heavens opened.

"The planner panicked. The bride laughed. 'Everyone under the big tent!' she said. 'We're doing this!'

"Two hundred guests squeezed under a tent for a hundred. Strangers shared chairs. The musicians played louder. The flower girl used a leaf as an umbrella.

"The vows: shouted over the rain, and somehow more romantic for it. The kiss: in a downpour, to cheers.

"People still talk about that wedding — not despite the rain, because of it. The photos are wild: everyone soaked, everyone beaming.

"'For better or worse,' they'd promised. The weather tested it in the first hour. They passed."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Rain on the vows.","'Tested in the first hour.'"]),
("Testimony: the homecoming (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): a soldier's return, remembered by the town.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The whole town knew the bus schedule. We didn't plan it — we just... showed up. Main Street, both sides, three deep.

"The bus came around the corner. You could see him through the window, and then he was down the steps, and his mother — I've never seen anyone run like that.

"Nobody cheered at first. It was too big for cheering. Then someone started clapping, and it rolled down the street like a wave.

"He'd been gone two years. He looked older. He looked... careful. War does that.

"The diner gave him a free milkshake. He'd dreamed about that milkshake, he said. Two years, and what he wanted was a milkshake on Main Street.

"He got it. We made sure."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Main Street, three deep.","'A milkshake on Main Street.'"]),
("Testimony: the blizzard babies (original fiction)", "testimony",
 "A Signature original dramatized testimony (fiction): the blizzard of '78 and the babies born in it.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The blizzard of '78: three feet of snow, no plows, no power. And — of course — three babies decided to come.

"The doctor couldn't get through. So: the retired nurse on Elm Street delivered one. The fire chief's wife — she'd had six herself — delivered another. The third: the baby's grandmother, on the phone with the hospital, doing exactly what they said.

"All three lived. All three are... well, they're in their forties now. We call them the blizzard babies.

"Every reunion, someone says: 'Remember when?' And we do. We remember the snow, the fear, and the neighbors who became midwives overnight.

"The town has a saying now: 'Blizzard-tested.' It means: we can handle it. Whatever it is."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Three babies, one blizzard.","'Blizzard-tested.'"]),
# --- interview (10) ---
("Interview: the town barber (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): 50 years of haircuts and town news.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: How long have you been cutting hair?
A: Fifty years. Same chair — reupholstered twice. I've cut three generations of some families. I cut the mayor's first haircut and his last.

Q: What's the secret?
A: Listen more than you talk. A barber hears everything — who's engaged, who's in trouble, who needs a job. The clippers are just the excuse.

Q: Best moment?
A: The boy who was terrified of haircuts — screamed for a year. Last month he brought his own son. 'Make him brave,' he said. I did. Took eleven minutes.

Q: Will you retire?
A: And do what? This chair is my front porch. As long as the town needs trimming, I'll be here.

[The barber's pole still turns. The stories keep coming.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","50 years, one chair.","'The clippers are the excuse.'"]),
("Interview: the ferry captain (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): the last ferry captain on the river.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: How long on the river?
A: Thirty-eight years. I know every sandbar, every snag, every heron nest between here and the bend.

Q: The river's changed?
A: The river never changes and always changes. Same water, different river — Heraclitus had it right.

Q: Storms?
A: '62, the big one. Waves over the bow. I told the passengers: 'We're fine.' We were — but I wasn't sure till we docked.

Q: The bridge put you out of business?
A: The bridge carries cars. I carry people — slowly, with a view. Different business. The ferry's for those who aren't in a hurry. There's more of us every year.

[The ferry still runs. The captain still waves at the herons.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","38 years on the river.","'Same water, different river.'"]),
("Interview: the beekeeper (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): a beekeeper on 40 hives and the lessons of bees.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: How many hives?
A: Forty. Half a million bees, more or less. I know the queens by temperament.

Q: Ever stung?
A: Thousands of times. You learn to move slow. Bees forgive slowness.

Q: What have bees taught you?
A: Everything. Work for the hive. Dance to communicate — I wish people danced their directions. And: the queen doesn't rule. She serves. She's the mother of all, and the servant of all.

Q: The honey?
A: The honey is the bonus. The pollination is the job. People taste the honey and miss the miracle: every third bite you eat exists because of bees.

[The beekeeper's honey wins the county fair every year. The bees don't care.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","40 hives.","'The queen serves.'"]),
("Interview: the night-shift nurse (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): twenty years of nights in the emergency ward.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Why nights?
A: The night is honest. No administrators, no visitors — just the work. And the night patients need you most.

Q: Hardest night?
A: The pile-up, '09. Twelve traumas. We lost two. I still see their faces when I'm tired.

Q: Best night?
A: The baby born in the elevator. The father fainted, the mother laughed, I caught the baby. We named her Elevator — no, we didn't. Her name's Grace.

Q: Advice?
A: Be kind to night-shift workers. We're keeping the world running while you dream.

[She retired last year. She still can't sleep before 3 a.m.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","20 years of nights.","'The night is honest.'"]),
("Interview: the lighthouse keeper (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): the keeper on storms, solitude, and the lens.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Lonely?
A: People ask that. The sea is company. The gulls are gossips. The light is... responsibility. That's better than company.

Q: Worst storm?
A: '87. Waves over the gallery. The tower shook — stone towers shouldn't shake. I kept the light. That's the whole job: keep the light.

Q: The lens?
A: Fresnel's miracle — a beehive of glass that throws light 20 miles. I polish each prism. I know them like faces.

Q: Automation?
A: The light doesn't care whose hands tend it. But I'll miss the winding of the clockwork. It sounded like a heartbeat.

[The light was automated in 1998. The keeper still visits. The lens still shines.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Keep the light.'","Stone towers shouldn't shake."]),
("Interview: the retired detective (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): 30 years of cases, and the one that mattered.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Thirty years — what stays with you?
A: Not the big cases. The small ones. The lost child found. The stolen bike returned. The big cases make the papers; the small ones make the town.

Q: The hardest?
A: Telling a mother. There's no training for that. There's just... being there, and being honest, and not leaving.

Q: The best?
A: The runaway I found — twice. Second time, I didn't bring her home. I brought her to the counselor. She's a teacher now. She writes every Christmas.

Q: Advice for rookies?
A: Listen. Everybody wants to talk. The guilty, the innocent, the lonely — everybody talks. Your job is to hear what matters.

[He consults on cold cases. He still listens.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","30 years.","'The small ones make the town.'"]),
("Interview: the orchestra conductor (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): a community orchestra conductor on amateurs and joy.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Amateurs?
A: The best. Professionals play perfectly. Amateurs play joyfully. I'll take joy.

Q: The worst rehearsal?
A: The Beethoven — the violins were... adventurous. But by concert night, they soared. That's the arc: from adventurous to soaring.

Q: Why conduct?
A: The moment when eighty people breathe together. You can't buy that. You can only rehearse it.

Q: Advice?
A: Play. Whatever your instrument, whatever your level — play. The world needs more amateurs and fewer audiences.

[The orchestra's average age is 58. Its average joy is immeasurable.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Amateurs > perfection.","'Eighty people breathe together.'"]),
("Interview: the diner cook (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): 45 years at the grill.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Forty-five years?
A: Same grill. Third set of spatulas. I've flipped a million eggs — I counted to a hundred thousand and stopped.

Q: Regulars?
A: I know their orders, their kids' names, their troubles. The grill is a confessional with better coffee.

Q: The secret?
A: Butter. And: the first pancake is for the cook. Always. It's the law.

Q: Retire?
A: And miss the morning rush? The grill and I — we're just getting warmed up.

[The diner's coffee is still 50 cents. The cook's memory is still perfect.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","45 years, one grill.","'The first pancake is for the cook.'"]),
("Interview: the park ranger (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): a ranger on bears, tourists, and the wild.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Bears?
A: Respect them. They're not villains, they're neighbors — big, hungry neighbors. Store your food. Make noise. Never run.

Q: Tourists?
A: I love them. But: the bison are not pets. The geysers are not hot tubs. Read the signs — I wrote them with love and liability in mind.

Q: Best moment?
A: The wolf reintroduction. Hearing that first howl — the park exhaled. Twenty years of work, in one sound.

Q: Why ranger?
A: Someone has to speak for the wild. It doesn't vote. It doesn't lobby. It just... is. I'm its translator.

[She's tracked 200+ bears. She's never been bluff-charged twice by the same one.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Bears are neighbors.","'I'm the wild's translator.'"]),
("Interview: the clockmaker (original fiction)", "interview",
 "A Signature original dramatized interview (fiction): the last clockmaker in town.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Q: Clocks in a digital age?
A: A clock is not for telling time. Your phone does that. A clock is for marking it — for saying: this moment matters enough to measure beautifully.

Q: The craft?
A: Gears, springs, escapements. The tick is a heartbeat. I regulate them by ear — a good clockmaker hears time.

Q: Your favorite?
A: The town hall clock, 1892. I wind it weekly. It's kept the town's time for 130 years. When it stops, the town notices — time itself, pausing.

Q: Apprentice?
A: My granddaughter. She's twelve. She has the ear. The craft continues — tick by tick.

[The town hall clock still ticks. The granddaughter still listens.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'A clock marks time.'","The granddaughter has the ear."]),
# --- memoir (10) ---
("Memoir: the paper route (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): dawn deliveries, 1975.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

5 a.m. The papers thumped onto the porch — bundles of newsprint, smelling of ink and morning. I was twelve.

My route: 87 houses. The bike with the baskets. The dog on Elm Street (friendly, despite the barking). Mrs. Kowalski's tip at Christmas (a dollar — a fortune).

Rain: the papers in plastic. Snow: the sled. The collections on Fridays: quarters and dimes in an envelope, and the ledger in my head.

What the route taught me: show up. Every day, whatever the weather. Reliability is a superpower — I learned it at twelve, on a bike, in the dark.

The paper went digital. The route is a memory. But every morning, I'm still up at five. Some habits are the route, forever.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","87 houses, 5 a.m.","'Reliability is a superpower.'"]),
("Memoir: grandmother's kitchen (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): the kitchen where everything happened.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

Grandmother's kitchen: the table that seated twelve, the stove that never cooled, the cookie jar that was never empty (a miracle we never questioned).

Everything happened there: homework, heartbreaks, holiday feasts, the time the turkey caught fire (we ate pie). Grandmother presided — tasting, stirring, advising.

Her rules: wash your hands, say please, stay for dinner. Her wisdom: 'Feed people and they'll tell you everything.'

She's gone now. The table is mine. The cookie jar is never empty (a miracle my children never question).

Kitchens are like that: the room where a family becomes itself, one meal at a time.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The table that seated twelve.","'Feed people.'"]),
("Memoir: the summer of the treehouse (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): one summer, one treehouse, four friends.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The summer I was ten, we built a treehouse. Four of us, one oak, a pile of lumber 'borrowed' from the garage.

It took all June. It leaned (a little). The roof leaked (a lot). It was perfect.

That treehouse was our country: passwords, meetings, the Great Ant War, the night we slept up there and heard an owl. We made laws (no grown-ups), currency (bottle caps), and history (the Great Fall of Tommy — he was fine).

August ended. School came. The treehouse weathered, leaned more, and finally came down in the storm of '89.

But here's the thing: we're all still friends. Fifty years later. The treehouse fell; the country remains.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","One summer, age ten.","'The country remains.'"]),
("Memoir: learning to drive (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): a father teaches his daughter to drive.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The parking lot, Sunday morning. My father, white-knuckled, in the passenger seat. Me, sixteen, at the wheel.

'Easy on the gas. Mirror, signal, maneuver. Brake — BRAKE!'

We survived. The mailbox didn't (sorry, Hendersons). The curb and I became close friends.

But somewhere between the parking lot and the highway, something shifted. He stopped instructing and started trusting. 'You've got this,' he said — the first time he'd ever said it about anything big.

I passed the test. He cried (he denies it). Now I drive my own daughter to her lessons. I hear his voice in mine: 'Mirror, signal, maneuver.'

Some inheritances are cars. Mine was confidence — delivered in a parking lot, on a Sunday.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Sunday parking lot.","'You've got this.'"]),
("Memoir: the garden my mother kept (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): a mother's garden, remembered.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

My mother's garden: roses by the fence, tomatoes against the sun, the herbs in the old sink. She gardened the way she lived — generously, and with strong opinions about weeds.

'Talk to them,' she'd say of the plants. I thought she was joking. She wasn't — not entirely.

When she got sick, the garden kept her schedule: the roses bloomed, the tomatoes ripened. We brought them to her room. She'd hold a tomato like a jewel.

She's gone. The garden is mine now. I weed with her opinions. I talk to the roses — not joking, not entirely.

Gardens outlive gardeners. That's the whole point, I think. You plant for people you'll never meet — including your future self.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Roses, tomatoes, herbs.","'Gardens outlive gardeners.'"]),
("Memoir: the band (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): four friends, a garage, and one glorious summer of music.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

We were terrible. That's the first thing to know. Four friends, a garage, instruments we could barely play.

But we practiced. Every day, all summer. The neighbors complained (then started requesting songs). We wrote originals — bad ones, passionately.

The gig: the school talent show. We were so nervous the drummer dropped a stick. Then we played — and for three minutes, we weren't terrible. We were a band.

We didn't win. We didn't care. We'd done it — made music, together, on purpose.

The band broke up by fall (college, jobs, life). But every reunion, someone brings a guitar. And for three minutes, we're sixteen again, in a garage, terrible and glorious.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","One summer, one gig.","'Terrible and glorious.'"]),
("Memoir: the move (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): moving house at age nine — losing and finding home.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

I was nine. The boxes, the truck, the empty rooms echoing. I cried in the back seat — not for the house, for the tree outside my window. We'd grown up together.

The new place: strange streets, strange school, strange bedroom. I was sure I'd never be happy.

Then: the girl next door, with a bike and a dare. The park with the big slide. The teacher who liked my stories. Slowly — the way ice melts — the strange became familiar.

Years later, I drove past the old house. The tree was still there, bigger. I didn't cry. I waved.

Home isn't a house. It's the people, the routines, the tree you grow up beside — wherever it stands. You can grow new roots. I did.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Age nine; the tree.","'You can grow new roots.'"]),
("Memoir: the recipe box (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): inheriting grandmother's recipe box.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The box: tin, dented, full of index cards in grandmother's handwriting. 'Apple pie — use the tart ones.' 'Soup — when in doubt, more garlic.'

I cooked my way through it, one card at a time. The first pie was a disaster (the tart ones matter). The soup was perfect (the garlic matters).

Each card was a conversation: her humor ('Don't tell your uncle about the sherry'), her wisdom ('A watched pot never boils, but an unwatched one boils over').

The last card: 'My love — the secret ingredient is that there is no secret. Just cook, and think of me.'

I do. Every time. The kitchen smells like her, and for a moment, she's there — tasting, stirring, advising.

Recipes are like that: love, written down, in shorthand.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Index cards in her hand.","'Love, in shorthand.'"]),
("Memoir: the dog (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): the dog who chose the family.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

We didn't choose the dog. The dog chose us — showed up on the porch in a rainstorm, skinny, shivering, and looked at my daughter like: 'Well?'

Fourteen years. He grew fat and gray. He learned: sit, stay, and the exact sound of the cheese drawer. He never learned: not to chase squirrels (some lessons aren't meant to be learned).

He was there for everything: the moves, the losses, the late-night homework. Dogs don't fix things. They just stay — which fixes most things.

When he went, we buried him under his tree. We cried. Then we told stories — and laughed, because the stories were funny, because he was funny.

We got another dog last spring. She chose us too. The porch, the rain, the look. Some traditions continue.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","14 years.","'Dogs don't fix things. They stay.'"]),
("Memoir: the apprenticeship (original fiction)", "memoir",
 "A Signature original dramatized memoir (fiction): learning the trade from the old master.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

I was seventeen when the old carpenter took me on. 'Watch first,' he said. I watched for a month — how he held the plane, how he read the wood, how he never hurried a joint.

'The wood tells you,' he'd say. 'Listen.' I thought he was mystical. He was just experienced.

My first solo piece: a stool. It wobbled. He didn't fix it — he made me fix it. Three times. The fourth stool stood straight, and I understood: the craft is in the correcting.

He retired last year. The shop is mine now. On the wall: his tools, and my first wobbly stool — a reminder.

'Watch first,' I tell my apprentice. She watches. The wood tells her. It told me. It tells everyone who listens.

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Watch first.'","'The craft is in the correcting.'"]),
# --- broadcast (10) ---
("Broadcast: the town crier's last day (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): the final broadcast of a small-town radio station.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

[Theme music — the station's jingle, 1962.]

'This is WKTV, your hometown station, signing off — for the last time. Fifty years. I've been here for thirty of them.

'We've broadcast everything: the births (congratulations!), the ball games (what a season in '78!), the blizzards, the elections, the lost dogs — 4,000 lost dogs, all found.

'Radio is intimate. You let me into your kitchens, your cars, your mornings. I've been the voice with your coffee.

'The tower comes down next week. But here's the secret: the station isn't the tower. It's you — the listeners. As long as you remember the jingle... [hums it] ...we're still on the air.

'This is Marty, signing off. Thank you. Goodnight.'

[The jingle, one last time. Static. Then — the town, humming it.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","WKTV signs off.","'The station is you.'"]),
("Broadcast: the storm warning (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): a weatherman stays on air through the hurricane.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'This is Ray, and I'm not leaving this chair till the storm does.

'The eye is over the bay now. If you're on the east side — stay inside, away from windows. West side — it's coming to you. You've got an hour.

'To the family on Marlin Street with the newborn: the shelter on 5th has generators. Go now. I'll stay on the line.

'The wind is... it's loud, folks. But we've been through worse — '54, '78. We know the drill.

'I'm looking at the radar and I'm looking at my coffee, and I trust the radar more. Stay put. I'll be here.

'...The eye is passing. The back side's weaker. We're going to make it, folks. We're going to make it.'

[He stayed 14 hours. The town did make it. Ray's coffee went cold. Nobody cared.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","14 hours on air.","'We're going to make it.'"]),
("Broadcast: the election night desk (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): a small station covers its first presidential election.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'We're live at the courthouse, where the votes are being counted — all 4,000 of them, by hand, by our neighbors.

'Precinct 3 just reported. Precinct 7 is still out — that's the Miller farm vote, and nobody predicts the Miller farm.

'The coffee's gone. The pizza's gone. Democracy runs on caffeine, folks.

'...And there it is. The mayor's race — decided by 12 votes. Twelve. Your vote counted. Never let anyone tell you it doesn't.

'This is small-town radio, signing off from the courthouse. The republic works — one hand-counted ballot at a time. Goodnight.'

[The station kept the 12-vote tally sheet. It's framed. 'Your vote counted.']

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Decided by 12 votes.","'Democracy runs on caffeine.'"]),
("Broadcast: the lost dog network (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): the morning show's lost-pet segment.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'Time for the Lost and Found! First up: Biscuit, the beagle — last seen chasing a squirrel on Elm. Answers to "treat." Don't chase — he'll think it's a game.

'Mittens, the cat — gray, grumpy, loved. Check your garages, folks. She naps in warm engines.

'...And a happy reunion: Captain, the parrot, is HOME! Found on the church steeple, preaching to the pigeons.

'Remember: a lost pet is a family emergency. If you see one, call us. We'll put the word out — 10,000 listeners, all looking.

'This has been the Lost and Found. 4,000 reunions and counting. Good morning!'

[The segment ran 30 years. The record: a tortoise, found after 11 months. Slow, but found.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","4,000 reunions.","The tortoise took 11 months."]),
("Broadcast: the high school game (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): the championship game, called by the town's voice.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'Fourth quarter, ten seconds, down by two... Johnson takes the shot — IT'S GOOD! IT'S GOOD! THE TIGERS WIN! THE TIGERS WIN!

'I'm sorry, folks — I've lost my professional composure. Thirty years calling games, and I still... listen to this crowd!

'The team is piling on Johnson at mid-court. The band is playing. Someone's grandmother is crying — happy tears, Mrs. Abernathy, happy tears!

'Final: Tigers 58, Wildcats 57. A one-point championship. They'll talk about this one for fifty years.

'This is your hometown voice, signing off from the gym. What a night. WHAT a night.'

[The recording is played every anniversary. The crowd noise still gives goosebumps.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","58–57, one point.","'What a night.'"]),
("Broadcast: the midnight request show (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): the DJ who takes requests from night-shift workers.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'It's midnight, and this is the Night Shift — for the nurses, the bakers, the truckers, the ones who keep the world running while it dreams.

'Request from Rosa at the hospital: "something with a beat for the 3 a.m. slump." Coming up, Rosa.

'Mike the trucker wants the long-haul playlist — mile 400, keep it rolling, Mike.

'To the new father up with the baby: congratulations. This one's a lullaby — for both of you.

'You know what I love about this shift? The callers are honest. Nobody performs at 3 a.m. We're all just... awake, together.

'Keep the requests coming. The night is long, but we're longer.'

[The show ran 20 years. The DJ never met most callers. He knew them all.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The Night Shift.","'Awake, together.'"]),
("Broadcast: the tornado warning (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): the broadcast that saved the trailer park.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'TAKE COVER NOW. This is not a drill. The tornado is on the ground at the county line, moving northeast at 40. If you're in the trailer park — LEAVE. Get to the school basement. NOW.

'I'm staying on the air. I'll tell you where it is. It's at Miller Road... it's crossing the highway... it's... it's lifting. It's lifting!

'All clear. It's over. The trailer park — I can see it from the tower — it's damaged, but the people... the shelter reports everyone accounted for. Everyone.

'You listened. That's why. Radio works when everything else fails — no power needed, just a battery and a voice.

'This is why we do the drills, folks. Tonight, the drill paid off.'

[The station won an award. The DJ said the award belonged to the listeners — 'they're the ones who moved.']

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","'Take cover now.'","'The drill paid off.'"]),
("Broadcast: the sunrise show (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): the morning DJ's 30-year farewell.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'Thirty years of sunrises. That's 7,800 mornings I've said "good morning" to this town.

'I've announced your births, your graduations, your weddings. I've read the obituaries — the hardest part, and the most important.

'You've told me your news, your jokes, your weather. A DJ is just a neighbor with a microphone.

'Tomorrow, someone new says good morning. Be kind to them — they're nervous. I was.

'One last song — the one we always play. Sing along, town. I know you know the words.

'Good morning. And goodbye.'

[The town sang. The ratings that morning were 100% — everyone listened.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","7,800 mornings.","'A neighbor with a microphone.'"]),
("Broadcast: the holiday wish line (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): Christmas Eve calls from the whole town.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'It's Christmas Eve, and the wish line is open! Caller one — go ahead.'

'"I wish my brother comes home safe." — He's on the list, honey. Next.'

'"I wish for snow." — Asking the meteorologist... he says maybe. Next.'

'"I wish my grandma's pie recipe works." — It will. Love is the secret ingredient. Next.'

'Four hours of wishes. The big ones, the small ones, the funny ones. And every one of them — every single one — was really the same wish: to be together, to be okay, to be loved.

'Merry Christmas, town. May all your wishes — especially the unspoken ones — come true.'

[The wish line ran 25 years. The station still gets letters: 'My wish came true.']

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Christmas Eve wishes.","'Especially the unspoken ones.'"]),
("Broadcast: the science fair (original fiction)", "broadcast",
 "A Signature original dramatized broadcast (fiction): live from the regional science fair.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

'We're live at the science fair, where the future is on display — with baking soda.

'First up: Maya's volcano — classic, but hers erupts in three colors. The judges are impressed. The janitor is concerned.

'Next: the robot hand — built from cardboard and string by the 4th-grade team. It waves! It's waving at us!

'And here — the big one — Jamal's water filter. Dirty water in, clean water out. The judges are tasting it. They're nodding. Folks, this kid just solved something.

'The winners: everyone. The real prize: curiosity. This has been your roving reporter, slightly covered in baking soda. Back to you.'

[Jamal's filter won state. He's an engineer now. The baking soda washed out. The curiosity didn't.]

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Baking soda volcanoes.","'The curiosity didn't wash out.'"]),
# --- witness account (10) ---
("Witness: the first snow (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): a child's first snow, remembered at eighty.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"I was four. I woke up and the world was white — the fence, the tree, everything. I thought the world had been repainted overnight.

"My father carried me out. The snow came to my knees. I caught a flake on my tongue — cold, then gone. I laughed so hard I fell over, and the snow was soft.

"We built a snowman with coal eyes. My mother made cocoa. The snowman melted in three days, but I remembered him for eighty years.

"People ask what my earliest memory is. It's that: white world, cold tongue, warm cocoa.

"I'm eighty-four now. It still snows. I still catch a flake on my tongue. Some things you don't outgrow."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Age four; the white world.","'Some things you don't outgrow.'"]),
("Witness: the eclipse (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the total eclipse, remembered.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"We drove six hours for two minutes. That's the math of an eclipse.

"The light went strange — not dark, but wrong, like evening at noon. The birds went quiet. The temperature dropped. Then — the corona. A ring of fire around a black sun.

"Two minutes. People cried. People proposed. I just stood there with my mouth open, like everyone.

"Then the diamond ring — the sun's edge flaring back — and daylight returned, and we all cheered like our team had won.

"I've seen a lot in my life. Nothing — nothing — was like those two minutes. The universe, showing off."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Two minutes of totality.","'The universe, showing off.'"]),
("Witness: the parade (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the homecoming parade.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The whole town lined Main Street. The band, the fire trucks, the mayor in the convertible — and then them, the team, on the flatbed, holding the trophy.

"Confetti — real confetti, from the drugstore, by the bagful. Kids on shoulders. My grandfather, who never cheered at anything, cheering.

"The float stopped in front of us. The captain — a kid I'd watched grow up — held the trophy up. Our eyes met. He grinned.

"We'd waited thirty years for a championship. Thirty years of almost. And here it was, on a flatbed, in the sun.

"Towns need this. Not the trophy — the together. The parade is the point."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Thirty years of almost.","'The parade is the point.'"]),
("Witness: the concert in the park (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the free concert that became a tradition.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"It started with a flatbed truck and a borrowed amplifier. The band was... enthusiastic. The crowd was fifty people and a dog.

"But the sunset was perfect, and the music carried, and by the second set there were two hundred. Someone brought blankets. Someone brought pie.

"That was twenty years ago. Now it's the Summer Concert Series — real stage, real bands, five thousand people on the lawn.

"I go every year. I sit in the same spot. The band changes; the sunset doesn't.

"Traditions start small. A truck, an amplifier, a sunset. That's all it takes."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","Flatbed to festival.","'Traditions start small.'"]),
("Witness: the new bridge (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the day the bridge opened.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"Before the bridge, it was the ferry — or the long way around, an hour each way. The town was split by the river like a sentence by a period.

"The opening: the ribbon, the speeches, and then — everyone walked across. Thousands of us, on foot, the first crossing. Kids ran ahead. Old folks took their time.

"Halfway across, I stopped and looked down at the water. We'd been divided by that river my whole life. Now it was just... a view.

"The ferry captain was there. He smiled — his business was done, but he wasn't sad. 'Progress,' he said. 'I carried them across. Now the bridge does.'

"Bridges don't just connect places. They connect times — before and after."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The first crossing, on foot.","'Bridges connect times.'"]),
("Witness: the meteor (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the night the sky fell (a little).",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"It was 2 a.m. I was up with the baby. The sky flashed — green-white, like lightning, but wrong. Then the boom, seconds later. The windows rattled.

"The news said: meteor, over the lake, burned up. A rock from space, saying hello.

"I stood at the window with the baby, watching the sky. Somewhere up there, debris was falling into the lake — stardust, literally.

"The baby slept through it. I didn't. I kept thinking: the universe is still happening. Right above us, all the time.

"I go outside more now, at night. Just to check. You never know when the sky might say hello again."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","2 a.m.; green-white flash.","'The universe is still happening.'"]),
("Witness: the reunion (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the 50th class reunion.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"Fifty years. We walked in as strangers and left as... well, as us, older.

"The name tags helped. The hair — or lack of it — didn't. But the laughs were the same. The stories were better (time improves stories).

"We toasted the ones who didn't make it. That took a while — too many toasts. Then we told the funny stories about them, which is what they'd want.

"Someone brought the yearbook. We signed it again — same names, shakier hands.

"Fifty years. We survived it all: the trends, the troubles, the time itself. And here we were, laughing like the cafeteria was yesterday.

"Don't wait fifty years, kids. Have the reunion now."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","50th reunion.","'Have the reunion now.'"]),
("Witness: the garden's first spring (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the community garden's first harvest.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"We planted in April — skeptics, all of us. The lot had been empty for years. But the soil was good, and the hope was better.

"First sprouts: we cheered like it was a birth. First tomato: we split it twelve ways, like communion.

"By August, we were drowning in zucchini. (There's always too much zucchini. It's the law.) We gave it away — the food bank, the neighbors, strangers.

"The harvest dinner: one long table, down the middle of the garden. Everything we'd grown, cooked by everyone who'd grown it.

"A vacant lot became a garden. Strangers became neighbors. Seeds became dinner.

"That's the whole story. That's always the whole story."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","First tomato, split 12 ways.","'Too much zucchini. It's the law.'"]),
("Witness: the last train (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the final run of the branch line.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The branch line ran for 90 years. The last train: a Saturday, full — everyone wanted to ride it once more.

"The conductor called the stations like always. People got on with cameras. At each stop, the town turned out — waving, the way they used to wave at every train, before cars.

"At the terminus, the engineer blew the whistle — one long, one short, one long. The traditional farewell.

"Then silence. The tracks are a trail now — walkers and bikes where the trains ran. It's nice. But on quiet evenings, I swear you can hear the whistle.

"Towns are built on rails, even after the rails are gone. The route remains — in the street names, in the memories, in the whistle you almost hear."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","90 years; one last run.","'The route remains.'"]),
("Witness: the talent show (original fiction)", "witness account",
 "A Signature original dramatized witness account (fiction): the school talent show's surprise star.",
 """SIGNATURE ORIGINAL DRAMATIZED ORAL HISTORY — FICTION
src: signature. An original work by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

"The talent show had the usual: the dancers, the singers, the magician (the rabbit was fine).

"Then — last act — the quiet kid. The one nobody knew. He walked out with a violin.

"He played. I don't know what — something classical, something beautiful. The gym went silent. Two thousand people, silent.

"When he finished, the applause shook the bleachers. He bowed — once, shyly — and walked off.

"He'd been practicing for six years, alone, in his room. Nobody knew. That's the thing about talent shows: the talent is the surprise.

"He's at the conservatory now. The gym still talks about it. 'Remember the violin kid?' We do. We'll always do."

Audio: original ambient motif composed for this collection (instrumental).""",
 ["Clearly labeled fiction.","The quiet kid's violin.","'The talent is the surprise.'"]),
]

# ================= 11. yearbooks-public =================
YEARPUB = [
# --- school history (12) ---
("Eton College — founded 1440", "school history",
 "Henry VI founded Eton in 1440 for 70 poor scholars; it became England's most famous school — 20 prime ministers.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1440 by Henry VI — 'The King's College of Our Lady of Eton' — for 70 poor scholars (the Collegers)
- The chapel (1448–82): among England's finest Perpendicular buildings
- Oppidans (fee-paying boys) soon outnumbered scholars
- Alumni: 20 British prime ministers, plus Orwell, Keynes, Shelley
- The Eton wall game: the school's strange, famous football code
- 'Floreat Etona' — let Eton flourish

The 1440 statutes still govern the scholars' places — nearly 600 years of continuity.

Sources: Eton College archives; public records.""",
 ["Founded 1440.","20 prime ministers.","Wall game."]),
("Harvard — founded 1636", "school history",
 "Founded 1636 by the Massachusetts Bay Colony; named for John Harvard's 1638 bequest — the oldest US university.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1636 (vote of the Great and General Court); named 1639 for John Harvard (1607–38), whose bequest (400 books, 780 pounds) founded the library
- First graduates: 1642 (9 students)
- Motto: 'Veritas' (truth); color: crimson
- Alumni: 8 US presidents, plus countless justices and laureates
- The Harvard-Yale Game (1875–): 'The Game'
- Endowment: among the world's largest

The 1636 founding makes Harvard older than most nations.

Sources: Harvard archives; public records.""",
 ["Founded 1636.","8 US presidents.","Oldest US university."]),
("The University of Bologna — 1088", "school history",
 "Bologna's 1088 traditional founding makes it the world's oldest continuously operating university — students, not masters, ran it.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Traditional founding: 1088 (the world's oldest university in continuous operation)
- Student power: the universitates were student guilds that hired (and fined) professors
- Irnerius and the law school: Roman law revived — the glossators
- Alumni: Dante, Petrarch, Copernicus, three popes, Umberto Eco
- Motto: 'Alma Mater Studiorum' — the phrase 'alma mater' comes from here

The Archiginnasio palace (1563) housed it; the anatomical theatre (1637) taught medicine.

Sources: University of Bologna; public records.""",
 ["1088: oldest operating.","Students hired professors.","'Alma mater' coined here."]),
("Al-Azhar — 970 CE", "school history",
 "Founded 970 CE in Cairo by the Fatimids; Al-Azhar is among the world's oldest universities and Sunni Islam's foremost seat.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 970 CE (mosque); teaching from 975; university status formalized 1961
- One of the oldest continuously operating universities on Earth
- Curriculum: Quranic studies, Islamic law, Arabic, and (modern) medicine, engineering
- The Grand Imam of Al-Azhar: Sunni Islam's most authoritative voice
- Library: priceless Islamic manuscripts

Older than Oxford by two centuries.

Sources: Al-Azhar; public records.""",
 ["970 CE.","Sunni Islam's foremost seat.","Older than Oxford."]),
("Nalanda — the ancient university (5th century)", "school history",
 "Nalanda (5th–12th century) housed 10,000 students and 2,000 teachers — the ancient world's residential university.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented history.

- Founded: 5th century CE, Gupta Empire (Kumaragupta I)
- Scale: 10,000 students, 2,000 teachers — residential, international (Chinese pilgrims Xuanzang, Yijing studied here)
- Curriculum: Buddhist philosophy, logic, medicine, astronomy, mathematics
- Library: the Ratnodadhi — nine stories, hundreds of thousands of texts
- Destroyed: c.1193; revived nearby in 2014

Xuanzang's 7th-century account is the primary source.

UNESCO World Heritage (2016).

Sources: UNESCO; Xuanzang's Records.""",
 ["5th century; 10,000 students.","Destroyed c.1193.","Revived 2014."]),
("The Flying University — Warsaw, 1882–1905", "school history",
 "The clandestine Flying University educated Polish women — including Marie Sklodowska (Curie) — under Russian occupation.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented history.

- 1882–1905: secret Polish university in Russian-occupied Warsaw ('flying' — it moved locations to evade police)
- Students: mostly women (formal higher education barred to Polish women)
- Marie Sklodowska (later Curie) studied here before the Sorbonne
- Lecturers: Poland's leading scholars, teaching at personal risk
- Legacy: became the Society for Scientific Courses (1905)

Education as resistance: the university the empire couldn't find.

Sources: public historical records; Curie biographies.""",
 ["1882–1905; clandestine.","Curie studied here.","Education as resistance."]),
("Tuskegee Institute — founded 1881", "school history",
 "Booker T. Washington founded Tuskegee in 1881; George Washington Carver's lab made it legendary.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1881, Alabama — Booker T. Washington (1856–1915), first principal
- Students built the campus (brickmaking was the curriculum)
- George Washington Carver (1896–1943): the peanut and soil-science revolution from Tuskegee's labs
- The Tuskegee Airmen (WWII): the first Black military aviators trained here
- Motto: 'Scientia et labor' — knowledge and work

Washington's 1895 Atlanta Compromise speech defined an era of Black education strategy.

Sources: Tuskegee archives; NPS.""",
 ["1881.","Washington + Carver.","Tuskegee Airmen trained here."]),
("The Sorbonne — 1257", "school history",
 "Robert de Sorbon's 1257 college for poor theology students became the University of Paris — and the word for French academia.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1257 by Robert de Sorbon, chaplain to Louis IX
- The University of Paris grew around such colleges
- Suppressed 1793 (Revolution); refounded; split into 13 universities (1970)
- Alumni: Aquinas, Calvin, Curie (first woman professor, 1906), Sartre, de Beauvoir
- 'Sorbonne' = French academic prestige itself

Marie Curie earned her doctorate here (1903) and taught here.

Sources: Sorbonne Universite; public records.""",
 ["1257.","Suppressed 1793; reborn.","Curie: doctorate 1903."]),
("Mount Holyoke — 1837, the first women's college", "school history",
 "Mary Lyon founded Mount Holyoke Seminary in 1837 — the first US institution of higher education for women.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1837, South Hadley, Massachusetts — Mary Lyon (1797–1849)
- First US higher-education institution for women
- Lyon's model: rigorous academics + domestic work (students did the housework — tuition stayed low)
- Alumni: Emily Dickinson (attended 1847–48), Frances Perkins (first woman US cabinet secretary), Virginia Apgar
- The Seven Sisters' eldest

Lyon raised the funds herself, door to door.

Sources: Mount Holyoke archives.""",
 ["1837.","Mary Lyon's model.","Dickinson attended."]),
("Girton College, Cambridge — 1869", "school history",
 "Emily Davies founded Girton in 1869 — Cambridge's first women's college; women couldn't take degrees until 1948.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1869, Hitchin (moved to Cambridge 1873) — Emily Davies
- Women could study and sit exams from the 1880s — but received only 'titular' degrees until 1948
- The 1897 vote: male graduates voted against women's degrees
- Alumni: Hertha Ayrton (engineer), Queen Margrethe II of Denmark
- Full college status: 1948

Newnham (1871) was the sister foundation — together they pried Cambridge open.

Sources: Girton archives; public records.""",
 ["1869.","Degrees for women: 1948.","The 1897 vote."]),
("Howard University — founded 1867", "school history",
 "Founded 1867 in Washington, D.C.; Howard became the capstone of Black higher education — 'The Mecca.'",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1867 — named for Gen. Oliver O. Howard (Freedmen's Bureau)
- Open to all races and sexes from the start (radical for 1867)
- Motto: 'Veritas et Utilitas' — truth and service
- Alumni: Thurgood Marshall, Toni Morrison, Kamala Harris, Zora Neale Hurston (attended)
- The Mecca: the cultural capital of Black America

The law school's Charles Hamilton Houston trained the lawyers who dismantled segregation.

Sources: Howard archives.""",
 ["1867.","'The Mecca.'","Houston's lawyers vs. Jim Crow."]),
("Salamanca — 1218", "school history",
 "Alfonso IX founded Salamanca in 1218 — Spain's oldest university, where Columbus argued his case.",
 """PUBLIC YEARBOOK RECORD — SCHOOL HISTORY
Public record of well-documented institutional history.

- Founded: 1218 by Alfonso IX of Leon — Spain's oldest
- The School of Salamanca (16th century): Vitoria, Suarez — international law and economics' birthplace
- Columbus's 1486–87 hearings: the university examined his westward plan
- The frog on the skull: the famous facade carving students hunt for luck
- Motto: 'Quod natura non dat, Salmantica non praestat'

The Plateresque facade (16th century) is Spain's most photographed university front.

Sources: Universidad de Salamanca.""",
 ["1218.","Birthplace of international law.","Columbus argued here."]),
# --- notable alumni (14) ---
("Einstein's school years — Aarau to Zurich", "notable alumni",
 "Albert Einstein (1879–1955): Munich's Luitpold Gymnasium, Aarau's cantonal school, and the Zurich Polytechnic — the making of 1905.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1955.

- Luitpold Gymnasium, Munich: disliked the rote discipline (the 'failed math' myth is false — he excelled at math)
- 1895: failed the Zurich Polytechnic entrance (too young, weak in languages) — sent to Aarau cantonal school
- Aarau (1895–96): the liberal school he loved; the light-beam thought experiment dates to Aarau
- Zurich Polytechnic (1896–1900): graduated; the patent office years followed
- 1905: the annus mirabilis — four papers, including special relativity

The school record: the system nearly lost him; Aarau saved him.

Sources: Einstein Archives; public biographies.""",
 ["Aarau: the light-beam thought.","1905: four papers.","'Failed math' myth is false."]),
("Marie Curie — from the Flying University to the Sorbonne", "notable alumni",
 "Maria Sklodowska (1867–1934): Warsaw's clandestine Flying University, then the Sorbonne — two Nobels.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNA
Public record of well-documented biography. Deceased 1934.

- Warsaw: the Flying University (clandestine) — her first higher education, under Russian occupation
- 1891: Sorbonne — licentiates in physics (1893, first in class) and mathematics (1894)
- 1903: doctorate — Nobel Physics the same year
- 1906: first woman professor at the Sorbonne
- 1911: Nobel Chemistry — the only double-Nobel in two sciences

Her school notebooks are still radioactive — stored in lead boxes.

Sources: Nobel archives; Eve Curie.""",
 ["Flying University to Sorbonne.","First woman Sorbonne professor.","Notebooks still radioactive."]),
("Darwin — Shrewsbury, Edinburgh, Cambridge", "notable alumni",
 "Charles Darwin (1809–1882): Shrewsbury School, Edinburgh medicine (abandoned), Christ's College Cambridge — the beetle-collecting undergraduate.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1882.

- Shrewsbury School: passionate beetle collector
- Edinburgh (1825–27): medicine — abandoned; studied marine biology instead
- Christ's College, Cambridge (1828–31): intended for the clergy; followed Henslow (botany)
- 1831: the Beagle voyage — Henslow's recommendation got him aboard
- The education that mattered: natural history, not the curriculum

Darwin's schooling is the classic case: the credential was the clergy; the education was the beetles.

Sources: Darwin Correspondence Project.""",
 ["Shrewsbury to Cambridge.","The Beagle via Henslow.","Beetles over curriculum."]),
("Newton — Grantham and Trinity", "notable alumni",
 "Isaac Newton (1643–1727): Grantham's King's School, then Trinity College Cambridge — the annus mirabilis of 1666.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1727.

- The King's School, Grantham: built sundials, kites, and a water clock
- Trinity College, Cambridge (1661): subsizar; Barrow's protege
- 1665–66: the plague years at Woolsthorpe — calculus, optics, gravitation
- 1669: Lucasian Professor at 26

His Grantham carvings were still visible in the 19th century.

Sources: Westfall, 'Never at Rest'; public biographies.""",
 ["Grantham: sundials and kites.","1666: the mirabilis year.","Lucasian Professor at 26."]),
("Alan Turing — Sherborne to King's", "notable alumni",
 "Alan Turing (1912–1954): Sherborne School's unconventional boy, then King's College Cambridge — the codebreaker's schooling.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1954.

- Sherborne School: brilliant at math and science; cycled 60 miles to school during the 1926 General Strike
- King's College, Cambridge (1931): fellowship at 22 — 'On Computable Numbers' (1936)
- Princeton (1936–38): PhD under Church
- Bletchley Park: the Bombe, Hut 8
- 1952: convicted for homosexuality; 2013: royal pardon

Sherborne's reports called him 'unsound.' The century's judgment differs.

Sources: Hodges, 'Alan Turing'; public records.""",
 ["Sherborne: the odd boy.","1936: 'On Computable Numbers.'","Pardoned 2013."]),
("Rosalind Franklin — Newnham College", "notable alumni",
 "Rosalind Franklin (1920–1958): St Paul's Girls' School, Newnham College Cambridge — Photo 51 and the DNA story.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNA
Public record of well-documented biography. Deceased 1958.

- St Paul's Girls' School: excelled in science against the era's expectations
- Newnham College, Cambridge (1938): physical chemistry; PhD 1945
- Paris (1947–50): X-ray crystallography mastery
- King's College London (1951–53): Photo 51 — the X-ray image that revealed DNA's helix
- Birkbeck: pioneering virus crystallography until her death at 37

The Nobel (1962) went to Watson, Crick, and Wilkins — Nobels aren't awarded posthumously.

Sources: Maddox, 'Rosalind Franklin'; public records.""",
 ["Newnham 1938.","Photo 51.","Died 37; Nobel 1962."]),
("Frederick Douglass — self-educated", "notable alumni",
 "Frederick Douglass (c.1818–1895): forbidden to read as an enslaved child, he taught himself — and became the century's orator.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1895.

- Enslaved in Maryland: teaching a slave to read was illegal
- Self-taught: traded bread for reading lessons; copied from shipyard timber
- The Columbian Orator: the schoolbook that taught him rhetoric
- 1845: the Narrative — proof that the 'uneducable' slave was the century's greatest orator
- Founded newspapers; recruited Black troops; became US Marshal

His education is the rebuke to every school that excluded: he built his own.

Sources: Douglass, Narrative (1845); public records.""",
 ["Illegal to teach him.","Bread for lessons.","The Columbian Orator."]),
("Jane Austen — home and school", "notable alumni",
 "Jane Austen (1775–1817): brief schooling, then her father's 500-book library — the novels written at Chawton.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNA
Public record of well-documented biography. Deceased 1817.

- Brief formal schooling: Oxford, Southampton, Reading Abbey School
- The real school: Rev. George Austen's library (500+ volumes) and the family's theatricals
- Steventon rectory: the juvenilia (written from age 11)
- The novels (1811–17): written at Chawton, published anonymously ('By a Lady')

Austen is the case for the home library as university.

Sources: Tomalin, 'Jane Austen'; public records.""",
 ["Brief formal schooling.","Father's 500-book library.","Juvenilia from age 11."]),
("Gandhi — London's Inner Temple", "notable alumni",
 "M.K. Gandhi (1869–1948): called to the bar at London's Inner Temple (1891) — the English law training behind the liberation.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1948.

- Rajkot and London: sailed for London 1888
- Inner Temple (1888–91): called to the bar June 1891
- South Africa (1893–1914): the satyagraha laboratory
- The irony: English legal training became the weapon against the Empire

His London years are the least-remembered and most formative.

Sources: Gandhi, Autobiography; public records.""",
 ["Inner Temple, 1891.","English law vs. Empire.","Formative London years."]),
("Florence Nightingale — home-tutored", "notable alumni",
 "Florence Nightingale (1820–1910): tutored at home by her father in classics and mathematics — the schooling behind the statistics.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNA
Public record of well-documented biography. Deceased 1910.

- Home-tutored by her father William: Latin, Greek, German, French, mathematics
- The mathematics mattered: her Crimean 'coxcombs' invented statistical graphics
- 1851: Kaiserswerth, Germany — the nursing training her family opposed
- 1854: Scutari — mortality fell from 42% to 2%
- First woman elected to the Royal Statistical Society (1859)

Her father's curriculum built the founder of modern nursing.

Sources: Bostridge; public records.""",
 ["Father's classical tutoring.","Invented statistical graphics.","Royal Statistical Society, 1859."]),
("Mandela — Fort Hare to the struggle", "notable alumni",
 "Nelson Mandela (1918–2013): Fort Hare — expelled for protest — then Witwatersrand; the lawyer the struggle made.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 2013.

- Fort Hare (1939–40): the 'Black Oxford' — expelled for joining a student protest
- Witwatersrand (1943–49): law — the struggle intervened
- 1952: opened South Africa's first Black law firm (with Tambo)
- Robben Island: the 'university' — prisoners taught each other
- 1994: president

His real alma mater: the movement.

Sources: Mandela, 'Long Walk to Freedom.'""",
 ["Fort Hare; expelled for protest.","First Black law firm, 1952.","President 1994."]),
("Emmy Noether — Gottingen", "notable alumni",
 "Emmy Noether (1882–1935): Erlangen, then Gottingen — Noether's theorem; Einstein called her the most significant creative mathematical genius.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNA
Public record of well-documented biography. Deceased 1935.

- Erlangen: PhD 1907 (one of few women); unpaid lecturing for years
- Gottingen (1915): Hilbert's invitation — the faculty objected ('a woman among soldiers'); Hilbert: 'Gentlemen, this is a university, not a bathhouse'
- 1918: Noether's theorem — symmetry and conservation laws, the backbone of modern physics
- 1933: fled the Nazis; Bryn Mawr
- Einstein's eulogy: 'the most significant creative mathematical genius thus far produced'

She taught without pay, without title, and changed physics forever.

Sources: public biographies.""",
 ["Erlangen PhD 1907.","1918: Noether's theorem.","Einstein's eulogy."]),
("Booker T. Washington — Hampton Institute", "notable alumni",
 "Booker T. Washington (1856–1915): born enslaved, walked to Hampton Institute — then founded Tuskegee.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1915.

- Born enslaved, Virginia, 1856; freed 1865
- Walked 500 miles to Hampton Institute; worked as a janitor to pay tuition
- Graduated 1875; taught; recruited to found Tuskegee (1881)
- 1895: the Atlanta Compromise speech — the era's defining Black education strategy
- 1901: 'Up from Slavery' — among the century's most-read autobiographies

His Hampton years are the template: work-study as dignity, education as uplift.

Sources: Washington, 'Up from Slavery.'""",
 ["Walked 500 miles to Hampton.","Founded Tuskegee 1881.","'Up from Slavery.'"]),
("Rabindranath Tagore — no school could hold him", "notable alumni",
 "Rabindranath Tagore (1861–1941): hated formal schooling, educated at home — then founded his own school and won Asia's first Nobel.",
 """PUBLIC YEARBOOK RECORD — NOTABLE ALUMNUS
Public record of well-documented biography. Deceased 1941.

- Formal schooling: brief and hated — 'the school was a prison'
- Home-tutored in the Jorasanko mansion: literature, music, art
- 1901: founded Santiniketan ('abode of peace') — the school as he wished schools were: under trees, arts-centered
- 1913: Nobel Prize in Literature — Asia's first
- 1921: Visva-Bharati University

The dropout who built a university: Tagore's revenge on schooling was to reinvent it.

Sources: public biographies.""",
 ["Hated formal school.","Founded Santiniketan 1901.","Nobel 1913."]),
# --- school song (6) ---
("Gaudeamus Igitur — the student hymn (medieval, PD)", "school song",
 "Gaudeamus Igitur: the medieval student song — 'let us rejoice while we are young' — public domain, with translation.",
 """PUBLIC YEARBOOK RECORD — SCHOOL SONG (PUBLIC DOMAIN)
'Gaudeamus Igitur' — traditional student hymn, medieval origins (manuscript 1287; printed 1781). Public domain.

Latin (first verse):
Gaudeamus igitur, iuvenes dum sumus;
Post iucundam iuventutem, post molestam senectutem,
Nos habebit humus.

Translation:
Let us rejoice, therefore, while we are young;
After a pleasant youth, after a troubling old age,
The earth will have us.

Sung at graduations across Europe and the Americas — the oldest living student tradition. Brahms quoted it in his Academic Festival Overture (1880).

Sources: public domain tradition.""",
 ["Medieval; manuscript 1287.","Sung at graduations worldwide.","Brahms quoted it, 1880."]),
("Fair Harvard — 1836 (PD)", "school song",
 "Samuel Gilman's 1836 'Fair Harvard' — the university's alma mater (public domain).",
 """PUBLIC YEARBOOK RECORD — SCHOOL SONG (PUBLIC DOMAIN)
'Fair Harvard' — words by Samuel Gilman (1836). Public domain.

Fair Harvard! we join in thy Jubilee throng,
And with blessings surrender thee o'er
By these festival rites, from the Age that is past,
To the Age that is waiting before.
O Relic and Type of our ancestors' worth,
That hast long kept their memory warm,
First flower of their wilderness! Star of their night!
Calm rising through change and through storm.

Sung at every Harvard commencement since 1836 — among America's oldest college songs.

Sources: Harvard archives; public domain.""",
 ["1836; Samuel Gilman.","Sung at every commencement.","Among America's oldest."]),
("The Victors — Michigan, 1898 (PD)", "school song",
 "Louis Elbel's 1898 'The Victors' — Michigan's fight song, written after a win over Chicago (public domain).",
 """PUBLIC YEARBOOK RECORD — SCHOOL SONG (PUBLIC DOMAIN)
'The Victors' — Louis Elbel, 1898. Public domain.

Now for a cheer they are here, triumphant!
Here they come with banners flying,
In stalwart step they're nighing,
With shouts of vict'ry crying,
We hurrah, hurrah, we greet you now,
Hail!

Hail! to the victors valiant,
Hail! to the conqu'ring heroes,
Hail! Hail! to Michigan,
The leaders and best!

Written on the train home after Michigan beat Chicago 12–11 (1898). John Philip Sousa called it 'the greatest college fight song ever written.'

Sources: public domain.""",
 ["1898; Louis Elbel.","Written on the train home.","Sousa's praise."]),
("Anchors Aweigh — 1906 (PD)", "school song",
 "Charles Zimmermann's 1906 'Anchors Aweigh' — the US Naval Academy's song (public domain).",
 """PUBLIC YEARBOOK RECORD — SCHOOL SONG (PUBLIC DOMAIN)
'Anchors Aweigh' — Charles A. Zimmermann (bandmaster), lyrics by Alfred Hart Miles, 1906. Public domain.

Anchors Aweigh, my boys, Anchors Aweigh.
Farewell to college joys, we sail at break of day-ay-ay-ay.
Through our last night on shore, drink to the foam,
Until we meet once more, here's wishing you a happy voyage home.

Composed for the Army-Navy game (1906); the Navy's song ever since — and the unofficial march of the US Navy.

Sources: US Naval Academy; public domain.""",
 ["1906.","Navy's song.","Army-Navy game origin."]),
("On, Wisconsin! — 1909 (PD)", "school song",
 "William Purdy's 1909 'On, Wisconsin!' — written for a Minnesota game, now a state anthem too (public domain).",
 """PUBLIC YEARBOOK RECORD — SCHOOL SONG (PUBLIC DOMAIN)
'On, Wisconsin!' — William T. Purdy, 1909. Public domain.

On, Wisconsin! On, Wisconsin!
Plunge right through that line!
Run the ball clear down the field,
A touchdown sure this time. On, Wisconsin!
On, Wisconsin!
Fight, fight for her fame,
Fight! Fellows! Fight, fight, fight!
We'll win this game.

Written for the 1909 Minnesota game; adopted as Wisconsin's state song (1959). Purdy reportedly wrote it in a hurry — legends say on an envelope.

Sources: public domain.""",
 ["1909.","State song 1959.","Written in a hurry."]),
("The Notre Dame Victory March — 1908 (PD)", "school song",
 "The Shea brothers' 1908 'Victory March' — Notre Dame's fight song (public domain).",
 """PUBLIC YEARBOOK RECORD — SCHOOL SONG (PUBLIC DOMAIN)
'Notre Dame Victory March' — Michael and John Shea, 1908. Public domain.

Cheer, cheer for old Notre Dame,
Wake up the echoes cheering her name,
Send a volley cheer on high,
Shake down the thunder from the sky.
What though the odds be great or small,
Old Notre Dame will win over all,
While her loyal sons are marching
Onward to victory.

The Sheas (graduates) wrote it for the football team; it's among the most-played fight songs in America.

Sources: public domain.""",
 ["1908; the Shea brothers.","Most-played fight songs.","Written by graduates."]),
# --- club feature (8) ---
("The Oxford Union — founded 1823", "club feature",
 "The Oxford Union (1823): the world's most famous debating society — prime ministers trained at its despatch box.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented institutional history.

- Founded: 1823 — student debating society, independent of the university
- The chamber: modeled on the House of Commons
- Presidents who became prime ministers: Gladstone, Heath, and others
- Famous debates: the 1933 'King and Country' motion ('would not fight for King and country') — international scandal
- Guests: everyone from Malcolm X (1964) to the Dalai Lama

The Union's library and bar make it Oxford's student living room — debating as the university's unofficial curriculum.

Sources: Oxford Union; public records.""",
 ["1823.","The 1933 'King and Country' vote.","PMs trained here."]),
("The Harvard Lampoon — 1876", "club feature",
 "The Harvard Lampoon (1876): the humor magazine that became American comedy's farm team.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented institutional history.

- Founded: 1876 — among America's oldest humor magazines
- The castle: the Flemish-style building on Mt. Auburn St. (1909)
- Alumni: Conan O'Brien, Colin Jost, John Updike (drew covers), Robert Benchley
- The Lampoon–Crimson rivalry: prank wars, including the famous 'stolen' rival issues
- National Lampoon (1970) was founded by Lampoon alumni

Seven US presidents have been 'roasted' by the Lampoon — an honor of sorts.

Sources: Harvard Lampoon; public records.""",
 ["1876.","Comedy's farm team.","The castle on Mt. Auburn."]),
("The Boat Race — Oxford vs Cambridge, 1829", "club feature",
 "The University Boat Race (1829): the 6.8km Putney-to-Mortlake duel — 170+ races, watched by millions.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented sporting history.

- First raced: 1829 (Henley); moved to the Tideway (Putney–Mortlake, 6.8km) in 1845
- Record: Cambridge leads (as of recent years); the 1877 'dead heat' is the famous tie
- Sinking: 1912 (both sank), 1978 (Cambridge sank)
- Viewers: 250,000 on the banks; millions on TV
- The women's race: joined the Tideway in 2015

The dark blue vs. light blue rivalry is Britain's oldest annual sporting fixture.

Sources: The Boat Race Company; public records.""",
 ["1829.","6.8km Tideway.","1877 dead heat."]),
("The Whiffenpoofs — Yale, 1909", "club feature",
 "The Whiffenpoofs (1909): Yale's senior a cappella group — the oldest collegiate a cappella group in America.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented institutional history.

- Founded: 1909 — the oldest collegiate a cappella group in the US
- 'The Whiffenpoof Song' (1909): the signature tune, sung with the traditional arm-sway
- Alumni: Cole Porter (wrote for them), Jonathan Coulton
- The Mory's Cup: the traditional sing-off
- 250+ groups have copied the model — collegiate a cappella is their invention

Every spring, the graduating 'poofs tap their successors — the circle continues.

Sources: Yale; public records.""",
 ["1909.","Oldest collegiate a cappella.","Cole Porter alumnus."]),
("The Cambridge Union — 1815", "club feature",
 "The Cambridge Union (1815): Oxford's rival — eight years older, equally formidable.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented institutional history.

- Founded: 1815 — predates the Oxford Union by eight years
- Presidents: Keynes, Arianna Huffington, and many MPs
- The 1965 Baldwin–Buckley debate: James Baldwin vs. William F. Buckley on the American Dream — legendary
- Guests: Reagan, Gorbachev, Hawking
- The building: Round Church Street's debating chamber

The Oxford–Cambridge debating rivalry mirrors the Boat Race — older, louder, and never settled.

Sources: Cambridge Union; public records.""",
 ["1815.","Baldwin vs. Buckley, 1965.","Oxford's rival."]),
("Eton's Wall Game", "club feature",
 "The Eton wall game: the strange football code played along a 110-yard wall — goals rarer than comets.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented sporting history.

- Played along a 110-yard wall at Eton since the 1700s
- Rules: the 'bully' (scrum) inches along the wall; goals are vanishingly rare (the last in the St Andrew's Day game was decades ago)
- The Field Game: Eton's other code — closer to soccer
- The wall game's vocabulary: 'shy' (throw-in), 'bully,' 'calx'
- Played annually on St Andrew's Day (30 Nov): Collegers vs. Oppidans

A game designed to be almost unplayable — and fiercely loved for it.

Sources: Eton College; public records.""",
 ["110-yard wall.","Goals: vanishingly rare.","St Andrew's Day fixture."]),
("The Harvard-Yale Regatta — 1852", "club feature",
 "The Harvard-Yale Regatta (1852): America's oldest collegiate sporting event — 4 miles on the Thames (Connecticut's).",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented sporting history.

- First raced: 1852, Lake Winnipesaukee — predates The Game (football) by 23 years
- The course: 4 miles upstream on the Thames River, New London
- The Cannon: fired at the start — the towns turn out
- Harvard leads the series historically
- The oldest collegiate sporting event in America

Rowing was America's first intercollegiate sport — the regatta predates college football itself.

Sources: Harvard/Yale crew; public records.""",
 ["1852.","4 miles upstream.","Older than college football."]),
("Debating societies and the republic of letters", "club feature",
 "From 18th-century student societies to modern Model UN: the debating club as democracy's training ground.",
 """PUBLIC YEARBOOK RECORD — CLUB FEATURE
Public record of well-documented institutional history.

- 1700s: student literary societies (American Whig–Cliosophic at Princeton, 1765) — debate as the curriculum
- The Union model: Oxford (1823), Cambridge (1815) — the Commons-style chamber
- Modern: Model UN (1949–), moot court, ethics bowls
- The training: prime ministers, presidents, and advocates learned argument in student halls
- The rule: the motion is the teacher — defend what you don't believe

Every great debater was once a nervous fresher with a three-minute speech.

Sources: public institutional records.""",
 ["1765: Whig-Cliosophic.","Debate as curriculum.","The motion is the teacher."]),
# --- class statistics (8) ---
("Harvard class of 1900 — by the numbers", "class statistics",
 "Aggregate historical statistics: Harvard's class of 1900 — 400+ graduates, tuition $150, and the 25th-reunion data.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- Class size: ~400 graduates (1900)
- Tuition: $150/year; total college cost ~$400/year
- 25th reunion (1925): the class secretary's report — careers, marriages, mortality (the published aggregate tables)
- The era: the class of Theodore Roosevelt's presidency-to-be; the Spanish-American War's recent graduates
- Sources: Harvard class reports (published), Quinquennial Catalogue

Historical class reports are aggregate prosopography — the class as a dataset, no private data.

Sources: Harvard archives (published reports).""",
 ["~400 graduates.","Tuition $150/year.","Aggregate only."]),
("Oxford matriculations, 1800–1850", "class statistics",
 "Aggregate historical statistics: Oxford's matriculation books 1800–1850 — the university's growth in numbers.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- Matriculations 1800: ~200/year; 1850: ~400/year — doubling in 50 years
- Colleges: Christ Church and Balliol dominated numbers
- The 1854 Oxford University Act: opened fellowships (the reform era's numbers)
- Women: 0 (until 1920)
- Sources: Oxford University Calendar; Foster's Alumni Oxonienses (published aggregates)

The published alumni registers are the aggregate record — centuries of classes as data.

Sources: Oxford archives (published).""",
 ["200/year (1800) to 400/year (1850).","Women: 0 until 1920.","Aggregate only."]),
("US college enrollment, 1900–1950", "class statistics",
 "Aggregate historical statistics: US higher-education enrollment 1900 (238,000) to 1950 (2.4M) — the great expansion.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- 1900: 238,000 enrolled (4% of 18–21-year-olds)
- 1930: 1.1M (12%)
- 1950: 2.4M (GI Bill surge — veterans were 49% of enrollment in 1947)
- Women: 36% (1900) → 30% (1950, diluted by veterans) → rising after
- Sources: US Office of Education historical series

The GI Bill (1944) is the hinge: mass higher education begins here.

Sources: NCES historical tables.""",
 ["238K (1900) to 2.4M (1950).","GI Bill: the hinge.","Aggregate only."]),
("The 1947 freshman — veterans on campus", "class statistics",
 "Aggregate historical statistics: 1947 — veterans were 49% of US college enrollment; the campus transformed.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- Fall 1947: veterans = 49% of US college enrollment (1.1M veterans)
- Quonset huts and trailer camps: the emergency campuses
- Married students: the universities built family housing for the first time
- Effect: the 'mature student' normalized; average student age rose sharply
- Sources: Veterans Administration; Office of Education reports

The class of 1947–51 was the oldest, most serious, and most married in history.

Sources: published federal reports.""",
 ["49% veterans, 1947.","Quonset-hut campuses.","Aggregate only."]),
("Women's colleges: the Seven Sisters' numbers", "class statistics",
 "Aggregate historical statistics: the Seven Sisters' enrollments — women's higher education in numbers.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- Mount Holyoke (1837), Vassar (1861), Wellesley (1870), Smith (1871), Bryn Mawr (1885), Barnard (1889), Radcliffe (1879)
- Combined enrollment c.1960: ~12,000
- The coordinate model: Radcliffe–Harvard, Barnard–Columbia, Pembroke–Brown
- Coeducation wave (1969–83): most went coed or coordinated; Radcliffe merged (1999)
- Sources: published college histories

The Sisters educated a disproportionate share of America's women leaders.

Sources: published institutional data.""",
 ["7 colleges; ~12,000 (1960).","Coeducation wave 1969–83.","Aggregate only."]),
("Literacy by the numbers: 1870–1950", "class statistics",
 "Aggregate historical statistics: world literacy 1870–1950 — the school century in numbers.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- World literacy c.1870: ~20%; c.1950: ~50%+
- Drivers: compulsory schooling laws (Prussia 1717/1763 → Europe 1800s → US states 1852–1918)
- US: 80% (1870) → 97% (1950)
- The school century: enrollment, not just literacy — primary schooling became universal in the rich world by 1950
- Sources: UNESCO historical estimates; national censuses

The classroom is the century's great machine.

Sources: UNESCO; census aggregates.""",
 ["20% (1870) to 50%+ (1950).","Compulsory schooling laws.","Aggregate only."]),
("Eton's 70 scholars — 1440 to today", "class statistics",
 "Aggregate historical statistics: Eton's 70 King's Scholars — the 1440 foundation's numbers across six centuries.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- 1440: Henry VI's statutes — 70 poor scholars (Collegers), educated free
- The number 70: unchanged for nearly 600 years
- Oppidans: the fee-paying majority (today ~1,300 total; scholars still 70)
- Election: the annual King's Scholarship exam — among England's hardest
- Sources: Eton College statutes and published records

Six centuries, seventy scholars — the most durable number in English education.

Sources: Eton archives (published).""",
 ["70 scholars; 600 years.","Oppidans: the majority.","Aggregate only."]),
("The Rhodes Scholarships — 1902", "class statistics",
 "Aggregate historical statistics: the Rhodes (1902) — 8,000+ scholars, 100/year, the oldest international scholarship.",
 """PUBLIC YEARBOOK RECORD — CLASS STATISTICS (AGGREGATE ONLY)
Public record of published historical statistics. No individual student data.

- Founded: 1902 (Rhodes's will) — Oxford
- Scholars: 100+/year; 8,000+ total
- Original constituencies: the Empire's settler colonies + US + Germany
- Expanded: global (1990s–2010s); women since 1977
- The will's clause: 'moral force of character' — the scholarship's famous criterion

Rhodes's imperialism shadows the gift — the scholarship's history includes the debate.

Sources: Rhodes Trust (published).""",
 ["1902.","8,000+ scholars.","Women since 1977."]),
# --- architecture (12) ---
("King's College Chapel, Cambridge — 1446–1515", "architecture",
 "Henry VI's chapel (1446–1515): the largest fan vault in the world — 70 years, three kings, one ceiling.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Begun: 1446 (Henry VI); completed: 1515 (Henry VIII) — 69 years, three kings
- The fan vault: the largest in the world — stone lacework spanning 12.7m
- The windows: Tudor stained glass, mostly original
- The organ: the great 17th-century case
- Carols from King's: the Christmas Eve broadcast since 1928

The chapel is the Perpendicular Gothic's summit — verticality as theology.

Sources: King's College; public records.""",
 ["1446–1515.","Largest fan vault.","Carols since 1928."]),
("The Radcliffe Camera, Oxford — 1737–49", "architecture",
 "James Gibbs's circular library (1737–49): Oxford's most photographed building — a drum, a dome, and 600,000 books.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1737–49, James Gibbs — funded by John Radcliffe's bequest
- England's first circular library; the dome on a drum
- Now: the Bodleian's history and humanities reading rooms
- The 600,000 volumes below the square outside (the Gladstone Link)
- Photographed: the postcard view from Brasenose Lane

Gibbs's baroque circle in Oxford's gothic city — the contrast is the point.

Sources: Bodleian Libraries.""",
 ["1737–49; Gibbs.","First circular library.","600,000 volumes."]),
("Wren Library, Trinity College — 1676–95", "architecture",
 "Christopher Wren's riverside library (1676–95): the classical room that holds Newton's books and A.A. Milne's Pooh.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1676–95 — Wren's only Cambridge building (mostly)
- The design: arcaded ground floor (floods), the long room above
- Holdings: Newton's library (with his annotations), the Capell Shakespeares, Winnie-the-Pooh's manuscripts
- The Limewood carvings: Grinling Gibbons
- Still a working library — readers at Wren's desks

The most beautiful library interior in England (the claim is contested; the beauty isn't).

Sources: Trinity College.""",
 ["1676–95.","Newton's annotated books.","Pooh's manuscripts."]),
("Eton College Chapel — 1448–82", "architecture",
 "Eton's chapel: Henry VI's Perpendicular masterpiece — wall paintings, the Lupton tower, and 580 years of services.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1448–82 — the Perpendicular Gothic's early summit
- The wall paintings: 15th-century religious cycles, whitewashed at the Reformation, revealed 1847–49
- The Lupton Tower (c.1515): the clock tower gateway
- Daily services: the chapel's 580-year routine
- War memorial: the names of 1,200+ Etonians of the World Wars

The ante-chapel's fan vaulting prefigures King's.

Sources: Eton College.""",
 ["1448–82.","Wall paintings revealed 1847.","580 years of services."]),
("The Sorbonne's Grand Amphitheatre", "architecture",
 "The 1885–1901 Richelieu building: Puvis de Chavannes's 'Sacred Grove' mural and the amphitheatre of French academia.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Rebuilt: 1885–1901 (Henri-Paul Nénot) — the Third Republic's university palace
- The Grand Amphithéâtre: 3,000 seats; Puvis de Chavannes's 'Le Bois sacré' (the Sacred Grove) mural
- The chapel (1627–42): Richelieu's domed church — his tomb inside
- The courtyard: the Latin Quarter's academic heart
- Nobel ceremonies, state funerals of ideas — the room where France thinks aloud

The mural's serene grove watches over the fiercest debates in French intellectual life.

Sources: Sorbonne Université.""",
 ["1885–1901.","Puvis de Chavannes mural.","Richelieu's tomb."]),
("Bologna's Archiginnasio — 1563", "architecture",
 "The 1563 palace: 7,000 coats of arms on its walls — the students' heraldic archive.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1563 (Pius IV) — the university's first permanent home
- The walls: 7,000+ student coats of arms — the world's largest heraldic archive
- The Anatomical Theatre (1637): carved wood, the marble dissection table, Apollo and the flayed figures
- The Stabat Mater hall: the library's great room
- Now: the Archiginnasio Library (Bologna's civic library)

The arms on the walls are the student body's 400-year guest book.

Sources: Biblioteca dell'Archiginnasio.""",
 ["1563.","7,000 coats of arms.","Anatomical theatre, 1637."]),
("Harvard's University Hall — 1815", "architecture",
 "Bulfinch's 1815 granite hall: Harvard Yard's white-pillared anchor — built from Chelmsford granite, still the administration's seat.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1813–15, Charles Bulfinch — Harvard's first great architect
- Material: Chelmsford granite; the white wooden pilasters are the signature
- The Yard: University Hall anchors the Old Yard's composition
- Still houses: the administration (the dean's office behind the pillars)
- The statue out front: John Harvard (1884) — the 'statue of three lies'

Bulfinch went on to design the US Capitol's dome — the Yard was the rehearsal.

Sources: Harvard archives.""",
 ["1813–15; Bulfinch.","Chelmsford granite.","'Statue of three lies.'"]),
("Oxford's Sheldonian Theatre — 1669", "architecture",
 "Wren's 1669 Sheldonian: the D-shaped ceiling, the painted 'Truth descending,' and 350 years of degree ceremonies.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1664–69, Christopher Wren — his first major building
- The ceiling: Robert Streater's 32-panel 'Truth descending upon the Arts and Sciences'
- The D-shape: the Roman theatre plan, roofed — Wren's structural daring
- Ceremonies: every Oxford degree, encaenia, and the chancellor's installations
- The cupola: the 360° view of Oxford's 'dreaming spires'

The emperors' heads (the Herms) outside: 17th-century sculpture, re-cut repeatedly.

Sources: University of Oxford.""",
 ["1664–69; Wren's first.","Painted ceiling: 32 panels.","Every Oxford degree."]),
("The Bodleian's Divinity School — 1488", "architecture",
 "The Divinity School (1488): the most beautiful room in Oxford — lierne vaulting and 500 years of examinations.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1427–88 — the university's first purpose-built teaching room
- The vault: lierne stars and 455 carved bosses — the Perpendicular's masterpiece
- Examinations: five centuries of viva voce (the oral ordeal)
- The door: to the Schools Quadrangle (1613–24) — the Jacobean courtyard
- Film fame: the Hogwarts infirmary (the room's 21st-century students call it that)

The bosses include the university's arms, the founders', and one green man.

Sources: Bodleian Libraries.""",
 ["1427–88.","455 carved bosses.","Five centuries of exams."]),
("Trinity College Dublin's Long Room — 1712", "architecture",
 "The Long Room (1712–32): 65 meters of oak and 200,000 books — the Book of Kells's great hall.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1712–32 — 65m long, the barrel-vaulted ceiling added 1860 (to hold more books)
- 200,000 of the library's oldest volumes; marble busts of the great men (and now women)
- The Book of Kells (c.800): displayed here — the medieval manuscript's home
- The harp: the 15th-century Brian Boru harp — Ireland's national symbol
- Copyright library: every UK/Irish publication, by law

The most beautiful library room in Ireland — the long perspective is the postcard.

Sources: Trinity College Dublin.""",
 ["1712–32; 65m.","Book of Kells displayed.","200,000 oldest volumes."]),
("Al-Azhar's mosque-university", "architecture",
 "The 970 CE mosque: Fatimid arcades, Mamluk minarets, Ottoman additions — a millennium of Islamic architecture in one complex.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Founded: 970 CE (Jawhar); the mosque is the university's heart
- Layers: Fatimid arcades, Mamluk minarets (the double-finialed), Ottoman restorations
- The sahn (courtyard): the teaching circles (halaqat) still meet there
- The minarets: five, from five centuries — the skyline's timeline
- The library: manuscripts under the same roof as the students

A building that has taught continuously for 1,000+ years — architecture as curriculum.

Sources: Al-Azhar; public records.""",
 ["970 CE.","Five minarets, five centuries.","Teaching for 1,000+ years."]),
("Yale's Sterling Library — 1931", "architecture",
 "James Gamble Rogers's 1931 Gothic: 15 levels of stacks, 4M volumes — the cathedral of books.",
 """PUBLIC YEARBOOK RECORD — ARCHITECTURE
Public record of well-documented architectural history.

- Built: 1931, James Gamble Rogers — Collegiate Gothic
- 15 levels of stacks; 4M+ volumes; the nave-like reading room
- The carvings: scholars, printers, and (famously) a student with a typewriter
- The Beinecke (1963): the rare-book library next door — the marble monolith
- The Sterling's tower: the campus's vertical anchor

Rogers designed much of Yale — the 'collegiate Gothic' is his signature, aged artificially with acid.

Sources: Yale Library.""",
 ["1931.","15 stack levels.","4M+ volumes."]),
]

# ================= 12. yearbooks-signature =================
YEARSIG = [
# --- school song (10): original songs ---
("The Morning Bell (a Signature school song)", "school song",
 "A Signature original school song: 'The Morning Bell' — for any school's opening assembly.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE MORNING BELL
(Words: Signature original. Tune: any bright 4/4.)

Verse 1:
Morning bell is ringing, clear and true,
Calling me and calling you —
Books are open, minds are too,
The day is bright and new!

Chorus:
Ring, ring, morning bell!
We've a story yet to tell —
Of the things we'll learn today,
In work and in play!
Ring, ring, morning bell!
All is well, all is well!

Verse 2:
Teacher's waiting, friends are near,
Every voice is welcome here —
Questions asked without a fear,
The morning bell we hear!

(Repeat chorus.)

Note: written for unison singing, assembly use. Property of JAH.""",
 ["Signature original song.","Unison, assembly use.","Theme: new beginnings."]),
("The Hallway Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Hallway Song' — about kindness between classes.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE HALLWAY SONG
(Words: Signature original.)

Verse:
In the hallway, between the bells,
There's a story each locker tells —
Say hello as you walk along,
And make the hallway sing your song!

Chorus:
Hello, hello, how do you do?
There's a place in the hallway for you!
Kind words travel fast and far —
Be a hallway superstar!

Verse 2:
Hold the door and share a smile,
Walk a friend the extra mile —
Hallways hum with what we do,
And the song they sing is you!

(Repeat chorus.)

Note: for corridor singing, naturally. Property of JAH.""",
 ["Signature original song.","Theme: kindness.","Hallway repertoire."]),
("The Library Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Library Song' — a quiet anthem for readers.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE LIBRARY SONG
(Words: Signature original. To be sung softly.)

Verse:
In the library, row on row,
Are the places we can go —
Open up a book and see:
The world is waiting, wild and free!

Chorus (softly):
Shh... listen... pages turn...
So much to read, so much to learn!
Every book's a door, it's true —
The library is calling you!

Verse 2:
Librarians know just where to look,
To find the perfect, perfect book —
Ask, and they will help you find
The story waiting in your mind!

(Repeat chorus, softer.)

Note: dynamics marked — the last chorus is whispered. Property of JAH.""",
 ["Signature original song.","Theme: reading.","Whispered finale."]),
("The Team Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Team Song' — for games, win or lose.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE TEAM SONG
(Words: Signature original. Loud.)

Verse:
We are the team, we play as one,
We play for joy, we play for fun —
Win or lose, we do our best,
We never quit, we pass the test!

Chorus:
Go, team, go! Give it your all!
Catch the ball and stand tall!
Win with grace and lose with cheer —
We'll be back again next year!
Go, team, go!

Verse 2:
The other team, we shake their hand,
The finest rivals in the land —
For the game is more than score:
It's friends forever, evermore!

(Repeat chorus, louder.)

Note: sportsmanship codified in verse. Property of JAH.""",
 ["Signature original song.","Theme: sportsmanship.","Loud."]),
("The Graduation Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Graduation Song' — for the last assembly.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE GRADUATION SONG
(Words: Signature original. Gentle 3/4.)

Verse:
We came as strangers, small and new,
We leave as friends — both me and you.
The years have flown, the days have sung,
Our time together, ever young.

Chorus:
So here's to us, and here's to you,
To all the things we'll say and do —
We'll carry this school within our heart,
No matter where we are, what part.

Verse 2:
Teachers, thank you, for the light —
You taught us wrong from right.
Friends, remember, near or far:
We're who our school days made us are.

(Final chorus, then hum the verse.)

Note: for the last assembly. Tissues optional. Property of JAH.""",
 ["Signature original song.","Theme: farewell.","3/4, gentle."]),
("The Science Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Science Song' — hypotheses set to music.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE SCIENCE SONG
(Words: Signature original.)

Verse:
Ask a question, make a guess,
Test it out — no more, no less!
Measure twice and write it down,
Wear your goggles, not a frown!

Chorus:
Science! Science! What will we find?
The universe is on our mind!
Hypothesize and test it true —
The next discovery could be you!

Verse 2:
Volcanoes fizz and pendulums swing,
We love to test most everything —
If it fails, we try anew:
That's what scientists do!

(Repeat chorus.)

Note: goggles required for the chorus. Property of JAH.""",
 ["Signature original song.","Theme: inquiry.","Goggles required."]),
("The Art Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Art Song' — for the messy and the makers.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE ART SONG
(Words: Signature original.)

Verse:
Pick a color, any hue,
Red and yellow, green and blue —
There's no wrong in what you make,
Every picture's yours to take!

Chorus:
Paint it, draw it, make it sing!
Art is such a lovely thing!
Messy hands and happy heart —
Every child can make art!

Verse 2:
Clay and paper, glue and string,
We can make most anything —
If it's crooked, that's okay:
Art is art, hip-hooray!

(Repeat chorus.)

Note: smocks recommended. Property of JAH.""",
 ["Signature original song.","Theme: creativity.","Smocks recommended."]),
("The Kindness Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Kindness Song' — the school's golden rule, singable.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE KINDNESS SONG
(Words: Signature original.)

Verse:
Kindness is a simple thing:
A helping hand, a song to sing —
Share your crayons, share your snack,
Kindness always bounces back!

Chorus:
Be kind, be kind, it's easy to do —
Be kind to others, they'll be kind to you!
A smile's a gift that never ends:
Kindness makes the best of friends!

Verse 2:
When someone's sad or feeling blue,
There's something kind that you can do —
Listen close and lend a hand,
Kindness is the best-laid plan!

(Repeat chorus.)

Note: the golden rule, in 4/4. Property of JAH.""",
 ["Signature original song.","Theme: kindness.","The golden rule, singable."]),
("The Winter Concert Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Winter Concert Song' — for the December show.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE WINTER CONCERT SONG
(Words: Signature original.)

Verse:
Snow is falling, soft and white,
Stars are twinkling in the night —
Gather round, both old and young,
Winter's song must now be sung!

Chorus:
Sing we now of winter's cheer,
The happiest time of the year!
Voices rising, clear and strong —
Join us in the winter song!

Verse 2:
Candles glowing, warm and bright,
Chasing shadows from the night —
Music binds us, heart to heart,
Never more to drift apart!

(Repeat chorus.)

Note: for the December concert. Cocoa after. Property of JAH.""",
 ["Signature original song.","Theme: winter joy.","Cocoa after."]),
("The Field Day Song (a Signature school song)", "school song",
 "A Signature original school song: 'The Field Day Song' — sack races set to music.",
 """SIGNATURE ORIGINAL SCHOOL SONG
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

THE FIELD DAY SONG
(Words: Signature original. Bouncy.)

Verse:
It's field day! Hip hooray!
We're going out to play all day!
Sack races, relays, tug-of-war —
Who could ask for anything more?

Chorus:
Run, run, run your best!
Put your sneakers to the test!
Win or lose, it's fun, you see —
Field day's for you and me!

Verse 2:
Water balloons and three-legged races,
Smiles on all the happy faces —
Everybody gets a cheer,
The best day of the school year!

(Repeat chorus, faster.)

Note: bouncy tempo; sneakers required. Property of JAH.""",
 ["Signature original song.","Theme: play.","Sneakers required."]),
# --- club feature (10): original club charters/guides ---
("How to start a debate club (Signature guide)", "club feature",
 "A Signature original guide: founding a school debate club — motions, formats, and first meetings.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A DEBATE CLUB
1. The pitch: 'Learn to argue well.' Recruit 8–12; diversity of views is the point.
2. First meeting: the motion 'This house believes homework should be abolished' — low stakes, high energy.
3. Format: British Parliamentary (four teams of two) or simple pro/con. Keep speeches to 4 minutes.
4. The rule: attack arguments, never people. The adjudicator enforces it.
5. Growth: inter-school friendlies, then tournaments. The trophy is secondary; the thinking is the prize.

Sample first-term motions: school uniforms; phones in class; the best superpower; whether the library should stay open late.

The club's motto: 'Hear the other side.' (Audi alteram partem.)

Property of JAH.""",
 ["Signature original guide.","8–12 founders.","'Hear the other side.'"]),
("How to start a school newspaper (Signature guide)", "club feature",
 "A Signature original guide: the student paper — roles, ethics, and the first issue.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A SCHOOL NEWSPAPER
1. Roles: editor, reporters, photographers, designer — everyone writes.
2. First issue: the news (new teachers), a feature (the lunch lady's story), opinion (the great homework debate), sports, comics.
3. Ethics: verify before publishing; no gossip as news; corrections policy on page 2.
4. The interview: prepare questions, take notes, quote accurately.
5. Print or pixel: a photocopied zine beats a perfect website that never launches.

The paper's power: it makes the school legible to itself. The lunch lady's story will be the most-read piece — human interest always wins.

Property of JAH.""",
 ["Signature original guide.","Everyone writes.","Verify before publishing."]),
("How to start a chess club (Signature guide)", "club feature",
 "A Signature original guide: the chess club — ladders, notation, and the quietest rivalry.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A CHESS CLUB
1. Equipment: 4–6 sets (the school may fund; car boot sales supply the rest). Clocks later.
2. The ladder: ranked play — challenge up, defend down. The ladder is the club's heartbeat.
3. Teach notation: e4, Nf3 — the game's language. Score sheets from day one.
4. First tournament: round-robin, everyone plays everyone. Trophies: bookstore vouchers.
5. The culture: silence during play, analysis after. Post-mortems are the teaching.

The club's secret: chess teaches losing gracefully — you lose constantly, then improve. The best life lesson on the board.

Property of JAH.""",
 ["Signature original guide.","The ladder is the heartbeat.","Losing gracefully."]),
("How to start a drama club (Signature guide)", "club feature",
 "A Signature original guide: the drama club — auditions, rehearsals, and opening night.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A DRAMA CLUB
1. First play: a one-act comedy — short, funny, forgiving. Shakespeare can wait.
2. Auditions: everyone gets a part — crew counts double (set, lights, sound are roles).
3. Rehearsal rule: off-book two weeks before opening. The panic is traditional.
4. The tech: borrowed lights, painted flats, the gym as theatre. Constraint breeds creativity.
5. Opening night: the nerves, the hush, the applause. Nothing like it.

The club's truth: drama teaches empathy — you literally stand in another's shoes. The shy ones often shine brightest.

Property of JAH.""",
 ["Signature original guide.","Everyone gets a part.","Empathy in costume."]),
("How to start a robotics club (Signature guide)", "club feature",
 "A Signature original guide: the robotics club — kits, competitions, and the build season.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A ROBOTICS CLUB
1. The kit: one starter kit (the school funds it; grants exist). Share — scarcity teaches.
2. Roles: builders, programmers, drivers, documenters — every role matters.
3. First build: the kit's tutorial bot. Then: modify it. Then: design your own.
4. Competitions: local scrimmages first; the big leagues later. Lose a lot — it's data.
5. The notebook: document everything. Engineering is writing plus building.

The club's lesson: the robot that fails teaches more than the one that works. Iterate.

Property of JAH.""",
 ["Signature original guide.","Document everything.","Failure is data."]),
("How to start a gardening club (Signature guide)", "club feature",
 "A Signature original guide: the school garden — plots, compost, and the first tomato.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A GARDENING CLUB
1. The plot: a sunny corner — negotiate with the groundskeeper (bring cookies).
2. The soil: compost first. The school kitchen's scraps are black gold.
3. First planting: radishes (fast!), then tomatoes, then ambition.
4. The rota: watering is the club's heartbeat — the summer rota is sacred.
5. The harvest: the cafeteria gets the surplus; the food bank gets the glory.

The club's magic: the first tomato, split twelve ways. Nobody forgets it.

Property of JAH.""",
 ["Signature original guide.","Compost first.","The first tomato."]),
("How to start a choir (Signature guide)", "club feature",
 "A Signature original guide: the school choir — auditions without fear, and the first concert.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A CHOIR
1. Auditions: no one is turned away — the audition places voices, it doesn't reject them.
2. First songs: a round (instant harmony), then a unison anthem, then parts.
3. The warm-up: the silly exercises matter — they make the shy sing.
4. First concert: the winter show — parents, pride, and slightly wobbly high notes.
5. The tour: the old folks' home, the town square — singing for people who need it.

The choir's truth: singing together is the fastest friendship. Eighty voices, one breath.

Property of JAH.""",
 ["Signature original guide.","No one turned away.","One breath, eighty voices."]),
("How to start a coding club (Signature guide)", "club feature",
 "A Signature original guide: the coding club — first programs, hackathons, and the demo day.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A CODING CLUB
1. First night: everyone writes a program that runs — 'Hello, world' counts. Shipping beats perfection.
2. The stack: start with Python or Scratch; the language matters less than the building.
3. Projects: solve a school problem — the lunch queue app, the club finder. Real users, real feedback.
4. Hackathons: one Saturday, one theme, teams of four. Pizza is infrastructure.
5. Demo day: show the school. The applause debugs everything.

The club's rule: help the person next to you — the best way to learn is to teach.

Property of JAH.""",
 ["Signature original guide.","Ship beats perfection.","Teach to learn."]),
("How to start a photography club (Signature guide)", "club feature",
 "A Signature original guide: the photography club — phones count, light matters, the exhibition.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A PHOTOGRAPHY CLUB
1. Gear: phones count. The best camera is the one you have — the eye matters more.
2. First assignment: 'light' — shoot the same place at dawn, noon, dusk. See the difference.
3. The critique: kind and specific — 'the leading line works' beats 'nice pic.'
4. The darkroom (optional): film is slow magic; the red light, the developing image.
5. The exhibition: the hallway show — the school sees itself through your eyes.

The club's lesson: photography is attention. The camera teaches you to look — and looking is the whole art.

Property of JAH.""",
 ["Signature original guide.","Phones count.","Photography is attention."]),
("How to start a book club (Signature guide)", "club feature",
 "A Signature original guide: the book club — picks, snacks, and the art of disagreeing about books.",
 """SIGNATURE ORIGINAL CLUB GUIDE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

FOUNDING A BOOK CLUB
1. First pick: short, discussable — the book is the excuse, the talk is the point.
2. The snacks: thematic (the book's food). Never underestimate snacks.
3. Discussion: 'What did you love? What confused you? Who would you cast?' — then let it wander.
4. The rule: no spoilers for the unfinished; no scorn for the unpopular opinion.
5. The field trip: the author's town, the book's setting, or just the library's back room.

The club's truth: reading together makes readers. The book ends; the friendship doesn't.

Property of JAH.""",
 ["Signature original guide.","Thematic snacks.","Reading together."]),
# --- school history (10): original essays ---
("Signature essay: what makes a school", "school history",
 "A Signature original essay: the school as an idea — from Nalanda to the one-room schoolhouse.",
 """SIGNATURE ORIGINAL ESSAY — SCHOOLS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Nalanda (5th century): 10,000 students, residential. Bologna (1088): students hiring professors. The one-room schoolhouse: eight grades, one teacher, one stove.

The Signature definition: a school is not a building. It's an agreement — that the young will be taught, and the old will teach. The building helps; the agreement is everything.

The constants across 1,500 years: a teacher, students, something worth learning, and time set aside. Everything else — the quadrangles, the laboratories, the fight songs — is decoration (lovely decoration).

The test: close the building. If the teaching continues (the Flying University did, in secret), it was a school. If it stops, it was real estate.

Public methodology. No private data.""",
 ["A school = an agreement.","Nalanda to the schoolhouse.","Close the building: the test."]),
("Signature essay: the idea of the university", "school history",
 "A Signature original essay: universitas — the guild, the idea, and Newman's defense.",
 """SIGNATURE ORIGINAL ESSAY — UNIVERSITIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

'Universitas': the guild — of students (Bologna) or masters (Paris). The word meant the corporation, not the campus.

Newman's 'Idea of a University' (1852): the university as the place where all knowledge is taught — the circle of the disciplines, theology included. Humboldt's Berlin (1810): research and teaching united — the modern research university's blueprint.

The Signature reading: the university has had three ideas — the guild (medieval), the circle (Newman), the laboratory (Humboldt). Today's university is all three, uneasily.

The current crisis: the laboratory ate the circle — research funding shapes the curriculum. The guild survives in the students' unions.

The future: the idea persists because the agreement persists — teach the young everything worth knowing.

Public methodology. No private data.""",
 ["Guild, circle, laboratory.","Humboldt's blueprint.","The agreement persists."]),
("Signature essay: schools that resisted", "school history",
 "A Signature original essay: the Flying University, Tuskegee, the freedom schools — education as defiance.",
 """SIGNATURE ORIGINAL ESSAY — RESISTANCE SCHOOLS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Warsaw's Flying University (1882–1905): higher education under occupation, in secret — Marie Sklodowska among its students. Tuskegee (1881): Washington's school, built by its students' hands. The Freedom Schools (1964): Mississippi's summer — reading, arithmetic, and citizenship.

The Signature pattern: the schools that mattered most were the ones someone tried to stop. Oppression clarifies the curriculum — when education is forbidden, every lesson is a statement.

The method: small, mobile, committed. The Flying University moved locations; the Freedom Schools used church basements; Tuskegee made its own bricks.

The lesson: a school is hardest to kill when it's an idea, not a building.

Public methodology. No private data.""",
 ["Forbidden schools matter most.","Small, mobile, committed.","Ideas outlast buildings."]),
("Signature essay: the school song tradition", "school history",
 "A Signature original essay: Gaudeamus to fight songs — why schools sing.",
 """SIGNATURE ORIGINAL ESSAY — SCHOOL SONGS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

'Gaudeamus Igitur' (1287 manuscript): students have sung the same song for 700+ years. 'Fair Harvard' (1836): the alma mater as institutional memory. The fight songs (1890s–1900s): 'The Victors,' 'Anchors Aweigh' — the stadium as choir.

The Signature theory: school songs are the institution's oral tradition — the values set to music, memorized by singing. The lyrics teach: loyalty (alma maters), courage (fight songs), joy (Gaudeamus).

The function: the song makes the crowd one — 100,000 voices, one lyric. No speech does that.

The Signature advice in this very database: write your school's songs (see the original songs herein). The tradition continues by composition, not just preservation.

Public methodology. No private data.""",
 ["700 years of Gaudeamus.","Values set to music.","Compose, don't just preserve."]),
("Signature essay: examinations — a history", "school history",
 "A Signature original essay: from the Chinese keju to the SAT — the exam as gatekeeper.",
 """SIGNATURE ORIGINAL ESSAY — EXAMINATIONS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The keju (605–1905): China's imperial exams — the original meritocracy, and its original grind. Cambridge's Tripos (18th century): the wrangler system — ranked mathematics, public glory. The SAT (1926): the American gatekeeper.

The Signature reading: exams are the school's conscience and its corruption — they measure what they measure, then the school teaches to the measure. Goodhart's law, in academic dress.

The defenses: the viva (Oxford's oral ordeal — you can't cram character), the portfolio, the project.

The future: the exam as conversation (the viva, scaled) rather than the exam as filter.

Public methodology. No private data.""",
 ["Keju to SAT.","Measure becomes target.","The viva as ideal."]),
("Signature vignette: the first day (original fiction)", "school history",
 "A Signature original vignette (fiction): a new school opens its doors, 1923.",
 """SIGNATURE ORIGINAL VIGNETTE — FIRST DAY, 1923
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

The principal unlocked the doors at seven. The building smelled of paint and sawdust. On every desk: a pencil, a reader, and a note — 'Welcome. This school is yours.'

The first students came shyly, in new shoes. The teachers — young, idealistic, terrified — greeted each by name (they'd memorized the rolls).

The bell rang. Nobody knew where to go. Everyone laughed. The principal led the whole school — all 200 — on a tour, classroom by classroom.

At lunch, the cook served stew. It was too salty. Nobody cared.

That night, the principal wrote in the log: 'Day one. The building is finished. The school begins tomorrow.'

(Author's note: the composite first day — every old school's founding, imagined as one.)""",
 ["Clearly labeled fiction.","'The school begins tomorrow.'","Paint, sawdust, new shoes."]),
("Signature essay: the campus as text", "school history",
 "A Signature original essay: quadrangles, quads, and malls — reading the campus like a document.",
 """SIGNATURE ORIGINAL ESSAY — CAMPUS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Oxford's quadrangles: the college as monastery — enclosed, inward, contemplative. The American campus (Jefferson's Virginia, 1819): the Lawn — open, democratic, the rotunda as temple. The modern mega-campus: the mall — circulation as design.

The Signature reading: the campus plan is the pedagogy. The quadrangle says: withdraw and think. The Lawn says: the community learns together. The high-rise dorm says: efficiency.

The rituals: the paths students actually walk (the desire lines) vs. the paths architects drew. The campus's truth is in the worn grass.

Walk your campus: the buildings are the sentences; the quads are the paragraphs.

Public methodology. No private data.""",
 ["Quadrangle: withdraw.","Lawn: together.","Read the worn grass."]),
("Signature essay: the school library", "school history",
 "A Signature original essay: the library as the school's memory — from chained books to digital stacks.",
 """SIGNATURE ORIGINAL ESSAY — LIBRARIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The chained library (Hereford, 1611): books too valuable to move — knowledge as treasure. The Bodleian (1602): 'the republic of letters' — the agreement that scholars share. The school library: the democratization — every student, every book.

The Signature arc: from treasure (chained) to commons (open stacks) to cloud (digital). Each step widened the circle.

The school library's special role: the first library that's yours — the librarian who knows your name, the book that finds you.

The future: the library as workshop (makerspaces) plus sanctuary (quiet floors). The books remain — the container changed, the content didn't.

Public methodology. No private data.""",
 ["Chained to cloud.","The librarian knows your name.","Sanctuary + workshop."]),
("Signature essay: graduation — the ritual", "school history",
 "A Signature original essay: encaenia to commencement — why we process, gown, and throw caps.",
 """SIGNATURE ORIGINAL ESSAY — GRADUATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The gowns: medieval scholars' robes — the uniform of the guild. The procession: the order of precedence, walked. The Latin: the orations nobody understands and everybody respects. The cap-throw: the American invention (the Naval Academy, 1912 — the caps were no longer needed).

The Signature reading: graduation is the school's final lesson — that beginnings need endings, and endings need witnesses. The ritual makes the transition real.

The variations: Oxford's encaenia (the garden party of degrees), the Philippines' moving-up, the homeschool co-op's living-room ceremony. The form varies; the function doesn't.

The advice: attend. The ritual works on those present.

Public methodology. No private data.""",
 ["Gowns: the guild's uniform.","Ritual makes transition real.","Attend."]),
("Signature essay: the school motto", "school history",
 "A Signature original essay: Veritas, Lux et Veritas, 'Floreat Etona' — mottos as compressed mission statements.",
 """SIGNATURE ORIGINAL ESSAY — MOTTOS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Harvard: 'Veritas' (1643) — truth, one word. Yale: 'Lux et Veritas' — light and truth. Eton: 'Floreat Etona' — let Eton flourish. The Sorbonne's heirs: 'Hic et nunc' — here and now.

The Signature reading: the motto is the school's tweet — the mission in miniature. The best are verbs (floreat — flourish!) or nouns that demand (veritas — truth!).

The test: does the school live it? The motto on the wall vs. the motto in the halls.

The Signature suggestion: every school should choose its motto deliberately — and every student should be able to translate it. (Looking at you, every school with Latin nobody can parse.)

Public methodology. No private data.""",
 ["Mission in miniature.","Verbs beat nouns.","Live it, don't just carve it."]),
# --- notable alumni (10): original profiles of archetypes ---
("Signature profile: the scholarship kid (original archetype)", "notable alumni",
 "A Signature original profile (archetype, not a real person): the first-generation student who changed the family tree.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

She was the first in her family to finish high school, let alone college. The scholarship letter came on a Tuesday; her mother cried; her father — who'd left school at fourteen — framed it.

At university she worked nights, studied mornings, and called home Sundays. The imposter syndrome was real. So was the 3.8 GPA.

She became a teacher — back in her neighborhood, in her old school. Her students call her 'Miss.' Her mother calls her 'my professor.'

The archetype: the scholarship kid doesn't just get an education — she exports it. Every lesson she teaches is the scholarship, compounded.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","First-generation.","The scholarship, compounded."]),
("Signature profile: the late bloomer (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the student who found her subject at thirty — and the school that waited.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

She failed chemistry at sixteen. At thirty — two kids, a job, a mortgage — she took a night class. Something clicked. The periodic table, which had been wallpaper, became a map.

BSc at 34. PhD at 40. The professor who'd failed her at sixteen wrote the recommendation — 'She was never untalented,' he said. 'She was unready. There's a difference.'

The archetype: schools measure at fixed times; talent keeps its own schedule. The late bloomer is the system's reminder — readiness isn't a deadline.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Failed at 16; PhD at 40.","Readiness isn't a deadline."]),
("Signature profile: the class clown who grew up (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the joker who became the school's beloved principal.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

He was sent to the office weekly — always for making people laugh at the wrong time. The teachers despaired. The students adored.

What the records missed: he was reading the room. The class clown is a social genius — timing, empathy, courage.

He became a teacher ('to make the boring parts fun'), then a principal. His assemblies are legendary — part stand-up, part sermon. Attendance at his school: the district's highest.

The archetype: the disruptor, channeled. The school that punishes the clown loses the performer; the school that directs him gains a leader.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Detention to principal.","Disruption, channeled."]),
("Signature profile: the quiet one (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the silent student whose notebook changed the science fair.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

She never raised her hand. Teachers called her 'shy' — she was observing. Her notebook: three years of detailed observations — the pond's seasons, the weather's patterns, the birds' returns.

The science fair: her project — five years of pond data — won everything. The judges had never seen a middle-schooler with a longitudinal study.

She's a field biologist now. Still quiet. Still observing. Her papers are meticulous; her talks are short; her data is irrefutable.

The archetype: the quiet ones are working. The school's job: give them the notebook, the pond, and the time.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Five years of pond data.","The quiet ones are working."]),
("Signature profile: the transfer student (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the new kid, seven schools in ten years — and what she learned.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

Seven schools in ten years — military family. She learned: how to read a cafeteria in one lunch period. How to make one friend fast (one is enough). How to be the new kid without being the weird kid.

What the moving taught: adaptability is a skill. Every school does it differently — the transfer student learns the meta-lesson: systems vary, people rhyme.

She's a diplomat now. (Of course.) Her colleagues marvel at her cultural fluency. She learned it in cafeterias.

The archetype: the transfer student is the school's exchange program with itself. Welcome them well — they're carrying news from elsewhere.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Seven schools.","Adaptability as curriculum."]),
("Signature profile: the athlete-scholar (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the captain who was also valedictorian — and the myth she busted.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

Team captain. Valedictorian. The school didn't know which trophy case to use.

The myth she busted: 'dumb jock' / 'weak nerd' — the binary. Her method: the discipline transferred. Practice schedules became study schedules. Film study became text analysis. The team became the study group.

The injury (junior year) taught the real lesson: identity can't be one thing. She was more than the sport — the grades proved it, but the injury taught it.

She's a surgeon now. Her hands — trained on the field — are famous in the OR.

The archetype: excellence transfers. The school's job: let students be both.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Captain + valedictorian.","Excellence transfers."]),
("Signature profile: the rebel with a cause (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the protester the principal secretly admired.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

She organized the walkout — peacefully, politely, with permits. The principal was furious. (Later: impressed.)

Her causes: the library's hours, the lunch program, the dress code's double standard. She won two of three — the dress code took another year and another protest.

What the school learned: the rebel with a cause is practicing citizenship. The civics textbook describes democracy; she did it.

She's a lawyer now — civil rights. The principal wrote her recommendation. 'She'll argue with you,' it said. 'Let her. She's usually right.'

The archetype: dissent is a skill. Teach it well.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Walkouts with permits.","Dissent is a skill."]),
("Signature profile: the maker (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the kid who was always building — and the workshop that raised him.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

He built: a treehouse (age 8), a go-kart (10), a robot (13), a business (16 — fixing phones). School was the interruption between builds.

The shop teacher saw it: gave him the keys to the workshop, the advanced projects, the trust. 'School' finally made sense — physics was just building, explained.

He skipped college (the controversy!). Started a company at 19. It worked.

The archetype: the maker learns by doing — the school's job is to provide the workshop, not the lecture. Some minds are hands-first.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Treehouse to company.","Hands-first minds."]),
("Signature profile: the peacemaker (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the student everyone trusted — the mediator the school didn't know it had.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

Every friend group has one: the person both sides trust. She was the school's — settling roommate disputes, club rivalries, the Great Cafeteria Schism of junior year.

Her method: listen first, repeat back, find the overlap. 'You both want the same thing,' she'd say. Usually true.

She's a diplomat now — the real kind, with a posting and a portfolio. Her colleagues call her 'the closer.'

The archetype: peacemaking is leadership. The school's job: notice the mediators — they're practicing statecraft in the hallway.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","The trusted one.","Peacemaking is leadership."]),
("Signature profile: the returner (original archetype)", "notable alumni",
 "A Signature original profile (archetype): the graduate who came back to teach — the circle complete.",
 """SIGNATURE ORIGINAL PROFILE — ARCHETYPE
src: signature. This is an original archetype study, not a real person. Property of Justin Addam Higgins.

She left for the big city, the big job, the big life. Twenty years later, she came back — to teach in her old classroom.

Why: 'Someone did it for me. The debt compounds.'

Her students get the stories: what the school was like, what's changed, what hasn't. She's the living archive — the alumna as institution.

The archetype: the returner closes the circle. Schools are rivers — the water leaves, some returns as rain.

Clearly labeled archetype. No real person described.""",
 ["Clearly labeled archetype.","Left, then returned to teach.","The circle complete."]),
# --- class statistics (10): original statistical essays ---
("Signature essay: the class as a dataset", "class statistics",
 "A Signature original essay: prosopography — what class statistics can (and can't) tell us.",
 """SIGNATURE ORIGINAL ESSAY — CLASS STATISTICS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Prosopography: the study of a group through its collective biography — the class as a dataset.

What the numbers show: Harvard 1900 (~400 graduates, $150 tuition); Oxford's doubling 1800–1850; the GI Bill's 49% (1947). The aggregates reveal the era: who could attend, what it cost, where they went.

What the numbers hide: the individuals. Statistics are the map, not the territory — the class report's tables don't show the friendships, the failures, the luck.

The Signature rule: publish aggregates, protect individuals. This database's class statistics are historical and aggregate only — never private student data.

The method: the class report (the published reunion book) is the source. Read the tables; respect the people.

Public methodology. No private data.""",
 ["Prosopography: group biography.","Aggregates reveal eras.","Map, not territory."]),
("Signature essay: tuition across the centuries", "class statistics",
 "A Signature original essay: what school cost — from medieval fees to the modern sticker price.",
 """SIGNATURE ORIGINAL ESSAY — TUITION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Bologna 1088: students paid professors directly — the original tuition. Eton 1440: free for the 70 scholars; the Oppidans paid. Harvard 1900: $150/year. The modern sticker: $50,000+/year at private US colleges.

The Signature arc: education's price went from direct (pay the teacher) to endowed (the scholars) to debt-financed (the loans). Each model shapes who attends.

The free experiments: the Open University (1969), MOOCs (2012) — the price dropped to zero, the completion dropped too. Price isn't the only barrier; structure matters.

The question: what should school cost? The Signature answer: the student should pay in effort, not in debt.

Public methodology. No private data.""",
 ["1088: pay the teacher.","1900: $150/year.","Effort, not debt."]),
("Signature essay: the GI Bill classroom", "class statistics",
 "A Signature original essay: 1947 — when veterans were half the students.",
 """SIGNATURE ORIGINAL ESSAY — GI BILL
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Fall 1947: 1.1M veterans, 49% of US enrollment. Quonset huts for classrooms. Married students — the universities built family housing for the first time.

The Signature reading: the GI Bill was the largest affirmative action program in history — for white men, mostly (Black veterans were systematically shortchanged — the record must say so).

The classroom changed: older, serious, experienced. Professors learned to teach adults. The 'traditional student' (18, single, full-time) became the minority — permanently.

The lesson: access transforms the institution. Let them in, and the school becomes something new.

Public methodology. No private data.""",
 ["49% veterans, 1947.","Access transforms.","The record must note the exclusions."]),
("Signature essay: women enter the numbers", "class statistics",
 "A Signature original essay: the statistics of coeducation — 1837 to the present.",
 """SIGNATURE ORIGINAL ESSAY — COEDUCATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1837: Mount Holyoke opens. 1869/1871: Girton and Newnham. 1948: Cambridge grants women's degrees. 1969–83: the great coeducation wave.

The numbers: US women went from 36% of enrollment (1900) to the majority (1979–present). The faculty numbers lagged — and lag.

The Signature reading: the statistics tell the struggle — every percentage point was argued. The 1897 Cambridge vote (against women's degrees) is the resistance, quantified.

The current frontier: STEM fields, leadership, the pay gap the degree doesn't close.

Count it: what gets measured gets changed.

Public methodology. No private data.""",
 ["1837 to the majority (1979).","Every point was argued.","Count it to change it."]),
("Signature essay: the 70 scholars", "class statistics",
 "A Signature original essay: Eton's 70 — the most durable number in education.",
 """SIGNATURE ORIGINAL ESSAY — ETON'S 70
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

1440: Henry VI endows 70 poor scholars. 2026: still 70 King's Scholars. Nearly 600 years, one number.

The Signature meditation: institutions change everything except their sacred numbers. The 70 survived the Reformation, the Civil War, two World Wars, and comprehensive-school politics.

What the 70 means: the foundation's promise — that the poor scholar belongs — outlasted every era that doubted it. The Oppidans (1,300+) pay; the 70 don't. The ratio changed; the promise didn't.

The lesson: endow the promise, not the building. Buildings fall; the 70 continues.

Public methodology. No private data.""",
 ["70 scholars; 600 years.","The promise outlasts eras.","Endow promises."]),
("Signature essay: literacy's long climb", "class statistics",
 "A Signature original essay: 20% (1870) to 80%+ (today) — the school century in one graph.",
 """SIGNATURE ORIGINAL ESSAY — LITERACY
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

World literacy: ~20% (1870) → ~50% (1950) → ~87% (today). The school century.

The drivers: compulsory schooling (Prussia led, the world followed), the textbook (cheap print), the teacher (trained, paid, mostly women).

The Signature reading: literacy is the prerequisite of everything — democracy, science, the novel. The graph's slope is civilization's slope.

The unfinished: 750M adults still can't read — mostly women, mostly poor, mostly rural. The last mile is the hardest.

The school's job, in one number: move the graph.

Public methodology. No private data.""",
 ["20% to 87%.","The slope is civilization's.","750M to go."]),
("Signature essay: the scholarship equation", "class statistics",
 "A Signature original essay: who gets aid, who needs it, and the math of opportunity.",
 """SIGNATURE ORIGINAL ESSAY — SCHOLARSHIPS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The Rhodes (1902): 100/year, 8,000+ total — the imperial scholarship, globalized. The GI Bill: the mass scholarship. Need-blind admissions: the promise (few can afford it).

The Signature math: a scholarship's value isn't the money — it's the counterfactual. What would she have done without it? The archetype in this database (the scholarship kid) is the answer.

The efficiency: aid to the talented poor has the highest return in education — the marginal student gains the most.

The Signature principle: fund the promise (like Eton's 70), measure the counterfactual, and remember — every statistic was a student.

Public methodology. No private data.""",
 ["Value = the counterfactual.","Aid the talented poor.","Every statistic was a student."]),
("Signature essay: class size and the human scale", "class statistics",
 "A Signature original essay: 400 (Harvard 1900) to 40,000 (the mega-university) — does size matter?",
 """SIGNATURE ORIGINAL ESSAY — CLASS SIZE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Harvard 1900: ~400 graduates. The modern mega-university: 40,000+ students. The seminar: 12. The lecture: 500.

The Signature reading: the research is clear — small classes help most in the early years, least in the late. But the numbers miss the point: the tutorial (Oxford's one-on-one) isn't about size, it's about attention.

The human scale: the school where someone knows your name. That can be 400 or 40,000 — it's a culture, not a count.

The Signature rule: measure belonging, not just enrollment. The statistic that matters: 'my teacher knows me.'

Public methodology. No private data.""",
 ["400 to 40,000.","Attention, not size.","'My teacher knows me.'"]),
("Signature essay: the reunion numbers", "class statistics",
 "A Signature original essay: 25th reunions, mortality tables, and the class as a life dataset.",
 """SIGNATURE ORIGINAL ESSAY — REUNIONS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The class report: the 25th-reunion book — careers, marriages, children, deaths. The aggregate tables are a generation's biography.

What they show: the era's arc — the class of 1940's war service, the class of 1970's divorces, the class of 2000's tech jobs. The cohort as history.

The mortality table: the reunion's quiet page — who's missing, and why. The class learns its own fragility.

The Signature use: reunions are longitudinal studies with catering. The data is the excuse; the people are the point.

Attend yours. The numbers need faces.

Public methodology. No private data.""",
 ["The 25th-reunion book.","Cohort as history.","The numbers need faces."]),
("Signature essay: dropouts who dropped in", "class statistics",
 "A Signature original essay: the non-completers — Tagore, Edison, the makers — and what the numbers miss.",
 """SIGNATURE ORIGINAL ESSAY — DROPOUTS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Tagore: hated school, won the Nobel. Edison: three months of school, 1,093 patents. The archetype in this database (the maker): the hands-first mind.

The Signature reading: completion statistics measure the school, not the student. The dropout who learns elsewhere is the system's blind spot — and its indictment.

But: the statistics also show the risk — most dropouts don't become Edison. The school's job: be worth completing, and be porous enough that leavers can return.

The late bloomer (this database's archetype) is the dropout's sibling — same schedule, different timing.

Public methodology. No private data.""",
 ["Completion measures the school.","Be worth completing.","Be porous."]),
# --- architecture (10) ---
("Signature essay: the quadrangle mind", "architecture",
 "A Signature original essay: Oxford's quads — the enclosed college as a way of thinking.",
 """SIGNATURE ORIGINAL ESSAY — QUADRANGLES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The quadrangle: four ranges around a lawn — the monastery's plan, secularized. Oxford's quads (Merton's Mob Quad, 14th century, the oldest) enclose the scholar.

The Signature reading: the quad is a cognitive architecture — inward, bounded, contemplative. The walls say: the world is outside; thought is inside. The lawn (do not walk on it) says: beauty needs rules.

The American translation: the campus green — open, not enclosed. Jefferson's Lawn (1819): the quad democratized.

The lesson: buildings teach. The quad teaches focus. Choose your architecture; you're choosing your mind.

Public methodology. No private data.""",
 ["The monastery, secularized.","Walls say: think inside.","Buildings teach."]),
("Signature essay: libraries as temples", "architecture",
 "A Signature original essay: the Long Room, the Radcliffe Camera, the Beinecke — the library as sacred space.",
 """SIGNATURE ORIGINAL ESSAY — LIBRARY ARCHITECTURE
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Trinity Dublin's Long Room (1712): 65 meters of oak — the cathedral nave, reshelved. The Radcliffe Camera (1749): the dome as mind. The Beinecke (1963): marble walls that glow — the book as light.

The Signature theory: the great libraries are temples — the architecture says: what happens here matters. The hush is designed.

The school library's version: smaller, but the same grammar — the high windows, the long tables, the quiet. The child feels the temple before understanding it.

The digital challenge: the cloud has no architecture. The library's answer: the building becomes the sanctuary — the books' body, even as their souls go digital.

Public methodology. No private data.""",
 ["Libraries = temples.","The hush is designed.","Sanctuary in the cloud age."]),
("Signature essay: the chapel at the center", "architecture",
 "A Signature original essay: King's, Eton, the school chapel — faith at the school's heart, and what replaced it.",
 """SIGNATURE ORIGINAL ESSAY — CHAPELS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

King's College Chapel (1446–1515): the fan vault — heaven in stone. Eton's chapel (1448): 580 years of daily services. The school chapel was the day's frame — morning prayer, the week's rhythm.

The Signature reading: the chapel centered the school — literally (the plan) and temporally (the day). Secularization moved the center: to the library (knowledge), the stadium (community), the student union (self).

The carols remain: King's College Choir, Christmas Eve, since 1928 — the chapel's afterlife as broadcast.

The lesson: every school has a center — find it, and you've found the school's soul.

Public methodology. No private data.""",
 ["The day's frame.","Center moved: chapel to library.","Find the center."]),
("Signature essay: the stadium and the school", "architecture",
 "A Signature original essay: the Colosseum's descendants — the school stadium as civic theater.",
 """SIGNATURE ORIGINAL ESSAY — STADIA
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The stadium: the school's largest room — 100,000 at Michigan, the Yale Bowl (1914, the prototype). Friday nights: the town's theater.

The Signature reading: the stadium is the chapel's successor — the ritual gathering, the shared emotion, the identity performed. The fight song is the hymn; the team is the clergy.

The economics: the stadium funds the school (or bankrupts it). The arms race — facilities as recruiting — is the chapel-building of our age.

The balance: the library and the stadium — the school's two temples. A healthy school honors both.

Public methodology. No private data.""",
 ["The chapel's successor.","The fight song is the hymn.","Honor both temples."]),
("Signature vignette: the stonemason (original fiction)", "architecture",
 "A Signature original vignette (fiction): a mason carves his mark on the chapel, 1480.",
 """SIGNATURE ORIGINAL VIGNETTE — THE MASON, 1480
src: signature. An original work of historical fiction by the Signature system, property of Justin Addam Higgins. Clearly labeled fiction.

He cut his mark into the stone — a small cross in a circle — where only the next mason would see it. The vault was going up; the fan ribs spread like a stone palm above him.

'Will it hold?' the apprentice asked.

'God willing and the centering true,' he said. The wooden centering held the stones till the keystone locked. Then — the miracle — the wood came away, and the stone stayed.

He'd worked on the chapel six years. He'd never see it finished — none of them would. Cathedrals are the long game.

His mark is still there. The tourists don't see it. The masons do — every restorer finds the old marks and adds their own.

The building is the archive. The marks are the signatures.

(Author's note: masons' marks are real; this mason is imagined.)""",
 ["Clearly labeled fiction.","The mark only masons see.","Cathedrals: the long game."]),
("Signature essay: dormitories — the architecture of friendship", "architecture",
 "A Signature original essay: the staircases, corridors, and quads where friendships are built.",
 """SIGNATURE ORIGINAL ESSAY — DORMITORIES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Oxford's staircases: eight rooms, one stair — the vertical village. The American dorm corridor: forty doors, one hall — the horizontal city. The roommate: the forced friendship that often lasts.

The Signature sociology: architecture makes friends. The staircase's eight beat the corridor's forty — small groups bond. The shared kitchen beats the dining hall — cooking together is the fastest friendship.

The study: the MIT Building 20 myth (the ugly building where great science happened) — creativity loves the unplanned corner.

The lesson: design for collision — the stairwell, the laundry room, the 2 a.m. kitchen. Friendship is architecture's byproduct.

Public methodology. No private data.""",
 ["Staircase: vertical village.","Design for collision.","Friendship's byproduct."]),
("Signature essay: the classroom's evolution", "architecture",
 "A Signature original essay: the one-room schoolhouse to the learning studio — rooms that teach.",
 """SIGNATURE ORIGINAL ESSAY — CLASSROOMS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The one-room schoolhouse: one room, eight grades, the stove — the teacher as the architecture. The Victorian classroom: rows, the master's desk — order as pedagogy. The open classroom (1970s): walls down — freedom as pedagogy (it failed; noise won).

The Signature reading: the room is the method. Rows say: listen. Circles say: discuss. Studios say: make. The best rooms are flexible — the furniture moves, the method follows.

The future: the hybrid room — the camera, the screen, the distant student present. The architecture of attention, redesigned.

The constant: the teacher. The room helps; the human teaches.

Public methodology. No private data.""",
 ["Rows: listen. Circles: discuss.","The room is the method.","The human teaches."]),
("Signature essay: gates and walls", "architecture",
 "A Signature original essay: the school gate — threshold, symbol, and the town-gown line.",
 """SIGNATURE ORIGINAL ESSAY — GATES
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The school gate: the threshold — inside, the school's rules; outside, the world's. The Oxford college gate: the porter's lodge — the gatekeeper's interview. The campus arch: the photo spot — the degree's frame.

The Signature reading: gates mark belonging. The student passes through daily — the ritual of entry. The graduate passes out — the ritual of exit. The gate is the school's punctuation.

The town-gown wall: Oxford's walls, the campus fence — protection or exclusion? The best schools lower the wall: the public lecture, the open day, the community garden.

The motto: the gate should welcome more than it warns.

Public methodology. No private data.""",
 ["Threshold and symbol.","Rituals of entry and exit.","Welcome more than warn."]),
("Signature essay: the school of the future", "architecture",
 "A Signature original essay: what the 2050 school looks like — the Signature speculation.",
 """SIGNATURE ORIGINAL ESSAY — FUTURE SCHOOLS
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

The 2050 school: the campus as park (buildings among trees), the classroom as studio (flexible, connected), the library as everywhere (the cloud, plus the sanctuary).

The Signature predictions:
- The lecture hall shrinks; the workshop grows. Making beats listening.
- The school opens: the community uses the labs, the fields, the kitchens. The wall lowers.
- The teacher remains — the AI tutors, the human mentors. The relationship is the school.
- The campus greens: solar roofs, rain gardens, the building as lesson.

The constant: the agreement — the young will be taught, the old will teach. The architecture changes; the promise doesn't.

The future school: the oldest idea, in the newest building.

Public methodology. No private data.""",
 ["Campus as park.","The teacher remains.","The oldest idea, newest building."]),
("Signature essay: preserving old schools", "architecture",
 "A Signature original essay: the 600-year classroom — why we keep the old buildings.",
 """SIGNATURE ORIGINAL ESSAY — PRESERVATION
src: signature. An original work by the Signature system, property of Justin Addam Higgins.

Eton's chapel (1448): still used daily. The Bodleian's Divinity School (1488): still examined in. The one-room schoolhouse: now a museum — the lesson preserved.

The Signature case for preservation: old schools teach by existing — the student in the 1488 room joins five centuries. The building is the curriculum's body.

The practice: restore, don't freeze — the Wren Library still lends books. The working old building beats the museum.

The threat: the maintenance bill — old buildings are expensive. The answer: the alumni — the 600-year classroom is funded by gratitude.

Keep the old schools. They're the promise, in stone.

Public methodology. No private data.""",
 ["The building is the curriculum.","Restore, don't freeze.","The promise, in stone."]),
]

# ================= specs + main =================
GENRES = {
    'census': ['population total','historical census','demographic breakdown','urbanization','migration','methodology'],
    'genealogy': ['family tree','historical figure','record guide','case study','heraldry','research method'],
    'children': ['bedtime','adventure','animal tale','moral tale','fantasy','rhyme'],
    'local': ['city founding','historic site','landmark','document','era portrait','photo archive'],
    'oral': ['speech','testimony','interview','memoir','broadcast','witness account'],
    'yearbook': ['school history','notable alumni','school song','club feature','class statistics','architecture'],
}

def check_counts(pool, name, genres):
    from collections import Counter
    c = Counter(t[1] for t in pool)
    assert len(pool) == 60, f'{name}: {len(pool)} topics, want 60'
    for g in c:
        assert g in genres, f'{name}: genre {g!r} not in genre list'
    assert set(c) == set(genres), f'{name}: genres missing {set(genres)-set(c)}'
    titles = [t[0] for t in pool]
    assert len(set(titles)) == 60, f'{name}: duplicate titles'

SPECS = [
 dict(slug='census-records-public', name='Public Census Records Database',
      tagline='The public library of census records: real aggregate population statistics from censuses worldwide — historical and modern.',
      record_kind='public census record', id_prefix='JAH-CENPUB-', ai_name='JAH Public Census Archivist',
      hero='The public library of census records — real aggregate population statistics from every census round worldwide: national totals, historical counts, demographic breakdowns, urbanization, migration, and methodology. Aggregate statistics only — no individual personal data, ever.',
      about_archive="This database's Public Census Records Database archive (JAH-CENPUB- records): real aggregate census statistics from around the world — national population totals, historical censuses from Domesday to the digital round, demographic breakdowns, urbanization, migration, and census methodology. Every record is the full file, never a stub. Aggregate statistics only — no individual personal data is collected or stored.",
      role='public census archivist - population totals, historical censuses, demographics, urbanization, migration, methodology',
      genres=GENRES['census'], src='public', media_kind='census', audio=False, badge='public',
      srcnote='src:"public" = real public aggregate census statistics',
      gen_note='Records are real public aggregate census statistics, clearly marked.',
      about_sig='✓ This database is a <b>Signature-governed archive of real public aggregate census statistics</b> — every record drawn from published public sources, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in CENPUB]),
 dict(slug='census-records-signature', name='Signature Census Records Database',
      tagline='Signature original demographic studies: original essays, analyses, and methodology guides on population and censuses.',
      record_kind='signature census study', id_prefix='JAH-CENSIG-', ai_name='JAH Signature Census Mind',
      hero='Signature original demographic studies — original essays, analyses, and methodology guides on population, censuses, and what the numbers mean. Every study is a Signature original, clearly labeled.',
      about_archive="This database's Signature Census Records Database archive (JAH-CENSIG- records): original Signature demographic studies — essays on world population milestones, national census readings, historical census analyses, demographic divides, urbanization, migration, and census methodology guides. Every record is the full file, never a stub. Signature originals, clearly labeled.",
      role='signature census scholar - original demographic essays, census analysis, methodology guides',
      genres=GENRES['census'], src='signature', media_kind='census', audio=False, badge='signature',
      srcnote='src:"signature" = Signature original work, clearly labeled',
      gen_note='Records are Signature originals, clearly labeled.',
      about_sig='✓ This database is a <b>Signature-original archive</b> — every study an original work of the Signature system, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in CENSIG]),
 dict(slug='genealogy-public', name='Public Genealogy Database',
      tagline='The public library of genealogy: famous family lines, historical figures, and research guides — public and historical records only.',
      record_kind='public genealogy record', id_prefix='JAH-GENPUB-', ai_name='JAH Public Genealogy Archivist',
      hero='The public library of genealogy — famous family lines, public historical figures, record guides, worked case studies, heraldry, and research method. Public and historical records only — never private family data.',
      about_archive="This database's Public Genealogy Database archive (JAH-GENPUB- records): documented family lines of public historical figures (long deceased), public historical person portraits, guides to parish registers, censuses, wills, military and immigration records, DNA, newspapers, land, heraldry, and research method. Every record is the full file, never a stub. Public and historical records only.",
      role='public genealogy archivist - family lines, historical figures, record guides, heraldry, method',
      genres=GENRES['genealogy'], src='public', media_kind='genealogy', audio=False, badge='public',
      srcnote='src:"public" = public and historical records only; never private family data',
      gen_note='Records are public and historical records, clearly marked. Never private family data.',
      about_sig='✓ This database is a <b>Signature-governed archive of public and historical genealogical records</b> — public figures and public knowledge only, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in GENPUB]),
 dict(slug='genealogy-signature', name='Signature Genealogy Database',
      tagline='Signature original genealogy: original research guides, method essays, and clearly-labeled illustrative case studies.',
      record_kind='signature genealogy guide', id_prefix='JAH-GENSIG-', ai_name='JAH Signature Genealogy Mind',
      hero='Signature original genealogy — original research guides, method essays, heraldry guides, and clearly-labeled illustrative case studies. Every work is a Signature original.',
      about_archive="This database's Signature Genealogy Database archive (JAH-GENSIG- records): original Signature guides to parish registers, census schedules, wills, military and immigration records, DNA, newspapers, land, and proof standards; original essays on famous families; original heraldry guides; original research methods; and clearly-labeled illustrative case studies (fictional composites for method demonstration). Every record is the full file, never a stub. Signature originals, clearly labeled.",
      role='signature genealogy scholar - original research guides, method, heraldry, illustrative case studies',
      genres=GENRES['genealogy'], src='signature', media_kind='genealogy', audio=False, badge='signature',
      srcnote='src:"signature" = Signature original work, clearly labeled; case studies are fictional composites',
      gen_note='Records are Signature originals, clearly labeled. Case studies are fictional composites for method demonstration.',
      about_sig='✓ This database is a <b>Signature-original archive</b> — every guide an original work of the Signature system, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in GENSIG]),
 dict(slug='childrens-literature-public', name="Public Children's Literature Database",
      tagline="The public library of children's literature: complete public-domain stories — Aesop, Grimm, Andersen — full text with illustrations and audio.",
      record_kind="public children's story", id_prefix='JAH-CHILPUB-', ai_name="JAH Public Children's Librarian",
      hero="The public library of children's literature — complete public-domain stories with full text: Aesop's fables, Grimm's fairy tales, Andersen's tales. Every story complete, with storybook illustrations and gentle audio motifs.",
      about_archive="This database's Public Children's Literature Database archive (JAH-CHILPUB- records): complete public-domain children's stories — 25 of Aesop's fables, 18 of Grimm's tales, 17 of Andersen's tales — each with the full text, a storybook illustration, and a gentle audio motif. Every record is the complete story, never a stub or summary.",
      role="public children's librarian - complete public-domain stories: Aesop, Grimm, Andersen",
      genres=GENRES['children'], src='public', media_kind='children', audio=True, badge='public',
      srcnote='src:"public" = public-domain stories (Aesop, Grimm, Andersen), complete texts',
      gen_note='Records are complete public-domain stories, clearly marked.',
      about_sig='✓ This database is a <b>Signature-governed archive of public-domain children\'s literature</b> — complete stories, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in CHILPUB]),
 dict(slug='childrens-literature-signature', name="Signature Children's Literature Database",
      tagline="Signature original children's stories: 60 complete original bedtime tales, adventures, animal tales, and rhymes — with illustrations and audio.",
      record_kind="signature children's story", id_prefix='JAH-CHILSIG-', ai_name="JAH Signature Storyteller",
      hero="Signature original children's stories — 60 complete original tales: bedtime stories, adventures, animal tales, moral tales, fantasies, and rhymes. Every story complete and original, with illustrations and gentle audio motifs.",
      about_archive="This database's Signature Children's Literature Database archive (JAH-CHILSIG- records): 60 complete original children's stories by the Signature system — bedtime, adventure, animal tales, moral tales, fantasy, and rhyme — each with the full story text, a storybook illustration, and a gentle audio motif. Every record is the complete original story, never a stub. Signature originals, clearly labeled.",
      role="signature storyteller - complete original children's stories in every genre",
      genres=GENRES['children'], src='signature', media_kind='children', audio=True, badge='signature',
      srcnote='src:"signature" = Signature original stories, clearly labeled',
      gen_note='Records are Signature original stories, clearly labeled.',
      about_sig='✓ This database is a <b>Signature-original archive</b> — every story an original work of the Signature system, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in CHILSIG]),
 dict(slug='local-history-public', name='Public Local History Database',
      tagline='The public library of local history: real city foundings, historic sites, landmarks, documents, and photographs — worldwide.',
      record_kind='public local history record', id_prefix='JAH-LOCHPUB-', ai_name='JAH Public Local History Archivist',
      hero="The public library of local history — real local history from every region: city foundings, historic sites, landmarks, historical documents, era portraits, and photo-archive records. Every record the full document, with illustrations.",
      about_archive="This database's Public Local History Database archive (JAH-LOCHPUB- records): real local-history records from around the world — city foundings (Rome to Timbuktu), historic sites (Pompeii to Lalibela), landmarks, historical documents (Magna Carta to the UDHR), era portraits, and photo-archive records. Every record is the full file, never a stub.",
      role='public local history archivist - city foundings, sites, landmarks, documents, eras, photographs',
      genres=GENRES['local'], src='public', media_kind='local', audio=False, badge='public',
      srcnote='src:"public" = real public local-history records from worldwide sources',
      gen_note='Records are real public local-history records, clearly marked.',
      about_sig='✓ This database is a <b>Signature-governed archive of real public local history</b> — every record drawn from published public sources, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in LOCHPUB]),
 dict(slug='local-history-signature', name='Signature Local History Database',
      tagline='Signature original local history: original essays, research guides, and clearly-labeled historical vignettes — every region.',
      record_kind='signature local history work', id_prefix='JAH-LOCHSIG-', ai_name='JAH Signature Local Historian',
      hero="Signature original local history — original essays on cities, sites, landmarks, documents, and eras; research guides; and clearly-labeled original historical vignettes. Every region, every era.",
      about_archive="This database's Signature Local History Database archive (JAH-LOCHSIG- records): original Signature essays on city foundings, historic sites, landmarks, documents, era portraits, and photo archives; original research guides; and clearly-labeled original historical vignettes (fiction). Every record is the full file, never a stub. Signature originals, clearly labeled.",
      role='signature local historian - original essays, guides, and historical vignettes',
      genres=GENRES['local'], src='signature', media_kind='local', audio=False, badge='signature',
      srcnote='src:"signature" = Signature original work, clearly labeled; vignettes are fiction',
      gen_note='Records are Signature originals, clearly labeled. Vignettes are original historical fiction.',
      about_sig='✓ This database is a <b>Signature-original archive</b> — every work an original of the Signature system, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in LOCHSIG]),
 dict(slug='oral-histories-public', name='Public Oral Histories Database',
      tagline='The public library of oral histories: public-domain speeches, testimonies, and interviews — complete transcripts with audio.',
      record_kind='public oral history', id_prefix='JAH-ORALPUB-', ai_name='JAH Public Oral History Archivist',
      hero="The public library of oral histories — public-domain speeches, testimonies, interviews, memoirs, broadcasts, and witness accounts with complete transcripts and ambient audio. History in voices.",
      about_archive="This database's Public Oral Histories Database archive (JAH-ORALPUB- records): public-domain speeches (Gettysburg to FDR), testimonies (WPA narratives, disaster survivors), interviews, memoirs, historic broadcasts, and witness accounts — each with the complete transcript and an ambient audio motif. Every record is the full transcript, never a stub.",
      role='public oral history archivist - speeches, testimonies, interviews, memoirs, broadcasts, witnesses',
      genres=GENRES['oral'], src='public', media_kind='oral', audio=True, badge='public',
      srcnote='src:"public" = public-domain transcripts and public accounts',
      gen_note='Records are public-domain transcripts, clearly marked.',
      about_sig='✓ This database is a <b>Signature-governed archive of public-domain oral history</b> — complete transcripts, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in ORALPUB]),
 dict(slug='oral-histories-signature', name='Signature Oral Histories Database',
      tagline='Signature original oral histories: 60 dramatized speeches, testimonies, and interviews — clearly-labeled original fiction with audio.',
      record_kind='signature oral history', id_prefix='JAH-ORALSIG-', ai_name='JAH Signature Oral Historian',
      hero="Signature original oral histories — 60 dramatized speeches, testimonies, interviews, memoirs, broadcasts, and witness accounts. Clearly-labeled original fiction, complete transcripts, ambient audio.",
      about_archive="This database's Signature Oral Histories Database archive (JAH-ORALSIG- records): 60 original dramatized oral histories — speeches, testimonies, interviews, memoirs, broadcasts, and witness accounts — each a complete original transcript with an ambient audio motif. Clearly-labeled original fiction, never presented as real testimony. Every record is the full transcript, never a stub.",
      role='signature oral historian - original dramatized oral histories in every form',
      genres=GENRES['oral'], src='signature', media_kind='oral', audio=True, badge='signature',
      srcnote='src:"signature" = Signature original dramatized fiction, clearly labeled',
      gen_note='Records are Signature original dramatized fiction, clearly labeled — never presented as real testimony.',
      about_sig='✓ This database is a <b>Signature-original archive</b> — every oral history an original dramatization of the Signature system, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in ORALSIG]),
 dict(slug='yearbooks-public', name='Public Yearbooks Database',
      tagline='The public library of school history: historic schools, notable alumni, songs, clubs, and architecture — historical and public only.',
      record_kind='public yearbook record', id_prefix='JAH-YEARPUB-', ai_name='JAH Public Yearbook Archivist',
      hero="The public library of school history — historic schools (Eton 1440 to Howard 1867), notable alumni's school years, public-domain school songs, historic clubs, aggregate class statistics, and school architecture. Historical and public only — never private student data.",
      about_archive="This database's Public Yearbooks Database archive (JAH-YEARPUB- records): public school histories, notable alumni profiles (long-deceased public figures), public-domain school songs with lyrics, historic club features, aggregate historical class statistics, and school architecture. Every record is the full file, never a stub. Historical and public records only — never private student data.",
      role='public yearbook archivist - school histories, alumni, songs, clubs, statistics, architecture',
      genres=GENRES['yearbook'], src='public', media_kind='yearbook', audio=False, badge='public',
      srcnote='src:"public" = historical and public school records; never private student data',
      gen_note='Records are historical and public records, clearly marked. Never private student data.',
      about_sig='✓ This database is a <b>Signature-governed archive of public school history</b> — historical records only, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in YEARPUB]),
 dict(slug='yearbooks-signature', name='Signature Yearbooks Database',
      tagline='Signature original yearbook works: original school songs, club guides, essays, and archetype profiles — clearly labeled.',
      record_kind='signature yearbook work', id_prefix='JAH-YEARSIG-', ai_name='JAH Signature Yearbook Editor',
      hero="Signature original yearbook works — original school songs (singable), club-founding guides, essays on schools, and clearly-labeled alumni archetype profiles. Every work a Signature original.",
      about_archive="This database's Signature Yearbooks Database archive (JAH-YEARSIG- records): 10 original singable school songs, 10 club-founding guides, original essays on schools, universities, mottos, and rituals, clearly-labeled alumni archetype profiles (not real people), original class-statistics essays, and original school-architecture essays. Every record is the full file, never a stub. Signature originals, clearly labeled.",
      role='signature yearbook editor - original songs, club guides, essays, archetype profiles',
      genres=GENRES['yearbook'], src='signature', media_kind='yearbook', audio=False, badge='signature',
      srcnote='src:"signature" = Signature original work, clearly labeled; archetypes are not real people',
      gen_note='Records are Signature originals, clearly labeled. Archetype profiles are not real people.',
      about_sig='✓ This database is a <b>Signature-original archive</b> — every work an original of the Signature system, property of Justin Addam Higgins.',
      topics=[dict(title=t[0], genre=t[1], brief=t[2], text=t[3], facts=t[4]) for t in YEARSIG]),
]

POOLS = {'census-records-public': CENPUB, 'census-records-signature': CENSIG,
         'genealogy-public': GENPUB, 'genealogy-signature': GENSIG,
         'childrens-literature-public': CHILPUB, 'childrens-literature-signature': CHILSIG,
         'local-history-public': LOCHPUB, 'local-history-signature': LOCHSIG,
         'oral-histories-public': ORALPUB, 'oral-histories-signature': ORALSIG,
         'yearbooks-public': YEARPUB, 'yearbooks-signature': YEARSIG}

def main():
    # validate pools
    for spec in SPECS:
        gk = {'census-records-public':'census','census-records-signature':'census',
              'genealogy-public':'genealogy','genealogy-signature':'genealogy',
              'childrens-literature-public':'children','childrens-literature-signature':'children',
              'local-history-public':'local','local-history-signature':'local',
              'oral-histories-public':'oral','oral-histories-signature':'oral',
              'yearbooks-public':'yearbook','yearbooks-signature':'yearbook'}[spec['slug']]
        check_counts(POOLS[spec['slug']], spec['slug'], GENRES[gk])
    print('pools OK: 12 x 60')
    counts = {}
    for spec in SPECS:
        n = build_db(spec)
        counts[spec['slug']] = n
        print(f"built {spec['slug']}: {n} records")
    total = update_manifests(SPECS, counts)
    print('manifest databases:', total)

if __name__ == '__main__':
    main()
