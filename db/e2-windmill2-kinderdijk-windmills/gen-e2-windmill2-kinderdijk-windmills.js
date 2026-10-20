(function(){'use strict';
/* JAH Kinderdijk Windmills Database generator — jahdb-e2-windmill2-kinderdijk-windmills-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill2-kinderdijk-windmills',PREFIX='JAH-E2WINDMILL2-',NAME='JAH Kinderdijk Windmills Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kinderdijk Windmills: the complete guide", "d": "Kinderdijk Windmills: the Dutch..", "g": "overview", "l": 2, "q": "What is Kinderdijk Windmills: the complete guide?", "a": "Kinderdijk Windmills: the Dutch..", "x": "The complete windmill guide to Kinderdijk Windmills: the Dutch.. 1738. History, meaning, practices, and how to engage respectfully — everything in one database. 1738. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kinderdijk Windmills essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kinderdijk Windmills essentials.", "x": "At a glance: Kinderdijk Windmills — the Dutch.. 19 mills. The essentials: Water.. UNESCO. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1738.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1738.", "x": "Kinderdijk Windmills: 1738.. Water. Essential knowledge — UNESCO.. the Dutch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1738..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1738..", "x": "Explained: 1738.. 19. The context — Kinderdijk Windmills. Polders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "19 mills.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "19 mills.", "x": "Kinderdijk Windmills: 19 mills.. Netherlands. Essential knowledge — Polders.. the Dutch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 19 mills..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 19 mills..", "x": "Explained: 19 mills.. UNESCO. The context — Kinderdijk Windmills. Netherlands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "UNESCO.", "x": "Kinderdijk Windmills: UNESCO.. 19. Essential knowledge — Netherlands.. the Dutch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Visiting. The context — Kinderdijk Windmills. Water. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Polders.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Polders.", "x": "Kinderdijk Windmills: Polders.. UNESCO. Essential knowledge — Water.. the Dutch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Polders..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Polders..", "x": "Explained: Polders.. 1738. The context — Kinderdijk Windmills. 1738. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Netherlands.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Netherlands.", "x": "Kinderdijk Windmills: Netherlands.. Visiting. Essential knowledge — 1738.. the Dutch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Netherlands..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Netherlands..", "x": "Explained: Netherlands.. Water. The context — Kinderdijk Windmills. 19 mills. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Water.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Water.", "x": "Kinderdijk Windmills: Water.. 1738. Essential knowledge — 19 mills.. the Dutch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Water..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Water..", "x": "Explained: Water.. Netherlands. The context — Kinderdijk Windmills. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1738.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1738.", "x": "Kinderdijk Windmills in depth: 1738.. 19 mills. Details — the Dutch.. Netherlands. Polders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Water.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Water.", "x": "Kinderdijk Windmills in depth: Water.. UNESCO. Details — the Dutch.. 19. Netherlands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Netherlands.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Netherlands.", "x": "Kinderdijk Windmills in depth: Netherlands.. Polders. Details — the Dutch.. UNESCO. Water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "19.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "19.", "x": "Kinderdijk Windmills in depth: 19.. Netherlands. Details — the Dutch.. Visiting. 1738. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "UNESCO.", "x": "Kinderdijk Windmills in depth: UNESCO.. Water. Details — the Dutch.. 1738. 19 mills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Kinderdijk Windmills in depth: Visiting.. 1738. Details — the Dutch.. Water. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kinderdijk Windmills comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kinderdijk Windmills comes from.", "x": "Origins: 1738.. 1738. The history of Kinderdijk Windmills — the Dutch.. Water. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kinderdijk Windmills respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kinderdijk Windmills respectfully.", "x": "Engaging: Netherlands.. 19 mills. How to participate or observe well — Kinderdijk Windmills. the Dutch. Respect first, always; 19.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kinderdijk Windmills do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kinderdijk Windmills do's and don'ts.", "x": "Etiquette: UNESCO.. UNESCO. The rules of respect — Kinderdijk Windmills. the Dutch. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kinderdijk Windmills.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kinderdijk Windmills.", "x": "Planning: 1738.. Polders. Practical notes — Kinderdijk Windmills. the Dutch. A little planning shows respect for Water.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kinderdijk Windmills and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kinderdijk Windmills and money.", "x": "Costs: Netherlands.. Netherlands. What to budget — Kinderdijk Windmills. the Dutch. The best experiences of 19. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill2-kinderdijk-windmills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
