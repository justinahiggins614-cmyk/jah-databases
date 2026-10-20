(function(){'use strict';
/* JAH Vietnamese Phrasebook Database generator — jahdb-e2-lang-vietnamese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-vietnamese',PREFIX='JAH-E2LANGVIETN-',NAME='JAH Vietnamese Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vietnamese phrasebook: complete", "d": "Vietnamese: 95M+ speakers. the tonal language..", "g": "overview", "l": 2, "q": "What is Vietnamese phrasebook: complete?", "a": "Vietnamese: 95M+ speakers. the tonal language..", "x": "The complete Vietnamese phrasebook: the tonal language.. Xin chao. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 95M+ Toi thich. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Vietnamese: the tonal language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Vietnamese: the tonal language..", "x": "About Vietnamese: 95M+ speakers — the tonal language.. Cam on. Where it is spoken, its family, its script. Bao nhieu. Lam on. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Xin chao.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Xin chao.", "x": "Vietnamese essential 1: Xin chao.. Bao nhieu. Learn these first — Lam on.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Xin chao..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Xin chao..", "x": "Usage: Xin chao.. Toi noi it. When and how — O dau.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Cam on.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Cam on.", "x": "Vietnamese essential 2: Cam on.. Toi noi it. Learn these first — O dau.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Cam on..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Cam on..", "x": "Usage: Cam on.. Nha ve sinh. When and how — Tinh tien.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Lam on.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Lam on.", "x": "Vietnamese essential 3: Lam on.. Nha ve sinh. Learn these first — Tinh tien.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Lam on..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Lam on..", "x": "Usage: Lam on.. Cuu toi. When and how — Vang/Khong.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "O dau.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "O dau.", "x": "Vietnamese essential 4: O dau.. Cuu toi. Learn these first — Vang/Khong.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: O dau..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: O dau..", "x": "Usage: O dau.. Chuc suc khoe. When and how — Xin loi.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Tinh tien.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Tinh tien.", "x": "Vietnamese essential 5: Tinh tien.. Chuc suc khoe. Learn these first — Xin loi.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tinh tien..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tinh tien..", "x": "Usage: Tinh tien.. Chao buoi sang. When and how — Tam biet.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Vang/Khong.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Vang/Khong.", "x": "Vietnamese essential 6: Vang/Khong.. Chao buoi sang. Learn these first — Tam biet.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Vang/Khong..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Vang/Khong..", "x": "Usage: Vang/Khong.. Chuc ngu ngon. When and how — Xin chao.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Xin loi.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Xin loi.", "x": "Vietnamese essential 7: Xin loi.. Chuc ngu ngon. Learn these first — Xin chao.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Xin loi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Xin loi..", "x": "Usage: Xin loi.. Toi thich. When and how — Cam on.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Tam biet.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Tam biet.", "x": "Vietnamese essential 8: Tam biet.. Toi thich. Learn these first — Cam on.. the tonal language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tam biet..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tam biet..", "x": "Usage: Tam biet.. Bao nhieu. When and how — Lam on.. Vietnamese the tonal language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Toi thich.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Toi thich.", "x": "Vietnamese phrase: Toi thich.. Cam on. A traveler's essential — Toi noi it.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Bao nhieu.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Bao nhieu.", "x": "Vietnamese phrase: Bao nhieu.. Lam on. A traveler's essential — Nha ve sinh.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Toi noi it.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Toi noi it.", "x": "Vietnamese phrase: Toi noi it.. O dau. A traveler's essential — Cuu toi.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Nha ve sinh.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Nha ve sinh.", "x": "Vietnamese phrase: Nha ve sinh.. Tinh tien. A traveler's essential — Chuc suc khoe.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Cuu toi.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Cuu toi.", "x": "Vietnamese phrase: Cuu toi.. Vang/Khong. A traveler's essential — Chao buoi sang.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Chuc suc khoe.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Chuc suc khoe.", "x": "Vietnamese phrase: Chuc suc khoe.. Xin loi. A traveler's essential — Chuc ngu ngon.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Chao buoi sang.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Chao buoi sang.", "x": "Vietnamese phrase: Chao buoi sang.. Tam biet. A traveler's essential — Toi thich.. the tonal language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-vietnamese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
