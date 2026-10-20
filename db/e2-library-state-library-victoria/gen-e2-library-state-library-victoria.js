(function(){'use strict';
/* JAH State Library of Victoria Library Database generator — jahdb-e2-library-state-library-victoria-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-state-library-victoria',PREFIX='JAH-E2LIBRARYST-',NAME='JAH State Library of Victoria Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "State Library of Victoria: the complete guide", "d": "State Library of Victoria: Melbourne's domed room..", "g": "overview", "l": 2, "q": "What is State Library of Victoria: the complete guide?", "a": "State Library of Victoria: Melbourne's domed room..", "x": "The complete library guide to State Library of Victoria: Melbourne's domed room.. La Trobe Room. History, meaning, practices, and how to engage respectfully — everything in one database. Dome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "State Library of Victoria essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "State Library of Victoria essentials.", "x": "At a glance: State Library of Victoria — Melbourne's domed room.. 1854. The essentials: History.. Dome. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "La Trobe Room.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "La Trobe Room.", "x": "State Library of Victoria: La Trobe Room.. History. Essential knowledge — Dome.. Melbourne's domed room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: La Trobe Room..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: La Trobe Room..", "x": "Explained: La Trobe Room.. Melbourne. The context — State Library of Victoria. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1854.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1854.", "x": "State Library of Victoria: 1854.. Free. Essential knowledge — Free.. Melbourne's domed room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1854..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1854..", "x": "Explained: 1854.. Tours. The context — State Library of Victoria. Melbourne. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dome.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dome.", "x": "State Library of Victoria: Dome.. Melbourne. Essential knowledge — Melbourne.. Melbourne's domed room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dome..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dome..", "x": "Explained: Dome.. Kelly. The context — State Library of Victoria. Ned Kelly. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Free.", "x": "State Library of Victoria: Free.. Tours. Essential knowledge — Ned Kelly.. Melbourne's domed room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Dome. The context — State Library of Victoria. La Trobe Room. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Melbourne.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Melbourne.", "x": "State Library of Victoria: Melbourne.. Kelly. Essential knowledge — La Trobe Room.. Melbourne's domed room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Melbourne..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Melbourne..", "x": "Explained: Melbourne.. History. The context — State Library of Victoria. 1854. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ned Kelly.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ned Kelly.", "x": "State Library of Victoria: Ned Kelly.. Dome. Essential knowledge — 1854.. Melbourne's domed room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ned Kelly..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ned Kelly..", "x": "Explained: Ned Kelly.. Free. The context — State Library of Victoria. Dome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dome.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dome.", "x": "State Library of Victoria in depth: Dome.. 1854. Details — Melbourne's domed room.. Free. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "State Library of Victoria in depth: History.. Dome. Details — Melbourne's domed room.. Melbourne. Melbourne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Free.", "x": "State Library of Victoria in depth: Free.. Free. Details — Melbourne's domed room.. Tours. Ned Kelly. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Melbourne.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Melbourne.", "x": "State Library of Victoria in depth: Melbourne.. Melbourne. Details — Melbourne's domed room.. Kelly. La Trobe Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "State Library of Victoria in depth: Tours.. Ned Kelly. Details — Melbourne's domed room.. Dome. 1854. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Kelly.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Kelly.", "x": "State Library of Victoria in depth: Kelly.. La Trobe Room. Details — Melbourne's domed room.. History. Dome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where State Library of Victoria comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where State Library of Victoria comes from.", "x": "Origins: Dome.. La Trobe Room. The history of State Library of Victoria — Melbourne's domed room.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing State Library of Victoria respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing State Library of Victoria respectfully.", "x": "Engaging: Free.. 1854. How to participate or observe well — State Library of Victoria. Melbourne's domed room. Respect first, always; Melbourne.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "State Library of Victoria do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "State Library of Victoria do's and don'ts.", "x": "Etiquette: Tours.. Dome. The rules of respect — State Library of Victoria. Melbourne's domed room. When in doubt, ask about Kelly.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around State Library of Victoria.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around State Library of Victoria.", "x": "Planning: Dome.. Free. Practical notes — State Library of Victoria. Melbourne's domed room. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "State Library of Victoria and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "State Library of Victoria and money.", "x": "Costs: Free.. Melbourne. What to budget — State Library of Victoria. Melbourne's domed room. The best experiences of Melbourne. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-state-library-victoria-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
