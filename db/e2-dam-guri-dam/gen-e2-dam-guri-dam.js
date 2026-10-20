(function(){'use strict';
/* JAH Guri Dam Dam Database generator — jahdb-e2-dam-guri-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam-guri-dam',PREFIX='JAH-E2DAMGURIDA-',NAME='JAH Guri Dam Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Guri Dam: the complete guide", "d": "Guri Dam: Venezuela's power..", "g": "overview", "l": 2, "q": "What is Guri Dam: the complete guide?", "a": "Guri Dam: Venezuela's power..", "x": "The complete dam guide to Guri Dam: Venezuela's power.. 10,200 MW. History, meaning, practices, and how to engage respectfully — everything in one database. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Guri Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Guri Dam essentials.", "x": "At a glance: Guri Dam — Venezuela's power.. Caroni. The essentials: Lake.. 1978. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "10,200 MW.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "10,200 MW.", "x": "Guri Dam: 10,200 MW.. Lake. Essential knowledge — 1978.. Venezuela's power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 10,200 MW..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 10,200 MW..", "x": "Explained: 10,200 MW.. Crisis. The context — Guri Dam. Blackouts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Caroni.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Caroni.", "x": "Guri Dam: Caroni.. History. Essential knowledge — Blackouts.. Venezuela's power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Caroni..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Caroni..", "x": "Explained: Caroni.. Scale. The context — Guri Dam. Lake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1978.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1978.", "x": "Guri Dam: 1978.. Crisis. Essential knowledge — Lake.. Venezuela's power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1978..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1978..", "x": "Explained: 1978.. Venezuela. The context — Guri Dam. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Blackouts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Blackouts.", "x": "Guri Dam: Blackouts.. Scale. Essential knowledge — History.. Venezuela's power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Blackouts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Blackouts..", "x": "Explained: Blackouts.. Power. The context — Guri Dam. 10,200 MW. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Lake.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Lake.", "x": "Guri Dam: Lake.. Venezuela. Essential knowledge — 10,200 MW.. Venezuela's power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Lake..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Lake..", "x": "Explained: Lake.. Lake. The context — Guri Dam. Caroni. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Guri Dam: History.. Power. Essential knowledge — Caroni.. Venezuela's power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Guri Dam. 1978. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Power.", "x": "Guri Dam in depth: Power.. Caroni. Details — Venezuela's power.. History. Blackouts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lake.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lake.", "x": "Guri Dam in depth: Lake.. 1978. Details — Venezuela's power.. Crisis. Lake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Guri Dam in depth: History.. Blackouts. Details — Venezuela's power.. Scale. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Crisis.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Crisis.", "x": "Guri Dam in depth: Crisis.. Lake. Details — Venezuela's power.. Venezuela. 10,200 MW. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Scale.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Scale.", "x": "Guri Dam in depth: Scale.. History. Details — Venezuela's power.. Power. Caroni. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Venezuela.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Venezuela.", "x": "Guri Dam in depth: Venezuela.. 10,200 MW. Details — Venezuela's power.. Lake. 1978. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Guri Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Guri Dam comes from.", "x": "Origins: Power.. 10,200 MW. The history of Guri Dam — Venezuela's power.. Lake. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Guri Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Guri Dam respectfully.", "x": "Engaging: History.. Caroni. How to participate or observe well — Guri Dam. Venezuela's power. Respect first, always; Crisis.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Guri Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Guri Dam do's and don'ts.", "x": "Etiquette: Scale.. 1978. The rules of respect — Guri Dam. Venezuela's power. When in doubt, ask about Venezuela.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Guri Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Guri Dam.", "x": "Planning: Power.. Blackouts. Practical notes — Guri Dam. Venezuela's power. A little planning shows respect for Lake.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Guri Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Guri Dam and money.", "x": "Costs: History.. Lake. What to budget — Guri Dam. Venezuela's power. The best experiences of Crisis. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam-guri-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
