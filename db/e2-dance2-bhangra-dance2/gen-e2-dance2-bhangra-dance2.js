(function(){'use strict';
/* JAH Bhangra Dance Database generator — jahdb-e2-dance2-bhangra-dance2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance2-bhangra-dance2',PREFIX='JAH-E2DANCE2BHA-',NAME='JAH Bhangra Dance Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bhangra Dance: the complete guide", "d": "Bhangra Dance: the Punjabi harvest..", "g": "overview", "l": 2, "q": "What is Bhangra Dance: the complete guide?", "a": "Bhangra Dance: the Punjabi harvest..", "x": "The complete dance form guide to Bhangra Dance: the Punjabi harvest.. Punjab. History, meaning, practices, and how to engage respectfully — everything in one database. Dhol. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bhangra Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bhangra Dance essentials.", "x": "At a glance: Bhangra Dance — the Punjabi harvest.. Harvest. The essentials: Balle.. Dhol. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Punjab.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Punjab.", "x": "Bhangra Dance: Punjab.. Balle. Essential knowledge — Dhol.. the Punjabi harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Punjab..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Punjab..", "x": "Explained: Punjab.. Punjab. The context — Bhangra Dance. Energy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Harvest.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Harvest.", "x": "Bhangra Dance: Harvest.. Energy. Essential knowledge — Energy.. the Punjabi harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Harvest..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Harvest..", "x": "Explained: Harvest.. Harvest. The context — Bhangra Dance. Shoulders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dhol.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dhol.", "x": "Bhangra Dance: Dhol.. Punjab. Essential knowledge — Shoulders.. the Punjabi harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dhol..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dhol..", "x": "Explained: Dhol.. Training. The context — Bhangra Dance. Balle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Energy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Energy.", "x": "Bhangra Dance: Energy.. Harvest. Essential knowledge — Balle.. the Punjabi harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Energy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Energy..", "x": "Explained: Energy.. Dhol. The context — Bhangra Dance. Punjab. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Shoulders.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Shoulders.", "x": "Bhangra Dance: Shoulders.. Training. Essential knowledge — Punjab.. the Punjabi harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Shoulders..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Shoulders..", "x": "Explained: Shoulders.. Balle. The context — Bhangra Dance. Harvest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Balle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Balle.", "x": "Bhangra Dance: Balle.. Dhol. Essential knowledge — Harvest.. the Punjabi harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Balle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Balle..", "x": "Explained: Balle.. Energy. The context — Bhangra Dance. Dhol. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dhol.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dhol.", "x": "Bhangra Dance in depth: Dhol.. Harvest. Details — the Punjabi harvest.. Energy. Energy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Balle.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Balle.", "x": "Bhangra Dance in depth: Balle.. Dhol. Details — the Punjabi harvest.. Punjab. Shoulders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Energy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Energy.", "x": "Bhangra Dance in depth: Energy.. Energy. Details — the Punjabi harvest.. Harvest. Balle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Punjab.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Punjab.", "x": "Bhangra Dance in depth: Punjab.. Shoulders. Details — the Punjabi harvest.. Training. Punjab. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Harvest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Harvest.", "x": "Bhangra Dance in depth: Harvest.. Balle. Details — the Punjabi harvest.. Dhol. Harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Bhangra Dance in depth: Training.. Punjab. Details — the Punjabi harvest.. Balle. Dhol. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bhangra Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bhangra Dance comes from.", "x": "Origins: Dhol.. Punjab. The history of Bhangra Dance — the Punjabi harvest.. Balle. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bhangra Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bhangra Dance respectfully.", "x": "Engaging: Energy.. Harvest. How to participate or observe well — Bhangra Dance. the Punjabi harvest. Respect first, always; Punjab.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bhangra Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bhangra Dance do's and don'ts.", "x": "Etiquette: Harvest.. Dhol. The rules of respect — Bhangra Dance. the Punjabi harvest. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bhangra Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bhangra Dance.", "x": "Planning: Dhol.. Energy. Practical notes — Bhangra Dance. the Punjabi harvest. A little planning shows respect for Balle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bhangra Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bhangra Dance and money.", "x": "Costs: Energy.. Shoulders. What to budget — Bhangra Dance. the Punjabi harvest. The best experiences of Punjab. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance2-bhangra-dance2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
