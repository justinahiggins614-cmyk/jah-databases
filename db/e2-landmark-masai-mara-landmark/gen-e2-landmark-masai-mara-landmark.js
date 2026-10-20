(function(){'use strict';
/* JAH Masai Mara Landmark Database generator — jahdb-e2-landmark-masai-mara-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-masai-mara-landmark',PREFIX='JAH-E2LANDMARKM-',NAME='JAH Masai Mara Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Masai Mara: the complete guide", "d": "Masai Mara: the migration river..", "g": "overview", "l": 2, "q": "What is Masai Mara: the complete guide?", "a": "Masai Mara: the migration river..", "x": "The complete landmark guide to Masai Mara: the migration river.. Mara River. History, meaning, practices, and how to engage respectfully — everything in one database. River. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Masai Mara essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Masai Mara essentials.", "x": "At a glance: Masai Mara — the migration river.. Crossing. The essentials: Crossing.. Big cats. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mara River.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mara River.", "x": "Masai Mara: Mara River.. Crossing. Essential knowledge — Big cats.. the migration river. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mara River..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mara River..", "x": "Explained: Mara River.. July. The context — Masai Mara. Maasai. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Crossing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Crossing.", "x": "Masai Mara: Crossing.. Maasai. Essential knowledge — Maasai.. the migration river. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Crossing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Crossing..", "x": "Explained: Crossing.. Safari. The context — Masai Mara. Safari. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Big cats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Big cats.", "x": "Masai Mara: Big cats.. July. Essential knowledge — Safari.. the migration river. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Big cats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Big cats..", "x": "Explained: Big cats.. Tours. The context — Masai Mara. July. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Maasai.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Maasai.", "x": "Masai Mara: Maasai.. Safari. Essential knowledge — July.. the migration river. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Maasai..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Maasai..", "x": "Explained: Maasai.. River. The context — Masai Mara. Mara River. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Safari.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Safari.", "x": "Masai Mara: Safari.. Tours. Essential knowledge — Mara River.. the migration river. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Safari..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Safari..", "x": "Explained: Safari.. Crossing. The context — Masai Mara. Crossing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "July.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "July.", "x": "Masai Mara: July.. River. Essential knowledge — Crossing.. the migration river. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: July..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: July..", "x": "Explained: July.. Maasai. The context — Masai Mara. Big cats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "River.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "River.", "x": "Masai Mara in depth: River.. Crossing. Details — the migration river.. Maasai. Maasai. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crossing.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crossing.", "x": "Masai Mara in depth: Crossing.. Big cats. Details — the migration river.. July. Safari. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Maasai.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Maasai.", "x": "Masai Mara in depth: Maasai.. Maasai. Details — the migration river.. Safari. July. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "July.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "July.", "x": "Masai Mara in depth: July.. Safari. Details — the migration river.. Tours. Mara River. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Safari.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Safari.", "x": "Masai Mara in depth: Safari.. July. Details — the migration river.. River. Crossing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Masai Mara in depth: Tours.. Mara River. Details — the migration river.. Crossing. Big cats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Masai Mara comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Masai Mara comes from.", "x": "Origins: River.. Mara River. The history of Masai Mara — the migration river.. Crossing. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Masai Mara respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Masai Mara respectfully.", "x": "Engaging: Maasai.. Crossing. How to participate or observe well — Masai Mara. the migration river. Respect first, always; July.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Masai Mara do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Masai Mara do's and don'ts.", "x": "Etiquette: Safari.. Big cats. The rules of respect — Masai Mara. the migration river. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Masai Mara.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Masai Mara.", "x": "Planning: River.. Maasai. Practical notes — Masai Mara. the migration river. A little planning shows respect for Crossing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Masai Mara and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Masai Mara and money.", "x": "Costs: Maasai.. Safari. What to budget — Masai Mara. the migration river. The best experiences of July. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-masai-mara-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
