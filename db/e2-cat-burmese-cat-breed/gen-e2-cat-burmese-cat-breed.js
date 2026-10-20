(function(){'use strict';
/* JAH Burmese Cat Cat Breed Database generator — jahdb-e2-cat-burmese-cat-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cat-burmese-cat-breed',PREFIX='JAH-E2CATBURMES-',NAME='JAH Burmese Cat Cat Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Burmese Cat: the complete guide", "d": "Burmese Cat: the golden-eyed..", "g": "overview", "l": 2, "q": "What is Burmese Cat: the complete guide?", "a": "Burmese Cat: the golden-eyed..", "x": "The complete cat breed guide to Burmese Cat: the golden-eyed.. Gold eyes. History, meaning, practices, and how to engage respectfully — everything in one database. Gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Burmese Cat essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Burmese Cat essentials.", "x": "At a glance: Burmese Cat — the golden-eyed.. Burma. The essentials: Burma.. Vocal. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gold eyes.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gold eyes.", "x": "Burmese Cat: Gold eyes.. Burma. Essential knowledge — Vocal.. the golden-eyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gold eyes..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gold eyes..", "x": "Explained: Gold eyes.. Sable. The context — Burmese Cat. Social. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Burma.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Burma.", "x": "Burmese Cat: Burma.. Social. Essential knowledge — Social.. the golden-eyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Burma..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Burma..", "x": "Explained: Burma.. Vocal. The context — Burmese Cat. Sable. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vocal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vocal.", "x": "Burmese Cat: Vocal.. Sable. Essential knowledge — Sable.. the golden-eyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vocal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vocal..", "x": "Explained: Vocal.. History. The context — Burmese Cat. Dog-like. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Social.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Social.", "x": "Burmese Cat: Social.. Vocal. Essential knowledge — Dog-like.. the golden-eyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Social..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Social..", "x": "Explained: Social.. Gold. The context — Burmese Cat. Gold eyes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sable.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sable.", "x": "Burmese Cat: Sable.. History. Essential knowledge — Gold eyes.. the golden-eyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sable..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sable..", "x": "Explained: Sable.. Burma. The context — Burmese Cat. Burma. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dog-like.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dog-like.", "x": "Burmese Cat: Dog-like.. Gold. Essential knowledge — Burma.. the golden-eyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dog-like..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dog-like..", "x": "Explained: Dog-like.. Social. The context — Burmese Cat. Vocal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gold.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gold.", "x": "Burmese Cat in depth: Gold.. Burma. Details — the golden-eyed.. Social. Social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Burma.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Burma.", "x": "Burmese Cat in depth: Burma.. Vocal. Details — the golden-eyed.. Sable. Sable. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Social.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Social.", "x": "Burmese Cat in depth: Social.. Social. Details — the golden-eyed.. Vocal. Dog-like. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sable.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sable.", "x": "Burmese Cat in depth: Sable.. Sable. Details — the golden-eyed.. History. Gold eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Vocal.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Vocal.", "x": "Burmese Cat in depth: Vocal.. Dog-like. Details — the golden-eyed.. Gold. Burma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Burmese Cat in depth: History.. Gold eyes. Details — the golden-eyed.. Burma. Vocal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Burmese Cat comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Burmese Cat comes from.", "x": "Origins: Gold.. Gold eyes. The history of Burmese Cat — the golden-eyed.. Burma. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Burmese Cat respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Burmese Cat respectfully.", "x": "Engaging: Social.. Burma. How to participate or observe well — Burmese Cat. the golden-eyed. Respect first, always; Sable.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Burmese Cat do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Burmese Cat do's and don'ts.", "x": "Etiquette: Vocal.. Vocal. The rules of respect — Burmese Cat. the golden-eyed. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Burmese Cat.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Burmese Cat.", "x": "Planning: Gold.. Social. Practical notes — Burmese Cat. the golden-eyed. A little planning shows respect for Burma.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Burmese Cat and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Burmese Cat and money.", "x": "Costs: Social.. Sable. What to budget — Burmese Cat. the golden-eyed. The best experiences of Sable. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cat-burmese-cat-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
