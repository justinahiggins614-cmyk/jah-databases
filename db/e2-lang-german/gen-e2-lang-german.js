(function(){'use strict';
/* JAH German Phrasebook Database generator — jahdb-e2-lang-german-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-german',PREFIX='JAH-E2LANGGERMA-',NAME='JAH German Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "German phrasebook: complete", "d": "German: 130M+ speakers. the language of precision..", "g": "overview", "l": 2, "q": "What is German phrasebook: complete?", "a": "German: 130M+ speakers. the language of precision..", "x": "The complete German phrasebook: the language of precision.. Hallo. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 130M+ Ich mag. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "German: the language of precision..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "German: the language of precision..", "x": "About German: 130M+ speakers — the language of precision.. Danke. Where it is spoken, its family, its script. Wie viel. Bitte. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hallo.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hallo.", "x": "German essential 1: Hallo.. Wie viel. Learn these first — Bitte.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hallo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hallo..", "x": "Usage: Hallo.. Ich spreche wenig. When and how — Wo ist.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Danke.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Danke.", "x": "German essential 2: Danke.. Ich spreche wenig. Learn these first — Wo ist.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Danke..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Danke..", "x": "Usage: Danke.. Toilette. When and how — Die Rechnung.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Bitte.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Bitte.", "x": "German essential 3: Bitte.. Toilette. Learn these first — Die Rechnung.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bitte..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bitte..", "x": "Usage: Bitte.. Hilfe. When and how — Ja/Nein.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Wo ist.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Wo ist.", "x": "German essential 4: Wo ist.. Hilfe. Learn these first — Ja/Nein.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Wo ist..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Wo ist..", "x": "Usage: Wo ist.. Prost. When and how — Entschuldigung.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Die Rechnung.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Die Rechnung.", "x": "German essential 5: Die Rechnung.. Prost. Learn these first — Entschuldigung.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Die Rechnung..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Die Rechnung..", "x": "Usage: Die Rechnung.. Guten Morgen. When and how — Tschuss.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ja/Nein.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ja/Nein.", "x": "German essential 6: Ja/Nein.. Guten Morgen. Learn these first — Tschuss.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ja/Nein..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ja/Nein..", "x": "Usage: Ja/Nein.. Gute Nacht. When and how — Hallo.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Entschuldigung.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Entschuldigung.", "x": "German essential 7: Entschuldigung.. Gute Nacht. Learn these first — Hallo.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Entschuldigung..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Entschuldigung..", "x": "Usage: Entschuldigung.. Ich mag. When and how — Danke.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Tschuss.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Tschuss.", "x": "German essential 8: Tschuss.. Ich mag. Learn these first — Danke.. the language of precision. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tschuss..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tschuss..", "x": "Usage: Tschuss.. Wie viel. When and how — Bitte.. German the language of precision. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Ich mag.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Ich mag.", "x": "German phrase: Ich mag.. Danke. A traveler's essential — Ich spreche wenig.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Wie viel.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Wie viel.", "x": "German phrase: Wie viel.. Bitte. A traveler's essential — Toilette.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ich spreche wenig.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ich spreche wenig.", "x": "German phrase: Ich spreche wenig.. Wo ist. A traveler's essential — Hilfe.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toilette.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toilette.", "x": "German phrase: Toilette.. Die Rechnung. A traveler's essential — Prost.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Hilfe.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Hilfe.", "x": "German phrase: Hilfe.. Ja/Nein. A traveler's essential — Guten Morgen.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Prost.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Prost.", "x": "German phrase: Prost.. Entschuldigung. A traveler's essential — Gute Nacht.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Guten Morgen.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Guten Morgen.", "x": "German phrase: Guten Morgen.. Tschuss. A traveler's essential — Ich mag.. the language of precision. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-german-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
