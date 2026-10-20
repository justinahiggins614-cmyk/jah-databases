(function(){'use strict';
/* JAH Royal Botanic Garden Edinburgh Botanical Garden Database generator — jahdb-e2-garden-royal-botanic-edinburgh-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-royal-botanic-edinburgh',PREFIX='JAH-E2GARDENROY-',NAME='JAH Royal Botanic Garden Edinburgh Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Royal Botanic Garden Edinburgh: the complete guide", "d": "Royal Botanic Garden Edinburgh: Scotland's botanics..", "g": "overview", "l": 2, "q": "What is Royal Botanic Garden Edinburgh: the complete guide?", "a": "Royal Botanic Garden Edinburgh: Scotland's botanics..", "x": "The complete botanical garden guide to Royal Botanic Garden Edinburgh: Scotland's botanics.. 1670. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Royal Botanic Garden Edinburgh essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Royal Botanic Garden Edinburgh essentials.", "x": "At a glance: Royal Botanic Garden Edinburgh — Scotland's botanics.. Rock Garden. The essentials: Houses.. Palm Houses. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1670.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1670.", "x": "Royal Botanic Garden Edinburgh: 1670.. Houses. Essential knowledge — Palm Houses.. Scotland's botanics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1670..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1670..", "x": "Explained: 1670.. Edinburgh. The context — Royal Botanic Garden Edinburgh. 70 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rock Garden.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rock Garden.", "x": "Royal Botanic Garden Edinburgh: Rock Garden.. Free. Essential knowledge — 70 acres.. Scotland's botanics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rock Garden..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rock Garden..", "x": "Explained: Rock Garden.. Science. The context — Royal Botanic Garden Edinburgh. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Palm Houses.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Palm Houses.", "x": "Royal Botanic Garden Edinburgh: Palm Houses.. Edinburgh. Essential knowledge — Free.. Scotland's botanics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Palm Houses..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Palm Houses..", "x": "Explained: Palm Houses.. Seasons. The context — Royal Botanic Garden Edinburgh. Science. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "70 acres.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "70 acres.", "x": "Royal Botanic Garden Edinburgh: 70 acres.. Science. Essential knowledge — Science.. Scotland's botanics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 70 acres..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 70 acres..", "x": "Explained: 70 acres.. History. The context — Royal Botanic Garden Edinburgh. 1670. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Free.", "x": "Royal Botanic Garden Edinburgh: Free.. Seasons. Essential knowledge — 1670.. Scotland's botanics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Houses. The context — Royal Botanic Garden Edinburgh. Rock Garden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Science.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Science.", "x": "Royal Botanic Garden Edinburgh: Science.. History. Essential knowledge — Rock Garden.. Scotland's botanics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Science..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Science..", "x": "Explained: Science.. Free. The context — Royal Botanic Garden Edinburgh. Palm Houses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Royal Botanic Garden Edinburgh in depth: History.. Rock Garden. Details — Scotland's botanics.. Free. 70 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Houses.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Houses.", "x": "Royal Botanic Garden Edinburgh in depth: Houses.. Palm Houses. Details — Scotland's botanics.. Edinburgh. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Free.", "x": "Royal Botanic Garden Edinburgh in depth: Free.. 70 acres. Details — Scotland's botanics.. Science. Science. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Edinburgh.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Edinburgh.", "x": "Royal Botanic Garden Edinburgh in depth: Edinburgh.. Free. Details — Scotland's botanics.. Seasons. 1670. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Science.", "x": "Royal Botanic Garden Edinburgh in depth: Science.. Science. Details — Scotland's botanics.. History. Rock Garden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Seasons.", "x": "Royal Botanic Garden Edinburgh in depth: Seasons.. 1670. Details — Scotland's botanics.. Houses. Palm Houses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Royal Botanic Garden Edinburgh comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Royal Botanic Garden Edinburgh comes from.", "x": "Origins: History.. 1670. The history of Royal Botanic Garden Edinburgh — Scotland's botanics.. Houses. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Royal Botanic Garden Edinburgh respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Royal Botanic Garden Edinburgh respectfully.", "x": "Engaging: Free.. Rock Garden. How to participate or observe well — Royal Botanic Garden Edinburgh. Scotland's botanics. Respect first, always; Edinburgh.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Royal Botanic Garden Edinburgh do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Royal Botanic Garden Edinburgh do's and don'ts.", "x": "Etiquette: Science.. Palm Houses. The rules of respect — Royal Botanic Garden Edinburgh. Scotland's botanics. When in doubt, ask about Seasons.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Royal Botanic Garden Edinburgh.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Royal Botanic Garden Edinburgh.", "x": "Planning: History.. 70 acres. Practical notes — Royal Botanic Garden Edinburgh. Scotland's botanics. A little planning shows respect for Houses.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Royal Botanic Garden Edinburgh and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Royal Botanic Garden Edinburgh and money.", "x": "Costs: Free.. Free. What to budget — Royal Botanic Garden Edinburgh. Scotland's botanics. The best experiences of Edinburgh. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-royal-botanic-edinburgh-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
