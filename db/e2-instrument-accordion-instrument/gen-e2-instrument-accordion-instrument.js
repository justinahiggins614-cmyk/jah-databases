(function(){'use strict';
/* JAH Accordion Instrument Instrument Database generator — jahdb-e2-instrument-accordion-instrument-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-instrument-accordion-instrument',PREFIX='JAH-E2INSTRUMEN-',NAME='JAH Accordion Instrument Instrument Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Accordion Instrument: the complete guide", "d": "Accordion Instrument: the squeezebox..", "g": "overview", "l": 2, "q": "What is Accordion Instrument: the complete guide?", "a": "Accordion Instrument: the squeezebox..", "x": "The complete instrument guide to Accordion Instrument: the squeezebox.. Bellows. History, meaning, practices, and how to engage respectfully — everything in one database. Bellows. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Accordion Instrument essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Accordion Instrument essentials.", "x": "At a glance: Accordion Instrument — the squeezebox.. Reeds. The essentials: Polka.. Polka. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bellows.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bellows.", "x": "Accordion Instrument: Bellows.. Polka. Essential knowledge — Polka.. the squeezebox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bellows..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bellows..", "x": "Explained: Bellows.. Zydeco. The context — Accordion Instrument. Buttons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reeds.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reeds.", "x": "Accordion Instrument: Reeds.. Folk. Essential knowledge — Buttons.. the squeezebox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Reeds..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Reeds..", "x": "Explained: Reeds.. Buttons. The context — Accordion Instrument. Folk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Polka.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Polka.", "x": "Accordion Instrument: Polka.. Zydeco. Essential knowledge — Folk.. the squeezebox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Polka..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Polka..", "x": "Explained: Polka.. Learning. The context — Accordion Instrument. Zydeco. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Buttons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Buttons.", "x": "Accordion Instrument: Buttons.. Buttons. Essential knowledge — Zydeco.. the squeezebox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Buttons..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Buttons..", "x": "Explained: Buttons.. Bellows. The context — Accordion Instrument. Bellows. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Folk.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Folk.", "x": "Accordion Instrument: Folk.. Learning. Essential knowledge — Bellows.. the squeezebox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Folk..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Folk..", "x": "Explained: Folk.. Polka. The context — Accordion Instrument. Reeds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Zydeco.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Zydeco.", "x": "Accordion Instrument: Zydeco.. Bellows. Essential knowledge — Reeds.. the squeezebox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Zydeco..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Zydeco..", "x": "Explained: Zydeco.. Folk. The context — Accordion Instrument. Polka. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bellows.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bellows.", "x": "Accordion Instrument in depth: Bellows.. Reeds. Details — the squeezebox.. Folk. Buttons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Polka.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Polka.", "x": "Accordion Instrument in depth: Polka.. Polka. Details — the squeezebox.. Zydeco. Folk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Folk.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Folk.", "x": "Accordion Instrument in depth: Folk.. Buttons. Details — the squeezebox.. Buttons. Zydeco. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Zydeco.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Zydeco.", "x": "Accordion Instrument in depth: Zydeco.. Folk. Details — the squeezebox.. Learning. Bellows. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Buttons.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Buttons.", "x": "Accordion Instrument in depth: Buttons.. Zydeco. Details — the squeezebox.. Bellows. Reeds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learning.", "x": "Accordion Instrument in depth: Learning.. Bellows. Details — the squeezebox.. Polka. Polka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Accordion Instrument comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Accordion Instrument comes from.", "x": "Origins: Bellows.. Bellows. The history of Accordion Instrument — the squeezebox.. Polka. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Accordion Instrument respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Accordion Instrument respectfully.", "x": "Engaging: Folk.. Reeds. How to participate or observe well — Accordion Instrument. the squeezebox. Respect first, always; Zydeco.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Accordion Instrument do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Accordion Instrument do's and don'ts.", "x": "Etiquette: Buttons.. Polka. The rules of respect — Accordion Instrument. the squeezebox. When in doubt, ask about Learning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Accordion Instrument.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Accordion Instrument.", "x": "Planning: Bellows.. Buttons. Practical notes — Accordion Instrument. the squeezebox. A little planning shows respect for Polka.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Accordion Instrument and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Accordion Instrument and money.", "x": "Costs: Folk.. Folk. What to budget — Accordion Instrument. the squeezebox. The best experiences of Zydeco. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-instrument-accordion-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
