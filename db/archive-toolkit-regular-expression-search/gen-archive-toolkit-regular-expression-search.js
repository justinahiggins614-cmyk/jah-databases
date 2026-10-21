(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK103-";
var KIND="search method";
var TOOLNAME="Regular Expression Search";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Literal and metacharacter basics", "d": "A regex is a pattern where most characters match themselves and metacharacters like . * + ? carry special meaning. Escaping with a backslash turns a metacharacter back into a literal, so '\\.' matches a real period. Knowing exactly which characters are special in the engine at hand prevents the most common pattern bugs.", "c": "fundamentals", "r": 1, "p": {"PATTERN": "archive\\.txt", "TEXT": "see archive.txt and archive_txt here"}}, {"t": "Character classes", "d": "Bracket expressions like [0-9] or [a-zA-Z] match any single character from the listed set. Negated classes [^0-9] match anything outside the set, and shorthands like \\d, \\w, \\s cover the everyday cases. Classes keep patterns readable where alternations of single characters would sprawl.", "c": "algorithms", "r": 1, "p": {"PATTERN": "JAH-[0-9]+", "TEXT": "ids JAH-101 and JAH-202, not JAH-"}}, {"t": "Quantifiers: greedy and lazy", "d": "Quantifiers *, +, ?, and {m,n} repeat the preceding atom; by default they are greedy, consuming as much as possible. Appending ? makes them lazy, matching as little as possible, which changes what '<.*>' captures in '<a><b>'. Choosing greedy versus lazy correctly is the difference between one big match and many small ones.", "c": "implementation", "r": 1, "p": {"PATTERN": "<.*?>", "TEXT": "<a>one</a> <b>two</b>"}}, {"t": "Anchors and boundaries", "d": "The anchors ^ and $ pin a match to the start or end of the string (or line, in multiline mode). The word boundary \\b sits between word and non-word characters, so '\\bcat\\b' skips 'catalog'. Anchors turn substring search into whole-field validation, the basis of input checking.", "c": "optimization", "r": 1, "p": {"PATTERN": "^Chapter [0-9]+", "TEXT": "Chapter 3 begins\\nsee Chapter 3 later"}}, {"t": "Groups and capturing", "d": "Parentheses group atoms for quantification and alternation, and by default they also capture the matched text. Numbered backreferences \\1, \\2 reuse a captured group later in the same pattern, enabling duplicate-word detection. Non-capturing groups (?:...) give the grouping without the bookkeeping overhead.", "c": "evaluation", "r": 1, "p": {"PATTERN": "(\\w+) \\1", "TEXT": "the the quick brown fox fox jumped"}}, {"t": "Alternation", "d": "The pipe a|b tries the left branch first and falls back to the right, scoped by the enclosing group. Ordering matters: 'cat|catalog' on 'catalog' matches just 'cat' unless the longer branch comes first or a boundary is added. Alternation is how patterns express synonyms and spelling variants in one pass.", "c": "fundamentals", "r": 2, "p": {"PATTERN": "catalog|index|archive", "TEXT": "the archive index and the catalog"}}, {"t": "Backreferences and lookarounds", "d": "Lookahead (?=...) and lookbehind (?<=...) assert context without consuming characters, so '\\w+(?=:) ' finds labels. Negative variants (?!...) and (?<!...) assert absence, the regex way of saying 'not followed by'. These zero-width assertions add boolean-style conditions to otherwise linear patterns.", "c": "algorithms", "r": 2, "p": {"PATTERN": "\\w+(?=:)", "TEXT": "title: Hello\\nbody: World"}}, {"t": "NFA simulation and backtracking", "d": "Most popular engines implement regexes as nondeterministic finite automata explored with backtracking. Backtracking tries one path, and on failure rewinds to the last choice point to try another, which is why nested quantifiers like '(a+)+$' can explode exponentially. Understanding backtracking explains catastrophic slowdowns and motivates possessive quantifiers and atomic groups.", "c": "implementation", "r": 2, "p": {"PATTERN": "(a+)+$", "TEXT": "aaaaaaaab"}}, {"t": "DFA-based matching", "d": "DFA engines convert the pattern to a deterministic automaton once, then scan the text in guaranteed linear time. They give up backreferences and lookarounds but never suffer catastrophic backtracking. For untrusted patterns or huge inputs, linear-time engines are the safe choice.", "c": "optimization", "r": 2, "p": {"PATTERN": "a+b", "TEXT": "aaab aab ab"}}, {"t": "Regex over large archives", "d": "Scanning terabytes with one regex is I/O-bound, so engines split work across chunks and stream matches without loading whole files. Pre-filters like trigram indexes skip chunks that cannot match, running the full regex only on candidates. This two-phase design is how code search tools stay fast over entire repositories.", "c": "evaluation", "r": 2, "p": {"PATTERN": "TODO|FIXME", "TEXT": "line one\\nTODO: fix this\\nline three"}}, {"t": "Multiline and dotall modes", "d": "By default ^ and $ anchor to the whole string and . skips newlines; multiline mode makes anchors per-line and dotall lets . cross lines. Flags (or inline (?m), (?s)) switch these behaviors without rewriting the pattern. Choosing the right mode is essential when patterns span log entries or document sections.", "c": "fundamentals", "r": 3, "p": {"PATTERN": "(?m)^ERROR.*", "TEXT": "INFO ok\\nERROR disk full\\nINFO ok"}}, {"t": "Unicode character properties", "d": "Modern engines match by Unicode property, so '\\p{L}+' finds letters in any script, not just ASCII. Case-insensitive matching then follows Unicode case folding rules rather than ASCII upper/lower tables. Property-based patterns keep multilingual archives searchable with a single expression.", "c": "algorithms", "r": 3, "p": {"PATTERN": "\\w+", "TEXT": "café naïve resume"}}, {"t": "Replacement with regex", "d": "Substitution replaces each match with a template that can reference captured groups, as in re.sub(r'(\\w+)@(\\w+)', r'\\2/\\1'). A replacement function can compute the substitute per match, enabling normalization and redaction pipelines. Regex replacement is the engine inside most text-cleaning workflows.", "c": "implementation", "r": 3, "p": {"PATTERN": "(\\d{3})-(\\d{4})", "TEXT": "call 555-1234 now"}}, {"t": "Pattern testing and debugging", "d": "Testers run a pattern against positive and negative example strings before it touches real data. Debuggers visualize the automaton or trace backtracking steps to reveal why a match failed or ran long. A pattern without tests is a bug waiting for production data.", "c": "optimization", "r": 3, "p": {"PATTERN": "^[A-Z]{2,4}-[0-9]{3,5}$", "TEXT": "JAH-101\\nJAH-12345\\njah-101\\nTOOL-99"}}, {"t": "From regex to index-assisted search", "d": "Trigram indexes extract all 3-character substrings of both the corpus and the pattern's required literals. Chunks lacking a required trigram are skipped without running the regex at all. This is how indexed code search answers regex queries over millions of files in under a second.", "c": "evaluation", "r": 3, "p": {"PATTERN": "archive_[0-9]+", "TEXT": "file archive_42 here\\nno match there"}}];
var DEMO="# Regex search: compile the pattern once, scan each line, report matches with spans.\nimport re\ntext = \"\"\"%%TEXT%%\"\"\"\npattern = r\"%%PATTERN%%\"\nrx = re.compile(pattern)\nprint(\"Pattern:\", pattern)\nfound = False\nfor i, line in enumerate(text.splitlines(), 1):\n    for m in rx.finditer(line):\n        found = True\n        print(f\"line {i} [{m.start()}:{m.end()}]: {m.group(0)!r}\")\nif not found:\n    print(\"no matches\")\n";
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
  if(!new RegExp("^JAH\\-ATK103\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-regular-expression-search-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-regular-expression-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
