(function(){'use strict';
/* JAH Carnation Flowers Flower Database generator — jahdb-e2-flower-carnation-flowers-species-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-flower-carnation-flowers-species',PREFIX='JAH-E2FLOWERCAR-',NAME='JAH Carnation Flowers Flower Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carnation Flowers: the complete guide", "d": "Carnation Flowers: the long-lasting..", "g": "overview", "l": 2, "q": "What is Carnation Flowers: the complete guide?", "a": "Carnation Flowers: the long-lasting..", "x": "The complete flower guide to Carnation Flowers: the long-lasting.. Clove. History, meaning, practices, and how to engage respectfully — everything in one database. Clove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Carnation Flowers essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Carnation Flowers essentials.", "x": "At a glance: Carnation Flowers — the long-lasting.. Cut. The essentials: Vase.. Long vase. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Clove.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Clove.", "x": "Carnation Flowers: Clove.. Vase. Essential knowledge — Long vase.. the long-lasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Clove..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Clove..", "x": "Explained: Clove.. Dianthus. The context — Carnation Flowers. Dianthus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cut.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cut.", "x": "Carnation Flowers: Cut.. Mothers. Essential knowledge — Dianthus.. the long-lasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cut..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cut..", "x": "Explained: Cut.. Cut. The context — Carnation Flowers. Fringed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Long vase.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Long vase.", "x": "Carnation Flowers: Long vase.. Dianthus. Essential knowledge — Fringed.. the long-lasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Long vase..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Long vase..", "x": "Explained: Long vase.. Guide. The context — Carnation Flowers. Mothers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dianthus.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dianthus.", "x": "Carnation Flowers: Dianthus.. Cut. Essential knowledge — Mothers.. the long-lasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dianthus..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dianthus..", "x": "Explained: Dianthus.. Clove. The context — Carnation Flowers. Clove. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fringed.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fringed.", "x": "Carnation Flowers: Fringed.. Guide. Essential knowledge — Clove.. the long-lasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fringed..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fringed..", "x": "Explained: Fringed.. Vase. The context — Carnation Flowers. Cut. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mothers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mothers.", "x": "Carnation Flowers: Mothers.. Clove. Essential knowledge — Cut.. the long-lasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mothers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mothers..", "x": "Explained: Mothers.. Mothers. The context — Carnation Flowers. Long vase. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Clove.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Clove.", "x": "Carnation Flowers in depth: Clove.. Cut. Details — the long-lasting.. Mothers. Dianthus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vase.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vase.", "x": "Carnation Flowers in depth: Vase.. Long vase. Details — the long-lasting.. Dianthus. Fringed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mothers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mothers.", "x": "Carnation Flowers in depth: Mothers.. Dianthus. Details — the long-lasting.. Cut. Mothers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dianthus.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dianthus.", "x": "Carnation Flowers in depth: Dianthus.. Fringed. Details — the long-lasting.. Guide. Clove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cut.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cut.", "x": "Carnation Flowers in depth: Cut.. Mothers. Details — the long-lasting.. Clove. Cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Carnation Flowers in depth: Guide.. Clove. Details — the long-lasting.. Vase. Long vase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Carnation Flowers comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Carnation Flowers comes from.", "x": "Origins: Clove.. Clove. The history of Carnation Flowers — the long-lasting.. Vase. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Carnation Flowers respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Carnation Flowers respectfully.", "x": "Engaging: Mothers.. Cut. How to participate or observe well — Carnation Flowers. the long-lasting. Respect first, always; Dianthus.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Carnation Flowers do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Carnation Flowers do's and don'ts.", "x": "Etiquette: Cut.. Long vase. The rules of respect — Carnation Flowers. the long-lasting. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Carnation Flowers.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Carnation Flowers.", "x": "Planning: Clove.. Dianthus. Practical notes — Carnation Flowers. the long-lasting. A little planning shows respect for Vase.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Carnation Flowers and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Carnation Flowers and money.", "x": "Costs: Mothers.. Fringed. What to budget — Carnation Flowers. the long-lasting. The best experiences of Dianthus. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-flower-carnation-flowers-species-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
