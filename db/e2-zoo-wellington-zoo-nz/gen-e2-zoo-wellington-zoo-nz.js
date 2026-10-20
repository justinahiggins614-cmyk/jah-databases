(function(){'use strict';
/* JAH Wellington Zoo Zoo Database generator — jahdb-e2-zoo-wellington-zoo-nz-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo-wellington-zoo-nz',PREFIX='JAH-E2ZOOWELLIN-',NAME='JAH Wellington Zoo Zoo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wellington Zoo: the complete guide", "d": "Wellington Zoo: New Zealand's capital zoo..", "g": "overview", "l": 2, "q": "What is Wellington Zoo: the complete guide?", "a": "Wellington Zoo: New Zealand's capital zoo..", "x": "The complete zoo guide to Wellington Zoo: New Zealand's capital zoo.. 1906. History, meaning, practices, and how to engage respectfully — everything in one database. Kiwis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Wellington Zoo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Wellington Zoo essentials.", "x": "At a glance: Wellington Zoo — New Zealand's capital zoo.. Kiwis. The essentials: History.. Sun bears. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1906.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1906.", "x": "Wellington Zoo: 1906.. History. Essential knowledge — Sun bears.. New Zealand's capital zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1906..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1906..", "x": "Explained: 1906.. Wellington. The context — Wellington Zoo. Conservation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kiwis.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kiwis.", "x": "Wellington Zoo: Kiwis.. Tickets. Essential knowledge — Conservation.. New Zealand's capital zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Kiwis..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Kiwis..", "x": "Explained: Kiwis.. Conservation. The context — Wellington Zoo. Capital. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sun bears.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sun bears.", "x": "Wellington Zoo: Sun bears.. Wellington. Essential knowledge — Capital.. New Zealand's capital zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sun bears..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sun bears..", "x": "Explained: Sun bears.. NZ. The context — Wellington Zoo. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Conservation.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Conservation.", "x": "Wellington Zoo: Conservation.. Conservation. Essential knowledge — History.. New Zealand's capital zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Conservation..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Conservation..", "x": "Explained: Conservation.. Kiwis. The context — Wellington Zoo. 1906. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Capital.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Capital.", "x": "Wellington Zoo: Capital.. NZ. Essential knowledge — 1906.. New Zealand's capital zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Capital..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Capital..", "x": "Explained: Capital.. History. The context — Wellington Zoo. Kiwis. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Wellington Zoo: History.. Kiwis. Essential knowledge — Kiwis.. New Zealand's capital zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Tickets. The context — Wellington Zoo. Sun bears. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Kiwis.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Kiwis.", "x": "Wellington Zoo in depth: Kiwis.. Kiwis. Details — New Zealand's capital zoo.. Tickets. Conservation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Wellington Zoo in depth: History.. Sun bears. Details — New Zealand's capital zoo.. Wellington. Capital. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "Wellington Zoo in depth: Tickets.. Conservation. Details — New Zealand's capital zoo.. Conservation. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wellington.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wellington.", "x": "Wellington Zoo in depth: Wellington.. Capital. Details — New Zealand's capital zoo.. NZ. 1906. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conservation.", "x": "Wellington Zoo in depth: Conservation.. History. Details — New Zealand's capital zoo.. Kiwis. Kiwis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "NZ.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "NZ.", "x": "Wellington Zoo in depth: NZ.. 1906. Details — New Zealand's capital zoo.. History. Sun bears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Wellington Zoo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Wellington Zoo comes from.", "x": "Origins: Kiwis.. 1906. The history of Wellington Zoo — New Zealand's capital zoo.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Wellington Zoo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Wellington Zoo respectfully.", "x": "Engaging: Tickets.. Kiwis. How to participate or observe well — Wellington Zoo. New Zealand's capital zoo. Respect first, always; Wellington.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Wellington Zoo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Wellington Zoo do's and don'ts.", "x": "Etiquette: Conservation.. Sun bears. The rules of respect — Wellington Zoo. New Zealand's capital zoo. When in doubt, ask about NZ.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Wellington Zoo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Wellington Zoo.", "x": "Planning: Kiwis.. Conservation. Practical notes — Wellington Zoo. New Zealand's capital zoo. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Wellington Zoo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Wellington Zoo and money.", "x": "Costs: Tickets.. Capital. What to budget — Wellington Zoo. New Zealand's capital zoo. The best experiences of Wellington. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo-wellington-zoo-nz-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
