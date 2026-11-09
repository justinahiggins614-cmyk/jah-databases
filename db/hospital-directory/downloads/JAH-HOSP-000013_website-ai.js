#!/usr/bin/env node
/* JAH Hospital Librarian — website Q&A AI for Brook Urgent Care Center (JAH-HOSP-000013).
   The same Q&A router as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/hospital-directory/records/JAH-HOSP-000013.html, over the same knowledge
   base (this page's records and their cited sources). Run: node <file> "your question"
   Free forever. Part of The 'Merica-L Internet. */
var KB = {"current": {"id": "JAH-HOSP-000013", "title": "Brook Urgent Care Center", "family": "urgent-care", "desc": "Brook Urgent Care Center", "spec": {"mechanism": "Brook Urgent Care Center"}, "key_figures": {"beds": 11, "rating": 1.2}, "url": "JAH-HOSP-000013.html"}, "records": [{"id": "JAH-HOSP-000001", "title": "Riverside Cancer Center", "family": "specialty", "desc": "Riverside Cancer Center", "spec": {"mechanism": "Riverside Cancer Center"}, "key_figures": {"beds": 299, "rating": 4.9}, "url": "JAH-HOSP-000001.html"}, {"id": "JAH-HOSP-000002", "title": "Meadow Orthopedic Institute", "family": "specialty", "desc": "Meadow Orthopedic Institute", "spec": {"mechanism": "Meadow Orthopedic Institute"}, "key_figures": {"beds": 247, "rating": 3.2}, "url": "JAH-HOSP-000002.html"}, {"id": "JAH-HOSP-000003", "title": "Riverside Cancer Center", "family": "specialty", "desc": "Riverside Cancer Center", "spec": {"mechanism": "Riverside Cancer Center"}, "key_figures": {"beds": 188, "rating": 1.3}, "url": "JAH-HOSP-000003.html"}, {"id": "JAH-HOSP-000004", "title": "Meadow Rehabilitation Center", "family": "rehab", "desc": "Meadow Rehabilitation Center", "spec": {"mechanism": "Meadow Rehabilitation Center"}, "key_figures": {"beds": 163, "rating": 1.3}, "url": "JAH-HOSP-000004.html"}, {"id": "JAH-HOSP-000005", "title": "Silver Orthopedic Institute", "family": "specialty", "desc": "Silver Orthopedic Institute", "spec": {"mechanism": "Silver Orthopedic Institute"}, "key_figures": {"beds": 245, "rating": 3.5}, "url": "JAH-HOSP-000005.html"}, {"id": "JAH-HOSP-000006", "title": "Riverside Express Care Clinic", "family": "urgent-care", "desc": "Riverside Express Care Clinic", "spec": {"mechanism": "Riverside Express Care Clinic"}, "key_figures": {"beds": 20, "rating": 1.8}, "url": "JAH-HOSP-000006.html"}, {"id": "JAH-HOSP-000007", "title": "Lakeside Regional Hospital", "family": "hospital", "desc": "Lakeside Regional Hospital", "spec": {"mechanism": "Lakeside Regional Hospital"}, "key_figures": {"beds": 684, "rating": 3.8}, "url": "JAH-HOSP-000007.html"}, {"id": "JAH-HOSP-000008", "title": "Redwood Medical Center", "family": "hospital", "desc": "Redwood Medical Center", "spec": {"mechanism": "Redwood Medical Center"}, "key_figures": {"beds": 148, "rating": 3.8}, "url": "JAH-HOSP-000008.html"}, {"id": "JAH-HOSP-000009", "title": "Prairie General Hospital", "family": "hospital", "desc": "Prairie General Hospital", "spec": {"mechanism": "Prairie General Hospital"}, "key_figures": {"beds": 659, "rating": 4.3}, "url": "JAH-HOSP-000009.html"}, {"id": "JAH-HOSP-000010", "title": "Ocean After-Hours Care", "family": "urgent-care", "desc": "Ocean After-Hours Care", "spec": {"mechanism": "Ocean After-Hours Care"}, "key_figures": {"beds": 20, "rating": 4.2}, "url": "JAH-HOSP-000010.html"}, {"id": "JAH-HOSP-000011", "title": "Maple Express Care Clinic", "family": "urgent-care", "desc": "Maple Express Care Clinic", "spec": {"mechanism": "Maple Express Care Clinic"}, "key_figures": {"beds": 10, "rating": 3.4}, "url": "JAH-HOSP-000011.html"}, {"id": "JAH-HOSP-000012", "title": "Lakeside Community Clinic", "family": "clinic", "desc": "Lakeside Community Clinic", "spec": {"mechanism": "Lakeside Community Clinic"}, "key_figures": {"beds": 17, "rating": 4.8}, "url": "JAH-HOSP-000012.html"}, {"id": "JAH-HOSP-000013", "title": "Brook Urgent Care Center", "family": "urgent-care", "desc": "Brook Urgent Care Center", "spec": {"mechanism": "Brook Urgent Care Center"}, "key_figures": {"beds": 11, "rating": 1.2}, "url": "JAH-HOSP-000013.html"}, {"id": "JAH-HOSP-000014", "title": "Pine Express Care Clinic", "family": "urgent-care", "desc": "Pine Express Care Clinic", "spec": {"mechanism": "Pine Express Care Clinic"}, "key_figures": {"beds": 18, "rating": 2.4}, "url": "JAH-HOSP-000014.html"}, {"id": "JAH-HOSP-000015", "title": "Stone Health Clinic", "family": "clinic", "desc": "Stone Health Clinic", "spec": {"mechanism": "Stone Health Clinic"}, "key_figures": {"beds": 11, "rating": 2.8}, "url": "JAH-HOSP-000015.html"}, {"id": "JAH-HOSP-000016", "title": "Cedar Neurology Institute", "family": "specialty", "desc": "Cedar Neurology Institute", "spec": {"mechanism": "Cedar Neurology Institute"}, "key_figures": {"beds": 97, "rating": 2.6}, "url": "JAH-HOSP-000016.html"}, {"id": "JAH-HOSP-000017", "title": "Willow Cancer Center", "family": "specialty", "desc": "Willow Cancer Center", "spec": {"mechanism": "Willow Cancer Center"}, "key_figures": {"beds": 126, "rating": 1.7}, "url": "JAH-HOSP-000017.html"}, {"id": "JAH-HOSP-000018", "title": "Aspen Community Clinic", "family": "clinic", "desc": "Aspen Community Clinic", "spec": {"mechanism": "Aspen Community Clinic"}, "key_figures": {"beds": 12, "rating": 1.8}, "url": "JAH-HOSP-000018.html"}, {"id": "JAH-HOSP-000019", "title": "Meadow Medical Center", "family": "hospital", "desc": "Meadow Medical Center", "spec": {"mechanism": "Meadow Medical Center"}, "key_figures": {"beds": 191, "rating": 4}, "url": "JAH-HOSP-000019.html"}, {"id": "JAH-HOSP-000020", "title": "Stone Cancer Center", "family": "specialty", "desc": "Stone Cancer Center", "spec": {"mechanism": "Stone Cancer Center"}, "key_figures": {"beds": 154, "rating": 2.1}, "url": "JAH-HOSP-000020.html"}, {"id": "JAH-HOSP-000021", "title": "Pine Urgent Care Center", "family": "urgent-care", "desc": "Pine Urgent Care Center", "spec": {"mechanism": "Pine Urgent Care Center"}, "key_figures": {"beds": 7, "rating": 2.5}, "url": "JAH-HOSP-000021.html"}, {"id": "JAH-HOSP-000022", "title": "Granite Orthopedic Institute", "family": "specialty", "desc": "Granite Orthopedic Institute", "spec": {"mechanism": "Granite Orthopedic Institute"}, "key_figures": {"beds": 83, "rating": 1.8}, "url": "JAH-HOSP-000022.html"}, {"id": "JAH-HOSP-000023", "title": "Lakeside Community Hospital", "family": "hospital", "desc": "Lakeside Community Hospital", "spec": {"mechanism": "Lakeside Community Hospital"}, "key_figures": {"beds": 761, "rating": 2.2}, "url": "JAH-HOSP-000023.html"}, {"id": "JAH-HOSP-000024", "title": "Mountain Health Clinic", "family": "clinic", "desc": "Mountain Health Clinic", "spec": {"mechanism": "Mountain Health Clinic"}, "key_figures": {"beds": 27, "rating": 1.4}, "url": "JAH-HOSP-000024.html"}], "twin": {"id": "hospital-directory-signature", "title": "JAH Hospital Directory Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-HOSP-GEN-"};
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
console.log(answerQuestion(q, KB, "JAH Hospital Librarian"));
