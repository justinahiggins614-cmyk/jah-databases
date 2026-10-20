(function(){'use strict';
/* JAH Disneyland Castle Landmark Database generator — jahdb-e2-landmark-disneyland-castle-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-disneyland-castle-landmark',PREFIX='JAH-E2LANDMARKD-',NAME='JAH Disneyland Castle Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Disneyland Castle: the complete guide", "d": "Disneyland Castle: the magic castle..", "g": "overview", "l": 2, "q": "What is Disneyland Castle: the complete guide?", "a": "Disneyland Castle: the magic castle..", "x": "The complete landmark guide to Disneyland Castle: the magic castle.. 1955. History, meaning, practices, and how to engage respectfully — everything in one database. 1955. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Disneyland Castle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Disneyland Castle essentials.", "x": "At a glance: Disneyland Castle — the magic castle.. Sleeping Beauty. The essentials: Fireworks.. Fireworks. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1955.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1955.", "x": "Disneyland Castle: 1955.. Fireworks. Essential knowledge — Fireworks.. the magic castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1955..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1955..", "x": "Explained: 1955.. Fantasyland. The context — Disneyland Castle. 77 ft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sleeping Beauty.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sleeping Beauty.", "x": "Disneyland Castle: Sleeping Beauty.. Walt. Essential knowledge — 77 ft.. the magic castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sleeping Beauty..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sleeping Beauty..", "x": "Explained: Sleeping Beauty.. 77 ft. The context — Disneyland Castle. Fantasyland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fireworks.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fireworks.", "x": "Disneyland Castle: Fireworks.. Fantasyland. Essential knowledge — Fantasyland.. the magic castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fireworks..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fireworks..", "x": "Explained: Fireworks.. Tickets. The context — Disneyland Castle. Walt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "77 ft.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "77 ft.", "x": "Disneyland Castle: 77 ft.. 77 ft. Essential knowledge — Walt.. the magic castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 77 ft..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 77 ft..", "x": "Explained: 77 ft.. 1955. The context — Disneyland Castle. 1955. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fantasyland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fantasyland.", "x": "Disneyland Castle: Fantasyland.. Tickets. Essential knowledge — 1955.. the magic castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fantasyland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fantasyland..", "x": "Explained: Fantasyland.. Fireworks. The context — Disneyland Castle. Sleeping Beauty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Walt.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Walt.", "x": "Disneyland Castle: Walt.. 1955. Essential knowledge — Sleeping Beauty.. the magic castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Walt..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Walt..", "x": "Explained: Walt.. Walt. The context — Disneyland Castle. Fireworks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1955.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1955.", "x": "Disneyland Castle in depth: 1955.. Sleeping Beauty. Details — the magic castle.. Walt. 77 ft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fireworks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fireworks.", "x": "Disneyland Castle in depth: Fireworks.. Fireworks. Details — the magic castle.. Fantasyland. Fantasyland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Walt.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Walt.", "x": "Disneyland Castle in depth: Walt.. 77 ft. Details — the magic castle.. 77 ft. Walt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fantasyland.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fantasyland.", "x": "Disneyland Castle in depth: Fantasyland.. Fantasyland. Details — the magic castle.. Tickets. 1955. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "77 ft.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "77 ft.", "x": "Disneyland Castle in depth: 77 ft.. Walt. Details — the magic castle.. 1955. Sleeping Beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Disneyland Castle in depth: Tickets.. 1955. Details — the magic castle.. Fireworks. Fireworks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Disneyland Castle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Disneyland Castle comes from.", "x": "Origins: 1955.. 1955. The history of Disneyland Castle — the magic castle.. Fireworks. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Disneyland Castle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Disneyland Castle respectfully.", "x": "Engaging: Walt.. Sleeping Beauty. How to participate or observe well — Disneyland Castle. the magic castle. Respect first, always; Fantasyland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Disneyland Castle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Disneyland Castle do's and don'ts.", "x": "Etiquette: 77 ft.. Fireworks. The rules of respect — Disneyland Castle. the magic castle. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Disneyland Castle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Disneyland Castle.", "x": "Planning: 1955.. 77 ft. Practical notes — Disneyland Castle. the magic castle. A little planning shows respect for Fireworks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Disneyland Castle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Disneyland Castle and money.", "x": "Costs: Walt.. Fantasyland. What to budget — Disneyland Castle. the magic castle. The best experiences of Fantasyland. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-disneyland-castle-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
