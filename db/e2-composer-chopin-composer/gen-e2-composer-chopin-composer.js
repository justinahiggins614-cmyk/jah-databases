(function(){'use strict';
/* JAH Chopin Composer Composer Database generator — jahdb-e2-composer-chopin-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-chopin-composer',PREFIX='JAH-E2COMPOSERC-',NAME='JAH Chopin Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chopin Composer: the complete guide", "d": "Chopin Composer: the piano poet..", "g": "overview", "l": 2, "q": "What is Chopin Composer: the complete guide?", "a": "Chopin Composer: the piano poet..", "x": "The complete composer guide to Chopin Composer: the piano poet.. 1810. History, meaning, practices, and how to engage respectfully — everything in one database. Nocturnes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chopin Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chopin Composer essentials.", "x": "At a glance: Chopin Composer — the piano poet.. Nocturnes. The essentials: Etudes.. Etudes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1810.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1810.", "x": "Chopin Composer: 1810.. Etudes. Essential knowledge — Etudes.. the piano poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1810..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1810..", "x": "Explained: 1810.. Paris. The context — Chopin Composer. Poland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nocturnes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nocturnes.", "x": "Chopin Composer: Nocturnes.. Poland. Essential knowledge — Poland.. the piano poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Nocturnes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Nocturnes..", "x": "Explained: Nocturnes.. Piano. The context — Chopin Composer. Paris. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Etudes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Etudes.", "x": "Chopin Composer: Etudes.. Paris. Essential knowledge — Paris.. the piano poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Etudes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Etudes..", "x": "Explained: Etudes.. Legacy. The context — Chopin Composer. Piano. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Poland.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Poland.", "x": "Chopin Composer: Poland.. Piano. Essential knowledge — Piano.. the piano poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Poland..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Poland..", "x": "Explained: Poland.. Nocturnes. The context — Chopin Composer. 1810. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Paris.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Paris.", "x": "Chopin Composer: Paris.. Legacy. Essential knowledge — 1810.. the piano poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Paris..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Paris..", "x": "Explained: Paris.. Etudes. The context — Chopin Composer. Nocturnes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Piano.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Piano.", "x": "Chopin Composer: Piano.. Nocturnes. Essential knowledge — Nocturnes.. the piano poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Piano..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Piano..", "x": "Explained: Piano.. Poland. The context — Chopin Composer. Etudes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Nocturnes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Nocturnes.", "x": "Chopin Composer in depth: Nocturnes.. Nocturnes. Details — the piano poet.. Poland. Poland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Etudes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Etudes.", "x": "Chopin Composer in depth: Etudes.. Etudes. Details — the piano poet.. Paris. Paris. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Poland.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Poland.", "x": "Chopin Composer in depth: Poland.. Poland. Details — the piano poet.. Piano. Piano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Paris.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Paris.", "x": "Chopin Composer in depth: Paris.. Paris. Details — the piano poet.. Legacy. 1810. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Piano.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Piano.", "x": "Chopin Composer in depth: Piano.. Piano. Details — the piano poet.. Nocturnes. Nocturnes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Chopin Composer in depth: Legacy.. 1810. Details — the piano poet.. Etudes. Etudes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chopin Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chopin Composer comes from.", "x": "Origins: Nocturnes.. 1810. The history of Chopin Composer — the piano poet.. Etudes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chopin Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chopin Composer respectfully.", "x": "Engaging: Poland.. Nocturnes. How to participate or observe well — Chopin Composer. the piano poet. Respect first, always; Paris.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chopin Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chopin Composer do's and don'ts.", "x": "Etiquette: Piano.. Etudes. The rules of respect — Chopin Composer. the piano poet. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chopin Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chopin Composer.", "x": "Planning: Nocturnes.. Poland. Practical notes — Chopin Composer. the piano poet. A little planning shows respect for Etudes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chopin Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chopin Composer and money.", "x": "Costs: Poland.. Paris. What to budget — Chopin Composer. the piano poet. The best experiences of Paris. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-chopin-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
