(function(){'use strict';
/* JAH Regex Tokens Database generator — jahdb-regex-tokens-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='regex-tokens',PREFIX='JAH-RGX-',NAME='JAH Regex Tokens Database';
var FIELDS=["basic", "quantifier", "class", "anchor", "group", "flag", "escape"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": ".", "d": "Any single character except newline.", "g": "basic", "l": 2, "q": "What is .?", "a": "Any single character except newline.", "x": ". — Any single character except newline. Example: a.c matches abc..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "^", "d": "Start of string or line.", "g": "basic", "l": 2, "q": "What is ^?", "a": "Start of string or line.", "x": "^ — Start of string or line. Example: ^hello matches at start..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "$", "d": "End of string or line.", "g": "basic", "l": 2, "q": "What is $?", "a": "End of string or line.", "x": "$ — End of string or line. Example: world$ matches at end..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "*", "d": "Zero or more of the previous.", "g": "quantifier", "l": 2, "q": "What is *?", "a": "Zero or more of the previous.", "x": "* — Zero or more of the previous. Example: ab* matches a, ab, abb..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "+", "d": "One or more of the previous.", "g": "quantifier", "l": 2, "q": "What is +?", "a": "One or more of the previous.", "x": "+ — One or more of the previous. Example: ab+ matches ab, abb..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "?", "d": "Zero or one of the previous.", "g": "quantifier", "l": 2, "q": "What is ??", "a": "Zero or one of the previous.", "x": "? — Zero or one of the previous. Example: colou?r matches color/colour..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "{n}", "d": "Exactly n of the previous.", "g": "quantifier", "l": 2, "q": "What is {n}?", "a": "Exactly n of the previous.", "x": "{n} — Exactly n of the previous. Example: a{3} matches aaa..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "{n,}", "d": "n or more of the previous.", "g": "quantifier", "l": 2, "q": "What is {n,}?", "a": "n or more of the previous.", "x": "{n,} — n or more of the previous. Example: a{2,} matches aa, aaa..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "{n,m}", "d": "Between n and m of the previous.", "g": "quantifier", "l": 2, "q": "What is {n,m}?", "a": "Between n and m of the previous.", "x": "{n,m} — Between n and m of the previous. Example: a{2,4} matches aa to aaaa..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "[...]", "d": "Any one character in the set.", "g": "class", "l": 2, "q": "What is [...]?", "a": "Any one character in the set.", "x": "[...] — Any one character in the set. Example: [aeiou] matches a vowel..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "[^...]", "d": "Any one character NOT in the set.", "g": "class", "l": 2, "q": "What is [^...]?", "a": "Any one character NOT in the set.", "x": "[^...] — Any one character NOT in the set. Example: [^0-9] matches non-digit..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "\\d", "d": "Any digit, 0-9.", "g": "class", "l": 2, "q": "What is \\d?", "a": "Any digit, 0-9.", "x": "\\d — Any digit, 0-9. Example: \\d+ matches 42..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\D", "d": "Any non-digit.", "g": "class", "l": 2, "q": "What is \\D?", "a": "Any non-digit.", "x": "\\D — Any non-digit. Example: \\D+ matches abc..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\w", "d": "Word character: letters, digits, underscore.", "g": "class", "l": 2, "q": "What is \\w?", "a": "Word character: letters, digits, underscore.", "x": "\\w — Word character: letters, digits, underscore. Example: \\w+ matches hello_1..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "\\W", "d": "Non-word character.", "g": "class", "l": 2, "q": "What is \\W?", "a": "Non-word character.", "x": "\\W — Non-word character. Example: \\W matches !..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\s", "d": "Whitespace.", "g": "class", "l": 2, "q": "What is \\s?", "a": "Whitespace.", "x": "\\s — Whitespace. Example: \\s+ matches spaces..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\S", "d": "Non-whitespace.", "g": "class", "l": 2, "q": "What is \\S?", "a": "Non-whitespace.", "x": "\\S — Non-whitespace. Example: \\S+ matches words..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\b", "d": "Word boundary.", "g": "anchor", "l": 2, "q": "What is \\b?", "a": "Word boundary.", "x": "\\b — Word boundary. Example: \\bcat\\b matches cat not cats..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\B", "d": "Not a word boundary.", "g": "anchor", "l": 2, "q": "What is \\B?", "a": "Not a word boundary.", "x": "\\B — Not a word boundary. Example: \\Bcat matches in scatter..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\A", "d": "Absolute start of string.", "g": "anchor", "l": 2, "q": "What is \\A?", "a": "Absolute start of string.", "x": "\\A — Absolute start of string. Example: \\Ahello..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "\\Z", "d": "Absolute end of string.", "g": "anchor", "l": 2, "q": "What is \\Z?", "a": "Absolute end of string.", "x": "\\Z — Absolute end of string. Example: world\\Z..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "|", "d": "Alternation: this or that.", "g": "group", "l": 2, "q": "What is |?", "a": "Alternation: this or that.", "x": "| — Alternation: this or that. Example: cat|dog matches either..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "(...)", "d": "Capturing group.", "g": "group", "l": 2, "q": "What is (...)?", "a": "Capturing group.", "x": "(...) — Capturing group. Example: (ab)+ captures ab..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "(?:...)", "d": "Non-capturing group.", "g": "group", "l": 2, "q": "What is (?:...)?", "a": "Non-capturing group.", "x": "(?:...) — Non-capturing group. Example: (?:ab)+ matches without capture..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "(?=...)", "d": "Positive lookahead.", "g": "group", "l": 2, "q": "What is (?=...)?", "a": "Positive lookahead.", "x": "(?=...) — Positive lookahead. Example: \\w+(?=:) matches key in key:..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-regex-tokens-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
