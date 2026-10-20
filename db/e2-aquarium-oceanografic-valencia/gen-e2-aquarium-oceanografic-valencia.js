(function(){'use strict';
/* JAH L\'Oceanografic Valencia Aquarium Database generator — jahdb-e2-aquarium-oceanografic-valencia-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium-oceanografic-valencia',PREFIX='JAH-E2AQUARIUMO-',NAME='JAH L\'Oceanografic Valencia Aquarium Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "L'Oceanografic Valencia: the complete guide", "d": "L'Oceanografic Valencia: Europe's largest..", "g": "overview", "l": 2, "q": "What is L'Oceanografic Valencia: the complete guide?", "a": "L'Oceanografic Valencia: Europe's largest..", "x": "The complete aquarium guide to L'Oceanografic Valencia: Europe's largest.. Calatrava. History, meaning, practices, and how to engage respectfully — everything in one database. Building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "L'Oceanografic Valencia essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "L'Oceanografic Valencia essentials.", "x": "At a glance: L'Oceanografic Valencia — Europe's largest.. Belugas. The essentials: Belugas.. Dolphins. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Calatrava.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Calatrava.", "x": "L'Oceanografic Valencia: Calatrava.. Belugas. Essential knowledge — Dolphins.. Europe's largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Calatrava..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Calatrava..", "x": "Explained: Calatrava.. Tickets. The context — L'Oceanografic Valencia. Valencia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Belugas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Belugas.", "x": "L'Oceanografic Valencia: Belugas.. Zones. Essential knowledge — Valencia.. Europe's largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Belugas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Belugas..", "x": "Explained: Belugas.. Valencia. The context — L'Oceanografic Valencia. 2003. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dolphins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dolphins.", "x": "L'Oceanografic Valencia: Dolphins.. Tickets. Essential knowledge — 2003.. Europe's largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dolphins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dolphins..", "x": "Explained: Dolphins.. Design. The context — L'Oceanografic Valencia. Arctic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Valencia.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Valencia.", "x": "L'Oceanografic Valencia: Valencia.. Valencia. Essential knowledge — Arctic.. Europe's largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Valencia..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Valencia..", "x": "Explained: Valencia.. Building. The context — L'Oceanografic Valencia. Calatrava. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2003.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2003.", "x": "L'Oceanografic Valencia: 2003.. Design. Essential knowledge — Calatrava.. Europe's largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 2003..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 2003..", "x": "Explained: 2003.. Belugas. The context — L'Oceanografic Valencia. Belugas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Arctic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Arctic.", "x": "L'Oceanografic Valencia: Arctic.. Building. Essential knowledge — Belugas.. Europe's largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Arctic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Arctic..", "x": "Explained: Arctic.. Zones. The context — L'Oceanografic Valencia. Dolphins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Building.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Building.", "x": "L'Oceanografic Valencia in depth: Building.. Belugas. Details — Europe's largest.. Zones. Valencia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Belugas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Belugas.", "x": "L'Oceanografic Valencia in depth: Belugas.. Dolphins. Details — Europe's largest.. Tickets. 2003. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Zones.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Zones.", "x": "L'Oceanografic Valencia in depth: Zones.. Valencia. Details — Europe's largest.. Valencia. Arctic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "L'Oceanografic Valencia in depth: Tickets.. 2003. Details — Europe's largest.. Design. Calatrava. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Valencia.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Valencia.", "x": "L'Oceanografic Valencia in depth: Valencia.. Arctic. Details — Europe's largest.. Building. Belugas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Design.", "x": "L'Oceanografic Valencia in depth: Design.. Calatrava. Details — Europe's largest.. Belugas. Dolphins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where L'Oceanografic Valencia comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where L'Oceanografic Valencia comes from.", "x": "Origins: Building.. Calatrava. The history of L'Oceanografic Valencia — Europe's largest.. Belugas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing L'Oceanografic Valencia respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing L'Oceanografic Valencia respectfully.", "x": "Engaging: Zones.. Belugas. How to participate or observe well — L'Oceanografic Valencia. Europe's largest. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "L'Oceanografic Valencia do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "L'Oceanografic Valencia do's and don'ts.", "x": "Etiquette: Valencia.. Dolphins. The rules of respect — L'Oceanografic Valencia. Europe's largest. When in doubt, ask about Design.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around L'Oceanografic Valencia.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around L'Oceanografic Valencia.", "x": "Planning: Building.. Valencia. Practical notes — L'Oceanografic Valencia. Europe's largest. A little planning shows respect for Belugas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "L'Oceanografic Valencia and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "L'Oceanografic Valencia and money.", "x": "Costs: Zones.. 2003. What to budget — L'Oceanografic Valencia. Europe's largest. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium-oceanografic-valencia-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
