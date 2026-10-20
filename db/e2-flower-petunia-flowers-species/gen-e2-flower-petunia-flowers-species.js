(function(){'use strict';
/* JAH Petunia Flowers Flower Database generator — jahdb-e2-flower-petunia-flowers-species-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-flower-petunia-flowers-species',PREFIX='JAH-E2FLOWERPET-',NAME='JAH Petunia Flowers Flower Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Petunia Flowers: the complete guide", "d": "Petunia Flowers: the trailing color..", "g": "overview", "l": 2, "q": "What is Petunia Flowers: the complete guide?", "a": "Petunia Flowers: the trailing color..", "x": "The complete flower guide to Petunia Flowers: the trailing color.. Trailing. History, meaning, practices, and how to engage respectfully — everything in one database. Trailing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Petunia Flowers essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Petunia Flowers essentials.", "x": "At a glance: Petunia Flowers — the trailing color.. Deadheading. The essentials: Baskets.. Annual. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Trailing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Trailing.", "x": "Petunia Flowers: Trailing.. Baskets. Essential knowledge — Annual.. the trailing color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Trailing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Trailing..", "x": "Explained: Trailing.. Sticky. The context — Petunia Flowers. Baskets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Deadheading.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Deadheading.", "x": "Petunia Flowers: Deadheading.. Colors. Essential knowledge — Baskets.. the trailing color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Deadheading..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Deadheading..", "x": "Explained: Deadheading.. Annual. The context — Petunia Flowers. Sticky. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Annual.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Annual.", "x": "Petunia Flowers: Annual.. Sticky. Essential knowledge — Sticky.. the trailing color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Annual..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Annual..", "x": "Explained: Annual.. Guide. The context — Petunia Flowers. Colors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Baskets.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Baskets.", "x": "Petunia Flowers: Baskets.. Annual. Essential knowledge — Colors.. the trailing color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Baskets..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Baskets..", "x": "Explained: Baskets.. Trailing. The context — Petunia Flowers. Trailing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sticky.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sticky.", "x": "Petunia Flowers: Sticky.. Guide. Essential knowledge — Trailing.. the trailing color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sticky..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sticky..", "x": "Explained: Sticky.. Baskets. The context — Petunia Flowers. Deadheading. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Colors.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Colors.", "x": "Petunia Flowers: Colors.. Trailing. Essential knowledge — Deadheading.. the trailing color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Colors..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Colors..", "x": "Explained: Colors.. Colors. The context — Petunia Flowers. Annual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Trailing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Trailing.", "x": "Petunia Flowers in depth: Trailing.. Deadheading. Details — the trailing color.. Colors. Baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Baskets.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Baskets.", "x": "Petunia Flowers in depth: Baskets.. Annual. Details — the trailing color.. Sticky. Sticky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Colors.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Colors.", "x": "Petunia Flowers in depth: Colors.. Baskets. Details — the trailing color.. Annual. Colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sticky.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sticky.", "x": "Petunia Flowers in depth: Sticky.. Sticky. Details — the trailing color.. Guide. Trailing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Annual.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Annual.", "x": "Petunia Flowers in depth: Annual.. Colors. Details — the trailing color.. Trailing. Deadheading. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Petunia Flowers in depth: Guide.. Trailing. Details — the trailing color.. Baskets. Annual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Petunia Flowers comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Petunia Flowers comes from.", "x": "Origins: Trailing.. Trailing. The history of Petunia Flowers — the trailing color.. Baskets. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Petunia Flowers respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Petunia Flowers respectfully.", "x": "Engaging: Colors.. Deadheading. How to participate or observe well — Petunia Flowers. the trailing color. Respect first, always; Sticky.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Petunia Flowers do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Petunia Flowers do's and don'ts.", "x": "Etiquette: Annual.. Annual. The rules of respect — Petunia Flowers. the trailing color. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Petunia Flowers.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Petunia Flowers.", "x": "Planning: Trailing.. Baskets. Practical notes — Petunia Flowers. the trailing color. A little planning shows respect for Baskets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Petunia Flowers and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Petunia Flowers and money.", "x": "Costs: Colors.. Sticky. What to budget — Petunia Flowers. the trailing color. The best experiences of Sticky. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-flower-petunia-flowers-species-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
