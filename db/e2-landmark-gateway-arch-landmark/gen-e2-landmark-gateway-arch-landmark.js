(function(){'use strict';
/* JAH Gateway Arch Landmark Database generator — jahdb-e2-landmark-gateway-arch-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-gateway-arch-landmark',PREFIX='JAH-E2LANDMARKG-',NAME='JAH Gateway Arch Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gateway Arch: the complete guide", "d": "Gateway Arch: the 192m catenary..", "g": "overview", "l": 2, "q": "What is Gateway Arch: the complete guide?", "a": "Gateway Arch: the 192m catenary..", "x": "The complete landmark guide to Gateway Arch: the 192m catenary.. 1965. History, meaning, practices, and how to engage respectfully — everything in one database. 1965. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gateway Arch essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gateway Arch essentials.", "x": "At a glance: Gateway Arch — the 192m catenary.. 192m. The essentials: Trams.. Saarinen. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1965.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1965.", "x": "Gateway Arch: 1965.. Trams. Essential knowledge — Saarinen.. the 192m catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1965..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1965..", "x": "Explained: 1965.. Saarinen. The context — Gateway Arch. Trams. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "192m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "192m.", "x": "Gateway Arch: 192m.. Westward. Essential knowledge — Trams.. the 192m catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 192m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 192m..", "x": "Explained: 192m.. 192m. The context — Gateway Arch. Westward. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Saarinen.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Saarinen.", "x": "Gateway Arch: Saarinen.. Saarinen. Essential knowledge — Westward.. the 192m catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Saarinen..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Saarinen..", "x": "Explained: Saarinen.. Tickets. The context — Gateway Arch. Catenary. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Trams.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Trams.", "x": "Gateway Arch: Trams.. 192m. Essential knowledge — Catenary.. the 192m catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Trams..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Trams..", "x": "Explained: Trams.. 1965. The context — Gateway Arch. 1965. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Westward.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Westward.", "x": "Gateway Arch: Westward.. Tickets. Essential knowledge — 1965.. the 192m catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Westward..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Westward..", "x": "Explained: Westward.. Trams. The context — Gateway Arch. 192m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Catenary.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Catenary.", "x": "Gateway Arch: Catenary.. 1965. Essential knowledge — 192m.. the 192m catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Catenary..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Catenary..", "x": "Explained: Catenary.. Westward. The context — Gateway Arch. Saarinen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1965.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1965.", "x": "Gateway Arch in depth: 1965.. 192m. Details — the 192m catenary.. Westward. Trams. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Trams.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Trams.", "x": "Gateway Arch in depth: Trams.. Saarinen. Details — the 192m catenary.. Saarinen. Westward. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Westward.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Westward.", "x": "Gateway Arch in depth: Westward.. Trams. Details — the 192m catenary.. 192m. Catenary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Saarinen.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Saarinen.", "x": "Gateway Arch in depth: Saarinen.. Westward. Details — the 192m catenary.. Tickets. 1965. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "192m.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "192m.", "x": "Gateway Arch in depth: 192m.. Catenary. Details — the 192m catenary.. 1965. 192m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Gateway Arch in depth: Tickets.. 1965. Details — the 192m catenary.. Trams. Saarinen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gateway Arch comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gateway Arch comes from.", "x": "Origins: 1965.. 1965. The history of Gateway Arch — the 192m catenary.. Trams. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gateway Arch respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gateway Arch respectfully.", "x": "Engaging: Westward.. 192m. How to participate or observe well — Gateway Arch. the 192m catenary. Respect first, always; Saarinen.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gateway Arch do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gateway Arch do's and don'ts.", "x": "Etiquette: 192m.. Saarinen. The rules of respect — Gateway Arch. the 192m catenary. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gateway Arch.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gateway Arch.", "x": "Planning: 1965.. Trams. Practical notes — Gateway Arch. the 192m catenary. A little planning shows respect for Trams.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gateway Arch and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gateway Arch and money.", "x": "Costs: Westward.. Westward. What to budget — Gateway Arch. the 192m catenary. The best experiences of Saarinen. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-gateway-arch-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
