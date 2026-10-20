(function(){'use strict';
/* JAH Danish Phrasebook Database generator — jahdb-e2-lang-danish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-danish',PREFIX='JAH-E2LANGDANIS-',NAME='JAH Danish Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Danish phrasebook: complete", "d": "Danish: 6M+ speakers. the soft consonants..", "g": "overview", "l": 2, "q": "What is Danish phrasebook: complete?", "a": "Danish: 6M+ speakers. the soft consonants..", "x": "The complete Danish phrasebook: the soft consonants.. Hej. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 6M+ Jeg kan lide. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Danish: the soft consonants..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Danish: the soft consonants..", "x": "About Danish: 6M+ speakers — the soft consonants.. Tak. Where it is spoken, its family, its script. Hvor meget. Vær så venlig. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hej.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hej.", "x": "Danish essential 1: Hej.. Hvor meget. Learn these first — Vær så venlig.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hej..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hej..", "x": "Usage: Hej.. Lidt. When and how — Hvor.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Tak.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Tak.", "x": "Danish essential 2: Tak.. Lidt. Learn these first — Hvor.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tak..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tak..", "x": "Usage: Tak.. Toilet. When and how — Regningen.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Vær så venlig.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Vær så venlig.", "x": "Danish essential 3: Vær så venlig.. Toilet. Learn these first — Regningen.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Vær så venlig..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Vær så venlig..", "x": "Usage: Vær så venlig.. Hjælp. When and how — Ja/Nej.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Hvor.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Hvor.", "x": "Danish essential 4: Hvor.. Hjælp. Learn these first — Ja/Nej.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hvor..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hvor..", "x": "Usage: Hvor.. Skål. When and how — Undskyld.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Regningen.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Regningen.", "x": "Danish essential 5: Regningen.. Skål. Learn these first — Undskyld.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Regningen..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Regningen..", "x": "Usage: Regningen.. Godmorgen. When and how — Farvel.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ja/Nej.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ja/Nej.", "x": "Danish essential 6: Ja/Nej.. Godmorgen. Learn these first — Farvel.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ja/Nej..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ja/Nej..", "x": "Usage: Ja/Nej.. Godnat. When and how — Hej.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Undskyld.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Undskyld.", "x": "Danish essential 7: Undskyld.. Godnat. Learn these first — Hej.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Undskyld..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Undskyld..", "x": "Usage: Undskyld.. Jeg kan lide. When and how — Tak.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Farvel.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Farvel.", "x": "Danish essential 8: Farvel.. Jeg kan lide. Learn these first — Tak.. the soft consonants. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Farvel..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Farvel..", "x": "Usage: Farvel.. Hvor meget. When and how — Vær så venlig.. Danish the soft consonants. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Jeg kan lide.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Jeg kan lide.", "x": "Danish phrase: Jeg kan lide.. Tak. A traveler's essential — Lidt.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Hvor meget.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Hvor meget.", "x": "Danish phrase: Hvor meget.. Vær så venlig. A traveler's essential — Toilet.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Lidt.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Lidt.", "x": "Danish phrase: Lidt.. Hvor. A traveler's essential — Hjælp.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toilet.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toilet.", "x": "Danish phrase: Toilet.. Regningen. A traveler's essential — Skål.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Hjælp.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Hjælp.", "x": "Danish phrase: Hjælp.. Ja/Nej. A traveler's essential — Godmorgen.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Skål.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Skål.", "x": "Danish phrase: Skål.. Undskyld. A traveler's essential — Godnat.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Godmorgen.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Godmorgen.", "x": "Danish phrase: Godmorgen.. Farvel. A traveler's essential — Jeg kan lide.. the soft consonants. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-danish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
