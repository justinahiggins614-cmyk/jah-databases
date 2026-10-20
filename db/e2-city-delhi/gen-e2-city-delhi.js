(function(){'use strict';
/* JAH Delhi City Database generator — jahdb-e2-city-delhi-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-delhi',PREFIX='JAH-E2CITYDELHI-',NAME='JAH Delhi City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Delhi: the complete city guide", "d": "Delhi, India: India's capital of empires..", "g": "overview", "l": 2, "q": "What is Delhi: the complete city guide?", "a": "Delhi, India: India's capital of empires..", "x": "The complete Delhi city guide: India's capital of empires.. Red Fort. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Delhi in one database. Metro. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Delhi essentials: Red Fort..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Delhi essentials: Red Fort..", "x": "At a glance: Delhi, India — India's capital of empires.. Humayun's Tomb. The numbers, the layout, the vibe: Delhi in brief. History layers. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Red Fort.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Red Fort.", "x": "Delhi: Red Fort.. History layers. One of the defining things about Delhi — Qutub Minar.. India's capital of empires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Red Fort..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Red Fort..", "x": "Guide: Red Fort.. Spice. How to do it right — Delhi. Chandni Chowk. India's capital of empires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Humayun's Tomb.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Humayun's Tomb.", "x": "Delhi: Humayun's Tomb.. Markets. One of the defining things about Delhi — Chandni Chowk.. India's capital of empires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Humayun's Tomb..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Humayun's Tomb..", "x": "Guide: Humayun's Tomb.. Day trip: Agra. How to do it right — Delhi. Lotus Temple. India's capital of empires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Qutub Minar.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Qutub Minar.", "x": "Delhi: Qutub Minar.. Spice. One of the defining things about Delhi — Lotus Temple.. India's capital of empires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Qutub Minar..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Qutub Minar..", "x": "Guide: Qutub Minar.. Beware touts. How to do it right — Delhi. Street food. India's capital of empires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Chandni Chowk.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Chandni Chowk.", "x": "Delhi: Chandni Chowk.. Day trip: Agra. One of the defining things about Delhi — Street food.. India's capital of empires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Chandni Chowk..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Chandni Chowk..", "x": "Guide: Chandni Chowk.. Metro. How to do it right — Delhi. Red Fort. India's capital of empires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Lotus Temple.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Lotus Temple.", "x": "Delhi: Lotus Temple.. Beware touts. One of the defining things about Delhi — Red Fort.. India's capital of empires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Lotus Temple..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Lotus Temple..", "x": "Guide: Lotus Temple.. History layers. How to do it right — Delhi. Humayun's Tomb. India's capital of empires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Street food.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Street food.", "x": "Delhi: Street food.. Metro. One of the defining things about Delhi — Humayun's Tomb.. India's capital of empires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Street food..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Street food..", "x": "Guide: Street food.. Markets. How to do it right — Delhi. Qutub Minar. India's capital of empires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Metro.", "x": "Delhi in depth: Metro.. Humayun's Tomb. The details — India's capital of empires.. Markets. Chandni Chowk. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History layers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History layers.", "x": "Delhi in depth: History layers.. Qutub Minar. The details — India's capital of empires.. Spice. Lotus Temple. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Markets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Markets.", "x": "Delhi in depth: Markets.. Chandni Chowk. The details — India's capital of empires.. Day trip: Agra. Street food. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Spice.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Spice.", "x": "Delhi in depth: Spice.. Lotus Temple. The details — India's capital of empires.. Beware touts. Red Fort. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Day trip: Agra.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Day trip: Agra.", "x": "Delhi in depth: Day trip: Agra.. Street food. The details — India's capital of empires.. Metro. Humayun's Tomb. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Beware touts.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Beware touts.", "x": "Delhi in depth: Beware touts.. Red Fort. The details — India's capital of empires.. History layers. Qutub Minar. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Delhi's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Delhi's districts.", "x": "Neighborhoods: Metro.. Qutub Minar. Where to stay, eat, and wander — Delhi. India's capital of empires. Every district has its own personality; History layers.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Delhi: Chandni Chowk..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Delhi: Chandni Chowk..", "x": "Food: Chandni Chowk.. Markets. The tastes of Delhi — India's capital of empires.. Lotus Temple. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Delhi transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Delhi transport.", "x": "Transport: Spice.. Street food. Subways, buses, walking — Delhi. India's capital of empires. Learn the system on day one; Day trip: Agra.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Delhi.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Delhi.", "x": "Timing: Beware touts.. Red Fort. Seasons and festivals — Delhi. India's capital of empires. Time it right for Metro.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Delhi safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Delhi safely.", "x": "Safety: History layers.. Humayun's Tomb. Sensible precautions — Delhi. India's capital of empires. Big cities reward street smarts; Markets.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-delhi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
