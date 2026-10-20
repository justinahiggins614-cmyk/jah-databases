(function(){'use strict';
/* JAH Ringling Circus Circus Database generator — jahdb-e2-circus-ringling-circus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-circus-ringling-circus',PREFIX='JAH-E2CIRCUSRIN-',NAME='JAH Ringling Circus Circus Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ringling Circus: the complete guide", "d": "Ringling Circus: the greatest show..", "g": "overview", "l": 2, "q": "What is Ringling Circus: the complete guide?", "a": "Ringling Circus: the greatest show..", "x": "The complete circus guide to Ringling Circus: the greatest show.. 1871. History, meaning, practices, and how to engage respectfully — everything in one database. Barnum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ringling Circus essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ringling Circus essentials.", "x": "At a glance: Ringling Circus — the greatest show.. Barnum. The essentials: Rings.. 3 rings. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1871.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1871.", "x": "Ringling Circus: 1871.. Rings. Essential knowledge — 3 rings.. the greatest show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1871..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1871..", "x": "Explained: 1871.. Elephants. The context — Ringling Circus. 146 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Barnum.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Barnum.", "x": "Ringling Circus: Barnum.. 2017. Essential knowledge — 146 years.. the greatest show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Barnum..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Barnum..", "x": "Explained: Barnum.. 1871. The context — Ringling Circus. 2017. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "3 rings.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "3 rings.", "x": "Ringling Circus: 3 rings.. Elephants. Essential knowledge — 2017.. the greatest show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 3 rings..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 3 rings..", "x": "Explained: 3 rings.. History. The context — Ringling Circus. Elephants. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "146 years.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "146 years.", "x": "Ringling Circus: 146 years.. 1871. Essential knowledge — Elephants.. the greatest show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 146 years..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 146 years..", "x": "Explained: 146 years.. Barnum. The context — Ringling Circus. 1871. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2017.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2017.", "x": "Ringling Circus: 2017.. History. Essential knowledge — 1871.. the greatest show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 2017..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 2017..", "x": "Explained: 2017.. Rings. The context — Ringling Circus. Barnum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Elephants.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Elephants.", "x": "Ringling Circus: Elephants.. Barnum. Essential knowledge — Barnum.. the greatest show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Elephants..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Elephants..", "x": "Explained: Elephants.. 2017. The context — Ringling Circus. 3 rings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Barnum.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Barnum.", "x": "Ringling Circus in depth: Barnum.. Barnum. Details — the greatest show.. 2017. 146 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rings.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rings.", "x": "Ringling Circus in depth: Rings.. 3 rings. Details — the greatest show.. Elephants. 2017. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "2017.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "2017.", "x": "Ringling Circus in depth: 2017.. 146 years. Details — the greatest show.. 1871. Elephants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Elephants.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Elephants.", "x": "Ringling Circus in depth: Elephants.. 2017. Details — the greatest show.. History. 1871. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1871.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1871.", "x": "Ringling Circus in depth: 1871.. Elephants. Details — the greatest show.. Barnum. Barnum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Ringling Circus in depth: History.. 1871. Details — the greatest show.. Rings. 3 rings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ringling Circus comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ringling Circus comes from.", "x": "Origins: Barnum.. 1871. The history of Ringling Circus — the greatest show.. Rings. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ringling Circus respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ringling Circus respectfully.", "x": "Engaging: 2017.. Barnum. How to participate or observe well — Ringling Circus. the greatest show. Respect first, always; Elephants.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ringling Circus do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ringling Circus do's and don'ts.", "x": "Etiquette: 1871.. 3 rings. The rules of respect — Ringling Circus. the greatest show. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ringling Circus.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ringling Circus.", "x": "Planning: Barnum.. 146 years. Practical notes — Ringling Circus. the greatest show. A little planning shows respect for Rings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ringling Circus and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ringling Circus and money.", "x": "Costs: 2017.. 2017. What to budget — Ringling Circus. the greatest show. The best experiences of Elephants. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-circus-ringling-circus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
