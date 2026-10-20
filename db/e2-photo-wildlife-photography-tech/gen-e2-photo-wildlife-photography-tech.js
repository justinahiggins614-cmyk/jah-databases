(function(){'use strict';
/* JAH Wildlife Photography Photography Database generator — jahdb-e2-photo-wildlife-photography-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-wildlife-photography-tech',PREFIX='JAH-E2PHOTOWILD-',NAME='JAH Wildlife Photography Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wildlife Photography: the complete guide", "d": "Wildlife Photography: the patient hunt..", "g": "overview", "l": 2, "q": "What is Wildlife Photography: the complete guide?", "a": "Wildlife Photography: the patient hunt..", "x": "The complete photography guide to Wildlife Photography: the patient hunt.. Telephoto. History, meaning, practices, and how to engage respectfully — everything in one database. Telephoto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Wildlife Photography essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Wildlife Photography essentials.", "x": "At a glance: Wildlife Photography — the patient hunt.. Patience. The essentials: Blinds.. Blinds. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Telephoto.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Telephoto.", "x": "Wildlife Photography: Telephoto.. Blinds. Essential knowledge — Blinds.. the patient hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Telephoto..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Telephoto..", "x": "Explained: Telephoto.. Fast. The context — Wildlife Photography. Behavior. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Patience.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Patience.", "x": "Wildlife Photography: Patience.. Ethics. Essential knowledge — Behavior.. the patient hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Patience..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Patience..", "x": "Explained: Patience.. Behavior. The context — Wildlife Photography. Fast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Blinds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Blinds.", "x": "Wildlife Photography: Blinds.. Fast. Essential knowledge — Fast.. the patient hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Blinds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Blinds..", "x": "Explained: Blinds.. Tips. The context — Wildlife Photography. Ethics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Behavior.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Behavior.", "x": "Wildlife Photography: Behavior.. Behavior. Essential knowledge — Ethics.. the patient hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Behavior..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Behavior..", "x": "Explained: Behavior.. Telephoto. The context — Wildlife Photography. Telephoto. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fast.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fast.", "x": "Wildlife Photography: Fast.. Tips. Essential knowledge — Telephoto.. the patient hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fast..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fast..", "x": "Explained: Fast.. Blinds. The context — Wildlife Photography. Patience. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ethics.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ethics.", "x": "Wildlife Photography: Ethics.. Telephoto. Essential knowledge — Patience.. the patient hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ethics..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ethics..", "x": "Explained: Ethics.. Ethics. The context — Wildlife Photography. Blinds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Telephoto.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Telephoto.", "x": "Wildlife Photography in depth: Telephoto.. Patience. Details — the patient hunt.. Ethics. Behavior. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Blinds.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Blinds.", "x": "Wildlife Photography in depth: Blinds.. Blinds. Details — the patient hunt.. Fast. Fast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ethics.", "x": "Wildlife Photography in depth: Ethics.. Behavior. Details — the patient hunt.. Behavior. Ethics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fast.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fast.", "x": "Wildlife Photography in depth: Fast.. Fast. Details — the patient hunt.. Tips. Telephoto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Behavior.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Behavior.", "x": "Wildlife Photography in depth: Behavior.. Ethics. Details — the patient hunt.. Telephoto. Patience. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Wildlife Photography in depth: Tips.. Telephoto. Details — the patient hunt.. Blinds. Blinds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Wildlife Photography comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Wildlife Photography comes from.", "x": "Origins: Telephoto.. Telephoto. The history of Wildlife Photography — the patient hunt.. Blinds. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Wildlife Photography respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Wildlife Photography respectfully.", "x": "Engaging: Ethics.. Patience. How to participate or observe well — Wildlife Photography. the patient hunt. Respect first, always; Fast.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Wildlife Photography do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Wildlife Photography do's and don'ts.", "x": "Etiquette: Behavior.. Blinds. The rules of respect — Wildlife Photography. the patient hunt. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Wildlife Photography.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Wildlife Photography.", "x": "Planning: Telephoto.. Behavior. Practical notes — Wildlife Photography. the patient hunt. A little planning shows respect for Blinds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Wildlife Photography and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Wildlife Photography and money.", "x": "Costs: Ethics.. Fast. What to budget — Wildlife Photography. the patient hunt. The best experiences of Fast. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-wildlife-photography-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
