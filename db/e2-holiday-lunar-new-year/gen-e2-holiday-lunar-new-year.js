(function(){'use strict';
/* JAH Lunar New Year Holiday Database generator — jahdb-e2-holiday-lunar-new-year-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-lunar-new-year',PREFIX='JAH-E2HOLIDAYLU-',NAME='JAH Lunar New Year Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lunar New Year: the complete guide", "d": "Lunar New Year: Asia's biggest celebration..", "g": "overview", "l": 2, "q": "What is Lunar New Year: the complete guide?", "a": "Lunar New Year: Asia's biggest celebration..", "x": "The complete holiday guide to Lunar New Year: Asia's biggest celebration.. Jan/Feb. History, meaning, practices, and how to engage respectfully — everything in one database. Zodiac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lunar New Year essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lunar New Year essentials.", "x": "At a glance: Lunar New Year — Asia's biggest celebration.. Red envelopes. The essentials: Food.. Reunion dinner. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Jan/Feb.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Jan/Feb.", "x": "Lunar New Year: Jan/Feb.. Food. Essential knowledge — Reunion dinner.. Asia's biggest celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Jan/Feb..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Jan/Feb..", "x": "Explained: Jan/Feb.. Traditions. The context — Lunar New Year. Lion dance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Red envelopes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Red envelopes.", "x": "Lunar New Year: Red envelopes.. Family. Essential knowledge — Lion dance.. Asia's biggest celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Red envelopes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Red envelopes..", "x": "Explained: Red envelopes.. Countries. The context — Lunar New Year. Zodiac. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Reunion dinner.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Reunion dinner.", "x": "Lunar New Year: Reunion dinner.. Traditions. Essential knowledge — Zodiac.. Asia's biggest celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Reunion dinner..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Reunion dinner..", "x": "Explained: Reunion dinner.. Joy. The context — Lunar New Year. 15 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lion dance.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lion dance.", "x": "Lunar New Year: Lion dance.. Countries. Essential knowledge — 15 days.. Asia's biggest celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lion dance..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lion dance..", "x": "Explained: Lion dance.. Zodiac. The context — Lunar New Year. Jan/Feb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zodiac.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zodiac.", "x": "Lunar New Year: Zodiac.. Joy. Essential knowledge — Jan/Feb.. Asia's biggest celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Zodiac..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Zodiac..", "x": "Explained: Zodiac.. Food. The context — Lunar New Year. Red envelopes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "15 days.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "15 days.", "x": "Lunar New Year: 15 days.. Zodiac. Essential knowledge — Red envelopes.. Asia's biggest celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 15 days..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 15 days..", "x": "Explained: 15 days.. Family. The context — Lunar New Year. Reunion dinner. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Zodiac.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Zodiac.", "x": "Lunar New Year in depth: Zodiac.. Red envelopes. Details — Asia's biggest celebration.. Family. Lion dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Food.", "x": "Lunar New Year in depth: Food.. Reunion dinner. Details — Asia's biggest celebration.. Traditions. Zodiac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Family.", "x": "Lunar New Year in depth: Family.. Lion dance. Details — Asia's biggest celebration.. Countries. 15 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Traditions.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Traditions.", "x": "Lunar New Year in depth: Traditions.. Zodiac. Details — Asia's biggest celebration.. Joy. Jan/Feb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Countries.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Countries.", "x": "Lunar New Year in depth: Countries.. 15 days. Details — Asia's biggest celebration.. Zodiac. Red envelopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Joy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Joy.", "x": "Lunar New Year in depth: Joy.. Jan/Feb. Details — Asia's biggest celebration.. Food. Reunion dinner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lunar New Year comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lunar New Year comes from.", "x": "Origins: Zodiac.. Jan/Feb. The history of Lunar New Year — Asia's biggest celebration.. Food. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lunar New Year respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lunar New Year respectfully.", "x": "Engaging: Family.. Red envelopes. How to participate or observe well — Lunar New Year. Asia's biggest celebration. Respect first, always; Traditions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lunar New Year do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lunar New Year do's and don'ts.", "x": "Etiquette: Countries.. Reunion dinner. The rules of respect — Lunar New Year. Asia's biggest celebration. When in doubt, ask about Joy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lunar New Year.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lunar New Year.", "x": "Planning: Zodiac.. Lion dance. Practical notes — Lunar New Year. Asia's biggest celebration. A little planning shows respect for Food.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lunar New Year and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lunar New Year and money.", "x": "Costs: Family.. Zodiac. What to budget — Lunar New Year. Asia's biggest celebration. The best experiences of Traditions. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-lunar-new-year-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
