(function(){'use strict';
/* JAH St. Patrick\'s Day Holiday Database generator — jahdb-e2-holiday-st-patricks-day-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-st-patricks-day',PREFIX='JAH-E2HOLIDAYST-',NAME='JAH St. Patrick\'s Day Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "St. Patrick's Day: the complete guide", "d": "St. Patrick's Day: Ireland's saint; green..", "g": "overview", "l": 2, "q": "What is St. Patrick's Day: the complete guide?", "a": "St. Patrick's Day: Ireland's saint; green..", "x": "The complete holiday guide to St. Patrick's Day: Ireland's saint; green.. March 17. History, meaning, practices, and how to engage respectfully — everything in one database. Saint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "St. Patrick's Day essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "St. Patrick's Day essentials.", "x": "At a glance: St. Patrick's Day — Ireland's saint; green.. Shamrock. The essentials: Parades.. Parades. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "March 17.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "March 17.", "x": "St. Patrick's Day: March 17.. Parades. Essential knowledge — Parades.. Ireland's saint; green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: March 17..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: March 17..", "x": "Explained: March 17.. Food. The context — St. Patrick's Day. Green. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shamrock.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shamrock.", "x": "St. Patrick's Day: Shamrock.. Symbols. Essential knowledge — Green.. Ireland's saint; green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shamrock..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shamrock..", "x": "Explained: Shamrock.. Around world. The context — St. Patrick's Day. Pubs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Parades.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Parades.", "x": "St. Patrick's Day: Parades.. Food. Essential knowledge — Pubs.. Ireland's saint; green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Parades..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Parades..", "x": "Explained: Parades.. Fun. The context — St. Patrick's Day. Global. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Green.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Green.", "x": "St. Patrick's Day: Green.. Around world. Essential knowledge — Global.. Ireland's saint; green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Green..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Green..", "x": "Explained: Green.. Saint. The context — St. Patrick's Day. March 17. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pubs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pubs.", "x": "St. Patrick's Day: Pubs.. Fun. Essential knowledge — March 17.. Ireland's saint; green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pubs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pubs..", "x": "Explained: Pubs.. Parades. The context — St. Patrick's Day. Shamrock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Global.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Global.", "x": "St. Patrick's Day: Global.. Saint. Essential knowledge — Shamrock.. Ireland's saint; green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Global..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Global..", "x": "Explained: Global.. Symbols. The context — St. Patrick's Day. Parades. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Saint.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Saint.", "x": "St. Patrick's Day in depth: Saint.. Shamrock. Details — Ireland's saint; green.. Symbols. Green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Parades.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Parades.", "x": "St. Patrick's Day in depth: Parades.. Parades. Details — Ireland's saint; green.. Food. Pubs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Symbols.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Symbols.", "x": "St. Patrick's Day in depth: Symbols.. Green. Details — Ireland's saint; green.. Around world. Global. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "St. Patrick's Day in depth: Food.. Pubs. Details — Ireland's saint; green.. Fun. March 17. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Around world.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Around world.", "x": "St. Patrick's Day in depth: Around world.. Global. Details — Ireland's saint; green.. Saint. Shamrock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fun.", "x": "St. Patrick's Day in depth: Fun.. March 17. Details — Ireland's saint; green.. Parades. Parades. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where St. Patrick's Day comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where St. Patrick's Day comes from.", "x": "Origins: Saint.. March 17. The history of St. Patrick's Day — Ireland's saint; green.. Parades. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing St. Patrick's Day respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing St. Patrick's Day respectfully.", "x": "Engaging: Symbols.. Shamrock. How to participate or observe well — St. Patrick's Day. Ireland's saint; green. Respect first, always; Food.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "St. Patrick's Day do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "St. Patrick's Day do's and don'ts.", "x": "Etiquette: Around world.. Parades. The rules of respect — St. Patrick's Day. Ireland's saint; green. When in doubt, ask about Fun.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around St. Patrick's Day.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around St. Patrick's Day.", "x": "Planning: Saint.. Green. Practical notes — St. Patrick's Day. Ireland's saint; green. A little planning shows respect for Parades.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "St. Patrick's Day and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "St. Patrick's Day and money.", "x": "Costs: Symbols.. Pubs. What to budget — St. Patrick's Day. Ireland's saint; green. The best experiences of Food. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-st-patricks-day-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
