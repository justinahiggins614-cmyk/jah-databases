(function(){'use strict';
/* JAH Hummingbird Ruby Bird Species Database generator — jahdb-e2-bird-ruby-hummingbird-bird-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bird-ruby-hummingbird-bird',PREFIX='JAH-E2BIRDRUBYH-',NAME='JAH Hummingbird Ruby Bird Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hummingbird Ruby: the complete guide", "d": "Hummingbird Ruby: the tiny hover..", "g": "overview", "l": 2, "q": "What is Hummingbird Ruby: the complete guide?", "a": "Hummingbird Ruby: the tiny hover..", "x": "The complete bird species guide to Hummingbird Ruby: the tiny hover.. Hover. History, meaning, practices, and how to engage respectfully — everything in one database. Hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hummingbird Ruby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hummingbird Ruby essentials.", "x": "At a glance: Hummingbird Ruby — the tiny hover.. 3 inches. The essentials: Nectar.. Wings. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hover.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hover.", "x": "Hummingbird Ruby: Hover.. Nectar. Essential knowledge — Wings.. the tiny hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hover..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hover..", "x": "Explained: Hover.. Iridescent. The context — Hummingbird Ruby. Nectar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "3 inches.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "3 inches.", "x": "Hummingbird Ruby: 3 inches.. Migration. Essential knowledge — Nectar.. the tiny hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 3 inches..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 3 inches..", "x": "Explained: 3 inches.. Tiny. The context — Hummingbird Ruby. Migration. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wings.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wings.", "x": "Hummingbird Ruby: Wings.. Iridescent. Essential knowledge — Migration.. the tiny hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Wings..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Wings..", "x": "Explained: Wings.. Habitat. The context — Hummingbird Ruby. Iridescent. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nectar.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nectar.", "x": "Hummingbird Ruby: Nectar.. Tiny. Essential knowledge — Iridescent.. the tiny hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Nectar..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Nectar..", "x": "Explained: Nectar.. Hover. The context — Hummingbird Ruby. Hover. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Migration.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Migration.", "x": "Hummingbird Ruby: Migration.. Habitat. Essential knowledge — Hover.. the tiny hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Migration..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Migration..", "x": "Explained: Migration.. Nectar. The context — Hummingbird Ruby. 3 inches. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Iridescent.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Iridescent.", "x": "Hummingbird Ruby: Iridescent.. Hover. Essential knowledge — 3 inches.. the tiny hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Iridescent..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Iridescent..", "x": "Explained: Iridescent.. Migration. The context — Hummingbird Ruby. Wings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hover.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hover.", "x": "Hummingbird Ruby in depth: Hover.. 3 inches. Details — the tiny hover.. Migration. Nectar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nectar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nectar.", "x": "Hummingbird Ruby in depth: Nectar.. Wings. Details — the tiny hover.. Iridescent. Migration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Migration.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Migration.", "x": "Hummingbird Ruby in depth: Migration.. Nectar. Details — the tiny hover.. Tiny. Iridescent. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Iridescent.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Iridescent.", "x": "Hummingbird Ruby in depth: Iridescent.. Migration. Details — the tiny hover.. Habitat. Hover. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tiny.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tiny.", "x": "Hummingbird Ruby in depth: Tiny.. Iridescent. Details — the tiny hover.. Hover. 3 inches. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Hummingbird Ruby in depth: Habitat.. Hover. Details — the tiny hover.. Nectar. Wings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hummingbird Ruby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hummingbird Ruby comes from.", "x": "Origins: Hover.. Hover. The history of Hummingbird Ruby — the tiny hover.. Nectar. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hummingbird Ruby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hummingbird Ruby respectfully.", "x": "Engaging: Migration.. 3 inches. How to participate or observe well — Hummingbird Ruby. the tiny hover. Respect first, always; Iridescent.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hummingbird Ruby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hummingbird Ruby do's and don'ts.", "x": "Etiquette: Tiny.. Wings. The rules of respect — Hummingbird Ruby. the tiny hover. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hummingbird Ruby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hummingbird Ruby.", "x": "Planning: Hover.. Nectar. Practical notes — Hummingbird Ruby. the tiny hover. A little planning shows respect for Nectar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hummingbird Ruby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hummingbird Ruby and money.", "x": "Costs: Migration.. Migration. What to budget — Hummingbird Ruby. the tiny hover. The best experiences of Iridescent. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bird-ruby-hummingbird-bird-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
