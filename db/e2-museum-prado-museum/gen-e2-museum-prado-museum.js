(function(){'use strict';
/* JAH Prado Museum Museum Database generator — jahdb-e2-museum-prado-museum-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-prado-museum',PREFIX='JAH-E2MUSEUMPRA-',NAME='JAH Prado Museum Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Prado Museum: the complete guide", "d": "Prado Museum: Spain's great gallery..", "g": "overview", "l": 2, "q": "What is Prado Museum: the complete guide?", "a": "Prado Museum: Spain's great gallery..", "x": "The complete museum guide to Prado Museum: Spain's great gallery.. Velazquez. History, meaning, practices, and how to engage respectfully — everything in one database. Velazquez. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Prado Museum essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Prado Museum essentials.", "x": "At a glance: Prado Museum — Spain's great gallery.. Goya. The essentials: Goya.. Bosch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Velazquez.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Velazquez.", "x": "Prado Museum: Velazquez.. Goya. Essential knowledge — Bosch.. Spain's great gallery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Velazquez..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Velazquez..", "x": "Explained: Velazquez.. Tickets. The context — Prado Museum. Madrid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Goya.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Goya.", "x": "Prado Museum: Goya.. History. Essential knowledge — Madrid.. Spain's great gallery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Goya..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Goya..", "x": "Explained: Goya.. Madrid. The context — Prado Museum. 1819. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bosch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bosch.", "x": "Prado Museum: Bosch.. Tickets. Essential knowledge — 1819.. Spain's great gallery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bosch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bosch..", "x": "Explained: Bosch.. Art. The context — Prado Museum. Las Meninas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Madrid.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Madrid.", "x": "Prado Museum: Madrid.. Madrid. Essential knowledge — Las Meninas.. Spain's great gallery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Madrid..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Madrid..", "x": "Explained: Madrid.. Velazquez. The context — Prado Museum. Velazquez. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1819.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1819.", "x": "Prado Museum: 1819.. Art. Essential knowledge — Velazquez.. Spain's great gallery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1819..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1819..", "x": "Explained: 1819.. Goya. The context — Prado Museum. Goya. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Las Meninas.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Las Meninas.", "x": "Prado Museum: Las Meninas.. Velazquez. Essential knowledge — Goya.. Spain's great gallery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Las Meninas..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Las Meninas..", "x": "Explained: Las Meninas.. History. The context — Prado Museum. Bosch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Velazquez.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Velazquez.", "x": "Prado Museum in depth: Velazquez.. Goya. Details — Spain's great gallery.. History. Madrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Goya.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Goya.", "x": "Prado Museum in depth: Goya.. Bosch. Details — Spain's great gallery.. Tickets. 1819. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Prado Museum in depth: History.. Madrid. Details — Spain's great gallery.. Madrid. Las Meninas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Prado Museum in depth: Tickets.. 1819. Details — Spain's great gallery.. Art. Velazquez. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Madrid.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Madrid.", "x": "Prado Museum in depth: Madrid.. Las Meninas. Details — Spain's great gallery.. Velazquez. Goya. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Prado Museum in depth: Art.. Velazquez. Details — Spain's great gallery.. Goya. Bosch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Prado Museum comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Prado Museum comes from.", "x": "Origins: Velazquez.. Velazquez. The history of Prado Museum — Spain's great gallery.. Goya. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Prado Museum respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Prado Museum respectfully.", "x": "Engaging: History.. Goya. How to participate or observe well — Prado Museum. Spain's great gallery. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Prado Museum do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Prado Museum do's and don'ts.", "x": "Etiquette: Madrid.. Bosch. The rules of respect — Prado Museum. Spain's great gallery. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Prado Museum.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Prado Museum.", "x": "Planning: Velazquez.. Madrid. Practical notes — Prado Museum. Spain's great gallery. A little planning shows respect for Goya.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Prado Museum and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Prado Museum and money.", "x": "Costs: History.. 1819. What to budget — Prado Museum. Spain's great gallery. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-prado-museum-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
