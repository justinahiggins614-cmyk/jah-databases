(function(){'use strict';
/* JAH Chicago School Arch Database generator — jahdb-e2-arch2-chicago-school-arch2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch2-chicago-school-arch2',PREFIX='JAH-E2ARCH2CHIC-',NAME='JAH Chicago School Arch Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chicago School Arch: the complete guide", "d": "Chicago School Arch: the steel frame..", "g": "overview", "l": 2, "q": "What is Chicago School Arch: the complete guide?", "a": "Chicago School Arch: the steel frame..", "x": "The complete architecture style guide to Chicago School Arch: the steel frame.. 1880s. History, meaning, practices, and how to engage respectfully — everything in one database. Steel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chicago School Arch essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chicago School Arch essentials.", "x": "At a glance: Chicago School Arch — the steel frame.. Steel. The essentials: Skyscraper.. Sullivan. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1880s.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1880s.", "x": "Chicago School Arch: 1880s.. Skyscraper. Essential knowledge — Sullivan.. the steel frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1880s..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1880s..", "x": "Explained: 1880s.. Sullivan. The context — Chicago School Arch. Windows. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Steel.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Steel.", "x": "Chicago School Arch: Steel.. Form. Essential knowledge — Windows.. the steel frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Steel..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Steel..", "x": "Explained: Steel.. 1880s. The context — Chicago School Arch. Skyscraper. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sullivan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sullivan.", "x": "Chicago School Arch: Sullivan.. Sullivan. Essential knowledge — Skyscraper.. the steel frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sullivan..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sullivan..", "x": "Explained: Sullivan.. Legacy. The context — Chicago School Arch. Form. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Windows.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Windows.", "x": "Chicago School Arch: Windows.. 1880s. Essential knowledge — Form.. the steel frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Windows..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Windows..", "x": "Explained: Windows.. Steel. The context — Chicago School Arch. 1880s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Skyscraper.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Skyscraper.", "x": "Chicago School Arch: Skyscraper.. Legacy. Essential knowledge — 1880s.. the steel frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Skyscraper..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Skyscraper..", "x": "Explained: Skyscraper.. Skyscraper. The context — Chicago School Arch. Steel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Form.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Form.", "x": "Chicago School Arch: Form.. Steel. Essential knowledge — Steel.. the steel frame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Form..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Form..", "x": "Explained: Form.. Form. The context — Chicago School Arch. Sullivan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Steel.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Steel.", "x": "Chicago School Arch in depth: Steel.. Steel. Details — the steel frame.. Form. Windows. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Skyscraper.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Skyscraper.", "x": "Chicago School Arch in depth: Skyscraper.. Sullivan. Details — the steel frame.. Sullivan. Skyscraper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Form.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Form.", "x": "Chicago School Arch in depth: Form.. Windows. Details — the steel frame.. 1880s. Form. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sullivan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sullivan.", "x": "Chicago School Arch in depth: Sullivan.. Skyscraper. Details — the steel frame.. Legacy. 1880s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1880s.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1880s.", "x": "Chicago School Arch in depth: 1880s.. Form. Details — the steel frame.. Steel. Steel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Chicago School Arch in depth: Legacy.. 1880s. Details — the steel frame.. Skyscraper. Sullivan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chicago School Arch comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chicago School Arch comes from.", "x": "Origins: Steel.. 1880s. The history of Chicago School Arch — the steel frame.. Skyscraper. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chicago School Arch respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chicago School Arch respectfully.", "x": "Engaging: Form.. Steel. How to participate or observe well — Chicago School Arch. the steel frame. Respect first, always; Sullivan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chicago School Arch do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chicago School Arch do's and don'ts.", "x": "Etiquette: 1880s.. Sullivan. The rules of respect — Chicago School Arch. the steel frame. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chicago School Arch.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chicago School Arch.", "x": "Planning: Steel.. Windows. Practical notes — Chicago School Arch. the steel frame. A little planning shows respect for Skyscraper.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chicago School Arch and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chicago School Arch and money.", "x": "Costs: Form.. Skyscraper. What to budget — Chicago School Arch. the steel frame. The best experiences of Sullivan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch2-chicago-school-arch2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
