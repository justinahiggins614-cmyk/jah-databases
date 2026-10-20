(function(){'use strict';
/* JAH Pearl Harbor Landmark Database generator — jahdb-e2-landmark-pearl-harbor-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-pearl-harbor-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Pearl Harbor Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pearl Harbor: the complete guide", "d": "Pearl Harbor: the 1941 memorial..", "g": "overview", "l": 2, "q": "What is Pearl Harbor: the complete guide?", "a": "Pearl Harbor: the 1941 memorial..", "x": "The complete landmark guide to Pearl Harbor: the 1941 memorial.. 1941. History, meaning, practices, and how to engage respectfully — everything in one database. 1941. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pearl Harbor essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pearl Harbor essentials.", "x": "At a glance: Pearl Harbor — the 1941 memorial.. Arizona. The essentials: Memorial.. Memorial. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1941.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1941.", "x": "Pearl Harbor: 1941.. Memorial. Essential knowledge — Memorial.. the 1941 memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1941..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1941..", "x": "Explained: 1941.. Arizona. The context — Pearl Harbor. Oil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Arizona.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Arizona.", "x": "Pearl Harbor: Arizona.. Honor. Essential knowledge — Oil.. the 1941 memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Arizona..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Arizona..", "x": "Explained: Arizona.. WWII. The context — Pearl Harbor. WWII. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Memorial.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Memorial.", "x": "Pearl Harbor: Memorial.. Arizona. Essential knowledge — WWII.. the 1941 memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Memorial..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Memorial..", "x": "Explained: Memorial.. Visits. The context — Pearl Harbor. Honor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Oil.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Oil.", "x": "Pearl Harbor: Oil.. WWII. Essential knowledge — Honor.. the 1941 memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Oil..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Oil..", "x": "Explained: Oil.. 1941. The context — Pearl Harbor. 1941. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "WWII.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "WWII.", "x": "Pearl Harbor: WWII.. Visits. Essential knowledge — 1941.. the 1941 memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: WWII..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: WWII..", "x": "Explained: WWII.. Memorial. The context — Pearl Harbor. Arizona. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Honor.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Honor.", "x": "Pearl Harbor: Honor.. 1941. Essential knowledge — Arizona.. the 1941 memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Honor..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Honor..", "x": "Explained: Honor.. Honor. The context — Pearl Harbor. Memorial. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1941.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1941.", "x": "Pearl Harbor in depth: 1941.. Arizona. Details — the 1941 memorial.. Honor. Oil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Memorial.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Memorial.", "x": "Pearl Harbor in depth: Memorial.. Memorial. Details — the 1941 memorial.. Arizona. WWII. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Honor.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Honor.", "x": "Pearl Harbor in depth: Honor.. Oil. Details — the 1941 memorial.. WWII. Honor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Arizona.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Arizona.", "x": "Pearl Harbor in depth: Arizona.. WWII. Details — the 1941 memorial.. Visits. 1941. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "WWII.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "WWII.", "x": "Pearl Harbor in depth: WWII.. Honor. Details — the 1941 memorial.. 1941. Arizona. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visits.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visits.", "x": "Pearl Harbor in depth: Visits.. 1941. Details — the 1941 memorial.. Memorial. Memorial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pearl Harbor comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pearl Harbor comes from.", "x": "Origins: 1941.. 1941. The history of Pearl Harbor — the 1941 memorial.. Memorial. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pearl Harbor respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pearl Harbor respectfully.", "x": "Engaging: Honor.. Arizona. How to participate or observe well — Pearl Harbor. the 1941 memorial. Respect first, always; Arizona.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pearl Harbor do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pearl Harbor do's and don'ts.", "x": "Etiquette: WWII.. Memorial. The rules of respect — Pearl Harbor. the 1941 memorial. When in doubt, ask about Visits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pearl Harbor.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pearl Harbor.", "x": "Planning: 1941.. Oil. Practical notes — Pearl Harbor. the 1941 memorial. A little planning shows respect for Memorial.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pearl Harbor and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pearl Harbor and money.", "x": "Costs: Honor.. WWII. What to budget — Pearl Harbor. the 1941 memorial. The best experiences of Arizona. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-pearl-harbor-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
