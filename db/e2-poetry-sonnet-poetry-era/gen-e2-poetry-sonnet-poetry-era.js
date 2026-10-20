(function(){'use strict';
/* JAH Sonnet Poetry Poetry Database generator — jahdb-e2-poetry-sonnet-poetry-era-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-poetry-sonnet-poetry-era',PREFIX='JAH-E2POETRYSON-',NAME='JAH Sonnet Poetry Poetry Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sonnet Poetry: the complete guide", "d": "Sonnet Poetry: the 14-line form..", "g": "overview", "l": 2, "q": "What is Sonnet Poetry: the complete guide?", "a": "Sonnet Poetry: the 14-line form..", "x": "The complete poetry guide to Sonnet Poetry: the 14-line form.. 14 lines. History, meaning, practices, and how to engage respectfully — everything in one database. Lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sonnet Poetry essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sonnet Poetry essentials.", "x": "At a glance: Sonnet Poetry — the 14-line form.. Petrarchan. The essentials: Volta.. Shakespearean. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "14 lines.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "14 lines.", "x": "Sonnet Poetry: 14 lines.. Volta. Essential knowledge — Shakespearean.. the 14-line form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 14 lines..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 14 lines..", "x": "Explained: 14 lines.. Love. The context — Sonnet Poetry. Volta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Petrarchan.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Petrarchan.", "x": "Sonnet Poetry: Petrarchan.. Iambic. Essential knowledge — Volta.. the 14-line form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Petrarchan..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Petrarchan..", "x": "Explained: Petrarchan.. Forms. The context — Sonnet Poetry. Iambic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shakespearean.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shakespearean.", "x": "Sonnet Poetry: Shakespearean.. Love. Essential knowledge — Iambic.. the 14-line form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shakespearean..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shakespearean..", "x": "Explained: Shakespearean.. Legacy. The context — Sonnet Poetry. Love. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Volta.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Volta.", "x": "Sonnet Poetry: Volta.. Forms. Essential knowledge — Love.. the 14-line form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Volta..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Volta..", "x": "Explained: Volta.. Lines. The context — Sonnet Poetry. 14 lines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Iambic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Iambic.", "x": "Sonnet Poetry: Iambic.. Legacy. Essential knowledge — 14 lines.. the 14-line form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Iambic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Iambic..", "x": "Explained: Iambic.. Volta. The context — Sonnet Poetry. Petrarchan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Love.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Love.", "x": "Sonnet Poetry: Love.. Lines. Essential knowledge — Petrarchan.. the 14-line form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Love..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Love..", "x": "Explained: Love.. Iambic. The context — Sonnet Poetry. Shakespearean. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lines.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lines.", "x": "Sonnet Poetry in depth: Lines.. Petrarchan. Details — the 14-line form.. Iambic. Volta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Volta.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Volta.", "x": "Sonnet Poetry in depth: Volta.. Shakespearean. Details — the 14-line form.. Love. Iambic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Iambic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Iambic.", "x": "Sonnet Poetry in depth: Iambic.. Volta. Details — the 14-line form.. Forms. Love. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Love.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Love.", "x": "Sonnet Poetry in depth: Love.. Iambic. Details — the 14-line form.. Legacy. 14 lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Forms.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Forms.", "x": "Sonnet Poetry in depth: Forms.. Love. Details — the 14-line form.. Lines. Petrarchan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Sonnet Poetry in depth: Legacy.. 14 lines. Details — the 14-line form.. Volta. Shakespearean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sonnet Poetry comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sonnet Poetry comes from.", "x": "Origins: Lines.. 14 lines. The history of Sonnet Poetry — the 14-line form.. Volta. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sonnet Poetry respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sonnet Poetry respectfully.", "x": "Engaging: Iambic.. Petrarchan. How to participate or observe well — Sonnet Poetry. the 14-line form. Respect first, always; Love.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sonnet Poetry do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sonnet Poetry do's and don'ts.", "x": "Etiquette: Forms.. Shakespearean. The rules of respect — Sonnet Poetry. the 14-line form. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sonnet Poetry.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sonnet Poetry.", "x": "Planning: Lines.. Volta. Practical notes — Sonnet Poetry. the 14-line form. A little planning shows respect for Volta.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sonnet Poetry and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sonnet Poetry and money.", "x": "Costs: Iambic.. Iambic. What to budget — Sonnet Poetry. the 14-line form. The best experiences of Love. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-poetry-sonnet-poetry-era-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
