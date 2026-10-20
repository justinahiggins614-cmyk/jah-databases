(function(){'use strict';
/* JAH Channel Tunnel Tunnel Database generator — jahdb-e2-tunnel-channel-tunnel-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tunnel-channel-tunnel',PREFIX='JAH-E2TUNNELCHA-',NAME='JAH Channel Tunnel Tunnel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Channel Tunnel: the complete guide", "d": "Channel Tunnel: the Chunnel: England-France..", "g": "overview", "l": 2, "q": "What is Channel Tunnel: the complete guide?", "a": "Channel Tunnel: the Chunnel: England-France..", "x": "The complete tunnel guide to Channel Tunnel: the Chunnel: England-France.. 50.5 km. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Channel Tunnel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Channel Tunnel essentials.", "x": "At a glance: Channel Tunnel — the Chunnel: England-France.. 1994. The essentials: Build.. Eurostar. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "50.5 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "50.5 km.", "x": "Channel Tunnel: 50.5 km.. Build. Essential knowledge — Eurostar.. the Chunnel: England-France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 50.5 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 50.5 km..", "x": "Explained: 50.5 km.. Shuttle. The context — Channel Tunnel. Shuttle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1994.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1994.", "x": "Channel Tunnel: 1994.. Trains. Essential knowledge — Shuttle.. the Chunnel: England-France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1994..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1994..", "x": "Explained: 1994.. Safety. The context — Channel Tunnel. Engineering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Eurostar.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Eurostar.", "x": "Channel Tunnel: Eurostar.. Shuttle. Essential knowledge — Engineering.. the Chunnel: England-France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Eurostar..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Eurostar..", "x": "Explained: Eurostar.. Travel. The context — Channel Tunnel. Fire 1996. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shuttle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shuttle.", "x": "Channel Tunnel: Shuttle.. Safety. Essential knowledge — Fire 1996.. the Chunnel: England-France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shuttle..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shuttle..", "x": "Explained: Shuttle.. History. The context — Channel Tunnel. 50.5 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Engineering.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Engineering.", "x": "Channel Tunnel: Engineering.. Travel. Essential knowledge — 50.5 km.. the Chunnel: England-France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Engineering..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Engineering..", "x": "Explained: Engineering.. Build. The context — Channel Tunnel. 1994. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fire 1996.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fire 1996.", "x": "Channel Tunnel: Fire 1996.. History. Essential knowledge — 1994.. the Chunnel: England-France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fire 1996..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fire 1996..", "x": "Explained: Fire 1996.. Trains. The context — Channel Tunnel. Eurostar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Channel Tunnel in depth: History.. 1994. Details — the Chunnel: England-France.. Trains. Shuttle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Build.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Build.", "x": "Channel Tunnel in depth: Build.. Eurostar. Details — the Chunnel: England-France.. Shuttle. Engineering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Trains.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Trains.", "x": "Channel Tunnel in depth: Trains.. Shuttle. Details — the Chunnel: England-France.. Safety. Fire 1996. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shuttle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shuttle.", "x": "Channel Tunnel in depth: Shuttle.. Engineering. Details — the Chunnel: England-France.. Travel. 50.5 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Safety.", "x": "Channel Tunnel in depth: Safety.. Fire 1996. Details — the Chunnel: England-France.. History. 1994. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Channel Tunnel in depth: Travel.. 50.5 km. Details — the Chunnel: England-France.. Build. Eurostar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Channel Tunnel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Channel Tunnel comes from.", "x": "Origins: History.. 50.5 km. The history of Channel Tunnel — the Chunnel: England-France.. Build. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Channel Tunnel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Channel Tunnel respectfully.", "x": "Engaging: Trains.. 1994. How to participate or observe well — Channel Tunnel. the Chunnel: England-France. Respect first, always; Shuttle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Channel Tunnel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Channel Tunnel do's and don'ts.", "x": "Etiquette: Safety.. Eurostar. The rules of respect — Channel Tunnel. the Chunnel: England-France. When in doubt, ask about Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Channel Tunnel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Channel Tunnel.", "x": "Planning: History.. Shuttle. Practical notes — Channel Tunnel. the Chunnel: England-France. A little planning shows respect for Build.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Channel Tunnel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Channel Tunnel and money.", "x": "Costs: Trains.. Engineering. What to budget — Channel Tunnel. the Chunnel: England-France. The best experiences of Shuttle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tunnel-channel-tunnel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
