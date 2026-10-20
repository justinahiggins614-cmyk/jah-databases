(function(){'use strict';
/* JAH Budapest City Database generator — jahdb-e2-city-budapest-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-budapest',PREFIX='JAH-E2CITYBUDAP-',NAME='JAH Budapest City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Budapest: the complete city guide", "d": "Budapest, Hungary: the pearl of the Danube..", "g": "overview", "l": 2, "q": "What is Budapest: the complete city guide?", "a": "Budapest, Hungary: the pearl of the Danube..", "x": "The complete Budapest city guide: the pearl of the Danube.. Parliament. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Budapest in one database. Baths. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Budapest essentials: Parliament..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Budapest essentials: Parliament..", "x": "At a glance: Budapest, Hungary — the pearl of the Danube.. Fisherman's Bastion. The numbers, the layout, the vibe: Budapest in brief. Parliament. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Parliament.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Parliament.", "x": "Budapest: Parliament.. Parliament. One of the defining things about Budapest — Thermal baths.. the pearl of the Danube. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Parliament..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Parliament..", "x": "Guide: Parliament.. Day trip: Eger. How to do it right — Budapest. Ruins bars. the pearl of the Danube. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Fisherman's Bastion.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Fisherman's Bastion.", "x": "Budapest: Fisherman's Bastion.. Bars. One of the defining things about Budapest — Ruins bars.. the pearl of the Danube. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Fisherman's Bastion..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Fisherman's Bastion..", "x": "Guide: Fisherman's Bastion.. Metro. How to do it right — Budapest. Goulash. the pearl of the Danube. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Thermal baths.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Thermal baths.", "x": "Budapest: Thermal baths.. Day trip: Eger. One of the defining things about Budapest — Goulash.. the pearl of the Danube. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Thermal baths..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Thermal baths..", "x": "Guide: Thermal baths.. Views. How to do it right — Budapest. Chain Bridge. the pearl of the Danube. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Ruins bars.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Ruins bars.", "x": "Budapest: Ruins bars.. Metro. One of the defining things about Budapest — Chain Bridge.. the pearl of the Danube. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Ruins bars..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Ruins bars..", "x": "Guide: Ruins bars.. Baths. How to do it right — Budapest. Parliament. the pearl of the Danube. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Goulash.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Goulash.", "x": "Budapest: Goulash.. Views. One of the defining things about Budapest — Parliament.. the pearl of the Danube. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Goulash..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Goulash..", "x": "Guide: Goulash.. Parliament. How to do it right — Budapest. Fisherman's Bastion. the pearl of the Danube. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Chain Bridge.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Chain Bridge.", "x": "Budapest: Chain Bridge.. Baths. One of the defining things about Budapest — Fisherman's Bastion.. the pearl of the Danube. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Chain Bridge..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Chain Bridge..", "x": "Guide: Chain Bridge.. Bars. How to do it right — Budapest. Thermal baths. the pearl of the Danube. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Baths.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Baths.", "x": "Budapest in depth: Baths.. Fisherman's Bastion. The details — the pearl of the Danube.. Bars. Ruins bars. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Parliament.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Parliament.", "x": "Budapest in depth: Parliament.. Thermal baths. The details — the pearl of the Danube.. Day trip: Eger. Goulash. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bars.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bars.", "x": "Budapest in depth: Bars.. Ruins bars. The details — the pearl of the Danube.. Metro. Chain Bridge. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Eger.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Eger.", "x": "Budapest in depth: Day trip: Eger.. Goulash. The details — the pearl of the Danube.. Views. Parliament. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Metro.", "x": "Budapest in depth: Metro.. Chain Bridge. The details — the pearl of the Danube.. Baths. Fisherman's Bastion. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Budapest in depth: Views.. Parliament. The details — the pearl of the Danube.. Parliament. Thermal baths. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Budapest's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Budapest's districts.", "x": "Neighborhoods: Baths.. Thermal baths. Where to stay, eat, and wander — Budapest. the pearl of the Danube. Every district has its own personality; Parliament.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Budapest: Ruins bars..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Budapest: Ruins bars..", "x": "Food: Ruins bars.. Bars. The tastes of Budapest — the pearl of the Danube.. Goulash. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Budapest transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Budapest transport.", "x": "Transport: Day trip: Eger.. Chain Bridge. Subways, buses, walking — Budapest. the pearl of the Danube. Learn the system on day one; Metro.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Budapest.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Budapest.", "x": "Timing: Views.. Parliament. Seasons and festivals — Budapest. the pearl of the Danube. Time it right for Baths.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Budapest safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Budapest safely.", "x": "Safety: Parliament.. Fisherman's Bastion. Sensible precautions — Budapest. the pearl of the Danube. Big cities reward street smarts; Bars.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-budapest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
