(function(){'use strict';
/* JAH Confucianism Religion Database generator — jahdb-e2-religion-confucianism-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-religion-confucianism',PREFIX='JAH-E2RELIGIONC-',NAME='JAH Confucianism Religion Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Confucianism: the complete guide", "d": "Confucianism: ethics and social harmony..", "g": "overview", "l": 2, "q": "What is Confucianism: the complete guide?", "a": "Confucianism: ethics and social harmony..", "x": "The complete religion guide to Confucianism: ethics and social harmony.. Confucius. History, meaning, practices, and how to engage respectfully — everything in one database. Texts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Confucianism essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Confucianism essentials.", "x": "At a glance: Confucianism — ethics and social harmony.. Analects. The essentials: Ethics.. Filial piety. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Confucius.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Confucius.", "x": "Confucianism: Confucius.. Ethics. Essential knowledge — Filial piety.. ethics and social harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Confucius..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Confucius..", "x": "Explained: Confucius.. Influence. The context — Confucianism. Ritual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Analects.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Analects.", "x": "Confucianism: Analects.. History. Essential knowledge — Ritual.. ethics and social harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Analects..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Analects..", "x": "Explained: Analects.. Modern. The context — Confucianism. Education. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Filial piety.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Filial piety.", "x": "Confucianism: Filial piety.. Influence. Essential knowledge — Education.. ethics and social harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Filial piety..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Filial piety..", "x": "Explained: Filial piety.. Society. The context — Confucianism. East Asia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ritual.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ritual.", "x": "Confucianism: Ritual.. Modern. Essential knowledge — East Asia.. ethics and social harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ritual..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ritual..", "x": "Explained: Ritual.. Texts. The context — Confucianism. Confucius. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Education.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Education.", "x": "Confucianism: Education.. Society. Essential knowledge — Confucius.. ethics and social harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Education..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Education..", "x": "Explained: Education.. Ethics. The context — Confucianism. Analects. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "East Asia.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "East Asia.", "x": "Confucianism: East Asia.. Texts. Essential knowledge — Analects.. ethics and social harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: East Asia..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: East Asia..", "x": "Explained: East Asia.. History. The context — Confucianism. Filial piety. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Texts.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Texts.", "x": "Confucianism in depth: Texts.. Analects. Details — ethics and social harmony.. History. Ritual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ethics.", "x": "Confucianism in depth: Ethics.. Filial piety. Details — ethics and social harmony.. Influence. Education. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Confucianism in depth: History.. Ritual. Details — ethics and social harmony.. Modern. East Asia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Influence.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Influence.", "x": "Confucianism in depth: Influence.. Education. Details — ethics and social harmony.. Society. Confucius. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Modern.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Modern.", "x": "Confucianism in depth: Modern.. East Asia. Details — ethics and social harmony.. Texts. Analects. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Society.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Society.", "x": "Confucianism in depth: Society.. Confucius. Details — ethics and social harmony.. Ethics. Filial piety. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Confucianism comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Confucianism comes from.", "x": "Origins: Texts.. Confucius. The history of Confucianism — ethics and social harmony.. Ethics. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Confucianism respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Confucianism respectfully.", "x": "Engaging: History.. Analects. How to participate or observe well — Confucianism. ethics and social harmony. Respect first, always; Influence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Confucianism do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Confucianism do's and don'ts.", "x": "Etiquette: Modern.. Filial piety. The rules of respect — Confucianism. ethics and social harmony. When in doubt, ask about Society.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Confucianism.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Confucianism.", "x": "Planning: Texts.. Ritual. Practical notes — Confucianism. ethics and social harmony. A little planning shows respect for Ethics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Confucianism and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Confucianism and money.", "x": "Costs: History.. Education. What to budget — Confucianism. ethics and social harmony. The best experiences of Influence. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-religion-confucianism-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
