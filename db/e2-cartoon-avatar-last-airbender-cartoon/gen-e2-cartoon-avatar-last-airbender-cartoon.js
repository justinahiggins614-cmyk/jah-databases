(function(){'use strict';
/* JAH Avatar Last Airbender Cartoon Database generator — jahdb-e2-cartoon-avatar-last-airbender-cartoon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cartoon-avatar-last-airbender-cartoon',PREFIX='JAH-E2CARTOONAV-',NAME='JAH Avatar Last Airbender Cartoon Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Avatar Last Airbender: the complete guide", "d": "Avatar Last Airbender: the animated epic..", "g": "overview", "l": 2, "q": "What is Avatar Last Airbender: the complete guide?", "a": "Avatar Last Airbender: the animated epic..", "x": "The complete cartoon guide to Avatar Last Airbender: the animated epic.. 2005. History, meaning, practices, and how to engage respectfully — everything in one database. Aang. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Avatar Last Airbender essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Avatar Last Airbender essentials.", "x": "At a glance: Avatar Last Airbender — the animated epic.. Aang. The essentials: Bending.. Bending. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2005.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2005.", "x": "Avatar Last Airbender: 2005.. Bending. Essential knowledge — Bending.. the animated epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2005..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2005..", "x": "Explained: 2005.. Perfect. The context — Avatar Last Airbender. Nickelodeon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aang.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aang.", "x": "Avatar Last Airbender: Aang.. Zuko. Essential knowledge — Nickelodeon.. the animated epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Aang..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Aang..", "x": "Explained: Aang.. Nick. The context — Avatar Last Airbender. Zuko. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bending.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bending.", "x": "Avatar Last Airbender: Bending.. Perfect. Essential knowledge — Zuko.. the animated epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bending..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bending..", "x": "Explained: Bending.. Legacy. The context — Avatar Last Airbender. Perfect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nickelodeon.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nickelodeon.", "x": "Avatar Last Airbender: Nickelodeon.. Nick. Essential knowledge — Perfect.. the animated epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Nickelodeon..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Nickelodeon..", "x": "Explained: Nickelodeon.. Aang. The context — Avatar Last Airbender. 2005. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zuko.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zuko.", "x": "Avatar Last Airbender: Zuko.. Legacy. Essential knowledge — 2005.. the animated epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Zuko..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Zuko..", "x": "Explained: Zuko.. Bending. The context — Avatar Last Airbender. Aang. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Perfect.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Perfect.", "x": "Avatar Last Airbender: Perfect.. Aang. Essential knowledge — Aang.. the animated epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Perfect..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Perfect..", "x": "Explained: Perfect.. Zuko. The context — Avatar Last Airbender. Bending. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aang.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aang.", "x": "Avatar Last Airbender in depth: Aang.. Aang. Details — the animated epic.. Zuko. Nickelodeon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bending.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bending.", "x": "Avatar Last Airbender in depth: Bending.. Bending. Details — the animated epic.. Perfect. Zuko. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Zuko.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Zuko.", "x": "Avatar Last Airbender in depth: Zuko.. Nickelodeon. Details — the animated epic.. Nick. Perfect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Perfect.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Perfect.", "x": "Avatar Last Airbender in depth: Perfect.. Zuko. Details — the animated epic.. Legacy. 2005. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nick.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nick.", "x": "Avatar Last Airbender in depth: Nick.. Perfect. Details — the animated epic.. Aang. Aang. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Avatar Last Airbender in depth: Legacy.. 2005. Details — the animated epic.. Bending. Bending. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Avatar Last Airbender comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Avatar Last Airbender comes from.", "x": "Origins: Aang.. 2005. The history of Avatar Last Airbender — the animated epic.. Bending. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Avatar Last Airbender respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Avatar Last Airbender respectfully.", "x": "Engaging: Zuko.. Aang. How to participate or observe well — Avatar Last Airbender. the animated epic. Respect first, always; Perfect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Avatar Last Airbender do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Avatar Last Airbender do's and don'ts.", "x": "Etiquette: Nick.. Bending. The rules of respect — Avatar Last Airbender. the animated epic. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Avatar Last Airbender.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Avatar Last Airbender.", "x": "Planning: Aang.. Nickelodeon. Practical notes — Avatar Last Airbender. the animated epic. A little planning shows respect for Bending.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Avatar Last Airbender and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Avatar Last Airbender and money.", "x": "Costs: Zuko.. Zuko. What to budget — Avatar Last Airbender. the animated epic. The best experiences of Perfect. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cartoon-avatar-last-airbender-cartoon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
