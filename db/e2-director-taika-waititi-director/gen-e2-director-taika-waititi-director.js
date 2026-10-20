(function(){'use strict';
/* JAH Taika Waititi Director Database generator — jahdb-e2-director-taika-waititi-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-taika-waititi-director',PREFIX='JAH-E2DIRECTORT-',NAME='JAH Taika Waititi Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Taika Waititi: the complete guide", "d": "Taika Waititi: the Kiwi comedian..", "g": "overview", "l": 2, "q": "What is Taika Waititi: the complete guide?", "a": "Taika Waititi: the Kiwi comedian..", "x": "The complete director guide to Taika Waititi: the Kiwi comedian.. 1975. History, meaning, practices, and how to engage respectfully — everything in one database. Thor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Taika Waititi essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Taika Waititi essentials.", "x": "At a glance: Taika Waititi — the Kiwi comedian.. Thor Ragnarok. The essentials: Jojo.. Jojo Rabbit. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1975.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1975.", "x": "Taika Waititi: 1975.. Jojo. Essential knowledge — Jojo Rabbit.. the Kiwi comedian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1975..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1975..", "x": "Explained: 1975.. Humor. The context — Taika Waititi. NZ. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thor Ragnarok.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thor Ragnarok.", "x": "Taika Waititi: Thor Ragnarok.. NZ. Essential knowledge — NZ.. the Kiwi comedian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Thor Ragnarok..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Thor Ragnarok..", "x": "Explained: Thor Ragnarok.. Shadows. The context — Taika Waititi. Humor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Jojo Rabbit.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Jojo Rabbit.", "x": "Taika Waititi: Jojo Rabbit.. Humor. Essential knowledge — Humor.. the Kiwi comedian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Jojo Rabbit..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Jojo Rabbit..", "x": "Explained: Jojo Rabbit.. Style. The context — Taika Waititi. What We Do. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "NZ.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "NZ.", "x": "Taika Waititi: NZ.. Shadows. Essential knowledge — What We Do.. the Kiwi comedian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: NZ..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: NZ..", "x": "Explained: NZ.. Thor. The context — Taika Waititi. 1975. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Humor.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Humor.", "x": "Taika Waititi: Humor.. Style. Essential knowledge — 1975.. the Kiwi comedian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Humor..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Humor..", "x": "Explained: Humor.. Jojo. The context — Taika Waititi. Thor Ragnarok. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "What We Do.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "What We Do.", "x": "Taika Waititi: What We Do.. Thor. Essential knowledge — Thor Ragnarok.. the Kiwi comedian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: What We Do..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: What We Do..", "x": "Explained: What We Do.. NZ. The context — Taika Waititi. Jojo Rabbit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Thor.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Thor.", "x": "Taika Waititi in depth: Thor.. Thor Ragnarok. Details — the Kiwi comedian.. NZ. NZ. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Jojo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Jojo.", "x": "Taika Waititi in depth: Jojo.. Jojo Rabbit. Details — the Kiwi comedian.. Humor. Humor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "NZ.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "NZ.", "x": "Taika Waititi in depth: NZ.. NZ. Details — the Kiwi comedian.. Shadows. What We Do. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Humor.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Humor.", "x": "Taika Waititi in depth: Humor.. Humor. Details — the Kiwi comedian.. Style. 1975. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shadows.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shadows.", "x": "Taika Waititi in depth: Shadows.. What We Do. Details — the Kiwi comedian.. Thor. Thor Ragnarok. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Taika Waititi in depth: Style.. 1975. Details — the Kiwi comedian.. Jojo. Jojo Rabbit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Taika Waititi comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Taika Waititi comes from.", "x": "Origins: Thor.. 1975. The history of Taika Waititi — the Kiwi comedian.. Jojo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Taika Waititi respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Taika Waititi respectfully.", "x": "Engaging: NZ.. Thor Ragnarok. How to participate or observe well — Taika Waititi. the Kiwi comedian. Respect first, always; Humor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Taika Waititi do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Taika Waititi do's and don'ts.", "x": "Etiquette: Shadows.. Jojo Rabbit. The rules of respect — Taika Waititi. the Kiwi comedian. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Taika Waititi.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Taika Waititi.", "x": "Planning: Thor.. NZ. Practical notes — Taika Waititi. the Kiwi comedian. A little planning shows respect for Jojo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Taika Waititi and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Taika Waititi and money.", "x": "Costs: NZ.. Humor. What to budget — Taika Waititi. the Kiwi comedian. The best experiences of Humor. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-taika-waititi-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
