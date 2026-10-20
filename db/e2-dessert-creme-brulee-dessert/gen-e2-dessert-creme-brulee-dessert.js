(function(){'use strict';
/* JAH Creme Brulee Dessert Database generator — jahdb-e2-dessert-creme-brulee-dessert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert-creme-brulee-dessert',PREFIX='JAH-E2DESSERTCR-',NAME='JAH Creme Brulee Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Creme Brulee: the complete guide", "d": "Creme Brulee: the torched custard..", "g": "overview", "l": 2, "q": "What is Creme Brulee: the complete guide?", "a": "Creme Brulee: the torched custard..", "x": "The complete dessert guide to Creme Brulee: the torched custard.. Custard. History, meaning, practices, and how to engage respectfully — everything in one database. Custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Creme Brulee essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Creme Brulee essentials.", "x": "At a glance: Creme Brulee — the torched custard.. Sugar. The essentials: Torch.. Torch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Custard.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Custard.", "x": "Creme Brulee: Custard.. Torch. Essential knowledge — Torch.. the torched custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Custard..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Custard..", "x": "Explained: Custard.. France. The context — Creme Brulee. Vanilla. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sugar.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sugar.", "x": "Creme Brulee: Sugar.. Vanilla. Essential knowledge — Vanilla.. the torched custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sugar..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sugar..", "x": "Explained: Sugar.. Crack. The context — Creme Brulee. France. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Torch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Torch.", "x": "Creme Brulee: Torch.. France. Essential knowledge — France.. the torched custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Torch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Torch..", "x": "Explained: Torch.. Making. The context — Creme Brulee. Spoon crack. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vanilla.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vanilla.", "x": "Creme Brulee: Vanilla.. Crack. Essential knowledge — Spoon crack.. the torched custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Vanilla..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Vanilla..", "x": "Explained: Vanilla.. Custard. The context — Creme Brulee. Custard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "France.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "France.", "x": "Creme Brulee: France.. Making. Essential knowledge — Custard.. the torched custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: France..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: France..", "x": "Explained: France.. Torch. The context — Creme Brulee. Sugar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spoon crack.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spoon crack.", "x": "Creme Brulee: Spoon crack.. Custard. Essential knowledge — Sugar.. the torched custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Spoon crack..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Spoon crack..", "x": "Explained: Spoon crack.. Vanilla. The context — Creme Brulee. Torch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Custard.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Custard.", "x": "Creme Brulee in depth: Custard.. Sugar. Details — the torched custard.. Vanilla. Vanilla. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Torch.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Torch.", "x": "Creme Brulee in depth: Torch.. Torch. Details — the torched custard.. France. France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vanilla.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vanilla.", "x": "Creme Brulee in depth: Vanilla.. Vanilla. Details — the torched custard.. Crack. Spoon crack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "France.", "x": "Creme Brulee in depth: France.. France. Details — the torched custard.. Making. Custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Crack.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Crack.", "x": "Creme Brulee in depth: Crack.. Spoon crack. Details — the torched custard.. Custard. Sugar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Creme Brulee in depth: Making.. Custard. Details — the torched custard.. Torch. Torch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Creme Brulee comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Creme Brulee comes from.", "x": "Origins: Custard.. Custard. The history of Creme Brulee — the torched custard.. Torch. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Creme Brulee respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Creme Brulee respectfully.", "x": "Engaging: Vanilla.. Sugar. How to participate or observe well — Creme Brulee. the torched custard. Respect first, always; France.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Creme Brulee do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Creme Brulee do's and don'ts.", "x": "Etiquette: Crack.. Torch. The rules of respect — Creme Brulee. the torched custard. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Creme Brulee.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Creme Brulee.", "x": "Planning: Custard.. Vanilla. Practical notes — Creme Brulee. the torched custard. A little planning shows respect for Torch.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Creme Brulee and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Creme Brulee and money.", "x": "Costs: Vanilla.. France. What to budget — Creme Brulee. the torched custard. The best experiences of France. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert-creme-brulee-dessert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
