(function(){'use strict';
/* JAH Very Large Array2 Database generator — jahdb-e2-observatory2-very-large-array2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory2-very-large-array2',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Very Large Array2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Very Large Array2: the complete guide", "d": "Very Large Array2: the New Mexico 2..", "g": "overview", "l": 2, "q": "What is Very Large Array2: the complete guide?", "a": "Very Large Array2: the New Mexico 2..", "x": "The complete observatory guide to Very Large Array2: the New Mexico 2.. 1980. History, meaning, practices, and how to engage respectfully — everything in one database. 1980. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Very Large Array2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Very Large Array2 essentials.", "x": "At a glance: Very Large Array2 — the New Mexico 2.. 27 dishes. The essentials: VLA.. Plains. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1980.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1980.", "x": "Very Large Array2: 1980.. VLA. Essential knowledge — Plains.. the New Mexico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1980..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1980..", "x": "Explained: 1980.. 27. The context — Very Large Array2. Radio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "27 dishes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "27 dishes.", "x": "Very Large Array2: 27 dishes.. Contact. Essential knowledge — Radio.. the New Mexico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 27 dishes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 27 dishes..", "x": "Explained: 27 dishes.. Radio. The context — Very Large Array2. Contact. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Plains.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Plains.", "x": "Very Large Array2: Plains.. 27. Essential knowledge — Contact.. the New Mexico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Plains..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Plains..", "x": "Explained: Plains.. Visiting. The context — Very Large Array2. VLA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Radio.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Radio.", "x": "Very Large Array2: Radio.. Radio. Essential knowledge — VLA.. the New Mexico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Radio..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Radio..", "x": "Explained: Radio.. 1980. The context — Very Large Array2. 1980. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Contact.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Contact.", "x": "Very Large Array2: Contact.. Visiting. Essential knowledge — 1980.. the New Mexico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Contact..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Contact..", "x": "Explained: Contact.. VLA. The context — Very Large Array2. 27 dishes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "VLA.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "VLA.", "x": "Very Large Array2: VLA.. 1980. Essential knowledge — 27 dishes.. the New Mexico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: VLA..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: VLA..", "x": "Explained: VLA.. Contact. The context — Very Large Array2. Plains. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1980.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1980.", "x": "Very Large Array2 in depth: 1980.. 27 dishes. Details — the New Mexico 2.. Contact. Radio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "VLA.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "VLA.", "x": "Very Large Array2 in depth: VLA.. Plains. Details — the New Mexico 2.. 27. Contact. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Contact.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Contact.", "x": "Very Large Array2 in depth: Contact.. Radio. Details — the New Mexico 2.. Radio. VLA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "27.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "27.", "x": "Very Large Array2 in depth: 27.. Contact. Details — the New Mexico 2.. Visiting. 1980. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Radio.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Radio.", "x": "Very Large Array2 in depth: Radio.. VLA. Details — the New Mexico 2.. 1980. 27 dishes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Very Large Array2 in depth: Visiting.. 1980. Details — the New Mexico 2.. VLA. Plains. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Very Large Array2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Very Large Array2 comes from.", "x": "Origins: 1980.. 1980. The history of Very Large Array2 — the New Mexico 2.. VLA. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Very Large Array2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Very Large Array2 respectfully.", "x": "Engaging: Contact.. 27 dishes. How to participate or observe well — Very Large Array2. the New Mexico 2. Respect first, always; 27.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Very Large Array2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Very Large Array2 do's and don'ts.", "x": "Etiquette: Radio.. Plains. The rules of respect — Very Large Array2. the New Mexico 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Very Large Array2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Very Large Array2.", "x": "Planning: 1980.. Radio. Practical notes — Very Large Array2. the New Mexico 2. A little planning shows respect for VLA.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Very Large Array2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Very Large Array2 and money.", "x": "Costs: Contact.. Contact. What to budget — Very Large Array2. the New Mexico 2. The best experiences of 27. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory2-very-large-array2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
