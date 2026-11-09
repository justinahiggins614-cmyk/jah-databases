#!/usr/bin/env node
/* JAH Automotive Database — Signature edition — AI version of the database JAH Automotive Database — Signature edition (automotive-signature).
   The database itself, as an AI: answers questions as the database,
   from the database's own records and their cited sources, using the
   same Q&A router as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/automotive/website/mirror/index.html. Run: node <file> "your question"
   Free forever. Part of The 'Merica-L Internet. */
var KB = {"records": [{"id": "JAH-AUTO-SIG-000001", "title": "Signature Alignment Signs (overview)", "family": "signature automotive creation", "desc": "Signature Alignment Signs (overview)", "spec": {"mechanism": "Signature Alignment Signs (overview)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000002", "title": "Signature Tire Change Drill (detailed)", "family": "signature automotive creation", "desc": "Signature Tire Change Drill (detailed)", "spec": {"mechanism": "Signature Tire Change Drill (detailed)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000003", "title": "Signature Tire Change Drill (overview)", "family": "signature automotive creation", "desc": "Signature Tire Change Drill (overview)", "spec": {"mechanism": "Signature Tire Change Drill (overview)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000004", "title": "Signature Teen Driver Prep (detailed)", "family": "signature automotive creation", "desc": "Signature Teen Driver Prep (detailed)", "spec": {"mechanism": "Signature Teen Driver Prep (detailed)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000005", "title": "Signature Charging Setup (history)", "family": "signature automotive creation", "desc": "Signature Charging Setup (history)", "spec": {"mechanism": "Signature Charging Setup (history)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000006", "title": "Signature Fuel Log (overview)", "family": "signature automotive creation", "desc": "Signature Fuel Log (overview)", "spec": {"mechanism": "Signature Fuel Log (overview)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000007", "title": "Signature Oil Change Ritual (overview)", "family": "signature automotive creation", "desc": "Signature Oil Change Ritual (overview)", "spec": {"mechanism": "Signature Oil Change Ritual (overview)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000008", "title": "Signature Battery Care (faq)", "family": "signature automotive creation", "desc": "Signature Battery Care (faq)", "spec": {"mechanism": "Signature Battery Care (faq)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000009", "title": "Signature OBD-II Reading (applications)", "family": "signature automotive creation", "desc": "Signature OBD-II Reading (applications)", "spec": {"mechanism": "Signature OBD-II Reading (applications)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000010", "title": "Signature Winter Prep (applications)", "family": "signature automotive creation", "desc": "Signature Winter Prep (applications)", "spec": {"mechanism": "Signature Winter Prep (applications)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000011", "title": "Signature Winter Prep (faq)", "family": "signature automotive creation", "desc": "Signature Winter Prep (faq)", "spec": {"mechanism": "Signature Winter Prep (faq)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000012", "title": "Signature Jump Start Safety (overview)", "family": "signature automotive creation", "desc": "Signature Jump Start Safety (overview)", "spec": {"mechanism": "Signature Jump Start Safety (overview)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000013", "title": "Signature Noise Diagnosis (examples)", "family": "signature automotive creation", "desc": "Signature Noise Diagnosis (examples)", "spec": {"mechanism": "Signature Noise Diagnosis (examples)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000014", "title": "Signature Interior Detailing (examples)", "family": "signature automotive creation", "desc": "Signature Interior Detailing (examples)", "spec": {"mechanism": "Signature Interior Detailing (examples)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000015", "title": "Signature Used Car Inspection (examples)", "family": "signature automotive creation", "desc": "Signature Used Car Inspection (examples)", "spec": {"mechanism": "Signature Used Car Inspection (examples)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000016", "title": "Signature EV Basics (detailed)", "family": "signature automotive creation", "desc": "Signature EV Basics (detailed)", "spec": {"mechanism": "Signature EV Basics (detailed)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000017", "title": "Signature Wiper Wisdom (faq)", "family": "signature automotive creation", "desc": "Signature Wiper Wisdom (faq)", "spec": {"mechanism": "Signature Wiper Wisdom (faq)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000018", "title": "Signature Tire Literacy (detailed)", "family": "signature automotive creation", "desc": "Signature Tire Literacy (detailed)", "spec": {"mechanism": "Signature Tire Literacy (detailed)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000019", "title": "Signature Tire Change Drill (examples)", "family": "signature automotive creation", "desc": "Signature Tire Change Drill (examples)", "spec": {"mechanism": "Signature Tire Change Drill (examples)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}, {"id": "JAH-AUTO-SIG-000020", "title": "Signature Headlight Restoration (examples)", "family": "signature automotive creation", "desc": "Signature Headlight Restoration (examples)", "spec": {"mechanism": "Signature Headlight Restoration (examples)"}, "key_figures": {}, "url": "../../../automotive-signature/index.html"}], "twin": {"id": "automotive", "title": "JAH Automotive Database", "url": "../index.html"}, "sources": [], "gen_prefix": "JAH-AUTO-SIGGEN-"};
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
  console.log('Example: node ' + process.argv[1] + ' "What records does this database hold?"');
  console.log('This AI answers only from this database\u2019s own records and their cited sources.');
  process.exit(0); }
console.log(answerQuestion(q, KB, "JAH Automotive Database \u2014 Signature edition"));
