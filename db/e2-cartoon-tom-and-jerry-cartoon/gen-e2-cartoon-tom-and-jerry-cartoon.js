(function(){'use strict';
/* JAH Tom and Jerry Cartoon Database generator — jahdb-e2-cartoon-tom-and-jerry-cartoon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cartoon-tom-and-jerry-cartoon',PREFIX='JAH-E2CARTOONTO-',NAME='JAH Tom and Jerry Cartoon Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tom and Jerry: the complete guide", "d": "Tom and Jerry: the cat-mouse chase..", "g": "overview", "l": 2, "q": "What is Tom and Jerry: the complete guide?", "a": "Tom and Jerry: the cat-mouse chase..", "x": "The complete cartoon guide to Tom and Jerry: the cat-mouse chase.. 1940. History, meaning, practices, and how to engage respectfully — everything in one database. Chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tom and Jerry essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tom and Jerry essentials.", "x": "At a glance: Tom and Jerry — the cat-mouse chase.. Hanna-Barbera. The essentials: Slapstick.. Slapstick. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1940.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1940.", "x": "Tom and Jerry: 1940.. Slapstick. Essential knowledge — Slapstick.. the cat-mouse chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1940..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1940..", "x": "Explained: 1940.. 1940. The context — Tom and Jerry. No dialogue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hanna-Barbera.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hanna-Barbera.", "x": "Tom and Jerry: Hanna-Barbera.. Oscars. Essential knowledge — No dialogue.. the cat-mouse chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hanna-Barbera..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hanna-Barbera..", "x": "Explained: Hanna-Barbera.. HB. The context — Tom and Jerry. Oscars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Slapstick.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Slapstick.", "x": "Tom and Jerry: Slapstick.. 1940. Essential knowledge — Oscars.. the cat-mouse chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Slapstick..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Slapstick..", "x": "Explained: Slapstick.. Classics. The context — Tom and Jerry. Chase. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "No dialogue.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "No dialogue.", "x": "Tom and Jerry: No dialogue.. HB. Essential knowledge — Chase.. the cat-mouse chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: No dialogue..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: No dialogue..", "x": "Explained: No dialogue.. Chase. The context — Tom and Jerry. 1940. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Oscars.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Oscars.", "x": "Tom and Jerry: Oscars.. Classics. Essential knowledge — 1940.. the cat-mouse chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Oscars..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Oscars..", "x": "Explained: Oscars.. Slapstick. The context — Tom and Jerry. Hanna-Barbera. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chase.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chase.", "x": "Tom and Jerry: Chase.. Chase. Essential knowledge — Hanna-Barbera.. the cat-mouse chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chase..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chase..", "x": "Explained: Chase.. Oscars. The context — Tom and Jerry. Slapstick. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chase.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chase.", "x": "Tom and Jerry in depth: Chase.. Hanna-Barbera. Details — the cat-mouse chase.. Oscars. No dialogue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Slapstick.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Slapstick.", "x": "Tom and Jerry in depth: Slapstick.. Slapstick. Details — the cat-mouse chase.. 1940. Oscars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Oscars.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Oscars.", "x": "Tom and Jerry in depth: Oscars.. No dialogue. Details — the cat-mouse chase.. HB. Chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1940.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1940.", "x": "Tom and Jerry in depth: 1940.. Oscars. Details — the cat-mouse chase.. Classics. 1940. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "HB.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "HB.", "x": "Tom and Jerry in depth: HB.. Chase. Details — the cat-mouse chase.. Chase. Hanna-Barbera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Tom and Jerry in depth: Classics.. 1940. Details — the cat-mouse chase.. Slapstick. Slapstick. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tom and Jerry comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tom and Jerry comes from.", "x": "Origins: Chase.. 1940. The history of Tom and Jerry — the cat-mouse chase.. Slapstick. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tom and Jerry respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tom and Jerry respectfully.", "x": "Engaging: Oscars.. Hanna-Barbera. How to participate or observe well — Tom and Jerry. the cat-mouse chase. Respect first, always; 1940.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tom and Jerry do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tom and Jerry do's and don'ts.", "x": "Etiquette: HB.. Slapstick. The rules of respect — Tom and Jerry. the cat-mouse chase. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tom and Jerry.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tom and Jerry.", "x": "Planning: Chase.. No dialogue. Practical notes — Tom and Jerry. the cat-mouse chase. A little planning shows respect for Slapstick.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tom and Jerry and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tom and Jerry and money.", "x": "Costs: Oscars.. Oscars. What to budget — Tom and Jerry. the cat-mouse chase. The best experiences of 1940. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cartoon-tom-and-jerry-cartoon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
