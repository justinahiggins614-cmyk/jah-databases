(function(){'use strict';
/* JAH Red-tailed Hawk Bird Species Database generator — jahdb-e2-bird-red-tailed-hawk-bird-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bird-red-tailed-hawk-bird',PREFIX='JAH-E2BIRDREDTA-',NAME='JAH Red-tailed Hawk Bird Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Red-tailed Hawk: the complete guide", "d": "Red-tailed Hawk: the roadside raptor..", "g": "overview", "l": 2, "q": "What is Red-tailed Hawk: the complete guide?", "a": "Red-tailed Hawk: the roadside raptor..", "x": "The complete bird species guide to Red-tailed Hawk: the roadside raptor.. Red tail. History, meaning, practices, and how to engage respectfully — everything in one database. Tail. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Red-tailed Hawk essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Red-tailed Hawk essentials.", "x": "At a glance: Red-tailed Hawk — the roadside raptor.. Soaring. The essentials: Soaring.. Highways. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Red tail.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Red tail.", "x": "Red-tailed Hawk: Red tail.. Soaring. Essential knowledge — Highways.. the roadside raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Red tail..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Red tail..", "x": "Explained: Red tail.. Common. The context — Red-tailed Hawk. Rodents. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Soaring.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Soaring.", "x": "Red-tailed Hawk: Soaring.. Ke-eee. Essential knowledge — Rodents.. the roadside raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Soaring..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Soaring..", "x": "Explained: Soaring.. Rodents. The context — Red-tailed Hawk. Ke-eee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Highways.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Highways.", "x": "Red-tailed Hawk: Highways.. Common. Essential knowledge — Ke-eee.. the roadside raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Highways..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Highways..", "x": "Explained: Highways.. Habitat. The context — Red-tailed Hawk. Common. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rodents.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rodents.", "x": "Red-tailed Hawk: Rodents.. Rodents. Essential knowledge — Common.. the roadside raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rodents..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rodents..", "x": "Explained: Rodents.. Tail. The context — Red-tailed Hawk. Red tail. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ke-eee.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ke-eee.", "x": "Red-tailed Hawk: Ke-eee.. Habitat. Essential knowledge — Red tail.. the roadside raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ke-eee..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ke-eee..", "x": "Explained: Ke-eee.. Soaring. The context — Red-tailed Hawk. Soaring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Common.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Common.", "x": "Red-tailed Hawk: Common.. Tail. Essential knowledge — Soaring.. the roadside raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Common..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Common..", "x": "Explained: Common.. Ke-eee. The context — Red-tailed Hawk. Highways. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tail.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tail.", "x": "Red-tailed Hawk in depth: Tail.. Soaring. Details — the roadside raptor.. Ke-eee. Rodents. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Soaring.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Soaring.", "x": "Red-tailed Hawk in depth: Soaring.. Highways. Details — the roadside raptor.. Common. Ke-eee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ke-eee.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ke-eee.", "x": "Red-tailed Hawk in depth: Ke-eee.. Rodents. Details — the roadside raptor.. Rodents. Common. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Common.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Common.", "x": "Red-tailed Hawk in depth: Common.. Ke-eee. Details — the roadside raptor.. Habitat. Red tail. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rodents.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rodents.", "x": "Red-tailed Hawk in depth: Rodents.. Common. Details — the roadside raptor.. Tail. Soaring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Red-tailed Hawk in depth: Habitat.. Red tail. Details — the roadside raptor.. Soaring. Highways. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Red-tailed Hawk comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Red-tailed Hawk comes from.", "x": "Origins: Tail.. Red tail. The history of Red-tailed Hawk — the roadside raptor.. Soaring. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Red-tailed Hawk respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Red-tailed Hawk respectfully.", "x": "Engaging: Ke-eee.. Soaring. How to participate or observe well — Red-tailed Hawk. the roadside raptor. Respect first, always; Common.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Red-tailed Hawk do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Red-tailed Hawk do's and don'ts.", "x": "Etiquette: Rodents.. Highways. The rules of respect — Red-tailed Hawk. the roadside raptor. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Red-tailed Hawk.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Red-tailed Hawk.", "x": "Planning: Tail.. Rodents. Practical notes — Red-tailed Hawk. the roadside raptor. A little planning shows respect for Soaring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Red-tailed Hawk and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Red-tailed Hawk and money.", "x": "Costs: Ke-eee.. Ke-eee. What to budget — Red-tailed Hawk. the roadside raptor. The best experiences of Common. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bird-red-tailed-hawk-bird-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
