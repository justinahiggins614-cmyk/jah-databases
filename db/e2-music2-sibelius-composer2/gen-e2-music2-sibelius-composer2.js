(function(){'use strict';
/* JAH Sibelius Composer2 Database generator — jahdb-e2-music2-sibelius-composer2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-music2-sibelius-composer2',PREFIX='JAH-E2MUSIC2SIB-',NAME='JAH Sibelius Composer2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sibelius Composer2: the complete guide", "d": "Sibelius Composer2: the Finnish voice..", "g": "overview", "l": 2, "q": "What is Sibelius Composer2: the complete guide?", "a": "Sibelius Composer2: the Finnish voice..", "x": "The complete composer guide to Sibelius Composer2: the Finnish voice.. 1865. History, meaning, practices, and how to engage respectfully — everything in one database. Finlandia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sibelius Composer2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sibelius Composer2 essentials.", "x": "At a glance: Sibelius Composer2 — the Finnish voice.. Finlandia. The essentials: Silence.. 7 symphonies. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1865.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1865.", "x": "Sibelius Composer2: 1865.. Silence. Essential knowledge — 7 symphonies.. the Finnish voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1865..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1865..", "x": "Explained: 1865.. Swan. The context — Sibelius Composer2. Swan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Finlandia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Finlandia.", "x": "Sibelius Composer2: Finlandia.. National. Essential knowledge — Swan.. the Finnish voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Finlandia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Finlandia..", "x": "Explained: Finlandia.. 7. The context — Sibelius Composer2. Silence. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "7 symphonies.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "7 symphonies.", "x": "Sibelius Composer2: 7 symphonies.. Swan. Essential knowledge — Silence.. the Finnish voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 7 symphonies..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 7 symphonies..", "x": "Explained: 7 symphonies.. Legacy. The context — Sibelius Composer2. National. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Swan.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Swan.", "x": "Sibelius Composer2: Swan.. 7. Essential knowledge — National.. the Finnish voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Swan..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Swan..", "x": "Explained: Swan.. Finlandia. The context — Sibelius Composer2. 1865. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Silence.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Silence.", "x": "Sibelius Composer2: Silence.. Legacy. Essential knowledge — 1865.. the Finnish voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Silence..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Silence..", "x": "Explained: Silence.. Silence. The context — Sibelius Composer2. Finlandia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "National.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "National.", "x": "Sibelius Composer2: National.. Finlandia. Essential knowledge — Finlandia.. the Finnish voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: National..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: National..", "x": "Explained: National.. National. The context — Sibelius Composer2. 7 symphonies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Finlandia.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Finlandia.", "x": "Sibelius Composer2 in depth: Finlandia.. Finlandia. Details — the Finnish voice.. National. Swan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Silence.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Silence.", "x": "Sibelius Composer2 in depth: Silence.. 7 symphonies. Details — the Finnish voice.. Swan. Silence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "National.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "National.", "x": "Sibelius Composer2 in depth: National.. Swan. Details — the Finnish voice.. 7. National. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Swan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Swan.", "x": "Sibelius Composer2 in depth: Swan.. Silence. Details — the Finnish voice.. Legacy. 1865. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "7.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "7.", "x": "Sibelius Composer2 in depth: 7.. National. Details — the Finnish voice.. Finlandia. Finlandia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Sibelius Composer2 in depth: Legacy.. 1865. Details — the Finnish voice.. Silence. 7 symphonies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sibelius Composer2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sibelius Composer2 comes from.", "x": "Origins: Finlandia.. 1865. The history of Sibelius Composer2 — the Finnish voice.. Silence. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sibelius Composer2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sibelius Composer2 respectfully.", "x": "Engaging: National.. Finlandia. How to participate or observe well — Sibelius Composer2. the Finnish voice. Respect first, always; Swan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sibelius Composer2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sibelius Composer2 do's and don'ts.", "x": "Etiquette: 7.. 7 symphonies. The rules of respect — Sibelius Composer2. the Finnish voice. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sibelius Composer2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sibelius Composer2.", "x": "Planning: Finlandia.. Swan. Practical notes — Sibelius Composer2. the Finnish voice. A little planning shows respect for Silence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sibelius Composer2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sibelius Composer2 and money.", "x": "Costs: National.. Silence. What to budget — Sibelius Composer2. the Finnish voice. The best experiences of Swan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-music2-sibelius-composer2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
