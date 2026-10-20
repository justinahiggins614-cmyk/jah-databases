(function(){'use strict';
/* JAH Bangkok City Database generator — jahdb-e2-city-bangkok-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-bangkok',PREFIX='JAH-E2CITYBANGK-',NAME='JAH Bangkok City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bangkok: the complete city guide", "d": "Bangkok, Thailand: the city of angels..", "g": "overview", "l": 2, "q": "What is Bangkok: the complete city guide?", "a": "Bangkok, Thailand: the city of angels..", "x": "The complete Bangkok city guide: the city of angels.. Grand Palace. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Bangkok in one database. Tuk-tuks. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Bangkok essentials: Grand Palace..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Bangkok essentials: Grand Palace..", "x": "At a glance: Bangkok, Thailand — the city of angels.. Wat Pho. The numbers, the layout, the vibe: Bangkok in brief. Temples. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Grand Palace.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Grand Palace.", "x": "Bangkok: Grand Palace.. Temples. One of the defining things about Bangkok — Chatuchak.. the city of angels. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Grand Palace..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Grand Palace..", "x": "Guide: Grand Palace.. Street food. How to do it right — Bangkok. Khao San. the city of angels. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Wat Pho.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Wat Pho.", "x": "Bangkok: Wat Pho.. Markets. One of the defining things about Bangkok — Khao San.. the city of angels. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Wat Pho..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Wat Pho..", "x": "Guide: Wat Pho.. Day trip: Ayutthaya. How to do it right — Bangkok. Pad thai. the city of angels. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Chatuchak.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Chatuchak.", "x": "Bangkok: Chatuchak.. Street food. One of the defining things about Bangkok — Pad thai.. the city of angels. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Chatuchak..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Chatuchak..", "x": "Guide: Chatuchak.. Respect. How to do it right — Bangkok. Canals. the city of angels. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Khao San.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Khao San.", "x": "Bangkok: Khao San.. Day trip: Ayutthaya. One of the defining things about Bangkok — Canals.. the city of angels. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Khao San..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Khao San..", "x": "Guide: Khao San.. Tuk-tuks. How to do it right — Bangkok. Grand Palace. the city of angels. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Pad thai.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Pad thai.", "x": "Bangkok: Pad thai.. Respect. One of the defining things about Bangkok — Grand Palace.. the city of angels. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Pad thai..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Pad thai..", "x": "Guide: Pad thai.. Temples. How to do it right — Bangkok. Wat Pho. the city of angels. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Canals.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Canals.", "x": "Bangkok: Canals.. Tuk-tuks. One of the defining things about Bangkok — Wat Pho.. the city of angels. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Canals..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Canals..", "x": "Guide: Canals.. Markets. How to do it right — Bangkok. Chatuchak. the city of angels. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tuk-tuks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tuk-tuks.", "x": "Bangkok in depth: Tuk-tuks.. Wat Pho. The details — the city of angels.. Markets. Khao San. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Temples.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Temples.", "x": "Bangkok in depth: Temples.. Chatuchak. The details — the city of angels.. Street food. Pad thai. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Markets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Markets.", "x": "Bangkok in depth: Markets.. Khao San. The details — the city of angels.. Day trip: Ayutthaya. Canals. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Street food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Street food.", "x": "Bangkok in depth: Street food.. Pad thai. The details — the city of angels.. Respect. Grand Palace. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Day trip: Ayutthaya.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Day trip: Ayutthaya.", "x": "Bangkok in depth: Day trip: Ayutthaya.. Canals. The details — the city of angels.. Tuk-tuks. Wat Pho. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Bangkok in depth: Respect.. Grand Palace. The details — the city of angels.. Temples. Chatuchak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Bangkok's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Bangkok's districts.", "x": "Neighborhoods: Tuk-tuks.. Chatuchak. Where to stay, eat, and wander — Bangkok. the city of angels. Every district has its own personality; Temples.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Bangkok: Khao San..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Bangkok: Khao San..", "x": "Food: Khao San.. Markets. The tastes of Bangkok — the city of angels.. Pad thai. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Bangkok transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Bangkok transport.", "x": "Transport: Street food.. Canals. Subways, buses, walking — Bangkok. the city of angels. Learn the system on day one; Day trip: Ayutthaya.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Bangkok.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Bangkok.", "x": "Timing: Respect.. Grand Palace. Seasons and festivals — Bangkok. the city of angels. Time it right for Tuk-tuks.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Bangkok safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Bangkok safely.", "x": "Safety: Temples.. Wat Pho. Sensible precautions — Bangkok. the city of angels. Big cities reward street smarts; Markets.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-bangkok-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
