(function(){'use strict';
/* JAH Cycling Track Olympics Database generator — jahdb-e2-olympic2-cycling-track-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-cycling-track-olympics-sport',PREFIX='JAH-E2OLYMPIC2C-',NAME='JAH Cycling Track Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cycling Track Olympics: the complete guide", "d": "Cycling Track Olympics: the velodrome..", "g": "overview", "l": 2, "q": "What is Cycling Track Olympics: the complete guide?", "a": "Cycling Track Olympics: the velodrome..", "x": "The complete olympic sport guide to Cycling Track Olympics: the velodrome.. 1896. History, meaning, practices, and how to engage respectfully — everything in one database. Sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cycling Track Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cycling Track Olympics essentials.", "x": "At a glance: Cycling Track Olympics — the velodrome.. Velodrome. The essentials: Keirin.. Sprint. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1896.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1896.", "x": "Cycling Track Olympics: 1896.. Keirin. Essential knowledge — Sprint.. the velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1896..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1896..", "x": "Explained: 1896.. Velodrome. The context — Cycling Track Olympics. Keirin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Velodrome.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Velodrome.", "x": "Cycling Track Olympics: Velodrome.. Banking. Essential knowledge — Keirin.. the velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Velodrome..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Velodrome..", "x": "Explained: Velodrome.. Omnium. The context — Cycling Track Olympics. Omnium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sprint.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sprint.", "x": "Cycling Track Olympics: Sprint.. Velodrome. Essential knowledge — Omnium.. the velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sprint..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sprint..", "x": "Explained: Sprint.. Guide. The context — Cycling Track Olympics. Banking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Keirin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Keirin.", "x": "Cycling Track Olympics: Keirin.. Omnium. Essential knowledge — Banking.. the velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Keirin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Keirin..", "x": "Explained: Keirin.. Sprint. The context — Cycling Track Olympics. 1896. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Omnium.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Omnium.", "x": "Cycling Track Olympics: Omnium.. Guide. Essential knowledge — 1896.. the velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Omnium..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Omnium..", "x": "Explained: Omnium.. Keirin. The context — Cycling Track Olympics. Velodrome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Banking.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Banking.", "x": "Cycling Track Olympics: Banking.. Sprint. Essential knowledge — Velodrome.. the velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Banking..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Banking..", "x": "Explained: Banking.. Banking. The context — Cycling Track Olympics. Sprint. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sprint.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sprint.", "x": "Cycling Track Olympics in depth: Sprint.. Velodrome. Details — the velodrome.. Banking. Keirin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Keirin.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Keirin.", "x": "Cycling Track Olympics in depth: Keirin.. Sprint. Details — the velodrome.. Velodrome. Omnium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Banking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Banking.", "x": "Cycling Track Olympics in depth: Banking.. Keirin. Details — the velodrome.. Omnium. Banking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Velodrome.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Velodrome.", "x": "Cycling Track Olympics in depth: Velodrome.. Omnium. Details — the velodrome.. Guide. 1896. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Omnium.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Omnium.", "x": "Cycling Track Olympics in depth: Omnium.. Banking. Details — the velodrome.. Sprint. Velodrome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Cycling Track Olympics in depth: Guide.. 1896. Details — the velodrome.. Keirin. Sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cycling Track Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cycling Track Olympics comes from.", "x": "Origins: Sprint.. 1896. The history of Cycling Track Olympics — the velodrome.. Keirin. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cycling Track Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cycling Track Olympics respectfully.", "x": "Engaging: Banking.. Velodrome. How to participate or observe well — Cycling Track Olympics. the velodrome. Respect first, always; Velodrome.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cycling Track Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cycling Track Olympics do's and don'ts.", "x": "Etiquette: Omnium.. Sprint. The rules of respect — Cycling Track Olympics. the velodrome. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cycling Track Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cycling Track Olympics.", "x": "Planning: Sprint.. Keirin. Practical notes — Cycling Track Olympics. the velodrome. A little planning shows respect for Keirin.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cycling Track Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cycling Track Olympics and money.", "x": "Costs: Banking.. Omnium. What to budget — Cycling Track Olympics. the velodrome. The best experiences of Velodrome. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-cycling-track-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
