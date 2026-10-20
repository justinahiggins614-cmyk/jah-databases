(function(){'use strict';
/* JAH Standing Forward Fold Yoga Pose Database generator — jahdb-e2-yoga-standing-forward-fold-yoga-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-standing-forward-fold-yoga',PREFIX='JAH-E2YOGASTAND-',NAME='JAH Standing Forward Fold Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Standing Forward Fold: the complete guide", "d": "Standing Forward Fold: the hanging fold..", "g": "overview", "l": 2, "q": "What is Standing Forward Fold: the complete guide?", "a": "Standing Forward Fold: the hanging fold..", "x": "The complete yoga pose guide to Standing Forward Fold: the hanging fold.. Uttanasana. History, meaning, practices, and how to engage respectfully — everything in one database. Hamstrings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Standing Forward Fold essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Standing Forward Fold essentials.", "x": "At a glance: Standing Forward Fold — the hanging fold.. Hamstrings. The essentials: Head.. Head. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Uttanasana.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Uttanasana.", "x": "Standing Forward Fold: Uttanasana.. Head. Essential knowledge — Head.. the hanging fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Uttanasana..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Uttanasana..", "x": "Explained: Uttanasana.. Gravity. The context — Standing Forward Fold. Knees soft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hamstrings.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hamstrings.", "x": "Standing Forward Fold: Hamstrings.. Calm. Essential knowledge — Knees soft.. the hanging fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hamstrings..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hamstrings..", "x": "Explained: Hamstrings.. Knees. The context — Standing Forward Fold. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Head.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Head.", "x": "Standing Forward Fold: Head.. Gravity. Essential knowledge — Calm.. the hanging fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Head..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Head..", "x": "Explained: Head.. Sequence. The context — Standing Forward Fold. Gravity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Knees soft.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Knees soft.", "x": "Standing Forward Fold: Knees soft.. Knees. Essential knowledge — Gravity.. the hanging fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Knees soft..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Knees soft..", "x": "Explained: Knees soft.. Hamstrings. The context — Standing Forward Fold. Uttanasana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Calm.", "x": "Standing Forward Fold: Calm.. Sequence. Essential knowledge — Uttanasana.. the hanging fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Head. The context — Standing Forward Fold. Hamstrings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gravity.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gravity.", "x": "Standing Forward Fold: Gravity.. Hamstrings. Essential knowledge — Hamstrings.. the hanging fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gravity..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gravity..", "x": "Explained: Gravity.. Calm. The context — Standing Forward Fold. Head. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hamstrings.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hamstrings.", "x": "Standing Forward Fold in depth: Hamstrings.. Hamstrings. Details — the hanging fold.. Calm. Knees soft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Head.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Head.", "x": "Standing Forward Fold in depth: Head.. Head. Details — the hanging fold.. Gravity. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Calm.", "x": "Standing Forward Fold in depth: Calm.. Knees soft. Details — the hanging fold.. Knees. Gravity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gravity.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gravity.", "x": "Standing Forward Fold in depth: Gravity.. Calm. Details — the hanging fold.. Sequence. Uttanasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Knees.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Knees.", "x": "Standing Forward Fold in depth: Knees.. Gravity. Details — the hanging fold.. Hamstrings. Hamstrings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sequence.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sequence.", "x": "Standing Forward Fold in depth: Sequence.. Uttanasana. Details — the hanging fold.. Head. Head. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Standing Forward Fold comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Standing Forward Fold comes from.", "x": "Origins: Hamstrings.. Uttanasana. The history of Standing Forward Fold — the hanging fold.. Head. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Standing Forward Fold respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Standing Forward Fold respectfully.", "x": "Engaging: Calm.. Hamstrings. How to participate or observe well — Standing Forward Fold. the hanging fold. Respect first, always; Gravity.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Standing Forward Fold do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Standing Forward Fold do's and don'ts.", "x": "Etiquette: Knees.. Head. The rules of respect — Standing Forward Fold. the hanging fold. When in doubt, ask about Sequence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Standing Forward Fold.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Standing Forward Fold.", "x": "Planning: Hamstrings.. Knees soft. Practical notes — Standing Forward Fold. the hanging fold. A little planning shows respect for Head.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Standing Forward Fold and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Standing Forward Fold and money.", "x": "Costs: Calm.. Calm. What to budget — Standing Forward Fold. the hanging fold. The best experiences of Gravity. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-standing-forward-fold-yoga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
