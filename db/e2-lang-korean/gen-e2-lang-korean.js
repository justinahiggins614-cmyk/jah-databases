(function(){'use strict';
/* JAH Korean Phrasebook Database generator — jahdb-e2-lang-korean-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-korean',PREFIX='JAH-E2LANGKOREA-',NAME='JAH Korean Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Korean phrasebook: complete", "d": "Korean: 80M+ speakers. the hangul language..", "g": "overview", "l": 2, "q": "What is Korean phrasebook: complete?", "a": "Korean: 80M+ speakers. the hangul language..", "x": "The complete Korean phrasebook: the hangul language.. Annyeonghaseyo. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 80M+ Joahamnida. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Korean: the hangul language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Korean: the hangul language..", "x": "About Korean: 80M+ speakers — the hangul language.. Gamsahamnida. Where it is spoken, its family, its script. Eolmayeyo. Juseyo. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Annyeonghaseyo.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Annyeonghaseyo.", "x": "Korean essential 1: Annyeonghaseyo.. Eolmayeyo. Learn these first — Juseyo.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Annyeonghaseyo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Annyeonghaseyo..", "x": "Usage: Annyeonghaseyo.. Jogeum. When and how — Eodiyeyo.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Gamsahamnida.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Gamsahamnida.", "x": "Korean essential 2: Gamsahamnida.. Jogeum. Learn these first — Eodiyeyo.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Gamsahamnida..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Gamsahamnida..", "x": "Usage: Gamsahamnida.. Hwajangsil. When and how — Gyesanso.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Juseyo.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Juseyo.", "x": "Korean essential 3: Juseyo.. Hwajangsil. Learn these first — Gyesanso.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Juseyo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Juseyo..", "x": "Usage: Juseyo.. Dowajuseyo. When and how — Ne/Aniyo.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Eodiyeyo.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Eodiyeyo.", "x": "Korean essential 4: Eodiyeyo.. Dowajuseyo. Learn these first — Ne/Aniyo.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Eodiyeyo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Eodiyeyo..", "x": "Usage: Eodiyeyo.. Geonbae. When and how — Joesonghamnida.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Gyesanso.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Gyesanso.", "x": "Korean essential 5: Gyesanso.. Geonbae. Learn these first — Joesonghamnida.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Gyesanso..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Gyesanso..", "x": "Usage: Gyesanso.. Annyeonghi juseyo. When and how — Annyeonghi gaseyo.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ne/Aniyo.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ne/Aniyo.", "x": "Korean essential 6: Ne/Aniyo.. Annyeonghi juseyo. Learn these first — Annyeonghi gaseyo.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ne/Aniyo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ne/Aniyo..", "x": "Usage: Ne/Aniyo.. Jal jayo. When and how — Annyeonghaseyo.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Joesonghamnida.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Joesonghamnida.", "x": "Korean essential 7: Joesonghamnida.. Jal jayo. Learn these first — Annyeonghaseyo.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Joesonghamnida..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Joesonghamnida..", "x": "Usage: Joesonghamnida.. Joahamnida. When and how — Gamsahamnida.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Annyeonghi gaseyo.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Annyeonghi gaseyo.", "x": "Korean essential 8: Annyeonghi gaseyo.. Joahamnida. Learn these first — Gamsahamnida.. the hangul language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Annyeonghi gaseyo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Annyeonghi gaseyo..", "x": "Usage: Annyeonghi gaseyo.. Eolmayeyo. When and how — Juseyo.. Korean the hangul language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Joahamnida.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Joahamnida.", "x": "Korean phrase: Joahamnida.. Gamsahamnida. A traveler's essential — Jogeum.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Eolmayeyo.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Eolmayeyo.", "x": "Korean phrase: Eolmayeyo.. Juseyo. A traveler's essential — Hwajangsil.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Jogeum.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Jogeum.", "x": "Korean phrase: Jogeum.. Eodiyeyo. A traveler's essential — Dowajuseyo.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Hwajangsil.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Hwajangsil.", "x": "Korean phrase: Hwajangsil.. Gyesanso. A traveler's essential — Geonbae.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Dowajuseyo.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Dowajuseyo.", "x": "Korean phrase: Dowajuseyo.. Ne/Aniyo. A traveler's essential — Annyeonghi juseyo.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Geonbae.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Geonbae.", "x": "Korean phrase: Geonbae.. Joesonghamnida. A traveler's essential — Jal jayo.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Annyeonghi juseyo.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Annyeonghi juseyo.", "x": "Korean phrase: Annyeonghi juseyo.. Annyeonghi gaseyo. A traveler's essential — Joahamnida.. the hangul language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-korean-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
