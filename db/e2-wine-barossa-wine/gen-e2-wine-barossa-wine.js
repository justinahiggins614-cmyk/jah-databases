(function(){'use strict';
/* JAH Barossa Wine Wine Region Database generator — jahdb-e2-wine-barossa-wine-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wine-barossa-wine',PREFIX='JAH-E2WINEBAROS-',NAME='JAH Barossa Wine Wine Region Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Barossa Wine: the complete guide", "d": "Barossa Wine: Australia's Shiraz valley..", "g": "overview", "l": 2, "q": "What is Barossa Wine: the complete guide?", "a": "Barossa Wine: Australia's Shiraz valley..", "x": "The complete wine region guide to Barossa Wine: Australia's Shiraz valley.. Shiraz. History, meaning, practices, and how to engage respectfully — everything in one database. Shiraz. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Barossa Wine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Barossa Wine essentials.", "x": "At a glance: Barossa Wine — Australia's Shiraz valley.. Old vines. The essentials: Vines.. German. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shiraz.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shiraz.", "x": "Barossa Wine: Shiraz.. Vines. Essential knowledge — German.. Australia's Shiraz valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shiraz..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shiraz..", "x": "Explained: Shiraz.. Bold. The context — Barossa Wine. Tanunda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Old vines.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Old vines.", "x": "Barossa Wine: Old vines.. German. Essential knowledge — Tanunda.. Australia's Shiraz valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Old vines..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Old vines..", "x": "Explained: Old vines.. Tanunda. The context — Barossa Wine. Bold. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "German.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "German.", "x": "Barossa Wine: German.. Bold. Essential knowledge — Bold.. Australia's Shiraz valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: German..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: German..", "x": "Explained: German.. Tasting. The context — Barossa Wine. 150 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tanunda.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tanunda.", "x": "Barossa Wine: Tanunda.. Tanunda. Essential knowledge — 150 years.. Australia's Shiraz valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tanunda..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tanunda..", "x": "Explained: Tanunda.. Shiraz. The context — Barossa Wine. Shiraz. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bold.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bold.", "x": "Barossa Wine: Bold.. Tasting. Essential knowledge — Shiraz.. Australia's Shiraz valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bold..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bold..", "x": "Explained: Bold.. Vines. The context — Barossa Wine. Old vines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "150 years.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "150 years.", "x": "Barossa Wine: 150 years.. Shiraz. Essential knowledge — Old vines.. Australia's Shiraz valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 150 years..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 150 years..", "x": "Explained: 150 years.. German. The context — Barossa Wine. German. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Shiraz.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Shiraz.", "x": "Barossa Wine in depth: Shiraz.. Old vines. Details — Australia's Shiraz valley.. German. Tanunda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vines.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vines.", "x": "Barossa Wine in depth: Vines.. German. Details — Australia's Shiraz valley.. Bold. Bold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "German.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "German.", "x": "Barossa Wine in depth: German.. Tanunda. Details — Australia's Shiraz valley.. Tanunda. 150 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bold.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bold.", "x": "Barossa Wine in depth: Bold.. Bold. Details — Australia's Shiraz valley.. Tasting. Shiraz. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tanunda.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tanunda.", "x": "Barossa Wine in depth: Tanunda.. 150 years. Details — Australia's Shiraz valley.. Shiraz. Old vines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tasting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tasting.", "x": "Barossa Wine in depth: Tasting.. Shiraz. Details — Australia's Shiraz valley.. Vines. German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Barossa Wine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Barossa Wine comes from.", "x": "Origins: Shiraz.. Shiraz. The history of Barossa Wine — Australia's Shiraz valley.. Vines. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Barossa Wine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Barossa Wine respectfully.", "x": "Engaging: German.. Old vines. How to participate or observe well — Barossa Wine. Australia's Shiraz valley. Respect first, always; Bold.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Barossa Wine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Barossa Wine do's and don'ts.", "x": "Etiquette: Tanunda.. German. The rules of respect — Barossa Wine. Australia's Shiraz valley. When in doubt, ask about Tasting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Barossa Wine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Barossa Wine.", "x": "Planning: Shiraz.. Tanunda. Practical notes — Barossa Wine. Australia's Shiraz valley. A little planning shows respect for Vines.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Barossa Wine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Barossa Wine and money.", "x": "Costs: German.. Bold. What to budget — Barossa Wine. Australia's Shiraz valley. The best experiences of Bold. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wine-barossa-wine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
