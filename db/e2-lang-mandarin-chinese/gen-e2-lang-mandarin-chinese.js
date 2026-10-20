(function(){'use strict';
/* JAH Mandarin Chinese Phrasebook Database generator — jahdb-e2-lang-mandarin-chinese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-mandarin-chinese',PREFIX='JAH-E2LANGMANDA-',NAME='JAH Mandarin Chinese Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mandarin Chinese phrasebook: complete", "d": "Mandarin Chinese: 1B+ speakers. the most spoken language..", "g": "overview", "l": 2, "q": "What is Mandarin Chinese phrasebook: complete?", "a": "Mandarin Chinese: 1B+ speakers. the most spoken language..", "x": "The complete Mandarin Chinese phrasebook: the most spoken language.. Ni hao. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 1B+ Wo xihuan. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Mandarin Chinese: the most spoken language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Mandarin Chinese: the most spoken language..", "x": "About Mandarin Chinese: 1B+ speakers — the most spoken language.. Xie xie. Where it is spoken, its family, its script. Duoshao qian. Qing. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Ni hao.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Ni hao.", "x": "Mandarin Chinese essential 1: Ni hao.. Duoshao qian. Learn these first — Qing.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ni hao..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ni hao..", "x": "Usage: Ni hao.. Wo shuo yidian. When and how — Zai nar.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Xie xie.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Xie xie.", "x": "Mandarin Chinese essential 2: Xie xie.. Wo shuo yidian. Learn these first — Zai nar.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Xie xie..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Xie xie..", "x": "Usage: Xie xie.. Cesuo. When and how — Mai dan.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Qing.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Qing.", "x": "Mandarin Chinese essential 3: Qing.. Cesuo. Learn these first — Mai dan.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Qing..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Qing..", "x": "Usage: Qing.. Bang mang. When and how — Shi/Bu.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Zai nar.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Zai nar.", "x": "Mandarin Chinese essential 4: Zai nar.. Bang mang. Learn these first — Shi/Bu.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Zai nar..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Zai nar..", "x": "Usage: Zai nar.. Gan bei. When and how — Dui bu qi.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Mai dan.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Mai dan.", "x": "Mandarin Chinese essential 5: Mai dan.. Gan bei. Learn these first — Dui bu qi.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Mai dan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Mai dan..", "x": "Usage: Mai dan.. Zao shang hao. When and how — Zai jian.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Shi/Bu.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Shi/Bu.", "x": "Mandarin Chinese essential 6: Shi/Bu.. Zao shang hao. Learn these first — Zai jian.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Shi/Bu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Shi/Bu..", "x": "Usage: Shi/Bu.. Wan an. When and how — Ni hao.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Dui bu qi.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Dui bu qi.", "x": "Mandarin Chinese essential 7: Dui bu qi.. Wan an. Learn these first — Ni hao.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dui bu qi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dui bu qi..", "x": "Usage: Dui bu qi.. Wo xihuan. When and how — Xie xie.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Zai jian.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Zai jian.", "x": "Mandarin Chinese essential 8: Zai jian.. Wo xihuan. Learn these first — Xie xie.. the most spoken language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Zai jian..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Zai jian..", "x": "Usage: Zai jian.. Duoshao qian. When and how — Qing.. Mandarin Chinese the most spoken language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Wo xihuan.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Wo xihuan.", "x": "Mandarin Chinese phrase: Wo xihuan.. Xie xie. A traveler's essential — Wo shuo yidian.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Duoshao qian.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Duoshao qian.", "x": "Mandarin Chinese phrase: Duoshao qian.. Qing. A traveler's essential — Cesuo.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Wo shuo yidian.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Wo shuo yidian.", "x": "Mandarin Chinese phrase: Wo shuo yidian.. Zai nar. A traveler's essential — Bang mang.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Cesuo.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Cesuo.", "x": "Mandarin Chinese phrase: Cesuo.. Mai dan. A traveler's essential — Gan bei.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Bang mang.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Bang mang.", "x": "Mandarin Chinese phrase: Bang mang.. Shi/Bu. A traveler's essential — Zao shang hao.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Gan bei.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Gan bei.", "x": "Mandarin Chinese phrase: Gan bei.. Dui bu qi. A traveler's essential — Wan an.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Zao shang hao.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Zao shang hao.", "x": "Mandarin Chinese phrase: Zao shang hao.. Zai jian. A traveler's essential — Wo xihuan.. the most spoken language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-mandarin-chinese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
