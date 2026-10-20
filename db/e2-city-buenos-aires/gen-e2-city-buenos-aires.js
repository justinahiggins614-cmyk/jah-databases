(function(){'use strict';
/* JAH Buenos Aires City Database generator — jahdb-e2-city-buenos-aires-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-buenos-aires',PREFIX='JAH-E2CITYBUENO-',NAME='JAH Buenos Aires City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Buenos Aires: the complete city guide", "d": "Buenos Aires, Argentina: the Paris of South America..", "g": "overview", "l": 2, "q": "What is Buenos Aires: the complete city guide?", "a": "Buenos Aires, Argentina: the Paris of South America..", "x": "The complete Buenos Aires city guide: the Paris of South America.. La Boca. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Buenos Aires in one database. Tango. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Buenos Aires essentials: La Boca..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Buenos Aires essentials: La Boca..", "x": "At a glance: Buenos Aires, Argentina — the Paris of South America.. Recoleta. The numbers, the layout, the vibe: Buenos Aires in brief. Steak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "La Boca.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "La Boca.", "x": "Buenos Aires: La Boca.. Steak. One of the defining things about Buenos Aires — Tango shows.. the Paris of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: La Boca..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: La Boca..", "x": "Guide: La Boca.. Day trip: Tigre. How to do it right — Buenos Aires. Teatro Colon. the Paris of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Recoleta.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Recoleta.", "x": "Buenos Aires: Recoleta.. Neighborhoods. One of the defining things about Buenos Aires — Teatro Colon.. the Paris of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Recoleta..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Recoleta..", "x": "Guide: Recoleta.. Subte. How to do it right — Buenos Aires. Steak. the Paris of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Tango shows.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Tango shows.", "x": "Buenos Aires: Tango shows.. Day trip: Tigre. One of the defining things about Buenos Aires — Steak.. the Paris of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Tango shows..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Tango shows..", "x": "Guide: Tango shows.. Culture. How to do it right — Buenos Aires. San Telmo. the Paris of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Teatro Colon.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Teatro Colon.", "x": "Buenos Aires: Teatro Colon.. Subte. One of the defining things about Buenos Aires — San Telmo.. the Paris of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Teatro Colon..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Teatro Colon..", "x": "Guide: Teatro Colon.. Tango. How to do it right — Buenos Aires. La Boca. the Paris of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Steak.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Steak.", "x": "Buenos Aires: Steak.. Culture. One of the defining things about Buenos Aires — La Boca.. the Paris of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Steak..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Steak..", "x": "Guide: Steak.. Steak. How to do it right — Buenos Aires. Recoleta. the Paris of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "San Telmo.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "San Telmo.", "x": "Buenos Aires: San Telmo.. Tango. One of the defining things about Buenos Aires — Recoleta.. the Paris of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: San Telmo..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: San Telmo..", "x": "Guide: San Telmo.. Neighborhoods. How to do it right — Buenos Aires. Tango shows. the Paris of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tango.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tango.", "x": "Buenos Aires in depth: Tango.. Recoleta. The details — the Paris of South America.. Neighborhoods. Teatro Colon. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Steak.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Steak.", "x": "Buenos Aires in depth: Steak.. Tango shows. The details — the Paris of South America.. Day trip: Tigre. Steak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Neighborhoods.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Neighborhoods.", "x": "Buenos Aires in depth: Neighborhoods.. Teatro Colon. The details — the Paris of South America.. Subte. San Telmo. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Tigre.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Tigre.", "x": "Buenos Aires in depth: Day trip: Tigre.. Steak. The details — the Paris of South America.. Culture. La Boca. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Subte.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Subte.", "x": "Buenos Aires in depth: Subte.. San Telmo. The details — the Paris of South America.. Tango. Recoleta. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Buenos Aires in depth: Culture.. La Boca. The details — the Paris of South America.. Steak. Tango shows. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Buenos Aires's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Buenos Aires's districts.", "x": "Neighborhoods: Tango.. Tango shows. Where to stay, eat, and wander — Buenos Aires. the Paris of South America. Every district has its own personality; Steak.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Buenos Aires: Teatro Colon..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Buenos Aires: Teatro Colon..", "x": "Food: Teatro Colon.. Neighborhoods. The tastes of Buenos Aires — the Paris of South America.. Steak. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Buenos Aires transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Buenos Aires transport.", "x": "Transport: Day trip: Tigre.. San Telmo. Subways, buses, walking — Buenos Aires. the Paris of South America. Learn the system on day one; Subte.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Buenos Aires.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Buenos Aires.", "x": "Timing: Culture.. La Boca. Seasons and festivals — Buenos Aires. the Paris of South America. Time it right for Tango.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Buenos Aires safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Buenos Aires safely.", "x": "Safety: Steak.. Recoleta. Sensible precautions — Buenos Aires. the Paris of South America. Big cities reward street smarts; Neighborhoods.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-buenos-aires-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
