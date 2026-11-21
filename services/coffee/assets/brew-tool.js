/* Coffee brew-ratio tool — pure functions (no DOM), so they can be tested in Node.
   Ratios are the archive's own figures (JAH Coffee Guide Database records):
   pour over 1:16 (JAH-COF-000011), Chemex 1:16 (JAH-COF-000012),
   french press 1:14 (JAH-COF-000013), AeroPress 1:13 (JAH-COF-000014),
   cold brew 1:8 (JAH-COF-000009), Turkish 1:10 (JAH-COF-000016),
   espresso 1:2 (JAH-COF-000001). The 1:15 and 1:17 presets are the
   standard pour-over range either side of the archive's 1:16. */
var BREW_PRESETS = {
  'pour-over':   {label: 'Pour over (V60)', ratio: 16, grind: 'medium-fine', time: '3 min'},
  'chemex':      {label: 'Chemex', ratio: 16, grind: 'medium-coarse', time: '4 min'},
  'french-press':{label: 'French press', ratio: 14, grind: 'coarse', time: '4 min'},
  'aeropress':   {label: 'AeroPress', ratio: 13, grind: 'fine-medium', time: '2 min'},
  'cold-brew':   {label: 'Cold brew', ratio: 8, grind: 'coarse', time: '12-24 hours'},
  'turkish':     {label: 'Turkish coffee', ratio: 10, grind: 'powder', time: '3 min'},
  'espresso':    {label: 'Espresso', ratio: 2, grind: 'fine', time: '25-30 sec'},
  'moka':        {label: 'Moka pot', ratio: 10, grind: 'fine-medium', time: '5 min'}
};
function brewWater(coffeeGrams, ratio) {
  var c = Number(coffeeGrams), r = Number(ratio);
  if (!isFinite(c) || !isFinite(r)) return {ok: false, error: 'Enter numbers for coffee and ratio.'};
  if (c <= 0) return {ok: false, error: 'Coffee must be more than 0 grams.'};
  if (r <= 0) return {ok: false, error: 'Ratio must be more than 0.'};
  if (c > 1000) return {ok: false, error: 'That is more than 1,000 g of coffee — check the amount.'};
  return {ok: true, water: Math.round(c * r * 10) / 10};
}
function brewCoffee(waterGrams, ratio) {
  var w = Number(waterGrams), r = Number(ratio);
  if (!isFinite(w) || !isFinite(r)) return {ok: false, error: 'Enter numbers for water and ratio.'};
  if (w <= 0) return {ok: false, error: 'Water must be more than 0 grams.'};
  if (r <= 0) return {ok: false, error: 'Ratio must be more than 0.'};
  return {ok: true, coffee: Math.round((w / r) * 10) / 10};
}
function brewSummary(coffeeGrams, ratio) {
  var res = brewWater(coffeeGrams, ratio);
  if (!res.ok) return res;
  return {ok: true, water: res.water,
    text: coffeeGrams + ' g of coffee at 1:' + ratio + ' needs ' + res.water + ' g of water.'};
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {brewWater: brewWater, brewCoffee: brewCoffee, brewSummary: brewSummary, BREW_PRESETS: BREW_PRESETS};
}
