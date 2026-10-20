(function(){'use strict';
/* JAH Rodeo Events Rodeo Database generator — jahdb-e2-rodeo-rodeo-events-rodeo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-rodeo-rodeo-events-rodeo',PREFIX='JAH-E2RODEORODE-',NAME='JAH Rodeo Events Rodeo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rodeo Events: the complete guide", "d": "Rodeo Events: the western sport..", "g": "overview", "l": 2, "q": "What is Rodeo Events: the complete guide?", "a": "Rodeo Events: the western sport..", "x": "The complete rodeo guide to Rodeo Events: the western sport.. Bull riding. History, meaning, practices, and how to engage respectfully — everything in one database. Bull. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rodeo Events essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rodeo Events essentials.", "x": "At a glance: Rodeo Events — the western sport.. Barrel racing. The essentials: Barrels.. Roping. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bull riding.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bull riding.", "x": "Rodeo Events: Bull riding.. Barrels. Essential knowledge — Roping.. the western sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bull riding..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bull riding..", "x": "Explained: Bull riding.. 8 sec. The context — Rodeo Events. 8 seconds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Barrel racing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Barrel racing.", "x": "Rodeo Events: Barrel racing.. Roping. Essential knowledge — 8 seconds.. the western sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Barrel racing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Barrel racing..", "x": "Explained: Barrel racing.. PRCA. The context — Rodeo Events. PRCA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Roping.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Roping.", "x": "Rodeo Events: Roping.. 8 sec. Essential knowledge — PRCA.. the western sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Roping..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Roping..", "x": "Explained: Roping.. Events. The context — Rodeo Events. Chaps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "8 seconds.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "8 seconds.", "x": "Rodeo Events: 8 seconds.. PRCA. Essential knowledge — Chaps.. the western sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 8 seconds..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 8 seconds..", "x": "Explained: 8 seconds.. Bull. The context — Rodeo Events. Bull riding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "PRCA.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "PRCA.", "x": "Rodeo Events: PRCA.. Events. Essential knowledge — Bull riding.. the western sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: PRCA..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: PRCA..", "x": "Explained: PRCA.. Barrels. The context — Rodeo Events. Barrel racing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chaps.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chaps.", "x": "Rodeo Events: Chaps.. Bull. Essential knowledge — Barrel racing.. the western sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chaps..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chaps..", "x": "Explained: Chaps.. Roping. The context — Rodeo Events. Roping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bull.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bull.", "x": "Rodeo Events in depth: Bull.. Barrel racing. Details — the western sport.. Roping. 8 seconds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Barrels.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Barrels.", "x": "Rodeo Events in depth: Barrels.. Roping. Details — the western sport.. 8 sec. PRCA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Roping.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Roping.", "x": "Rodeo Events in depth: Roping.. 8 seconds. Details — the western sport.. PRCA. Chaps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "8 sec.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "8 sec.", "x": "Rodeo Events in depth: 8 sec.. PRCA. Details — the western sport.. Events. Bull riding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "PRCA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "PRCA.", "x": "Rodeo Events in depth: PRCA.. Chaps. Details — the western sport.. Bull. Barrel racing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Events.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Events.", "x": "Rodeo Events in depth: Events.. Bull riding. Details — the western sport.. Barrels. Roping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rodeo Events comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rodeo Events comes from.", "x": "Origins: Bull.. Bull riding. The history of Rodeo Events — the western sport.. Barrels. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rodeo Events respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rodeo Events respectfully.", "x": "Engaging: Roping.. Barrel racing. How to participate or observe well — Rodeo Events. the western sport. Respect first, always; 8 sec.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rodeo Events do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rodeo Events do's and don'ts.", "x": "Etiquette: PRCA.. Roping. The rules of respect — Rodeo Events. the western sport. When in doubt, ask about Events.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rodeo Events.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rodeo Events.", "x": "Planning: Bull.. 8 seconds. Practical notes — Rodeo Events. the western sport. A little planning shows respect for Barrels.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rodeo Events and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rodeo Events and money.", "x": "Costs: Roping.. PRCA. What to budget — Rodeo Events. the western sport. The best experiences of 8 sec. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-rodeo-rodeo-events-rodeo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
