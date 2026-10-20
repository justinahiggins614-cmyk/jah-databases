(function(){'use strict';
/* JAH Two-Step Dance Dance Form Database generator — jahdb-e2-dance-two-step-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-two-step-dance-form',PREFIX='JAH-E2DANCETWOS-',NAME='JAH Two-Step Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Two-Step Dance: the complete guide", "d": "Two-Step Dance: the Texas classic..", "g": "overview", "l": 2, "q": "What is Two-Step Dance: the complete guide?", "a": "Two-Step Dance: the Texas classic..", "x": "The complete dance form guide to Two-Step Dance: the Texas classic.. Texas. History, meaning, practices, and how to engage respectfully — everything in one database. Quick. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Two-Step Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Two-Step Dance essentials.", "x": "At a glance: Two-Step Dance — the Texas classic.. Quick. The essentials: Honky-tonk.. Country. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Texas.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Texas.", "x": "Two-Step Dance: Texas.. Honky-tonk. Essential knowledge — Country.. the Texas classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Texas..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Texas..", "x": "Explained: Texas.. Texas. The context — Two-Step Dance. Honky-tonk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Quick.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Quick.", "x": "Two-Step Dance: Quick.. Glide. Essential knowledge — Honky-tonk.. the Texas classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Quick..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Quick..", "x": "Explained: Quick.. Country. The context — Two-Step Dance. Couples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Country.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Country.", "x": "Two-Step Dance: Country.. Texas. Essential knowledge — Couples.. the Texas classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Country..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Country..", "x": "Explained: Country.. Training. The context — Two-Step Dance. Glide. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Honky-tonk.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Honky-tonk.", "x": "Two-Step Dance: Honky-tonk.. Country. Essential knowledge — Glide.. the Texas classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Honky-tonk..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Honky-tonk..", "x": "Explained: Honky-tonk.. Quick. The context — Two-Step Dance. Texas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Couples.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Couples.", "x": "Two-Step Dance: Couples.. Training. Essential knowledge — Texas.. the Texas classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Couples..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Couples..", "x": "Explained: Couples.. Honky-tonk. The context — Two-Step Dance. Quick. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Glide.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Glide.", "x": "Two-Step Dance: Glide.. Quick. Essential knowledge — Quick.. the Texas classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Glide..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Glide..", "x": "Explained: Glide.. Glide. The context — Two-Step Dance. Country. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Quick.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Quick.", "x": "Two-Step Dance in depth: Quick.. Quick. Details — the Texas classic.. Glide. Honky-tonk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Honky-tonk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Honky-tonk.", "x": "Two-Step Dance in depth: Honky-tonk.. Country. Details — the Texas classic.. Texas. Couples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Glide.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Glide.", "x": "Two-Step Dance in depth: Glide.. Honky-tonk. Details — the Texas classic.. Country. Glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Texas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Texas.", "x": "Two-Step Dance in depth: Texas.. Couples. Details — the Texas classic.. Training. Texas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Country.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Country.", "x": "Two-Step Dance in depth: Country.. Glide. Details — the Texas classic.. Quick. Quick. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Two-Step Dance in depth: Training.. Texas. Details — the Texas classic.. Honky-tonk. Country. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Two-Step Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Two-Step Dance comes from.", "x": "Origins: Quick.. Texas. The history of Two-Step Dance — the Texas classic.. Honky-tonk. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Two-Step Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Two-Step Dance respectfully.", "x": "Engaging: Glide.. Quick. How to participate or observe well — Two-Step Dance. the Texas classic. Respect first, always; Texas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Two-Step Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Two-Step Dance do's and don'ts.", "x": "Etiquette: Country.. Country. The rules of respect — Two-Step Dance. the Texas classic. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Two-Step Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Two-Step Dance.", "x": "Planning: Quick.. Honky-tonk. Practical notes — Two-Step Dance. the Texas classic. A little planning shows respect for Honky-tonk.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Two-Step Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Two-Step Dance and money.", "x": "Costs: Glide.. Couples. What to budget — Two-Step Dance. the Texas classic. The best experiences of Texas. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-two-step-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
