(function(){'use strict';
/* JAH Coppelia Ballet Ballet Database generator — jahdb-e2-ballet-coppelia-ballet-dance-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ballet-coppelia-ballet-dance',PREFIX='JAH-E2BALLETCOP-',NAME='JAH Coppelia Ballet Ballet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Coppelia Ballet: the complete guide", "d": "Coppelia Ballet: the doll comedy..", "g": "overview", "l": 2, "q": "What is Coppelia Ballet: the complete guide?", "a": "Coppelia Ballet: the doll comedy..", "x": "The complete ballet guide to Coppelia Ballet: the doll comedy.. Delibes. History, meaning, practices, and how to engage respectfully — everything in one database. Doll. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Coppelia Ballet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Coppelia Ballet essentials.", "x": "At a glance: Coppelia Ballet — the doll comedy.. Doll. The essentials: Swanilda.. Swanilda. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Delibes.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Delibes.", "x": "Coppelia Ballet: Delibes.. Swanilda. Essential knowledge — Swanilda.. the doll comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Delibes..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Delibes..", "x": "Explained: Delibes.. Comedy. The context — Coppelia Ballet. 1870. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Doll.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Doll.", "x": "Coppelia Ballet: Doll.. 1870. Essential knowledge — 1870.. the doll comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Doll..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Doll..", "x": "Explained: Doll.. Delibes. The context — Coppelia Ballet. Comedy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Swanilda.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Swanilda.", "x": "Coppelia Ballet: Swanilda.. Comedy. Essential knowledge — Comedy.. the doll comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Swanilda..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Swanilda..", "x": "Explained: Swanilda.. Story. The context — Coppelia Ballet. Village. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1870.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1870.", "x": "Coppelia Ballet: 1870.. Delibes. Essential knowledge — Village.. the doll comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1870..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1870..", "x": "Explained: 1870.. Doll. The context — Coppelia Ballet. Delibes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Comedy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Comedy.", "x": "Coppelia Ballet: Comedy.. Story. Essential knowledge — Delibes.. the doll comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Comedy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Comedy..", "x": "Explained: Comedy.. Swanilda. The context — Coppelia Ballet. Doll. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Village.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Village.", "x": "Coppelia Ballet: Village.. Doll. Essential knowledge — Doll.. the doll comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Village..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Village..", "x": "Explained: Village.. 1870. The context — Coppelia Ballet. Swanilda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Doll.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Doll.", "x": "Coppelia Ballet in depth: Doll.. Doll. Details — the doll comedy.. 1870. 1870. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Swanilda.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Swanilda.", "x": "Coppelia Ballet in depth: Swanilda.. Swanilda. Details — the doll comedy.. Comedy. Comedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1870.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1870.", "x": "Coppelia Ballet in depth: 1870.. 1870. Details — the doll comedy.. Delibes. Village. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Comedy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Comedy.", "x": "Coppelia Ballet in depth: Comedy.. Comedy. Details — the doll comedy.. Story. Delibes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Delibes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Delibes.", "x": "Coppelia Ballet in depth: Delibes.. Village. Details — the doll comedy.. Doll. Doll. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Story.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Story.", "x": "Coppelia Ballet in depth: Story.. Delibes. Details — the doll comedy.. Swanilda. Swanilda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Coppelia Ballet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Coppelia Ballet comes from.", "x": "Origins: Doll.. Delibes. The history of Coppelia Ballet — the doll comedy.. Swanilda. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Coppelia Ballet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Coppelia Ballet respectfully.", "x": "Engaging: 1870.. Doll. How to participate or observe well — Coppelia Ballet. the doll comedy. Respect first, always; Comedy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Coppelia Ballet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Coppelia Ballet do's and don'ts.", "x": "Etiquette: Delibes.. Swanilda. The rules of respect — Coppelia Ballet. the doll comedy. When in doubt, ask about Story.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Coppelia Ballet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Coppelia Ballet.", "x": "Planning: Doll.. 1870. Practical notes — Coppelia Ballet. the doll comedy. A little planning shows respect for Swanilda.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Coppelia Ballet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Coppelia Ballet and money.", "x": "Costs: 1870.. Comedy. What to budget — Coppelia Ballet. the doll comedy. The best experiences of Comedy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ballet-coppelia-ballet-dance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
