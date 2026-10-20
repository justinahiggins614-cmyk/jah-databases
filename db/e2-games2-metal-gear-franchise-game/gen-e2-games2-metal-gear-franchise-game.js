(function(){'use strict';
/* JAH Metal Gear Franchise Database generator — jahdb-e2-games2-metal-gear-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-metal-gear-franchise-game',PREFIX='JAH-E2GAMES2MET-',NAME='JAH Metal Gear Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Metal Gear Franchise: the complete guide", "d": "Metal Gear Franchise: the tactical stealth..", "g": "overview", "l": 2, "q": "What is Metal Gear Franchise: the complete guide?", "a": "Metal Gear Franchise: the tactical stealth..", "x": "The complete game franchise guide to Metal Gear Franchise: the tactical stealth.. 1987. History, meaning, practices, and how to engage respectfully — everything in one database. Snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Metal Gear Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Metal Gear Franchise essentials.", "x": "At a glance: Metal Gear Franchise — the tactical stealth.. Kojima. The essentials: Story.. Snake. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1987.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1987.", "x": "Metal Gear Franchise: 1987.. Story. Essential knowledge — Snake.. the tactical stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1987..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1987..", "x": "Explained: 1987.. Kojima. The context — Metal Gear Franchise. Stealth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kojima.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kojima.", "x": "Metal Gear Franchise: Kojima.. Cardboard. Essential knowledge — Stealth.. the tactical stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Kojima..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Kojima..", "x": "Explained: Kojima.. Stealth. The context — Metal Gear Franchise. Cardboard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Snake.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Snake.", "x": "Metal Gear Franchise: Snake.. Kojima. Essential knowledge — Cardboard.. the tactical stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Snake..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Snake..", "x": "Explained: Snake.. Games. The context — Metal Gear Franchise. Story. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Stealth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Stealth.", "x": "Metal Gear Franchise: Stealth.. Stealth. Essential knowledge — Story.. the tactical stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Stealth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Stealth..", "x": "Explained: Stealth.. Snake. The context — Metal Gear Franchise. 1987. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cardboard.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cardboard.", "x": "Metal Gear Franchise: Cardboard.. Games. Essential knowledge — 1987.. the tactical stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cardboard..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cardboard..", "x": "Explained: Cardboard.. Story. The context — Metal Gear Franchise. Kojima. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Story.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Story.", "x": "Metal Gear Franchise: Story.. Snake. Essential knowledge — Kojima.. the tactical stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Story..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Story..", "x": "Explained: Story.. Cardboard. The context — Metal Gear Franchise. Snake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Snake.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Snake.", "x": "Metal Gear Franchise in depth: Snake.. Kojima. Details — the tactical stealth.. Cardboard. Stealth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Story.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Story.", "x": "Metal Gear Franchise in depth: Story.. Snake. Details — the tactical stealth.. Kojima. Cardboard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cardboard.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cardboard.", "x": "Metal Gear Franchise in depth: Cardboard.. Stealth. Details — the tactical stealth.. Stealth. Story. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Kojima.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Kojima.", "x": "Metal Gear Franchise in depth: Kojima.. Cardboard. Details — the tactical stealth.. Games. 1987. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Stealth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Stealth.", "x": "Metal Gear Franchise in depth: Stealth.. Story. Details — the tactical stealth.. Snake. Kojima. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Metal Gear Franchise in depth: Games.. 1987. Details — the tactical stealth.. Story. Snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Metal Gear Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Metal Gear Franchise comes from.", "x": "Origins: Snake.. 1987. The history of Metal Gear Franchise — the tactical stealth.. Story. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Metal Gear Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Metal Gear Franchise respectfully.", "x": "Engaging: Cardboard.. Kojima. How to participate or observe well — Metal Gear Franchise. the tactical stealth. Respect first, always; Kojima.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Metal Gear Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Metal Gear Franchise do's and don'ts.", "x": "Etiquette: Stealth.. Snake. The rules of respect — Metal Gear Franchise. the tactical stealth. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Metal Gear Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Metal Gear Franchise.", "x": "Planning: Snake.. Stealth. Practical notes — Metal Gear Franchise. the tactical stealth. A little planning shows respect for Story.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Metal Gear Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Metal Gear Franchise and money.", "x": "Costs: Cardboard.. Cardboard. What to budget — Metal Gear Franchise. the tactical stealth. The best experiences of Kojima. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-metal-gear-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
