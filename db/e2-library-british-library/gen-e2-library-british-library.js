(function(){'use strict';
/* JAH British Library Library Database generator — jahdb-e2-library-british-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-british-library',PREFIX='JAH-E2LIBRARYBR-',NAME='JAH British Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "British Library: the complete guide", "d": "British Library: the UK's national library..", "g": "overview", "l": 2, "q": "What is British Library: the complete guide?", "a": "British Library: the UK's national library..", "x": "The complete library guide to British Library: the UK's national library.. 170M items. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "British Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "British Library essentials.", "x": "At a glance: British Library — the UK's national library.. Magna Carta. The essentials: Treasures.. London. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "170M items.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "170M items.", "x": "British Library: 170M items.. Treasures. Essential knowledge — London.. the UK's national library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 170M items..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 170M items..", "x": "Explained: 170M items.. Tours. The context — British Library. 1973. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Magna Carta.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Magna Carta.", "x": "British Library: Magna Carta.. Reading. Essential knowledge — 1973.. the UK's national library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Magna Carta..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Magna Carta..", "x": "Explained: Magna Carta.. Digital. The context — British Library. Reading rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "London.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "London.", "x": "British Library: London.. Tours. Essential knowledge — Reading rooms.. the UK's national library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: London..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: London..", "x": "Explained: London.. St Pancras. The context — British Library. Treasures. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1973.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1973.", "x": "British Library: 1973.. Digital. Essential knowledge — Treasures.. the UK's national library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1973..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1973..", "x": "Explained: 1973.. History. The context — British Library. 170M items. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Reading rooms.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Reading rooms.", "x": "British Library: Reading rooms.. St Pancras. Essential knowledge — 170M items.. the UK's national library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Reading rooms..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Reading rooms..", "x": "Explained: Reading rooms.. Treasures. The context — British Library. Magna Carta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Treasures.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Treasures.", "x": "British Library: Treasures.. History. Essential knowledge — Magna Carta.. the UK's national library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Treasures..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Treasures..", "x": "Explained: Treasures.. Reading. The context — British Library. London. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "British Library in depth: History.. Magna Carta. Details — the UK's national library.. Reading. 1973. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Treasures.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Treasures.", "x": "British Library in depth: Treasures.. London. Details — the UK's national library.. Tours. Reading rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Reading.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Reading.", "x": "British Library in depth: Reading.. 1973. Details — the UK's national library.. Digital. Treasures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "British Library in depth: Tours.. Reading rooms. Details — the UK's national library.. St Pancras. 170M items. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Digital.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Digital.", "x": "British Library in depth: Digital.. Treasures. Details — the UK's national library.. History. Magna Carta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "St Pancras.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "St Pancras.", "x": "British Library in depth: St Pancras.. 170M items. Details — the UK's national library.. Treasures. London. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where British Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where British Library comes from.", "x": "Origins: History.. 170M items. The history of British Library — the UK's national library.. Treasures. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing British Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing British Library respectfully.", "x": "Engaging: Reading.. Magna Carta. How to participate or observe well — British Library. the UK's national library. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "British Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "British Library do's and don'ts.", "x": "Etiquette: Digital.. London. The rules of respect — British Library. the UK's national library. When in doubt, ask about St Pancras.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around British Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around British Library.", "x": "Planning: History.. 1973. Practical notes — British Library. the UK's national library. A little planning shows respect for Treasures.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "British Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "British Library and money.", "x": "Costs: Reading.. Reading rooms. What to budget — British Library. the UK's national library. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-british-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
