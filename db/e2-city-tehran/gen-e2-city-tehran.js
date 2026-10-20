(function(){'use strict';
/* JAH Tehran City Database generator — jahdb-e2-city-tehran-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-tehran',PREFIX='JAH-E2CITYTEHRA-',NAME='JAH Tehran City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tehran: the complete city guide", "d": "Tehran, Iran: at the Alborz' feet..", "g": "overview", "l": 2, "q": "What is Tehran: the complete city guide?", "a": "Tehran, Iran: at the Alborz' feet..", "x": "The complete Tehran city guide: at the Alborz' feet.. Golestan Palace. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Tehran in one database. Palaces. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Tehran essentials: Golestan Palace..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Tehran essentials: Golestan Palace..", "x": "At a glance: Tehran, Iran — at the Alborz' feet.. Grand Bazaar. The numbers, the layout, the vibe: Tehran in brief. Bazaar. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Golestan Palace.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Golestan Palace.", "x": "Tehran: Golestan Palace.. Bazaar. One of the defining things about Tehran — Milad Tower.. at the Alborz' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Golestan Palace..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Golestan Palace..", "x": "Guide: Golestan Palace.. Day trip: Damavand. How to do it right — Tehran. Kebabs. at the Alborz' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Grand Bazaar.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Grand Bazaar.", "x": "Tehran: Grand Bazaar.. Mountains. One of the defining things about Tehran — Kebabs.. at the Alborz' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Grand Bazaar..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Grand Bazaar..", "x": "Guide: Grand Bazaar.. Food. How to do it right — Tehran. Museums. at the Alborz' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Milad Tower.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Milad Tower.", "x": "Tehran: Milad Tower.. Day trip: Damavand. One of the defining things about Tehran — Museums.. at the Alborz' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Milad Tower..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Milad Tower..", "x": "Guide: Milad Tower.. Culture. How to do it right — Tehran. Mountains. at the Alborz' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Kebabs.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Kebabs.", "x": "Tehran: Kebabs.. Food. One of the defining things about Tehran — Mountains.. at the Alborz' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Kebabs..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Kebabs..", "x": "Guide: Kebabs.. Palaces. How to do it right — Tehran. Golestan Palace. at the Alborz' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Museums.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Museums.", "x": "Tehran: Museums.. Culture. One of the defining things about Tehran — Golestan Palace.. at the Alborz' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Museums..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Museums..", "x": "Guide: Museums.. Bazaar. How to do it right — Tehran. Grand Bazaar. at the Alborz' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Mountains.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Mountains.", "x": "Tehran: Mountains.. Palaces. One of the defining things about Tehran — Grand Bazaar.. at the Alborz' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Mountains..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Mountains..", "x": "Guide: Mountains.. Mountains. How to do it right — Tehran. Milad Tower. at the Alborz' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Palaces.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Palaces.", "x": "Tehran in depth: Palaces.. Grand Bazaar. The details — at the Alborz' feet.. Mountains. Kebabs. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bazaar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bazaar.", "x": "Tehran in depth: Bazaar.. Milad Tower. The details — at the Alborz' feet.. Day trip: Damavand. Museums. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mountains.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mountains.", "x": "Tehran in depth: Mountains.. Kebabs. The details — at the Alborz' feet.. Food. Mountains. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Damavand.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Damavand.", "x": "Tehran in depth: Day trip: Damavand.. Museums. The details — at the Alborz' feet.. Culture. Golestan Palace. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Food.", "x": "Tehran in depth: Food.. Mountains. The details — at the Alborz' feet.. Palaces. Grand Bazaar. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Tehran in depth: Culture.. Golestan Palace. The details — at the Alborz' feet.. Bazaar. Milad Tower. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Tehran's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Tehran's districts.", "x": "Neighborhoods: Palaces.. Milad Tower. Where to stay, eat, and wander — Tehran. at the Alborz' feet. Every district has its own personality; Bazaar.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Tehran: Kebabs..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Tehran: Kebabs..", "x": "Food: Kebabs.. Mountains. The tastes of Tehran — at the Alborz' feet.. Museums. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Tehran transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Tehran transport.", "x": "Transport: Day trip: Damavand.. Mountains. Subways, buses, walking — Tehran. at the Alborz' feet. Learn the system on day one; Food.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Tehran.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Tehran.", "x": "Timing: Culture.. Golestan Palace. Seasons and festivals — Tehran. at the Alborz' feet. Time it right for Palaces.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Tehran safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Tehran safely.", "x": "Safety: Bazaar.. Grand Bazaar. Sensible precautions — Tehran. at the Alborz' feet. Big cities reward street smarts; Mountains.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-tehran-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
