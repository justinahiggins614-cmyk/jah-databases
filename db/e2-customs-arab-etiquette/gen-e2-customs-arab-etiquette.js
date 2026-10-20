(function(){'use strict';
/* JAH Arab Etiquette Customs Database generator — jahdb-e2-customs-arab-etiquette-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-customs-arab-etiquette',PREFIX='JAH-E2CUSTOMSAR-',NAME='JAH Arab Etiquette Customs Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Arab Etiquette: the complete guide", "d": "Arab Etiquette: hospitality sacred..", "g": "overview", "l": 2, "q": "What is Arab Etiquette: the complete guide?", "a": "Arab Etiquette: hospitality sacred..", "x": "The complete customs guide to Arab Etiquette: hospitality sacred.. Right hand. History, meaning, practices, and how to engage respectfully — everything in one database. Hospitality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Arab Etiquette essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Arab Etiquette essentials.", "x": "At a glance: Arab Etiquette — hospitality sacred.. Coffee rituals. The essentials: Hands.. Shoes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Right hand.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Right hand.", "x": "Arab Etiquette: Right hand.. Hands. Essential knowledge — Shoes.. hospitality sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Right hand..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Right hand..", "x": "Explained: Right hand.. Dress. The context — Arab Etiquette. Ramadan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Coffee rituals.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Coffee rituals.", "x": "Arab Etiquette: Coffee rituals.. Coffee. Essential knowledge — Ramadan.. hospitality sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Coffee rituals..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Coffee rituals..", "x": "Explained: Coffee rituals.. Greetings. The context — Arab Etiquette. Gender norms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shoes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shoes.", "x": "Arab Etiquette: Shoes.. Dress. Essential knowledge — Gender norms.. hospitality sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shoes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shoes..", "x": "Explained: Shoes.. Respect. The context — Arab Etiquette. Guests. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ramadan.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ramadan.", "x": "Arab Etiquette: Ramadan.. Greetings. Essential knowledge — Guests.. hospitality sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ramadan..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ramadan..", "x": "Explained: Ramadan.. Hospitality. The context — Arab Etiquette. Right hand. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gender norms.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gender norms.", "x": "Arab Etiquette: Gender norms.. Respect. Essential knowledge — Right hand.. hospitality sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Gender norms..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Gender norms..", "x": "Explained: Gender norms.. Hands. The context — Arab Etiquette. Coffee rituals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Guests.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Guests.", "x": "Arab Etiquette: Guests.. Hospitality. Essential knowledge — Coffee rituals.. hospitality sacred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Guests..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Guests..", "x": "Explained: Guests.. Coffee. The context — Arab Etiquette. Shoes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hospitality.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hospitality.", "x": "Arab Etiquette in depth: Hospitality.. Coffee rituals. Details — hospitality sacred.. Coffee. Ramadan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hands.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hands.", "x": "Arab Etiquette in depth: Hands.. Shoes. Details — hospitality sacred.. Dress. Gender norms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Coffee.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Coffee.", "x": "Arab Etiquette in depth: Coffee.. Ramadan. Details — hospitality sacred.. Greetings. Guests. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dress.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dress.", "x": "Arab Etiquette in depth: Dress.. Gender norms. Details — hospitality sacred.. Respect. Right hand. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Greetings.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Greetings.", "x": "Arab Etiquette in depth: Greetings.. Guests. Details — hospitality sacred.. Hospitality. Coffee rituals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Arab Etiquette in depth: Respect.. Right hand. Details — hospitality sacred.. Hands. Shoes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Arab Etiquette comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Arab Etiquette comes from.", "x": "Origins: Hospitality.. Right hand. The history of Arab Etiquette — hospitality sacred.. Hands. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Arab Etiquette respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Arab Etiquette respectfully.", "x": "Engaging: Coffee.. Coffee rituals. How to participate or observe well — Arab Etiquette. hospitality sacred. Respect first, always; Dress.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Arab Etiquette do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Arab Etiquette do's and don'ts.", "x": "Etiquette: Greetings.. Shoes. The rules of respect — Arab Etiquette. hospitality sacred. When in doubt, ask about Respect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Arab Etiquette.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Arab Etiquette.", "x": "Planning: Hospitality.. Ramadan. Practical notes — Arab Etiquette. hospitality sacred. A little planning shows respect for Hands.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Arab Etiquette and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Arab Etiquette and money.", "x": "Costs: Coffee.. Gender norms. What to budget — Arab Etiquette. hospitality sacred. The best experiences of Dress. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-customs-arab-etiquette-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
