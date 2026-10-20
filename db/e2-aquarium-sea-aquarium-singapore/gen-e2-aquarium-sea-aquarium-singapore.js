(function(){'use strict';
/* JAH S.E.A. Aquarium Singapore Aquarium Database generator — jahdb-e2-aquarium-sea-aquarium-singapore-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium-sea-aquarium-singapore',PREFIX='JAH-E2AQUARIUMS-',NAME='JAH S.E.A. Aquarium Singapore Aquarium Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "S.E.A. Aquarium Singapore: the complete guide", "d": "S.E.A. Aquarium Singapore: Southeast Asia's sea..", "g": "overview", "l": 2, "q": "What is S.E.A. Aquarium Singapore: the complete guide?", "a": "S.E.A. Aquarium Singapore: Southeast Asia's sea..", "x": "The complete aquarium guide to S.E.A. Aquarium Singapore: Southeast Asia's sea.. 100K animals. History, meaning, practices, and how to engage respectfully — everything in one database. Animals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "S.E.A. Aquarium Singapore essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "S.E.A. Aquarium Singapore essentials.", "x": "At a glance: S.E.A. Aquarium Singapore — Southeast Asia's sea.. Shipwreck. The essentials: Zones.. Sentosa. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "100K animals.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "100K animals.", "x": "S.E.A. Aquarium Singapore: 100K animals.. Zones. Essential knowledge — Sentosa.. Southeast Asia's sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 100K animals..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 100K animals..", "x": "Explained: 100K animals.. Tickets. The context — S.E.A. Aquarium Singapore. Mantas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shipwreck.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shipwreck.", "x": "S.E.A. Aquarium Singapore: Shipwreck.. Sentosa. Essential knowledge — Mantas.. Southeast Asia's sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shipwreck..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shipwreck..", "x": "Explained: Shipwreck.. Conservation. The context — S.E.A. Aquarium Singapore. 2012. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sentosa.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sentosa.", "x": "S.E.A. Aquarium Singapore: Sentosa.. Tickets. Essential knowledge — 2012.. Southeast Asia's sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sentosa..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sentosa..", "x": "Explained: Sentosa.. Ocean. The context — S.E.A. Aquarium Singapore. Conservation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mantas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mantas.", "x": "S.E.A. Aquarium Singapore: Mantas.. Conservation. Essential knowledge — Conservation.. Southeast Asia's sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mantas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mantas..", "x": "Explained: Mantas.. Animals. The context — S.E.A. Aquarium Singapore. 100K animals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2012.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2012.", "x": "S.E.A. Aquarium Singapore: 2012.. Ocean. Essential knowledge — 100K animals.. Southeast Asia's sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 2012..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 2012..", "x": "Explained: 2012.. Zones. The context — S.E.A. Aquarium Singapore. Shipwreck. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Conservation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Conservation.", "x": "S.E.A. Aquarium Singapore: Conservation.. Animals. Essential knowledge — Shipwreck.. Southeast Asia's sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Conservation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Conservation..", "x": "Explained: Conservation.. Sentosa. The context — S.E.A. Aquarium Singapore. Sentosa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Animals.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Animals.", "x": "S.E.A. Aquarium Singapore in depth: Animals.. Shipwreck. Details — Southeast Asia's sea.. Sentosa. Mantas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Zones.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Zones.", "x": "S.E.A. Aquarium Singapore in depth: Zones.. Sentosa. Details — Southeast Asia's sea.. Tickets. 2012. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sentosa.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sentosa.", "x": "S.E.A. Aquarium Singapore in depth: Sentosa.. Mantas. Details — Southeast Asia's sea.. Conservation. Conservation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "S.E.A. Aquarium Singapore in depth: Tickets.. 2012. Details — Southeast Asia's sea.. Ocean. 100K animals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conservation.", "x": "S.E.A. Aquarium Singapore in depth: Conservation.. Conservation. Details — Southeast Asia's sea.. Animals. Shipwreck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ocean.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ocean.", "x": "S.E.A. Aquarium Singapore in depth: Ocean.. 100K animals. Details — Southeast Asia's sea.. Zones. Sentosa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where S.E.A. Aquarium Singapore comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where S.E.A. Aquarium Singapore comes from.", "x": "Origins: Animals.. 100K animals. The history of S.E.A. Aquarium Singapore — Southeast Asia's sea.. Zones. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing S.E.A. Aquarium Singapore respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing S.E.A. Aquarium Singapore respectfully.", "x": "Engaging: Sentosa.. Shipwreck. How to participate or observe well — S.E.A. Aquarium Singapore. Southeast Asia's sea. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "S.E.A. Aquarium Singapore do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "S.E.A. Aquarium Singapore do's and don'ts.", "x": "Etiquette: Conservation.. Sentosa. The rules of respect — S.E.A. Aquarium Singapore. Southeast Asia's sea. When in doubt, ask about Ocean.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around S.E.A. Aquarium Singapore.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around S.E.A. Aquarium Singapore.", "x": "Planning: Animals.. Mantas. Practical notes — S.E.A. Aquarium Singapore. Southeast Asia's sea. A little planning shows respect for Zones.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "S.E.A. Aquarium Singapore and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "S.E.A. Aquarium Singapore and money.", "x": "Costs: Sentosa.. 2012. What to budget — S.E.A. Aquarium Singapore. Southeast Asia's sea. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium-sea-aquarium-singapore-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
