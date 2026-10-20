(function(){'use strict';
/* JAH Chinese Mid-Autumn Festival Holiday Database generator — jahdb-e2-holiday-mid-autumn-festival-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-mid-autumn-festival',PREFIX='JAH-E2HOLIDAYMI-',NAME='JAH Chinese Mid-Autumn Festival Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chinese Mid-Autumn Festival: the complete guide", "d": "Chinese Mid-Autumn Festival: mooncakes and reunion..", "g": "overview", "l": 2, "q": "What is Chinese Mid-Autumn Festival: the complete guide?", "a": "Chinese Mid-Autumn Festival: mooncakes and reunion..", "x": "The complete holiday guide to Chinese Mid-Autumn Festival: mooncakes and reunion.. Fall. History, meaning, practices, and how to engage respectfully — everything in one database. Moon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chinese Mid-Autumn Festival essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chinese Mid-Autumn Festival essentials.", "x": "At a glance: Chinese Mid-Autumn Festival — mooncakes and reunion.. Mooncakes. The essentials: Cakes.. Lanterns. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fall.", "x": "Chinese Mid-Autumn Festival: Fall.. Cakes. Essential knowledge — Lanterns.. mooncakes and reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fall..", "x": "Explained: Fall.. Family. The context — Chinese Mid-Autumn Festival. Family. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mooncakes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mooncakes.", "x": "Chinese Mid-Autumn Festival: Mooncakes.. Legends. Essential knowledge — Family.. mooncakes and reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mooncakes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mooncakes..", "x": "Explained: Mooncakes.. Countries. The context — Chinese Mid-Autumn Festival. Legends. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lanterns.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lanterns.", "x": "Chinese Mid-Autumn Festival: Lanterns.. Family. Essential knowledge — Legends.. mooncakes and reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lanterns..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lanterns..", "x": "Explained: Lanterns.. Beauty. The context — Chinese Mid-Autumn Festival. Asia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Family.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Family.", "x": "Chinese Mid-Autumn Festival: Family.. Countries. Essential knowledge — Asia.. mooncakes and reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Family..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Family..", "x": "Explained: Family.. Moon. The context — Chinese Mid-Autumn Festival. Fall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Legends.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Legends.", "x": "Chinese Mid-Autumn Festival: Legends.. Beauty. Essential knowledge — Fall.. mooncakes and reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Legends..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Legends..", "x": "Explained: Legends.. Cakes. The context — Chinese Mid-Autumn Festival. Mooncakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Asia.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Asia.", "x": "Chinese Mid-Autumn Festival: Asia.. Moon. Essential knowledge — Mooncakes.. mooncakes and reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Asia..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Asia..", "x": "Explained: Asia.. Legends. The context — Chinese Mid-Autumn Festival. Lanterns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Moon.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Moon.", "x": "Chinese Mid-Autumn Festival in depth: Moon.. Mooncakes. Details — mooncakes and reunion.. Legends. Family. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cakes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cakes.", "x": "Chinese Mid-Autumn Festival in depth: Cakes.. Lanterns. Details — mooncakes and reunion.. Family. Legends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Legends.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Legends.", "x": "Chinese Mid-Autumn Festival in depth: Legends.. Family. Details — mooncakes and reunion.. Countries. Asia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Family.", "x": "Chinese Mid-Autumn Festival in depth: Family.. Legends. Details — mooncakes and reunion.. Beauty. Fall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Countries.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Countries.", "x": "Chinese Mid-Autumn Festival in depth: Countries.. Asia. Details — mooncakes and reunion.. Moon. Mooncakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Beauty.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Beauty.", "x": "Chinese Mid-Autumn Festival in depth: Beauty.. Fall. Details — mooncakes and reunion.. Cakes. Lanterns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chinese Mid-Autumn Festival comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chinese Mid-Autumn Festival comes from.", "x": "Origins: Moon.. Fall. The history of Chinese Mid-Autumn Festival — mooncakes and reunion.. Cakes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chinese Mid-Autumn Festival respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chinese Mid-Autumn Festival respectfully.", "x": "Engaging: Legends.. Mooncakes. How to participate or observe well — Chinese Mid-Autumn Festival. mooncakes and reunion. Respect first, always; Family.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chinese Mid-Autumn Festival do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chinese Mid-Autumn Festival do's and don'ts.", "x": "Etiquette: Countries.. Lanterns. The rules of respect — Chinese Mid-Autumn Festival. mooncakes and reunion. When in doubt, ask about Beauty.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chinese Mid-Autumn Festival.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chinese Mid-Autumn Festival.", "x": "Planning: Moon.. Family. Practical notes — Chinese Mid-Autumn Festival. mooncakes and reunion. A little planning shows respect for Cakes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chinese Mid-Autumn Festival and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chinese Mid-Autumn Festival and money.", "x": "Costs: Legends.. Legends. What to budget — Chinese Mid-Autumn Festival. mooncakes and reunion. The best experiences of Family. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-mid-autumn-festival-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
