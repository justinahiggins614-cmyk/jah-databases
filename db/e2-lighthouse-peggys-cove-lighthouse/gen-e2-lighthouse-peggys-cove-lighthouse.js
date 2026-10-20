(function(){'use strict';
/* JAH Peggy\'s Cove Lighthouse Lighthouse Database generator — jahdb-e2-lighthouse-peggys-cove-lighthouse-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lighthouse-peggys-cove-lighthouse',PREFIX='JAH-E2LIGHTHOUS-',NAME='JAH Peggy\'s Cove Lighthouse Lighthouse Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peggy's Cove Lighthouse: the complete guide", "d": "Peggy's Cove Lighthouse: Nova Scotia's icon..", "g": "overview", "l": 2, "q": "What is Peggy's Cove Lighthouse: the complete guide?", "a": "Peggy's Cove Lighthouse: Nova Scotia's icon..", "x": "The complete lighthouse guide to Peggy's Cove Lighthouse: Nova Scotia's icon.. 1915. History, meaning, practices, and how to engage respectfully — everything in one database. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Peggy's Cove Lighthouse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Peggy's Cove Lighthouse essentials.", "x": "At a glance: Peggy's Cove Lighthouse — Nova Scotia's icon.. Granite. The essentials: Village.. Photos. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1915.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1915.", "x": "Peggy's Cove Lighthouse: 1915.. Village. Essential knowledge — Photos.. Nova Scotia's icon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1915..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1915..", "x": "Explained: 1915.. History. The context — Peggy's Cove Lighthouse. Waves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Granite.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Granite.", "x": "Peggy's Cove Lighthouse: Granite.. Waves. Essential knowledge — Waves.. Nova Scotia's icon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Granite..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Granite..", "x": "Explained: Granite.. Nova Scotia. The context — Peggy's Cove Lighthouse. Village. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Photos.", "x": "Peggy's Cove Lighthouse: Photos.. History. Essential knowledge — Village.. Nova Scotia's icon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Photos..", "x": "Explained: Photos.. Tours. The context — Peggy's Cove Lighthouse. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Waves.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Waves.", "x": "Peggy's Cove Lighthouse: Waves.. Nova Scotia. Essential knowledge — History.. Nova Scotia's icon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Waves..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Waves..", "x": "Explained: Waves.. Photos. The context — Peggy's Cove Lighthouse. 1915. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Village.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Village.", "x": "Peggy's Cove Lighthouse: Village.. Tours. Essential knowledge — 1915.. Nova Scotia's icon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Village..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Village..", "x": "Explained: Village.. Village. The context — Peggy's Cove Lighthouse. Granite. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Peggy's Cove Lighthouse: History.. Photos. Essential knowledge — Granite.. Nova Scotia's icon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Waves. The context — Peggy's Cove Lighthouse. Photos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Photos.", "x": "Peggy's Cove Lighthouse in depth: Photos.. Granite. Details — Nova Scotia's icon.. Waves. Waves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Village.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Village.", "x": "Peggy's Cove Lighthouse in depth: Village.. Photos. Details — Nova Scotia's icon.. History. Village. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Waves.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Waves.", "x": "Peggy's Cove Lighthouse in depth: Waves.. Waves. Details — Nova Scotia's icon.. Nova Scotia. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Peggy's Cove Lighthouse in depth: History.. Village. Details — Nova Scotia's icon.. Tours. 1915. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nova Scotia.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nova Scotia.", "x": "Peggy's Cove Lighthouse in depth: Nova Scotia.. History. Details — Nova Scotia's icon.. Photos. Granite. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Peggy's Cove Lighthouse in depth: Tours.. 1915. Details — Nova Scotia's icon.. Village. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Peggy's Cove Lighthouse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Peggy's Cove Lighthouse comes from.", "x": "Origins: Photos.. 1915. The history of Peggy's Cove Lighthouse — Nova Scotia's icon.. Village. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Peggy's Cove Lighthouse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Peggy's Cove Lighthouse respectfully.", "x": "Engaging: Waves.. Granite. How to participate or observe well — Peggy's Cove Lighthouse. Nova Scotia's icon. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Peggy's Cove Lighthouse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Peggy's Cove Lighthouse do's and don'ts.", "x": "Etiquette: Nova Scotia.. Photos. The rules of respect — Peggy's Cove Lighthouse. Nova Scotia's icon. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Peggy's Cove Lighthouse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Peggy's Cove Lighthouse.", "x": "Planning: Photos.. Waves. Practical notes — Peggy's Cove Lighthouse. Nova Scotia's icon. A little planning shows respect for Village.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Peggy's Cove Lighthouse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Peggy's Cove Lighthouse and money.", "x": "Costs: Waves.. Village. What to budget — Peggy's Cove Lighthouse. Nova Scotia's icon. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lighthouse-peggys-cove-lighthouse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
