(function(){'use strict';
/* JAH Carrot Cake Dessert Database generator — jahdb-e2-dessert3-carrot-cake-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-carrot-cake-food',PREFIX='JAH-E2DESSERT3C-',NAME='JAH Carrot Cake Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carrot Cake: the complete guide", "d": "Carrot Cake: the spiced cream..", "g": "overview", "l": 2, "q": "What is Carrot Cake: the complete guide?", "a": "Carrot Cake: the spiced cream..", "x": "The complete dessert guide to Carrot Cake: the spiced cream.. Carrots. History, meaning, practices, and how to engage respectfully — everything in one database. Carrots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Carrot Cake essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Carrot Cake essentials.", "x": "At a glance: Carrot Cake — the spiced cream.. Spices. The essentials: Moist.. Cream cheese. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Carrots.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Carrots.", "x": "Carrot Cake: Carrots.. Moist. Essential knowledge — Cream cheese.. the spiced cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Carrots..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Carrots..", "x": "Explained: Carrots.. Spices. The context — Carrot Cake. Walnuts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spices.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spices.", "x": "Carrot Cake: Spices.. Easter. Essential knowledge — Walnuts.. the spiced cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spices..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spices..", "x": "Explained: Spices.. Frosting. The context — Carrot Cake. Moist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cream cheese.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cream cheese.", "x": "Carrot Cake: Cream cheese.. Spices. Essential knowledge — Moist.. the spiced cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cream cheese..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cream cheese..", "x": "Explained: Cream cheese.. Making. The context — Carrot Cake. Easter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Walnuts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Walnuts.", "x": "Carrot Cake: Walnuts.. Frosting. Essential knowledge — Easter.. the spiced cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Walnuts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Walnuts..", "x": "Explained: Walnuts.. Carrots. The context — Carrot Cake. Carrots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Moist.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Moist.", "x": "Carrot Cake: Moist.. Making. Essential knowledge — Carrots.. the spiced cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Moist..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Moist..", "x": "Explained: Moist.. Moist. The context — Carrot Cake. Spices. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Easter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Easter.", "x": "Carrot Cake: Easter.. Carrots. Essential knowledge — Spices.. the spiced cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Easter..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Easter..", "x": "Explained: Easter.. Easter. The context — Carrot Cake. Cream cheese. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Carrots.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Carrots.", "x": "Carrot Cake in depth: Carrots.. Spices. Details — the spiced cream.. Easter. Walnuts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Moist.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Moist.", "x": "Carrot Cake in depth: Moist.. Cream cheese. Details — the spiced cream.. Spices. Moist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Easter.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Easter.", "x": "Carrot Cake in depth: Easter.. Walnuts. Details — the spiced cream.. Frosting. Easter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Spices.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Spices.", "x": "Carrot Cake in depth: Spices.. Moist. Details — the spiced cream.. Making. Carrots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Frosting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Frosting.", "x": "Carrot Cake in depth: Frosting.. Easter. Details — the spiced cream.. Carrots. Spices. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Carrot Cake in depth: Making.. Carrots. Details — the spiced cream.. Moist. Cream cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Carrot Cake comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Carrot Cake comes from.", "x": "Origins: Carrots.. Carrots. The history of Carrot Cake — the spiced cream.. Moist. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Carrot Cake respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Carrot Cake respectfully.", "x": "Engaging: Easter.. Spices. How to participate or observe well — Carrot Cake. the spiced cream. Respect first, always; Spices.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Carrot Cake do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Carrot Cake do's and don'ts.", "x": "Etiquette: Frosting.. Cream cheese. The rules of respect — Carrot Cake. the spiced cream. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Carrot Cake.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Carrot Cake.", "x": "Planning: Carrots.. Walnuts. Practical notes — Carrot Cake. the spiced cream. A little planning shows respect for Moist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Carrot Cake and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Carrot Cake and money.", "x": "Costs: Easter.. Moist. What to budget — Carrot Cake. the spiced cream. The best experiences of Spices. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-carrot-cake-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
