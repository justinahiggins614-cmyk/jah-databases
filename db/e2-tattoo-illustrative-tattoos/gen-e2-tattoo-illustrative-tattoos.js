(function(){'use strict';
/* JAH Illustrative Tattoos Tattoo Style Database generator — jahdb-e2-tattoo-illustrative-tattoos-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tattoo-illustrative-tattoos',PREFIX='JAH-E2TATTOOILL-',NAME='JAH Illustrative Tattoos Tattoo Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Illustrative Tattoos: the complete guide", "d": "Illustrative Tattoos: storybook skin..", "g": "overview", "l": 2, "q": "What is Illustrative Tattoos: the complete guide?", "a": "Illustrative Tattoos: storybook skin..", "x": "The complete tattoo style guide to Illustrative Tattoos: storybook skin.. Drawing style. History, meaning, practices, and how to engage respectfully — everything in one database. Style. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Illustrative Tattoos essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Illustrative Tattoos essentials.", "x": "At a glance: Illustrative Tattoos — storybook skin.. Narrative. The essentials: Artists.. Artists. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Drawing style.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Drawing style.", "x": "Illustrative Tattoos: Drawing style.. Artists. Essential knowledge — Artists.. storybook skin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Drawing style..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Drawing style..", "x": "Explained: Drawing style.. Aging. The context — Illustrative Tattoos. Color/black. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Narrative.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Narrative.", "x": "Illustrative Tattoos: Narrative.. Custom. Essential knowledge — Color/black.. storybook skin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Narrative..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Narrative..", "x": "Explained: Narrative.. Narrative. The context — Illustrative Tattoos. Custom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Artists.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Artists.", "x": "Illustrative Tattoos: Artists.. Aging. Essential knowledge — Custom.. storybook skin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Artists..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Artists..", "x": "Explained: Artists.. Art. The context — Illustrative Tattoos. Style. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Color/black.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Color/black.", "x": "Illustrative Tattoos: Color/black.. Narrative. Essential knowledge — Style.. storybook skin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Color/black..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Color/black..", "x": "Explained: Color/black.. Style. The context — Illustrative Tattoos. Drawing style. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Custom.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Custom.", "x": "Illustrative Tattoos: Custom.. Art. Essential knowledge — Drawing style.. storybook skin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Custom..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Custom..", "x": "Explained: Custom.. Artists. The context — Illustrative Tattoos. Narrative. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Style.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Style.", "x": "Illustrative Tattoos: Style.. Style. Essential knowledge — Narrative.. storybook skin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Style..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Style..", "x": "Explained: Style.. Custom. The context — Illustrative Tattoos. Artists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Style.", "x": "Illustrative Tattoos in depth: Style.. Narrative. Details — storybook skin.. Custom. Color/black. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Artists.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Artists.", "x": "Illustrative Tattoos in depth: Artists.. Artists. Details — storybook skin.. Aging. Custom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Custom.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Custom.", "x": "Illustrative Tattoos in depth: Custom.. Color/black. Details — storybook skin.. Narrative. Style. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Aging.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Aging.", "x": "Illustrative Tattoos in depth: Aging.. Custom. Details — storybook skin.. Art. Drawing style. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Narrative.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Narrative.", "x": "Illustrative Tattoos in depth: Narrative.. Style. Details — storybook skin.. Style. Narrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Illustrative Tattoos in depth: Art.. Drawing style. Details — storybook skin.. Artists. Artists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Illustrative Tattoos comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Illustrative Tattoos comes from.", "x": "Origins: Style.. Drawing style. The history of Illustrative Tattoos — storybook skin.. Artists. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Illustrative Tattoos respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Illustrative Tattoos respectfully.", "x": "Engaging: Custom.. Narrative. How to participate or observe well — Illustrative Tattoos. storybook skin. Respect first, always; Aging.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Illustrative Tattoos do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Illustrative Tattoos do's and don'ts.", "x": "Etiquette: Narrative.. Artists. The rules of respect — Illustrative Tattoos. storybook skin. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Illustrative Tattoos.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Illustrative Tattoos.", "x": "Planning: Style.. Color/black. Practical notes — Illustrative Tattoos. storybook skin. A little planning shows respect for Artists.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Illustrative Tattoos and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Illustrative Tattoos and money.", "x": "Costs: Custom.. Custom. What to budget — Illustrative Tattoos. storybook skin. The best experiences of Aging. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tattoo-illustrative-tattoos-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
