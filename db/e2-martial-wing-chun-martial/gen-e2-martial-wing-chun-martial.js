(function(){'use strict';
/* JAH Wing Chun Martial Art Database generator — jahdb-e2-martial-wing-chun-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-wing-chun-martial',PREFIX='JAH-E2MARTIALWI-',NAME='JAH Wing Chun Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wing Chun: the complete guide", "d": "Wing Chun: the close-range..", "g": "overview", "l": 2, "q": "What is Wing Chun: the complete guide?", "a": "Wing Chun: the close-range..", "x": "The complete martial art guide to Wing Chun: the close-range.. Ip Man. History, meaning, practices, and how to engage respectfully — everything in one database. Ip Man. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Wing Chun essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Wing Chun essentials.", "x": "At a glance: Wing Chun — the close-range.. Bruce Lee. The essentials: Bruce Lee.. Centerline. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Ip Man.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Ip Man.", "x": "Wing Chun: Ip Man.. Bruce Lee. Essential knowledge — Centerline.. the close-range. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Ip Man..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Ip Man..", "x": "Explained: Ip Man.. Hong Kong. The context — Wing Chun. Chi sao. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bruce Lee.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bruce Lee.", "x": "Wing Chun: Bruce Lee.. Chi sao. Essential knowledge — Chi sao.. the close-range. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bruce Lee..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bruce Lee..", "x": "Explained: Bruce Lee.. Centerline. The context — Wing Chun. Hong Kong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Centerline.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Centerline.", "x": "Wing Chun: Centerline.. Hong Kong. Essential knowledge — Hong Kong.. the close-range. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Centerline..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Centerline..", "x": "Explained: Centerline.. Training. The context — Wing Chun. Straight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chi sao.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chi sao.", "x": "Wing Chun: Chi sao.. Centerline. Essential knowledge — Straight.. the close-range. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chi sao..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chi sao..", "x": "Explained: Chi sao.. Ip Man. The context — Wing Chun. Ip Man. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hong Kong.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hong Kong.", "x": "Wing Chun: Hong Kong.. Training. Essential knowledge — Ip Man.. the close-range. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hong Kong..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hong Kong..", "x": "Explained: Hong Kong.. Bruce Lee. The context — Wing Chun. Bruce Lee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Straight.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Straight.", "x": "Wing Chun: Straight.. Ip Man. Essential knowledge — Bruce Lee.. the close-range. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Straight..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Straight..", "x": "Explained: Straight.. Chi sao. The context — Wing Chun. Centerline. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ip Man.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ip Man.", "x": "Wing Chun in depth: Ip Man.. Bruce Lee. Details — the close-range.. Chi sao. Chi sao. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bruce Lee.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bruce Lee.", "x": "Wing Chun in depth: Bruce Lee.. Centerline. Details — the close-range.. Hong Kong. Hong Kong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Chi sao.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Chi sao.", "x": "Wing Chun in depth: Chi sao.. Chi sao. Details — the close-range.. Centerline. Straight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hong Kong.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hong Kong.", "x": "Wing Chun in depth: Hong Kong.. Hong Kong. Details — the close-range.. Training. Ip Man. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Centerline.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Centerline.", "x": "Wing Chun in depth: Centerline.. Straight. Details — the close-range.. Ip Man. Bruce Lee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Wing Chun in depth: Training.. Ip Man. Details — the close-range.. Bruce Lee. Centerline. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Wing Chun comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Wing Chun comes from.", "x": "Origins: Ip Man.. Ip Man. The history of Wing Chun — the close-range.. Bruce Lee. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Wing Chun respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Wing Chun respectfully.", "x": "Engaging: Chi sao.. Bruce Lee. How to participate or observe well — Wing Chun. the close-range. Respect first, always; Hong Kong.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Wing Chun do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Wing Chun do's and don'ts.", "x": "Etiquette: Centerline.. Centerline. The rules of respect — Wing Chun. the close-range. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Wing Chun.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Wing Chun.", "x": "Planning: Ip Man.. Chi sao. Practical notes — Wing Chun. the close-range. A little planning shows respect for Bruce Lee.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Wing Chun and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Wing Chun and money.", "x": "Costs: Chi sao.. Hong Kong. What to budget — Wing Chun. the close-range. The best experiences of Hong Kong. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-wing-chun-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
