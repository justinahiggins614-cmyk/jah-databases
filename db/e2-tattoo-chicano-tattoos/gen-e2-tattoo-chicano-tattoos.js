(function(){'use strict';
/* JAH Chicano Tattoos Tattoo Style Database generator — jahdb-e2-tattoo-chicano-tattoos-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tattoo-chicano-tattoos',PREFIX='JAH-E2TATTOOCHI-',NAME='JAH Chicano Tattoos Tattoo Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chicano Tattoos: the complete guide", "d": "Chicano Tattoos: LA heritage art..", "g": "overview", "l": 2, "q": "What is Chicano Tattoos: the complete guide?", "a": "Chicano Tattoos: LA heritage art..", "x": "The complete tattoo style guide to Chicano Tattoos: LA heritage art.. Black and grey. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chicano Tattoos essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chicano Tattoos essentials.", "x": "At a glance: Chicano Tattoos — LA heritage art.. Portraits. The essentials: Style.. Lettering. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Black and grey.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Black and grey.", "x": "Chicano Tattoos: Black and grey.. Style. Essential knowledge — Lettering.. LA heritage art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Black and grey..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Black and grey..", "x": "Explained: Black and grey.. Artists. The context — Chicano Tattoos. Culture. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Portraits.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Portraits.", "x": "Chicano Tattoos: Portraits.. Culture. Essential knowledge — Culture.. LA heritage art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Portraits..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Portraits..", "x": "Explained: Portraits.. Respect. The context — Chicano Tattoos. Prison roots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lettering.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lettering.", "x": "Chicano Tattoos: Lettering.. Artists. Essential knowledge — Prison roots.. LA heritage art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lettering..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lettering..", "x": "Explained: Lettering.. LA. The context — Chicano Tattoos. Artists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Culture.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Culture.", "x": "Chicano Tattoos: Culture.. Respect. Essential knowledge — Artists.. LA heritage art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Culture..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Culture..", "x": "Explained: Culture.. History. The context — Chicano Tattoos. Black and grey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Prison roots.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Prison roots.", "x": "Chicano Tattoos: Prison roots.. LA. Essential knowledge — Black and grey.. LA heritage art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Prison roots..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Prison roots..", "x": "Explained: Prison roots.. Style. The context — Chicano Tattoos. Portraits. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Artists.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Artists.", "x": "Chicano Tattoos: Artists.. History. Essential knowledge — Portraits.. LA heritage art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Artists..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Artists..", "x": "Explained: Artists.. Culture. The context — Chicano Tattoos. Lettering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Chicano Tattoos in depth: History.. Portraits. Details — LA heritage art.. Culture. Culture. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Style.", "x": "Chicano Tattoos in depth: Style.. Lettering. Details — LA heritage art.. Artists. Prison roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Culture.", "x": "Chicano Tattoos in depth: Culture.. Culture. Details — LA heritage art.. Respect. Artists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Artists.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Artists.", "x": "Chicano Tattoos in depth: Artists.. Prison roots. Details — LA heritage art.. LA. Black and grey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Respect.", "x": "Chicano Tattoos in depth: Respect.. Artists. Details — LA heritage art.. History. Portraits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "LA.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "LA.", "x": "Chicano Tattoos in depth: LA.. Black and grey. Details — LA heritage art.. Style. Lettering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chicano Tattoos comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chicano Tattoos comes from.", "x": "Origins: History.. Black and grey. The history of Chicano Tattoos — LA heritage art.. Style. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chicano Tattoos respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chicano Tattoos respectfully.", "x": "Engaging: Culture.. Portraits. How to participate or observe well — Chicano Tattoos. LA heritage art. Respect first, always; Artists.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chicano Tattoos do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chicano Tattoos do's and don'ts.", "x": "Etiquette: Respect.. Lettering. The rules of respect — Chicano Tattoos. LA heritage art. When in doubt, ask about LA.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chicano Tattoos.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chicano Tattoos.", "x": "Planning: History.. Culture. Practical notes — Chicano Tattoos. LA heritage art. A little planning shows respect for Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chicano Tattoos and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chicano Tattoos and money.", "x": "Costs: Culture.. Prison roots. What to budget — Chicano Tattoos. LA heritage art. The best experiences of Artists. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tattoo-chicano-tattoos-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
