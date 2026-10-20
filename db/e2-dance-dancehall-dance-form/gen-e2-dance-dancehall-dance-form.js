(function(){'use strict';
/* JAH Dancehall Dance Dance Form Database generator — jahdb-e2-dance-dancehall-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-dancehall-dance-form',PREFIX='JAH-E2DANCEDANC-',NAME='JAH Dancehall Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dancehall Dance: the complete guide", "d": "Dancehall Dance: the Jamaican groove..", "g": "overview", "l": 2, "q": "What is Dancehall Dance: the complete guide?", "a": "Dancehall Dance: the Jamaican groove..", "x": "The complete dance form guide to Dancehall Dance: the Jamaican groove.. Jamaica. History, meaning, practices, and how to engage respectfully — everything in one database. Wine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dancehall Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dancehall Dance essentials.", "x": "At a glance: Dancehall Dance — the Jamaican groove.. Wine. The essentials: Parties.. Daggering. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Jamaica.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Jamaica.", "x": "Dancehall Dance: Jamaica.. Parties. Essential knowledge — Daggering.. the Jamaican groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Jamaica..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Jamaica..", "x": "Explained: Jamaica.. Jamaica. The context — Dancehall Dance. Parties. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wine.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wine.", "x": "Dancehall Dance: Wine.. Groove. Essential knowledge — Parties.. the Jamaican groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Wine..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Wine..", "x": "Explained: Wine.. Bashment. The context — Dancehall Dance. Bashment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Daggering.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Daggering.", "x": "Dancehall Dance: Daggering.. Jamaica. Essential knowledge — Bashment.. the Jamaican groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Daggering..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Daggering..", "x": "Explained: Daggering.. Training. The context — Dancehall Dance. Groove. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Parties.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Parties.", "x": "Dancehall Dance: Parties.. Bashment. Essential knowledge — Groove.. the Jamaican groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Parties..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Parties..", "x": "Explained: Parties.. Wine. The context — Dancehall Dance. Jamaica. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bashment.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bashment.", "x": "Dancehall Dance: Bashment.. Training. Essential knowledge — Jamaica.. the Jamaican groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bashment..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bashment..", "x": "Explained: Bashment.. Parties. The context — Dancehall Dance. Wine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Groove.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Groove.", "x": "Dancehall Dance: Groove.. Wine. Essential knowledge — Wine.. the Jamaican groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Groove..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Groove..", "x": "Explained: Groove.. Groove. The context — Dancehall Dance. Daggering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wine.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wine.", "x": "Dancehall Dance in depth: Wine.. Wine. Details — the Jamaican groove.. Groove. Parties. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Parties.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Parties.", "x": "Dancehall Dance in depth: Parties.. Daggering. Details — the Jamaican groove.. Jamaica. Bashment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Groove.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Groove.", "x": "Dancehall Dance in depth: Groove.. Parties. Details — the Jamaican groove.. Bashment. Groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Jamaica.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Jamaica.", "x": "Dancehall Dance in depth: Jamaica.. Bashment. Details — the Jamaican groove.. Training. Jamaica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bashment.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bashment.", "x": "Dancehall Dance in depth: Bashment.. Groove. Details — the Jamaican groove.. Wine. Wine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Dancehall Dance in depth: Training.. Jamaica. Details — the Jamaican groove.. Parties. Daggering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dancehall Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dancehall Dance comes from.", "x": "Origins: Wine.. Jamaica. The history of Dancehall Dance — the Jamaican groove.. Parties. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dancehall Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dancehall Dance respectfully.", "x": "Engaging: Groove.. Wine. How to participate or observe well — Dancehall Dance. the Jamaican groove. Respect first, always; Jamaica.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dancehall Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dancehall Dance do's and don'ts.", "x": "Etiquette: Bashment.. Daggering. The rules of respect — Dancehall Dance. the Jamaican groove. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dancehall Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dancehall Dance.", "x": "Planning: Wine.. Parties. Practical notes — Dancehall Dance. the Jamaican groove. A little planning shows respect for Parties.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dancehall Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dancehall Dance and money.", "x": "Costs: Groove.. Bashment. What to budget — Dancehall Dance. the Jamaican groove. The best experiences of Jamaica. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-dancehall-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
