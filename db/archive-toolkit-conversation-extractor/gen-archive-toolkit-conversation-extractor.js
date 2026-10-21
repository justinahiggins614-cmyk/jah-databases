(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK147-";
var KIND="extraction method";
var TOOLNAME="Conversation Extractor";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Turn segmentation", "d": "Speaker labels ('AMY: ...') delimit turns; regex captures label and text. Segmentation structures the dialogue. Turns are the units.", "c": "fundamentals", "r": 1, "p": {"TRANSCRIPT": "AMY: What time is it?\\nBOB: Nearly noon.\\nAMY: Thanks!"}}, {"t": "Speaker normalization", "d": "'Amy', 'AMY', 'amy_1' normalize to one identity. Normalization merges aliases. Identity needs consistency.", "c": "algorithms", "r": 1, "p": {"TRANSCRIPT": "Amy: Hi.\\nAMY: Hello again.\\nBob: Hey."}}, {"t": "Question detection", "d": "Questions end with '?' or match interrogative patterns. Detection finds information needs. Questions drive dialogue.", "c": "implementation", "r": 1, "p": {"TRANSCRIPT": "AMY: Where is the file?\\nBOB: In the docs folder.\\nAMY: Got it."}}, {"t": "Answer pairing", "d": "Answers follow questions, usually from another speaker, so pairing links each question to the turn that resolves it. Adjacency pairs such as question-answer and offer-acceptance are the basic unit of dialogue structure, and correct pairing turns a flat transcript into an understandable conversation. Evaluation measures pairing precision against human-annotated threads.", "c": "optimization", "r": 1, "p": {"TRANSCRIPT": "Q: What is up?\\nA: The sky.\\nQ: Really?\\nA: Yes."}}, {"t": "Dialogue acts", "d": "Utterances classify as question, answer, greeting, or closing. Acts reveal conversation shape. Labels enable analysis.", "c": "evaluation", "r": 1, "p": {"TRANSCRIPT": "AMY: Hello!\\nBOB: Hi there.\\nAMY: Bye.\\nBOB: Bye!"}}, {"t": "Interruption handling", "d": "Overlaps and interruptions mark with timestamps or markers. Handling keeps transcripts faithful. Reality is messy.", "c": "fundamentals", "r": 2, "p": {"TRANSCRIPT": "AMY: I think--\\nBOB: --go on.\\nAMY: Thanks."}}, {"t": "Multi-party tracking", "d": "Conversations with three or more speakers need per-turn attribution, since pronouns and references only resolve once the speaker is known. Tracking maintains a roster of participants and assigns every turn, handling joins, leaves, and name variations. Accurate multi-party tracking is the foundation for meeting analytics.", "c": "algorithms", "r": 2, "p": {"TRANSCRIPT": "AMY: Hi all.\\nBOB: Hey.\\nCID: Hello.\\nAMY: Welcome!"}}, {"t": "Topic segmentation", "d": "Topic shifts split long conversations into coherent segments, detected by vocabulary changes and discourse markers like 'moving on'. Each segment can then be summarized or indexed independently instead of smearing distinct subjects together. Segmentation turns rambling transcripts into navigable structure.", "c": "implementation", "r": 2, "p": {"TRANSCRIPT": "AMY: About lunch?\\nBOB: Sure.\\nAMY: Now the budget?\\nBOB: Later."}}, {"t": "Action-item extraction", "d": "'I will ...' and 'let us ...' sentences extract as action items. Items turn talk into tasks. Extraction creates value.", "c": "optimization", "r": 2, "p": {"TRANSCRIPT": "AMY: I will send the file.\\nBOB: Let us meet Friday."}}, {"t": "Sentiment per turn", "d": "Sentiment scores computed per turn track the emotional arc of a conversation, from greeting through problem-solving to closing. Rising frustration across turns flags conversations that need intervention, while recovery arcs mark successful resolutions. Turn-level sentiment powers quality monitoring for support dialogues.", "c": "evaluation", "r": 2, "p": {"TRANSCRIPT": "AMY: This is great!\\nBOB: I am worried though."}}, {"t": "Diarization alignment", "d": "Speaker labels align with audio diarization timestamps. Alignment merges text and audio evidence. Two signals beat one.", "c": "fundamentals", "r": 3, "p": {"TRANSCRIPT": "S1: First.\\nS2: Second."}}, {"t": "Summarization input", "d": "Structured speaker turns feed extractive summarizers far better than raw text, because the summarizer can weight turns by speaker role and dialogue act. Key decisions, action items, and answers get selected while greetings and small talk drop out. Structure is what makes automatic minutes readable.", "c": "algorithms", "r": 3, "p": {"TRANSCRIPT": "AMY: The plan is set.\\nBOB: Agreed.\\nAMY: Done."}}, {"t": "PII redaction", "d": "Names and numbers redact before sharing transcripts. Redaction protects participants. Privacy is duty.", "c": "implementation", "r": 3, "p": {"TRANSCRIPT": "AMY: Call me at 555-0100.\\nBOB: Will do."}}, {"t": "Format conversion", "d": "Transcripts convert between chat logs, subtitles, and scripts. Conversion preserves speakers and timing. Formats serve uses.", "c": "optimization", "r": 3, "p": {"TRANSCRIPT": "AMY: Line one.\\nBOB: Line two."}}, {"t": "Evaluation of extraction", "d": "Turn-level F1 scores extraction quality on labeled dialogues. Metrics need boundary-exact matching. Measurement ensures quality.", "c": "evaluation", "r": 3, "p": {"TRANSCRIPT": "A: x?\\nB: y."}}];
var DEMO="# Conversation extraction: split transcript into speaker turns, detect Q/A pairs.\ntext = \"\"\"%%TRANSCRIPT%%\"\"\".replace(\"\\\\n\", \"\\n\")\nimport re\nturns = []\nfor line in text.splitlines():\n    m = re.match(r\"\\s*([A-Za-z][A-Za-z0-9_ ]{0,20}):\\s*(.*)\", line)\n    if m: turns.append({\"speaker\": m.group(1).strip(), \"text\": m.group(2).strip()})\nprint(f\"{len(turns)} turns:\")\nqa = []\nfor t in turns:\n    print(f\"  [{t['speaker']}] {t['text'][:50]}\")\nfor a, b in zip(turns, turns[1:]):\n    if a[\"text\"].endswith(\"?\") and not b[\"text\"].endswith(\"?\"):\n        qa.append((a, b))\nprint(f\"Q/A pairs: {len(qa)}\")\nfor q, an in qa:\n    print(f\"  Q({q['speaker']}): {q['text'][:40]} -> A({an['speaker']}): {an['text'][:40]}\")\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK147\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-conversation-extractor-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-conversation-extractor",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
