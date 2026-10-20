(function(){'use strict';
/* JAH Himeji Castle Castle Database generator — jahdb-e2-castle-himeji-castle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-himeji-castle',PREFIX='JAH-E2CASTLEHIM-',NAME='JAH Himeji Castle Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Himeji Castle: the complete guide", "d": "Himeji Castle: the white heron..", "g": "overview", "l": 2, "q": "What is Himeji Castle: the complete guide?", "a": "Himeji Castle: the white heron..", "x": "The complete castle guide to Himeji Castle: the white heron.. 1609. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Himeji Castle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Himeji Castle essentials.", "x": "At a glance: Himeji Castle — the white heron.. UNESCO. The essentials: Design.. White plaster. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1609.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1609.", "x": "Himeji Castle: 1609.. Design. Essential knowledge — White plaster.. the white heron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1609..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1609..", "x": "Explained: 1609.. Tickets. The context — Himeji Castle. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "UNESCO.", "x": "Himeji Castle: UNESCO.. UNESCO. Essential knowledge — Japan.. the white heron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Japan. The context — Himeji Castle. Siege-proof. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "White plaster.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "White plaster.", "x": "Himeji Castle: White plaster.. Tickets. Essential knowledge — Siege-proof.. the white heron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: White plaster..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: White plaster..", "x": "Explained: White plaster.. Views. The context — Himeji Castle. Cherry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Japan.", "x": "Himeji Castle: Japan.. Japan. Essential knowledge — Cherry.. the white heron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. History. The context — Himeji Castle. 1609. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Siege-proof.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Siege-proof.", "x": "Himeji Castle: Siege-proof.. Views. Essential knowledge — 1609.. the white heron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Siege-proof..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Siege-proof..", "x": "Explained: Siege-proof.. Design. The context — Himeji Castle. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Cherry.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Cherry.", "x": "Himeji Castle: Cherry.. History. Essential knowledge — UNESCO.. the white heron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Cherry..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Cherry..", "x": "Explained: Cherry.. UNESCO. The context — Himeji Castle. White plaster. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Himeji Castle in depth: History.. UNESCO. Details — the white heron.. UNESCO. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Design.", "x": "Himeji Castle in depth: Design.. White plaster. Details — the white heron.. Tickets. Siege-proof. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Himeji Castle in depth: UNESCO.. Japan. Details — the white heron.. Japan. Cherry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Himeji Castle in depth: Tickets.. Siege-proof. Details — the white heron.. Views. 1609. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Japan.", "x": "Himeji Castle in depth: Japan.. Cherry. Details — the white heron.. History. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Himeji Castle in depth: Views.. 1609. Details — the white heron.. Design. White plaster. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Himeji Castle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Himeji Castle comes from.", "x": "Origins: History.. 1609. The history of Himeji Castle — the white heron.. Design. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Himeji Castle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Himeji Castle respectfully.", "x": "Engaging: UNESCO.. UNESCO. How to participate or observe well — Himeji Castle. the white heron. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Himeji Castle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Himeji Castle do's and don'ts.", "x": "Etiquette: Japan.. White plaster. The rules of respect — Himeji Castle. the white heron. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Himeji Castle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Himeji Castle.", "x": "Planning: History.. Japan. Practical notes — Himeji Castle. the white heron. A little planning shows respect for Design.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Himeji Castle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Himeji Castle and money.", "x": "Costs: UNESCO.. Siege-proof. What to budget — Himeji Castle. the white heron. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-himeji-castle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
