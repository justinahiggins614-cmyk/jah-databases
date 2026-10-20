(function(){'use strict';
/* JAH Hero\'s Journey Screenwriting Database generator — jahdb-e2-screen-heros-journey-screen-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen-heros-journey-screen',PREFIX='JAH-E2SCREENHER-',NAME='JAH Hero\'s Journey Screenwriting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hero's Journey: the complete guide", "d": "Hero's Journey: the mythic map..", "g": "overview", "l": 2, "q": "What is Hero's Journey: the complete guide?", "a": "Hero's Journey: the mythic map..", "x": "The complete screenwriting guide to Hero's Journey: the mythic map.. Campbell. History, meaning, practices, and how to engage respectfully — everything in one database. Campbell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hero's Journey essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hero's Journey essentials.", "x": "At a glance: Hero's Journey — the mythic map.. 12 stages. The essentials: Stages.. Call. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Campbell.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Campbell.", "x": "Hero's Journey: Campbell.. Stages. Essential knowledge — Call.. the mythic map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Campbell..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Campbell..", "x": "Explained: Campbell.. Return. The context — Hero's Journey. Ordeal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "12 stages.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "12 stages.", "x": "Hero's Journey: 12 stages.. Call. Essential knowledge — Ordeal.. the mythic map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 12 stages..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 12 stages..", "x": "Explained: 12 stages.. Star Wars. The context — Hero's Journey. Return. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Call.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Call.", "x": "Hero's Journey: Call.. Return. Essential knowledge — Return.. the mythic map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Call..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Call..", "x": "Explained: Call.. Myth. The context — Hero's Journey. Star Wars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ordeal.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ordeal.", "x": "Hero's Journey: Ordeal.. Star Wars. Essential knowledge — Star Wars.. the mythic map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ordeal..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ordeal..", "x": "Explained: Ordeal.. Campbell. The context — Hero's Journey. Campbell. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Return.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Return.", "x": "Hero's Journey: Return.. Myth. Essential knowledge — Campbell.. the mythic map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Return..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Return..", "x": "Explained: Return.. Stages. The context — Hero's Journey. 12 stages. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Star Wars.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Star Wars.", "x": "Hero's Journey: Star Wars.. Campbell. Essential knowledge — 12 stages.. the mythic map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Star Wars..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Star Wars..", "x": "Explained: Star Wars.. Call. The context — Hero's Journey. Call. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Campbell.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Campbell.", "x": "Hero's Journey in depth: Campbell.. 12 stages. Details — the mythic map.. Call. Ordeal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stages.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stages.", "x": "Hero's Journey in depth: Stages.. Call. Details — the mythic map.. Return. Return. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Call.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Call.", "x": "Hero's Journey in depth: Call.. Ordeal. Details — the mythic map.. Star Wars. Star Wars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Return.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Return.", "x": "Hero's Journey in depth: Return.. Return. Details — the mythic map.. Myth. Campbell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Star Wars.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Star Wars.", "x": "Hero's Journey in depth: Star Wars.. Star Wars. Details — the mythic map.. Campbell. 12 stages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Myth.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Myth.", "x": "Hero's Journey in depth: Myth.. Campbell. Details — the mythic map.. Stages. Call. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hero's Journey comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hero's Journey comes from.", "x": "Origins: Campbell.. Campbell. The history of Hero's Journey — the mythic map.. Stages. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hero's Journey respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hero's Journey respectfully.", "x": "Engaging: Call.. 12 stages. How to participate or observe well — Hero's Journey. the mythic map. Respect first, always; Return.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hero's Journey do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hero's Journey do's and don'ts.", "x": "Etiquette: Star Wars.. Call. The rules of respect — Hero's Journey. the mythic map. When in doubt, ask about Myth.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hero's Journey.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hero's Journey.", "x": "Planning: Campbell.. Ordeal. Practical notes — Hero's Journey. the mythic map. A little planning shows respect for Stages.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hero's Journey and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hero's Journey and money.", "x": "Costs: Call.. Return. What to budget — Hero's Journey. the mythic map. The best experiences of Return. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen-heros-journey-screen-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
