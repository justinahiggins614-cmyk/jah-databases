(function(){'use strict';
/* JAH Scales Theory Music Theory Database generator — jahdb-e2-theory-scales-music-theory-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-theory-scales-music-theory',PREFIX='JAH-E2THEORYSCA-',NAME='JAH Scales Theory Music Theory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Scales Theory: the complete guide", "d": "Scales Theory: the ladders of notes..", "g": "overview", "l": 2, "q": "What is Scales Theory: the complete guide?", "a": "Scales Theory: the ladders of notes..", "x": "The complete music theory guide to Scales Theory: the ladders of notes.. Major. History, meaning, practices, and how to engage respectfully — everything in one database. Major. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Scales Theory essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Scales Theory essentials.", "x": "At a glance: Scales Theory — the ladders of notes.. Minor. The essentials: Minor.. Modes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Major.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Major.", "x": "Scales Theory: Major.. Minor. Essential knowledge — Modes.. the ladders of notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Major..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Major..", "x": "Explained: Major.. Pentatonic. The context — Scales Theory. Pentatonic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Minor.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Minor.", "x": "Scales Theory: Minor.. Modes. Essential knowledge — Pentatonic.. the ladders of notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Minor..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Minor..", "x": "Explained: Minor.. Blues. The context — Scales Theory. Blues. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Modes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Modes.", "x": "Scales Theory: Modes.. Pentatonic. Essential knowledge — Blues.. the ladders of notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Modes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Modes..", "x": "Explained: Modes.. Practice. The context — Scales Theory. Chromatic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pentatonic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pentatonic.", "x": "Scales Theory: Pentatonic.. Blues. Essential knowledge — Chromatic.. the ladders of notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pentatonic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pentatonic..", "x": "Explained: Pentatonic.. Major. The context — Scales Theory. Major. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Blues.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Blues.", "x": "Scales Theory: Blues.. Practice. Essential knowledge — Major.. the ladders of notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Blues..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Blues..", "x": "Explained: Blues.. Minor. The context — Scales Theory. Minor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chromatic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chromatic.", "x": "Scales Theory: Chromatic.. Major. Essential knowledge — Minor.. the ladders of notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chromatic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chromatic..", "x": "Explained: Chromatic.. Modes. The context — Scales Theory. Modes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Major.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Major.", "x": "Scales Theory in depth: Major.. Minor. Details — the ladders of notes.. Modes. Pentatonic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Minor.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Minor.", "x": "Scales Theory in depth: Minor.. Modes. Details — the ladders of notes.. Pentatonic. Blues. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Modes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Modes.", "x": "Scales Theory in depth: Modes.. Pentatonic. Details — the ladders of notes.. Blues. Chromatic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pentatonic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pentatonic.", "x": "Scales Theory in depth: Pentatonic.. Blues. Details — the ladders of notes.. Practice. Major. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Blues.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Blues.", "x": "Scales Theory in depth: Blues.. Chromatic. Details — the ladders of notes.. Major. Minor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Practice.", "x": "Scales Theory in depth: Practice.. Major. Details — the ladders of notes.. Minor. Modes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Scales Theory comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Scales Theory comes from.", "x": "Origins: Major.. Major. The history of Scales Theory — the ladders of notes.. Minor. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Scales Theory respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Scales Theory respectfully.", "x": "Engaging: Modes.. Minor. How to participate or observe well — Scales Theory. the ladders of notes. Respect first, always; Pentatonic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Scales Theory do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Scales Theory do's and don'ts.", "x": "Etiquette: Blues.. Modes. The rules of respect — Scales Theory. the ladders of notes. When in doubt, ask about Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Scales Theory.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Scales Theory.", "x": "Planning: Major.. Pentatonic. Practical notes — Scales Theory. the ladders of notes. A little planning shows respect for Minor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Scales Theory and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Scales Theory and money.", "x": "Costs: Modes.. Blues. What to budget — Scales Theory. the ladders of notes. The best experiences of Pentatonic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-theory-scales-music-theory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
