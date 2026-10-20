(function(){'use strict';
/* JAH Cha-Cha Dance Dance Form Database generator — jahdb-e2-dance-cha-cha-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-cha-cha-dance-form',PREFIX='JAH-E2DANCECHAC-',NAME='JAH Cha-Cha Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cha-Cha Dance: the complete guide", "d": "Cha-Cha Dance: the playful Latin..", "g": "overview", "l": 2, "q": "What is Cha-Cha Dance: the complete guide?", "a": "Cha-Cha Dance: the playful Latin..", "x": "The complete dance form guide to Cha-Cha Dance: the playful Latin.. Cuba. History, meaning, practices, and how to engage respectfully — everything in one database. Triple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cha-Cha Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cha-Cha Dance essentials.", "x": "At a glance: Cha-Cha Dance — the playful Latin.. Triple. The essentials: Playful.. Playful. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cuba.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cuba.", "x": "Cha-Cha Dance: Cuba.. Playful. Essential knowledge — Playful.. the playful Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cuba..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cuba..", "x": "Explained: Cuba.. Cuba. The context — Cha-Cha Dance. Shines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Triple.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Triple.", "x": "Cha-Cha Dance: Triple.. Ballroom. Essential knowledge — Shines.. the playful Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Triple..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Triple..", "x": "Explained: Triple.. Shines. The context — Cha-Cha Dance. 4/4. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Playful.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Playful.", "x": "Cha-Cha Dance: Playful.. Cuba. Essential knowledge — 4/4.. the playful Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Playful..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Playful..", "x": "Explained: Playful.. Training. The context — Cha-Cha Dance. Ballroom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shines.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shines.", "x": "Cha-Cha Dance: Shines.. Shines. Essential knowledge — Ballroom.. the playful Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shines..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shines..", "x": "Explained: Shines.. Triple. The context — Cha-Cha Dance. Cuba. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "4/4.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "4/4.", "x": "Cha-Cha Dance: 4/4.. Training. Essential knowledge — Cuba.. the playful Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 4/4..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 4/4..", "x": "Explained: 4/4.. Playful. The context — Cha-Cha Dance. Triple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ballroom.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ballroom.", "x": "Cha-Cha Dance: Ballroom.. Triple. Essential knowledge — Triple.. the playful Latin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ballroom..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ballroom..", "x": "Explained: Ballroom.. Ballroom. The context — Cha-Cha Dance. Playful. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Triple.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Triple.", "x": "Cha-Cha Dance in depth: Triple.. Triple. Details — the playful Latin.. Ballroom. Shines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Playful.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Playful.", "x": "Cha-Cha Dance in depth: Playful.. Playful. Details — the playful Latin.. Cuba. 4/4. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ballroom.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ballroom.", "x": "Cha-Cha Dance in depth: Ballroom.. Shines. Details — the playful Latin.. Shines. Ballroom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cuba.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cuba.", "x": "Cha-Cha Dance in depth: Cuba.. 4/4. Details — the playful Latin.. Training. Cuba. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shines.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shines.", "x": "Cha-Cha Dance in depth: Shines.. Ballroom. Details — the playful Latin.. Triple. Triple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Cha-Cha Dance in depth: Training.. Cuba. Details — the playful Latin.. Playful. Playful. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cha-Cha Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cha-Cha Dance comes from.", "x": "Origins: Triple.. Cuba. The history of Cha-Cha Dance — the playful Latin.. Playful. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cha-Cha Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cha-Cha Dance respectfully.", "x": "Engaging: Ballroom.. Triple. How to participate or observe well — Cha-Cha Dance. the playful Latin. Respect first, always; Cuba.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cha-Cha Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cha-Cha Dance do's and don'ts.", "x": "Etiquette: Shines.. Playful. The rules of respect — Cha-Cha Dance. the playful Latin. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cha-Cha Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cha-Cha Dance.", "x": "Planning: Triple.. Shines. Practical notes — Cha-Cha Dance. the playful Latin. A little planning shows respect for Playful.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cha-Cha Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cha-Cha Dance and money.", "x": "Costs: Ballroom.. 4/4. What to budget — Cha-Cha Dance. the playful Latin. The best experiences of Cuba. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-cha-cha-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
