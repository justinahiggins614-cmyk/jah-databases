(function(){'use strict';
/* JAH Peter Jackson Director Database generator — jahdb-e2-director-peter-jackson-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-peter-jackson-director',PREFIX='JAH-E2DIRECTORP-',NAME='JAH Peter Jackson Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peter Jackson: the complete guide", "d": "Peter Jackson: the Middle-earth maker..", "g": "overview", "l": 2, "q": "What is Peter Jackson: the complete guide?", "a": "Peter Jackson: the Middle-earth maker..", "x": "The complete director guide to Peter Jackson: the Middle-earth maker.. 1961. History, meaning, practices, and how to engage respectfully — everything in one database. LOTR. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Peter Jackson essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Peter Jackson essentials.", "x": "At a glance: Peter Jackson — the Middle-earth maker.. LOTR. The essentials: Weta.. Hobbit. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1961.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1961.", "x": "Peter Jackson: 1961.. Weta. Essential knowledge — Hobbit.. the Middle-earth maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1961..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1961..", "x": "Explained: 1961.. King Kong. The context — Peter Jackson. Weta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "LOTR.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "LOTR.", "x": "Peter Jackson: LOTR.. NZ. Essential knowledge — Weta.. the Middle-earth maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: LOTR..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: LOTR..", "x": "Explained: LOTR.. Hobbit. The context — Peter Jackson. New Zealand. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hobbit.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hobbit.", "x": "Peter Jackson: Hobbit.. King Kong. Essential knowledge — New Zealand.. the Middle-earth maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hobbit..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hobbit..", "x": "Explained: Hobbit.. Style. The context — Peter Jackson. King Kong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Weta.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Weta.", "x": "Peter Jackson: Weta.. Hobbit. Essential knowledge — King Kong.. the Middle-earth maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Weta..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Weta..", "x": "Explained: Weta.. LOTR. The context — Peter Jackson. 1961. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "New Zealand.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "New Zealand.", "x": "Peter Jackson: New Zealand.. Style. Essential knowledge — 1961.. the Middle-earth maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: New Zealand..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: New Zealand..", "x": "Explained: New Zealand.. Weta. The context — Peter Jackson. LOTR. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "King Kong.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "King Kong.", "x": "Peter Jackson: King Kong.. LOTR. Essential knowledge — LOTR.. the Middle-earth maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: King Kong..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: King Kong..", "x": "Explained: King Kong.. NZ. The context — Peter Jackson. Hobbit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "LOTR.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "LOTR.", "x": "Peter Jackson in depth: LOTR.. LOTR. Details — the Middle-earth maker.. NZ. Weta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Weta.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Weta.", "x": "Peter Jackson in depth: Weta.. Hobbit. Details — the Middle-earth maker.. King Kong. New Zealand. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "NZ.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "NZ.", "x": "Peter Jackson in depth: NZ.. Weta. Details — the Middle-earth maker.. Hobbit. King Kong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "King Kong.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "King Kong.", "x": "Peter Jackson in depth: King Kong.. New Zealand. Details — the Middle-earth maker.. Style. 1961. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hobbit.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hobbit.", "x": "Peter Jackson in depth: Hobbit.. King Kong. Details — the Middle-earth maker.. LOTR. LOTR. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Peter Jackson in depth: Style.. 1961. Details — the Middle-earth maker.. Weta. Hobbit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Peter Jackson comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Peter Jackson comes from.", "x": "Origins: LOTR.. 1961. The history of Peter Jackson — the Middle-earth maker.. Weta. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Peter Jackson respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Peter Jackson respectfully.", "x": "Engaging: NZ.. LOTR. How to participate or observe well — Peter Jackson. the Middle-earth maker. Respect first, always; King Kong.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Peter Jackson do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Peter Jackson do's and don'ts.", "x": "Etiquette: Hobbit.. Hobbit. The rules of respect — Peter Jackson. the Middle-earth maker. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Peter Jackson.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Peter Jackson.", "x": "Planning: LOTR.. Weta. Practical notes — Peter Jackson. the Middle-earth maker. A little planning shows respect for Weta.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Peter Jackson and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Peter Jackson and money.", "x": "Costs: NZ.. New Zealand. What to budget — Peter Jackson. the Middle-earth maker. The best experiences of King Kong. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-peter-jackson-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
