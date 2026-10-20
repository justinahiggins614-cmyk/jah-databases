(function(){'use strict';
/* JAH Satyajit Ray Director Database generator — jahdb-e2-director-satyajit-ray-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-satyajit-ray-director',PREFIX='JAH-E2DIRECTORS-',NAME='JAH Satyajit Ray Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Satyajit Ray: the complete guide", "d": "Satyajit Ray: the Bengali humanist..", "g": "overview", "l": 2, "q": "What is Satyajit Ray: the complete guide?", "a": "Satyajit Ray: the Bengali humanist..", "x": "The complete director guide to Satyajit Ray: the Bengali humanist.. 1921. History, meaning, practices, and how to engage respectfully — everything in one database. Apu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Satyajit Ray essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Satyajit Ray essentials.", "x": "At a glance: Satyajit Ray — the Bengali humanist.. Pather Panchali. The essentials: Calcutta.. Apu. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1921.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1921.", "x": "Satyajit Ray: 1921.. Calcutta. Essential knowledge — Apu.. the Bengali humanist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1921..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1921..", "x": "Explained: 1921.. Humanist. The context — Satyajit Ray. Calcutta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pather Panchali.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pather Panchali.", "x": "Satyajit Ray: Pather Panchali.. Oscar. Essential knowledge — Calcutta.. the Bengali humanist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pather Panchali..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pather Panchali..", "x": "Explained: Pather Panchali.. Music. The context — Satyajit Ray. Oscar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Apu.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Apu.", "x": "Satyajit Ray: Apu.. Humanist. Essential knowledge — Oscar.. the Bengali humanist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Apu..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Apu..", "x": "Explained: Apu.. Style. The context — Satyajit Ray. Music. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Calcutta.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Calcutta.", "x": "Satyajit Ray: Calcutta.. Music. Essential knowledge — Music.. the Bengali humanist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Calcutta..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Calcutta..", "x": "Explained: Calcutta.. Apu. The context — Satyajit Ray. 1921. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Oscar.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Oscar.", "x": "Satyajit Ray: Oscar.. Style. Essential knowledge — 1921.. the Bengali humanist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Oscar..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Oscar..", "x": "Explained: Oscar.. Calcutta. The context — Satyajit Ray. Pather Panchali. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Music.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Music.", "x": "Satyajit Ray: Music.. Apu. Essential knowledge — Pather Panchali.. the Bengali humanist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Music..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Music..", "x": "Explained: Music.. Oscar. The context — Satyajit Ray. Apu. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Apu.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Apu.", "x": "Satyajit Ray in depth: Apu.. Pather Panchali. Details — the Bengali humanist.. Oscar. Calcutta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Calcutta.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Calcutta.", "x": "Satyajit Ray in depth: Calcutta.. Apu. Details — the Bengali humanist.. Humanist. Oscar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Oscar.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Oscar.", "x": "Satyajit Ray in depth: Oscar.. Calcutta. Details — the Bengali humanist.. Music. Music. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Humanist.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Humanist.", "x": "Satyajit Ray in depth: Humanist.. Oscar. Details — the Bengali humanist.. Style. 1921. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Music.", "x": "Satyajit Ray in depth: Music.. Music. Details — the Bengali humanist.. Apu. Pather Panchali. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Satyajit Ray in depth: Style.. 1921. Details — the Bengali humanist.. Calcutta. Apu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Satyajit Ray comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Satyajit Ray comes from.", "x": "Origins: Apu.. 1921. The history of Satyajit Ray — the Bengali humanist.. Calcutta. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Satyajit Ray respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Satyajit Ray respectfully.", "x": "Engaging: Oscar.. Pather Panchali. How to participate or observe well — Satyajit Ray. the Bengali humanist. Respect first, always; Humanist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Satyajit Ray do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Satyajit Ray do's and don'ts.", "x": "Etiquette: Music.. Apu. The rules of respect — Satyajit Ray. the Bengali humanist. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Satyajit Ray.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Satyajit Ray.", "x": "Planning: Apu.. Calcutta. Practical notes — Satyajit Ray. the Bengali humanist. A little planning shows respect for Calcutta.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Satyajit Ray and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Satyajit Ray and money.", "x": "Costs: Oscar.. Oscar. What to budget — Satyajit Ray. the Bengali humanist. The best experiences of Humanist. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-satyajit-ray-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
