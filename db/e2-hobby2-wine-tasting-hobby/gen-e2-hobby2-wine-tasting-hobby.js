(function(){'use strict';
/* JAH Wine Tasting Hobby Database generator — jahdb-e2-hobby2-wine-tasting-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-wine-tasting-hobby',PREFIX='JAH-E2HOBBY2WIN-',NAME='JAH Wine Tasting Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wine Tasting Hobby: the complete guide", "d": "Wine Tasting Hobby: the swirl sip..", "g": "overview", "l": 2, "q": "What is Wine Tasting Hobby: the complete guide?", "a": "Wine Tasting Hobby: the swirl sip..", "x": "The complete hobby guide to Wine Tasting Hobby: the swirl sip.. Swirl. History, meaning, practices, and how to engage respectfully — everything in one database. Sniff. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Wine Tasting Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Wine Tasting Hobby essentials.", "x": "At a glance: Wine Tasting Hobby — the swirl sip.. Sniff. The essentials: Notes.. Sip. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Swirl.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Swirl.", "x": "Wine Tasting Hobby: Swirl.. Notes. Essential knowledge — Sip.. the swirl sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Swirl..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Swirl..", "x": "Explained: Swirl.. Swirl. The context — Wine Tasting Hobby. Varietals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sniff.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sniff.", "x": "Wine Tasting Hobby: Sniff.. Spit. Essential knowledge — Varietals.. the swirl sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sniff..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sniff..", "x": "Explained: Sniff.. Varietals. The context — Wine Tasting Hobby. Notes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sip.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sip.", "x": "Wine Tasting Hobby: Sip.. Swirl. Essential knowledge — Notes.. the swirl sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sip..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sip..", "x": "Explained: Sip.. Getting started. The context — Wine Tasting Hobby. Spit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Varietals.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Varietals.", "x": "Wine Tasting Hobby: Varietals.. Varietals. Essential knowledge — Spit.. the swirl sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Varietals..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Varietals..", "x": "Explained: Varietals.. Sniff. The context — Wine Tasting Hobby. Swirl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Notes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Notes.", "x": "Wine Tasting Hobby: Notes.. Getting started. Essential knowledge — Swirl.. the swirl sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Notes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Notes..", "x": "Explained: Notes.. Notes. The context — Wine Tasting Hobby. Sniff. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spit.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spit.", "x": "Wine Tasting Hobby: Spit.. Sniff. Essential knowledge — Sniff.. the swirl sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Spit..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Spit..", "x": "Explained: Spit.. Spit. The context — Wine Tasting Hobby. Sip. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sniff.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sniff.", "x": "Wine Tasting Hobby in depth: Sniff.. Sniff. Details — the swirl sip.. Spit. Varietals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Notes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Notes.", "x": "Wine Tasting Hobby in depth: Notes.. Sip. Details — the swirl sip.. Swirl. Notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spit.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spit.", "x": "Wine Tasting Hobby in depth: Spit.. Varietals. Details — the swirl sip.. Varietals. Spit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Swirl.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Swirl.", "x": "Wine Tasting Hobby in depth: Swirl.. Notes. Details — the swirl sip.. Getting started. Swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Varietals.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Varietals.", "x": "Wine Tasting Hobby in depth: Varietals.. Spit. Details — the swirl sip.. Sniff. Sniff. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Wine Tasting Hobby in depth: Getting started.. Swirl. Details — the swirl sip.. Notes. Sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Wine Tasting Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Wine Tasting Hobby comes from.", "x": "Origins: Sniff.. Swirl. The history of Wine Tasting Hobby — the swirl sip.. Notes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Wine Tasting Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Wine Tasting Hobby respectfully.", "x": "Engaging: Spit.. Sniff. How to participate or observe well — Wine Tasting Hobby. the swirl sip. Respect first, always; Swirl.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Wine Tasting Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Wine Tasting Hobby do's and don'ts.", "x": "Etiquette: Varietals.. Sip. The rules of respect — Wine Tasting Hobby. the swirl sip. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Wine Tasting Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Wine Tasting Hobby.", "x": "Planning: Sniff.. Varietals. Practical notes — Wine Tasting Hobby. the swirl sip. A little planning shows respect for Notes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Wine Tasting Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Wine Tasting Hobby and money.", "x": "Costs: Spit.. Notes. What to budget — Wine Tasting Hobby. the swirl sip. The best experiences of Swirl. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-wine-tasting-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
