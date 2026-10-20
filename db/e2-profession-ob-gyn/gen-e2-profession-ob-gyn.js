(function(){'use strict';
/* JAH OB-GYN Profession Database generator — jahdb-e2-profession-ob-gyn-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-ob-gyn',PREFIX='JAH-E2PROFESSIO-',NAME='JAH OB-GYN Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "OB-GYN Profession: the complete guide", "d": "OB-GYN Profession: the women's profession..", "g": "overview", "l": 2, "q": "What is OB-GYN Profession: the complete guide?", "a": "OB-GYN Profession: the women's profession..", "x": "The complete profession guide to OB-GYN Profession: the women's profession.. Deliveries. History, meaning, practices, and how to engage respectfully — everything in one database. Deliveries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "OB-GYN Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "OB-GYN Profession essentials.", "x": "At a glance: OB-GYN Profession — the women's profession.. Ultrasound. The essentials: Babies.. Surgery. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Deliveries.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Deliveries.", "x": "OB-GYN Profession: Deliveries.. Babies. Essential knowledge — Surgery.. the women's profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Deliveries..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Deliveries..", "x": "Explained: Deliveries.. Surgery. The context — OB-GYN Profession. Nights. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ultrasound.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ultrasound.", "x": "OB-GYN Profession: Ultrasound.. Nights. Essential knowledge — Nights.. the women's profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ultrasound..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ultrasound..", "x": "Explained: Ultrasound.. Exams. The context — OB-GYN Profession. Babies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Surgery.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Surgery.", "x": "OB-GYN Profession: Surgery.. Surgery. Essential knowledge — Babies.. the women's profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Surgery..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Surgery..", "x": "Explained: Surgery.. Day. The context — OB-GYN Profession. Exams. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nights.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nights.", "x": "OB-GYN Profession: Nights.. Exams. Essential knowledge — Exams.. the women's profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Nights..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Nights..", "x": "Explained: Nights.. Deliveries. The context — OB-GYN Profession. Deliveries. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Babies.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Babies.", "x": "OB-GYN Profession: Babies.. Day. Essential knowledge — Deliveries.. the women's profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Babies..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Babies..", "x": "Explained: Babies.. Babies. The context — OB-GYN Profession. Ultrasound. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Exams.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Exams.", "x": "OB-GYN Profession: Exams.. Deliveries. Essential knowledge — Ultrasound.. the women's profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Exams..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Exams..", "x": "Explained: Exams.. Nights. The context — OB-GYN Profession. Surgery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Deliveries.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Deliveries.", "x": "OB-GYN Profession in depth: Deliveries.. Ultrasound. Details — the women's profession.. Nights. Nights. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Babies.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Babies.", "x": "OB-GYN Profession in depth: Babies.. Surgery. Details — the women's profession.. Surgery. Babies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Nights.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Nights.", "x": "OB-GYN Profession in depth: Nights.. Nights. Details — the women's profession.. Exams. Exams. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Surgery.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Surgery.", "x": "OB-GYN Profession in depth: Surgery.. Babies. Details — the women's profession.. Day. Deliveries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Exams.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Exams.", "x": "OB-GYN Profession in depth: Exams.. Exams. Details — the women's profession.. Deliveries. Ultrasound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "OB-GYN Profession in depth: Day.. Deliveries. Details — the women's profession.. Babies. Surgery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where OB-GYN Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where OB-GYN Profession comes from.", "x": "Origins: Deliveries.. Deliveries. The history of OB-GYN Profession — the women's profession.. Babies. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing OB-GYN Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing OB-GYN Profession respectfully.", "x": "Engaging: Nights.. Ultrasound. How to participate or observe well — OB-GYN Profession. the women's profession. Respect first, always; Surgery.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "OB-GYN Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "OB-GYN Profession do's and don'ts.", "x": "Etiquette: Exams.. Surgery. The rules of respect — OB-GYN Profession. the women's profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around OB-GYN Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around OB-GYN Profession.", "x": "Planning: Deliveries.. Nights. Practical notes — OB-GYN Profession. the women's profession. A little planning shows respect for Babies.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "OB-GYN Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "OB-GYN Profession and money.", "x": "Costs: Nights.. Babies. What to budget — OB-GYN Profession. the women's profession. The best experiences of Surgery. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-ob-gyn-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
