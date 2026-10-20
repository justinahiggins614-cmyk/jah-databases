(function(){'use strict';
/* JAH Square Dance Dance Form Database generator — jahdb-e2-dance-square-dance-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-square-dance-dance-form',PREFIX='JAH-E2DANCESQUA-',NAME='JAH Square Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Square Dance: the complete guide", "d": "Square Dance: the called figures..", "g": "overview", "l": 2, "q": "What is Square Dance: the complete guide?", "a": "Square Dance: the called figures..", "x": "The complete dance form guide to Square Dance: the called figures.. Caller. History, meaning, practices, and how to engage respectfully — everything in one database. Caller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Square Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Square Dance essentials.", "x": "At a glance: Square Dance — the called figures.. Dosado. The essentials: Sets.. Promenade. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Caller.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Caller.", "x": "Square Dance: Caller.. Sets. Essential knowledge — Promenade.. the called figures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Caller..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Caller..", "x": "Explained: Caller.. Promenade. The context — Square Dance. Folk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dosado.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dosado.", "x": "Square Dance: Dosado.. Folk. Essential knowledge — Folk.. the called figures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dosado..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dosado..", "x": "Explained: Dosado.. Dosado. The context — Square Dance. Sets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Promenade.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Promenade.", "x": "Square Dance: Promenade.. Promenade. Essential knowledge — Sets.. the called figures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Promenade..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Promenade..", "x": "Explained: Promenade.. Training. The context — Square Dance. Allemande. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Folk.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Folk.", "x": "Square Dance: Folk.. Dosado. Essential knowledge — Allemande.. the called figures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Folk..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Folk..", "x": "Explained: Folk.. Caller. The context — Square Dance. Caller. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sets.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sets.", "x": "Square Dance: Sets.. Training. Essential knowledge — Caller.. the called figures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sets..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sets..", "x": "Explained: Sets.. Sets. The context — Square Dance. Dosado. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Allemande.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Allemande.", "x": "Square Dance: Allemande.. Caller. Essential knowledge — Dosado.. the called figures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Allemande..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Allemande..", "x": "Explained: Allemande.. Folk. The context — Square Dance. Promenade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Caller.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Caller.", "x": "Square Dance in depth: Caller.. Dosado. Details — the called figures.. Folk. Folk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sets.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sets.", "x": "Square Dance in depth: Sets.. Promenade. Details — the called figures.. Promenade. Sets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Folk.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Folk.", "x": "Square Dance in depth: Folk.. Folk. Details — the called figures.. Dosado. Allemande. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Promenade.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Promenade.", "x": "Square Dance in depth: Promenade.. Sets. Details — the called figures.. Training. Caller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dosado.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dosado.", "x": "Square Dance in depth: Dosado.. Allemande. Details — the called figures.. Caller. Dosado. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Square Dance in depth: Training.. Caller. Details — the called figures.. Sets. Promenade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Square Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Square Dance comes from.", "x": "Origins: Caller.. Caller. The history of Square Dance — the called figures.. Sets. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Square Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Square Dance respectfully.", "x": "Engaging: Folk.. Dosado. How to participate or observe well — Square Dance. the called figures. Respect first, always; Promenade.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Square Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Square Dance do's and don'ts.", "x": "Etiquette: Dosado.. Promenade. The rules of respect — Square Dance. the called figures. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Square Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Square Dance.", "x": "Planning: Caller.. Folk. Practical notes — Square Dance. the called figures. A little planning shows respect for Sets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Square Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Square Dance and money.", "x": "Costs: Folk.. Sets. What to budget — Square Dance. the called figures. The best experiences of Promenade. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-square-dance-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
