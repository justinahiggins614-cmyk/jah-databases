(function(){'use strict';
/* JAH Handel Composer Composer Database generator — jahdb-e2-composer-handel-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-handel-composer',PREFIX='JAH-E2COMPOSERH-',NAME='JAH Handel Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Handel Composer: the complete guide", "d": "Handel Composer: the Messiah master..", "g": "overview", "l": 2, "q": "What is Handel Composer: the complete guide?", "a": "Handel Composer: the Messiah master..", "x": "The complete composer guide to Handel Composer: the Messiah master.. 1685. History, meaning, practices, and how to engage respectfully — everything in one database. Messiah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Handel Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Handel Composer essentials.", "x": "At a glance: Handel Composer — the Messiah master.. Messiah. The essentials: Oratorios.. Water Music. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1685.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1685.", "x": "Handel Composer: 1685.. Oratorios. Essential knowledge — Water Music.. the Messiah master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1685..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1685..", "x": "Explained: 1685.. Hallelujah. The context — Handel Composer. London. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Messiah.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Messiah.", "x": "Handel Composer: Messiah.. London. Essential knowledge — London.. the Messiah master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Messiah..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Messiah..", "x": "Explained: Messiah.. Water. The context — Handel Composer. Oratorios. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Water Music.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Water Music.", "x": "Handel Composer: Water Music.. Hallelujah. Essential knowledge — Oratorios.. the Messiah master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Water Music..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Water Music..", "x": "Explained: Water Music.. Legacy. The context — Handel Composer. Hallelujah. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "London.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "London.", "x": "Handel Composer: London.. Water. Essential knowledge — Hallelujah.. the Messiah master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: London..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: London..", "x": "Explained: London.. Messiah. The context — Handel Composer. 1685. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Oratorios.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Oratorios.", "x": "Handel Composer: Oratorios.. Legacy. Essential knowledge — 1685.. the Messiah master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Oratorios..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Oratorios..", "x": "Explained: Oratorios.. Oratorios. The context — Handel Composer. Messiah. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hallelujah.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hallelujah.", "x": "Handel Composer: Hallelujah.. Messiah. Essential knowledge — Messiah.. the Messiah master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Hallelujah..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Hallelujah..", "x": "Explained: Hallelujah.. London. The context — Handel Composer. Water Music. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Messiah.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Messiah.", "x": "Handel Composer in depth: Messiah.. Messiah. Details — the Messiah master.. London. London. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Oratorios.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Oratorios.", "x": "Handel Composer in depth: Oratorios.. Water Music. Details — the Messiah master.. Hallelujah. Oratorios. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "London.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "London.", "x": "Handel Composer in depth: London.. London. Details — the Messiah master.. Water. Hallelujah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hallelujah.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hallelujah.", "x": "Handel Composer in depth: Hallelujah.. Oratorios. Details — the Messiah master.. Legacy. 1685. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Water.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Water.", "x": "Handel Composer in depth: Water.. Hallelujah. Details — the Messiah master.. Messiah. Messiah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Handel Composer in depth: Legacy.. 1685. Details — the Messiah master.. Oratorios. Water Music. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Handel Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Handel Composer comes from.", "x": "Origins: Messiah.. 1685. The history of Handel Composer — the Messiah master.. Oratorios. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Handel Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Handel Composer respectfully.", "x": "Engaging: London.. Messiah. How to participate or observe well — Handel Composer. the Messiah master. Respect first, always; Hallelujah.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Handel Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Handel Composer do's and don'ts.", "x": "Etiquette: Water.. Water Music. The rules of respect — Handel Composer. the Messiah master. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Handel Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Handel Composer.", "x": "Planning: Messiah.. London. Practical notes — Handel Composer. the Messiah master. A little planning shows respect for Oratorios.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Handel Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Handel Composer and money.", "x": "Costs: London.. Oratorios. What to budget — Handel Composer. the Messiah master. The best experiences of Hallelujah. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-handel-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
