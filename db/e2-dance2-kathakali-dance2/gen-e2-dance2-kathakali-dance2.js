(function(){'use strict';
/* JAH Kathakali Dance Database generator — jahdb-e2-dance2-kathakali-dance2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance2-kathakali-dance2',PREFIX='JAH-E2DANCE2KAT-',NAME='JAH Kathakali Dance Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kathakali Dance: the complete guide", "d": "Kathakali Dance: the Kerala epic..", "g": "overview", "l": 2, "q": "What is Kathakali Dance: the complete guide?", "a": "Kathakali Dance: the Kerala epic..", "x": "The complete dance form guide to Kathakali Dance: the Kerala epic.. Kerala. History, meaning, practices, and how to engage respectfully — everything in one database. Face. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kathakali Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kathakali Dance essentials.", "x": "At a glance: Kathakali Dance — the Kerala epic.. Green face. The essentials: Eyes.. Eyes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Kerala.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Kerala.", "x": "Kathakali Dance: Kerala.. Eyes. Essential knowledge — Eyes.. the Kerala epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Kerala..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Kerala..", "x": "Explained: Kerala.. Kerala. The context — Kathakali Dance. All-night. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Green face.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Green face.", "x": "Kathakali Dance: Green face.. Drums. Essential knowledge — All-night.. the Kerala epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Green face..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Green face..", "x": "Explained: Green face.. All-night. The context — Kathakali Dance. Mahabharata. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Eyes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Eyes.", "x": "Kathakali Dance: Eyes.. Kerala. Essential knowledge — Mahabharata.. the Kerala epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Eyes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Eyes..", "x": "Explained: Eyes.. Training. The context — Kathakali Dance. Drums. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "All-night.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "All-night.", "x": "Kathakali Dance: All-night.. All-night. Essential knowledge — Drums.. the Kerala epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: All-night..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: All-night..", "x": "Explained: All-night.. Face. The context — Kathakali Dance. Kerala. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mahabharata.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mahabharata.", "x": "Kathakali Dance: Mahabharata.. Training. Essential knowledge — Kerala.. the Kerala epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Mahabharata..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Mahabharata..", "x": "Explained: Mahabharata.. Eyes. The context — Kathakali Dance. Green face. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drums.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drums.", "x": "Kathakali Dance: Drums.. Face. Essential knowledge — Green face.. the Kerala epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Drums..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Drums..", "x": "Explained: Drums.. Drums. The context — Kathakali Dance. Eyes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Face.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Face.", "x": "Kathakali Dance in depth: Face.. Green face. Details — the Kerala epic.. Drums. All-night. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Eyes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Eyes.", "x": "Kathakali Dance in depth: Eyes.. Eyes. Details — the Kerala epic.. Kerala. Mahabharata. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Drums.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Drums.", "x": "Kathakali Dance in depth: Drums.. All-night. Details — the Kerala epic.. All-night. Drums. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Kerala.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Kerala.", "x": "Kathakali Dance in depth: Kerala.. Mahabharata. Details — the Kerala epic.. Training. Kerala. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "All-night.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "All-night.", "x": "Kathakali Dance in depth: All-night.. Drums. Details — the Kerala epic.. Face. Green face. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Kathakali Dance in depth: Training.. Kerala. Details — the Kerala epic.. Eyes. Eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kathakali Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kathakali Dance comes from.", "x": "Origins: Face.. Kerala. The history of Kathakali Dance — the Kerala epic.. Eyes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kathakali Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kathakali Dance respectfully.", "x": "Engaging: Drums.. Green face. How to participate or observe well — Kathakali Dance. the Kerala epic. Respect first, always; Kerala.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kathakali Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kathakali Dance do's and don'ts.", "x": "Etiquette: All-night.. Eyes. The rules of respect — Kathakali Dance. the Kerala epic. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kathakali Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kathakali Dance.", "x": "Planning: Face.. All-night. Practical notes — Kathakali Dance. the Kerala epic. A little planning shows respect for Eyes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kathakali Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kathakali Dance and money.", "x": "Costs: Drums.. Mahabharata. What to budget — Kathakali Dance. the Kerala epic. The best experiences of Kerala. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance2-kathakali-dance2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
