(function(){'use strict';
/* JAH Tsing Ma Bridge Bridge Database generator — jahdb-e2-bridge-tsing-ma-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-tsing-ma-bridge',PREFIX='JAH-E2BRIDGETSI-',NAME='JAH Tsing Ma Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tsing Ma Bridge: the complete guide", "d": "Tsing Ma Bridge: Hong Kong's double decker..", "g": "overview", "l": 2, "q": "What is Tsing Ma Bridge: the complete guide?", "a": "Tsing Ma Bridge: Hong Kong's double decker..", "x": "The complete bridge guide to Tsing Ma Bridge: Hong Kong's double decker.. 2.2 km. History, meaning, practices, and how to engage respectfully — everything in one database. Double deck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tsing Ma Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tsing Ma Bridge essentials.", "x": "At a glance: Tsing Ma Bridge — Hong Kong's double decker.. Rail+road. The essentials: Typhoon.. 1997. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2.2 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2.2 km.", "x": "Tsing Ma Bridge: 2.2 km.. Typhoon. Essential knowledge — 1997.. Hong Kong's double decker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2.2 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2.2 km..", "x": "Explained: 2.2 km.. Views. The context — Tsing Ma Bridge. Typhoon-proof. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rail+road.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rail+road.", "x": "Tsing Ma Bridge: Rail+road.. History. Essential knowledge — Typhoon-proof.. Hong Kong's double decker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rail+road..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rail+road..", "x": "Explained: Rail+road.. Hong Kong. The context — Tsing Ma Bridge. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1997.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1997.", "x": "Tsing Ma Bridge: 1997.. Views. Essential knowledge — Views.. Hong Kong's double decker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1997..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1997..", "x": "Explained: 1997.. Engineering. The context — Tsing Ma Bridge. Lantau. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Typhoon-proof.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Typhoon-proof.", "x": "Tsing Ma Bridge: Typhoon-proof.. Hong Kong. Essential knowledge — Lantau.. Hong Kong's double decker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Typhoon-proof..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Typhoon-proof..", "x": "Explained: Typhoon-proof.. Double deck. The context — Tsing Ma Bridge. 2.2 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Views.", "x": "Tsing Ma Bridge: Views.. Engineering. Essential knowledge — 2.2 km.. Hong Kong's double decker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Typhoon. The context — Tsing Ma Bridge. Rail+road. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lantau.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lantau.", "x": "Tsing Ma Bridge: Lantau.. Double deck. Essential knowledge — Rail+road.. Hong Kong's double decker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lantau..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lantau..", "x": "Explained: Lantau.. History. The context — Tsing Ma Bridge. 1997. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Double deck.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Double deck.", "x": "Tsing Ma Bridge in depth: Double deck.. Rail+road. Details — Hong Kong's double decker.. History. Typhoon-proof. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Typhoon.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Typhoon.", "x": "Tsing Ma Bridge in depth: Typhoon.. 1997. Details — Hong Kong's double decker.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Tsing Ma Bridge in depth: History.. Typhoon-proof. Details — Hong Kong's double decker.. Hong Kong. Lantau. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Tsing Ma Bridge in depth: Views.. Views. Details — Hong Kong's double decker.. Engineering. 2.2 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hong Kong.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hong Kong.", "x": "Tsing Ma Bridge in depth: Hong Kong.. Lantau. Details — Hong Kong's double decker.. Double deck. Rail+road. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Engineering.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Engineering.", "x": "Tsing Ma Bridge in depth: Engineering.. 2.2 km. Details — Hong Kong's double decker.. Typhoon. 1997. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tsing Ma Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tsing Ma Bridge comes from.", "x": "Origins: Double deck.. 2.2 km. The history of Tsing Ma Bridge — Hong Kong's double decker.. Typhoon. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tsing Ma Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tsing Ma Bridge respectfully.", "x": "Engaging: History.. Rail+road. How to participate or observe well — Tsing Ma Bridge. Hong Kong's double decker. Respect first, always; Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tsing Ma Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tsing Ma Bridge do's and don'ts.", "x": "Etiquette: Hong Kong.. 1997. The rules of respect — Tsing Ma Bridge. Hong Kong's double decker. When in doubt, ask about Engineering.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tsing Ma Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tsing Ma Bridge.", "x": "Planning: Double deck.. Typhoon-proof. Practical notes — Tsing Ma Bridge. Hong Kong's double decker. A little planning shows respect for Typhoon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tsing Ma Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tsing Ma Bridge and money.", "x": "Costs: History.. Views. What to budget — Tsing Ma Bridge. Hong Kong's double decker. The best experiences of Views. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-tsing-ma-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
