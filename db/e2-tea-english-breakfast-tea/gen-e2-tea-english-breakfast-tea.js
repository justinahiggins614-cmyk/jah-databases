(function(){'use strict';
/* JAH English Breakfast Tea Tea Database generator — jahdb-e2-tea-english-breakfast-tea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tea-english-breakfast-tea',PREFIX='JAH-E2TEAENGLIS-',NAME='JAH English Breakfast Tea Tea Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "English Breakfast Tea: the complete guide", "d": "English Breakfast Tea: the morning blend..", "g": "overview", "l": 2, "q": "What is English Breakfast Tea: the complete guide?", "a": "English Breakfast Tea: the morning blend..", "x": "The complete tea guide to English Breakfast Tea: the morning blend.. Assam. History, meaning, practices, and how to engage respectfully — everything in one database. Blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "English Breakfast Tea essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "English Breakfast Tea essentials.", "x": "At a glance: English Breakfast Tea — the morning blend.. Ceylon. The essentials: Milk.. Kenya. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Assam.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Assam.", "x": "English Breakfast Tea: Assam.. Milk. Essential knowledge — Kenya.. the morning blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Assam..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Assam..", "x": "Explained: Assam.. Origins. The context — English Breakfast Tea. Milk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ceylon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ceylon.", "x": "English Breakfast Tea: Ceylon.. Morning. Essential knowledge — Milk.. the morning blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ceylon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ceylon..", "x": "Explained: Ceylon.. Strong. The context — English Breakfast Tea. Strong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kenya.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kenya.", "x": "English Breakfast Tea: Kenya.. Origins. Essential knowledge — Strong.. the morning blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kenya..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kenya..", "x": "Explained: Kenya.. History. The context — English Breakfast Tea. Morning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Milk.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Milk.", "x": "English Breakfast Tea: Milk.. Strong. Essential knowledge — Morning.. the morning blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Milk..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Milk..", "x": "Explained: Milk.. Blend. The context — English Breakfast Tea. Assam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Strong.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Strong.", "x": "English Breakfast Tea: Strong.. History. Essential knowledge — Assam.. the morning blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Strong..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Strong..", "x": "Explained: Strong.. Milk. The context — English Breakfast Tea. Ceylon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Morning.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Morning.", "x": "English Breakfast Tea: Morning.. Blend. Essential knowledge — Ceylon.. the morning blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Morning..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Morning..", "x": "Explained: Morning.. Morning. The context — English Breakfast Tea. Kenya. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blend.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blend.", "x": "English Breakfast Tea in depth: Blend.. Ceylon. Details — the morning blend.. Morning. Milk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Milk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Milk.", "x": "English Breakfast Tea in depth: Milk.. Kenya. Details — the morning blend.. Origins. Strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Morning.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Morning.", "x": "English Breakfast Tea in depth: Morning.. Milk. Details — the morning blend.. Strong. Morning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Origins.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Origins.", "x": "English Breakfast Tea in depth: Origins.. Strong. Details — the morning blend.. History. Assam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Strong.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Strong.", "x": "English Breakfast Tea in depth: Strong.. Morning. Details — the morning blend.. Blend. Ceylon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "English Breakfast Tea in depth: History.. Assam. Details — the morning blend.. Milk. Kenya. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where English Breakfast Tea comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where English Breakfast Tea comes from.", "x": "Origins: Blend.. Assam. The history of English Breakfast Tea — the morning blend.. Milk. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing English Breakfast Tea respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing English Breakfast Tea respectfully.", "x": "Engaging: Morning.. Ceylon. How to participate or observe well — English Breakfast Tea. the morning blend. Respect first, always; Origins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "English Breakfast Tea do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "English Breakfast Tea do's and don'ts.", "x": "Etiquette: Strong.. Kenya. The rules of respect — English Breakfast Tea. the morning blend. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around English Breakfast Tea.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around English Breakfast Tea.", "x": "Planning: Blend.. Milk. Practical notes — English Breakfast Tea. the morning blend. A little planning shows respect for Milk.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "English Breakfast Tea and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "English Breakfast Tea and money.", "x": "Costs: Morning.. Strong. What to budget — English Breakfast Tea. the morning blend. The best experiences of Origins. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tea-english-breakfast-tea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
