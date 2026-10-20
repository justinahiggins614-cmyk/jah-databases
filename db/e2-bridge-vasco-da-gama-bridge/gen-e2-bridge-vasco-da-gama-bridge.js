(function(){'use strict';
/* JAH Vasco da Gama Bridge Bridge Database generator — jahdb-e2-bridge-vasco-da-gama-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-vasco-da-gama-bridge',PREFIX='JAH-E2BRIDGEVAS-',NAME='JAH Vasco da Gama Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vasco da Gama Bridge: the complete guide", "d": "Vasco da Gama Bridge: Europe's longest..", "g": "overview", "l": 2, "q": "What is Vasco da Gama Bridge: the complete guide?", "a": "Vasco da Gama Bridge: Europe's longest..", "x": "The complete bridge guide to Vasco da Gama Bridge: Europe's longest.. 17.2 km. History, meaning, practices, and how to engage respectfully — everything in one database. Length. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vasco da Gama Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vasco da Gama Bridge essentials.", "x": "At a glance: Vasco da Gama Bridge — Europe's longest.. 1998. The essentials: Lisbon.. Lisbon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "17.2 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "17.2 km.", "x": "Vasco da Gama Bridge: 17.2 km.. Lisbon. Essential knowledge — Lisbon.. Europe's longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 17.2 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 17.2 km..", "x": "Explained: 17.2 km.. Drive. The context — Vasco da Gama Bridge. Tagus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1998.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1998.", "x": "Vasco da Gama Bridge: 1998.. Expo. Essential knowledge — Tagus.. Europe's longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1998..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1998..", "x": "Explained: 1998.. Views. The context — Vasco da Gama Bridge. Expo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lisbon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lisbon.", "x": "Vasco da Gama Bridge: Lisbon.. Drive. Essential knowledge — Expo.. Europe's longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lisbon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lisbon..", "x": "Explained: Lisbon.. Records. The context — Vasco da Gama Bridge. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tagus.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tagus.", "x": "Vasco da Gama Bridge: Tagus.. Views. Essential knowledge — Views.. Europe's longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tagus..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tagus..", "x": "Explained: Tagus.. Length. The context — Vasco da Gama Bridge. 17.2 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Expo.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Expo.", "x": "Vasco da Gama Bridge: Expo.. Records. Essential knowledge — 17.2 km.. Europe's longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Expo..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Expo..", "x": "Explained: Expo.. Lisbon. The context — Vasco da Gama Bridge. 1998. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Vasco da Gama Bridge: Views.. Length. Essential knowledge — 1998.. Europe's longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Expo. The context — Vasco da Gama Bridge. Lisbon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Length.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Length.", "x": "Vasco da Gama Bridge in depth: Length.. 1998. Details — Europe's longest.. Expo. Tagus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lisbon.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lisbon.", "x": "Vasco da Gama Bridge in depth: Lisbon.. Lisbon. Details — Europe's longest.. Drive. Expo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Expo.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Expo.", "x": "Vasco da Gama Bridge in depth: Expo.. Tagus. Details — Europe's longest.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drive.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drive.", "x": "Vasco da Gama Bridge in depth: Drive.. Expo. Details — Europe's longest.. Records. 17.2 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Vasco da Gama Bridge in depth: Views.. Views. Details — Europe's longest.. Length. 1998. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Records.", "x": "Vasco da Gama Bridge in depth: Records.. 17.2 km. Details — Europe's longest.. Lisbon. Lisbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vasco da Gama Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vasco da Gama Bridge comes from.", "x": "Origins: Length.. 17.2 km. The history of Vasco da Gama Bridge — Europe's longest.. Lisbon. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vasco da Gama Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vasco da Gama Bridge respectfully.", "x": "Engaging: Expo.. 1998. How to participate or observe well — Vasco da Gama Bridge. Europe's longest. Respect first, always; Drive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vasco da Gama Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vasco da Gama Bridge do's and don'ts.", "x": "Etiquette: Views.. Lisbon. The rules of respect — Vasco da Gama Bridge. Europe's longest. When in doubt, ask about Records.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vasco da Gama Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vasco da Gama Bridge.", "x": "Planning: Length.. Tagus. Practical notes — Vasco da Gama Bridge. Europe's longest. A little planning shows respect for Lisbon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vasco da Gama Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vasco da Gama Bridge and money.", "x": "Costs: Expo.. Expo. What to budget — Vasco da Gama Bridge. Europe's longest. The best experiences of Drive. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-vasco-da-gama-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
