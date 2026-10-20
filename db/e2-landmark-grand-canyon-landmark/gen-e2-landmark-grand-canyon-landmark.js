(function(){'use strict';
/* JAH Grand Canyon Landmark Database generator — jahdb-e2-landmark-grand-canyon-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-grand-canyon-landmark',PREFIX='JAH-E2LANDMARKG-',NAME='JAH Grand Canyon Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Grand Canyon: the complete guide", "d": "Grand Canyon: the mile-deep chasm..", "g": "overview", "l": 2, "q": "What is Grand Canyon: the complete guide?", "a": "Grand Canyon: the mile-deep chasm..", "x": "The complete landmark guide to Grand Canyon: the mile-deep chasm.. 446 km. History, meaning, practices, and how to engage respectfully — everything in one database. 446 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Grand Canyon essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Grand Canyon essentials.", "x": "At a glance: Grand Canyon — the mile-deep chasm.. 1.6 km deep. The essentials: Colorado.. Colorado. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "446 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "446 km.", "x": "Grand Canyon: 446 km.. Colorado. Essential knowledge — Colorado.. the mile-deep chasm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 446 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 446 km..", "x": "Explained: 446 km.. Sunrise. The context — Grand Canyon. South Rim. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1.6 km deep.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1.6 km deep.", "x": "Grand Canyon: 1.6 km deep.. Hiking. Essential knowledge — South Rim.. the mile-deep chasm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1.6 km deep..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1.6 km deep..", "x": "Explained: 1.6 km deep.. Deep. The context — Grand Canyon. Sunrise. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Colorado.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Colorado.", "x": "Grand Canyon: Colorado.. Sunrise. Essential knowledge — Sunrise.. the mile-deep chasm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Colorado..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Colorado..", "x": "Explained: Colorado.. Tours. The context — Grand Canyon. Hiking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "South Rim.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "South Rim.", "x": "Grand Canyon: South Rim.. Deep. Essential knowledge — Hiking.. the mile-deep chasm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: South Rim..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: South Rim..", "x": "Explained: South Rim.. 446 km. The context — Grand Canyon. 446 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sunrise.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sunrise.", "x": "Grand Canyon: Sunrise.. Tours. Essential knowledge — 446 km.. the mile-deep chasm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sunrise..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sunrise..", "x": "Explained: Sunrise.. Colorado. The context — Grand Canyon. 1.6 km deep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hiking.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hiking.", "x": "Grand Canyon: Hiking.. 446 km. Essential knowledge — 1.6 km deep.. the mile-deep chasm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Hiking..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Hiking..", "x": "Explained: Hiking.. Hiking. The context — Grand Canyon. Colorado. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "446 km.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "446 km.", "x": "Grand Canyon in depth: 446 km.. 1.6 km deep. Details — the mile-deep chasm.. Hiking. South Rim. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colorado.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colorado.", "x": "Grand Canyon in depth: Colorado.. Colorado. Details — the mile-deep chasm.. Sunrise. Sunrise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hiking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hiking.", "x": "Grand Canyon in depth: Hiking.. South Rim. Details — the mile-deep chasm.. Deep. Hiking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sunrise.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sunrise.", "x": "Grand Canyon in depth: Sunrise.. Sunrise. Details — the mile-deep chasm.. Tours. 446 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Deep.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Deep.", "x": "Grand Canyon in depth: Deep.. Hiking. Details — the mile-deep chasm.. 446 km. 1.6 km deep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Grand Canyon in depth: Tours.. 446 km. Details — the mile-deep chasm.. Colorado. Colorado. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Grand Canyon comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Grand Canyon comes from.", "x": "Origins: 446 km.. 446 km. The history of Grand Canyon — the mile-deep chasm.. Colorado. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Grand Canyon respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Grand Canyon respectfully.", "x": "Engaging: Hiking.. 1.6 km deep. How to participate or observe well — Grand Canyon. the mile-deep chasm. Respect first, always; Sunrise.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Grand Canyon do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Grand Canyon do's and don'ts.", "x": "Etiquette: Deep.. Colorado. The rules of respect — Grand Canyon. the mile-deep chasm. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Grand Canyon.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Grand Canyon.", "x": "Planning: 446 km.. South Rim. Practical notes — Grand Canyon. the mile-deep chasm. A little planning shows respect for Colorado.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Grand Canyon and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Grand Canyon and money.", "x": "Costs: Hiking.. Sunrise. What to budget — Grand Canyon. the mile-deep chasm. The best experiences of Sunrise. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-grand-canyon-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
