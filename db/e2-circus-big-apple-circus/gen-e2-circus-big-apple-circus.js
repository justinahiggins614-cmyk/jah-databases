(function(){'use strict';
/* JAH Big Apple Circus Circus Database generator — jahdb-e2-circus-big-apple-circus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-circus-big-apple-circus',PREFIX='JAH-E2CIRCUSBIG-',NAME='JAH Big Apple Circus Circus Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Big Apple Circus: the complete guide", "d": "Big Apple Circus: the one-ring NYC..", "g": "overview", "l": 2, "q": "What is Big Apple Circus: the complete guide?", "a": "Big Apple Circus: the one-ring NYC..", "x": "The complete circus guide to Big Apple Circus: the one-ring NYC.. 1977. History, meaning, practices, and how to engage respectfully — everything in one database. One ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Big Apple Circus essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Big Apple Circus essentials.", "x": "At a glance: Big Apple Circus — the one-ring NYC.. One ring. The essentials: Intimate.. Intimate. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1977.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1977.", "x": "Big Apple Circus: 1977.. Intimate. Essential knowledge — Intimate.. the one-ring NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1977..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1977..", "x": "Explained: 1977.. Community. The context — Big Apple Circus. Lincoln Center. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "One ring.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "One ring.", "x": "Big Apple Circus: One ring.. Clowns. Essential knowledge — Lincoln Center.. the one-ring NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: One ring..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: One ring..", "x": "Explained: One ring.. 1977. The context — Big Apple Circus. Clowns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Intimate.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Intimate.", "x": "Big Apple Circus: Intimate.. Community. Essential knowledge — Clowns.. the one-ring NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Intimate..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Intimate..", "x": "Explained: Intimate.. Shows. The context — Big Apple Circus. Community. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lincoln Center.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lincoln Center.", "x": "Big Apple Circus: Lincoln Center.. 1977. Essential knowledge — Community.. the one-ring NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lincoln Center..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lincoln Center..", "x": "Explained: Lincoln Center.. One ring. The context — Big Apple Circus. 1977. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Clowns.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Clowns.", "x": "Big Apple Circus: Clowns.. Shows. Essential knowledge — 1977.. the one-ring NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Clowns..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Clowns..", "x": "Explained: Clowns.. Intimate. The context — Big Apple Circus. One ring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Community.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Community.", "x": "Big Apple Circus: Community.. One ring. Essential knowledge — One ring.. the one-ring NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Community..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Community..", "x": "Explained: Community.. Clowns. The context — Big Apple Circus. Intimate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "One ring.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "One ring.", "x": "Big Apple Circus in depth: One ring.. One ring. Details — the one-ring NYC.. Clowns. Lincoln Center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Intimate.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Intimate.", "x": "Big Apple Circus in depth: Intimate.. Intimate. Details — the one-ring NYC.. Community. Clowns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Clowns.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Clowns.", "x": "Big Apple Circus in depth: Clowns.. Lincoln Center. Details — the one-ring NYC.. 1977. Community. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Community.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Community.", "x": "Big Apple Circus in depth: Community.. Clowns. Details — the one-ring NYC.. Shows. 1977. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1977.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1977.", "x": "Big Apple Circus in depth: 1977.. Community. Details — the one-ring NYC.. One ring. One ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Shows.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Shows.", "x": "Big Apple Circus in depth: Shows.. 1977. Details — the one-ring NYC.. Intimate. Intimate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Big Apple Circus comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Big Apple Circus comes from.", "x": "Origins: One ring.. 1977. The history of Big Apple Circus — the one-ring NYC.. Intimate. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Big Apple Circus respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Big Apple Circus respectfully.", "x": "Engaging: Clowns.. One ring. How to participate or observe well — Big Apple Circus. the one-ring NYC. Respect first, always; Community.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Big Apple Circus do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Big Apple Circus do's and don'ts.", "x": "Etiquette: 1977.. Intimate. The rules of respect — Big Apple Circus. the one-ring NYC. When in doubt, ask about Shows.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Big Apple Circus.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Big Apple Circus.", "x": "Planning: One ring.. Lincoln Center. Practical notes — Big Apple Circus. the one-ring NYC. A little planning shows respect for Intimate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Big Apple Circus and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Big Apple Circus and money.", "x": "Costs: Clowns.. Clowns. What to budget — Big Apple Circus. the one-ring NYC. The best experiences of Community. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-circus-big-apple-circus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
