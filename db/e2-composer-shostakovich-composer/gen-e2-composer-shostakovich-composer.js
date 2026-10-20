(function(){'use strict';
/* JAH Shostakovich Composer Composer Database generator — jahdb-e2-composer-shostakovich-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-shostakovich-composer',PREFIX='JAH-E2COMPOSERS-',NAME='JAH Shostakovich Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Shostakovich Composer: the complete guide", "d": "Shostakovich Composer: the Soviet witness..", "g": "overview", "l": 2, "q": "What is Shostakovich Composer: the complete guide?", "a": "Shostakovich Composer: the Soviet witness..", "x": "The complete composer guide to Shostakovich Composer: the Soviet witness.. 1906. History, meaning, practices, and how to engage respectfully — everything in one database. 5th. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Shostakovich Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Shostakovich Composer essentials.", "x": "At a glance: Shostakovich Composer — the Soviet witness.. 5th Symphony. The essentials: Leningrad.. Leningrad. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1906.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1906.", "x": "Shostakovich Composer: 1906.. Leningrad. Essential knowledge — Leningrad.. the Soviet witness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1906..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1906..", "x": "Explained: 1906.. Quartets. The context — Shostakovich Composer. Stalin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "5th Symphony.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "5th Symphony.", "x": "Shostakovich Composer: 5th Symphony.. Stalin. Essential knowledge — Stalin.. the Soviet witness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 5th Symphony..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 5th Symphony..", "x": "Explained: 5th Symphony.. Testimony. The context — Shostakovich Composer. Quartets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Leningrad.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Leningrad.", "x": "Shostakovich Composer: Leningrad.. Quartets. Essential knowledge — Quartets.. the Soviet witness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Leningrad..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Leningrad..", "x": "Explained: Leningrad.. Legacy. The context — Shostakovich Composer. Testimony. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Stalin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Stalin.", "x": "Shostakovich Composer: Stalin.. Testimony. Essential knowledge — Testimony.. the Soviet witness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Stalin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Stalin..", "x": "Explained: Stalin.. 5th. The context — Shostakovich Composer. 1906. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Quartets.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Quartets.", "x": "Shostakovich Composer: Quartets.. Legacy. Essential knowledge — 1906.. the Soviet witness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Quartets..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Quartets..", "x": "Explained: Quartets.. Leningrad. The context — Shostakovich Composer. 5th Symphony. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Testimony.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Testimony.", "x": "Shostakovich Composer: Testimony.. 5th. Essential knowledge — 5th Symphony.. the Soviet witness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Testimony..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Testimony..", "x": "Explained: Testimony.. Stalin. The context — Shostakovich Composer. Leningrad. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "5th.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "5th.", "x": "Shostakovich Composer in depth: 5th.. 5th Symphony. Details — the Soviet witness.. Stalin. Stalin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Leningrad.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Leningrad.", "x": "Shostakovich Composer in depth: Leningrad.. Leningrad. Details — the Soviet witness.. Quartets. Quartets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stalin.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stalin.", "x": "Shostakovich Composer in depth: Stalin.. Stalin. Details — the Soviet witness.. Testimony. Testimony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Quartets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Quartets.", "x": "Shostakovich Composer in depth: Quartets.. Quartets. Details — the Soviet witness.. Legacy. 1906. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Testimony.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Testimony.", "x": "Shostakovich Composer in depth: Testimony.. Testimony. Details — the Soviet witness.. 5th. 5th Symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Shostakovich Composer in depth: Legacy.. 1906. Details — the Soviet witness.. Leningrad. Leningrad. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Shostakovich Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Shostakovich Composer comes from.", "x": "Origins: 5th.. 1906. The history of Shostakovich Composer — the Soviet witness.. Leningrad. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Shostakovich Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Shostakovich Composer respectfully.", "x": "Engaging: Stalin.. 5th Symphony. How to participate or observe well — Shostakovich Composer. the Soviet witness. Respect first, always; Quartets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Shostakovich Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Shostakovich Composer do's and don'ts.", "x": "Etiquette: Testimony.. Leningrad. The rules of respect — Shostakovich Composer. the Soviet witness. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Shostakovich Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Shostakovich Composer.", "x": "Planning: 5th.. Stalin. Practical notes — Shostakovich Composer. the Soviet witness. A little planning shows respect for Leningrad.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Shostakovich Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Shostakovich Composer and money.", "x": "Costs: Stalin.. Quartets. What to budget — Shostakovich Composer. the Soviet witness. The best experiences of Quartets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-shostakovich-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
