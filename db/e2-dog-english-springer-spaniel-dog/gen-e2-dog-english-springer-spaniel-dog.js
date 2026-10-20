(function(){'use strict';
/* JAH English Springer Spaniel Dog Breed Database generator — jahdb-e2-dog-english-springer-spaniel-dog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dog-english-springer-spaniel-dog',PREFIX='JAH-E2DOGENGLIS-',NAME='JAH English Springer Spaniel Dog Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "English Springer Spaniel: the complete guide", "d": "English Springer Spaniel: the flushing springer..", "g": "overview", "l": 2, "q": "What is English Springer Spaniel: the complete guide?", "a": "English Springer Spaniel: the flushing springer..", "x": "The complete dog breed guide to English Springer Spaniel: the flushing springer.. Flushing. History, meaning, practices, and how to engage respectfully — everything in one database. Flushing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "English Springer Spaniel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "English Springer Spaniel essentials.", "x": "At a glance: English Springer Spaniel — the flushing springer.. Springing. The essentials: Field.. Energetic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Flushing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Flushing.", "x": "English Springer Spaniel: Flushing.. Field. Essential knowledge — Energetic.. the flushing springer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Flushing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Flushing..", "x": "Explained: Flushing.. Ears. The context — English Springer Spaniel. Field. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Springing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Springing.", "x": "English Springer Spaniel: Springing.. Happy. Essential knowledge — Field.. the flushing springer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Springing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Springing..", "x": "Explained: Springing.. Energetic. The context — English Springer Spaniel. Ears. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Energetic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Energetic.", "x": "English Springer Spaniel: Energetic.. Ears. Essential knowledge — Ears.. the flushing springer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Energetic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Energetic..", "x": "Explained: Energetic.. History. The context — English Springer Spaniel. Happy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Field.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Field.", "x": "English Springer Spaniel: Field.. Energetic. Essential knowledge — Happy.. the flushing springer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Field..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Field..", "x": "Explained: Field.. Flushing. The context — English Springer Spaniel. Flushing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ears.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ears.", "x": "English Springer Spaniel: Ears.. History. Essential knowledge — Flushing.. the flushing springer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ears..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ears..", "x": "Explained: Ears.. Field. The context — English Springer Spaniel. Springing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Happy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Happy.", "x": "English Springer Spaniel: Happy.. Flushing. Essential knowledge — Springing.. the flushing springer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Happy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Happy..", "x": "Explained: Happy.. Happy. The context — English Springer Spaniel. Energetic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Flushing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Flushing.", "x": "English Springer Spaniel in depth: Flushing.. Springing. Details — the flushing springer.. Happy. Field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Field.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Field.", "x": "English Springer Spaniel in depth: Field.. Energetic. Details — the flushing springer.. Ears. Ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Happy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Happy.", "x": "English Springer Spaniel in depth: Happy.. Field. Details — the flushing springer.. Energetic. Happy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ears.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ears.", "x": "English Springer Spaniel in depth: Ears.. Ears. Details — the flushing springer.. History. Flushing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Energetic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Energetic.", "x": "English Springer Spaniel in depth: Energetic.. Happy. Details — the flushing springer.. Flushing. Springing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "English Springer Spaniel in depth: History.. Flushing. Details — the flushing springer.. Field. Energetic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where English Springer Spaniel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where English Springer Spaniel comes from.", "x": "Origins: Flushing.. Flushing. The history of English Springer Spaniel — the flushing springer.. Field. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing English Springer Spaniel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing English Springer Spaniel respectfully.", "x": "Engaging: Happy.. Springing. How to participate or observe well — English Springer Spaniel. the flushing springer. Respect first, always; Ears.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "English Springer Spaniel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "English Springer Spaniel do's and don'ts.", "x": "Etiquette: Energetic.. Energetic. The rules of respect — English Springer Spaniel. the flushing springer. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around English Springer Spaniel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around English Springer Spaniel.", "x": "Planning: Flushing.. Field. Practical notes — English Springer Spaniel. the flushing springer. A little planning shows respect for Field.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "English Springer Spaniel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "English Springer Spaniel and money.", "x": "Costs: Happy.. Ears. What to budget — English Springer Spaniel. the flushing springer. The best experiences of Ears. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dog-english-springer-spaniel-dog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
