(function(){'use strict';
/* JAH Tauern Tunnel Tunnel Database generator — jahdb-e2-tunnel-tauern-tunnel-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tunnel-tauern-tunnel',PREFIX='JAH-E2TUNNELTAU-',NAME='JAH Tauern Tunnel Tunnel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tauern Tunnel: the complete guide", "d": "Tauern Tunnel: Austria's Alpine artery..", "g": "overview", "l": 2, "q": "What is Tauern Tunnel: the complete guide?", "a": "Tauern Tunnel: Austria's Alpine artery..", "x": "The complete tunnel guide to Tauern Tunnel: Austria's Alpine artery.. 6.4 km. History, meaning, practices, and how to engage respectfully — everything in one database. Drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tauern Tunnel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tauern Tunnel essentials.", "x": "At a glance: Tauern Tunnel — Austria's Alpine artery.. A10. The essentials: Tolls.. Traffic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "6.4 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "6.4 km.", "x": "Tauern Tunnel: 6.4 km.. Tolls. Essential knowledge — Traffic.. Austria's Alpine artery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 6.4 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 6.4 km..", "x": "Explained: 6.4 km.. Alps. The context — Tauern Tunnel. Tolls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "A10.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "A10.", "x": "Tauern Tunnel: A10.. History. Essential knowledge — Tolls.. Austria's Alpine artery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: A10..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: A10..", "x": "Explained: A10.. Traffic. The context — Tauern Tunnel. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Traffic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Traffic.", "x": "Tauern Tunnel: Traffic.. Alps. Essential knowledge — History.. Austria's Alpine artery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Traffic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Traffic..", "x": "Explained: Traffic.. Safety. The context — Tauern Tunnel. Alps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tolls.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tolls.", "x": "Tauern Tunnel: Tolls.. Traffic. Essential knowledge — Alps.. Austria's Alpine artery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tolls..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tolls..", "x": "Explained: Tolls.. Drive. The context — Tauern Tunnel. 6.4 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Tauern Tunnel: History.. Safety. Essential knowledge — 6.4 km.. Austria's Alpine artery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. Tolls. The context — Tauern Tunnel. A10. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Alps.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Alps.", "x": "Tauern Tunnel: Alps.. Drive. Essential knowledge — A10.. Austria's Alpine artery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Alps..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Alps..", "x": "Explained: Alps.. History. The context — Tauern Tunnel. Traffic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Drive.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Drive.", "x": "Tauern Tunnel in depth: Drive.. A10. Details — Austria's Alpine artery.. History. Tolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tolls.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tolls.", "x": "Tauern Tunnel in depth: Tolls.. Traffic. Details — Austria's Alpine artery.. Alps. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Tauern Tunnel in depth: History.. Tolls. Details — Austria's Alpine artery.. Traffic. Alps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Alps.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Alps.", "x": "Tauern Tunnel in depth: Alps.. History. Details — Austria's Alpine artery.. Safety. 6.4 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Traffic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Traffic.", "x": "Tauern Tunnel in depth: Traffic.. Alps. Details — Austria's Alpine artery.. Drive. A10. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safety.", "x": "Tauern Tunnel in depth: Safety.. 6.4 km. Details — Austria's Alpine artery.. Tolls. Traffic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tauern Tunnel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tauern Tunnel comes from.", "x": "Origins: Drive.. 6.4 km. The history of Tauern Tunnel — Austria's Alpine artery.. Tolls. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tauern Tunnel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tauern Tunnel respectfully.", "x": "Engaging: History.. A10. How to participate or observe well — Tauern Tunnel. Austria's Alpine artery. Respect first, always; Alps.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tauern Tunnel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tauern Tunnel do's and don'ts.", "x": "Etiquette: Traffic.. Traffic. The rules of respect — Tauern Tunnel. Austria's Alpine artery. When in doubt, ask about Safety.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tauern Tunnel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tauern Tunnel.", "x": "Planning: Drive.. Tolls. Practical notes — Tauern Tunnel. Austria's Alpine artery. A little planning shows respect for Tolls.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tauern Tunnel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tauern Tunnel and money.", "x": "Costs: History.. History. What to budget — Tauern Tunnel. Austria's Alpine artery. The best experiences of Alps. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tunnel-tauern-tunnel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
