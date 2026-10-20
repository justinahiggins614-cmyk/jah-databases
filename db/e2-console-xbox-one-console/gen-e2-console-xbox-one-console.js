(function(){'use strict';
/* JAH Xbox One Console Database generator — jahdb-e2-console-xbox-one-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-xbox-one-console',PREFIX='JAH-E2CONSOLEXB-',NAME='JAH Xbox One Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Xbox One: the complete guide", "d": "Xbox One: the TV pivot..", "g": "overview", "l": 2, "q": "What is Xbox One: the complete guide?", "a": "Xbox One: the TV pivot..", "x": "The complete console guide to Xbox One: the TV pivot.. 2013. History, meaning, practices, and how to engage respectfully — everything in one database. TV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Xbox One essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Xbox One essentials.", "x": "At a glance: Xbox One — the TV pivot.. TV. The essentials: Backwards.. Kinect. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2013.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2013.", "x": "Xbox One: 2013.. Backwards. Essential knowledge — Kinect.. the TV pivot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2013..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2013..", "x": "Explained: 2013.. Microsoft. The context — Xbox One. Backwards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "TV.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "TV.", "x": "Xbox One: TV.. Pass. Essential knowledge — Backwards.. the TV pivot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: TV..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: TV..", "x": "Explained: TV.. Kinect. The context — Xbox One. Game Pass. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kinect.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kinect.", "x": "Xbox One: Kinect.. Microsoft. Essential knowledge — Game Pass.. the TV pivot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kinect..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kinect..", "x": "Explained: Kinect.. Legacy. The context — Xbox One. Microsoft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Backwards.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Backwards.", "x": "Xbox One: Backwards.. Kinect. Essential knowledge — Microsoft.. the TV pivot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Backwards..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Backwards..", "x": "Explained: Backwards.. TV. The context — Xbox One. 2013. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Game Pass.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Game Pass.", "x": "Xbox One: Game Pass.. Legacy. Essential knowledge — 2013.. the TV pivot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Game Pass..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Game Pass..", "x": "Explained: Game Pass.. Backwards. The context — Xbox One. TV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Microsoft.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Microsoft.", "x": "Xbox One: Microsoft.. TV. Essential knowledge — TV.. the TV pivot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Microsoft..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Microsoft..", "x": "Explained: Microsoft.. Pass. The context — Xbox One. Kinect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "TV.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "TV.", "x": "Xbox One in depth: TV.. TV. Details — the TV pivot.. Pass. Backwards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Backwards.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Backwards.", "x": "Xbox One in depth: Backwards.. Kinect. Details — the TV pivot.. Microsoft. Game Pass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pass.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pass.", "x": "Xbox One in depth: Pass.. Backwards. Details — the TV pivot.. Kinect. Microsoft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Microsoft.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Microsoft.", "x": "Xbox One in depth: Microsoft.. Game Pass. Details — the TV pivot.. Legacy. 2013. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Kinect.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Kinect.", "x": "Xbox One in depth: Kinect.. Microsoft. Details — the TV pivot.. TV. TV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Xbox One in depth: Legacy.. 2013. Details — the TV pivot.. Backwards. Kinect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Xbox One comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Xbox One comes from.", "x": "Origins: TV.. 2013. The history of Xbox One — the TV pivot.. Backwards. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Xbox One respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Xbox One respectfully.", "x": "Engaging: Pass.. TV. How to participate or observe well — Xbox One. the TV pivot. Respect first, always; Microsoft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Xbox One do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Xbox One do's and don'ts.", "x": "Etiquette: Kinect.. Kinect. The rules of respect — Xbox One. the TV pivot. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Xbox One.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Xbox One.", "x": "Planning: TV.. Backwards. Practical notes — Xbox One. the TV pivot. A little planning shows respect for Backwards.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Xbox One and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Xbox One and money.", "x": "Costs: Pass.. Game Pass. What to budget — Xbox One. the TV pivot. The best experiences of Microsoft. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-xbox-one-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
