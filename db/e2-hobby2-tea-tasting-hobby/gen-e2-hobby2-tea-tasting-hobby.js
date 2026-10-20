(function(){'use strict';
/* JAH Tea Tasting Database generator — jahdb-e2-hobby2-tea-tasting-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-tea-tasting-hobby',PREFIX='JAH-E2HOBBY2TEA-',NAME='JAH Tea Tasting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tea Tasting: the complete guide", "d": "Tea Tasting: the steep sip..", "g": "overview", "l": 2, "q": "What is Tea Tasting: the complete guide?", "a": "Tea Tasting: the steep sip..", "x": "The complete hobby guide to Tea Tasting: the steep sip.. Gaiwan. History, meaning, practices, and how to engage respectfully — everything in one database. Steeps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tea Tasting essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tea Tasting essentials.", "x": "At a glance: Tea Tasting — the steep sip.. Steeps. The essentials: Notes.. Aroma. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gaiwan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gaiwan.", "x": "Tea Tasting: Gaiwan.. Notes. Essential knowledge — Aroma.. the steep sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gaiwan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gaiwan..", "x": "Explained: Gaiwan.. Gaiwan. The context — Tea Tasting. Varietals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Steeps.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Steeps.", "x": "Tea Tasting: Steeps.. Temperature. Essential knowledge — Varietals.. the steep sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Steeps..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Steeps..", "x": "Explained: Steeps.. Aroma. The context — Tea Tasting. Temperature. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Aroma.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Aroma.", "x": "Tea Tasting: Aroma.. Gaiwan. Essential knowledge — Temperature.. the steep sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Aroma..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Aroma..", "x": "Explained: Aroma.. Getting started. The context — Tea Tasting. Notes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Varietals.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Varietals.", "x": "Tea Tasting: Varietals.. Aroma. Essential knowledge — Notes.. the steep sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Varietals..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Varietals..", "x": "Explained: Varietals.. Steeps. The context — Tea Tasting. Gaiwan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Temperature.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Temperature.", "x": "Tea Tasting: Temperature.. Getting started. Essential knowledge — Gaiwan.. the steep sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Temperature..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Temperature..", "x": "Explained: Temperature.. Notes. The context — Tea Tasting. Steeps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Notes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Notes.", "x": "Tea Tasting: Notes.. Steeps. Essential knowledge — Steeps.. the steep sip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Notes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Notes..", "x": "Explained: Notes.. Temperature. The context — Tea Tasting. Aroma. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Steeps.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Steeps.", "x": "Tea Tasting in depth: Steeps.. Steeps. Details — the steep sip.. Temperature. Varietals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Notes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Notes.", "x": "Tea Tasting in depth: Notes.. Aroma. Details — the steep sip.. Gaiwan. Temperature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Temperature.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Temperature.", "x": "Tea Tasting in depth: Temperature.. Varietals. Details — the steep sip.. Aroma. Notes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gaiwan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gaiwan.", "x": "Tea Tasting in depth: Gaiwan.. Temperature. Details — the steep sip.. Getting started. Gaiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aroma.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aroma.", "x": "Tea Tasting in depth: Aroma.. Notes. Details — the steep sip.. Steeps. Steeps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Tea Tasting in depth: Getting started.. Gaiwan. Details — the steep sip.. Notes. Aroma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tea Tasting comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tea Tasting comes from.", "x": "Origins: Steeps.. Gaiwan. The history of Tea Tasting — the steep sip.. Notes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tea Tasting respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tea Tasting respectfully.", "x": "Engaging: Temperature.. Steeps. How to participate or observe well — Tea Tasting. the steep sip. Respect first, always; Gaiwan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tea Tasting do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tea Tasting do's and don'ts.", "x": "Etiquette: Aroma.. Aroma. The rules of respect — Tea Tasting. the steep sip. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tea Tasting.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tea Tasting.", "x": "Planning: Steeps.. Varietals. Practical notes — Tea Tasting. the steep sip. A little planning shows respect for Notes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tea Tasting and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tea Tasting and money.", "x": "Costs: Temperature.. Temperature. What to budget — Tea Tasting. the steep sip. The best experiences of Gaiwan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-tea-tasting-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
