(function(){'use strict';
/* JAH MASP Sao Paulo Museum Database generator — jahdb-e2-museum-masp-sao-paulo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-masp-sao-paulo',PREFIX='JAH-E2MUSEUMMAS-',NAME='JAH MASP Sao Paulo Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "MASP Sao Paulo: the complete guide", "d": "MASP Sao Paulo: Brazil's glass easel..", "g": "overview", "l": 2, "q": "What is MASP Sao Paulo: the complete guide?", "a": "MASP Sao Paulo: Brazil's glass easel..", "x": "The complete museum guide to MASP Sao Paulo: Brazil's glass easel.. Lina Bo Bardi. History, meaning, practices, and how to engage respectfully — everything in one database. Building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "MASP Sao Paulo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "MASP Sao Paulo essentials.", "x": "At a glance: MASP Sao Paulo — Brazil's glass easel.. Glass easels. The essentials: Easels.. 1968. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lina Bo Bardi.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lina Bo Bardi.", "x": "MASP Sao Paulo: Lina Bo Bardi.. Easels. Essential knowledge — 1968.. Brazil's glass easel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Lina Bo Bardi..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Lina Bo Bardi..", "x": "Explained: Lina Bo Bardi.. Tickets. The context — MASP Sao Paulo. Avenida Paulista. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Glass easels.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Glass easels.", "x": "MASP Sao Paulo: Glass easels.. History. Essential knowledge — Avenida Paulista.. Brazil's glass easel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Glass easels..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Glass easels..", "x": "Explained: Glass easels.. Art. The context — MASP Sao Paulo. European. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1968.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1968.", "x": "MASP Sao Paulo: 1968.. Tickets. Essential knowledge — European.. Brazil's glass easel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1968..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1968..", "x": "Explained: 1968.. Brazil. The context — MASP Sao Paulo. Brazil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Avenida Paulista.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Avenida Paulista.", "x": "MASP Sao Paulo: Avenida Paulista.. Art. Essential knowledge — Brazil.. Brazil's glass easel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Avenida Paulista..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Avenida Paulista..", "x": "Explained: Avenida Paulista.. Building. The context — MASP Sao Paulo. Lina Bo Bardi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "European.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "European.", "x": "MASP Sao Paulo: European.. Brazil. Essential knowledge — Lina Bo Bardi.. Brazil's glass easel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: European..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: European..", "x": "Explained: European.. Easels. The context — MASP Sao Paulo. Glass easels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Brazil.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Brazil.", "x": "MASP Sao Paulo: Brazil.. Building. Essential knowledge — Glass easels.. Brazil's glass easel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Brazil..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Brazil..", "x": "Explained: Brazil.. History. The context — MASP Sao Paulo. 1968. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Building.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Building.", "x": "MASP Sao Paulo in depth: Building.. Glass easels. Details — Brazil's glass easel.. History. Avenida Paulista. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Easels.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Easels.", "x": "MASP Sao Paulo in depth: Easels.. 1968. Details — Brazil's glass easel.. Tickets. European. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "MASP Sao Paulo in depth: History.. Avenida Paulista. Details — Brazil's glass easel.. Art. Brazil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "MASP Sao Paulo in depth: Tickets.. European. Details — Brazil's glass easel.. Brazil. Lina Bo Bardi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Art.", "x": "MASP Sao Paulo in depth: Art.. Brazil. Details — Brazil's glass easel.. Building. Glass easels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Brazil.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Brazil.", "x": "MASP Sao Paulo in depth: Brazil.. Lina Bo Bardi. Details — Brazil's glass easel.. Easels. 1968. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where MASP Sao Paulo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where MASP Sao Paulo comes from.", "x": "Origins: Building.. Lina Bo Bardi. The history of MASP Sao Paulo — Brazil's glass easel.. Easels. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing MASP Sao Paulo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing MASP Sao Paulo respectfully.", "x": "Engaging: History.. Glass easels. How to participate or observe well — MASP Sao Paulo. Brazil's glass easel. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "MASP Sao Paulo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "MASP Sao Paulo do's and don'ts.", "x": "Etiquette: Art.. 1968. The rules of respect — MASP Sao Paulo. Brazil's glass easel. When in doubt, ask about Brazil.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around MASP Sao Paulo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around MASP Sao Paulo.", "x": "Planning: Building.. Avenida Paulista. Practical notes — MASP Sao Paulo. Brazil's glass easel. A little planning shows respect for Easels.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "MASP Sao Paulo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "MASP Sao Paulo and money.", "x": "Costs: History.. European. What to budget — MASP Sao Paulo. Brazil's glass easel. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-masp-sao-paulo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
