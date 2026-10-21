(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["web-text", "code", "multimodal", "audio-speech", "instruction", "evaluation"] */
var CATS=["web-text", "code", "multimodal", "audio-speech", "instruction", "evaluation"];
var PREFIX='JAH-TRNDS-S-';
var FIELDS=["modality", "size", "license", "source_org", "use_cases"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["web-text", "Signature Web Crawl Tier 1", "Signature-authored plan for a 2T-token curated web corpus: crawl sources, quality tiers, and license posture, designed by JAH.", "Signature Web Crawl Tier 1 is a JAH-designed compilation plan for a two-trillion-token web corpus built only from permissively licensed or public-domain sources plus licensed publisher feeds. The plan defines three quality tiers (Tier 1 editorial, Tier 2 curated forums/docs, Tier 3 broad web), a MinHash dedup budget, and a per-document license ledger so every token carries provenance. It is a compilation design — the corpus is assembled by running the plan — and is labeled Signature throughout.", "web text", "2T tokens (planned)", "Signature compilation plan; source-dependent", "Signature Systems (JAH)", ["LLM pretraining", "license-clean corpora", "tiered quality research"], "python", "Tiered corpus budget planner", "tiers = {\"tier1_editorial\": 0.15, \"tier2_curated\": 0.35, \"tier3_broad\": 0.50}\ntotal = 2e12\nfor tier, frac in tiers.items():\n    print(f\"{tier:16s} {frac*100:4.0f}%  {frac*total/1e12:.2f}T tokens\")"],
 ["instruction", "JAH Instruction Forge", "Signature-authored design for a 5M-pair instruction corpus: task taxonomy, generation recipes, and quality gates.", "JAH Instruction Forge is a JAH-original compilation design covering five million instruction-response pairs across a 400-task taxonomy (coding, math, writing, reasoning, tool use). The design specifies generation recipes per task family, a three-stage quality gate (format check, model-judge scoring, human audit sample), and a contamination screen against 40 public benchmarks. Every pair carries task-family and difficulty labels for curriculum use. Labeled Signature; the pairs are produced by executing the design.", "instruction pairs", "5M pairs (planned)", "Signature compilation plan", "Signature Systems (JAH)", ["chat SFT", "curriculum training", "benchmark-decontaminated tuning"], "python", "Task taxonomy sampler", "import random\ntasks = [\"code_debug\", \"math_proof\", \"summarize\", \"tool_plan\", \"translate\"]\nrandom.seed(7)\nplan = {t: 5_000_000 // len(tasks) for t in tasks}\nfor t, n in plan.items():\n    print(f\"{t:12s} {n:,} pairs\")"],
 ["code", "Signature Code Quarry", "Signature-authored plan for a 1 TB permissive-license code corpus with per-file license ledger.", "Signature Code Quarry is a JAH-designed code corpus plan targeting one terabyte of source code drawn strictly from permissive licenses (MIT, Apache-2.0, BSD, ISC), with a per-file license ledger and an opt-out registry honoring developer requests. The design includes language-balanced sampling across 80 languages, near-dedup at repository level, and a secrets scanner that strips keys and tokens before packaging. Labeled Signature throughout.", "source code", "1 TB (planned); 80 languages", "Permissive-only (MIT/Apache/BSD/ISC)", "Signature Systems (JAH)", ["code LLM pretraining", "license-safe code models", "secrets-free corpora"], "python", "License ledger check", "allowed = {\"mit\", \"apache-2.0\", \"bsd-2-clause\", \"bsd-3-clause\", \"isc\"}\nledger = [{\"file\": \"net.py\", \"license\": \"mit\"},\n          {\"file\": \"ui.js\", \"license\": \"gpl-3.0\"}]\nclean = [e for e in ledger if e[\"license\"] in allowed]\nprint(\"admitted:\", [e[\"file\"] for e in clean])"],
 ["multimodal", "JAH Multimodal Pairs", "Signature-authored design for 500M curated image-text pairs with CLIP-score and safety filtering.", "JAH Multimodal Pairs is a JAH-original plan for half a billion image-text pairs: source from openly licensed image repositories, filter by CLIP similarity (>=0.30), run NSFW and watermark detectors, and keep per-pair source URLs plus license tags. The design adds a multilingual caption-expansion stage that machine-translates captions into 20 languages with human audit sampling. Labeled Signature; pairs are produced by running the plan.", "image-text pairs", "500M pairs (planned)", "Signature compilation plan; per-pair license tags", "Signature Systems (JAH)", ["text-to-image training", "multilingual CLIP", "captioning models"], "python", "Pair filtering sketch", "pairs = [{\"clip\": 0.34, \"nsfw\": 0.01}, {\"clip\": 0.22, \"nsfw\": 0.02},\n          {\"clip\": 0.41, \"nsfw\": 0.80}]\nkept = [p for p in pairs if p[\"clip\"] >= 0.30 and p[\"nsfw\"] < 0.10]\nprint(f\"kept {len(kept)}/{len(pairs)} pairs\")"],
 ["audio-speech", "Signature Speech Mine", "Signature-authored plan for 50K hours of transcribed speech across 40 languages.", "Signature Speech Mine is a JAH-designed speech corpus plan: 50,000 hours of transcribed audio spanning 40 languages, sourced from public-domain audiobooks, licensed podcast feeds, and community contributions. The design specifies a transcription pipeline (base ASR + human correction on a 5% audit slice), speaker-diversity quotas, and noise-condition labels (clean, street, call-center) so models train robustly. Labeled Signature throughout.", "speech audio", "50K hours; 40 languages (planned)", "Signature compilation plan", "Signature Systems (JAH)", ["multilingual ASR", "robust speech models", "TTS training"], "python", "Language hour quotas", "langs = 40\ntotal_hours = 50_000\nquota = {\"en\": 0.30}\nrest = (1 - quota[\"en\"]) / (langs - 1)\nquotas = {\"en\": quota[\"en\"] * total_hours}\nquotas.update({f\"lang_{i}\": rest * total_hours for i in range(1, langs)})\nprint(\"en hours:\", quotas[\"en\"], \"| others each:\", round(quotas[\"lang_1\"]))"],
 ["web-text", "JAH Textbook Vault", "Signature-authored plan for 100K open textbooks distilled into a clean educational corpus.", "JAH Textbook Vault is a JAH-original design for a 100,000-textbook educational corpus built from openly licensed textbooks (OpenStax-style) plus public-domain classics. The plan adds a distillation stage: long chapters are compressed into study-note form by a teacher model, then verified against the source, producing parallel long/short pairs for training models that explain clearly. Labeled Signature; the corpus is built by executing the plan.", "educational text", "100K textbooks + distilled notes (planned)", "Open licenses + public domain", "Signature Systems (JAH)", ["educational LLMs", "tutoring models", "explanation training"], "python", "Chapter distillation record", "chapter = {\"title\": \"Fractions\", \"words\": 4200}\nnote = {\"title\": chapter[\"title\"] + \" (study notes)\",\n        \"words\": 600, \"verified_against\": chapter[\"title\"]}\nprint(note)\nprint(\"compression:\", round(chapter[\"words\"]/note[\"words\"], 1), \"x\")"],
 ["web-text", "Signature Math Proofs Corpus", "Signature-authored design for 2M formal and informal math proofs with step labels.", "This JAH-designed corpus plan targets two million mathematics proofs: formal proofs in Lean/Coq style plus informal textbook proofs, each annotated with step boundaries and the theorem it proves. The design includes an autoformalization track (informal to Lean, checked by the kernel) and a difficulty ladder from arithmetic to graduate topics. Labeled Signature throughout.", "math text", "2M proofs (planned)", "Signature compilation plan; open sources", "Signature Systems (JAH)", ["math reasoning models", "autoformalization", "proof assistants"], "python", "Proof step record", "proof = {\"theorem\": \"sqrt(2) is irrational\",\n           \"steps\": [\"assume sqrt(2)=a/b reduced\",\n                     \"then 2b^2=a^2, so a even\",\n                     \"then b even: contradiction\"]}\nprint(f\"{proof['theorem']}: {len(proof['steps'])} steps\")"],
 ["instruction", "JAH Dialogue Garden", "Signature-authored plan for 10M multi-turn conversations across 60 scenario families.", "JAH Dialogue Garden is a JAH-original design for ten million multi-turn dialogues spanning 60 scenario families (customer support, tutoring, negotiation, brainstorming, therapy-adjacent wellness coaching with safety rails). Each dialogue carries scenario, turn count, and outcome labels, and a 1% slice gets human quality review. The plan forbids real private conversations — all dialogues are synthetic or actor-performed. Labeled Signature.", "dialogues", "10M dialogues; 60 scenarios (planned)", "Signature compilation plan (synthetic/acted)", "Signature Systems (JAH)", ["conversational AI", "multi-turn training", "scenario evaluation"], "python", "Dialogue schema validation", "d = {\"scenario\": \"tutoring\", \"turns\": [\n    {\"role\": \"user\", \"text\": \"Explain fractions.\"},\n    {\"role\": \"assistant\", \"text\": \"A fraction is part of a whole.\"}]}\nassert all(t[\"role\"] in (\"user\", \"assistant\") for t in d[\"turns\"])\nprint(\"valid dialogue:\", d[\"scenario\"], len(d[\"turns\"]), \"turns\")"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,title:b[1],t:b[1],g:cat,c:1,summary:b[2],details:b[3]};
  for(var i=0;i<FIELDS.length;i++){rec[FIELDS[i]]=b[4+i];}
  var di=4+FIELDS.length;
  rec.ladder_rank=1+(seed%3);
  rec.demo={language:b[di],title:b[di+1],program:b[di+2]};
  rec.provenance="Signature Systems (JAH)";
  rec.last_verified='2026-10-20';
  rec.src="signature-generated-completion";
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.summary!=='string'||!r.summary.length)e.push('summary');
  if(typeof r.details!=='string'||!r.details.length)e.push('details');
  if(CATS.indexOf(r.g)<0)e.push('g');
  for(var i=0;i<FIELDS.length;i++){
    var v=r[FIELDS[i]];
    if(v===undefined||v===null||(typeof v==='string'&&!v.length))e.push('field:'+FIELDS[i]);
  }
  if(!(r.ladder_rank===1||r.ladder_rank===2||r.ladder_rank===3))e.push('ladder_rank');
  var d=r.demo;
  if(!d||typeof d.language!=='string'||!d.language.length||typeof d.title!=='string'||!d.title.length||typeof d.program!=='string'||!d.program.length)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-20')e.push('last_verified');
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ai-training-datasets-signature-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-training-datasets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
