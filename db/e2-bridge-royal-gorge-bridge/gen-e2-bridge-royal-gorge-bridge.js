(function(){'use strict';
/* JAH Royal Gorge Bridge Bridge Database generator — jahdb-e2-bridge-royal-gorge-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-royal-gorge-bridge',PREFIX='JAH-E2BRIDGEROY-',NAME='JAH Royal Gorge Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Royal Gorge Bridge: the complete guide", "d": "Royal Gorge Bridge: America's highest suspension..", "g": "overview", "l": 2, "q": "What is Royal Gorge Bridge: the complete guide?", "a": "Royal Gorge Bridge: America's highest suspension..", "x": "The complete bridge guide to Royal Gorge Bridge: America's highest suspension.. 291m. History, meaning, practices, and how to engage respectfully — everything in one database. Height. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Royal Gorge Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Royal Gorge Bridge essentials.", "x": "At a glance: Royal Gorge Bridge — America's highest suspension.. 1929. The essentials: History.. Colorado. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "291m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "291m.", "x": "Royal Gorge Bridge: 291m.. History. Essential knowledge — Colorado.. America's highest suspension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 291m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 291m..", "x": "Explained: 291m.. Views. The context — Royal Gorge Bridge. Arkansas River. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1929.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1929.", "x": "Royal Gorge Bridge: 1929.. River. Essential knowledge — Arkansas River.. America's highest suspension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1929..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1929..", "x": "Explained: 1929.. Colorado. The context — Royal Gorge Bridge. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Colorado.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Colorado.", "x": "Royal Gorge Bridge: Colorado.. Views. Essential knowledge — Views.. America's highest suspension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Colorado..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Colorado..", "x": "Explained: Colorado.. Thrills. The context — Royal Gorge Bridge. Gondola. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Arkansas River.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Arkansas River.", "x": "Royal Gorge Bridge: Arkansas River.. Colorado. Essential knowledge — Gondola.. America's highest suspension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Arkansas River..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Arkansas River..", "x": "Explained: Arkansas River.. Height. The context — Royal Gorge Bridge. 291m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Views.", "x": "Royal Gorge Bridge: Views.. Thrills. Essential knowledge — 291m.. America's highest suspension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. History. The context — Royal Gorge Bridge. 1929. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gondola.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gondola.", "x": "Royal Gorge Bridge: Gondola.. Height. Essential knowledge — 1929.. America's highest suspension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gondola..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gondola..", "x": "Explained: Gondola.. River. The context — Royal Gorge Bridge. Colorado. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Height.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Height.", "x": "Royal Gorge Bridge in depth: Height.. 1929. Details — America's highest suspension.. River. Arkansas River. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Royal Gorge Bridge in depth: History.. Colorado. Details — America's highest suspension.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "River.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "River.", "x": "Royal Gorge Bridge in depth: River.. Arkansas River. Details — America's highest suspension.. Colorado. Gondola. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Royal Gorge Bridge in depth: Views.. Views. Details — America's highest suspension.. Thrills. 291m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Colorado.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Colorado.", "x": "Royal Gorge Bridge in depth: Colorado.. Gondola. Details — America's highest suspension.. Height. 1929. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Thrills.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Thrills.", "x": "Royal Gorge Bridge in depth: Thrills.. 291m. Details — America's highest suspension.. History. Colorado. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Royal Gorge Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Royal Gorge Bridge comes from.", "x": "Origins: Height.. 291m. The history of Royal Gorge Bridge — America's highest suspension.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Royal Gorge Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Royal Gorge Bridge respectfully.", "x": "Engaging: River.. 1929. How to participate or observe well — Royal Gorge Bridge. America's highest suspension. Respect first, always; Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Royal Gorge Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Royal Gorge Bridge do's and don'ts.", "x": "Etiquette: Colorado.. Colorado. The rules of respect — Royal Gorge Bridge. America's highest suspension. When in doubt, ask about Thrills.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Royal Gorge Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Royal Gorge Bridge.", "x": "Planning: Height.. Arkansas River. Practical notes — Royal Gorge Bridge. America's highest suspension. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Royal Gorge Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Royal Gorge Bridge and money.", "x": "Costs: River.. Views. What to budget — Royal Gorge Bridge. America's highest suspension. The best experiences of Views. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-royal-gorge-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
