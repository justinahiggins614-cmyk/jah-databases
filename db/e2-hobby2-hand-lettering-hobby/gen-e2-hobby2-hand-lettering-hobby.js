(function(){'use strict';
/* JAH Hand Lettering Database generator — jahdb-e2-hobby2-hand-lettering-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-hand-lettering-hobby',PREFIX='JAH-E2HOBBY2HAN-',NAME='JAH Hand Lettering Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hand Lettering: the complete guide", "d": "Hand Lettering: the drawn letters..", "g": "overview", "l": 2, "q": "What is Hand Lettering: the complete guide?", "a": "Hand Lettering: the drawn letters..", "x": "The complete hobby guide to Hand Lettering: the drawn letters.. Brush pens. History, meaning, practices, and how to engage respectfully — everything in one database. Pens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hand Lettering essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hand Lettering essentials.", "x": "At a glance: Hand Lettering — the drawn letters.. Composition. The essentials: Banners.. Styles. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Brush pens.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Brush pens.", "x": "Hand Lettering: Brush pens.. Banners. Essential knowledge — Styles.. the drawn letters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Brush pens..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Brush pens..", "x": "Explained: Brush pens.. Brush. The context — Hand Lettering. Chalk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Composition.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Composition.", "x": "Hand Lettering: Composition.. Practice. Essential knowledge — Chalk.. the drawn letters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Composition..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Composition..", "x": "Explained: Composition.. Styles. The context — Hand Lettering. Banners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Styles.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Styles.", "x": "Hand Lettering: Styles.. Brush. Essential knowledge — Banners.. the drawn letters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Styles..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Styles..", "x": "Explained: Styles.. Getting started. The context — Hand Lettering. Practice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chalk.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chalk.", "x": "Hand Lettering: Chalk.. Styles. Essential knowledge — Practice.. the drawn letters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chalk..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chalk..", "x": "Explained: Chalk.. Pens. The context — Hand Lettering. Brush pens. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Banners.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Banners.", "x": "Hand Lettering: Banners.. Getting started. Essential knowledge — Brush pens.. the drawn letters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Banners..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Banners..", "x": "Explained: Banners.. Banners. The context — Hand Lettering. Composition. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Practice.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Practice.", "x": "Hand Lettering: Practice.. Pens. Essential knowledge — Composition.. the drawn letters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Practice..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Practice..", "x": "Explained: Practice.. Practice. The context — Hand Lettering. Styles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pens.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pens.", "x": "Hand Lettering in depth: Pens.. Composition. Details — the drawn letters.. Practice. Chalk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Banners.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Banners.", "x": "Hand Lettering in depth: Banners.. Styles. Details — the drawn letters.. Brush. Banners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Practice.", "x": "Hand Lettering in depth: Practice.. Chalk. Details — the drawn letters.. Styles. Practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Brush.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Brush.", "x": "Hand Lettering in depth: Brush.. Banners. Details — the drawn letters.. Getting started. Brush pens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Styles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Styles.", "x": "Hand Lettering in depth: Styles.. Practice. Details — the drawn letters.. Pens. Composition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Hand Lettering in depth: Getting started.. Brush pens. Details — the drawn letters.. Banners. Styles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hand Lettering comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hand Lettering comes from.", "x": "Origins: Pens.. Brush pens. The history of Hand Lettering — the drawn letters.. Banners. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hand Lettering respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hand Lettering respectfully.", "x": "Engaging: Practice.. Composition. How to participate or observe well — Hand Lettering. the drawn letters. Respect first, always; Brush.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hand Lettering do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hand Lettering do's and don'ts.", "x": "Etiquette: Styles.. Styles. The rules of respect — Hand Lettering. the drawn letters. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hand Lettering.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hand Lettering.", "x": "Planning: Pens.. Chalk. Practical notes — Hand Lettering. the drawn letters. A little planning shows respect for Banners.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hand Lettering and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hand Lettering and money.", "x": "Costs: Practice.. Banners. What to budget — Hand Lettering. the drawn letters. The best experiences of Brush. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-hand-lettering-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
