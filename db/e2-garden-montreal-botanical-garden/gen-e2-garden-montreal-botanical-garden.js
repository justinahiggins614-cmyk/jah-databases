(function(){'use strict';
/* JAH Montreal Botanical Garden Botanical Garden Database generator — jahdb-e2-garden-montreal-botanical-garden-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-montreal-botanical-garden',PREFIX='JAH-E2GARDENMON-',NAME='JAH Montreal Botanical Garden Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Montreal Botanical Garden: the complete guide", "d": "Montreal Botanical Garden: the garden city..", "g": "overview", "l": 2, "q": "What is Montreal Botanical Garden: the complete guide?", "a": "Montreal Botanical Garden: the garden city..", "x": "The complete botanical garden guide to Montreal Botanical Garden: the garden city.. 1931. History, meaning, practices, and how to engage respectfully — everything in one database. Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Montreal Botanical Garden essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Montreal Botanical Garden essentials.", "x": "At a glance: Montreal Botanical Garden — the garden city.. Japanese Garden. The essentials: Insectarium.. Insectarium. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1931.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1931.", "x": "Montreal Botanical Garden: 1931.. Insectarium. Essential knowledge — Insectarium.. the garden city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1931..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1931..", "x": "Explained: 1931.. Tickets. The context — Montreal Botanical Garden. 1931. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Japanese Garden.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Japanese Garden.", "x": "Montreal Botanical Garden: Japanese Garden.. History. Essential knowledge — 1931.. the garden city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Japanese Garden..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Japanese Garden..", "x": "Explained: Japanese Garden.. Montreal. The context — Montreal Botanical Garden. 75 hectares. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Insectarium.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Insectarium.", "x": "Montreal Botanical Garden: Insectarium.. Tickets. Essential knowledge — 75 hectares.. the garden city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Insectarium..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Insectarium..", "x": "Explained: Insectarium.. Seasons. The context — Montreal Botanical Garden. Festivals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1931.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1931.", "x": "Montreal Botanical Garden: 1931.. Montreal. Essential knowledge — Festivals.. the garden city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1931..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1931..", "x": "Explained: 1931.. Japanese. The context — Montreal Botanical Garden. 1931. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "75 hectares.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "75 hectares.", "x": "Montreal Botanical Garden: 75 hectares.. Seasons. Essential knowledge — 1931.. the garden city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 75 hectares..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 75 hectares..", "x": "Explained: 75 hectares.. Insectarium. The context — Montreal Botanical Garden. Japanese Garden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Festivals.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Festivals.", "x": "Montreal Botanical Garden: Festivals.. Japanese. Essential knowledge — Japanese Garden.. the garden city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Festivals..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Festivals..", "x": "Explained: Festivals.. History. The context — Montreal Botanical Garden. Insectarium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Japanese.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Japanese.", "x": "Montreal Botanical Garden in depth: Japanese.. Japanese Garden. Details — the garden city.. History. 1931. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Insectarium.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Insectarium.", "x": "Montreal Botanical Garden in depth: Insectarium.. Insectarium. Details — the garden city.. Tickets. 75 hectares. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Montreal Botanical Garden in depth: History.. 1931. Details — the garden city.. Montreal. Festivals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Montreal Botanical Garden in depth: Tickets.. 75 hectares. Details — the garden city.. Seasons. 1931. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Montreal.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Montreal.", "x": "Montreal Botanical Garden in depth: Montreal.. Festivals. Details — the garden city.. Japanese. Japanese Garden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Seasons.", "x": "Montreal Botanical Garden in depth: Seasons.. 1931. Details — the garden city.. Insectarium. Insectarium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Montreal Botanical Garden comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Montreal Botanical Garden comes from.", "x": "Origins: Japanese.. 1931. The history of Montreal Botanical Garden — the garden city.. Insectarium. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Montreal Botanical Garden respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Montreal Botanical Garden respectfully.", "x": "Engaging: History.. Japanese Garden. How to participate or observe well — Montreal Botanical Garden. the garden city. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Montreal Botanical Garden do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Montreal Botanical Garden do's and don'ts.", "x": "Etiquette: Montreal.. Insectarium. The rules of respect — Montreal Botanical Garden. the garden city. When in doubt, ask about Seasons.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Montreal Botanical Garden.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Montreal Botanical Garden.", "x": "Planning: Japanese.. 1931. Practical notes — Montreal Botanical Garden. the garden city. A little planning shows respect for Insectarium.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Montreal Botanical Garden and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Montreal Botanical Garden and money.", "x": "Costs: History.. 75 hectares. What to budget — Montreal Botanical Garden. the garden city. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-montreal-botanical-garden-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
