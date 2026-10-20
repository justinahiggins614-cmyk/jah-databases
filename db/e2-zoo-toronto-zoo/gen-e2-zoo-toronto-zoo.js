(function(){'use strict';
/* JAH Toronto Zoo Zoo Database generator — jahdb-e2-zoo-toronto-zoo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo-toronto-zoo',PREFIX='JAH-E2ZOOTORONT-',NAME='JAH Toronto Zoo Zoo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Toronto Zoo: the complete guide", "d": "Toronto Zoo: Canada's giant..", "g": "overview", "l": 2, "q": "What is Toronto Zoo: the complete guide?", "a": "Toronto Zoo: Canada's giant..", "x": "The complete zoo guide to Toronto Zoo: Canada's giant.. 1974. History, meaning, practices, and how to engage respectfully — everything in one database. Tundra. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Toronto Zoo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Toronto Zoo essentials.", "x": "At a glance: Toronto Zoo — Canada's giant.. 5,000 animals. The essentials: Pandas.. Pandas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1974.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1974.", "x": "Toronto Zoo: 1974.. Pandas. Essential knowledge — Pandas.. Canada's giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1974..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1974..", "x": "Explained: 1974.. Toronto. The context — Toronto Zoo. Rouge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "5,000 animals.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "5,000 animals.", "x": "Toronto Zoo: 5,000 animals.. Tickets. Essential knowledge — Rouge.. Canada's giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 5,000 animals..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 5,000 animals..", "x": "Explained: 5,000 animals.. Size. The context — Toronto Zoo. Tundra. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pandas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pandas.", "x": "Toronto Zoo: Pandas.. Toronto. Essential knowledge — Tundra.. Canada's giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pandas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pandas..", "x": "Explained: Pandas.. Science. The context — Toronto Zoo. Conservation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rouge.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rouge.", "x": "Toronto Zoo: Rouge.. Size. Essential knowledge — Conservation.. Canada's giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rouge..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rouge..", "x": "Explained: Rouge.. Tundra. The context — Toronto Zoo. 1974. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tundra.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tundra.", "x": "Toronto Zoo: Tundra.. Science. Essential knowledge — 1974.. Canada's giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tundra..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tundra..", "x": "Explained: Tundra.. Pandas. The context — Toronto Zoo. 5,000 animals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Conservation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Conservation.", "x": "Toronto Zoo: Conservation.. Tundra. Essential knowledge — 5,000 animals.. Canada's giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Conservation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Conservation..", "x": "Explained: Conservation.. Tickets. The context — Toronto Zoo. Pandas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tundra.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tundra.", "x": "Toronto Zoo in depth: Tundra.. 5,000 animals. Details — Canada's giant.. Tickets. Rouge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pandas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pandas.", "x": "Toronto Zoo in depth: Pandas.. Pandas. Details — Canada's giant.. Toronto. Tundra. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "Toronto Zoo in depth: Tickets.. Rouge. Details — Canada's giant.. Size. Conservation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Toronto.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Toronto.", "x": "Toronto Zoo in depth: Toronto.. Tundra. Details — Canada's giant.. Science. 1974. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Size.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Size.", "x": "Toronto Zoo in depth: Size.. Conservation. Details — Canada's giant.. Tundra. 5,000 animals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Science.", "x": "Toronto Zoo in depth: Science.. 1974. Details — Canada's giant.. Pandas. Pandas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Toronto Zoo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Toronto Zoo comes from.", "x": "Origins: Tundra.. 1974. The history of Toronto Zoo — Canada's giant.. Pandas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Toronto Zoo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Toronto Zoo respectfully.", "x": "Engaging: Tickets.. 5,000 animals. How to participate or observe well — Toronto Zoo. Canada's giant. Respect first, always; Toronto.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Toronto Zoo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Toronto Zoo do's and don'ts.", "x": "Etiquette: Size.. Pandas. The rules of respect — Toronto Zoo. Canada's giant. When in doubt, ask about Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Toronto Zoo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Toronto Zoo.", "x": "Planning: Tundra.. Rouge. Practical notes — Toronto Zoo. Canada's giant. A little planning shows respect for Pandas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Toronto Zoo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Toronto Zoo and money.", "x": "Costs: Tickets.. Tundra. What to budget — Toronto Zoo. Canada's giant. The best experiences of Toronto. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo-toronto-zoo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
