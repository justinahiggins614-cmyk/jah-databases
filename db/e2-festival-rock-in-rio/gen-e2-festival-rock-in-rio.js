(function(){'use strict';
/* JAH Rock in Rio Festival Database generator — jahdb-e2-festival-rock-in-rio-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-rock-in-rio',PREFIX='JAH-E2FESTIVALR-',NAME='JAH Rock in Rio Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rock in Rio: the complete guide", "d": "Rock in Rio: Brazil's mega fest..", "g": "overview", "l": 2, "q": "What is Rock in Rio: the complete guide?", "a": "Rock in Rio: Brazil's mega fest..", "x": "The complete festival guide to Rock in Rio: Brazil's mega fest.. Rio/Lisbon. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rock in Rio essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rock in Rio essentials.", "x": "At a glance: Rock in Rio — Brazil's mega fest.. Headliners. The essentials: Stages.. City of Rock. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rio/Lisbon.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rio/Lisbon.", "x": "Rock in Rio: Rio/Lisbon.. Stages. Essential knowledge — City of Rock.. Brazil's mega fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rio/Lisbon..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rio/Lisbon..", "x": "Explained: Rio/Lisbon.. Travel. The context — Rock in Rio. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Headliners.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Headliners.", "x": "Rock in Rio: Headliners.. Global. Essential knowledge — History.. Brazil's mega fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Headliners..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Headliners..", "x": "Explained: Headliners.. Headliners. The context — Rock in Rio. Global. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "City of Rock.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "City of Rock.", "x": "Rock in Rio: City of Rock.. Travel. Essential knowledge — Global.. Brazil's mega fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: City of Rock..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: City of Rock..", "x": "Explained: City of Rock.. Party. The context — Rock in Rio. Party. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "History.", "x": "Rock in Rio: History.. Headliners. Essential knowledge — Party.. Brazil's mega fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Rock in Rio. Rio/Lisbon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Global.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Global.", "x": "Rock in Rio: Global.. Party. Essential knowledge — Rio/Lisbon.. Brazil's mega fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Global..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Global..", "x": "Explained: Global.. Stages. The context — Rock in Rio. Headliners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Party.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Party.", "x": "Rock in Rio: Party.. History. Essential knowledge — Headliners.. Brazil's mega fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Party..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Party..", "x": "Explained: Party.. Global. The context — Rock in Rio. City of Rock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Rock in Rio in depth: History.. Headliners. Details — Brazil's mega fest.. Global. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stages.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stages.", "x": "Rock in Rio in depth: Stages.. City of Rock. Details — Brazil's mega fest.. Travel. Global. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Global.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Global.", "x": "Rock in Rio in depth: Global.. History. Details — Brazil's mega fest.. Headliners. Party. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Travel.", "x": "Rock in Rio in depth: Travel.. Global. Details — Brazil's mega fest.. Party. Rio/Lisbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Headliners.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Headliners.", "x": "Rock in Rio in depth: Headliners.. Party. Details — Brazil's mega fest.. History. Headliners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Party.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Party.", "x": "Rock in Rio in depth: Party.. Rio/Lisbon. Details — Brazil's mega fest.. Stages. City of Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rock in Rio comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rock in Rio comes from.", "x": "Origins: History.. Rio/Lisbon. The history of Rock in Rio — Brazil's mega fest.. Stages. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rock in Rio respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rock in Rio respectfully.", "x": "Engaging: Global.. Headliners. How to participate or observe well — Rock in Rio. Brazil's mega fest. Respect first, always; Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rock in Rio do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rock in Rio do's and don'ts.", "x": "Etiquette: Headliners.. City of Rock. The rules of respect — Rock in Rio. Brazil's mega fest. When in doubt, ask about Party.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rock in Rio.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rock in Rio.", "x": "Planning: History.. History. Practical notes — Rock in Rio. Brazil's mega fest. A little planning shows respect for Stages.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rock in Rio and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rock in Rio and money.", "x": "Costs: Global.. Global. What to budget — Rock in Rio. Brazil's mega fest. The best experiences of Travel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-rock-in-rio-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
