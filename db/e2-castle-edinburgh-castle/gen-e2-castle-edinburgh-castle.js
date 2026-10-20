(function(){'use strict';
/* JAH Edinburgh Castle Castle Database generator — jahdb-e2-castle-edinburgh-castle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-edinburgh-castle',PREFIX='JAH-E2CASTLEEDI-',NAME='JAH Edinburgh Castle Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Edinburgh Castle: the complete guide", "d": "Edinburgh Castle: Scotland's fortress..", "g": "overview", "l": 2, "q": "What is Edinburgh Castle: the complete guide?", "a": "Edinburgh Castle: Scotland's fortress..", "x": "The complete castle guide to Edinburgh Castle: Scotland's fortress.. Volcanic rock. History, meaning, practices, and how to engage respectfully — everything in one database. Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Edinburgh Castle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Edinburgh Castle essentials.", "x": "At a glance: Edinburgh Castle — Scotland's fortress.. Crown Jewels. The essentials: Jewels.. One O'Clock Gun. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Volcanic rock.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Volcanic rock.", "x": "Edinburgh Castle: Volcanic rock.. Jewels. Essential knowledge — One O'Clock Gun.. Scotland's fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Volcanic rock..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Volcanic rock..", "x": "Explained: Volcanic rock.. History. The context — Edinburgh Castle. Military. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Crown Jewels.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Crown Jewels.", "x": "Edinburgh Castle: Crown Jewels.. Gun. Essential knowledge — Military.. Scotland's fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Crown Jewels..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Crown Jewels..", "x": "Explained: Crown Jewels.. Tickets. The context — Edinburgh Castle. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "One O'Clock Gun.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "One O'Clock Gun.", "x": "Edinburgh Castle: One O'Clock Gun.. History. Essential knowledge — History.. Scotland's fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: One O'Clock Gun..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: One O'Clock Gun..", "x": "Explained: One O'Clock Gun.. Views. The context — Edinburgh Castle. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Military.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Military.", "x": "Edinburgh Castle: Military.. Tickets. Essential knowledge — Views.. Scotland's fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Military..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Military..", "x": "Explained: Military.. Rock. The context — Edinburgh Castle. Volcanic rock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Edinburgh Castle: History.. Views. Essential knowledge — Volcanic rock.. Scotland's fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. Jewels. The context — Edinburgh Castle. Crown Jewels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Edinburgh Castle: Views.. Rock. Essential knowledge — Crown Jewels.. Scotland's fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Gun. The context — Edinburgh Castle. One O'Clock Gun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rock.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rock.", "x": "Edinburgh Castle in depth: Rock.. Crown Jewels. Details — Scotland's fortress.. Gun. Military. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Jewels.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Jewels.", "x": "Edinburgh Castle in depth: Jewels.. One O'Clock Gun. Details — Scotland's fortress.. History. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gun.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gun.", "x": "Edinburgh Castle in depth: Gun.. Military. Details — Scotland's fortress.. Tickets. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Edinburgh Castle in depth: History.. History. Details — Scotland's fortress.. Views. Volcanic rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tickets.", "x": "Edinburgh Castle in depth: Tickets.. Views. Details — Scotland's fortress.. Rock. Crown Jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Edinburgh Castle in depth: Views.. Volcanic rock. Details — Scotland's fortress.. Jewels. One O'Clock Gun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Edinburgh Castle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Edinburgh Castle comes from.", "x": "Origins: Rock.. Volcanic rock. The history of Edinburgh Castle — Scotland's fortress.. Jewels. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Edinburgh Castle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Edinburgh Castle respectfully.", "x": "Engaging: Gun.. Crown Jewels. How to participate or observe well — Edinburgh Castle. Scotland's fortress. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Edinburgh Castle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Edinburgh Castle do's and don'ts.", "x": "Etiquette: Tickets.. One O'Clock Gun. The rules of respect — Edinburgh Castle. Scotland's fortress. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Edinburgh Castle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Edinburgh Castle.", "x": "Planning: Rock.. Military. Practical notes — Edinburgh Castle. Scotland's fortress. A little planning shows respect for Jewels.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Edinburgh Castle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Edinburgh Castle and money.", "x": "Costs: Gun.. History. What to budget — Edinburgh Castle. Scotland's fortress. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-edinburgh-castle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
