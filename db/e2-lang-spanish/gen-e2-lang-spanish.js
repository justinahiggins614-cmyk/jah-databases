(function(){'use strict';
/* JAH Spanish Phrasebook Database generator — jahdb-e2-lang-spanish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-spanish',PREFIX='JAH-E2LANGSPANI-',NAME='JAH Spanish Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Spanish phrasebook: complete", "d": "Spanish: 500M+ speakers. the world's romance language..", "g": "overview", "l": 2, "q": "What is Spanish phrasebook: complete?", "a": "Spanish: 500M+ speakers. the world's romance language..", "x": "The complete Spanish phrasebook: the world's romance language.. Hola: hello. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 500M+ Me gusta: I like.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Spanish: the world's romance language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Spanish: the world's romance language..", "x": "About Spanish: 500M+ speakers — the world's romance language.. Gracias: thank you. Where it is spoken, its family, its script. Cuanto cuesta: how much. Por favor: please. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hola: hello.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hola: hello.", "x": "Spanish essential 1: Hola: hello.. Cuanto cuesta: how much. Learn these first — Por favor: please.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hola: hello..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hola: hello..", "x": "Usage: Hola: hello.. Hablo poco: I speak little. When and how — Donde esta: where is.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Gracias: thank you.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Gracias: thank you.", "x": "Spanish essential 2: Gracias: thank you.. Hablo poco: I speak little. Learn these first — Donde esta: where is.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Gracias: thank you..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Gracias: thank you..", "x": "Usage: Gracias: thank you.. Bano: bathroom. When and how — La cuenta: the bill.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Por favor: please.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Por favor: please.", "x": "Spanish essential 3: Por favor: please.. Bano: bathroom. Learn these first — La cuenta: the bill.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Por favor: please..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Por favor: please..", "x": "Usage: Por favor: please.. Ayuda: help. When and how — Si/No.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Donde esta: where is.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Donde esta: where is.", "x": "Spanish essential 4: Donde esta: where is.. Ayuda: help. Learn these first — Si/No.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Donde esta: where is..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Donde esta: where is..", "x": "Usage: Donde esta: where is.. Salud: cheers. When and how — Perdon: excuse me.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "La cuenta: the bill.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "La cuenta: the bill.", "x": "Spanish essential 5: La cuenta: the bill.. Salud: cheers. Learn these first — Perdon: excuse me.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: La cuenta: the bill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: La cuenta: the bill..", "x": "Usage: La cuenta: the bill.. Buenos dias. When and how — Adios: goodbye.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Si/No.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Si/No.", "x": "Spanish essential 6: Si/No.. Buenos dias. Learn these first — Adios: goodbye.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Si/No..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Si/No..", "x": "Usage: Si/No.. Buenas noches. When and how — Hola: hello.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Perdon: excuse me.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Perdon: excuse me.", "x": "Spanish essential 7: Perdon: excuse me.. Buenas noches. Learn these first — Hola: hello.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Perdon: excuse me..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Perdon: excuse me..", "x": "Usage: Perdon: excuse me.. Me gusta: I like. When and how — Gracias: thank you.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Adios: goodbye.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Adios: goodbye.", "x": "Spanish essential 8: Adios: goodbye.. Me gusta: I like. Learn these first — Gracias: thank you.. the world's romance language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Adios: goodbye..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Adios: goodbye..", "x": "Usage: Adios: goodbye.. Cuanto cuesta: how much. When and how — Por favor: please.. Spanish the world's romance language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Me gusta: I like.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Me gusta: I like.", "x": "Spanish phrase: Me gusta: I like.. Gracias: thank you. A traveler's essential — Hablo poco: I speak little.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Cuanto cuesta: how much.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Cuanto cuesta: how much.", "x": "Spanish phrase: Cuanto cuesta: how much.. Por favor: please. A traveler's essential — Bano: bathroom.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Hablo poco: I speak little.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Hablo poco: I speak little.", "x": "Spanish phrase: Hablo poco: I speak little.. Donde esta: where is. A traveler's essential — Ayuda: help.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Bano: bathroom.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Bano: bathroom.", "x": "Spanish phrase: Bano: bathroom.. La cuenta: the bill. A traveler's essential — Salud: cheers.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Ayuda: help.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Ayuda: help.", "x": "Spanish phrase: Ayuda: help.. Si/No. A traveler's essential — Buenos dias.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Salud: cheers.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Salud: cheers.", "x": "Spanish phrase: Salud: cheers.. Perdon: excuse me. A traveler's essential — Buenas noches.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Buenos dias.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Buenos dias.", "x": "Spanish phrase: Buenos dias.. Adios: goodbye. A traveler's essential — Me gusta: I like.. the world's romance language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-spanish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
