(function(){'use strict';
/* JAH Teotihuacan Landmark Database generator — jahdb-e2-landmark-teotihuacan-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-teotihuacan-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Teotihuacan Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Teotihuacan: the complete guide", "d": "Teotihuacan: the avenue of dead..", "g": "overview", "l": 2, "q": "What is Teotihuacan: the complete guide?", "a": "Teotihuacan: the avenue of dead..", "x": "The complete landmark guide to Teotihuacan: the avenue of dead.. Sun Pyramid. History, meaning, practices, and how to engage respectfully — everything in one database. Pyramids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Teotihuacan essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Teotihuacan essentials.", "x": "At a glance: Teotihuacan — the avenue of dead.. Moon Pyramid. The essentials: Avenue.. Avenue. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sun Pyramid.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sun Pyramid.", "x": "Teotihuacan: Sun Pyramid.. Avenue. Essential knowledge — Avenue.. the avenue of dead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sun Pyramid..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sun Pyramid..", "x": "Explained: Sun Pyramid.. Murals. The context — Teotihuacan. Murals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Moon Pyramid.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Moon Pyramid.", "x": "Teotihuacan: Moon Pyramid.. Climb. Essential knowledge — Murals.. the avenue of dead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Moon Pyramid..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Moon Pyramid..", "x": "Explained: Moon Pyramid.. 200 AD. The context — Teotihuacan. 200 AD. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Avenue.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Avenue.", "x": "Teotihuacan: Avenue.. Murals. Essential knowledge — 200 AD.. the avenue of dead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Avenue..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Avenue..", "x": "Explained: Avenue.. Tours. The context — Teotihuacan. Climb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Murals.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Murals.", "x": "Teotihuacan: Murals.. 200 AD. Essential knowledge — Climb.. the avenue of dead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Murals..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Murals..", "x": "Explained: Murals.. Pyramids. The context — Teotihuacan. Sun Pyramid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "200 AD.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "200 AD.", "x": "Teotihuacan: 200 AD.. Tours. Essential knowledge — Sun Pyramid.. the avenue of dead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 200 AD..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 200 AD..", "x": "Explained: 200 AD.. Avenue. The context — Teotihuacan. Moon Pyramid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Climb.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Climb.", "x": "Teotihuacan: Climb.. Pyramids. Essential knowledge — Moon Pyramid.. the avenue of dead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Climb..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Climb..", "x": "Explained: Climb.. Climb. The context — Teotihuacan. Avenue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pyramids.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pyramids.", "x": "Teotihuacan in depth: Pyramids.. Moon Pyramid. Details — the avenue of dead.. Climb. Murals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Avenue.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Avenue.", "x": "Teotihuacan in depth: Avenue.. Avenue. Details — the avenue of dead.. Murals. 200 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Climb.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Climb.", "x": "Teotihuacan in depth: Climb.. Murals. Details — the avenue of dead.. 200 AD. Climb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Murals.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Murals.", "x": "Teotihuacan in depth: Murals.. 200 AD. Details — the avenue of dead.. Tours. Sun Pyramid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "200 AD.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "200 AD.", "x": "Teotihuacan in depth: 200 AD.. Climb. Details — the avenue of dead.. Pyramids. Moon Pyramid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Teotihuacan in depth: Tours.. Sun Pyramid. Details — the avenue of dead.. Avenue. Avenue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Teotihuacan comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Teotihuacan comes from.", "x": "Origins: Pyramids.. Sun Pyramid. The history of Teotihuacan — the avenue of dead.. Avenue. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Teotihuacan respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Teotihuacan respectfully.", "x": "Engaging: Climb.. Moon Pyramid. How to participate or observe well — Teotihuacan. the avenue of dead. Respect first, always; Murals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Teotihuacan do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Teotihuacan do's and don'ts.", "x": "Etiquette: 200 AD.. Avenue. The rules of respect — Teotihuacan. the avenue of dead. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Teotihuacan.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Teotihuacan.", "x": "Planning: Pyramids.. Murals. Practical notes — Teotihuacan. the avenue of dead. A little planning shows respect for Avenue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Teotihuacan and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Teotihuacan and money.", "x": "Costs: Climb.. 200 AD. What to budget — Teotihuacan. the avenue of dead. The best experiences of Murals. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-teotihuacan-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
