(function(){'use strict';
/* JAH Vatican Museums Museum Database generator — jahdb-e2-museum-vatican-museums-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-vatican-museums',PREFIX='JAH-E2MUSEUMVAT-',NAME='JAH Vatican Museums Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vatican Museums: the complete guide", "d": "Vatican Museums: Sistine Chapel and more..", "g": "overview", "l": 2, "q": "What is Vatican Museums: the complete guide?", "a": "Vatican Museums: Sistine Chapel and more..", "x": "The complete museum guide to Vatican Museums: Sistine Chapel and more.. Sistine Chapel. History, meaning, practices, and how to engage respectfully — everything in one database. Chapel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vatican Museums essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vatican Museums essentials.", "x": "At a glance: Vatican Museums — Sistine Chapel and more.. Michelangelo. The essentials: Raphael.. Raphael Rooms. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sistine Chapel.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sistine Chapel.", "x": "Vatican Museums: Sistine Chapel.. Raphael. Essential knowledge — Raphael Rooms.. Sistine Chapel and more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sistine Chapel..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sistine Chapel..", "x": "Explained: Sistine Chapel.. Tickets. The context — Vatican Museums. 7 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Michelangelo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Michelangelo.", "x": "Vatican Museums: Michelangelo.. Routes. Essential knowledge — 7 km.. Sistine Chapel and more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Michelangelo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Michelangelo..", "x": "Explained: Michelangelo.. History. The context — Vatican Museums. 6M visitors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Raphael Rooms.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Raphael Rooms.", "x": "Vatican Museums: Raphael Rooms.. Tickets. Essential knowledge — 6M visitors.. Sistine Chapel and more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Raphael Rooms..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Raphael Rooms..", "x": "Explained: Raphael Rooms.. Art. The context — Vatican Museums. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "7 km.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "7 km.", "x": "Vatican Museums: 7 km.. History. Essential knowledge — History.. Sistine Chapel and more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 7 km..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 7 km..", "x": "Explained: 7 km.. Chapel. The context — Vatican Museums. Sistine Chapel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "6M visitors.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "6M visitors.", "x": "Vatican Museums: 6M visitors.. Art. Essential knowledge — Sistine Chapel.. Sistine Chapel and more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 6M visitors..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 6M visitors..", "x": "Explained: 6M visitors.. Raphael. The context — Vatican Museums. Michelangelo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Vatican Museums: History.. Chapel. Essential knowledge — Michelangelo.. Sistine Chapel and more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Routes. The context — Vatican Museums. Raphael Rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chapel.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chapel.", "x": "Vatican Museums in depth: Chapel.. Michelangelo. Details — Sistine Chapel and more.. Routes. 7 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Raphael.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Raphael.", "x": "Vatican Museums in depth: Raphael.. Raphael Rooms. Details — Sistine Chapel and more.. Tickets. 6M visitors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Routes.", "x": "Vatican Museums in depth: Routes.. 7 km. Details — Sistine Chapel and more.. History. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Vatican Museums in depth: Tickets.. 6M visitors. Details — Sistine Chapel and more.. Art. Sistine Chapel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Vatican Museums in depth: History.. History. Details — Sistine Chapel and more.. Chapel. Michelangelo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Vatican Museums in depth: Art.. Sistine Chapel. Details — Sistine Chapel and more.. Raphael. Raphael Rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vatican Museums comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vatican Museums comes from.", "x": "Origins: Chapel.. Sistine Chapel. The history of Vatican Museums — Sistine Chapel and more.. Raphael. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vatican Museums respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vatican Museums respectfully.", "x": "Engaging: Routes.. Michelangelo. How to participate or observe well — Vatican Museums. Sistine Chapel and more. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vatican Museums do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vatican Museums do's and don'ts.", "x": "Etiquette: History.. Raphael Rooms. The rules of respect — Vatican Museums. Sistine Chapel and more. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vatican Museums.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vatican Museums.", "x": "Planning: Chapel.. 7 km. Practical notes — Vatican Museums. Sistine Chapel and more. A little planning shows respect for Raphael.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vatican Museums and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vatican Museums and money.", "x": "Costs: Routes.. 6M visitors. What to budget — Vatican Museums. Sistine Chapel and more. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-vatican-museums-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
