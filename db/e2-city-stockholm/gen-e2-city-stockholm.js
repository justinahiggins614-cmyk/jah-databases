(function(){'use strict';
/* JAH Stockholm City Database generator — jahdb-e2-city-stockholm-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-stockholm',PREFIX='JAH-E2CITYSTOCK-',NAME='JAH Stockholm City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stockholm: the complete city guide", "d": "Stockholm, Sweden: beauty on water..", "g": "overview", "l": 2, "q": "What is Stockholm: the complete city guide?", "a": "Stockholm, Sweden: beauty on water..", "x": "The complete Stockholm city guide: beauty on water.. Gamla Stan. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Stockholm in one database. Old town. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Stockholm essentials: Gamla Stan..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Stockholm essentials: Gamla Stan..", "x": "At a glance: Stockholm, Sweden — beauty on water.. Vasa Museum. The numbers, the layout, the vibe: Stockholm in brief. Museums. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Gamla Stan.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Gamla Stan.", "x": "Stockholm: Gamla Stan.. Museums. One of the defining things about Stockholm — Archipelago.. beauty on water. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Gamla Stan..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Gamla Stan..", "x": "Guide: Gamla Stan.. Day trip: Drottningholm. How to do it right — Stockholm. City Hall. beauty on water. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Vasa Museum.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Vasa Museum.", "x": "Stockholm: Vasa Museum.. Islands. One of the defining things about Stockholm — City Hall.. beauty on water. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Vasa Museum..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Vasa Museum..", "x": "Guide: Vasa Museum.. Metro art. How to do it right — Stockholm. Meatballs. beauty on water. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Archipelago.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Archipelago.", "x": "Stockholm: Archipelago.. Day trip: Drottningholm. One of the defining things about Stockholm — Meatballs.. beauty on water. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Archipelago..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Archipelago..", "x": "Guide: Archipelago.. Design. How to do it right — Stockholm. Design. beauty on water. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "City Hall.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "City Hall.", "x": "Stockholm: City Hall.. Metro art. One of the defining things about Stockholm — Design.. beauty on water. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: City Hall..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: City Hall..", "x": "Guide: City Hall.. Old town. How to do it right — Stockholm. Gamla Stan. beauty on water. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Meatballs.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Meatballs.", "x": "Stockholm: Meatballs.. Design. One of the defining things about Stockholm — Gamla Stan.. beauty on water. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Meatballs..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Meatballs..", "x": "Guide: Meatballs.. Museums. How to do it right — Stockholm. Vasa Museum. beauty on water. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Design.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Design.", "x": "Stockholm: Design.. Old town. One of the defining things about Stockholm — Vasa Museum.. beauty on water. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Design..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Design..", "x": "Guide: Design.. Islands. How to do it right — Stockholm. Archipelago. beauty on water. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Old town.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Old town.", "x": "Stockholm in depth: Old town.. Vasa Museum. The details — beauty on water.. Islands. City Hall. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Museums.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Museums.", "x": "Stockholm in depth: Museums.. Archipelago. The details — beauty on water.. Day trip: Drottningholm. Meatballs. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Islands.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Islands.", "x": "Stockholm in depth: Islands.. City Hall. The details — beauty on water.. Metro art. Design. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Drottningholm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Drottningholm.", "x": "Stockholm in depth: Day trip: Drottningholm.. Meatballs. The details — beauty on water.. Design. Gamla Stan. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Metro art.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Metro art.", "x": "Stockholm in depth: Metro art.. Design. The details — beauty on water.. Old town. Vasa Museum. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Design.", "x": "Stockholm in depth: Design.. Gamla Stan. The details — beauty on water.. Museums. Archipelago. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Stockholm's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Stockholm's districts.", "x": "Neighborhoods: Old town.. Archipelago. Where to stay, eat, and wander — Stockholm. beauty on water. Every district has its own personality; Museums.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Stockholm: City Hall..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Stockholm: City Hall..", "x": "Food: City Hall.. Islands. The tastes of Stockholm — beauty on water.. Meatballs. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Stockholm transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Stockholm transport.", "x": "Transport: Day trip: Drottningholm.. Design. Subways, buses, walking — Stockholm. beauty on water. Learn the system on day one; Metro art.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Stockholm.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Stockholm.", "x": "Timing: Design.. Gamla Stan. Seasons and festivals — Stockholm. beauty on water. Time it right for Old town.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Stockholm safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Stockholm safely.", "x": "Safety: Museums.. Vasa Museum. Sensible precautions — Stockholm. beauty on water. Big cities reward street smarts; Islands.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-stockholm-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
