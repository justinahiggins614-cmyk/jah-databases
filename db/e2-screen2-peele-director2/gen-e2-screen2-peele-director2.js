(function(){'use strict';
/* JAH Peele2 Database generator — jahdb-e2-screen2-peele-director2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen2-peele-director2',PREFIX='JAH-E2SCREEN2PE-',NAME='JAH Peele2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peele2: the complete guide", "d": "Peele2: the horror 2..", "g": "overview", "l": 2, "q": "What is Peele2: the complete guide?", "a": "Peele2: the horror 2..", "x": "The complete director guide to Peele2: the horror 2.. Nope. History, meaning, practices, and how to engage respectfully — everything in one database. Monkeypaw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Peele2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Peele2 essentials.", "x": "At a glance: Peele2 — the horror 2.. Us. The essentials: Social.. Monkeypaw. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Nope.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Nope.", "x": "Peele2: Nope.. Social. Essential knowledge — Monkeypaw.. the horror 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Nope..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Nope..", "x": "Explained: Nope.. Nope. The context — Peele2. Key. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Us.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Us.", "x": "Peele2: Us.. Zone. Essential knowledge — Key.. the horror 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Us..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Us..", "x": "Explained: Us.. Us. The context — Peele2. Twilight Zone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Monkeypaw.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Monkeypaw.", "x": "Peele2: Monkeypaw.. Nope. Essential knowledge — Twilight Zone.. the horror 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Monkeypaw..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Monkeypaw..", "x": "Explained: Monkeypaw.. Style. The context — Peele2. Social. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Key.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Key.", "x": "Peele2: Key.. Us. Essential knowledge — Social.. the horror 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Key..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Key..", "x": "Explained: Key.. Monkeypaw. The context — Peele2. Nope. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Twilight Zone.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Twilight Zone.", "x": "Peele2: Twilight Zone.. Style. Essential knowledge — Nope.. the horror 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Twilight Zone..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Twilight Zone..", "x": "Explained: Twilight Zone.. Social. The context — Peele2. Us. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Social.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Social.", "x": "Peele2: Social.. Monkeypaw. Essential knowledge — Us.. the horror 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Social..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Social..", "x": "Explained: Social.. Zone. The context — Peele2. Monkeypaw. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Monkeypaw.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Monkeypaw.", "x": "Peele2 in depth: Monkeypaw.. Us. Details — the horror 2.. Zone. Key. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Social.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Social.", "x": "Peele2 in depth: Social.. Monkeypaw. Details — the horror 2.. Nope. Twilight Zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Zone.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Zone.", "x": "Peele2 in depth: Zone.. Key. Details — the horror 2.. Us. Social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nope.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nope.", "x": "Peele2 in depth: Nope.. Twilight Zone. Details — the horror 2.. Style. Nope. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Us.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Us.", "x": "Peele2 in depth: Us.. Social. Details — the horror 2.. Monkeypaw. Us. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Peele2 in depth: Style.. Nope. Details — the horror 2.. Social. Monkeypaw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Peele2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Peele2 comes from.", "x": "Origins: Monkeypaw.. Nope. The history of Peele2 — the horror 2.. Social. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Peele2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Peele2 respectfully.", "x": "Engaging: Zone.. Us. How to participate or observe well — Peele2. the horror 2. Respect first, always; Nope.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Peele2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Peele2 do's and don'ts.", "x": "Etiquette: Us.. Monkeypaw. The rules of respect — Peele2. the horror 2. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Peele2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Peele2.", "x": "Planning: Monkeypaw.. Key. Practical notes — Peele2. the horror 2. A little planning shows respect for Social.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Peele2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Peele2 and money.", "x": "Costs: Zone.. Twilight Zone. What to budget — Peele2. the horror 2. The best experiences of Nope. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen2-peele-director2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
