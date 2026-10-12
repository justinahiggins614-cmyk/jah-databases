/* ✳ SIGNATURE — ComicArt: HD cover art for the JAH Comic Data Base.
   Property of Justin Addam Higgins (JAH).

   Two art sources, one rule — real painted cover if the record has one,
   otherwise a deterministic comic-style SVG cover:
   1) REAL: 29 painted covers harvested from the comic store (9 series covers
      + 20 hero portraits), matched by series key / hero code to their
      flagship issue in the archive index.
   2) GENERATED: ComicArt.generate(comic) -> deterministic 400x600 SVG in
      classic comic-cover style: bold black inks, Ben-Day halftone dots,
      speed lines, explosive shapes, comic typography. Same record id =>
      same cover, every time, on every device. */
(function () {
  'use strict';

  var COVER_BASE = 'https://justinahiggins614-cmyk.github.io/jah-databases-comics-shard-1/data/comics/covers/';

  /* series key -> painted series cover (covers the series' flagship issue) */
  var SERIES_COVERS = {
    signal: 'cover-signal.jpg', ember: 'cover-ember.jpg', circuit: 'cover-circuit.jpg',
    tide: 'cover-tide.jpg', gloam: 'cover-gloam.jpg', starlog: 'cover-starlog.jpg',
    clockwork: 'cover-clockwork.jpg', junior: 'cover-junior.jpg', event: 'cover-event.jpg'
  };
  /* hero code -> painted hero portrait (covers the first issue starring them) */
  var HERO_COVERS = {
    'BASTION': 'portrait-bastion.jpg', 'SWIFTSURE': 'portrait-swiftsure.jpg',
    'NIGHTWARDEN': 'portrait-nightwarden.jpg', 'STRANDLINE': 'portrait-strandline.jpg',
    'THE KINDRED': 'portrait-kindred.jpg', 'STARWARDEN': 'portrait-starwarden.jpg',
    'PLATEFORGE': 'portrait-plateforge.jpg', 'RUNESAYER': 'portrait-runesayer.jpg',
    'SHIELDMAIDEN SABLE': 'portrait-sable.jpg', 'PRISMWARD': 'portrait-prismward.jpg',
    'PLIANT': 'portrait-pliant.jpg', 'MAGNITUDE': 'portrait-magnitude.jpg',
    'TIDECROWN': 'portrait-tidecrown.jpg', 'GALEFORGE': 'portrait-galeforge.jpg',
    'UMBRASTEP': 'portrait-umbrastep.jpg', 'BRIARCLAW': 'portrait-briarclaw.jpg',
    'VOIDHERALD': 'portrait-voidherald.jpg', 'MOUNTAINHEART': 'portrait-mountainheart.jpg',
    'SPROCKET': 'portrait-sprocket.jpg', 'KINGSWARD': 'portrait-kingsward.jpg'
  };

  /* ---- deterministic hashing / PRNG ---- */
  function hashStr(s) {
    var h = 2166136261 >>> 0;
    s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function mulberry(seed) {
    var a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function field(r, full, compact) {
    if (r == null) return '';
    if (r[full] != null) return r[full];
    return r[compact] != null ? r[compact] : '';
  }
  function recId(r) { return String(field(r, 'id', 'id') || 'JAH-COMIC-?'); }

  /* ---- real-art map: record id -> cover file (29 flagship records) ---- */
  function buildRealMap(idxRows) {
    var map = {}, seenSeries = {}, seenHero = {};
    var rows = idxRows || [];
    /* pass 1: each series' flagship (lowest id) gets its painted cover */
    rows.forEach(function (r) {
      var id = r.id, sk = String(r.sk || r.skey || '').toLowerCase();
      if (id && sk && SERIES_COVERS[sk] && !seenSeries[sk]) {
        seenSeries[sk] = 1; map[id] = SERIES_COVERS[sk];
      }
    });
    /* pass 2: each portrait hero -> an issue starring them that is not already
       carrying art. Rarest heroes pick first so all 29 covers land on
       29 distinct records. */
    var cands = {};
    Object.keys(HERO_COVERS).forEach(function (h) { cands[h] = []; });
    rows.forEach(function (r) {
      if (!r.id || map[r.id]) return;
      var chs = r.ch || r.chars || [], seen = {};
      for (var i = 0; i < chs.length; i++) {
        var code = String(chs[i] && chs[i].code || '').toUpperCase();
        if (code && cands[code] && !seen[code]) { seen[code] = 1; cands[code].push(r.id); }
      }
    });
    Object.keys(cands).sort(function (a, b) { return cands[a].length - cands[b].length; })
      .forEach(function (h) {
        var list = cands[h];
        for (var i = 0; i < list.length; i++) {
          if (!map[list[i]]) { map[list[i]] = HERO_COVERS[h]; return; }
        }
      });
    return map;
  }
  function realURL(id, realMap) {
    var f = realMap && realMap[id];
    return f ? COVER_BASE + f : null;
  }

  /* ---- comic-cover palettes: [hot, pop, deep] ---- */
  var PALETTES = [
    ['#e6392b', '#ffd21f', '#101d3a'], /* classic red/yellow/navy   */
    ['#1f6fd6', '#ff7a1a', '#0e1b36'], /* blue/orange                */
    ['#7b2ff2', '#2ee6a8', '#170b2e'], /* purple/mint                */
    ['#0aa6a6', '#ff3d6e', '#0b2030'], /* teal/crimson               */
    ['#d63df2', '#ffd21f', '#241031'], /* magenta/yellow             */
    ['#ff5a1f', '#3a86ff', '#221006'], /* ember/blue                 */
    ['#22b14c', '#fff200', '#0d2417'], /* green/yellow               */
    ['#ff2e63', '#08d9d6', '#1c0b16']  /* hot pink/cyan              */
  ];
  var SFX = ['KRAKOOM!', 'WHAM!', 'ZAP!', 'BOOM!', 'KRAK!', 'POW!', 'THOOM!', 'SKREE!'];
  var MOTIFS = ['hero', 'blast', 'city', 'cosmos', 'tide', 'flames', 'gears', 'panels'];
  /* series affinity: which motifs suit each series key */
  var AFFIN = {
    signal: ['city', 'hero', 'blast'], ember: ['flames', 'blast', 'hero'],
    circuit: ['blast', 'gears', 'city'], tide: ['tide', 'hero', 'cosmos'],
    gloam: ['cosmos', 'city', 'panels'], starlog: ['cosmos', 'blast', 'hero'],
    clockwork: ['gears', 'city', 'panels'], junior: ['hero', 'panels', 'blast'],
    event: ['blast', 'cosmos', 'hero']
  };

  /* ---- SVG helpers ---- */
  function burst(cx, cy, r1, r2, n, rot, fill, stroke, sw) {
    var pts = [];
    for (var i = 0; i < n * 2; i++) {
      var a = rot + (Math.PI * i) / n, rr = (i % 2 === 0) ? r1 : r2;
      pts.push((cx + rr * Math.cos(a)).toFixed(1) + ',' + (cy + rr * Math.sin(a)).toFixed(1));
    }
    return '<polygon points="' + pts.join(' ') + '" fill="' + fill + '"' +
      (stroke ? ' stroke="' + stroke + '" stroke-width="' + sw + '"' : '') + '/>';
  }
  function speedLines(u, cx, cy, rnd, color, n, rMin, rMax) {
    var s = '';
    for (var i = 0; i < n; i++) {
      var a = rnd() * Math.PI * 2, w = 1 + rnd() * 3.5;
      var x1 = cx + rMin * Math.cos(a), y1 = cy + rMin * Math.sin(a);
      var x2 = cx + (rMin + rnd() * (rMax - rMin)) * Math.cos(a);
      var y2 = cy + (rMin + rnd() * (rMax - rMin)) * Math.sin(a);
      s += '<line x1="' + x1.toFixed(0) + '" y1="' + y1.toFixed(0) + '" x2="' + x2.toFixed(0) +
        '" y2="' + y2.toFixed(0) + '" stroke="' + color + '" stroke-width="' + w.toFixed(1) +
        '" opacity="0.55" stroke-linecap="round"/>';
    }
    return s;
  }
  /* caped hero silhouette, lunging right, cape billowing left */
  function heroFigure(cx, cy, s, suit, cape, rim) {
    return '<g transform="translate(' + cx + ',' + cy + ') scale(' + s + ')">' +
      '<path d="M10,-95 C-60,-90 -110,-60 -150,-30 C-110,-25 -70,-20 -30,-28 C-70,-5 -100,30 -115,70 C-70,55 -30,40 5,45 C-15,70 -20,95 -18,120 L30,120 C28,90 30,65 38,45 C70,40 100,30 125,15 C95,5 60,-5 30,-12 C55,-35 60,-65 50,-95 Z" fill="' + cape + '" stroke="#000" stroke-width="7"/>' +
      '<circle cx="78" cy="-78" r="26" fill="' + suit + '" stroke="#000" stroke-width="7"/>' +
      '<path d="M62,-78 L94,-78 L86,-70 Z" fill="' + rim + '"/>' +
      '<path d="M58,-52 C40,-30 30,-5 28,25 L95,30 C95,0 92,-28 100,-50 Z" fill="' + suit + '" stroke="#000" stroke-width="7"/>' +
      '<path d="M28,25 L95,30 L110,95 L60,105 Z" fill="' + suit + '" stroke="#000" stroke-width="7"/>' +
      '<path d="M28,25 L60,105 L20,140 L-5,95 Z" fill="' + suit + '" stroke="#000" stroke-width="7"/>' +
      '<path d="M95,30 L150,-10 L165,8 L108,48 Z" fill="' + suit + '" stroke="#000" stroke-width="7"/>' +
      '<circle cx="165" cy="2" r="13" fill="' + suit + '" stroke="#000" stroke-width="6"/>' +
      '<path d="M58,-52 L20,-30 L28,-12 L62,-28 Z" fill="' + suit + '" stroke="#000" stroke-width="7"/>' +
      '<circle cx="14" cy="-22" r="12" fill="' + suit + '" stroke="#000" stroke-width="6"/>' +
      '<path d="M60,55 L118,62" stroke="' + rim + '" stroke-width="5" opacity="0.9"/>' +
      '</g>';
  }
  function gearShape(cx, cy, r, teeth, fill) {
    var s = '<g transform="translate(' + cx + ',' + cy + ')">';
    for (var i = 0; i < teeth; i++) {
      s += '<rect x="' + (-r * 0.16) + '" y="' + (-r * 1.28) + '" width="' + (r * 0.32) + '" height="' + (r * 0.42) +
        '" fill="' + fill + '" stroke="#000" stroke-width="4" transform="rotate(' + (360 * i / teeth) + ')"/>';
    }
    s += '<circle r="' + r + '" fill="' + fill + '" stroke="#000" stroke-width="6"/>' +
      '<circle r="' + (r * 0.42) + '" fill="#0a0f1e" stroke="#000" stroke-width="5"/>' +
      '<circle r="' + (r * 0.16) + '" fill="' + fill + '"/></g>';
    return s;
  }

  /* ================= the generator ================= */
  function generate(comic) {
    var id = recId(comic);
    var seed = hashStr(id);
    var rnd = mulberry(seed);
    var u = 'c' + (seed % 1294967296).toString(36);
    var pal = PALETTES[Math.floor(rnd() * PALETTES.length)];
    var hot = pal[0], pop = pal[1], deep = pal[2];
    var title = String(field(comic, 'title', 't') || 'UNTITLED').toUpperCase();
    var series = String(field(comic, 'series', 's') || 'JAH COMICS').toUpperCase();
    var sk = String(field(comic, 'skey', 'sk') || '').toLowerCase();
    var num = field(comic, 'num', 'n') || '?';
    var words = field(comic, 'words', 'w') || '';
    var chars = field(comic, 'chars', 'ch') || [];
    var starLine = chars.slice(0, 3).map(function (c) { return String(c.code || c.name || '').toUpperCase(); })
      .filter(Boolean).join(' • ');

    /* motif: series affinity 2/3 of the time, pure hash otherwise */
    var pool = AFFIN[sk] || MOTIFS;
    var motif = rnd() < 0.67 ? pick(rnd, pool) : pick(rnd, MOTIFS);
    var sfx = pick(rnd, SFX);
    var focalX = 200, focalY = 235;

    var s = '';
    /* --- base: deep field + halftone dots --- */
    s += '<defs>' +
      '<radialGradient id="bg' + u + '" cx="50%" cy="38%" r="80%">' +
      '<stop offset="0%" stop-color="' + hot + '"/><stop offset="55%" stop-color="' + deep + '"/>' +
      '<stop offset="100%" stop-color="#05070f"/></radialGradient>' +
      '<pattern id="ht' + u + '" width="13" height="13" patternUnits="userSpaceOnUse">' +
      '<circle cx="4" cy="4" r="2.6" fill="#000" opacity="0.38"/></pattern>' +
      '<pattern id="ht2' + u + '" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(18)">' +
      '<circle cx="6" cy="6" r="3.4" fill="' + pop + '" opacity="0.30"/></pattern>' +
      '</defs>';
    s += '<rect width="400" height="600" fill="url(#bg' + u + ')"/>';
    s += '<rect width="400" height="600" fill="url(#ht' + u + ')"/>';

    /* --- motif art --- */
    if (motif === 'hero') {
      s += burst(200, 240, 235, 120, 18, rnd() * 0.4, pop, '#000', 5);
      s += '<rect width="400" height="600" fill="url(#ht2' + u + ')" opacity="0.5"/>';
      s += speedLines(u, 200, 240, rnd, '#000', 26, 130, 260);
      s += heroFigure(185, 300, 1.05, hot, deep === '#101d3a' ? '#0a1330' : '#0a0f1e', pop);
      s += '<g transform="translate(292,150) rotate(14)">' + burst(0, 0, 74, 46, 12, 0, '#fff', '#000', 5) +
        '<text x="0" y="12" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-style="italic" font-size="26" fill="' + hot + '" stroke="#000" stroke-width="1.5">' + esc(sfx) + '</text></g>';
    } else if (motif === 'blast') {
      s += '<rect width="400" height="600" fill="url(#ht2' + u + ')" opacity="0.6"/>';
      s += burst(200, 250, 260, 150, 20, 0.2, hot, '#000', 6);
      s += burst(200, 250, 190, 105, 16, 0.5, pop, '#000', 5);
      s += burst(200, 250, 120, 62, 12, 0.1, '#fff', '#000', 5);
      s += speedLines(u, 200, 250, rnd, '#fff', 18, 90, 220);
      s += '<text x="200" y="272" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-style="italic" font-size="52" fill="' + deep + '" stroke="#fff" stroke-width="2" transform="rotate(-6 200 250)">' + esc(sfx) + '</text>';
    } else if (motif === 'city') {
      s += '<circle cx="310" cy="120" r="52" fill="' + pop + '" stroke="#000" stroke-width="5"/>';
      s += '<rect width="400" height="600" fill="url(#ht2' + u + ')" opacity="0.45"/>';
      var bx = 8;
      while (bx < 400) {
        var bw = ri(rnd, 34, 62), bh = ri(rnd, 130, 260), by = 470 - bh;
        s += '<rect x="' + bx + '" y="' + by + '" width="' + bw + '" height="' + bh + '" fill="#0a0f1e" stroke="#000" stroke-width="5"/>';
        for (var wy = by + 14; wy < 452; wy += 26) for (var wx = bx + 8; wx < bx + bw - 8; wx += 18) {
          if (rnd() < 0.55) s += '<rect x="' + wx + '" y="' + wy + '" width="9" height="12" fill="' + pop + '" opacity="0.85"/>';
        }
        bx += bw + ri(rnd, 4, 14);
      }
      s += '<polygon points="200,470 130,180 270,180" fill="' + pop + '" opacity="0.28"/>';
      s += '<rect x="0" y="470" width="400" height="130" fill="#05070f" stroke="#000" stroke-width="5"/>';
      s += '<rect x="60" y="440" width="280" height="10" fill="' + hot + '" stroke="#000" stroke-width="3"/>';
      s += heroFigure(200, 470, 0.5, '#0a0f1e', '#0a0f1e', pop);
    } else if (motif === 'cosmos') {
      for (var st = 0; st < 60; st++) {
        s += '<circle cx="' + (rnd() * 400).toFixed(0) + '" cy="' + (rnd() * 470).toFixed(0) + '" r="' + (0.8 + rnd() * 2.2).toFixed(1) + '" fill="#fff" opacity="' + (0.4 + rnd() * 0.6).toFixed(2) + '"/>';
      }
      s += '<circle cx="200" cy="220" r="105" fill="' + hot + '" stroke="#000" stroke-width="7"/>';
      s += '<circle cx="200" cy="220" r="105" fill="url(#ht' + u + ')" opacity="0.5"/>';
      s += '<ellipse cx="200" cy="220" rx="168" ry="42" fill="none" stroke="' + pop + '" stroke-width="13" transform="rotate(-16 200 220)"/>';
      s += '<ellipse cx="200" cy="220" rx="168" ry="42" fill="none" stroke="#000" stroke-width="18" transform="rotate(-16 200 220)" opacity="0.35"/>';
      s += '<path d="M96,420 q60,-46 208,-30" stroke="' + pop + '" stroke-width="7" fill="none" opacity="0.8"/>';
      s += '<path d="M120,455 q70,-40 180,-26" stroke="' + hot + '" stroke-width="5" fill="none" opacity="0.7"/>';
      s += '<polygon points="316,96 330,128 364,132 336,152 344,186 316,168 288,186 296,152 268,132 302,128" fill="' + pop + '" stroke="#000" stroke-width="4"/>';
    } else if (motif === 'tide') {
      for (var wv = 0; wv < 4; wv++) {
        var wyy = 190 + wv * 78, amp = 60 - wv * 8;
        s += '<path d="M-20,' + wyy + ' q60,-' + amp + ' 120,0 t120,0 t120,0 t60,-' + (amp / 2) +
          ' L420,620 L-20,620 Z" fill="' + (wv % 2 ? hot : '#1f6fd6') + '" stroke="#000" stroke-width="6" opacity="' + (0.95 - wv * 0.12).toFixed(2) + '"/>';
      }
      s += '<rect width="400" height="600" fill="url(#ht2' + u + ')" opacity="0.4"/>';
      for (var fb = 0; fb < 26; fb++) {
        s += '<circle cx="' + (rnd() * 400).toFixed(0) + '" cy="' + (170 + rnd() * 300).toFixed(0) + '" r="' + (2 + rnd() * 6).toFixed(1) + '" fill="#fff" opacity="0.8" stroke="#000" stroke-width="2"/>';
      }
      s += '<g transform="translate(110,150) rotate(-12)">' + burst(0, 0, 66, 40, 12, 0, '#fff', '#000', 5) +
        '<text x="0" y="11" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-style="italic" font-size="24" fill="#1f6fd6" stroke="#000" stroke-width="1.2">' + esc(sfx) + '</text></g>';
    } else if (motif === 'flames') {
      for (var fl = 0; fl < 7; fl++) {
        var fx = 40 + fl * 48, fh = ri(rnd, 200, 380), fw2 = ri(rnd, 40, 64);
        s += '<path d="M' + fx + ',520 C' + (fx - fw2) + ',420 ' + (fx + fw2) + ',380 ' + (fx - 10) + ',' + (520 - fh) +
          ' C' + (fx + fw2) + ',' + (520 - fh + 90) + ' ' + (fx - fw2) + ',' + (520 - fh + 150) + ' ' + fx + ',520 Z" fill="' +
          (fl % 2 ? hot : pop) + '" stroke="#000" stroke-width="6" opacity="0.95"/>';
      }
      s += '<rect width="400" height="600" fill="url(#ht' + u + ')" opacity="0.55"/>';
      for (var sp = 0; sp < 24; sp++) {
        s += '<circle cx="' + (rnd() * 400).toFixed(0) + '" cy="' + (rnd() * 420).toFixed(0) + '" r="' + (1.5 + rnd() * 3.5).toFixed(1) + '" fill="' + pop + '" stroke="#000" stroke-width="1.5"/>';
      }
      s += heroFigure(210, 430, 0.85, '#14100c', '#1d1410', hot);
    } else if (motif === 'gears') {
      s += '<rect width="400" height="600" fill="url(#ht2' + u + ')" opacity="0.55"/>';
      s += burst(200, 250, 240, 130, 18, 0.3, '#0a0f1e', '#000', 5);
      s += gearShape(140, 210, 78, 10, hot);
      s += gearShape(272, 300, 96, 12, pop);
      s += gearShape(150, 400, 52, 8, '#8a93ad');
      s += '<circle cx="272" cy="300" r="30" fill="' + deep + '" stroke="#000" stroke-width="5"/>';
      s += speedLines(u, 272, 300, rnd, pop, 14, 110, 200);
    } else { /* panels: 3-panel strip */
      var py = [96, 236, 376], ph = [128, 128, 128];
      for (var pn = 0; pn < 3; pn++) {
        s += '<rect x="28" y="' + py[pn] + '" width="344" height="' + ph[pn] + '" fill="' + (pn % 2 ? pop : '#f4f1e6') + '" stroke="#000" stroke-width="7"/>';
        s += '<rect x="28" y="' + py[pn] + '" width="344" height="' + ph[pn] + '" fill="url(#ht' + u + ')" opacity="0.35"/>';
      }
      s += burst(120, 160, 66, 34, 12, 0.2, hot, '#000', 4);
      s += heroFigure(250, 218, 0.42, '#0a0f1e', '#0a0f1e', hot);
      s += '<rect x="48" y="330" width="308" height="18" fill="#000"/>';
      s += '<rect x="48" y="356" width="220" height="14" fill="#000" opacity="0.75"/>';
      s += '<rect x="48" y="376" width="264" height="14" fill="#000" opacity="0.55"/>';
      s += '<g transform="translate(310,438) rotate(10)">' + burst(0, 0, 56, 34, 10, 0, hot, '#000', 4) +
        '<text x="0" y="9" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-style="italic" font-size="20" fill="#fff">' + esc(sfx) + '</text></g>';
    }

    /* --- top series banner (font shrinks to fit long series names) --- */
    var bfs = series.length > 14 ? Math.max(13, Math.floor(330 / (series.length * 0.72))) : 24;
    s += '<g transform="rotate(-3 200 60)"><rect x="30" y="34" width="340" height="40" fill="#000"/>' +
      '<rect x="34" y="30" width="340" height="40" fill="' + pop + '" stroke="#000" stroke-width="4"/>' +
      '<text x="204" y="59" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-size="' + bfs + '" letter-spacing="2" fill="#000">' + esc(series.slice(0, 26)) + '</text></g>';
    /* --- classic corner box --- */
    s += '<g><rect x="10" y="88" width="64" height="64" fill="#fff" stroke="#000" stroke-width="5"/>' +
      '<text x="42" y="114" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-size="22" fill="' + hot + '">JAH</text>' +
      '<text x="42" y="138" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-size="17" fill="#000">#' + esc(String(num)).slice(0, 6) + '</text></g>';
    s += '<g transform="rotate(6 360 100)"><rect x="322" y="88" width="62" height="30" fill="' + hot + '" stroke="#000" stroke-width="4"/>' +
      '<text x="353" y="110" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-size="17" fill="#fff">HD</text></g>';

    /* --- title block: explosive caption over the art --- */
    var wordsArr = title.split(/\s+/);
    var lines = [], cur = '';
    wordsArr.forEach(function (w) {
      if ((cur + ' ' + w).trim().length > 13) { if (cur) lines.push(cur); cur = w; }
      else cur = (cur + ' ' + w).trim();
    });
    if (cur) lines.push(cur);
    lines = lines.slice(0, 3);
    var fs = lines.length > 2 ? 34 : 40;
    var ty = 470;
    s += burst(200, ty + 6, 205, 150, 14, 0.15, '#000', null, 0);
    s += burst(200, ty + 6, 188, 138, 14, 0.15, '#fff', '#000', 5);
    lines.forEach(function (ln, i) {
      s += '<text x="200" y="' + (ty - (lines.length - 1) * fs * 0.55 + i * fs * 1.02) +
        '" text-anchor="middle" font-family="Arial Black,Impact,sans-serif" font-weight="900" font-style="italic" font-size="' + fs +
        '" fill="' + hot + '" stroke="#000" stroke-width="2" paint-order="stroke" transform="rotate(-3 200 ' + ty + ')">' +
        esc(ln.slice(0, 18)) + '</text>';
    });

    /* --- bottom strip (runs to the page edge; the frame draws over it) --- */
    s += '<rect x="0" y="548" width="400" height="52" fill="#000"/>';
    s += '<text x="200" y="565" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="13" letter-spacing="1.5" fill="' + pop + '">JAH COMICS • FULL ISSUE' + (words ? ' • ' + words + ' WORDS' : '') + '</text>';
    if (starLine) s += '<text x="200" y="582" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="11" letter-spacing="1" fill="#9fb3d8">STARRING: ' + esc(starLine.slice(0, 52)) + '</text>';

    /* --- cover frame --- */
    s += '<rect x="4" y="4" width="392" height="592" fill="none" stroke="#000" stroke-width="9"/>';
    s += '<rect x="14" y="14" width="372" height="572" fill="none" stroke="#fff" stroke-width="2" opacity="0.85"/>';

    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="400" height="600" role="img" aria-label="' +
      esc(title) + ' comic cover">' + s + '</svg>';
  }

  function svgURI(svg) {
    return 'data:image/svg+xml,' + encodeURIComponent(svg)
      .replace(/'/g, '%27').replace(/\(/g, '%28').replace(/\)/g, '%29');
  }

  /* img tag: real painted cover when mapped (falls back to generated art
     if the file ever fails to load), otherwise the generated cover. */
  function imgTag(rec, realMap, cls, alt) {
    var id = recId(rec);
    var url = realURL(id, realMap);
    var genURI = svgURI(generate(rec));
    var a = esc((alt || field(rec, 'title', 't') || id) + ' cover art');
    if (url) {
      return '<img loading="lazy" class="' + cls + '" src="' + url + '" alt="' + a + '"' +
        ' onerror="this.onerror=null;this.src=\'' + genURI.replace(/'/g, '%27') + '\'">';
    }
    return '<img loading="lazy" class="' + cls + '" src="' + genURI + '" alt="' + a + '">';
  }
  function artKind(rec, realMap) {
    return realURL(recId(rec), realMap) ? 'real' : 'generated';
  }

  window.ComicArt = {
    COVER_BASE: COVER_BASE,
    SERIES_COVERS: SERIES_COVERS,
    HERO_COVERS: HERO_COVERS,
    buildRealMap: buildRealMap,
    realURL: realURL,
    generate: generate,
    svgURI: svgURI,
    imgTag: imgTag,
    artKind: artKind,
    hashStr: hashStr
  };
})();
