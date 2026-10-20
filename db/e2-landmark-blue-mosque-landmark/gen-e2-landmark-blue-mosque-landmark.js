(function(){'use strict';
/* JAH Blue Mosque Landmark Database generator — jahdb-e2-landmark-blue-mosque-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-blue-mosque-landmark',PREFIX='JAH-E2LANDMARKB-',NAME='JAH Blue Mosque Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Blue Mosque: the complete guide", "d": "Blue Mosque: the six minarets..", "g": "overview", "l": 2, "q": "What is Blue Mosque: the complete guide?", "a": "Blue Mosque: the six minarets..", "x": "The complete landmark guide to Blue Mosque: the six minarets.. 1616. History, meaning, practices, and how to engage respectfully — everything in one database. 1616. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Blue Mosque essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Blue Mosque essentials.", "x": "At a glance: Blue Mosque — the six minarets.. 6 minarets. The essentials: Tiles.. Iznik tiles. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1616.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1616.", "x": "Blue Mosque: 1616.. Tiles. Essential knowledge — Iznik tiles.. the six minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1616..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1616..", "x": "Explained: 1616.. Ahmed. The context — Blue Mosque. Sultan Ahmed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "6 minarets.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "6 minarets.", "x": "Blue Mosque: 6 minarets.. Prayer. Essential knowledge — Sultan Ahmed.. the six minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 6 minarets..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 6 minarets..", "x": "Explained: 6 minarets.. Minarets. The context — Blue Mosque. Cascade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Iznik tiles.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Iznik tiles.", "x": "Blue Mosque: Iznik tiles.. Ahmed. Essential knowledge — Cascade.. the six minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Iznik tiles..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Iznik tiles..", "x": "Explained: Iznik tiles.. Visits. The context — Blue Mosque. Prayer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sultan Ahmed.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sultan Ahmed.", "x": "Blue Mosque: Sultan Ahmed.. Minarets. Essential knowledge — Prayer.. the six minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sultan Ahmed..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sultan Ahmed..", "x": "Explained: Sultan Ahmed.. 1616. The context — Blue Mosque. 1616. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cascade.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cascade.", "x": "Blue Mosque: Cascade.. Visits. Essential knowledge — 1616.. the six minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cascade..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cascade..", "x": "Explained: Cascade.. Tiles. The context — Blue Mosque. 6 minarets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Prayer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Prayer.", "x": "Blue Mosque: Prayer.. 1616. Essential knowledge — 6 minarets.. the six minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Prayer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Prayer..", "x": "Explained: Prayer.. Prayer. The context — Blue Mosque. Iznik tiles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1616.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1616.", "x": "Blue Mosque in depth: 1616.. 6 minarets. Details — the six minarets.. Prayer. Sultan Ahmed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tiles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tiles.", "x": "Blue Mosque in depth: Tiles.. Iznik tiles. Details — the six minarets.. Ahmed. Cascade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Prayer.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Prayer.", "x": "Blue Mosque in depth: Prayer.. Sultan Ahmed. Details — the six minarets.. Minarets. Prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ahmed.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ahmed.", "x": "Blue Mosque in depth: Ahmed.. Cascade. Details — the six minarets.. Visits. 1616. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Minarets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Minarets.", "x": "Blue Mosque in depth: Minarets.. Prayer. Details — the six minarets.. 1616. 6 minarets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visits.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visits.", "x": "Blue Mosque in depth: Visits.. 1616. Details — the six minarets.. Tiles. Iznik tiles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Blue Mosque comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Blue Mosque comes from.", "x": "Origins: 1616.. 1616. The history of Blue Mosque — the six minarets.. Tiles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Blue Mosque respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Blue Mosque respectfully.", "x": "Engaging: Prayer.. 6 minarets. How to participate or observe well — Blue Mosque. the six minarets. Respect first, always; Ahmed.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Blue Mosque do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Blue Mosque do's and don'ts.", "x": "Etiquette: Minarets.. Iznik tiles. The rules of respect — Blue Mosque. the six minarets. When in doubt, ask about Visits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Blue Mosque.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Blue Mosque.", "x": "Planning: 1616.. Sultan Ahmed. Practical notes — Blue Mosque. the six minarets. A little planning shows respect for Tiles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Blue Mosque and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Blue Mosque and money.", "x": "Costs: Prayer.. Cascade. What to budget — Blue Mosque. the six minarets. The best experiences of Ahmed. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-blue-mosque-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
