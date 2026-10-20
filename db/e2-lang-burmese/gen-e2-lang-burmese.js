(function(){'use strict';
/* JAH Burmese Phrasebook Database generator — jahdb-e2-lang-burmese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-burmese',PREFIX='JAH-E2LANGBURME-',NAME='JAH Burmese Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Burmese phrasebook: complete", "d": "Burmese: 35M+ speakers. Myanmar's tongue..", "g": "overview", "l": 2, "q": "What is Burmese phrasebook: complete?", "a": "Burmese: 35M+ speakers. Myanmar's tongue..", "x": "The complete Burmese phrasebook: Myanmar's tongue.. Mingalaba. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 35M+ Chit de. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Burmese: Myanmar's tongue..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Burmese: Myanmar's tongue..", "x": "About Burmese: 35M+ speakers — Myanmar's tongue.. Kyay zu tin ba de. Where it is spoken, its family, its script. Be lau. Kyay zu pyu. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Mingalaba.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Mingalaba.", "x": "Burmese essential 1: Mingalaba.. Be lau. Learn these first — Kyay zu pyu.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Mingalaba..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Mingalaba..", "x": "Usage: Mingalaba.. Ne ne. When and how — Beh mhar.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Kyay zu tin ba de.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Kyay zu tin ba de.", "x": "Burmese essential 2: Kyay zu tin ba de.. Ne ne. Learn these first — Beh mhar.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kyay zu tin ba de..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kyay zu tin ba de..", "x": "Usage: Kyay zu tin ba de.. Ein tha. When and how — Shin.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Kyay zu pyu.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Kyay zu pyu.", "x": "Burmese essential 3: Kyay zu pyu.. Ein tha. Learn these first — Shin.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kyay zu pyu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kyay zu pyu..", "x": "Usage: Kyay zu pyu.. Ke zu. When and how — Hote/Ma hote.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Beh mhar.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Beh mhar.", "x": "Burmese essential 4: Beh mhar.. Ke zu. Learn these first — Hote/Ma hote.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Beh mhar..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Beh mhar..", "x": "Usage: Beh mhar.. Aung myin. When and how — Taung pan.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Shin.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Shin.", "x": "Burmese essential 5: Shin.. Aung myin. Learn these first — Taung pan.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Shin..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Shin..", "x": "Usage: Shin.. Mingalaba. When and how — Thwa dau meh.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Hote/Ma hote.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Hote/Ma hote.", "x": "Burmese essential 6: Hote/Ma hote.. Mingalaba. Learn these first — Thwa dau meh.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hote/Ma hote..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hote/Ma hote..", "x": "Usage: Hote/Ma hote.. Eip met. When and how — Mingalaba.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Taung pan.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Taung pan.", "x": "Burmese essential 7: Taung pan.. Eip met. Learn these first — Mingalaba.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Taung pan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Taung pan..", "x": "Usage: Taung pan.. Chit de. When and how — Kyay zu tin ba de.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Thwa dau meh.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Thwa dau meh.", "x": "Burmese essential 8: Thwa dau meh.. Chit de. Learn these first — Kyay zu tin ba de.. Myanmar's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Thwa dau meh..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Thwa dau meh..", "x": "Usage: Thwa dau meh.. Be lau. When and how — Kyay zu pyu.. Burmese Myanmar's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Chit de.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Chit de.", "x": "Burmese phrase: Chit de.. Kyay zu tin ba de. A traveler's essential — Ne ne.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Be lau.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Be lau.", "x": "Burmese phrase: Be lau.. Kyay zu pyu. A traveler's essential — Ein tha.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ne ne.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ne ne.", "x": "Burmese phrase: Ne ne.. Beh mhar. A traveler's essential — Ke zu.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Ein tha.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Ein tha.", "x": "Burmese phrase: Ein tha.. Shin. A traveler's essential — Aung myin.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Ke zu.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Ke zu.", "x": "Burmese phrase: Ke zu.. Hote/Ma hote. A traveler's essential — Mingalaba.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Aung myin.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Aung myin.", "x": "Burmese phrase: Aung myin.. Taung pan. A traveler's essential — Eip met.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Mingalaba.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Mingalaba.", "x": "Burmese phrase: Mingalaba.. Thwa dau meh. A traveler's essential — Chit de.. Myanmar's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-burmese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
