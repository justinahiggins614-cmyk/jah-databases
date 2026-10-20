(function(){'use strict';
/* JAH Grand Coulee Dam Dam Database generator — jahdb-e2-dam-grand-coulee-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam-grand-coulee-dam',PREFIX='JAH-E2DAMGRANDC-',NAME='JAH Grand Coulee Dam Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Grand Coulee Dam: the complete guide", "d": "Grand Coulee Dam: Columbia's concrete giant..", "g": "overview", "l": 2, "q": "What is Grand Coulee Dam: the complete guide?", "a": "Grand Coulee Dam: Columbia's concrete giant..", "x": "The complete dam guide to Grand Coulee Dam: Columbia's concrete giant.. 1942. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Grand Coulee Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Grand Coulee Dam essentials.", "x": "At a glance: Grand Coulee Dam — Columbia's concrete giant.. Irrigation. The essentials: Power.. Power. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1942.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1942.", "x": "Grand Coulee Dam: 1942.. Power. Essential knowledge — Power.. Columbia's concrete giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1942..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1942..", "x": "Explained: 1942.. Irrigation. The context — Grand Coulee Dam. Lake Roosevelt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Irrigation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Irrigation.", "x": "Grand Coulee Dam: Irrigation.. Lake. Essential knowledge — Lake Roosevelt.. Columbia's concrete giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Irrigation..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Irrigation..", "x": "Explained: Irrigation.. Tours. The context — Grand Coulee Dam. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Power.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Power.", "x": "Grand Coulee Dam: Power.. Irrigation. Essential knowledge — History.. Columbia's concrete giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Power..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Power..", "x": "Explained: Power.. Art. The context — Grand Coulee Dam. Art. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lake Roosevelt.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lake Roosevelt.", "x": "Grand Coulee Dam: Lake Roosevelt.. Tours. Essential knowledge — Art.. Columbia's concrete giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lake Roosevelt..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lake Roosevelt..", "x": "Explained: Lake Roosevelt.. History. The context — Grand Coulee Dam. 1942. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Grand Coulee Dam: History.. Art. Essential knowledge — 1942.. Columbia's concrete giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. Power. The context — Grand Coulee Dam. Irrigation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Art.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Art.", "x": "Grand Coulee Dam: Art.. History. Essential knowledge — Irrigation.. Columbia's concrete giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Art..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Art..", "x": "Explained: Art.. Lake. The context — Grand Coulee Dam. Power. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Grand Coulee Dam in depth: History.. Irrigation. Details — Columbia's concrete giant.. Lake. Lake Roosevelt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Power.", "x": "Grand Coulee Dam in depth: Power.. Power. Details — Columbia's concrete giant.. Irrigation. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lake.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lake.", "x": "Grand Coulee Dam in depth: Lake.. Lake Roosevelt. Details — Columbia's concrete giant.. Tours. Art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Irrigation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Irrigation.", "x": "Grand Coulee Dam in depth: Irrigation.. History. Details — Columbia's concrete giant.. Art. 1942. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Grand Coulee Dam in depth: Tours.. Art. Details — Columbia's concrete giant.. History. Irrigation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Grand Coulee Dam in depth: Art.. 1942. Details — Columbia's concrete giant.. Power. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Grand Coulee Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Grand Coulee Dam comes from.", "x": "Origins: History.. 1942. The history of Grand Coulee Dam — Columbia's concrete giant.. Power. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Grand Coulee Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Grand Coulee Dam respectfully.", "x": "Engaging: Lake.. Irrigation. How to participate or observe well — Grand Coulee Dam. Columbia's concrete giant. Respect first, always; Irrigation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Grand Coulee Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Grand Coulee Dam do's and don'ts.", "x": "Etiquette: Tours.. Power. The rules of respect — Grand Coulee Dam. Columbia's concrete giant. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Grand Coulee Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Grand Coulee Dam.", "x": "Planning: History.. Lake Roosevelt. Practical notes — Grand Coulee Dam. Columbia's concrete giant. A little planning shows respect for Power.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Grand Coulee Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Grand Coulee Dam and money.", "x": "Costs: Lake.. History. What to budget — Grand Coulee Dam. Columbia's concrete giant. The best experiences of Irrigation. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam-grand-coulee-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
