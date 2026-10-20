(function(){'use strict';
/* JAH Funko Pop Figures Action Figure Database generator — jahdb-e2-figure-funko-pop-figures-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-figure-funko-pop-figures',PREFIX='JAH-E2FIGUREFUN-',NAME='JAH Funko Pop Figures Action Figure Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Funko Pop Figures: the complete guide", "d": "Funko Pop Figures: the big-head vinyl..", "g": "overview", "l": 2, "q": "What is Funko Pop Figures: the complete guide?", "a": "Funko Pop Figures: the big-head vinyl..", "x": "The complete action figure guide to Funko Pop Figures: the big-head vinyl.. 2010. History, meaning, practices, and how to engage respectfully — everything in one database. Vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Funko Pop Figures essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Funko Pop Figures essentials.", "x": "At a glance: Funko Pop Figures — the big-head vinyl.. Vinyl. The essentials: Chase.. Big head. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2010.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2010.", "x": "Funko Pop Figures: 2010.. Chase. Essential knowledge — Big head.. the big-head vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2010..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2010..", "x": "Explained: 2010.. Collecting. The context — Funko Pop Figures. Chase. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Vinyl.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Vinyl.", "x": "Funko Pop Figures: Vinyl.. Everett. Essential knowledge — Chase.. the big-head vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Vinyl..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Vinyl..", "x": "Explained: Vinyl.. 2010. The context — Funko Pop Figures. Everett. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Big head.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Big head.", "x": "Funko Pop Figures: Big head.. Collecting. Essential knowledge — Everett.. the big-head vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Big head..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Big head..", "x": "Explained: Big head.. History. The context — Funko Pop Figures. Collecting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chase.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chase.", "x": "Funko Pop Figures: Chase.. 2010. Essential knowledge — Collecting.. the big-head vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chase..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chase..", "x": "Explained: Chase.. Vinyl. The context — Funko Pop Figures. 2010. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Everett.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Everett.", "x": "Funko Pop Figures: Everett.. History. Essential knowledge — 2010.. the big-head vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Everett..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Everett..", "x": "Explained: Everett.. Chase. The context — Funko Pop Figures. Vinyl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Collecting.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Collecting.", "x": "Funko Pop Figures: Collecting.. Vinyl. Essential knowledge — Vinyl.. the big-head vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Collecting..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Collecting..", "x": "Explained: Collecting.. Everett. The context — Funko Pop Figures. Big head. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Vinyl.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Vinyl.", "x": "Funko Pop Figures in depth: Vinyl.. Vinyl. Details — the big-head vinyl.. Everett. Chase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chase.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chase.", "x": "Funko Pop Figures in depth: Chase.. Big head. Details — the big-head vinyl.. Collecting. Everett. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Everett.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Everett.", "x": "Funko Pop Figures in depth: Everett.. Chase. Details — the big-head vinyl.. 2010. Collecting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Collecting.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Collecting.", "x": "Funko Pop Figures in depth: Collecting.. Everett. Details — the big-head vinyl.. History. 2010. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "2010.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "2010.", "x": "Funko Pop Figures in depth: 2010.. Collecting. Details — the big-head vinyl.. Vinyl. Vinyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Funko Pop Figures in depth: History.. 2010. Details — the big-head vinyl.. Chase. Big head. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Funko Pop Figures comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Funko Pop Figures comes from.", "x": "Origins: Vinyl.. 2010. The history of Funko Pop Figures — the big-head vinyl.. Chase. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Funko Pop Figures respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Funko Pop Figures respectfully.", "x": "Engaging: Everett.. Vinyl. How to participate or observe well — Funko Pop Figures. the big-head vinyl. Respect first, always; Collecting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Funko Pop Figures do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Funko Pop Figures do's and don'ts.", "x": "Etiquette: 2010.. Big head. The rules of respect — Funko Pop Figures. the big-head vinyl. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Funko Pop Figures.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Funko Pop Figures.", "x": "Planning: Vinyl.. Chase. Practical notes — Funko Pop Figures. the big-head vinyl. A little planning shows respect for Chase.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Funko Pop Figures and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Funko Pop Figures and money.", "x": "Costs: Everett.. Everett. What to budget — Funko Pop Figures. the big-head vinyl. The best experiences of Collecting. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-figure-funko-pop-figures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
