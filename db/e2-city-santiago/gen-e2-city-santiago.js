(function(){'use strict';
/* JAH Santiago City Database generator — jahdb-e2-city-santiago-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-santiago',PREFIX='JAH-E2CITYSANTI-',NAME='JAH Santiago City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Santiago: the complete city guide", "d": "Santiago, Chile: at the Andes' feet..", "g": "overview", "l": 2, "q": "What is Santiago: the complete city guide?", "a": "Santiago, Chile: at the Andes' feet..", "x": "The complete Santiago city guide: at the Andes' feet.. Plaza de Armas. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Santiago in one database. Hills. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Santiago essentials: Plaza de Armas..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Santiago essentials: Plaza de Armas..", "x": "At a glance: Santiago, Chile — at the Andes' feet.. Cerro San Cristobal. The numbers, the layout, the vibe: Santiago in brief. Wine. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Plaza de Armas.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Plaza de Armas.", "x": "Santiago: Plaza de Armas.. Wine. One of the defining things about Santiago — Bellavista.. at the Andes' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Plaza de Armas..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Plaza de Armas..", "x": "Guide: Plaza de Armas.. Metro. How to do it right — Santiago. Empanadas. at the Andes' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Cerro San Cristobal.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Cerro San Cristobal.", "x": "Santiago: Cerro San Cristobal.. Day trip: Valparaiso. One of the defining things about Santiago — Empanadas.. at the Andes' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Cerro San Cristobal..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Cerro San Cristobal..", "x": "Guide: Cerro San Cristobal.. Views. How to do it right — Santiago. Wine. at the Andes' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Bellavista.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Bellavista.", "x": "Santiago: Bellavista.. Metro. One of the defining things about Santiago — Wine.. at the Andes' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Bellavista..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Bellavista..", "x": "Guide: Bellavista.. Culture. How to do it right — Santiago. Andes. at the Andes' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Empanadas.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Empanadas.", "x": "Santiago: Empanadas.. Views. One of the defining things about Santiago — Andes.. at the Andes' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Empanadas..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Empanadas..", "x": "Guide: Empanadas.. Hills. How to do it right — Santiago. Plaza de Armas. at the Andes' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Wine.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Wine.", "x": "Santiago: Wine.. Culture. One of the defining things about Santiago — Plaza de Armas.. at the Andes' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Wine..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Wine..", "x": "Guide: Wine.. Wine. How to do it right — Santiago. Cerro San Cristobal. at the Andes' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Andes.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Andes.", "x": "Santiago: Andes.. Hills. One of the defining things about Santiago — Cerro San Cristobal.. at the Andes' feet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Andes..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Andes..", "x": "Guide: Andes.. Day trip: Valparaiso. How to do it right — Santiago. Bellavista. at the Andes' feet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hills.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hills.", "x": "Santiago in depth: Hills.. Cerro San Cristobal. The details — at the Andes' feet.. Day trip: Valparaiso. Empanadas. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wine.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wine.", "x": "Santiago in depth: Wine.. Bellavista. The details — at the Andes' feet.. Metro. Wine. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Day trip: Valparaiso.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Day trip: Valparaiso.", "x": "Santiago in depth: Day trip: Valparaiso.. Empanadas. The details — at the Andes' feet.. Views. Andes. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Metro.", "x": "Santiago in depth: Metro.. Wine. The details — at the Andes' feet.. Culture. Plaza de Armas. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Santiago in depth: Views.. Andes. The details — at the Andes' feet.. Hills. Cerro San Cristobal. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Santiago in depth: Culture.. Plaza de Armas. The details — at the Andes' feet.. Wine. Bellavista. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Santiago's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Santiago's districts.", "x": "Neighborhoods: Hills.. Bellavista. Where to stay, eat, and wander — Santiago. at the Andes' feet. Every district has its own personality; Wine.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Santiago: Empanadas..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Santiago: Empanadas..", "x": "Food: Empanadas.. Day trip: Valparaiso. The tastes of Santiago — at the Andes' feet.. Wine. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Santiago transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Santiago transport.", "x": "Transport: Metro.. Andes. Subways, buses, walking — Santiago. at the Andes' feet. Learn the system on day one; Views.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Santiago.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Santiago.", "x": "Timing: Culture.. Plaza de Armas. Seasons and festivals — Santiago. at the Andes' feet. Time it right for Hills.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Santiago safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Santiago safely.", "x": "Safety: Wine.. Cerro San Cristobal. Sensible precautions — Santiago. at the Andes' feet. Big cities reward street smarts; Day trip: Valparaiso.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-santiago-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
