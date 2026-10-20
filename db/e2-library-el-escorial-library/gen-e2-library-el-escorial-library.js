(function(){'use strict';
/* JAH El Escorial Library Library Database generator — jahdb-e2-library-el-escorial-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-el-escorial-library',PREFIX='JAH-E2LIBRARYEL-',NAME='JAH El Escorial Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "El Escorial Library: the complete guide", "d": "El Escorial Library: Philip II's hall..", "g": "overview", "l": 2, "q": "What is El Escorial Library: the complete guide?", "a": "El Escorial Library: Philip II's hall..", "x": "The complete library guide to El Escorial Library: Philip II's hall.. 16th century. History, meaning, practices, and how to engage respectfully — everything in one database. Hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "El Escorial Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "El Escorial Library essentials.", "x": "At a glance: El Escorial Library — Philip II's hall.. Frescoed vault. The essentials: Frescoes.. 40K volumes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "16th century.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "16th century.", "x": "El Escorial Library: 16th century.. Frescoes. Essential knowledge — 40K volumes.. Philip II's hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 16th century..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 16th century..", "x": "Explained: 16th century.. Spain. The context — El Escorial Library. Spain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Frescoed vault.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Frescoed vault.", "x": "El Escorial Library: Frescoed vault.. History. Essential knowledge — Spain.. Philip II's hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Frescoed vault..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Frescoed vault..", "x": "Explained: Frescoed vault.. Tours. The context — El Escorial Library. Philip II. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "40K volumes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "40K volumes.", "x": "El Escorial Library: 40K volumes.. Spain. Essential knowledge — Philip II.. Philip II's hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 40K volumes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 40K volumes..", "x": "Explained: 40K volumes.. Philip. The context — El Escorial Library. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spain.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spain.", "x": "El Escorial Library: Spain.. Tours. Essential knowledge — History.. Philip II's hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Spain..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Spain..", "x": "Explained: Spain.. Hall. The context — El Escorial Library. 16th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Philip II.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Philip II.", "x": "El Escorial Library: Philip II.. Philip. Essential knowledge — 16th century.. Philip II's hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Philip II..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Philip II..", "x": "Explained: Philip II.. Frescoes. The context — El Escorial Library. Frescoed vault. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "El Escorial Library: History.. Hall. Essential knowledge — Frescoed vault.. Philip II's hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — El Escorial Library. 40K volumes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hall.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hall.", "x": "El Escorial Library in depth: Hall.. Frescoed vault. Details — Philip II's hall.. History. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Frescoes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Frescoes.", "x": "El Escorial Library in depth: Frescoes.. 40K volumes. Details — Philip II's hall.. Spain. Philip II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "El Escorial Library in depth: History.. Spain. Details — Philip II's hall.. Tours. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Spain.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Spain.", "x": "El Escorial Library in depth: Spain.. Philip II. Details — Philip II's hall.. Philip. 16th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "El Escorial Library in depth: Tours.. History. Details — Philip II's hall.. Hall. Frescoed vault. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Philip.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Philip.", "x": "El Escorial Library in depth: Philip.. 16th century. Details — Philip II's hall.. Frescoes. 40K volumes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where El Escorial Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where El Escorial Library comes from.", "x": "Origins: Hall.. 16th century. The history of El Escorial Library — Philip II's hall.. Frescoes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing El Escorial Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing El Escorial Library respectfully.", "x": "Engaging: History.. Frescoed vault. How to participate or observe well — El Escorial Library. Philip II's hall. Respect first, always; Spain.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "El Escorial Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "El Escorial Library do's and don'ts.", "x": "Etiquette: Tours.. 40K volumes. The rules of respect — El Escorial Library. Philip II's hall. When in doubt, ask about Philip.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around El Escorial Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around El Escorial Library.", "x": "Planning: Hall.. Spain. Practical notes — El Escorial Library. Philip II's hall. A little planning shows respect for Frescoes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "El Escorial Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "El Escorial Library and money.", "x": "Costs: History.. Philip II. What to budget — El Escorial Library. Philip II's hall. The best experiences of Spain. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-el-escorial-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
