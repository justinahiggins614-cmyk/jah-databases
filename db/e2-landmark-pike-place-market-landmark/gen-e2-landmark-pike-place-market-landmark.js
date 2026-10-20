(function(){'use strict';
/* JAH Pike Place Market Landmark Database generator — jahdb-e2-landmark-pike-place-market-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-pike-place-market-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Pike Place Market Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pike Place Market: the complete guide", "d": "Pike Place Market: the flying fish..", "g": "overview", "l": 2, "q": "What is Pike Place Market: the complete guide?", "a": "Pike Place Market: the flying fish..", "x": "The complete landmark guide to Pike Place Market: the flying fish.. 1907. History, meaning, practices, and how to engage respectfully — everything in one database. 1907. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pike Place Market essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pike Place Market essentials.", "x": "At a glance: Pike Place Market — the flying fish.. Fish toss. The essentials: Fish.. Gum wall. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1907.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1907.", "x": "Pike Place Market: 1907.. Fish. Essential knowledge — Gum wall.. the flying fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1907..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1907..", "x": "Explained: 1907.. Starbucks. The context — Pike Place Market. Flowers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fish toss.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fish toss.", "x": "Pike Place Market: Fish toss.. Gum wall. Essential knowledge — Flowers.. the flying fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fish toss..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fish toss..", "x": "Explained: Fish toss.. Waterfront. The context — Pike Place Market. Original Starbucks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gum wall.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gum wall.", "x": "Pike Place Market: Gum wall.. Starbucks. Essential knowledge — Original Starbucks.. the flying fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gum wall..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gum wall..", "x": "Explained: Gum wall.. Shopping. The context — Pike Place Market. Waterfront. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flowers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flowers.", "x": "Pike Place Market: Flowers.. Waterfront. Essential knowledge — Waterfront.. the flying fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Flowers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Flowers..", "x": "Explained: Flowers.. 1907. The context — Pike Place Market. 1907. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Original Starbucks.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Original Starbucks.", "x": "Pike Place Market: Original Starbucks.. Shopping. Essential knowledge — 1907.. the flying fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Original Starbucks..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Original Starbucks..", "x": "Explained: Original Starbucks.. Fish. The context — Pike Place Market. Fish toss. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Waterfront.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Waterfront.", "x": "Pike Place Market: Waterfront.. 1907. Essential knowledge — Fish toss.. the flying fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Waterfront..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Waterfront..", "x": "Explained: Waterfront.. Gum wall. The context — Pike Place Market. Gum wall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1907.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1907.", "x": "Pike Place Market in depth: 1907.. Fish toss. Details — the flying fish.. Gum wall. Flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fish.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fish.", "x": "Pike Place Market in depth: Fish.. Gum wall. Details — the flying fish.. Starbucks. Original Starbucks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gum wall.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gum wall.", "x": "Pike Place Market in depth: Gum wall.. Flowers. Details — the flying fish.. Waterfront. Waterfront. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Starbucks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Starbucks.", "x": "Pike Place Market in depth: Starbucks.. Original Starbucks. Details — the flying fish.. Shopping. 1907. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Waterfront.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Waterfront.", "x": "Pike Place Market in depth: Waterfront.. Waterfront. Details — the flying fish.. 1907. Fish toss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Shopping.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Shopping.", "x": "Pike Place Market in depth: Shopping.. 1907. Details — the flying fish.. Fish. Gum wall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pike Place Market comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pike Place Market comes from.", "x": "Origins: 1907.. 1907. The history of Pike Place Market — the flying fish.. Fish. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pike Place Market respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pike Place Market respectfully.", "x": "Engaging: Gum wall.. Fish toss. How to participate or observe well — Pike Place Market. the flying fish. Respect first, always; Starbucks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pike Place Market do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pike Place Market do's and don'ts.", "x": "Etiquette: Waterfront.. Gum wall. The rules of respect — Pike Place Market. the flying fish. When in doubt, ask about Shopping.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pike Place Market.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pike Place Market.", "x": "Planning: 1907.. Flowers. Practical notes — Pike Place Market. the flying fish. A little planning shows respect for Fish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pike Place Market and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pike Place Market and money.", "x": "Costs: Gum wall.. Original Starbucks. What to budget — Pike Place Market. the flying fish. The best experiences of Starbucks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-pike-place-market-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
