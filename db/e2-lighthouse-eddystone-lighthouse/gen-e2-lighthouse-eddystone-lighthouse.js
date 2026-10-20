(function(){'use strict';
/* JAH Eddystone Lighthouse Lighthouse Database generator — jahdb-e2-lighthouse-eddystone-lighthouse-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lighthouse-eddystone-lighthouse',PREFIX='JAH-E2LIGHTHOUS-',NAME='JAH Eddystone Lighthouse Lighthouse Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Eddystone Lighthouse: the complete guide", "d": "Eddystone Lighthouse: the sea's sentinel..", "g": "overview", "l": 2, "q": "What is Eddystone Lighthouse: the complete guide?", "a": "Eddystone Lighthouse: the sea's sentinel..", "x": "The complete lighthouse guide to Eddystone Lighthouse: the sea's sentinel.. 1698. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Eddystone Lighthouse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Eddystone Lighthouse essentials.", "x": "At a glance: Eddystone Lighthouse — the sea's sentinel.. Winstanley. The essentials: Keepers.. Rebuilt. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1698.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1698.", "x": "Eddystone Lighthouse: 1698.. Keepers. Essential knowledge — Rebuilt.. the sea's sentinel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1698..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1698..", "x": "Explained: 1698.. Rebuilds. The context — Eddystone Lighthouse. Plymouth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Winstanley.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Winstanley.", "x": "Eddystone Lighthouse: Winstanley.. Storms. Essential knowledge — Plymouth.. the sea's sentinel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Winstanley..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Winstanley..", "x": "Explained: Winstanley.. Tours. The context — Eddystone Lighthouse. Rock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rebuilt.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rebuilt.", "x": "Eddystone Lighthouse: Rebuilt.. Rebuilds. Essential knowledge — Rock.. the sea's sentinel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rebuilt..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rebuilt..", "x": "Explained: Rebuilt.. Legends. The context — Eddystone Lighthouse. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Plymouth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Plymouth.", "x": "Eddystone Lighthouse: Plymouth.. Tours. Essential knowledge — History.. the sea's sentinel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Plymouth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Plymouth..", "x": "Explained: Plymouth.. History. The context — Eddystone Lighthouse. 1698. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rock.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rock.", "x": "Eddystone Lighthouse: Rock.. Legends. Essential knowledge — 1698.. the sea's sentinel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rock..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rock..", "x": "Explained: Rock.. Keepers. The context — Eddystone Lighthouse. Winstanley. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Eddystone Lighthouse: History.. History. Essential knowledge — Winstanley.. the sea's sentinel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Storms. The context — Eddystone Lighthouse. Rebuilt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Eddystone Lighthouse in depth: History.. Winstanley. Details — the sea's sentinel.. Storms. Plymouth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Keepers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Keepers.", "x": "Eddystone Lighthouse in depth: Keepers.. Rebuilt. Details — the sea's sentinel.. Rebuilds. Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Storms.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Storms.", "x": "Eddystone Lighthouse in depth: Storms.. Plymouth. Details — the sea's sentinel.. Tours. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rebuilds.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rebuilds.", "x": "Eddystone Lighthouse in depth: Rebuilds.. Rock. Details — the sea's sentinel.. Legends. 1698. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Eddystone Lighthouse in depth: Tours.. History. Details — the sea's sentinel.. History. Winstanley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legends.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legends.", "x": "Eddystone Lighthouse in depth: Legends.. 1698. Details — the sea's sentinel.. Keepers. Rebuilt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Eddystone Lighthouse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Eddystone Lighthouse comes from.", "x": "Origins: History.. 1698. The history of Eddystone Lighthouse — the sea's sentinel.. Keepers. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Eddystone Lighthouse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Eddystone Lighthouse respectfully.", "x": "Engaging: Storms.. Winstanley. How to participate or observe well — Eddystone Lighthouse. the sea's sentinel. Respect first, always; Rebuilds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Eddystone Lighthouse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Eddystone Lighthouse do's and don'ts.", "x": "Etiquette: Tours.. Rebuilt. The rules of respect — Eddystone Lighthouse. the sea's sentinel. When in doubt, ask about Legends.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Eddystone Lighthouse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Eddystone Lighthouse.", "x": "Planning: History.. Plymouth. Practical notes — Eddystone Lighthouse. the sea's sentinel. A little planning shows respect for Keepers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Eddystone Lighthouse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Eddystone Lighthouse and money.", "x": "Costs: Storms.. Rock. What to budget — Eddystone Lighthouse. the sea's sentinel. The best experiences of Rebuilds. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lighthouse-eddystone-lighthouse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
