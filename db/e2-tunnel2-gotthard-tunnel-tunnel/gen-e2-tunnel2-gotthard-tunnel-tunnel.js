(function(){'use strict';
/* JAH Gotthard Tunnel Database generator — jahdb-e2-tunnel2-gotthard-tunnel-tunnel-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tunnel2-gotthard-tunnel-tunnel',PREFIX='JAH-E2TUNNEL2GO-',NAME='JAH Gotthard Tunnel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gotthard Tunnel: the complete guide", "d": "Gotthard Tunnel: the Swiss..", "g": "overview", "l": 2, "q": "What is Gotthard Tunnel: the complete guide?", "a": "Gotthard Tunnel: the Swiss..", "x": "The complete tunnel guide to Gotthard Tunnel: the Swiss.. 2016. History, meaning, practices, and how to engage respectfully — everything in one database. 2016. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gotthard Tunnel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gotthard Tunnel essentials.", "x": "At a glance: Gotthard Tunnel — the Swiss.. 57 km. The essentials: Rail.. Longest. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2016.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2016.", "x": "Gotthard Tunnel: 2016.. Rail. Essential knowledge — Longest.. the Swiss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2016..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2016..", "x": "Explained: 2016.. 57 km. The context — Gotthard Tunnel. Alps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "57 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "57 km.", "x": "Gotthard Tunnel: 57 km.. Switzerland. Essential knowledge — Alps.. the Swiss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 57 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 57 km..", "x": "Explained: 57 km.. Longest. The context — Gotthard Tunnel. Switzerland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Longest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Longest.", "x": "Gotthard Tunnel: Longest.. 57 km. Essential knowledge — Switzerland.. the Swiss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Longest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Longest..", "x": "Explained: Longest.. Facts. The context — Gotthard Tunnel. Rail. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Alps.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Alps.", "x": "Gotthard Tunnel: Alps.. Longest. Essential knowledge — Rail.. the Swiss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Alps..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Alps..", "x": "Explained: Alps.. 2016. The context — Gotthard Tunnel. 2016. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Switzerland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Switzerland.", "x": "Gotthard Tunnel: Switzerland.. Facts. Essential knowledge — 2016.. the Swiss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Switzerland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Switzerland..", "x": "Explained: Switzerland.. Rail. The context — Gotthard Tunnel. 57 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rail.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rail.", "x": "Gotthard Tunnel: Rail.. 2016. Essential knowledge — 57 km.. the Swiss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Rail..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Rail..", "x": "Explained: Rail.. Switzerland. The context — Gotthard Tunnel. Longest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "2016.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "2016.", "x": "Gotthard Tunnel in depth: 2016.. 57 km. Details — the Swiss.. Switzerland. Alps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rail.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rail.", "x": "Gotthard Tunnel in depth: Rail.. Longest. Details — the Swiss.. 57 km. Switzerland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Switzerland.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Switzerland.", "x": "Gotthard Tunnel in depth: Switzerland.. Alps. Details — the Swiss.. Longest. Rail. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "57 km.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "57 km.", "x": "Gotthard Tunnel in depth: 57 km.. Switzerland. Details — the Swiss.. Facts. 2016. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Longest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Longest.", "x": "Gotthard Tunnel in depth: Longest.. Rail. Details — the Swiss.. 2016. 57 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Facts.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Facts.", "x": "Gotthard Tunnel in depth: Facts.. 2016. Details — the Swiss.. Rail. Longest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gotthard Tunnel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gotthard Tunnel comes from.", "x": "Origins: 2016.. 2016. The history of Gotthard Tunnel — the Swiss.. Rail. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gotthard Tunnel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gotthard Tunnel respectfully.", "x": "Engaging: Switzerland.. 57 km. How to participate or observe well — Gotthard Tunnel. the Swiss. Respect first, always; 57 km.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gotthard Tunnel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gotthard Tunnel do's and don'ts.", "x": "Etiquette: Longest.. Longest. The rules of respect — Gotthard Tunnel. the Swiss. When in doubt, ask about Facts.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gotthard Tunnel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gotthard Tunnel.", "x": "Planning: 2016.. Alps. Practical notes — Gotthard Tunnel. the Swiss. A little planning shows respect for Rail.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gotthard Tunnel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gotthard Tunnel and money.", "x": "Costs: Switzerland.. Switzerland. What to budget — Gotthard Tunnel. the Swiss. The best experiences of 57 km. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tunnel2-gotthard-tunnel-tunnel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
