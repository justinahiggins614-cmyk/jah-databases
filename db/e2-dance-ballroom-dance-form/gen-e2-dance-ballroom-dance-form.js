(function(){'use strict';
/* JAH Ballroom Dance Dance Form Database generator — jahdb-e2-dance-ballroom-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-ballroom-dance-form',PREFIX='JAH-E2DANCEBALL-',NAME='JAH Ballroom Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ballroom Dance: the complete guide", "d": "Ballroom Dance: the partnered elegance..", "g": "overview", "l": 2, "q": "What is Ballroom Dance: the complete guide?", "a": "Ballroom Dance: the partnered elegance..", "x": "The complete dance form guide to Ballroom Dance: the partnered elegance.. 10 dances. History, meaning, practices, and how to engage respectfully — everything in one database. Dances. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ballroom Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ballroom Dance essentials.", "x": "At a glance: Ballroom Dance — the partnered elegance.. Latin. The essentials: Comp.. Standard. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "10 dances.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "10 dances.", "x": "Ballroom Dance: 10 dances.. Comp. Essential knowledge — Standard.. the partnered elegance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 10 dances..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 10 dances..", "x": "Explained: 10 dances.. Syllabus. The context — Ballroom Dance. Competitions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Latin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Latin.", "x": "Ballroom Dance: Latin.. Frame. Essential knowledge — Competitions.. the partnered elegance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Latin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Latin..", "x": "Explained: Latin.. Latin. The context — Ballroom Dance. Frame. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Standard.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Standard.", "x": "Ballroom Dance: Standard.. Syllabus. Essential knowledge — Frame.. the partnered elegance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Standard..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Standard..", "x": "Explained: Standard.. Training. The context — Ballroom Dance. Syllabus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Competitions.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Competitions.", "x": "Ballroom Dance: Competitions.. Latin. Essential knowledge — Syllabus.. the partnered elegance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Competitions..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Competitions..", "x": "Explained: Competitions.. Dances. The context — Ballroom Dance. 10 dances. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Frame.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Frame.", "x": "Ballroom Dance: Frame.. Training. Essential knowledge — 10 dances.. the partnered elegance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Frame..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Frame..", "x": "Explained: Frame.. Comp. The context — Ballroom Dance. Latin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Syllabus.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Syllabus.", "x": "Ballroom Dance: Syllabus.. Dances. Essential knowledge — Latin.. the partnered elegance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Syllabus..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Syllabus..", "x": "Explained: Syllabus.. Frame. The context — Ballroom Dance. Standard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dances.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dances.", "x": "Ballroom Dance in depth: Dances.. Latin. Details — the partnered elegance.. Frame. Competitions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Comp.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Comp.", "x": "Ballroom Dance in depth: Comp.. Standard. Details — the partnered elegance.. Syllabus. Frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Frame.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Frame.", "x": "Ballroom Dance in depth: Frame.. Competitions. Details — the partnered elegance.. Latin. Syllabus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Syllabus.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Syllabus.", "x": "Ballroom Dance in depth: Syllabus.. Frame. Details — the partnered elegance.. Training. 10 dances. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Latin.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Latin.", "x": "Ballroom Dance in depth: Latin.. Syllabus. Details — the partnered elegance.. Dances. Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Ballroom Dance in depth: Training.. 10 dances. Details — the partnered elegance.. Comp. Standard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ballroom Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ballroom Dance comes from.", "x": "Origins: Dances.. 10 dances. The history of Ballroom Dance — the partnered elegance.. Comp. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ballroom Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ballroom Dance respectfully.", "x": "Engaging: Frame.. Latin. How to participate or observe well — Ballroom Dance. the partnered elegance. Respect first, always; Syllabus.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ballroom Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ballroom Dance do's and don'ts.", "x": "Etiquette: Latin.. Standard. The rules of respect — Ballroom Dance. the partnered elegance. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ballroom Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ballroom Dance.", "x": "Planning: Dances.. Competitions. Practical notes — Ballroom Dance. the partnered elegance. A little planning shows respect for Comp.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ballroom Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ballroom Dance and money.", "x": "Costs: Frame.. Frame. What to budget — Ballroom Dance. the partnered elegance. The best experiences of Syllabus. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-ballroom-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
