/* Seeded deterministic generator for Signature Maps. Same seed = same output.
   Shared by the page (window) and by Node tests (module.exports). */
(function (root) {
  'use strict';
  var DATA = {"stops": ["North Gate", "Harbor", "Market Square", "Old Mill", "Hilltop", "River Bridge", "Library", "Station"], "edges": [["North Gate", "Market Square", 2], ["Market Square", "Harbor", 3], ["Market Square", "Old Mill", 4], ["Old Mill", "Hilltop", 3], ["Harbor", "River Bridge", 2], ["River Bridge", "Library", 2], ["Library", "Station", 3], ["Hilltop", "Station", 4], ["North Gate", "River Bridge", 5], ["Market Square", "Library", 5]]};
  function hashStr(s) {
    var h = 2166136261, i;
    s = String(s == null ? '' : s);
    for (i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  var STOP = ['what','does','do','did','is','are','was','were','the','a','an','how','why','when','where','which','who','whom','whose','can','could','would','should','i','you','me','my','it','its','this','that','these','those','of','for','from','to','in','on','at','by','with','about','and','or','but','not','no','yes','please','tell','give','show','there','here','then','than','as','be','been','being','have','has','had','will','shall','may','might','must','your','our','their','his','her','we','they','he','she','am','an'];
  function words(s) { return String(s == null ? '' : s).toLowerCase().match(/[a-z0-9]+/g) || []; }
  function contentWords(s) { return words(s).filter(function (w) { return STOP.indexOf(w) < 0; }); }
  function scoreEntry(q, name, keywords) {
    var qw = words(q), n = words(name), k = words(keywords), s = 0, i, w;
    for (i = 0; i < qw.length; i++) {
      w = qw[i];
      if (n.indexOf(w) < 0 && k.indexOf(w) < 0) return null;
      s += 3 * n.filter(function (x) { return x === w; }).length +
           1 * k.filter(function (x) { return x === w; }).length;
    }
    return s;
  }
  function shuffle(arr, rnd) {
    var a = arr.slice(), i, j, t;
    for (i = a.length - 1; i > 0; i--) { j = Math.floor(rnd() * (i + 1)); t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function genId(seed) { return 'GEN-' + 'MAPS' + '-' + String(100000 + (hashStr(seed) % 900000)); }
  function dijkstra(stops, edges, a, b) {
    var adj = {}, dist = {}, prev = {}, un = stops.slice(), u, i, pair, v, d;
    stops.forEach(function (s) { adj[s] = []; dist[s] = Infinity; });
    edges.forEach(function (e) { adj[e[0]].push([e[1], e[2]]); adj[e[1]].push([e[0], e[2]]); });
    dist[a] = 0;
    while (un.length) {
      un.sort(function (x, y) { return dist[x] - dist[y]; });
      u = un.shift();
      if (u === b) break;
      adj[u].forEach(function (pr) { v = pr[0]; d = pr[1]; if (dist[u] + d < dist[v]) { dist[v] = dist[u] + d; prev[v] = u; } });
    }
    var path = [b], cur = b;
    while (cur !== a) { cur = prev[cur]; path.unshift(cur); }
    return { path: path, distance: dist[b] };
  }
  function make(seed, n) {
    seed = String(seed == null || seed === '' ? 'morning-trail' : seed);
    n = Math.max(1, Math.min(5, parseInt(n, 10) || 3));
    var rnd = mulberry32(hashStr(seed));
    var out = { seed: seed, id: genId(seed), generated: true, label: 'generated — simulated, not an archive record' };
    if ('maps' === 'search') {
      var picked = shuffle(DATA.index, rnd).slice(0, n);
      out.items = picked.map(function (e) {
        var q = words(e[2])[0] || words(e[0])[0];
        var ranked = DATA.index.map(function (x) { return { entry: x, score: scoreEntry(q, x[0], x[2]) }; })
          .filter(function (r) { return r.score !== null; })
          .sort(function (a, b) { return b.score - a.score || (a.entry[0] < b.entry[0] ? -1 : 1); });
        return { query: q, top: ranked[0].entry[0], score: ranked[0].score, link: ranked[0].entry[1] };
      });
    } else if ('maps' === 'encyclopedia') {
      var arts = DATA.articles, trail = [], cur = arts[Math.floor(rnd() * arts.length)];
      trail.push(cur);
      while (trail.length < n) {
        var shared = arts.filter(function (a) {
          return a !== cur && words(a[1]).some(function (w) { return words(cur[1]).indexOf(w) >= 0; });
        });
        if (!shared.length) break;
        cur = shared[Math.floor(rnd() * shared.length)];
        if (trail.indexOf(cur) >= 0) break;
        trail.push(cur);
      }
      out.items = trail.map(function (a) { return { title: a[0], keywords: a[1], summary: a[2] }; });
    } else if ('maps' === 'news') {
      var picked = shuffle(DATA.reports, rnd).slice(0, 5);
      picked.sort(function (a, b) { return b[2] < a[2] ? -1 : (b[2] > a[2] ? 1 : (a[0] < b[0] ? -1 : 1)); });
      out.items = picked.map(function (r) { return { headline: r[0], subject: r[1], date: r[2], body: r[3] }; });
    } else if ('maps' === 'weather') {
      var places = shuffle(DATA.table, rnd).slice(0, 4);
      out.items = places.map(function (p) {
        var days = [0, 1, 2].map(function (d) {
          var shift = Math.floor(rnd() * 5) - 2;
          var t = p[2] + shift;
          var band = t >= 25 ? 'warm' : (t >= 15 ? 'mild' : (t >= 5 ? 'cool' : 'cold'));
          return { day: 'Day ' + (d + 1), temperature: t, feelsLike: t - p[3] / 2, band: band };
        });
        return { place: p[0], condition: p[1], wind: p[3], days: days };
      });
    } else {
      var stops = shuffle(DATA.stops, rnd);
      var a = stops[0], b = stops[1], r = dijkstra(DATA.stops, DATA.edges, a, b);
      out.items = [{ from: a, to: b, route: r.path, distance: r.distance, unit: 'km' }];
    }
    return out;
  }
  var api = { make: make, genId: genId, hashStr: hashStr, scoreEntry: scoreEntry, dijkstra: dijkstra, DATA: DATA };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.MirrorGen = api;
})(typeof window !== 'undefined' ? window : this);
