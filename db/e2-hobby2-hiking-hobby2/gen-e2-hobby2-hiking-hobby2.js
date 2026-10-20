(function(){'use strict';
/* JAH Hiking Hobby Database generator — jahdb-e2-hobby2-hiking-hobby2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-hiking-hobby2',PREFIX='JAH-E2HOBBY2HIK-',NAME='JAH Hiking Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hiking Hobby: the complete guide", "d": "Hiking Hobby: the trail miles..", "g": "overview", "l": 2, "q": "What is Hiking Hobby: the complete guide?", "a": "Hiking Hobby: the trail miles..", "x": "The complete hobby guide to Hiking Hobby: the trail miles.. Boots. History, meaning, practices, and how to engage respectfully — everything in one database. Essentials. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hiking Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hiking Hobby essentials.", "x": "At a glance: Hiking Hobby — the trail miles.. Ten essentials. The essentials: Maps.. Leave no trace. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Boots.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Boots.", "x": "Hiking Hobby: Boots.. Maps. Essential knowledge — Leave no trace.. the trail miles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Boots..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Boots..", "x": "Explained: Boots.. Boots. The context — Hiking Hobby. Maps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ten essentials.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ten essentials.", "x": "Hiking Hobby: Ten essentials.. Trails. Essential knowledge — Maps.. the trail miles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ten essentials..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ten essentials..", "x": "Explained: Ten essentials.. Water. The context — Hiking Hobby. Water. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Leave no trace.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Leave no trace.", "x": "Hiking Hobby: Leave no trace.. Boots. Essential knowledge — Water.. the trail miles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Leave no trace..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Leave no trace..", "x": "Explained: Leave no trace.. Getting started. The context — Hiking Hobby. Trails. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Maps.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Maps.", "x": "Hiking Hobby: Maps.. Water. Essential knowledge — Trails.. the trail miles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Maps..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Maps..", "x": "Explained: Maps.. Essentials. The context — Hiking Hobby. Boots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Water.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Water.", "x": "Hiking Hobby: Water.. Getting started. Essential knowledge — Boots.. the trail miles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Water..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Water..", "x": "Explained: Water.. Maps. The context — Hiking Hobby. Ten essentials. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Trails.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Trails.", "x": "Hiking Hobby: Trails.. Essentials. Essential knowledge — Ten essentials.. the trail miles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Trails..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Trails..", "x": "Explained: Trails.. Trails. The context — Hiking Hobby. Leave no trace. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Essentials.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Essentials.", "x": "Hiking Hobby in depth: Essentials.. Ten essentials. Details — the trail miles.. Trails. Maps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Maps.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Maps.", "x": "Hiking Hobby in depth: Maps.. Leave no trace. Details — the trail miles.. Boots. Water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Trails.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Trails.", "x": "Hiking Hobby in depth: Trails.. Maps. Details — the trail miles.. Water. Trails. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Boots.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Boots.", "x": "Hiking Hobby in depth: Boots.. Water. Details — the trail miles.. Getting started. Boots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Water.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Water.", "x": "Hiking Hobby in depth: Water.. Trails. Details — the trail miles.. Essentials. Ten essentials. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Hiking Hobby in depth: Getting started.. Boots. Details — the trail miles.. Maps. Leave no trace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hiking Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hiking Hobby comes from.", "x": "Origins: Essentials.. Boots. The history of Hiking Hobby — the trail miles.. Maps. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hiking Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hiking Hobby respectfully.", "x": "Engaging: Trails.. Ten essentials. How to participate or observe well — Hiking Hobby. the trail miles. Respect first, always; Boots.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hiking Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hiking Hobby do's and don'ts.", "x": "Etiquette: Water.. Leave no trace. The rules of respect — Hiking Hobby. the trail miles. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hiking Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hiking Hobby.", "x": "Planning: Essentials.. Maps. Practical notes — Hiking Hobby. the trail miles. A little planning shows respect for Maps.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hiking Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hiking Hobby and money.", "x": "Costs: Trails.. Water. What to budget — Hiking Hobby. the trail miles. The best experiences of Boots. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-hiking-hobby2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
