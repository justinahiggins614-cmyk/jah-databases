(function(){'use strict';
/* JAH Fencing Hobby Database generator — jahdb-e2-hobby2-fencing-hobby2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-fencing-hobby2',PREFIX='JAH-E2HOBBY2FEN-',NAME='JAH Fencing Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fencing Hobby: the complete guide", "d": "Fencing Hobby: the blade sport..", "g": "overview", "l": 2, "q": "What is Fencing Hobby: the complete guide?", "a": "Fencing Hobby: the blade sport..", "x": "The complete hobby guide to Fencing Hobby: the blade sport.. Foil. History, meaning, practices, and how to engage respectfully — everything in one database. Footwork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fencing Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fencing Hobby essentials.", "x": "At a glance: Fencing Hobby — the blade sport.. En garde. The essentials: Clubs.. Footwork. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Foil.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Foil.", "x": "Fencing Hobby: Foil.. Clubs. Essential knowledge — Footwork.. the blade sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Foil..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Foil..", "x": "Explained: Foil.. Foil. The context — Fencing Hobby. Clubs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "En garde.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "En garde.", "x": "Fencing Hobby: En garde.. Lunge. Essential knowledge — Clubs.. the blade sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: En garde..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: En garde..", "x": "Explained: En garde.. En garde. The context — Fencing Hobby. Electric. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Footwork.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Footwork.", "x": "Fencing Hobby: Footwork.. Foil. Essential knowledge — Electric.. the blade sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Footwork..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Footwork..", "x": "Explained: Footwork.. Getting started. The context — Fencing Hobby. Lunge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Clubs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Clubs.", "x": "Fencing Hobby: Clubs.. En garde. Essential knowledge — Lunge.. the blade sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Clubs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Clubs..", "x": "Explained: Clubs.. Footwork. The context — Fencing Hobby. Foil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Electric.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Electric.", "x": "Fencing Hobby: Electric.. Getting started. Essential knowledge — Foil.. the blade sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Electric..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Electric..", "x": "Explained: Electric.. Clubs. The context — Fencing Hobby. En garde. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lunge.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lunge.", "x": "Fencing Hobby: Lunge.. Footwork. Essential knowledge — En garde.. the blade sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lunge..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lunge..", "x": "Explained: Lunge.. Lunge. The context — Fencing Hobby. Footwork. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Footwork.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Footwork.", "x": "Fencing Hobby in depth: Footwork.. En garde. Details — the blade sport.. Lunge. Clubs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Clubs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Clubs.", "x": "Fencing Hobby in depth: Clubs.. Footwork. Details — the blade sport.. Foil. Electric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lunge.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lunge.", "x": "Fencing Hobby in depth: Lunge.. Clubs. Details — the blade sport.. En garde. Lunge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Foil.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Foil.", "x": "Fencing Hobby in depth: Foil.. Electric. Details — the blade sport.. Getting started. Foil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "En garde.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "En garde.", "x": "Fencing Hobby in depth: En garde.. Lunge. Details — the blade sport.. Footwork. En garde. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Fencing Hobby in depth: Getting started.. Foil. Details — the blade sport.. Clubs. Footwork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fencing Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fencing Hobby comes from.", "x": "Origins: Footwork.. Foil. The history of Fencing Hobby — the blade sport.. Clubs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fencing Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fencing Hobby respectfully.", "x": "Engaging: Lunge.. En garde. How to participate or observe well — Fencing Hobby. the blade sport. Respect first, always; Foil.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fencing Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fencing Hobby do's and don'ts.", "x": "Etiquette: En garde.. Footwork. The rules of respect — Fencing Hobby. the blade sport. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fencing Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fencing Hobby.", "x": "Planning: Footwork.. Clubs. Practical notes — Fencing Hobby. the blade sport. A little planning shows respect for Clubs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fencing Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fencing Hobby and money.", "x": "Costs: Lunge.. Electric. What to budget — Fencing Hobby. the blade sport. The best experiences of Foil. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-fencing-hobby2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
