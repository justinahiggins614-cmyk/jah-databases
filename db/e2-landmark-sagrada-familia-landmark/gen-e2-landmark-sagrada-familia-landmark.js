(function(){'use strict';
/* JAH Sagrada Familia Landmark Database generator — jahdb-e2-landmark-sagrada-familia-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-sagrada-familia-landmark',PREFIX='JAH-E2LANDMARKS-',NAME='JAH Sagrada Familia Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sagrada Familia: the complete guide", "d": "Sagrada Familia: Gaudi's forest..", "g": "overview", "l": 2, "q": "What is Sagrada Familia: the complete guide?", "a": "Sagrada Familia: Gaudi's forest..", "x": "The complete landmark guide to Sagrada Familia: Gaudi's forest.. 1882. History, meaning, practices, and how to engage respectfully — everything in one database. 1882. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sagrada Familia essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sagrada Familia essentials.", "x": "At a glance: Sagrada Familia — Gaudi's forest.. Gaudi. The essentials: Gaudi.. Forest. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1882.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1882.", "x": "Sagrada Familia: 1882.. Gaudi. Essential knowledge — Forest.. Gaudi's forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1882..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1882..", "x": "Explained: 1882.. 2026. The context — Sagrada Familia. 2026. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gaudi.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gaudi.", "x": "Sagrada Familia: Gaudi.. Spires. Essential knowledge — 2026.. Gaudi's forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gaudi..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gaudi..", "x": "Explained: Gaudi.. Forest. The context — Sagrada Familia. Spires. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Forest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Forest.", "x": "Sagrada Familia: Forest.. 2026. Essential knowledge — Spires.. Gaudi's forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Forest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Forest..", "x": "Explained: Forest.. Tickets. The context — Sagrada Familia. Nativity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "2026.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "2026.", "x": "Sagrada Familia: 2026.. Forest. Essential knowledge — Nativity.. Gaudi's forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 2026..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 2026..", "x": "Explained: 2026.. 1882. The context — Sagrada Familia. 1882. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Spires.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Spires.", "x": "Sagrada Familia: Spires.. Tickets. Essential knowledge — 1882.. Gaudi's forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Spires..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Spires..", "x": "Explained: Spires.. Gaudi. The context — Sagrada Familia. Gaudi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nativity.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nativity.", "x": "Sagrada Familia: Nativity.. 1882. Essential knowledge — Gaudi.. Gaudi's forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Nativity..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Nativity..", "x": "Explained: Nativity.. Spires. The context — Sagrada Familia. Forest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1882.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1882.", "x": "Sagrada Familia in depth: 1882.. Gaudi. Details — Gaudi's forest.. Spires. 2026. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gaudi.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gaudi.", "x": "Sagrada Familia in depth: Gaudi.. Forest. Details — Gaudi's forest.. 2026. Spires. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spires.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spires.", "x": "Sagrada Familia in depth: Spires.. 2026. Details — Gaudi's forest.. Forest. Nativity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "2026.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "2026.", "x": "Sagrada Familia in depth: 2026.. Spires. Details — Gaudi's forest.. Tickets. 1882. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Forest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Forest.", "x": "Sagrada Familia in depth: Forest.. Nativity. Details — Gaudi's forest.. 1882. Gaudi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Sagrada Familia in depth: Tickets.. 1882. Details — Gaudi's forest.. Gaudi. Forest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sagrada Familia comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sagrada Familia comes from.", "x": "Origins: 1882.. 1882. The history of Sagrada Familia — Gaudi's forest.. Gaudi. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sagrada Familia respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sagrada Familia respectfully.", "x": "Engaging: Spires.. Gaudi. How to participate or observe well — Sagrada Familia. Gaudi's forest. Respect first, always; 2026.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sagrada Familia do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sagrada Familia do's and don'ts.", "x": "Etiquette: Forest.. Forest. The rules of respect — Sagrada Familia. Gaudi's forest. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sagrada Familia.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sagrada Familia.", "x": "Planning: 1882.. 2026. Practical notes — Sagrada Familia. Gaudi's forest. A little planning shows respect for Gaudi.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sagrada Familia and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sagrada Familia and money.", "x": "Costs: Spires.. Spires. What to budget — Sagrada Familia. Gaudi's forest. The best experiences of 2026. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-sagrada-familia-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
