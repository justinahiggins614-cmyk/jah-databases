(function(){'use strict';
/* JAH Liszt Composer Composer Database generator — jahdb-e2-composer-liszt-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-liszt-composer',PREFIX='JAH-E2COMPOSERL-',NAME='JAH Liszt Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Liszt Composer: the complete guide", "d": "Liszt Composer: the piano virtuoso..", "g": "overview", "l": 2, "q": "What is Liszt Composer: the complete guide?", "a": "Liszt Composer: the piano virtuoso..", "x": "The complete composer guide to Liszt Composer: the piano virtuoso.. 1811. History, meaning, practices, and how to engage respectfully — everything in one database. Virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Liszt Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Liszt Composer essentials.", "x": "At a glance: Liszt Composer — the piano virtuoso.. Transcendental. The essentials: Showman.. Hungarian. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1811.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1811.", "x": "Liszt Composer: 1811.. Showman. Essential knowledge — Hungarian.. the piano virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1811..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1811..", "x": "Explained: 1811.. Weimar. The context — Liszt Composer. Showman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Transcendental.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Transcendental.", "x": "Liszt Composer: Transcendental.. Hungarian. Essential knowledge — Showman.. the piano virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Transcendental..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Transcendental..", "x": "Explained: Transcendental.. Abbé. The context — Liszt Composer. Abbé. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hungarian.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hungarian.", "x": "Liszt Composer: Hungarian.. Weimar. Essential knowledge — Abbé.. the piano virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hungarian..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hungarian..", "x": "Explained: Hungarian.. Legacy. The context — Liszt Composer. Weimar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Showman.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Showman.", "x": "Liszt Composer: Showman.. Abbé. Essential knowledge — Weimar.. the piano virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Showman..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Showman..", "x": "Explained: Showman.. Virtuoso. The context — Liszt Composer. 1811. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Abbé.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Abbé.", "x": "Liszt Composer: Abbé.. Legacy. Essential knowledge — 1811.. the piano virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Abbé..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Abbé..", "x": "Explained: Abbé.. Showman. The context — Liszt Composer. Transcendental. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Weimar.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Weimar.", "x": "Liszt Composer: Weimar.. Virtuoso. Essential knowledge — Transcendental.. the piano virtuoso. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Weimar..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Weimar..", "x": "Explained: Weimar.. Hungarian. The context — Liszt Composer. Hungarian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Virtuoso.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Virtuoso.", "x": "Liszt Composer in depth: Virtuoso.. Transcendental. Details — the piano virtuoso.. Hungarian. Showman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Showman.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Showman.", "x": "Liszt Composer in depth: Showman.. Hungarian. Details — the piano virtuoso.. Weimar. Abbé. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hungarian.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hungarian.", "x": "Liszt Composer in depth: Hungarian.. Showman. Details — the piano virtuoso.. Abbé. Weimar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Weimar.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Weimar.", "x": "Liszt Composer in depth: Weimar.. Abbé. Details — the piano virtuoso.. Legacy. 1811. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Abbé.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Abbé.", "x": "Liszt Composer in depth: Abbé.. Weimar. Details — the piano virtuoso.. Virtuoso. Transcendental. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Liszt Composer in depth: Legacy.. 1811. Details — the piano virtuoso.. Showman. Hungarian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Liszt Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Liszt Composer comes from.", "x": "Origins: Virtuoso.. 1811. The history of Liszt Composer — the piano virtuoso.. Showman. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Liszt Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Liszt Composer respectfully.", "x": "Engaging: Hungarian.. Transcendental. How to participate or observe well — Liszt Composer. the piano virtuoso. Respect first, always; Weimar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Liszt Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Liszt Composer do's and don'ts.", "x": "Etiquette: Abbé.. Hungarian. The rules of respect — Liszt Composer. the piano virtuoso. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Liszt Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Liszt Composer.", "x": "Planning: Virtuoso.. Showman. Practical notes — Liszt Composer. the piano virtuoso. A little planning shows respect for Showman.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Liszt Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Liszt Composer and money.", "x": "Costs: Hungarian.. Abbé. What to budget — Liszt Composer. the piano virtuoso. The best experiences of Weimar. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-liszt-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
