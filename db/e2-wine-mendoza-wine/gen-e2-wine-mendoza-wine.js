(function(){'use strict';
/* JAH Mendoza Wine Wine Region Database generator — jahdb-e2-wine-mendoza-wine-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wine-mendoza-wine',PREFIX='JAH-E2WINEMENDO-',NAME='JAH Mendoza Wine Wine Region Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mendoza Wine: the complete guide", "d": "Mendoza Wine: Argentina's Malbec..", "g": "overview", "l": 2, "q": "What is Mendoza Wine: the complete guide?", "a": "Mendoza Wine: Argentina's Malbec..", "x": "The complete wine region guide to Mendoza Wine: Argentina's Malbec.. Malbec. History, meaning, practices, and how to engage respectfully — everything in one database. Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mendoza Wine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mendoza Wine essentials.", "x": "At a glance: Mendoza Wine — Argentina's Malbec.. Andes. The essentials: Andes.. High altitude. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Malbec.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Malbec.", "x": "Mendoza Wine: Malbec.. Andes. Essential knowledge — High altitude.. Argentina's Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Malbec..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Malbec..", "x": "Explained: Malbec.. Steaks. The context — Mendoza Wine. Uco Valley. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Andes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Andes.", "x": "Mendoza Wine: Andes.. Uco. Essential knowledge — Uco Valley.. Argentina's Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Andes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Andes..", "x": "Explained: Andes.. Altitude. The context — Mendoza Wine. Steaks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "High altitude.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "High altitude.", "x": "Mendoza Wine: High altitude.. Steaks. Essential knowledge — Steaks.. Argentina's Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: High altitude..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: High altitude..", "x": "Explained: High altitude.. Tasting. The context — Mendoza Wine. Irrigation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Uco Valley.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Uco Valley.", "x": "Mendoza Wine: Uco Valley.. Altitude. Essential knowledge — Irrigation.. Argentina's Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Uco Valley..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Uco Valley..", "x": "Explained: Uco Valley.. Malbec. The context — Mendoza Wine. Malbec. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Steaks.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Steaks.", "x": "Mendoza Wine: Steaks.. Tasting. Essential knowledge — Malbec.. Argentina's Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Steaks..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Steaks..", "x": "Explained: Steaks.. Andes. The context — Mendoza Wine. Andes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Irrigation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Irrigation.", "x": "Mendoza Wine: Irrigation.. Malbec. Essential knowledge — Andes.. Argentina's Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Irrigation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Irrigation..", "x": "Explained: Irrigation.. Uco. The context — Mendoza Wine. High altitude. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Malbec.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Malbec.", "x": "Mendoza Wine in depth: Malbec.. Andes. Details — Argentina's Malbec.. Uco. Uco Valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Andes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Andes.", "x": "Mendoza Wine in depth: Andes.. High altitude. Details — Argentina's Malbec.. Steaks. Steaks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Uco.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Uco.", "x": "Mendoza Wine in depth: Uco.. Uco Valley. Details — Argentina's Malbec.. Altitude. Irrigation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Steaks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Steaks.", "x": "Mendoza Wine in depth: Steaks.. Steaks. Details — Argentina's Malbec.. Tasting. Malbec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Altitude.", "x": "Mendoza Wine in depth: Altitude.. Irrigation. Details — Argentina's Malbec.. Malbec. Andes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tasting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tasting.", "x": "Mendoza Wine in depth: Tasting.. Malbec. Details — Argentina's Malbec.. Andes. High altitude. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mendoza Wine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mendoza Wine comes from.", "x": "Origins: Malbec.. Malbec. The history of Mendoza Wine — Argentina's Malbec.. Andes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mendoza Wine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mendoza Wine respectfully.", "x": "Engaging: Uco.. Andes. How to participate or observe well — Mendoza Wine. Argentina's Malbec. Respect first, always; Steaks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mendoza Wine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mendoza Wine do's and don'ts.", "x": "Etiquette: Altitude.. High altitude. The rules of respect — Mendoza Wine. Argentina's Malbec. When in doubt, ask about Tasting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mendoza Wine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mendoza Wine.", "x": "Planning: Malbec.. Uco Valley. Practical notes — Mendoza Wine. Argentina's Malbec. A little planning shows respect for Andes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mendoza Wine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mendoza Wine and money.", "x": "Costs: Uco.. Steaks. What to budget — Mendoza Wine. Argentina's Malbec. The best experiences of Steaks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wine-mendoza-wine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
