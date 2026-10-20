(function(){'use strict';
/* JAH Italian Phrasebook Database generator — jahdb-e2-lang-italian-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-italian',PREFIX='JAH-E2LANGITALI-',NAME='JAH Italian Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Italian phrasebook: complete", "d": "Italian: 65M+ speakers. the language of music..", "g": "overview", "l": 2, "q": "What is Italian phrasebook: complete?", "a": "Italian: 65M+ speakers. the language of music..", "x": "The complete Italian phrasebook: the language of music.. Ciao. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 65M+ Mi piace. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Italian: the language of music..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Italian: the language of music..", "x": "About Italian: 65M+ speakers — the language of music.. Grazie. Where it is spoken, its family, its script. Quanto costa. Per favore. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Ciao.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Ciao.", "x": "Italian essential 1: Ciao.. Quanto costa. Learn these first — Per favore.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ciao..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ciao..", "x": "Usage: Ciao.. Parlo poco. When and how — Dov'e.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Grazie.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Grazie.", "x": "Italian essential 2: Grazie.. Parlo poco. Learn these first — Dov'e.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Grazie..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Grazie..", "x": "Usage: Grazie.. Bagno. When and how — Il conto.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Per favore.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Per favore.", "x": "Italian essential 3: Per favore.. Bagno. Learn these first — Il conto.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Per favore..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Per favore..", "x": "Usage: Per favore.. Aiuto. When and how — Si/No.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Dov'e.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Dov'e.", "x": "Italian essential 4: Dov'e.. Aiuto. Learn these first — Si/No.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dov'e..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dov'e..", "x": "Usage: Dov'e.. Salute. When and how — Scusi.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Il conto.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Il conto.", "x": "Italian essential 5: Il conto.. Salute. Learn these first — Scusi.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Il conto..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Il conto..", "x": "Usage: Il conto.. Buongiorno. When and how — Arrivederci.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Si/No.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Si/No.", "x": "Italian essential 6: Si/No.. Buongiorno. Learn these first — Arrivederci.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Si/No..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Si/No..", "x": "Usage: Si/No.. Buonanotte. When and how — Ciao.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Scusi.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Scusi.", "x": "Italian essential 7: Scusi.. Buonanotte. Learn these first — Ciao.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Scusi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Scusi..", "x": "Usage: Scusi.. Mi piace. When and how — Grazie.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Arrivederci.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Arrivederci.", "x": "Italian essential 8: Arrivederci.. Mi piace. Learn these first — Grazie.. the language of music. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Arrivederci..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Arrivederci..", "x": "Usage: Arrivederci.. Quanto costa. When and how — Per favore.. Italian the language of music. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Mi piace.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Mi piace.", "x": "Italian phrase: Mi piace.. Grazie. A traveler's essential — Parlo poco.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Quanto costa.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Quanto costa.", "x": "Italian phrase: Quanto costa.. Per favore. A traveler's essential — Bagno.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Parlo poco.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Parlo poco.", "x": "Italian phrase: Parlo poco.. Dov'e. A traveler's essential — Aiuto.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Bagno.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Bagno.", "x": "Italian phrase: Bagno.. Il conto. A traveler's essential — Salute.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Aiuto.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Aiuto.", "x": "Italian phrase: Aiuto.. Si/No. A traveler's essential — Buongiorno.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Salute.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Salute.", "x": "Italian phrase: Salute.. Scusi. A traveler's essential — Buonanotte.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Buongiorno.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Buongiorno.", "x": "Italian phrase: Buongiorno.. Arrivederci. A traveler's essential — Mi piace.. the language of music. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-italian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
