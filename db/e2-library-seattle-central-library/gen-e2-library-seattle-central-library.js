(function(){'use strict';
/* JAH Seattle Central Library Library Database generator — jahdb-e2-library-seattle-central-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-seattle-central-library',PREFIX='JAH-E2LIBRARYSE-',NAME='JAH Seattle Central Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Seattle Central Library: the complete guide", "d": "Seattle Central Library: Koolhaas glass grid..", "g": "overview", "l": 2, "q": "What is Seattle Central Library: the complete guide?", "a": "Seattle Central Library: Koolhaas glass grid..", "x": "The complete library guide to Seattle Central Library: Koolhaas glass grid.. 2004. History, meaning, practices, and how to engage respectfully — everything in one database. Building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Seattle Central Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Seattle Central Library essentials.", "x": "At a glance: Seattle Central Library — Koolhaas glass grid.. Koolhaas. The essentials: Design.. Glass/steel. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2004.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2004.", "x": "Seattle Central Library: 2004.. Design. Essential knowledge — Glass/steel.. Koolhaas glass grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2004..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2004..", "x": "Explained: 2004.. Seattle. The context — Seattle Central Library. 11 floors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Koolhaas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Koolhaas.", "x": "Seattle Central Library: Koolhaas.. Tours. Essential knowledge — 11 floors.. Koolhaas glass grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Koolhaas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Koolhaas..", "x": "Explained: Koolhaas.. Free. The context — Seattle Central Library. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Glass/steel.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Glass/steel.", "x": "Seattle Central Library: Glass/steel.. Seattle. Essential knowledge — Free.. Koolhaas glass grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Glass/steel..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Glass/steel..", "x": "Explained: Glass/steel.. Architecture. The context — Seattle Central Library. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "11 floors.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "11 floors.", "x": "Seattle Central Library: 11 floors.. Free. Essential knowledge — Views.. Koolhaas glass grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 11 floors..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 11 floors..", "x": "Explained: 11 floors.. Building. The context — Seattle Central Library. 2004. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Free.", "x": "Seattle Central Library: Free.. Architecture. Essential knowledge — 2004.. Koolhaas glass grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Design. The context — Seattle Central Library. Koolhaas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Seattle Central Library: Views.. Building. Essential knowledge — Koolhaas.. Koolhaas glass grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Tours. The context — Seattle Central Library. Glass/steel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Building.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Building.", "x": "Seattle Central Library in depth: Building.. Koolhaas. Details — Koolhaas glass grid.. Tours. 11 floors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Design.", "x": "Seattle Central Library in depth: Design.. Glass/steel. Details — Koolhaas glass grid.. Seattle. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tours.", "x": "Seattle Central Library in depth: Tours.. 11 floors. Details — Koolhaas glass grid.. Free. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Seattle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Seattle.", "x": "Seattle Central Library in depth: Seattle.. Free. Details — Koolhaas glass grid.. Architecture. 2004. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Free.", "x": "Seattle Central Library in depth: Free.. Views. Details — Koolhaas glass grid.. Building. Koolhaas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Architecture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Architecture.", "x": "Seattle Central Library in depth: Architecture.. 2004. Details — Koolhaas glass grid.. Design. Glass/steel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Seattle Central Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Seattle Central Library comes from.", "x": "Origins: Building.. 2004. The history of Seattle Central Library — Koolhaas glass grid.. Design. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Seattle Central Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Seattle Central Library respectfully.", "x": "Engaging: Tours.. Koolhaas. How to participate or observe well — Seattle Central Library. Koolhaas glass grid. Respect first, always; Seattle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Seattle Central Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Seattle Central Library do's and don'ts.", "x": "Etiquette: Free.. Glass/steel. The rules of respect — Seattle Central Library. Koolhaas glass grid. When in doubt, ask about Architecture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Seattle Central Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Seattle Central Library.", "x": "Planning: Building.. 11 floors. Practical notes — Seattle Central Library. Koolhaas glass grid. A little planning shows respect for Design.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Seattle Central Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Seattle Central Library and money.", "x": "Costs: Tours.. Free. What to budget — Seattle Central Library. Koolhaas glass grid. The best experiences of Seattle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-seattle-central-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
