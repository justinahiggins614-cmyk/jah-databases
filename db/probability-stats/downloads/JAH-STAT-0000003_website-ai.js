#!/usr/bin/env node
/* JAH Statistics Creator — website Q&A AI for Factorial 2! (JAH-STAT-0000003).
   The same Q&A router as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/probability-stats/records/JAH-STAT-0000003.html, over the same knowledge
   base (this page's records and their cited sources). Run: node <file> "your question"
   Free forever. Part of The 'Merica-L Internet. */
var KB = {"current": {"id": "JAH-STAT-0000003", "title": "Factorial 2!", "family": "probability", "desc": "2! = 2. Factorials count orderings of 2 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 2}, "url": "JAH-STAT-0000003.html"}, "records": [{"id": "JAH-STAT-0000001", "title": "Factorial 0!", "family": "probability", "desc": "0! = 1. Factorials count orderings of 0 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 1}, "url": "JAH-STAT-0000001.html"}, {"id": "JAH-STAT-0000002", "title": "Factorial 1!", "family": "probability", "desc": "1! = 1. Factorials count orderings of 1 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 1}, "url": "JAH-STAT-0000002.html"}, {"id": "JAH-STAT-0000003", "title": "Factorial 2!", "family": "probability", "desc": "2! = 2. Factorials count orderings of 2 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 2}, "url": "JAH-STAT-0000003.html"}, {"id": "JAH-STAT-0000004", "title": "Factorial 3!", "family": "probability", "desc": "3! = 6. Factorials count orderings of 3 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 6}, "url": "JAH-STAT-0000004.html"}, {"id": "JAH-STAT-0000005", "title": "Factorial 4!", "family": "probability", "desc": "4! = 24. Factorials count orderings of 4 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 24}, "url": "JAH-STAT-0000005.html"}, {"id": "JAH-STAT-0000006", "title": "Factorial 5!", "family": "probability", "desc": "5! = 120. Factorials count orderings of 5 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 120}, "url": "JAH-STAT-0000006.html"}, {"id": "JAH-STAT-0000007", "title": "Factorial 6!", "family": "probability", "desc": "6! = 720. Factorials count orderings of 6 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 720}, "url": "JAH-STAT-0000007.html"}, {"id": "JAH-STAT-0000008", "title": "Factorial 7!", "family": "probability", "desc": "7! = 5040. Factorials count orderings of 7 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 5040}, "url": "JAH-STAT-0000008.html"}, {"id": "JAH-STAT-0000009", "title": "Factorial 8!", "family": "probability", "desc": "8! = 40320. Factorials count orderings of 8 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 40320}, "url": "JAH-STAT-0000009.html"}, {"id": "JAH-STAT-0000010", "title": "Factorial 9!", "family": "probability", "desc": "9! = 362880. Factorials count orderings of 9 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 362880}, "url": "JAH-STAT-0000010.html"}, {"id": "JAH-STAT-0000011", "title": "Factorial 10!", "family": "probability", "desc": "10! = 3628800. Factorials count orderings of 10 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 3628800}, "url": "JAH-STAT-0000011.html"}, {"id": "JAH-STAT-0000012", "title": "Factorial 11!", "family": "probability", "desc": "11! = 39916800. Factorials count orderings of 11 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 39916800}, "url": "JAH-STAT-0000012.html"}, {"id": "JAH-STAT-0000013", "title": "Factorial 12!", "family": "probability", "desc": "12! = 479001600. Factorials count orderings of 12 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 479001600}, "url": "JAH-STAT-0000013.html"}, {"id": "JAH-STAT-0000014", "title": "Factorial 13!", "family": "probability", "desc": "13! = 6227020800. Factorials count orderings of 13 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 6227020800}, "url": "JAH-STAT-0000014.html"}, {"id": "JAH-STAT-0000015", "title": "Factorial 14!", "family": "probability", "desc": "14! = 87178291200. Factorials count orderings of 14 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 87178291200}, "url": "JAH-STAT-0000015.html"}, {"id": "JAH-STAT-0000016", "title": "Factorial 15!", "family": "probability", "desc": "15! = 1307674368000. Factorials count orderings of 15 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 1307674368000}, "url": "JAH-STAT-0000016.html"}, {"id": "JAH-STAT-0000017", "title": "Factorial 16!", "family": "probability", "desc": "16! = 20922789888000. Factorials count orderings of 16 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 20922789888000}, "url": "JAH-STAT-0000017.html"}, {"id": "JAH-STAT-0000018", "title": "Factorial 17!", "family": "probability", "desc": "17! = 355687428096000. Factorials count orderings of 17 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 355687428096000}, "url": "JAH-STAT-0000018.html"}, {"id": "JAH-STAT-0000019", "title": "Factorial 18!", "family": "probability", "desc": "18! = 6402373705728000. Factorials count orderings of 18 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 6402373705728000}, "url": "JAH-STAT-0000019.html"}, {"id": "JAH-STAT-0000020", "title": "Factorial 19!", "family": "probability", "desc": "19! = 121645100408832000. Factorials count orderings of 19 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 121645100408832000}, "url": "JAH-STAT-0000020.html"}, {"id": "JAH-STAT-0000021", "title": "Factorial 20!", "family": "probability", "desc": "20! = 2432902008176640000. Factorials count orderings of 20 distinct objects.", "spec": {"mechanism": "factorial"}, "key_figures": {"output": 2432902008176640000}, "url": "JAH-STAT-0000021.html"}, {"id": "JAH-STAT-0000022", "title": "C(0,0) = 1", "family": "probability", "desc": "C(0,0) = 1", "spec": {"mechanism": "ncr"}, "key_figures": {"output": 1}, "url": "JAH-STAT-0000022.html"}, {"id": "JAH-STAT-0000023", "title": "C(1,0) = 1", "family": "probability", "desc": "C(1,0) = 1", "spec": {"mechanism": "ncr"}, "key_figures": {"output": 1}, "url": "JAH-STAT-0000023.html"}, {"id": "JAH-STAT-0000024", "title": "C(1,1) = 1", "family": "probability", "desc": "C(1,1) = 1", "spec": {"mechanism": "ncr"}, "key_figures": {"output": 1}, "url": "JAH-STAT-0000024.html"}], "twin": {"id": "probability-stats-signature", "title": "JAH Probability and Statistics Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-STAT-GEN-"};
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
console.log(answerQuestion(q, KB, "JAH Statistics Creator"));
