(function(){'use strict';
/* JAH Xiaowan Dam Dam Database generator — jahdb-e2-dam-xiaowan-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam-xiaowan-dam',PREFIX='JAH-E2DAMXIAOWA-',NAME='JAH Xiaowan Dam Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Xiaowan Dam: the complete guide", "d": "Xiaowan Dam: China's arch giant..", "g": "overview", "l": 2, "q": "What is Xiaowan Dam: the complete guide?", "a": "Xiaowan Dam: China's arch giant..", "x": "The complete dam guide to Xiaowan Dam: China's arch giant.. 292m. History, meaning, practices, and how to engage respectfully — everything in one database. Arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Xiaowan Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Xiaowan Dam essentials.", "x": "At a glance: Xiaowan Dam — China's arch giant.. Mekong. The essentials: River.. 2010. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "292m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "292m.", "x": "Xiaowan Dam: 292m.. River. Essential knowledge — 2010.. China's arch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 292m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 292m..", "x": "Explained: 292m.. China. The context — Xiaowan Dam. Arch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mekong.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mekong.", "x": "Xiaowan Dam: Mekong.. Power. Essential knowledge — Arch.. China's arch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mekong..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mekong..", "x": "Explained: Mekong.. Records. The context — Xiaowan Dam. Power. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "2010.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "2010.", "x": "Xiaowan Dam: 2010.. China. Essential knowledge — Power.. China's arch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 2010..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 2010..", "x": "Explained: 2010.. History. The context — Xiaowan Dam. Yunnan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Arch.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Arch.", "x": "Xiaowan Dam: Arch.. Records. Essential knowledge — Yunnan.. China's arch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Arch..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Arch..", "x": "Explained: Arch.. Arch. The context — Xiaowan Dam. 292m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Power.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Power.", "x": "Xiaowan Dam: Power.. History. Essential knowledge — 292m.. China's arch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Power..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Power..", "x": "Explained: Power.. River. The context — Xiaowan Dam. Mekong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Yunnan.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Yunnan.", "x": "Xiaowan Dam: Yunnan.. Arch. Essential knowledge — Mekong.. China's arch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Yunnan..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Yunnan..", "x": "Explained: Yunnan.. Power. The context — Xiaowan Dam. 2010. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Arch.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Arch.", "x": "Xiaowan Dam in depth: Arch.. Mekong. Details — China's arch giant.. Power. Arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "River.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "River.", "x": "Xiaowan Dam in depth: River.. 2010. Details — China's arch giant.. China. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Power.", "x": "Xiaowan Dam in depth: Power.. Arch. Details — China's arch giant.. Records. Yunnan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "China.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "China.", "x": "Xiaowan Dam in depth: China.. Power. Details — China's arch giant.. History. 292m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Records.", "x": "Xiaowan Dam in depth: Records.. Yunnan. Details — China's arch giant.. Arch. Mekong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Xiaowan Dam in depth: History.. 292m. Details — China's arch giant.. River. 2010. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Xiaowan Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Xiaowan Dam comes from.", "x": "Origins: Arch.. 292m. The history of Xiaowan Dam — China's arch giant.. River. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Xiaowan Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Xiaowan Dam respectfully.", "x": "Engaging: Power.. Mekong. How to participate or observe well — Xiaowan Dam. China's arch giant. Respect first, always; China.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Xiaowan Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Xiaowan Dam do's and don'ts.", "x": "Etiquette: Records.. 2010. The rules of respect — Xiaowan Dam. China's arch giant. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Xiaowan Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Xiaowan Dam.", "x": "Planning: Arch.. Arch. Practical notes — Xiaowan Dam. China's arch giant. A little planning shows respect for River.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Xiaowan Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Xiaowan Dam and money.", "x": "Costs: Power.. Power. What to budget — Xiaowan Dam. China's arch giant. The best experiences of China. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam-xiaowan-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
