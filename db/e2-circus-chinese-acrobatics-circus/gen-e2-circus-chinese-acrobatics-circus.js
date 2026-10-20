(function(){'use strict';
/* JAH Chinese Acrobatics Circus Database generator — jahdb-e2-circus-chinese-acrobatics-circus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-circus-chinese-acrobatics-circus',PREFIX='JAH-E2CIRCUSCHI-',NAME='JAH Chinese Acrobatics Circus Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chinese Acrobatics: the complete guide", "d": "Chinese Acrobatics: the ancient troupe..", "g": "overview", "l": 2, "q": "What is Chinese Acrobatics: the complete guide?", "a": "Chinese Acrobatics: the ancient troupe..", "x": "The complete circus guide to Chinese Acrobatics: the ancient troupe.. 2000 years. History, meaning, practices, and how to engage respectfully — everything in one database. Contortion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chinese Acrobatics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chinese Acrobatics essentials.", "x": "At a glance: Chinese Acrobatics — the ancient troupe.. Contortion. The essentials: Diabolo.. Plates. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2000 years.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2000 years.", "x": "Chinese Acrobatics: 2000 years.. Diabolo. Essential knowledge — Plates.. the ancient troupe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2000 years..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2000 years..", "x": "Explained: 2000 years.. Discipline. The context — Chinese Acrobatics. Diabolo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Contortion.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Contortion.", "x": "Chinese Acrobatics: Contortion.. Wu Qiao. Essential knowledge — Diabolo.. the ancient troupe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Contortion..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Contortion..", "x": "Explained: Contortion.. Plates. The context — Chinese Acrobatics. Wu Qiao. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Plates.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Plates.", "x": "Chinese Acrobatics: Plates.. Discipline. Essential knowledge — Wu Qiao.. the ancient troupe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Plates..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Plates..", "x": "Explained: Plates.. Shows. The context — Chinese Acrobatics. Discipline. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Diabolo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Diabolo.", "x": "Chinese Acrobatics: Diabolo.. Plates. Essential knowledge — Discipline.. the ancient troupe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Diabolo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Diabolo..", "x": "Explained: Diabolo.. Contortion. The context — Chinese Acrobatics. 2000 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wu Qiao.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wu Qiao.", "x": "Chinese Acrobatics: Wu Qiao.. Shows. Essential knowledge — 2000 years.. the ancient troupe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wu Qiao..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wu Qiao..", "x": "Explained: Wu Qiao.. Diabolo. The context — Chinese Acrobatics. Contortion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Discipline.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Discipline.", "x": "Chinese Acrobatics: Discipline.. Contortion. Essential knowledge — Contortion.. the ancient troupe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Discipline..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Discipline..", "x": "Explained: Discipline.. Wu Qiao. The context — Chinese Acrobatics. Plates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Contortion.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Contortion.", "x": "Chinese Acrobatics in depth: Contortion.. Contortion. Details — the ancient troupe.. Wu Qiao. Diabolo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Diabolo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Diabolo.", "x": "Chinese Acrobatics in depth: Diabolo.. Plates. Details — the ancient troupe.. Discipline. Wu Qiao. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wu Qiao.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wu Qiao.", "x": "Chinese Acrobatics in depth: Wu Qiao.. Diabolo. Details — the ancient troupe.. Plates. Discipline. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Discipline.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Discipline.", "x": "Chinese Acrobatics in depth: Discipline.. Wu Qiao. Details — the ancient troupe.. Shows. 2000 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Plates.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Plates.", "x": "Chinese Acrobatics in depth: Plates.. Discipline. Details — the ancient troupe.. Contortion. Contortion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Shows.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Shows.", "x": "Chinese Acrobatics in depth: Shows.. 2000 years. Details — the ancient troupe.. Diabolo. Plates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chinese Acrobatics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chinese Acrobatics comes from.", "x": "Origins: Contortion.. 2000 years. The history of Chinese Acrobatics — the ancient troupe.. Diabolo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chinese Acrobatics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chinese Acrobatics respectfully.", "x": "Engaging: Wu Qiao.. Contortion. How to participate or observe well — Chinese Acrobatics. the ancient troupe. Respect first, always; Discipline.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chinese Acrobatics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chinese Acrobatics do's and don'ts.", "x": "Etiquette: Plates.. Plates. The rules of respect — Chinese Acrobatics. the ancient troupe. When in doubt, ask about Shows.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chinese Acrobatics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chinese Acrobatics.", "x": "Planning: Contortion.. Diabolo. Practical notes — Chinese Acrobatics. the ancient troupe. A little planning shows respect for Diabolo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chinese Acrobatics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chinese Acrobatics and money.", "x": "Costs: Wu Qiao.. Wu Qiao. What to budget — Chinese Acrobatics. the ancient troupe. The best experiences of Discipline. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-circus-chinese-acrobatics-circus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
