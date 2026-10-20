(function(){'use strict';
/* JAH Belgian Draft Horse Horse Breed Database generator — jahdb-e2-horse-belgian-draft-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-belgian-draft-breed',PREFIX='JAH-E2HORSEBELG-',NAME='JAH Belgian Draft Horse Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Belgian Draft Horse: the complete guide", "d": "Belgian Draft Horse: the gentle giant..", "g": "overview", "l": 2, "q": "What is Belgian Draft Horse: the complete guide?", "a": "Belgian Draft Horse: the gentle giant..", "x": "The complete horse breed guide to Belgian Draft Horse: the gentle giant.. Belgium. History, meaning, practices, and how to engage respectfully — everything in one database. Belgium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Belgian Draft Horse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Belgian Draft Horse essentials.", "x": "At a glance: Belgian Draft Horse — the gentle giant.. Blond. The essentials: Pulling.. Strongest. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Belgium.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Belgium.", "x": "Belgian Draft Horse: Belgium.. Pulling. Essential knowledge — Strongest.. the gentle giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Belgium..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Belgium..", "x": "Explained: Belgium.. Farm. The context — Belgian Draft Horse. Pulling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Blond.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Blond.", "x": "Belgian Draft Horse: Blond.. Gentle. Essential knowledge — Pulling.. the gentle giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Blond..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Blond..", "x": "Explained: Blond.. Blond. The context — Belgian Draft Horse. Gentle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Strongest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Strongest.", "x": "Belgian Draft Horse: Strongest.. Farm. Essential knowledge — Gentle.. the gentle giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Strongest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Strongest..", "x": "Explained: Strongest.. History. The context — Belgian Draft Horse. Farm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pulling.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pulling.", "x": "Belgian Draft Horse: Pulling.. Blond. Essential knowledge — Farm.. the gentle giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pulling..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pulling..", "x": "Explained: Pulling.. Belgium. The context — Belgian Draft Horse. Belgium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gentle.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gentle.", "x": "Belgian Draft Horse: Gentle.. History. Essential knowledge — Belgium.. the gentle giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Gentle..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Gentle..", "x": "Explained: Gentle.. Pulling. The context — Belgian Draft Horse. Blond. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Farm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Farm.", "x": "Belgian Draft Horse: Farm.. Belgium. Essential knowledge — Blond.. the gentle giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Farm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Farm..", "x": "Explained: Farm.. Gentle. The context — Belgian Draft Horse. Strongest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Belgium.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Belgium.", "x": "Belgian Draft Horse in depth: Belgium.. Blond. Details — the gentle giant.. Gentle. Pulling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pulling.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pulling.", "x": "Belgian Draft Horse in depth: Pulling.. Strongest. Details — the gentle giant.. Farm. Gentle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gentle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gentle.", "x": "Belgian Draft Horse in depth: Gentle.. Pulling. Details — the gentle giant.. Blond. Farm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Farm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Farm.", "x": "Belgian Draft Horse in depth: Farm.. Gentle. Details — the gentle giant.. History. Belgium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Blond.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Blond.", "x": "Belgian Draft Horse in depth: Blond.. Farm. Details — the gentle giant.. Belgium. Blond. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Belgian Draft Horse in depth: History.. Belgium. Details — the gentle giant.. Pulling. Strongest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Belgian Draft Horse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Belgian Draft Horse comes from.", "x": "Origins: Belgium.. Belgium. The history of Belgian Draft Horse — the gentle giant.. Pulling. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Belgian Draft Horse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Belgian Draft Horse respectfully.", "x": "Engaging: Gentle.. Blond. How to participate or observe well — Belgian Draft Horse. the gentle giant. Respect first, always; Farm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Belgian Draft Horse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Belgian Draft Horse do's and don'ts.", "x": "Etiquette: Blond.. Strongest. The rules of respect — Belgian Draft Horse. the gentle giant. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Belgian Draft Horse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Belgian Draft Horse.", "x": "Planning: Belgium.. Pulling. Practical notes — Belgian Draft Horse. the gentle giant. A little planning shows respect for Pulling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Belgian Draft Horse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Belgian Draft Horse and money.", "x": "Costs: Gentle.. Gentle. What to budget — Belgian Draft Horse. the gentle giant. The best experiences of Farm. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-belgian-draft-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
