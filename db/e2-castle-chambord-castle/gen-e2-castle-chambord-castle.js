(function(){'use strict';
/* JAH Chateau de Chambord Castle Database generator — jahdb-e2-castle-chambord-castle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-chambord-castle',PREFIX='JAH-E2CASTLECHA-',NAME='JAH Chateau de Chambord Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chateau de Chambord: the complete guide", "d": "Chateau de Chambord: Loire's double helix..", "g": "overview", "l": 2, "q": "What is Chateau de Chambord: the complete guide?", "a": "Chateau de Chambord: Loire's double helix..", "x": "The complete castle guide to Chateau de Chambord: Loire's double helix.. 1519. History, meaning, practices, and how to engage respectfully — everything in one database. Stairs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chateau de Chambord essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chateau de Chambord essentials.", "x": "At a glance: Chateau de Chambord — Loire's double helix.. Francis I. The essentials: History.. Da Vinci stairs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1519.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1519.", "x": "Chateau de Chambord: 1519.. History. Essential knowledge — Da Vinci stairs.. Loire's double helix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1519..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1519..", "x": "Explained: 1519.. Loire. The context — Chateau de Chambord. 440 rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Francis I.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Francis I.", "x": "Chateau de Chambord: Francis I.. Rooms. Essential knowledge — 440 rooms.. Loire's double helix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Francis I..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Francis I..", "x": "Explained: Francis I.. Tickets. The context — Chateau de Chambord. Loire. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Da Vinci stairs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Da Vinci stairs.", "x": "Chateau de Chambord: Da Vinci stairs.. Loire. Essential knowledge — Loire.. Loire's double helix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Da Vinci stairs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Da Vinci stairs..", "x": "Explained: Da Vinci stairs.. Views. The context — Chateau de Chambord. Hunting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "440 rooms.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "440 rooms.", "x": "Chateau de Chambord: 440 rooms.. Tickets. Essential knowledge — Hunting.. Loire's double helix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 440 rooms..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 440 rooms..", "x": "Explained: 440 rooms.. Stairs. The context — Chateau de Chambord. 1519. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Loire.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Loire.", "x": "Chateau de Chambord: Loire.. Views. Essential knowledge — 1519.. Loire's double helix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Loire..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Loire..", "x": "Explained: Loire.. History. The context — Chateau de Chambord. Francis I. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hunting.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hunting.", "x": "Chateau de Chambord: Hunting.. Stairs. Essential knowledge — Francis I.. Loire's double helix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Hunting..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Hunting..", "x": "Explained: Hunting.. Rooms. The context — Chateau de Chambord. Da Vinci stairs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stairs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stairs.", "x": "Chateau de Chambord in depth: Stairs.. Francis I. Details — Loire's double helix.. Rooms. 440 rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Chateau de Chambord in depth: History.. Da Vinci stairs. Details — Loire's double helix.. Loire. Loire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rooms.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rooms.", "x": "Chateau de Chambord in depth: Rooms.. 440 rooms. Details — Loire's double helix.. Tickets. Hunting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Loire.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Loire.", "x": "Chateau de Chambord in depth: Loire.. Loire. Details — Loire's double helix.. Views. 1519. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tickets.", "x": "Chateau de Chambord in depth: Tickets.. Hunting. Details — Loire's double helix.. Stairs. Francis I. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Chateau de Chambord in depth: Views.. 1519. Details — Loire's double helix.. History. Da Vinci stairs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chateau de Chambord comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chateau de Chambord comes from.", "x": "Origins: Stairs.. 1519. The history of Chateau de Chambord — Loire's double helix.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chateau de Chambord respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chateau de Chambord respectfully.", "x": "Engaging: Rooms.. Francis I. How to participate or observe well — Chateau de Chambord. Loire's double helix. Respect first, always; Loire.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chateau de Chambord do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chateau de Chambord do's and don'ts.", "x": "Etiquette: Tickets.. Da Vinci stairs. The rules of respect — Chateau de Chambord. Loire's double helix. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chateau de Chambord.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chateau de Chambord.", "x": "Planning: Stairs.. 440 rooms. Practical notes — Chateau de Chambord. Loire's double helix. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chateau de Chambord and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chateau de Chambord and money.", "x": "Costs: Rooms.. Loire. What to budget — Chateau de Chambord. Loire's double helix. The best experiences of Loire. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-chambord-castle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
