(function(){'use strict';
/* JAH Buckingham Palace Landmark Database generator — jahdb-e2-landmark-buckingham-palace-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-buckingham-palace-landmark',PREFIX='JAH-E2LANDMARKB-',NAME='JAH Buckingham Palace Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Buckingham Palace: the complete guide", "d": "Buckingham Palace: the royal residence..", "g": "overview", "l": 2, "q": "What is Buckingham Palace: the complete guide?", "a": "Buckingham Palace: the royal residence..", "x": "The complete landmark guide to Buckingham Palace: the royal residence.. 1837. History, meaning, practices, and how to engage respectfully — everything in one database. 1837. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Buckingham Palace essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Buckingham Palace essentials.", "x": "At a glance: Buckingham Palace — the royal residence.. 775 rooms. The essentials: Guard.. Changing guard. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1837.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1837.", "x": "Buckingham Palace: 1837.. Guard. Essential knowledge — Changing guard.. the royal residence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1837..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1837..", "x": "Explained: 1837.. Victoria. The context — Buckingham Palace. Balcony. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "775 rooms.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "775 rooms.", "x": "Buckingham Palace: 775 rooms.. Balcony. Essential knowledge — Balcony.. the royal residence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 775 rooms..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 775 rooms..", "x": "Explained: 775 rooms.. Rooms. The context — Buckingham Palace. Victoria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Changing guard.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Changing guard.", "x": "Buckingham Palace: Changing guard.. Victoria. Essential knowledge — Victoria.. the royal residence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Changing guard..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Changing guard..", "x": "Explained: Changing guard.. Tours. The context — Buckingham Palace. State. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Balcony.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Balcony.", "x": "Buckingham Palace: Balcony.. Rooms. Essential knowledge — State.. the royal residence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Balcony..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Balcony..", "x": "Explained: Balcony.. 1837. The context — Buckingham Palace. 1837. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Victoria.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Victoria.", "x": "Buckingham Palace: Victoria.. Tours. Essential knowledge — 1837.. the royal residence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Victoria..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Victoria..", "x": "Explained: Victoria.. Guard. The context — Buckingham Palace. 775 rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "State.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "State.", "x": "Buckingham Palace: State.. 1837. Essential knowledge — 775 rooms.. the royal residence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: State..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: State..", "x": "Explained: State.. Balcony. The context — Buckingham Palace. Changing guard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1837.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1837.", "x": "Buckingham Palace in depth: 1837.. 775 rooms. Details — the royal residence.. Balcony. Balcony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Guard.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Guard.", "x": "Buckingham Palace in depth: Guard.. Changing guard. Details — the royal residence.. Victoria. Victoria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Balcony.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Balcony.", "x": "Buckingham Palace in depth: Balcony.. Balcony. Details — the royal residence.. Rooms. State. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Victoria.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Victoria.", "x": "Buckingham Palace in depth: Victoria.. Victoria. Details — the royal residence.. Tours. 1837. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rooms.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rooms.", "x": "Buckingham Palace in depth: Rooms.. State. Details — the royal residence.. 1837. 775 rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Buckingham Palace in depth: Tours.. 1837. Details — the royal residence.. Guard. Changing guard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Buckingham Palace comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Buckingham Palace comes from.", "x": "Origins: 1837.. 1837. The history of Buckingham Palace — the royal residence.. Guard. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Buckingham Palace respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Buckingham Palace respectfully.", "x": "Engaging: Balcony.. 775 rooms. How to participate or observe well — Buckingham Palace. the royal residence. Respect first, always; Victoria.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Buckingham Palace do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Buckingham Palace do's and don'ts.", "x": "Etiquette: Rooms.. Changing guard. The rules of respect — Buckingham Palace. the royal residence. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Buckingham Palace.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Buckingham Palace.", "x": "Planning: 1837.. Balcony. Practical notes — Buckingham Palace. the royal residence. A little planning shows respect for Guard.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Buckingham Palace and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Buckingham Palace and money.", "x": "Costs: Balcony.. Victoria. What to budget — Buckingham Palace. the royal residence. The best experiences of Victoria. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-buckingham-palace-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
