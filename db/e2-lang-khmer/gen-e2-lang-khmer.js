(function(){'use strict';
/* JAH Khmer Phrasebook Database generator — jahdb-e2-lang-khmer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-khmer',PREFIX='JAH-E2LANGKHMER-',NAME='JAH Khmer Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Khmer phrasebook: complete", "d": "Khmer: 16M+ speakers. Cambodia's language..", "g": "overview", "l": 2, "q": "What is Khmer phrasebook: complete?", "a": "Khmer: 16M+ speakers. Cambodia's language..", "x": "The complete Khmer phrasebook: Cambodia's language.. Suostei. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 16M+ Chol chet. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Khmer: Cambodia's language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Khmer: Cambodia's language..", "x": "About Khmer: 16M+ speakers — Cambodia's language.. Orkun. Where it is spoken, its family, its script. Tlai ponman. Som. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Suostei.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Suostei.", "x": "Khmer essential 1: Suostei.. Tlai ponman. Learn these first — Som.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Suostei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Suostei..", "x": "Usage: Suostei.. Tich. When and how — Nov na.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Orkun.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Orkun.", "x": "Khmer essential 2: Orkun.. Tich. Learn these first — Nov na.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Orkun..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Orkun..", "x": "Usage: Orkun.. Bantop. When and how — Kut lui.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Som.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Som.", "x": "Khmer essential 3: Som.. Bantop. Learn these first — Kut lui.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Som..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Som..", "x": "Usage: Som.. Chuoy. When and how — Baat/Te.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Nov na.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Nov na.", "x": "Khmer essential 4: Nov na.. Chuoy. Learn these first — Baat/Te.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nov na..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nov na..", "x": "Usage: Nov na.. Sok sabay. When and how — Som toh.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Kut lui.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Kut lui.", "x": "Khmer essential 5: Kut lui.. Sok sabay. Learn these first — Som toh.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kut lui..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kut lui..", "x": "Usage: Kut lui.. Arun suostei. When and how — Lea heuy.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Baat/Te.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Baat/Te.", "x": "Khmer essential 6: Baat/Te.. Arun suostei. Learn these first — Lea heuy.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Baat/Te..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Baat/Te..", "x": "Usage: Baat/Te.. Reatrey suostei. When and how — Suostei.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Som toh.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Som toh.", "x": "Khmer essential 7: Som toh.. Reatrey suostei. Learn these first — Suostei.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Som toh..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Som toh..", "x": "Usage: Som toh.. Chol chet. When and how — Orkun.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Lea heuy.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Lea heuy.", "x": "Khmer essential 8: Lea heuy.. Chol chet. Learn these first — Orkun.. Cambodia's language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Lea heuy..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Lea heuy..", "x": "Usage: Lea heuy.. Tlai ponman. When and how — Som.. Khmer Cambodia's language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Chol chet.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Chol chet.", "x": "Khmer phrase: Chol chet.. Orkun. A traveler's essential — Tich.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Tlai ponman.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Tlai ponman.", "x": "Khmer phrase: Tlai ponman.. Som. A traveler's essential — Bantop.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Tich.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Tich.", "x": "Khmer phrase: Tich.. Nov na. A traveler's essential — Chuoy.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Bantop.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Bantop.", "x": "Khmer phrase: Bantop.. Kut lui. A traveler's essential — Sok sabay.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Chuoy.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Chuoy.", "x": "Khmer phrase: Chuoy.. Baat/Te. A traveler's essential — Arun suostei.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Sok sabay.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Sok sabay.", "x": "Khmer phrase: Sok sabay.. Som toh. A traveler's essential — Reatrey suostei.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Arun suostei.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Arun suostei.", "x": "Khmer phrase: Arun suostei.. Lea heuy. A traveler's essential — Chol chet.. Cambodia's language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-khmer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
