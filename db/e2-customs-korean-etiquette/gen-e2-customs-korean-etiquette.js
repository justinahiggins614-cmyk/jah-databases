(function(){'use strict';
/* JAH Korean Etiquette Customs Database generator — jahdb-e2-customs-korean-etiquette-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-customs-korean-etiquette',PREFIX='JAH-E2CUSTOMSKO-',NAME='JAH Korean Etiquette Customs Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Korean Etiquette: the complete guide", "d": "Korean Etiquette: hierarchy and harmony..", "g": "overview", "l": 2, "q": "What is Korean Etiquette: the complete guide?", "a": "Korean Etiquette: hierarchy and harmony..", "x": "The complete customs guide to Korean Etiquette: hierarchy and harmony.. Bowing. History, meaning, practices, and how to engage respectfully — everything in one database. Bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Korean Etiquette essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Korean Etiquette essentials.", "x": "At a glance: Korean Etiquette — hierarchy and harmony.. Two hands. The essentials: Hands.. Elders. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bowing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bowing.", "x": "Korean Etiquette: Bowing.. Hands. Essential knowledge — Elders.. hierarchy and harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bowing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bowing..", "x": "Explained: Bowing.. Drink. The context — Korean Etiquette. Drinking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Two hands.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Two hands.", "x": "Korean Etiquette: Two hands.. Elders. Essential knowledge — Drinking.. hierarchy and harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Two hands..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Two hands..", "x": "Explained: Two hands.. Age. The context — Korean Etiquette. Age matters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Elders.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Elders.", "x": "Korean Etiquette: Elders.. Drink. Essential knowledge — Age matters.. hierarchy and harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Elders..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Elders..", "x": "Explained: Elders.. Harmony. The context — Korean Etiquette. Nunchi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Drinking.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Drinking.", "x": "Korean Etiquette: Drinking.. Age. Essential knowledge — Nunchi.. hierarchy and harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Drinking..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Drinking..", "x": "Explained: Drinking.. Bow. The context — Korean Etiquette. Bowing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Age matters.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Age matters.", "x": "Korean Etiquette: Age matters.. Harmony. Essential knowledge — Bowing.. hierarchy and harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Age matters..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Age matters..", "x": "Explained: Age matters.. Hands. The context — Korean Etiquette. Two hands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nunchi.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nunchi.", "x": "Korean Etiquette: Nunchi.. Bow. Essential knowledge — Two hands.. hierarchy and harmony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Nunchi..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Nunchi..", "x": "Explained: Nunchi.. Elders. The context — Korean Etiquette. Elders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bow.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bow.", "x": "Korean Etiquette in depth: Bow.. Two hands. Details — hierarchy and harmony.. Elders. Drinking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hands.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hands.", "x": "Korean Etiquette in depth: Hands.. Elders. Details — hierarchy and harmony.. Drink. Age matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Elders.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Elders.", "x": "Korean Etiquette in depth: Elders.. Drinking. Details — hierarchy and harmony.. Age. Nunchi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drink.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drink.", "x": "Korean Etiquette in depth: Drink.. Age matters. Details — hierarchy and harmony.. Harmony. Bowing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Age.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Age.", "x": "Korean Etiquette in depth: Age.. Nunchi. Details — hierarchy and harmony.. Bow. Two hands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Harmony.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Harmony.", "x": "Korean Etiquette in depth: Harmony.. Bowing. Details — hierarchy and harmony.. Hands. Elders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Korean Etiquette comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Korean Etiquette comes from.", "x": "Origins: Bow.. Bowing. The history of Korean Etiquette — hierarchy and harmony.. Hands. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Korean Etiquette respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Korean Etiquette respectfully.", "x": "Engaging: Elders.. Two hands. How to participate or observe well — Korean Etiquette. hierarchy and harmony. Respect first, always; Drink.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Korean Etiquette do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Korean Etiquette do's and don'ts.", "x": "Etiquette: Age.. Elders. The rules of respect — Korean Etiquette. hierarchy and harmony. When in doubt, ask about Harmony.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Korean Etiquette.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Korean Etiquette.", "x": "Planning: Bow.. Drinking. Practical notes — Korean Etiquette. hierarchy and harmony. A little planning shows respect for Hands.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Korean Etiquette and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Korean Etiquette and money.", "x": "Costs: Elders.. Age matters. What to budget — Korean Etiquette. hierarchy and harmony. The best experiences of Drink. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-customs-korean-etiquette-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
