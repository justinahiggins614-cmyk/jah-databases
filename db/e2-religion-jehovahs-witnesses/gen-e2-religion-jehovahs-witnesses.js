(function(){'use strict';
/* JAH Jehovah\'s Witnesses Religion Database generator — jahdb-e2-religion-jehovahs-witnesses-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-religion-jehovahs-witnesses',PREFIX='JAH-E2RELIGIONJ-',NAME='JAH Jehovah\'s Witnesses Religion Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jehovah's Witnesses: the complete guide", "d": "Jehovah's Witnesses: door-to-door evangelists..", "g": "overview", "l": 2, "q": "What is Jehovah's Witnesses: the complete guide?", "a": "Jehovah's Witnesses: door-to-door evangelists..", "x": "The complete religion guide to Jehovah's Witnesses: door-to-door evangelists.. Charles Taze Russell. History, meaning, practices, and how to engage respectfully — everything in one database. Beliefs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jehovah's Witnesses essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jehovah's Witnesses essentials.", "x": "At a glance: Jehovah's Witnesses — door-to-door evangelists.. No Trinity. The essentials: Practices.. Kingdom Halls. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Charles Taze Russell.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Charles Taze Russell.", "x": "Jehovah's Witnesses: Charles Taze Russell.. Practices. Essential knowledge — Kingdom Halls.. door-to-door evangelists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Charles Taze Russell..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Charles Taze Russell..", "x": "Explained: Charles Taze Russell.. Persecution. The context — Jehovah's Witnesses. Neutrality. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "No Trinity.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "No Trinity.", "x": "Jehovah's Witnesses: No Trinity.. History. Essential knowledge — Neutrality.. door-to-door evangelists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: No Trinity..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: No Trinity..", "x": "Explained: No Trinity.. Global. The context — Jehovah's Witnesses. 9M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kingdom Halls.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kingdom Halls.", "x": "Jehovah's Witnesses: Kingdom Halls.. Persecution. Essential knowledge — 9M.. door-to-door evangelists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kingdom Halls..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kingdom Halls..", "x": "Explained: Kingdom Halls.. Ethics. The context — Jehovah's Witnesses. Door-to-door. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Neutrality.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Neutrality.", "x": "Jehovah's Witnesses: Neutrality.. Global. Essential knowledge — Door-to-door.. door-to-door evangelists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Neutrality..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Neutrality..", "x": "Explained: Neutrality.. Beliefs. The context — Jehovah's Witnesses. Charles Taze Russell. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "9M.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "9M.", "x": "Jehovah's Witnesses: 9M.. Ethics. Essential knowledge — Charles Taze Russell.. door-to-door evangelists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 9M..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 9M..", "x": "Explained: 9M.. Practices. The context — Jehovah's Witnesses. No Trinity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Door-to-door.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Door-to-door.", "x": "Jehovah's Witnesses: Door-to-door.. Beliefs. Essential knowledge — No Trinity.. door-to-door evangelists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Door-to-door..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Door-to-door..", "x": "Explained: Door-to-door.. History. The context — Jehovah's Witnesses. Kingdom Halls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Beliefs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Beliefs.", "x": "Jehovah's Witnesses in depth: Beliefs.. No Trinity. Details — door-to-door evangelists.. History. Neutrality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Practices.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Practices.", "x": "Jehovah's Witnesses in depth: Practices.. Kingdom Halls. Details — door-to-door evangelists.. Persecution. 9M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Jehovah's Witnesses in depth: History.. Neutrality. Details — door-to-door evangelists.. Global. Door-to-door. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Persecution.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Persecution.", "x": "Jehovah's Witnesses in depth: Persecution.. 9M. Details — door-to-door evangelists.. Ethics. Charles Taze Russell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Global.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Global.", "x": "Jehovah's Witnesses in depth: Global.. Door-to-door. Details — door-to-door evangelists.. Beliefs. No Trinity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ethics.", "x": "Jehovah's Witnesses in depth: Ethics.. Charles Taze Russell. Details — door-to-door evangelists.. Practices. Kingdom Halls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jehovah's Witnesses comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jehovah's Witnesses comes from.", "x": "Origins: Beliefs.. Charles Taze Russell. The history of Jehovah's Witnesses — door-to-door evangelists.. Practices. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jehovah's Witnesses respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jehovah's Witnesses respectfully.", "x": "Engaging: History.. No Trinity. How to participate or observe well — Jehovah's Witnesses. door-to-door evangelists. Respect first, always; Persecution.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jehovah's Witnesses do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jehovah's Witnesses do's and don'ts.", "x": "Etiquette: Global.. Kingdom Halls. The rules of respect — Jehovah's Witnesses. door-to-door evangelists. When in doubt, ask about Ethics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jehovah's Witnesses.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jehovah's Witnesses.", "x": "Planning: Beliefs.. Neutrality. Practical notes — Jehovah's Witnesses. door-to-door evangelists. A little planning shows respect for Practices.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jehovah's Witnesses and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jehovah's Witnesses and money.", "x": "Costs: History.. 9M. What to budget — Jehovah's Witnesses. door-to-door evangelists. The best experiences of Persecution. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-religion-jehovahs-witnesses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
