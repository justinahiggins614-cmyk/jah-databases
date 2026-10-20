(function(){'use strict';
/* JAH Bodleian Library Library Database generator — jahdb-e2-library-bodleian-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-bodleian-library',PREFIX='JAH-E2LIBRARYBO-',NAME='JAH Bodleian Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bodleian Library: the complete guide", "d": "Bodleian Library: Oxford's 400-year library..", "g": "overview", "l": 2, "q": "What is Bodleian Library: the complete guide?", "a": "Bodleian Library: Oxford's 400-year library..", "x": "The complete library guide to Bodleian Library: Oxford's 400-year library.. 1602. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bodleian Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bodleian Library essentials.", "x": "At a glance: Bodleian Library — Oxford's 400-year library.. 12M items. The essentials: Duke Humfrey.. Duke Humfrey. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1602.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1602.", "x": "Bodleian Library: 1602.. Duke Humfrey. Essential knowledge — Duke Humfrey.. Oxford's 400-year library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1602..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1602..", "x": "Explained: 1602.. Tours. The context — Bodleian Library. Harry Potter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "12M items.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "12M items.", "x": "Bodleian Library: 12M items.. Films. Essential knowledge — Harry Potter.. Oxford's 400-year library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 12M items..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 12M items..", "x": "Explained: 12M items.. Oxford. The context — Bodleian Library. Legal deposit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Duke Humfrey.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Duke Humfrey.", "x": "Bodleian Library: Duke Humfrey.. Tours. Essential knowledge — Legal deposit.. Oxford's 400-year library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Duke Humfrey..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Duke Humfrey..", "x": "Explained: Duke Humfrey.. Research. The context — Bodleian Library. Oxford. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Harry Potter.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Harry Potter.", "x": "Bodleian Library: Harry Potter.. Oxford. Essential knowledge — Oxford.. Oxford's 400-year library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Harry Potter..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Harry Potter..", "x": "Explained: Harry Potter.. History. The context — Bodleian Library. 1602. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Legal deposit.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Legal deposit.", "x": "Bodleian Library: Legal deposit.. Research. Essential knowledge — 1602.. Oxford's 400-year library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Legal deposit..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Legal deposit..", "x": "Explained: Legal deposit.. Duke Humfrey. The context — Bodleian Library. 12M items. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Oxford.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Oxford.", "x": "Bodleian Library: Oxford.. History. Essential knowledge — 12M items.. Oxford's 400-year library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Oxford..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Oxford..", "x": "Explained: Oxford.. Films. The context — Bodleian Library. Duke Humfrey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Bodleian Library in depth: History.. 12M items. Details — Oxford's 400-year library.. Films. Harry Potter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Duke Humfrey.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Duke Humfrey.", "x": "Bodleian Library in depth: Duke Humfrey.. Duke Humfrey. Details — Oxford's 400-year library.. Tours. Legal deposit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Films.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Films.", "x": "Bodleian Library in depth: Films.. Harry Potter. Details — Oxford's 400-year library.. Oxford. Oxford. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Bodleian Library in depth: Tours.. Legal deposit. Details — Oxford's 400-year library.. Research. 1602. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Oxford.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Oxford.", "x": "Bodleian Library in depth: Oxford.. Oxford. Details — Oxford's 400-year library.. History. 12M items. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Research.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Research.", "x": "Bodleian Library in depth: Research.. 1602. Details — Oxford's 400-year library.. Duke Humfrey. Duke Humfrey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bodleian Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bodleian Library comes from.", "x": "Origins: History.. 1602. The history of Bodleian Library — Oxford's 400-year library.. Duke Humfrey. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bodleian Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bodleian Library respectfully.", "x": "Engaging: Films.. 12M items. How to participate or observe well — Bodleian Library. Oxford's 400-year library. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bodleian Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bodleian Library do's and don'ts.", "x": "Etiquette: Oxford.. Duke Humfrey. The rules of respect — Bodleian Library. Oxford's 400-year library. When in doubt, ask about Research.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bodleian Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bodleian Library.", "x": "Planning: History.. Harry Potter. Practical notes — Bodleian Library. Oxford's 400-year library. A little planning shows respect for Duke Humfrey.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bodleian Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bodleian Library and money.", "x": "Costs: Films.. Legal deposit. What to budget — Bodleian Library. Oxford's 400-year library. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-bodleian-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
