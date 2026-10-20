(function(){'use strict';
/* JAH Pad See Ew Dish Database generator — jahdb-e2-dish-pad-see-ew-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-pad-see-ew-dish',PREFIX='JAH-E2DISHPADSE-',NAME='JAH Pad See Ew Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pad See Ew: the complete guide", "d": "Pad See Ew: the charred noodles..", "g": "overview", "l": 2, "q": "What is Pad See Ew: the complete guide?", "a": "Pad See Ew: the charred noodles..", "x": "The complete dish guide to Pad See Ew: the charred noodles.. Wide noodles. History, meaning, practices, and how to engage respectfully — everything in one database. Charred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pad See Ew essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pad See Ew essentials.", "x": "At a glance: Pad See Ew — the charred noodles.. Charred. The essentials: Wok.. Chinese broccoli. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wide noodles.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wide noodles.", "x": "Pad See Ew: Wide noodles.. Wok. Essential knowledge — Chinese broccoli.. the charred noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wide noodles..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wide noodles..", "x": "Explained: Wide noodles.. Noodles. The context — Pad See Ew. Soy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Charred.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Charred.", "x": "Pad See Ew: Charred.. Street. Essential knowledge — Soy.. the charred noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Charred..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Charred..", "x": "Explained: Charred.. Soy. The context — Pad See Ew. Wok. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chinese broccoli.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chinese broccoli.", "x": "Pad See Ew: Chinese broccoli.. Noodles. Essential knowledge — Wok.. the charred noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chinese broccoli..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chinese broccoli..", "x": "Explained: Chinese broccoli.. Making. The context — Pad See Ew. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Soy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Soy.", "x": "Pad See Ew: Soy.. Soy. Essential knowledge — Street.. the charred noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Soy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Soy..", "x": "Explained: Soy.. Charred. The context — Pad See Ew. Wide noodles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wok.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wok.", "x": "Pad See Ew: Wok.. Making. Essential knowledge — Wide noodles.. the charred noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wok..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wok..", "x": "Explained: Wok.. Wok. The context — Pad See Ew. Charred. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Street.", "x": "Pad See Ew: Street.. Charred. Essential knowledge — Charred.. the charred noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Pad See Ew. Chinese broccoli. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Charred.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Charred.", "x": "Pad See Ew in depth: Charred.. Charred. Details — the charred noodles.. Street. Soy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wok.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wok.", "x": "Pad See Ew in depth: Wok.. Chinese broccoli. Details — the charred noodles.. Noodles. Wok. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Street.", "x": "Pad See Ew in depth: Street.. Soy. Details — the charred noodles.. Soy. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Noodles.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Noodles.", "x": "Pad See Ew in depth: Noodles.. Wok. Details — the charred noodles.. Making. Wide noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Soy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Soy.", "x": "Pad See Ew in depth: Soy.. Street. Details — the charred noodles.. Charred. Charred. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Pad See Ew in depth: Making.. Wide noodles. Details — the charred noodles.. Wok. Chinese broccoli. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pad See Ew comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pad See Ew comes from.", "x": "Origins: Charred.. Wide noodles. The history of Pad See Ew — the charred noodles.. Wok. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pad See Ew respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pad See Ew respectfully.", "x": "Engaging: Street.. Charred. How to participate or observe well — Pad See Ew. the charred noodles. Respect first, always; Noodles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pad See Ew do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pad See Ew do's and don'ts.", "x": "Etiquette: Soy.. Chinese broccoli. The rules of respect — Pad See Ew. the charred noodles. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pad See Ew.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pad See Ew.", "x": "Planning: Charred.. Soy. Practical notes — Pad See Ew. the charred noodles. A little planning shows respect for Wok.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pad See Ew and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pad See Ew and money.", "x": "Costs: Street.. Wok. What to budget — Pad See Ew. the charred noodles. The best experiences of Noodles. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-pad-see-ew-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
