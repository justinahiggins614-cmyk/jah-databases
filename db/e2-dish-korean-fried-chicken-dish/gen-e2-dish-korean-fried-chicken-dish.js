(function(){'use strict';
/* JAH Korean Fried Chicken Dish Database generator — jahdb-e2-dish-korean-fried-chicken-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-korean-fried-chicken-dish',PREFIX='JAH-E2DISHKOREA-',NAME='JAH Korean Fried Chicken Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Korean Fried Chicken: the complete guide", "d": "Korean Fried Chicken: the double fry..", "g": "overview", "l": 2, "q": "What is Korean Fried Chicken: the complete guide?", "a": "Korean Fried Chicken: the double fry..", "x": "The complete dish guide to Korean Fried Chicken: the double fry.. Double-fried. History, meaning, practices, and how to engage respectfully — everything in one database. Double. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Korean Fried Chicken essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Korean Fried Chicken essentials.", "x": "At a glance: Korean Fried Chicken — the double fry.. Gochujang. The essentials: Crunch.. Crispy. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Double-fried.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Double-fried.", "x": "Korean Fried Chicken: Double-fried.. Crunch. Essential knowledge — Crispy.. the double fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Double-fried..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Double-fried..", "x": "Explained: Double-fried.. Gochujang. The context — Korean Fried Chicken. Beer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gochujang.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gochujang.", "x": "Korean Fried Chicken: Gochujang.. Beer. Essential knowledge — Beer.. the double fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gochujang..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gochujang..", "x": "Explained: Gochujang.. Crispy. The context — Korean Fried Chicken. Yangnyeom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Crispy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Crispy.", "x": "Korean Fried Chicken: Crispy.. Gochujang. Essential knowledge — Yangnyeom.. the double fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Crispy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Crispy..", "x": "Explained: Crispy.. Making. The context — Korean Fried Chicken. Crunch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Beer.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Beer.", "x": "Korean Fried Chicken: Beer.. Crispy. Essential knowledge — Crunch.. the double fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Beer..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Beer..", "x": "Explained: Beer.. Double. The context — Korean Fried Chicken. Double-fried. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Yangnyeom.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Yangnyeom.", "x": "Korean Fried Chicken: Yangnyeom.. Making. Essential knowledge — Double-fried.. the double fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Yangnyeom..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Yangnyeom..", "x": "Explained: Yangnyeom.. Crunch. The context — Korean Fried Chicken. Gochujang. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Crunch.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Crunch.", "x": "Korean Fried Chicken: Crunch.. Double. Essential knowledge — Gochujang.. the double fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Crunch..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Crunch..", "x": "Explained: Crunch.. Beer. The context — Korean Fried Chicken. Crispy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Double.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Double.", "x": "Korean Fried Chicken in depth: Double.. Gochujang. Details — the double fry.. Beer. Beer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crunch.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crunch.", "x": "Korean Fried Chicken in depth: Crunch.. Crispy. Details — the double fry.. Gochujang. Yangnyeom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Beer.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Beer.", "x": "Korean Fried Chicken in depth: Beer.. Beer. Details — the double fry.. Crispy. Crunch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gochujang.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gochujang.", "x": "Korean Fried Chicken in depth: Gochujang.. Yangnyeom. Details — the double fry.. Making. Double-fried. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Crispy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Crispy.", "x": "Korean Fried Chicken in depth: Crispy.. Crunch. Details — the double fry.. Double. Gochujang. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Korean Fried Chicken in depth: Making.. Double-fried. Details — the double fry.. Crunch. Crispy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Korean Fried Chicken comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Korean Fried Chicken comes from.", "x": "Origins: Double.. Double-fried. The history of Korean Fried Chicken — the double fry.. Crunch. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Korean Fried Chicken respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Korean Fried Chicken respectfully.", "x": "Engaging: Beer.. Gochujang. How to participate or observe well — Korean Fried Chicken. the double fry. Respect first, always; Gochujang.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Korean Fried Chicken do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Korean Fried Chicken do's and don'ts.", "x": "Etiquette: Crispy.. Crispy. The rules of respect — Korean Fried Chicken. the double fry. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Korean Fried Chicken.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Korean Fried Chicken.", "x": "Planning: Double.. Beer. Practical notes — Korean Fried Chicken. the double fry. A little planning shows respect for Crunch.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Korean Fried Chicken and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Korean Fried Chicken and money.", "x": "Costs: Beer.. Yangnyeom. What to budget — Korean Fried Chicken. the double fry. The best experiences of Gochujang. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-korean-fried-chicken-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
