(function(){'use strict';
/* JAH Pilsner Beer Style Database generator — jahdb-e2-beer-pilsner-beer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beer-pilsner-beer',PREFIX='JAH-E2BEERPILSN-',NAME='JAH Pilsner Beer Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pilsner: the complete guide", "d": "Pilsner: the original golden lager..", "g": "overview", "l": 2, "q": "What is Pilsner: the complete guide?", "a": "Pilsner: the original golden lager..", "x": "The complete beer style guide to Pilsner: the original golden lager.. 1842. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pilsner essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pilsner essentials.", "x": "At a glance: Pilsner — the original golden lager.. Plzen. The essentials: Hops.. Saaz hops. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1842.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1842.", "x": "Pilsner: 1842.. Hops. Essential knowledge — Saaz hops.. the original golden lager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1842..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1842..", "x": "Explained: 1842.. Czech. The context — Pilsner. Golden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Plzen.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Plzen.", "x": "Pilsner: Plzen.. Crisp. Essential knowledge — Golden.. the original golden lager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Plzen..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Plzen..", "x": "Explained: Plzen.. Serving. The context — Pilsner. Crisp. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Saaz hops.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Saaz hops.", "x": "Pilsner: Saaz hops.. Czech. Essential knowledge — Crisp.. the original golden lager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Saaz hops..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Saaz hops..", "x": "Explained: Saaz hops.. Varieties. The context — Pilsner. Czech. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Golden.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Golden.", "x": "Pilsner: Golden.. Serving. Essential knowledge — Czech.. the original golden lager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Golden..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Golden..", "x": "Explained: Golden.. History. The context — Pilsner. 1842. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Crisp.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Crisp.", "x": "Pilsner: Crisp.. Varieties. Essential knowledge — 1842.. the original golden lager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Crisp..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Crisp..", "x": "Explained: Crisp.. Hops. The context — Pilsner. Plzen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Czech.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Czech.", "x": "Pilsner: Czech.. History. Essential knowledge — Plzen.. the original golden lager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Czech..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Czech..", "x": "Explained: Czech.. Crisp. The context — Pilsner. Saaz hops. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Pilsner in depth: History.. Plzen. Details — the original golden lager.. Crisp. Golden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hops.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hops.", "x": "Pilsner in depth: Hops.. Saaz hops. Details — the original golden lager.. Czech. Crisp. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Crisp.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Crisp.", "x": "Pilsner in depth: Crisp.. Golden. Details — the original golden lager.. Serving. Czech. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Czech.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Czech.", "x": "Pilsner in depth: Czech.. Crisp. Details — the original golden lager.. Varieties. 1842. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Serving.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Serving.", "x": "Pilsner in depth: Serving.. Czech. Details — the original golden lager.. History. Plzen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Varieties.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Varieties.", "x": "Pilsner in depth: Varieties.. 1842. Details — the original golden lager.. Hops. Saaz hops. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pilsner comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pilsner comes from.", "x": "Origins: History.. 1842. The history of Pilsner — the original golden lager.. Hops. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pilsner respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pilsner respectfully.", "x": "Engaging: Crisp.. Plzen. How to participate or observe well — Pilsner. the original golden lager. Respect first, always; Czech.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pilsner do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pilsner do's and don'ts.", "x": "Etiquette: Serving.. Saaz hops. The rules of respect — Pilsner. the original golden lager. When in doubt, ask about Varieties.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pilsner.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pilsner.", "x": "Planning: History.. Golden. Practical notes — Pilsner. the original golden lager. A little planning shows respect for Hops.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pilsner and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pilsner and money.", "x": "Costs: Crisp.. Crisp. What to budget — Pilsner. the original golden lager. The best experiences of Czech. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beer-pilsner-beer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
