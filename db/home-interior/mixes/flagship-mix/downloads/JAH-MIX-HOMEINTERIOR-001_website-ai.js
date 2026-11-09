#!/usr/bin/env node
/* JAH Interior Creator — website Q&A AI for Flagship Mix — Dining table — Piece profile × Signature JAH Home and Interior Field Guide: The Core Defini (JAH-MIX-HOMEINTERIOR-001).
   The same Q&A router as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/home-interior/mixes/flagship-mix/index.html, over the same knowledge
   base (this page's records and their cited sources). Run: node <file> "your question"
   Free forever. Part of The 'Merica-L Internet. */
var KB = {"current": {"id": "JAH-MIX-HOMEINTERIOR-001", "title": "Flagship Mix — Dining table — Piece profile × Signature JAH Home and Interior Field Guide: The Core Defini", "family": "flagship mix", "desc": "The flagship mix of the JAH Home and Interior database: Dining table — Piece profile (JAH-HOME-0000001) blended with Signature JAH Home and Interior Field Guide: The Core Definitions (JAH-HOMES-000001). The mix combines the two records — their numbers, mechanisms, and descriptions — and scales the blend at A1 pocket (0.6×), A2 standard (1.0×), and A3 workshop (1.6×).", "spec": {"mechanism": "Dining table is a furniture for dining, standard: 28–30 in high; 36–48 in wide. Origin: Worldwide, era modern. Standard table height pairs with 17–19 in chairs. Archived in the JAH Home and Interior Database for designers.; JAH Home and Interior is the Signature system's original body of knowledge for jah home and interior: the terms, the tools, and the working methods, all created in the Signature system and labeled Signature-original. Nothing here claims to be a public record; it is new creative and technical work built for study, practice, and imagination.\n\nThis field guide defines the five"}, "key_figures": {}, "url": "index.html"}, "records": [{"id": "JAH-HOME-0000001", "title": "Dining table — Piece profile", "family": "furniture", "desc": "Dining table is a furniture for dining, standard: 28–30 in high; 36–48 in wide. Origin: Worldwide, era modern. Standard table height pairs with 17–19 in chairs. Archived in the JAH Home and Interior Database for designers.", "spec": {"mechanism": "Dining table is a furniture for dining, standard: 28–30 in high; 36–48 in wide. Origin: Worldwide, era modern. Standard table height pairs with 17–19 in chairs. Archived in the JAH Home and Interior Database for designers."}, "key_figures": {}, "url": "../../records/JAH-HOME-0000001.html"}, {"id": "JAH-HOMES-000001", "title": "Signature JAH Home and Interior Field Guide: The Core Definitions", "family": "interior record", "desc": "JAH Home and Interior is the Signature system's original body of knowledge for jah home and interior: the terms, the tools, and the working methods, all created in the Signature system and labeled Signature-original. Nothing here claims to be a public record; it is new creative and technical work built for study, practice, and imagination.\n\nThis field guide defines the five load-bearing ideas of j", "spec": {"mechanism": "JAH Home and Interior is the Signature system's original body of knowledge for jah home and interior: the terms, the tools, and the working methods, all created in the Signature system and labeled Signature-original. Nothing here claims to be a public record; it is new creative and technical work built for study, practice, and imagination.\n\nThis field guide defines the five load-bearing ideas of jah home and interior: the Signature method, the compounding generation, the teaching ladder, the working version, and the archive-aware AI. Each definition below is written to stand alone, so a newcom"}, "key_figures": {}, "url": "../../website/mirror/index.html"}], "twin": null, "sources": [{"title": "Record source", "url": "https://www.coohom.com/article/standard-dimensions-for-furniture-design", "text": ""}], "gen_prefix": "JAH-HOME-GEN-"};
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
console.log(answerQuestion(q, KB, "JAH Interior Creator"));
