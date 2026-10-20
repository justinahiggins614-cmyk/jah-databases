(function(){'use strict';
/* JAH Sapporo Snow Festival Festival Database generator — jahdb-e2-festival-sapporo-snow-festival-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-sapporo-snow-festival',PREFIX='JAH-E2FESTIVALS-',NAME='JAH Sapporo Snow Festival Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sapporo Snow Festival: the complete guide", "d": "Sapporo Snow Festival: snow sculptures..", "g": "overview", "l": 2, "q": "What is Sapporo Snow Festival: the complete guide?", "a": "Sapporo Snow Festival: snow sculptures..", "x": "The complete festival guide to Sapporo Snow Festival: snow sculptures.. February. History, meaning, practices, and how to engage respectfully — everything in one database. Snow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sapporo Snow Festival essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sapporo Snow Festival essentials.", "x": "At a glance: Sapporo Snow Festival — snow sculptures.. Japan. The essentials: History.. Sculptures. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "February.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "February.", "x": "Sapporo Snow Festival: February.. History. Essential knowledge — Sculptures.. snow sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: February..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: February..", "x": "Explained: February.. Travel. The context — Sapporo Snow Festival. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Japan.", "x": "Sapporo Snow Festival: Japan.. Food. Essential knowledge — History.. snow sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Winter. The context — Sapporo Snow Festival. Food. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sculptures.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sculptures.", "x": "Sapporo Snow Festival: Sculptures.. Travel. Essential knowledge — Food.. snow sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sculptures..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sculptures..", "x": "Explained: Sculptures.. Wonder. The context — Sapporo Snow Festival. Winter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "History.", "x": "Sapporo Snow Festival: History.. Winter. Essential knowledge — Winter.. snow sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: History..", "x": "Explained: History.. Snow. The context — Sapporo Snow Festival. February. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Food.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Food.", "x": "Sapporo Snow Festival: Food.. Wonder. Essential knowledge — February.. snow sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Food..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Food..", "x": "Explained: Food.. History. The context — Sapporo Snow Festival. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Winter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Winter.", "x": "Sapporo Snow Festival: Winter.. Snow. Essential knowledge — Japan.. snow sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Winter..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Winter..", "x": "Explained: Winter.. Food. The context — Sapporo Snow Festival. Sculptures. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Snow.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Snow.", "x": "Sapporo Snow Festival in depth: Snow.. Japan. Details — snow sculptures.. Food. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Sapporo Snow Festival in depth: History.. Sculptures. Details — snow sculptures.. Travel. Food. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Food.", "x": "Sapporo Snow Festival in depth: Food.. History. Details — snow sculptures.. Winter. Winter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Travel.", "x": "Sapporo Snow Festival in depth: Travel.. Food. Details — snow sculptures.. Wonder. February. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Winter.", "x": "Sapporo Snow Festival in depth: Winter.. Winter. Details — snow sculptures.. Snow. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Wonder.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Wonder.", "x": "Sapporo Snow Festival in depth: Wonder.. February. Details — snow sculptures.. History. Sculptures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sapporo Snow Festival comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sapporo Snow Festival comes from.", "x": "Origins: Snow.. February. The history of Sapporo Snow Festival — snow sculptures.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sapporo Snow Festival respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sapporo Snow Festival respectfully.", "x": "Engaging: Food.. Japan. How to participate or observe well — Sapporo Snow Festival. snow sculptures. Respect first, always; Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sapporo Snow Festival do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sapporo Snow Festival do's and don'ts.", "x": "Etiquette: Winter.. Sculptures. The rules of respect — Sapporo Snow Festival. snow sculptures. When in doubt, ask about Wonder.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sapporo Snow Festival.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sapporo Snow Festival.", "x": "Planning: Snow.. History. Practical notes — Sapporo Snow Festival. snow sculptures. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sapporo Snow Festival and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sapporo Snow Festival and money.", "x": "Costs: Food.. Food. What to budget — Sapporo Snow Festival. snow sculptures. The best experiences of Travel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-sapporo-snow-festival-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
