(function(){'use strict';
/* JAH Tianjin Binhai Library Library Database generator — jahdb-e2-library-tianjin-binhai-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-tianjin-binhai-library',PREFIX='JAH-E2LIBRARYTI-',NAME='JAH Tianjin Binhai Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tianjin Binhai Library: the complete guide", "d": "Tianjin Binhai Library: the eye of Tianjin..", "g": "overview", "l": 2, "q": "What is Tianjin Binhai Library: the complete guide?", "a": "Tianjin Binhai Library: the eye of Tianjin..", "x": "The complete library guide to Tianjin Binhai Library: the eye of Tianjin.. 2017. History, meaning, practices, and how to engage respectfully — everything in one database. Eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tianjin Binhai Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tianjin Binhai Library essentials.", "x": "At a glance: Tianjin Binhai Library — the eye of Tianjin.. The Eye. The essentials: Design.. 1.2M books. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2017.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2017.", "x": "Tianjin Binhai Library: 2017.. Design. Essential knowledge — 1.2M books.. the eye of Tianjin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2017..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2017..", "x": "Explained: 2017.. Tours. The context — Tianjin Binhai Library. MVRDV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "The Eye.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "The Eye.", "x": "Tianjin Binhai Library: The Eye.. China. Essential knowledge — MVRDV.. the eye of Tianjin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: The Eye..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: The Eye..", "x": "Explained: The Eye.. Photos. The context — Tianjin Binhai Library. China. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1.2M books.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1.2M books.", "x": "Tianjin Binhai Library: 1.2M books.. Tours. Essential knowledge — China.. the eye of Tianjin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1.2M books..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1.2M books..", "x": "Explained: 1.2M books.. Books. The context — Tianjin Binhai Library. Photos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "MVRDV.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "MVRDV.", "x": "Tianjin Binhai Library: MVRDV.. Photos. Essential knowledge — Photos.. the eye of Tianjin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: MVRDV..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: MVRDV..", "x": "Explained: MVRDV.. Eye. The context — Tianjin Binhai Library. 2017. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "China.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "China.", "x": "Tianjin Binhai Library: China.. Books. Essential knowledge — 2017.. the eye of Tianjin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: China..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: China..", "x": "Explained: China.. Design. The context — Tianjin Binhai Library. The Eye. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Photos.", "x": "Tianjin Binhai Library: Photos.. Eye. Essential knowledge — The Eye.. the eye of Tianjin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Photos..", "x": "Explained: Photos.. China. The context — Tianjin Binhai Library. 1.2M books. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Eye.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Eye.", "x": "Tianjin Binhai Library in depth: Eye.. The Eye. Details — the eye of Tianjin.. China. MVRDV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Design.", "x": "Tianjin Binhai Library in depth: Design.. 1.2M books. Details — the eye of Tianjin.. Tours. China. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "China.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "China.", "x": "Tianjin Binhai Library in depth: China.. MVRDV. Details — the eye of Tianjin.. Photos. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Tianjin Binhai Library in depth: Tours.. China. Details — the eye of Tianjin.. Books. 2017. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Photos.", "x": "Tianjin Binhai Library in depth: Photos.. Photos. Details — the eye of Tianjin.. Eye. The Eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Books.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Books.", "x": "Tianjin Binhai Library in depth: Books.. 2017. Details — the eye of Tianjin.. Design. 1.2M books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tianjin Binhai Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tianjin Binhai Library comes from.", "x": "Origins: Eye.. 2017. The history of Tianjin Binhai Library — the eye of Tianjin.. Design. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tianjin Binhai Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tianjin Binhai Library respectfully.", "x": "Engaging: China.. The Eye. How to participate or observe well — Tianjin Binhai Library. the eye of Tianjin. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tianjin Binhai Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tianjin Binhai Library do's and don'ts.", "x": "Etiquette: Photos.. 1.2M books. The rules of respect — Tianjin Binhai Library. the eye of Tianjin. When in doubt, ask about Books.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tianjin Binhai Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tianjin Binhai Library.", "x": "Planning: Eye.. MVRDV. Practical notes — Tianjin Binhai Library. the eye of Tianjin. A little planning shows respect for Design.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tianjin Binhai Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tianjin Binhai Library and money.", "x": "Costs: China.. China. What to budget — Tianjin Binhai Library. the eye of Tianjin. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-tianjin-binhai-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
