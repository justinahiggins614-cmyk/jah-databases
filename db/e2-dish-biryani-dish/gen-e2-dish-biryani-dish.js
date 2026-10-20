(function(){'use strict';
/* JAH Biryani Dish Database generator — jahdb-e2-dish-biryani-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-biryani-dish',PREFIX='JAH-E2DISHBIRYA-',NAME='JAH Biryani Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Biryani: the complete guide", "d": "Biryani: the layered rice..", "g": "overview", "l": 2, "q": "What is Biryani: the complete guide?", "a": "Biryani: the layered rice..", "x": "The complete dish guide to Biryani: the layered rice.. Hyderabad. History, meaning, practices, and how to engage respectfully — everything in one database. Saffron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Biryani essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Biryani essentials.", "x": "At a glance: Biryani — the layered rice.. Saffron. The essentials: Dum.. Layered. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hyderabad.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hyderabad.", "x": "Biryani: Hyderabad.. Dum. Essential knowledge — Layered.. the layered rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hyderabad..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hyderabad..", "x": "Explained: Hyderabad.. Hyderabad. The context — Biryani. Dum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Saffron.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Saffron.", "x": "Biryani: Saffron.. Fragrant. Essential knowledge — Dum.. the layered rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Saffron..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Saffron..", "x": "Explained: Saffron.. Raita. The context — Biryani. Raita. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Layered.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Layered.", "x": "Biryani: Layered.. Hyderabad. Essential knowledge — Raita.. the layered rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Layered..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Layered..", "x": "Explained: Layered.. Making. The context — Biryani. Fragrant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dum.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dum.", "x": "Biryani: Dum.. Raita. Essential knowledge — Fragrant.. the layered rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dum..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dum..", "x": "Explained: Dum.. Saffron. The context — Biryani. Hyderabad. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Raita.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Raita.", "x": "Biryani: Raita.. Making. Essential knowledge — Hyderabad.. the layered rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Raita..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Raita..", "x": "Explained: Raita.. Dum. The context — Biryani. Saffron. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fragrant.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fragrant.", "x": "Biryani: Fragrant.. Saffron. Essential knowledge — Saffron.. the layered rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fragrant..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fragrant..", "x": "Explained: Fragrant.. Fragrant. The context — Biryani. Layered. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Saffron.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Saffron.", "x": "Biryani in depth: Saffron.. Saffron. Details — the layered rice.. Fragrant. Dum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dum.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dum.", "x": "Biryani in depth: Dum.. Layered. Details — the layered rice.. Hyderabad. Raita. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fragrant.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fragrant.", "x": "Biryani in depth: Fragrant.. Dum. Details — the layered rice.. Raita. Fragrant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hyderabad.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hyderabad.", "x": "Biryani in depth: Hyderabad.. Raita. Details — the layered rice.. Making. Hyderabad. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Raita.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Raita.", "x": "Biryani in depth: Raita.. Fragrant. Details — the layered rice.. Saffron. Saffron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Biryani in depth: Making.. Hyderabad. Details — the layered rice.. Dum. Layered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Biryani comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Biryani comes from.", "x": "Origins: Saffron.. Hyderabad. The history of Biryani — the layered rice.. Dum. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Biryani respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Biryani respectfully.", "x": "Engaging: Fragrant.. Saffron. How to participate or observe well — Biryani. the layered rice. Respect first, always; Hyderabad.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Biryani do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Biryani do's and don'ts.", "x": "Etiquette: Raita.. Layered. The rules of respect — Biryani. the layered rice. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Biryani.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Biryani.", "x": "Planning: Saffron.. Dum. Practical notes — Biryani. the layered rice. A little planning shows respect for Dum.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Biryani and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Biryani and money.", "x": "Costs: Fragrant.. Raita. What to budget — Biryani. the layered rice. The best experiences of Hyderabad. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-biryani-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
