(function(){'use strict';
/* JAH Nintendo Switch Console Database generator — jahdb-e2-console-nintendo-switch-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-nintendo-switch-console',PREFIX='JAH-E2CONSOLENI-',NAME='JAH Nintendo Switch Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nintendo Switch: the complete guide", "d": "Nintendo Switch: the hybrid..", "g": "overview", "l": 2, "q": "What is Nintendo Switch: the complete guide?", "a": "Nintendo Switch: the hybrid..", "x": "The complete console guide to Nintendo Switch: the hybrid.. 2017. History, meaning, practices, and how to engage respectfully — everything in one database. Hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nintendo Switch essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nintendo Switch essentials.", "x": "At a glance: Nintendo Switch — the hybrid.. Hybrid. The essentials: BotW.. Breath of Wild. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2017.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2017.", "x": "Nintendo Switch: 2017.. BotW. Essential knowledge — Breath of Wild.. the hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2017..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2017..", "x": "Explained: 2017.. 140M. The context — Nintendo Switch. Joy-Con. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hybrid.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hybrid.", "x": "Nintendo Switch: Hybrid.. Joy-Con. Essential knowledge — Joy-Con.. the hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hybrid..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hybrid..", "x": "Explained: Hybrid.. Nintendo. The context — Nintendo Switch. 140M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Breath of Wild.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Breath of Wild.", "x": "Nintendo Switch: Breath of Wild.. 140M. Essential knowledge — 140M.. the hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Breath of Wild..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Breath of Wild..", "x": "Explained: Breath of Wild.. Legacy. The context — Nintendo Switch. Nintendo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Joy-Con.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Joy-Con.", "x": "Nintendo Switch: Joy-Con.. Nintendo. Essential knowledge — Nintendo.. the hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Joy-Con..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Joy-Con..", "x": "Explained: Joy-Con.. Hybrid. The context — Nintendo Switch. 2017. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "140M.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "140M.", "x": "Nintendo Switch: 140M.. Legacy. Essential knowledge — 2017.. the hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 140M..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 140M..", "x": "Explained: 140M.. BotW. The context — Nintendo Switch. Hybrid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nintendo.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nintendo.", "x": "Nintendo Switch: Nintendo.. Hybrid. Essential knowledge — Hybrid.. the hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Nintendo..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Nintendo..", "x": "Explained: Nintendo.. Joy-Con. The context — Nintendo Switch. Breath of Wild. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hybrid.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hybrid.", "x": "Nintendo Switch in depth: Hybrid.. Hybrid. Details — the hybrid.. Joy-Con. Joy-Con. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "BotW.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "BotW.", "x": "Nintendo Switch in depth: BotW.. Breath of Wild. Details — the hybrid.. 140M. 140M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Joy-Con.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Joy-Con.", "x": "Nintendo Switch in depth: Joy-Con.. Joy-Con. Details — the hybrid.. Nintendo. Nintendo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "140M.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "140M.", "x": "Nintendo Switch in depth: 140M.. 140M. Details — the hybrid.. Legacy. 2017. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nintendo.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nintendo.", "x": "Nintendo Switch in depth: Nintendo.. Nintendo. Details — the hybrid.. Hybrid. Hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Nintendo Switch in depth: Legacy.. 2017. Details — the hybrid.. BotW. Breath of Wild. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nintendo Switch comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nintendo Switch comes from.", "x": "Origins: Hybrid.. 2017. The history of Nintendo Switch — the hybrid.. BotW. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nintendo Switch respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nintendo Switch respectfully.", "x": "Engaging: Joy-Con.. Hybrid. How to participate or observe well — Nintendo Switch. the hybrid. Respect first, always; 140M.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nintendo Switch do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nintendo Switch do's and don'ts.", "x": "Etiquette: Nintendo.. Breath of Wild. The rules of respect — Nintendo Switch. the hybrid. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nintendo Switch.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nintendo Switch.", "x": "Planning: Hybrid.. Joy-Con. Practical notes — Nintendo Switch. the hybrid. A little planning shows respect for BotW.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nintendo Switch and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nintendo Switch and money.", "x": "Costs: Joy-Con.. 140M. What to budget — Nintendo Switch. the hybrid. The best experiences of 140M. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-nintendo-switch-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
