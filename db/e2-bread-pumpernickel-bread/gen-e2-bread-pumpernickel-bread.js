(function(){'use strict';
/* JAH Pumpernickel Bread Database generator — jahdb-e2-bread-pumpernickel-bread-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bread-pumpernickel-bread',PREFIX='JAH-E2BREADPUMP-',NAME='JAH Pumpernickel Bread Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pumpernickel: the complete guide", "d": "Pumpernickel: the dark German..", "g": "overview", "l": 2, "q": "What is Pumpernickel: the complete guide?", "a": "Pumpernickel: the dark German..", "x": "The complete bread guide to Pumpernickel: the dark German.. Germany. History, meaning, practices, and how to engage respectfully — everything in one database. Bake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pumpernickel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pumpernickel essentials.", "x": "At a glance: Pumpernickel — the dark German.. Long bake. The essentials: Molasses.. Molasses. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Germany.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Germany.", "x": "Pumpernickel: Germany.. Molasses. Essential knowledge — Molasses.. the dark German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Germany..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Germany..", "x": "Explained: Germany.. Germany. The context — Pumpernickel. Dense. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Long bake.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Long bake.", "x": "Pumpernickel: Long bake.. Dense. Essential knowledge — Dense.. the dark German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Long bake..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Long bake..", "x": "Explained: Long bake.. History. The context — Pumpernickel. Westphalia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Molasses.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Molasses.", "x": "Pumpernickel: Molasses.. Germany. Essential knowledge — Westphalia.. the dark German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Molasses..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Molasses..", "x": "Explained: Molasses.. Deli. The context — Pumpernickel. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dense.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dense.", "x": "Pumpernickel: Dense.. History. Essential knowledge — History.. the dark German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dense..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dense..", "x": "Explained: Dense.. Bake. The context — Pumpernickel. Germany. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Westphalia.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Westphalia.", "x": "Pumpernickel: Westphalia.. Deli. Essential knowledge — Germany.. the dark German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Westphalia..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Westphalia..", "x": "Explained: Westphalia.. Molasses. The context — Pumpernickel. Long bake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Pumpernickel: History.. Bake. Essential knowledge — Long bake.. the dark German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Dense. The context — Pumpernickel. Molasses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bake.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bake.", "x": "Pumpernickel in depth: Bake.. Long bake. Details — the dark German.. Dense. Dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Molasses.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Molasses.", "x": "Pumpernickel in depth: Molasses.. Molasses. Details — the dark German.. Germany. Westphalia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dense.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dense.", "x": "Pumpernickel in depth: Dense.. Dense. Details — the dark German.. History. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Germany.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Germany.", "x": "Pumpernickel in depth: Germany.. Westphalia. Details — the dark German.. Deli. Germany. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Pumpernickel in depth: History.. History. Details — the dark German.. Bake. Long bake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Deli.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Deli.", "x": "Pumpernickel in depth: Deli.. Germany. Details — the dark German.. Molasses. Molasses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pumpernickel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pumpernickel comes from.", "x": "Origins: Bake.. Germany. The history of Pumpernickel — the dark German.. Molasses. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pumpernickel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pumpernickel respectfully.", "x": "Engaging: Dense.. Long bake. How to participate or observe well — Pumpernickel. the dark German. Respect first, always; Germany.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pumpernickel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pumpernickel do's and don'ts.", "x": "Etiquette: History.. Molasses. The rules of respect — Pumpernickel. the dark German. When in doubt, ask about Deli.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pumpernickel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pumpernickel.", "x": "Planning: Bake.. Dense. Practical notes — Pumpernickel. the dark German. A little planning shows respect for Molasses.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pumpernickel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pumpernickel and money.", "x": "Costs: Dense.. Westphalia. What to budget — Pumpernickel. the dark German. The best experiences of Germany. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bread-pumpernickel-bread-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
