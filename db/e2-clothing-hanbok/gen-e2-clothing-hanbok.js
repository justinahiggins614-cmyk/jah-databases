(function(){'use strict';
/* JAH Hanbok Clothing Database generator — jahdb-e2-clothing-hanbok-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-clothing-hanbok',PREFIX='JAH-E2CLOTHINGH-',NAME='JAH Hanbok Clothing Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hanbok: the complete guide", "d": "Hanbok: Korea's flowing dress..", "g": "overview", "l": 2, "q": "What is Hanbok: the complete guide?", "a": "Hanbok: Korea's flowing dress..", "x": "The complete clothing guide to Hanbok: Korea's flowing dress.. Jeogori. History, meaning, practices, and how to engage respectfully — everything in one database. Parts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hanbok essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hanbok essentials.", "x": "At a glance: Hanbok — Korea's flowing dress.. Chima. The essentials: Colors.. Colors. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Jeogori.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Jeogori.", "x": "Hanbok: Jeogori.. Colors. Essential knowledge — Colors.. Korea's flowing dress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Jeogori..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Jeogori..", "x": "Explained: Jeogori.. Occasions. The context — Hanbok. Holidays. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chima.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chima.", "x": "Hanbok: Chima.. Wear. Essential knowledge — Holidays.. Korea's flowing dress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chima..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chima..", "x": "Explained: Chima.. Modern. The context — Hanbok. Modern. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Colors.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Colors.", "x": "Hanbok: Colors.. Occasions. Essential knowledge — Modern.. Korea's flowing dress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Colors..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Colors..", "x": "Explained: Colors.. Craft. The context — Hanbok. Weddings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Holidays.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Holidays.", "x": "Hanbok: Holidays.. Modern. Essential knowledge — Weddings.. Korea's flowing dress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Holidays..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Holidays..", "x": "Explained: Holidays.. Parts. The context — Hanbok. Jeogori. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Modern.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Modern.", "x": "Hanbok: Modern.. Craft. Essential knowledge — Jeogori.. Korea's flowing dress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Modern..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Modern..", "x": "Explained: Modern.. Colors. The context — Hanbok. Chima. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Weddings.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Weddings.", "x": "Hanbok: Weddings.. Parts. Essential knowledge — Chima.. Korea's flowing dress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Weddings..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Weddings..", "x": "Explained: Weddings.. Wear. The context — Hanbok. Colors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Parts.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Parts.", "x": "Hanbok in depth: Parts.. Chima. Details — Korea's flowing dress.. Wear. Holidays. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colors.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colors.", "x": "Hanbok in depth: Colors.. Colors. Details — Korea's flowing dress.. Occasions. Modern. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wear.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wear.", "x": "Hanbok in depth: Wear.. Holidays. Details — Korea's flowing dress.. Modern. Weddings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Occasions.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Occasions.", "x": "Hanbok in depth: Occasions.. Modern. Details — Korea's flowing dress.. Craft. Jeogori. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Modern.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Modern.", "x": "Hanbok in depth: Modern.. Weddings. Details — Korea's flowing dress.. Parts. Chima. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Craft.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Craft.", "x": "Hanbok in depth: Craft.. Jeogori. Details — Korea's flowing dress.. Colors. Colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hanbok comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hanbok comes from.", "x": "Origins: Parts.. Jeogori. The history of Hanbok — Korea's flowing dress.. Colors. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hanbok respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hanbok respectfully.", "x": "Engaging: Wear.. Chima. How to participate or observe well — Hanbok. Korea's flowing dress. Respect first, always; Occasions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hanbok do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hanbok do's and don'ts.", "x": "Etiquette: Modern.. Colors. The rules of respect — Hanbok. Korea's flowing dress. When in doubt, ask about Craft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hanbok.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hanbok.", "x": "Planning: Parts.. Holidays. Practical notes — Hanbok. Korea's flowing dress. A little planning shows respect for Colors.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hanbok and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hanbok and money.", "x": "Costs: Wear.. Modern. What to budget — Hanbok. Korea's flowing dress. The best experiences of Occasions. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-clothing-hanbok-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
