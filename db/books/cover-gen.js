/* SIGNATURE — JAH Book Database deterministic cover engine.
   BookCover.generate(book) -> SVG string (400x600). Pure function of book.id:
   same id => byte-identical cover, in every browser and in node. 16 genres x
   4 palettes x 6 motifs x 4 layouts = 1536 deterministic combinations.
   Book record fields used: id, title (or t), author, genre (or g), gkey. */
var BookCover = (function () {
  'use strict';
  var W = 400, H = 600;

  /* ---------- deterministic primitives ---------- */
  function fnv(s) {
    var h = 2166136261; s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function mulberry(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function esc(s) {
    return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function rf(rnd, a, b) { return a + rnd() * (b - a); }
  function fmt(n) { return (Math.round(n * 10) / 10).toString(); }

  /* ---------- genre key ---------- */
  var GKEYS = {
    'science fiction': 'sf', 'fantasy': 'fantasy', 'mystery': 'mystery',
    'romance': 'romance', 'horror': 'horror', 'mathematics': 'math',
    'physics': 'physics', 'chemistry': 'chemistry', 'biology': 'biology',
    'history': 'history', 'computer science': 'cs', "children's": 'children',
    'children': 'children', 'poetry': 'poetry', 'technical manual': 'manual',
    'philosophy': 'philosophy', 'business': 'business'
  };
  var GLABEL = {
    sf: 'Science Fiction', fantasy: 'Fantasy', mystery: 'Mystery', romance: 'Romance',
    horror: 'Horror', math: 'Mathematics', physics: 'Physics', chemistry: 'Chemistry',
    biology: 'Biology', history: 'History', cs: 'Computer Science', children: "Children's",
    poetry: 'Poetry', manual: 'Technical Manual', philosophy: 'Philosophy', business: 'Business'
  };

  /* ---------- palettes: 4 per genre [bg1, bg2, fg, accent, accent2, muted] ---------- */
  var PAL = {
    sf: [
      ['#05070f', '#0d1b2e', '#e8f1ff', '#4fd8ff', '#b46bff', '#7fa3c8'],
      ['#0b0014', '#1d0a33', '#f2e9ff', '#b46bff', '#4fd8ff', '#8f7fb8'],
      ['#001318', '#013a3f', '#e6fffa', '#2ee6a8', '#4fd8ff', '#6fa8a0'],
      ['#12060a', '#3a0f1d', '#ffe9d6', '#ff7a3d', '#ffd166', '#b88a6a']],
    fantasy: [
      ['#0d1f16', '#1d4d33', '#f3e9c8', '#d4af37', '#a3e635', '#9db89a'],
      ['#160a24', '#3b1a5e', '#efe3ff', '#c9a227', '#b46bff', '#a58fc9'],
      ['#0a1a2e', '#143b63', '#e7f0ff', '#58c4dc', '#d4af37', '#8aa3c2'],
      ['#220d12', '#5e1a26', '#ffe6cf', '#e8b04b', '#ff7a5e', '#c49a8a']],
    mystery: [
      ['#07090d', '#141a24', '#dfe6ee', '#c0392b', '#d4af37', '#6b7a8d'],
      ['#0a0d12', '#1c2733', '#e8edf3', '#d4af37', '#8a97a5', '#7d8fa3'],
      ['#05070a', '#101418', '#cfd6dd', '#8a97a5', '#c0392b', '#5a6672'],
      ['#0d0a08', '#241a12', '#f0e6d2', '#b3541e', '#d4af37', '#93826a']],
    romance: [
      ['#2b0f16', '#6e2233', '#ffeef2', '#ff9db4', '#ffd166', '#c98a96'],
      ['#fff3e8', '#f6d9c0', '#5e2b1a', '#c0392b', '#b3541e', '#a97c5f'],
      ['#1d0b12', '#4a1530', '#ffe3ec', '#e86a92', '#ffb3c6', '#b98aa0'],
      ['#3a1c0d', '#7a3f16', '#fff0dd', '#ffb347', '#ff7a5e', '#d3a06f']],
    horror: [
      ['#030304', '#141216', '#e8e4da', '#a4161a', '#5e5e5e', '#6e6a63'],
      ['#060a06', '#14210f', '#e2e8d5', '#8fa31f', '#a4161a', '#6f7a5a'],
      ['#0a0508', '#221016', '#f0dfe4', '#c1121f', '#8a97a5', '#9a7a82'],
      ['#020202', '#101010', '#d6d6d6', '#5e5e5e', '#a4161a', '#4a4a4a']],
    math: [
      ['#10231c', '#1d3a2e', '#f4f1e6', '#ffd166', '#7fd4ff', '#9db8a4'],
      ['#0c1a2b', '#1c3a5e', '#eaf2fb', '#7fd4ff', '#ffd166', '#8fa9c4'],
      ['#1a1a1a', '#33302a', '#f5f2ea', '#e07a5f', '#ffd166', '#a8a29a'],
      ['#f5f2ea', '#e3dccb', '#1f2937', '#b3541e', '#0a4d8c', '#8a7f6a']],
    physics: [
      ['#050914', '#0f2140', '#eaf4ff', '#4cc9f0', '#f72585', '#8298b8'],
      ['#0d0616', '#2b1245', '#f3ecff', '#f72585', '#4cc9f0', '#a58fc9'],
      ['#00100c', '#06302a', '#e6fff8', '#80ffdb', '#ffd166', '#6fa89b'],
      ['#140b02', '#3d2408', '#ffedd8', '#ffb703', '#ff7a3d', '#c49a6a']],
    chemistry: [
      ['#0a1410', '#1c3a2c', '#eefbef', '#95d5b2', '#ffd166', '#7fa08a'],
      ['#120e04', '#3a2c0c', '#fff6dd', '#ffb703', '#ff6b5e', '#c4a96a'],
      ['#0b0f1a', '#1d2a4a', '#e8efff', '#6cb2f5', '#95d5b2', '#8a9cc4'],
      ['#160607', '#3d1215', '#ffe9e4', '#ff6b5e', '#ffb703', '#c49a92']],
    biology: [
      ['#0a1a0c', '#1e4d24', '#eefbe8', '#a3e635', '#5eead4', '#8ab87f'],
      ['#062a2e', '#0f5a60', '#e6fffa', '#5eead4', '#a3e635', '#6fa8a0'],
      ['#241505', '#5a3a10', '#fff3d9', '#fbbf24', '#a3e635', '#c4a06a'],
      ['#f2f7e9', '#dbe8c8', '#1e3a1f', '#4d7c0f', '#b3541e', '#7a8a6a']],
    history: [
      ['#2b2118', '#4a3a26', '#f5ead2', '#d4af37', '#b3541e', '#b8a67f'],
      ['#1c1410', '#3a2c20', '#efe3cb', '#b3541e', '#d4af37', '#a08a6a'],
      ['#101418', '#26313a', '#e8e4d8', '#c9a227', '#8a97a5', '#8a94a0'],
      ['#f0e8d5', '#d9cba6', '#2b2118', '#8b0000', '#b3541e', '#8a7a5f']],
    cs: [
      ['#020604', '#0a1f0e', '#d8ffd8', '#33ff66', '#4fd8ff', '#5a8a6a'],
      ['#04060e', '#0e1c3a', '#e0ecff', '#4d7cff', '#33ff66', '#6a7fa8'],
      ['#0a0a0c', '#232329', '#f0f0f5', '#ff9f1c', '#4d7cff', '#8a8a94'],
      ['#eef2f5', '#cfd9e3', '#101820', '#0057b8', '#c0392b', '#6a7a8a']],
    children: [
      ['#1e6fd9', '#7ec8ff', '#ffffff', '#ffde59', '#ff8c42', '#bfe0ff'],
      ['#ff8c42', '#ffd166', '#4a1d05', '#e63946', '#1e6fd9', '#a86a3a'],
      ['#7b2ff7', '#c084fc', '#ffffff', '#fde047', '#5eead4', '#d6bcfa'],
      ['#0ea5a5', '#99f6e4', '#04302c', '#f472b6', '#ffde59', '#4a8a80']],
    poetry: [
      ['#e8e2d5', '#cfc3ab', '#2b2620', '#8b5e34', '#b3541e', '#8a7f6a'],
      ['#2b2733', '#4a4458', '#efeaf5', '#c4b5fd', '#ff9db4', '#9a92ad'],
      ['#f5f0e8', '#e0d5c0', '#3a3230', '#b3541e', '#8b5e34', '#a08a76'],
      ['#1d2b26', '#3a5a50', '#eef5f0', '#a7d7c5', '#ffd166', '#8aa89b']],
    manual: [
      ['#0a2a5e', '#14418f', '#ffffff', '#ffd166', '#7fd4ff', '#9db8e8'],
      ['#101418', '#2b343d', '#f0f4f8', '#ff6b35', '#ffd166', '#8a97a3'],
      ['#e8ecf0', '#c8d2dc', '#16202a', '#c0392b', '#0a4d8c', '#7a8a99'],
      ['#06231c', '#0e4a3e', '#f0faf5', '#f4d35e', '#7fd4ff', '#8ab8a4']],
    philosophy: [
      ['#e8e4da', '#c9c2b2', '#1f1c17', '#8b5e34', '#b3541e', '#8a8378'],
      ['#141210', '#2e2a24', '#efe9dc', '#c9a227', '#8b5e34', '#a09a8a'],
      ['#1c2430', '#33414f', '#eef2f5', '#9db8d4', '#c9a227', '#8a97a3'],
      ['#2a1f16', '#4d3a26', '#f5ead2', '#cd7f32', '#d4af37', '#b8a07f']],
    business: [
      ['#0a1628', '#16294a', '#f0f4fa', '#d4af37', '#4d7cff', '#8aa0c0'],
      ['#101010', '#2b2b2b', '#f5f5f5', '#c0c0c0', '#d4af37', '#8a8a8a'],
      ['#f5f5f0', '#dcdcd2', '#16202a', '#0a4d8c', '#b3541e', '#7a8a99'],
      ['#1a0f14', '#3d1f2b', '#fbeef2', '#e8b04b', '#e86a92', '#b89aa4']]
  };

  /* ---------- motif painters: g=array, cx,cy center, s=scale, P=palette, rnd ---------- */
  function circ(g, cx, cy, r, fill, op, sw, sc) {
    g.push('<circle cx="' + fmt(cx) + '" cy="' + fmt(cy) + '" r="' + fmt(r) + '"' +
      (fill ? ' fill="' + fill + '"' : ' fill="none"') +
      (op != null ? ' opacity="' + op + '"' : '') +
      (sw ? ' stroke="' + (sc || fill) + '" stroke-width="' + sw + '"' : '') + '/>');
  }
  function line(g, x1, y1, x2, y2, sc, sw, op) {
    g.push('<line x1="' + fmt(x1) + '" y1="' + fmt(y1) + '" x2="' + fmt(x2) + '" y2="' + fmt(y2) +
      '" stroke="' + sc + '" stroke-width="' + sw + '"' + (op != null ? ' opacity="' + op + '"' : '') + '/>');
  }
  function path(g, d, fill, sc, sw, op) {
    g.push('<path d="' + d + '" fill="' + (fill || 'none') + '"' +
      (sc ? ' stroke="' + sc + '" stroke-width="' + (sw || 2) + '"' : '') +
      (op != null ? ' opacity="' + op + '"' : '') + '/>');
  }

  var MF = {};
  MF.starfield = function (g, cx, cy, s, P, rnd) {
    for (var i = 0; i < 60; i++) {
      var x = cx - s + rnd() * 2 * s, y = cy - s + rnd() * 2 * s, r = rf(rnd, 0.8, 2.6);
      circ(g, x, y, r, rnd() < 0.25 ? P.accent : P.fg, rf(rnd, 0.35, 0.95));
    }
    for (var j = 0; j < 4; j++) {
      var sx = cx - s * 0.6 + rnd() * 1.2 * s, sy = cy - s * 0.6 + rnd() * 1.2 * s, L = rf(rnd, 6, 12);
      line(g, sx - L, sy, sx + L, sy, P.accent, 1, 0.7); line(g, sx, sy - L, sx, sy + L, P.accent, 1, 0.7);
    }
  };
  MF.orbitalRings = function (g, cx, cy, s, P) {
    circ(g, cx, cy, s * 0.22, P.accent, 0.95);
    circ(g, cx, cy, s * 0.22, 'none', 1, 1.5, P.fg);
    for (var i = 0; i < 3; i++) {
      var rx = s * (0.55 + i * 0.22), ry = rx * 0.34, rot = -18 + i * 16;
      g.push('<ellipse cx="' + fmt(cx) + '" cy="' + fmt(cy) + '" rx="' + fmt(rx) + '" ry="' + fmt(ry) +
        '" fill="none" stroke="' + (i === 1 ? P.accent2 : P.fg) + '" stroke-width="1.6" opacity="0.75" transform="rotate(' + rot + ' ' + fmt(cx) + ' ' + fmt(cy) + ')"/>');
    }
    circ(g, cx + s * 0.62, cy - s * 0.3, s * 0.05, P.fg, 0.9);
  };
  MF.circuitLines = function (g, cx, cy, s, P, rnd) {
    for (var i = 0; i < 9; i++) {
      var x = cx - s + rnd() * 2 * s, y = cy - s + rnd() * 2 * s;
      var x2 = x + (rnd() < 0.5 ? -1 : 1) * rf(rnd, 20, 70), y2 = y + (rnd() < 0.5 ? -1 : 1) * rf(rnd, 20, 70);
      path(g, 'M' + fmt(x) + ' ' + fmt(y) + ' L' + fmt(x2) + ' ' + fmt(y) + ' L' + fmt(x2) + ' ' + fmt(y2),
        'none', P.accent, 1.6, 0.65);
      circ(g, x, y, 3, P.accent, 0.9); circ(g, x2, y2, 4.5, 'none', 1, 1.6, P.accent);
    }
  };
  MF.geoGrid = function (g, cx, cy, s, P) {
    var i, x;
    for (i = -5; i <= 5; i++) {
      x = cx + i * s * 0.2;
      line(g, x, cy + s * 0.1, cx + i * s * 0.05, cy - s, P.accent, 1.2, 0.5);
    }
    for (i = 0; i < 7; i++) {
      var y = cy - s + i * s * 0.18, w = (i / 6) * s * 1.1;
      line(g, cx - w, y, cx + w, y, P.fg, 1, 0.28);
    }
    line(g, cx - s * 1.1, cy - s, cx + s * 1.1, cy - s, P.accent, 2, 0.9);
  };
  MF.waveform = function (g, cx, cy, s, P) {
    var d = 'M' + fmt(cx - s);
    for (var x = -s; x <= s; x += 6) d += ' L' + fmt(cx + x) + ' ' + fmt(cy + Math.sin(x / 14) * s * 0.42);
    path(g, d, 'none', P.accent, 2.4, 0.95);
    var d2 = 'M' + fmt(cx - s);
    for (var x2 = -s; x2 <= s; x2 += 6) d2 += ' L' + fmt(cx + x2) + ' ' + fmt(cy + Math.sin(x2 / 14 + 1.3) * s * 0.42);
    path(g, d2, 'none', P.fg, 1.2, 0.4);
  };
  MF.compassRose = function (g, cx, cy, s, P) {
    var pts = [];
    for (var i = 0; i < 16; i++) {
      var a = i * Math.PI / 8, r = (i % 2 === 0) ? s : s * 0.32;
      pts.push(fmt(cx + Math.cos(a) * r) + ',' + fmt(cy + Math.sin(a) * r));
    }
    g.push('<polygon points="' + pts.join(' ') + '" fill="' + P.accent + '" opacity="0.9"/>');
    circ(g, cx, cy, s * 0.14, P.fg, 0.95);
    circ(g, cx, cy, s * 1.08, 'none', 1, 2, P.fg);
    for (var t = 0; t < 36; t++) {
      var a2 = t * Math.PI / 18, r1 = s * 1.14, r2 = s * (t % 9 === 0 ? 1.3 : 1.22);
      line(g, cx + Math.cos(a2) * r1, cy + Math.sin(a2) * r1, cx + Math.cos(a2) * r2, cy + Math.sin(a2) * r2, P.muted, 1.4, 0.8);
    }
  };
  MF.crest = function (g, cx, cy, s, P) {
    var w = s * 1.1, hh = s * 1.3;
    path(g, 'M' + fmt(cx - w / 2) + ' ' + fmt(cy - hh / 2) +
      ' L' + fmt(cx + w / 2) + ' ' + fmt(cy - hh / 2) +
      ' L' + fmt(cx + w / 2) + ' ' + fmt(cy + hh * 0.1) +
      ' Q' + fmt(cx + w / 2) + ' ' + fmt(cy + hh / 2) + ' ' + fmt(cx) + ' ' + fmt(cy + hh / 2) +
      ' Q' + fmt(cx - w / 2) + ' ' + fmt(cy + hh / 2) + ' ' + fmt(cx - w / 2) + ' ' + fmt(cy + hh * 0.1) + ' Z',
      'none', P.accent, 2.4, 0.95);
    circ(g, cx, cy - s * 0.05, s * 0.34, 'none', 1, 2, P.fg);
    circ(g, cx, cy - s * 0.05, s * 0.12, P.accent2, 0.95);
    path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.42) + ' L' + fmt(cx + s * 0.3) + ' ' + fmt(cy + s * 0.16) +
      ' L' + fmt(cx - s * 0.3) + ' ' + fmt(cy + s * 0.16) + ' Z', P.accent, 0.85);
  };
  MF.filigree = function (g, cx, cy, s, P) {
    var sw = 2;
    [-1, 1].forEach(function (sgn) {
      path(g, 'M' + fmt(cx) + ' ' + fmt(cy) + ' C' + fmt(cx + sgn * s * 0.5) + ' ' + fmt(cy - s * 0.5) + ' ' +
        fmt(cx + sgn * s * 0.9) + ' ' + fmt(cy) + ' ' + fmt(cx + sgn * s * 0.7) + ' ' + fmt(cy + s * 0.42),
        'none', P.accent, sw, 0.9);
      path(g, 'M' + fmt(cx + sgn * s * 0.28) + ' ' + fmt(cy - s * 0.06) + ' c' + fmt(sgn * 14) + ' ' + fmt(-20) + ' ' +
        fmt(sgn * 34) + ' ' + fmt(-14) + ' ' + fmt(sgn * 30) + ' ' + fmt(10), 'none', P.fg, 1.4, 0.7);
      circ(g, cx + sgn * s * 0.55, cy - s * 0.28, 4, P.accent2, 0.9);
    });
    circ(g, cx, cy, 5, P.accent, 0.95);
  };
  MF.mountains = function (g, cx, cy, s, P) {
    circ(g, cx + s * 0.5, cy - s * 0.55, s * 0.22, P.accent, 0.85);
    var layers = [[0.9, 0.5], [0.6, 0.75], [0.3, 1]];
    layers.forEach(function (L, i) {
      var base = cy + s * 0.8, peak = cy - s * L[0] * 0.5, w = s * L[1];
      path(g, 'M' + fmt(cx - w) + ' ' + fmt(base) + ' L' + fmt(cx - w * 0.35) + ' ' + fmt(peak) +
        ' L' + fmt(cx) + ' ' + fmt(base - s * 0.18) + ' L' + fmt(cx + w * 0.4) + ' ' + fmt(peak - s * 0.1) +
        ' L' + fmt(cx + w) + ' ' + fmt(base) + ' Z', P.bg2 || P.muted, 0.55 + i * 0.2);
    });
    line(g, cx - s, cy + s * 0.8, cx + s, cy + s * 0.8, P.fg, 1.4, 0.6);
  };
  MF.moonSword = function (g, cx, cy, s, P) {
    g.push('<path d="M' + fmt(cx + s * 0.55) + ' ' + fmt(cy - s * 0.75) +
      ' A' + fmt(s * 0.78) + ' ' + fmt(s * 0.78) + ' 0 1 0 ' + fmt(cx + s * 0.55) + ' ' + fmt(cy + s * 0.75) +
      ' A' + fmt(s * 0.62) + ' ' + fmt(s * 0.62) + ' 0 1 1 ' + fmt(cx + s * 0.55) + ' ' + fmt(cy - s * 0.75) +
      ' Z" fill="' + P.accent + '" opacity="0.92"/>');
    line(g, cx - s * 0.7, cy + s * 0.75, cx + s * 0.75, cy - s * 0.7, P.fg, 5, 0.9);
    line(g, cx - s * 0.28, cy + s * 0.28, cx - s * 0.05, cy + s * 0.05, P.accent2, 8, 0.95);
    circ(g, cx - s * 0.7, cy + s * 0.75, s * 0.07, P.accent2, 0.95);
  };
  MF.treeOfLife = function (g, cx, cy, s, P, rnd) {
    path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.9) + ' C' + fmt(cx - s * 0.12) + ' ' + fmt(cy + s * 0.3) + ' ' +
      fmt(cx + s * 0.1) + ' ' + fmt(cy) + ' ' + fmt(cx - s * 0.04) + ' ' + fmt(cy - s * 0.5),
      'none', P.accent, s * 0.09, 0.95);
    for (var i = 0; i < 7; i++) {
      var bx = cx + rf(rnd, -s * 0.15, s * 0.15), by = cy - s * 0.5 + rf(rnd, -s * 0.1, s * 0.35);
      var dir = rnd() < 0.5 ? -1 : 1, len = rf(rnd, s * 0.3, s * 0.6);
      path(g, 'M' + fmt(bx) + ' ' + fmt(by) + ' Q' + fmt(bx + dir * len * 0.6) + ' ' + fmt(by - len * 0.3) + ' ' +
        fmt(bx + dir * len) + ' ' + fmt(by - len * 0.7), 'none', P.accent, 2.4, 0.85);
    }
    for (var j = 0; j < 26; j++) {
      var a = rnd() * Math.PI * 2, rr = Math.sqrt(rnd()) * s * 0.85;
      circ(g, cx + Math.cos(a) * rr, cy - s * 0.42 + Math.sin(a) * rr * 0.8, rf(rnd, 3, 9),
        rnd() < 0.3 ? P.accent2 : P.accent, rf(rnd, 0.4, 0.85));
    }
    circ(g, cx, cy + s * 0.9, s * 1.05, 'none', 1, 1.6, P.fg);
  };
  MF.laurel = function (g, cx, cy, s, P) {
    [-1, 1].forEach(function (sgn) {
      path(g, 'M' + fmt(cx + sgn * s * 0.15) + ' ' + fmt(cy + s * 0.85) +
        ' Q' + fmt(cx + sgn * s * 0.95) + ' ' + fmt(cy + s * 0.2) + ' ' + fmt(cx + sgn * s * 0.3) + ' ' + fmt(cy - s * 0.8),
        'none', P.accent, 2.2, 0.95);
      for (var i = 0; i < 8; i++) {
        var t = i / 7, lx = cx + sgn * (s * 0.15 + t * t * s * 0.75 * 0.9), ly = cy + s * 0.85 - t * s * 1.55;
        var ang = sgn * (55 - t * 30);
        g.push('<ellipse cx="' + fmt(lx) + '" cy="' + fmt(ly) + '" rx="' + fmt(s * 0.16) + '" ry="' + fmt(s * 0.055) +
          '" fill="' + P.accent + '" opacity="0.85" transform="rotate(' + fmt(ang) + ' ' + fmt(lx) + ' ' + fmt(ly) + ')"/>');
      }
    });
  };
  MF.keyhole = function (g, cx, cy, s, P) {
    circ(g, cx, cy - s * 0.25, s * 0.38, 'none', 1, 3, P.accent);
    path(g, 'M' + fmt(cx - s * 0.2) + ' ' + fmt(cy - s * 0.02) + ' L' + fmt(cx - s * 0.32) + ' ' + fmt(cy + s * 0.75) +
      ' L' + fmt(cx + s * 0.32) + ' ' + fmt(cy + s * 0.75) + ' L' + fmt(cx + s * 0.2) + ' ' + fmt(cy - s * 0.02) + ' Z',
      'none', P.accent, 3, 0.95);
    circ(g, cx, cy - s * 0.25, s * 0.1, P.accent2, 0.9);
    circ(g, cx, cy, s * 1.05, 'none', 1, 1.4, P.fg);
  };
  MF.fingerprint = function (g, cx, cy, s, P) {
    for (var i = 0; i < 6; i++) {
      var r = s * (0.25 + i * 0.14);
      path(g, 'M' + fmt(cx - r) + ' ' + fmt(cy + s * 0.25) + ' A' + fmt(r) + ' ' + fmt(r) + ' 0 0 1 ' +
        fmt(cx + r) + ' ' + fmt(cy + s * 0.25), 'none', i % 2 ? P.accent : P.fg, 1.8, 0.75);
    }
    circ(g, cx, cy - s * 0.35, s * 0.09, P.accent2, 0.95);
  };
  MF.fogBands = function (g, cx, cy, s, P, rnd) {
    circ(g, cx + s * 0.42, cy - s * 0.72, s * 0.3, P.accent, 0.14);
    circ(g, cx + s * 0.42, cy - s * 0.72, s * 0.18, P.fg, 0.5);
    for (var i = 0; i < 6; i++) {
      var y = cy - s * 0.75 + i * s * 0.3, amp = s * rf(rnd, 0.06, 0.14), ph = rnd() * 6.28;
      var d = 'M' + fmt(cx - s * 1.05);
      for (var x = -s * 1.05; x <= s * 1.05; x += 10) {
        d += ' L' + fmt(cx + x) + ' ' + fmt(y + Math.sin(x / (s * 0.45) + ph) * amp);
      }
      path(g, d, 'none', i % 2 ? P.accent : P.fg, rf(rnd, 3, 7), rf(rnd, 0.12, 0.3));
    }
  };
  MF.blinds = function (g, cx, cy, s, P, rnd) {
    for (var i = -6; i <= 6; i++) {
      var x = cx + i * s * 0.14;
      line(g, x, cy - s, x, cy + s, i % 3 === 0 ? P.accent : P.fg, i % 3 === 0 ? 3 : 1.4, rf(rnd, 0.25, 0.7));
    }
    circ(g, cx - s * 0.3, cy + s * 0.1, s * 0.42, 'none', 1, 2.4, P.accent);
    line(g, cx + s * 0.02, cy + s * 0.42, cx + s * 0.35, cy + s * 0.75, P.accent, 2.4, 0.95);
  };
  MF.spiral = function (g, cx, cy, s, P) {
    var d = '', turns = 4.2, steps = 90;
    for (var i = 0; i <= steps; i++) {
      var t = i / steps, a = t * turns * Math.PI * 2, r = t * s;
      d += (i === 0 ? 'M' : ' L') + fmt(cx + Math.cos(a) * r) + ' ' + fmt(cy + Math.sin(a) * r);
    }
    path(g, d, 'none', P.accent, 2.6, 0.95);
    circ(g, cx, cy, s * 0.06, P.accent2, 0.95);
    circ(g, cx, cy, s * 1.12, 'none', 1, 1.4, P.fg);
  };
  MF.roseSpiral = function (g, cx, cy, s, P) {
    for (var ring = 0; ring < 3; ring++) {
      var n = 5 + ring * 3, rr = s * (0.28 + ring * 0.24);
      for (var i = 0; i < n; i++) {
        var a = i * Math.PI * 2 / n + ring * 0.5;
        var px = cx + Math.cos(a) * rr, py = cy + Math.sin(a) * rr;
        g.push('<ellipse cx="' + fmt(px) + '" cy="' + fmt(py) + '" rx="' + fmt(s * 0.2) + '" ry="' + fmt(s * 0.11) +
          '" fill="' + (ring === 2 ? P.accent2 : P.accent) + '" opacity="' + (0.9 - ring * 0.22).toFixed(2) +
          '" transform="rotate(' + fmt(a * 180 / Math.PI) + ' ' + fmt(px) + ' ' + fmt(py) + ')"/>');
      }
    }
    circ(g, cx, cy, s * 0.13, P.fg, 0.95);
  };
  MF.heartLine = function (g, cx, cy, s, P) {
    path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.62) +
      ' C' + fmt(cx - s * 1.15) + ' ' + fmt(cy - s * 0.1) + ' ' + fmt(cx - s * 0.62) + ' ' + fmt(cy - s * 0.78) + ' ' + fmt(cx) + ' ' + fmt(cy - s * 0.28) +
      ' C' + fmt(cx + s * 0.62) + ' ' + fmt(cy - s * 0.78) + ' ' + fmt(cx + s * 1.15) + ' ' + fmt(cy - s * 0.1) + ' ' + fmt(cx) + ' ' + fmt(cy + s * 0.62) + ' Z',
      'none', P.accent, 3, 0.95);
    path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.62) +
      ' C' + fmt(cx - s * 0.8) + ' ' + fmt(cy) + ' ' + fmt(cx - s * 0.4) + ' ' + fmt(cy - s * 0.5) + ' ' + fmt(cx) + ' ' + fmt(cy - s * 0.2) +
      ' C' + fmt(cx + s * 0.4) + ' ' + fmt(cy - s * 0.5) + ' ' + fmt(cx + s * 0.8) + ' ' + fmt(cy) + ' ' + fmt(cx) + ' ' + fmt(cy + s * 0.62) + ' Z',
      P.accent, 0.28);
  };
  MF.doveWings = function (g, cx, cy, s, P) {
    [-1, 1].forEach(function (sgn) {
      path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.3) +
        ' Q' + fmt(cx + sgn * s * 0.7) + ' ' + fmt(cy - s * 0.5) + ' ' + fmt(cx + sgn * s * 1.05) + ' ' + fmt(cy - s * 0.15) +
        ' Q' + fmt(cx + sgn * s * 0.75) + ' ' + fmt(cy - s * 0.05) + ' ' + fmt(cx + sgn * s * 0.55) + ' ' + fmt(cy + s * 0.15) +
        ' Q' + fmt(cx + sgn * s * 0.35) + ' ' + fmt(cy + s * 0.1) + ' ' + fmt(cx) + ' ' + fmt(cy + s * 0.3) + ' Z',
        P.fg, 0.85);
      path(g, 'M' + fmt(cx + sgn * s * 0.15) + ' ' + fmt(cy + s * 0.1) + ' Q' + fmt(cx + sgn * s * 0.6) + ' ' + fmt(cy - s * 0.25) + ' ' +
        fmt(cx + sgn * s * 0.9) + ' ' + fmt(cy - s * 0.1), 'none', P.accent, 1.8, 0.9);
    });
    circ(g, cx, cy + s * 0.42, s * 0.1, P.accent2, 0.95);
  };
  MF.crackMoon = function (g, cx, cy, s, P) {
    circ(g, cx, cy, s * 0.72, P.fg, 0.9);
    circ(g, cx, cy, s * 0.72, 'none', 1, 2, P.accent);
    path(g, 'M' + fmt(cx - s * 0.1) + ' ' + fmt(cy - s * 0.7) + ' L' + fmt(cx + s * 0.12) + ' ' + fmt(cy - s * 0.3) +
      ' L' + fmt(cx - s * 0.15) + ' ' + fmt(cy) + ' L' + fmt(cx + s * 0.18) + ' ' + fmt(cy + s * 0.35) +
      ' L' + fmt(cx - s * 0.05) + ' ' + fmt(cy + s * 0.7), 'none', P.accent, 2.6, 0.95);
    for (var i = 0; i < 5; i++) circ(g, cx - s * 0.6 + i * s * 0.14, cy - s * 0.75, 2.2, P.accent, 0.8);
  };
  MF.thorns = function (g, cx, cy, s, P, rnd) {
    for (var i = 0; i < 5; i++) {
      var x0 = cx - s + i * s * 0.5;
      path(g, 'M' + fmt(x0) + ' ' + fmt(cy + s * 0.8) + ' Q' + fmt(x0 + s * 0.3) + ' ' + fmt(cy) + ' ' +
        fmt(x0 + s * 0.1) + ' ' + fmt(cy - s * 0.7), 'none', P.accent, 2.6, 0.9);
      for (var j = 0; j < 3; j++) {
        var ty = cy + s * 0.5 - j * s * 0.4, tx = x0 + s * 0.22 - j * s * 0.04;
        path(g, 'M' + fmt(tx) + ' ' + fmt(ty) + ' l' + fmt(14) + ' ' + fmt(-8) + ' l' + fmt(-16) + ' ' + fmt(-2) + ' Z', P.accent2, 0.85);
      }
    }
    circ(g, cx, cy - s * 0.85, s * 0.3, P.accent, 0.18);
  };
  MF.batSil = function (g, cx, cy, s, P, rnd) {
    for (var i = 0; i < 4; i++) {
      var bx = cx - s * 0.8 + rnd() * s * 1.6, by = cy - s * 0.6 + rnd() * s * 1.1, b = rf(rnd, 14, 26);
      path(g, 'M' + fmt(bx - b) + ' ' + fmt(by) + ' Q' + fmt(bx - b * 0.4) + ' ' + fmt(by - b * 0.7) + ' ' + fmt(bx) + ' ' + fmt(by - b * 0.15) +
        ' Q' + fmt(bx + b * 0.4) + ' ' + fmt(by - b * 0.7) + ' ' + fmt(bx + b) + ' ' + fmt(by) +
        ' Q' + fmt(bx + b * 0.5) + ' ' + fmt(by + b * 0.25) + ' ' + fmt(bx) + ' ' + fmt(by + b * 0.1) +
        ' Q' + fmt(bx - b * 0.5) + ' ' + fmt(by + b * 0.25) + ' ' + fmt(bx - b) + ' ' + fmt(by) + ' Z',
        P.fg, 0.85);
    }
    circ(g, cx + s * 0.45, cy - s * 0.55, s * 0.34, P.accent, 0.9);
  };
  MF.chalkEq = function (g, cx, cy, s, P, rnd) {
    var syms = ['∫', 'Σ', 'π', '√', 'Δ', '∞', 'φ', 'λ', '≠', '∂'];
    for (var i = 0; i < 9; i++) {
      var x = cx - s + rnd() * 2 * s, y = cy - s + rnd() * 2 * s, fs = ri(rnd, 22, 54);
      g.push('<text x="' + fmt(x) + '" y="' + fmt(y) + '" font-family="Georgia,serif" font-size="' + fs +
        '" fill="' + (rnd() < 0.35 ? P.accent : P.fg) + '" opacity="' + rf(rnd, 0.4, 0.9).toFixed(2) +
        '" text-anchor="middle" transform="rotate(' + ri(rnd, -18, 18) + ' ' + fmt(x) + ' ' + fmt(y) + ')">' +
        syms[ri(rnd, 0, syms.length - 1)] + '</text>');
    }
    circ(g, cx, cy, s * 1.05, 'none', 1, 1.6, P.fg);
  };
  MF.atom = function (g, cx, cy, s, P) {
    for (var i = 0; i < 3; i++) {
      var rot = i * 60;
      g.push('<ellipse cx="' + fmt(cx) + '" cy="' + fmt(cy) + '" rx="' + fmt(s * 0.95) + '" ry="' + fmt(s * 0.34) +
        '" fill="none" stroke="' + (i === 0 ? P.accent : P.fg) + '" stroke-width="2" opacity="0.9" transform="rotate(' +
        rot + ' ' + fmt(cx) + ' ' + fmt(cy) + ')"/>');
    }
    circ(g, cx, cy, s * 0.14, P.accent2, 0.95);
    circ(g, cx + s * 0.95, cy - s * 0.2, s * 0.06, P.fg, 0.9);
    circ(g, cx - s * 0.5, cy + s * 0.75, s * 0.06, P.accent, 0.9);
  };
  MF.flask = function (g, cx, cy, s, P, rnd) {
    path(g, 'M' + fmt(cx - s * 0.32) + ' ' + fmt(cy - s * 0.8) + ' L' + fmt(cx - s * 0.32) + ' ' + fmt(cy - s * 0.1) +
      ' L' + fmt(cx - s * 0.72) + ' ' + fmt(cy + s * 0.65) + ' L' + fmt(cx + s * 0.72) + ' ' + fmt(cy + s * 0.65) +
      ' L' + fmt(cx + s * 0.32) + ' ' + fmt(cy - s * 0.1) + ' L' + fmt(cx + s * 0.32) + ' ' + fmt(cy - s * 0.8) + ' Z',
      'none', P.fg, 2.6, 0.95);
    path(g, 'M' + fmt(cx - s * 0.58) + ' ' + fmt(cy + s * 0.28) + ' L' + fmt(cx - s * 0.66) + ' ' + fmt(cy + s * 0.6) +
      ' L' + fmt(cx + s * 0.66) + ' ' + fmt(cy + s * 0.6) + ' L' + fmt(cx + s * 0.58) + ' ' + fmt(cy + s * 0.28) + ' Z',
      P.accent, 0.75);
    for (var i = 0; i < 6; i++) circ(g, cx + rf(rnd, -s * 0.4, s * 0.4), cy + rf(rnd, -s * 0.5, s * 0.1), rf(rnd, 2, 6), P.accent2, 0.85);
    line(g, cx - s * 0.45, cy - s * 0.8, cx + s * 0.45, cy - s * 0.8, P.fg, 2.6, 0.95);
  };
  MF.dna = function (g, cx, cy, s, P) {
    var d1 = 'M' + fmt(cx - s * 0.5), d2 = 'M' + fmt(cx - s * 0.5);
    for (var y = -s; y <= s; y += 8) {
      d1 += ' L' + fmt(cx + Math.sin(y / 22) * s * 0.5) + ' ' + fmt(cy + y);
      d2 += ' L' + fmt(cx + Math.sin(y / 22 + Math.PI) * s * 0.5) + ' ' + fmt(cy + y);
    }
    path(g, d1, 'none', P.accent, 2.6, 0.95);
    path(g, d2, 'none', P.accent2, 2.6, 0.95);
    for (var y2 = -s * 0.9; y2 <= s * 0.9; y2 += 26) {
      var x1 = cx + Math.sin(y2 / 22) * s * 0.5, x2 = cx + Math.sin(y2 / 22 + Math.PI) * s * 0.5;
      line(g, x1, cy + y2, x2, cy + y2, P.fg, 1.4, 0.7);
    }
  };
  MF.leaf = function (g, cx, cy, s, P) {
    path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.85) +
      ' Q' + fmt(cx - s * 0.95) + ' ' + fmt(cy + s * 0.1) + ' ' + fmt(cx) + ' ' + fmt(cy - s * 0.85) +
      ' Q' + fmt(cx + s * 0.95) + ' ' + fmt(cy + s * 0.1) + ' ' + fmt(cx) + ' ' + fmt(cy + s * 0.85) + ' Z',
      P.accent, 0.32);
    path(g, 'M' + fmt(cx) + ' ' + fmt(cy + s * 0.85) + ' Q' + fmt(cx - s * 0.95) + ' ' + fmt(cy + s * 0.1) + ' ' +
      fmt(cx) + ' ' + fmt(cy - s * 0.85) + ' Q' + fmt(cx + s * 0.95) + ' ' + fmt(cy + s * 0.1) + ' ' +
      fmt(cx) + ' ' + fmt(cy + s * 0.85) + ' Z', 'none', P.fg, 2.2, 0.95);
    line(g, cx, cy + s * 0.8, cx, cy - s * 0.78, P.fg, 2, 0.8);
    for (var i = 0; i < 5; i++) {
      var vy = cy + s * 0.55 - i * s * 0.3;
      line(g, cx, vy, cx - s * 0.4, vy - s * 0.22, P.fg, 1.4, 0.6);
      line(g, cx, vy, cx + s * 0.4, vy - s * 0.22, P.fg, 1.4, 0.6);
    }
  };
  MF.column = function (g, cx, cy, s, P) {
    var w = s * 0.5;
    g.push('<rect x="' + fmt(cx - w * 1.5) + '" y="' + fmt(cy - s * 0.95) + '" width="' + fmt(w * 3) + '" height="' + fmt(s * 0.14) + '" fill="' + P.accent + '" opacity="0.92"/>');
    g.push('<rect x="' + fmt(cx - w * 1.3) + '" y="' + fmt(cy - s * 0.78) + '" width="' + fmt(w * 2.6) + '" height="' + fmt(s * 0.1) + '" fill="' + P.fg + '" opacity="0.7"/>');
    for (var i = -1; i <= 1; i++) {
      g.push('<rect x="' + fmt(cx + i * w - w * 0.22) + '" y="' + fmt(cy - s * 0.68) + '" width="' + fmt(w * 0.44) + '" height="' + fmt(s * 1.2) + '" fill="none" stroke="' + P.fg + '" stroke-width="2" opacity="0.9"/>');
    }
    g.push('<rect x="' + fmt(cx - w * 1.5) + '" y="' + fmt(cy + s * 0.62) + '" width="' + fmt(w * 3) + '" height="' + fmt(s * 0.12) + '" fill="' + P.accent + '" opacity="0.92"/>');
    g.push('<rect x="' + fmt(cx - w * 1.7) + '" y="' + fmt(cy + s * 0.78) + '" width="' + fmt(w * 3.4) + '" height="' + fmt(s * 0.12) + '" fill="' + P.fg + '" opacity="0.7"/>');
  };
  MF.scroll = function (g, cx, cy, s, P) {
    var w = s * 1.5, hh = s * 0.85;
    g.push('<rect x="' + fmt(cx - w / 2) + '" y="' + fmt(cy - hh / 2) + '" width="' + fmt(w) + '" height="' + fmt(hh) +
      '" fill="' + P.accent + '" opacity="0.28"/>');
    g.push('<rect x="' + fmt(cx - w / 2) + '" y="' + fmt(cy - hh / 2) + '" width="' + fmt(w) + '" height="' + fmt(hh) +
      '" fill="none" stroke="' + P.fg + '" stroke-width="2" opacity="0.9"/>');
    circ(g, cx - w / 2, cy, hh / 2, P.accent, 0.85);
    circ(g, cx + w / 2, cy, hh / 2, P.accent, 0.85);
    circ(g, cx - w / 2, cy, hh / 4, P.bg1 || '#000', 1);
    circ(g, cx + w / 2, cy, hh / 4, P.bg1 || '#000', 1);
    for (var i = 0; i < 4; i++) line(g, cx - w * 0.32, cy - hh * 0.25 + i * hh * 0.17, cx + w * 0.32, cy - hh * 0.25 + i * hh * 0.17, P.fg, 1.6, 0.6);
  };
  MF.codeBrackets = function (g, cx, cy, s, P) {
    g.push('<text x="' + fmt(cx) + '" y="' + fmt(cy + s * 0.35) + '" font-family="Consolas,monospace" font-size="' + fmt(s * 1.5) +
      '" fill="' + P.accent + '" text-anchor="middle" opacity="0.95">{ }</text>');
    g.push('<text x="' + fmt(cx) + '" y="' + fmt(cy - s * 0.55) + '" font-family="Consolas,monospace" font-size="' + fmt(s * 0.4) +
      '" fill="' + P.fg + '" text-anchor="middle" opacity="0.7">&lt;/&gt;</text>');
    circ(g, cx - s * 0.85, cy + s * 0.7, 5, P.accent2, 0.85);
    circ(g, cx + s * 0.85, cy - s * 0.7, 5, P.accent2, 0.85);
  };
  MF.gear = function (g, cx, cy, s, P) {
    var pts = [];
    for (var i = 0; i < 24; i++) {
      var a = i * Math.PI / 12, r = (i % 2 === 0) ? s : s * 0.78;
      pts.push(fmt(cx + Math.cos(a) * r) + ',' + fmt(cy + Math.sin(a) * r));
    }
    g.push('<polygon points="' + pts.join(' ') + '" fill="none" stroke="' + P.accent + '" stroke-width="4" opacity="0.95"/>');
    circ(g, cx, cy, s * 0.42, 'none', 1, 3, P.fg);
    circ(g, cx, cy, s * 0.14, P.accent2, 0.95);
  };
  MF.balloon = function (g, cx, cy, s, P, rnd) {
    var bs = s * 1.28;
    for (var i = 0; i < 5; i++) {
      var bx = cx - bs * 0.82 + i * bs * 0.41, by = cy - bs * 0.45 + (rnd() - 0.5) * bs * 0.28;
      var col = [P.accent, P.accent2, P.fg][i % 3];
      path(g, 'M' + fmt(bx) + ' ' + fmt(by - bs * 0.42) + ' C' + fmt(bx + bs * 0.3) + ' ' + fmt(by - bs * 0.42) + ' ' +
        fmt(bx + bs * 0.3) + ' ' + fmt(by + bs * 0.05) + ' ' + fmt(bx) + ' ' + fmt(by + bs * 0.05) +
        ' C' + fmt(bx - bs * 0.3) + ' ' + fmt(by + bs * 0.05) + ' ' + fmt(bx - bs * 0.3) + ' ' + fmt(by - bs * 0.42) + ' ' +
        fmt(bx) + ' ' + fmt(by - bs * 0.42) + ' Z', col, 0.92);
      path(g, 'M' + fmt(bx - bs * 0.06) + ' ' + fmt(by + bs * 0.05) + ' L' + fmt(bx + bs * 0.06) + ' ' + fmt(by + bs * 0.05) +
        ' L' + fmt(bx) + ' ' + fmt(by + bs * 0.16) + ' Z', col, 0.92);
      circ(g, bx - bs * 0.1, by - bs * 0.24, bs * 0.05, '#ffffff', 0.55);
      path(g, 'M' + fmt(bx) + ' ' + fmt(by + bs * 0.16) + ' Q' + fmt(bx + bs * 0.2) + ' ' + fmt(by + bs * 0.5) + ' ' +
        fmt(cx + (rnd() - 0.5) * 20) + ' ' + fmt(cy + bs * 0.72), 'none', P.fg, 1.6, 0.75);
    }
  };
  MF.star5 = function (g, cx, cy, s, P, rnd) {
    function star(sx, sy, r, fill, op) {
      var pts = [];
      for (var i = 0; i < 10; i++) {
        var a = -Math.PI / 2 + i * Math.PI / 5, rr = (i % 2 === 0) ? r : r * 0.42;
        pts.push(fmt(sx + Math.cos(a) * rr) + ',' + fmt(sy + Math.sin(a) * rr));
      }
      g.push('<polygon points="' + pts.join(' ') + '" fill="' + fill + '" opacity="' + op + '"/>');
    }
    star(cx, cy, s * 0.75, P.accent, 0.95);
    star(cx, cy, s * 0.4, P.accent2, 0.9);
    for (var i = 0; i < 8; i++) star(cx - s + rnd() * 2 * s, cy - s + rnd() * 2 * s, rf(rnd, 4, 12), P.fg, rf(rnd, 0.4, 0.9));
  };
  MF.rainbowArcs = function (g, cx, cy, s, P) {
    var cols = [P.accent, P.accent2, P.fg, P.muted];
    for (var i = 0; i < 4; i++) {
      var r = s * (0.95 - i * 0.2);
      path(g, 'M' + fmt(cx - r) + ' ' + fmt(cy + s * 0.5) + ' A' + fmt(r) + ' ' + fmt(r) + ' 0 0 1 ' +
        fmt(cx + r) + ' ' + fmt(cy + s * 0.5), 'none', cols[i], s * 0.14, 0.85);
    }
    circ(g, cx - s * 1.05, cy - s * 0.35, s * 0.22, P.accent2, 0.5);
    circ(g, cx + s * 1.05, cy - s * 0.35, s * 0.22, P.accent2, 0.5);
  };
  MF.sun = function (g, cx, cy, s, P) {
    circ(g, cx, cy, s * 0.42, P.accent, 0.95);
    circ(g, cx, cy, s * 0.42, 'none', 1, 2, P.fg);
    for (var i = 0; i < 12; i++) {
      var a = i * Math.PI / 6, r1 = s * 0.55, r2 = s * (i % 2 ? 0.72 : 0.9);
      line(g, cx + Math.cos(a) * r1, cy + Math.sin(a) * r1, cx + Math.cos(a) * r2, cy + Math.sin(a) * r2, P.accent, 3, 0.9);
    }
  };
  MF.quill = function (g, cx, cy, s, P) {
    path(g, 'M' + fmt(cx - s * 0.5) + ' ' + fmt(cy + s * 0.85) +
      ' Q' + fmt(cx - s * 0.7) + ' ' + fmt(cy - s * 0.3) + ' ' + fmt(cx + s * 0.35) + ' ' + fmt(cy - s * 0.8) +
      ' Q' + fmt(cx + s * 0.1) + ' ' + fmt(cy - s * 0.1) + ' ' + fmt(cx - s * 0.5) + ' ' + fmt(cy + s * 0.85) + ' Z',
      P.fg, 0.28);
    path(g, 'M' + fmt(cx - s * 0.5) + ' ' + fmt(cy + s * 0.85) +
      ' Q' + fmt(cx - s * 0.7) + ' ' + fmt(cy - s * 0.3) + ' ' + fmt(cx + s * 0.35) + ' ' + fmt(cy - s * 0.8),
      'none', P.accent, 2.4, 0.95);
    line(g, cx - s * 0.35, cy + s * 0.6, cx + s * 0.28, cy - s * 0.62, P.accent, 1.8, 0.9);
    for (var i = 0; i < 6; i++) {
      var t = i / 5, qx = cx - s * 0.5 + t * s * 0.85, qy = cy + s * 0.85 - t * s * 1.65;
      line(g, qx, qy, qx - s * 0.22, qy - s * 0.12, P.fg, 1.2, 0.6);
    }
  };
  MF.moonGlow = function (g, cx, cy, s, P) {
    circ(g, cx, cy, s * 0.95, P.accent, 0.12);
    circ(g, cx, cy, s * 0.68, P.accent, 0.16);
    circ(g, cx, cy, s * 0.45, P.fg, 0.92);
    circ(g, cx - s * 0.12, cy - s * 0.1, s * 0.08, P.muted, 0.5);
    circ(g, cx + s * 0.14, cy + s * 0.12, s * 0.06, P.muted, 0.5);
    circ(g, cx + s * 0.05, cy - s * 0.2, s * 0.045, P.muted, 0.5);
  };
  MF.rulerTicks = function (g, cx, cy, s, P) {
    line(g, cx - s, cy, cx + s, cy, P.fg, 2.4, 0.95);
    for (var i = -10; i <= 10; i++) {
      var x = cx + i * s * 0.1, len = (i % 5 === 0) ? s * 0.34 : s * 0.18;
      line(g, x, cy, x, cy - len, i % 5 === 0 ? P.accent : P.fg, i % 5 === 0 ? 2.4 : 1.4, 0.9);
    }
    circ(g, cx - s * 0.7, cy - s * 0.6, s * 0.3, 'none', 1, 2.4, P.accent);
    line(g, cx - s * 0.7, cy - s * 0.3, cx - s * 0.7, cy + s * 0.5, P.accent, 2.4, 0.9);
  };
  MF.crosshair = function (g, cx, cy, s, P) {
    circ(g, cx, cy, s * 0.7, 'none', 1, 2.4, P.accent);
    circ(g, cx, cy, s * 0.45, 'none', 1, 1.6, P.fg);
    line(g, cx - s, cy, cx - s * 0.78, cy, P.accent, 2.4, 0.9);
    line(g, cx + s * 0.78, cy, cx + s, cy, P.accent, 2.4, 0.9);
    line(g, cx, cy - s, cx, cy - s * 0.78, P.accent, 2.4, 0.9);
    line(g, cx, cy + s * 0.78, cx, cy + s, P.accent, 2.4, 0.9);
    circ(g, cx, cy, s * 0.08, P.accent2, 0.95);
  };
  MF.chartBars = function (g, cx, cy, s, P) {
    var vals = [0.35, 0.55, 0.45, 0.7, 0.62, 0.9];
    for (var i = 0; i < vals.length; i++) {
      var bw = s * 0.22, x = cx - s * 0.85 + i * s * 0.3, hh = s * vals[i];
      g.push('<rect x="' + fmt(x) + '" y="' + fmt(cy + s * 0.6 - hh) + '" width="' + fmt(bw) + '" height="' + fmt(hh) +
        '" fill="' + (i === vals.length - 1 ? P.accent : P.fg) + '" opacity="' + (i === vals.length - 1 ? 0.95 : 0.55) + '"/>');
    }
    path(g, 'M' + fmt(cx - s * 0.85) + ' ' + fmt(cy + s * 0.25) + ' L' + fmt(cx - s * 0.1) + ' ' + fmt(cy - s * 0.05) +
      ' L' + fmt(cx + s * 0.35) + ' ' + fmt(cy + s * 0.1) + ' L' + fmt(cx + s * 0.85) + ' ' + fmt(cy - s * 0.35),
      'none', P.accent2, 3, 0.95);
    path(g, 'M' + fmt(cx + s * 0.85) + ' ' + fmt(cy - s * 0.35) + ' l' + fmt(-18) + ' ' + fmt(2) + ' M' +
      fmt(cx + s * 0.85) + ' ' + fmt(cy - s * 0.35) + ' l' + fmt(-2) + ' ' + fmt(18), 'none', P.accent2, 3, 0.95);
    line(g, cx - s, cy + s * 0.6, cx + s, cy + s * 0.6, P.fg, 1.6, 0.7);
  };
  MF.coin = function (g, cx, cy, s, P) {
    circ(g, cx, cy, s * 0.75, P.accent, 0.9);
    circ(g, cx, cy, s * 0.62, 'none', 1, 2, P.bg1 || '#000');
    circ(g, cx, cy, s * 0.75, 'none', 1, 2.4, P.fg);
    g.push('<text x="' + fmt(cx) + '" y="' + fmt(cy + s * 0.28) + '" font-family="Georgia,serif" font-size="' + fmt(s * 0.8) +
      '" fill="' + (P.bg1 || '#000') + '" text-anchor="middle" font-weight="bold">J</text>');
    for (var i = 0; i < 20; i++) {
      var a = i * Math.PI / 10;
      circ(g, cx + Math.cos(a) * s * 0.68, cy + Math.sin(a) * s * 0.68, 1.8, P.bg1 || '#000', 0.8);
    }
  };
  MF.chevrons = function (g, cx, cy, s, P) {
    for (var i = 0; i < 4; i++) {
      var y = cy - s * 0.6 + i * s * 0.38;
      path(g, 'M' + fmt(cx - s * 0.8) + ' ' + fmt(y) + ' L' + fmt(cx) + ' ' + fmt(y + s * 0.3) + ' L' +
        fmt(cx + s * 0.8) + ' ' + fmt(y), 'none', i === 3 ? P.accent : P.fg, i === 3 ? 4 : 2.4, i === 3 ? 0.95 : 0.6);
    }
  };
  MF.hexagons = function (g, cx, cy, s, P, rnd) {
    var r = s * 0.34;
    for (var row = -2; row <= 2; row++) {
      for (var colI = -2; colI <= 2; colI++) {
        var hx = cx + colI * r * 1.75 + (row % 2 ? r * 0.87 : 0), hy = cy + row * r * 1.55;
        if (Math.hypot(hx - cx, hy - cy) > s * 1.05) continue;
        var pts = [];
        for (var i = 0; i < 6; i++) {
          var a = i * Math.PI / 3 + Math.PI / 6;
          pts.push(fmt(hx + Math.cos(a) * r) + ',' + fmt(hy + Math.sin(a) * r));
        }
        var hot = rnd() < 0.22;
        g.push('<polygon points="' + pts.join(' ') + '" fill="' + (hot ? P.accent : 'none') +
          '" fill-opacity="' + (hot ? 0.5 : 0) + '" stroke="' + (hot ? P.accent2 : P.fg) +
          '" stroke-width="1.6" opacity="0.8"/>');
      }
    }
  };
  MF.enso = function (g, cx, cy, s, P) {
    path(g, 'M' + fmt(cx + s * 0.78) + ' ' + fmt(cy - s * 0.35) +
      ' A' + fmt(s * 0.85) + ' ' + fmt(s * 0.85) + ' 0 1 1 ' + fmt(cx + s * 0.62) + ' ' + fmt(cy + s * 0.58),
      'none', P.accent, s * 0.16, 0.9);
    path(g, 'M' + fmt(cx + s * 0.78) + ' ' + fmt(cy - s * 0.35) +
      ' A' + fmt(s * 0.85) + ' ' + fmt(s * 0.85) + ' 0 1 1 ' + fmt(cx + s * 0.62) + ' ' + fmt(cy + s * 0.58),
      'none', P.fg, s * 0.05, 0.5);
    circ(g, cx, cy, s * 0.2, P.accent2, 0.85);
  };
  MF.gridFine = function (g, cx, cy, s, P) {
    for (var x = -10; x <= 10; x++) line(g, cx + x * s * 0.1, cy - s, cx + x * s * 0.1, cy + s, P.fg, 0.8, 0.3);
    for (var y = -10; y <= 10; y++) line(g, cx - s, cy + y * s * 0.1, cx + s, cy + y * s * 0.1, P.fg, 0.8, 0.3);
    circ(g, cx, cy, s * 0.5, 'none', 1, 2.4, P.accent);
    line(g, cx - s, cy, cx + s, cy, P.accent, 1.6, 0.8);
    line(g, cx, cy - s, cx, cy + s, P.accent, 1.6, 0.8);
  };
  MF.magnifier = function (g, cx, cy, s, P) {
    circ(g, cx - s * 0.12, cy - s * 0.18, s * 0.52, 'none', 1, 3.4, P.accent);
    circ(g, cx - s * 0.12, cy - s * 0.18, s * 0.52, P.fg, 0.1);
    line(g, cx + s * 0.26, cy + s * 0.2, cx + s * 0.75, cy + s * 0.68, P.accent, 4, 0.95);
    path(g, 'M' + fmt(cx - s * 0.35) + ' ' + fmt(cy - s * 0.4) + ' l' + fmt(s * 0.2) + ' ' + fmt(s * 0.28) +
      ' M' + fmt(cx - s * 0.05) + ' ' + fmt(cy - s * 0.5) + ' l' + fmt(s * 0.14) + ' ' + fmt(s * 0.2), 'none', P.fg, 1.6, 0.7);
  };
  MF.waves = function (g, cx, cy, s, P) {
    for (var i = 0; i < 7; i++) {
      var y = cy - s + i * s * 0.3, amp = s * 0.16, d = 'M' + fmt(cx - s);
      for (var x = -s; x <= s; x += 8) d += ' L' + fmt(cx + x) + ' ' + fmt(y + Math.sin((x + i * 22) / 26) * amp);
      path(g, d, 'none', i % 2 ? P.accent : P.fg, 1.8, 0.55 + (i % 3) * 0.15);
    }
  };
  MF.dots = function (g, cx, cy, s, P, rnd) {
    for (var i = 0; i < 40; i++) {
      circ(g, cx - s + rnd() * 2 * s, cy - s + rnd() * 2 * s, rf(rnd, 1.5, 4),
        rnd() < 0.4 ? P.accent : P.fg, rf(rnd, 0.3, 0.8));
    }
  };

  /* ---------- motif assignment: 6 per genre ---------- */
  var MOT = {
    sf: ['starfield', 'orbitalRings', 'circuitLines', 'geoGrid', 'waveform', 'compassRose'],
    fantasy: ['crest', 'filigree', 'mountains', 'moonSword', 'treeOfLife', 'laurel'],
    mystery: ['keyhole', 'fingerprint', 'fogBands', 'blinds', 'magnifier', 'spiral'],
    romance: ['roseSpiral', 'heartLine', 'doveWings', 'filigree', 'moonGlow', 'laurel'],
    horror: ['crackMoon', 'thorns', 'batSil', 'fogBands', 'spiral', 'keyhole'],
    math: ['chalkEq', 'geoGrid', 'spiral', 'compassRose', 'waves', 'circuitLines'],
    physics: ['atom', 'orbitalRings', 'waveform', 'starfield', 'compassRose', 'geoGrid'],
    chemistry: ['flask', 'atom', 'hexagons', 'waves', 'circuitLines', 'dots'],
    biology: ['leaf', 'dna', 'treeOfLife', 'waves', 'hexagons', 'mountains'],
    history: ['column', 'scroll', 'laurel', 'compassRose', 'crest', 'waves'],
    cs: ['circuitLines', 'codeBrackets', 'geoGrid', 'hexagons', 'waveform', 'gear'],
    children: ['balloon', 'star5', 'rainbowArcs', 'sun', 'waves', 'dots'],
    poetry: ['quill', 'moonGlow', 'filigree', 'waves', 'laurel', 'doveWings'],
    manual: ['rulerTicks', 'gear', 'gridFine', 'crosshair', 'chevrons', 'circuitLines'],
    philosophy: ['enso', 'column', 'waves', 'spiral', 'laurel', 'keyhole'],
    business: ['chartBars', 'coin', 'laurel', 'chevrons', 'compassRose', 'gridFine']
  };

  /* ---------- text ---------- */
  var SERIF = "Georgia,'Times New Roman','Nimbus Roman',serif";
  var SANS = "Verdana,'Segoe UI',Helvetica,Arial,sans-serif";

  function wrapTitle(title, maxChars) {
    var words = String(title || 'Untitled').split(/\s+/).filter(Boolean);
    var lines = [], cur = '';
    words.forEach(function (w) {
      if ((cur + ' ' + w).trim().length <= maxChars) { cur = (cur + ' ' + w).trim(); }
      else { if (cur) lines.push(cur); cur = w; }
    });
    if (cur) lines.push(cur);
    /* hard-break one absurdly long word */
    for (var i = 0; i < lines.length; i++) {
      if (lines[i].length > maxChars + 8) {
        var w0 = lines[i], parts = [];
        while (w0.length > maxChars) { parts.push(w0.slice(0, maxChars) + '-'); w0 = w0.slice(maxChars); }
        parts.push(w0);
        lines.splice.apply(lines, [i, 1].concat(parts));
      }
    }
    return lines;
  }

  function textBlock(g, lines, cx, y, size, color, family, weight, ls, lh) {
    lh = lh || 1.22;
    for (var i = 0; i < lines.length; i++) {
      g.push('<text x="' + fmt(cx) + '" y="' + fmt(y + i * size * lh) + '" text-anchor="middle" font-family="' + family +
        '" font-size="' + size + '" fill="' + color + '"' + (weight ? ' font-weight="' + weight + '"' : '') +
        (ls ? ' letter-spacing="' + ls + '"' : '') + '>' + esc(lines[i]) + '</text>');
    }
    return y + (lines.length - 1) * size * lh;
  }

  /* ---------- frame ---------- */
  function frame(g, P, style) {
    var m = 14;
    if (style === 0) {
      g.push('<rect x="' + m + '" y="' + m + '" width="' + (W - 2 * m) + '" height="' + (H - 2 * m) +
        '" fill="none" stroke="' + P.accent + '" stroke-width="2.5" opacity="0.9"/>');
      g.push('<rect x="' + (m + 7) + '" y="' + (m + 7) + '" width="' + (W - 2 * m - 14) + '" height="' + (H - 2 * m - 14) +
        '" fill="none" stroke="' + P.fg + '" stroke-width="1" opacity="0.5"/>');
    } else if (style === 1) {
      g.push('<rect x="' + m + '" y="' + m + '" width="' + (W - 2 * m) + '" height="' + (H - 2 * m) +
        '" fill="none" stroke="' + P.fg + '" stroke-width="1.4" opacity="0.75"/>');
    } else {
      var c = 26;
      [[m, m], [W - m, m], [m, H - m], [W - m, H - m]].forEach(function (p) {
        var sx = p[0] === m ? 1 : -1, sy = p[1] === m ? 1 : -1;
        path(g, 'M' + p[0] + ' ' + (p[1] + sy * c) + ' L' + p[0] + ' ' + p[1] + ' L' + (p[0] + sx * c) + ' ' + p[1],
          'none', P.accent, 2.5, 0.9);
      });
    }
  }

  function imprint(g, label, cx, y, P) {
    var t = String(label).toUpperCase();
    textBlock(g, [t], cx, y, 12.5, P.muted, SANS, 'normal', 4);
    var w = t.length * 9.5;
    line(g, cx - w / 2 - 26, y - 4, cx - w / 2 - 8, y - 4, P.accent, 1.4, 0.8);
    line(g, cx + w / 2 + 8, y - 4, cx + w / 2 + 26, y - 4, P.accent, 1.4, 0.8);
  }

  function divider(g, cx, y, P, w) {
    w = w || 120;
    line(g, cx - w / 2, y, cx - 12, y, P.accent, 1.4, 0.8);
    line(g, cx + 12, y, cx + w / 2, y, P.accent, 1.4, 0.8);
    g.push('<rect x="' + fmt(cx - 6) + '" y="' + fmt(y - 6) + '" width="12" height="12" fill="' + P.accent +
      '" opacity="0.9" transform="rotate(45 ' + fmt(cx) + ' ' + fmt(y) + ')"/>');
  }

  /* ---------- main ---------- */
  function generate(book) {
    book = book || {};
    var id = String(book.id || '');
    var title = book.title || book.t || 'Untitled';
    var author = book.author || 'Justin Addam Higgins';
    var h = fnv(id || ('t:' + title));
    if (!h) h = 1;
    var rnd = mulberry(h);

    var gk = (function () {
      var k = book.gkey || book.gk || '';
      if (k && PAL[k]) return k;
      var n = String(book.genre || book.g || '').toLowerCase().trim();
      return GKEYS[n] || 'sf';
    })();

    var pals = PAL[gk];
    var pi = h % 4;
    var P = { bg1: pals[pi][0], bg2: pals[pi][1], fg: pals[pi][2], accent: pals[pi][3], accent2: pals[pi][4], muted: pals[pi][5] };
    var motifName = MOT[gk][((h >>> 3) % 6 + 6) % 6];
    var paint = MF[motifName] || MF.starfield;
    var layout = (h >>> 6) % 4;
    var fstyle = (h >>> 9) % 3;
    var g = [];

    /* backdrop */
    g.push('<defs>' +
      '<linearGradient id="bg" x1="0" y1="0" x2="0.9" y2="1">' +
      '<stop offset="0" stop-color="' + P.bg1 + '"/><stop offset="1" stop-color="' + P.bg2 + '"/></linearGradient>' +
      '<radialGradient id="vig" cx="0.5" cy="0.42" r="0.9">' +
      '<stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.38"/></radialGradient>' +
      '<filter id="soft" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="16"/></filter>' +
      '</defs>');
    g.push('<rect width="' + W + '" height="' + H + '" fill="url(#bg)"/>');
    /* paper grain */
    for (var gi = 0; gi < 46; gi++) {
      circ(g, rnd() * W, rnd() * H, rf(rnd, 0.6, 1.8), P.fg, rf(rnd, 0.02, 0.06));
    }
    g.push('<rect width="' + W + '" height="' + H + '" fill="url(#vig)"/>');
    frame(g, P, fstyle);

    var cx = W / 2;
    var label = GLABEL[gk] || gk;

    /* title sizing: shrink until it fits in 5 lines */
    var size = 40, lines = [], maxChars = 17;
    while (size >= 24) {
      maxChars = Math.max(10, Math.floor(300 / (size * 0.52)));
      lines = wrapTitle(title, maxChars);
      if (lines.length <= 5) break;
      size -= 3;
    }
    var lh = 1.22, titleH = lines.length * size * lh;

    if (layout === 0) {
      /* classic: imprint / title / divider / motif / author */
      imprint(g, label, cx, 56, P);
      var ty = 108;
      textBlock(g, lines, cx, ty, size, P.fg, SERIF, 'bold', 0.5, lh);
      divider(g, cx, ty + titleH + 18, P, 130);
      paint(g, cx, 400, 118, P, rnd);
      textBlock(g, [String(author).toUpperCase()], cx, 538, 14, P.fg, SANS, 'normal', 3.5);
      textBlock(g, [(id ? id + '  ·  ' : '') + 'JAH BOOK ARCHIVE'], cx, 564, 9.5, P.muted, SANS, 'normal', 2.5);
    } else if (layout === 1) {
      /* band: motif band across the top, title below */
      g.push('<rect x="0" y="0" width="' + W + '" height="212" fill="#000" opacity="0.28"/>');
      paint(g, cx, 106, 105, P, rnd);
      line(g, 40, 224, W - 40, 224, P.accent, 1.6, 0.85);
      imprint(g, label, cx, 262, P);
      var ty1 = 300;
      textBlock(g, lines, cx, ty1, size, P.fg, SERIF, 'bold', 0.5, lh);
      textBlock(g, [String(author).toUpperCase()], cx, 522, 14, P.fg, SANS, 'normal', 3.5);
      textBlock(g, [(id ? id + '  ·  ' : '') + 'JAH BOOK ARCHIVE'], cx, 548, 9.5, P.muted, SANS, 'normal', 2.5);
    } else if (layout === 2) {
      /* bleed: large motif, scrim, title low */
      paint(g, cx, 268, 210, P, rnd);
      g.push('<defs><linearGradient id="scrim" x1="0" y1="0" x2="0" y2="1">' +
        '<stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.72"/></linearGradient></defs>');
      g.push('<rect y="240" width="' + W + '" height="360" fill="url(#scrim)"/>');
      imprint(g, label, cx, 56, P);
      var ty2 = 600 - 210 - titleH;
      g.push('<rect x="34" y="' + fmt(ty2 - 52) + '" width="332" height="' + fmt(titleH + 84) +
        '" rx="20" fill="#000" opacity="0.5" filter="url(#soft)"/>');
      textBlock(g, lines, cx, ty2, size, '#ffffff', SERIF, 'bold', 0.5, lh);
      divider(g, cx, ty2 + titleH + 16, P, 110);
      textBlock(g, [String(author).toUpperCase()], cx, 540, 14, '#ffffff', SANS, 'normal', 3.5);
      textBlock(g, [(id ? id + '  ·  ' : '') + 'JAH BOOK ARCHIVE'], cx, 566, 9.5, P.muted, SANS, 'normal', 2.5);
    } else {
      /* framed emblem: small crest top, centered title, author */
      paint(g, cx, 128, 84, P, rnd);
      divider(g, cx, 196, P, 150);
      var ty3 = 250;
      textBlock(g, lines, cx, ty3, size, P.fg, SERIF, 'bold', 0.5, lh);
      divider(g, cx, ty3 + titleH + 18, P, 110);
      textBlock(g, [String(author).toUpperCase()], cx, 522, 14, P.fg, SANS, 'normal', 3.5);
      textBlock(g, [(id ? id + '  ·  ' : '') + 'JAH BOOK ARCHIVE'], cx, 548, 9.5, P.muted, SANS, 'normal', 2.5);
    }

    return '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="600" viewBox="0 0 400 600" role="img" aria-label="' +
      esc('Book cover: ' + title) + '">' + g.join('') + '</svg>';
  }

  return { generate: generate, version: 'cover-gen-1.0' };
})();

/* node export for verification tooling */
if (typeof module !== 'undefined' && module.exports) { module.exports = BookCover; }
