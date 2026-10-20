(function(){'use strict';
/* JAH Christ the Redeemer Landmark Database generator — jahdb-e2-landmark-christ-redeemer-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-christ-redeemer-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Christ the Redeemer Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Christ the Redeemer: the complete guide", "d": "Christ the Redeemer: the open arms..", "g": "overview", "l": 2, "q": "What is Christ the Redeemer: the complete guide?", "a": "Christ the Redeemer: the open arms..", "x": "The complete landmark guide to Christ the Redeemer: the open arms.. 1931. History, meaning, practices, and how to engage respectfully — everything in one database. 1931. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Christ the Redeemer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Christ the Redeemer essentials.", "x": "At a glance: Christ the Redeemer — the open arms.. 30m. The essentials: Corcovado.. Corcovado. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1931.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1931.", "x": "Christ the Redeemer: 1931.. Corcovado. Essential knowledge — Corcovado.. the open arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1931..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1931..", "x": "Explained: 1931.. Arms. The context — Christ the Redeemer. Art Deco. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "30m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "30m.", "x": "Christ the Redeemer: 30m.. Soapstone. Essential knowledge — Art Deco.. the open arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 30m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 30m..", "x": "Explained: 30m.. Deco. The context — Christ the Redeemer. Soapstone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Corcovado.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Corcovado.", "x": "Christ the Redeemer: Corcovado.. Arms. Essential knowledge — Soapstone.. the open arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Corcovado..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Corcovado..", "x": "Explained: Corcovado.. Tickets. The context — Christ the Redeemer. Arms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Art Deco.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Art Deco.", "x": "Christ the Redeemer: Art Deco.. Deco. Essential knowledge — Arms.. the open arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Art Deco..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Art Deco..", "x": "Explained: Art Deco.. 1931. The context — Christ the Redeemer. 1931. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Soapstone.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Soapstone.", "x": "Christ the Redeemer: Soapstone.. Tickets. Essential knowledge — 1931.. the open arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Soapstone..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Soapstone..", "x": "Explained: Soapstone.. Corcovado. The context — Christ the Redeemer. 30m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Arms.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Arms.", "x": "Christ the Redeemer: Arms.. 1931. Essential knowledge — 30m.. the open arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Arms..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Arms..", "x": "Explained: Arms.. Soapstone. The context — Christ the Redeemer. Corcovado. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1931.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1931.", "x": "Christ the Redeemer in depth: 1931.. 30m. Details — the open arms.. Soapstone. Art Deco. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Corcovado.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Corcovado.", "x": "Christ the Redeemer in depth: Corcovado.. Corcovado. Details — the open arms.. Arms. Soapstone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Soapstone.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Soapstone.", "x": "Christ the Redeemer in depth: Soapstone.. Art Deco. Details — the open arms.. Deco. Arms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Arms.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Arms.", "x": "Christ the Redeemer in depth: Arms.. Soapstone. Details — the open arms.. Tickets. 1931. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Deco.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Deco.", "x": "Christ the Redeemer in depth: Deco.. Arms. Details — the open arms.. 1931. 30m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Christ the Redeemer in depth: Tickets.. 1931. Details — the open arms.. Corcovado. Corcovado. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Christ the Redeemer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Christ the Redeemer comes from.", "x": "Origins: 1931.. 1931. The history of Christ the Redeemer — the open arms.. Corcovado. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Christ the Redeemer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Christ the Redeemer respectfully.", "x": "Engaging: Soapstone.. 30m. How to participate or observe well — Christ the Redeemer. the open arms. Respect first, always; Arms.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Christ the Redeemer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Christ the Redeemer do's and don'ts.", "x": "Etiquette: Deco.. Corcovado. The rules of respect — Christ the Redeemer. the open arms. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Christ the Redeemer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Christ the Redeemer.", "x": "Planning: 1931.. Art Deco. Practical notes — Christ the Redeemer. the open arms. A little planning shows respect for Corcovado.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Christ the Redeemer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Christ the Redeemer and money.", "x": "Costs: Soapstone.. Soapstone. What to budget — Christ the Redeemer. the open arms. The best experiences of Arms. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-christ-redeemer-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
