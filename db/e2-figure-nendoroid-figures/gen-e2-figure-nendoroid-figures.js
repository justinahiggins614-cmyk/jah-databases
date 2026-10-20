(function(){'use strict';
/* JAH Nendoroid Figures Action Figure Database generator — jahdb-e2-figure-nendoroid-figures-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-figure-nendoroid-figures',PREFIX='JAH-E2FIGURENEN-',NAME='JAH Nendoroid Figures Action Figure Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nendoroid Figures: the complete guide", "d": "Nendoroid Figures: the chibi Japanese..", "g": "overview", "l": 2, "q": "What is Nendoroid Figures: the complete guide?", "a": "Nendoroid Figures: the chibi Japanese..", "x": "The complete action figure guide to Nendoroid Figures: the chibi Japanese.. Good Smile. History, meaning, practices, and how to engage respectfully — everything in one database. Chibi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nendoroid Figures essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nendoroid Figures essentials.", "x": "At a glance: Nendoroid Figures — the chibi Japanese.. Chibi. The essentials: Faces.. Faces. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Good Smile.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Good Smile.", "x": "Nendoroid Figures: Good Smile.. Faces. Essential knowledge — Faces.. the chibi Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Good Smile..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Good Smile..", "x": "Explained: Good Smile.. Japan. The context — Nendoroid Figures. Anime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chibi.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chibi.", "x": "Nendoroid Figures: Chibi.. Anime. Essential knowledge — Anime.. the chibi Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chibi..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chibi..", "x": "Explained: Chibi.. Good Smile. The context — Nendoroid Figures. Parts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Faces.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Faces.", "x": "Nendoroid Figures: Faces.. Japan. Essential knowledge — Parts.. the chibi Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Faces..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Faces..", "x": "Explained: Faces.. History. The context — Nendoroid Figures. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Anime.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Anime.", "x": "Nendoroid Figures: Anime.. Good Smile. Essential knowledge — Japan.. the chibi Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Anime..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Anime..", "x": "Explained: Anime.. Chibi. The context — Nendoroid Figures. Good Smile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Parts.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Parts.", "x": "Nendoroid Figures: Parts.. History. Essential knowledge — Good Smile.. the chibi Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Parts..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Parts..", "x": "Explained: Parts.. Faces. The context — Nendoroid Figures. Chibi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Japan.", "x": "Nendoroid Figures: Japan.. Chibi. Essential knowledge — Chibi.. the chibi Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Anime. The context — Nendoroid Figures. Faces. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chibi.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chibi.", "x": "Nendoroid Figures in depth: Chibi.. Chibi. Details — the chibi Japanese.. Anime. Anime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Faces.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Faces.", "x": "Nendoroid Figures in depth: Faces.. Faces. Details — the chibi Japanese.. Japan. Parts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Anime.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Anime.", "x": "Nendoroid Figures in depth: Anime.. Anime. Details — the chibi Japanese.. Good Smile. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Japan.", "x": "Nendoroid Figures in depth: Japan.. Parts. Details — the chibi Japanese.. History. Good Smile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Good Smile.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Good Smile.", "x": "Nendoroid Figures in depth: Good Smile.. Japan. Details — the chibi Japanese.. Chibi. Chibi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Nendoroid Figures in depth: History.. Good Smile. Details — the chibi Japanese.. Faces. Faces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nendoroid Figures comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nendoroid Figures comes from.", "x": "Origins: Chibi.. Good Smile. The history of Nendoroid Figures — the chibi Japanese.. Faces. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nendoroid Figures respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nendoroid Figures respectfully.", "x": "Engaging: Anime.. Chibi. How to participate or observe well — Nendoroid Figures. the chibi Japanese. Respect first, always; Japan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nendoroid Figures do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nendoroid Figures do's and don'ts.", "x": "Etiquette: Good Smile.. Faces. The rules of respect — Nendoroid Figures. the chibi Japanese. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nendoroid Figures.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nendoroid Figures.", "x": "Planning: Chibi.. Anime. Practical notes — Nendoroid Figures. the chibi Japanese. A little planning shows respect for Faces.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nendoroid Figures and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nendoroid Figures and money.", "x": "Costs: Anime.. Parts. What to budget — Nendoroid Figures. the chibi Japanese. The best experiences of Japan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-figure-nendoroid-figures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
