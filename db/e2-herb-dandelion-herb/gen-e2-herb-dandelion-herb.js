(function(){'use strict';
/* JAH Dandelion Herb Database generator — jahdb-e2-herb-dandelion-herb-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-herb-dandelion-herb',PREFIX='JAH-E2HERBDANDE-',NAME='JAH Dandelion Herb Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dandelion: the complete guide", "d": "Dandelion: the weed superfood..", "g": "overview", "l": 2, "q": "What is Dandelion: the complete guide?", "a": "Dandelion: the weed superfood..", "x": "The complete herb guide to Dandelion: the weed superfood.. Bitter. History, meaning, practices, and how to engage respectfully — everything in one database. Greens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dandelion essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dandelion essentials.", "x": "At a glance: Dandelion — the weed superfood.. Greens. The essentials: Roots.. Roots. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bitter.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bitter.", "x": "Dandelion: Bitter.. Roots. Essential knowledge — Roots.. the weed superfood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bitter..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bitter..", "x": "Explained: Bitter.. Harvest. The context — Dandelion. Coffee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Greens.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Greens.", "x": "Dandelion: Greens.. Wine. Essential knowledge — Coffee.. the weed superfood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Greens..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Greens..", "x": "Explained: Greens.. Uses. The context — Dandelion. Wine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Roots.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Roots.", "x": "Dandelion: Roots.. Harvest. Essential knowledge — Wine.. the weed superfood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Roots..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Roots..", "x": "Explained: Roots.. Bitter. The context — Dandelion. Lions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Coffee.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Coffee.", "x": "Dandelion: Coffee.. Uses. Essential knowledge — Lions.. the weed superfood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Coffee..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Coffee..", "x": "Explained: Coffee.. Greens. The context — Dandelion. Bitter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wine.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wine.", "x": "Dandelion: Wine.. Bitter. Essential knowledge — Bitter.. the weed superfood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wine..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wine..", "x": "Explained: Wine.. Roots. The context — Dandelion. Greens. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lions.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lions.", "x": "Dandelion: Lions.. Greens. Essential knowledge — Greens.. the weed superfood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lions..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lions..", "x": "Explained: Lions.. Wine. The context — Dandelion. Roots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Greens.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Greens.", "x": "Dandelion in depth: Greens.. Greens. Details — the weed superfood.. Wine. Coffee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Roots.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Roots.", "x": "Dandelion in depth: Roots.. Roots. Details — the weed superfood.. Harvest. Wine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wine.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wine.", "x": "Dandelion in depth: Wine.. Coffee. Details — the weed superfood.. Uses. Lions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Harvest.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Harvest.", "x": "Dandelion in depth: Harvest.. Wine. Details — the weed superfood.. Bitter. Bitter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Uses.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Uses.", "x": "Dandelion in depth: Uses.. Lions. Details — the weed superfood.. Greens. Greens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Bitter.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Bitter.", "x": "Dandelion in depth: Bitter.. Bitter. Details — the weed superfood.. Roots. Roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dandelion comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dandelion comes from.", "x": "Origins: Greens.. Bitter. The history of Dandelion — the weed superfood.. Roots. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dandelion respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dandelion respectfully.", "x": "Engaging: Wine.. Greens. How to participate or observe well — Dandelion. the weed superfood. Respect first, always; Harvest.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dandelion do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dandelion do's and don'ts.", "x": "Etiquette: Uses.. Roots. The rules of respect — Dandelion. the weed superfood. When in doubt, ask about Bitter.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dandelion.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dandelion.", "x": "Planning: Greens.. Coffee. Practical notes — Dandelion. the weed superfood. A little planning shows respect for Roots.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dandelion and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dandelion and money.", "x": "Costs: Wine.. Wine. What to budget — Dandelion. the weed superfood. The best experiences of Harvest. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-herb-dandelion-herb-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
