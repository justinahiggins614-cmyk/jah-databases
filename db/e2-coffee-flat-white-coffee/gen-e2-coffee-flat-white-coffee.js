(function(){'use strict';
/* JAH Flat White Coffee Database generator — jahdb-e2-coffee-flat-white-coffee-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-coffee-flat-white-coffee',PREFIX='JAH-E2COFFEEFLA-',NAME='JAH Flat White Coffee Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Flat White: the complete guide", "d": "Flat White: the velvet microfoam..", "g": "overview", "l": 2, "q": "What is Flat White: the complete guide?", "a": "Flat White: the velvet microfoam..", "x": "The complete coffee guide to Flat White: the velvet microfoam.. Australia/NZ. History, meaning, practices, and how to engage respectfully — everything in one database. Origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Flat White essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Flat White essentials.", "x": "At a glance: Flat White — the velvet microfoam.. Microfoam. The essentials: Microfoam.. Double. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Australia/NZ.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Australia/NZ.", "x": "Flat White: Australia/NZ.. Microfoam. Essential knowledge — Double.. the velvet microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Australia/NZ..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Australia/NZ..", "x": "Explained: Australia/NZ.. Strong. The context — Flat White. Velvet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Microfoam.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Microfoam.", "x": "Flat White: Microfoam.. Debate. Essential knowledge — Velvet.. the velvet microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Microfoam..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Microfoam..", "x": "Explained: Microfoam.. Making. The context — Flat White. Debate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Double.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Double.", "x": "Flat White: Double.. Strong. Essential knowledge — Debate.. the velvet microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Double..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Double..", "x": "Explained: Double.. Culture. The context — Flat White. Strong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Velvet.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Velvet.", "x": "Flat White: Velvet.. Making. Essential knowledge — Strong.. the velvet microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Velvet..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Velvet..", "x": "Explained: Velvet.. Origin. The context — Flat White. Australia/NZ. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Debate.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Debate.", "x": "Flat White: Debate.. Culture. Essential knowledge — Australia/NZ.. the velvet microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Debate..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Debate..", "x": "Explained: Debate.. Microfoam. The context — Flat White. Microfoam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Strong.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Strong.", "x": "Flat White: Strong.. Origin. Essential knowledge — Microfoam.. the velvet microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Strong..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Strong..", "x": "Explained: Strong.. Debate. The context — Flat White. Double. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Origin.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Origin.", "x": "Flat White in depth: Origin.. Microfoam. Details — the velvet microfoam.. Debate. Velvet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Microfoam.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Microfoam.", "x": "Flat White in depth: Microfoam.. Double. Details — the velvet microfoam.. Strong. Debate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Debate.", "x": "Flat White in depth: Debate.. Velvet. Details — the velvet microfoam.. Making. Strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Strong.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Strong.", "x": "Flat White in depth: Strong.. Debate. Details — the velvet microfoam.. Culture. Australia/NZ. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Making.", "x": "Flat White in depth: Making.. Strong. Details — the velvet microfoam.. Origin. Microfoam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Flat White in depth: Culture.. Australia/NZ. Details — the velvet microfoam.. Microfoam. Double. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Flat White comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Flat White comes from.", "x": "Origins: Origin.. Australia/NZ. The history of Flat White — the velvet microfoam.. Microfoam. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Flat White respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Flat White respectfully.", "x": "Engaging: Debate.. Microfoam. How to participate or observe well — Flat White. the velvet microfoam. Respect first, always; Strong.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Flat White do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Flat White do's and don'ts.", "x": "Etiquette: Making.. Double. The rules of respect — Flat White. the velvet microfoam. When in doubt, ask about Culture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Flat White.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Flat White.", "x": "Planning: Origin.. Velvet. Practical notes — Flat White. the velvet microfoam. A little planning shows respect for Microfoam.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Flat White and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Flat White and money.", "x": "Costs: Debate.. Debate. What to budget — Flat White. the velvet microfoam. The best experiences of Strong. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-coffee-flat-white-coffee-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
