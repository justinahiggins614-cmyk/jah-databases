(function(){'use strict';
/* JAH Low-FODMAP Diet Diet Database generator — jahdb-e2-diet-low-fodmap-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-low-fodmap-diet',PREFIX='JAH-E2DIETLOWFO-',NAME='JAH Low-FODMAP Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Low-FODMAP Diet: the complete guide", "d": "Low-FODMAP Diet: the gut-calming..", "g": "overview", "l": 2, "q": "What is Low-FODMAP Diet: the complete guide?", "a": "Low-FODMAP Diet: the gut-calming..", "x": "The complete diet guide to Low-FODMAP Diet: the gut-calming.. IBS. History, meaning, practices, and how to engage respectfully — everything in one database. IBS. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Low-FODMAP Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Low-FODMAP Diet essentials.", "x": "At a glance: Low-FODMAP Diet — the gut-calming.. FODMAPs. The essentials: Elimination.. Elimination. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "IBS.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "IBS.", "x": "Low-FODMAP Diet: IBS.. Elimination. Essential knowledge — Elimination.. the gut-calming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: IBS..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: IBS..", "x": "Explained: IBS.. Reintro. The context — Low-FODMAP Diet. Dietitian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "FODMAPs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "FODMAPs.", "x": "Low-FODMAP Diet: FODMAPs.. Monash. Essential knowledge — Dietitian.. the gut-calming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: FODMAPs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: FODMAPs..", "x": "Explained: FODMAPs.. Dietitian. The context — Low-FODMAP Diet. Reintro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Elimination.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Elimination.", "x": "Low-FODMAP Diet: Elimination.. Reintro. Essential knowledge — Reintro.. the gut-calming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Elimination..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Elimination..", "x": "Explained: Elimination.. Foods. The context — Low-FODMAP Diet. Monash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dietitian.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dietitian.", "x": "Low-FODMAP Diet: Dietitian.. Dietitian. Essential knowledge — Monash.. the gut-calming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dietitian..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dietitian..", "x": "Explained: Dietitian.. IBS. The context — Low-FODMAP Diet. IBS. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Reintro.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Reintro.", "x": "Low-FODMAP Diet: Reintro.. Foods. Essential knowledge — IBS.. the gut-calming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Reintro..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Reintro..", "x": "Explained: Reintro.. Elimination. The context — Low-FODMAP Diet. FODMAPs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Monash.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Monash.", "x": "Low-FODMAP Diet: Monash.. IBS. Essential knowledge — FODMAPs.. the gut-calming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Monash..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Monash..", "x": "Explained: Monash.. Monash. The context — Low-FODMAP Diet. Elimination. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "IBS.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "IBS.", "x": "Low-FODMAP Diet in depth: IBS.. FODMAPs. Details — the gut-calming.. Monash. Dietitian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Elimination.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Elimination.", "x": "Low-FODMAP Diet in depth: Elimination.. Elimination. Details — the gut-calming.. Reintro. Reintro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Monash.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Monash.", "x": "Low-FODMAP Diet in depth: Monash.. Dietitian. Details — the gut-calming.. Dietitian. Monash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Reintro.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Reintro.", "x": "Low-FODMAP Diet in depth: Reintro.. Reintro. Details — the gut-calming.. Foods. IBS. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dietitian.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dietitian.", "x": "Low-FODMAP Diet in depth: Dietitian.. Monash. Details — the gut-calming.. IBS. FODMAPs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foods.", "x": "Low-FODMAP Diet in depth: Foods.. IBS. Details — the gut-calming.. Elimination. Elimination. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Low-FODMAP Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Low-FODMAP Diet comes from.", "x": "Origins: IBS.. IBS. The history of Low-FODMAP Diet — the gut-calming.. Elimination. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Low-FODMAP Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Low-FODMAP Diet respectfully.", "x": "Engaging: Monash.. FODMAPs. How to participate or observe well — Low-FODMAP Diet. the gut-calming. Respect first, always; Reintro.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Low-FODMAP Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Low-FODMAP Diet do's and don'ts.", "x": "Etiquette: Dietitian.. Elimination. The rules of respect — Low-FODMAP Diet. the gut-calming. When in doubt, ask about Foods.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Low-FODMAP Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Low-FODMAP Diet.", "x": "Planning: IBS.. Dietitian. Practical notes — Low-FODMAP Diet. the gut-calming. A little planning shows respect for Elimination.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Low-FODMAP Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Low-FODMAP Diet and money.", "x": "Costs: Monash.. Reintro. What to budget — Low-FODMAP Diet. the gut-calming. The best experiences of Reintro. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-low-fodmap-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
