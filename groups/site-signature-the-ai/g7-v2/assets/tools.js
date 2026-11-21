var LIBS = [["text-shorten", "Shorten"], ["text-count", "Count"], ["text-clean", "Clean"], ["text-keywords", "Keywords"], ["text-summarize", "Summarize"], ["text-template", "Template Fill"], ["text-diff", "Diff Words"], ["text-wrap", "Wrap"], ["text-tone", "Tone Shift"], ["text-bullets", "Bullets"], ["think-steps", "Step Thinker"], ["think-proscons", "Pros & Cons"], ["think-decide", "Decider"], ["think-why", "Five Whys"], ["think-socratic", "Socratic Questions"], ["think-fermi", "Fermi Estimator"], ["think-invert", "Invert"], ["think-analogy", "Analogy"], ["think-assume", "Find Assumptions"], ["think-checklist", "Checklist"], ["mem-note", "Notes"], ["mem-facts", "Fact Store"], ["mem-pin", "Pin Board"], ["mem-timeline", "Timeline"], ["mem-review", "Review Scheduler"], ["mem-context", "Context Packer"], ["mem-session", "Session Log"], ["mem-export", "Memory Export"], ["mem-digest", "Digest"], ["mem-search", "Memory Search"], ["chat-persona", "Persona"], ["chat-greet", "Greeter"], ["chat-farewell", "Farewell"], ["chat-frames", "Prompt Frames"], ["chat-history", "History Keeper"], ["chat-suggest", "Reply Suggester"], ["chat-recap", "Chat Recap"], ["chat-emoji", "Mood Emoji"], ["chat-opener", "Opener"], ["chat-closer", "Closer"], ["search-score", "Scorer"], ["search-highlight", "Highlighter"], ["search-filter", "Filter List"], ["search-suggest", "Suggester"], ["search-rank", "Ranker"], ["search-snippet", "Snippet"], ["search-dedupe", "Dedupe"], ["search-group", "Group By"], ["search-page", "Paginator"], ["search-recent", "Recent Searches"], ["math-calc", "Safe Calculator"], ["math-stats", "Statistics"], ["math-percent", "Percent"], ["math-convert", "Unit Converter"], ["math-geometry", "Geometry"], ["math-finance", "Money Math"], ["math-random", "Random"], ["math-seq", "Sequences"], ["math-clamp", "Clamp & Round"], ["math-logic", "Logic"], ["web-query", "Query Strings"], ["web-url", "URL Tools"], ["web-share", "Share Links"], ["web-meta", "Meta Tags"], ["web-ping", "Ping"], ["web-get", "Get JSON"], ["web-retry", "Retry"], ["web-cache", "Cache"], ["web-embed", "Embed Tags"], ["web-sitemap", "Sitemap"], ["data-json", "JSON Tools"], ["data-csv", "CSV Tools"], ["data-table", "Markdown Table"], ["data-sort", "Sort By"], ["data-chunk", "Chunk"], ["data-flatten", "Flatten"], ["data-hash", "Hash & ID"], ["data-validate", "Validate"], ["data-download", "Download Text"], ["data-lines", "Lines"], ["voice-speak", "Speak"], ["voice-stop", "Stop Voice"], ["voice-chunk", "Speech Chunks"], ["voice-presets", "Voice Presets"], ["voice-queue", "Speech Queue"], ["voice-buttons", "Read Buttons"], ["voice-announce", "Announce"], ["voice-captions", "Captions"], ["voice-clean", "Clean Transcript"], ["voice-rate", "Reading Time"], ["safe-honesty", "Honesty Notes"], ["safe-pii", "Redact PII"], ["safe-clamp", "Clamp Output"], ["safe-disclaimer", "Disclaimers"], ["safe-hedge", "Hedge Check"], ["safe-kid", "Kid Filter"], ["safe-guard", "Prompt Guard"], ["safe-ratelimit", "Rate Limit"], ["safe-audit", "Audit Log"], ["safe-license", "License Text"], ["embed-snippet", "Embed Code"], ["embed-ask", "Ask Snippet"], ["embed-chatbox", "Chat Box"], ["embed-dictlink", "Dictionary Link"], ["embed-sectionlink", "Section Link"], ["embed-loader", "Library Loader"], ["embed-optimal", "Optimal Apply"], ["embed-status", "Status Pill"], ["embed-manifest", "Manifest URL"], ["embed-copybtn", "Copy Button"], ["fun-joke", "Joke Setups"], ["fun-story", "Story Starters"], ["fun-haiku", "Haiku"], ["fun-riddle", "Riddles"], ["fun-name", "AI Namer"], ["fun-praise", "Praise"], ["fun-quest", "Quest Maker"], ["fun-mashup", "Mashup"], ["fun-emoji", "Emoji Story"], ["fun-banner", "Banner"], ["conv-deep-talk", "Deep Talk"], ["conv-ecosystem-guide", "Ecosystem Guide"], ["conv-socratic", "Socratic Reasoner"], ["conv-story-weaver", "Story Weaver"], ["conv-debate", "Debate Partner"]];
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }

function tokenEstimate(words){
  var w=Number(words);
  if(!isFinite(w)) return {error:'Enter a number of words.'};
  if(w<0||Math.floor(w)!==w) return {error:'Word count must be a whole number, zero or more.'};
  if(w===0) return {words:0, tokens:0};
  return {words:w, tokens:Math.round(w*1.3)};
}
function librarySearch(q){
  if(!q||typeof q!=='string') return [];
  var needle=q.toLowerCase().trim();
  if(!needle) return [];
  var out=[];
  for(var i=0;i<LIBS.length && out.length<10;i++){
    if(LIBS[i][0].toLowerCase().indexOf(needle)!==-1 || LIBS[i][1].toLowerCase().indexOf(needle)!==-1) out.push(LIBS[i][1]+' ('+LIBS[i][0]+')');
  }
  return out;
}
var TITLES = ["Shorten", "Count", "Clean", "Keywords", "Summarize", "Template Fill", "Diff Words", "Wrap", "Tone Shift", "Bullets", "Step Thinker", "Pros & Cons", "Decider", "Five Whys", "Socratic Questions", "Fermi Estimator", "Invert", "Analogy", "Find Assumptions", "Checklist", "Notes", "Fact Store", "Pin Board", "Timeline"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var t=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: Lumen lit the Engine Hall and found "'+t+'" on the last shelf — filed under "L".';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { tokenEstimate: tokenEstimate, librarySearch: librarySearch, makeFun: makeFun };
