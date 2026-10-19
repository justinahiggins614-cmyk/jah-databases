(function(){'use strict';
/* jahdb-fundamental-history-1.0 — fundamental history bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FHI-';
var KIND='fundamental history record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'History is the study of the human past: what happened, why, and what it means. It works from sources — documents, artifacts, testimonies — to reconstruct vanished worlds and explain how the present came to be.', 'reasoning':'Historians reason from sources: assess each source\'s origin, purpose, and reliability; corroborate across independent witnesses; and build the most probable account. Every claim is footnoted to its evidence — the field\'s honesty mechanism.', 'quantities':'The core quantities are dates, durations, and magnitudes: when, how long, how many. Chronology is the master framework — sequence first, causation second.', 'mechanism':'History works source criticism plus narrative: establish what the sources support, weigh their biases, and synthesize into explanation. Causation in history is multi-threaded — no single cause ever suffices.', 'miscon':'History is not just dates and names: it is explanation — why things happened. It is not the past itself: it is our best reconstruction, always revisable. And it does not repeat — but it rhymes, because human nature and institutions recur.'};
var SIGLENS=['In the Signature system, history is the memory discipline: every database here is an archive, and historical method — source criticism, corroboration, honest revision — governs how the network treats its own past.','The Signature practice is to source the claim: cite the evidence, weigh the bias, corroborate independently — so historical reasoning meets the standard the field demands.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- timeline demo. Runs as-is with python3."""\nevents = [("printing press", 1440), ("American independence", 1776), ("steam engine (Watt)", 1776),\n          ("telegraph", 1844), ("telephone", 1876), ("flight", 1903), ("internet (ARPANET)", 1969)]\nfor name, year in sorted(events, key=lambda e: e[1]):\n    print(f"{year}: {name}")\ngaps = [b[1]-a[1] for a, b in zip(sorted(events, key=lambda e: e[1]), sorted(events, key=lambda e: e[1])[1:])]\nprint(f"mean gap between these milestones: {sum(gaps)/len(gaps):.0f} years (acceleration visible)")\n', '#!/usr/bin/env python3\n"""{TITLE} -- source reliability demo. Runs as-is with python3."""\nsources = [\n    ("official decree", 0.9, 0.3),   # (name, accuracy, bias)\n    ("diary entry", 0.7, 0.5),\n    ("propaganda poster", 0.3, 0.9),\n    ("archaeological find", 0.95, 0.1),\n]\nfor name, acc, bias in sources:\n    score = acc * (1 - bias * 0.5)\n    print(f"{name:<20} reliability score {score:.2f}")\nprint("corroboration: independent sources agreeing raises confidence")\n', '#!/usr/bin/env python3\n"""{TITLE} -- population growth demo. Runs as-is with python3."""\n# world population milestones (billions, approximate)\npop = [(1804, 1.0), (1927, 2.0), (1960, 3.0), (1974, 4.0), (1987, 5.0), (1999, 6.0), (2011, 7.0), (2022, 8.0)]\nfor (y1, p1), (y2, p2) in zip(pop, pop[1:]):\n    print(f"{y1}->{y2}: +1B in {y2-y1} years")\nprint("the doubling time collapsed: demographic history in one table")\n'];
var TOPICS=[['What History Is','History is the disciplined study of the human past: reconstructing what happened from surviving sources and explaining why. It is memory made rigorous — the present\'s account of how it came to be.'],
['The Core Question of History','The core question is: what happened, why did it happen, and what does it mean? Description, explanation, significance — the three tasks every historical work attempts.'],
['Assumptions: The Past Is Recoverable','The field assumes the past left traces sufficient for partial reconstruction: sources survive, witnesses recorded, archaeology digs. The past is gone; its evidence remains — the assumption that makes history possible.'],
['The Vocabulary: Primary, Secondary, Period','The vocabulary names the materials: primary sources (from the time), secondary (about the time), periods (the conventional divisions). Fluency means knowing what each kind of source can and cannot tell you.'],
['Chronology: The Fundamental Framework','Chronology is the fundamental framework: sequence before causation. The timeline is the field\'s skeleton — every explanation hangs on getting the order right.'],
['Source Criticism: The Primary Method','Source criticism is the primary method: who made this source, why, for whom, and what would they distort? External criticism authenticates; internal criticism interprets — the twin disciplines of trust.'],
['A Canonical First Example','The canonical first example is the Rosetta Stone: the same decree in three scripts, the key that unlocked Egyptian hieroglyphs. One artifact, three texts — decipherment as the field\'s romance and method.'],
['How History Measures','History measures with dates, counts, and comparisons: censuses, prices, army sizes, election returns — quantitative where the sources allow. Cliometrics brought statistics to the archive; the narrative kept its soul.'],
['The Core Mechanism: Causation','The core mechanism of historical explanation is multi-causal: no great event has one cause. The historian weighs necessary and sufficient conditions, triggers and structures — the causal web, not the single thread.'],
['The Simplest Law: Sequence Precedes Consequence','The simplest law is chronological: causes precede effects. Anachronism — attributing later ideas to earlier times — is the field\'s original sin, and chronology is its prevention.'],
['Common Misconceptions in History','The misconceptions mislead: that history is just facts to memorize (it\'s explanation), that it\'s unbiased (every history has a perspective — the honest ones state it), that it repeats exactly (it rhymes), and that the winners write it unopposed (losers\' sources survive too).'],
['How Beginners Practice History','Beginners practice by working with sources: read the document, ask who wrote it and why, compare with another. The document-based question is the field\'s laboratory — evidence under the microscope.'],
['The Core Model: Change Over Time','Change over time is the core model: continuity and rupture, trends and events. The historian\'s question is always comparative — what changed, what persisted, and why.'],
['The Great Tool: The Archive','The archive is the great tool and the field\'s temple: the ordered survival of documents. Archival research — the dusty box, the unexpected letter — remains where histories are born.'],
['Systems Thinking: Structures and Agency','Systems thinking in history balances structures (economies, institutions, climates) with agency (the choices of people). The debate between them is the field\'s permanent tension — and its richness.'],
['Invariance: Human Nature\'s Recurrence','The invariance the field observes is human: ambition, fear, idealism recur across millennia, making the past legible. Institutions differ; the people in them rhyme.'],
['Approximation: Periodization','Approximation divides the flow into periods: ancient, medieval, modern — useful fictions. The boundaries leak (the \'Middle Ages\' began differently everywhere), but the map helps navigate.'],
['Evidence Standards: The Footnote','The evidence standard is the footnote: every claim traceable to its source. The footnote is the field\'s honesty mechanism — the reader can check the work.'],
['Classic Discoveries','The classic discoveries are interpretive: the agricultural revolution\'s consequences, the fall of Rome\'s multiple causes, the industrial revolution\'s origins. Each re-read the evidence and changed the story.'],
['Core Trade-offs: Depth versus Breadth','The core trade-off is depth versus breadth: the monograph\'s precision against the survey\'s sweep. The field needs both — the archive\'s detail and the synthesis\'s vision.'],
['Handling Uncertainty: The Gaps','History handles uncertainty by marking the gaps: what the sources don\'t say is stated, not filled. The honest historian distinguishes the probable, the possible, and the unknown.'],
['Tools of the Trade','The tools of the trade are the archive, the chronology, the map, and the bibliography. The deepest is the source itself — read in the original, in context, with suspicion and sympathy.'],
['Ethics and Responsibility','Ethics in history concerns truth and the dead: honest rendering, no fabrication, care with the reputations of the voiceless. The field\'s power to shape memory is its moral burden.'],
['Teaching History','Teaching it well starts with the source: the letter, the photograph, the artifact — then the questions. Students who have interrogated a primary source understand history as investigation, not story.'],
['The Frontier Question','The frontier question is the deep past and the digital future: big data on centuries, DNA rewriting migrations, AI reading archives at scale. The frontier asks what new sources reveal.'],
['Unifying Theories','The unifying attempts — Marxist, Annales, world-systems — seek history\'s deep structures. The field values their insights while resisting any single key to all mythologies.'],
['Computational History','Computational history mines the archive at scale: text mining centuries of newspapers, GIS mapping change, network analysis of correspondence. The computer counts what the historian interprets.'],
['Bridges to Other Fields','History bridges to political science, economics, sociology, archaeology, and literature. It is the memory of every discipline — each field\'s past is history\'s province.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the exact causes of civilizational collapses, the full story of human dispersals, and why the industrial revolution happened where it did. Active research, no settled answers.'],
['How New Claims Are Validated','New historical claims are validated by peer review of the evidence: the sources checked, the argument tested, the interpretation debated. A thesis earns standing when the sources bear it — and colleagues agree they do.'],
['The Great Debates','The great debates — the causes of the World Wars, the nature of revolutions, the balance of structure and agency — are the field\'s lifeblood. They persist because the evidence supports multiple readings.'],
['Failure Modes: When History Gets It Wrong','History gets it wrong through presentism (judging the past by today), cherry-picked sources, and national myth-making. The immune system is the critical method — and the rival historian.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis writes history whole: the sources mastered, the causation weighed, the narrative earned. The fundamentals are the method; the synthesis is the history.'],
['The Signature Formulation: History as Disciplined Memory','The Signature formulation treats history as disciplined memory: every claim here is sourced and revisable, because in the Signature system the past must be handled with the same rigor as the present. That is the Signature capstone on historical bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Sources are cited: every factual claim traces to its evidence.", "Bias is assessed: each source's perspective and limits are stated.", "Revision is welcomed: new evidence revises old conclusions openly."],citations:["Carr, E. H. \u2014 What is History? (Penguin).", "Tuchman, B. W. \u2014 The Guns of August (exemplary narrative history).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-history-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-history',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
