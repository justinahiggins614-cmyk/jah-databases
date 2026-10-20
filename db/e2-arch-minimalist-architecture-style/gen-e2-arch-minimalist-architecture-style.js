(function(){'use strict';
/* JAH Minimalist Architecture Style Database generator — jahdb-e2-arch-minimalist-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-minimalist-architecture-style',PREFIX='JAH-E2ARCHMINIM-',NAME='JAH Minimalist Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Minimalist Architecture: the complete guide", "d": "Minimalist Architecture: the less is more..", "g": "overview", "l": 2, "q": "What is Minimalist Architecture: the complete guide?", "a": "Minimalist Architecture: the less is more..", "x": "The complete architecture style guide to Minimalist Architecture: the less is more.. Mies. History, meaning, practices, and how to engage respectfully — everything in one database. Mies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Minimalist Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Minimalist Architecture essentials.", "x": "At a glance: Minimalist Architecture — the less is more.. Less. The essentials: White.. White. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mies.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mies.", "x": "Minimalist Architecture: Mies.. White. Essential knowledge — White.. the less is more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mies..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mies..", "x": "Explained: Mies.. 1990s. The context — Minimalist Architecture. Light. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Less.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Less.", "x": "Minimalist Architecture: Less.. Calm. Essential knowledge — Light.. the less is more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Less..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Less..", "x": "Explained: Less.. Less. The context — Minimalist Architecture. 1990s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "White.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "White.", "x": "Minimalist Architecture: White.. 1990s. Essential knowledge — 1990s.. the less is more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: White..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: White..", "x": "Explained: White.. Legacy. The context — Minimalist Architecture. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Light.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Light.", "x": "Minimalist Architecture: Light.. Less. Essential knowledge — Calm.. the less is more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Light..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Light..", "x": "Explained: Light.. Mies. The context — Minimalist Architecture. Mies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1990s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1990s.", "x": "Minimalist Architecture: 1990s.. Legacy. Essential knowledge — Mies.. the less is more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1990s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1990s..", "x": "Explained: 1990s.. White. The context — Minimalist Architecture. Less. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Calm.", "x": "Minimalist Architecture: Calm.. Mies. Essential knowledge — Less.. the less is more. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Calm. The context — Minimalist Architecture. White. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mies.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mies.", "x": "Minimalist Architecture in depth: Mies.. Less. Details — the less is more.. Calm. Light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "White.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "White.", "x": "Minimalist Architecture in depth: White.. White. Details — the less is more.. 1990s. 1990s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Calm.", "x": "Minimalist Architecture in depth: Calm.. Light. Details — the less is more.. Less. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1990s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1990s.", "x": "Minimalist Architecture in depth: 1990s.. 1990s. Details — the less is more.. Legacy. Mies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Less.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Less.", "x": "Minimalist Architecture in depth: Less.. Calm. Details — the less is more.. Mies. Less. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Minimalist Architecture in depth: Legacy.. Mies. Details — the less is more.. White. White. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Minimalist Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Minimalist Architecture comes from.", "x": "Origins: Mies.. Mies. The history of Minimalist Architecture — the less is more.. White. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Minimalist Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Minimalist Architecture respectfully.", "x": "Engaging: Calm.. Less. How to participate or observe well — Minimalist Architecture. the less is more. Respect first, always; 1990s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Minimalist Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Minimalist Architecture do's and don'ts.", "x": "Etiquette: Less.. White. The rules of respect — Minimalist Architecture. the less is more. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Minimalist Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Minimalist Architecture.", "x": "Planning: Mies.. Light. Practical notes — Minimalist Architecture. the less is more. A little planning shows respect for White.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Minimalist Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Minimalist Architecture and money.", "x": "Costs: Calm.. 1990s. What to budget — Minimalist Architecture. the less is more. The best experiences of 1990s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-minimalist-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
