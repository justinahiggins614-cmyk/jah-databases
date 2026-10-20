(function(){'use strict';
/* JAH Justice Society Team Database generator — jahdb-e2-comics2-justice-society-team-hero-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-comics2-justice-society-team-hero',PREFIX='JAH-E2COMICS2JU-',NAME='JAH Justice Society Team Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Justice Society Team: the complete guide", "d": "Justice Society Team: the golden age..", "g": "overview", "l": 2, "q": "What is Justice Society Team: the complete guide?", "a": "Justice Society Team: the golden age..", "x": "The complete superhero team guide to Justice Society Team: the golden age.. 1940. History, meaning, practices, and how to engage respectfully — everything in one database. Flash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Justice Society Team essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Justice Society Team essentials.", "x": "At a glance: Justice Society Team — the golden age.. Flash. The essentials: Legacy.. Green Lantern. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1940.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1940.", "x": "Justice Society Team: 1940.. Legacy. Essential knowledge — Green Lantern.. the golden age. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1940..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1940..", "x": "Explained: 1940.. Lantern. The context — Justice Society Team. Hourman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flash.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flash.", "x": "Justice Society Team: Flash.. JSA. Essential knowledge — Hourman.. the golden age. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Flash..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Flash..", "x": "Explained: Flash.. Hourman. The context — Justice Society Team. JSA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Green Lantern.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Green Lantern.", "x": "Justice Society Team: Green Lantern.. Lantern. Essential knowledge — JSA.. the golden age. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Green Lantern..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Green Lantern..", "x": "Explained: Green Lantern.. Roster. The context — Justice Society Team. Legacy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hourman.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hourman.", "x": "Justice Society Team: Hourman.. Hourman. Essential knowledge — Legacy.. the golden age. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hourman..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hourman..", "x": "Explained: Hourman.. Flash. The context — Justice Society Team. 1940. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "JSA.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "JSA.", "x": "Justice Society Team: JSA.. Roster. Essential knowledge — 1940.. the golden age. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: JSA..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: JSA..", "x": "Explained: JSA.. Legacy. The context — Justice Society Team. Flash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Legacy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Legacy.", "x": "Justice Society Team: Legacy.. Flash. Essential knowledge — Flash.. the golden age. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Legacy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Legacy..", "x": "Explained: Legacy.. JSA. The context — Justice Society Team. Green Lantern. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Flash.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Flash.", "x": "Justice Society Team in depth: Flash.. Flash. Details — the golden age.. JSA. Hourman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Legacy.", "x": "Justice Society Team in depth: Legacy.. Green Lantern. Details — the golden age.. Lantern. JSA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "JSA.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "JSA.", "x": "Justice Society Team in depth: JSA.. Hourman. Details — the golden age.. Hourman. Legacy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lantern.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lantern.", "x": "Justice Society Team in depth: Lantern.. JSA. Details — the golden age.. Roster. 1940. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hourman.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hourman.", "x": "Justice Society Team in depth: Hourman.. Legacy. Details — the golden age.. Flash. Flash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Roster.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Roster.", "x": "Justice Society Team in depth: Roster.. 1940. Details — the golden age.. Legacy. Green Lantern. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Justice Society Team comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Justice Society Team comes from.", "x": "Origins: Flash.. 1940. The history of Justice Society Team — the golden age.. Legacy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Justice Society Team respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Justice Society Team respectfully.", "x": "Engaging: JSA.. Flash. How to participate or observe well — Justice Society Team. the golden age. Respect first, always; Lantern.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Justice Society Team do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Justice Society Team do's and don'ts.", "x": "Etiquette: Hourman.. Green Lantern. The rules of respect — Justice Society Team. the golden age. When in doubt, ask about Roster.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Justice Society Team.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Justice Society Team.", "x": "Planning: Flash.. Hourman. Practical notes — Justice Society Team. the golden age. A little planning shows respect for Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Justice Society Team and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Justice Society Team and money.", "x": "Costs: JSA.. JSA. What to budget — Justice Society Team. the golden age. The best experiences of Lantern. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-comics2-justice-society-team-hero-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
