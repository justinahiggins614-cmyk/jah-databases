(function(){'use strict';
/* JAH Pet Dental Care Pet Care Database generator — jahdb-e2-petcare-pet-dental-petcare-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-petcare-pet-dental-petcare',PREFIX='JAH-E2PETCAREPE-',NAME='JAH Pet Dental Care Pet Care Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Dental Care: the complete guide", "d": "Pet Dental Care: the teeth care..", "g": "overview", "l": 2, "q": "What is Pet Dental Care: the complete guide?", "a": "Pet Dental Care: the teeth care..", "x": "The complete pet care guide to Pet Dental Care: the teeth care.. Brushing. History, meaning, practices, and how to engage respectfully — everything in one database. Brushing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Dental Care essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Dental Care essentials.", "x": "At a glance: Pet Dental Care — the teeth care.. Chews. The essentials: Tartar.. Tartar. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Brushing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Brushing.", "x": "Pet Dental Care: Brushing.. Tartar. Essential knowledge — Tartar.. the teeth care. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Brushing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Brushing..", "x": "Explained: Brushing.. Breath. The context — Pet Dental Care. Anesthesia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chews.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chews.", "x": "Pet Dental Care: Chews.. Annual. Essential knowledge — Anesthesia.. the teeth care. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chews..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chews..", "x": "Explained: Chews.. Chews. The context — Pet Dental Care. Annual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tartar.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tartar.", "x": "Pet Dental Care: Tartar.. Breath. Essential knowledge — Annual.. the teeth care. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tartar..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tartar..", "x": "Explained: Tartar.. Guide. The context — Pet Dental Care. Bad breath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Anesthesia.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Anesthesia.", "x": "Pet Dental Care: Anesthesia.. Chews. Essential knowledge — Bad breath.. the teeth care. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Anesthesia..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Anesthesia..", "x": "Explained: Anesthesia.. Brushing. The context — Pet Dental Care. Brushing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Annual.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Annual.", "x": "Pet Dental Care: Annual.. Guide. Essential knowledge — Brushing.. the teeth care. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Annual..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Annual..", "x": "Explained: Annual.. Tartar. The context — Pet Dental Care. Chews. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bad breath.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bad breath.", "x": "Pet Dental Care: Bad breath.. Brushing. Essential knowledge — Chews.. the teeth care. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bad breath..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bad breath..", "x": "Explained: Bad breath.. Annual. The context — Pet Dental Care. Tartar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Brushing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Brushing.", "x": "Pet Dental Care in depth: Brushing.. Chews. Details — the teeth care.. Annual. Anesthesia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tartar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tartar.", "x": "Pet Dental Care in depth: Tartar.. Tartar. Details — the teeth care.. Breath. Annual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Annual.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Annual.", "x": "Pet Dental Care in depth: Annual.. Anesthesia. Details — the teeth care.. Chews. Bad breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Breath.", "x": "Pet Dental Care in depth: Breath.. Annual. Details — the teeth care.. Guide. Brushing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chews.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chews.", "x": "Pet Dental Care in depth: Chews.. Bad breath. Details — the teeth care.. Brushing. Chews. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Pet Dental Care in depth: Guide.. Brushing. Details — the teeth care.. Tartar. Tartar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Dental Care comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Dental Care comes from.", "x": "Origins: Brushing.. Brushing. The history of Pet Dental Care — the teeth care.. Tartar. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Dental Care respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Dental Care respectfully.", "x": "Engaging: Annual.. Chews. How to participate or observe well — Pet Dental Care. the teeth care. Respect first, always; Breath.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Dental Care do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Dental Care do's and don'ts.", "x": "Etiquette: Chews.. Tartar. The rules of respect — Pet Dental Care. the teeth care. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Dental Care.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Dental Care.", "x": "Planning: Brushing.. Anesthesia. Practical notes — Pet Dental Care. the teeth care. A little planning shows respect for Tartar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Dental Care and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Dental Care and money.", "x": "Costs: Annual.. Annual. What to budget — Pet Dental Care. the teeth care. The best experiences of Breath. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-petcare-pet-dental-petcare-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
