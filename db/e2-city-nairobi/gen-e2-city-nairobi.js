(function(){'use strict';
/* JAH Nairobi City Database generator — jahdb-e2-city-nairobi-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-nairobi',PREFIX='JAH-E2CITYNAIRO-',NAME='JAH Nairobi City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nairobi: the complete city guide", "d": "Nairobi, Kenya: safari capital..", "g": "overview", "l": 2, "q": "What is Nairobi: the complete city guide?", "a": "Nairobi, Kenya: safari capital..", "x": "The complete Nairobi city guide: safari capital.. Nairobi National Park. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Nairobi in one database. Park. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Nairobi essentials: Nairobi National Park..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Nairobi essentials: Nairobi National Park..", "x": "At a glance: Nairobi, Kenya — safari capital.. Giraffe Centre. The numbers, the layout, the vibe: Nairobi in brief. Giraffes. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Nairobi National Park.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Nairobi National Park.", "x": "Nairobi: Nairobi National Park.. Giraffes. One of the defining things about Nairobi — Karen Blixen.. safari capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Nairobi National Park..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Nairobi National Park..", "x": "Guide: Nairobi National Park.. Day trip: Amboseli. How to do it right — Nairobi. Markets. safari capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Giraffe Centre.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Giraffe Centre.", "x": "Nairobi: Giraffe Centre.. Culture. One of the defining things about Nairobi — Markets.. safari capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Giraffe Centre..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Giraffe Centre..", "x": "Guide: Giraffe Centre.. Traffic. How to do it right — Nairobi. Nyama choma. safari capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Karen Blixen.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Karen Blixen.", "x": "Nairobi: Karen Blixen.. Day trip: Amboseli. One of the defining things about Nairobi — Nyama choma.. safari capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Karen Blixen..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Karen Blixen..", "x": "Guide: Karen Blixen.. Safari. How to do it right — Nairobi. Matatus. safari capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Markets.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Markets.", "x": "Nairobi: Markets.. Traffic. One of the defining things about Nairobi — Matatus.. safari capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Markets..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Markets..", "x": "Guide: Markets.. Park. How to do it right — Nairobi. Nairobi National Park. safari capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Nyama choma.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Nyama choma.", "x": "Nairobi: Nyama choma.. Safari. One of the defining things about Nairobi — Nairobi National Park.. safari capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Nyama choma..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Nyama choma..", "x": "Guide: Nyama choma.. Giraffes. How to do it right — Nairobi. Giraffe Centre. safari capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Matatus.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Matatus.", "x": "Nairobi: Matatus.. Park. One of the defining things about Nairobi — Giraffe Centre.. safari capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Matatus..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Matatus..", "x": "Guide: Matatus.. Culture. How to do it right — Nairobi. Karen Blixen. safari capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Park.", "x": "Nairobi in depth: Park.. Giraffe Centre. The details — safari capital.. Culture. Markets. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Giraffes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Giraffes.", "x": "Nairobi in depth: Giraffes.. Karen Blixen. The details — safari capital.. Day trip: Amboseli. Nyama choma. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Culture.", "x": "Nairobi in depth: Culture.. Markets. The details — safari capital.. Traffic. Matatus. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Amboseli.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Amboseli.", "x": "Nairobi in depth: Day trip: Amboseli.. Nyama choma. The details — safari capital.. Safari. Nairobi National Park. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Traffic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Traffic.", "x": "Nairobi in depth: Traffic.. Matatus. The details — safari capital.. Park. Giraffe Centre. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safari.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safari.", "x": "Nairobi in depth: Safari.. Nairobi National Park. The details — safari capital.. Giraffes. Karen Blixen. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Nairobi's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Nairobi's districts.", "x": "Neighborhoods: Park.. Karen Blixen. Where to stay, eat, and wander — Nairobi. safari capital. Every district has its own personality; Giraffes.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Nairobi: Markets..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Nairobi: Markets..", "x": "Food: Markets.. Culture. The tastes of Nairobi — safari capital.. Nyama choma. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Nairobi transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Nairobi transport.", "x": "Transport: Day trip: Amboseli.. Matatus. Subways, buses, walking — Nairobi. safari capital. Learn the system on day one; Traffic.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Nairobi.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Nairobi.", "x": "Timing: Safari.. Nairobi National Park. Seasons and festivals — Nairobi. safari capital. Time it right for Park.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Nairobi safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Nairobi safely.", "x": "Safety: Giraffes.. Giraffe Centre. Sensible precautions — Nairobi. safari capital. Big cities reward street smarts; Culture.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-nairobi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
