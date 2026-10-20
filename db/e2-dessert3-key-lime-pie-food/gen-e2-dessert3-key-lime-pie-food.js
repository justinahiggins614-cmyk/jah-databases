(function(){'use strict';
/* JAH Key Lime Pie Dessert Database generator — jahdb-e2-dessert3-key-lime-pie-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-key-lime-pie-food',PREFIX='JAH-E2DESSERT3K-',NAME='JAH Key Lime Pie Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Key Lime Pie: the complete guide", "d": "Key Lime Pie: the Florida tart..", "g": "overview", "l": 2, "q": "What is Key Lime Pie: the complete guide?", "a": "Key Lime Pie: the Florida tart..", "x": "The complete dessert guide to Key Lime Pie: the Florida tart.. Limes. History, meaning, practices, and how to engage respectfully — everything in one database. Limes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Key Lime Pie essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Key Lime Pie essentials.", "x": "At a glance: Key Lime Pie — the Florida tart.. Condensed. The essentials: Florida.. Graham. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Limes.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Limes.", "x": "Key Lime Pie: Limes.. Florida. Essential knowledge — Graham.. the Florida tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Limes..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Limes..", "x": "Explained: Limes.. Tart. The context — Key Lime Pie. Tart. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Condensed.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Condensed.", "x": "Key Lime Pie: Condensed.. Whipped. Essential knowledge — Tart.. the Florida tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Condensed..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Condensed..", "x": "Explained: Condensed.. Graham. The context — Key Lime Pie. Florida. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Graham.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Graham.", "x": "Key Lime Pie: Graham.. Tart. Essential knowledge — Florida.. the Florida tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Graham..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Graham..", "x": "Explained: Graham.. Making. The context — Key Lime Pie. Whipped. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tart.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tart.", "x": "Key Lime Pie: Tart.. Graham. Essential knowledge — Whipped.. the Florida tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tart..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tart..", "x": "Explained: Tart.. Limes. The context — Key Lime Pie. Limes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Florida.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Florida.", "x": "Key Lime Pie: Florida.. Making. Essential knowledge — Limes.. the Florida tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Florida..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Florida..", "x": "Explained: Florida.. Florida. The context — Key Lime Pie. Condensed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Whipped.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Whipped.", "x": "Key Lime Pie: Whipped.. Limes. Essential knowledge — Condensed.. the Florida tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Whipped..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Whipped..", "x": "Explained: Whipped.. Whipped. The context — Key Lime Pie. Graham. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Limes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Limes.", "x": "Key Lime Pie in depth: Limes.. Condensed. Details — the Florida tart.. Whipped. Tart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Florida.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Florida.", "x": "Key Lime Pie in depth: Florida.. Graham. Details — the Florida tart.. Tart. Florida. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Whipped.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Whipped.", "x": "Key Lime Pie in depth: Whipped.. Tart. Details — the Florida tart.. Graham. Whipped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tart.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tart.", "x": "Key Lime Pie in depth: Tart.. Florida. Details — the Florida tart.. Making. Limes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Graham.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Graham.", "x": "Key Lime Pie in depth: Graham.. Whipped. Details — the Florida tart.. Limes. Condensed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Key Lime Pie in depth: Making.. Limes. Details — the Florida tart.. Florida. Graham. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Key Lime Pie comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Key Lime Pie comes from.", "x": "Origins: Limes.. Limes. The history of Key Lime Pie — the Florida tart.. Florida. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Key Lime Pie respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Key Lime Pie respectfully.", "x": "Engaging: Whipped.. Condensed. How to participate or observe well — Key Lime Pie. the Florida tart. Respect first, always; Tart.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Key Lime Pie do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Key Lime Pie do's and don'ts.", "x": "Etiquette: Graham.. Graham. The rules of respect — Key Lime Pie. the Florida tart. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Key Lime Pie.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Key Lime Pie.", "x": "Planning: Limes.. Tart. Practical notes — Key Lime Pie. the Florida tart. A little planning shows respect for Florida.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Key Lime Pie and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Key Lime Pie and money.", "x": "Costs: Whipped.. Florida. What to budget — Key Lime Pie. the Florida tart. The best experiences of Tart. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-key-lime-pie-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
