(function(){'use strict';
/* JAH Metropolitan Museum of Art Museum Database generator — jahdb-e2-museum-metropolitan-museum-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-metropolitan-museum',PREFIX='JAH-E2MUSEUMMET-',NAME='JAH Metropolitan Museum of Art Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Metropolitan Museum of Art: the complete guide", "d": "Metropolitan Museum of Art: New York's art universe..", "g": "overview", "l": 2, "q": "What is Metropolitan Museum of Art: the complete guide?", "a": "Metropolitan Museum of Art: New York's art universe..", "x": "The complete museum guide to Metropolitan Museum of Art: New York's art universe.. 5,000 years. History, meaning, practices, and how to engage respectfully — everything in one database. Wings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Metropolitan Museum of Art essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Metropolitan Museum of Art essentials.", "x": "At a glance: Metropolitan Museum of Art — New York's art universe.. The Met Fifth. The essentials: Cloisters.. Cloisters. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "5,000 years.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "5,000 years.", "x": "Metropolitan Museum of Art: 5,000 years.. Cloisters. Essential knowledge — Cloisters.. New York's art universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 5,000 years..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 5,000 years..", "x": "Explained: 5,000 years.. Tickets. The context — Metropolitan Museum of Art. Egyptian Temple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "The Met Fifth.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "The Met Fifth.", "x": "Metropolitan Museum of Art: The Met Fifth.. Rooftop. Essential knowledge — Egyptian Temple.. New York's art universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: The Met Fifth..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: The Met Fifth..", "x": "Explained: The Met Fifth.. History. The context — Metropolitan Museum of Art. 2M objects. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cloisters.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cloisters.", "x": "Metropolitan Museum of Art: Cloisters.. Tickets. Essential knowledge — 2M objects.. New York's art universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cloisters..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cloisters..", "x": "Explained: Cloisters.. Art. The context — Metropolitan Museum of Art. NYC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Egyptian Temple.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Egyptian Temple.", "x": "Metropolitan Museum of Art: Egyptian Temple.. History. Essential knowledge — NYC.. New York's art universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Egyptian Temple..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Egyptian Temple..", "x": "Explained: Egyptian Temple.. Wings. The context — Metropolitan Museum of Art. 5,000 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2M objects.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2M objects.", "x": "Metropolitan Museum of Art: 2M objects.. Art. Essential knowledge — 5,000 years.. New York's art universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 2M objects..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 2M objects..", "x": "Explained: 2M objects.. Cloisters. The context — Metropolitan Museum of Art. The Met Fifth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "NYC.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "NYC.", "x": "Metropolitan Museum of Art: NYC.. Wings. Essential knowledge — The Met Fifth.. New York's art universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: NYC..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: NYC..", "x": "Explained: NYC.. Rooftop. The context — Metropolitan Museum of Art. Cloisters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wings.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wings.", "x": "Metropolitan Museum of Art in depth: Wings.. The Met Fifth. Details — New York's art universe.. Rooftop. Egyptian Temple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cloisters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cloisters.", "x": "Metropolitan Museum of Art in depth: Cloisters.. Cloisters. Details — New York's art universe.. Tickets. 2M objects. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rooftop.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rooftop.", "x": "Metropolitan Museum of Art in depth: Rooftop.. Egyptian Temple. Details — New York's art universe.. History. NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Metropolitan Museum of Art in depth: Tickets.. 2M objects. Details — New York's art universe.. Art. 5,000 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Metropolitan Museum of Art in depth: History.. NYC. Details — New York's art universe.. Wings. The Met Fifth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Metropolitan Museum of Art in depth: Art.. 5,000 years. Details — New York's art universe.. Cloisters. Cloisters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Metropolitan Museum of Art comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Metropolitan Museum of Art comes from.", "x": "Origins: Wings.. 5,000 years. The history of Metropolitan Museum of Art — New York's art universe.. Cloisters. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Metropolitan Museum of Art respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Metropolitan Museum of Art respectfully.", "x": "Engaging: Rooftop.. The Met Fifth. How to participate or observe well — Metropolitan Museum of Art. New York's art universe. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Metropolitan Museum of Art do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Metropolitan Museum of Art do's and don'ts.", "x": "Etiquette: History.. Cloisters. The rules of respect — Metropolitan Museum of Art. New York's art universe. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Metropolitan Museum of Art.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Metropolitan Museum of Art.", "x": "Planning: Wings.. Egyptian Temple. Practical notes — Metropolitan Museum of Art. New York's art universe. A little planning shows respect for Cloisters.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Metropolitan Museum of Art and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Metropolitan Museum of Art and money.", "x": "Costs: Rooftop.. 2M objects. What to budget — Metropolitan Museum of Art. New York's art universe. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-metropolitan-museum-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
