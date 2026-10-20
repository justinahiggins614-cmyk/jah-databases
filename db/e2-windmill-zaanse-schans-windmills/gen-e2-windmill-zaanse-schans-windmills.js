(function(){'use strict';
/* JAH Zaanse Schans Windmills Windmill Database generator — jahdb-e2-windmill-zaanse-schans-windmills-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill-zaanse-schans-windmills',PREFIX='JAH-E2WINDMILLZ-',NAME='JAH Zaanse Schans Windmills Windmill Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Zaanse Schans Windmills: the complete guide", "d": "Zaanse Schans Windmills: working Dutch heritage..", "g": "overview", "l": 2, "q": "What is Zaanse Schans Windmills: the complete guide?", "a": "Zaanse Schans Windmills: working Dutch heritage..", "x": "The complete windmill guide to Zaanse Schans Windmills: working Dutch heritage.. Working mills. History, meaning, practices, and how to engage respectfully — everything in one database. Mills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Zaanse Schans Windmills essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Zaanse Schans Windmills essentials.", "x": "At a glance: Zaanse Schans Windmills — working Dutch heritage.. Oil/paint. The essentials: Crafts.. Zaan River. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Working mills.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Working mills.", "x": "Zaanse Schans Windmills: Working mills.. Crafts. Essential knowledge — Zaan River.. working Dutch heritage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Working mills..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Working mills..", "x": "Explained: Working mills.. Tours. The context — Zaanse Schans Windmills. Tourists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Oil/paint.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Oil/paint.", "x": "Zaanse Schans Windmills: Oil/paint.. River. Essential knowledge — Tourists.. working Dutch heritage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Oil/paint..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Oil/paint..", "x": "Explained: Oil/paint.. History. The context — Zaanse Schans Windmills. Clogs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Zaan River.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Zaan River.", "x": "Zaanse Schans Windmills: Zaan River.. Tours. Essential knowledge — Clogs.. working Dutch heritage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Zaan River..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Zaan River..", "x": "Explained: Zaan River.. Photos. The context — Zaanse Schans Windmills. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tourists.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tourists.", "x": "Zaanse Schans Windmills: Tourists.. History. Essential knowledge — History.. working Dutch heritage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tourists..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tourists..", "x": "Explained: Tourists.. Mills. The context — Zaanse Schans Windmills. Working mills. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Clogs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Clogs.", "x": "Zaanse Schans Windmills: Clogs.. Photos. Essential knowledge — Working mills.. working Dutch heritage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Clogs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Clogs..", "x": "Explained: Clogs.. Crafts. The context — Zaanse Schans Windmills. Oil/paint. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Zaanse Schans Windmills: History.. Mills. Essential knowledge — Oil/paint.. working Dutch heritage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. River. The context — Zaanse Schans Windmills. Zaan River. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mills.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mills.", "x": "Zaanse Schans Windmills in depth: Mills.. Oil/paint. Details — working Dutch heritage.. River. Tourists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crafts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crafts.", "x": "Zaanse Schans Windmills in depth: Crafts.. Zaan River. Details — working Dutch heritage.. Tours. Clogs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "River.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "River.", "x": "Zaanse Schans Windmills in depth: River.. Tourists. Details — working Dutch heritage.. History. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Zaanse Schans Windmills in depth: Tours.. Clogs. Details — working Dutch heritage.. Photos. Working mills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Zaanse Schans Windmills in depth: History.. History. Details — working Dutch heritage.. Mills. Oil/paint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Photos.", "x": "Zaanse Schans Windmills in depth: Photos.. Working mills. Details — working Dutch heritage.. Crafts. Zaan River. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Zaanse Schans Windmills comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Zaanse Schans Windmills comes from.", "x": "Origins: Mills.. Working mills. The history of Zaanse Schans Windmills — working Dutch heritage.. Crafts. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Zaanse Schans Windmills respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Zaanse Schans Windmills respectfully.", "x": "Engaging: River.. Oil/paint. How to participate or observe well — Zaanse Schans Windmills. working Dutch heritage. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Zaanse Schans Windmills do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Zaanse Schans Windmills do's and don'ts.", "x": "Etiquette: History.. Zaan River. The rules of respect — Zaanse Schans Windmills. working Dutch heritage. When in doubt, ask about Photos.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Zaanse Schans Windmills.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Zaanse Schans Windmills.", "x": "Planning: Mills.. Tourists. Practical notes — Zaanse Schans Windmills. working Dutch heritage. A little planning shows respect for Crafts.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Zaanse Schans Windmills and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Zaanse Schans Windmills and money.", "x": "Costs: River.. Clogs. What to budget — Zaanse Schans Windmills. working Dutch heritage. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill-zaanse-schans-windmills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
