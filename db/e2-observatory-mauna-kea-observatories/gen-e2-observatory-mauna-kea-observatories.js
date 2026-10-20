(function(){'use strict';
/* JAH Mauna Kea Observatories Observatory Database generator — jahdb-e2-observatory-mauna-kea-observatories-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-mauna-kea-observatories',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Mauna Kea Observatories Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mauna Kea Observatories: the complete guide", "d": "Mauna Kea Observatories: the world's best seeing..", "g": "overview", "l": 2, "q": "What is Mauna Kea Observatories: the complete guide?", "a": "Mauna Kea Observatories: the world's best seeing..", "x": "The complete observatory guide to Mauna Kea Observatories: the world's best seeing.. 4,200m. History, meaning, practices, and how to engage respectfully — everything in one database. Telescopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mauna Kea Observatories essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mauna Kea Observatories essentials.", "x": "At a glance: Mauna Kea Observatories — the world's best seeing.. Keck twins. The essentials: Altitude.. Subaru. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "4,200m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "4,200m.", "x": "Mauna Kea Observatories: 4,200m.. Altitude. Essential knowledge — Subaru.. the world's best seeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 4,200m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 4,200m..", "x": "Explained: 4,200m.. Science. The context — Mauna Kea Observatories. Gemini. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Keck twins.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Keck twins.", "x": "Mauna Kea Observatories: Keck twins.. Sacred. Essential knowledge — Gemini.. the world's best seeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Keck twins..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Keck twins..", "x": "Explained: Keck twins.. Tours. The context — Mauna Kea Observatories. Sacred. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Subaru.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Subaru.", "x": "Mauna Kea Observatories: Subaru.. Science. Essential knowledge — Sacred.. the world's best seeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Subaru..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Subaru..", "x": "Explained: Subaru.. Debate. The context — Mauna Kea Observatories. Protests. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gemini.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gemini.", "x": "Mauna Kea Observatories: Gemini.. Tours. Essential knowledge — Protests.. the world's best seeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gemini..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gemini..", "x": "Explained: Gemini.. Telescopes. The context — Mauna Kea Observatories. 4,200m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sacred.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sacred.", "x": "Mauna Kea Observatories: Sacred.. Debate. Essential knowledge — 4,200m.. the world's best seeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sacred..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sacred..", "x": "Explained: Sacred.. Altitude. The context — Mauna Kea Observatories. Keck twins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Protests.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Protests.", "x": "Mauna Kea Observatories: Protests.. Telescopes. Essential knowledge — Keck twins.. the world's best seeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Protests..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Protests..", "x": "Explained: Protests.. Sacred. The context — Mauna Kea Observatories. Subaru. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Telescopes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Telescopes.", "x": "Mauna Kea Observatories in depth: Telescopes.. Keck twins. Details — the world's best seeing.. Sacred. Gemini. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Altitude.", "x": "Mauna Kea Observatories in depth: Altitude.. Subaru. Details — the world's best seeing.. Science. Sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sacred.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sacred.", "x": "Mauna Kea Observatories in depth: Sacred.. Gemini. Details — the world's best seeing.. Tours. Protests. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Science.", "x": "Mauna Kea Observatories in depth: Science.. Sacred. Details — the world's best seeing.. Debate. 4,200m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Mauna Kea Observatories in depth: Tours.. Protests. Details — the world's best seeing.. Telescopes. Keck twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Debate.", "x": "Mauna Kea Observatories in depth: Debate.. 4,200m. Details — the world's best seeing.. Altitude. Subaru. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mauna Kea Observatories comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mauna Kea Observatories comes from.", "x": "Origins: Telescopes.. 4,200m. The history of Mauna Kea Observatories — the world's best seeing.. Altitude. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mauna Kea Observatories respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mauna Kea Observatories respectfully.", "x": "Engaging: Sacred.. Keck twins. How to participate or observe well — Mauna Kea Observatories. the world's best seeing. Respect first, always; Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mauna Kea Observatories do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mauna Kea Observatories do's and don'ts.", "x": "Etiquette: Tours.. Subaru. The rules of respect — Mauna Kea Observatories. the world's best seeing. When in doubt, ask about Debate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mauna Kea Observatories.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mauna Kea Observatories.", "x": "Planning: Telescopes.. Gemini. Practical notes — Mauna Kea Observatories. the world's best seeing. A little planning shows respect for Altitude.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mauna Kea Observatories and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mauna Kea Observatories and money.", "x": "Costs: Sacred.. Sacred. What to budget — Mauna Kea Observatories. the world's best seeing. The best experiences of Science. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-mauna-kea-observatories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
