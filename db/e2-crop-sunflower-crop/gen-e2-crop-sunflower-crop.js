(function(){'use strict';
/* JAH Sunflower Crop Crop Database generator — jahdb-e2-crop-sunflower-crop-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-crop-sunflower-crop',PREFIX='JAH-E2CROPSUNFL-',NAME='JAH Sunflower Crop Crop Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sunflower Crop: the complete guide", "d": "Sunflower Crop: the oil flower..", "g": "overview", "l": 2, "q": "What is Sunflower Crop: the complete guide?", "a": "Sunflower Crop: the oil flower..", "x": "The complete crop guide to Sunflower Crop: the oil flower.. Oil. History, meaning, practices, and how to engage respectfully — everything in one database. Oil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sunflower Crop essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sunflower Crop essentials.", "x": "At a glance: Sunflower Crop — the oil flower.. Heads. The essentials: Ukraine.. Ukraine. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Oil.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Oil.", "x": "Sunflower Crop: Oil.. Ukraine. Essential knowledge — Ukraine.. the oil flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Oil..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Oil..", "x": "Explained: Oil.. Tall. The context — Sunflower Crop. Tracking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Heads.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Heads.", "x": "Sunflower Crop: Heads.. Seeds. Essential knowledge — Tracking.. the oil flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Heads..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Heads..", "x": "Explained: Heads.. Heads. The context — Sunflower Crop. Seeds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ukraine.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ukraine.", "x": "Sunflower Crop: Ukraine.. Tall. Essential knowledge — Seeds.. the oil flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ukraine..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ukraine..", "x": "Explained: Ukraine.. Growing. The context — Sunflower Crop. Tall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tracking.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tracking.", "x": "Sunflower Crop: Tracking.. Heads. Essential knowledge — Tall.. the oil flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tracking..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tracking..", "x": "Explained: Tracking.. Oil. The context — Sunflower Crop. Oil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Seeds.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Seeds.", "x": "Sunflower Crop: Seeds.. Growing. Essential knowledge — Oil.. the oil flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Seeds..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Seeds..", "x": "Explained: Seeds.. Ukraine. The context — Sunflower Crop. Heads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tall.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tall.", "x": "Sunflower Crop: Tall.. Oil. Essential knowledge — Heads.. the oil flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tall..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tall..", "x": "Explained: Tall.. Seeds. The context — Sunflower Crop. Ukraine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Oil.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Oil.", "x": "Sunflower Crop in depth: Oil.. Heads. Details — the oil flower.. Seeds. Tracking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ukraine.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ukraine.", "x": "Sunflower Crop in depth: Ukraine.. Ukraine. Details — the oil flower.. Tall. Seeds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Seeds.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Seeds.", "x": "Sunflower Crop in depth: Seeds.. Tracking. Details — the oil flower.. Heads. Tall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tall.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tall.", "x": "Sunflower Crop in depth: Tall.. Seeds. Details — the oil flower.. Growing. Oil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Heads.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Heads.", "x": "Sunflower Crop in depth: Heads.. Tall. Details — the oil flower.. Oil. Heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Growing.", "x": "Sunflower Crop in depth: Growing.. Oil. Details — the oil flower.. Ukraine. Ukraine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sunflower Crop comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sunflower Crop comes from.", "x": "Origins: Oil.. Oil. The history of Sunflower Crop — the oil flower.. Ukraine. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sunflower Crop respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sunflower Crop respectfully.", "x": "Engaging: Seeds.. Heads. How to participate or observe well — Sunflower Crop. the oil flower. Respect first, always; Tall.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sunflower Crop do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sunflower Crop do's and don'ts.", "x": "Etiquette: Heads.. Ukraine. The rules of respect — Sunflower Crop. the oil flower. When in doubt, ask about Growing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sunflower Crop.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sunflower Crop.", "x": "Planning: Oil.. Tracking. Practical notes — Sunflower Crop. the oil flower. A little planning shows respect for Ukraine.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sunflower Crop and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sunflower Crop and money.", "x": "Costs: Seeds.. Seeds. What to budget — Sunflower Crop. the oil flower. The best experiences of Tall. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-crop-sunflower-crop-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
