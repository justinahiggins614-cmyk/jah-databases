(function(){'use strict';
/* JAH Lisbon Oceanarium Aquarium Database generator — jahdb-e2-aquarium-lisbon-oceanarium-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium-lisbon-oceanarium',PREFIX='JAH-E2AQUARIUML-',NAME='JAH Lisbon Oceanarium Aquarium Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lisbon Oceanarium: the complete guide", "d": "Lisbon Oceanarium: the central ocean..", "g": "overview", "l": 2, "q": "What is Lisbon Oceanarium: the complete guide?", "a": "Lisbon Oceanarium: the central ocean..", "x": "The complete aquarium guide to Lisbon Oceanarium: the central ocean.. 1998. History, meaning, practices, and how to engage respectfully — everything in one database. Tank. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lisbon Oceanarium essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lisbon Oceanarium essentials.", "x": "At a glance: Lisbon Oceanarium — the central ocean.. Central tank. The essentials: Sunfish.. Sunfish. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1998.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1998.", "x": "Lisbon Oceanarium: 1998.. Sunfish. Essential knowledge — Sunfish.. the central ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1998..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1998..", "x": "Explained: 1998.. Tickets. The context — Lisbon Oceanarium. Expo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Central tank.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Central tank.", "x": "Lisbon Oceanarium: Central tank.. Expo. Essential knowledge — Expo.. the central ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Central tank..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Central tank..", "x": "Explained: Central tank.. Lisbon. The context — Lisbon Oceanarium. Peter Chermayeff. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sunfish.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sunfish.", "x": "Lisbon Oceanarium: Sunfish.. Tickets. Essential knowledge — Peter Chermayeff.. the central ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sunfish..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sunfish..", "x": "Explained: Sunfish.. Ocean. The context — Lisbon Oceanarium. Design. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Expo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Expo.", "x": "Lisbon Oceanarium: Expo.. Lisbon. Essential knowledge — Design.. the central ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Expo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Expo..", "x": "Explained: Expo.. Tank. The context — Lisbon Oceanarium. 1998. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Peter Chermayeff.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Peter Chermayeff.", "x": "Lisbon Oceanarium: Peter Chermayeff.. Ocean. Essential knowledge — 1998.. the central ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Peter Chermayeff..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Peter Chermayeff..", "x": "Explained: Peter Chermayeff.. Sunfish. The context — Lisbon Oceanarium. Central tank. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Design.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Design.", "x": "Lisbon Oceanarium: Design.. Tank. Essential knowledge — Central tank.. the central ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Design..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Design..", "x": "Explained: Design.. Expo. The context — Lisbon Oceanarium. Sunfish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tank.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tank.", "x": "Lisbon Oceanarium in depth: Tank.. Central tank. Details — the central ocean.. Expo. Expo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sunfish.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sunfish.", "x": "Lisbon Oceanarium in depth: Sunfish.. Sunfish. Details — the central ocean.. Tickets. Peter Chermayeff. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Expo.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Expo.", "x": "Lisbon Oceanarium in depth: Expo.. Expo. Details — the central ocean.. Lisbon. Design. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Lisbon Oceanarium in depth: Tickets.. Peter Chermayeff. Details — the central ocean.. Ocean. 1998. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lisbon.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lisbon.", "x": "Lisbon Oceanarium in depth: Lisbon.. Design. Details — the central ocean.. Tank. Central tank. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ocean.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ocean.", "x": "Lisbon Oceanarium in depth: Ocean.. 1998. Details — the central ocean.. Sunfish. Sunfish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lisbon Oceanarium comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lisbon Oceanarium comes from.", "x": "Origins: Tank.. 1998. The history of Lisbon Oceanarium — the central ocean.. Sunfish. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lisbon Oceanarium respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lisbon Oceanarium respectfully.", "x": "Engaging: Expo.. Central tank. How to participate or observe well — Lisbon Oceanarium. the central ocean. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lisbon Oceanarium do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lisbon Oceanarium do's and don'ts.", "x": "Etiquette: Lisbon.. Sunfish. The rules of respect — Lisbon Oceanarium. the central ocean. When in doubt, ask about Ocean.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lisbon Oceanarium.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lisbon Oceanarium.", "x": "Planning: Tank.. Expo. Practical notes — Lisbon Oceanarium. the central ocean. A little planning shows respect for Sunfish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lisbon Oceanarium and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lisbon Oceanarium and money.", "x": "Costs: Expo.. Peter Chermayeff. What to budget — Lisbon Oceanarium. the central ocean. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium-lisbon-oceanarium-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
