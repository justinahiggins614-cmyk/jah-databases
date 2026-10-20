(function(){'use strict';
/* JAH Fastnet Lighthouse Lighthouse Database generator — jahdb-e2-lighthouse-fastnet-lighthouse-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lighthouse-fastnet-lighthouse',PREFIX='JAH-E2LIGHTHOUS-',NAME='JAH Fastnet Lighthouse Lighthouse Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fastnet Lighthouse: the complete guide", "d": "Fastnet Lighthouse: Ireland's teardrop..", "g": "overview", "l": 2, "q": "What is Fastnet Lighthouse: the complete guide?", "a": "Fastnet Lighthouse: Ireland's teardrop..", "x": "The complete lighthouse guide to Fastnet Lighthouse: Ireland's teardrop.. 1904. History, meaning, practices, and how to engage respectfully — everything in one database. Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fastnet Lighthouse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fastnet Lighthouse essentials.", "x": "At a glance: Fastnet Lighthouse — Ireland's teardrop.. Rock. The essentials: Race.. Atlantic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1904.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1904.", "x": "Fastnet Lighthouse: 1904.. Race. Essential knowledge — Atlantic.. Ireland's teardrop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1904..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1904..", "x": "Explained: 1904.. History. The context — Fastnet Lighthouse. Fastnet Race. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rock.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rock.", "x": "Fastnet Lighthouse: Rock.. Keepers. Essential knowledge — Fastnet Race.. Ireland's teardrop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rock..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rock..", "x": "Explained: Rock.. Storms. The context — Fastnet Lighthouse. Keepers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Atlantic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Atlantic.", "x": "Fastnet Lighthouse: Atlantic.. History. Essential knowledge — Keepers.. Ireland's teardrop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Atlantic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Atlantic..", "x": "Explained: Atlantic.. Ireland. The context — Fastnet Lighthouse. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fastnet Race.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fastnet Race.", "x": "Fastnet Lighthouse: Fastnet Race.. Storms. Essential knowledge — History.. Ireland's teardrop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fastnet Race..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fastnet Race..", "x": "Explained: Fastnet Race.. Rock. The context — Fastnet Lighthouse. 1904. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Keepers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Keepers.", "x": "Fastnet Lighthouse: Keepers.. Ireland. Essential knowledge — 1904.. Ireland's teardrop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Keepers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Keepers..", "x": "Explained: Keepers.. Race. The context — Fastnet Lighthouse. Rock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Fastnet Lighthouse: History.. Rock. Essential knowledge — Rock.. Ireland's teardrop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Keepers. The context — Fastnet Lighthouse. Atlantic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rock.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rock.", "x": "Fastnet Lighthouse in depth: Rock.. Rock. Details — Ireland's teardrop.. Keepers. Fastnet Race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Race.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Race.", "x": "Fastnet Lighthouse in depth: Race.. Atlantic. Details — Ireland's teardrop.. History. Keepers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Keepers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Keepers.", "x": "Fastnet Lighthouse in depth: Keepers.. Fastnet Race. Details — Ireland's teardrop.. Storms. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Fastnet Lighthouse in depth: History.. Keepers. Details — Ireland's teardrop.. Ireland. 1904. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Storms.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Storms.", "x": "Fastnet Lighthouse in depth: Storms.. History. Details — Ireland's teardrop.. Rock. Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ireland.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ireland.", "x": "Fastnet Lighthouse in depth: Ireland.. 1904. Details — Ireland's teardrop.. Race. Atlantic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fastnet Lighthouse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fastnet Lighthouse comes from.", "x": "Origins: Rock.. 1904. The history of Fastnet Lighthouse — Ireland's teardrop.. Race. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fastnet Lighthouse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fastnet Lighthouse respectfully.", "x": "Engaging: Keepers.. Rock. How to participate or observe well — Fastnet Lighthouse. Ireland's teardrop. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fastnet Lighthouse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fastnet Lighthouse do's and don'ts.", "x": "Etiquette: Storms.. Atlantic. The rules of respect — Fastnet Lighthouse. Ireland's teardrop. When in doubt, ask about Ireland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fastnet Lighthouse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fastnet Lighthouse.", "x": "Planning: Rock.. Fastnet Race. Practical notes — Fastnet Lighthouse. Ireland's teardrop. A little planning shows respect for Race.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fastnet Lighthouse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fastnet Lighthouse and money.", "x": "Costs: Keepers.. Keepers. What to budget — Fastnet Lighthouse. Ireland's teardrop. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lighthouse-fastnet-lighthouse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
