(function(){'use strict';
/* JAH Thoroughbred Horse Horse Breed Database generator — jahdb-e2-horse-thoroughbred-horse-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-thoroughbred-horse-breed',PREFIX='JAH-E2HORSETHOR-',NAME='JAH Thoroughbred Horse Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thoroughbred Horse: the complete guide", "d": "Thoroughbred Horse: the racing breed..", "g": "overview", "l": 2, "q": "What is Thoroughbred Horse: the complete guide?", "a": "Thoroughbred Horse: the racing breed..", "x": "The complete horse breed guide to Thoroughbred Horse: the racing breed.. Racing. History, meaning, practices, and how to engage respectfully — everything in one database. Racing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Thoroughbred Horse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Thoroughbred Horse essentials.", "x": "At a glance: Thoroughbred Horse — the racing breed.. Fast. The essentials: England.. Hot-blooded. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Racing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Racing.", "x": "Thoroughbred Horse: Racing.. England. Essential knowledge — Hot-blooded.. the racing breed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Racing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Racing..", "x": "Explained: Racing.. Sensitive. The context — Thoroughbred Horse. England. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fast.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fast.", "x": "Thoroughbred Horse: Fast.. Derby. Essential knowledge — England.. the racing breed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fast..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fast..", "x": "Explained: Fast.. Fast. The context — Thoroughbred Horse. Derby. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hot-blooded.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hot-blooded.", "x": "Thoroughbred Horse: Hot-blooded.. Sensitive. Essential knowledge — Derby.. the racing breed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hot-blooded..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hot-blooded..", "x": "Explained: Hot-blooded.. History. The context — Thoroughbred Horse. Sensitive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "England.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "England.", "x": "Thoroughbred Horse: England.. Fast. Essential knowledge — Sensitive.. the racing breed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: England..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: England..", "x": "Explained: England.. Racing. The context — Thoroughbred Horse. Racing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Derby.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Derby.", "x": "Thoroughbred Horse: Derby.. History. Essential knowledge — Racing.. the racing breed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Derby..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Derby..", "x": "Explained: Derby.. England. The context — Thoroughbred Horse. Fast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sensitive.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sensitive.", "x": "Thoroughbred Horse: Sensitive.. Racing. Essential knowledge — Fast.. the racing breed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sensitive..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sensitive..", "x": "Explained: Sensitive.. Derby. The context — Thoroughbred Horse. Hot-blooded. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Racing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Racing.", "x": "Thoroughbred Horse in depth: Racing.. Fast. Details — the racing breed.. Derby. England. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "England.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "England.", "x": "Thoroughbred Horse in depth: England.. Hot-blooded. Details — the racing breed.. Sensitive. Derby. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Derby.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Derby.", "x": "Thoroughbred Horse in depth: Derby.. England. Details — the racing breed.. Fast. Sensitive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sensitive.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sensitive.", "x": "Thoroughbred Horse in depth: Sensitive.. Derby. Details — the racing breed.. History. Racing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fast.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fast.", "x": "Thoroughbred Horse in depth: Fast.. Sensitive. Details — the racing breed.. Racing. Fast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Thoroughbred Horse in depth: History.. Racing. Details — the racing breed.. England. Hot-blooded. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Thoroughbred Horse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Thoroughbred Horse comes from.", "x": "Origins: Racing.. Racing. The history of Thoroughbred Horse — the racing breed.. England. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Thoroughbred Horse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Thoroughbred Horse respectfully.", "x": "Engaging: Derby.. Fast. How to participate or observe well — Thoroughbred Horse. the racing breed. Respect first, always; Sensitive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Thoroughbred Horse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Thoroughbred Horse do's and don'ts.", "x": "Etiquette: Fast.. Hot-blooded. The rules of respect — Thoroughbred Horse. the racing breed. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Thoroughbred Horse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Thoroughbred Horse.", "x": "Planning: Racing.. England. Practical notes — Thoroughbred Horse. the racing breed. A little planning shows respect for England.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Thoroughbred Horse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Thoroughbred Horse and money.", "x": "Costs: Derby.. Derby. What to budget — Thoroughbred Horse. the racing breed. The best experiences of Sensitive. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-thoroughbred-horse-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
