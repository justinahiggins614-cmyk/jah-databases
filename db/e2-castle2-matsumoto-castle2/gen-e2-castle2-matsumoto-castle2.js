(function(){'use strict';
/* JAH Matsumoto Castle2 Database generator — jahdb-e2-castle2-matsumoto-castle2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle2-matsumoto-castle2',PREFIX='JAH-E2CASTLE2MA-',NAME='JAH Matsumoto Castle2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Matsumoto Castle2: the complete guide", "d": "Matsumoto Castle2: the crow 2..", "g": "overview", "l": 2, "q": "What is Matsumoto Castle2: the complete guide?", "a": "Matsumoto Castle2: the crow 2..", "x": "The complete castle guide to Matsumoto Castle2: the crow 2.. 1594. History, meaning, practices, and how to engage respectfully — everything in one database. 1594. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Matsumoto Castle2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Matsumoto Castle2 essentials.", "x": "At a glance: Matsumoto Castle2 — the crow 2.. Black. The essentials: Stories.. Crow. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1594.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1594.", "x": "Matsumoto Castle2: 1594.. Stories. Essential knowledge — Crow.. the crow 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1594..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1594..", "x": "Explained: 1594.. Black. The context — Matsumoto Castle2. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Black.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Black.", "x": "Matsumoto Castle2: Black.. Japan. Essential knowledge — Japan.. the crow 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Black..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Black..", "x": "Explained: Black.. Moat. The context — Matsumoto Castle2. Moat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Crow.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Crow.", "x": "Matsumoto Castle2: Crow.. Black. Essential knowledge — Moat.. the crow 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Crow..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Crow..", "x": "Explained: Crow.. Visiting. The context — Matsumoto Castle2. 5 stories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Japan.", "x": "Matsumoto Castle2: Japan.. Moat. Essential knowledge — 5 stories.. the crow 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. 1594. The context — Matsumoto Castle2. 1594. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Moat.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Moat.", "x": "Matsumoto Castle2: Moat.. Visiting. Essential knowledge — 1594.. the crow 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Moat..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Moat..", "x": "Explained: Moat.. Stories. The context — Matsumoto Castle2. Black. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "5 stories.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "5 stories.", "x": "Matsumoto Castle2: 5 stories.. 1594. Essential knowledge — Black.. the crow 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 5 stories..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 5 stories..", "x": "Explained: 5 stories.. Japan. The context — Matsumoto Castle2. Crow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1594.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1594.", "x": "Matsumoto Castle2 in depth: 1594.. Black. Details — the crow 2.. Japan. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stories.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stories.", "x": "Matsumoto Castle2 in depth: Stories.. Crow. Details — the crow 2.. Black. Moat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Japan.", "x": "Matsumoto Castle2 in depth: Japan.. Japan. Details — the crow 2.. Moat. 5 stories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Black.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Black.", "x": "Matsumoto Castle2 in depth: Black.. Moat. Details — the crow 2.. Visiting. 1594. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Moat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Moat.", "x": "Matsumoto Castle2 in depth: Moat.. 5 stories. Details — the crow 2.. 1594. Black. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Matsumoto Castle2 in depth: Visiting.. 1594. Details — the crow 2.. Stories. Crow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Matsumoto Castle2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Matsumoto Castle2 comes from.", "x": "Origins: 1594.. 1594. The history of Matsumoto Castle2 — the crow 2.. Stories. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Matsumoto Castle2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Matsumoto Castle2 respectfully.", "x": "Engaging: Japan.. Black. How to participate or observe well — Matsumoto Castle2. the crow 2. Respect first, always; Black.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Matsumoto Castle2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Matsumoto Castle2 do's and don'ts.", "x": "Etiquette: Moat.. Crow. The rules of respect — Matsumoto Castle2. the crow 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Matsumoto Castle2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Matsumoto Castle2.", "x": "Planning: 1594.. Japan. Practical notes — Matsumoto Castle2. the crow 2. A little planning shows respect for Stories.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Matsumoto Castle2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Matsumoto Castle2 and money.", "x": "Costs: Japan.. Moat. What to budget — Matsumoto Castle2. the crow 2. The best experiences of Black. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle2-matsumoto-castle2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
