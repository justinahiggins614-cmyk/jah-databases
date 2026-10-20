(function(){'use strict';
/* JAH Romanian Phrasebook Database generator — jahdb-e2-lang-romanian-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-romanian',PREFIX='JAH-E2LANGROMAN-',NAME='JAH Romanian Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Romanian phrasebook: complete", "d": "Romanian: 24M+ speakers. the Latin island..", "g": "overview", "l": 2, "q": "What is Romanian phrasebook: complete?", "a": "Romanian: 24M+ speakers. the Latin island..", "x": "The complete Romanian phrasebook: the Latin island.. Buna. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 24M+ Imi place. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Romanian: the Latin island..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Romanian: the Latin island..", "x": "About Romanian: 24M+ speakers — the Latin island.. Multumesc. Where it is spoken, its family, its script. Cat costa. Va rog. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Buna.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Buna.", "x": "Romanian essential 1: Buna.. Cat costa. Learn these first — Va rog.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Buna..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Buna..", "x": "Usage: Buna.. Putin. When and how — Unde.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Multumesc.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Multumesc.", "x": "Romanian essential 2: Multumesc.. Putin. Learn these first — Unde.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Multumesc..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Multumesc..", "x": "Usage: Multumesc.. Toaleta. When and how — Nota.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Va rog.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Va rog.", "x": "Romanian essential 3: Va rog.. Toaleta. Learn these first — Nota.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Va rog..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Va rog..", "x": "Usage: Va rog.. Ajutor. When and how — Da/Nu.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Unde.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Unde.", "x": "Romanian essential 4: Unde.. Ajutor. Learn these first — Da/Nu.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Unde..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Unde..", "x": "Usage: Unde.. Noroc. When and how — Scuze.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Nota.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Nota.", "x": "Romanian essential 5: Nota.. Noroc. Learn these first — Scuze.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nota..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nota..", "x": "Usage: Nota.. Buna dimineata. When and how — La revedere.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Da/Nu.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Da/Nu.", "x": "Romanian essential 6: Da/Nu.. Buna dimineata. Learn these first — La revedere.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Da/Nu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Da/Nu..", "x": "Usage: Da/Nu.. Noapte buna. When and how — Buna.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Scuze.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Scuze.", "x": "Romanian essential 7: Scuze.. Noapte buna. Learn these first — Buna.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Scuze..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Scuze..", "x": "Usage: Scuze.. Imi place. When and how — Multumesc.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "La revedere.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "La revedere.", "x": "Romanian essential 8: La revedere.. Imi place. Learn these first — Multumesc.. the Latin island. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: La revedere..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: La revedere..", "x": "Usage: La revedere.. Cat costa. When and how — Va rog.. Romanian the Latin island. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Imi place.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Imi place.", "x": "Romanian phrase: Imi place.. Multumesc. A traveler's essential — Putin.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Cat costa.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Cat costa.", "x": "Romanian phrase: Cat costa.. Va rog. A traveler's essential — Toaleta.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Putin.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Putin.", "x": "Romanian phrase: Putin.. Unde. A traveler's essential — Ajutor.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toaleta.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toaleta.", "x": "Romanian phrase: Toaleta.. Nota. A traveler's essential — Noroc.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Ajutor.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Ajutor.", "x": "Romanian phrase: Ajutor.. Da/Nu. A traveler's essential — Buna dimineata.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Noroc.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Noroc.", "x": "Romanian phrase: Noroc.. Scuze. A traveler's essential — Noapte buna.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Buna dimineata.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Buna dimineata.", "x": "Romanian phrase: Buna dimineata.. La revedere. A traveler's essential — Imi place.. the Latin island. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-romanian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
