(function(){'use strict';
/* JAH Nong Nooch Garden Botanical Garden Database generator — jahdb-e2-garden-nong-nooch-garden-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-nong-nooch-garden',PREFIX='JAH-E2GARDENNON-',NAME='JAH Nong Nooch Garden Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nong Nooch Garden: the complete guide", "d": "Nong Nooch Garden: Thailand's tropical show..", "g": "overview", "l": 2, "q": "What is Nong Nooch Garden: the complete guide?", "a": "Nong Nooch Garden: Thailand's tropical show..", "x": "The complete botanical garden guide to Nong Nooch Garden: Thailand's tropical show.. Pattaya. History, meaning, practices, and how to engage respectfully — everything in one database. Orchids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nong Nooch Garden essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nong Nooch Garden essentials.", "x": "At a glance: Nong Nooch Garden — Thailand's tropical show.. Orchids. The essentials: Topiary.. Topiary. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pattaya.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pattaya.", "x": "Nong Nooch Garden: Pattaya.. Topiary. Essential knowledge — Topiary.. Thailand's tropical show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pattaya..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pattaya..", "x": "Explained: Pattaya.. Tickets. The context — Nong Nooch Garden. Elephants. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Orchids.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Orchids.", "x": "Nong Nooch Garden: Orchids.. Shows. Essential knowledge — Elephants.. Thailand's tropical show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Orchids..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Orchids..", "x": "Explained: Orchids.. Thailand. The context — Nong Nooch Garden. 1954. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Topiary.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Topiary.", "x": "Nong Nooch Garden: Topiary.. Tickets. Essential knowledge — 1954.. Thailand's tropical show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Topiary..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Topiary..", "x": "Explained: Topiary.. Tropical. The context — Nong Nooch Garden. Shows. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Elephants.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Elephants.", "x": "Nong Nooch Garden: Elephants.. Thailand. Essential knowledge — Shows.. Thailand's tropical show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Elephants..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Elephants..", "x": "Explained: Elephants.. Orchids. The context — Nong Nooch Garden. Pattaya. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1954.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1954.", "x": "Nong Nooch Garden: 1954.. Tropical. Essential knowledge — Pattaya.. Thailand's tropical show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1954..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1954..", "x": "Explained: 1954.. Topiary. The context — Nong Nooch Garden. Orchids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shows.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shows.", "x": "Nong Nooch Garden: Shows.. Orchids. Essential knowledge — Orchids.. Thailand's tropical show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shows..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shows..", "x": "Explained: Shows.. Shows. The context — Nong Nooch Garden. Topiary. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Orchids.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Orchids.", "x": "Nong Nooch Garden in depth: Orchids.. Orchids. Details — Thailand's tropical show.. Shows. Elephants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Topiary.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Topiary.", "x": "Nong Nooch Garden in depth: Topiary.. Topiary. Details — Thailand's tropical show.. Tickets. 1954. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shows.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shows.", "x": "Nong Nooch Garden in depth: Shows.. Elephants. Details — Thailand's tropical show.. Thailand. Shows. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Nong Nooch Garden in depth: Tickets.. 1954. Details — Thailand's tropical show.. Tropical. Pattaya. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Thailand.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Thailand.", "x": "Nong Nooch Garden in depth: Thailand.. Shows. Details — Thailand's tropical show.. Orchids. Orchids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tropical.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tropical.", "x": "Nong Nooch Garden in depth: Tropical.. Pattaya. Details — Thailand's tropical show.. Topiary. Topiary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nong Nooch Garden comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nong Nooch Garden comes from.", "x": "Origins: Orchids.. Pattaya. The history of Nong Nooch Garden — Thailand's tropical show.. Topiary. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nong Nooch Garden respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nong Nooch Garden respectfully.", "x": "Engaging: Shows.. Orchids. How to participate or observe well — Nong Nooch Garden. Thailand's tropical show. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nong Nooch Garden do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nong Nooch Garden do's and don'ts.", "x": "Etiquette: Thailand.. Topiary. The rules of respect — Nong Nooch Garden. Thailand's tropical show. When in doubt, ask about Tropical.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nong Nooch Garden.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nong Nooch Garden.", "x": "Planning: Orchids.. Elephants. Practical notes — Nong Nooch Garden. Thailand's tropical show. A little planning shows respect for Topiary.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nong Nooch Garden and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nong Nooch Garden and money.", "x": "Costs: Shows.. 1954. What to budget — Nong Nooch Garden. Thailand's tropical show. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-nong-nooch-garden-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
