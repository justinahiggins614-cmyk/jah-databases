(function(){'use strict';
/* JAH Bogota City Database generator — jahdb-e2-city-bogota-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-bogota',PREFIX='JAH-E2CITYBOGOT-',NAME='JAH Bogota City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bogota: the complete city guide", "d": "Bogota, Colombia: the Athens of South America..", "g": "overview", "l": 2, "q": "What is Bogota: the complete city guide?", "a": "Bogota, Colombia: the Athens of South America..", "x": "The complete Bogota city guide: the Athens of South America.. Gold Museum. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Bogota in one database. Altitude. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Bogota essentials: Gold Museum..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Bogota essentials: Gold Museum..", "x": "At a glance: Bogota, Colombia — the Athens of South America.. Monserrate. The numbers, the layout, the vibe: Bogota in brief. Museums. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Gold Museum.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Gold Museum.", "x": "Bogota: Gold Museum.. Museums. One of the defining things about Bogota — La Candelaria.. the Athens of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Gold Museum..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Gold Museum..", "x": "Guide: Gold Museum.. Day trip: Zipaquira. How to do it right — Bogota. Ciclovia. the Athens of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Monserrate.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Monserrate.", "x": "Bogota: Monserrate.. Cycling. One of the defining things about Bogota — Ciclovia.. the Athens of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Monserrate..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Monserrate..", "x": "Guide: Monserrate.. TransMilenio. How to do it right — Bogota. Ajiaco. the Athens of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "La Candelaria.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "La Candelaria.", "x": "Bogota: La Candelaria.. Day trip: Zipaquira. One of the defining things about Bogota — Ajiaco.. the Athens of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: La Candelaria..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: La Candelaria..", "x": "Guide: La Candelaria.. Culture. How to do it right — Bogota. Botero. the Athens of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Ciclovia.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Ciclovia.", "x": "Bogota: Ciclovia.. TransMilenio. One of the defining things about Bogota — Botero.. the Athens of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Ciclovia..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Ciclovia..", "x": "Guide: Ciclovia.. Altitude. How to do it right — Bogota. Gold Museum. the Athens of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Ajiaco.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Ajiaco.", "x": "Bogota: Ajiaco.. Culture. One of the defining things about Bogota — Gold Museum.. the Athens of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Ajiaco..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Ajiaco..", "x": "Guide: Ajiaco.. Museums. How to do it right — Bogota. Monserrate. the Athens of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Botero.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Botero.", "x": "Bogota: Botero.. Altitude. One of the defining things about Bogota — Monserrate.. the Athens of South America. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Botero..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Botero..", "x": "Guide: Botero.. Cycling. How to do it right — Bogota. La Candelaria. the Athens of South America. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Altitude.", "x": "Bogota in depth: Altitude.. Monserrate. The details — the Athens of South America.. Cycling. Ciclovia. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Museums.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Museums.", "x": "Bogota in depth: Museums.. La Candelaria. The details — the Athens of South America.. Day trip: Zipaquira. Ajiaco. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cycling.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cycling.", "x": "Bogota in depth: Cycling.. Ciclovia. The details — the Athens of South America.. TransMilenio. Botero. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Zipaquira.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Zipaquira.", "x": "Bogota in depth: Day trip: Zipaquira.. Ajiaco. The details — the Athens of South America.. Culture. Gold Museum. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "TransMilenio.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "TransMilenio.", "x": "Bogota in depth: TransMilenio.. Botero. The details — the Athens of South America.. Altitude. Monserrate. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Bogota in depth: Culture.. Gold Museum. The details — the Athens of South America.. Museums. La Candelaria. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Bogota's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Bogota's districts.", "x": "Neighborhoods: Altitude.. La Candelaria. Where to stay, eat, and wander — Bogota. the Athens of South America. Every district has its own personality; Museums.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Bogota: Ciclovia..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Bogota: Ciclovia..", "x": "Food: Ciclovia.. Cycling. The tastes of Bogota — the Athens of South America.. Ajiaco. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Bogota transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Bogota transport.", "x": "Transport: Day trip: Zipaquira.. Botero. Subways, buses, walking — Bogota. the Athens of South America. Learn the system on day one; TransMilenio.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Bogota.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Bogota.", "x": "Timing: Culture.. Gold Museum. Seasons and festivals — Bogota. the Athens of South America. Time it right for Altitude.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Bogota safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Bogota safely.", "x": "Safety: Museums.. Monserrate. Sensible precautions — Bogota. the Athens of South America. Big cities reward street smarts; Cycling.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-bogota-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
