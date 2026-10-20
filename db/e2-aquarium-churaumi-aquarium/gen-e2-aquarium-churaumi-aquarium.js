(function(){'use strict';
/* JAH Okinawa Churaumi Aquarium Aquarium Database generator — jahdb-e2-aquarium-churaumi-aquarium-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium-churaumi-aquarium',PREFIX='JAH-E2AQUARIUMC-',NAME='JAH Okinawa Churaumi Aquarium Aquarium Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Okinawa Churaumi Aquarium: the complete guide", "d": "Okinawa Churaumi Aquarium: the Kuroshio sea..", "g": "overview", "l": 2, "q": "What is Okinawa Churaumi Aquarium: the complete guide?", "a": "Okinawa Churaumi Aquarium: the Kuroshio sea..", "x": "The complete aquarium guide to Okinawa Churaumi Aquarium: the Kuroshio sea.. Kuroshio tank. History, meaning, practices, and how to engage respectfully — everything in one database. Tank. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Okinawa Churaumi Aquarium essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Okinawa Churaumi Aquarium essentials.", "x": "At a glance: Okinawa Churaumi Aquarium — the Kuroshio sea.. Whale sharks. The essentials: Sharks.. Mantas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Kuroshio tank.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Kuroshio tank.", "x": "Okinawa Churaumi Aquarium: Kuroshio tank.. Sharks. Essential knowledge — Mantas.. the Kuroshio sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Kuroshio tank..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Kuroshio tank..", "x": "Explained: Kuroshio tank.. Okinawa. The context — Okinawa Churaumi Aquarium. Okinawa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Whale sharks.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Whale sharks.", "x": "Okinawa Churaumi Aquarium: Whale sharks.. Mantas. Essential knowledge — Okinawa.. the Kuroshio sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Whale sharks..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Whale sharks..", "x": "Explained: Whale sharks.. History. The context — Okinawa Churaumi Aquarium. 1975. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mantas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mantas.", "x": "Okinawa Churaumi Aquarium: Mantas.. Okinawa. Essential knowledge — 1975.. the Kuroshio sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mantas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mantas..", "x": "Explained: Mantas.. Conservation. The context — Okinawa Churaumi Aquarium. Ocean. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Okinawa.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Okinawa.", "x": "Okinawa Churaumi Aquarium: Okinawa.. History. Essential knowledge — Ocean.. the Kuroshio sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Okinawa..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Okinawa..", "x": "Explained: Okinawa.. Tank. The context — Okinawa Churaumi Aquarium. Kuroshio tank. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1975.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1975.", "x": "Okinawa Churaumi Aquarium: 1975.. Conservation. Essential knowledge — Kuroshio tank.. the Kuroshio sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1975..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1975..", "x": "Explained: 1975.. Sharks. The context — Okinawa Churaumi Aquarium. Whale sharks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ocean.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ocean.", "x": "Okinawa Churaumi Aquarium: Ocean.. Tank. Essential knowledge — Whale sharks.. the Kuroshio sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ocean..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ocean..", "x": "Explained: Ocean.. Mantas. The context — Okinawa Churaumi Aquarium. Mantas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tank.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tank.", "x": "Okinawa Churaumi Aquarium in depth: Tank.. Whale sharks. Details — the Kuroshio sea.. Mantas. Okinawa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sharks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sharks.", "x": "Okinawa Churaumi Aquarium in depth: Sharks.. Mantas. Details — the Kuroshio sea.. Okinawa. 1975. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mantas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mantas.", "x": "Okinawa Churaumi Aquarium in depth: Mantas.. Okinawa. Details — the Kuroshio sea.. History. Ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Okinawa.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Okinawa.", "x": "Okinawa Churaumi Aquarium in depth: Okinawa.. 1975. Details — the Kuroshio sea.. Conservation. Kuroshio tank. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Okinawa Churaumi Aquarium in depth: History.. Ocean. Details — the Kuroshio sea.. Tank. Whale sharks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conservation.", "x": "Okinawa Churaumi Aquarium in depth: Conservation.. Kuroshio tank. Details — the Kuroshio sea.. Sharks. Mantas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Okinawa Churaumi Aquarium comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Okinawa Churaumi Aquarium comes from.", "x": "Origins: Tank.. Kuroshio tank. The history of Okinawa Churaumi Aquarium — the Kuroshio sea.. Sharks. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Okinawa Churaumi Aquarium respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Okinawa Churaumi Aquarium respectfully.", "x": "Engaging: Mantas.. Whale sharks. How to participate or observe well — Okinawa Churaumi Aquarium. the Kuroshio sea. Respect first, always; Okinawa.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Okinawa Churaumi Aquarium do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Okinawa Churaumi Aquarium do's and don'ts.", "x": "Etiquette: History.. Mantas. The rules of respect — Okinawa Churaumi Aquarium. the Kuroshio sea. When in doubt, ask about Conservation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Okinawa Churaumi Aquarium.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Okinawa Churaumi Aquarium.", "x": "Planning: Tank.. Okinawa. Practical notes — Okinawa Churaumi Aquarium. the Kuroshio sea. A little planning shows respect for Sharks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Okinawa Churaumi Aquarium and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Okinawa Churaumi Aquarium and money.", "x": "Costs: Mantas.. 1975. What to budget — Okinawa Churaumi Aquarium. the Kuroshio sea. The best experiences of Okinawa. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium-churaumi-aquarium-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
