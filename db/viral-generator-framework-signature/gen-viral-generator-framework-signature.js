/* Viral Generator Framework (Signature edition) — reusable viral generator framework.
   Real implemented components: prompt processing, data retrieval, generation,
   rendering, validation, personalization, export. Node-executable and tested.
   Dual runtime: node CLI (`node gen-viral-generator-framework-signature.js --n 1 --seed 7`) prints the 8 full
   records as JSONL; browser via window.JAHDB.registerGenerator.
   Deterministic: same seed = same records. HARD_CAP = 10^15. */
'use strict';
var SLUG = "viral-generator-framework-signature";
var EDITION = "signature";
var SRC = "signature-generated-completion";
var AI_NAME = "JAH Viral Signature Framework Librarian";
var ID_PREFIX = "JAH-VRLS-";
var RUNTIME_STATUS = 'tested';
var VERIFICATION_STATUS = 'tested';
var BODIES = ["The Signature edition record for the framework component: Framework Overview. The whole framework: components, pipeline, and how tools assemble from parts. This is the overview record of the reusable viral generator framework, the strongest direction named in the catalog: instead of programming every viral tool from scratch, new tools assemble from common components. The framework provides seven components. The prompt processor normalizes prompts, extracts keywords, and detects intent. The data retriever fetches matching templates deterministically by seed. The generation core combines the processed prompt with retrieved material into a concept with a title, hook, beats, and call to action. The renderer turns concepts into markdown, HTML, or plain-text share cards. The validator checks every concept against its schema. The personalizer applies style and audience preferences supplied at runtime and stores nothing. The exporter packages everything with attribution. The overview demo runs the entire pipeline end to end on a sample prompt and reports each stage, so the framework is exercised, not just described. Reference implementation: every component is real working JavaScript, executed and tested in node. A specification alone does not perform media rendering \u2014 video, audio, or photoreal image output still requires a real model or connected rendering engine wired to the renderer interface. Runtime status is tested: the code runs in node and every demo output stored here was produced by executing it.", "The Signature edition record for the framework component: Prompt Processor. Normalizes prompts, extracts keywords, and detects intent. The prompt processor takes a raw user prompt and returns a structured request: the original text, normalized tokens, keywords, detected intents, and a word count. Intent detection is heuristic and honest about it: keyword patterns map to video-concept, meme, challenge, story, music, visual, or general-concept. Prompts are trimmed and length-bounded, punctuation is normalized, and empty input yields a clean general-concept request rather than an error. The demo processes a sample prompt and returns its tokens, keywords, and intents as data.", "The Signature edition record for the framework component: Data Retriever. Deterministic template retrieval by seed and intent. The data retriever matches a processed prompt against an embedded template bank using a deterministic hash of the keywords and the seed. Same keywords and same seed always return the same templates, which makes retrieval reproducible and testable. Templates are matched by intent first, falling back to the whole bank for general requests. Three templates are returned per query: enough to combine, few enough to stay coherent. The demo retrieves for a sample prompt and lists the template ids and titles returned.", "The Signature edition record for the framework component: Generation Core. Combines processed prompts with retrieved material into concepts. The generation core takes the processed prompt and the retrieved templates and assembles a concept: a title built from the top template and the user's keywords, a hook phrased as a question, a sequence of beats drawn from the templates, and a call to action inviting remixing. Generation is pure and deterministic: no network, no model call, no randomness beyond the seed. The demo generates a concept from a sample prompt and returns its title, kind, hook, beat count, and call to action.", "The Signature edition record for the framework component: Renderer. Renders concepts to markdown, HTML, and plain text. The renderer converts a concept into shareable text in three formats. Markdown gives a headed document with bold hook and numbered beats. HTML gives a self-contained article element. Plain text gives a clean share-card body. Rendering is total: every concept renders in every format with no failures, and the output is plain human-readable text. The demo renders a sample concept to markdown and reports the length and a preview.", "The Signature edition record for the framework component: Output Validator. Schema and quality checks on generated concepts. The output validator checks every generated concept before it ships: title, kind, hook, beats, and call to action must be present; beats must number at least two; titles stay within length. It returns an honest verdict with an error list, never a silent pass. The demo validates one good and one bad concept and reports both verdicts, proving the checker catches real defects.", "The Signature edition record for the framework component: Personalizer. Applies runtime-supplied style and audience preferences; stores nothing. The personalizer applies style and audience preferences to a concept: epic rephrases the hook, cozy softens the call to action, and any style is recorded on the record. Preferences arrive at runtime from the user and are never stored: the personalized record carries the preferences used, not the person. The demo personalizes a sample concept with epic style for a friends audience and returns the result.", "The Signature edition record for the framework component: Exporter. Packages concepts as JSON, markdown, HTML, or share-card text with attribution. The exporter packages a concept for the world: JSON for machines, markdown for documents, HTML for pages, and plain-text share cards for social platforms. Every package includes an attribution line naming the framework, because viral spread without credit is a bug. The demo exports a sample concept as a share card and reports the format, filename, byte size, and attribution."];
var HONESTY = "Reference implementation: every component is real working JavaScript, executed and tested in node. A specification alone does not perform media rendering \u2014 video, audio, or photoreal image output still requires a real model or connected rendering engine wired to the renderer interface.";
var HARD_CAP = 1e15;
var LADDER = ['simple','competitive','mix-and-match','unmade','top-notch-or-better','future-grade','god-mode','god-mode'];
var SECTIONS = [{"code": "FW-OVERVIEW", "title": "Framework Overview", "desc": "The whole framework: components, pipeline, and how tools assemble from parts.", "capabilities": ["Assembles viral tools from common parts", "End-to-end pipeline", "Deterministic and testable"]}, {"code": "FW-PROMPT", "title": "Prompt Processor", "desc": "Normalizes prompts, extracts keywords, and detects intent.", "capabilities": ["Prompt normalization", "Keyword extraction", "Intent detection"]}, {"code": "FW-RETRIEVE", "title": "Data Retriever", "desc": "Deterministic template retrieval by seed and intent.", "capabilities": ["Seed-deterministic retrieval", "Intent-matched templates", "No network needed"]}, {"code": "FW-GENERATE", "title": "Generation Core", "desc": "Combines processed prompts with retrieved material into concepts.", "capabilities": ["Concept assembly", "Hook generation", "Beat sequencing"]}, {"code": "FW-RENDER", "title": "Renderer", "desc": "Renders concepts to markdown, HTML, and plain text.", "capabilities": ["Markdown rendering", "HTML rendering", "Plain-text share cards"]}, {"code": "FW-VALIDATE", "title": "Output Validator", "desc": "Schema and quality checks on generated concepts.", "capabilities": ["Schema checking", "Quality gates", "Honest pass/fail verdicts"]}, {"code": "FW-PERSONALIZE", "title": "Personalizer", "desc": "Applies runtime-supplied style and audience preferences; stores nothing.", "capabilities": ["Runtime personalization", "Style and audience options", "Zero stored personal data"]}, {"code": "FW-EXPORT", "title": "Exporter", "desc": "Packages concepts as JSON, markdown, HTML, or share-card text with attribution.", "capabilities": ["Multi-format export", "Automatic attribution", "Portable packages"]}];

/* ================= real framework components ================= */
function PromptProcessor(){
  this.process = function(prompt){
    var p = String(prompt == null ? '' : prompt).trim().slice(0, 500);
    var low = p.toLowerCase();
    var tokens = low.replace(/[^a-z0-9\s]/g,'').split(/\s+/).filter(function(t){return t;});
    var intents = [];
    if (/video|clip|trailer|scene/.test(low)) intents.push('video-concept');
    if (/meme|funny|joke|parody/.test(low)) intents.push('meme');
    if (/challenge|game|contest|quiz|tournament|battle/.test(low)) intents.push('challenge');
    if (/story|adventure|quest|mystery/.test(low)) intents.push('story');
    if (/song|music|lyrics|anthem/.test(low)) intents.push('music');
    if (/image|logo|poster|card|emblem/.test(low)) intents.push('visual');
    if (!intents.length) intents.push('general-concept');
    var keywords = tokens.filter(function(t){return t.length > 3;}).slice(0, 8);
    return {original: p, tokens: tokens, keywords: keywords, intents: intents, word_count: tokens.length};
  };
}

var TEMPLATE_BANK = [
  {id:'t01', kind:'challenge', title:'One-Minute Invention Sprint', body:'Invent a fix for a random everyday annoyance in 60 seconds.'},
  {id:'t02', kind:'meme', title:'Expectation Flip', body:'Setup, escalation, then a punchline that flips the expectation.'},
  {id:'t03', kind:'story', title:'The Tiny Heist', body:'A crew of miniature robots plans an impossible tabletop heist.'},
  {id:'t04', kind:'visual', title:'Emblem of the Ordinary', body:'Turn an everyday object into a heroic emblem with a motto.'},
  {id:'t05', kind:'video-concept', title:'Trailer for a Toaster', body:'An epic 30-second trailer script for the humblest appliance.'},
  {id:'t06', kind:'music', title:'Anthem of Small Wins', body:'Lyrics celebrating tiny daily victories, verse-chorus-verse.'},
  {id:'t07', kind:'challenge', title:'Prediction Arena', body:'Friends predict harmless everyday outcomes; scores update live.'},
  {id:'t08', kind:'story', title:'The Reverse Museum', body:'Exhibits of things that never happened, cataloged seriously.'},
  {id:'t09', kind:'meme', title:'Genre Swap', body:'The same scene retold as horror, then as comedy.'},
  {id:'t10', kind:'visual', title:'Civilization Card', body:'A fictional civilization profile: values, emblem, strengths.'},
  {id:'t11', kind:'video-concept', title:'Before-and-After Epic', body:'A dramatic fictional transformation in three beats.'},
  {id:'t12', kind:'challenge', title:'Remix Chain', body:'Each player transforms the previous player\'s creation.'}
];

function DataRetriever(){
  this.retrieve = function(processed, seed){
    var h = 0, s = processed.keywords.join(' ') + '|' + String(seed);
    for (var i=0;i<s.length;i++) h = ((h*31) + s.charCodeAt(i)) >>> 0;
    var want = processed.intents[0];
    var pool = TEMPLATE_BANK.filter(function(t){return t.kind===want || want==='general-concept';});
    if (!pool.length) pool = TEMPLATE_BANK;
    var hits = [];
    for (var k=0;k<3;k++) hits.push(pool[(h + k*5) % pool.length]);
    return {query_keywords: processed.keywords, intent: want, seed: seed, templates: hits};
  };
}

function GeneratorCore(){
  this.generate = function(processed, retrieved){
    var t0 = retrieved.templates[0], t1 = retrieved.templates[1], t2 = retrieved.templates[2];
    var kw = processed.keywords.slice(0,3).join(' ') || 'a bold new idea';
    return {
      title: t0.title + ': ' + kw,
      kind: retrieved.intent,
      hook: 'What if ' + kw + ' met ' + t1.title.toLowerCase() + '?',
      beats: [t0.body, t1.body, t2.body],
      cta: 'Remix this with a friend and post your version.',
      keywords: processed.keywords
    };
  };
}

function Renderer(){
  this.render = function(concept, format){
    format = format || 'markdown';
    if (format === 'html'){
      return '<article><h1>'+concept.title+'</h1><p><strong>Hook:</strong> '+concept.hook+'</p><ol>'+
        concept.beats.map(function(b){return '<li>'+b+'</li>';}).join('')+
        '</ol><p><em>'+concept.cta+'</em></p></article>';
    }
    if (format === 'text'){
      return concept.title + '\nHook: ' + concept.hook + '\n' +
        concept.beats.map(function(b,i){return (i+1)+'. '+b;}).join('\n') + '\n' + concept.cta;
    }
    return '# '+concept.title+'\n\n**Hook:** '+concept.hook+'\n\n'+
      concept.beats.map(function(b,i){return (i+1)+'. '+b;}).join('\n')+'\n\n_'+concept.cta+'_';
  };
}

function OutputValidator(){
  this.check = function(concept){
    var errors = [];
    ['title','kind','hook','beats','cta'].forEach(function(k){ if(!concept[k]) errors.push('missing '+k); });
    if (concept.beats && concept.beats.length < 2) errors.push('needs at least 2 beats');
    if (concept.title && concept.title.length > 140) errors.push('title too long');
    return {ok: errors.length===0, errors: errors};
  };
}

function Personalizer(){
  this.apply = function(concept, prefs){
    prefs = prefs || {};
    var c = JSON.parse(JSON.stringify(concept));
    c.style = prefs.style || 'playful';
    c.audience = prefs.audience || 'general';
    if (prefs.style === 'epic') c.hook = c.hook.replace(/^What if/, 'BEHOLD: what if');
    if (prefs.style === 'cozy') c.cta = 'Share this with someone who needs a smile.';
    c.personalized_for = 'runtime-supplied preferences only; nothing stored';
    return c;
  };
}

function Exporter(){
  this.exportPackage = function(concept, format){
    format = format || 'json';
    var renderer = new Renderer();
    var content, filename;
    if (format === 'markdown'){ content = renderer.render(concept,'markdown'); filename = 'viral-concept.md'; }
    else if (format === 'share-card'){ content = renderer.render(concept,'text'); filename = 'viral-share-card.txt'; }
    else if (format === 'html'){ content = renderer.render(concept,'html'); filename = 'viral-concept.html'; }
    else { content = JSON.stringify(concept, null, 2); filename = 'viral-concept.json'; }
    return {format: format, filename: filename, bytes: content.length, content: content,
      attribution: 'Made with the JAH-N Signature Viral Generator Framework'};
  };
}

/* ================= demos (executed during generation) ================= */
var SAMPLE_PROMPT = 'Make a viral space-emperor challenge for my friends';

function demoOverview(){
  var pp = new PromptProcessor(), dr = new DataRetriever(), gc = new GeneratorCore(),
      rn = new Renderer(), ov = new OutputValidator(), pz = new Personalizer(), ex = new Exporter();
  var processed = pp.process(SAMPLE_PROMPT);
  var retrieved = dr.retrieve(processed, 7);
  var concept = gc.generate(processed, retrieved);
  var check = ov.check(concept);
  var personalized = pz.apply(concept, {style:'epic', audience:'friends'});
  var pack = ex.exportPackage(personalized, 'share-card');
  return {pipeline: ['prompt','retrieve','generate','render','validate','personalize','export'],
    intents: processed.intents, templates_used: retrieved.templates.map(function(t){return t.id;}),
    validation_ok: check.ok, export_format: pack.format, export_bytes: pack.bytes,
    note: 'Full framework pipeline executed end to end on a sample prompt.'};
}
function demoPrompt(){
  var r = new PromptProcessor().process(SAMPLE_PROMPT);
  return {tokens: r.tokens, keywords: r.keywords, intents: r.intents, word_count: r.word_count};
}
function demoRetrieve(){
  var pp = new PromptProcessor();
  var r = new DataRetriever().retrieve(pp.process(SAMPLE_PROMPT), 7);
  return {intent: r.intent, seed: r.seed, template_ids: r.templates.map(function(t){return t.id;}),
    titles: r.templates.map(function(t){return t.title;})};
}
function demoGenerate(){
  var pp = new PromptProcessor(), dr = new DataRetriever();
  var processed = pp.process(SAMPLE_PROMPT);
  var c = new GeneratorCore().generate(processed, dr.retrieve(processed, 7));
  return {title: c.title, kind: c.kind, hook: c.hook, beats: c.beats.length, cta: c.cta};
}
function demoRender(){
  var pp = new PromptProcessor(), dr = new DataRetriever();
  var processed = pp.process(SAMPLE_PROMPT);
  var c = new GeneratorCore().generate(processed, dr.retrieve(processed, 7));
  var md = new Renderer().render(c, 'markdown');
  return {format: 'markdown', length: md.length, preview: md.slice(0, 80)};
}
function demoValidate(){
  var ov = new OutputValidator();
  var good = {title:'x', kind:'challenge', hook:'y', beats:['a','b'], cta:'z'};
  var bad = {title:'x'};
  var g = ov.check(good), b = ov.check(bad);
  return {good_ok: g.ok, bad_ok: b.ok, bad_errors: b.errors};
}
function demoPersonalize(){
  var pp = new PromptProcessor(), dr = new DataRetriever();
  var processed = pp.process(SAMPLE_PROMPT);
  var c = new GeneratorCore().generate(processed, dr.retrieve(processed, 7));
  var p = new Personalizer().apply(c, {style:'epic', audience:'friends'});
  return {style: p.style, audience: p.audience, hook: p.hook, privacy: p.personalized_for};
}
function demoExport(){
  var pp = new PromptProcessor(), dr = new DataRetriever();
  var processed = pp.process(SAMPLE_PROMPT);
  var c = new GeneratorCore().generate(processed, dr.retrieve(processed, 7));
  var e = new Exporter().exportPackage(c, 'share-card');
  return {format: e.format, filename: e.filename, bytes: e.bytes, attribution: e.attribution,
    preview: e.content.slice(0, 80)};
}
var DEMOS = [demoOverview, demoPrompt, demoRetrieve, demoGenerate, demoRender, demoValidate, demoPersonalize, demoExport];

function buildRecord(i, seed){
  var sec = SECTIONS[i];
  var fn = DEMOS[i];
  var program = fn.toString();
  var output;
  try { output = JSON.stringify(fn()); }
  catch(e){ output = JSON.stringify({error: String((e && e.message) || e)}); }
  return {
    id: ID_PREFIX + 'FW-' + String(i+1).padStart(2,'0'),
    title: 'Viral Generator Framework \u2014 ' + sec.title,
    description: sec.desc,
    body: BODIES[i],
    capabilities: sec.capabilities,
    demo: {program: program, output: output, executed_in: 'node', generator: 'gen-'+SLUG+'.js'},
    provenance: {built_by: 'assistant-built', built_for: 'Justin Addam Higgins (JAH)', date: '2026-10-22',
      round: 'R22', lane: 'viral', framework: true},
    licensing: 'Property of Justin Addam Higgins (JAH). Reference implementation for the Signature ecosystem.',
    src: SRC, edition: EDITION,
    ladder_rank: LADDER[i],
    generator: {name: 'jahdb-'+SLUG+'-1.0', seed: seed, record_index: i},
    verification_status: VERIFICATION_STATUS,
    runtime_status: RUNTIME_STATUS,
    honesty: HONESTY,
    links: [{rel:'data-index', href:'https://justinahiggins614-cmyk.github.io/jah-databases-data-2/data/viral-generator-framework-signature/index.jsonl.gz'},
            {rel:'generator', href:'gen-'+SLUG+'.js'}],
    record_kind: 'generator-framework'
  };
}

function generate(seed, opts){
  opts = opts || {};
  var recs = [];
  for (var i=0;i<8;i++) recs.push(buildRecord(i, seed));
  return recs;
}

function validate(r){
  var errors = [];
  ['id','title','description','body','edition','src','ladder_rank','demo'].forEach(function(k){
    if(!r[k]) errors.push('missing '+k);
  });
  if (r.id && r.id.indexOf(ID_PREFIX)!==0) errors.push('id prefix mismatch');
  if (r.demo){
    if(!r.demo.program) errors.push('demo.program missing');
    if(!r.demo.output) errors.push('demo.output missing');
    else { try{ JSON.parse(r.demo.output); }catch(e){ errors.push('demo.output not JSON'); } }
  }
  return {ok: errors.length===0, errors: errors};
}

function main(){
  var n=1, seed=7, a;
  for (a=2;a<process.argv.length;a++){
    var p=process.argv[a];
    if(p==='--n') n=parseInt(process.argv[++a],10);
    else if(p==='--seed') seed=parseInt(process.argv[++a],10);
  }
  if(!(n>=1) || n>HARD_CAP){ console.error('HARD_CAP exceeded or bad --n (max 1e15)'); process.exit(1); }
  for (var s=0;s<n;s++){
    var recs=generate(seed+s,{});
    for (var j=0;j<recs.length;j++) console.log(JSON.stringify(recs[j]));
  }
}
if (typeof process!=='undefined' && process.argv && process.argv[1] && process.argv[1].indexOf('gen-')>=0) main();
if (typeof window!=='undefined' && window.JAHDB && JAHDB.registerGenerator) JAHDB.registerGenerator(SLUG, {generate: generate, validate: validate});
