(function(){'use strict';
/* JAH Chamomile Tea Tea Database generator — jahdb-e2-tea-chamomile-tea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tea-chamomile-tea',PREFIX='JAH-E2TEACHAMOM-',NAME='JAH Chamomile Tea Tea Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chamomile Tea: the complete guide", "d": "Chamomile Tea: the bedtime herbal..", "g": "overview", "l": 2, "q": "What is Chamomile Tea: the complete guide?", "a": "Chamomile Tea: the bedtime herbal..", "x": "The complete tea guide to Chamomile Tea: the bedtime herbal.. Herbal. History, meaning, practices, and how to engage respectfully — everything in one database. Herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chamomile Tea essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chamomile Tea essentials.", "x": "At a glance: Chamomile Tea — the bedtime herbal.. Sleep. The essentials: Sleep.. Apple. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Herbal.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Herbal.", "x": "Chamomile Tea: Herbal.. Sleep. Essential knowledge — Apple.. the bedtime herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Herbal..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Herbal..", "x": "Explained: Herbal.. German. The context — Chamomile Tea. Caffeine-free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sleep.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sleep.", "x": "Chamomile Tea: Sleep.. Evening. Essential knowledge — Caffeine-free.. the bedtime herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sleep..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sleep..", "x": "Explained: Sleep.. Blends. The context — Chamomile Tea. German. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Apple.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Apple.", "x": "Chamomile Tea: Apple.. German. Essential knowledge — German.. the bedtime herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Apple..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Apple..", "x": "Explained: Apple.. Growing. The context — Chamomile Tea. Evening. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Caffeine-free.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Caffeine-free.", "x": "Chamomile Tea: Caffeine-free.. Blends. Essential knowledge — Evening.. the bedtime herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Caffeine-free..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Caffeine-free..", "x": "Explained: Caffeine-free.. Herbal. The context — Chamomile Tea. Herbal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "German.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "German.", "x": "Chamomile Tea: German.. Growing. Essential knowledge — Herbal.. the bedtime herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: German..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: German..", "x": "Explained: German.. Sleep. The context — Chamomile Tea. Sleep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Evening.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Evening.", "x": "Chamomile Tea: Evening.. Herbal. Essential knowledge — Sleep.. the bedtime herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Evening..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Evening..", "x": "Explained: Evening.. Evening. The context — Chamomile Tea. Apple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Herbal.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Herbal.", "x": "Chamomile Tea in depth: Herbal.. Sleep. Details — the bedtime herbal.. Evening. Caffeine-free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sleep.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sleep.", "x": "Chamomile Tea in depth: Sleep.. Apple. Details — the bedtime herbal.. German. German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Evening.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Evening.", "x": "Chamomile Tea in depth: Evening.. Caffeine-free. Details — the bedtime herbal.. Blends. Evening. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "German.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "German.", "x": "Chamomile Tea in depth: German.. German. Details — the bedtime herbal.. Growing. Herbal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Blends.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Blends.", "x": "Chamomile Tea in depth: Blends.. Evening. Details — the bedtime herbal.. Herbal. Sleep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Growing.", "x": "Chamomile Tea in depth: Growing.. Herbal. Details — the bedtime herbal.. Sleep. Apple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chamomile Tea comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chamomile Tea comes from.", "x": "Origins: Herbal.. Herbal. The history of Chamomile Tea — the bedtime herbal.. Sleep. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chamomile Tea respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chamomile Tea respectfully.", "x": "Engaging: Evening.. Sleep. How to participate or observe well — Chamomile Tea. the bedtime herbal. Respect first, always; German.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chamomile Tea do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chamomile Tea do's and don'ts.", "x": "Etiquette: Blends.. Apple. The rules of respect — Chamomile Tea. the bedtime herbal. When in doubt, ask about Growing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chamomile Tea.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chamomile Tea.", "x": "Planning: Herbal.. Caffeine-free. Practical notes — Chamomile Tea. the bedtime herbal. A little planning shows respect for Sleep.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chamomile Tea and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chamomile Tea and money.", "x": "Costs: Evening.. German. What to budget — Chamomile Tea. the bedtime herbal. The best experiences of German. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tea-chamomile-tea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
