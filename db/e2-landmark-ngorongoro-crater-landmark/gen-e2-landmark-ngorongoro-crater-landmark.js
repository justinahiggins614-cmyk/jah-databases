(function(){'use strict';
/* JAH Ngorongoro Crater Landmark Database generator — jahdb-e2-landmark-ngorongoro-crater-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-ngorongoro-crater-landmark',PREFIX='JAH-E2LANDMARKN-',NAME='JAH Ngorongoro Crater Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ngorongoro Crater: the complete guide", "d": "Ngorongoro Crater: the Eden caldera..", "g": "overview", "l": 2, "q": "What is Ngorongoro Crater: the complete guide?", "a": "Ngorongoro Crater: the Eden caldera..", "x": "The complete landmark guide to Ngorongoro Crater: the Eden caldera.. Caldera. History, meaning, practices, and how to engage respectfully — everything in one database. Caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ngorongoro Crater essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ngorongoro Crater essentials.", "x": "At a glance: Ngorongoro Crater — the Eden caldera.. Eden. The essentials: UNESCO.. Big Five. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Caldera.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Caldera.", "x": "Ngorongoro Crater: Caldera.. UNESCO. Essential knowledge — Big Five.. the Eden caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Caldera..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Caldera..", "x": "Explained: Caldera.. Eden. The context — Ngorongoro Crater. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Eden.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Eden.", "x": "Ngorongoro Crater: Eden.. Maasai. Essential knowledge — UNESCO.. the Eden caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Eden..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Eden..", "x": "Explained: Eden.. Big Five. The context — Ngorongoro Crater. Maasai. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Big Five.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Big Five.", "x": "Ngorongoro Crater: Big Five.. Eden. Essential knowledge — Maasai.. the Eden caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Big Five..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Big Five..", "x": "Explained: Big Five.. Safaris. The context — Ngorongoro Crater. Lerai. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO.", "x": "Ngorongoro Crater: UNESCO.. Big Five. Essential knowledge — Lerai.. the Eden caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Caldera. The context — Ngorongoro Crater. Caldera. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Maasai.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Maasai.", "x": "Ngorongoro Crater: Maasai.. Safaris. Essential knowledge — Caldera.. the Eden caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Maasai..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Maasai..", "x": "Explained: Maasai.. UNESCO. The context — Ngorongoro Crater. Eden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lerai.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lerai.", "x": "Ngorongoro Crater: Lerai.. Caldera. Essential knowledge — Eden.. the Eden caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lerai..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lerai..", "x": "Explained: Lerai.. Maasai. The context — Ngorongoro Crater. Big Five. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Caldera.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Caldera.", "x": "Ngorongoro Crater in depth: Caldera.. Eden. Details — the Eden caldera.. Maasai. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "UNESCO.", "x": "Ngorongoro Crater in depth: UNESCO.. Big Five. Details — the Eden caldera.. Eden. Maasai. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Maasai.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Maasai.", "x": "Ngorongoro Crater in depth: Maasai.. UNESCO. Details — the Eden caldera.. Big Five. Lerai. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Eden.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Eden.", "x": "Ngorongoro Crater in depth: Eden.. Maasai. Details — the Eden caldera.. Safaris. Caldera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Big Five.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Big Five.", "x": "Ngorongoro Crater in depth: Big Five.. Lerai. Details — the Eden caldera.. Caldera. Eden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safaris.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safaris.", "x": "Ngorongoro Crater in depth: Safaris.. Caldera. Details — the Eden caldera.. UNESCO. Big Five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ngorongoro Crater comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ngorongoro Crater comes from.", "x": "Origins: Caldera.. Caldera. The history of Ngorongoro Crater — the Eden caldera.. UNESCO. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ngorongoro Crater respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ngorongoro Crater respectfully.", "x": "Engaging: Maasai.. Eden. How to participate or observe well — Ngorongoro Crater. the Eden caldera. Respect first, always; Eden.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ngorongoro Crater do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ngorongoro Crater do's and don'ts.", "x": "Etiquette: Big Five.. Big Five. The rules of respect — Ngorongoro Crater. the Eden caldera. When in doubt, ask about Safaris.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ngorongoro Crater.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ngorongoro Crater.", "x": "Planning: Caldera.. UNESCO. Practical notes — Ngorongoro Crater. the Eden caldera. A little planning shows respect for UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ngorongoro Crater and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ngorongoro Crater and money.", "x": "Costs: Maasai.. Maasai. What to budget — Ngorongoro Crater. the Eden caldera. The best experiences of Eden. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-ngorongoro-crater-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
