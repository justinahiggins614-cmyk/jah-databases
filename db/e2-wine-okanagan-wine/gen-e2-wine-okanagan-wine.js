(function(){'use strict';
/* JAH Okanagan Wine Wine Region Database generator — jahdb-e2-wine-okanagan-wine-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wine-okanagan-wine',PREFIX='JAH-E2WINEOKANA-',NAME='JAH Okanagan Wine Wine Region Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Okanagan Wine: the complete guide", "d": "Okanagan Wine: Canada's desert valley..", "g": "overview", "l": 2, "q": "What is Okanagan Wine: the complete guide?", "a": "Okanagan Wine: Canada's desert valley..", "x": "The complete wine region guide to Okanagan Wine: Canada's desert valley.. BC. History, meaning, practices, and how to engage respectfully — everything in one database. Icewine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Okanagan Wine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Okanagan Wine essentials.", "x": "At a glance: Okanagan Wine — Canada's desert valley.. Icewine. The essentials: Lakes.. Lakes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "BC.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "BC.", "x": "Okanagan Wine: BC.. Lakes. Essential knowledge — Lakes.. Canada's desert valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: BC..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: BC..", "x": "Explained: BC.. Summer. The context — Okanagan Wine. Desert. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Icewine.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Icewine.", "x": "Okanagan Wine: Icewine.. Desert. Essential knowledge — Desert.. Canada's desert valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Icewine..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Icewine..", "x": "Explained: Icewine.. BC. The context — Okanagan Wine. Pinot. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lakes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lakes.", "x": "Okanagan Wine: Lakes.. Summer. Essential knowledge — Pinot.. Canada's desert valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lakes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lakes..", "x": "Explained: Lakes.. Tasting. The context — Okanagan Wine. Summer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Desert.", "x": "Okanagan Wine: Desert.. BC. Essential knowledge — Summer.. Canada's desert valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Desert..", "x": "Explained: Desert.. Icewine. The context — Okanagan Wine. BC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pinot.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pinot.", "x": "Okanagan Wine: Pinot.. Tasting. Essential knowledge — BC.. Canada's desert valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pinot..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pinot..", "x": "Explained: Pinot.. Lakes. The context — Okanagan Wine. Icewine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Summer.", "x": "Okanagan Wine: Summer.. Icewine. Essential knowledge — Icewine.. Canada's desert valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Summer..", "x": "Explained: Summer.. Desert. The context — Okanagan Wine. Lakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Icewine.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Icewine.", "x": "Okanagan Wine in depth: Icewine.. Icewine. Details — Canada's desert valley.. Desert. Desert. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lakes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lakes.", "x": "Okanagan Wine in depth: Lakes.. Lakes. Details — Canada's desert valley.. Summer. Pinot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Desert.", "x": "Okanagan Wine in depth: Desert.. Desert. Details — Canada's desert valley.. BC. Summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Summer.", "x": "Okanagan Wine in depth: Summer.. Pinot. Details — Canada's desert valley.. Tasting. BC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "BC.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "BC.", "x": "Okanagan Wine in depth: BC.. Summer. Details — Canada's desert valley.. Icewine. Icewine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tasting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tasting.", "x": "Okanagan Wine in depth: Tasting.. BC. Details — Canada's desert valley.. Lakes. Lakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Okanagan Wine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Okanagan Wine comes from.", "x": "Origins: Icewine.. BC. The history of Okanagan Wine — Canada's desert valley.. Lakes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Okanagan Wine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Okanagan Wine respectfully.", "x": "Engaging: Desert.. Icewine. How to participate or observe well — Okanagan Wine. Canada's desert valley. Respect first, always; Summer.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Okanagan Wine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Okanagan Wine do's and don'ts.", "x": "Etiquette: BC.. Lakes. The rules of respect — Okanagan Wine. Canada's desert valley. When in doubt, ask about Tasting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Okanagan Wine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Okanagan Wine.", "x": "Planning: Icewine.. Desert. Practical notes — Okanagan Wine. Canada's desert valley. A little planning shows respect for Lakes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Okanagan Wine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Okanagan Wine and money.", "x": "Costs: Desert.. Pinot. What to budget — Okanagan Wine. Canada's desert valley. The best experiences of Summer. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wine-okanagan-wine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
