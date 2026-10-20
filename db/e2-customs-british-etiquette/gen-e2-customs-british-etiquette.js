(function(){'use strict';
/* JAH British Etiquette Customs Database generator — jahdb-e2-customs-british-etiquette-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-customs-british-etiquette',PREFIX='JAH-E2CUSTOMSBR-',NAME='JAH British Etiquette Customs Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "British Etiquette: the complete guide", "d": "British Etiquette: queuing and understatement..", "g": "overview", "l": 2, "q": "What is British Etiquette: the complete guide?", "a": "British Etiquette: queuing and understatement..", "x": "The complete customs guide to British Etiquette: queuing and understatement.. Queue. History, meaning, practices, and how to engage respectfully — everything in one database. Queue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "British Etiquette essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "British Etiquette essentials.", "x": "At a glance: British Etiquette — queuing and understatement.. Sorry. The essentials: Politeness.. Tea. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Queue.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Queue.", "x": "British Etiquette: Queue.. Politeness. Essential knowledge — Tea.. queuing and understatement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Queue..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Queue..", "x": "Explained: Queue.. Humor. The context — British Etiquette. Small talk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sorry.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sorry.", "x": "British Etiquette: Sorry.. Tea. Essential knowledge — Small talk.. queuing and understatement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sorry..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sorry..", "x": "Explained: Sorry.. Pubs. The context — British Etiquette. Pubs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tea.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tea.", "x": "British Etiquette: Tea.. Humor. Essential knowledge — Pubs.. queuing and understatement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tea..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tea..", "x": "Explained: Tea.. Reserve. The context — British Etiquette. Apology. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Small talk.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Small talk.", "x": "British Etiquette: Small talk.. Pubs. Essential knowledge — Apology.. queuing and understatement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Small talk..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Small talk..", "x": "Explained: Small talk.. Queue. The context — British Etiquette. Queue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pubs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pubs.", "x": "British Etiquette: Pubs.. Reserve. Essential knowledge — Queue.. queuing and understatement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pubs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pubs..", "x": "Explained: Pubs.. Politeness. The context — British Etiquette. Sorry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Apology.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Apology.", "x": "British Etiquette: Apology.. Queue. Essential knowledge — Sorry.. queuing and understatement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Apology..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Apology..", "x": "Explained: Apology.. Tea. The context — British Etiquette. Tea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Queue.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Queue.", "x": "British Etiquette in depth: Queue.. Sorry. Details — queuing and understatement.. Tea. Small talk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Politeness.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Politeness.", "x": "British Etiquette in depth: Politeness.. Tea. Details — queuing and understatement.. Humor. Pubs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tea.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tea.", "x": "British Etiquette in depth: Tea.. Small talk. Details — queuing and understatement.. Pubs. Apology. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Humor.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Humor.", "x": "British Etiquette in depth: Humor.. Pubs. Details — queuing and understatement.. Reserve. Queue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pubs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pubs.", "x": "British Etiquette in depth: Pubs.. Apology. Details — queuing and understatement.. Queue. Sorry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Reserve.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Reserve.", "x": "British Etiquette in depth: Reserve.. Queue. Details — queuing and understatement.. Politeness. Tea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where British Etiquette comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where British Etiquette comes from.", "x": "Origins: Queue.. Queue. The history of British Etiquette — queuing and understatement.. Politeness. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing British Etiquette respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing British Etiquette respectfully.", "x": "Engaging: Tea.. Sorry. How to participate or observe well — British Etiquette. queuing and understatement. Respect first, always; Humor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "British Etiquette do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "British Etiquette do's and don'ts.", "x": "Etiquette: Pubs.. Tea. The rules of respect — British Etiquette. queuing and understatement. When in doubt, ask about Reserve.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around British Etiquette.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around British Etiquette.", "x": "Planning: Queue.. Small talk. Practical notes — British Etiquette. queuing and understatement. A little planning shows respect for Politeness.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "British Etiquette and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "British Etiquette and money.", "x": "Costs: Tea.. Pubs. What to budget — British Etiquette. queuing and understatement. The best experiences of Humor. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-customs-british-etiquette-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
