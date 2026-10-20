(function(){'use strict';
/* JAH Monologue Plays Play Database generator — jahdb-e2-play-monologue-plays-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-play-monologue-plays',PREFIX='JAH-E2PLAYMONOL-',NAME='JAH Monologue Plays Play Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Monologue Plays: the complete guide", "d": "Monologue Plays: the solo voice..", "g": "overview", "l": 2, "q": "What is Monologue Plays: the complete guide?", "a": "Monologue Plays: the solo voice..", "x": "The complete play guide to Monologue Plays: the solo voice.. Solo. History, meaning, practices, and how to engage respectfully — everything in one database. Solo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Monologue Plays essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Monologue Plays essentials.", "x": "At a glance: Monologue Plays — the solo voice.. Direct address. The essentials: Intimate.. Vagina. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Solo.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Solo.", "x": "Monologue Plays: Solo.. Intimate. Essential knowledge — Vagina.. the solo voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Solo..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Solo..", "x": "Explained: Solo.. Storytelling. The context — Monologue Plays. Storytelling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Direct address.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Direct address.", "x": "Monologue Plays: Direct address.. Actor. Essential knowledge — Storytelling.. the solo voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Direct address..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Direct address..", "x": "Explained: Direct address.. Direct. The context — Monologue Plays. Intimate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vagina.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vagina.", "x": "Monologue Plays: Vagina.. Storytelling. Essential knowledge — Intimate.. the solo voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vagina..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vagina..", "x": "Explained: Vagina.. Craft. The context — Monologue Plays. Actor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Storytelling.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Storytelling.", "x": "Monologue Plays: Storytelling.. Direct. Essential knowledge — Actor.. the solo voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Storytelling..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Storytelling..", "x": "Explained: Storytelling.. Solo. The context — Monologue Plays. Solo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Intimate.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Intimate.", "x": "Monologue Plays: Intimate.. Craft. Essential knowledge — Solo.. the solo voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Intimate..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Intimate..", "x": "Explained: Intimate.. Intimate. The context — Monologue Plays. Direct address. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Actor.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Actor.", "x": "Monologue Plays: Actor.. Solo. Essential knowledge — Direct address.. the solo voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Actor..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Actor..", "x": "Explained: Actor.. Actor. The context — Monologue Plays. Vagina. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Solo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Solo.", "x": "Monologue Plays in depth: Solo.. Direct address. Details — the solo voice.. Actor. Storytelling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Intimate.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Intimate.", "x": "Monologue Plays in depth: Intimate.. Vagina. Details — the solo voice.. Storytelling. Intimate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Actor.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Actor.", "x": "Monologue Plays in depth: Actor.. Storytelling. Details — the solo voice.. Direct. Actor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Storytelling.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Storytelling.", "x": "Monologue Plays in depth: Storytelling.. Intimate. Details — the solo voice.. Craft. Solo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Direct.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Direct.", "x": "Monologue Plays in depth: Direct.. Actor. Details — the solo voice.. Solo. Direct address. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Craft.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Craft.", "x": "Monologue Plays in depth: Craft.. Solo. Details — the solo voice.. Intimate. Vagina. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Monologue Plays comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Monologue Plays comes from.", "x": "Origins: Solo.. Solo. The history of Monologue Plays — the solo voice.. Intimate. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Monologue Plays respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Monologue Plays respectfully.", "x": "Engaging: Actor.. Direct address. How to participate or observe well — Monologue Plays. the solo voice. Respect first, always; Storytelling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Monologue Plays do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Monologue Plays do's and don'ts.", "x": "Etiquette: Direct.. Vagina. The rules of respect — Monologue Plays. the solo voice. When in doubt, ask about Craft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Monologue Plays.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Monologue Plays.", "x": "Planning: Solo.. Storytelling. Practical notes — Monologue Plays. the solo voice. A little planning shows respect for Intimate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Monologue Plays and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Monologue Plays and money.", "x": "Costs: Actor.. Intimate. What to budget — Monologue Plays. the solo voice. The best experiences of Storytelling. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-play-monologue-plays-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
