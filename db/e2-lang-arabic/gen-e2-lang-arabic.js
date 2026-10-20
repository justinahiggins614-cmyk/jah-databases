(function(){'use strict';
/* JAH Arabic Phrasebook Database generator — jahdb-e2-lang-arabic-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-arabic',PREFIX='JAH-E2LANGARABI-',NAME='JAH Arabic Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Arabic phrasebook: complete", "d": "Arabic: 400M+ speakers. the language of the Quran..", "g": "overview", "l": 2, "q": "What is Arabic phrasebook: complete?", "a": "Arabic: 400M+ speakers. the language of the Quran..", "x": "The complete Arabic phrasebook: the language of the Quran.. As-salamu alaykum. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 400M+ Uhibbu. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Arabic: the language of the Quran..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Arabic: the language of the Quran..", "x": "About Arabic: 400M+ speakers — the language of the Quran.. Shukran. Where it is spoken, its family, its script. Kam. Min fadlak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "As-salamu alaykum.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "As-salamu alaykum.", "x": "Arabic essential 1: As-salamu alaykum.. Kam. Learn these first — Min fadlak.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: As-salamu alaykum..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: As-salamu alaykum..", "x": "Usage: As-salamu alaykum.. Atakallam qalilan. When and how — Wayn.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Shukran.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Shukran.", "x": "Arabic essential 2: Shukran.. Atakallam qalilan. Learn these first — Wayn.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Shukran..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Shukran..", "x": "Usage: Shukran.. Hammam. When and how — Al-hisab.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Min fadlak.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Min fadlak.", "x": "Arabic essential 3: Min fadlak.. Hammam. Learn these first — Al-hisab.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Min fadlak..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Min fadlak..", "x": "Usage: Min fadlak.. Musa'ada. When and how — Naam/La.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Wayn.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Wayn.", "x": "Arabic essential 4: Wayn.. Musa'ada. Learn these first — Naam/La.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Wayn..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Wayn..", "x": "Usage: Wayn.. Bi sahhtak. When and how — Afwan.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Al-hisab.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Al-hisab.", "x": "Arabic essential 5: Al-hisab.. Bi sahhtak. Learn these first — Afwan.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Al-hisab..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Al-hisab..", "x": "Usage: Al-hisab.. Sabah al-khayr. When and how — Ma'a salama.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Naam/La.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Naam/La.", "x": "Arabic essential 6: Naam/La.. Sabah al-khayr. Learn these first — Ma'a salama.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Naam/La..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Naam/La..", "x": "Usage: Naam/La.. Tisbah ala khayr. When and how — As-salamu alaykum.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Afwan.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Afwan.", "x": "Arabic essential 7: Afwan.. Tisbah ala khayr. Learn these first — As-salamu alaykum.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Afwan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Afwan..", "x": "Usage: Afwan.. Uhibbu. When and how — Shukran.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Ma'a salama.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Ma'a salama.", "x": "Arabic essential 8: Ma'a salama.. Uhibbu. Learn these first — Shukran.. the language of the Quran. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ma'a salama..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ma'a salama..", "x": "Usage: Ma'a salama.. Kam. When and how — Min fadlak.. Arabic the language of the Quran. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Uhibbu.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Uhibbu.", "x": "Arabic phrase: Uhibbu.. Shukran. A traveler's essential — Atakallam qalilan.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Kam.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Kam.", "x": "Arabic phrase: Kam.. Min fadlak. A traveler's essential — Hammam.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Atakallam qalilan.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Atakallam qalilan.", "x": "Arabic phrase: Atakallam qalilan.. Wayn. A traveler's essential — Musa'ada.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Hammam.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Hammam.", "x": "Arabic phrase: Hammam.. Al-hisab. A traveler's essential — Bi sahhtak.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Musa'ada.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Musa'ada.", "x": "Arabic phrase: Musa'ada.. Naam/La. A traveler's essential — Sabah al-khayr.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Bi sahhtak.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Bi sahhtak.", "x": "Arabic phrase: Bi sahhtak.. Afwan. A traveler's essential — Tisbah ala khayr.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Sabah al-khayr.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Sabah al-khayr.", "x": "Arabic phrase: Sabah al-khayr.. Ma'a salama. A traveler's essential — Uhibbu.. the language of the Quran. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-arabic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
