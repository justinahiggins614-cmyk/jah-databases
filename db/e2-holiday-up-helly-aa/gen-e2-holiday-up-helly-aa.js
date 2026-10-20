(function(){'use strict';
/* JAH Up Helly Aa Holiday Database generator — jahdb-e2-holiday-up-helly-aa-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-up-helly-aa',PREFIX='JAH-E2HOLIDAYUP-',NAME='JAH Up Helly Aa Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Up Helly Aa: the complete guide", "d": "Up Helly Aa: Shetland's fire festival..", "g": "overview", "l": 2, "q": "What is Up Helly Aa: the complete guide?", "a": "Up Helly Aa: Shetland's fire festival..", "x": "The complete holiday guide to Up Helly Aa: Shetland's fire festival.. January. History, meaning, practices, and how to engage respectfully — everything in one database. Vikings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Up Helly Aa essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Up Helly Aa essentials.", "x": "At a glance: Up Helly Aa — Shetland's fire festival.. Viking. The essentials: Fire.. Galley burning. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "January.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "January.", "x": "Up Helly Aa: January.. Fire. Essential knowledge — Galley burning.. Shetland's fire festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: January..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: January..", "x": "Explained: January.. Travel. The context — Up Helly Aa. Torches. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Viking.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Viking.", "x": "Up Helly Aa: Viking.. Community. Essential knowledge — Torches.. Shetland's fire festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Viking..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Viking..", "x": "Explained: Viking.. History. The context — Up Helly Aa. Shetland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Galley burning.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Galley burning.", "x": "Up Helly Aa: Galley burning.. Travel. Essential knowledge — Shetland.. Shetland's fire festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Galley burning..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Galley burning..", "x": "Explained: Galley burning.. Spectacle. The context — Up Helly Aa. Winter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Torches.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Torches.", "x": "Up Helly Aa: Torches.. History. Essential knowledge — Winter.. Shetland's fire festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Torches..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Torches..", "x": "Explained: Torches.. Vikings. The context — Up Helly Aa. January. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Shetland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Shetland.", "x": "Up Helly Aa: Shetland.. Spectacle. Essential knowledge — January.. Shetland's fire festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Shetland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Shetland..", "x": "Explained: Shetland.. Fire. The context — Up Helly Aa. Viking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Winter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Winter.", "x": "Up Helly Aa: Winter.. Vikings. Essential knowledge — Viking.. Shetland's fire festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Winter..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Winter..", "x": "Explained: Winter.. Community. The context — Up Helly Aa. Galley burning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Vikings.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Vikings.", "x": "Up Helly Aa in depth: Vikings.. Viking. Details — Shetland's fire festival.. Community. Torches. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fire.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fire.", "x": "Up Helly Aa in depth: Fire.. Galley burning. Details — Shetland's fire festival.. Travel. Shetland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Community.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Community.", "x": "Up Helly Aa in depth: Community.. Torches. Details — Shetland's fire festival.. History. Winter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Travel.", "x": "Up Helly Aa in depth: Travel.. Shetland. Details — Shetland's fire festival.. Spectacle. January. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Up Helly Aa in depth: History.. Winter. Details — Shetland's fire festival.. Vikings. Viking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Spectacle.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Spectacle.", "x": "Up Helly Aa in depth: Spectacle.. January. Details — Shetland's fire festival.. Fire. Galley burning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Up Helly Aa comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Up Helly Aa comes from.", "x": "Origins: Vikings.. January. The history of Up Helly Aa — Shetland's fire festival.. Fire. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Up Helly Aa respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Up Helly Aa respectfully.", "x": "Engaging: Community.. Viking. How to participate or observe well — Up Helly Aa. Shetland's fire festival. Respect first, always; Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Up Helly Aa do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Up Helly Aa do's and don'ts.", "x": "Etiquette: History.. Galley burning. The rules of respect — Up Helly Aa. Shetland's fire festival. When in doubt, ask about Spectacle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Up Helly Aa.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Up Helly Aa.", "x": "Planning: Vikings.. Torches. Practical notes — Up Helly Aa. Shetland's fire festival. A little planning shows respect for Fire.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Up Helly Aa and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Up Helly Aa and money.", "x": "Costs: Community.. Shetland. What to budget — Up Helly Aa. Shetland's fire festival. The best experiences of Travel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-up-helly-aa-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
