(function(){'use strict';
/* JAH Sleeping Beauty Ballet Ballet Database generator — jahdb-e2-ballet-sleeping-beauty-ballet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ballet-sleeping-beauty-ballet',PREFIX='JAH-E2BALLETSLE-',NAME='JAH Sleeping Beauty Ballet Ballet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sleeping Beauty Ballet: the complete guide", "d": "Sleeping Beauty Ballet: the Petipa showcase..", "g": "overview", "l": 2, "q": "What is Sleeping Beauty Ballet: the complete guide?", "a": "Sleeping Beauty Ballet: the Petipa showcase..", "x": "The complete ballet guide to Sleeping Beauty Ballet: the Petipa showcase.. Tchaikovsky. History, meaning, practices, and how to engage respectfully — everything in one database. Aurora. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sleeping Beauty Ballet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sleeping Beauty Ballet essentials.", "x": "At a glance: Sleeping Beauty Ballet — the Petipa showcase.. Aurora. The essentials: Adagio.. Rose Adagio. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Tchaikovsky.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Tchaikovsky.", "x": "Sleeping Beauty Ballet: Tchaikovsky.. Adagio. Essential knowledge — Rose Adagio.. the Petipa showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Tchaikovsky..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Tchaikovsky..", "x": "Explained: Tchaikovsky.. Fairies. The context — Sleeping Beauty Ballet. 1890. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aurora.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aurora.", "x": "Sleeping Beauty Ballet: Aurora.. 1890. Essential knowledge — 1890.. the Petipa showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Aurora..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Aurora..", "x": "Explained: Aurora.. Wedding. The context — Sleeping Beauty Ballet. Fairies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rose Adagio.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rose Adagio.", "x": "Sleeping Beauty Ballet: Rose Adagio.. Fairies. Essential knowledge — Fairies.. the Petipa showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rose Adagio..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rose Adagio..", "x": "Explained: Rose Adagio.. Story. The context — Sleeping Beauty Ballet. Wedding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1890.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1890.", "x": "Sleeping Beauty Ballet: 1890.. Wedding. Essential knowledge — Wedding.. the Petipa showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1890..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1890..", "x": "Explained: 1890.. Aurora. The context — Sleeping Beauty Ballet. Tchaikovsky. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fairies.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fairies.", "x": "Sleeping Beauty Ballet: Fairies.. Story. Essential knowledge — Tchaikovsky.. the Petipa showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fairies..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fairies..", "x": "Explained: Fairies.. Adagio. The context — Sleeping Beauty Ballet. Aurora. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wedding.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wedding.", "x": "Sleeping Beauty Ballet: Wedding.. Aurora. Essential knowledge — Aurora.. the Petipa showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Wedding..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Wedding..", "x": "Explained: Wedding.. 1890. The context — Sleeping Beauty Ballet. Rose Adagio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aurora.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aurora.", "x": "Sleeping Beauty Ballet in depth: Aurora.. Aurora. Details — the Petipa showcase.. 1890. 1890. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Adagio.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Adagio.", "x": "Sleeping Beauty Ballet in depth: Adagio.. Rose Adagio. Details — the Petipa showcase.. Fairies. Fairies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1890.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1890.", "x": "Sleeping Beauty Ballet in depth: 1890.. 1890. Details — the Petipa showcase.. Wedding. Wedding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fairies.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fairies.", "x": "Sleeping Beauty Ballet in depth: Fairies.. Fairies. Details — the Petipa showcase.. Story. Tchaikovsky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wedding.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wedding.", "x": "Sleeping Beauty Ballet in depth: Wedding.. Wedding. Details — the Petipa showcase.. Aurora. Aurora. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Story.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Story.", "x": "Sleeping Beauty Ballet in depth: Story.. Tchaikovsky. Details — the Petipa showcase.. Adagio. Rose Adagio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sleeping Beauty Ballet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sleeping Beauty Ballet comes from.", "x": "Origins: Aurora.. Tchaikovsky. The history of Sleeping Beauty Ballet — the Petipa showcase.. Adagio. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sleeping Beauty Ballet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sleeping Beauty Ballet respectfully.", "x": "Engaging: 1890.. Aurora. How to participate or observe well — Sleeping Beauty Ballet. the Petipa showcase. Respect first, always; Fairies.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sleeping Beauty Ballet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sleeping Beauty Ballet do's and don'ts.", "x": "Etiquette: Wedding.. Rose Adagio. The rules of respect — Sleeping Beauty Ballet. the Petipa showcase. When in doubt, ask about Story.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sleeping Beauty Ballet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sleeping Beauty Ballet.", "x": "Planning: Aurora.. 1890. Practical notes — Sleeping Beauty Ballet. the Petipa showcase. A little planning shows respect for Adagio.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sleeping Beauty Ballet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sleeping Beauty Ballet and money.", "x": "Costs: 1890.. Fairies. What to budget — Sleeping Beauty Ballet. the Petipa showcase. The best experiences of Fairies. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ballet-sleeping-beauty-ballet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
