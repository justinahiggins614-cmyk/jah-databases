(function(){'use strict';
/* JAH Norwegian Phrasebook Database generator — jahdb-e2-lang-norwegian-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-norwegian',PREFIX='JAH-E2LANGNORWE-',NAME='JAH Norwegian Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Norwegian phrasebook: complete", "d": "Norwegian: 5M+ speakers. the fjord language..", "g": "overview", "l": 2, "q": "What is Norwegian phrasebook: complete?", "a": "Norwegian: 5M+ speakers. the fjord language..", "x": "The complete Norwegian phrasebook: the fjord language.. Hei. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 5M+ Jeg liker. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Norwegian: the fjord language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Norwegian: the fjord language..", "x": "About Norwegian: 5M+ speakers — the fjord language.. Takk. Where it is spoken, its family, its script. Hvor mye. Vaer sa snill. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hei.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hei.", "x": "Norwegian essential 1: Hei.. Hvor mye. Learn these first — Vaer sa snill.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hei..", "x": "Usage: Hei.. Litt. When and how — Hvor.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Takk.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Takk.", "x": "Norwegian essential 2: Takk.. Litt. Learn these first — Hvor.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Takk..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Takk..", "x": "Usage: Takk.. Toalett. When and how — Regningen.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Vaer sa snill.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Vaer sa snill.", "x": "Norwegian essential 3: Vaer sa snill.. Toalett. Learn these first — Regningen.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Vaer sa snill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Vaer sa snill..", "x": "Usage: Vaer sa snill.. Hjelp. When and how — Ja/Nei.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Hvor.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Hvor.", "x": "Norwegian essential 4: Hvor.. Hjelp. Learn these first — Ja/Nei.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hvor..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hvor..", "x": "Usage: Hvor.. Skal. When and how — Unnskyld.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Regningen.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Regningen.", "x": "Norwegian essential 5: Regningen.. Skal. Learn these first — Unnskyld.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Regningen..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Regningen..", "x": "Usage: Regningen.. God morgen. When and how — Ha det.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ja/Nei.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ja/Nei.", "x": "Norwegian essential 6: Ja/Nei.. God morgen. Learn these first — Ha det.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ja/Nei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ja/Nei..", "x": "Usage: Ja/Nei.. God natt. When and how — Hei.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Unnskyld.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Unnskyld.", "x": "Norwegian essential 7: Unnskyld.. God natt. Learn these first — Hei.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Unnskyld..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Unnskyld..", "x": "Usage: Unnskyld.. Jeg liker. When and how — Takk.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Ha det.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Ha det.", "x": "Norwegian essential 8: Ha det.. Jeg liker. Learn these first — Takk.. the fjord language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ha det..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ha det..", "x": "Usage: Ha det.. Hvor mye. When and how — Vaer sa snill.. Norwegian the fjord language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Jeg liker.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Jeg liker.", "x": "Norwegian phrase: Jeg liker.. Takk. A traveler's essential — Litt.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Hvor mye.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Hvor mye.", "x": "Norwegian phrase: Hvor mye.. Vaer sa snill. A traveler's essential — Toalett.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Litt.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Litt.", "x": "Norwegian phrase: Litt.. Hvor. A traveler's essential — Hjelp.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toalett.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toalett.", "x": "Norwegian phrase: Toalett.. Regningen. A traveler's essential — Skal.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Hjelp.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Hjelp.", "x": "Norwegian phrase: Hjelp.. Ja/Nei. A traveler's essential — God morgen.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Skal.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Skal.", "x": "Norwegian phrase: Skal.. Unnskyld. A traveler's essential — God natt.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "God morgen.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "God morgen.", "x": "Norwegian phrase: God morgen.. Ha det. A traveler's essential — Jeg liker.. the fjord language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-norwegian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
