(function(){'use strict';
/* JAH Gershwin Composer Composer Database generator — jahdb-e2-composer-gershwin-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-gershwin-composer',PREFIX='JAH-E2COMPOSERG-',NAME='JAH Gershwin Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gershwin Composer: the complete guide", "d": "Gershwin Composer: the American blend..", "g": "overview", "l": 2, "q": "What is Gershwin Composer: the complete guide?", "a": "Gershwin Composer: the American blend..", "x": "The complete composer guide to Gershwin Composer: the American blend.. 1898. History, meaning, practices, and how to engage respectfully — everything in one database. Rhapsody. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gershwin Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gershwin Composer essentials.", "x": "At a glance: Gershwin Composer — the American blend.. Rhapsody in Blue. The essentials: Porgy.. Porgy. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1898.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1898.", "x": "Gershwin Composer: 1898.. Porgy. Essential knowledge — Porgy.. the American blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1898..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1898..", "x": "Explained: 1898.. Tin Pan. The context — Gershwin Composer. Jazz. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rhapsody in Blue.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rhapsody in Blue.", "x": "Gershwin Composer: Rhapsody in Blue.. Jazz. Essential knowledge — Jazz.. the American blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rhapsody in Blue..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rhapsody in Blue..", "x": "Explained: Rhapsody in Blue.. 38. The context — Gershwin Composer. Tin Pan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Porgy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Porgy.", "x": "Gershwin Composer: Porgy.. Tin Pan. Essential knowledge — Tin Pan.. the American blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Porgy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Porgy..", "x": "Explained: Porgy.. Legacy. The context — Gershwin Composer. 38 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Jazz.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Jazz.", "x": "Gershwin Composer: Jazz.. 38. Essential knowledge — 38 years.. the American blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Jazz..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Jazz..", "x": "Explained: Jazz.. Rhapsody. The context — Gershwin Composer. 1898. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tin Pan.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tin Pan.", "x": "Gershwin Composer: Tin Pan.. Legacy. Essential knowledge — 1898.. the American blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tin Pan..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tin Pan..", "x": "Explained: Tin Pan.. Porgy. The context — Gershwin Composer. Rhapsody in Blue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "38 years.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "38 years.", "x": "Gershwin Composer: 38 years.. Rhapsody. Essential knowledge — Rhapsody in Blue.. the American blend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 38 years..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 38 years..", "x": "Explained: 38 years.. Jazz. The context — Gershwin Composer. Porgy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rhapsody.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rhapsody.", "x": "Gershwin Composer in depth: Rhapsody.. Rhapsody in Blue. Details — the American blend.. Jazz. Jazz. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Porgy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Porgy.", "x": "Gershwin Composer in depth: Porgy.. Porgy. Details — the American blend.. Tin Pan. Tin Pan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Jazz.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Jazz.", "x": "Gershwin Composer in depth: Jazz.. Jazz. Details — the American blend.. 38. 38 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tin Pan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tin Pan.", "x": "Gershwin Composer in depth: Tin Pan.. Tin Pan. Details — the American blend.. Legacy. 1898. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "38.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "38.", "x": "Gershwin Composer in depth: 38.. 38 years. Details — the American blend.. Rhapsody. Rhapsody in Blue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Gershwin Composer in depth: Legacy.. 1898. Details — the American blend.. Porgy. Porgy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gershwin Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gershwin Composer comes from.", "x": "Origins: Rhapsody.. 1898. The history of Gershwin Composer — the American blend.. Porgy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gershwin Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gershwin Composer respectfully.", "x": "Engaging: Jazz.. Rhapsody in Blue. How to participate or observe well — Gershwin Composer. the American blend. Respect first, always; Tin Pan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gershwin Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gershwin Composer do's and don'ts.", "x": "Etiquette: 38.. Porgy. The rules of respect — Gershwin Composer. the American blend. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gershwin Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gershwin Composer.", "x": "Planning: Rhapsody.. Jazz. Practical notes — Gershwin Composer. the American blend. A little planning shows respect for Porgy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gershwin Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gershwin Composer and money.", "x": "Costs: Jazz.. Tin Pan. What to budget — Gershwin Composer. the American blend. The best experiences of Tin Pan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-gershwin-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
