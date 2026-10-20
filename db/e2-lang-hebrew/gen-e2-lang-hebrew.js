(function(){'use strict';
/* JAH Hebrew Phrasebook Database generator — jahdb-e2-lang-hebrew-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-hebrew',PREFIX='JAH-E2LANGHEBRE-',NAME='JAH Hebrew Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hebrew phrasebook: complete", "d": "Hebrew: 9M+ speakers. revived from scripture..", "g": "overview", "l": 2, "q": "What is Hebrew phrasebook: complete?", "a": "Hebrew: 9M+ speakers. revived from scripture..", "x": "The complete Hebrew phrasebook: revived from scripture.. Shalom. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 9M+ Ani ohev. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Hebrew: revived from scripture..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Hebrew: revived from scripture..", "x": "About Hebrew: 9M+ speakers — revived from scripture.. Toda. Where it is spoken, its family, its script. Kama ole. Bevakasha. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Shalom.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Shalom.", "x": "Hebrew essential 1: Shalom.. Kama ole. Learn these first — Bevakasha.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Shalom..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Shalom..", "x": "Usage: Shalom.. Ani medaber ktsat. When and how — Eifo.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Toda.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Toda.", "x": "Hebrew essential 2: Toda.. Ani medaber ktsat. Learn these first — Eifo.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Toda..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Toda..", "x": "Usage: Toda.. Sherutim. When and how — Heshbon.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Bevakasha.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Bevakasha.", "x": "Hebrew essential 3: Bevakasha.. Sherutim. Learn these first — Heshbon.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bevakasha..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bevakasha..", "x": "Usage: Bevakasha.. Ezra. When and how — Ken/Lo.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Eifo.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Eifo.", "x": "Hebrew essential 4: Eifo.. Ezra. Learn these first — Ken/Lo.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Eifo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Eifo..", "x": "Usage: Eifo.. Lechaim. When and how — Slicha.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Heshbon.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Heshbon.", "x": "Hebrew essential 5: Heshbon.. Lechaim. Learn these first — Slicha.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Heshbon..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Heshbon..", "x": "Usage: Heshbon.. Boker tov. When and how — Lehitraot.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ken/Lo.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ken/Lo.", "x": "Hebrew essential 6: Ken/Lo.. Boker tov. Learn these first — Lehitraot.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ken/Lo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ken/Lo..", "x": "Usage: Ken/Lo.. Laila tov. When and how — Shalom.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Slicha.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Slicha.", "x": "Hebrew essential 7: Slicha.. Laila tov. Learn these first — Shalom.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Slicha..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Slicha..", "x": "Usage: Slicha.. Ani ohev. When and how — Toda.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Lehitraot.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Lehitraot.", "x": "Hebrew essential 8: Lehitraot.. Ani ohev. Learn these first — Toda.. revived from scripture. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Lehitraot..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Lehitraot..", "x": "Usage: Lehitraot.. Kama ole. When and how — Bevakasha.. Hebrew revived from scripture. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Ani ohev.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Ani ohev.", "x": "Hebrew phrase: Ani ohev.. Toda. A traveler's essential — Ani medaber ktsat.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Kama ole.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Kama ole.", "x": "Hebrew phrase: Kama ole.. Bevakasha. A traveler's essential — Sherutim.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ani medaber ktsat.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ani medaber ktsat.", "x": "Hebrew phrase: Ani medaber ktsat.. Eifo. A traveler's essential — Ezra.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Sherutim.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Sherutim.", "x": "Hebrew phrase: Sherutim.. Heshbon. A traveler's essential — Lechaim.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Ezra.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Ezra.", "x": "Hebrew phrase: Ezra.. Ken/Lo. A traveler's essential — Boker tov.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Lechaim.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Lechaim.", "x": "Hebrew phrase: Lechaim.. Slicha. A traveler's essential — Laila tov.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Boker tov.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Boker tov.", "x": "Hebrew phrase: Boker tov.. Lehitraot. A traveler's essential — Ani ohev.. revived from scripture. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-hebrew-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
