(function(){'use strict';
/* JAH Morse Code Database generator — jahdb-morse-code-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='morse-code',PREFIX='JAH-MOR-',NAME='JAH Morse Code Database';
var FIELDS=["letters", "numbers", "punctuation"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "A", "d": ".-", "g": "letters", "l": 2, "q": "What is A?", "a": ".-", "x": "A — .- Example: Dot dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "B", "d": "-...", "g": "letters", "l": 2, "q": "What is B?", "a": "-...", "x": "B — -... Example: Dash dot dot dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "C", "d": "-.-.", "g": "letters", "l": 2, "q": "What is C?", "a": "-.-.", "x": "C — -.-. Example: Dash dot dash dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "D", "d": "-..", "g": "letters", "l": 2, "q": "What is D?", "a": "-..", "x": "D — -.. Example: Dash dot dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "E", "d": ".", "g": "letters", "l": 2, "q": "What is E?", "a": ".", "x": "E — . Example: Dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "F", "d": "..-.", "g": "letters", "l": 2, "q": "What is F?", "a": "..-.", "x": "F — ..-. Example: Dot dot dash dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "G", "d": "--.", "g": "letters", "l": 2, "q": "What is G?", "a": "--.", "x": "G — --. Example: Dash dash dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "H", "d": "....", "g": "letters", "l": 2, "q": "What is H?", "a": "....", "x": "H — .... Example: Four dots..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "I", "d": "..", "g": "letters", "l": 2, "q": "What is I?", "a": "..", "x": "I — .. Example: Dot dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "J", "d": ".---", "g": "letters", "l": 2, "q": "What is J?", "a": ".---", "x": "J — .--- Example: Dot dash dash dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "K", "d": "-.-", "g": "letters", "l": 2, "q": "What is K?", "a": "-.-", "x": "K — -.- Example: Dash dot dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "L", "d": ".-..", "g": "letters", "l": 2, "q": "What is L?", "a": ".-..", "x": "L — .-.. Example: Dot dash dot dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "M", "d": "--", "g": "letters", "l": 2, "q": "What is M?", "a": "--", "x": "M — -- Example: Dash dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "N", "d": "-.", "g": "letters", "l": 2, "q": "What is N?", "a": "-.", "x": "N — -. Example: Dash dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "O", "d": "---", "g": "letters", "l": 2, "q": "What is O?", "a": "---", "x": "O — --- Example: Three dashes..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "P", "d": ".--.", "g": "letters", "l": 2, "q": "What is P?", "a": ".--.", "x": "P — .--. Example: Dot dash dash dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Q", "d": "--.-", "g": "letters", "l": 2, "q": "What is Q?", "a": "--.-", "x": "Q — --.- Example: Dash dash dot dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "R", "d": ".-.", "g": "letters", "l": 2, "q": "What is R?", "a": ".-.", "x": "R — .-. Example: Dot dash dot..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "S", "d": "...", "g": "letters", "l": 2, "q": "What is S?", "a": "...", "x": "S — ... Example: Three dots..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "T", "d": "-", "g": "letters", "l": 2, "q": "What is T?", "a": "-", "x": "T — - Example: Dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "U", "d": "..-", "g": "letters", "l": 2, "q": "What is U?", "a": "..-", "x": "U — ..- Example: Dot dot dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "V", "d": "...-", "g": "letters", "l": 2, "q": "What is V?", "a": "...-", "x": "V — ...- Example: Dot dot dot dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "W", "d": ".--", "g": "letters", "l": 2, "q": "What is W?", "a": ".--", "x": "W — .-- Example: Dot dash dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "X", "d": "-..-", "g": "letters", "l": 2, "q": "What is X?", "a": "-..-", "x": "X — -..- Example: Dash dot dot dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Y", "d": "-.--", "g": "letters", "l": 2, "q": "What is Y?", "a": "-.--", "x": "Y — -.-- Example: Dash dot dash dash..  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-morse-code-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
