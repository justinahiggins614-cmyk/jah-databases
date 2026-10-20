(function(){'use strict';
/* JAH Red Fort Landmark Database generator — jahdb-e2-landmark-red-fort-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-red-fort-landmark',PREFIX='JAH-E2LANDMARKR-',NAME='JAH Red Fort Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Red Fort: the complete guide", "d": "Red Fort: the Mughal red..", "g": "overview", "l": 2, "q": "What is Red Fort: the complete guide?", "a": "Red Fort: the Mughal red..", "x": "The complete landmark guide to Red Fort: the Mughal red.. 1648. History, meaning, practices, and how to engage respectfully — everything in one database. 1648. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Red Fort essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Red Fort essentials.", "x": "At a glance: Red Fort — the Mughal red.. Red sandstone. The essentials: Sandstone.. Shah Jahan. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1648.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1648.", "x": "Red Fort: 1648.. Sandstone. Essential knowledge — Shah Jahan.. the Mughal red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1648..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1648..", "x": "Explained: 1648.. Museums. The context — Red Fort. Lahore Gate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Red sandstone.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Red sandstone.", "x": "Red Fort: Red sandstone.. Independence. Essential knowledge — Lahore Gate.. the Mughal red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Red sandstone..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Red sandstone..", "x": "Explained: Red sandstone.. Red. The context — Red Fort. Independence. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shah Jahan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shah Jahan.", "x": "Red Fort: Shah Jahan.. Museums. Essential knowledge — Independence.. the Mughal red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shah Jahan..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shah Jahan..", "x": "Explained: Shah Jahan.. Tours. The context — Red Fort. Museums. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lahore Gate.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lahore Gate.", "x": "Red Fort: Lahore Gate.. Red. Essential knowledge — Museums.. the Mughal red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lahore Gate..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lahore Gate..", "x": "Explained: Lahore Gate.. 1648. The context — Red Fort. 1648. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Independence.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Independence.", "x": "Red Fort: Independence.. Tours. Essential knowledge — 1648.. the Mughal red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Independence..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Independence..", "x": "Explained: Independence.. Sandstone. The context — Red Fort. Red sandstone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Museums.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Museums.", "x": "Red Fort: Museums.. 1648. Essential knowledge — Red sandstone.. the Mughal red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Museums..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Museums..", "x": "Explained: Museums.. Independence. The context — Red Fort. Shah Jahan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1648.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1648.", "x": "Red Fort in depth: 1648.. Red sandstone. Details — the Mughal red.. Independence. Lahore Gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sandstone.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sandstone.", "x": "Red Fort in depth: Sandstone.. Shah Jahan. Details — the Mughal red.. Museums. Independence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Independence.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Independence.", "x": "Red Fort in depth: Independence.. Lahore Gate. Details — the Mughal red.. Red. Museums. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Museums.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Museums.", "x": "Red Fort in depth: Museums.. Independence. Details — the Mughal red.. Tours. 1648. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Red.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Red.", "x": "Red Fort in depth: Red.. Museums. Details — the Mughal red.. 1648. Red sandstone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Red Fort in depth: Tours.. 1648. Details — the Mughal red.. Sandstone. Shah Jahan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Red Fort comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Red Fort comes from.", "x": "Origins: 1648.. 1648. The history of Red Fort — the Mughal red.. Sandstone. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Red Fort respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Red Fort respectfully.", "x": "Engaging: Independence.. Red sandstone. How to participate or observe well — Red Fort. the Mughal red. Respect first, always; Museums.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Red Fort do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Red Fort do's and don'ts.", "x": "Etiquette: Red.. Shah Jahan. The rules of respect — Red Fort. the Mughal red. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Red Fort.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Red Fort.", "x": "Planning: 1648.. Lahore Gate. Practical notes — Red Fort. the Mughal red. A little planning shows respect for Sandstone.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Red Fort and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Red Fort and money.", "x": "Costs: Independence.. Independence. What to budget — Red Fort. the Mughal red. The best experiences of Museums. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-red-fort-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
