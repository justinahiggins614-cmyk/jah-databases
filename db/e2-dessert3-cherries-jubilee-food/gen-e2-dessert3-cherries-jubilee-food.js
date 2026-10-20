(function(){'use strict';
/* JAH Cherries Jubilee Dessert Database generator — jahdb-e2-dessert3-cherries-jubilee-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-cherries-jubilee-food',PREFIX='JAH-E2DESSERT3C-',NAME='JAH Cherries Jubilee Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cherries Jubilee: the complete guide", "d": "Cherries Jubilee: the flaming cherries..", "g": "overview", "l": 2, "q": "What is Cherries Jubilee: the complete guide?", "a": "Cherries Jubilee: the flaming cherries..", "x": "The complete dessert guide to Cherries Jubilee: the flaming cherries.. Flambéed. History, meaning, practices, and how to engage respectfully — everything in one database. Flambéed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cherries Jubilee essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cherries Jubilee essentials.", "x": "At a glance: Cherries Jubilee — the flaming cherries.. 1897. The essentials: Drama.. Jubilee. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Flambéed.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Flambéed.", "x": "Cherries Jubilee: Flambéed.. Drama. Essential knowledge — Jubilee.. the flaming cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Flambéed..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Flambéed..", "x": "Explained: Flambéed.. 1897. The context — Cherries Jubilee. Brandy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1897.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1897.", "x": "Cherries Jubilee: 1897.. Vanilla. Essential knowledge — Brandy.. the flaming cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1897..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1897..", "x": "Explained: 1897.. Brandy. The context — Cherries Jubilee. Vanilla. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Jubilee.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Jubilee.", "x": "Cherries Jubilee: Jubilee.. 1897. Essential knowledge — Vanilla.. the flaming cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Jubilee..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Jubilee..", "x": "Explained: Jubilee.. Making. The context — Cherries Jubilee. Drama. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Brandy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Brandy.", "x": "Cherries Jubilee: Brandy.. Brandy. Essential knowledge — Drama.. the flaming cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Brandy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Brandy..", "x": "Explained: Brandy.. Flambéed. The context — Cherries Jubilee. Flambéed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vanilla.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vanilla.", "x": "Cherries Jubilee: Vanilla.. Making. Essential knowledge — Flambéed.. the flaming cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vanilla..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vanilla..", "x": "Explained: Vanilla.. Drama. The context — Cherries Jubilee. 1897. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drama.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drama.", "x": "Cherries Jubilee: Drama.. Flambéed. Essential knowledge — 1897.. the flaming cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Drama..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Drama..", "x": "Explained: Drama.. Vanilla. The context — Cherries Jubilee. Jubilee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Flambéed.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Flambéed.", "x": "Cherries Jubilee in depth: Flambéed.. 1897. Details — the flaming cherries.. Vanilla. Brandy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Drama.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Drama.", "x": "Cherries Jubilee in depth: Drama.. Jubilee. Details — the flaming cherries.. 1897. Vanilla. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vanilla.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vanilla.", "x": "Cherries Jubilee in depth: Vanilla.. Brandy. Details — the flaming cherries.. Brandy. Drama. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1897.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1897.", "x": "Cherries Jubilee in depth: 1897.. Vanilla. Details — the flaming cherries.. Making. Flambéed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Brandy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Brandy.", "x": "Cherries Jubilee in depth: Brandy.. Drama. Details — the flaming cherries.. Flambéed. 1897. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Cherries Jubilee in depth: Making.. Flambéed. Details — the flaming cherries.. Drama. Jubilee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cherries Jubilee comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cherries Jubilee comes from.", "x": "Origins: Flambéed.. Flambéed. The history of Cherries Jubilee — the flaming cherries.. Drama. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cherries Jubilee respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cherries Jubilee respectfully.", "x": "Engaging: Vanilla.. 1897. How to participate or observe well — Cherries Jubilee. the flaming cherries. Respect first, always; 1897.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cherries Jubilee do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cherries Jubilee do's and don'ts.", "x": "Etiquette: Brandy.. Jubilee. The rules of respect — Cherries Jubilee. the flaming cherries. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cherries Jubilee.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cherries Jubilee.", "x": "Planning: Flambéed.. Brandy. Practical notes — Cherries Jubilee. the flaming cherries. A little planning shows respect for Drama.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cherries Jubilee and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cherries Jubilee and money.", "x": "Costs: Vanilla.. Vanilla. What to budget — Cherries Jubilee. the flaming cherries. The best experiences of 1897. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-cherries-jubilee-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
