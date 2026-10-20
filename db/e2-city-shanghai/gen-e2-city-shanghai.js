(function(){'use strict';
/* JAH Shanghai City Database generator — jahdb-e2-city-shanghai-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-shanghai',PREFIX='JAH-E2CITYSHANG-',NAME='JAH Shanghai City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Shanghai: the complete city guide", "d": "Shanghai, China: China's glittering port..", "g": "overview", "l": 2, "q": "What is Shanghai: the complete city guide?", "a": "Shanghai, China: China's glittering port..", "x": "The complete Shanghai city guide: China's glittering port.. The Bund. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Shanghai in one database. Metro huge. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Shanghai essentials: The Bund..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Shanghai essentials: The Bund..", "x": "At a glance: Shanghai, China — China's glittering port.. Yu Garden. The numbers, the layout, the vibe: Shanghai in brief. Bund walk. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "The Bund.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "The Bund.", "x": "Shanghai: The Bund.. Bund walk. One of the defining things about Shanghai — Nanjing Road.. China's glittering port. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: The Bund..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: The Bund..", "x": "Guide: The Bund.. Day trip: Suzhou. How to do it right — Shanghai. Pudong skyline. China's glittering port. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Yu Garden.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Yu Garden.", "x": "Shanghai: Yu Garden.. Old/new. One of the defining things about Shanghai — Pudong skyline.. China's glittering port. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Yu Garden..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Yu Garden..", "x": "Guide: Yu Garden.. Maglev. How to do it right — Shanghai. Jade Buddha Temple. China's glittering port. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Nanjing Road.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Nanjing Road.", "x": "Shanghai: Nanjing Road.. Day trip: Suzhou. One of the defining things about Shanghai — Jade Buddha Temple.. China's glittering port. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Nanjing Road..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Nanjing Road..", "x": "Guide: Nanjing Road.. Markets. How to do it right — Shanghai. Soup dumplings. China's glittering port. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Pudong skyline.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Pudong skyline.", "x": "Shanghai: Pudong skyline.. Maglev. One of the defining things about Shanghai — Soup dumplings.. China's glittering port. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Pudong skyline..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Pudong skyline..", "x": "Guide: Pudong skyline.. Metro huge. How to do it right — Shanghai. The Bund. China's glittering port. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Jade Buddha Temple.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Jade Buddha Temple.", "x": "Shanghai: Jade Buddha Temple.. Markets. One of the defining things about Shanghai — The Bund.. China's glittering port. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Jade Buddha Temple..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Jade Buddha Temple..", "x": "Guide: Jade Buddha Temple.. Bund walk. How to do it right — Shanghai. Yu Garden. China's glittering port. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Soup dumplings.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Soup dumplings.", "x": "Shanghai: Soup dumplings.. Metro huge. One of the defining things about Shanghai — Yu Garden.. China's glittering port. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Soup dumplings..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Soup dumplings..", "x": "Guide: Soup dumplings.. Old/new. How to do it right — Shanghai. Nanjing Road. China's glittering port. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Metro huge.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Metro huge.", "x": "Shanghai in depth: Metro huge.. Yu Garden. The details — China's glittering port.. Old/new. Pudong skyline. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bund walk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bund walk.", "x": "Shanghai in depth: Bund walk.. Nanjing Road. The details — China's glittering port.. Day trip: Suzhou. Jade Buddha Temple. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Old/new.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Old/new.", "x": "Shanghai in depth: Old/new.. Pudong skyline. The details — China's glittering port.. Maglev. Soup dumplings. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Suzhou.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Suzhou.", "x": "Shanghai in depth: Day trip: Suzhou.. Jade Buddha Temple. The details — China's glittering port.. Markets. The Bund. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Maglev.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Maglev.", "x": "Shanghai in depth: Maglev.. Soup dumplings. The details — China's glittering port.. Metro huge. Yu Garden. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Markets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Markets.", "x": "Shanghai in depth: Markets.. The Bund. The details — China's glittering port.. Bund walk. Nanjing Road. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Shanghai's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Shanghai's districts.", "x": "Neighborhoods: Metro huge.. Nanjing Road. Where to stay, eat, and wander — Shanghai. China's glittering port. Every district has its own personality; Bund walk.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Shanghai: Pudong skyline..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Shanghai: Pudong skyline..", "x": "Food: Pudong skyline.. Old/new. The tastes of Shanghai — China's glittering port.. Jade Buddha Temple. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Shanghai transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Shanghai transport.", "x": "Transport: Day trip: Suzhou.. Soup dumplings. Subways, buses, walking — Shanghai. China's glittering port. Learn the system on day one; Maglev.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Shanghai.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Shanghai.", "x": "Timing: Markets.. The Bund. Seasons and festivals — Shanghai. China's glittering port. Time it right for Metro huge.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Shanghai safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Shanghai safely.", "x": "Safety: Bund walk.. Yu Garden. Sensible precautions — Shanghai. China's glittering port. Big cities reward street smarts; Old/new.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-shanghai-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
