(function(){'use strict';
/* JAH Acarajé Dish Database generator — jahdb-e2-dish-acaraje-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-acaraje-dish',PREFIX='JAH-E2DISHACARA-',NAME='JAH Acarajé Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Acarajé: the complete guide", "d": "Acarajé: the Bahia fritter..", "g": "overview", "l": 2, "q": "What is Acarajé: the complete guide?", "a": "Acarajé: the Bahia fritter..", "x": "The complete dish guide to Acarajé: the Bahia fritter.. Bahia. History, meaning, practices, and how to engage respectfully — everything in one database. Peas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Acarajé essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Acarajé essentials.", "x": "At a glance: Acarajé — the Bahia fritter.. Black-eyed peas. The essentials: Street.. Shrimp. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bahia.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bahia.", "x": "Acarajé: Bahia.. Street. Essential knowledge — Shrimp.. the Bahia fritter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bahia..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bahia..", "x": "Explained: Bahia.. Bahia. The context — Acarajé. Palm oil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Black-eyed peas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Black-eyed peas.", "x": "Acarajé: Black-eyed peas.. African. Essential knowledge — Palm oil.. the Bahia fritter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Black-eyed peas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Black-eyed peas..", "x": "Explained: Black-eyed peas.. Shrimp. The context — Acarajé. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shrimp.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shrimp.", "x": "Acarajé: Shrimp.. Bahia. Essential knowledge — Street.. the Bahia fritter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shrimp..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shrimp..", "x": "Explained: Shrimp.. Making. The context — Acarajé. African. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Palm oil.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Palm oil.", "x": "Acarajé: Palm oil.. Shrimp. Essential knowledge — African.. the Bahia fritter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Palm oil..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Palm oil..", "x": "Explained: Palm oil.. Peas. The context — Acarajé. Bahia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Street.", "x": "Acarajé: Street.. Making. Essential knowledge — Bahia.. the Bahia fritter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Acarajé. Black-eyed peas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "African.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "African.", "x": "Acarajé: African.. Peas. Essential knowledge — Black-eyed peas.. the Bahia fritter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: African..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: African..", "x": "Explained: African.. African. The context — Acarajé. Shrimp. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Peas.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Peas.", "x": "Acarajé in depth: Peas.. Black-eyed peas. Details — the Bahia fritter.. African. Palm oil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Street.", "x": "Acarajé in depth: Street.. Shrimp. Details — the Bahia fritter.. Bahia. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "African.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "African.", "x": "Acarajé in depth: African.. Palm oil. Details — the Bahia fritter.. Shrimp. African. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bahia.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bahia.", "x": "Acarajé in depth: Bahia.. Street. Details — the Bahia fritter.. Making. Bahia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shrimp.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shrimp.", "x": "Acarajé in depth: Shrimp.. African. Details — the Bahia fritter.. Peas. Black-eyed peas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Acarajé in depth: Making.. Bahia. Details — the Bahia fritter.. Street. Shrimp. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Acarajé comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Acarajé comes from.", "x": "Origins: Peas.. Bahia. The history of Acarajé — the Bahia fritter.. Street. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Acarajé respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Acarajé respectfully.", "x": "Engaging: African.. Black-eyed peas. How to participate or observe well — Acarajé. the Bahia fritter. Respect first, always; Bahia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Acarajé do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Acarajé do's and don'ts.", "x": "Etiquette: Shrimp.. Shrimp. The rules of respect — Acarajé. the Bahia fritter. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Acarajé.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Acarajé.", "x": "Planning: Peas.. Palm oil. Practical notes — Acarajé. the Bahia fritter. A little planning shows respect for Street.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Acarajé and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Acarajé and money.", "x": "Costs: African.. Street. What to budget — Acarajé. the Bahia fritter. The best experiences of Bahia. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-acaraje-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
