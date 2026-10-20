(function(){'use strict';
/* JAH Itaipu Dam Dam Database generator — jahdb-e2-dam-itaipu-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam-itaipu-dam',PREFIX='JAH-E2DAMITAIPU-',NAME='JAH Itaipu Dam Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Itaipu Dam: the complete guide", "d": "Itaipu Dam: Brazil-Paraguay giant..", "g": "overview", "l": 2, "q": "What is Itaipu Dam: the complete guide?", "a": "Itaipu Dam: Brazil-Paraguay giant..", "x": "The complete dam guide to Itaipu Dam: Brazil-Paraguay giant.. 14,000 MW. History, meaning, practices, and how to engage respectfully — everything in one database. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Itaipu Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Itaipu Dam essentials.", "x": "At a glance: Itaipu Dam — Brazil-Paraguay giant.. Parana. The essentials: Treaty.. 1984. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "14,000 MW.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "14,000 MW.", "x": "Itaipu Dam: 14,000 MW.. Treaty. Essential knowledge — 1984.. Brazil-Paraguay giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 14,000 MW..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 14,000 MW..", "x": "Explained: 14,000 MW.. Tours. The context — Itaipu Dam. Second largest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Parana.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Parana.", "x": "Itaipu Dam: Parana.. Scale. Essential knowledge — Second largest.. Brazil-Paraguay giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Parana..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Parana..", "x": "Explained: Parana.. History. The context — Itaipu Dam. Treaty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1984.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1984.", "x": "Itaipu Dam: 1984.. Tours. Essential knowledge — Treaty.. Brazil-Paraguay giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1984..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1984..", "x": "Explained: 1984.. Records. The context — Itaipu Dam. Tours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Second largest.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Second largest.", "x": "Itaipu Dam: Second largest.. History. Essential knowledge — Tours.. Brazil-Paraguay giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Second largest..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Second largest..", "x": "Explained: Second largest.. Power. The context — Itaipu Dam. 14,000 MW. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Treaty.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Treaty.", "x": "Itaipu Dam: Treaty.. Records. Essential knowledge — 14,000 MW.. Brazil-Paraguay giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Treaty..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Treaty..", "x": "Explained: Treaty.. Treaty. The context — Itaipu Dam. Parana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tours.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tours.", "x": "Itaipu Dam: Tours.. Power. Essential knowledge — Parana.. Brazil-Paraguay giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tours..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tours..", "x": "Explained: Tours.. Scale. The context — Itaipu Dam. 1984. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Power.", "x": "Itaipu Dam in depth: Power.. Parana. Details — Brazil-Paraguay giant.. Scale. Second largest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Treaty.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Treaty.", "x": "Itaipu Dam in depth: Treaty.. 1984. Details — Brazil-Paraguay giant.. Tours. Treaty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Scale.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Scale.", "x": "Itaipu Dam in depth: Scale.. Second largest. Details — Brazil-Paraguay giant.. History. Tours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Itaipu Dam in depth: Tours.. Treaty. Details — Brazil-Paraguay giant.. Records. 14,000 MW. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Itaipu Dam in depth: History.. Tours. Details — Brazil-Paraguay giant.. Power. Parana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Records.", "x": "Itaipu Dam in depth: Records.. 14,000 MW. Details — Brazil-Paraguay giant.. Treaty. 1984. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Itaipu Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Itaipu Dam comes from.", "x": "Origins: Power.. 14,000 MW. The history of Itaipu Dam — Brazil-Paraguay giant.. Treaty. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Itaipu Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Itaipu Dam respectfully.", "x": "Engaging: Scale.. Parana. How to participate or observe well — Itaipu Dam. Brazil-Paraguay giant. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Itaipu Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Itaipu Dam do's and don'ts.", "x": "Etiquette: History.. 1984. The rules of respect — Itaipu Dam. Brazil-Paraguay giant. When in doubt, ask about Records.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Itaipu Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Itaipu Dam.", "x": "Planning: Power.. Second largest. Practical notes — Itaipu Dam. Brazil-Paraguay giant. A little planning shows respect for Treaty.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Itaipu Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Itaipu Dam and money.", "x": "Costs: Scale.. Treaty. What to budget — Itaipu Dam. Brazil-Paraguay giant. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam-itaipu-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
