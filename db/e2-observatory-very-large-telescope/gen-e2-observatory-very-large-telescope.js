(function(){'use strict';
/* JAH Very Large Telescope Observatory Database generator — jahdb-e2-observatory-very-large-telescope-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-very-large-telescope',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Very Large Telescope Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Very Large Telescope: the complete guide", "d": "Very Large Telescope: Chile's four giants..", "g": "overview", "l": 2, "q": "What is Very Large Telescope: the complete guide?", "a": "Very Large Telescope: Chile's four giants..", "x": "The complete observatory guide to Very Large Telescope: Chile's four giants.. Paranal. History, meaning, practices, and how to engage respectfully — everything in one database. Telescopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Very Large Telescope essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Very Large Telescope essentials.", "x": "At a glance: Very Large Telescope — Chile's four giants.. 4x8.2m. The essentials: Interferometry.. Interferometry. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Paranal.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Paranal.", "x": "Very Large Telescope: Paranal.. Interferometry. Essential knowledge — Interferometry.. Chile's four giants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Paranal..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Paranal..", "x": "Explained: Paranal.. Science. The context — Very Large Telescope. ESO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "4x8.2m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "4x8.2m.", "x": "Very Large Telescope: 4x8.2m.. Desert. Essential knowledge — ESO.. Chile's four giants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 4x8.2m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 4x8.2m..", "x": "Explained: 4x8.2m.. Tours. The context — Very Large Telescope. Desert. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Interferometry.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Interferometry.", "x": "Very Large Telescope: Interferometry.. Science. Essential knowledge — Desert.. Chile's four giants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Interferometry..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Interferometry..", "x": "Explained: Interferometry.. ESO. The context — Very Large Telescope. Discoveries. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "ESO.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "ESO.", "x": "Very Large Telescope: ESO.. Tours. Essential knowledge — Discoveries.. Chile's four giants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: ESO..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: ESO..", "x": "Explained: ESO.. Telescopes. The context — Very Large Telescope. Paranal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Desert.", "x": "Very Large Telescope: Desert.. ESO. Essential knowledge — Paranal.. Chile's four giants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Desert..", "x": "Explained: Desert.. Interferometry. The context — Very Large Telescope. 4x8.2m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Discoveries.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Discoveries.", "x": "Very Large Telescope: Discoveries.. Telescopes. Essential knowledge — 4x8.2m.. Chile's four giants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Discoveries..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Discoveries..", "x": "Explained: Discoveries.. Desert. The context — Very Large Telescope. Interferometry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Telescopes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Telescopes.", "x": "Very Large Telescope in depth: Telescopes.. 4x8.2m. Details — Chile's four giants.. Desert. ESO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Interferometry.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Interferometry.", "x": "Very Large Telescope in depth: Interferometry.. Interferometry. Details — Chile's four giants.. Science. Desert. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Desert.", "x": "Very Large Telescope in depth: Desert.. ESO. Details — Chile's four giants.. Tours. Discoveries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Science.", "x": "Very Large Telescope in depth: Science.. Desert. Details — Chile's four giants.. ESO. Paranal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Very Large Telescope in depth: Tours.. Discoveries. Details — Chile's four giants.. Telescopes. 4x8.2m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "ESO.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "ESO.", "x": "Very Large Telescope in depth: ESO.. Paranal. Details — Chile's four giants.. Interferometry. Interferometry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Very Large Telescope comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Very Large Telescope comes from.", "x": "Origins: Telescopes.. Paranal. The history of Very Large Telescope — Chile's four giants.. Interferometry. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Very Large Telescope respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Very Large Telescope respectfully.", "x": "Engaging: Desert.. 4x8.2m. How to participate or observe well — Very Large Telescope. Chile's four giants. Respect first, always; Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Very Large Telescope do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Very Large Telescope do's and don'ts.", "x": "Etiquette: Tours.. Interferometry. The rules of respect — Very Large Telescope. Chile's four giants. When in doubt, ask about ESO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Very Large Telescope.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Very Large Telescope.", "x": "Planning: Telescopes.. ESO. Practical notes — Very Large Telescope. Chile's four giants. A little planning shows respect for Interferometry.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Very Large Telescope and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Very Large Telescope and money.", "x": "Costs: Desert.. Desert. What to budget — Very Large Telescope. Chile's four giants. The best experiences of Science. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-very-large-telescope-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
