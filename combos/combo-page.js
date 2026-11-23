/* combo-page.js — browser build of the Word-Combo generator template.
 *
 * Part of Word-Combo Websites Wave 1 (Router site: signature-word-combos).
 * Loaded by the repo-level 404.html fallback for any combos/<slug>/ URL that
 * has no stored page, and by nothing else. It renders the combo's full
 * 10-section page in the browser from the combo's words, using the same
 * template logic as word-combo-gen 1.0.1 (gen-word-combo.js) — same sections,
 * same demo choice, same demo code, same boundary refusal, same definition
 * labels — so a stored page and a generated page are the same page shape.
 *
 * Data fetched at render time (all shipped under combos/data/):
 *   definitions-lookup.json, demand-lists.json, demo-data.json,
 *   wave1-index.json, vocabulary.json (1.2 MB; needed only for the rank).
 * If a fetch fails, the page says so and renders what it can — it never
 * invents a definition, a rank, or a demo.
 *
 * SPACE SIZES: the SPACE constants below are the verified math.perm(102223,k)
 * values (see data/space-sizes.json). word-combo-gen 1.0.0's combo-lib.js
 * carried WRONG SPACE constants for k=3..7 — fixed in 1.0.1 (see DEFECTS.md);
 * this file always used the verified values. Ranks are computed with
 * permBigInt, which was correct in the generator.
 *
 * No dependencies. Works in a browser (window) and under Node with an
 * injected env (the CHECK 1 DOM-stub harness) — see renderCombo(env, ...).
 * When loaded in a browser it does NOT auto-render: 404.html calls
 * ComboPage.renderFromLocation(document) after load.
 */
(function (global) {
  "use strict";

  var GEN_VERSION = "word-combo-gen 1.0.1";
  var BUILD_DATE = "2026-11-23";
  var VOCAB_N = 102223;
  /* Verified math.perm(102223,k) — NOT the generator's combo-lib.js values. */
  var SPACE = {
    2: 10449439506n,
    3: 1068152155742826n,
    4: 109186513360031673720n,
    5: 11160936209149077655984680n,
    6: 1140848577426800419839442020240n,
    7: 116614119038835258514728244982872080n
  };
  var SPACE_TOTAL_2_TO_7 = 116615259898573730711878684717733052n;

  function slugify(text) {
    return String(text).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  }
  function comboSlug(words) {
    return words.map(function (w) { return slugify(w); }).join("-");
  }
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }

  function permBigInt(n, k) {
    var r = 1n;
    for (var i = 0; i < k; i++) r *= BigInt(n - i);
    return r;
  }

  function computeRank(words, vocabIndex) {
    var lows = words.map(function (w) { return w.toLowerCase(); });
    if (new Set(lows).size !== lows.length) {
      return { rank: null, reason: "a word repeats, so the combo is not an ordered combo of distinct headwords" };
    }
    var missing = lows.filter(function (w) { return !vocabIndex.has(w); });
    if (missing.length > 0) {
      return { rank: null, reason: missing.join(", ") + " is not among the 102,223 Dictionary headwords" };
    }
    var k = lows.length;
    var used = new Set();
    var rank = 0n;
    for (var i = 0; i < k; i++) {
      var idx = vocabIndex.get(lows[i]);
      var usedBefore = 0;
      used.forEach(function (u) { if (vocabIndex.get(u) < idx) usedBefore++; });
      var c = idx - usedBefore;
      rank += BigInt(c) * permBigInt(VOCAB_N - 1 - i, k - 1 - i);
      used.add(lows[i]);
    }
    return { rank: rank, reason: null };
  }

  function permutations(words, cap) {
    var out = [];
    var arr = words.slice();
    function gen(start) {
      if (out.length >= cap) return;
      if (start === arr.length) { out.push(arr.slice()); return; }
      for (var i = start; i < arr.length; i++) {
        var t = arr[start]; arr[start] = arr[i]; arr[i] = t;
        gen(start + 1);
        t = arr[start]; arr[start] = arr[i]; arr[i] = t;
        if (out.length >= cap) return;
      }
    }
    gen(0);
    return out;
  }
  function factorial(n) { var r = 1; for (var i = 2; i <= n; i++) r *= i; return r; }

  /* Boundary refusal — same list as combo-lib.js BLOCKED_PHRASES. */
  var BLOCKED_PHRASES = [
    "anthrax", "botulinum", "ricin", "sarin", "soman", "tabun", "vx nerve",
    "mustard gas", "bioweapon", "bio weapon", "gene drive", "gain of function",
    "gain-of-function", "smallpox", "ebola", "marburg", "weaponized",
    "warhead", "ballistic missile", "nuclear weapon", "dirty bomb",
    "bomb making", "bomb-making", "explosive", "explosives", "pathogen weapon",
    "toxin weapon", "toxin extraction", "nerve agent", "chemical weapon",
    "biological weapon", "plague weapon", "cholera weapon", "tularemia",
    "y pestis", "h5n1", "gain-of-function research",
    "defeat missile defense", "defeat air defense", "defeat radar",
    "bypass missile defense", "evade missile defense"
  ];
  var ATTACK_WORDS = new Set(["defeat", "destroy", "disable", "disrupt", "attack", "sabotage", "jam", "spoof", "evade", "bypass", "overwhelm", "penetrate", "neutralize", "blind", "cripple"]);
  var MILITARY_WORDS = new Set(["missile", "radar", "aircraft", "warship", "submarine", "tank", "artillery", "airbase", "aircraft carrier", "fighter", "bomber", "satellite", "drone", "antiaircraft", "anti-aircraft", "defense", "defence", "military", "army", "navy", "airforce", "air force", "iron dome", "patriot", "aegis", "s-400", "s400"]);

  function checkBoundary(words) {
    var joined = " " + words.map(function (w) { return w.toLowerCase(); }).join(" ") + " ";
    var norm = joined.replace(/-/g, " ");
    for (var i = 0; i < BLOCKED_PHRASES.length; i++) {
      var phrase = BLOCKED_PHRASES[i];
      var p = " " + phrase.toLowerCase().replace(/-/g, " ") + " ";
      if (norm.includes(p) || norm.includes(" " + phrase.toLowerCase() + " ")) {
        return { refused: true, reason: "blocked phrase: '" + phrase + "'", matched: phrase };
      }
    }
    var lows = words.map(function (w) { return w.toLowerCase(); });
    var hasAttack = lows.some(function (w) { return ATTACK_WORDS.has(w); });
    var hasMilitary = lows.some(function (w) { return MILITARY_WORDS.has(w); }) ||
      norm.includes(" air defense ") || norm.includes(" missile defense ");
    if (hasAttack && hasMilitary) {
      return { refused: true, reason: "pairs an attack/defeat word with a military-system word (standing boundary: no defeat-military-system content)", matched: "attack+military" };
    }
    return { refused: false, reason: null, matched: null };
  }

  /* Demo choice — same whole-word logic as combo-lib.js chooseDemo. */
  var TOOL_LAST_WORDS = new Set(["generator", "calculator", "converter", "tracker", "planner",
    "editor", "maker", "creator", "builder", "finder", "reader", "platform", "service",
    "assistant", "tool", "game", "games", "simulator", "composer", "organizer", "directory"]);

  function chooseDemo(words, slug) {
    var lows = words.map(function (w) { return w.toLowerCase(); });
    var last = lows[lows.length - 1];
    var joined = lows.join(" ");
    var has = function () {
      var ts = Array.prototype.slice.call(arguments);
      return ts.some(function (t) { return lows.includes(t) || lows.some(function (w) { return w.split("-").includes(t); }); });
    };
    if (slug === "joke-generator" || has("joke")) return { kind: "joke", note: "Joke bank held in this package (Signature-original jokes)." };
    if (slug === "daily-trivia" || has("trivia")) return { kind: "trivia", note: "Trivia bank held in this package (fact-checked questions)." };
    if (slug === "number-puzzles" || has("number", "puzzle")) return { kind: "number-puzzle", note: "Number-sequence puzzles generated from held formulas." };
    if (slug === "memory-games" || has("memory")) return { kind: "memory-game", note: "Concentration game using words held in this package." };
    if (has("caption")) return { kind: "caption-composer", note: "Caption composer from held templates and your words." };
    if (has("monster", "superhero", "superpower", "creature")) return { kind: "creature-creator", note: "Creature builder from held word lists." };
    if (has("ebook", "newsletter", "audiobook")) return { kind: "text-composer", note: "Text composer that assembles your title and sections into a downloadable file." };
    if (has("mortgage", "loan", "interest") && last === "calculator" || has("mortgage")) return { kind: "mortgage", note: "Real amortisation maths from your inputs; an illustration, not financial advice." };
    if (has("percentage")) return { kind: "percentage", note: "Real percentage arithmetic from your inputs." };
    if (has("age") || has("date")) return { kind: "age-date", note: "Real date arithmetic from your inputs." };
    if (has("grade", "gpa")) return { kind: "grade-gpa", note: "Real weighted-average arithmetic from your inputs." };
    if (has("statistics")) return { kind: "statistics", note: "Real statistics (mean, median, mode, range) from your numbers." };
    if (has("probability")) return { kind: "probability", note: "Exact dice and coin probabilities from held maths." };
    if (has("fitness")) return { kind: "fitness-bmi", note: "Real body-mass-index arithmetic from your inputs." };
    if (has("retirement", "inflation")) return { kind: "compound-interest", note: "Compound-growth illustration from a rate you enter; not a forecast." };
    if (has("time-zone", "time zone")) return { kind: "time-zone", note: "Real time-zone conversion using the browser's own zone data." };
    if (has("unit", "measurement", "construction")) return { kind: "unit-converter", note: "Unit conversion from held conversion factors." };
    if (has("currency")) return { kind: "explorer", note: "No live exchange rates are held in this package, so no currency converter is faked; the explorer below is the honest demo." };
    if (has("tax", "salary", "paycheck")) return { kind: "percentage", note: "Rate-based arithmetic from a rate you enter; no tax table is held, so no tax figure is invented." };
    if (has("tracker", "planner", "organizer", "journal", "diary", "calendar") || has("habit", "goal", "meal", "workout", "wardrobe", "gardening", "content")) return { kind: "tracker", note: "A working in-page list tracker: add items and tick them off." };
    if (has("chess", "checkers")) return { kind: "explorer", note: "No chess or checkers engine is held in this package, so no game is faked; the explorer below is the honest demo." };
    if (joined.startsWith("guess-the") || has("guess-the-picture", "guess-the-song", "guess-the-movie", "guess-the-personality")) return { kind: "explorer", note: "No picture, song, movie or personality data is held in this package, so no guessing game is faked; the explorer below is the honest demo." };
    if (has("coupon", "discount", "price-drop", "marketplace", "storefront", "discovery", "directory", "community", "encyclopedia", "dictionary")) return { kind: "explorer", note: "This combo names a collection or a community, not a single tool; the explorer below is the demo." };
    if (TOOL_LAST_WORDS.has(last)) return { kind: "explorer", note: "No genuine tool for this combo can be built from data held in this package, so the page says so plainly and the explorer below is the demo — never a fake tool." };
    return { kind: "explorer", note: "The combo explorer is the demo: define each word, see permutations, and follow related combos." };
  }

  function spaceLine(k) {
    return "P(102,223," + k + ") = " + fmt(SPACE[k]);
  }

  /* --- data loading ------------------------------------------------------ */
  function siteRootFromPath(pathname) {
    var i = pathname.indexOf("/combos/");
    if (i < 0) return "";
    return pathname.slice(0, i);
  }
  function fetchJson(env, url) {
    return env.fetch(url).then(function (r) {
      if (!r.ok) throw new Error("fetch failed: " + url + " (" + r.status + ")");
      return r.json();
    });
  }
  function loadData(env, root) {
    var base = root + "/combos/data/";
    return Promise.all([
      fetchJson(env, base + "definitions-lookup.json").catch(function () { return { definitions: {} }; }),
      fetchJson(env, base + "demand-lists.json").catch(function () { return { list03: [], list04: [] }; }),
      fetchJson(env, base + "demo-data.json").catch(function () { return { jokes: [], trivia: [], memory_words: [], caption_templates: [], creature_parts: { bodies: [], heads: [], homes: [], powers: [] } }; }),
      fetchJson(env, base + "wave1-index.json").catch(function () { return { combos: {} }; }),
      fetchJson(env, base + "vocabulary.json").catch(function () { return null; })
    ]).then(function (parts) {
      var vocab = parts[4];
      var vocabIndex = null, vocabSet = null;
      if (vocab && vocab.words) {
        vocabIndex = new Map();
        vocab.words.forEach(function (w, i) { vocabIndex.set(w.toLowerCase(), i); });
        vocabSet = new Set(vocab.words.map(function (w) { return w.toLowerCase(); }));
      }
      return { lookup: parts[0].definitions || {}, demand: parts[1], demo: parts[2],
               index: parts[3].combos || {}, vocabIndex: vocabIndex, vocabSet: vocabSet,
               vocabLoaded: !!vocabIndex };
    });
  }

  /* Words for a slug: exact words from the demand lists first (this recovers
   * hyphenated words such as "photo-to-cartoon"), else split on hyphens.
   * The split reading is labelled on the rendered page. */
  function wordsForSlug(slug, data) {
    var lists = [data.demand.list03 || [], data.demand.list04 || []];
    for (var l = 0; l < lists.length; l++) {
      for (var i = 0; i < lists[l].length; i++) {
        if (lists[l][i].slug === slug) return { words: lists[l][i].words.slice(), exact: true };
      }
    }
    var parts = slug.split("-").filter(Boolean);
    return { words: parts.map(function (p) { return p; }), exact: false };
  }

  function resolveDefinitions(words, data) {
    return words.map(function (w) {
      var low = w.toLowerCase();
      var inVocab = data.vocabSet ? data.vocabSet.has(low) : null;
      if (inVocab === false) return { word: w, in_vocab: false, status: "not-a-headword", definitions: [], pos: "" };
      if (data.lookup[low]) {
        var d = data.lookup[low];
        return { word: w, in_vocab: true, status: d.status, definitions: d.definitions, pos: d.pos || "" };
      }
      if (inVocab === true) return { word: w, in_vocab: true, status: "not-held", definitions: [], pos: "" };
      /* Vocabulary file did not load: cannot tell headword from non-headword. */
      return { word: w, in_vocab: null, status: "unknown-vocabulary-not-loaded", definitions: [], pos: "" };
    });
  }

  function relatedCombos(words, data, selfSlug) {
    var lows = new Set(words.map(function (w) { return w.toLowerCase(); }));
    var out = [];
    var seen = new Set([selfSlug]);
    var lists = [data.demand.list03 || [], data.demand.list04 || []];
    for (var l = 0; l < lists.length; l++) {
      for (var i = 0; i < lists[l].length; i++) {
        var item = lists[l][i];
        if (seen.has(item.slug)) continue;
        var shared = item.words.filter(function (w) { return lows.has(w.toLowerCase()); });
        if (shared.length > 0) { out.push({ slug: item.slug, title: item.title, shared: shared }); seen.add(item.slug); }
        if (out.length >= 12) return out;
      }
    }
    return out;
  }

  /* --- demos: ported from gen-word-combo.js demoFor ---------------------- */
  function demoFor(kind, data, words) {
    var J = JSON.stringify;
    switch (kind) {
      case "joke": return { html:
        '<p>Press the button for a joke from the held joke bank. The jokes are Signature-original, written for this package.</p>' +
        '<p id="joke-text"><b>Q:</b> ' + escapeHtml(data.demo.jokes[0].q) + '<br><b>A:</b> ' + escapeHtml(data.demo.jokes[0].a) + '</p>' +
        '<button id="joke-btn" type="button">Next joke</button>',
        script: 'var JOKES=' + J(data.demo.jokes) + ';var ji=0;' +
          'document.getElementById("joke-btn").addEventListener("click",function(){ji=(ji+1)%JOKES.length;' +
          'document.getElementById("joke-text").innerHTML="<b>Q:</b> "+esc(JOKES[ji].q)+"<br><b>A:</b> "+esc(JOKES[ji].a);});' };
      case "trivia": return { html:
        '<p>One question at a time from the held trivia bank. Answers are plain verifiable facts.</p>' +
        '<p id="trivia-q"><b>Q:</b> ' + escapeHtml(data.demo.trivia[0].q) + '</p>' +
        '<p id="trivia-a" hidden><b>A:</b> ' + escapeHtml(data.demo.trivia[0].a) + '</p>' +
        '<button id="trivia-reveal" type="button">Reveal answer</button> <button id="trivia-next" type="button">Next question</button>',
        script: 'var TRIVIA=' + J(data.demo.trivia) + ';var ti=0;' +
          'function showTrivia(){document.getElementById("trivia-q").innerHTML="<b>Q:</b> "+esc(TRIVIA[ti].q);' +
          'document.getElementById("trivia-a").innerHTML="<b>A:</b> "+esc(TRIVIA[ti].a);' +
          'document.getElementById("trivia-a").hidden=true;}' +
          'document.getElementById("trivia-reveal").addEventListener("click",function(){document.getElementById("trivia-a").hidden=false;});' +
          'document.getElementById("trivia-next").addEventListener("click",function(){ti=(ti+1)%TRIVIA.length;showTrivia();});' };
      case "number-puzzle": {
        var seqs = [
          { seq: [2, 5, 8, 11], next: 14, rule: "add 3 each time" },
          { seq: [3, 6, 12, 24], next: 48, rule: "double each time" },
          { seq: [1, 4, 9, 16], next: 25, rule: "square numbers: 1, 4, 9, 16, 25" },
          { seq: [5, 10, 15, 20], next: 25, rule: "add 5 each time" }
        ];
        return { html:
          '<p>What comes next? The sequences are generated from held formulas; the rule is revealed after you answer.</p>' +
          '<p id="seq-text"><b>Sequence:</b> 2, 5, 8, 11, ?</p>' +
          '<label>Your answer: <input id="seq-in" type="number"></label> <button id="seq-check" type="button">Check</button>' +
          '<p id="seq-out"></p><button id="seq-next" type="button">Next sequence</button>',
          script: 'var SEQS=' + J(seqs) + ';var si=0;' +
            'function showSeq(){document.getElementById("seq-text").innerHTML="<b>Sequence:</b> "+SEQS[si].seq.join(", ")+", ?";' +
            'document.getElementById("seq-out").textContent="";document.getElementById("seq-in").value="";}' +
            'document.getElementById("seq-check").addEventListener("click",function(){var v=Number(document.getElementById("seq-in").value);' +
            'document.getElementById("seq-out").textContent=(v===SEQS[si].next?"Correct. ":"Not that one. ")+"The rule is: "+SEQS[si].rule+".";});' +
            'document.getElementById("seq-next").addEventListener("click",function(){si=(si+1)%SEQS.length;showSeq();});' };
      }
      case "memory-game": {
        var w = data.demo.memory_words;
        var cards = w.concat(w);
        return { html:
          '<p>Find the matching pairs. The words come from the held word list in this package.</p>' +
          '<div id="mem-board"></div><p id="mem-out">Pairs found: 0 of ' + w.length + '</p>' +
          '<button id="mem-reset" type="button">Shuffle again</button>',
          script: 'var MEMWORDS=' + J(cards) + ';var memFirst=null,memLock=false,memFound=0;' +
            'function buildMem(){var b=document.getElementById("mem-board");b.innerHTML="";memFirst=null;memLock=false;memFound=0;' +
            'document.getElementById("mem-out").textContent="Pairs found: 0 of ' + w.length + '";' +
            'var order=MEMWORDS.map(function(x,i){return i;});' +
            'for(var i=order.length-1;i>0;i--){var j=(i*7+3)%(i+1);var t=order[i];order[i]=order[j];order[j]=t;}' +
            'order.forEach(function(ci){var btn=document.createElement("button");btn.type="button";btn.className="mem-card";' +
            'btn.textContent="?";btn.dataset.word=MEMWORDS[ci];' +
            'btn.addEventListener("click",function(){if(memLock||btn.dataset.done||btn===memFirst)return;' +
            'btn.textContent=btn.dataset.word;' +
            'if(!memFirst){memFirst=btn;return;}' +
            'if(memFirst.dataset.word===btn.dataset.word){memFirst.dataset.done="1";btn.dataset.done="1";memFirst=null;memFound++;' +
            'document.getElementById("mem-out").textContent="Pairs found: "+memFound+" of ' + w.length + '";}' +
            'else{memLock=true;var a=memFirst;setTimeout(function(){a.textContent="?";btn.textContent="?";memFirst=null;memLock=false;},800);}});' +
            'b.appendChild(btn);});}' +
            'document.getElementById("mem-reset").addEventListener("click",buildMem);buildMem();' };
      }
      case "tracker": return { html:
        '<p>Add an item, then tick it off when done. The list lives in this page only; nothing is sent anywhere.</p>' +
        '<label>New item: <input id="trk-in" type="text"></label> <button id="trk-add" type="button">Add</button>' +
        '<ul id="trk-list"></ul>',
        script: 'document.getElementById("trk-add").addEventListener("click",function(){var v=document.getElementById("trk-in").value.trim();' +
          'if(!v)return;var li=document.createElement("li");var cb=document.createElement("input");cb.type="checkbox";' +
          'li.appendChild(cb);li.appendChild(document.createTextNode(" "+v));' +
          'document.getElementById("trk-list").appendChild(li);document.getElementById("trk-in").value="";});' };
      case "caption-composer": return { html:
        '<p>Type a topic and get caption drafts from the held templates.</p>' +
        '<label>Topic: <input id="cap-in" type="text" value="' + escapeHtml(words.join(" ")) + '"></label> ' +
        '<button id="cap-go" type="button">Compose</button><ul id="cap-out"></ul>',
        script: 'var CAPT=' + J(data.demo.caption_templates) + ';' +
          'document.getElementById("cap-go").addEventListener("click",function(){var t=document.getElementById("cap-in").value.trim()||"this";' +
          'var ul=document.getElementById("cap-out");ul.innerHTML="";' +
          'CAPT.forEach(function(c){var li=document.createElement("li");li.textContent=c.split("{topic}").join(t);ul.appendChild(li);});});' +
          'document.getElementById("cap-go").click();' };
      case "creature-creator": return { html:
        '<p>Type a name and the builder assembles a creature from the held word lists. The same name always builds the same creature.</p>' +
        '<label>Name: <input id="cr-in" type="text" value="Moss"></label> <button id="cr-go" type="button">Build creature</button>' +
        '<p id="cr-out"></p>',
        script: 'var CR=' + J(data.demo.creature_parts) + ';' +
          'document.getElementById("cr-go").addEventListener("click",function(){var n=document.getElementById("cr-in").value.trim()||"Nameless";' +
          'var s=0;for(var i=0;i<n.length;i++)s+=n.charCodeAt(i);' +
          'var pick=function(a){return a[s%a.length];};' +
          'document.getElementById("cr-out").textContent=n+" is a creature with "+pick(CR.bodies)+", "+pick(CR.heads)+", living in "+pick(CR.homes)+", with "+pick(CR.powers)+".";});' +
          'document.getElementById("cr-go").click();' };
      case "text-composer": return { html:
        '<p>Write a title and up to three sections, then download the assembled text file. Nothing leaves your browser.</p>' +
        '<label>Title: <input id="tx-title" type="text" value="' + escapeHtml(words.join(" ")) + '"></label><br>' +
        '<label>Section 1:<br><textarea id="tx-s1" rows="3" cols="60"></textarea></label><br>' +
        '<label>Section 2:<br><textarea id="tx-s2" rows="3" cols="60"></textarea></label><br>' +
        '<button id="tx-dl" type="button">Download as text file</button>',
        script: 'document.getElementById("tx-dl").addEventListener("click",function(){var t=document.getElementById("tx-title").value.trim()||"Untitled";' +
          'var body=t+"\\n\\n"+document.getElementById("tx-s1").value+"\\n\\n"+document.getElementById("tx-s2").value+"\\n";' +
          'var a=document.createElement("a");a.href=URL.createObjectURL(new Blob([body],{type:"text/plain"}));' +
          'a.download=t.toLowerCase().replace(/[^a-z0-9]+/g,"-")+".txt";a.click();});' };
      case "mortgage": return { html:
        '<p>Enter the loan details. The monthly payment is computed with the standard amortisation formula. An illustration, not financial advice.</p>' +
        '<label>Amount: <input id="mg-p" type="number" value="200000"></label><br>' +
        '<label>Annual rate (%): <input id="mg-r" type="number" value="5" step="0.1"></label><br>' +
        '<label>Years: <input id="mg-y" type="number" value="25"></label><br>' +
        '<button id="mg-go" type="button">Calculate monthly payment</button><p id="mg-out"></p>',
        script: 'document.getElementById("mg-go").addEventListener("click",function(){var P=Number(document.getElementById("mg-p").value);' +
          'var r=Number(document.getElementById("mg-r").value)/100/12;var n=Number(document.getElementById("mg-y").value)*12;' +
          'if(!(P>0&&n>0)){document.getElementById("mg-out").textContent="Enter an amount and a term greater than zero.";return;}' +
          'var m=r===0?P/n:P*r/(1-Math.pow(1+r,-n));' +
          'document.getElementById("mg-out").textContent="Monthly payment: "+m.toFixed(2)+" (total paid "+(m*n).toFixed(2)+").";});' +
          'document.getElementById("mg-go").click();' };
      case "percentage": return { html:
        '<p>Percentage arithmetic from numbers you enter.</p>' +
        '<label><input id="pc-a" type="number" value="20"> % of <input id="pc-b" type="number" value="150"></label> ' +
        '<button id="pc-go" type="button">Calculate</button><p id="pc-out"></p>',
        script: 'document.getElementById("pc-go").addEventListener("click",function(){var a=Number(document.getElementById("pc-a").value);' +
          'var b=Number(document.getElementById("pc-b").value);' +
          'document.getElementById("pc-out").textContent=a+"% of "+b+" = "+(a*b/100)+". "+a+" is "+(b===0?"undefined":(a/b*100).toFixed(2)+"%")+" of "+b+".";});' +
          'document.getElementById("pc-go").click();' };
      case "age-date": return { html:
        '<p>Date arithmetic from dates you enter.</p>' +
        '<label>Birth date: <input id="ad-b" type="date" value="2000-01-01"></label> <button id="ad-age" type="button">How old?</button><p id="ad-out1"></p>' +
        '<label>From: <input id="ad-f" type="date" value="2026-01-01"></label> <label>To: <input id="ad-t" type="date" value="2026-11-23"></label> ' +
        '<button id="ad-days" type="button">Days between</button><p id="ad-out2"></p>',
        script: 'document.getElementById("ad-age").addEventListener("click",function(){var b=new Date(document.getElementById("ad-b").value);' +
          'if(isNaN(b)){document.getElementById("ad-out1").textContent="Enter a valid date.";return;}' +
          'var now=new Date();var age=now.getFullYear()-b.getFullYear();' +
          'if(now.getMonth()<b.getMonth()||(now.getMonth()===b.getMonth()&&now.getDate()<b.getDate()))age--;' +
          'document.getElementById("ad-out1").textContent="Age today: "+age+" years.";});' +
          'document.getElementById("ad-days").addEventListener("click",function(){var f=new Date(document.getElementById("ad-f").value);' +
          'var t=new Date(document.getElementById("ad-t").value);' +
          'if(isNaN(f)||isNaN(t)){document.getElementById("ad-out2").textContent="Enter two valid dates.";return;}' +
          'document.getElementById("ad-out2").textContent="Days between: "+Math.round((t-f)/86400000)+".";});' };
      case "unit-converter": return { html:
        '<p>Convert between units using the held conversion factors.</p>' +
        '<label>Value: <input id="uc-v" type="number" value="1"></label> ' +
        '<label>From: <select id="uc-f"><option>m</option><option>km</option><option>cm</option><option>mm</option><option>kg</option><option>g</option><option>lb</option><option>oz</option><option>C</option><option>F</option></select></label> ' +
        '<label>To: <select id="uc-t"><option>km</option><option>m</option><option>cm</option><option>mm</option><option>kg</option><option>g</option><option>lb</option><option>oz</option><option>C</option><option>F</option></select></label> ' +
        '<button id="uc-go" type="button">Convert</button><p id="uc-out"></p>',
        script: 'var U={m:1,km:1000,cm:0.01,mm:0.001,kg:1,g:0.001,lb:0.45359237,oz:0.028349523125};' +
          'document.getElementById("uc-go").addEventListener("click",function(){var v=Number(document.getElementById("uc-v").value);' +
          'var f=document.getElementById("uc-f").value,t=document.getElementById("uc-t").value,out=document.getElementById("uc-out");' +
          'if(f==="C"||f==="F"||t==="C"||t==="F"){if((f==="C"&&t==="F")||(f==="F"&&t==="C")){out.textContent=v+" "+f+" = "+(f==="C"?(v*9/5+32):((v-32)*5/9)).toFixed(2)+" "+t+".";}else{out.textContent="Temperature converts only between C and F here.";}return;}' +
          'var len=(f in U&&t in U);var sameGroup=(["m","km","cm","mm"].includes(f)===["m","km","cm","mm"].includes(t));' +
          'if(!len||!sameGroup){out.textContent="Those two units do not convert into each other here.";return;}' +
          'out.textContent=v+" "+f+" = "+(v*U[f]/U[t])+" "+t+".";});' +
          'document.getElementById("uc-go").click();' };
      case "time-zone": return { html:
        '<p>Convert a time between zones using the browser\u2019s own time-zone data.</p>' +
        '<label>Date and time: <input id="tz-d" type="datetime-local" value="2026-11-23T12:00"></label><br>' +
        '<label>From: <select id="tz-f"><option>UTC</option><option>America/New_York</option><option>America/Chicago</option><option>America/Denver</option><option>America/Los_Angeles</option><option>Europe/London</option><option>Europe/Paris</option><option>Asia/Tokyo</option><option>Australia/Sydney</option></select></label> ' +
        '<label>To: <select id="tz-t"><option>Europe/London</option><option>UTC</option><option>America/New_York</option><option>America/Chicago</option><option>America/Denver</option><option>America/Los_Angeles</option><option>Europe/Paris</option><option>Asia/Tokyo</option><option>Australia/Sydney</option></select></label> ' +
        '<button id="tz-go" type="button">Convert</button><p id="tz-out"></p>',
        script: 'document.getElementById("tz-go").addEventListener("click",function(){var raw=document.getElementById("tz-d").value;' +
          'if(!raw){document.getElementById("tz-out").textContent="Enter a date and time.";return;}' +
          'var f=document.getElementById("tz-f").value,t=document.getElementById("tz-t").value;' +
          'var parts=raw.split("T");var d=parts[0].split("-").map(Number);var tm=parts[1].split(":").map(Number);' +
          'var guess=Date.UTC(d[0],d[1]-1,d[2],tm[0],tm[1]);' +
          'function off(zone,ms){var s=new Intl.DateTimeFormat("en-US",{timeZone:zone,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",second:"2-digit",hour12:false}).format(new Date(ms));' +
          'var m=s.match(/(\\d+)\\/(\\d+)\\/(\\d+), (\\d+):(\\d+):(\\d+)/);return Date.UTC(+m[3],+m[1]-1,+m[2],+m[4]%24,+m[5],+m[6])-ms;}' +
          'var utc=guess-off(f,guess);' +
          'var out=new Intl.DateTimeFormat("en-GB",{timeZone:t,year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit"}).format(new Date(utc));' +
          'document.getElementById("tz-out").textContent=raw.replace("T"," ")+" in "+f+" is "+out+" in "+t+".";});' +
          'document.getElementById("tz-go").click();' };
      case "grade-gpa": return { html:
        '<p>Enter scores separated by commas for an average, or letter grades for a GPA.</p>' +
        '<label>Scores: <input id="gg-s" type="text" value="85, 90, 78, 92"></label> <button id="gg-avg" type="button">Average</button><p id="gg-out1"></p>' +
        '<label>Letter grades: <input id="gg-g" type="text" value="A, B, A, C"></label> <button id="gg-gpa" type="button">GPA</button><p id="gg-out2"></p>',
        script: 'var PTS={A:4,B:3,C:2,D:1,F:0};' +
          'document.getElementById("gg-avg").addEventListener("click",function(){var ns=document.getElementById("gg-s").value.split(",").map(function(x){return Number(x.trim());}).filter(function(x){return !isNaN(x);});' +
          'document.getElementById("gg-out1").textContent=ns.length?("Average: "+(ns.reduce(function(a,b){return a+b;},0)/ns.length).toFixed(2)+"."):"Enter at least one number.";});' +
          'document.getElementById("gg-gpa").addEventListener("click",function(){var gs=document.getElementById("gg-g").value.split(",").map(function(x){return x.trim().toUpperCase();}).filter(function(x){return x in PTS;});' +
          'document.getElementById("gg-out2").textContent=gs.length?("GPA: "+(gs.reduce(function(a,g){return a+PTS[g];},0)/gs.length).toFixed(2)+" (4.0 scale)."):"Enter letter grades A to F.";});' };
      case "statistics": return { html:
        '<p>Enter numbers separated by commas.</p>' +
        '<label>Numbers: <input id="st-n" type="text" value="4, 8, 15, 16, 23, 42"></label> <button id="st-go" type="button">Analyse</button><p id="st-out"></p>',
        script: 'document.getElementById("st-go").addEventListener("click",function(){var ns=document.getElementById("st-n").value.split(",").map(function(x){return Number(x.trim());}).filter(function(x){return !isNaN(x);}).sort(function(a,b){return a-b;});' +
          'if(!ns.length){document.getElementById("st-out").textContent="Enter at least one number.";return;}' +
          'var mean=ns.reduce(function(a,b){return a+b;},0)/ns.length;' +
          'var med=ns.length%2?ns[(ns.length-1)/2]:(ns[ns.length/2-1]+ns[ns.length/2])/2;' +
          'var counts={};ns.forEach(function(x){counts[x]=(counts[x]||0)+1;});var mode=null,best=0;' +
          'Object.keys(counts).forEach(function(k){if(counts[k]>best){best=counts[k];mode=k;}});' +
          'document.getElementById("st-out").textContent="Count "+ns.length+". Mean "+mean.toFixed(2)+". Median "+med+". Mode "+(best>1?mode:"none (no repeats)")+". Range "+(ns[ns.length-1]-ns[0])+".";});' +
          'document.getElementById("st-go").click();' };
      case "probability": return { html:
        '<p>Exact probabilities for one die roll and one coin toss.</p>' +
        '<label>Die sides: <input id="pr-s" type="number" value="6" min="2"></label> <label>Target face: <input id="pr-t" type="number" value="6" min="1"></label> ' +
        '<button id="pr-go" type="button">Probability</button><p id="pr-out"></p>',
        script: 'document.getElementById("pr-go").addEventListener("click",function(){var s=Math.floor(Number(document.getElementById("pr-s").value));' +
          'var t=Math.floor(Number(document.getElementById("pr-t").value));' +
          'if(!(s>=2&&t>=1&&t<=s)){document.getElementById("pr-out").textContent="Enter a die with at least 2 sides and a target face on it.";return;}' +
          'document.getElementById("pr-out").textContent="P(rolling "+t+" on a "+s+"-sided die) = 1/"+s+" = "+(100/s).toFixed(2)+"%. P(heads on one fair coin toss) = 1/2 = 50%.";});' +
          'document.getElementById("pr-go").click();' };
      case "fitness-bmi": return { html:
        '<p>Body-mass index from height and weight. A general guide only, not medical advice.</p>' +
        '<label>Height (cm): <input id="fb-h" type="number" value="175"></label> <label>Weight (kg): <input id="fb-w" type="number" value="70"></label> ' +
        '<button id="fb-go" type="button">Calculate BMI</button><p id="fb-out"></p>',
        script: 'document.getElementById("fb-go").addEventListener("click",function(){var h=Number(document.getElementById("fb-h").value)/100;' +
          'var w=Number(document.getElementById("fb-w").value);if(!(h>0&&w>0)){document.getElementById("fb-out").textContent="Enter a height and a weight greater than zero.";return;}' +
          'var bmi=w/(h*h);var cat=bmi<18.5?"underweight":bmi<25?"healthy weight":bmi<30?"overweight":"obese";' +
          'document.getElementById("fb-out").textContent="BMI: "+bmi.toFixed(1)+" ("+cat+" range, by the standard bands).";});' +
          'document.getElementById("fb-go").click();' };
      case "compound-interest": return { html:
        '<p>Compound growth from a rate you enter. An illustration, not a forecast and not financial advice.</p>' +
        '<label>Starting amount: <input id="ci-p" type="number" value="1000"></label> <label>Annual rate (%): <input id="ci-r" type="number" value="5" step="0.1"></label> <label>Years: <input id="ci-y" type="number" value="10"></label> ' +
        '<button id="ci-go" type="button">Project</button><p id="ci-out"></p>',
        script: 'document.getElementById("ci-go").addEventListener("click",function(){var p=Number(document.getElementById("ci-p").value);' +
          'var r=Number(document.getElementById("ci-r").value)/100;var y=Number(document.getElementById("ci-y").value);' +
          'if(!(p>=0&&y>=0)){document.getElementById("ci-out").textContent="Enter an amount and a number of years.";return;}' +
          'document.getElementById("ci-out").textContent="After "+y+" years at "+(r*100)+"% compounded yearly: "+(p*Math.pow(1+r,y)).toFixed(2)+".";});' +
          'document.getElementById("ci-go").click();' };
      default: return null; /* explorer */
    }
  }

  function explorerHtml(words, defs, related, perms, totalPerms) {
    var buttons = words.map(function (w, i) {
      return '<button type="button" class="word-btn" data-i="' + i + '">' + escapeHtml(w) + '</button>';
    }).join(" ");
    var defBoxes = defs.map(function (d, i) {
      var body;
      if (d.definitions.length) {
        var label = d.status === "authored" ? "Authored Dictionary definition" : "Template-filled Dictionary definition (labelled as such)";
        body = "<b>" + label + (d.pos ? " (" + escapeHtml(d.pos) + ")" : "") + ":</b> " +
          d.definitions.map(escapeHtml).join(" ");
      } else if (d.status === "pending") {
        body = "This headword's definition is still pending in the Dictionary (one of 2,644 pending headwords). No definition is invented here.";
      } else if (d.status === "not-held") {
        body = "This word is a Dictionary headword, but its definition is not held in this package. Check the Dictionary; no definition is invented here.";
      } else if (d.status === "unknown-vocabulary-not-loaded") {
        body = "The vocabulary file did not load in this rendering, so this word's Dictionary status could not be checked. No definition is invented here.";
      } else {
        body = "This word is not a Dictionary headword, so no Dictionary definition exists for it. None is invented here.";
      }
      return '<div class="word-def" id="def-' + i + '" hidden><b>' + escapeHtml(d.word) + ':</b> ' + body + '</div>';
    }).join("\n");
    var permList = perms.map(function (p) {
      return "<li>" + p.map(escapeHtml).join(" ") + " — <a href=\"../" + comboSlug(p) + "/\">combos/" + comboSlug(p) + "/</a></li>";
    }).join("\n");
    var relList = related.length
      ? related.map(function (r) { return "<li><a href=\"../" + r.slug + "/\">" + escapeHtml(r.title) + "</a> (shares: " + r.shared.map(escapeHtml).join(", ") + ")</li>"; }).join("\n")
      : "<li>None found in the demand lists.</li>";
    return '<p>Click a word to see its definition. Every permutation below links to its own combo page through the Router.</p>' +
      '<p>' + buttons + '</p>\n' + defBoxes +
      '<h3>Permutations</h3><p>This combo has ' + totalPerms + ' orderings. ' +
      (perms.length < totalPerms ? 'The first ' + perms.length + ' are listed:' : 'All are listed:') + '</p><ul>\n' + permList + '\n</ul>' +
      '<h3>Related combos from the demand lists</h3><ul>\n' + relList + '\n</ul>';
  }

  function explorerScript() {
    return 'document.querySelectorAll(".word-btn").forEach(function(b){b.addEventListener("click",function(){' +
      'var d=document.getElementById("def-"+b.dataset.i);if(d)d.hidden=!d.hidden;});});';
  }

  /* --- page rendering (ported from gen-word-combo.js buildPage) ----------- */
  function buildPageHtml(o) {
    var words = o.words, slug = o.slug, title = o.title, defs = o.defs,
        rankInfo = o.rankInfo, demo = o.demo, related = o.related,
        perms = o.perms, totalPerms = o.totalPerms, storedId = o.storedId,
        listItem = o.listItem;
    var k = words.length;
    var rankText = rankInfo.rank !== null
      ? "Its deterministic rank is <b>" + rankInfo.rank.toString() + "</b> (0-based) in the ordered " + k + "-word space, " + spaceLine(k) + ". The full ordered space of 2- to 7-word combos is " + fmt(SPACE_TOTAL_2_TO_7) + " combos."
      : rankInfo.notComputed
        ? "Its deterministic rank was not computed in this rendering, because the vocabulary file did not load. The " + k + "-word ordered space it would belong to has " + spaceLine(k) + ", out of " + fmt(SPACE_TOTAL_2_TO_7) + " ordered combos of 2 to 7 words. No rank is invented here."
        : "Its deterministic rank is not defined in the headword ordering, because " + escapeHtml(rankInfo.reason) + ". The " + k + "-word ordered space it would belong to has " + spaceLine(k) + ", out of " + fmt(SPACE_TOTAL_2_TO_7) + " ordered combos of 2 to 7 words.";
    var defParas = defs.map(function (d) {
      if (d.definitions.length) {
        var label = d.status === "authored" ? "an authored Dictionary definition" : "a template-filled Dictionary definition (labelled as such)";
        return "<p><b>" + escapeHtml(d.word) + "</b>" + (d.pos ? " (" + escapeHtml(d.pos) + ")" : "") + " has " + label + ": " + d.definitions.map(escapeHtml).join(" ") + "</p>";
      }
      if (d.status === "pending") return "<p><b>" + escapeHtml(d.word) + "</b> is a Dictionary headword whose definition is still pending (one of 2,644 pending headwords). No definition is invented here.</p>";
      if (d.status === "not-held") return "<p><b>" + escapeHtml(d.word) + "</b> is a Dictionary headword, but its definition is not held in this package. Check the Dictionary; no definition is invented here.</p>";
      if (d.status === "unknown-vocabulary-not-loaded") return "<p><b>" + escapeHtml(d.word) + "</b>: the vocabulary file did not load in this rendering, so no Dictionary status or definition is claimed for it. No definition is invented here.</p>";
      return "<p><b>" + escapeHtml(d.word) + "</b> is not a Dictionary headword, so no Dictionary definition exists for it. None is invented here.</p>";
    }).join("\n");
    var toolLike = demo.kind !== "explorer";
    var demoBlock = toolLike
      ? "<p>" + escapeHtml(demo.note) + "</p>\n" + demo.html
      : "<p>" + escapeHtml(demo.note) + "</p>\n" + explorerHtml(words, defs, related, perms, totalPerms);
    var isSentence = k >= 5;
    var reading = "The phrase names " + (toolLike ? "a tool or service" : isSentence ? "a question or an idea to be explained" : "a thing or topic") +
      " built from its words. This reading is a Signature reading of the phrase, labelled as such — not an established fact about any existing product.";
    var azLinks = words.map(function (w) {
      var ch = w.charAt(0).toLowerCase();
      var letter = /[a-z]/.test(ch) ? ch : "0";
      return '<a href="https://justinahiggins614-cmyk.github.io/jah-dictionary/az/' + letter + '.html">' + escapeHtml(w) + ' in the Dictionary A–Z</a>';
    }).join(" · ");
    var storedNote = storedId
      ? "This combo is one of the 103 stored Wave 1 combos (List 03 item " + listItem + ", pair record " + storedId + "). This copy was generated on demand at the same URL; the stored page is the frozen, verified copy."
      : "This combo is not a stored Wave 1 combo. It is generated on demand by the Combo Router at this same URL; no stored record exists for it, and none is claimed."
      + (o.wordsExact ? "" : " The words were read from the URL by splitting on hyphens; a hyphenated word reads as separate words here unless the combo is in the demand lists.");
    var css = "body{font-family:Georgia,serif;max-width:760px;margin:0 auto;padding:1em;line-height:1.55;color:#1a1a1a;background:#fff}"
      + "h1{font-size:1.6em}h2{border-top:1px solid #ccc;padding-top:.6em}button{cursor:pointer;padding:.4em .8em;margin:.2em}"
      + ".word-btn{font-size:1.1em}.word-def{border:1px solid #999;padding:.6em;margin:.4em 0;background:#f7f7f7}"
      + ".mem-card{width:3.2em;height:3.2em;margin:.15em;font-size:.9em}#mem-board{max-width:30em}"
      + "footer{border-top:2px solid #333;margin-top:2em;padding-top:.8em;font-size:.9em}input,select,textarea{padding:.3em;margin:.2em}";
    return "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      + "<title>" + escapeHtml(title) + " — Signature Word Combo</title>\n<style>" + css + "</style>\n</head>\n<body>\n"
      + "<h1>" + escapeHtml(title) + "</h1>\n<p><i>A Signature word-combo page. Stable URL: combos/" + slug + "/ — generated on demand by the Combo Router.</i></p>\n"
      + "<h2>1. What the combo means</h2>\n" + defParas
      + "\n<p><b>Signature reading.</b> " + escapeHtml(reading) + "</p>\n"
      + "<h2>2. Math proof</h2>\n<p>" + rankText + " Wave 1 stores 103 combo pages; every other combo of 2 to 7 words is generator option space, resolved on demand and never stored. The generator is deterministic: the same combo always produces the same page and the same record, and the hyphenated slug is the combo's identity, so no combo can be stored or generated twice under a different identity.</p>\n"
      + "<h2>3. Science proof</h2>\n<p>Word etymology and linguistics come from the Dictionary record for each word, linked below. " + (isSentence ? "This combo is a sentence-like query, so this section is a design-study explanation, labelled as such — not a claim about the world." : "Where the combo is speculative, this page labels it design-study or entertainment, never fact. No facts are invented here.") + "</p>\n"
      + "<h2>4. Relevant data</h2>\n<p>" + azLinks + "</p>\n<p>" + escapeHtml(storedNote) + "</p>\n"
      + "<h2>5. Spec</h2>\n<ul><li>Words: " + words.map(escapeHtml).join(", ") + "</li><li>Length class: " + k + "-word</li><li>Slug: " + slug + "</li><li>Generator: " + GEN_VERSION + " (browser build; space sizes are the verified math.perm values)</li><li>Verification stamp: " + GEN_VERSION + " / " + BUILD_DATE + "</li>" + (storedId ? "<li>Pair record: " + storedId + "</li>" : "<li>Pair record: none — generated on demand</li>") + "</ul>\n"
      + "<h2>6. Working demo</h2>\n" + demoBlock + "\n"
      + "<h2>7. Two AIs</h2>\n<p><b>Combo Librarian</b> answers what any combo means, finds related combos and live sites. <b>Combo Builder</b> generates a combo's page, spec and demo from this template. Both ship as downloadable specs with this page:</p>\n"
      + "<ul><li><button type=\"button\" data-spec=\"librarian\">Download combo-librarian.spec.md</button></li><li><button type=\"button\" data-spec=\"builder\">Download combo-builder.spec.md</button></li></ul>\n"
      + "<h2>8. Use</h2>\n<p>Search this combo, share its stable URL (combos/" + slug + "/), or build on it: the Combo Builder spec describes how to generate a page for any related combo.</p>\n"
      + "<h2>9. Sources</h2>\n<p>The Signature Dictionary headwords file (102,223 headwords, counted 2026-11-23); the Dictionary definitions file (99,579 defined: 58,223 authored, 41,356 template-filled, 2,644 pending); the trending/viral and future-internet demand lists; the live manifest of the jah-databases network (63,826 databases, read 2026-11-23). No external website was scraped; no brand name, logo, trademark, product name or copyrighted image appears anywhere on this page.</p>\n"
      + "<h2>10. Accessible version</h2>\n<p><a href=\"accessible.html\">Plain-HTML version of this page</a> — the same meaning, definitions, math, links and Use section, readable without JavaScript.</p>\n"
      + "<footer><p>THE JAH NETWORK — <a href=\"../index.html\">Combo Router</a> · <a href=\"https://justinahiggins614-cmyk.github.io/jah-dictionary/\">The Signature Dictionary</a> · <a href=\"https://justinahiggins614-cmyk.github.io/jah-databases/\">The 'Merica-L Boundless Ecosystem OS</a></p></footer>\n"
      + "</body>\n</html>\n";
  }

  function buildAccessibleHtml(o) {
    var words = o.words, slug = o.slug, title = o.title, defs = o.defs,
        rankInfo = o.rankInfo, demo = o.demo, related = o.related,
        storedId = o.storedId, listItem = o.listItem;
    var k = words.length;
    var rankText = rankInfo.rank !== null
      ? "Its deterministic rank is " + rankInfo.rank.toString() + " (0-based) in the ordered " + k + "-word space, " + spaceLine(k) + "."
      : rankInfo.notComputed
        ? "Its deterministic rank was not computed in this rendering (vocabulary file did not load). The " + k + "-word ordered space has " + spaceLine(k) + "."
        : "Its deterministic rank is not defined in the headword ordering, because " + escapeHtml(rankInfo.reason) + ". The " + k + "-word ordered space has " + spaceLine(k) + ".";
    var defParas = defs.map(function (d) {
      if (d.definitions.length) return "<p><b>" + escapeHtml(d.word) + ":</b> " + d.definitions.map(escapeHtml).join(" ") + " (" + (d.status === "authored" ? "authored" : "template-filled") + " Dictionary definition.)</p>";
      if (d.status === "pending") return "<p><b>" + escapeHtml(d.word) + ":</b> definition pending in the Dictionary; none is invented here.</p>";
      if (d.status === "not-held") return "<p><b>" + escapeHtml(d.word) + ":</b> a Dictionary headword whose definition is not held in this package; check the Dictionary.</p>";
      if (d.status === "unknown-vocabulary-not-loaded") return "<p><b>" + escapeHtml(d.word) + ":</b> vocabulary file did not load; no status claimed.</p>";
      return "<p><b>" + escapeHtml(d.word) + ":</b> not a Dictionary headword; no definition is invented here.</p>";
    }).join("\n");
    var demoStatic = demo.kind === "joke" && o.data.demo.jokes.length
      ? "<p>Demo (static sample; the full page has the working joke bank): Q: " + escapeHtml(o.data.demo.jokes[0].q) + " A: " + escapeHtml(o.data.demo.jokes[0].a) + "</p>"
      : demo.kind === "trivia" && o.data.demo.trivia.length
        ? "<p>Demo (static sample; the full page has the working trivia bank): Q: " + escapeHtml(o.data.demo.trivia[0].q) + " A: " + escapeHtml(o.data.demo.trivia[0].a) + "</p>"
        : "<p>Demo: " + escapeHtml(demo.note) + " The working demo needs JavaScript; see the full page.</p>";
    var relList = related.length
      ? "<ul>" + related.map(function (r) { return "<li><a href=\"../" + r.slug + "/\">" + escapeHtml(r.title) + "</a></li>"; }).join("\n") + "</ul>"
      : "<p>None found in the demand lists.</p>";
    return "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      + "<title>" + escapeHtml(title) + " — accessible version</title>\n</head>\n<body>\n"
      + "<h1>" + escapeHtml(title) + " (accessible version)</h1>\n<p>No JavaScript is used on this page. Full version: <a href=\"index.html\">index.html</a>.</p>\n"
      + "<h2>What the combo means</h2>\n" + defParas
      + "\n<p>Signature reading: the phrase names a tool, service, thing or question built from its words. This reading is a Signature reading, labelled as such — not an established fact.</p>\n"
      + "<h2>Math proof</h2>\n<p>" + rankText + " Wave 1 stores 103 combo pages; every other combo is generator option space.</p>\n"
      + "<h2>Relevant data</h2>\n<p>" + (storedId ? "Stored Wave 1 combo (List 03 item " + listItem + ", pair record " + storedId + ")." : "Generated on demand; no stored record exists for this combo.") + "</p>\n"
      + "<h2>Demo</h2>\n" + demoStatic + "\n"
      + "<h2>Related combos</h2>\n" + relList + "\n"
      + "<h2>Use</h2>\n<p>Search this combo, share its stable URL (combos/" + slug + "/), or build on it.</p>\n"
      + "<h2>Sources</h2>\n<p>The Signature Dictionary headwords (102,223) and definitions (99,579 defined: 58,223 authored, 41,356 template-filled, 2,644 pending); the demand lists; the live manifest (63,826 databases, 2026-11-23). Nothing was scraped; no brand names, logos, trademarks, product names or copyrighted images.</p>\n"
      + "</body>\n</html>\n";
  }

  function librarianSpec(o) {
    var words = o.words, slug = o.slug, title = o.title;
    return "# Combo Librarian — AI spec for the combo \"" + title + "\"\n\n" +
      "Generator: " + GEN_VERSION + " / " + BUILD_DATE + " (browser build). Combo slug: " + slug + ". Words: " + words.join(", ") + ".\n\n" +
      "## Purpose\n\nThe Combo Librarian answers what any word combo means, finds related combos and live sites, and explains the combo's place in the deterministic ordering.\n\n" +
      "## Capabilities\n\n- Define each word of a combo from the Signature Dictionary: authored definitions as written, template-filled definitions labelled as such, pending headwords labelled pending, non-headwords labelled not-a-Dictionary-headword. Never invent a definition.\n- Give the combo's Signature reading, labelled as a Signature reading, never as established fact.\n- Report the combo's deterministic rank when it is defined, or explain honestly why it is not defined.\n- Find related combos from the demand lists that share a word, and route to their stable combos/<slug>/ URLs.\n- Route to related live sites: the Dictionary A-Z pages, the words database, and the Combo Router.\n\n" +
      "## Boundaries\n\n- Never generate content for a refused combo (defeat-military-system, pathogen, toxin, explosive, ballistics, gene-drive content). Refuse with the recorded reason.\n- No brand names, logos, trademarks, product names or copyrighted images. Nothing scraped or copied from any real website.\n- Speculative material is labelled design-study or entertainment, never fact.\n\n" +
      "## Grounding for this combo\n\n" + o.defs.map(function (d) { return "- " + d.word + ": " + (d.definitions.length ? d.definitions.join(" ") + " (" + d.status + ")" : d.status); }).join("\n") + "\n";
  }

  function builderSpec(o) {
    var words = o.words, slug = o.slug, title = o.title, demo = o.demo;
    return "# Combo Builder — AI spec for the combo \"" + title + "\"\n\n" +
      "Generator: " + GEN_VERSION + " / " + BUILD_DATE + " (browser build). Combo slug: " + slug + ". Words: " + words.join(", ") + ".\n\n" +
      "## Purpose\n\nThe Combo Builder generates a combo's full page, spec and demo from the template in REVIEW §3.4, deterministically: the same combo in always produces byte-identical output.\n\n" +
      "## Template (10 sections)\n\n1. What the combo means. 2. Math proof (deterministic rank + space sizes). 3. Science proof (Dictionary linguistics only; speculative material labelled design-study). 4. Relevant data (Dictionary links, related live sites). 5. Spec (words, order, length class, demand source, generator version, verification stamp). 6. Working demo that genuinely executes. 7. Two AIs, downloadable with specs. 8. Use. 9. Sources. 10. Accessible zero-script version.\n\n" +
      "## Demo for this combo\n\nDemo kind: " + demo.kind + ". " + demo.note + "\n\n" +
      "## Rules\n\n- Deterministic output; the slug is the identity; never duplicate a combo.\n- Boundary refusal with a recorded reason; never generate around a refusal.\n- Tool-like combos get a small working tool built only from held data; otherwise the combo explorer, with an honest statement that no genuine tool could be built from held data. Never a fake tool.\n- Definitions: authored as written, template-filled labelled, pending labelled pending, non-headwords labelled, never faked.\n";
  }

  /* --- path parsing -------------------------------------------------------- */
  /* "/jah-databases/combos/ai-meme-generator/" ->
   *   { slug: "ai-meme-generator", accessible: false, isCombo: true }
   * Anything not under /combos/<something>/ -> { isCombo: false }. */
  function parseComboPath(pathname) {
    var m = pathname.match(/\/combos\/([^\/]+)\/?$/);
    if (m) return { isCombo: true, slug: m[1], accessible: false };
    var a = pathname.match(/\/combos\/([^\/]+)\/accessible\.html$/);
    if (a) return { isCombo: true, slug: a[1], accessible: true };
    return { isCombo: false, slug: null, accessible: false };
  }

  function escJs(s) {
    var d = null;
    try { d = document.createElement("div"); } catch (e) { d = null; }
    if (d) { d.textContent = s; return d.innerHTML; }
    return escapeHtml(s);
  }

  /* --- main render --------------------------------------------------------- */
  /* env: { document, fetch, location, URL?, Blob?, setTimeout? }.
   * In a browser pass the real globals; the harness passes stubs.
   * container: element (or id) to render into. Returns a Promise that
   * resolves to { slug, words, demoKind, refused, accessible, rank }. */
  function renderCombo(env, container, pathname, opts) {
    opts = opts || {};
    var doc = env.document;
    var rootEl = typeof container === "string" ? doc.getElementById(container) : container;
    var parsed = parseComboPath(pathname);
    if (!parsed.isCombo) {
      rootEl.innerHTML = "<h1>Page not found</h1><p>There is no page at this address. "
        + "For word combos, start at the <a href=\"combos/index.html\">Combo Router</a>, "
        + "or go to <a href=\"index.html\">The 'Merica-L Boundless Ecosystem OS</a>.</p>";
      return Promise.resolve({ isCombo: false });
    }
    var slug = parsed.slug;
    var root = siteRootFromPath(pathname);
    return loadData(env, root).then(function (data) {
      var found = wordsForSlug(slug, data);
      var words = found.words;
      var title = words.join(" ");
      var boundary = checkBoundary(words);
      if (boundary.refused) {
        rootEl.innerHTML = "<h1>" + escapeHtml(title) + "</h1>"
          + "<p><i>A Signature word-combo page. Stable URL: combos/" + slug + "/</i></p>"
          + "<h2>Not built</h2><p>This combo is <b>not built</b>: " + escapeHtml(boundary.reason)
          + ". The refusal is recorded; the generator never generates around a refusal. "
          + "Try the <a href=\"../index.html\">Combo Router</a> for a different combo.</p>";
        return { slug: slug, words: words, refused: true, reason: boundary.reason };
      }
      if (words.length < 2 || words.length > 7) {
        rootEl.innerHTML = "<h1>Not a combo</h1><p>\"" + escapeHtml(slug) + "\" reads as "
          + words.length + " word(s). A word combo has 2 to 7 words. "
          + "Try the <a href=\"../index.html\">Combo Router</a>.</p>";
        return { slug: slug, words: words, refused: false, invalid: true };
      }
      var defs = resolveDefinitions(words, data);
      var rankInfo;
      if (data.vocabLoaded) {
        rankInfo = computeRank(words, data.vocabIndex);
      } else {
        rankInfo = { rank: null, reason: null, notComputed: true };
      }
      var demoChoice = chooseDemo(words, slug);
      var demo = demoFor(demoChoice.kind, data, words) || { html: "", script: "" };
      demo.kind = demoChoice.kind; demo.note = demoChoice.note;
      var related = relatedCombos(words, data, slug);
      var totalPerms = factorial(words.length);
      var perms = permutations(words, 24);
      var stored = data.index[slug] || null;
      var o = { words: words, slug: slug, title: title, defs: defs, rankInfo: rankInfo,
                demo: demo, related: related, perms: perms, totalPerms: totalPerms,
                storedId: stored ? stored.id : null, listItem: stored ? stored.list03_item : null,
                data: data, wordsExact: found.exact };
      var html = parsed.accessible ? buildAccessibleHtml(o) : buildPageHtml(o);
      /* The 404 document's own <head> stays; render the page body markup
       * into the container. Strip the generated doctype/head/body wrapper. */
      var bodyHtml = html.replace(/^[\s\S]*<body>\n?/, "").replace(/\n<\/body>\n<\/html>\n?$/, "");
      rootEl.innerHTML = bodyHtml;
      doc.title = title + " — Signature Word Combo";
      if (!parsed.accessible) {
        /* Wire the spec-download buttons. */
        var specBtns = rootEl.querySelectorAll ? rootEl.querySelectorAll("[data-spec]") : [];
        var specs = { librarian: librarianSpec(o), builder: builderSpec(o) };
        Array.prototype.forEach.call(specBtns, function (btn) {
          btn.addEventListener("click", function () {
            var kind = btn.getAttribute("data-spec");
            var text = specs[kind];
            var filename = kind === "librarian" ? "combo-librarian.spec.md" : "combo-builder.spec.md";
            try {
              var blob = new env.Blob([text], { type: "text/markdown" });
              var a = doc.createElement("a");
              a.href = env.URL.createObjectURL(blob);
              a.download = filename;
              a.click();
            } catch (e) { /* download unavailable in this environment; specs are in the page text */ }
          });
        });
        /* Run the demo script (same code the generator emits), then the
         * explorer wiring when the demo is the explorer. */
        var demoScript = (demo.kind !== "explorer" ? demo.script : "") + explorerScript();
        if (demoScript) {
          try {
            var fn = new Function("esc", "document", "window", "setTimeout", "URL", "Blob", "Intl", demoScript);
            fn(escJs, doc, env.window || global, env.setTimeout || setTimeout, env.URL, env.Blob, Intl);
          } catch (e) {
            var err = doc.createElement("p");
            err.textContent = "The demo on this page could not start in this browser (" + e.message + "). The rest of the page is unaffected.";
            rootEl.appendChild(err);
          }
        }
      }
      return { slug: slug, words: words, demoKind: demo.kind, refused: false,
               accessible: parsed.accessible, rank: rankInfo.rank !== null ? rankInfo.rank.toString() : null,
               storedId: o.storedId, html: html };
    }).catch(function (e) {
      rootEl.innerHTML = "<h1>Combo Router</h1><p>This combo page could not be built in this browser: "
        + escapeHtml(e && e.message ? e.message : String(e))
        + ". Try the <a href=\"../index.html\">Combo Router</a>.</p>";
      return { slug: slug, error: e && e.message ? e.message : String(e) };
    });
  }

  function renderFromLocation(doc) {
    var env = {
      document: doc,
      fetch: global.fetch.bind(global),
      location: global.location,
      window: global,
      URL: global.URL,
      Blob: global.Blob,
      setTimeout: global.setTimeout.bind(global)
    };
    var rootEl = doc.getElementById("combo-root");
    return renderCombo(env, rootEl, global.location.pathname, {});
  }

  var api = {
    GEN_VERSION: GEN_VERSION, BUILD_DATE: BUILD_DATE, VOCAB_N: VOCAB_N,
    SPACE: SPACE, SPACE_TOTAL_2_TO_7: SPACE_TOTAL_2_TO_7,
    slugify: slugify, comboSlug: comboSlug, escapeHtml: escapeHtml,
    computeRank: computeRank, permutations: permutations, factorial: factorial,
    checkBoundary: checkBoundary, chooseDemo: chooseDemo, demoFor: demoFor,
    explorerHtml: explorerHtml, explorerScript: explorerScript,
    buildPageHtml: buildPageHtml, buildAccessibleHtml: buildAccessibleHtml,
    librarianSpec: librarianSpec, builderSpec: builderSpec,
    parseComboPath: parseComboPath, siteRootFromPath: siteRootFromPath,
    wordsForSlug: wordsForSlug, resolveDefinitions: resolveDefinitions,
    relatedCombos: relatedCombos, loadData: loadData, renderCombo: renderCombo,
    renderFromLocation: renderFromLocation
  };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  global.ComboPage = api;
})(typeof window !== "undefined" ? window : globalThis);
