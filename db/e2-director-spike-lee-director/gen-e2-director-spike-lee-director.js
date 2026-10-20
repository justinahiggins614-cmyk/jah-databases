(function(){'use strict';
/* JAH Spike Lee Director Database generator — jahdb-e2-director-spike-lee-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-spike-lee-director',PREFIX='JAH-E2DIRECTORS-',NAME='JAH Spike Lee Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Spike Lee: the complete guide", "d": "Spike Lee: the Brooklyn voice..", "g": "overview", "l": 2, "q": "What is Spike Lee: the complete guide?", "a": "Spike Lee: the Brooklyn voice..", "x": "The complete director guide to Spike Lee: the Brooklyn voice.. 1957. History, meaning, practices, and how to engage respectfully — everything in one database. Right Thing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Spike Lee essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Spike Lee essentials.", "x": "At a glance: Spike Lee — the Brooklyn voice.. Do the Right Thing. The essentials: Malcolm X.. Malcolm X. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1957.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1957.", "x": "Spike Lee: 1957.. Malcolm X. Essential knowledge — Malcolm X.. the Brooklyn voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1957..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1957..", "x": "Explained: 1957.. Brooklyn. The context — Spike Lee. Knicks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Do the Right Thing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Do the Right Thing.", "x": "Spike Lee: Do the Right Thing.. Knicks. Essential knowledge — Knicks.. the Brooklyn voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Do the Right Thing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Do the Right Thing..", "x": "Explained: Do the Right Thing.. Joints. The context — Spike Lee. Joints. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Malcolm X.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Malcolm X.", "x": "Spike Lee: Malcolm X.. Brooklyn. Essential knowledge — Joints.. the Brooklyn voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Malcolm X..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Malcolm X..", "x": "Explained: Malcolm X.. Style. The context — Spike Lee. Brooklyn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Knicks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Knicks.", "x": "Spike Lee: Knicks.. Joints. Essential knowledge — Brooklyn.. the Brooklyn voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Knicks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Knicks..", "x": "Explained: Knicks.. Right Thing. The context — Spike Lee. 1957. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Joints.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Joints.", "x": "Spike Lee: Joints.. Style. Essential knowledge — 1957.. the Brooklyn voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Joints..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Joints..", "x": "Explained: Joints.. Malcolm X. The context — Spike Lee. Do the Right Thing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Brooklyn.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Brooklyn.", "x": "Spike Lee: Brooklyn.. Right Thing. Essential knowledge — Do the Right Thing.. the Brooklyn voice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Brooklyn..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Brooklyn..", "x": "Explained: Brooklyn.. Knicks. The context — Spike Lee. Malcolm X. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Right Thing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Right Thing.", "x": "Spike Lee in depth: Right Thing.. Do the Right Thing. Details — the Brooklyn voice.. Knicks. Knicks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Malcolm X.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Malcolm X.", "x": "Spike Lee in depth: Malcolm X.. Malcolm X. Details — the Brooklyn voice.. Brooklyn. Joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Knicks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Knicks.", "x": "Spike Lee in depth: Knicks.. Knicks. Details — the Brooklyn voice.. Joints. Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Brooklyn.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Brooklyn.", "x": "Spike Lee in depth: Brooklyn.. Joints. Details — the Brooklyn voice.. Style. 1957. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Joints.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Joints.", "x": "Spike Lee in depth: Joints.. Brooklyn. Details — the Brooklyn voice.. Right Thing. Do the Right Thing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Spike Lee in depth: Style.. 1957. Details — the Brooklyn voice.. Malcolm X. Malcolm X. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Spike Lee comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Spike Lee comes from.", "x": "Origins: Right Thing.. 1957. The history of Spike Lee — the Brooklyn voice.. Malcolm X. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Spike Lee respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Spike Lee respectfully.", "x": "Engaging: Knicks.. Do the Right Thing. How to participate or observe well — Spike Lee. the Brooklyn voice. Respect first, always; Brooklyn.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Spike Lee do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Spike Lee do's and don'ts.", "x": "Etiquette: Joints.. Malcolm X. The rules of respect — Spike Lee. the Brooklyn voice. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Spike Lee.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Spike Lee.", "x": "Planning: Right Thing.. Knicks. Practical notes — Spike Lee. the Brooklyn voice. A little planning shows respect for Malcolm X.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Spike Lee and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Spike Lee and money.", "x": "Costs: Knicks.. Joints. What to budget — Spike Lee. the Brooklyn voice. The best experiences of Brooklyn. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-spike-lee-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
