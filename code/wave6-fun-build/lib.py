"""Wave 6 fun/social build library — shared engine for 150 databases.
Property of Justin Addam Higgins (JAH)."""
import json, gzip, os, re, subprocess, html, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = open(os.path.join(HERE, 'page_template.html')).read()
PREFIXES = json.load(open(os.path.join(HERE, 'prefixes.json')))
DATA_ROOT = '/home/hatch/workspace/jah-databases-data-1/data'
PAGES_ROOT = '/home/hatch/workspace/jah-databases/db'
GITHUB = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data'

def sig_prefix(pub_prefix):
    return pub_prefix[:-1] + 'S-'

def sig_name(name):
    # "The X Database" -> "The X Signature Database"
    if name.endswith(' Database'):
        return name[:-len(' Database')] + ' Signature Database'
    return name + ' (Signature)'

# ---------------- record renderers ----------------
def _paras(items):
    return '\n'.join(items)

def render_concept(item, pack, rank):
    """pack: sub[list], points[list], req[list], std[list], cite[list],
             demo_kind, demo_program, demo_note, data[dict|None]"""
    return {
        'description': _paras(pack['sub']),
        'how_it_works': _paras(pack.get('how', [])),
        'key_points': pack['points'],
        'requirements': pack['req'],
        'standards': pack['std'],
        'citations': pack['cite'],
        'demo': {'kind': pack['demo_kind'], 'language': 'python',
                 'program': pack['demo_program'], 'note': pack['demo_note']},
        '_data': pack.get('data'),
    }

def _lum(hexcode):
    h = hexcode.lstrip('#')
    r, g, b = (int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r) + 0.7152*f(g) + 0.0722*f(b)

def render_palette(item, pack, rank):
    """pack: colors[(name,hex)], mood, setting, combos[list], technique[list],
             cite[list]"""
    colors = pack['colors']
    clist = '; '.join('%s %s' % (n, hx) for n, hx in colors)
    sub = [
        '%s is a five-color palette built for %s. The colors are %s.' % (pack['t'], pack['setting'], clist),
        'Mood and character: %s Working from this palette means every choice — background, accent, text, highlight — is drawn from the same family, so the result reads as one deliberate design instead of five competing decisions.' % pack['mood'],
        'How to use it: pick one dominant color for roughly 60 percent of the surface, a secondary color for 30 percent, and reserve the remaining 10 percent for the accent that carries the focal point. The two leftover colors act as support — neutrals for breathing room or bridges between the loud colors.',
    ]
    how = [
        'Start with the dominant color and lay it across the largest area. Add the secondary color to the next-largest shapes.',
        'Place the accent color only where the eye should land first — a single button, one headline, the hero object.',
        'Check every text-over-background pair for contrast: the demonstration program below computes the WCAG contrast ratio for each pair in this palette.',
        'If a pair fails at 4.5:1 for body text, darken the background or lighten the text within the same hue family rather than swapping hues.',
    ] + ['Technique note: %s' % t for t in pack.get('technique', [])]
    points = [
        'Five locked colors: %s.' % clist,
        '60-30-10 distribution keeps one color dominant and one color as the accent.',
        'Combos that work inside this palette: %s.' % '; '.join(pack['combos']),
        'Every pair is contrast-checked by the demo program; aim for 4.5:1 or better on text.',
        'Mood target: %s' % pack['mood'],
    ]
    req = ['A surface to apply color to (canvas, slide, room, garment, screen)',
           'The five hex values above, kept consistent across the piece',
           'A way to preview at small size — palettes that work tiny work everywhere']
    std = ['Text contrast of at least 4.5:1 against its background',
           'No more than one high-saturation accent per composition',
           'The same five hex values used everywhere — no drift']
    demo_program = (
        '# Palette contrast check — %s\n'
        'colors = [%s]\n'
        'def lum(h):\n'
        '    r, g, b = (int(h[i:i+2], 16) / 255.0 for i in (1, 3, 5))\n'
        '    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4\n'
        '    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)\n'
        'def ratio(a, b):\n'
        '    x, y = sorted((lum(a), lum(b)), reverse=True)\n'
        '    return (x + 0.05) / (y + 0.05)\n'
        'print("Palette: %s")\n'
        'best = None\n'
        'for i, (n1, h1) in enumerate(colors):\n'
        '    for n2, h2 in colors[i+1:]:\n'
        '        r = ratio(h1, h2)\n'
        '        mark = "PASS" if r >= 4.5 else ("large-text" if r >= 3.0 else "fail")\n'
        '        print("%%s on %%s: %%.2f [%%s]" %% (n1, n2, r, mark))\n'
        '        if best is None or r > best[0]:\n'
        '            best = (r, n1, n2)\n'
        'print("Strongest pair:", best[1], "on", best[2], "at %%.2f:1" %% best[0])\n'
    ) % (pack['t'].replace("'", ""), ', '.join('("%s", "%s")' % (n, hx) for n, hx in colors), pack['t'].replace("'", ""))
    return {
        'description': _paras(sub),
        'how_it_works': _paras(how),
        'key_points': points,
        'requirements': req,
        'standards': std,
        'citations': pack['cite'],
        'demo': {'kind': 'palette-contrast-check', 'language': 'python',
                 'program': demo_program,
                 'note': 'Computes WCAG contrast ratios for every pair in this palette.'},
        '_data': {'colors': [{'name': n, 'hex': hx} for n, hx in colors], 'mood': pack['mood']},
    }

def render_steps(item, pack, rank):
    """pack: steps (16-char x/./- string), sig, bpm, voices[list], origin,
             groove, cite[list]"""
    steps = pack['steps']
    grid = ' '.join('X' if c == 'x' else ('.' if c == '.' else '-') for c in steps)
    sub = [
        '%s is a %s rhythm at %d BPM built on a 16-step grid: %s.' % (pack['t'], pack['sig'], pack['bpm'], grid),
        'Origin and feel: %s The pattern is written as one bar of sixteenth notes, left to right, four beats of four steps each.' % pack['origin'],
        'Voices: %s. Play it by counting "1-e-and-a 2-e-and-a" and striking each voice on its marked steps.' % '; '.join(pack['voices']),
    ]
    how = [
        'Set the tempo to %d BPM and loop one bar.' % pack['bpm'],
        'Layer the voices one at a time: start with the lowest voice, then add the next, until the full groove is running.',
        'Groove note: %s' % pack['groove'],
        'The demo program prints the step grid and the density of each quarter of the bar.',
    ]
    points = [
        'Time signature %s, tempo %d BPM, one bar of 16 steps.' % (pack['sig'], pack['bpm']),
        'Step grid: %s.' % grid,
        'Voices: %s.' % '; '.join(pack['voices']),
        'Feel: %s' % pack['groove'],
        'Origin: %s' % pack['origin'],
    ]
    demo_program = (
        '# Rhythm grid — %s\n'
        'steps = "%s"\n'
        'voices = [%s]\n'
        'print("Grid (16 steps, 4 beats):")\n'
        'print(" ".join("X" if c == "x" else "." for c in steps))\n'
        'print(" ".join("%%2d" %% (i + 1) for i in range(16)))\n'
        'hits = sum(1 for c in steps if c == "x")\n'
        'print("Hits: %%d/16 (density %%.1f%%%%)" %% (hits, 100.0 * hits / 16))\n'
        'for q in range(4):\n'
        '    seg = steps[q*4:(q+1)*4]\n'
        '    print("Beat %%d: %%s (%%d hits)" %% (q + 1, " ".join("X" if c == "x" else "." for c in seg), seg.count("x")))\n'
        'print("Voices:", "; ".join(voices))\n'
    ) % (pack['t'].replace('"', ''), steps, ', '.join('"%s"' % v for v in pack['voices']))
    return {
        'description': _paras(sub),
        'how_it_works': _paras(how),
        'key_points': points,
        'requirements': ['Something to keep time (metronome, drum machine, hands on a table)',
                         'One sound source per voice',
                         'The 16-step grid above'],
        'standards': ['The grid loops cleanly with no extra or missing steps',
                      'Tempo stays within 2 BPM of the target',
                      'Each voice is distinguishable in the mix'],
        'citations': pack['cite'],
        'demo': {'kind': 'rhythm-grid', 'language': 'python', 'program': demo_program,
                 'note': 'Prints the 16-step grid, hit density, and per-beat breakdown.'},
        '_data': {'steps': steps, 'time_signature': pack['sig'], 'bpm': pack['bpm'], 'voices': pack['voices']},
    }

def render_factual(item, pack, rank):
    """pack: story[list paragraphs], specs[(k,v)], points[list], req[list],
             std[list], cite[list], demo_kind, demo_program, demo_note"""
    spec_lines = ['%s: %s' % (k, v) for k, v in pack['specs']]
    sub = list(pack['story']) + ['Key specifications — ' + '; '.join(spec_lines) + '.']
    return {
        'description': _paras(sub),
        'how_it_works': _paras(pack.get('how', [])),
        'key_points': pack['points'],
        'requirements': pack['req'],
        'standards': pack['std'],
        'citations': pack['cite'],
        'demo': {'kind': pack['demo_kind'], 'language': 'python',
                 'program': pack['demo_program'], 'note': pack['demo_note']},
        '_data': {'specifications': {k: v for k, v in pack['specs']}},
    }

RENDERERS = {'concept': render_concept, 'palette': render_palette,
             'steps': render_steps, 'factual': render_factual, 'guide': render_concept}

SIG_LEAD = ('Signature treatment — the Signature system takes this record further: '
            'every element is re-examined for what only this system can add, and the '
            'result is an original Signature expansion, clearly labeled, never presented '
            'as an authentic public record.')

def sig_wrap(rec, item, sig_points):
    rec = dict(rec)
    rec['description'] = SIG_LEAD + '\n' + rec['description']
    rec['key_points'] = list(rec['key_points']) + list(sig_points)
    rec['src'] = 'signature'
    rec.pop('sample', None)
    rec.pop('disclaimer', None)
    return rec

def make_record(item, pack, rank, sig, prefix):
    renderer = RENDERERS[item['renderer']]
    body = renderer(item, pack, rank)
    title = pack['t']
    field = pack['g']
    rec = {
        'id': '%s%06d' % (prefix, rank),
        't': title,
        'g': field,
        'name': title,
        'title': title,
        'description': body['description'],
        'how_it_works': body['how_it_works'],
        'key_points': body['key_points'],
        'requirements': body['requirements'],
        'standards': body['standards'],
        'citations': body['citations'],
        'src': 'signature-generated-sample' if item['cls'] == 'gen' else 'public-harvest',
        'ladder_rank': rank,
        'ladder_tier': field,
        'demo': body['demo'],
    }
    if body.get('_data'):
        rec['_render_data'] = body['_data']
    if item['cls'] == 'gen':
        rec['sample'] = True
        rec['disclaimer'] = 'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.'
    if sig:
        rec = sig_wrap(rec, item, pack.get('sig_points', [
            'Signature expansion: this record carries the Signature system treatment on top of the public knowledge.',
            'Cross-database aware: connects to sibling Signature databases in the network.',
        ]))
    return rec

# ---------------- demo runner ----------------
def run_demo(program, timeout=15):
    try:
        p = subprocess.run(['python3', '-c', program], capture_output=True,
                           text=True, timeout=timeout)
        return p.returncode == 0, (p.stdout + p.stderr)[-2000:]
    except Exception as e:
        return False, str(e)

# ---------------- content gates ----------------
BLOCKLIST = ['fuck', 'shit', 'bitch', ' bastard', 'slut', 'whore', 'nigger',
             'faggot', 'retard', 'kike', 'chink', 'spic', 'kill yourself',
             'suicide']
RELIGIOUS = ['\bgod\b', 'jesus', 'christ', '\ballah\b', 'bible', 'quran',
             'koran', 'torah', 'prayer', 'worship', 'holy ', 'sacred',
             'divine', 'scripture', 'prophet', 'messiah', 'church', 'mosque',
             'temple worship', 'blessed by']

def gate_scan(text, label):
    low = text.lower()
    hits = [w for w in BLOCKLIST if w in low]
    rel = [w for w in RELIGIOUS if re.search(w, low)]
    return hits, rel, label

# ---------------- page rendering ----------------
def render_page(item, sig):
    slug = item['slug'] + ('-signature' if sig else '')
    name = sig_name(item['name']) if sig else item['name']
    tagline = item['sig_tagline'] if sig and item.get('sig_tagline') else item['tagline']
    ai_name = item['ai_name'] + (' (Signature)' if sig else '')
    genver = 'jahdb-%s-1.0' % slug
    if item['cls'] == 'gen':
        typeline = 'Generator — real working client-side generator with seeded sample records'
        gendesc = item['gen_desc']
        aboutarch = ('Seeded generator sample records, marching toward one million records. '
                     'The client-side generator below produces genuine outputs; seeded samples are the authoritative entries.')
        aboutgen = '%s — %s' % (genver, item['gen_desc'])
        drift = 'Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.'
    elif sig:
        typeline = 'Signature originals — the Signature system\u2019s expanded treatment'
        gendesc = 'Generate clearly-labeled Signature studies. Seeded Signature records are the authoritative entries.'
        aboutarch = ('Seeded Signature-original records, marching toward one million records. '
                     'Clearly labeled Signature-made, never presented as authentic public record. '
                     'Presented in teaching-ladder order: %s.' % ', '.join(f.lower() for f in item['fields']))
        aboutgen = '%s — Generate clearly-labeled Signature studies. Seeded Signature records are the authoritative entries.' % genver
        drift = 'Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.'
    else:
        typeline = 'Public records organized in the Signature system'
        gendesc = 'Generate clearly-labeled studies. Seeded archive records are the authoritative entries.'
        aboutarch = ('Seeded public-record records, marching toward one million records. '
                     'Presented in teaching-ladder order: %s.' % ', '.join(f.lower() for f in item['fields']))
        aboutgen = '%s — Generate clearly-labeled studies. Seeded archive records are the authoritative entries.' % genver
        drift = 'Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.'
    hero = tagline + ' ' + item['hero_extra']
    fieldsline = ' \u00b7 '.join(item['fields']) + ' - each tier opens on demand and loads only what you open'
    greet = 'I am the %s. %s' % (ai_name, item['greet'])
    aiabout = '%s — %s — and aware of the whole JAH Databases network through cross-database reasoning. On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured.' % (ai_name, item['role'])
    sigsys = ('Signature originals, expanded in the Signature system. Property of Justin Addam Higgins (JAH).'
              if sig else 'Public records organized in the Signature system. Property of Justin Addam Higgins (JAH).')
    rep = {
        '%%NAME%%': name, '%%SLUG%%': slug, '%%TAGLINE%%': tagline,
        '%%HERO%%': hero, '%%GENVER%%': genver, '%%TYPELINE%%': typeline,
        '%%SEARCHPH%%': item['searchph'], '%%GENHEAD%%': '%s generator' % name,
        '%%GENDESC%%': gendesc, '%%ABOUTARCH%%': aboutarch,
        '%%SCHEMA%%': 'id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo',
        '%%FIELDSLINE%%': fieldsline, '%%ABOUTGEN%%': aboutgen,
        '%%DRIFT%%': drift, '%%AINAME%%': ai_name, '%%CHATPH%%': item['chatph'],
        '%%GREET%%': greet, '%%ROLE%%': item['role'], '%%RECORDKIND%%': item['record_kind'],
        '%%AIABOUT%%': aiabout, '%%SIGSYS%%': sigsys,
        '%%FOOT%%': 'JAH Databases. ' + sigsys,
        '%%GENJS%%': 'gen-%s.js' % slug, '%%EMBLEMPREFIX%%': "'JAH-SI-'",
    }
    out = TEMPLATE
    for k, v in rep.items():
        out = out.replace(k, v)
    assert '%%' not in out, 'unreplaced token in page for %s' % slug
    return out

# ---------------- db-class generator JS ----------------
DB_GENJS_TMPL = """(function(){'use strict';
/* JAH %s generator — %s.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="%s";
var FIELDS=%s;
var TOPICS=%s;
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "# %s — "+safe+"\\n"
   + "# Field: "+field+"\\n"
   + "record = {'title': \\""+safe+"\\", 'field': \\""+field+"\\"}\\n"
   + "def summarize(r):\\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\\n"
   + "print(summarize(record))\\n"
   + "print('Sample record — structural sample, not an archive entry.')\\n";
}
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
    demo:{kind:"%s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'%s',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('%s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

def genjs_db(item, sig):
    slug = item['slug'] + ('-signature' if sig else '')
    prefix = sig_prefix(item['prefix']) if sig else item['prefix']
    topics = {}
    for t in item['topics']:
        topics.setdefault(t['g'], []).append(t['t'])
    return DB_GENJS_TMPL % (
        item['name'], 'jahdb-%s-1.0' % slug, prefix,
        json.dumps(item['fields']), json.dumps(topics, indent=1),
        item['short'],
        item['record_kind'], item['record_kind'], item['short'],
        'jahdb-%s-1.0' % slug, slug)

# ---------------- data + manifest writers ----------------
def write_data(slug, records):
    ddir = os.path.join(DATA_ROOT, slug)
    cdir = os.path.join(ddir, 'chunks')
    os.makedirs(cdir, exist_ok=True)
    slim = [{'id': r['id'], 't': r['t'], 'g': r['g']} for r in records]
    with gzip.open(os.path.join(ddir, 'index.jsonl.gz'), 'wt', encoding='utf-8') as f:
        for r in slim:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    clean = []
    for r in records:
        r = dict(r)
        r.pop('_render_data', None)
        clean.append(r)
    with gzip.open(os.path.join(cdir, 'chunk-0000.jsonl.gz'), 'wt', encoding='utf-8') as f:
        for r in clean:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    return ddir

def write_page(slug, html_text, genjs_text):
    pdir = os.path.join(PAGES_ROOT, slug)
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_text)
    with open(os.path.join(pdir, 'gen-%s.js' % slug), 'w', encoding='utf-8') as f:
        f.write(genjs_text)
    return pdir

def manifest_entry(item, sig):
    slug = item['slug'] + ('-signature' if sig else '')
    prefix = sig_prefix(item['prefix']) if sig else item['prefix']
    name = sig_name(item['name']) if sig else item['name']
    tagline = item['sig_tagline'] if sig and item.get('sig_tagline') else item['tagline']
    ai_name = item['ai_name'] + (' (Signature)' if sig else '')
    if sig:
        source = 'signature'
    elif item['cls'] == 'gen':
        source = 'signature-generated-sample'
    else:
        source = 'public-harvest'
    return {
        'slug': slug, 'name': name, 'tagline': tagline,
        'record_kind': item['record_kind'], 'id_prefix': prefix,
        'ai_name': ai_name,
        'local_index': 'data/%s/index.jsonl.gz' % slug,
        'page_url': 'db/%s/' % slug,
        'index': 'data/%s/index.jsonl.gz' % slug,
        'chunk_pattern': 'data/%s/chunks/chunk-NNNN.jsonl.gz' % slug,
        'source': source, 'record_count': 34, 'full_records': 34,
        'status': 'staged',
    }

def node_check(path):
    p = subprocess.run(['node', '--check', path], capture_output=True, text=True)
    return p.returncode == 0, p.stderr[-500:]

def node_functional_test(path):
    """Load gen module, run generate/validate/driftCheck on several seeds."""
    harness = (
        "var g=require(%s);var F=g.fields||[];"
        "var out=[];"
        "for(var s=1;s<=6;s++){var r=g.generate(s,{});var v=g.validate(r);"
        "if(!v.ok)throw new Error('validate failed seed '+s+': '+v.errors.join(','));"
        "if(!r.demo||!r.demo.program)throw new Error('no demo program seed '+s);"
        "out.push(r.id);}"
        "for(var i=0;i<F.length;i++){var r2=g.generate(100+i,{field:F[i]});var v2=g.validate(r2);"
        "if(!v2.ok)throw new Error('field validate failed '+F[i]);"
        "if(r2.field!==F[i])throw new Error('field mismatch '+F[i]);}"
        "var d=g.driftCheck(g.generate(7,{}),[g.generate(7,{})]);"
        "if(d.ok)throw new Error('driftCheck should flag duplicate');"
        "console.log('OK '+out.join(','));"
    ) % json.dumps(path)
    p = subprocess.run(['node', '-e', harness], capture_output=True, text=True, timeout=60)
    return p.returncode == 0, (p.stdout + p.stderr)[-800:]
