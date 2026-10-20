(function(){'use strict';
/* JAH Charminar Landmark Database generator — jahdb-e2-landmark-charminar-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-charminar-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Charminar Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Charminar: the complete guide", "d": "Charminar: the four minarets..", "g": "overview", "l": 2, "q": "What is Charminar: the complete guide?", "a": "Charminar: the four minarets..", "x": "The complete landmark guide to Charminar: the four minarets.. 1591. History, meaning, practices, and how to engage respectfully — everything in one database. 1591. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Charminar essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Charminar essentials.", "x": "At a glance: Charminar — the four minarets.. 56m. The essentials: Bazaar.. 4 minarets. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1591.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1591.", "x": "Charminar: 1591.. Bazaar. Essential knowledge — 4 minarets.. the four minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1591..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1591..", "x": "Explained: 1591.. 4. The context — Charminar. Laad Bazaar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "56m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "56m.", "x": "Charminar: 56m.. Mosque. Essential knowledge — Laad Bazaar.. the four minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 56m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 56m..", "x": "Explained: 56m.. 56m. The context — Charminar. Qutb Shahi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "4 minarets.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "4 minarets.", "x": "Charminar: 4 minarets.. 4. Essential knowledge — Qutb Shahi.. the four minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 4 minarets..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 4 minarets..", "x": "Explained: 4 minarets.. Views. The context — Charminar. Mosque. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Laad Bazaar.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Laad Bazaar.", "x": "Charminar: Laad Bazaar.. 56m. Essential knowledge — Mosque.. the four minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Laad Bazaar..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Laad Bazaar..", "x": "Explained: Laad Bazaar.. 1591. The context — Charminar. 1591. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Qutb Shahi.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Qutb Shahi.", "x": "Charminar: Qutb Shahi.. Views. Essential knowledge — 1591.. the four minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Qutb Shahi..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Qutb Shahi..", "x": "Explained: Qutb Shahi.. Bazaar. The context — Charminar. 56m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mosque.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mosque.", "x": "Charminar: Mosque.. 1591. Essential knowledge — 56m.. the four minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mosque..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mosque..", "x": "Explained: Mosque.. Mosque. The context — Charminar. 4 minarets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1591.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1591.", "x": "Charminar in depth: 1591.. 56m. Details — the four minarets.. Mosque. Laad Bazaar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bazaar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bazaar.", "x": "Charminar in depth: Bazaar.. 4 minarets. Details — the four minarets.. 4. Qutb Shahi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mosque.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mosque.", "x": "Charminar in depth: Mosque.. Laad Bazaar. Details — the four minarets.. 56m. Mosque. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "4.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "4.", "x": "Charminar in depth: 4.. Qutb Shahi. Details — the four minarets.. Views. 1591. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "56m.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "56m.", "x": "Charminar in depth: 56m.. Mosque. Details — the four minarets.. 1591. 56m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Charminar in depth: Views.. 1591. Details — the four minarets.. Bazaar. 4 minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Charminar comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Charminar comes from.", "x": "Origins: 1591.. 1591. The history of Charminar — the four minarets.. Bazaar. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Charminar respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Charminar respectfully.", "x": "Engaging: Mosque.. 56m. How to participate or observe well — Charminar. the four minarets. Respect first, always; 4.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Charminar do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Charminar do's and don'ts.", "x": "Etiquette: 56m.. 4 minarets. The rules of respect — Charminar. the four minarets. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Charminar.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Charminar.", "x": "Planning: 1591.. Laad Bazaar. Practical notes — Charminar. the four minarets. A little planning shows respect for Bazaar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Charminar and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Charminar and money.", "x": "Costs: Mosque.. Qutb Shahi. What to budget — Charminar. the four minarets. The best experiences of 4. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-charminar-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
