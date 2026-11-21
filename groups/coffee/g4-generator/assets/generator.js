/* Coffee blend generator — deterministic and seeded. The same seed always
   makes the same blends. Everything it emits is a GENERATED blend record,
   labelled generated, never presented as an archive record. Methods, grinds,
   ratios and roast notes come from the JAH Coffee Guide Database records
   (JAH-COF-000001..000030); bean origins are the generator's own option list. */
var GEN_ORIGINS = ['Brazil', 'Ethiopia', 'Colombia', 'Kenya', 'Sumatra', 'Guatemala'];
var GEN_NOTES = {
  'Brazil': 'nutty, chocolate, low acid', 'Ethiopia': 'floral, bergamot, bright',
  'Colombia': 'caramel, red apple, balanced', 'Kenya': 'blackcurrant, winey, bright',
  'Sumatra': 'earthy, dark chocolate, heavy', 'Guatemala': 'cocoa, spice, smoky'
};
var GEN_ROASTS = [
  {name: 'Light roast', note: 'keeps origin character: bright, tea-like'},
  {name: 'Medium roast', note: 'balances origin and caramel: the crowd-pleaser'},
  {name: 'Dark roast', note: 'roast flavour forward: smoky, bold, low acid'}
];
var GEN_METHODS = [
  {name: 'Pour over (V60)', ratio: 16, grind: 'medium-fine', time: '3 min'},
  {name: 'French press', ratio: 14, grind: 'coarse', time: '4 min'},
  {name: 'Espresso', ratio: 2, grind: 'fine', time: '25-30 sec'},
  {name: 'Cold brew', ratio: 8, grind: 'coarse', time: '12-24 hours'},
  {name: 'Chemex', ratio: 16, grind: 'medium-coarse', time: '4 min'},
  {name: 'AeroPress', ratio: 13, grind: 'fine-medium', time: '2 min'}
];
function genHash(str) {
  var h = 2166136261;
  str = String(str == null ? '' : str);
  for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); }
  return h >>> 0;
}
function genPrng(seed) {
  var a = genHash(seed);
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    var t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function genBlend(seed, index) {
  var rnd = genPrng(seed + ':' + index);
  var o1 = GEN_ORIGINS[Math.floor(rnd() * GEN_ORIGINS.length)];
  var o2 = GEN_ORIGINS[Math.floor(rnd() * GEN_ORIGINS.length)];
  if (o2 === o1) o2 = GEN_ORIGINS[(GEN_ORIGINS.indexOf(o1) + 3) % GEN_ORIGINS.length];
  var pct1 = 50 + Math.floor(rnd() * 5) * 10; /* 50, 60, 70, 80 or 90 */
  var roast = GEN_ROASTS[Math.floor(rnd() * GEN_ROASTS.length)];
  var method = GEN_METHODS[Math.floor(rnd() * GEN_METHODS.length)];
  var dose = 15 + Math.floor(rnd() * 11); /* 15-25 g */
  var id = 'JAH-COFGEN-' + String(100000 + (genHash(seed + ':' + index) % 900000));
  return {
    id: id, seed: String(seed), index: index,
    title: pct1 + '% ' + o1 + ' + ' + (100 - pct1) + '% ' + o2 + ' — ' + roast.name,
    beans: pct1 + '% Arabica ' + o1 + ' (' + GEN_NOTES[o1] + '), ' + (100 - pct1) + '% Arabica ' + o2 + ' (' + GEN_NOTES[o2] + ')',
    roast: roast.name, roastNote: roast.note,
    method: method.name, ratio: '1:' + method.ratio, grind: method.grind, time: method.time,
    dose: dose, water: dose * method.ratio,
    steps: 'Grind ' + dose + ' g ' + method.grind + '. ' + method.name + ' at 1:' + method.ratio +
      ' — ' + (dose * method.ratio) + ' g water at 90-96 C. Brew ' + method.time + '.',
    generated: true
  };
}
function genBlends(seed, count) {
  var n = Math.floor(Number(count));
  if (!isFinite(n) || n < 1) n = 1;
  if (n > 5) n = 5;
  if (String(seed == null ? '' : seed).trim() === '') seed = 'morning-cup';
  var out = [];
  for (var i = 0; i < n; i++) out.push(genBlend(seed, i + 1));
  return out;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {genBlend: genBlend, genBlends: genBlends, genHash: genHash};
}
