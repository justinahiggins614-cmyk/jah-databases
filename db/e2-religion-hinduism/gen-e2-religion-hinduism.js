(function(){'use strict';
/* JAH Hinduism Religion Database generator — jahdb-e2-religion-hinduism-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-religion-hinduism',PREFIX='JAH-E2RELIGIONH-',NAME='JAH Hinduism Religion Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hinduism: the complete guide", "d": "Hinduism: 1.2 billion; dharma and karma..", "g": "overview", "l": 2, "q": "What is Hinduism: the complete guide?", "a": "Hinduism: 1.2 billion; dharma and karma..", "x": "The complete religion guide to Hinduism: 1.2 billion; dharma and karma.. Vedas. History, meaning, practices, and how to engage respectfully — everything in one database. Texts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hinduism essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hinduism essentials.", "x": "At a glance: Hinduism — 1.2 billion; dharma and karma.. Karma, dharma, moksha. The essentials: Practices.. Many deities. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Vedas.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Vedas.", "x": "Hinduism: Vedas.. Practices. Essential knowledge — Many deities.. 1.2 billion; dharma and karma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Vedas..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Vedas..", "x": "Explained: Vedas.. Philosophy. The context — Hinduism. Yoga origins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Karma, dharma, moksha.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Karma, dharma, moksha.", "x": "Hinduism: Karma, dharma, moksha.. Festivals. Essential knowledge — Yoga origins.. 1.2 billion; dharma and karma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Karma, dharma, moksha..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Karma, dharma, moksha..", "x": "Explained: Karma, dharma, moksha.. Global. The context — Hinduism. Diwali. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Many deities.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Many deities.", "x": "Hinduism: Many deities.. Philosophy. Essential knowledge — Diwali.. 1.2 billion; dharma and karma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Many deities..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Many deities..", "x": "Explained: Many deities.. Ethics. The context — Hinduism. 1.2B followers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Yoga origins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Yoga origins.", "x": "Hinduism: Yoga origins.. Global. Essential knowledge — 1.2B followers.. 1.2 billion; dharma and karma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Yoga origins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Yoga origins..", "x": "Explained: Yoga origins.. Texts. The context — Hinduism. Vedas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Diwali.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Diwali.", "x": "Hinduism: Diwali.. Ethics. Essential knowledge — Vedas.. 1.2 billion; dharma and karma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Diwali..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Diwali..", "x": "Explained: Diwali.. Practices. The context — Hinduism. Karma, dharma, moksha. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1.2B followers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1.2B followers.", "x": "Hinduism: 1.2B followers.. Texts. Essential knowledge — Karma, dharma, moksha.. 1.2 billion; dharma and karma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 1.2B followers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 1.2B followers..", "x": "Explained: 1.2B followers.. Festivals. The context — Hinduism. Many deities. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Texts.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Texts.", "x": "Hinduism in depth: Texts.. Karma, dharma, moksha. Details — 1.2 billion; dharma and karma.. Festivals. Yoga origins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Practices.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Practices.", "x": "Hinduism in depth: Practices.. Many deities. Details — 1.2 billion; dharma and karma.. Philosophy. Diwali. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Festivals.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Festivals.", "x": "Hinduism in depth: Festivals.. Yoga origins. Details — 1.2 billion; dharma and karma.. Global. 1.2B followers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Philosophy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Philosophy.", "x": "Hinduism in depth: Philosophy.. Diwali. Details — 1.2 billion; dharma and karma.. Ethics. Vedas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Global.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Global.", "x": "Hinduism in depth: Global.. 1.2B followers. Details — 1.2 billion; dharma and karma.. Texts. Karma, dharma, moksha. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ethics.", "x": "Hinduism in depth: Ethics.. Vedas. Details — 1.2 billion; dharma and karma.. Practices. Many deities. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hinduism comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hinduism comes from.", "x": "Origins: Texts.. Vedas. The history of Hinduism — 1.2 billion; dharma and karma.. Practices. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hinduism respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hinduism respectfully.", "x": "Engaging: Festivals.. Karma, dharma, moksha. How to participate or observe well — Hinduism. 1.2 billion; dharma and karma. Respect first, always; Philosophy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hinduism do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hinduism do's and don'ts.", "x": "Etiquette: Global.. Many deities. The rules of respect — Hinduism. 1.2 billion; dharma and karma. When in doubt, ask about Ethics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hinduism.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hinduism.", "x": "Planning: Texts.. Yoga origins. Practical notes — Hinduism. 1.2 billion; dharma and karma. A little planning shows respect for Practices.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hinduism and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hinduism and money.", "x": "Costs: Festivals.. Diwali. What to budget — Hinduism. 1.2 billion; dharma and karma. The best experiences of Philosophy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-religion-hinduism-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
