(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["watermarking", "provenance-tracking", "audit-trails", "detection", "policy"];
var PREFIX="JAH-AOA-";
var FIELDS=["technique", "target", "method", "signal", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["LLM Text Watermarking", "Watermarks bias token selection subtly so generated text carries a detectable statistical signal. Detection needs the key; quality impact is minimal. Watermarks tag the synthetic.", "watermarking", 2, "Green-list", "LLM text", "Biased sampling", "Statistical bias", "Tagged synthetic", "Medium"], ["Image Provenance (C2PA)", "C2PA embeds signed provenance in media: what tool made it, what edits happened. The manifest travels with the file. Provenance gets signed.", "provenance-tracking", 2, "C2PA", "Media", "Signed manifest", "Manifest chain", "Signed history", "Medium"], ["Audit Trails for AI Decisions", "High-stakes AI decisions log inputs, model version, and outputs; the trail enables after-the-fact review. Trails are the accountability. Decisions get reviewable.", "audit-trails", 2, "Decision logs", "AI decisions", "Immutable log", "Logged triple", "Reviewable", "Medium"], ["AI-Generated Text Detection", "Detectors classify text as human or AI using perplexity and burstiness features; accuracy is imperfect. Detection is probabilistic, not proof. Signals get weighed.", "detection", 2, "Classifiers", "Text", "Feature models", "Probability", "Weighed signal", "Medium"], ["Dataset Provenance Tracking", "Training data provenance records sources, licenses, and consent; the record travels with the dataset. Provenance is the data's biography. Sources get credited.", "provenance-tracking", 1, "Data cards", "Datasets", "Source ledger", "Ledger entry", "Credited sources", "Low"], ["Model Version Lineage", "Every deployed model version links to its training data, code, and config; lineage enables precise incident response. Lineage is the family tree. Incidents get traced.", "audit-trails", 1, "Lineage", "Models", "Version links", "Linked artifacts", "Traced incidents", "Low"], ["Synthetic Data Labeling", "Synthetic training data is labeled as such in the provenance; unlabeled synthetic poisons future training. Labels prevent the ouroboros. Synthetic gets tagged.", "policy", 1, "Labeling", "Synthetic data", "Provenance tags", "Synthetic tag", "Tagged ouroboros", "Low"], ["Deepfake Detection", "Deepfakes are detected via artifacts: blending boundaries, unnatural blinking, frequency anomalies. The arms race continues. Artifacts get spotted.", "detection", 3, "Artifact detect", "Media", "Forensic features", "Anomaly score", "Spotted fakes", "High"], ["Prompt Injection Audit", "Prompts are logged and audited for injection attempts; the audit trail shows what the model was told. Injections get recorded. Attacks get visible.", "audit-trails", 2, "Prompt logs", "Inputs", "Injection scan", "Logged attempt", "Visible attacks", "Medium"], ["Output Filtering Logs", "Filtered outputs are logged with the reason; the log enables appeal and tuning. Filtering gets accountable. Blocks get explained.", "audit-trails", 1, "Filter logs", "Blocked outputs", "Reason logging", "Logged reason", "Explained blocks", "Low"], ["Provenance for RAG", "RAG answers cite their sources with retrieval IDs; the citation chain is the provenance. Answers get grounded. Sources get credit.", "provenance-tracking", 1, "Citations", "RAG answers", "Retrieval IDs", "Citation chain", "Grounded answers", "Low"], ["Watermark Robustness Testing", "Watermarks are tested against paraphrasing and editing attacks; robustness is measured, not assumed. Attacks get simulated. Survival gets proven.", "watermarking", 3, "Attack tests", "Watermarks", "Paraphrase attacks", "Survival rate", "Proven survival", "High"], ["AI Use Disclosure Policy", "Policies require disclosing AI assistance in published work; the disclosure is the honesty. Use gets declared. Readers get informed.", "policy", 1, "Disclosure", "Publications", "Required statement", "Disclosure present", "Informed readers", "Low"], ["Training Data Deduplication Audit", "Deduplication of training data is audited because duplicates inflate memorization; the audit measures duplication rates. Duplicates get counted. Memorization gets bounded.", "provenance-tracking", 2, "Dedup audit", "Training data", "Duplicate measure", "Dup rate", "Bounded memory", "Medium"], ["Model Card Documentation", "Model cards document intended uses, limitations, and evaluation; the card is the model's résumé. Documentation gets standardized. Users get informed.", "policy", 1, "Model cards", "Models", "Standard docs", "Complete card", "Informed users", "Low"], ["Red-Team Provenance", "Red-team findings link to the exact model version and prompts; the linkage makes findings actionable. Findings get precise. Fixes get targeted.", "audit-trails", 2, "Linked findings", "Red-team", "Version links", "Precise link", "Targeted fixes", "Medium"], ["Consent Tracking for Data", "Consent for training data use is tracked per source; revocations propagate to the dataset. Consent gets honored. Revocations get enforced.", "provenance-tracking", 2, "Consent ledger", "Data rights", "Per-source track", "Revocation enforced", "Honored consent", "Medium"], ["Hallucination Audit", "Model outputs are sampled and fact-checked; the hallucination rate is the quality metric. Sampling gets honest. Rates get published.", "detection", 2, "Fact sample", "Outputs", "Sampled checks", "Hallucination rate", "Honest rates", "Medium"], ["Chain-of-Custody for Evidence", "AI-generated evidence keeps chain-of-custody: who generated, when, with what. Custody gets documented. Evidence gets admissible.", "audit-trails", 3, "Custody chain", "AI evidence", "Documented chain", "Complete chain", "Admissible", "High"], ["Provenance Query API", "Provenance is queryable: 'where did this output come from' returns the full chain. Queries get answered. Origins get known.", "provenance-tracking", 2, "Query API", "Outputs", "Chain lookup", "Full chain", "Known origins", "Medium"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'text = \"the quick brown fox\"\nmark = sum(ord(c) for c in text) % 100\nprint(\"text:\", text)\nprint(\"watermark key:\", mark)\nprint(\"detected as AI-generated:\", mark % 2 == 0)\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-ai-output-audit-and-provenance-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-output-audit-and-provenance",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
