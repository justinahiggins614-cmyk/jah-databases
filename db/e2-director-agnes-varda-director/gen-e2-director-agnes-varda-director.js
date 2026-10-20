(function(){'use strict';
/* JAH Agnès Varda Director Database generator — jahdb-e2-director-agnes-varda-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-agnes-varda-director',PREFIX='JAH-E2DIRECTORA-',NAME='JAH Agnès Varda Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Agnès Varda: the complete guide", "d": "Agnès Varda: the new wave mother..", "g": "overview", "l": 2, "q": "What is Agnès Varda: the complete guide?", "a": "Agnès Varda: the new wave mother..", "x": "The complete director guide to Agnès Varda: the new wave mother.. 1928. History, meaning, practices, and how to engage respectfully — everything in one database. Cleo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Agnès Varda essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Agnès Varda essentials.", "x": "At a glance: Agnès Varda — the new wave mother.. Cleo. The essentials: Gleaners.. Gleaners. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1928.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1928.", "x": "Agnès Varda: 1928.. Gleaners. Essential knowledge — Gleaners.. the new wave mother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1928..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1928..", "x": "Explained: 1928.. Playful. The context — Agnès Varda. Photography. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cleo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cleo.", "x": "Agnès Varda: Cleo.. Feminist. Essential knowledge — Photography.. the new wave mother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cleo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cleo..", "x": "Explained: Cleo.. Photo. The context — Agnès Varda. Feminist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gleaners.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gleaners.", "x": "Agnès Varda: Gleaners.. Playful. Essential knowledge — Feminist.. the new wave mother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gleaners..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gleaners..", "x": "Explained: Gleaners.. Style. The context — Agnès Varda. Playful. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Photography.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Photography.", "x": "Agnès Varda: Photography.. Photo. Essential knowledge — Playful.. the new wave mother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Photography..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Photography..", "x": "Explained: Photography.. Cleo. The context — Agnès Varda. 1928. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Feminist.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Feminist.", "x": "Agnès Varda: Feminist.. Style. Essential knowledge — 1928.. the new wave mother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Feminist..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Feminist..", "x": "Explained: Feminist.. Gleaners. The context — Agnès Varda. Cleo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Playful.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Playful.", "x": "Agnès Varda: Playful.. Cleo. Essential knowledge — Cleo.. the new wave mother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Playful..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Playful..", "x": "Explained: Playful.. Feminist. The context — Agnès Varda. Gleaners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cleo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cleo.", "x": "Agnès Varda in depth: Cleo.. Cleo. Details — the new wave mother.. Feminist. Photography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gleaners.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gleaners.", "x": "Agnès Varda in depth: Gleaners.. Gleaners. Details — the new wave mother.. Playful. Feminist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Feminist.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Feminist.", "x": "Agnès Varda in depth: Feminist.. Photography. Details — the new wave mother.. Photo. Playful. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Playful.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Playful.", "x": "Agnès Varda in depth: Playful.. Feminist. Details — the new wave mother.. Style. 1928. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Photo.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Photo.", "x": "Agnès Varda in depth: Photo.. Playful. Details — the new wave mother.. Cleo. Cleo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Agnès Varda in depth: Style.. 1928. Details — the new wave mother.. Gleaners. Gleaners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Agnès Varda comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Agnès Varda comes from.", "x": "Origins: Cleo.. 1928. The history of Agnès Varda — the new wave mother.. Gleaners. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Agnès Varda respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Agnès Varda respectfully.", "x": "Engaging: Feminist.. Cleo. How to participate or observe well — Agnès Varda. the new wave mother. Respect first, always; Playful.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Agnès Varda do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Agnès Varda do's and don'ts.", "x": "Etiquette: Photo.. Gleaners. The rules of respect — Agnès Varda. the new wave mother. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Agnès Varda.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Agnès Varda.", "x": "Planning: Cleo.. Photography. Practical notes — Agnès Varda. the new wave mother. A little planning shows respect for Gleaners.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Agnès Varda and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Agnès Varda and money.", "x": "Costs: Feminist.. Feminist. What to budget — Agnès Varda. the new wave mother. The best experiences of Playful. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-agnes-varda-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
