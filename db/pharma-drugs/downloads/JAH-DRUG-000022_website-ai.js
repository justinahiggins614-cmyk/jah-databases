#!/usr/bin/env node
/* JAH Pharma Librarian — website Q&A AI for JAH-DRUG-000022 (JAH-DRUG-000022).
   The same Q&A router as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/pharma-drugs/records/JAH-DRUG-000022.html, over the same knowledge
   base (this page's records and their cited sources). Run: node <file> "your question"
   Free forever. Part of The 'Merica-L Internet. */
var KB = {"current": {"id": "JAH-DRUG-000022", "title": "JAH-DRUG-000022", "family": "drug record", "desc": "JAH-DRUG-000022", "spec": {"mechanism": "JAH-DRUG-000022"}, "key_figures": {}, "url": "JAH-DRUG-000022.html"}, "records": [{"id": "JAH-DRUG-000001", "title": "JAH-DRUG-000001", "family": "drug record", "desc": "JAH-DRUG-000001", "spec": {"mechanism": "JAH-DRUG-000001"}, "key_figures": {}, "url": "JAH-DRUG-000001.html"}, {"id": "JAH-DRUG-000002", "title": "JAH-DRUG-000002", "family": "drug record", "desc": "JAH-DRUG-000002", "spec": {"mechanism": "JAH-DRUG-000002"}, "key_figures": {}, "url": "JAH-DRUG-000002.html"}, {"id": "JAH-DRUG-000003", "title": "JAH-DRUG-000003", "family": "drug record", "desc": "JAH-DRUG-000003", "spec": {"mechanism": "JAH-DRUG-000003"}, "key_figures": {}, "url": "JAH-DRUG-000003.html"}, {"id": "JAH-DRUG-000004", "title": "JAH-DRUG-000004", "family": "drug record", "desc": "JAH-DRUG-000004", "spec": {"mechanism": "JAH-DRUG-000004"}, "key_figures": {}, "url": "JAH-DRUG-000004.html"}, {"id": "JAH-DRUG-000005", "title": "JAH-DRUG-000005", "family": "drug record", "desc": "JAH-DRUG-000005", "spec": {"mechanism": "JAH-DRUG-000005"}, "key_figures": {}, "url": "JAH-DRUG-000005.html"}, {"id": "JAH-DRUG-000006", "title": "JAH-DRUG-000006", "family": "drug record", "desc": "JAH-DRUG-000006", "spec": {"mechanism": "JAH-DRUG-000006"}, "key_figures": {}, "url": "JAH-DRUG-000006.html"}, {"id": "JAH-DRUG-000007", "title": "JAH-DRUG-000007", "family": "drug record", "desc": "JAH-DRUG-000007", "spec": {"mechanism": "JAH-DRUG-000007"}, "key_figures": {}, "url": "JAH-DRUG-000007.html"}, {"id": "JAH-DRUG-000008", "title": "JAH-DRUG-000008", "family": "drug record", "desc": "JAH-DRUG-000008", "spec": {"mechanism": "JAH-DRUG-000008"}, "key_figures": {}, "url": "JAH-DRUG-000008.html"}, {"id": "JAH-DRUG-000009", "title": "JAH-DRUG-000009", "family": "drug record", "desc": "JAH-DRUG-000009", "spec": {"mechanism": "JAH-DRUG-000009"}, "key_figures": {}, "url": "JAH-DRUG-000009.html"}, {"id": "JAH-DRUG-000010", "title": "JAH-DRUG-000010", "family": "drug record", "desc": "JAH-DRUG-000010", "spec": {"mechanism": "JAH-DRUG-000010"}, "key_figures": {}, "url": "JAH-DRUG-000010.html"}, {"id": "JAH-DRUG-000011", "title": "JAH-DRUG-000011", "family": "drug record", "desc": "JAH-DRUG-000011", "spec": {"mechanism": "JAH-DRUG-000011"}, "key_figures": {}, "url": "JAH-DRUG-000011.html"}, {"id": "JAH-DRUG-000012", "title": "JAH-DRUG-000012", "family": "drug record", "desc": "JAH-DRUG-000012", "spec": {"mechanism": "JAH-DRUG-000012"}, "key_figures": {}, "url": "JAH-DRUG-000012.html"}, {"id": "JAH-DRUG-000013", "title": "JAH-DRUG-000013", "family": "drug record", "desc": "JAH-DRUG-000013", "spec": {"mechanism": "JAH-DRUG-000013"}, "key_figures": {}, "url": "JAH-DRUG-000013.html"}, {"id": "JAH-DRUG-000014", "title": "JAH-DRUG-000014", "family": "drug record", "desc": "JAH-DRUG-000014", "spec": {"mechanism": "JAH-DRUG-000014"}, "key_figures": {}, "url": "JAH-DRUG-000014.html"}, {"id": "JAH-DRUG-000015", "title": "JAH-DRUG-000015", "family": "drug record", "desc": "JAH-DRUG-000015", "spec": {"mechanism": "JAH-DRUG-000015"}, "key_figures": {}, "url": "JAH-DRUG-000015.html"}, {"id": "JAH-DRUG-000016", "title": "JAH-DRUG-000016", "family": "drug record", "desc": "JAH-DRUG-000016", "spec": {"mechanism": "JAH-DRUG-000016"}, "key_figures": {}, "url": "JAH-DRUG-000016.html"}, {"id": "JAH-DRUG-000017", "title": "JAH-DRUG-000017", "family": "drug record", "desc": "JAH-DRUG-000017", "spec": {"mechanism": "JAH-DRUG-000017"}, "key_figures": {}, "url": "JAH-DRUG-000017.html"}, {"id": "JAH-DRUG-000018", "title": "JAH-DRUG-000018", "family": "drug record", "desc": "JAH-DRUG-000018", "spec": {"mechanism": "JAH-DRUG-000018"}, "key_figures": {}, "url": "JAH-DRUG-000018.html"}, {"id": "JAH-DRUG-000019", "title": "JAH-DRUG-000019", "family": "drug record", "desc": "JAH-DRUG-000019", "spec": {"mechanism": "JAH-DRUG-000019"}, "key_figures": {}, "url": "JAH-DRUG-000019.html"}, {"id": "JAH-DRUG-000020", "title": "JAH-DRUG-000020", "family": "drug record", "desc": "JAH-DRUG-000020", "spec": {"mechanism": "JAH-DRUG-000020"}, "key_figures": {}, "url": "JAH-DRUG-000020.html"}, {"id": "JAH-DRUG-000021", "title": "JAH-DRUG-000021", "family": "drug record", "desc": "JAH-DRUG-000021", "spec": {"mechanism": "JAH-DRUG-000021"}, "key_figures": {}, "url": "JAH-DRUG-000021.html"}, {"id": "JAH-DRUG-000022", "title": "JAH-DRUG-000022", "family": "drug record", "desc": "JAH-DRUG-000022", "spec": {"mechanism": "JAH-DRUG-000022"}, "key_figures": {}, "url": "JAH-DRUG-000022.html"}, {"id": "JAH-DRUG-000023", "title": "JAH-DRUG-000023", "family": "drug record", "desc": "JAH-DRUG-000023", "spec": {"mechanism": "JAH-DRUG-000023"}, "key_figures": {}, "url": "JAH-DRUG-000023.html"}, {"id": "JAH-DRUG-000024", "title": "JAH-DRUG-000024", "family": "drug record", "desc": "JAH-DRUG-000024", "spec": {"mechanism": "JAH-DRUG-000024"}, "key_figures": {}, "url": "JAH-DRUG-000024.html"}], "twin": {"id": "pharma-drugs-signature", "title": "JAH Drug Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-DRUG-GEN-"};
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
console.log(answerQuestion(q, KB, "JAH Pharma Librarian"));
