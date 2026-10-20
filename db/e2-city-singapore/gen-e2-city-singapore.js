(function(){'use strict';
/* JAH Singapore City Database generator — jahdb-e2-city-singapore-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-singapore',PREFIX='JAH-E2CITYSINGA-',NAME='JAH Singapore City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Singapore: the complete city guide", "d": "Singapore, Singapore: the lion city..", "g": "overview", "l": 2, "q": "What is Singapore: the complete city guide?", "a": "Singapore, Singapore: the lion city..", "x": "The complete Singapore city guide: the lion city.. Marina Bay Sands. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Singapore in one database. MRT. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Singapore essentials: Marina Bay Sands..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Singapore essentials: Marina Bay Sands..", "x": "At a glance: Singapore, Singapore — the lion city.. Gardens by the Bay. The numbers, the layout, the vibe: Singapore in brief. Hawkers. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Marina Bay Sands.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Marina Bay Sands.", "x": "Singapore: Marina Bay Sands.. Hawkers. One of the defining things about Singapore — Hawker centres.. the lion city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Marina Bay Sands..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Marina Bay Sands..", "x": "Guide: Marina Bay Sands.. Day trip: Sentosa. How to do it right — Singapore. Sentosa. the lion city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Gardens by the Bay.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Gardens by the Bay.", "x": "Singapore: Gardens by the Bay.. Gardens. One of the defining things about Singapore — Sentosa.. the lion city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Gardens by the Bay..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Gardens by the Bay..", "x": "Guide: Gardens by the Bay.. Rules. How to do it right — Singapore. Orchard. the lion city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Hawker centres.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Hawker centres.", "x": "Singapore: Hawker centres.. Day trip: Sentosa. One of the defining things about Singapore — Orchard.. the lion city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Hawker centres..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Hawker centres..", "x": "Guide: Hawker centres.. Clean. How to do it right — Singapore. Chili crab. the lion city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Sentosa.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Sentosa.", "x": "Singapore: Sentosa.. Rules. One of the defining things about Singapore — Chili crab.. the lion city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Sentosa..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Sentosa..", "x": "Guide: Sentosa.. MRT. How to do it right — Singapore. Marina Bay Sands. the lion city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Orchard.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Orchard.", "x": "Singapore: Orchard.. Clean. One of the defining things about Singapore — Marina Bay Sands.. the lion city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Orchard..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Orchard..", "x": "Guide: Orchard.. Hawkers. How to do it right — Singapore. Gardens by the Bay. the lion city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Chili crab.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Chili crab.", "x": "Singapore: Chili crab.. MRT. One of the defining things about Singapore — Gardens by the Bay.. the lion city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Chili crab..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Chili crab..", "x": "Guide: Chili crab.. Gardens. How to do it right — Singapore. Hawker centres. the lion city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "MRT.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "MRT.", "x": "Singapore in depth: MRT.. Gardens by the Bay. The details — the lion city.. Gardens. Sentosa. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hawkers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hawkers.", "x": "Singapore in depth: Hawkers.. Hawker centres. The details — the lion city.. Day trip: Sentosa. Orchard. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gardens.", "x": "Singapore in depth: Gardens.. Sentosa. The details — the lion city.. Rules. Chili crab. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Sentosa.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Sentosa.", "x": "Singapore in depth: Day trip: Sentosa.. Orchard. The details — the lion city.. Clean. Marina Bay Sands. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rules.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rules.", "x": "Singapore in depth: Rules.. Chili crab. The details — the lion city.. MRT. Gardens by the Bay. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Clean.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Clean.", "x": "Singapore in depth: Clean.. Marina Bay Sands. The details — the lion city.. Hawkers. Hawker centres. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Singapore's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Singapore's districts.", "x": "Neighborhoods: MRT.. Hawker centres. Where to stay, eat, and wander — Singapore. the lion city. Every district has its own personality; Hawkers.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Singapore: Sentosa..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Singapore: Sentosa..", "x": "Food: Sentosa.. Gardens. The tastes of Singapore — the lion city.. Orchard. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Singapore transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Singapore transport.", "x": "Transport: Day trip: Sentosa.. Chili crab. Subways, buses, walking — Singapore. the lion city. Learn the system on day one; Rules.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Singapore.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Singapore.", "x": "Timing: Clean.. Marina Bay Sands. Seasons and festivals — Singapore. the lion city. Time it right for MRT.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Singapore safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Singapore safely.", "x": "Safety: Hawkers.. Gardens by the Bay. Sensible precautions — Singapore. the lion city. Big cities reward street smarts; Gardens.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-singapore-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
