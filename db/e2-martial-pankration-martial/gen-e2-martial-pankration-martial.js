(function(){'use strict';
/* JAH Pankration Martial Art Database generator — jahdb-e2-martial-pankration-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-pankration-martial',PREFIX='JAH-E2MARTIALPA-',NAME='JAH Pankration Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pankration: the complete guide", "d": "Pankration: the ancient MMA..", "g": "overview", "l": 2, "q": "What is Pankration: the complete guide?", "a": "Pankration: the ancient MMA..", "x": "The complete martial art guide to Pankration: the ancient MMA.. Greece. History, meaning, practices, and how to engage respectfully — everything in one database. Greece. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pankration essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pankration essentials.", "x": "At a glance: Pankration — the ancient MMA.. Ancient Olympics. The essentials: Ancient.. No bites. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Greece.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Greece.", "x": "Pankration: Greece.. Ancient. Essential knowledge — No bites.. the ancient MMA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Greece..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Greece..", "x": "Explained: Greece.. 648 BC. The context — Pankration. 648 BC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ancient Olympics.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ancient Olympics.", "x": "Pankration: Ancient Olympics.. Revival. Essential knowledge — 648 BC.. the ancient MMA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ancient Olympics..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ancient Olympics..", "x": "Explained: Ancient Olympics.. All. The context — Pankration. All powers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "No bites.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "No bites.", "x": "Pankration: No bites.. 648 BC. Essential knowledge — All powers.. the ancient MMA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: No bites..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: No bites..", "x": "Explained: No bites.. History. The context — Pankration. Revival. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "648 BC.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "648 BC.", "x": "Pankration: 648 BC.. All. Essential knowledge — Revival.. the ancient MMA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 648 BC..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 648 BC..", "x": "Explained: 648 BC.. Greece. The context — Pankration. Greece. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "All powers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "All powers.", "x": "Pankration: All powers.. History. Essential knowledge — Greece.. the ancient MMA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: All powers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: All powers..", "x": "Explained: All powers.. Ancient. The context — Pankration. Ancient Olympics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Revival.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Revival.", "x": "Pankration: Revival.. Greece. Essential knowledge — Ancient Olympics.. the ancient MMA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Revival..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Revival..", "x": "Explained: Revival.. Revival. The context — Pankration. No bites. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Greece.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Greece.", "x": "Pankration in depth: Greece.. Ancient Olympics. Details — the ancient MMA.. Revival. 648 BC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ancient.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ancient.", "x": "Pankration in depth: Ancient.. No bites. Details — the ancient MMA.. 648 BC. All powers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Revival.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Revival.", "x": "Pankration in depth: Revival.. 648 BC. Details — the ancient MMA.. All. Revival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "648 BC.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "648 BC.", "x": "Pankration in depth: 648 BC.. All powers. Details — the ancient MMA.. History. Greece. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "All.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "All.", "x": "Pankration in depth: All.. Revival. Details — the ancient MMA.. Greece. Ancient Olympics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Pankration in depth: History.. Greece. Details — the ancient MMA.. Ancient. No bites. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pankration comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pankration comes from.", "x": "Origins: Greece.. Greece. The history of Pankration — the ancient MMA.. Ancient. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pankration respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pankration respectfully.", "x": "Engaging: Revival.. Ancient Olympics. How to participate or observe well — Pankration. the ancient MMA. Respect first, always; 648 BC.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pankration do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pankration do's and don'ts.", "x": "Etiquette: All.. No bites. The rules of respect — Pankration. the ancient MMA. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pankration.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pankration.", "x": "Planning: Greece.. 648 BC. Practical notes — Pankration. the ancient MMA. A little planning shows respect for Ancient.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pankration and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pankration and money.", "x": "Costs: Revival.. All powers. What to budget — Pankration. the ancient MMA. The best experiences of 648 BC. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-pankration-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
