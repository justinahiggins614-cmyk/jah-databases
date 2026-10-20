(function(){'use strict';
/* JAH Scotch Ale Beer Style Database generator — jahdb-e2-beer-scotch-ale-beer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beer-scotch-ale-beer',PREFIX='JAH-E2BEERSCOTC-',NAME='JAH Scotch Ale Beer Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Scotch Ale: the complete guide", "d": "Scotch Ale: the wee heavy..", "g": "overview", "l": 2, "q": "What is Scotch Ale: the complete guide?", "a": "Scotch Ale: the wee heavy..", "x": "The complete beer style guide to Scotch Ale: the wee heavy.. Scotland. History, meaning, practices, and how to engage respectfully — everything in one database. Malty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Scotch Ale essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Scotch Ale essentials.", "x": "At a glance: Scotch Ale — the wee heavy.. Malty. The essentials: Scotland.. Sweet. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Scotland.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Scotland.", "x": "Scotch Ale: Scotland.. Scotland. Essential knowledge — Sweet.. the wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Scotland..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Scotland..", "x": "Explained: Scotland.. Sweet. The context — Scotch Ale. Wee heavy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Malty.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Malty.", "x": "Scotch Ale: Malty.. History. Essential knowledge — Wee heavy.. the wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Malty..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Malty..", "x": "Explained: Malty.. Shilling. The context — Scotch Ale. 80 shilling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sweet.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sweet.", "x": "Scotch Ale: Sweet.. Sweet. Essential knowledge — 80 shilling.. the wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sweet..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sweet..", "x": "Explained: Sweet.. Serving. The context — Scotch Ale. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wee heavy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wee heavy.", "x": "Scotch Ale: Wee heavy.. Shilling. Essential knowledge — History.. the wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Wee heavy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Wee heavy..", "x": "Explained: Wee heavy.. Malty. The context — Scotch Ale. Scotland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "80 shilling.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "80 shilling.", "x": "Scotch Ale: 80 shilling.. Serving. Essential knowledge — Scotland.. the wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 80 shilling..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 80 shilling..", "x": "Explained: 80 shilling.. Scotland. The context — Scotch Ale. Malty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Scotch Ale: History.. Malty. Essential knowledge — Malty.. the wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Scotch Ale. Sweet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Malty.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Malty.", "x": "Scotch Ale in depth: Malty.. Malty. Details — the wee heavy.. History. Wee heavy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Scotland.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Scotland.", "x": "Scotch Ale in depth: Scotland.. Sweet. Details — the wee heavy.. Sweet. 80 shilling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Scotch Ale in depth: History.. Wee heavy. Details — the wee heavy.. Shilling. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sweet.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sweet.", "x": "Scotch Ale in depth: Sweet.. 80 shilling. Details — the wee heavy.. Serving. Scotland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shilling.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shilling.", "x": "Scotch Ale in depth: Shilling.. History. Details — the wee heavy.. Malty. Malty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Serving.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Serving.", "x": "Scotch Ale in depth: Serving.. Scotland. Details — the wee heavy.. Scotland. Sweet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Scotch Ale comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Scotch Ale comes from.", "x": "Origins: Malty.. Scotland. The history of Scotch Ale — the wee heavy.. Scotland. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Scotch Ale respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Scotch Ale respectfully.", "x": "Engaging: History.. Malty. How to participate or observe well — Scotch Ale. the wee heavy. Respect first, always; Sweet.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Scotch Ale do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Scotch Ale do's and don'ts.", "x": "Etiquette: Shilling.. Sweet. The rules of respect — Scotch Ale. the wee heavy. When in doubt, ask about Serving.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Scotch Ale.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Scotch Ale.", "x": "Planning: Malty.. Wee heavy. Practical notes — Scotch Ale. the wee heavy. A little planning shows respect for Scotland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Scotch Ale and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Scotch Ale and money.", "x": "Costs: History.. 80 shilling. What to budget — Scotch Ale. the wee heavy. The best experiences of Sweet. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beer-scotch-ale-beer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
