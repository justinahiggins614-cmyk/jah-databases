#!/usr/bin/env node
/* JAH Recipe Librarian — website Q&A AI for Guacamole (JAH-RECIPE-000001).
   The same Q&A router as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/cookbook/records/JAH-RECIPE-000001.html, over the same knowledge
   base (this page's records and their cited sources). Run: node <file> "your question"
   Free forever. Part of The 'Merica-L Internet. */
var KB = {"current": {"id": "JAH-RECIPE-000001", "title": "Guacamole", "family": "recipe", "desc": "Guacamole", "spec": {"mechanism": "Guacamole"}, "key_figures": {"cook_min": 0, "prep_min": 10, "servings": 6, "total_min": 10}, "url": "JAH-RECIPE-000001.html"}, "records": [{"id": "JAH-RECIPE-000001", "title": "Guacamole", "family": "recipe", "desc": "Guacamole", "spec": {"mechanism": "Guacamole"}, "key_figures": {"cook_min": 0, "prep_min": 10, "servings": 6, "total_min": 10}, "url": "JAH-RECIPE-000001.html"}, {"id": "JAH-RECIPE-000002", "title": "Classic Hummus", "family": "recipe", "desc": "Classic Hummus", "spec": {"mechanism": "Classic Hummus"}, "key_figures": {"cook_min": 0, "prep_min": 10, "servings": 4, "total_min": 10}, "url": "JAH-RECIPE-000002.html"}, {"id": "JAH-RECIPE-000003", "title": "Deviled Eggs", "family": "recipe", "desc": "Deviled Eggs", "spec": {"mechanism": "Deviled Eggs"}, "key_figures": {"cook_min": 20, "prep_min": 20, "servings": 2, "total_min": 40}, "url": "JAH-RECIPE-000003.html"}, {"id": "JAH-RECIPE-000004", "title": "Bruschetta", "family": "recipe", "desc": "Bruschetta", "spec": {"mechanism": "Bruschetta"}, "key_figures": {"cook_min": 12, "prep_min": 20, "servings": 4, "total_min": 32}, "url": "JAH-RECIPE-000004.html"}, {"id": "JAH-RECIPE-000005", "title": "Chicken Noodle Soup", "family": "recipe", "desc": "Chicken Noodle Soup", "spec": {"mechanism": "Chicken Noodle Soup"}, "key_figures": {"cook_min": 50, "prep_min": 15, "servings": 4, "total_min": 65}, "url": "JAH-RECIPE-000005.html"}, {"id": "JAH-RECIPE-000006", "title": "Tomato Soup", "family": "recipe", "desc": "Tomato Soup", "spec": {"mechanism": "Tomato Soup"}, "key_figures": {"cook_min": 30, "prep_min": 15, "servings": 2, "total_min": 45}, "url": "JAH-RECIPE-000006.html"}, {"id": "JAH-RECIPE-000007", "title": "Beef Stew", "family": "recipe", "desc": "Beef Stew", "spec": {"mechanism": "Beef Stew"}, "key_figures": {"cook_min": 40, "prep_min": 15, "servings": 4, "total_min": 55}, "url": "JAH-RECIPE-000007.html"}, {"id": "JAH-RECIPE-000008", "title": "Caesar Salad", "family": "recipe", "desc": "Caesar Salad", "spec": {"mechanism": "Caesar Salad"}, "key_figures": {"cook_min": 0, "prep_min": 15, "servings": 4, "total_min": 15}, "url": "JAH-RECIPE-000008.html"}, {"id": "JAH-RECIPE-000009", "title": "Greek Salad", "family": "recipe", "desc": "Greek Salad", "spec": {"mechanism": "Greek Salad"}, "key_figures": {"cook_min": 0, "prep_min": 15, "servings": 4, "total_min": 15}, "url": "JAH-RECIPE-000009.html"}, {"id": "JAH-RECIPE-000010", "title": "Roast Chicken", "family": "recipe", "desc": "Roast Chicken", "spec": {"mechanism": "Roast Chicken"}, "key_figures": {"cook_min": 45, "prep_min": 15, "servings": 2, "total_min": 60}, "url": "JAH-RECIPE-000010.html"}, {"id": "JAH-RECIPE-000011", "title": "Chicken Stir-Fry", "family": "recipe", "desc": "Chicken Stir-Fry", "spec": {"mechanism": "Chicken Stir-Fry"}, "key_figures": {"cook_min": 75, "prep_min": 15, "servings": 2, "total_min": 90}, "url": "JAH-RECIPE-000011.html"}, {"id": "JAH-RECIPE-000012", "title": "Spaghetti Bolognese", "family": "recipe", "desc": "Spaghetti Bolognese", "spec": {"mechanism": "Spaghetti Bolognese"}, "key_figures": {"cook_min": 20, "prep_min": 10, "servings": 4, "total_min": 30}, "url": "JAH-RECIPE-000012.html"}, {"id": "JAH-RECIPE-000013", "title": "Lasagna", "family": "recipe", "desc": "Lasagna", "spec": {"mechanism": "Lasagna"}, "key_figures": {"cook_min": 20, "prep_min": 10, "servings": 4, "total_min": 30}, "url": "JAH-RECIPE-000013.html"}, {"id": "JAH-RECIPE-000014", "title": "Baked Salmon", "family": "recipe", "desc": "Baked Salmon", "spec": {"mechanism": "Baked Salmon"}, "key_figures": {"cook_min": 12, "prep_min": 10, "servings": 4, "total_min": 22}, "url": "JAH-RECIPE-000014.html"}, {"id": "JAH-RECIPE-000015", "title": "Meatloaf", "family": "recipe", "desc": "Meatloaf", "spec": {"mechanism": "Meatloaf"}, "key_figures": {"cook_min": 75, "prep_min": 15, "servings": 2, "total_min": 90}, "url": "JAH-RECIPE-000015.html"}, {"id": "JAH-RECIPE-000016", "title": "Mashed Potatoes", "family": "recipe", "desc": "Mashed Potatoes", "spec": {"mechanism": "Mashed Potatoes"}, "key_figures": {"cook_min": 35, "prep_min": 10, "servings": 2, "total_min": 45}, "url": "JAH-RECIPE-000016.html"}, {"id": "JAH-RECIPE-000017", "title": "Roasted Broccoli", "family": "recipe", "desc": "Roasted Broccoli", "spec": {"mechanism": "Roasted Broccoli"}, "key_figures": {"cook_min": 20, "prep_min": 10, "servings": 6, "total_min": 30}, "url": "JAH-RECIPE-000017.html"}, {"id": "JAH-RECIPE-000018", "title": "Rice Pilaf", "family": "recipe", "desc": "Rice Pilaf", "spec": {"mechanism": "Rice Pilaf"}, "key_figures": {"cook_min": 23, "prep_min": 5, "servings": 6, "total_min": 28}, "url": "JAH-RECIPE-000018.html"}, {"id": "JAH-RECIPE-000019", "title": "Banana Bread", "family": "recipe", "desc": "Banana Bread", "spec": {"mechanism": "Banana Bread"}, "key_figures": {"cook_min": 60, "prep_min": 15, "servings": 10, "total_min": 75}, "url": "JAH-RECIPE-000019.html"}, {"id": "JAH-RECIPE-000020", "title": "Garlic Bread", "family": "recipe", "desc": "Garlic Bread", "spec": {"mechanism": "Garlic Bread"}, "key_figures": {"cook_min": 12, "prep_min": 25, "servings": 4, "total_min": 37}, "url": "JAH-RECIPE-000020.html"}, {"id": "JAH-RECIPE-000021", "title": "Dinner Rolls", "family": "recipe", "desc": "Dinner Rolls", "spec": {"mechanism": "Dinner Rolls"}, "key_figures": {"cook_min": 115, "prep_min": 30, "servings": 12, "total_min": 145}, "url": "JAH-RECIPE-000021.html"}, {"id": "JAH-RECIPE-000022", "title": "Chocolate Chip Cookies", "family": "recipe", "desc": "Chocolate Chip Cookies", "spec": {"mechanism": "Chocolate Chip Cookies"}, "key_figures": {"cook_min": 12, "prep_min": 15, "servings": 10, "total_min": 27}, "url": "JAH-RECIPE-000022.html"}, {"id": "JAH-RECIPE-000023", "title": "Vanilla Cake", "family": "recipe", "desc": "Vanilla Cake", "spec": {"mechanism": "Vanilla Cake"}, "key_figures": {"cook_min": 28, "prep_min": 20, "servings": 12, "total_min": 48}, "url": "JAH-RECIPE-000023.html"}, {"id": "JAH-RECIPE-000024", "title": "Apple Pie", "family": "recipe", "desc": "Apple Pie", "spec": {"mechanism": "Apple Pie"}, "key_figures": {"cook_min": 40, "prep_min": 25, "servings": 10, "total_min": 65}, "url": "JAH-RECIPE-000024.html"}], "twin": {"id": "cookbook-signature", "title": "The Signature Cookbook Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-RECIPE-GEN-"};
function norm(s){ return (s || '').toLowerCase().replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim(); }
function toks(s){ return norm(s).split(' ').filter(function(w){ return w.length > 1; }); }
var STOPWORDS = {what:1,is:1,the:1,of:1,a:1,an:1,and:1,or:1,to:1,in:1,on:1,for:1,how:1,does:1,do:1,did:1,can:1,could:1,would:1,should:1,it:1,its:1,this:1,that:1,there:1,here:1,me:1,my:1,you:1,your:1,please:1,tell:1,about:1,show:1,give:1,get:1,with:1,by:1,from:1,at:1,as:1,be:1,are:1,was:1,were:1,has:1,have:1,had:1,i:1,we:1,they:1,he:1,she:1,who:1,whom:1,whose:1,which:1,when:1,where:1,why:1,not:1,no:1,yes:1,if:1,then:1,than:1,so:1,such:1,any:1,some:1,all:1,each:1,every:1,other:1,another:1,more:1,most:1,many:1,much:1,few:1,little:1,own:1,same:1,too:1,very:1,just:1,also:1,only:1,even:1,still:1,already:1,now:1};
function scoreRec(q, rec){
  var hay = norm((rec.title || '') + ' ' + (rec.family || '') + ' ' + (rec.desc || '') + ' ' + (rec.spec || ''));
  var qT = toks(q).filter(function(w){ return !STOPWORDS[w]; }), hT = toks(hay);
  var sc = 0;
  qT.forEach(function(w){ if (hT.indexOf(w) >= 0) sc += 2; else if (hay.indexOf(w) >= 0) sc += 1; });
  return sc;
}
function answerQuestion(q, kb, persona){
  var nq = norm(q);
  if (!nq) return 'Ask me something about this page — a record, a number, a material, a step.';
  if (kb && kb.legal && /\blegal\b|\blaw\b|\bjurisdiction\b/.test(nq)) return kb.legal;
  if (/\bdownload\b/.test(nq)) return 'Every download on this page is a real file: the full record, the demo program, the full program, the spec sheet, the complete file, and both downloadable AIs with their spec sheets. See section 8, Use, download, copy — all free forever.';
  if (/\bcopy\b/.test(nq)) return 'Use the Copy-all button in section 8. It copies the full record text, including the demo code, with its sources attached.';
  if (/\bread aloud\b|\bread this\b|\blisten\b/.test(nq)) return 'Press the Read aloud button at the top of the page. It reads the whole page aloud and stops when you press Stop reading.';
  if (/\bgenerat|\bscale\b|\bbigger\b|\bsmaller\b|\bvariant\b/.test(nq)) return 'Use the boundless generator in section 8: pick a seed (1 to 999,999,999) or a pocket / standard / workshop scale and press Generate. The generator ceiling is 1,000,000,000 scales per file.';
  if (/\bsources?\b|\bcitation\b|\bwhere.*from\b/.test(nq)) {
    if (kb && kb.sources && kb.sources.length) return 'Sources for this record: ' + kb.sources.map(function(s){ return s.text ? (s.title + ': ' + s.text.slice(0, 300)) : (s.title + ' — ' + s.url); }).join('; ') + '.';
    return 'This record carries no external source list in the archive. Its provenance is the archive itself, stated on the page.';
  }
  if (/\btwin\b|\bsignature\b|\bpublic version\b/.test(nq)) {
    if (kb && kb.twin) return 'The twin edition is ' + kb.twin.title + ' (' + kb.twin.id + '). Open it here: ' + kb.twin.url;
    return 'This page has no twin edition.';
  }
  var recs = (kb && kb.records) || ((kb && kb.current) ? [kb.current] : []);
  var best = null, bestSc = 0;
  recs.forEach(function(r){ var s = scoreRec(q, r); if (s > bestSc) { bestSc = s; best = r; } });
  var explicitRef = /\bthis\b|\bit\b|\bthe (record|thing|item|entry|database|archive|mix|program|file|option|supply)\b/.test(nq);
  var target = best;
  if (!target && kb && kb.current && explicitRef) target = kb.current;
  if (target && (bestSc > 0 || explicitRef)) {
    var spec = target.spec || {};
    if (/\bdimension|\bsize\b|\bhow big|\bhow tall|\bhow wide|\bdiameter\b/.test(nq) && spec.dimensions) return target.title + ' — dimensions: ' + spec.dimensions;
    if (/\bmaterial|\bmade of|\bmade from\b/.test(nq) && spec.materials) return target.title + ' — materials: ' + spec.materials;
    if (/\bmechanism|\bhow.*work|\bhow does\b/.test(nq) && spec.mechanism) return target.title + ' — mechanism: ' + spec.mechanism;
    if (/\buse\b|\bhow.*use\b|\bhow to use\b/.test(nq) && spec.use) return target.title + ' — use: ' + spec.use;
    if (/\bcare\b|\bclean\b/.test(nq) && spec.care) return target.title + ' — care: ' + spec.care;
    if (/\bvariant|\bversion\b/.test(nq) && spec.variants) return target.title + ' — variants: ' + spec.variants;
    if (/\bdemo\b|\bprogram\b|\bcalculat|\bcompute\b/.test(nq)) return 'The demo for ' + target.title + ' is in section 6. Run it from the download, or use the live calculator on this page — it runs the record\u2019s own numbers in your browser and matches the record\u2019s official output exactly at the record\u2019s own inputs.';
    if (/\bwhat is\b|\bwhat.*(this|that)\b|\btell me about\b/.test(nq) || bestSc > 0) {
      var ans = target.title + ': ' + (target.desc || '');
      if (target.url) ans += ' Full record: ' + target.url;
      return ans;
    }
  }
  if (recs.length > 1) return 'I answer only from this page\u2019s own records. Try asking about a record by name, a material, a dimension, a mechanism, or a use — or ask for the full list.';
  return 'That goes outside what this page\u2019s records cover. I answer only from this page\u2019s own records and their cited sources, and I say so plainly when a question goes outside them.';
}

var q = process.argv.slice(2).join(' ');
if (!q) { console.log('Usage: node ' + process.argv[1] + ' "your question"');
  console.log('Example: node ' + process.argv[1] + ' "What is this record made of?"');
  console.log('This AI answers only from this page\u2019s own records and their cited sources.');
  process.exit(0); }
console.log(answerQuestion(q, KB, "JAH Recipe Librarian"));
