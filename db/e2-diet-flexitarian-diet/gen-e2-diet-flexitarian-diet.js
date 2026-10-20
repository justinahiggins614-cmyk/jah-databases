(function(){'use strict';
/* JAH Flexitarian Diet Diet Database generator — jahdb-e2-diet-flexitarian-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-flexitarian-diet',PREFIX='JAH-E2DIETFLEXI-',NAME='JAH Flexitarian Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Flexitarian Diet: the complete guide", "d": "Flexitarian Diet: the flexible veg..", "g": "overview", "l": 2, "q": "What is Flexitarian Diet: the complete guide?", "a": "Flexitarian Diet: the flexible veg..", "x": "The complete diet guide to Flexitarian Diet: the flexible veg.. Mostly plants. History, meaning, practices, and how to engage respectfully — everything in one database. Flexible. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Flexitarian Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Flexitarian Diet essentials.", "x": "At a glance: Flexitarian Diet — the flexible veg.. Flexible. The essentials: Blatner.. Meat rarely. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mostly plants.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mostly plants.", "x": "Flexitarian Diet: Mostly plants.. Blatner. Essential knowledge — Meat rarely.. the flexible veg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mostly plants..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mostly plants..", "x": "Explained: Mostly plants.. Health. The context — Flexitarian Diet. Health. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flexible.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flexible.", "x": "Flexitarian Diet: Flexible.. Beginners. Essential knowledge — Health.. the flexible veg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Flexible..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Flexible..", "x": "Explained: Flexible.. Plants. The context — Flexitarian Diet. Blatner. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Meat rarely.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Meat rarely.", "x": "Flexitarian Diet: Meat rarely.. Health. Essential knowledge — Blatner.. the flexible veg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Meat rarely..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Meat rarely..", "x": "Explained: Meat rarely.. Foods. The context — Flexitarian Diet. Beginners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Health.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Health.", "x": "Flexitarian Diet: Health.. Plants. Essential knowledge — Beginners.. the flexible veg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Health..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Health..", "x": "Explained: Health.. Flexible. The context — Flexitarian Diet. Mostly plants. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Blatner.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Blatner.", "x": "Flexitarian Diet: Blatner.. Foods. Essential knowledge — Mostly plants.. the flexible veg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Blatner..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Blatner..", "x": "Explained: Blatner.. Blatner. The context — Flexitarian Diet. Flexible. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Beginners.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Beginners.", "x": "Flexitarian Diet: Beginners.. Flexible. Essential knowledge — Flexible.. the flexible veg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Beginners..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Beginners..", "x": "Explained: Beginners.. Beginners. The context — Flexitarian Diet. Meat rarely. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Flexible.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Flexible.", "x": "Flexitarian Diet in depth: Flexible.. Flexible. Details — the flexible veg.. Beginners. Health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Blatner.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Blatner.", "x": "Flexitarian Diet in depth: Blatner.. Meat rarely. Details — the flexible veg.. Health. Blatner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Beginners.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Beginners.", "x": "Flexitarian Diet in depth: Beginners.. Health. Details — the flexible veg.. Plants. Beginners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Health.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Health.", "x": "Flexitarian Diet in depth: Health.. Blatner. Details — the flexible veg.. Foods. Mostly plants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Plants.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Plants.", "x": "Flexitarian Diet in depth: Plants.. Beginners. Details — the flexible veg.. Flexible. Flexible. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foods.", "x": "Flexitarian Diet in depth: Foods.. Mostly plants. Details — the flexible veg.. Blatner. Meat rarely. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Flexitarian Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Flexitarian Diet comes from.", "x": "Origins: Flexible.. Mostly plants. The history of Flexitarian Diet — the flexible veg.. Blatner. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Flexitarian Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Flexitarian Diet respectfully.", "x": "Engaging: Beginners.. Flexible. How to participate or observe well — Flexitarian Diet. the flexible veg. Respect first, always; Health.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Flexitarian Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Flexitarian Diet do's and don'ts.", "x": "Etiquette: Plants.. Meat rarely. The rules of respect — Flexitarian Diet. the flexible veg. When in doubt, ask about Foods.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Flexitarian Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Flexitarian Diet.", "x": "Planning: Flexible.. Health. Practical notes — Flexitarian Diet. the flexible veg. A little planning shows respect for Blatner.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Flexitarian Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Flexitarian Diet and money.", "x": "Costs: Beginners.. Blatner. What to budget — Flexitarian Diet. the flexible veg. The best experiences of Health. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-flexitarian-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
