/* Themed tools for Signature News. Plain JavaScript, no backend, no key.
   Shared by the page (window) and by Node tests (module.exports). */
(function (root) {
  'use strict';
  var DATA = {"reports": [["Network passes one million generator outputs", "Network", "2026-11-10", "The generator archive passed one million outputs. The count is stamped in the archive manifest."], ["New sample articles added to the encyclopedia mirror", "Network", "2026-11-09", "The encyclopedia mirror gained new sample articles this week."], ["Cookbook mirror adds bread and soup pages", "Food", "2026-11-08", "The cookbook mirror gained bread and soup pages this week."], ["Music studio mirror adds song demos", "Music", "2026-11-07", "The music studio mirror gained new song demos this week."], ["Book depository mirror lists new shelf", "Books", "2026-11-06", "The book depository mirror lists a new shelf of sample books."], ["Maps mirror adds sample walking routes", "Maps", "2026-11-05", "The maps mirror gained sample walking routes this week."], ["Science notes: how rain forms", "Science", "2026-11-04", "Rain forms when water vapour cools and gathers into drops."], ["Science notes: why clocks keep time", "Science", "2026-11-03", "A clock keeps time with a steady beat from a spring or a crystal."], ["Food notes: baking bread at home", "Food", "2026-11-02", "Bread needs flour, water, yeast, and heat from an oven."], ["Music notes: how a song is built", "Music", "2026-11-01", "A song is built from a tune, a beat, and words that fit the tune."]]};
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
  function dijkstra(stops, edges, a, b) {
    var adj = {}, dist = {}, prev = {}, un = stops.slice(), u, pair, v, d;
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
  var api = {};
  if ('news' === 'search' || 'news' === 'encyclopedia') {
    api.score = function (q) {
      var list = ('news' === 'search') ? DATA.index.map(function (e) { return { name: e[0], link: e[1], keywords: e[2] }; })
        : DATA.articles.map(function (a) { return { name: a[0], link: '', keywords: a[1], summary: a[2] }; });
      var out = list.map(function (e) { return { entry: e, score: scoreEntry(q, e.name, e.keywords) }; })
        .filter(function (r) { return r.score !== null; })
        .sort(function (a, b) { return b.score - a.score || (a.entry.name < b.entry.name ? -1 : 1); });
      return out;
    };
    api.readingMinutes = function (text) {
      var n = words(text).length;
      return Math.max(1, Math.ceil(n / 200));
    };
  }
  if ('news' === 'news') {
    api.filter = function (q) {
      var qw = words(q), out = [];
      if (!qw.length) return out;
      DATA.reports.forEach(function (r) {
        var hay = words(r[0] + ' ' + r[1] + ' ' + r[3]);
        if (qw.every(function (w) { return hay.indexOf(w) >= 0; })) out.push({ headline: r[0], subject: r[1], date: r[2], body: r[3] });
      });
      out.sort(function (a, b) { return b.date < a.date ? -1 : (b.date > a.date ? 1 : (a.headline < b.headline ? -1 : 1)); });
      return out;
    };
    api.bySubject = function (subject) {
      return DATA.reports.filter(function (r) { return r[1] === subject; })
        .map(function (r) { return { headline: r[0], subject: r[1], date: r[2], body: r[3] }; });
    };
  }
  if ('news' === 'weather') {
    api.forecast = function (place) {
      var row = null;
      DATA.table.forEach(function (r) { if (r[0].toLowerCase() === String(place).toLowerCase()) row = r; });
      if (!row) return null;
      var fl = row[2] - row[3] / 2;
      var band = row[2] >= 25 ? 'warm' : (row[2] >= 15 ? 'mild' : (row[2] >= 5 ? 'cool' : 'cold'));
      return { place: row[0], condition: row[1], temperature: row[2], wind: row[3], feelsLike: fl, band: band,
               sentence: row[0] + ' — ' + row[1] + ', ' + row[2] + ' degrees (' + band + '), feels like ' + fl + '.' };
    };
    api.warmest = function () {
      var best = DATA.table[0];
      DATA.table.forEach(function (r) { if (r[2] > best[2]) best = r; });
      return best[0];
    };
  }
  if ('news' === 'maps') {
    api.route = function (a, b) {
      if (DATA.stops.indexOf(a) < 0 || DATA.stops.indexOf(b) < 0) return null;
      if (a === b) return { path: [a], distance: 0 };
      return dijkstra(DATA.stops, DATA.edges, a, b);
    };
    api.stops = function () { return DATA.stops.slice(); };
  }
  api.DATA = DATA;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.MirrorTools = api;
})(typeof window !== 'undefined' ? window : this);
