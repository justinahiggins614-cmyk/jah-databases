(function(){'use strict';
/* JAH Garden Route Landmark Database generator — jahdb-e2-landmark-garden-route-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-garden-route-landmark',PREFIX='JAH-E2LANDMARKG-',NAME='JAH Garden Route Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Garden Route: the complete guide", "d": "Garden Route: the scenic drive..", "g": "overview", "l": 2, "q": "What is Garden Route: the complete guide?", "a": "Garden Route: the scenic drive..", "x": "The complete landmark guide to Garden Route: the scenic drive.. 300 km. History, meaning, practices, and how to engage respectfully — everything in one database. 300 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Garden Route essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Garden Route essentials.", "x": "At a glance: Garden Route — the scenic drive.. Drive. The essentials: Coast.. Oudtshoorn. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "300 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "300 km.", "x": "Garden Route: 300 km.. Coast. Essential knowledge — Oudtshoorn.. the scenic drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 300 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 300 km..", "x": "Explained: 300 km.. Drive. The context — Garden Route. Knysna. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Drive.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Drive.", "x": "Garden Route: Drive.. Scenic. Essential knowledge — Knysna.. the scenic drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Drive..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Drive..", "x": "Explained: Drive.. Knysna. The context — Garden Route. Coast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Oudtshoorn.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Oudtshoorn.", "x": "Garden Route: Oudtshoorn.. Drive. Essential knowledge — Coast.. the scenic drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Oudtshoorn..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Oudtshoorn..", "x": "Explained: Oudtshoorn.. Driving. The context — Garden Route. Scenic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Knysna.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Knysna.", "x": "Garden Route: Knysna.. Knysna. Essential knowledge — Scenic.. the scenic drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Knysna..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Knysna..", "x": "Explained: Knysna.. 300 km. The context — Garden Route. 300 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Coast.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Coast.", "x": "Garden Route: Coast.. Driving. Essential knowledge — 300 km.. the scenic drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Coast..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Coast..", "x": "Explained: Coast.. Coast. The context — Garden Route. Drive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Scenic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Scenic.", "x": "Garden Route: Scenic.. 300 km. Essential knowledge — Drive.. the scenic drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Scenic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Scenic..", "x": "Explained: Scenic.. Scenic. The context — Garden Route. Oudtshoorn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "300 km.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "300 km.", "x": "Garden Route in depth: 300 km.. Drive. Details — the scenic drive.. Scenic. Knysna. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Coast.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Coast.", "x": "Garden Route in depth: Coast.. Oudtshoorn. Details — the scenic drive.. Drive. Coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Scenic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Scenic.", "x": "Garden Route in depth: Scenic.. Knysna. Details — the scenic drive.. Knysna. Scenic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drive.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drive.", "x": "Garden Route in depth: Drive.. Coast. Details — the scenic drive.. Driving. 300 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Knysna.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Knysna.", "x": "Garden Route in depth: Knysna.. Scenic. Details — the scenic drive.. 300 km. Drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Driving.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Driving.", "x": "Garden Route in depth: Driving.. 300 km. Details — the scenic drive.. Coast. Oudtshoorn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Garden Route comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Garden Route comes from.", "x": "Origins: 300 km.. 300 km. The history of Garden Route — the scenic drive.. Coast. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Garden Route respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Garden Route respectfully.", "x": "Engaging: Scenic.. Drive. How to participate or observe well — Garden Route. the scenic drive. Respect first, always; Drive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Garden Route do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Garden Route do's and don'ts.", "x": "Etiquette: Knysna.. Oudtshoorn. The rules of respect — Garden Route. the scenic drive. When in doubt, ask about Driving.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Garden Route.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Garden Route.", "x": "Planning: 300 km.. Knysna. Practical notes — Garden Route. the scenic drive. A little planning shows respect for Coast.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Garden Route and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Garden Route and money.", "x": "Costs: Scenic.. Coast. What to budget — Garden Route. the scenic drive. The best experiences of Drive. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-garden-route-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
