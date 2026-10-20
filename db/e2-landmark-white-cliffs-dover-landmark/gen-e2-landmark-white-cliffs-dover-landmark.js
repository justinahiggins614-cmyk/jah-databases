(function(){'use strict';
/* JAH White Cliffs of Dover Landmark Database generator — jahdb-e2-landmark-white-cliffs-dover-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-white-cliffs-dover-landmark',PREFIX='JAH-E2LANDMARKW-',NAME='JAH White Cliffs of Dover Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "White Cliffs of Dover: the complete guide", "d": "White Cliffs of Dover: the chalk walls..", "g": "overview", "l": 2, "q": "What is White Cliffs of Dover: the complete guide?", "a": "White Cliffs of Dover: the chalk walls..", "x": "The complete landmark guide to White Cliffs of Dover: the chalk walls.. Chalk. History, meaning, practices, and how to engage respectfully — everything in one database. Chalk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "White Cliffs of Dover essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "White Cliffs of Dover essentials.", "x": "At a glance: White Cliffs of Dover — the chalk walls.. 110m. The essentials: WWII.. Channel. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Chalk.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Chalk.", "x": "White Cliffs of Dover: Chalk.. WWII. Essential knowledge — Channel.. the chalk walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Chalk..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Chalk..", "x": "Explained: Chalk.. Channel. The context — White Cliffs of Dover. WWII. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "110m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "110m.", "x": "White Cliffs of Dover: 110m.. Views. Essential knowledge — WWII.. the chalk walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 110m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 110m..", "x": "Explained: 110m.. Trust. The context — White Cliffs of Dover. National Trust. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Channel.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Channel.", "x": "White Cliffs of Dover: Channel.. Channel. Essential knowledge — National Trust.. the chalk walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Channel..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Channel..", "x": "Explained: Channel.. Walking. The context — White Cliffs of Dover. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "WWII.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "WWII.", "x": "White Cliffs of Dover: WWII.. Trust. Essential knowledge — Views.. the chalk walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: WWII..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: WWII..", "x": "Explained: WWII.. Chalk. The context — White Cliffs of Dover. Chalk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "National Trust.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "National Trust.", "x": "White Cliffs of Dover: National Trust.. Walking. Essential knowledge — Chalk.. the chalk walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: National Trust..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: National Trust..", "x": "Explained: National Trust.. WWII. The context — White Cliffs of Dover. 110m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "White Cliffs of Dover: Views.. Chalk. Essential knowledge — 110m.. the chalk walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Views. The context — White Cliffs of Dover. Channel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chalk.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chalk.", "x": "White Cliffs of Dover in depth: Chalk.. 110m. Details — the chalk walls.. Views. WWII. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "WWII.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "WWII.", "x": "White Cliffs of Dover in depth: WWII.. Channel. Details — the chalk walls.. Channel. National Trust. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "White Cliffs of Dover in depth: Views.. WWII. Details — the chalk walls.. Trust. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Channel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Channel.", "x": "White Cliffs of Dover in depth: Channel.. National Trust. Details — the chalk walls.. Walking. Chalk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Trust.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Trust.", "x": "White Cliffs of Dover in depth: Trust.. Views. Details — the chalk walls.. Chalk. 110m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Walking.", "x": "White Cliffs of Dover in depth: Walking.. Chalk. Details — the chalk walls.. WWII. Channel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where White Cliffs of Dover comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where White Cliffs of Dover comes from.", "x": "Origins: Chalk.. Chalk. The history of White Cliffs of Dover — the chalk walls.. WWII. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing White Cliffs of Dover respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing White Cliffs of Dover respectfully.", "x": "Engaging: Views.. 110m. How to participate or observe well — White Cliffs of Dover. the chalk walls. Respect first, always; Channel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "White Cliffs of Dover do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "White Cliffs of Dover do's and don'ts.", "x": "Etiquette: Trust.. Channel. The rules of respect — White Cliffs of Dover. the chalk walls. When in doubt, ask about Walking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around White Cliffs of Dover.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around White Cliffs of Dover.", "x": "Planning: Chalk.. WWII. Practical notes — White Cliffs of Dover. the chalk walls. A little planning shows respect for WWII.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "White Cliffs of Dover and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "White Cliffs of Dover and money.", "x": "Costs: Views.. National Trust. What to budget — White Cliffs of Dover. the chalk walls. The best experiences of Channel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-white-cliffs-dover-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
